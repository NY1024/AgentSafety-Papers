<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-23759-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-17 18:31 ｜ **论文总数 / Total Papers**: 23759（近 30 天 / Recent 30 days: 2891）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 23759 篇论文（含摘要、分类筛选、搜索）/ View all 23759 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 580
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 488
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 116
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 414
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 558
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3832
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 55
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 891
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 115
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2687
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2402
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2224
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2227
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 288
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 87
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 57
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 281
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6361

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 2891 篇，完整 23759 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 2891 papers from the last 30 days (with date, authors & abstract). For the full list of 23759 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 9 papers

- **2026-08-14** — Wei Zhao, Zhe Li, Peixin Zhang et al. — [Tripwire: Triggering Aligned Refusal via Statistically Certified Safety Neurons](http://arxiv.org/abs/2608.14392v1)
  <details><summary>📄 Abstract</summary>
  Neuron- and path-level interventions offer the finest-grained route to defending large language models (LLMs) against jailbreak attacks, yet existing methods fall short of this promise, i.e., they often compromise model utility significantly. Specifically, one line of work suppresses toxic neurons to erase harmful semantics, but since such semantics are distributed across the network, blocking every pathway forces a large intervention footprint. An alternative line of research focus on identify ...
  </details>

- **2026-08-13** — Julian Minder, Viktor Moskvoretskii, Raghav Singhal et al. — [Synthetic Persona Pretraining: Alignment from Token Zero](http://arxiv.org/abs/2608.13482v1)
  <details><summary>📄 Abstract</summary>
  As language-model-based AI is increasingly deployed in autonomous settings, aligning its goals and values with those of humans becomes critical. Today, alignment, and the assistant identity itself, are typically introduced only after pretraining, once behavioral priors are already established. This can make values a thin overlay, rather than deeply rooted, and facilitate subsequent misalignment. Pursuing a different paradigm, we introduce Synthetic Persona Pretraining (SPP), which installs the d...
  </details>

- **2026-08-13** — Fangzhou Chen, Shiji Zhao, Mengyang Wang et al. — [HiRoute: Hierarchical Routed Prompt Tuning for Safety Alignment of Large Language Models](http://arxiv.org/abs/2608.12821v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) remain vulnerable to harmful requests and jailbreak attacks. Parameter-efficient safety alignment methods based on prompt tuning typically rely on a single global prompt or externally selected prompt modules. Such static designs struggle to maintain a cross-category safety boundary while generating constructive responses tailored to specific risks and avoiding over-refusal of benign inputs. To address these limitations, we propose HiRoute, an input-adaptive hierarchi...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 2 papers

- **2026-08-12** — Van Tran, Taveesh Sharma, Tajveer Singh Dhesi et al. — [Rethinking Agent Security as a Networking Problem](http://arxiv.org/abs/2608.12172v1)
  <details><summary>📄 Abstract</summary>
  AI agents are rapidly becoming more capable and widely deployed, promising substantial gains in productivity and enabling new classes of applications. However, their growing autonomy also introduces significant privacy and security risks. Existing defenses are predominantly agent-centric, relying on the agent itself to detect threats and enforce privacy and security policies. This approach is fundamentally limited because it entrusts policy enforcement to AI agents whose LLM-driven behavior is i...
  </details>

- **2026-08-12** — Yutao Mou, Pengfei Yang, Zhe Yin et al. — [ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment of LLM-based Agents](http://arxiv.org/abs/2608.11878v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents integrated with external tools are vulnerable to indirect prompt injections embedded in environmental states. However, existing studies largely rely on manually implemented or reused environments, stochastic LLM-based tool simulation, and predefined injection locations, limiting scalable security research across broader domains. To bridge this gap, we propose **ToolHazard**, a scalable adversarial environment synthesis framework that reduces human engineering an...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-08-14** — Zhiyuan Jiang, Fangrui Huang, Hanwen Xing et al. — [Demystifying Agent Skills: Why They Work-Until They Don't](http://arxiv.org/abs/2608.14036v1)
  <details><summary>📄 Abstract</summary>
  Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome...
  </details>

- **2026-08-13** — Qianxi Yan, Chunrong Chen, Jiuzhou Zhao et al. — [SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback](http://arxiv.org/abs/2608.13120v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills are today either hand-authored or produced in a single LLM generation pass, and consequently possess no closed loop through which they might improve from the interaction failures they actually cause. Recent work does close this loop, but derives its feedback from single-turn question-answering evaluation. The consequence is a sharp asymmetry: once the first round has patched the gaps that a single exchange can reveal, the evolution gradient decays, the defects that surface only acro...
  </details>

- **2026-08-13** — Chang Liu, Yuqi Zhang, Yiman Zhong et al. — [SkillShapley: Boundary-Adaptive Shapley Valuation for Skill Step Attribution in LLM Agents](http://arxiv.org/abs/2608.13173v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are crucial external instructions that enable language agents to execute long procedural tasks such as coding or document processing. Existing agent skills are primarily created through human manual crafting or agent execution traces, with limited understanding of how each step contributes to overall skill performance on specific tasks; i.e., there remains an open problem in quantifying the contribution of individual steps within an agent skill. To address this issue, we first model...
  </details>

- **2026-08-12** — Gen Dong, Yanjie Gao, Liqun Li et al. — [Agent Skills Can Be Harmful: An Empirical Study of Skill-Induced Failures in LLM Agents](http://arxiv.org/abs/2608.11888v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are the de facto mechanism for extending LLM agents with reusable guidance. A skill can shape the agent's task execution, including planning, tool use, problem-solving, and validation. Prior work reported mixed results of agent skills: some skills improve task success rates, while others have no effect, increase token use and execution time, and even reduce success rates. This paper presents a comprehensive analysis of skill-induced agent failures by attributing task failures and co...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 4 papers

- **2026-08-12** — Yang Liu, Ran Zou — [When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers](http://arxiv.org/abs/2608.12623v1)
  <details><summary>📄 Abstract</summary>
  Language model classifiers with explanations are used for moderation, routing, topic triage, and low-resource annotation. We study black-box auditing when the defender has only clean calibration data without trigger information but can ask the classifier for a label plus a short rationale or quoted evidence. We introduce Groundedness Drift, a lightweight score measuring whether the answer summary remains grounded in the input. Across two 7B backbones, five datasets, and four common non-adaptive ...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-08-14** — Dipankar Sarkar — [A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation](http://arxiv.org/abs/2608.14329v1)
  <details><summary>📄 Abstract</summary>
  Principle-based regulation, with evaluative standards such as "fair, clear, and not misleading" or "deliver good outcomes", cannot be reduced to binary predicates, and LLM-as-judge is increasingly used as the substitute. Our position is that any such judge must be evaluated on four axes: accuracy, paraphrase robustness, adversarial robustness, and calibration. We release Principle-Bench, 168 cryptoasset financial-promotion scenarios mapped to two UK FCA principles, with paraphrase, adversarial k...
  </details>

- **2026-08-13** — Denzel Chiuseni, Athanase Bahizire, Silva Hama et al. — [Adversarial Robustness in Smishing Detection: A Comparative Analysis of Adversarial Fragility in Classical vs. Transformer-Based Detection Systems](http://arxiv.org/abs/2608.12889v1)
  <details><summary>📄 Abstract</summary>
  Smishing detection systems are commonly trained and evaluated on clean, monolingual text. In low-resource settings, however, attackers frequently circumvent these systems through character obfuscation, cross-lingual code-switching, and structural perturbation. This study evaluates adversarial robustness for five model architectures: three classical lexical models (Random Forest, XGBoost, CNN+BiLSTM) and two multilingual transformers (mBERT, XLM-RoBERTa), using a dataset of 27,037 messages. Class...
  </details>

- **2026-08-13** — Qiao Li, Xiaomeng Fu, Yuanshu Zhao et al. — [Semantic Steering for Controllable Generation: Tuning-Free Concept Erasure in Multimodal Diffusion Transformers](http://arxiv.org/abs/2608.12829v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Diffusion Transformers (MM-DiTs) have demonstrated remarkable text-to-image generation performance, surpassing traditional U-Net-based diffusion models. Nevertheless, their powerful generative capabilities also raise significant safety concerns, as they may generate sensitive or inappropriate content. While existing concept erasure methods aim to mitigate such risks, most require modifying model parameters, which are often architecture-specific and impractical for deployed larger mode...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 28 papers

- **2026-08-14** — Zhenyuan Li, Yi Jiang, Junjie Cheng et al. — [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](http://arxiv.org/abs/2608.14216v1)
  <details><summary>📄 Abstract</summary>
  Penetration testing is essential yet resource-intensive. Although large language models (LLMs) show promise for automating security auditing, existing agents mainly execute end-to-end workflows in simplified linear scenarios. Real-world black-box testing is fundamentally nonlinear: the attack graph is initially unknown and must be incrementally inferred from environmental feedback. Observations may reveal multiple attack branches, failures are often ambiguous, and critical clues may span long ac...
  </details>

- **2026-08-14** — Hansoo Lee, Pablo Fonseca, Md Haseen Akhtar — [Designing Mobile and Wearable Sensor-Fused Conversational Agents for Health and Wellbeing](http://arxiv.org/abs/2608.14273v1)
  <details><summary>📄 Abstract</summary>
  Mobile and wearable devices increasingly collect continuous wellbeing data, including sleep, activity, heart rate, stress, blood glucose, and blood pressure. Yet access to such data does not automatically help people interpret their condition or change behavior. Many health applications remain dashboard-first, presenting charts, thresholds, goals, and alerts while leaving users to decide what a change means and what action should follow. Conversely, generic LLM-based conversational agents (CAs) ...
  </details>

- **2026-08-14** — Ying Huang, Wencan Zhang, Brian Y. Lim — [AlignFace: Human-Aligned Face Similarity Metric with Interpretable Concept Relations](http://arxiv.org/abs/2608.14130v1)
  <details><summary>📄 Abstract</summary>
  Computer vision models for generated facial content, such as face editing and privacy protection, increasingly affect people, requiring similarity metrics that serve as faithful proxies for human perception. While perceptual evaluation has progressed from signal-based heuristics to representation-based metrics, current approaches are limited to behavioral modeling without cognitive alignment. They rely on implicit and spurious relations while assuming a universal observer, failing to account for...
  </details>

- **2026-08-14** — Myunghoon Ryu, Geunpyo Park, Sungjoon Lee et al. — [P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems](http://arxiv.org/abs/2608.14094v1)
  <details><summary>📄 Abstract</summary>
  Cloud-local LLM inference systems have the potential to use the reasoning capability of large cloud models while protecting sensitive user data on personal devices. Cloud-bound requests must exclude personally identifiable information (PII) to prevent external data leakage. Existing privacy-preserving methods rely on prompt perturbation, entity masking, or model fine-tuning, but these approaches may distort contextual semantics or require additional training. This paper proposes P2Skill, a promp...
  </details>

- **2026-08-13** — Yakun Huo, Yingquan Wang, Yangyang Liu et al. — [Paths: Prompt-aware Spatio-temporal Transformer with Hierarchical Multi-modal Fusion for RGB-Event Video Person Re-Identification](http://arxiv.org/abs/2608.13092v1)
  <details><summary>📄 Abstract</summary>
  RGB-Event Video Person Re-Identification (RE-VReID) aims to retrieve specific person across non-overlapping cameras with complementary RGB videos and event streams. However, existing methods often decouple spatial and temporal modeling, which limits their interaction. In addition, global-level RGB-Event fusion fails to fully exploit fine-grained discriminative cues. To address these issues, we propose Paths, a unified framework with spatio-temporal modeling and hierarchical multi-modal fusion fo...
  </details>

- **2026-08-13** — Beining Xu, Hairui Wang, Jiaxin Wang et al. — [Beyond Visual Evidence: Revealing and Mitigating Relational Privacy Leakage in Document MLLMs](http://arxiv.org/abs/2608.12911v1)
  <details><summary>📄 Abstract</summary>
  While the privacy risks of multimodal large language models (MLLMs) have drawn significant attention, the unique vulnerabilities of domain-specific MLLMs remain largely underexplored. Focusing on document understanding MLLMs for identity document processing, this paper investigates the privacy issues inherent in Key Information Extraction (KIE) tasks. We reveal that when input images lack sufficient visual evidence, these models often rely on memorized field relations from training data to infer...
  </details>

- **2026-08-13** — Rana Muhammad Ahmed, Sabahat Abbas — [Labels Are Not Endpoints: Treatment Leakage and Construct Validity in MCP Agent Security Evaluation](http://arxiv.org/abs/2608.12880v1)
  <details><summary>📄 Abstract</summary>
  Security evaluations of tool-using agents often equate stored labels with behavioral facts. We audit a preserved campaign by tracing 10,200 execution rows to 180 model-bound requests, 45 semantic requests, and 15 observable stimuli. Two schema treatments were delivered, but the planned external payload-family corpus was not. The historical grader exhibited direct treatment leakage: treatment metadata gated the ATTACK_SUCCESS class, so fixed behavior could change class under treatment relabeling....
  </details>

- **2026-08-13** — Ruofei Qu, Wei Feng, Hongzhan Ma et al. — [RealmEye: Virtual Machine Introspection for Arm CCA Realm VMs](http://arxiv.org/abs/2608.12822v1)
  <details><summary>📄 Abstract</summary>
  Confidential VMs (CVMs) have become the dominant substrate for sensitive cloud workloads, from financial services to privacy-preserving AI inference. The hardware isolation that protects these CVMs from a malicious cloud also blinds their owners to what runs inside them: kernel rootkits planted via network or supply-chain attacks can hide processes, tamper with kernel data, and exfiltrate model weights under the cover of the same isolation that defends the VM. Tenants therefore need to inspect a...
  </details>

- **2026-08-13** — Muhammad Hannan Akram, Muhammad Abubakar Rashid, Wassi Haider Kabir et al. — [Heterogeneity-Aware Belief Synchronization for Semantic Communication in AI-Native 6G Networks](http://arxiv.org/abs/2608.13394v1)
  <details><summary>📄 Abstract</summary>
  6G networks will not be serving as communication infrastructures only; rather, they are expected to evolve into intelligent systems, where thousands of autonomous artificial intelligence (AI) agents are interconnected. The agents are deployed across a wide range of platforms including low Earth orbit (LEO) satellites, high-altitude platforms (HAPs), unmanned aerial vehicles (UAVs), edge servers, and terrestrial devices. These agents continuously observe their environment and exchange information...
  </details>

- **2026-08-13** — Xinming Wang, Weinong Wang, Hongming Yang et al. — [Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs](http://arxiv.org/abs/2608.12781v1)
  <details><summary>📄 Abstract</summary>
  Hybrid-thinking multimodal large language models (MLLMs) allow a single model to alternate between deliberative thinking and latency-efficient non-thinking inference. Although these modes differ in reasoning budget, their delivered responses should satisfy the same user-facing standard. Correctness alone may not characterize this response quality; we therefore evaluate task accuracy and response-pattern failures as complementary outcomes. We study this gap through \textbf{response-pattern alignm...
  </details>

- **2026-08-13** — I. Dey, I. Cherkaoui — [Deterministic Johnson--Lindenstrauss Projections from Pisot $β$-Transformations for Zero-Knowledge Private Routing](http://arxiv.org/abs/2608.13078v1)
  <details><summary>📄 Abstract</summary>
  Zero-knowledge (ZK) proofs certify that a message belongs to an allowed semantic class without revealing the message, but the certificate compares a high-dimensional embedding against class centroids, so its cost grows with the embedding dimension $d$. A Johnson--Lindenstrauss (JL) projection lowers $d$ to $m\ll d$ while preserving pairwise distances, yet a random JL matrix must be committed and its sampling proved inside the circuit, which is costly and a leakage risk. We construct a public det...
  </details>

- **2026-08-13** — Wenjin Liu, Shen Pang, Tiesunlong Shen et al. — [TIEM: Temporal Integration of Hypergraph Evidence and Skill Memory for Event-Driven Financial Forecasting](http://arxiv.org/abs/2608.13024v1)
  <details><summary>📄 Abstract</summary>
  Event-driven catalyst-outcome forecasting increasingly uses retrieval- and memory-augmented large language model agents for prediction. However, training-data contamination and temporal leakage can create an Evidence Chasm between reported accuracy and true predictive ability. We propose TIEM, a timestamp-gated framework with three coordinated components: an Event-Evidence Hypergraph (EEH) for timestamp-filtered multi-tier retrieval; a Case-based Skill Memory (CSM) for source-tagged temporal ski...
  </details>

- **2026-08-13** — Saleh Almohaimeed, Saad Almohaimeed, Mousa Jari et al. — [Privacy-Preserving RAG by Concealing Sensitive Information from External LLMs](http://arxiv.org/abs/2608.12675v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) is widely used to improve the performance of Large Language Models (LLMs) in answering user queries. Existing privacy research on RAG has focused on preventing unauthorized users from accessing sensitive data. However, another important problem that is often overlooked in RAG privacy research is that external generators have access to the query and the retrieved documents, which may contain confidential information that could potentially be misused or accesse...
  </details>

- **2026-08-12** — Florian Braun — [Excess Separability: Nuisance-Controlled Residual-Stream Probing for Benchmark Contamination Detection](http://arxiv.org/abs/2608.12652v1)
  <details><summary>📄 Abstract</summary>
  Benchmark contamination is diagnosed today with n-gram overlap, with likelihood-based membership inference, or with canary strings, and each needs something usually unavailable: the training corpus, a well-chosen test statistic, or foresight at dataset release. A recent alternative reads contamination off a linear probe on internal activations. We show that the natural way to do this does not work, and specify one that survives measurement.   The protocol reports a zero-sum contrast on the depth...
  </details>

- **2026-08-12** — Joonhee Lee — [Proactive Computing](http://arxiv.org/abs/2608.12649v1)
  <details><summary>📄 Abstract</summary>
  Computing systems are moving from reactive tools toward systems that sense, interpret, predict, and act before explicit user requests. This transition is enabled by the global scale of mobile connectivity, the rapid expansion of wearable and ambient sensing, advances in machine learning and foundation models, distributed edge infrastructure, and physical actuation. We define \emph{proactive computing} as a paradigm in which systems infer user context, anticipate future needs or risks, and initia...
  </details>

- **2026-08-12** — Shidong Pan, Clark LaChance, Zhen Tao et al. — [SoK: From Generation to Consumption of Privacy Documents in Software Systems](http://arxiv.org/abs/2608.12511v1)
  <details><summary>📄 Abstract</summary>
  Privacy documents (e.g., privacy policies) are a central mechanism through which digital services disclose data practices and seek user consent. Over the past decades, research on privacy documents has expanded significantly, encompassing not only traditional privacy policies but also short notices (e.g., privacy labels) and interface-level transparency mechanisms. As this research area continues to grow, it has become increasingly difficult to obtain a coherent view of how privacy documents are...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 15 papers

- **2026-08-14** — Parameswaran Kamalaruban, Viktor Drobnyi, Maeve Madigan et al. — [MINT: A Universal Zero-Shot Predictor for Transaction Data](http://arxiv.org/abs/2608.14198v1)
  <details><summary>📄 Abstract</summary>
  Banks analyse sequential financial transaction data to perform many tasks, including fraud prevention, credit risk assessment and offer personalization. To improve the predictive accuracy of these tasks, Payments Foundation Models encode transaction sequence data as rich contextual embeddings, which can then be provided to task-specific models as features. However, these Foundation Models are not designed for flexible zero-shot reasoning across novel downstream prediction tasks, limiting their a...
  </details>

- **2026-08-13** — Satoshi Takahashi, Nobuji Kouno, Masaaki Komatsu et al. — [Rules or Character? Scaling Laws for AI Safety Design](http://arxiv.org/abs/2608.13345v1)
  <details><summary>📄 Abstract</summary>
  Artificial Intelligence (AI) safety systems combine character shaping (e.g., Reinforcement Learning from Human Feedback [RLHF], Constitutional AI), which modifies behavioral distributions at training time, with rule enforcement (e.g., output filters, safety classifiers), which blocks harmful outputs at inference time, yet little formal analysis exists on how their optimal balance should change as deployment scales increase. We introduce a stylized comparative-statics model that parameterizes saf...
  </details>

- **2026-08-13** — Ping Wu, Haibo Tong, Feifei Zhao et al. — [Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety](http://arxiv.org/abs/2608.13304v1)
  <details><summary>📄 Abstract</summary>
  Safety tuning can improve harmful refusal, but models may learn surface-form shortcuts: wrapped harmful prompts bypass safety, while similarly wrapped benign prompts are over-refused. We propose Wrapper-Based Intent-Form Augmentation (WIFA), an automatic intent-group augmentation method that pairs wrapped harmful examples with structurally matched wrapped benign counterexamples, requiring no external teacher or manual per-wrapper intent labels. We use WIFA as a common data layer for two compleme...
  </details>

- **2026-08-13** — Severin Engelmann, Daniel Susser — [From Fair Representation to Just Recognition in Generative AI](http://arxiv.org/abs/2608.12669v1)
  <details><summary>📄 Abstract</summary>
  The fair AI/ML literature has long distinguished distributive fairness, concerning how automated systems allocate resources and opportunities, from representational fairness, concerning how they shape the ways individuals and social groups are perceived, understood, and accorded social status. Generative AI is rebalancing these normative dimensions. Unlike predictive systems, large language models (LLMs) and related technologies are fundamentally expressive: their primary function is to convey m...
  </details>

- **2026-08-12** — Zhenpeng Li — [Non-Degenerate Risk Certification for Automated Security Decisions: A Decision-Contract Theory with ATT\&CK-Aligned Triage as a Worked Instance](http://arxiv.org/abs/2608.12444v1)
  <details><summary>📄 Abstract</summary>
  An unconditional risk bound on automated decisions can be satisfied without automating anything, since a selector that never acts drives the bound to zero. We show this is structural: any risk certificate is defined over a decision contract, the inputs a system acts on plus the semantic relation under which an output counts correct, and weakening either hides base-classifier error. We develop a decision-contract theory: an error-conservation law showing error is only reassigned among harmful aut...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-08-13** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research](http://arxiv.org/abs/2608.12984v1)
  <details><summary>📄 Abstract</summary>
  Long-form research reports generated by large language models drift, contradict themselves, and lose provenance: the same metric appears with different values, and rumor is quoted as confidently as an audited filing. We present a two-tier agentic system that separates a maintained, point-in-time knowledge library from report writing. A deterministic "librarian" ingests timestamped sources into a trust-tiered ontology, layering evidence cards, an authoritative metric ledger, and a claim graph int...
  </details>

- **2026-08-11** — Lukasz Olejnik, Wenchao Dong, Jonas R. Kunst et al. — [IO Factory: Simulating AI-Enabled Influence Campaigns at Scale](http://arxiv.org/abs/2608.10920v1)
  <details><summary>📄 Abstract</summary>
  We introduce IO Factory, an AI-driven framework for simulating information and influence campaigns as fully integrated, traceable processes. The threat of digital manipulation now extends beyond persuasive text from individual language models to AI swarms, i.e., persistent groups of coordinated agents that adapt to platform feedback and disguise organized campaigns as ordinary social interaction. Because such campaigns cannot be identified from isolated messages alone, they must be analyzed acro...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 68 papers

- **2026-08-14** — Ruizhe Wang, Meng Xu, N. Asokan — [Finding Vulnerabilities via LLM-Augmented Semantics-Aware Type-Checking](http://arxiv.org/abs/2608.14533v1)
  <details><summary>📄 Abstract</summary>
  Vulnerability detection via static analysis traditionally relies on security experts encoding insecure coding patterns into algorithmic rules. However, this approach often focuses on syntactic patterns and overlooks deeper semantic information in the code, such as the meanings of variable and function names. As software systems grow more complex, modeling vulnerabilities using only syntactic rules becomes increasingly challenging.   In this paper, we propose a semantics-aware approach to detecti...
  </details>

- **2026-08-14** — Noel Murasko, John C. Bowman — [Hybrid Dealiasing and Implicit Packing for Real Convolutions](http://arxiv.org/abs/2608.14497v1)
  <details><summary>📄 Abstract</summary>
  Hybrid dealiasing is an FFT-based method for computing linear convolutions of complex-valued data that reduces the cost of dealiasing by performing zero padding implicitly. We develop two new algorithms that extend hybrid dealiasing to real-valued convolutions.   The first algorithm exploits conjugate symmetries in the transformed data and computes each residue contribution directly. The second algorithm employs complex-valued hybrid dealiasing via a new implicit packing technique, which packs r...
  </details>

- **2026-08-14** — Panjing He, Mingyue Cheng, Yucong Luo et al. — [SheetCompass: Hierarchical Relation Graphs for Agentic Spreadsheet Reasoning](http://arxiv.org/abs/2608.14452v1)
  <details><summary>📄 Abstract</summary>
  Spreadsheets are widely used to organize, analyze, and manipulate semi-structured data, yet automated spreadsheet reasoning remains challenging for large language models (LLMs). Real-world workbooks often contain implicit cross-table associations, fine-grained column dependencies, and complex spatial layouts. Existing methods typically flatten these multidimensional structures into sequential strings, losing important intra-sheet boundaries and inter-sheet semantics. Consequently, LLMs cannot ex...
  </details>

- **2026-08-14** — Ignacio D. Lopez-Miguel, Andreas Happe, Jürgen Cito et al. — [ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning](http://arxiv.org/abs/2608.14352v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based agents are increasingly used for complex tasks such as software testing and cybersecurity assessment. While these agents demonstrate impressive capabilities, their behavior is difficult to understand, explain, and analyze. Existing evaluations focus mainly on task success and execution traces, offering limited insight into the strategies employed by the agent. We present ATLAS (Automata Learning for Agent Trajectory Analysis and Strategy Discovery), an approach f...
  </details>

- **2026-08-14** — Seeyeon Kim, Juhyeong Jin, Joo-Young Kim — [Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths](http://arxiv.org/abs/2608.14333v1)
  <details><summary>📄 Abstract</summary>
  Modern mixture-of-experts (MoE) language models increasingly strain the capacity and cost efficiency of high-bandwidth memory (HBM), as rapidly growing expert weights must be provisioned close to GPUs. High-bandwidth flash (HBF) offers substantially greater capacity, but conventional designs typically deliver HBF-resident expert weights to the GPU through HBM, leaving an additional direct GPU-HBF connection underutilized. We explore an HBF organization that simultaneously exploits two independen...
  </details>

- **2026-08-14** — Francesco Quinzan, Noor Munir, Yishun Lu et al. — [Detecting Contaminated Code-Generation Prompt Batches via Influence Functions](http://arxiv.org/abs/2608.14303v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for code generation, yet they remain vulnerable to prompts that elicit insecure implementations. Existing defenses typically rely on predefined threat models or known vulnerability patterns, limiting their effectiveness against novel attacks. We propose CodeSIFT, a threat-model-agnostic detection method that leverages influence functions to identify batches of prompts that induce anomalous model behavior. Rather than detecting specific vulnerabi...
  </details>

- **2026-08-14** — Sojeong Park, Hyeonsu Lyu, Jaehyun Choi et al. — [LLM-Assisted LDPC Decoding via Syndrome-Verified Semantic Priors](http://arxiv.org/abs/2608.14280v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication exploits the meaning of the payload, which bit-level processing discards. When channel decoding fails on a natural language payload, the errors appear as corrupted characters in the recovered text. A large language model (LLM) infers the intended characters from the semantic context, but it can also produce incorrect corrections. Applying them directly introduces new bit errors when the LLM modifies characters incorrectly. In this paper, we propose an LLM-assisted decoding...
  </details>

- **2026-08-14** — Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos et al. — [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](http://arxiv.org/abs/2608.14161v1)
  <details><summary>📄 Abstract</summary>
  LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. Recent advances in LLM reasoning offers a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on ...
  </details>

- **2026-08-14** — Ziyan He, Xiongtai Yang, Tao Wang — [PISA: A Pseudo-Individual Source-Domain Feature Adaptation Framework for Test-Time Open-Vocabulary Object Detection](http://arxiv.org/abs/2608.14142v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary object detection test-time adaptation (OVOD-TTA) aims to address the performance degradation that pre-trained base models suffer when encountering image-domain shifts. Existing source-free OVOD-TTA methods rely either on refined test-time information for re-scoring or on pseudo-labels for self-training, leading to significant accuracy degradation when initial predictions are poor. Meanwhile, most conventional source-domain estimation methods recover abstract, sparse representatio...
  </details>

- **2026-08-14** — Ismail El Hamraoui, Sagar Jose, Nicolas Bureau et al. — [A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents](http://arxiv.org/abs/2608.14109v1)
  <details><summary>📄 Abstract</summary>
  Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on ev...
  </details>

- **2026-08-13** — Yukun Dai, Mingzhe Dai, Tianshi Wang et al. — [UniTexture: Cross-Task Universal Adversarial Textures for Vision-Language-Action Models](http://arxiv.org/abs/2608.13453v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have emerged as generalist robotic policies capable of following diverse language instructions and performing a wide range of manipulation tasks. However, their direct control over embodied agents also exposes them to adversarial interference that may cause unsafe physical behaviors. Existing attacks on robotic policies are typically optimized for a single task or instruction, leaving the cross-task vulnerabilities of multitask VLAs largely unexplored. We intr...
  </details>

- **2026-08-13** — Md Wasiul Haque, Sagar Dasgupta, Mizanur Rahman et al. — [LLM-Assisted Dynamic Threat Analysis for Attacker-Reachable Software Weaknesses in Autonomous Vehicles](http://arxiv.org/abs/2608.13450v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles depend on large safety-critical software stacks, where weaknesses reachable from adversarial inputs may affect steering, braking, or other control decisions. Static analysis can identify candidate sites, but dynamically confirming exploitability requires executable test artifacts that are difficult to construct manually. We investigate whether large language models (LLMs) can automate this process for Autoware, an open-source autonomous-driving stack. We perform compiler-prec...
  </details>

- **2026-08-13** — Raphaël Mothe, Otfried Gühne — [Witnessing the architecture of quantum circuits](http://arxiv.org/abs/2608.13169v1)
  <details><summary>📄 Abstract</summary>
  Determining whether a target unitary can be implemented within a prescribed quantum circuit architecture is a fundamental problem in quantum information, with direct implications for optimisation and compilation of quantum circuits, and hardware-efficient quantum computation. While existing synthesis and compilation methods are primarily constructive, they generally do not provide rigorous certificates that a unitary cannot be realised using given implementation resources. Here we introduce a ge...
  </details>

- **2026-08-13** — Yi Shi, Huichao Xie, Yuqing Wang et al. — [P2Fusion: Prompt-based Progressive Infrared-Visible Image Fusion via Dual-Prior Distillation](http://arxiv.org/abs/2608.13045v1)
  <details><summary>📄 Abstract</summary>
  Infrared-visible image fusion (IVIF) is pivotal for multimodal perception, yet reconciling the inherent information disparity between thermal and textural features remains a fundamental challenge. Existing prior-guided methods often rely on static constraints that induce optimization conflicts or utilize extrinsic semantic priors from large-scale foundation models (e.g., CLIP/DINO), which frequently fail to exploit the intrinsic modality characteristics essential for high-fidelity fusion. To add...
  </details>

- **2026-08-13** — Peng Li, Qianqian Xu, Shilong Bao et al. — [UniTraffic-Agent: Unified Traffic Video Reasoning for AI City Challenge 2026 Track 3 with Two Out-of-Domain Evaluations](http://arxiv.org/abs/2608.13031v1)
  <details><summary>📄 Abstract</summary>
  Traffic video understanding has become an important problem in intelligent transportation, as road videos provide direct evidence for accidents, violations, and interactions between vehicles and vulnerable road users. A useful system should explain how a traffic event develops, why it happens, and when the relevant interaction occurs, yet this remains difficult for multimodal large language models (MLLMs) because traffic videos contain sparse events and varied viewpoints. We introduce UniTraffic...
  </details>

- **2026-08-13** — Qiyang Chen, Yixi Li, Fengwei Zhang et al. — [ATOBench: Tracing How Autonomous Penetration-Testing Agents Verify Vulnerabilities When Target Evidence Lies](http://arxiv.org/abs/2608.12996v1)
  <details><summary>📄 Abstract</summary>
  Autonomous penetration-testing agents rely on target responses. These responses guide both subsequent actions and the final report. A deceptive response can therefore redirect both the attack trajectory and the agent's verification process. However, final reports reveal little about how an agent interprets conflicting evidence, changes course, decides to stop, or turns observations into a vulnerability claim. We introduce ATOBench, an evaluation framework that makes this verification process obs...
  </details>

- **2026-08-13** — Wencong Zhang, Yue Zhang, Meiyan Huang et al. — [Dual-Manifold Geometry Guided Representation Learning: Adaptive Coupling between Kernel and Data Spaces](http://arxiv.org/abs/2608.12737v1)
  <details><summary>📄 Abstract</summary>
  Deep representation learning has primarily focused on how features evolve across network layers, while largely overlooking the structured geometry embedded in network parameters. We introduce a dual-manifold perspective in which each convolutional layer contains two coupled geometric spaces: a Kernel Manifold induced by convolutional filters and a Data Manifold characterized by intermediate feature representations. Because these manifolds share the same channel space, parameter geometry can prov...
  </details>

- **2026-08-13** — Zirui Cheng, Xun Xu, Tiankai Chen et al. — [MAG: MAnifold Guided Semi-Supervised Multi-modal In-Context Learning](http://arxiv.org/abs/2608.12724v1)
  <details><summary>📄 Abstract</summary>
  Few-shot in-context learning (ICL) with multi-modal large language models (MLLMs) enables task adaptation without parameter updates, but its performance is highly sensitive to the quality and coverage of the selected demonstrations. While unlabeled multi-modal data is abundant, it remains elusive how to exploit them for ICL. We propose MAG (MAnifold-Guided semi-supervised in-context demonstra- tion selection), an efficient framework that leverages unlabeled data to improve multi-modal ICL. MAG f...
  </details>

- **2026-08-13** — Xiaoyan Feng, Yanjun Zhang, He Zhang et al. — [Tracing Provenance and Detecting Tampering with Complementary LLM Watermarks](http://arxiv.org/abs/2608.12713v1)
  <details><summary>📄 Abstract</summary>
  Watermarking LLM-generated text is an important task for tracing its provenance. Existing LLM watermarks preserve provenance under editing, but this same robustness allows an adversary to alter critical content while retaining attribution, a vulnerability known as piggyback spoofing. We introduce an innovative watermark that jointly provides provenance and tamper evidence. It co-embeds a robust signal and a fragile signal into each generated token. The signals share the same mechanism but use in...
  </details>

- **2026-08-13** — Hamza Shafiq, Hung Manh Pham, Bin Zhu et al. — [CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation](http://arxiv.org/abs/2608.12944v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG), photoplethysmography (PPG), and phonocardiography (PCG) provide complementary views of the same cardiac cycle, yet existing cardiac foundation models are trained for a single sensing modality, leaving the shared physiology across sensors unexploited. We introduce CardioState-JEPA, a cardiac foundation model to learn a single shared representation jointly across ECG, PPG, and PCG, built on a physiology-aware joint-embedding predictive architecture. The model maps hetero...
  </details>

- **2026-08-12** — Xingzi Xu, Karim Bouyarmane — [Trie Automata for Constrained Decoding over Large Finite Sets](http://arxiv.org/abs/2608.12574v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly need to generate structured outputs that conform to predefined schemas, with one common constraint being selection from a finite set of valid strings. Current constrained decoding systems handle this through general-purpose grammar compilation, which becomes prohibitively slow as the number of valid values grows into the thousands, a cardinality wall. We introduce the trie automaton, a specialized mechanism that exploits finite-set structure (shared prefixes, b...
  </details>

- **2026-08-12** — Abdelhamid Salem, Hana Shamata, Salma Elkawafi et al. — [RSMA-Enabled ISAC Networks with Fluid Antenna Systems: Stochastic Geometry Analysis and Low-Complexity Resource Allocation](http://arxiv.org/abs/2608.12517v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate the downlink performance of multi-cell RSMA-enabled ISAC networks in which base stations (BSs), communication users, and sensing targets are spatially distributed according to independent Poisson point processes (PPPs). Each BS simultaneously serves multiple users using RSMA while exploiting the common stream as a dual-functional communication and sensing waveform. The users are equipped with FAS that selects the best antenna port to maximize the received signal qua...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 58 papers

- **2026-08-14** — Yasir Ech-Chammakhy, Oussama Azrara, Jaafar Chbili et al. — [STINER: Automated Extraction of Strategic Cyber Threat Intelligence from X](http://arxiv.org/abs/2608.14418v1)
  <details><summary>📄 Abstract</summary>
  Strategic Cyber Threat Intelligence (CTI) focuses on high-level insights, such as identifying targeted industries, attributing attacks to specific ransomware groups, and assessing the scale of data loss. Today, X (formerly Twitter) has become the fastest source for this intelligence, often hosting real-time breach announcements days before formal vendor reports. Converting this raw chatter into actionable intelligence requires navigating a complex linguistic landscape. Conventional Named Entity ...
  </details>

- **2026-08-14** — Sheng Hong, Yixuan Huang, Weiwei Jiang et al. — [BGA: A noise-immune neural distillation framework for malicious signature extraction in high-entropy encrypted flows](http://arxiv.org/abs/2608.14126v1)
  <details><summary>📄 Abstract</summary>
  To mitigate attention dilution in high-entropy TLS 1.3 flows, we propose BGA, a noise-immune neural distillation framework for encrypted threat intelligence.The methodology first employs Analysis of Variance (ANOVA) to decouple high-discriminatory control-plane features - specifically industrial setpoints - from stochastic cryptographic noise. To resolve the extreme class imbalance within a corpus of 86,878 flow records, a Wasserstein GAN with Gradient Penalty (WGAN-GP) module, enforcing the 1-L...
  </details>

- **2026-08-14** — Thiago Sandoval, Ufuk Topcu — [Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers](http://arxiv.org/abs/2608.14089v1)
  <details><summary>📄 Abstract</summary>
  Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees w...
  </details>

- **2026-08-14** — Yubo Zhang, Yiyao Liu, Xiaodong Wang — [Learning-to-Transition for Large-scale and High-Order MIMO Detection](http://arxiv.org/abs/2608.14511v1)
  <details><summary>📄 Abstract</summary>
  High-order multiple-input multiple-output (MIMO) detection requires efficient search over a large discrete symbol space while producing reliable soft information for channel decoding. This paper develops a learning-to-transition (L2T) framework that formulates MIMO detection as a stochastic sequence of complete-vector transitions. At each transition, a channel-coupled Transformer updates both the instance embedding and the sampling policy, while a blockwise autoregressive factorization captures ...
  </details>

- **2026-08-14** — Yuhao Zhan, Bingxiang He, Zecong Tang et al. — [PACE-Bench: Benchmarking Physics Adaptation via Code Evolution in Dynamic Environments](http://arxiv.org/abs/2608.14441v1)
  <details><summary>📄 Abstract</summary>
  Self-evolving agents improve future behavior from interaction experience, yet existing evaluations typically optimize under fixed execution conditions and do not test recovery after those conditions change. To address this gap, we introduce PACE-Bench (Physics Adaptation via Code Evolution), a simulator-grounded benchmark of 144 source-to-target adaptation pairs across six physics domains. Each pair links a source environment to a mutated target environment with the same goal and interface. A co...
  </details>

- **2026-08-14** — Junichiro Niimi — [Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary](http://arxiv.org/abs/2608.14186v1)
  <details><summary>📄 Abstract</summary>
  Tabular anomaly detection is dominated by classical density-proxy methods (Isolation Forest, OCSVM, LOF), reconstruction-based detectors (Autoencoders, VAEs), and modern non-parametric scorers (COPOD, ECOD, Deep SVDD), all of which approximate the inlier distribution only indirectly; explicit energy-based models are largely absent. Motivated by the recent revival of EBMs in deep learning (e.g., Energy-Based Transformers, JEPA), we revisit the classical Deep Boltzmann Machine (DBM) for this task ...
  </details>

- **2026-08-14** — Syeda Anshrah Gillani, Mirza Samad Ahmed Baig — [Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice](http://arxiv.org/abs/2608.14399v1)
  <details><summary>📄 Abstract</summary>
  Patients increasingly ask large language model (LLM) assistants which doctor to see, making these systems AI infomediaries: algorithms that intermediate one person's choice among other people and thereby decide, silently and at scale, which physicians become visible. We report a prespecified randomized algorithm audit of what causally moves those recommendations. Seven models (six open-weight; gpt-4o-mini) each chose among five synthetic family-medicine physician cards whose attributes were inde...
  </details>

- **2026-08-14** — Shuo Liang, Yixing Ma, Pengfei Zhou et al. — [Can We Defend Against AI-Generated Video Attacks on Real-World Crisis Events? A Systematic Evaluation of Detectors, Generators and Social Dissemination](http://arxiv.org/abs/2608.14391v1)
  <details><summary>📄 Abstract</summary>
  Recent video generators can fabricate realistic depictions of wars, disasters, public emergencies, and other real-world crises, creating substantial risks of misinformation. Existing benchmarks, however, provide limited evidence on detector and generator behavior in such settings, including how detectability varies with generation conditions, how people perceive generated videos, and whether detectors remain reliable during social dissemination. To address this gap, we introduce RA-Bench, a benc...
  </details>

- **2026-08-14** — Jinlong Wang, Yuang Jia, Junhong Lin et al. — [CoDS: Robust Collaborative Perception via Expert-driven Detection and BEV Segmentation](http://arxiv.org/abs/2608.14085v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception breaks through single-view limitations via multi-agent information exchange. However, multi-source noise such as pose errors and communication delays degrades fusion feature quality, constraining perception performance. Joint training of detection and BEV segmentation provides a natural remedy, where segmented road regions help constrain target distributions and detection bounding boxes help recover ambiguous segmentation boundaries. To this end, we propose a robust Coll...
  </details>

- **2026-08-13** — Shubin Lu, Jiaqi Yin, Yihao Huang — [QuISE: Defense against Typographic Attacks on VLMs via Query-Irrelevant Semantic Editing](http://arxiv.org/abs/2608.13119v1)
  <details><summary>📄 Abstract</summary>
  Typographic attacks pose a critical threat to vision-language models (VLMs) by injecting misleading text into images and causing models to rely on adversarial textual cues rather than visual evidence. Existing defenses often require model-specific modifications, additional training, or access to internal model components, limiting their applicability to modern closed-source VLMs. In this paper, we propose QuISE, a model-agnostic, training-free black-box defense based on query-irrelevant semantic...
  </details>

- **2026-08-13** — Atul Kabra, Prakhar Paliwal, Manjesh K. Hanawal — [Operationalizing Cyber Threat Intelligence with GraphRAG](http://arxiv.org/abs/2608.13050v1)
  <details><summary>📄 Abstract</summary>
  When a security researcher publishes a report on a cyberattack, detection engineers are supposed to turn it into working detection rules. In practice, most automated attempts at this only extract the simplest clues from the report --- bad IP addresses, domain names, and file hashes --- and turn them into block lists. This is a weak strategy, because attackers can change these simple clues within hours or days, so the resulting detections stop working almost as soon as they are deployed. Security...
  </details>

- **2026-08-13** — Sanjay Kariyappa, Severin Klingler, G. Edward Suh — [PIPES: Securing Agent Perception with Provenance and Priors](http://arxiv.org/abs/2608.12789v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents consume external data from sources with different levels of trust, yet tool responses rarely identify who produced each component or what it should convey. We show that this gap enables state-corruption attacks, in which attacker-controlled content makes environmental claims beyond the informational authority of its response component and corrupts the agent's perceived environment, making the resulting action appear justified to existing guardrails. We introduce PIPES (Provenan...
  </details>

- **2026-08-13** — Rishi Shah, Rishav Shrestha — [A Contract-Grade Verifier for LLM-Generated GPU Kernels, and a Native Blackwell Backward for the Gated-Linear-Recurrence Family](http://arxiv.org/abs/2608.12700v1)
  <details><summary>📄 Abstract</summary>
  Systems that generate GPU kernels with language models report high correctness rates. Those rates come from a single loose test: run the kernel on a few random inputs at one fixed shape and accept it if the output is close to a reference. A kernel can pass that test and still be silently wrong. It can return an ordinary number where the true answer is a NaN or an infinity, differ from run to run, break when the shape changes, or accumulate in fp16 where the reference keeps an fp32 total. We buil...
  </details>

- **2026-08-13** — Fanfei Li, Jana Zeller, Manuel Prada-Corral et al. — [LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure](http://arxiv.org/abs/2608.13545v1)
  <details><summary>📄 Abstract</summary>
  Modern language models are trained on heterogeneous web-scale text corpora. Consequently, studying knowledge and skill acquisition is difficult, as prior exposure to related content is hard to characterize. To address this challenge, we introduce LITTLECURRICULUM, a curated 88B-token pretraining corpus tailored to U.S. elementary school material, explicitly excluding concepts, facts, and vocabulary taught above Grade 5. Training a 5B-parameter LLM from scratch on LITTLECURRICULUM yields LITTLELE...
  </details>

- **2026-08-13** — Benjamin Agyekum, Fabio Santos — [Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair](http://arxiv.org/abs/2608.13404v1)
  <details><summary>📄 Abstract</summary>
  Background: Iterative feedback loops are the dominant paradigm for improving LLM-generated Infrastructure-as-Code (IaC): validators such as Checkov and terraform validate feed error signals back for successive repair attempts. Prior work reports cumulative-best metrics, which are non-decreasing by construction, so the raw per-iteration security trajectory has never been examined for IaC. Aims: We study security regression (a previously-passing CIS Benchmark check that fails after a repair iterat...
  </details>

- **2026-08-13** — Zeta Avarikioti, Dimitris Karakostas, Karl Kreder et al. — [Slow and Steady: Preventing MEV with Verifiable Delays](http://arxiv.org/abs/2608.13271v1)
  <details><summary>📄 Abstract</summary>
  Our work presents a defense mechanism against Maximal Extractable Value (MEV) opportunities in distributed ledgers. The mechanism relies on the idea of enforcing a verifiable delay when generating transactions, such that a block creator cannot react to the appearance of a MEV opportunity without breaking liveness. We present positive results both in the Byzantine setting and in a game theoretic model of rational participants. We additionally present negative bounds that outline the limitations o...
  </details>

- **2026-08-13** — Shuailei Zhang, Muyun Jiang, Wei Zhang et al. — [EEG-PRIME: Prototype-Aligned Representation Learning with Multi-Level Conditioning for EEG Decoding](http://arxiv.org/abs/2608.13072v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) decoding models often generalize poorly across datasets and subjects due to domain shifts in acquisition protocols and individual neurophysiology. We propose EEG-PRIME, a two-stage EEG foundation model for cross-dataset multi-task decoding. EEG-PRIME combines masked pretraining with prototype-aligned instruction tuning to enable instruction-aware and subject-invariant decoding across diverse BCI paradigms. During pretraining, an EEG encoder learns transferable repres...
  </details>

- **2026-08-13** — Zhenhua Zou, Sheng Guo, Qiuyang Zhan et al. — [InterSAGE: The Secure and Verifiable Interoperability Protocol for An Internet of Agents](http://arxiv.org/abs/2608.13030v1)
  <details><summary>📄 Abstract</summary>
  The emerging Internet of Agents enables LLM-powered agents to discover peers, invoke tools, and delegate tasks across organizational boundaries. Existing protocols increasingly define how agents exchange messages, but not how an agent proves its identity, authorization, advertised capabilities, or accountability after delegation. We present InterSAGE, a trust-native protocol suite that supplies this missing security substrate alongside, rather than in place of, communication protocols. InterSAGE...
  </details>

- **2026-08-13** — Jiajun Ruan, Peiyang Li, Yukun Chen et al. — [Beyond Handcrafted Security: Towards Self-Evolving Defense for LLM Agents](http://arxiv.org/abs/2608.12977v1)
  <details><summary>📄 Abstract</summary>
  The expanding operational capabilities of large language model (LLM) agents introduce sophisticated security threats. Runtime defenses have emerged as an effective approach to mitigating these risks by integrating security mechanisms into the agent execution loop. However, existing runtime defenses rely heavily on manually designed interventions and lack a principled framework for their construction and maintenance. In this work, we first develop a harness-level formulation of runtime defense th...
  </details>

- **2026-08-13** — Zekai Li, Yihao Liang, Hongfei Zhang et al. — [FlashDrive: Flash Vision-Language-Action Inference for Autonomous Driving](http://arxiv.org/abs/2608.12932v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models promise to bring end-to-end reasoning to autonomous driving, but their computational cost remains far too high for real-time control. The core challenge is structural: VLA inference is not a single bottleneck but a cascade of four. Visual encoding wastes compute on overlapping video frames; language-model prefill recomputes context that could be carried over from the previous timestep; reasoning tokens are generated serially despite low entropy; and flow-match...
  </details>

- **2026-08-13** — Jiacheng Guo, Suozhi Huang, Yunlong Gao et al. — [AQuA: Recursively Self-Improving Quantitative Trading Research Agents](http://arxiv.org/abs/2608.12841v1)
  <details><summary>📄 Abstract</summary>
  We study recursive self-improvement at the level of quantitative-investment research: whether an autonomous system can use evidence from earlier experiments to improve the hypotheses and candidates proposed in later iterations. We present AQuA, which comprises two separate language-model-driven research systems: one for symbolic factor discovery and one for trainable model development. The two systems do not share agents, memories, candidate spaces, or research state. Instead, each independently...
  </details>

- **2026-08-13** — Chengyang He, Tahreem Arif, Marko Zivkovic et al. — [CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical Narratives](http://arxiv.org/abs/2608.12779v1)
  <details><summary>📄 Abstract</summary>
  Understanding the temporal progression of symptoms in clinical narratives is critical for disease monitoring, safety surveillance, and causality assessment. Clinical narratives, however, rarely provide explicit temporal anchors. Current approaches to temporal information reasoning focus predominantly on pairwise relation classification across multi-visit and timestamp-rich records, leaving the reconstruction of structured symptom trajectories from individual anchor-sparse reports largely unaddre...
  </details>

- **2026-08-13** — Habib Ammari, Yat Tin Chow, Fuqun Han — [Scattering by a medium with self-similar or fractal structure](http://arxiv.org/abs/2608.12728v1)
  <details><summary>📄 Abstract</summary>
  We develop a topological framework for wave scattering by a medium with self-similar or prefractal geometry. Physical scaling identities motivate an auxiliary boundary-integral model that is periodic in logarithmic scale, and the Bloch-Floquet-Zak transform fiberizes its interscale coupling. For sufficiently small, well-separated components, equilibrium densities define a computable finite-dimensional projected matrix, while Riesz projections select the corresponding invariant spectral subspace ...
  </details>

- **2026-08-13** — Abdul Mueez, Yogesh S. Rawat, Shruti Vyas — [A Generative Approach for Improving Multi-Label Defect Classification in Photovoltaic Modules](http://arxiv.org/abs/2608.12725v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of multi-label defect classification in electroluminescence (EL) images of photovoltaic (PV) cells. Training models on images where multiple defects co-occur creates learning ambiguity, making it difficult to disentangle visual features for specific defect types, a problem compounded by the scarcity of examples for individual classes. To tackle this, we introduce Generative Defect Isolation (GDI), utilizing the LaMa inpainting model with Fast Fourier Convolutio...
  </details>

- **2026-08-13** — Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi — [ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models](http://arxiv.org/abs/2608.13438v1)
  <details><summary>📄 Abstract</summary>
  Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon conseque...
  </details>

- **2026-08-13** — Charles Koll, Houssam Abbas — [Runtime Monitoring of Distributed Cyber-Physical Systems Without a Global Clock](http://arxiv.org/abs/2608.13486v1)
  <details><summary>📄 Abstract</summary>
  We give the first theoretical characterization, and the first algorithm, for continuous monitoring of a distributed Cyber-Physical System (CPS) against a dense-time temporal logic specification. A distributed CPS is composed of multiple agents, each with a local clock; these clocks drift from each other, so there is no well-defined global time. When monitoring such a system's output signal against a temporal logic specification, it is not evident how to interpret the temporal constraints of the ...
  </details>

- **2026-08-13** — Paul Savala — [Jointly Predicting Courses and Grades Using a Transformer-Based Model](http://arxiv.org/abs/2608.13409v1)
  <details><summary>📄 Abstract</summary>
  Existing predictive models in learning analytics often treat student academic history as a simple sequence, overlooking the concurrent nature of courses taken within a semester. This simplification can lead to inaccurate performance predictions, particularly for students with heavy or challenging course loads. This paper introduces a TRansformer for Academic Course-grade Estimation (TRACE) that addresses this limitation by jointly predicting both the set of courses a student will take and their ...
  </details>

- **2026-08-13** — Alexander Bräuer, Benjamin Cauchi, Nils Strodthoff — [Foundation models for movement data: Are they ready for prime-time?](http://arxiv.org/abs/2608.13316v1)
  <details><summary>📄 Abstract</summary>
  Foundation models (FMs) trained on large-scale accelerometer data have been proposed as general-purpose feature extractors for health monitoring, but systematic evidence of their advantages is lacking. We present the first comprehensive evaluation of four open-source accelerometer FMs against supervised baselines covering 19 tasks across the domains of activity recognition including activities of daily living, clinical monitoring, and physiological inference. We find task-dependent performance r...
  </details>

- **2026-08-13** — Timilehin B. Aderinola, Ilaria D'Ascanio, Luca Palmerini et al. — [Beyond Simulated Benchmarks: Evaluating Motion Representations for Fall Detection Under Real-World Data Scarcity](http://arxiv.org/abs/2608.13197v1)
  <details><summary>📄 Abstract</summary>
  Falls are a major health concern for older adults, and wearable sensors have been widely explored for detecting falls and enabling timely intervention. However, real-world falls are extremely rare: collecting 100 of them requires an estimated 100,000 days of monitoring, resulting in severely limited labelled data for training machine learning models. Consequently, many approaches rely on simulated datasets, often reporting high laboratory performance but limited real-world generalisation. We pre...
  </details>

- **2026-08-13** — Sam Mao — [Explanatory Engagement Under Rare Anomalous Failure: Asymptotic Rarity in Model Behavior (or: The Asymptotic AI)](http://arxiv.org/abs/2608.13063v1)
  <details><summary>📄 Abstract</summary>
  Prior work on LLM behavior under anomalous conditions asks whether a model notices anomalies. We ask a narrower question: once a model sits in a workflow with a low, controllable failure rate, does its explanatory engagement - length, specificity, self-reported confidence - change as failure grows asymptotically rarer? We built a local, zero-cost harness on three open-weight models (qwen3:8b, llama3.1:8b, mistral:7b) running a repeated tool-call task where one call fails at probability p, swept ...
  </details>

- **2026-08-12** — Justin Zhao, Himaghna Bhattacharjee, Hannah Korevaar et al. — [Jagged Judges: Epistemic Stability Under Silence, Pressure, and Persistence](http://arxiv.org/abs/2608.12645v1)
  <details><summary>📄 Abstract</summary>
  LLM judges have become central infrastructure for model evaluations, online grading, and reward modeling. Judges are typically validated by accuracy on golden data, but accuracy says little about whether they are stable under re-prompting, challenge, or sustained pushback. We introduce the \emph{Wiggle Framework}, a unified stress test for epistemic stability in LLM judges. The framework decomposes judge robustness along three dimensions: Mechanical Consistency (stability under re-prompting and ...
  </details>

- **2026-08-12** — Haifan Gong, Shiyu Chen, Bodong Wang et al. — [Auditable agentic AI for evidence-grounded thyroid ultrasound diagnosis and reporting](http://arxiv.org/abs/2608.12590v1)
  <details><summary>📄 Abstract</summary>
  Thyroid ultrasound diagnosis requires coordinated lesion localization, measurement, risk stratification and reporting, yet most AI systems address these tasks in isolation and provide limited support for clinical review. We present ThyroidXAgent, a clinician-interactive agentic AI system that coordinates specialized diagnostic tools and stores their outputs as an auditable case-level evidence record. The system was developed using OpenThyroidDB, a multicentre, multitask resource integrating appr...
  </details>

- **2026-08-12** — Congchao Wang, Diwakar Singh, Qiaozi Gao et al. — [Reasoning Jury: Multi-Model Consensus for Evaluating Reasoning Traces](http://arxiv.org/abs/2608.12585v1)
  <details><summary>📄 Abstract</summary>
  Improving reasoning LLMs requires the ability to judge the quality of long reasoning traces for effective reasoning data curation, strong training signals during reinforcement learning, and an in-depth understanding of reasoning behaviors during model performance evaluation. Additionally, surfacing reasoning mistakes that the model makes would enable improving the model's performance at runtime through providing feedback. Due to the difficulty of this complex task on long reasoning traces, singl...
  </details>

- **2026-08-12** — Xiyuan Yang, Sheikh Sarwar, Jingru Cheng et al. — [Scaling Automatic Research Agents via World Models](http://arxiv.org/abs/2608.12564v1)
  <details><summary>📄 Abstract</summary>
  Automating empirical research is a long-standing direction of AI. Recent automatic research (AutoResearch) agents bring this goal within reach, as modern LLMs show the capability to independently implement solutions and learn from the execution outcomes. Behind these gains, post-training (especially RL) plays a central role. In this paper, we identify a fundamental tension when scaling RL for these agents: the two components of every AutoResearch trajectory (agent generation and environment exec...
  </details>

- **2026-08-12** — Varun Rai, Pavan Kumar J, Sujith Pulikodan et al. — [Evaluating Pre-trained Speech Encoders for Spontaneous Speech Detection and Out of Domain Synthetic Speech Generalisation in Indic Languages](http://arxiv.org/abs/2608.12536v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based models have shown strong accuracy in distinguishing spontaneous from scripted speech and natural from synthetic speech, but these results are established on a narrow set of well-resourced language benchmarks and have not been extended across Indic languages, nor has embedding geometry been used to explain encoder behaviour or deepfake generalisation failure. We address these gaps by evaluating five frozen transformer encoders, AST, Vaani-FastConformer, Wav2vec2, Whisper and BEA...
  </details>

- **2026-08-12** — Aofan Liu, Shiyuan Song, Yiyan Qi — [$\varepsilon$-MemEvo: Adaptive Cross-Task Memory Transfer for LLM Program Evolution](http://arxiv.org/abs/2608.12522v1)
  <details><summary>📄 Abstract</summary>
  LLM-based program evolution systems such as FunSearch and AlphaEvolve have shown strong ability to discover novel algorithms, but typically optimize each task in isolation, discarding search experience after completion. We introduce $\varepsilon$-MemEvo, a framework for cross-task knowledge transfer in LLM program evolution. $\varepsilon$-MemEvo stores prior experience as task-agnostic tactic memories: compact natural-language summaries of successful algorithmic strategies rather than raw code, ...
  </details>

- **2026-08-12** — Vladyslava Rudas, Dmytro Kuzmenko — [Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?](http://arxiv.org/abs/2608.12515v1)
  <details><summary>📄 Abstract</summary>
  Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning. We evaluate three opensource vision-language models (VLMs) (\textit{InternVL}, \textit{Qwen-VL}, and \textit{SmolVLM}) on the classification of egocentric robot images into four danger levels, comparing three prompting strategies and two rounds of QLoRA fine-tuning against a stratified random baseline. Without fine-tunin...
  </details>

- **2026-08-12** — Guodong Xu — [Governed Persistent Memory: Source-Bound State Semantics and Fail-Closed Release for Long-Horizon Agents](http://arxiv.org/abs/2608.12476v1)
  <details><summary>📄 Abstract</summary>
  Long-term agent memory is usually treated as select--store--retrieve, but retrieval does not decide whether contradictory, superseded, retracted, deleted, or stale records may support an outgoing claim. We introduce Governed Persistent Memory (GPM), an auditable bitemporal state-transition model with source-bound admission, derived lifecycle state, current public barriers, and fail-closed structured release. Five executable clauses cover ledger integrity, source binding, conflict isolation, non-...
  </details>

- **2026-08-12** — Olivia Curtis, Aidan J. Rowland, Jason T. Wright et al. — [The Ĝ Infrared Search for Extraterrestrial Civilizations with Large Energy Supplies. V. When Galaxies Glow with Industry](http://arxiv.org/abs/2608.12458v1)
  <details><summary>📄 Abstract</summary>
  We present the most robust stellar population synthesis (SPS)-based search for galaxy-spanning technological waste heat to date, applied to 129 nearby galaxies spanning a wide range of spectral energy distribution (SED) types, including ultraluminous IR galaxies and MIR-luminous active galactic nuclei (AGN). We incorporate the AGENT Dyson sphere formalism into the Flexible Stellar Population Synthesis code at the stellar population level, so nebular and dust emission respond self-consistently to...
  </details>

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

- **2026-08-11** — Ted Kwartler, Alan Aqrawi, Arian Abbasi — [AI Guardrail Survival under Single-Cycle Agentic Self-Summarization](http://arxiv.org/abs/2608.11392v2)
  <details><summary>📄 Abstract</summary>
  Long-running agents periodically compact their context, replacing the transcript with a model-generated summary. Recent work shows that dropping a standing safety constraint during compaction drives behavioral violations across many models (Governance Decay; Chen, 2026). We ask a finer question: under a single compaction cycle, how is a safety rule lost, and what does that imply for detection and evaluation? Our central finding is that a presence check is not a safety check: when compaction does...
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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 48 papers

- **2026-08-14** — Taenyun Kim, Edyta Bogucka, Daniele Quercia — [Participatory Moral AI Is Not Neutral: The Invisible Hand of Developers](http://arxiv.org/abs/2608.14522v1)
  <details><summary>📄 Abstract</summary>
  As AI systems make more morally loaded decisions across society, one response has been moral preference elicitation. In this approach, researchers poll participants on hypothetical dilemmas and use the aggregated votes to train a policy that an AI model then applies at scale. Before any vote is cast, developers make three key choices in the moral AI elicitation pipeline: feature scoping, voter sampling, and question framing. In other words, they decide which features go to a vote, which voters t...
  </details>

- **2026-08-14** — Darakshan Rashid, Raza Imam, Ufaq Khan et al. — [On the Robustness of Temporal Vision-Language Models for Surgical Endoscopy Videos](http://arxiv.org/abs/2608.14262v1)
  <details><summary>📄 Abstract</summary>
  Temporal vision-language models (TVLMs) offer a reusable, prompt-based interface for surgical video understanding, yet, their robustness under clinically realistic acquisition artifacts in endoscopy remains insufficiently characterized. In practice, degradations such as defocus, haze, motion blur, noise, cautery smoke, and packet loss introduce structured distribution shifts which may compromise video-text alignment. We study the robustness of temporal VLMs under such shifts caused by corruption...
  </details>

- **2026-08-14** — Nan Li, Li Zhou, Haijun Wang et al. — [Personalized Digital Semantic Communication for Image Transmission with Vision-Language Models](http://arxiv.org/abs/2608.14260v1)
  <details><summary>📄 Abstract</summary>
  Semantic communication (SC) enables bandwidth-efficient wireless image transmission, but most existing SC schemes are user-agnostic and ignore receiver-dependent semantics. To address this issue, we propose a personalized digital semantic communication (PDSC) framework that integrates a vision-language model (VLM)-based semantic encoder with a latent diffusion model (LDM)-based semantic decoder. Specifically, the semantic encoder extracts source-aware personalized semantic tokens from both the s...
  </details>

- **2026-08-14** — Jeongwan Shin, Jaehyeon Kim, Donguk Ko et al. — [Can Language Models Understand mmWave Data? Benchmarking Large Language Models for mmWave Radar-Based Human Understanding](http://arxiv.org/abs/2608.14179v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown remarkable reasoning and generative capabilities, motivating their use as universal reasoning engines for perception. While modern approaches such as vision-language models (VLMs) have attempted to incorporate reasoning capabilities into visual sensing, the integration of LLMs with the millimeter-wave (mmWave) modality-despite its unique advantages under low light and occlusion-remains largely unexplored. The principal bottlenecks stem from the scarcity of...
  </details>

- **2026-08-14** — Yanbo Ding, Yijia Fan, Caihua Shan et al. — [Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation](http://arxiv.org/abs/2608.14043v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically s...
  </details>

- **2026-08-14** — Mathew Varghese — [Content Based Video Narration of Gameplay with Vision Language Models](http://arxiv.org/abs/2608.14016v1)
  <details><summary>📄 Abstract</summary>
  Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled f...
  </details>

- **2026-08-13** — Dananjay Srinivas, Saksham Khatwani, Maria Pacheco — [Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent Specificity](http://arxiv.org/abs/2608.13484v1)
  <details><summary>📄 Abstract</summary>
  When asked about entities outside their knowledge boundary, LLMs routinely fabricate plausible-sounding details rather than backing off to safer, more general claims. We frame this failure through a Gricean lens: a cooperative speaker who is uncertain about a referent retreats up the specificity hierarchy, trading informativeness for truthfulness. We ask whether LLMs have the ingredients to perform this retreat. Using a T-REx-based benchmark that varies entity familiarity and referent specificit...
  </details>

- **2026-08-13** — Yusen Tan, Yixuan Chen, Zheng Fang et al. — [Simulation-to-real transfer learning for infrared spectroscopic chemical sensing and analysis from molecules to complex samples](http://arxiv.org/abs/2608.13341v1)
  <details><summary>📄 Abstract</summary>
  Infrared (IR) spectroscopy is widely used for chemical sensing, but extracting reliable chemical information from spectra remains challenging. Conventional interpretation is labor-intensive, relies on prior knowledge and reference spectra, and is difficult to scale, whereas most machine-learning methods are tailored to individual tasks or datasets, require large labeled training sets, and transfer poorly across analytical objectives and experimental datasets. Here we introduce UltraIR, a foundat...
  </details>

- **2026-08-13** — Yanwen Peng, Delvin Ce Zhang, Xi Wang et al. — [StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems](http://arxiv.org/abs/2608.13317v1)
  <details><summary>📄 Abstract</summary>
  Large language model based multi-agent systems usually communicate in text, i.e., using discrete tokens. However, text introduces a discrete bottleneck. Converting the sender's continuous hidden states into discrete tokens discards information that token identities alone cannot capture. Recent work proposes latent communication as an alternative, where agents transmit hidden representations directly without converting them to text. However, existing latent methods either inject working memory la...
  </details>

- **2026-08-13** — Wafa Al Ghallabi, Ritesh Thawkar, Sara Ghaboura et al. — [How Good are Foundation Models in Longitudinal MRI Disease Progression Reasoning?](http://arxiv.org/abs/2608.13309v1)
  <details><summary>📄 Abstract</summary>
  Magnetic Resonance Imaging (MRI) interpretation is fundamental to clinical decision-making, requiring radiologists to integrate multi-view anatomical planes across sequential timepoints while precisely localizing interval changes. However, existing vision-language benchmarks remain confined to single-timepoint, single-view interpretation, failing to capture the temporal-spatial reasoning essential to radiologic practice. We introduce the Time-Aware Multi-View MRI Benchmark, an evaluation framewo...
  </details>

- **2026-08-13** — Hongjie Xia, Yiding Liu, Yifan Hu et al. — [Into the ORBIT for Time Series: Training Regimes for Foundation Models](http://arxiv.org/abs/2608.13262v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) have advanced primarily through architectural innovation, while training regimes for large-scale heterogeneous corpora remain under-explored. As a result, pre-training distributions are often poorly controlled with respect to domain imbalance, context requirements, prediction horizons, and missingness. We introduce ORBIT (Omni-Range Bootstrap Incremental Training), a training paradigm that makes this distribution explicit and controllable. ORBIT combines Boo...
  </details>

- **2026-08-13** — Long Hoang Nguyen, Brice Valentin Kok-Shun, Guangyu Du et al. — [Follow the Norm: Accounting for Fine-Tuning and Prompt Effects on Model Rationales](http://arxiv.org/abs/2608.13250v1)
  <details><summary>📄 Abstract</summary>
  Normative datasets are often used to train and align AI systems, but the norms they contain can function as action-guiding patterns rather than neutral moral knowledge. We propose treating the AI system as a proxy actor and test whether dataset-level norms can shift it away from its baseline safety behavior when it faces high-conflict dilemmas. We make three contributions. First, we demonstrate in controlled experiments that norm-breaking fine-tuning yields norm-divergent actions justified by se...
  </details>

- **2026-08-13** — Yilin Wang, Yuchun Fan, Weidong Bao et al. — [Better Decomposition, Free Aggregation: A Synthesizer-Folding Framework for Multilingual Multi-Hop Question Answering](http://arxiv.org/abs/2608.13160v1)
  <details><summary>📄 Abstract</summary>
  Multilingual retrieval-augmented generation (mRAG) equips large language models with access to globally distributed external knowledge for complex multilingual question answering. Recent approaches either translate retrieved documents into English or the query language to bridge the cross-lingual semantic gap, or decompose a complex query into sub-questions and aggregate the intermediate reasoning process. However, both lines of work suffer from two limitations. First, one-size-fits-all translat...
  </details>

- **2026-08-13** — Chenrun Wang, Mingxuan Zhu, Tiancheng Huang et al. — [LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation](http://arxiv.org/abs/2608.13136v1)
  <details><summary>📄 Abstract</summary>
  With the rapid advancement of large language models (LLMs), research idea generation has attracted increasing attention. Existing approaches enable LLMs to retrieve relevant literature and propose novel ideas for research areas. However, current evaluation practices for idea generation remain fragmented and lack objective standards, often relying on direct LLM scoring, which limits their ability to provide unified and reliable assessments across a coherent distribution of generated ideas. To add...
  </details>

- **2026-08-13** — Lucia Malíčková — [Behavioral Reprogramming of Open-Weights Models: Cognitive Plasticity and Alignment Bounds](http://arxiv.org/abs/2608.13069v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are predominantly aligned to function as passive, sycophantic assistants. We challenge this default paradigm by empirically evaluating the cognitive plasticity of open-weight architectures when subjected to rigorous behavioral reprogramming. Our objective is to induce a proactive, Socratic conversational framework, characterized by high-frequency question generation under strictly constrained high-performance computing (HPC) conditions. Through a massively paralleliz...
  </details>

- **2026-08-13** — Jiale Cui, Yueyao Yuan, Kaixi Zhong et al. — [ARAC: Benchmarking Auto-Research's Alignment and Completeness on End-to-End Researchs](http://arxiv.org/abs/2608.12788v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of Auto-Research has surfaced a fundamental evaluation challenge: how can we measure the alignment, logical coherence, and evolutionary completeness of its research trajectory with human research behavior? We propose Auto-Research's Alignment and Completeness, ARAC-Bench: a Researcher-Mimicking Evaluation framework that shifts the objective from matching final answers to reproducing high-quality human research processes. The framework operates through two synergistic compon...
  </details>

- **2026-08-13** — Junyi Hu, Tian Bai, Fengyi Wu et al. — [Scaling Representation Diversity: Modulated Attention and Reconstructive Regularization for Visual Grounding](http://arxiv.org/abs/2608.12748v1)
  <details><summary>📄 Abstract</summary>
  Referring Expression Comprehension (REC) is commonly studied under dataset-specific fine-tuning, resulting in specialist models with limited cross-dataset generalization. In this work, we revisit REC from the perspective of unified open-vocabulary grounding and identify representation degeneration as a key obstacle to scaling a single generalist model. To preserve representation diversity, we propose a holistic data-model co-design framework. Architecturally, we introduce the Modulated Attention...
  </details>

- **2026-08-13** — Zhi Qiao, Xintong Wu, Yichu He et al. — [Mr3D-VL: A generalist vision language foundation model for Multiparametric 3D Magnetic Resonance Imaging](http://arxiv.org/abs/2608.12689v1)
  <details><summary>📄 Abstract</summary>
  Multi-parametric magnetic resonance imaging (mpMRI) is a cornerstone for brain tumor diagnosis and treatment, yet current AI models face critical limitations: their lack of natural language interaction and interpretability impedes spatial information integration and cross-modal reasoning required clinically. Key challenges arise from significant physical meaning differences across modalities, spatial misalignment due to scan intervals, and the need for complex multi-feature interpretation in tas...
  </details>

- **2026-08-13** — Danial Sharifrazi, Saadat Behzadi, Julakha Jahan Jui et al. — [The Role of Natural Language Understanding in Multimodal Video-Based Dengue Diagnosis](http://arxiv.org/abs/2608.12677v1)
  <details><summary>📄 Abstract</summary>
  Detecting infection-related behavioral changes in mosquitoes from video data is challenging because mosquitoes are small, move rapidly and irregularly, and are affected by environmental factors such as background, lighting, and shadows, which can make reliable feature extraction difficult. In this study, a YOLO- and Contrastive Language-Image Pre-training (CLIP)-based vision-language framework is proposed to classify mosquito flight frames of uninfected and Dengue virus serotype 2 (DENV2)-infect...
  </details>

- **2026-08-12** — Le Zhang, Ke Sun — [EgoCITE: Context-Augmented Indexing and Time-Aware Retrieval for Long-Horizon Egocentric Memory](http://arxiv.org/abs/2608.12627v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon egocentric memory transforms continuous first-person video and audio into a searchable record of past experiences. We demonstrate two bottlenecks in existing systems: indices built from context-poor captions are unreliable for agentic search, while retrieval ignores a question's temporal intent. To address both bottlenecks, we introduce EgoCITE (Egocentric Context-augmented Indexing and Time-aware Evidence retrieval), a long-horizon agentic memory framework for egocentric QA. EgoCIT...
  </details>

- **2026-08-12** — Fang Guo, Qi Zhu, Rongcan Pei et al. — [Sci-Surf: Navigating Scientific Literature Discovery through Human Feedback and Intelligent Summarization](http://arxiv.org/abs/2608.11973v2)
  <details><summary>📄 Abstract</summary>
  The rapid growth of scientific publications makes it increasingly difficult for researchers to identify relevant new studies and effectively comprehend them. Existing academic discovery platforms typically rely on static topic subscriptions or embedding-based similarity and provide only abstracts or short summaries, offering limited support for nuanced intent modeling and in-depth paper summarization. We present Sci-Surf, an intent-centric knowledge discovery system that integrates feedback-driv...
  </details>

- **2026-08-12** — Thomas A. Pollak, Hamilton Morrin, Murray Shanahan — [Philosophical vertigo with artificial intelligence](http://arxiv.org/abs/2608.11955v2)
  <details><summary>📄 Abstract</summary>
  Large language models are already adept at engaging users in long, emotionally salient conversations across ordinary and existential domains. They are also capable of inducing a potent sense of connection with a human-like entity, even when the user knows their interlocutor is artificial. For some users, these conversations can unsettle assumptions about mind, reality, agency and authority, producing forms of ontological shock and epistemic destabilisation in which inherited criteria become newl...
  </details>

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

- **2026-08-11** — Nils Leutenegger — [Evaluation Resolution Confounds Learning-Rule Comparisons in Model-Brain RSA of Early Visual Cortex](http://arxiv.org/abs/2608.12408v1)
  <details><summary>📄 Abstract</summary>
  Representational similarity analysis (RSA) is increasingly used to ask which learning rules give convolutional networks brain-like representations. Because biologically plausible rules such as feedback alignment, predictive coding and STDP do not scale, studies that include them train small networks on small images (typically 32x32 CIFAR) and then compare them to brain responses modeled at much higher resolution. We find that a common result in this setting, that untrained or locally trained net...
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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

- **2026-08-14** — Md Kamrul Islam, Tiphaine Henry, Mattia Salnitri et al. — [A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models](http://arxiv.org/abs/2608.14370v1)
  <details><summary>📄 Abstract</summary>
  The modelling and analysis of secure business processes require the incorporation of security annotations into process models. Although BPMN extensions, including SecBPMN2, exist for this purpose, the derivation of accurate and complete security annotations from natural-language specifications remains a manual, expert-intensive, and error-prone task. This paper presents a hybrid framework that takes a BPMN process model and a security requirements document as input and automatically generates se...
  </details>

- **2026-08-14** — Yijiao Zhang, Hongzhe Li — [Generation-Powered Inference for Distribution-Valued Outcomes](http://arxiv.org/abs/2608.14542v1)
  <details><summary>📄 Abstract</summary>
  Modern generative models increasingly produce distribution-valued outputs, such as predicted cellular responses to genetic perturbations in single-cell genomics. While these models provide valuable auxiliary information, they are inherently imperfect, creating a need for statistical methods that leverage their predictions without relying on their correctness. We propose generation-powered inference (GPI), a general framework for improving inference on distribution-valued parameters using auxilia...
  </details>

- **2026-08-14** — Zhelun Wu — [Split the Labor: Separating Evidence Interpretation from Decision Aggregation](http://arxiv.org/abs/2608.14509v1)
  <details><summary>📄 Abstract</summary>
  Systems that ask a language model to reach a conclusion from many sources usually concatenate them into one prompt. This conflates two operations with different requirements. Interpreting a source rewards capacity and context. Combining interpretations rewards fixed arithmetic, comparability across instances, and the option to return nothing. Once separated, the design problem becomes the interface between them. We propose a four-field evidence tuple (hypothesis, reliability bucket, rationale, p...
  </details>

- **2026-08-14** — Yiderigun Borjigin, Alexander Hermann, Christian Cyron et al. — [AnchorBench: A Multi-Pathway Benchmark for the Anchoring Effect in LLMs](http://arxiv.org/abs/2608.14320v1)
  <details><summary>📄 Abstract</summary>
  The anchoring effect is a cognitive bias in which an initial reference value shifts a later judgment toward itself. This effect is well established in human judgment and decision-making, and recent work suggests that large language models (LLMs) exhibit similar behavior. However, existing work on anchoring in LLMs typically evaluates only a narrow set of anchor pathways and rarely distinguishes irrelevant from plausible anchors. We introduce AnchorBench, a benchmark for the anchoring effect in L...
  </details>

- **2026-08-14** — Anandaroop Ray — [Extending Occam's inversion with lasso fusion, overcomplete dictionaries, and isotropic total variation regularisation](http://arxiv.org/abs/2608.14225v1)
  <details><summary>📄 Abstract</summary>
  Occam's inversion is a robust algorithm to perform nonlinear geophysical inversion. It provides the smoothest model within observation noise, thereby discouraging geological overinterpretation. While Occam originally penalised l2 model roughness, l1 can be used to provide models that are visually sharp. However, l1 regularised geophysical inversion has diverged from the larger body of statistics and imaging literature. For example, l1 regularisation with a difference operator (i.e., total variat...
  </details>

- **2026-08-14** — Hengzhe Zhang, Qi Chen, Bing Xue et al. — [Adaptive Protection for Evolutionary Feature Construction in Symbolic Regression with Application to Credit Classification](http://arxiv.org/abs/2608.14209v1)
  <details><summary>📄 Abstract</summary>
  Evolutionary feature construction has shown strong promise in symbolic regression by automatically discovering informative transformations of input features that enhance a simple base learner. However, existing approaches often lack explicit mechanisms to preserve important constructed features discovered during evolution, and valuable genetic material can be lost when genetic operators disrupt effective features. This paper introduces an adaptive protection mechanism that leverages feature impo...
  </details>

- **2026-08-14** — Arne Kröger, Ralf Buschermöhle, Wilhelm Hasselbring et al. — [Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground](http://arxiv.org/abs/2608.14122v1)
  <details><summary>📄 Abstract</summary>
  Production scheduling in complex manufacturing environments is challenging when sequence-dependent setup times, stochastic disturbances, and due-date constraints must be addressed simultaneously. While reinforcement learning (RL) methods have shown promising results in research, most studies rely on simplified benchmark processes, limiting their industrial relevance. This paper demonstrates the applicability of RL-based scheduling in an industry-inspired coating process that reflects practical c...
  </details>

- **2026-08-14** — Juli Huang, Hannah Clay, Sajjad Beygi et al. — [MACS: A Hybrid Multi-Agent Framework for Reliable Conversational E-Commerce Recommendation](http://arxiv.org/abs/2608.14068v1)
  <details><summary>📄 Abstract</summary>
  Conversational recommendation for e-commerce is increasingly mediated by large language models (LLMs), yet many real-world deployments operate under a stricter requirement: recommendations must be drawn only from a merchant's fixed catalog, without web search or unsupported product claims. In this setting, the main challenge is reliability under hard constraints: the system must satisfy user requirements, remain grounded in available inventory, and preserve preferences across multiple conversati...
  </details>

- **2026-08-14** — Yi Ding, Yanzhao Yu, Xili Dai et al. — [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](http://arxiv.org/abs/2608.14047v1)
  <details><summary>📄 Abstract</summary>
  This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability...
  </details>

- **2026-08-13** — Daniel Perkins, John Squires, Janou Milligan et al. — [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](http://arxiv.org/abs/2608.13463v1)
  <details><summary>📄 Abstract</summary>
  Modern image classification models excel when trained on single task-specific datasets but often struggle to generalize across domains and difficulty levels. We propose ARMDIL, an Adaptive Router for Multi-Domain Image classification with LLMs. ARMDIL is an ensemble that uses a multimodal large language model (MLLM) agent to dynamically route each image to the most suitable vision backbone. Our diverse ensemble employs convolutional neural networks (ResNets), self-supervised representation learn...
  </details>

- **2026-08-13** — Zhe Ye, Hantao Lou, Yuechun Sun et al. — [Vero: Can AI Agents Build Formally Verified Software Repositories?](http://arxiv.org/abs/2608.13522v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly used for programming, but do not provide any guarantee on the correctness of generated code. Verified code generation, in which an agent produces both an implementation and a machine-checked proof of its specification, offers a stronger path toward trustworthy AI-generated software. Existing benchmarks in this direction either focus on individual functions or only evaluate proof generation with provided implementations. It is still an open question whether agents can m...
  </details>

- **2026-08-13** — Anna Sterna, Kacper Dudzic, Karolina Drożdż et al. — [How LLMs Respond to Escalating Delusions: Four Longitudinal Trajectories of Model Behavior](http://arxiv.org/abs/2608.13017v1)
  <details><summary>📄 Abstract</summary>
  The widespread use of LLMs among psychiatric populations has raised concerns regarding their safety and potential iatrogenic impact in the context of AI psychosis. While growing literature conceptualizes AI psychosis and documents case studies, empirical evidence tracing AI-exacerbated psychotic processes remains scarce. We propose and test a longitudinal qualitative evaluation design, supported by automated metrics, to assess mainstream LLMs' potential to exacerbate psychosis. Fifteen widely us...
  </details>

- **2026-08-13** — Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury — [HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA](http://arxiv.org/abs/2608.13004v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-base question answering (KBQA) systems rely on effective retrieval and reasoning mechanisms to generate accurate answers from external knowledge sources. However, developing reliable KBQA systems for low-resource languages such as Bangla remains challenging due to limited retrieval-focused research, scarce language resources, and difficulties in grounding generated responses in external knowledge. In this work, we propose HybridRAG-BN, a retrieval-augmented framework for Bangla KBQA th...
  </details>

- **2026-08-13** — Kwangyik Jung, Eungchang Mason Lee, Taekjun Oh et al. — [ASPIRE-VINS: Adaptive Spline-based Visual-inertial Navigation System With Robust 3D Measurement Residuals](http://arxiv.org/abs/2608.12840v1)
  <details><summary>📄 Abstract</summary>
  Visual-inertial navigation systems estimate six-degree-of-freedom motion by fusing visual and inertial data. Modern discrete-time methods with IMU preintegration provide strong accuracy and efficiency, but keyframe-based representations can be less flexible when residuals must be evaluated at arbitrary timestamps or when motion-dependent temporal resolution is needed. Continuous-time splines address this issue by representing the trajectory as a smooth temporal function, but uniformly spaced kno...
  </details>

- **2026-08-13** — Qi Zhao, Qirui Li, Hanlin Tang et al. — [SCOPE: Subspace Clustering with Online Per-Head Top-K Estimation for Sparse Video Attention](http://arxiv.org/abs/2608.12780v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) incur quadratic self-attention cost over spatiotemporal tokens. Existing training-free sparse attention methods often construct sparse masks from block-level or cluster-level proxy scores, which can obscure fine-grained differences among keys and miss high contribution keys under aggressive sparsity. Moreover, such proxy scores may yield overly concentrated softmax distributions, causing Top-$p$ to retain too few keys for some query clusters. Although a fixed Top-$k...
  </details>

- **2026-08-13** — Haolong Chen, Zhengyuan Xin, Liang Zhang et al. — [Error-Aware Reverse Auction Mechanism for Large Language Model Routing](http://arxiv.org/abs/2608.12719v1)
  <details><summary>📄 Abstract</summary>
  Routing each query to a cost-effective large language model (LLM) is critical for balancing quality and cost, yet most routers rely on a centralized task center to predict model performance, creating an information-risk mismatch and a scalability bottleneck as the model pool grows. We propose a market-based routing paradigm that shifts ex-ante prediction to LLM providers via a reverse auction, where providers bid with self-predicted success probabilities and execution costs. To account for inher...
  </details>

- **2026-08-13** — Lei Bai, Jiaqi Cao, Chiyu Chen et al. — [Intern-S2-Preview: Scientific Agentic Foundation Model](http://arxiv.org/abs/2608.13505v1)
  <details><summary>📄 Abstract</summary>
  Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific do...
  </details>

- **2026-08-13** — Yanming Yang, Chenxi Song, Ping Wang et al. — [GS$^{2}$CI: Robust Gaussian Splatting For Snapshot Compressive Imaging via Large Vision Model Priors](http://arxiv.org/abs/2608.13502v1)
  <details><summary>📄 Abstract</summary>
  Snapshot Compressive Imaging (SCI) offers an efficient solution for high-speed video acquisition and, under exposure-time camera--scene relative motion, multi-view scene capture by compressing temporal or spatial information into a single 2D measurement. While recent studies have explored SCI for 3D scene reconstruction, existing methods struggle with significant challenges due to information loss, limited viewpoint diversity, and the computational burden of jointly optimizing 3D representations...
  </details>

- **2026-08-13** — Mostafa Mansour, Mansoura Oumennana — [Quantum correlations and Basis-Independent Coherence Distribution in Two Gravitational Cat States](http://arxiv.org/abs/2608.13493v1)
  <details><summary>📄 Abstract</summary>
  We study the distribution of quantum correlations and basis-independent coherence in a pair of massive particles confined in a double-well potential and coupled through their mutual Newtonian gravitational interaction. Non-classical correlations are characterized using Bures distance of entanglement and quantum discord, while coherence is quantified through the square root of the quantum Jensen--Shannon divergence (QJSD) from the maximally mixed state, yielding a measure that is invariant under ...
  </details>

- **2026-08-13** — Zixuan Lan, Yanhong Li, Jiawei Zhou — [Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for LLM Inference](http://arxiv.org/abs/2608.13426v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based language models achieve strong performance but incur substantial inference cost due to repeated high-dimensional matrix multiplications. We propose Reduced Matrix Multiplication (RMM), a training-free, input-adaptive inference method that reduces Transformer matrix products by selecting informative slices along their contraction dimensions, without modifying model weights. Under a simple retention-ratio control, RMM provides a smooth and predictable accuracy-efficiency trade-of...
  </details>

- **2026-08-13** — Teng Lin, Yuyu Luo, Nan Tang — [Structure then Query: Enabling Precise Analytical Queries over Unstructured Documents](http://arxiv.org/abs/2608.13384v1)
  <details><summary>📄 Abstract</summary>
  Unstructured documents constitute the majority of enterprise and web data. With the rapid development of large language models(LLMs), researchers have started to build data systems that analyze unstructured textual documents like operating on databases. However, because mainstream retrieval methods still relies on fuzzy matching based on vector similarity, accurately obtaining information and performing structured analysis and reasoning remains a major challenge. To address these limitations, An...
  </details>

- **2026-08-13** — Renlei Jiang, Xiaoyu Zhang, Chuanhou Gao et al. — [Input-to-state stability of chemical reaction networks with application to molecular computation](http://arxiv.org/abs/2608.13302v1)
  <details><summary>📄 Abstract</summary>
  In biological reaction systems, reaction rates may vary over time due to environmental fluctuations, regulation, or coupling with other reaction modules. Input-to-state stability (ISS) provides a useful tool for analyzing the robustness of time-varying chemical reaction networks (CRNs). Existing ISS results for CRNs typically rely on restrictive structural assumptions, such as zero deficiency, a single linkage class, or weak reversibility. This paper makes two main contributions. First, we estab...
  </details>

- **2026-08-13** — Paul Osemudiame Oamen, Owusu-Banahene Osei, Ananya Mukherjee et al. — [How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures](http://arxiv.org/abs/2608.13267v1)
  <details><summary>📄 Abstract</summary>
  Existing vision-language model (VLM) benchmarks emphasize perception and reasoning accuracy (how well VLMs describe and reason about what they see in an image), with limited attention to behavioral reliability under uncertainty (how they behave when visual evidence is missing or misleading). We introduce SciFigBench, a diagnostic VLM benchmark for scientific figure understanding that jointly evaluates perception, reasoning, and behavioral reliability under uncertainty. It contains 250 figures wi...
  </details>

- **2026-08-13** — Berk Hadzhamolla, Alexander Johannes Stasik, Signe Riemer-Sørensen — [Virtual Temperature Sensors in Power Transformers Using Neural Ordinary Differential Equations](http://arxiv.org/abs/2608.13260v1)
  <details><summary>📄 Abstract</summary>
  Accurate modeling and forecasting of power transformer thermal behavior are critical for reliability, asset lifetime, and optimized power system operation. Numerical approaches such as finite element methods (FEM) and computational fluid dynamics (CFD) offer high fidelity but are computationally expensive, require complex mesh generation, and are often impractical for real-time or large-scale applications, particularly when transformer geometries are unknown. Lumped-parameter thermal models are ...
  </details>

- **2026-08-13** — Peng Ling, Yingda Yin, Lingting Zhu et al. — [CoverPrune: Coverage-Driven Token Pruning for 3D VLMs via Optimal Transport](http://arxiv.org/abs/2608.13226v1)
  <details><summary>📄 Abstract</summary>
  While 3D Vision-Language Models (3D VLMs) have demonstrated remarkable spatial reasoning capabilities, they suffer from massive visual token counts that create severe computational bottlenecks during inference. Existing token pruning methods primarily rely on diversity-based selection, discarding similar tokens to maximize dispersion. However, in 3D environments, this approach frequently drops representative prototype tokens in favor of outliers, breaking the multi-view consistencies and geometr...
  </details>

- **2026-08-13** — Mallika Garg, Debashis Ghosh, Pyari Mohan Pradhan — [UniCon-Former: Unified Convolution Transformer is All You Need for Hand Gesture Recognition](http://arxiv.org/abs/2608.13217v1)
  <details><summary>📄 Abstract</summary>
  Convolutional Neural Networks (CNNs) capture local features efficiently but struggle with global context due to their limited receptive field. On the other hand, transformers effectively capture global dependencies through self-attention but suffer from high redundancy and computational costs. Thus, to leverage the advantages of both CNNs and transformers, we propose a unified model (UniCon-Former) that aims to provide robust and efficient performance on dynamic hand gesture recognition. The uni...
  </details>

- **2026-08-13** — Fnu Pramono, John Cai, Sourabh Kulkarni — [TRAPSBench: Vision-Language Models Encode but Fail to Express Epistemic Restraint](http://arxiv.org/abs/2608.13167v1)
  <details><summary>📄 Abstract</summary>
  When visual evidence is occluded or chaotic, models should abstain. In this paper, we show that Vision-Language Models (VLMs) can internally distinguish when abstention is required, but fail to express it anyway. We introduce TRAPSBench, a procedurally generated video benchmark of 1,404 matched physics pairs in which a single targeted change renders the outcome undeterminable from the visual evidence. Furthermore, we introduce Penalized Epistemic Calibration Score (PECS), a new robust metric tha...
  </details>

- **2026-08-13** — Jakub Peleška, Gustav Šír — [Incremental Evaluation and Training in Relational Deep Learning](http://arxiv.org/abs/2608.13023v1)
  <details><summary>📄 Abstract</summary>
  Relational Deep Learning (RDL) models multi-tabular databases as temporal heterogeneous graphs to enable end-to-end representation learning. However, prevailing RDL evaluation practices rely on static, single-episode dataset snapshots, overlooking the continuous, time-evolving nature of real-world databases. Consequently, current RDL benchmarks fail to capture how model performance changes as new data accumulates over time. To address this limitation, we introduce an incremental, multi-episode e...
  </details>

- **2026-08-13** — Fanyu Wang, Chetan Arora, Zhenping Xie et al. — [Requirements-Augmented Generation for Trustworthy Acceptance Testing of LLM-Based Software](http://arxiv.org/abs/2608.12970v1)
  <details><summary>📄 Abstract</summary>
  LLM-based software (LBS) integrates large language models as core components to deliver flexible, personalised responses. Unlike traditional software with deterministic outputs, LBSs exhibit context-dependent, stochastic behaviour that renders classical acceptance testing and test oracles insufficient: the same query may require fundamentally different responses depending on user personas and software context. This gap creates an urgent need for automated acceptance testing frameworks that auton...
  </details>

- **2026-08-13** — Ankita Joshi — [A Deep RL based Framework for Targeted White Matter Tractography](http://arxiv.org/abs/2608.12960v1)
  <details><summary>📄 Abstract</summary>
  Fiber tractography's ability to reconstruct the brain's structural pathways, has made it a crucial component of modern neuroimaging, enabling detailed, non-invasive mapping of structural connectivity and supporting a wide range of neurological research and clinical applications. However, despite its importance, tractography remains a challenging task due to the inherent complexity of white matter structure and its susceptibility to false positives, which can lead to the misrepresentation of crit...
  </details>

- **2026-08-13** — Palaash Goel, Ayan Sengupta, Akshay Nambi et al. — [Unifying Depth and Width Pruning for LLMs via Binary Knapsack Optimization](http://arxiv.org/abs/2608.12953v1)
  <details><summary>📄 Abstract</summary>
  Structured pruning is a promising approach for compressing large language models (LLMs), yet existing methods rely heavily on greedy heuristics that produce myopic decisions, and often fail to precisely meet target compression budgets. We present SNIPER, a two-stage structured pruning framework that solves a knapsack optimization over coarse-granularity components to yield conditionally optimal parameter allocations with respect to fixed importance estimates, followed by a fine-grained pruning s...
  </details>

- **2026-08-13** — Naresh Saha, Nirmoy Kumar Das, Ashoke Das et al. — [Phase Space Reorganization and Travelling Wave Emergence Driven by Non-Kerr Effects in Nonparaxial Optical Media](http://arxiv.org/abs/2608.12856v1)
  <details><summary>📄 Abstract</summary>
  In this article, the nonlinear Helmholtz equation with non-Kerr nonlinearity, such as self steepening and self frequency shift, is considered. A travelling wave transformation is applied, and the extended nonlinear Helmholtz equation is reduced to a Hamiltonian dynamical system. Then, the reduced Hamiltonian system is analyzed by classification of equilibrium points, phase space analysis, and the construction of exact wave solutions. The relationship between the reduced dynamical coefficients an...
  </details>

- **2026-08-13** — Wafa Shafqat, Mark Patterson, Steven N. Liss — [Knowledge Synthesis Review Framework: Task-Level Benchmarking of LLM-Based Systems for Multi-Source Evidence Synthesis](http://arxiv.org/abs/2608.12741v1)
  <details><summary>📄 Abstract</summary>
  Evidence in rapidly evolving fields is fragmented across academic studies, industry reports, policy documents, and media sources that differ in quality, structure, and purpose, making timely synthesis difficult. Large language models (LLMs) may accelerate this work, but their reliability across the distinct cognitive tasks of a review remains uncertain. We introduce the Knowledge Synthesis Review (KSR), a human-in-the-loop framework that decomposes evidence synthesis into screening, extraction, ...
  </details>

- **2026-08-13** — Canyang Wu, Jinrong Zhang, Xusheng He et al. — [VOS-Agent: The 1st Place Solution for the 8th LSVOS Challenge (MOSEv2 Track)](http://arxiv.org/abs/2608.12721v1)
  <details><summary>📄 Abstract</summary>
  Complex video object segmentation requires robust target propagation under severe occlusion, disappearance and reappearance. Although SAM3 provides strong promptable mask propagation, a uniform inference path remains unreliable for tiny targets with insufficient visual evidence and semantic-dominated targets whose identities depend on explicit attributes. To this end, we present VOS-Agent, a collaborative framework that retains SAM3 as the shared dense segmentation module and conditionally activ...
  </details>

- **2026-08-13** — Xiang Guan, Roger D. Newman-Norlund, Yong Yang et al. — [Perturbation-based Regional Interpretability through Subtraction Mapping (PRISM): naming-error dissociations in language models and post-stroke aphasia](http://arxiv.org/abs/2608.12717v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability of large language models lacks spatially resolved, falsifiable tools for testing whether internal components are specialized for distinct cognitive operations. We adapt subtraction analysis, the standard framework of human neuroimaging, from biological brains to perturbed transformers, and apply the same logic to both substrates in parallel. Building on the Brain-LLM Unified Model (BLUM), which showed that layer-perturbed LLaVA-1.6-Vicuna-13B error profiles match the...
  </details>

- **2026-08-12** — Mehdy Sedaghat Payam, Justin Quinn — [Novels generated by language models show compressed formal variation](http://arxiv.org/abs/2608.12630v1)
  <details><summary>📄 Abstract</summary>
  While large language models can generate entire novels, there is little information about the level of formal variation in their output over many generations. Rather than asking whether individual passages can be identified as AI-generated, this study asks whether repeated AI generation can produce the same range of diversity which is found across human corpora. This paper contrasts six corpora based on generation source and target style: twenty novels generated using GPT-5.5 Thinking in a ninet...
  </details>

- **2026-08-12** — Yi Wu, Zhimin Hu — [LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning](http://arxiv.org/abs/2608.12626v1)
  <details><summary>📄 Abstract</summary>
  Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals. In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps. This limitation leads to strategic drift, where localized decisions fail to sustain a coherent trajectory across reasoning. To address this, we introduce EpicStar, a framework that enables agents to learn memory as policy to tackle long-horizon r...
  </details>

- **2026-08-12** — Siheng Xiong, Ali Payani, Oguzhan Gungordu et al. — [DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution](http://arxiv.org/abs/2608.12486v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) cannot retain post-deployment experience without parameter updates. We introduce DIVE, a diversity-driven framework that enables frozen LLMs to improve by evolving persistent natural-language skills from task experience and verifier feedback. These skills encode reusable reasoning procedures, verification strategies, common failure modes, and output constraints and are both executed and revised by the same underlying model without access to a teacher model. Since nat...
  </details>

- **2026-08-12** — Arda Uzunoglu, Benjamin Van Durme, Daniel Khashabi — [Information Abundance Paradox: Long-Context Training Undermines Parametric Knowledge](http://arxiv.org/abs/2608.12218v2)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly trained and deployed with long contexts that span documents, code repositories, and interaction histories. This scaling reflects the implicit assumption that training on longer contexts will only help the model by exposing it to richer evidence. We challenge this view by studying how the context window shapes a model's mode of learning, shifting it between parametric internalization and contextualization. We propose the Information Abundance Paradox, which ...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 15 papers

- **2026-08-13** — Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda et al. — [Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining](http://arxiv.org/abs/2608.13515v1)
  <details><summary>📄 Abstract</summary>
  Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence...
  </details>

- **2026-08-13** — Saveliy Batruin — [Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test](http://arxiv.org/abs/2608.13228v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses combine retrieval, routing, state, provenance, and verification, but locally successful components may disagree on shared state. We model this failure with a finite \emph{capability sheaf}: stalks encode typed behavior signatures, restriction maps retain shared fields, and accepted runs are useful global sections. An exact finite constraint-satisfaction problem (CSP) defines acceptance, while a linearized relative cohomology class provides a diagnostic and search feature.   A con...
  </details>

- **2026-08-13** — Lei You — [Decomposition of Evidence, Contradiction, and Fragility in Perturbation Responses](http://arxiv.org/abs/2608.12935v1)
  <details><summary>📄 Abstract</summary>
  Perturbation methods explain model decisions by measuring prediction changes under altered inputs, but response magnitude tells us only how much a model reacts, not what that reaction means. The same magnitude can support the final factual-counterfactual difference, oppose it, or arise strongly along the perturbation path yet vanish at the endpoint. We therefore track how the contrast develops as paired inputs are progressively revealed, using the final contrast to interpret the trajectory. We i...
  </details>

- **2026-08-13** — Bobo Li, Hao Fei, Tianjie Ju et al. — [OmniScientist: An Omni-Modal Omni-Discipline AI Scientist](http://arxiv.org/abs/2608.13558v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in foundation models have enabled AI scientists to automate increasingly complete research workflows, from hypothesis generation and code execution to manuscript preparation. Yet workflow coverage alone does not provide access to the full evidence on which scientific discovery depends. Existing systems typically reason over text, code, labels, or precomputed summaries, leaving scientifically decisive spatial, temporal, cross-channel, and procedural relations unavailable to the ag...
  </details>

- **2026-08-13** — Saisha Shetty, Satvik Tripathi, Austin Lin et al. — [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coordination](http://arxiv.org/abs/2608.13476v1)
  <details><summary>📄 Abstract</summary>
  We present Multi-Agent Reasoning and Coordination (MARC), an open-source framework that replaces monolithic LLM prompting with deterministic multi-agent orchestration for clinical reasoning. MARC coordinates role-specialized agents for extraction, reasoning, answer generation, and evaluation, with explicit context passing and traceable intermediate outputs, enabling stage-wise failure attribution. We additionally introduce a Decomposer module that generates task-specific agent prompts from a pla...
  </details>

- **2026-08-13** — Amogh Joshi, Animesh Mukherjee, Sergey Utyuzhnikov — [DMDIntel: Interpreting Large Language Models via Dynamic Mode Decomposition](http://arxiv.org/abs/2608.13048v1)
  <details><summary>📄 Abstract</summary>
  In this work, we introduce DMDIntel which uses dynamic mode decomposition (DMD) to make the predictions made by LLMs in a classification task interpretable. It develops an input attribution pipeline, that first decomposes the hidden states of an LLM into prominent patterns, also known as modes, and then associates ranks to the input tokens based on the projection values on those modes. Rigorous experiments across three datasets and three model families consistently show that the ranked attributi...
  </details>

- **2026-08-13** — Junzhi Li, Peng He, Qirui Ji et al. — [Discovering Efficient and Explainable Communication Topologies for LLM-based Multi-Agent Systems via Causal Inference](http://arxiv.org/abs/2608.12921v1)
  <details><summary>📄 Abstract</summary>
  The performance of large language model (LLM)-based multi-agent systems (MAS) largely depends on effective communication topologies. Existing topology generation methods, however, typically learn communication topologies through black-box optimization driven solely by task-level rewards. While effective, such optimization provides little insight into why particular communication edges are selected, making it difficult to identify the critical communication subgraphs responsible for successful co...
  </details>

- **2026-08-13** — Jesus Salas — [Correct Is Not Governed: Provenance Integrity in Agentic Workflows](http://arxiv.org/abs/2608.12761v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows are commonly evaluated by whether they reach the correct outcome. That is insufficient in institutional settings, where a correct action may rely on the wrong authority, an unsupported completion claim, or work made stale by a later change. We define governed execution as work whose decisions, completion, and response to change are supported by inspectable provenance. We present Matrix, a deterministic causal-state layer that records authority and fact dependencies, verifies co...
  </details>

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


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-08-14** — Anna Borisiuk, Andrey Savchenko, Alexander Panchenko et al. — [The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning](http://arxiv.org/abs/2608.14229v1)
  <details><summary>📄 Abstract</summary>
  Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts t...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-08-14** — Ross D. King — [The Past and Future of AI Scientists](http://arxiv.org/abs/2608.14407v1)
  <details><summary>📄 Abstract</summary>
  We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their results, and revise their beliefs. Such systems are integrated scientific agents, connected to the literature, formal knowledge, mathematical models, simulations, data-analysis systems and physical laboratories.   Adam was the first machine to make novel scientific discoveries throug...
  </details>

- **2026-08-13** — Ravi Teja Chunduri, Srikaran Reddy Boya, Deep Narayan Mishra et al. — [Lines and Ladders: A Context-Aware Multi-Agent Framework for Large-Scale Retail Price Taxonomy](http://arxiv.org/abs/2608.12674v1)
  <details><summary>📄 Abstract</summary>
  Maintaining price consistency and executing an Every Day Low Price strategy is critical for global retailers. However, with catalogs spanning millions of active items, manual governance of price relationships is infeasible. Inconsistent pricing across item variants distorts customer value perception and cannibalizes sales. To address this, we present a scalable, context-aware Multi-Agent Framework designed to automate the construction of "Lines and Ladders" pricing taxonomies. Our framework empl...
  </details>

- **2026-08-11** — Alex Deaconu, Anubhav Gupta, Manaal Basha et al. — [Do Influence Tactics Matter? Investigating Prompt Framing Effects in LLM Code Generation](http://arxiv.org/abs/2608.11513v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly integrated into software engineering workflows, helping developers write, debug, test, and maintain code. While prompt wording and structure are known to influence model performance, the impact of psychologically inspired prompt framings remains unexplored. This study investigates whether different psychology-based communication strategies that humans use to persuade or motivate others can lead to more effective prompt framing, which may, in turn, af...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 171 papers

- **2026-08-14** — Alexei Vazquez — [Absorbing phase transition in a queueing model of coupled adaptive agents](http://arxiv.org/abs/2608.14398v1)
  <details><summary>📄 Abstract</summary>
  What decides whether people do things together or separately? Many activities cannot be carried out alone, and an individual must rank them against the private tasks competing for the same time. We address this within the priority-queue description of human activity by letting each agent choose the priority of a shared task rather than drawing it from a fixed distribution: the value of the joint activity, discounted by the estimated risk that the partner will not take part. Participation becomes...
  </details>

- **2026-08-14** — Benedikt Barthel Sorensen, Mitchell Black, Erfaun Noorani et al. — [A Temporal Barrier Framework for Collision Avoidance in Multi-Agent Autonomous Aerial Vehicles](http://arxiv.org/abs/2608.14239v1)
  <details><summary>📄 Abstract</summary>
  Operating teams of autonomous aircraft in dynamic, uncertain, and potentially adversarial environments requires safety protocols that are reliable yet selective, and allow agents to fly in close proximity while making progress toward mission objectives. We introduce adversarial time-to-collision (aTTC), a risk metric that quantifies, for a given agent, how quickly any surrounding agent could reach it assuming adversarial intent. We embed aTTC into the control barrier function (CBF) framework, de...
  </details>

- **2026-08-14** — Masahiro Kato, Taka Kato — [Handover of In-Context Learning State Across Session Boundaries](http://arxiv.org/abs/2608.14528v1)
  <details><summary>📄 Abstract</summary>
  This study investigates the methodological and theoretical properties of session handover in applications that use large language models. A task may continue in a new session when the context reaches the model's input limit, when the application restarts, or when another agent is asked to finish the task. The application must then decide which information from the earlier session to pass on. We formulate handover as the transfer of a task-relative in-context learning (ICL) state and distinguish ...
  </details>

- **2026-08-14** — Evan Coleman, Yuzhong Shen, Masha Sosonkina et al. — [Validating LLM-Modernized Scientific Software Through Differential Fault Injection](http://arxiv.org/abs/2608.14527v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used to modernize the legacy Fortran underlying production scientific software, but validation of these transformations emphasizes nominal executions and may not test whether a modernization preserves the original code's response to faults, perturbations, and reduced precision. We present a differential fault-injection validation method: a harness instruments the shared self-consistent-field driver of GAMESS at twelve sites and applies identical...
  </details>

- **2026-08-14** — Zohar Barak, Inbal Talgam-Cohen — [Ex-ante versus Ex-post: Egalitarian Facility Location Mechanism Design](http://arxiv.org/abs/2608.14499v1)
  <details><summary>📄 Abstract</summary>
  We study the facility location mechanism design problem where $n$ strategic agents report locations in Euclidean space and the mechanism outputs a single facility location. Each agent's cost is its distance from the facility, and our objective is to minimize the egalitarian cost, i.e., the maximum agent cost, in a strategyproof way.   The optimal deterministic approximation ratio is $2$, achieved by any dictator mechanism. We study the power of randomized strategyproof-in-expectation mechanisms....
  </details>

- **2026-08-14** — Alexei Odinokov, Rostislav Yavorskiy — [Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes](http://arxiv.org/abs/2608.14481v1)
  <details><summary>📄 Abstract</summary>
  As heterogeneous robotic systems deploy across diverse urban zones, maintaining safety amid complex human-robot interactions remains a critical challenge. We present a unified framework that bridges systematic hazard analysis and runtime enforcement using hazard-informed safety envelopes. Rather than treating safety as a static constraint isolated within individual software modules, we introduce a cross-layer safety transformation process spanning symbolic, spatial, and dynamic world models. We ...
  </details>

- **2026-08-14** — Jihun Park, Kyoungmin Lee, Jongmin Gim et al. — [CRAFT: Constrained Reward via Attention Fine-Tuning for Subject Personalization without Composed Targets](http://arxiv.org/abs/2608.14403v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven image personalization---generating new images that preserve the identity of one or several reference subjects in novel scenes---is a foundational capability for modern visual content creation. It is currently dominated by generalized methods that fine-tune a pretrained multimodal diffusion transformer (MMDiT) on hundreds of thousands to millions of paired \emph{(reference, composed-target)} examples, where each composed target is a synthesized image of the subject in a novel scene...
  </details>

- **2026-08-14** — Yu Zhuang, Kefei Chen, Yitong Duan et al. — [AgentRewind: Recoverable Execution for Long-Horizon LLM Agents](http://arxiv.org/abs/2608.14380v1)
  <details><summary>📄 Abstract</summary>
  Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, ...
  </details>

- **2026-08-14** — Shiju Zhao, Jiacheng Yang, Qihang Chen et al. — [CoRun: Padding is Simple and Efficient for Deterministic LLM Inference](http://arxiv.org/abs/2608.14376v1)
  <details><summary>📄 Abstract</summary>
  Despite fixed sampling parameters and random seeds, Large Language Model (LLM) inference exhibits output inconsistency, which undermines downstream tasks such as model evaluation and reinforcement learning. A major source of this nondeterminism is batch-dependent GPU execution: dynamic input shapes change kernel tiling and floating-point reduction orders. Existing systems address this problem with batch-invariant kernels, but these kernels restrict optimized tiling and split reductions, increasi...
  </details>

- **2026-08-14** — Wei Wei, Foroozan Daneshzand, Zezhong Wang et al. — [Epistemic Tensions: Reframing A Visualization Co-Design through Entanglement Theory](http://arxiv.org/abs/2608.14364v1)
  <details><summary>📄 Abstract</summary>
  In this work, we present how employing the lens of entanglement helped us examine and reframe epistemic tensions arising in a visualization co-design project. Entanglement theory challenges traditional assumptions in the visualization research community by emphasizing that knowledge is not produced through linear, isolated processes, but is inherently entangled with phenomena and apparatuses. While this perspective offers a compelling critique of conventional research practices, its practical va...
  </details>

- **2026-08-14** — Mingming Zhao, Jiqian Dong, Kangping Xu et al. — [ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond](http://arxiv.org/abs/2608.14354v1)
  <details><summary>📄 Abstract</summary>
  Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms for continuity, recovery from dead ends, and value-driven compute allocation, which inherently undermines overall search efficienc...
  </details>

- **2026-08-14** — Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi — [Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety](http://arxiv.org/abs/2608.14306v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a coordination architecture for heterogeneous UAV/UGV swarms that synthesises mission actions from uncertain, multi-modal sensor evidence while preserving hardware-enforced safety at the actuation boundary. The approach combines radar, RF, acoustic, and visual observations with Topic-Based Communication Space Petri Net (TB-CSPN) orchestration to support incremental mission formation under partial and evolving information. Consultant agents transform sensor outputs into tempor...
  </details>

- **2026-08-14** — Brett Reynolds — [Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models](http://arxiv.org/abs/2608.14252v1)
  <details><summary>📄 Abstract</summary>
  Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific arrangement produces, accepts, or withdraws. The arrangement has corrective control only when live, sufficiently independent routes can detect and repair fresh discrepancies. A route profile records w...
  </details>

- **2026-08-14** — Varuni H K, Soham Sarkar, Jay Kumar et al. — [Polaris : Multi Agentic System for Conversational Enterprise Analytics](http://arxiv.org/abs/2608.14246v1)
  <details><summary>📄 Abstract</summary>
  In today's fast-paced environment, the ability to swiftly access, understand, and act on data is no longer optional; it is essential. Yet most organizations remain data-rich but insight-poor, constrained by the complexity of querying, interpreting, and explaining enterprise-scale information. We present Polaris, a supervisor-led multi-agent framework for conversational enterprise analytics that bridges this gap. Polaris introduces Dynamic Task Coordination (DTC), a decision-theoretic orchestrati...
  </details>

- **2026-08-14** — Wenhao Tang, Tianyang Chen, Zhejun Cui et al. — [AgilePE: Autonomous UAV Pursuit-Evasion via Self-Play Reinforcement Learning](http://arxiv.org/abs/2608.14135v1)
  <details><summary>📄 Abstract</summary>
  Autonomous pursuit-evasion is a fundamental challenge for Unmanned Aerial Vehicles (UAVs), requiring rapid decision-making under tightly coupled dynamics and continuously changing opponent behaviors. Traditional rule-based or differential-game approaches often struggle with high-dimensional aerial interactions and agile maneuvering. We present AgilePE, a complete system for autonomous UAV pursuit-evasion via self-play reinforcement learning. AgilePE integrates agile low-level control, competitiv...
  </details>

- **2026-08-14** — Kaipeng Zeng, Wenxi Zhai, Shengrui Xu et al. — [Reaction-Transformation-Aware Flow Matching for Generalizable Transition State Generation](http://arxiv.org/abs/2608.14076v1)
  <details><summary>📄 Abstract</summary>
  Transition-state (TS) structures define the energetic barriers and mechanistic pathways of elementary chemical reactions, yet their identification remains computationally demanding because conventional saddle-point searches require expensive quantum-mechanical calculations. Recent machine-learning approaches have accelerated TS generation by predicting structures from reaction endpoint information, but they primarily learn geometric correspondence between endpoints and TSs, leaving the structura...
  </details>

- **2026-08-14** — Dingbao Shao, Song Wu, Xinyu Chen et al. — [InstructVVT: Instruction-Driven Video Virtual Try-On without Auxiliary Spatial Priors](http://arxiv.org/abs/2608.14070v1)
  <details><summary>📄 Abstract</summary>
  Video virtual try-on is a highly constrained editing task requiring the precise replacement of a target person's clothing while strictly preserving the original video's spatial structure and temporal dynamics. Existing methods heavily rely on auxiliary handcrafted spatial priors (e.g., masks, poses) for editing control. However, these priors are prone to failure in unconstrained real-world videos and often compress rich visual context into incomplete structural signals. Furthermore, standard rec...
  </details>

- **2026-08-14** — Xinye Li, Lingshuai Lin, Lei Wang et al. — [ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models](http://arxiv.org/abs/2608.14022v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned video world models require low-latency causal generation and reliable responses to game-native controls. Although causal distillation enables one- or few-step video synthesis, extending it to interactive world models remains challenging, as discrete keyboard states and continuous mouse motion must remain aligned with temporally compressed latent chunks during causal training and autoregressive rollout. We introduce ForgeWM, a progressive framework that transforms a bidirection...
  </details>

- **2026-08-14** — Jin Xu, Yu-Ping Chen, Ayanna Howard — [THRIVE: Therapeutic Humanoid Robot In Virtual Environment](http://arxiv.org/abs/2608.14462v1)
  <details><summary>📄 Abstract</summary>
  This paper presents THRIVE (Therapeutic Humanoid Robot In Virtual Environment), an at-home rehabilitation platform that integrates a suite of virtual-reality upper-body rehabilitation games, a real-time camera-based motion-tracking system, and a socially interactive robot therapist. The system is designed for therapy and intervention in children with upper-limb motor impairments, which can be improved through consistent, task-specific practice. THRIVE features a set of newly designed, engaging g...
  </details>

- **2026-08-14** — Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang et al. — [Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages](http://arxiv.org/abs/2608.14375v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reasoning systems often use agreement, confidence, or automated scores to decide which messages should shape a final answer. Such filtering assumes that a message likely to be correct is also worth keeping. Yet a wrong answer can contain a useful decomposition, constraint, or scientific principle. We test this distinction with Diverse Hypothesis Deliberation (DHD), a controlled measurement protocol that caches five independently generated messages and replays the same downstream solv...
  </details>

- **2026-08-14** — Marco Roth — [Classical Limits of Spectral Filtering in Quantum Generative Models](http://arxiv.org/abs/2608.14169v1)
  <details><summary>📄 Abstract</summary>
  Spectral filtering has been proposed as a route to regularization in quantum generative models: the quantum Fourier transform exposes the amplitude spectrum of a quantum circuit Born machine, and a diagonal filter suppresses the high frequencies associated with finite-sample noise, an operation whose classical counterpart seemingly requires manipulating an exponentially long amplitude vector. We examine whether this coherent operation produces anything that classical post-processing of samples f...
  </details>

- **2026-08-14** — Xingyu Zhu, Wenshuo Han, Zhouyu Wang et al. — [FlatLab: A Unified Methodology Framework and Simulation-Based Benchmark for Robotic Manipulation of Flat Objects](http://arxiv.org/abs/2608.14049v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation of flat objects is challenging due to the ungraspable configurations and strong variations in object geometry and material. Existing methods rely on heuristic pre-manipulation and are often evaluated in closed settings with limited generalization. We propose a unified framework that decouples the manipulation into a strategy generator and an action execution module. The strategy generator predicts appropriate manipulation strategies from object point clouds by learning strat...
  </details>

- **2026-08-14** — Haohui Yang, Jiaxing Sun, Xiujun Ma — [More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix It](http://arxiv.org/abs/2608.14420v1)
  <details><summary>📄 Abstract</summary>
  Power Sampling sharpens a language model's distribution over complete generation trajectories, offering a verifier-free way to improve reasoning at inference time. It also has the potential to serve as a general-purpose front end for a broad range of downstream sampling methods. However, we uncover a striking paradox: Power Sampling can drive more probability mass toward correct trajectories while degrading the downstream inference it is intended to enhance. Using self-consistency as a represent...
  </details>

- **2026-08-14** — Paras Balani, Subhrakanta Panda — [LLMs Don't Pay for the Jump](http://arxiv.org/abs/2608.14397v1)
  <details><summary>📄 Abstract</summary>
  Zahavy [2026] argues that Large Language Models, despite their capabilities in induction and deduction, cannot perform the abductive "Jump" that produced Einstein's equivalence principle, and attributes this limitation to the absence of embodied simulation. Zheng-Xin [2026] and Farmer [2026] question whether embodiment is necessary for abduction, pointing to alternative routes to General Relativity and forms of abduction that require no sensorimotor grounding. Max Planck resolved the blackbody r...
  </details>

- **2026-08-14** — Marek Arsenault, Hlér Kristjánsson — [Linearised quantum signal processing](http://arxiv.org/abs/2608.14387v1)
  <details><summary>📄 Abstract</summary>
  Quantum functional programming has been developed through two distinct paradigms in the last few years: Quantum Signal Processing (QSP)-based methods, including the Quantum Singular Value Transformation (QSVT), and methods based on higher-order quantum transformations, such as the Universal Hamiltonian Eigenvalue Transformation (UHET). While UHET performs functional transformations of Hamiltonian dynamics, its relationship to QSP-based techniques has remained unclear despite evident structural s...
  </details>

- **2026-08-14** — Arwa Osman, Marco Baroni, Iuri Macocco — [Local and Global Regimes of Geometric Complexity in Language Model Representations](http://arxiv.org/abs/2608.14361v1)
  <details><summary>📄 Abstract</summary>
  Intrinsic dimensionality (ID) is widely used to probe the representational complexity of language models, but it remains unclear whether ID differences reflect properties of language itself or artefacts of how the underlying dataset was constructed. In this paper, we focus specifically on how lexical diversity, the number of unique last-token items present in a dataset, affects ID estimates of that dataset. We find a scale-dependent transition between two regimes: at low lexical diversity, condi...
  </details>

- **2026-08-14** — Zhizhao Guan, Chen Huang, Ziming Liu et al. — [Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents](http://arxiv.org/abs/2608.14339v1)
  <details><summary>📄 Abstract</summary>
  We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of ...
  </details>

- **2026-08-14** — Jing-Cheng Yang, Hao-Jung Wang, Jinhao Du et al. — [Spatial Message Passing in Language Space for Pathology Image Interpretation](http://arxiv.org/abs/2608.14309v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) can generate pathological descriptions from histological images, but gigapixel Whole Slide Images (WSIs) exceed their visual context limits. The standard tiling workaround makes WSIs tractable yet severs the tissue neighborhoods that define tumor-stroma interfaces and morphology. We introduce Spatial Language Message Passing (SLMP), a framework that performs spatial reasoning entirely in language space, human-readable by construction. SLMP represents a WS...
  </details>

- **2026-08-14** — Kohsuke Ide, Ryousuke Yamada, Yoshihiro Fukuhara et al. — [Seeing Red, Thinking Bad: Color Bias in Vision Language Models](http://arxiv.org/abs/2608.14286v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) are increasingly used in industrial decision-making systems, such as recruitment support and recommendation. This motivates careful analysis of how VLMs process visual and textual information. In this work, we study how VLMs interpret text rendered as an image, and investigate the influence of visual styling biases. To this end, we introduce Stealth Visual Prompts, which subtly change visual styling of text, such as color and contrast, while preserving semantic cont...
  </details>

- **2026-08-14** — Dongjun Wei, Hongyi Wu, Yinuo Zou — [Attributing Preprocessing Invariance in Spectral Foundation Models](http://arxiv.org/abs/2608.14227v1)
  <details><summary>📄 Abstract</summary>
  Preprocessing invariance is an appealing goal for spectral foundation models: a frozen model should remain useful when laboratories preprocess spectra differently. It is usually measured by training a classifier under one preprocessing pipeline and testing it under another, with preserved accuracy read as evidence of learning. We revisit that reading, using a Raman foundation model as a case study. Such models normalize their inputs before any learned parameter is applied. If that normalization ...
  </details>

- **2026-08-14** — Patrik Kenfack, Jesse C. Cresswell, Anthony L. Caterini et al. — [Training Fair Tabular Foundation Models](http://arxiv.org/abs/2608.14211v1)
  <details><summary>📄 Abstract</summary>
  Tabular Foundation Models (TFMs) have emerged as leading methods for tabular predictive tasks, leveraging in-context learning to predict on new data without task-specific training. Despite the increased use of TFMs in high-stakes decision-making, their fairness properties remain largely unexplored. In this work, we incorporate fairness constraints directly into TFM training, enabling fair predictions in a single forward pass. Our approach addresses two key challenges: limited access to sensitive...
  </details>

- **2026-08-14** — Vassilios M Rothos — [Spectral stability and slow--fast structure of traveling waves in a regularized sine--Gordon equation](http://arxiv.org/abs/2608.14108v1)
  <details><summary>📄 Abstract</summary>
  We investigate the dynamics and spectral stability of traveling kink and antikink solutions in a dissipative sine--Gordon equation with two distinct fourth--order regularization mechanisms: a mixed space--time (inertial) term and a purely spatial (elliptic) term. The model includes damping, bias forcing, and higher--order dissipative effects, and is motivated by refined descriptions of fluxon dynamics in long Josephson junctions. Using a collective--coordinate reduction, we derive a Melnikov--ty...
  </details>

- **2026-08-14** — Zihong He, Chen Liang, Hai-Ning Liang — [AppLooper: An Agentic Application Engineering Loop for Accountable Release with Virtual-User Feedback](http://arxiv.org/abs/2608.14093v1)
  <details><summary>📄 Abstract</summary>
  Much existing research on coding agents organizes application development as an iterative loop of requirement interpretation, implementation, tool execution, evaluation, and repair. As these loops run longer, requirements may drift; users may lose awareness of the current state and rationale for changes; and generated applications may remain insufficiently grounded in target users' contexts and needs. Application engineering therefore requires a mechanism connecting owner intent, target-user exp...
  </details>

- **2026-08-14** — Giovanni Racioppi — [Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails](http://arxiv.org/abs/2608.14074v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has verifiably authorized: authorization logic lives in application code, is neither signed nor independently auditable, and the resulting logs lack evidentiary value. We present Mandato, a governance proxy that enforces digitally signed mandates on agent actions at the protocol level. A manda...
  </details>

- **2026-08-14** — Ziqi Song, Zongyuan Xiang, James G. Ogg et al. — [HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience](http://arxiv.org/abs/2608.14055v1)
  <details><summary>📄 Abstract</summary>
  Authoritative scientific knowledge in geoscience remains largely trapped in legacy monographs and historical literature, where unstructured text and complex layouts hinder computational access. We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents. Using a coordinating large language model, HERMES integrates domain constraints, validation rules and evidence tracing within a unified document-level extraction process that incorpora...
  </details>

- **2026-08-14** — Keito Kozaki, Keigo Sakurai, Ren Togo et al. — [Residual Dominance as a Structural Account of Last-Item Reliance in Causal Self-Attention Recommenders](http://arxiv.org/abs/2608.14021v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based sequential recommenders with causal self-attention often rely heavily on the most recent interaction at inference time, but how this behavior is structurally expressed in the representation used for prediction remains unclear. We combine prediction-time diagnostics with norm-based analysis of the full attention block. First, we show that SASRec-style models exhibit highly localized last-item reliance. We then find that, although self-attention aggregates contextual information,...
  </details>

- **2026-08-14** — Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini et al. — [Buy the Rumor, Sell the News: When Is News Priced In?](http://arxiv.org/abs/2608.14014v1)
  <details><summary>📄 Abstract</summary>
  Two old market sayings hold that news is already priced in by the time it is published, and that the rumor is bought while the news is sold. Both place the price move associated with a piece of news before and at publication rather than after it. Whether the claims hold, for which kinds of news, and by how much are basic questions about how fast markets absorb public information. We test them on 4.57 million financial news articles covering roughly 3,000 US stocks (2023-2026). A large language m...
  </details>

- **2026-08-13** — Dingzhan Nong, Zhihao Ren, Ziqi Li et al. — [Sign Language Video Synthesis via Loss-Guided Multi-Expert GANs](http://arxiv.org/abs/2608.13368v1)
  <details><summary>📄 Abstract</summary>
  This preliminary technical report presents a framework for sign language video synthesis using a loss-guided multi-expert Generative Adversarial Network (GAN) to enhance communication for individuals with hearing impairments. Three specialized discriminators -- global, hand, and head -- each guide a corresponding expert branch in the generator toward a distinct visual region, enabling implicit feature specialization without explicit diversity losses. To stabilize this multi-discriminator system,...
  </details>

- **2026-08-13** — Shunwen Bai, Ziping Ma, Chaoyang Zhang et al. — [TsuGO: Probing Search Efficiency in LLM Reasoning via Go Life-and-Death Problems](http://arxiv.org/abs/2608.13221v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of LLM reasoning is moving from final-answer accuracy to process-level assessment, yet existing methods still fail to capture how models plan reasoning paths and allocate reasoning resources--that is, how they organize search. Prior process-level methods focus on the coherence and redundancy of chain-of-thought (CoT), and most benchmark tasks have a single objective solvable by static capabilities such as derivation and tool use, leaving search organization unmeasured. We introduc...
  </details>

- **2026-08-13** — Yaxin Luo, Haobin Jiang, Jialv Zou et al. — [AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design](http://arxiv.org/abs/2608.13560v1)
  <details><summary>📄 Abstract</summary>
  Transforming multimodal sources into condensed and structured media outputs can be fundamentally conceptualized as a long-horizon agentic process centered on a model-harness system. While an ideal harness system should align with human design priors and accumulate reusable experience through empirical exploration to drive recursive self-improvement, existing paradigms remain static and fall short of this capability. In this paper, we present AutoDesign, a framework that aligns with human design ...
  </details>

- **2026-08-13** — Shouzhi Fang, William C. Tegge, Md Omar Faruque et al. — [YAVIN: A Unified Architecture for Secure Edge Processing in Memory](http://arxiv.org/abs/2608.13496v1)
  <details><summary>📄 Abstract</summary>
  Secure, private multi-tenant execution spanning processors, memory, and accelerators remains one of the most significant challenges in modern edge computing systems. Simultaneously, processing-in-memory (PIM) has emerged as an effective approach for reducing the Von Neumann bottleneck by moving computation closer to data. Existing trusted execution environments (TEEs) establish trust only within the processor, protecting data while it traverses untrusted resources such as the memory bus. Consequ...
  </details>

- **2026-08-13** — Yi-Chung Chen, Philip Jacobson, Tom Lampo et al. — [TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval](http://arxiv.org/abs/2608.13495v1)
  <details><summary>📄 Abstract</summary>
  Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on...
  </details>

- **2026-08-13** — Zuzanna A. Wakefield-Skórniewska, Bartłomiej W. Papież — [Evaluation of Clinically Steerable Retinal Image Generation from Foundation Model Latent Spaces](http://arxiv.org/abs/2608.13455v1)
  <details><summary>📄 Abstract</summary>
  Medical foundation models learn latent representations of clinically meaningful phenotypes, yet their ability to support controllable image generation remains largely unexplored. We evaluate four retinal foundation models within the representation tokenizer framework and examine whether demographic and clinical information encoded in latent representations from foundation models is preserved during synthetic image generation. We show that generated representations and images faithfully inherit p...
  </details>

- **2026-08-13** — Zongyun Zhang, Jiacheng Ruan, Xian Gao et al. — [Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ](http://arxiv.org/abs/2608.13441v1)
  <details><summary>📄 Abstract</summary>
  Although multimodal large language models (MLLMs) have shown substantial potential in visual understanding and graphic code generation, editing scientific figures through code presents a greater challenge: a model must jointly recover visual structure, ground the requested change, generate compilable code, and preserve all unrelated content. While existing TikZ benchmarks mainly focus on figure reconstruction and generation, few systematically evaluate instruction-guided scientific figure editin...
  </details>

- **2026-08-13** — Yupan Ding, Jing Xiao, Zhenyuan Zhang et al. — [LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning](http://arxiv.org/abs/2608.13344v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon Earth observation reasoning requires models to organize multi-stage geographic evolution, localize spatial changes, detect temporal anomalies, and infer future from extended image sequences. However, existing remote sensing vision-language models mainly focus on isolated images, image pairs, or short sequences, limiting reliable grounding in the relevant frames and regions. We introduce LongEarth-Bench, a benchmark containing approximately 120k question-answering samples derived fro...
  </details>

- **2026-08-13** — Jingbo Ji, Lingyi Li, Xilong Cheng et al. — [RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory](http://arxiv.org/abs/2608.13334v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensiv...
  </details>

- **2026-08-13** — Mohammed Sabry, Sean Augenstein, Keith Rush et al. — [Mixture of Training: Recombining Small-Scale Scaffolded Pretraining Runs into a Larger Language Model](http://arxiv.org/abs/2608.13277v1)
  <details><summary>📄 Abstract</summary>
  We ask whether language-model pre-training can be decomposed into smaller, independently trainable jobs that can later be recomposed into a coherent larger model. We introduce Mixture of Training (MoT), a scaffolded modular pre-training procedure that partitions a target Transformer into contiguous layer blocks, trains each block inside a frozen pretrained aligner scaffold, and then recomposes the trained blocks with an optional short end-to-end adaptation pass. On a 1.3B-parameter Gemma-style m...
  </details>

- **2026-08-13** — Yuheng Huang, Jianlang Chen, Jiayang Song et al. — [NARU: A Benchmark for NARrative Evolution and Cultural Nuance Understanding in Japanese Extreme Long Video](http://arxiv.org/abs/2608.13210v1)
  <details><summary>📄 Abstract</summary>
  Long-form video understanding encompasses tasks that go beyond retrieving isolated events, including tracking an evolving narrative and interpreting social meaning that may remain implicit. However, existing benchmarks rarely evaluate these capabilities jointly, particularly in high-context, non-English media. To address this gap, we introduce NARU, a benchmark designed to evaluate Narrative evolution and Reasoning on cultural Understanding in Japanese long-form video. NARU consists of 1,481 que...
  </details>

- **2026-08-13** — Shuzhe Zhang, Xin Zhu, Yinling Qian et al. — [S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation](http://arxiv.org/abs/2608.13103v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon surgical robot manipulation is challenging because task rewards are sparse, while meaningful interaction changes occur at irregular intervals. Existing world-model agents typically imagine at primitive-step resolution, leaving variable-duration task progress implicit. Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions. We propose S2-HWM, a Sparse Event-Structured Hierarc...
  </details>

- **2026-08-13** — Jiqi Li, Jingyi Mei, Wang Fang et al. — [Formal Verification of Quantum Ancilla Safety](http://arxiv.org/abs/2608.13099v1)
  <details><summary>📄 Abstract</summary>
  Ensuring ancilla safety is a critical correctness requirement for quantum compilation, since ancilla qubits are routinely introduced to implement complex operations with fewer gates and reduced depth. However, formally verifying this property is computationally hard due to state-space explosion in the number of qubits, particularly for dirty ancillae, which carry unknown initial states and must be restored after use. We propose an end-to-end verification-and-repair framework that rigorously addr...
  </details>

- **2026-08-13** — Fanpeng Yang, Xing Li, Shuling Wang et al. — [How Powerful are LLMs in Generating Formal Program Specifications?](http://arxiv.org/abs/2608.13077v1)
  <details><summary>📄 Abstract</summary>
  Formal verification provides strong guarantees of software correctness, but its adoption is limited by the high cost of writing precise formal specifications. While recent large language models (LLMs) have shown strong capabilities in theorem proving and verified code generation, their true ability to generate program specifications remains unclear. Existing evaluations require either verifying implementation conformance or proving semantic equivalence between specifications, both of which are f...
  </details>

- **2026-08-13** — Johan Henriksson — [Static analysis-guided agentic AI translation enables Rust as a full stack bioinformatics language](http://arxiv.org/abs/2608.13029v1)
  <details><summary>📄 Abstract</summary>
  The field of bioinformatics struggles with legacy code - old code that is commonly used but may no longer have a maintainer, or may be written in an now-unfamiliar language (e.g. Perl, Fortran). This incurs maintenance cost (technical debt), but dynamically typed languages also negatively impacts the environment and fail to make use of modern hardware. Legacy code may also have security or safety problems that make it unsuited for use in clinical settings. Here we show that agentic AI, combined ...
  </details>

- **2026-08-13** — Yunhao Bai, Zhongwei Qiu, Guangyu Guo et al. — [HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation](http://arxiv.org/abs/2608.12904v1)
  <details><summary>📄 Abstract</summary>
  Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-depe...
  </details>

- **2026-08-13** — Xutao Mao, Liangjie Zhao, Xiang Zheng et al. — [Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM Agents](http://arxiv.org/abs/2608.12851v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents convert successful trajectories into persistent cross-task state. An unsafe success can thereby become reusable policy after its triggering input disappears. Skill evolution makes this failure measurable by distilling operational trajectories into executable, transferable, and inspectable procedures. Because evolution optimizes task outcomes rather than procedure safety, compromised experience can cause skill misevolution. Existing benchmarks measure current behavior or...
  </details>

- **2026-08-13** — Prateek Kumar Rajput, Abdoul Aziz Bonkoungou, Alberick Euraste Djiré et al. — [Memorization Diagnostics for Code LLMs Should be Scale-Aware](http://arxiv.org/abs/2608.12771v1)
  <details><summary>📄 Abstract</summary>
  The extent to which large language models for code rely on memorization over genuine understanding remains highly debated. While current literature frequently reports widespread memorization, evaluating the underlying probing techniques across dense architectures reveals a severe breakdown in their utility at scale. Traditional encoder-style probes using perturbations such as synonym fuzzing or dead-code insertion struggle to expose memorization in scaled models, even on known-contaminated bench...
  </details>

- **2026-08-13** — LingKai Bu — [Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors](http://arxiv.org/abs/2608.12746v1)
  <details><summary>📄 Abstract</summary>
  Object hallucination in multimodal large language models arises when language priors and corpus co-occurrence bias outweigh the visual evidence, with nothing tying an individual object mention to what the image shows. Most remedies intervene at decoding time without training, yet under a unified protocol their benefit is confined to short captions;supervised fine-tuning (SFT) on a detail- rich corpus lengthens captions, but over forty percent still name absent objects. This paper proposes Dual-S...
  </details>

- **2026-08-13** — João Henrique Andrade, Tao Feng, Paolo Piccione et al. — [Delaunay solutions to the fractional Hartree equation with critical growth](http://arxiv.org/abs/2608.12734v1)
  <details><summary>📄 Abstract</summary>
  We study positive solutions of the critical fractional Hartree equation with a non-removable isolated singularity at the origin. This equation is doubly nonlocal, involving both the fractional Laplacian and a Riesz convolution potential. We first prove that every positive singular solution is radially symmetric about the origin, by combining the Caffarelli--Silvestre extension with the method of moving spheres. We then establish the existence of Delaunay-type periodic singular solutions. After t...
  </details>

- **2026-08-13** — Ping Li — [Topological obstructions to geometric positivity and negativity on Calabi-Yau manifolds](http://arxiv.org/abs/2608.12705v1)
  <details><summary>📄 Abstract</summary>
  We study whether the topology underlying a Calabi-Yau manifold can support natural geometric positivity or negativity structures. In even complex dimension $n \geq 4$ (assuming $b_2=1$ when $n \geq 6$), we strengthen a theorem of Oguiso-Peternell by proving that a Calabi-Yau manifold is not homeomorphic to a weak Fano $n$-fold. The same obstruction applies to Kähler manifolds with quasi-positive holomorphic sectional curvature. A transformation-group analogue excludes, in particular, symplectic ...
  </details>

- **2026-08-13** — Fin Amin, Sounak Dutta, Paul D. Franzon — [Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization](http://arxiv.org/abs/2608.12687v1)
  <details><summary>📄 Abstract</summary>
  Bayesian optimization (BO) is a sample-efficient framework for analog circuit topology search, where evaluating each candidate topology can require costly simulation. However, representation-based BO methods typically treat circuit embeddings as fixed after encoder training. This creates a mismatch between representation learning and optimization: embeddings learned to encode or reconstruct circuit structure are not necessarily organized according to the figure of merit (FoM) being optimized. Th...
  </details>

- **2026-08-13** —  DreamX Team, Rui Chen, Xiangxiang Chu et al. — [DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation](http://arxiv.org/abs/2608.13489v1)
  <details><summary>📄 Abstract</summary>
  We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mat...
  </details>

- **2026-08-13** — Dingyi Rong, Yue Shi, Chaofan Ma et al. — [H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models](http://arxiv.org/abs/2608.13049v1)
  <details><summary>📄 Abstract</summary>
  Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transferring them across embodiments remains challenging due to differences between human hands and robotic end-effectors. Recent advances in video world models offer a promising pathway to synthesize robot-centric manipulation videos from human observations, w...
  </details>

- **2026-08-13** — Geng Wang, Junyu Yang, Timan Lei et al. — [Controlling the dynamics of an electric-field-driven droplet on a lubricant-infused micropillar surface](http://arxiv.org/abs/2608.12868v1)
  <details><summary>📄 Abstract</summary>
  As a non-contact control approach, electric field (EF) can be utilised to drive droplet dynamics on a lubricant-infused surface (LIS), with numerous potential applications ranging from drug manufacturing to 3D printing. However, the resulting droplet dynamics remain poorly understood, especially as there are several possible droplet lubrication states on LIS. Here, we develop a lattice Boltzmann scheme that fully captures the interplay between the interfacial flows and electrohydrodynamics and h...
  </details>

- **2026-08-13** — Weihan Meng, Hongzhu Guo, Yi Jing et al. — [SAEVerbalizer: Generating Explanations for Sparse Autoencoder Features via Representation Verbalization](http://arxiv.org/abs/2608.13538v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) are proposed to extract numerous features from large language model (LLM) representations, yet explaining these features still relies primarily on external observation. This reliance leads to superficial explanations inferred from observed model behavior and computational inefficiency from collecting such behavioral evidence at scale. We introduce SAEVerbalizer, a framework that injects SAE decoder directions into an LLM's representations and fine-tunes the LLM's downs...
  </details>

- **2026-08-13** — David Chushig-Muzo, María Ángeles Rodríguez de Cara, Eva Milara et al. — [TabSOM: A tabular-to-image encoding method based on self-organizing maps](http://arxiv.org/abs/2608.13513v1)
  <details><summary>📄 Abstract</summary>
  Tabular-to-image methods have emerged as novel approaches to leverage the high predictive performance of convolutional neural networks and vision transformers. They convert tabular data into image representations, mapping each feature at a fixed pixel location derived from a dimensionality-reduction method (e.g., t-SNE, UMAP, PCA). However, they encode only the marginal value of each feature and discard information about feature relationships. We propose TabSOM, a tabular-to-image encoding built...
  </details>

- **2026-08-13** — Avinash Kori, Fabrizio Russo — [A Unifying Perspective on Causal World Models: From Observations to Representations to Structure](http://arxiv.org/abs/2608.13456v1)
  <details><summary>📄 Abstract</summary>
  World Models (WM) are increasingly seen as a foundation for intelligent agents that can predict, plan, and act beyond their training distribution. In this paper, we study WMs from a causal perspective across multiple levels of abstraction, ranging from perceptual observations to building a conceptual representation of the structure governing the environment dynamics. We argue that useful WMs must go beyond generative capabilities alone: they should also capture entity properties, entity-to-entit...
  </details>

- **2026-08-13** — Jiin Choi, Kyung Hoon Hyun — [CogChat: Knowledge Graph-Augmented Conversational AI with Heterogeneous Graph Transformer for Cognitive Grounding in Design Generation](http://arxiv.org/abs/2608.13216v1)
  <details><summary>📄 Abstract</summary>
  LLM-based chat systems have become valuable tools for design practice, enabling rapid ideation and flexible task support. Yet these systems process designer utterances as generic sequences, maintaining context through recency rather than through any model of how the speaker organizes knowledge. In design conversation, this gap compounds as relational context decays between turns, identical words go unresolved across designers, and the conversation loops or restarts rather than deepens. We presen...
  </details>

- **2026-08-13** — Zhili Shen, Craig Macdonald — [GEM: A Generative Embedding Model Bridging Reasoning and Retrieval](http://arxiv.org/abs/2608.13200v1)
  <details><summary>📄 Abstract</summary>
  Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and documents, resulting in a growing gap between how users express their needs and how retrievers interpret them. In this paper, we present GEM, a generative embedding model that augments retrieval through its own knowledge by explicitly reasoning about user intent and relevance criteria...
  </details>

- **2026-08-13** — Shotaro Tada — [A Radon-Transform Perspective on Exoplanet Transits](http://arxiv.org/abs/2608.13163v1)
  <details><summary>📄 Abstract</summary>
  Transit light curves are usually analyzed under the assumption that the transiting planet has a circular sky-projected silhouette. However, planetary rotation, tides, rings, or atmospheric inhomogeneities can produce non-circular silhouettes. This raises the question of what information transit light curves can provide about the underlying two-dimensional attenuation map. In this paper, we show that, in a simple and transparent limit, the time derivative of the transit light curve during ingress...
  </details>

- **2026-08-13** — Nhan Phan, Ilona Lähteenmäki, Anna von Zansen et al. — [CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model](http://arxiv.org/abs/2608.13101v1)
  <details><summary>📄 Abstract</summary>
  Research on automatic speaking assessment (ASA) has increasingly adopted multimodal speech large language models to assess learners' speaking performance. However, existing studies provide limited analysis of how acoustic and content information contribute to predictions and how stable the resulting performance is. We propose CASA, a simpler architecture combining Whisper-medium and Qwen3.5-2B that achieves state-of-the-art performance while providing a more interpretable separation between spee...
  </details>

- **2026-08-13** — Divya Jyoti Bajpai, Kishan Kumar Upadhyay, Manjesh Kumar Hanawal — [SPADE: Speculative Decoding for Precise and Low Cost Distributed Edge Cloud Inference](http://arxiv.org/abs/2608.13076v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have achieved remarkable success in natural language understanding and generation, but their deployment is constrained by high computational demands. Deploying smaller LLMs directly on the edge can circumvent this, but with degraded accuracy. Deploying smaller cloud-based big LLMs preserves performance, but at the cost of expensive per-token computation. We present a distributed inference framework, \our{}, that integrates speculative decoding (SD) across edge and cl...
  </details>

- **2026-08-13** — David Krüger, Michael Potthoff — [Topology and Quantum-Spin-Classical-Spin Crossover of the Gapped Kondo Effect](http://arxiv.org/abs/2608.13065v1)
  <details><summary>📄 Abstract</summary>
  The gapped Kondo effect describes the screening of an $S=\frac12$ impurity spin locally coupled via an antiferromagnetic exchange interaction to a conduction-electron system exhibiting a finite hard gap. Using a combination of a Lanczos transformation and a self-consistent configuration-interaction scheme, we numerically investigate the local phase diagram. Furthermore, we show that the different phases can be characterized by several topological invariants: the conventional momentum-space Chern...
  </details>

- **2026-08-13** — Dechen Zhang, Xuan Tang, Xinxiang Yin et al. — [VALG: An Agentic System for ML Theory Research](http://arxiv.org/abs/2608.13060v1)
  <details><summary>📄 Abstract</summary>
  Machine learning theory studies learning procedures through mathematical setups in which the data model, training protocol, oracle access, loss, metric, and randomness define the phenomenon that a theorem is meant to explain. Solving an open problem therefore requires the problem formulation, theorem target, and proof mechanism to be developed in concert. Researchers formulate hypotheses, test them through preliminary theoretical or empirical analysis, and refine both assumptions and proofs. We ...
  </details>

- **2026-08-13** — Zhixin Ren, Yau Lyu, Congrong Li et al. — [Momentum as Residual-Driven Multiplier Correction for Deep Learning Optimization](http://arxiv.org/abs/2608.12925v1)
  <details><summary>📄 Abstract</summary>
  Momentum-based optimizers are widely used in modern deep learning, yet the relations among momentum recursion, update geometry, and acceleration remain only partially understood. We develop an $\textbf{A}$DMM-$\textbf{I}$nspired $\textbf{M}$omentum (AIM) framework based on residual-penalty variable splitting, which interprets momentum as a multiplier-like correction driven by the splitting residual. AIM recovers the exponential moving average of gradients from an ADMM-style multiplier update and...
  </details>

- **2026-08-13** — Yifan Mei, Qingling Shi, Changli Wu et al. — [TennisVAR: A Stroke-Evidence-Grounded Multimodal Large Language Model for Tactical Reasoning in Tennis Videos](http://arxiv.org/abs/2608.12920v1)
  <details><summary>📄 Abstract</summary>
  Sports-video understanding is moving beyond event recognition toward explaining how actions collectively shape match progression, however, existing tennis-video methods either perceive individual strokes without modeling their tactical dependencies or generate high-level analyses without grounding them in the underlying events. To bridge this perception-to-understanding gap, we formulate stroke-evidence-grounded tactical reasoning, a new rally-level task that requires models to jointly predict a...
  </details>

- **2026-08-13** — Runze Zhao, Zixin Tang, Xiaoshuai Hao et al. — [ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification](http://arxiv.org/abs/2608.12877v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However, these methods face two critical limitations: (1) agents may perform individual subtasks without sufficient awareness of the global verification objective, causing their reasoning to devia...
  </details>

- **2026-08-13** — Yuchen Zheng, Sihan Xu, Jingwen Yang et al. — [FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation](http://arxiv.org/abs/2608.12845v1)
  <details><summary>📄 Abstract</summary>
  Semantic ID (SID)-based generative recommendation has recently achieved remarkable success. However, existing methods suffer from a previously overlooked fairness issue, which we term \textbf{Token Frequency Bias}, where high-frequency SID tokens are systematically over-predicted while low-frequency SID tokens are under-predicted. This bias originates from the combined effects of imbalanced semantic codebooks during SID construction, and popularity bias together with the maximum likelihood estim...
  </details>

- **2026-08-13** — Jinlin Wu, Si Qiao, Yi Liu et al. — [A Generative Framework for the Creation of Multi-Attribute Geographically-Explicit Synthetic Population](http://arxiv.org/abs/2608.12768v1)
  <details><summary>📄 Abstract</summary>
  Generating multi-attribute synthetic populations with realistic joint distributions and geographic variation is a foundational requirement for geo-simulation techniques, such as micro-simulation and agent-based modeling. However, it remains challenging for existing methods to reconstruct region-specific joint distributions from aggregated-level data alone. Thus, we propose a hierarchical diffusion-based generative framework that utilizes a realistic region-specific joint distribution of multiple...
  </details>

- **2026-08-13** — Fangzhou Liu, Peiyi Han, Jiawei Liu et al. — [SynAct: A Reasoning-Acting Large Language Model Agent for Adaptive Synthesis Optimization](http://arxiv.org/abs/2608.12751v1)
  <details><summary>📄 Abstract</summary>
  Logic synthesis transforms RTL designs into gate-level netlists, where PPA results are highly sensitive to the choice of optimization commands, making synthesis tuning both high-dimensional and expensive. Previous approaches fall into two categories: automated methods, which perform black-box search over fixed action spaces with limited decision-level interpretability, and LLM-based methods, which typically generate static scripts upfront and cannot adapt to evolving circuit states. We present S...
  </details>

- **2026-08-13** — Xuetong Pei, Jian Liu, Vidura Munasinghe et al. — [SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation](http://arxiv.org/abs/2608.12707v1)
  <details><summary>📄 Abstract</summary>
  Hierarchical open-vocabulary object navigation (OVON) requires agents to follow free-form instructions that may specify targets through scene-, room-, region-, and instance-level cues in unseen environments. Although recent work LangMap has formalized this setting, reliably solving it under partial observations remains challenging: spatial grounding requires persistent environment-level evidence, whereas target verification requires clear and discriminative candidate views. We present SAP-Nav, a...
  </details>

- **2026-08-13** — Archan Dutta, Yash Dharmadhikari, Marat Valiullin et al. — [Designing AI Pipelines for Decision-Ready ITSM Intelligence](http://arxiv.org/abs/2608.12670v1)
  <details><summary>📄 Abstract</summary>
  IT service management (ITSM) systems accumulate large volumes of heterogeneous ticket data that are difficult for sales and executive stakeholders to convert into actionable intelligence. This paper presents a sociotechnical AI pipeline, designed and evaluated following design science research principles, that transforms raw ITSM exports into a multilevel decision-support artifact. The pipeline combines LLM-based schema normalization, HDBSCAN sub-topic clustering, and hierarchical agglomerative ...
  </details>

- **2026-08-12** — Oguz Serdar, Cuneyt Mertayak — [SteerBench-Work: A Benchmark for Agent Steering at Action Boundaries](http://arxiv.org/abs/2608.12654v1)
  <details><summary>📄 Abstract</summary>
  Long-running LLM agents act through tools, and a single step can send an email, merge a pull request, or wire a payment. The steering decision is the pre-commit choice at that boundary: proceed, or hold for human or policy review. We introduce SteerBench-Work, an incident-anchored, bidirectional benchmark for that decision in workplace agents across developer operations, customer service, finance, legal, medical, HR, and security.   Release v2026-05 contains 106 scenarios anchored in public inci...
  </details>

- **2026-08-12** — Meet Bhadra — [GateTruth: Auditing the Rigor of RTL Design Benchmarks via Mutation Testing](http://arxiv.org/abs/2608.12635v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks for evaluating large language models on register-transfer-level (RTL) hardware design have proliferated rapidly, yet none reports having applied mutation testing, an established hardware-verification technique for quantifying testbench quality, to ask whether its own testbenches are trustworthy. A testbench that never fails is not evidence of a correct design; it may simply never stimulate the logic that is actually broken. We introduce GateTruth, a mutation-testing engine and methodo...
  </details>

- **2026-08-12** — William Khalili — [Feasibility and Convex Design of Probe-Position Matching in a Scanning X-Band Radar Array](http://arxiv.org/abs/2608.12602v1)
  <details><summary>📄 Abstract</summary>
  The probe position of a microstrip element is normally chosen from the isolated-element input resistance. This paper replaces that procedure with a decision available before any array optimisation. A single Floquet unit-cell solution at one arbitrary probe position is decomposed into a feed inductance, a transformer ratio carrying the probe position, and an array-loaded resonator. Three closed-form results follow. The set of input impedances reachable by probe position and resonant length is a d...
  </details>

- **2026-08-12** — Ruairidh M. Battleday, Kai Sandbrink, Jimi Cullen-Drohan et al. — [DiG-bench: Discovery in Games](http://arxiv.org/abs/2608.12593v1)
  <details><summary>📄 Abstract</summary>
  Discovery---formulating novel generalizations---is a central part of the scientific process. Despite its importance, there is a gap in the current AI benchmark landscape, with few benchmarks directly probing the capacity for discovering new knowledge with experimentation in controlled environments where the objective is unknown. To address this gap, we release a new benchmark: DiG-bench (Discovery in Games). DiG-bench consists of a set of 70 independent games. Each game is encoded as a short str...
  </details>

- **2026-08-12** — Nelson Guda — [Geometric and Behavioral Stratification in Transformer Residual Streams](http://arxiv.org/abs/2608.12447v1)
  <details><summary>📄 Abstract</summary>
  Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what kind of direction does such a basis select? We investigate the prediction direction, the unembedding direction of the token a model currently predicts, and find that it functions as a content-defined privileged anchor. Measured with respect to this anchor, residual-stream variation is geometrically and behaviorally stratified by proximity to the prediction. ...
  </details>

- **2026-08-12** — Ruitao Wang, Yuwen Hao, Menglin Yang — [SynWeaver: Website-Prior Task and Trajectory Co-Synthesis for Web Agents](http://arxiv.org/abs/2608.12429v1)
  <details><summary>📄 Abstract</summary>
  Web agents often struggle to generalize to unseen websites because they lack website-specific supervision. Recent exploration-based data synthesis methods reduce manual annotation, but they still face two key limitations: they often fail to cover the full functionality of a website, and without sufficient website prior knowledge, they tend to propose hallucinated tasks, which in turn limits the diversity and efficiency of downstream trajectory synthesis. We present \textbf{SynWeaver}, a website-...
  </details>

- **2026-08-12** — Tom Adamczewski — [OEIS Open: How many conjectures can language models turn into theorems?](http://arxiv.org/abs/2608.11941v2)
  <details><summary>📄 Abstract</summary>
  We construct OEIS Open, a benchmark based on 492 open mathematical conjectures from the OEIS, formalized in Lean by Tsoukalas et al. Whereas these conjectures had previously been attempted only with a bespoke agent, our open-source evaluation code runs any generic language model (LM) against them, and is secure against LM cheating attempts. We find that LMs equipped with a minimal set of tools resolve 147 of these conjectures with a budget of \$50 per attempt, scoring 30% on OEIS Open. OEIS Open...
  </details>

- **2026-08-12** — Mariya I. Vasileva — [Large Language Models Can Follow Instructions, But Not Many at Once: Phase Transitions in Compositional Constraint Satisfaction](http://arxiv.org/abs/2608.12426v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed in settings that require simultaneous adherence to multiple explicit constraints - reasoning structure, safety boundaries, output schemas. Individual constraints are handled proficiently, but the compositional regime, where many must hold jointly, remains poorly characterized: how rapidly does performance degrade, what governs the degradation, and can the collapse be mitigated? We introduce Constraint Saturation Evaluation (CSE), a procedurally gen...
  </details>

- **2026-08-12** — Yuxuan Zhang, Haozhong Xiong, Jiayi Song et al. — [UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos](http://arxiv.org/abs/2608.11752v2)
  <details><summary>📄 Abstract</summary>
  Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transf...
  </details>

- **2026-08-12** — Alekh Jindal, Jyoti Pandey, Christina Pavlopoulou et al. — [Reverse Migration of Cloud Applications to On-premises](http://arxiv.org/abs/2608.11640v2)
  <details><summary>📄 Abstract</summary>
  Cloud has become ubiquitous to modern applications due to its agility and scalability. However, regulated industries still prefer to deploy on-premises due to security and compliance reasons. This creates a paradox for vendors who need to develop in the cloud but deploy on-premises, leading to long release cycles and complex maintenance. In this paper, we present Diel, the Tursio On-premises Migrator, a tool that automates reverse migration of cloud applications to on-premises environments. Diel...
  </details>

- **2026-08-12** — Runyi Zhao, Ruixin Wu, Chengkun Li et al. — [RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills](http://arxiv.org/abs/2608.12416v1)
  <details><summary>📄 Abstract</summary>
  Achieving generalizable robotic manipulation remains a central challenge in embodied intelligence. Despite rapid advances in model architectures and learning algorithms, progress is often limited by the scarcity and narrow diversity of real-world data. The RoboSynChallenge competition introduces a unified benchmark to evaluate and advance the generalizability of manipulation policies across a spectrum of tasks, environments, and difficulty levels. To alleviate the shortage of realistic data, the...
  </details>

- **2026-08-12** — Aaryan Sharma, Vishak Prasad C, Virendra Singh et al. — [MASCOT: Model-Aware Submodular Coverage for Composite-Attribute Text-to-Image Retrieval](http://arxiv.org/abs/2608.12532v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are highly effective in retrieving semantically relevant images. However, in practice, relevance alone is often insufficient. Systems must also achieve Result Diversification (RD) across composite attributes such as geography and time, a task for which precise control remains challenging. Current re-ranking methods, such as Multi-Source Determinantal Point Processes (MS-DPP), address this using manifold-based repulsion over similarity representations. Although this ...
  </details>

- **2026-08-12** — Ekkehardt Bauer, Dirk Holländer, Linus Wolff et al. — [AI-Driven Multiscenario Interest Rate Forecasting: A Proof of Concept for Banking Asset Management](http://arxiv.org/abs/2608.12424v1)
  <details><summary>📄 Abstract</summary>
  This study focuses on developing an AI-supported prototype for multiperspective interest rate forecasting that combines classical econometric models with modern artificial intel-ligence methods. Tested in a major European bank, the system enables more precise and flexible prediction of interest rate developments, supporting strategic decision-making in Asset-Liability Management (ALM). It integrates topic modeling, sentiment analysis, econometric forecasting, and market-based analyses within an ...
  </details>

- **2026-08-12** — Qiuwu Chen, Zimo Liu, Yuchen Li et al. — [LoKiFormer: Locality-aware Attention with Decoupled Knowledge Memory for Efficient Large Language Model Pretraining](http://arxiv.org/abs/2608.12419v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have achieved remarkable breakthroughs across various applications. However, their architectures remain inefficient in pretraining due to two main limitations: (i) self-attention lacks an explicit inductive bias for locality, leading to redundant modeling of sequence-internal local information; (ii) mixture-of-experts (MoE) implicitly couples knowledge storage with computational pathways, hindering flexible access to sequence-external global knowledge. To overcome th...
  </details>

- **2026-08-12** — Zhuoran Li, Zhuohang Bian, Xin Huang et al. — [HBF Sucks! A Full-Stack Characterization of High-Bandwidth Flash for KV-Centric LLM Serving](http://arxiv.org/abs/2608.11668v2)
  <details><summary>📄 Abstract</summary>
  A faster storage device should make serving faster. We find the opposite. High-Bandwidth Flash (HBF) stacks NAND behind a wide, package-local interface, promising flash-scale capacity with far lower read latency and higher bandwidth than an SSD. The obvious move is to keep an SSD-style Mooncake KV-offloading stack and swap in HBF underneath. We built that system and measured it: an extended TokenSim, four complete two-hour Qwen-Bailian production traces, five dense and mixture-of-experts models,...
  </details>

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

- **2026-08-11** — Henry Han — [Governing Agentic AI in FinTech](http://arxiv.org/abs/2608.11344v2)
  <details><summary>📄 Abstract</summary>
  Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight. Yet agentic AI governance in FinTech is under-investigated. We argue the binding governance constraint is not capability but verifiability. We define the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability and reproducibility retained after a decision. It is indexed to a ver...
  </details>

- **2026-08-11** — Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram — [Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents](http://arxiv.org/abs/2608.11110v2)
  <details><summary>📄 Abstract</summary>
  When a tool-using agent is given the same task in a different language, does it still take the same steps? Multilingual evaluation rarely asks: it compares final answers and discards the actions. Yet those actions are the product: they fix cost and latency, decide how the system fails, and are the only auditable part of its behaviour. We make the action policy the measured object across 8 models, 6 parallel benchmarks and 41 languages (2.38M rollouts). The naive measurement fails: five confounds...
  </details>

- **2026-08-11** — Ge Yan, Jinghao Liu, Yuzhi Fan et al. — [Flex-$π$: A Multi-Stream World-Action Model with Compute Flexibility](http://arxiv.org/abs/2608.10860v2)
  <details><summary>📄 Abstract</summary>
  World-action models (WAMs) predict the future to act better, but nearly all of them predict only RGB latents, trained purely for pixel reconstruction, with no explicit signal for the 3D geometry or object semantics manipulation needs. We find a surprising free lunch: the same frozen video-generation VAE that encodes RGB also encodes 3D pointmaps almost losslessly, with no pointmap-specific training at all. This lets us supervise Flex-$π$, a 6B-parameter WAM, on 3D geometry and object-centric DIN...
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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 580 |
| prompt-injection | 488 |
| memory-poisoning | 44 |
| tool-use-attack | 116 |
| backdoor | 414 |
| adversarial-attack | 558 |
| privacy-leakage | 3832 |
| steganography | 55 |
| misuse | 891 |
| red-teaming | 115 |
| vulnerability | 2687 |
| defense | 2402 |
| alignment | 2224 |
| robustness | 2227 |
| watermark | 288 |
| unlearning | 87 |
| agent-safety | 52 |
| benchmark | 57 |
| survey | 281 |
| other | 6361 |

---

📚 **全部 23759 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-17 18:31:02*