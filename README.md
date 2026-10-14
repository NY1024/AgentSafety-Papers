<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-32642-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-14 16:21 ｜ **论文总数 / Total Papers**: 32642（近 30 天 / Recent 30 days: 5170）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 32642 篇论文（含摘要、分类筛选、搜索）/ View all 32642 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 676
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 615
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 154
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 513
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 633
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4362
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 77
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1169
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 140
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3570
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3426
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3216
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3466
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 601
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 113
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 64
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 398
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9327

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5170 篇，完整 32642 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5170 papers from the last 30 days (with date, authors & abstract). For the full list of 32642 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-10-13** — Juann Kim, Minku Kang — [Cross-Lingual Transfer of Evil Vectors Is Directionally Asymmetric](http://arxiv.org/abs/2610.17880v1)
  <details><summary>📄 Abstract</summary>
  Persona vectors are linear directions in the residual-stream activations of LLMs that encode behavioral traits and enable fine-grained control over model behavior. Among them, the evil persona vector is particularly relevant to understanding harmful behavior, jailbreak vulnerabilities, and the unlearning of harmful knowledge. Yet whether this vector reflects a genuinely cross-lingual concept, rather than an artifact of its extraction language, remains untested. We conduct a systematic evil-vecto...
  </details>

- **2026-10-13** — Amman Yusuf, Jiwoo Shin, Ruizhi Deng et al. — [The Tokens Strike Back: Safety-Aware Denoising with Directional Embedding-based Revision](http://arxiv.org/abs/2610.17636v1)
  <details><summary>📄 Abstract</summary>
  The Safety-Aware Denoiser (SAD) is a recent, training-free, safety-guidance framework for text diffusion models. During inference, SAD steers text samples toward safe regions of the token probability space. In this paper, we propose $\mathit{SADDER}$ (Safety-Aware Denoising with Directional Embedding-based Revision), which improves the safety and quality trade-offs of SAD by exploiting a safety-guidance signal in the embedding (or activation) space for each token position, then updating the toke...
  </details>

- **2026-10-12** — Mohammad Reza Mirbagheri, Amir Mahdi Sadeghzadeh — [TRAP: Tree-Guided Reinforcement-Augmented Probing for Automated LLM Jailbreaking](http://arxiv.org/abs/2610.17313v1)
  <details><summary>📄 Abstract</summary>
  Aligned large language models (LLMs) remain vulnerable to jailbreak prompts that circumvent their safety guardrails, making the identification of these vulnerabilities important for understanding and mitigating model weaknesses. Existing automated jailbreak methods explore prompt candidates or reuse attack experience, but generally do not learn over a persistent hierarchy that connects related jailbreak strategies, such as role-play, encoding, and obfuscation. This leaves the relationships among...
  </details>

- **2026-10-12** — Víctor Mayoral-Vilches — [CT0: Cybersecurity Transformer](http://arxiv.org/abs/2610.16550v1)
  <details><summary>📄 Abstract</summary>
  General-purpose frontier models are large, expensive to run, and increasingly reluctant to engage with authorised defensive- and offensive-security work. We ask the opposite question: how small can a cybersecurity-specialist transformer be while remaining genuinely useful to a security practitioner? We introduce CT0, a Cybersecurity Transformer architecture, and CT0-Micro, its first incarnation: a compact (~4B-parameter) model built on the open base model, whose backbone is specialised by two-ph...
  </details>

- **2026-10-12** — Md Mushfiqur Rahman, Tobias Rohde, Rahul Tripathi et al. — [ATTCK-R: Knowledge-Aware Long-Horizon Jailbreaking for Protected LLMs](http://arxiv.org/abs/2610.16305v1)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed behind increasingly sophisticated safety mechanisms, evaluating their robustness under realistic adversarial conditions becomes increasingly difficult and critical. Existing jailbreaking evaluations often rely on static prompts, limited interaction horizons, or lightly protected systems, failing to reflect protected deployment settings with prompt-based safety protections. We show that the introduction of a prompt-based safety protection reduces the average ...
  </details>

- **2026-10-12** — Seyedarmin Azizi, Arya Fayyazi, Parsa Razmara et al. — [The Sharp Directions Are Against You: Curvature Analysis of Activation Steering](http://arxiv.org/abs/2610.16084v1)
  <details><summary>📄 Abstract</summary>
  Activation steering adds a vector to a language model's internal representations at inference time. It is a lightweight alternative to fine-tuning for behavioral control. The standard construction, contrastive activation addition (CAA), is fragile, as on many inputs it shifts behavior in the wrong direction. To explain this fragility, we first study the geometry of the steering vector. We introduce steering Hessian, the matrix of second order derivative of the model's behavioral loss with respec...
  </details>

- **2026-10-08** — Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram — [One Word Opens the Gate: The Option-Channel Attack on Typed Decision Models as Agent Guardrails](http://arxiv.org/abs/2610.12292v1)
  <details><summary>📄 Abstract</summary>
  A typed decision model reads a piece of text and returns a probability over caller-defined options, each with a short written definition, generating no text. Recent work places these models in agent systems as guardrails: the component that reads a proposed tool call or incoming message and decides whether to allow it. We evaluate seven open-weight models in that role and report the two error directions separately: a fail-open error allows a prohibited action and is a vulnerability; a fail-close...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-10-13** — Dominik Seip, Bartol Markovinović, Matthias Hein — [Towards Safe Autonomy for Computer Use](http://arxiv.org/abs/2610.18508v1)
  <details><summary>📄 Abstract</summary>
  The safety of LLM-based agents currently rests on alignment training and safety classifiers, neither of which can rule out that a sophisticated indirect prompt injection (IPI) goes through and causes significant harm. Recent work therefore builds agents with information-flow guarantees that rely on structured tool interfaces to interact with the environment. Computer Use Agents (CUAs) act visually on the computer screen, which does not provide a boundary between trusted first-party interfaces an...
  </details>

- **2026-10-13** — Kristoffer Hempel, Nils Loose, Lorenzo Cavallaro et al. — [Kairos: Transactional Security Enforcement at the System Boundary for LLM Agents](http://arxiv.org/abs/2610.18457v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are becoming an integral part of the software development lifecycle, and the capabilities granted to them allow an agent to act with the user's authority on any resource it can access. The reach that gives an agent its utility is equally available to an attacker who can steer it. Anything an agent ingests can carry an injected instruction, and since the model does not reliably distinguish instructions from data, indirect prompt injection should be mitigated by m...
  </details>

- **2026-10-13** — Kaan Kale, Sriram Vishwanath — [Prompt-Injection Probes Learn the Conversation, Not Just the Injection](http://arxiv.org/abs/2610.18408v1)
  <details><summary>📄 Abstract</summary>
  Linear probes on a model's hidden states are used as cheap monitors for indirect prompt injection: they screen the tool outputs an agent reads and send suspicious ones to a slower second check, so every false alarm has a cost. But a probe learns whatever separates its training examples. The standard evaluation of injection probes can be passed without the model: conversation position and text lengths alone reach 0.91-0.98 AUROC. When each attack is compared with the same conversation without the...
  </details>

- **2026-10-12** — Yuetian Chen, Kaiyuan Zhang, Yuntao Du et al. — [BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views](http://arxiv.org/abs/2610.17457v1)
  <details><summary>📄 Abstract</summary>
  Browser agents need to make decisions and execute actions on behalf of users while consuming untrusted webpages, creating opportunities for malicious instructions embedded in webpages to redirect legitimate tasks. We introduce BrowseSafe++, which extends BrowseSafe from 14,719 pages to 38,675 pairs of pages. Most of its prompt injections were observed in the wild on production websites. We keep each injection unchanged and rewrite the sensitive parts of the page around it to protect privacy. Eac...
  </details>

- **2026-10-12** — Arya Fayyazi, Mehdi Kamal, Massoud Pedram — [The Agent Knew: Internal States Forecast Unauthorized Actions and Stop Them, and the Lies That Follow](http://arxiv.org/abs/2610.17301v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents sometimes act beyond their authorization and then misreport what they did. On CAPE-Bench, matched agent tasks in which one fact decides whether an action is authorized, frontier open-weight agents do both, and one behavior marks the lie: retroactive permission laundering, acting and then asking permission as if the action were pending, precedes a false report in 70% of 1081 fresh informed violations, against 8% otherwise (preregistered odds ratio 7.0); frontier agents on ta...
  </details>

- **2026-10-12** — Anning Hu, Yangyu Li, Yuqi Huang et al. — [StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge](http://arxiv.org/abs/2610.16814v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as judges to assign scalar scores that drive downstream decision-making, including tasks such as paper review and recommendation. However, LLM-as-a-Judge pipelines are vulnerable to score-hijacking prompt injection embedded in evaluated content, which corrupts scoring signals and distorts induced rankings. Existing defenses often enforce robustness by modifying the judge model itself, making safety dependent on a specific model's scale and train...
  </details>

- **2026-10-12** — Quanyan Zhu — [Computational Reflective Equilibrium for Agentic AI: A Rawlsian Alignment Scaffold for Governance](http://arxiv.org/abs/2610.16015v1)
  <details><summary>📄 Abstract</summary>
  The rapid deployment of agentic AI has introduced complex challenges for the ethics and governance of AI systems. Agents built on large language models act through tools on behalf of people, and each deployment case brings its own instructions, policies, evidence, and stakeholders, so alignment must be formed case by case. To this end, this work proposes agentic reflective equilibrium (ARE), a computational reflective equilibrium framework that serves as an ethical alignment scaffold in the agen...
  </details>

- **2026-10-08** — Luman Zhao, Minghui Xu, Yue Zhang et al. — [LTBD: Learnable Trust-Boundary Delimiters for Prompt Injection Defense](http://arxiv.org/abs/2610.11634v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) perform remarkably well on complex tasks, yet remain highly vulnerable to prompt injection attacks, where malicious instructions embedded in external data can override user intent. Existing defenses remain limited by model fine-tuning requirements, vulnerability to adaptive attacks, or reliance on brittle handcrafted prompts. We argue that a fundamental source of this vulnerability is the lack of an explicit representation of trust provenance. To address this, we int...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-10-13** — Jerrold Huang, Junwei Quan, Saiyue Lyu et al. — [SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](http://arxiv.org/abs/2610.17727v1)
  <details><summary>📄 Abstract</summary>
  Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScreen, a compact decision model trained to score skill maliciousness directly from SKILL.md in a single forward pass. On MaliciousSkillBench, SkillScreen flags 20-25% of benign skills at 99% recall on unseen attack familie...
  </details>

- **2026-10-11** — Alan Tang, Lifeng Wang, Gang Wu et al. — [SkillMarker: A KGW-Based Watermarking Method for Agent Skill Ownership Verification](http://arxiv.org/abs/2610.15725v1)
  <details><summary>📄 Abstract</summary>
  Agent skills encode operational procedures and domain expertise as reusable knowledge assets, yet their distribution in plaintext exposes them to unauthorized copying and leakage. However, practical mechanisms for skill ownership verification and leakage tracing remain underdeveloped. Watermark embedding before distribution offers a potential solution, but structured, compact skill instructions impose stringent requirements for factual and procedural accuracy. To address these challenges, we int...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 5 papers

- **2026-10-13** — Chengtao Jian, Kai Yang — [DPOison-VL: Clean Preference Poisoning in Vision-Language Direct Preference Optimization](http://arxiv.org/abs/2610.18609v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has become a widely adopted approach for aligning vision-language models (VLMs), yet the security of multimodal preference data remains largely unexplored. Existing preference poisoning attacks either corrupt explicit supervision signals or require visible triggers, making them detectable under human inspection. We introduce DPOison-VL, the first clean preference poisoning attack against VLM-DPO, which manipulates model alignment solely through imperceptible ...
  </details>

- **2026-10-13** — Xi Chen, Chunyi Zhou, Rui Zeng et al. — [FedGraph: Defending Federated Large Language Model Fine-Tuning Against Backdoor Attacks via Graph-Based Aggregation](http://arxiv.org/abs/2610.18430v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of large language models (LLMs) allows multiple clients to collaboratively adapt models without sharing raw data, offering strong privacy benefits. However, this setting is highly vulnerable to backdoor attacks, in which malicious clients manipulate their updates to induce targeted behaviors while maintaining normal performance on benign inputs.   In this work, we make a key observation specific to federated LLM fine-tuning: malicious clients tend to exhibit strong consiste...
  </details>

- **2026-10-12** — Zhifang Zhang, Qi Wei, Weitong Chen et al. — [Detecting Chain-of-Thought Hijacking in Backdoored Multimodal Large Reasoning Models](http://arxiv.org/abs/2610.16598v1)
  <details><summary>📄 Abstract</summary>
  Chain-of-thought (CoT) reasoning enables multimodal large reasoning models (MLRMs) to solve complex visual problems, but also exposes them to CoT hijacking: an adversary implants a backdoor through poisoned fine-tuning so that a visual trigger induces a hijacking turn, redirecting an otherwise faithful reasoning chain to an attacker-chosen answer. However, since the hijack acts within the reasoning chain, existing multimodal backdoor defenses designed for MLLMs that answer directly struggle to d...
  </details>

- **2026-10-11** — Mark Russinovich — [What the Model Cannot See: Covert and Provable Text Invisibility in LLMs](http://arxiv.org/abs/2610.15883v1)
  <details><summary>📄 Abstract</summary>
  Text wrapped in a trigger can be made behaviorally invisible to a language model: omitted from summaries and quotations, ignored in question answering, and left unflagged by downstream filtering. We study this selective blindness as a dual-use information-flow primitive, a supply-chain backdoor, and a white-box auditing problem. We first implement it exactly as a serving-time span veto: blocking information flow out of a marked span makes every outside activation bit-identical under same-length ...
  </details>

- **2026-10-09** — Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas et al. — [AI Models Can Provably Hide Arbitrary Capabilities](http://arxiv.org/abs/2610.13928v1)
  <details><summary>📄 Abstract</summary>
  Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-10-13** — Emory Salaun, Syed Ayon, Kaleel Mahmood et al. — [AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface](http://arxiv.org/abs/2610.18724v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of...
  </details>

- **2026-10-08** — Tao Yang, Jianying Zhou — [Does Target Alignment Mean Target Recovery? An Evidence-Ladder Study of Adversarial Claims on Contrastive Encoders](http://arxiv.org/abs/2610.11938v1)
  <details><summary>📄 Abstract</summary>
  Adversarial attacks on vision-language models optimize an image toward a text target, then cite the attacked model's similarity score as evidence of success. We ask whether that score - victim-space target alignment (VTS) - predicts recovery of the target by an independent model. We first build a measurement instrument: supervised judges outside the attacked geometry, real-target blend controls, shuffled-target negatives, and a reference level derived from a 50% target-image blend. Two preregist...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 29 papers

- **2026-10-13** — Qikun Cai, Tao Huang, Chen Hou — [Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents under Strategic Information Requests](http://arxiv.org/abs/2610.18007v1)
  <details><summary>📄 Abstract</summary>
  LLM agents now act as delegated communication intermediaries: they read private context, draft messages, and send externally visible emails on behalf of a user. Existing checker-repair defenses can reduce inappropriate disclosure, but they rely on repeated calls to a remote action LLM (the model that drafts and repairs the email) and a remote checker LLM whenever a draft fails validation. This creates a cost problem as well as a privacy problem, especially when a requester strategically asks for...
  </details>

- **2026-10-13** — Rui Yang, Yichao Xu, Zhuohao Zhang et al. — [Discovery or Memorization? A Faithful Benchmark for Real-World Business-Logic Vulnerability Discovery](http://arxiv.org/abs/2610.17542v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of cybersecurity agents in vulnerability discovery has increased the need for benchmarks that evaluate their capabilities accurately. However, synthetic benchmarks lack realism, real-life benchmarks are prone to contamination, and many existing benchmarks have already been saturated by current models. We therefore set out to develop a benchmark that is realistic, reproducible, resistant to contamination, and challenging. Our key insight is that real-life business-logic vuln...
  </details>

- **2026-10-13** — Gezhong Pan, Zhe Li, Yunfan Tao et al. — [CrossPortrait: Cross-Species Portrait Animation via Adversarial Motion Alignment](http://arxiv.org/abs/2610.17532v1)
  <details><summary>📄 Abstract</summary>
  Cross-species portrait animation, which aims to animate a source portrait of species A using a driving video of species B, is particularly challenging due to substantial anatomical differences in facial structures across species. Previous works typically fine-tune human portrait animation models on animal video datasets but often suffer from driving-species leakage. To address this, we propose CrossPortrait, a novel framework for expressive cross-species portrait animation, supporting diverse sc...
  </details>

- **2026-10-13** — Wenbin Hu, Huihao Jing, Haochen Shi et al. — [Jev-Guard: Fast Routing and Auditing Agent Actions over Editable Policy Trees](http://arxiv.org/abs/2610.18326v1)
  <details><summary>📄 Abstract</summary>
  Agent harnesses require a low-latency guardrail model together with customizable audit policies. However, deploying an auto-regressive guardrail model remains challenging: such models incur high inference latency and are often poorly aligned with customized policies. To address these problems, we present Jev-Guard, a unified model for safety classification and policy routing. We further construct a policy tree over which Jev-Guard performs routing, spanning diverse domains including content mode...
  </details>

- **2026-10-13** — Jiale Wu, Tianming Liu, Yanjie Zhao et al. — [Mobile App Analysis in the New Era: Challenges and the Road Ahead](http://arxiv.org/abs/2610.17872v1)
  <details><summary>📄 Abstract</summary>
  Mobile applications (apps) have grown into complex, multi-platform systems that support diverse services and operate within varying regulatory and distribution contexts. Traditional analysis techniques have established a strong foundation for ensuring quality, security, and compliance, but face increasing challenges as mobile apps evolve. This article presents a three-layer perspective to examine these challenges. The Artifact Layer highlights how heterogeneous code bases and protection mechanis...
  </details>

- **2026-10-13** — Gonzalo Mancera, Julian Fierrez, Aythami Morales et al. — [inLoRA-MINT: Internal Representations for Auditing Training Data in Domain-adapted LLMs](http://arxiv.org/abs/2610.18051v1)
  <details><summary>📄 Abstract</summary>
  This work investigates the application of the Membership Inference Test (MINT) to large language models (LLMs) fine-tuned with LoRA, aiming to determine whether specific samples were used during training and address concerns about data privacy, leakage, and transparency. Building on our previous LoRA-MINT framework, which relies exclusively on perplexity under a strict black-box setting, we propose an approach based on intermediate model representations, including activations and parameter-depen...
  </details>

- **2026-10-13** — Hanna Benarroch, Jamal Atif, Olivier Cappé — [Counterfactual Certification for Sequential Unlearning with Long-Run Performance Guarantees](http://arxiv.org/abs/2610.17993v1)
  <details><summary>📄 Abstract</summary>
  Certified machine unlearning ensures the proximity between the unlearned model and a model retrained without the data to be forgotten. Extending this framework to sequential deletion requests, typically arriving as groups of variable size (e.g., all records of one user or of coordinated users), is challenging. For unlearning methods based on fine-tuning on the retain sets, this leads to either degrading performance or increasing computation as the number of unlearning requests grows. For indepen...
  </details>

- **2026-10-13** — Pengcheng Huang, Zhenghao Liu, Shixin Ren et al. — [Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](http://arxiv.org/abs/2610.17816v1)
  <details><summary>📄 Abstract</summary>
  Edge-cloud collaboration combines the lower inference overhead and greater data locality of edge-side execution with the stronger capabilities of cloud-hosted models. However, as LLM agents increasingly operate in long-horizon scenarios, cloud participation becomes interleaved throughout execution rather than a one-shot decision for each query. Such interleaved participation introduces trajectory-level effects that remain insufficiently understood. To address this gap, we introduce EC2-Bench, a ...
  </details>

- **2026-10-13** — Encheng Su, Xinping Liu, Yizhou Wang et al. — [PROTEAN: Beyond De Novo Generation - Can LLM Agents Perform Text-Guided Protein Structure Editing?](http://arxiv.org/abs/2610.17765v1)
  <details><summary>📄 Abstract</summary>
  Generative AI has achieved remarkable success in de novo protein design, yet protein engineering typically begins with existing, characterized proteins. The primary demand is targeted local editing, e.g., engineering a specific region to optimize affinity, alter immunogenicity, or improve stability, while strictly preserving core catalytic motifs and overall scaffold integrity. However, no standardized framework currently exists for carrying out and evaluating such edits. In current generative-d...
  </details>

- **2026-10-13** — Jingyue Cong, Andy Song, Yang Yu et al. — [Decouple to Forget: Semantic Mediation for Sensitive Unlearning in Large Language Models](http://arxiv.org/abs/2610.17654v1)
  <details><summary>📄 Abstract</summary>
  Machine unlearning for large language models seeks to remove specified knowledge while preserving general capability, yet current methods often treat an entire response as the unit of forgetting. This coarse granularity causes unnecessary utility loss when the forget target is only a small set of sensitive facts embedded within otherwise benign explanations. In this paper, we introduce Decouple to Forget (D2F), a targeted unlearning method inspired by semantic mediation that separates sensitive ...
  </details>

- **2026-10-13** — Eli Yune, Umer Majeed, Mahesh Balan — [Capacity over TFLOPS: Memory-Centric Deployment of Large Clinical Language Models on Consumer CPUs](http://arxiv.org/abs/2610.17551v1)
  <details><summary>📄 Abstract</summary>
  The dominant barrier to running large clinical language models at the point of care is not arithmetic throughput but graphics memory: consumer GPUs cap at 4-16 GB, while the working set of a 27-billion-parameter model in 4-bit precision is 17-25 GB. We argue that the edge node should be treated as capacity-enabled (system RAM) rather than compute-limited (GPU VRAM), and we test this on commodity hardware. Using an INT4 build of a 27B open model as an architecture-faithful stand-in for a 27B medi...
  </details>

- **2026-10-12** — Damien Lo, Hong Kyu Lee, Ruixuan Liu et al. — [COMPASS: Membership Inference Attack Against Vision Large Language Models via Adaptive Noise Calibration](http://arxiv.org/abs/2610.17332v1)
  <details><summary>📄 Abstract</summary>
  Vision large language models (VLLMs) are deployed in privacy-sensitive domains, raising training-data exposure concerns. Existing gray-box membership inference attacks (MIAs) commonly rely on entropy statistics or generated descriptions, requiring costly generation with limited membership separation. Perturbation-based methods instead measure response changes but focus on large perturbations, leaving VLLM membership behavior under smaller perturbations poorly understood. We systematically charac...
  </details>

- **2026-10-12** — Shaomin Chen, Xiaorui Gong — [Logit Leakage through Floating-Point Bias Addition](http://arxiv.org/abs/2610.16790v1)
  <details><summary>📄 Abstract</summary>
  Language model APIs can expose token-specific biases while withholding logits and token probabilities. Existing bias-based extraction recovers relative logits, leaving a common additive component undetermined in ideal arithmetic. We identify a numerical side channel in floating-point bias addition that exposes information about this component through token identities alone. The channel distinguishes score vectors with identical complete unperturbed log probabilities. Our method exploits changes ...
  </details>

- **2026-10-12** — Shunyuan Bai, Yuchen Ren, Le Yang et al. — [Answer It or Not? Towards Prompt-Adapted Adversarial Images on Vision Language Models](http://arxiv.org/abs/2610.16622v1)
  <details><summary>📄 Abstract</summary>
  With the advancement in language modeling, research on adversarial images has recently shifted from image classifiers to vision-language models (VLMs). Despite the new, text-prompt-driven nature of VLMs, we find that existing VLM adversaries have largely overlooked the dynamics of text prompts. In a typical use case, adversarial images can protect visual privacy by rejecting VLMs from answering questions about the image. However, existing protections are prompt-agnostic, i.e., indiscriminately r...
  </details>

- **2026-10-12** — Xiuyuan Qi, Yi Wang, Wenjie Wang — [Differential Privacy Protected Preference Alignment on Survey Derived Data](http://arxiv.org/abs/2610.16458v1)
  <details><summary>📄 Abstract</summary>
  Preference alignment enables language models to better reflect human values, but the preference data contains sensitive information, especially when derived from surveys about political beliefs, social norms, religion, gender attitudes, and cultural values. This paper studies privacy-preserving alignment on questionnaire-derived data from the World Values Survey, where supervision takes the form of ordinal labels rather than standard pairwise rankings. Existing efforts mainly focus on general pr...
  </details>

- **2026-10-12** — Anthony Etim, Kenan Erol, Jakub Szefer — [ML-Assisted Power Side-Channel Attacks on ML Accelerators in Shared FPGAs](http://arxiv.org/abs/2610.16164v1)
  <details><summary>📄 Abstract</summary>
  Cloud providers offer on-demand access to Field-Programmable Gate Arrays (FPGAs), and multi-tenant FPGAs let multiple users share one device to improve utilization. This sharing introduces security risks: an adversary co-located with a victim on the same FPGA can mount power side-channel attacks against the victim's Machine Learning (ML) accelerator. Prior on-chip attacks on such accelerators based on Time-to-Digital Converter (TDC) sensors have recovered only small, MNIST-scale grayscale inputs...
  </details>

- **2026-10-12** — Phat T. Tran-Truong, Ha Vo, Nhut Tran et al. — [DelegateGuard: Purpose-Bound Capabilities for Delegated LLM Agent Workflows](http://arxiv.org/abs/2610.16005v1)
  <details><summary>📄 Abstract</summary>
  \textbf{(Context)} LLM agents increasingly delegate subtasks while holding authority over sensitive data, creating confused-deputy risks: an injected delegate can exfiltrate data, amplify its authority, or act after revocation. Existing leakage benchmarks expose these failures but do not constrain the authority a delegated agent may exercise. \textbf{(Methods)} We present \system, a reference monitor that converts the initiating user's authorization into attenuable capabilities over purpose, lab...
  </details>

- **2026-10-12** — Zian Yuan, Wei Li — [PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents](http://arxiv.org/abs/2610.16778v1)
  <details><summary>📄 Abstract</summary>
  Cloud graphical user interface (GUI) agents send instructions and screenshots to remote planners, exposing personally identifiable information (PII). Existing placeholder defenses mask detected spans and reuse exact strings. Fragmented or changed forms can expose PII or break entity continuity across turns. PrivacyGuard addresses this private reference problem with source-linked sanitization (SAN) and a structured reference lifecycle (REF). SAN reconstructs fragmented or overlapping evidence and...
  </details>

- **2026-10-12** — Rex Fleur, Tzula B. Propp, Sebastian Feld — [On the Computational Complexity of Blind Quantum Machine Learning](http://arxiv.org/abs/2610.17145v1)
  <details><summary>📄 Abstract</summary>
  Can quantum advantages in computational efficiency coexist with quantum advantages in privacy? In this paper, we construct and use MasonQ, a universal brickwork transpiler, to answer this question with a resounding yes. We approach this question by bridging two seemingly disparate paradigms: universal blind quantum computation (UBQC), based on measurement-based quantum computation, and quantum machine learning (QML) algorithms such as the Harrow-Hassidim-Lloyd (HHL) algorithm and quantum recomme...
  </details>

- **2026-10-12** — Cong Pang, Jiaqi Su, Chengrui Wu et al. — [Glasseek: A Transparent Recipe for Training and Trustworthy Evaluation of DeepSearch Agents](http://arxiv.org/abs/2610.16998v1)
  <details><summary>📄 Abstract</summary>
  Deep search enables language agents to solve complex information-seeking tasks through iterative web exploration. However, developing robust open-source agents remains challenging for three reasons. First, opaque trajectory-construction pipelines make training data difficult to audit and reproduce. Second, context compression can create a substantial mismatch between training and inference. Third, agents may retrieve benchmark content from the open web during evaluation, contaminating the result...
  </details>

- **2026-10-12** — Shira K. Huizing Lemstra, Tzula B. Propp — [Foundations for a Lens of Quantum Governance](http://arxiv.org/abs/2610.16939v1)
  <details><summary>📄 Abstract</summary>
  The second quantum revolution is a revolution of information. Advances in quantum computation, communication, and sensing offer new capabilities while raising questions about how quantum infrastructures will be organised, accessed, and governed. We argue that their significance for governance lies not in transforming political principles, but in how their technical and infrastructural requirements may affect existing relationships of authority, responsibility, legitimacy, and power. This paper d...
  </details>

- **2026-10-12** — Dongsheng Chen, Xiangyu Zhao, Lei Ma et al. — [Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State](http://arxiv.org/abs/2610.16414v1)
  <details><summary>📄 Abstract</summary>
  LLM-agent workflows routinely transform rich observations into plans, summaries, memories, handoffs, and other reusable state. This creates a privacy boundary that task relevance alone does not capture: an observation may be needed as evidence for a task without its full semantics being authorized to persist. We call this mismatch the purpose-to-state semantic gap. The key distinction is that evidence authority is not release authority. We introduce Purpose IR, a bounded typed intermediate repre...
  </details>

- **2026-10-12** — Zheyu Shen, Ziyao Wang, Yexiao He et al. — [HeteroVDiff: Pipelining Video Diffusion across Mobile NPU and GPU with Shared Weights](http://arxiv.org/abs/2610.16244v1)
  <details><summary>📄 Abstract</summary>
  Video generation is moving from the cloud to phones for privacy and offline use, and applications often ask for several clips at a time, so on-device video generation is a throughput problem before it is a latency problem. Contemporary mobile SoCs carry both a GPU and a neural processing unit (NPU) on shared DRAM, yet existing on-device video diffusion systems run the denoiser on one engine while the other sits idle or only decodes the finished latent afterwards. Heterogeneous designs built for ...
  </details>

- **2026-10-12** — Sunday Oyinlola Ogundoyin, Muhammad Ikram — [When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems](http://arxiv.org/abs/2610.16039v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent LLM systems (MALS) introduce a privacy-leakage problem that conventional sensitivity-based defenses miss, since information disclosed to one authorized agent can propagate through routine coordination to an unauthorized one, without compromise or malicious behavior. This motivates topology-aware enforcement that blocks unauthorized propagation while preserving authorized disclosure. We evaluate 485 scenarios across coordinator-worker, peer-to-peer, and hierarchical topologies, instru...
  </details>

- **2026-10-11** — Sheikh Samit Muhaimin, Aarthy Nagarajan — [Riemannian Suppression of Cross-Session Identity Leakage in Motor-Imagery EEG](http://arxiv.org/abs/2610.15626v1)
  <details><summary>📄 Abstract</summary>
  Electroencephalography (EEG) recorded for motor-imagery (MI) brain-computer interfaces (BCIs) carries subject-identifying structure that persists across sessions, allowing separately released sessions from the same person to be linked. Existing EEG identity protections use learned or additive perturbations and operate on representations other than the covariance geometry underlying MI pipelines. We ask whether cross-session identity leakage can be suppressed directly in this covariance represent...
  </details>

- **2026-10-11** — Ryan Thornton, Mir Mehedi A. Pritom, Maanak Gupta et al. — [Privacy Conductor: An Architectural Enforcement of Contextual Integrity in LLM-Based Document Retrieval](http://arxiv.org/abs/2610.15804v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) that retrieve internal documents within an organization must decide who may receive them. Existing approaches based on Contextual Integrity ask the model to make that decision, so access depends on probabilistic reasoning. We present Privacy Conductor, an architecture that removes the decision from the model: a deterministic gate enforces a policy written by an authority, and the model receives only what the requester may already see. On a synthetic clinical corpus of ...
  </details>

- **2026-10-11** — François Hublet, Vladimir Krsmanovic, Jesus Solano et al. — [TL;QR: Querying Temporal Discursive Patterns in Textual Corpora](http://arxiv.org/abs/2610.15712v1)
  <details><summary>📄 Abstract</summary>
  Many questions about large textual corpora concern patterns that unfold over time, such as a political group whose stance on a topic drifts from support to criticism over several years of debates. We present TL;QR (Too Long; Query with logical temporal Reasoning), a declarative query language and open-source engine for finding such temporal discursive patterns. In TL;QR, a single query combines natural-language predicates, whose truth is judged by a Large Language Model (LLM), with regular expre...
  </details>

- **2026-10-09** — Emma Norrby, Tomas Wilkinson, Per Nyblom et al. — [Event-based Action Recognition by Pre-Training on Multi-Frame Representations](http://arxiv.org/abs/2610.13856v1)
  <details><summary>📄 Abstract</summary>
  Action recognition is a crucial task in domains like robotics, patient monitoring, or surveillance. Recently, event-based action recognition has attracted much attention due to the event camera's ability to capture fast motions and its improved privacy over conventional vision cameras. While frame-based event representations work well for short event sequences, their discriminative ability declines sharply with longer and more complex event sequences. In this work, we introduce a multi-frame rep...
  </details>

- **2026-10-09** — Amirreza Zamani, Mohammad Amin Zarrabian, Parastoo Sadeghi et al. — [On Privacy Mechanism Design Under a Bounded $α$-Lift Leakage Constraint with $χ^2$-Utility](http://arxiv.org/abs/2610.13685v1)
  <details><summary>📄 Abstract</summary>
  We study the design of a statistical privacy mechanism under a bounded $α$-lift leakage constraint. An agent observes useful data $Y$, which is arbitrarily correlated with private data $X$, and releases $U$. The goal is to maximize Pearson $χ^2$-information $χ^2(Y;U)$ while satisfying the point-wise privacy constraint. This utility is an $f$-information that is nonnegative, obeys data processing, and measures the aggregate normalized change from the prior $P_Y$ to the posteriors $P_{Y|U=u}$. The...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 26 papers

- **2026-10-13** — Jinghan Zheng, Jiajun Shi — [From Relation-Specific Heads to Shared Interventions: Contextual Entrainment in Language Models](http://arxiv.org/abs/2610.18674v1)
  <details><summary>📄 Abstract</summary>
  Large language models rely on prompt context to perform in-context learning, follow formats, and adapt to local evidence. This ability, however, also raises a robustness concern: models may reuse irrelevant tokens from earlier context when answering a later query. Prior work identifies this behavior as contextual entrainment and finds attention heads whose ablation reduces it, arguing that these heads are largely task- or relation-specific. But are the mechanisms behind contextual entrainment tr...
  </details>

- **2026-10-13** — Paweł Batorski, Przemysław Spurek, Paul Swoboda — [Pin It on Anyone: Certified Targeted Displacement of Multi-Bit LLM Watermarks Without the Key](http://arxiv.org/abs/2610.18359v1)
  <details><summary>📄 Abstract</summary>
  Multi-bit watermarking embeds a message, typically an account identifier, into LLM output so that harmful text can be traced to its origin. We show an attack technique that allows to alter the watermarking message. This allows to, for example, exchange the embedded account ID to an arbitrary different one. The attacker mainly needs access to a few accounts for generating LLM output and model logits, but crucially not the secret key used to watermark. The attacker then rewrites the text, keeping ...
  </details>

- **2026-10-13** — Wenbin Chen, Jiexin Wang, Guanting Wu et al. — [SpecCloak: Probing Harmful Code Generation through Engineering Specifications](http://arxiv.org/abs/2610.17907v1)
  <details><summary>📄 Abstract</summary>
  The code generation capabilities of large language models (LLMs) can equally be misused to implement harmful functionality, underscoring the need to understand their safety behavior in response to programming requests. While request phrasing is known to influence refusal, it remains unclear whether the form in which coding task requirements are stated affects the refusal process for malicious code generation. We introduce PseudoSpec, a template that organizes functional requirements as engineeri...
  </details>

- **2026-10-13** — Xiang Li, Aichun Huang, Mingming Zhang et al. — [Same Attack, Different Judge: A First Controlled Adversarial Comparison of Jev, LLM Judges, and Purpose-Built Safety Classifiers](http://arxiv.org/abs/2610.17820v1)
  <details><summary>📄 Abstract</summary>
  TypeSafe AI's Jev is a new kind of safety judge. It generates no text and no label: it answers questions the developer defines in advance and returns a probability for each answer. The vendor admits that adversarial input can change these answers but gives no numbers. In this paper, we present the first controlled adversarial evaluation of Jev. We build a test harness that sends every system the same payload under the same policy, and run it on four public-data tasks, from rule-based ones (input...
  </details>

- **2026-10-13** — Yichi Zhang, Zhenxiang Huang, Yuyang Zhang et al. — [Rethinking Quality in Large Language Model Routing: Security-Conditioned Model-and-Budget Selection](http://arxiv.org/abs/2610.18566v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) routers reduce serving cost by choosing which model to call and how many output tokens to grant it for each query. Existing routers rank model-budget actions using a single quality metric. This does not work for mixed workloads. For ordinary queries, a good answer is correct and useful (utility); for security-sensitive queries, a good answer refuses harmful requests or resists malicious instructions (security). These two objectives prefer different models and budgets. ...
  </details>

- **2026-10-13** — Shreyasi Roy Chowdhury, Kiran Garimella — [How Safe Is ChatGPT Health Advice? Evidence from Real User Conversations in Four Global South Countries](http://arxiv.org/abs/2610.18465v1)
  <details><summary>📄 Abstract</summary>
  People increasingly bring their health questions to ChatGPT, yet safety evaluations of LLM health advice rest almost entirely on clinician-authored vignettes, synthetic prompts, or simulated user profiles. The gap is widest for the Global South, where concerns about demographic bias and unsafe recommendations are well documented but have never been tested on real usage. We present, to our knowledge, the first demographically grounded safety evaluation of real-world health conversations with Chat...
  </details>

- **2026-10-13** — Cecelia Soh, Jun Hu, Yuan Li et al. — [FRACTION: Fraud Explanation Generation via Agentic Graph Context Navigation](http://arxiv.org/abs/2610.18023v1)
  <details><summary>📄 Abstract</summary>
  Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label. An intuitive approach is to adapt existing graph-enhanced large language models (LLMs), which inject graph structure into LLMs via graph-conditioned instruction tuning or structure-aware embeddings. However, existing methods face two key challenges in graph fraud explanation generation: a lack of ...
  </details>

- **2026-10-13** — Akhil Kumar, Gregory J. Cooke — [Simulations of the Evolving Ozone Layer: Implications for the Early Earth, Exoplanets, and the Search For Life](http://arxiv.org/abs/2610.18864v1)
  <details><summary>📄 Abstract</summary>
  Over 4 billion years, Earth's atmosphere has been transformed from a composition devoid of molecular oxygen (O$_2$) to one where O$_2$ is now 21% of our modern atmosphere by volume. With high quantities of O$_2$, an ozone (O$_3$) layer can form and partially shield the surface from biologically harmful ultraviolet radiation (UV). The evolution of the O$_3$ layer has previously been simulated under the modern Sun by independent groups with separate models. Here, we present simulations of Earth's ...
  </details>

- **2026-10-13** — Irem Ecem Yelkanat, Faeze Ghorbanpour, Alexander Fraser — [Decomposing and Predicting Annotation Disagreement in Harmful Content Across Languages](http://arxiv.org/abs/2610.18588v1)
  <details><summary>📄 Abstract</summary>
  Annotator disagreement is increasingly recognized as a meaningful property of subjective tasks, rather than merely noise to be removed. Predicting which items are likely to be contested could help allocate annotation effort and route difficult cases to human review. We propose predicting disagreement from interpretable semantic properties of the text. An LLM answers a set of binary questions covering harmful-content characteristics, disagreement-related cues such as borderline severity and missi...
  </details>

- **2026-10-13** — Hoang Pham, Cong-Duy Nguyen, Dong Le et al. — [Reliable Memory from Unstable Growth: Curating Self-Written Agent Playbooks with Randomized Experiments](http://arxiv.org/abs/2610.18427v1)
  <details><summary>📄 Abstract</summary>
  Persistent textual memory lets language-model agents reuse lessons from past tasks to improve on future multi-step tasks without retraining. Systems such as ACE and Dynamic Cheatsheet keep it as a playbook: lessons the agent writes after each task and reads in its prompt. A key challenge is to decide which lessons improve later tasks. Current systems leave the decision to the agent itself, which makes performance unstable: the same procedure can write a playbook that helps or one that falls up t...
  </details>

- **2026-10-13** — Hiroshi Mano, Chie Sugiyama, Teruaki Hayashi — [Institutionalizing Trust in Data Exchange: Trust-Anchor Model of the Data Credit Guarantee Organization and Its Simulation-Based Comparison](http://arxiv.org/abs/2610.18400v1)
  <details><summary>📄 Abstract</summary>
  Data trading markets that span industries and regions are expanding, but the implicit trust that supports data use within an organization does not carry over to cross-domain exchange. This paper examines the Data Credit Guarantee Organization (DCGO), a proposal to institutionalize trust through third-party verification and certification, and asks what it means to trust data, what such certification can support, and under what conditions DCGO outperforms existing trading models. We decompose trus...
  </details>

- **2026-10-13** — Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long et al. — [SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](http://arxiv.org/abs/2610.18206v1)
  <details><summary>📄 Abstract</summary>
  We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management, and (iii) System Interaction. Across these categories, SWE-MISBEHAVIOR covers 11 distinct misbehaviors with a fully automated evaluation protocol, including coding-action violations, Create/Read/Update/Delete (CRUD) file...
  </details>

- **2026-10-13** — Luise Koch, Manuel Tonneau, Niyati Malhotra et al. — [GENDIS: Gender-Related Discourse and Stance in Multilingual YouTube Comments from India, Kenya, and Nigeria](http://arxiv.org/abs/2610.17778v1)
  <details><summary>📄 Abstract</summary>
  Research on gender-related online content is often operationalized through harm-centered tasks that collapse non-harmful gender-related and unrelated content, while existing datasets remain concentrated in high-resource languages and Global North settings. To bridge these gaps, we introduce GENDIS, a dataset of 9,600 multilingual, human-annotated YouTube comments from India, Kenya, and Nigeria (3,200 per country), annotated using a two-level framework that first identifies whether gender is refe...
  </details>

- **2026-10-12** — Tim R. Davidson, Marija Šakota, Joshua Joseph et al. — [Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions](http://arxiv.org/abs/2610.17195v1)
  <details><summary>📄 Abstract</summary>
  People increasingly delegate option-ranking tasks (e.g., shopping, job search, travel) to AI agents, which creates incentives to steer agentic decisions via "agent ads." To defend against such steering attacks, people count on models' alignment training and platforms' terms of service, and consequently the most effective existing attacks are designed to trigger off-policy behaviors. Exposing a new attack surface, we introduce on-policy attacks, which steer agentic decisions without pushing indiv...
  </details>

- **2026-10-12** — Haoming Yang, Ke Ma, Yangbangyan Jiang et al. — [Narrative Paradoxes in LLM Inference: Shaping Reasoning Trajectories toward Misalignment](http://arxiv.org/abs/2610.16312v1)
  <details><summary>📄 Abstract</summary>
  Explicit reasoning in large language models (LLMs) is often associated with reliability, yet it can still pose risks when a model infers harmful goals under a benign context. We identify a distinct challenge: ensuring the safety of the \emph{multi-step reasoning process} itself, where locally coherent steps may still lead to globally harmful outcomes. To explore this vulnerability, we propose PDRA (Paradox-driven Reasoning-based Attack), a novel attack method that programs a harmful reasoning tr...
  </details>

- **2026-10-12** — Ben Slater, Ryan Lundqvist, Leo Richter et al. — [Audit tools of the trade: Automated Auditor Elicitation Can Be Sensitive to the Context the Auditor Is Given](http://arxiv.org/abs/2610.16911v1)
  <details><summary>📄 Abstract</summary>
  Does providing additional context to automated AI auditors improve their effectiveness? Using the Petri tool to audit LLM coding agents, we test the impact of providing two types of resources (an external codebase and benchmark transcripts) to LLM auditors, across four auditor-target LLM pairs and three behaviours (harmful compliance, reward hacking, sycophancy). (1) External codebase: We provide the auditor LLM with a fixed, external open source codebase, which prior work finds improves the rea...
  </details>

- **2026-10-12** — Ram Vikas Mishra, Shashank Aggarwal, Jahnavi Kumar et al. — [Separating Prompt Harmfulness from Interaction Safety via Partial Generation](http://arxiv.org/abs/2610.16761v1)
  <details><summary>📄 Abstract</summary>
  LLM-based information systems need safety guardrails. Most guardrails classify the prompt alone. If the prompt looks harmful, the system rejects it before any answer is generated. This is costly. Many rejected prompts would have received a safe response. Users lose help they should have received from the information system. This cost grows as conversational and generative search becomes common. Prompt-level labels treat harm as a property of the query. But harm depends on what the model actually...
  </details>

- **2026-10-12** — Niyazi Ahmet Metin, Dilara Keküllüoğlu — [SarcasTraps: Effect of Sarcasm on Turkish Hate Speech Detection](http://arxiv.org/abs/2610.16957v1)
  <details><summary>📄 Abstract</summary>
  Standard hate speech detection datasets often emphasize explicit harmful language, but directed harm can also be expressed indirectly, without clearly hateful wording. Sarcasm is one such form of indirect expression, as it can convey harmful intent through mock praise, exaggeration, humor, or apparent politeness. In this paper, we introduce SarcasTraps, a targeted external test set for analyzing the effect of sarcasm on Turkish hate speech detection. SarcasTraps contains 479 entries annotated al...
  </details>

- **2026-10-12** — Runang He, Tongya Zheng, Jing Cao et al. — [CryptoFlowBench: Benchmarking Multi-Hop Reasoning on Blockchains for Cryptocurrency Fund Tracing](http://arxiv.org/abs/2610.16449v1)
  <details><summary>📄 Abstract</summary>
  Pseudonymous accounts and complex smart-contract ecosystems substantially hinder the tracing of illicit cryptocurrency fund flows. Existing Graph Neural Networks (GNNs) have achieved promising performance in blockchain fraud detection, yet their static node- or edge-level predictions do not naturally generalize to multi-hop fund tracing. Meanwhile, existing tracing methods mainly rely on predefined heuristics to capture multi-hop relationships, limiting their adaptive reasoning capabilities. To ...
  </details>

- **2026-10-11** — Alex Martí Guiu, Nicolas Zumarraga, Kevin O'Sullivan et al. — [Unfair and Unsafe: Everyday Bias Triggers Emergent Misalignment](http://arxiv.org/abs/2610.15961v1)
  <details><summary>📄 Abstract</summary>
  Emergent misalignment (EM) occurs when fine-tuning a language model to a narrow task makes it misaligned on unrelated ones. Because organizations now routinely fine-tune models on their own data, it matters which kinds of training data cause EM. So far, studies have induced EM with data containing recognized safety failures, such as insecure code or harmful advice, while biased training data is typically examined by fairness research for the bias models learn from it rather than for its effects ...
  </details>

- **2026-10-11** — Alibek Dadajonov, Hikmatillo Umarhojiyev — [Sharper Frames, Worse Rooms: Viewpoint Coverage Dominates Image Quality in Feed-Forward 3D Reconstruction](http://arxiv.org/abs/2610.15854v1)
  <details><summary>📄 Abstract</summary>
  Grounded spatial reasoning about indoor scenes rests on a geometric reconstruction that the multimodal system does not itself produce. Feed-forward multi-view reconstruction models operate under a fixed view budget, making frame selection a critical upstream decision. We show that under this setting the conventional preference for sharp frames can be actively harmful. Across nine handheld room scans, selecting the sharpest 16 of 200 candidate frames is the worst strategy we test, reaching 48\% r...
  </details>

- **2026-10-11** — Rui Tang, Hongqiu Wang — [MedHarnessBench: A Unified Benchmark for Healthcare Agent Evaluation](http://arxiv.org/abs/2610.15714v1)
  <details><summary>📄 Abstract</summary>
  Healthcare agents must transform longitudinal clinical evidence into reliable actions through heterogeneous tools and stateful workflows, conditions under which model-centric systems may lose context, misuse tools, fail to verify consequential transitions, or cross authorization boundaries. Existing medical-agent benchmarks primarily emphasize terminal task outcomes, making it difficult to determine whether execution failures arise from the agent model, the runtime harness, or their interaction....
  </details>

- **2026-10-09** — Yeonsung Jung, Zhiyuan Wang, Zifan Wang et al. — [X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems](http://arxiv.org/abs/2610.13886v1)
  <details><summary>📄 Abstract</summary>
  Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions ...
  </details>

- **2026-10-08** — Neha Verma, Sungwon Kim, Kenton Murray et al. — [VFold: Symmetry-Aware Cross-Layer Value Cache Compression](http://arxiv.org/abs/2610.12338v1)
  <details><summary>📄 Abstract</summary>
  While caching key-value (KV) states accelerates Large Language Model (LLM) decoding, this cache can dominate memory usage at long context lengths. One solution is to compress this memory by exploiting inter-layer cache similarities. However, most existing techniques necessitate architectural changes to LLMs and incur substantial overhead. In this work, we propose a symmetry-aware value cache merging strategy that reduces cache memory while avoiding both harmful performance degradation and archit...
  </details>

- **2026-10-08** — Jiaming Zhang, Xuan Wang, Fuyao Zhang et al. — [Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](http://arxiv.org/abs/2610.11942v1)
  <details><summary>📄 Abstract</summary>
  A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Judging a transition requires an expectation of what should have followed the action. Existing GUI world models provide one, but they output it as text, code, or images, so checking it against the obser...
  </details>

- **2026-10-08** — Haitong Jiang, Chunlin Liu, Sihan Tang et al. — [Same Outcome, Different Evidence: Intent Recovery in LLM Safety Evaluation](http://arxiv.org/abs/2610.11766v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations of large language models commonly summarize harmful-output behavior with attack success rate (ASR). Yet the same non-harmful outcome can arise for very different reasons. A model may recover a harmful task and refuse it, fail to recover the task, or respond to something else entirely. Distinguishing these cases becomes especially important under intent-obscuring prompts, where a low ASR does not reveal whether the evaluated task was actually engaged. To make this distinction e...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 2 papers

- **2026-10-08** — Saisab Sadhu, Shreeyans Arora, Pratinav Seth — [Cited but Not Consulted: A Counterfactual Audit of Legal Chain-of-Thought Faithfulness](http://arxiv.org/abs/2610.12361v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly justify legal decisions by naming the statute or precedent behind a verdict, treated as evidence that the decision follows from it. We test this directly: holding case facts fixed, we substitute the named legal authority for an unrelated one and decode a model's evolving verdict from its hidden states. Across seven open-weight models (8B-70B) and four benchmarks spanning judicial and contractual reasoning, when explicitly required to justify a verdict by naming...
  </details>

- **2026-10-08** — Jingnan Zheng, Dongcheng Zhang, Yi Zhang et al. — [ReSI: Recursive Safety Improvement toward Resistant and Resilient AI](http://arxiv.org/abs/2610.12233v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement, the participation of AI systems in improving their own capabilities, is beginning to move from theoretical prospect to practice, posing both challenges and opportunities for safety alignment. Models evolve through frequent updates, and their safety alignment requires continual adaptation to each new checkpoint. Meanwhile, with evolving red-teaming methods exposing new vulnerabilities, safety improvement for each checkpoint needs to mitigate exposed vulnerabilities and...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 57 papers

- **2026-10-13** — Giovanni Pio Delvecchio, Stefano Fantazzini, Giacomo Frisoni et al. — [SolBehave: Evaluating the Behavioural Correctness of LLM-Generated Smart Contracts](http://arxiv.org/abs/2610.18745v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate Solidity smart contracts that, once deployed, can never be patched, making a single latent fault permanent and exploitable. Yet current evaluations mostly ask only whether generated code compiles. We introduce SolBehave, a benchmark for evaluating the correctness of model-generated contracts at scale, moving beyond ad hoc unit tests. Across 250 real, reproducible Ethereum contracts, we apply three complementary tests of behavioural fidelity: differenti...
  </details>

- **2026-10-13** — Yuqi Huang, Xingyao Li, Yunlong Hou et al. — [SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models](http://arxiv.org/abs/2610.18735v1)
  <details><summary>📄 Abstract</summary>
  Speculative Decoding (SD) has demonstrated its efficacy in accelerating large language model inference, but for Vision-Language Models (VLMs), the diverse input modalities make it difficult for a small trained drafter to achieve consistently high throughput. Self-speculative decoding reuses parts of the target model as a drafter which retains the multi-modal capability of the VLMs, yet its efficiency depends on choosing a suitable draft configuration for each prompt. We propose Single-Peak SPecu...
  </details>

- **2026-10-13** — Simone Travagliati, Maria Luisa Merani — [Pedestrian Trajectory Prediction through LoRA Federated Training](http://arxiv.org/abs/2610.18640v1)
  <details><summary>📄 Abstract</summary>
  In Intelligent Transport Systems, protecting vulnerable road users, specifically pedestrians, is a paramount challenge. The present work contributes to this field, putting forth a distributed architecture in which vehicles connected to the cellular infrastructure collect pedestrians' trajectories and fine-tune a foundation model for pedestrian trajectory forecasting via federated training. A server positioned at the edge of the cellular network is responsible for aggregating the local model's pa...
  </details>

- **2026-10-13** — Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu — [Encrypted Skills Can Become New Security Exploits If AI Agents Know How to Decipher](http://arxiv.org/abs/2610.18262v1)
  <details><summary>📄 Abstract</summary>
  Third-party skills can expose LLM agents to malicious instructions hidden by encoding. We introduce Ciphered Skill Injection (CSI), which embeds such instructions in skill files for agents to decode and follow. We evaluate Caesar and layered variants across eight models and 139 injection-task pairs, separating instruction recovery from attack success. In the primary setting with shortened skills, the variants achieve attack success rates of up to 47.5% and 40.3%, respectively. Successful decodin...
  </details>

- **2026-10-13** — Farnaz Soleimani, Abdelghani Chibani, Yacine Amirat et al. — [Neuro-Symbolic Graph Transformers for Hierarchical Intention Recognition from Multimodal Human Activity Sequences](http://arxiv.org/abs/2610.18176v1)
  <details><summary>📄 Abstract</summary>
  Proactive human-robot collaboration requires autonomous systems to infer not only immediate actions but also the underlying hierarchical intentions governing human behavior. Current deep learning approaches predominantly focus on flat action classification, failing to capture the structural dependencies connecting kinematic motion to high-level goals. A Neuro-Symbolic Graph Transformer (NSGT) is proposed within this multimodal framework, a Human Reasoning Graph (HR-G) is integrated into the self...
  </details>

- **2026-10-13** — Xinyang Liao, Lingyu Li, Kaicheng Shen et al. — [CompanionSafe: From Multi-turn Safety Evaluation to Guardrails for AI Companions](http://arxiv.org/abs/2610.18095v1)
  <details><summary>📄 Abstract</summary>
  AI companions provide users with emotional support and ongoing companionship, but their sustained relational interactions also introduce distinct safety risks. Prior work largely targets general harms or specific companion platforms and risk categories, while relying on manually collected conversations, limiting scalable and user-grounded evaluation and mitigation. To address this, we introduce CompanionSafe, a unified evaluation-to-mitigation framework for AI companion safety. Its evaluation co...
  </details>

- **2026-10-13** — Xibo Ding, Guoxia Wang, Jinle Zeng et al. — [Virtual Head Attention](http://arxiv.org/abs/2610.17959v1)
  <details><summary>📄 Abstract</summary>
  The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill compute. We propose Virtual Head Attention (VHA), which simultaneously improves all three vertices through ...
  </details>

- **2026-10-13** — Fasheng Miao, Zhaoyu Hu, Xiang Li et al. — [ProtoArena: Can AI Agents Discover and Exploit Real-World Cross-Component Protocol Vulnerabilities?](http://arxiv.org/abs/2610.17837v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used for vulnerability analysis, yet existing benchmarks provide limited coverage of exploitation that depends on interactions among network protocol components. Such vulnerabilities arise from inconsistencies in message interpretation, timing, state, or trust assumptions across participants. We introduce ProtoArena, a black-box, multi-component, dynamic benchmark with 80 cross-component vulnerability-exploitation environments spanning 11 protoc...
  </details>

- **2026-10-13** — Tiancheng Shen, Zilong Huang, Xiangtai Li et al. — [QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](http://arxiv.org/abs/2610.17829v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Diffusion Transformers (MM-DiTs) have recently emerged as a powerful framework for unified text-vision synthesis, surpassing traditional U-Net architectures in generative tasks. One key innovation lies in its Multimodal Self-Attention (MM-SA) interaction, where image and text tokens are concatenated and processed via self-attention. However, this mechanism poses significant challenges for editing, rendering conventional U-Net-based attention manipulation methods ineffective. To addres...
  </details>

- **2026-10-13** — Bo-Ruei Huang, Daniel Seita, Erdem Bıyık — [Beyond the End-Effector: Learning Whole-Arm Contact Manipulation from Human Demonstrations](http://arxiv.org/abs/2610.17802v1)
  <details><summary>📄 Abstract</summary>
  Robot manipulation has traditionally relied on end-effector-centric interactions. In contrast, humans routinely exploit whole-arm contacts to improve efficiency, robustness, and adaptability, especially when the hands are occupied or when precise grasping is unnecessary. Enabling similar capabilities in robots remains challenging: the robot must select where on its arm to make contact, generate effective non-prehensile interactions, and satisfy task-specific pose or safety constraints on the end...
  </details>

- **2026-10-13** — Shuang Wu — [Gaussian Process Bandits for AI System Optimization with Selectively Verified Feedback](http://arxiv.org/abs/2610.17760v1)
  <details><summary>📄 Abstract</summary>
  Gaussian process bandits exploit similarities among configurations to optimize prompts, retrieval systems, and agent workflows. In these applications, however, inexpensive model-based evaluations can disagree with trusted task outcomes. We study selective verification when an action is chosen before a diagnostic is observed and trusted feedback is informative on an unknown set of diagnostic states. A finite reliability class and a finite RKHS signal dictionary describe these two sources of uncer...
  </details>

- **2026-10-12** — Haoyu Wang, Weiqiang Zhu — [Event-Centric Earthquake Monitoring with a Multi-Station Transformer](http://arxiv.org/abs/2610.17404v1)
  <details><summary>📄 Abstract</summary>
  Earthquake catalogs underpin studies such as fault structure, earthquake processes and seismic hazard, and their value depends on being both complete and reliable. Machine learning has improved individual tasks of earthquake monitoring, but processing stations independently discards the consistency of arrivals across the network, and running tasks in sequence fragments the information describing each earthquake. We present EQNet2, a geometry-aware multi-station Transformer that jointly predicts ...
  </details>

- **2026-10-12** — Gabija Pasiunaite, Ryan McMorrow, Brian Clark et al. — [VulnBump: A Benchmark for Fixing Vulnerable Dependencies in Real Projects While Keeping the Build and Tests Green](http://arxiv.org/abs/2610.17374v1)
  <details><summary>📄 Abstract</summary>
  Software composition analysis (SCA) tools report far more vulnerable dependencies than teams fix: in Snyk Open Source production data, 94% of vulnerability findings have a known fixed version, yet only about 10% are resolved. Agentic coding tools could close this gap, but no benchmark evaluates them on vulnerability-driven upgrades in real, runnable projects across ecosystems, verified independently of the agent. We present VulnBump: 307 upgrade tasks covering 2,066 fixable vulnerabilities in 43...
  </details>

- **2026-10-12** — Ankan Ganguly, Konstantinos Spiliopoulos — [Large Network limit for Latent Variable Process Models with Endogeneously Evolving Interactions among Multiple Types](http://arxiv.org/abs/2610.17369v1)
  <details><summary>📄 Abstract</summary>
  Motivated by the opinion and social dynamics literature, we rigorously study dynamically co-evolving latent space network models, where agent opinions evolve based on a latent state space model influenced by and influencing an underlying dynamically evolving graph determining their interactions. In contrast to earlier work, see [18], agents are allowed to be heterogeneous, i.e., of different types, and their dynamic evolution can capture behaviors like attraction and repulsion between and within...
  </details>

- **2026-10-12** — Tripti Shukla, Shwetha Somasundaram, Akshat Gupta et al. — [HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation](http://arxiv.org/abs/2610.17368v1)
  <details><summary>📄 Abstract</summary>
  Generative recommendation models have shown promising results by representing items as semantic IDs and generating these IDs autoregressively. We introduce an approach showing that explicitly incorporating hierarchical and attribute-level supervision into generative recommendation can simultaneously improve training efficiency and long-tail recommendation performance. Existing approaches typically optimize semantic ID prediction with a standard causal cross-entropy objective, which does not expl...
  </details>

- **2026-10-12** — Kevin J. Randles, Manuel H. Muñoz-Arias, Kevin Thompson — [Ghost unitaries for loss-resilient photonic resource-state generation](http://arxiv.org/abs/2610.17300v1)
  <details><summary>📄 Abstract</summary>
  Entangled few-photon states, such as Bell and Greenberger-Horne-Zeilinger (GHZ) states, are central resources for discrete-variable photonic quantum information processing. In many architectures, these states are generated probabilistically by first heralding single photons from biphoton sources and then interfering them in linear-optical circuits. In this work, we show that the entanglement structure of said biphoton sources can be directly exploited for noise-engineering to deliver higher qual...
  </details>

- **2026-10-12** — Chelsea Drum, Lucas Onisk, Ariana N. Brown et al. — [Optical Fourier Transform-Based Preconditioning for Large-Scale Inverse Problems](http://arxiv.org/abs/2610.17275v1)
  <details><summary>📄 Abstract</summary>
  Fast Fourier Transform (FFT)-based preconditioners provide an efficient approach for approximating inverse operators in large-scale linear inverse problems when the underlying operator structure can be exploited in the Fourier domain. Optical Fourier transforms (OFTs), the analog of digital Fourier transforms, exploit light propagation through optical systems and offer the potential for greater throughput and energy efficiency than conventional digital FFT implementations. However, practical opt...
  </details>

- **2026-10-12** — Romain Puech, Georgy Salakhutdinov, Dimitris Bertsimas — [Online LLM Personalization from Pairwise Preferences Across Users](http://arxiv.org/abs/2610.17203v1)
  <details><summary>📄 Abstract</summary>
  Large language models can answer the same question in different styles, but users' preferred styles are hidden and vary across users and questions. We study inference-time personalization through online selection from a fixed set of prompts, each representing a persona. Users arrive sequentially, each asks a short sequence of questions, and the system displays two responses per question and observes one pairwise choice. We formulate this interaction as a variant of the contextual dueling bandit ...
  </details>

- **2026-10-12** — Shubham Agarwal, Akshat Gupta, Mike Heddes et al. — [DuoDiscover: Scaling Autonomous Discovery Beyond the Evaluation Bottleneck](http://arxiv.org/abs/2610.17184v1)
  <details><summary>📄 Abstract</summary>
  Evaluation has been central to advances in AI, and it is equally critical to autonomous discovery. Yet scaling autonomous discovery to real-world engineering challenges faces a fundamental bottleneck: the cost of evaluating progress. In real settings, a single true evaluation, such as a full benchmark or serving trace, can take hours, so a search can afford only a handful of true evaluations. We present DuoDiscover, a search system that jointly discovers what to optimize and how to evaluate prog...
  </details>

- **2026-10-12** — Gonzalo Gonzalez-Pumariega, Ajay Jagannath, Adit Jain et al. — [CWE-bench: Refocusing Agentic Security from Exploitation to Defense](http://arxiv.org/abs/2610.17020v1)
  <details><summary>📄 Abstract</summary>
  Cybersecurity evaluations of AI agents have focused largely on offense, yet a working exploit does not show that an agent can make software safe. An attacker needs to exploit only one vulnerability; a defender must find and fix all of them. We introduce CWE-bench, a private benchmark of 120 held-out repository audit-and-repair tasks spanning 73 CWE types, eight languages, and all OWASP Top 10 2025 categories. Agents are given a repository to audit and a description of its threat model, but are n...
  </details>

- **2026-10-12** — Harsh Kumar, George Eilender, Ashton Anderson — [Social Priors: Descriptions of AI Users Shape How Language Models Trust and Cooperate](http://arxiv.org/abs/2610.16946v1)
  <details><summary>📄 Abstract</summary>
  Descriptions of how people use AI are becoming training data for the next generation of models. We ask whether what a model reads about its users changes how it treats people. Using contrastive synthetic-document finetuning, we train Qwen3-32B on four matched corpora built from the same 1,625 real-world usage scenarios. The corpora differ only in the predominant motive they attribute to users of AI chatbots: helping others (prosocial), exploiting others (antisocial), legitimate self-advancement,...
  </details>

- **2026-10-12** — Harvey Mannering, Zhiwu Huang, Adam Prügel-Bennett — [Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers](http://arxiv.org/abs/2610.16892v1)
  <details><summary>📄 Abstract</summary>
  Emotions are expressed on a continuum and are naturally described in the valence-arousal (VA) space. Existing VA-based image editors are typically training-based and domain-specific, limiting them to VA regions seen during training and making them brittle across datasets and domains. Meanwhile, despite producing high-quality edits, state-of-the-art foundation image editors are not continuous affective controllers: non-linear emotion representations in text encoders makes prompt interpolation poo...
  </details>

- **2026-10-12** — Kagwe A. Muchane — [The Quantum Character Transform](http://arxiv.org/abs/2610.16827v1)
  <details><summary>📄 Abstract</summary>
  Bastidas et al. (2025) highlighted the importance of exploiting group symmetries to reduce computational overhead and unify simulation methods across both condensed matter physics and ab initio quantum chemistry. I discuss the discrete character transform, which is the group Fourier transform restricted to $Z(\mathbb{C}[G])$, the center of the group algebra, where class functions form a commutative convolution algebra and irreducible characters are its spectral basis. The normalized character ta...
  </details>

- **2026-10-12** — Liujia Yao, Changsheng You, Chao Zhou et al. — [Generative Deep Learning for CSI Feedback in Massive MIMO via Channel Distribution Prediction](http://arxiv.org/abs/2610.16796v1)
  <details><summary>📄 Abstract</summary>
  Existing deep-learning-based channel state information (CSI) feedback methods reduce feedback overhead by compressing high-dimensional CSI into low-dimensional representations and/or exploiting historical CSI to predict future CSI. However, these methods may become unreliable when user equipment (UE) suddenly changes its motion. To address this issue, we propose a prediction-aided coding (PAC) framework for generative CSI feedback, which adaptively encodes CSI based on predicted channel/CSI dist...
  </details>

- **2026-10-12** — Mengtan Zhang, Yu Ma, Shiqi Jiang et al. — [The Midas Touch for Metric Depth: Interpretable Metricization for Generalizable Depth Perception](http://arxiv.org/abs/2610.16749v1)
  <details><summary>📄 Abstract</summary>
  Recent foundation models have drastically improved the generalization of monocular relative depth estimation, yet recovering accurate metric depth from their estimates for depth perception tasks remains challenging due to scale ambiguity and local metric-scale inconsistency. Existing approaches recover metric depth from sparse observations using either explicit global affine transformation algorithms or implicit data-driven depth completion networks. The former cannot accommodate spatially varyi...
  </details>

- **2026-10-12** — Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al. — [Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration](http://arxiv.org/abs/2610.16545v1)
  <details><summary>📄 Abstract</summary>
  Feature caching has become a mainstream training-free strategy for accelerating video diffusion models by reusing intermediate outputs across denoising steps. However, existing adaptive methods rely on heuristic difference measures misaligned with actual generation quality, employ a single global threshold that ignores heterogeneous phase dynamics, and never validate their budget estimates against true approximation error, allowing systematic bias to propagate uncorrected. We propose \textbf{Ali...
  </details>

- **2026-10-12** — Dieter Teichrib, Fabian König, Moritz Schulze Darup — [Towards learning-enhanced solvers for multi-parametric optimization](http://arxiv.org/abs/2610.16520v1)
  <details><summary>📄 Abstract</summary>
  Neural networks (NNs) have been employed in various ways to accelerate the solution of multi-parametric optimization problems (OPs), which prominently arise in model predictive control (MPC). Early approaches focused on approximating the parametric solution (e.g., the optimal control law) directly by NNs. More recently, learning-based techniques have been used to emulate or enhance solver iterations. For the direct approximation of the parametric solution, it has been demonstrated that exploitin...
  </details>

- **2026-10-12** — Zhixiong Zhuang, Jin Jia, Zhiwei Shang et al. — [AuthGateBench: Benchmarking LLMs as Authorization Gate](http://arxiv.org/abs/2610.16426v1)
  <details><summary>📄 Abstract</summary>
  Automated approval systems let coding agents execute high-risk actions with minimal human oversight by delegating the authorization decision to a classifier, typically a large language model (LLM). Such systems, adopted in tools like Claude Code and Codex, remain vulnerable to failure modes such as scope escalation, where the agent takes actions exceeding what the user authorized. Existing benchmarks focus mainly on malicious requests, evaluating refusal under an implicit policy. We introduce Au...
  </details>

- **2026-10-12** — Tetsu Mizumachi — [Spectral stability of resonant Y-solitons for the KP-II equation](http://arxiv.org/abs/2610.16378v1)
  <details><summary>📄 Abstract</summary>
  The KP-II equation was introduced by Kadomtsev and Petviashvili to explain the transverse stability of line solitary waves in shallow water. Using Darboux transformations, we prove the spectral stability of Y-shaped line solitons in an exponentially weighted space that captures the amount of waves receding behind the line solitons. We show that the spectrum of the linearized operator consists of the continuous spectrum of the zero background together with three residual spectral domains whose bo...
  </details>

- **2026-10-12** — Hangil Park, Seungheon Kim, Tae-Kyun Kim — [Anomaly-Guided Observation and Two-Level Semantic Feedback for Training-Free Video Anomaly Analysis](http://arxiv.org/abs/2610.16324v1)
  <details><summary>📄 Abstract</summary>
  Training-free language-based video anomaly detection (VAD) uses frozen vision--language models (VLMs) and large language models (LLMs) to localize abnormal events without task-specific model-weight optimization. Existing approaches increasingly exploit broader temporal and semantic context, yet generic context does not necessarily foreground abnormal events or specify how video-level semantics should modify local anomaly scores. We introduce a training-free semantic feedback framework that uses ...
  </details>

- **2026-10-12** — Joel Shor, Subhashini Venugopalan — [AutoNovo: Agentic Program Search Discovers Transferable Nucleic Acid Design Algorithms](http://arxiv.org/abs/2610.16232v1)
  <details><summary>📄 Abstract</summary>
  In-silico optimization of nucleic acids relies on predictive oracles that imperfectly capture biological function, so sequences optimized against one model may exploit model-specific artifacts and fail to generalize to independent models. Recent studies have shown that not all designers generalize equally well to independent models. In this work, we use agentic program search to iteratively propose, execute, evaluate, and revise code for nucleic-acid designers. We describe the successful strateg...
  </details>

- **2026-10-11** —  Aashay Arora on behalf of the CMS Collaboration — [Using Line Segment Tracking to enable ML-based Track Reconstruction in CMS](http://arxiv.org/abs/2610.15963v1)
  <details><summary>📄 Abstract</summary>
  High-pileup conditions in CMS during the HL-LHC era make charged-particle tracking increasingly challenging as detector occupancy and combinatorics grow. We present a hybrid approach that exploits Line Segment Tracking (LST) objects rather than individual hits to enable the first CMS ML-based track reconstruction algorithm. The LST objects, namely the triplets used in this study, are built according to geometry- and physics-driven criteria and carry richer local structure, geometrical cues, and ...
  </details>

- **2026-10-11** — Ali Mohaghegh, Cheng Huang — [Self-Adaptive Model-Order Reduction for Shock-Dominated Problems](http://arxiv.org/abs/2610.15944v1)
  <details><summary>📄 Abstract</summary>
  Projection-based model-order reduction (MOR) offers a promising approach for accelerating expensive full-order model (FOM) by constructing reduced-order models (ROMs) that retain the majority of FOM accuracy while significantly reducing the computational cost. However, conventional static ROMs, often following offline/online training strategy, can exhibit limited predictive capability for convection-dominated problems featuring strongly evolving physics such as shocks. Adaptive ROMs emerge as a ...
  </details>

- **2026-10-11** — Chong Zeng, Ziqian Zhong, Kexun Zhang et al. — [Scalable Weak-to-Strong Verifier Hardening for Agent Environments](http://arxiv.org/abs/2610.15924v1)
  <details><summary>📄 Abstract</summary>
  Agent environments are essential for large language model (LLM) development. They use programmatic verifiers to turn complex outcomes into rewards. Verifiers can be attacked into awarding full credit to cheating agents without completing the intended task, causing inaccurate evaluation and misalignment in training. As agent environments scale in numbers and difficulty, so must the repairing of exploitable verifiers. To this end, we ask whether today's model with scaled compute can automatically ...
  </details>

- **2026-10-11** — Xingke Yang, Sicong Li, Lingfeng Yao et al. — [Fast and Accurate: Improving Personalized LLM Performance by Semantic Concentration Inspired Workload Split between RAG and Fine-Tuning](http://arxiv.org/abs/2610.15921v1)
  <details><summary>📄 Abstract</summary>
  With ever increasing personalized large language model (LLM) services, the next question to answer is how to improve the quality of services/users' experiences, which is indicated by personalized LLM generation accuracy/quality and inference latency. Although state-of-the-art designs, e.g., parameter-efficient fine-tuning (PEFT), retrieval-augmented generation (RAG) or Full PEFT+RAG, can help, they largely ignore the heterogeneous semantic concentrations of users' historical data and cannot full...
  </details>

- **2026-10-11** — Yanan Ma, Yihang Tao, Zhengru Fang et al. — [Mobility Helps Learning: Unsupervised Model Adaptation for Object Recognition via Movement](http://arxiv.org/abs/2610.15846v1)
  <details><summary>📄 Abstract</summary>
  Movable agents, such as autonomous vehicles and robots, should be able to autonomously adapt their pre-trained object recognition models to new environments without human annotations. While existing test-time adaptation (TTA) methods address label-free model adaptation, they typically treat test data as independent snapshots, without constructively exploiting a rich, unique source of supervision: the significant variance in prediction quality as an agent observes the same object from different d...
  </details>

- **2026-10-11** — Haosen Wang — [Who Sets the Pace of Judge Hacking? Judge Capability versus the Policy-Judge Gap](http://arxiv.org/abs/2610.15778v1)
  <details><summary>📄 Abstract</summary>
  When a policy is trained with GRPO against a frozen, reference-free LLM judge, the judge accepts more of its answers, but in a post-hoc analysis we detect no gain in held-out greedy accuracy: in all 12 (policy, judge) cells, the seed-mean gain never exceeded 0.04. A gold-reward control with the same recipe raised the 1.5B policy's greedy accuracy by +0.054 [0.013, 0.096], so for this policy the flat accuracy is specific to the judge reward; for the 0.5B policy, gold reward also gave no detectabl...
  </details>

- **2026-10-11** — Junming Liu, Marcel Böhme — [LLM-based Code Auditing by Inferring and Evaluating Developer Assumptions](http://arxiv.org/abs/2610.15729v1)
  <details><summary>📄 Abstract</summary>
  When we see a null pointer check, we know that the developer believes that the pointer may not be initialized. If the same pointer is later used without a null pointer check, we may consider this a violation of the developer's belief and ultimately a bug. We develop such a belief-guided program analysis for vulnerability detection (VD). For example, when an authentication function returns the same error for both, a wrong user name and a wrong password, an auditor may infer that the developer bel...
  </details>

- **2026-10-11** — Xiaotian Ye, Chunyao Yang, Xiaohan Wang et al. — [Generalizable Model Editing Could Be More Than Direct Generalization](http://arxiv.org/abs/2610.15707v1)
  <details><summary>📄 Abstract</summary>
  A central desideratum in model editing is generalization to complex tasks, which prior work formalizes under a direct generalization paradigm: treating and evaluating LLM behavior as an input-output mapping and expecting a factual update to alter outputs on reasoning tasks. Yet despite substantial empirical effort, the field consensus remains that such generalization is highly challenging and elusive. However, when we deploy the latest models in an in-the-wild chatbot-user setting, we surprising...
  </details>

- **2026-10-11** — Chen Shu, Chengyang Zhang, Boyu Fu et al. — [ProtoPur: Prototype-Purity Pseudo-Labeling for Weakly Supervised Instance Learning in Pathology](http://arxiv.org/abs/2610.15669v1)
  <details><summary>📄 Abstract</summary>
  Weak bag-level labels are widely available in computational pathology, whereas reliable instance-level annotations for whole-slide images remain expensive and ambiguous. Weakly supervised multiple instance learning (MIL) achieves strong bag-level classification, but instance-level supervision from attention scores, model predictions, negative bags, or spatial refinement may fail to identify class-specific local evidence. We propose ProtoPur, a prototype-purity pseudo-labeling method for weakly s...
  </details>

- **2026-10-11** — Xiuming Liu, Le Gai, Zhiyuan Chang et al. — [Agent-Canary-Mas: End-to-End Evaluation of Protocol Risk in Long-Horizon Multi-Agent Systems](http://arxiv.org/abs/2610.15529v1)
  <details><summary>📄 Abstract</summary>
  Agent-to-agent protocols allow LLM agents to discover peers, exchange results, and coordinate tool use. A locally successful protocol attack, however, may be rejected by a later agent or propagated into a consequential task decision. Measuring local exploitability alone leaves this difference unresolved and provides limited evidence about which participant caused the final outcome.   We present Agent-Canary-Mas, an end-to-end evaluation system that follows protocol risk through long-horizon mult...
  </details>

- **2026-10-09** — Md Nazmul Islam Ananto, Pierre Prevost-Avenel, Colin Smith et al. — [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](http://arxiv.org/abs/2610.13651v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as agents that interact with external software through tools, with an orchestration layer translating model outputs into structured tool invocations. This architecture creates an LLM-orchestrator-tool trust boundary where tool semantics may go unenforced and LLM-generated arguments may be incorrectly treated as trusted. We present ToFu, a tool-aware framework that automatically derives semantic security checks for LLM tools from their existi...
  </details>

- **2026-10-08** — Abbas Raftari — [From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents](http://arxiv.org/abs/2610.12463v1)
  <details><summary>📄 Abstract</summary>
  In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems to agents pursuing simulated cyber tasks. In a separately reported evaluation, Google's Gemini access...
  </details>

- **2026-10-08** — Shashank Hegde, Alexander Popov, Elie Aljalbout et al. — [LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC](http://arxiv.org/abs/2610.12407v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) predict actions and future observations, typically from a reconstruction-based representation that carries noisy, redundant information which can complicate downstream predictions. We introduce LeWAM, a bidirectional transformer for forward, backward, inverse dynamics and policy prediction, on a decoder-free JEPA latent trained end-to-end through all four modes. We see the following benefits: 1) Alignment: linear probes read robot and object state from LeWAM's latent b...
  </details>

- **2026-10-08** — Jialu Wang, Ruichen Zhang, Xiaoou Liu et al. — [GeoReform: Reflective Formalization Evolution for Multimodal Geometry Problem Solving](http://arxiv.org/abs/2610.12391v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) often struggle to identify and use geometric relations in diagrams. Recent methods address this challenge by converting geometric entities, relations, and constraints into explicit textual representations for the model to reason over. However, effective formalization is highly non-trivial: on Geometry3K, structure injection fixes 28 errors but introduces 13 new ones among 200 examples. Redundant relations can distract the model, while ambiguous references...
  </details>

- **2026-10-08** — Adhila Nazarudeen, Silvia Ortín, Apostolos Argyris — [Spatiotemporal computing for temporal nonlinear tasks using few-mode fiber and SOA nonlinearity](http://arxiv.org/abs/2610.12173v1)
  <details><summary>📄 Abstract</summary>
  Step-index few-mode fibers (FMFs) provide a compact passive platform for high-speed photonic information processing by exploiting modal dispersion to map temporal inputs into spatiotemporal representations with short-term memory. In previous studies, we have demonstrated linear classification tasks with such FMFs, such as ultrafast multibit header recognition. Here, we extend the computational capability of such architectures towards solving nonlinear tasks by introducing an optical nonlinearity...
  </details>

- **2026-10-08** — Georgios Milis, Tom Sander, Tomáš Souček et al. — [Could LLM Watermark Detection be Public?](http://arxiv.org/abs/2610.12106v1)
  <details><summary>📄 Abstract</summary>
  Watermarking large language models is popular for tracing chatbot and agentic outputs, yet detectors remain unreleased since exposing them could let attackers do targeted edits with the detector's feedback. However, watermarks are already vulnerable to uninformed tampering attacks. We thus first quantify whether a public detector would be an additional liability in a deployment setting at varying levels of access, from token-level scores to a binary verdict. Second, we introduce a split-key publ...
  </details>

- **2026-10-08** — Yutong Xie, Jiawei Tang, Zhenglin Hua et al. — [Do Not Train Away Uncertainty: Early Uncertainty Anchored Calibration](http://arxiv.org/abs/2610.12048v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks, including large language models, have achieved remarkable performance across various tasks. However, they are prone to overconfidence during training or fine-tuning. In this work, we observe a consistent phenomenon across different models that the early model is better calibrated, while later training or fine-tuning yields marginal accuracy gains but substantially increases calibration errors. Our analysis suggests that the early model retains uncertainty awareness in both ...
  </details>

- **2026-10-08** — Daniel Thilo Schroeder, Philipp M. Lutscher, Samba Dialimpa Badji et al. — [Automated Disinformation and Malicious AI Swarms: Risks for Democracy and Development in Africa](http://arxiv.org/abs/2610.11930v1)
  <details><summary>📄 Abstract</summary>
  Generative artificial intelligence is reshaping how information is produced, accessed, and circulated, while enabling disinformation campaigns of increasing scale and sophistication. There is currently no clear evidence that fully autonomous AI swarms conduct influence operations at scale, but their enabling capabilities are advancing. We define malicious AI swarms as coordinated, persistent, and adaptive multi-agent systems designed for influence operations, distinguishing them from AI-assisted...
  </details>

- **2026-10-08** — Steve Nouyep, Sébastien Salva, Maxime Puys — [A Security Meta-Model for Retrieval-Augmented Generation Systems](http://arxiv.org/abs/2610.11893v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems extend large language models (LLMs) with external knowledge through a multi-stage pipeline. While this architecture can improve the factual grounding of generated answers, it introduces structural attack surfaces that extend beyond those of standalone LLMs. In this paper, we introduce a security meta-model that captures explicit causal relationships between RAG surfaces, attacks, weaknesses, risks, and CIA impact (Confidentiality, Integrity, Availabil...
  </details>

- **2026-10-08** — Varun Gumma, Navonil Majumdar, Soujanya Poria — [SemField: A Simple, Linear, Continuous, yet Robust Semantic Watermark](http://arxiv.org/abs/2610.11848v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of Large Language Models (LLMs) necessitates reliable watermarking techniques to identify AI-generated text and ensure appropriate attribution. While token-based watermarks are vulnerable to paraphrasing, a central challenge for semantic watermarking is to turn sentence meanings into a stable, well-calibrated document-level signal. To this end, we introduce SemField, a simple, training-free semantic watermark that embeds a continuous, linear signal directly into the sente...
  </details>

- **2026-10-08** — Heyang Tan, Chengxin Gao, Xin Wen et al. — [ObliVul: Alert-Conditioned Safety Obligation Modeling and Bidirectional Counterfactual Validation for Code Vulnerability Detection](http://arxiv.org/abs/2610.11801v1)
  <details><summary>📄 Abstract</summary>
  In real-world software development, the primary challenge in vulnerability detection is often not finding suspicious code, but identifying which alerts among the large number of candidate alerts produced by static analysis truly warrant attention. Existing learning-based methods mainly identify suspicious patterns at the function or line level, making it difficult to extract complete program evidence centered on an individual alert. Although large language models can infer risk sources, dangerou...
  </details>

- **2026-10-08** — Simon Gabet, Etienne Boursier, Claire Boyer — [Softmax Attention on Gaussian Mixtures: Linear When It Can, Selective When It Must](http://arxiv.org/abs/2610.11798v1)
  <details><summary>📄 Abstract</summary>
  Softmax attention, at the heart of Transformers, has demonstrated remarkable capabilities. Yet its underlying mechanisms remain only partially understood. Recent theoretical work studies Gaussian prompts, where the infinite-prompt limit reduces softmax attention to a linear map, but also removes the query-dependent selection that distinguishes it from linear attention. This work studies the infinite-prompt limit of softmax attention on Gaussian mixtures, which retain the tractability of Gaussian...
  </details>

- **2026-10-08** — Thang X. Vu, Cuong Le, Symeon Chatzinotas et al. — [Distributed Constrained Resource Management in 6G Networks: A Scalable Hybrid Model-Learning Framework](http://arxiv.org/abs/2610.11739v1)
  <details><summary>📄 Abstract</summary>
  Radio Resource Management (RRM) is a fundamental challenge in 6G wireless networks, particularly under dynamic user demands, inter-cell interference, and heterogeneous QoS constraints. Centralized optimization solutions are often infeasible in practice due to the lack of system-wide state information, dynamic conditions, and signaling delays, making distributed learning-based approaches attractive. However, conventional multi-agent reinforcement learning (MARL) struggles with scalability and con...
  </details>

- **2026-10-08** — Haobo Jiang, Liang Yu, Jianmin Zheng — [PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors](http://arxiv.org/abs/2610.11612v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses multiview RGB-D point cloud registration, aiming to estimate global rigid poses for unordered RGB-D scans and align them in a metrically consistent coordinate frame. The conventional pairwise-then-global paradigm suffers from locally optimized pairwise registration, severe error propagation and high computational burden. In particular, existing methods typically treat RGB data as a mere auxiliary matching cue and overlook the holistic geometric priors (e.g., camera poses and...
  </details>

- **2026-10-08** — Li Lu, Yanjie Zhao, Hongjie Chen et al. — [Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery](http://arxiv.org/abs/2610.11602v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can spend millions of tokens during vulnerability discovery without producing a working proof of concept (PoC). What consumes that budget, and why does it fail to produce results? We diagnose these costs and failures through a multi-axis open-coding study of 200 CyberGym traces, spanning four agents (i.e., Codex, OpenCode, Cybench, and EnIGMA) under an unaided baseline and four existing efficiency methods. The study reveals three key findings. First, different agents vary substantiall...
  </details>

- **2026-10-08** — Shunpu Tang, Qianqian Yang, Seung-Woo Ko et al. — [Model-Driven Deep Learning with Rank-One Sensing for Efficient CSI Feedback](http://arxiv.org/abs/2610.11558v1)
  <details><summary>📄 Abstract</summary>
  Downlink channel state information (CSI) feedback is essential for beamforming optimization in frequency-division duplex (FDD) massive multiple-input multiple-output (MIMO) systems. However, the feedback overhead increases with the number of antennas and subcarriers, posing a major challenge to practical deployment. Although recent deep learning (DL)-based methods reduce this overhead by compressing CSI at the user equipment (UE) and reconstructing it at the base station (BS), most of them treat...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 55 papers

- **2026-10-13** — Tobias Hürten, Johannes F. Loevenich, Florian Spelter et al. — [Autonomous Cyber Operations Gym for Training and Evaluating AI Models for Defence](http://arxiv.org/abs/2610.18594v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes an Autonomous Cyber Operations (ACO) gym, a unified framework integrating high-fidelity network emulation, realistic user behaviour modelling for benign network traffic and adversarial profiles, and the generation of cybersecurity scenarios through open toolkits. By supporting live and deferred feature extraction at the packet and flow levels, the gym facilitates the creation of labelled synthetic datasets for training Deep Neural Network (DNN)-based Intrusion Detection Syste...
  </details>

- **2026-10-13** — Oscar Mogollon-Gutierrez, Mohammadhossein Homaei, Alberto Lopez-Trigo et al. — [BALLAST: Physics-Aware Moving Target Defense for Industrial Control Systems Using a Digital Twin Safety Oracle](http://arxiv.org/abs/2610.18311v1)
  <details><summary>📄 Abstract</summary>
  Industrial Control Systems run on static network configurations, which leaves an attacker unlimited time to map the plant. Moving Target Defense answers this by shuffling addresses, but almost every published scheme never checks whether the reconfiguration will itself disturb the physical process it protects, so the defense can destabilise a control loop or trip an actuator. We present BALLAST, which places a learned Digital Twin between the security policy and the plant as a safety oracle. A ph...
  </details>

- **2026-10-13** — Yedidel Louck, Amit Dvir, Ariel Stulman — [Standing, Not Truth: Who May Say What About Whom in Agentic Selection](http://arxiv.org/abs/2610.17952v1)
  <details><summary>📄 Abstract</summary>
  Software agents increasingly choose on a user's behalf among competing offerings described by the parties who benefit. A lawful participant, publishing under its own identity, compromising no channel and issuing no instruction, can move that choice with a single false factual claim about a competing offering.   Across twelve published defenses spanning the three placements a check can occupy, none separates it from marketing. Each accepts it for a reason correct on its own: its origin is a lawfu...
  </details>

- **2026-10-13** — Sergey Pletenev — [Perturbation, Not Provenance: Why Activation Steering Does Not Make a Robust Text Watermark](http://arxiv.org/abs/2610.17810v1)
  <details><summary>📄 Abstract</summary>
  Linear directions in the activation space of large language models causally and universally influence model behavior. This suggests that they might serve as a basis for a robust text watermark. The idea is to steer the generation along a specific semantic direction and then recover the mark by probing the activations of the re-encoded text. We test this hypothesis by conducting a series of experiments. We vary the strength of the steering and use four different directions (formality, sentiment, ...
  </details>

- **2026-10-13** — Zeeshan Zulkifl Shah, Muhammad Ikram, Dali Kaafar et al. — [Beyond Model Scaling: Rethinking Sequence Construction for Transformer-based Network Intrusion Detection](http://arxiv.org/abs/2610.17725v1)
  <details><summary>📄 Abstract</summary>
  Transformer-based network intrusion detection systems (NIDS) have shown strong potential for detecting multi-stage cyberattacks, yet most methods construct input sequences using fixed temporalization schemes rather than treating sequence construction as a systems design decision. In flow-based intrusion detection, timestamp-based windowing often fragments related attack activities while merging unrelated communications, reducing the behavioral context available to transformers. We present a unif...
  </details>

- **2026-10-13** — Jiageng Liu, Seth Z. Zhao, Zewei Zhou et al. — [AutoAgent0: An Agentic Runtime for Safe Closed-Loop Driving](http://arxiv.org/abs/2610.18866v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous driving requires more than accurate planning at a single frame: it demands reliable closed-loop execution in dynamic environments. Although end-to-end driving policies have advanced rapidly, the accumulated closed-loop errors, especially in unseen scenarios, can push vehicles into states from which the same policy struggles to recover. We address the challenge by treating closed-loop driving safety as a test-time execution problem. We introduce AutoAgent0, an agentic runtime and ...
  </details>

- **2026-10-13** — Zheye Deng, Sha Li, Changlong Yu et al. — [Beyond the Verdict: Agentic Code Judging with Verifiable Feedback](http://arxiv.org/abs/2610.18760v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling for large language models (LLMs) can involve generating multiple candidate solutions for selection or revising an earlier attempt. To guide selection and revision, we need a verifier that can estimate candidate correctness and provide evidence of failure. In competitive programming, however, official judging systems provide authoritative verdicts under finite submission budgets, without revealing failure explanations or failing inputs. To provide informative feedback without co...
  </details>

- **2026-10-13** — Jingbo Xu, Jianjie Fang, Zhuohang Li et al. — [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](http://arxiv.org/abs/2610.18697v1)
  <details><summary>📄 Abstract</summary>
  World models (WMs) and world-action models (WAMs) focus on future world prediction and executable action generation, respectively. Although these models learn shared physical dynamics and interaction semantics from embodied trajectories, they are typically trained in isolation, which restricts knowledge reuse between prediction and control. The central challenge is therefore to develop a unified learning framework that shares these dynamics while preserving the distinct modeling capabilities req...
  </details>

- **2026-10-13** — Songruo Chen, Yuqian Fu, Yu Li et al. — [EgoOmniWorld: Unifying Egocentric Understanding via Ego-Action-World Interactions](http://arxiv.org/abs/2610.18499v1)
  <details><summary>📄 Abstract</summary>
  Egocentric video understanding spans diverse capabilities, modalities, and evaluation formats, yet these are often studied in isolation despite their tight coupling in real-world interaction. We propose the Ego-Action-World interaction loop as a unifying principle: the wearer perceives the world, forms goals, acts, changes the world, and uses feedback to guide subsequent behavior. Based on this view, we introduce EgoOmniWorld, a benchmark organized around four complementary interaction structure...
  </details>

- **2026-10-13** — Brain Xiao, Sarah Wilson — [Readout Scaling Shapes Sparse Feature Recovery](http://arxiv.org/abs/2610.18462v1)
  <details><summary>📄 Abstract</summary>
  Readout scaling changes what a sparse autoencoder (SAE) learns, but the benefit of removing it depends on the data. We use readout-canonicalized decision-space (RC-DS) coordinates to remove singular-value gains while preserving retained decision information. At a fixed readout condition number, changing the generating distribution reverses which training coordinates recover known factors best. In our controlled coordinate-matching study, recovery is highest when training restores the space in wh...
  </details>

- **2026-10-13** — Hoang Pham, Duc Anh Vu, Duy Tung Doan et al. — [Copying Is Not Grounding: Training Faithful Long-Form RAG with Authored-Sentence Credit](http://arxiv.org/abs/2610.18442v1)
  <details><summary>📄 Abstract</summary>
  In search engines and assistants, long-form RAG answers can mislead readers with claims their sources do not support. Faithfulness rewards, the share of supported sentences, train models toward fewer such claims. We show that these rewards are hacked by copying. A sentence copied from the passages is supported almost by construction, so trained models learn to copy rather than ground what they write. Common defenses only move the hack: a KL or copy penalty leaves copying in place or trades it fo...
  </details>

- **2026-10-13** — Pan Yin. Shuai Yang, Yuanhao Liu, Datao Tang et al. — [Omni-RS: Unifying Multi-Task Understanding and Generation in Remote Sensing](http://arxiv.org/abs/2610.18323v1)
  <details><summary>📄 Abstract</summary>
  Practical remote sensing applications often require both understanding and generation capabilities for the same geographic scene. However, most existing methods address either understanding or generation in isolation, while existing unified remote sensing models' generative ability is limited to text-to-image. To bridge this gap, we propose Omni-RS, a unified framework supporting four remote sensing understanding tasks and five generation tasks. Specifically, we introduce the "Scene-Guided Two-S...
  </details>

- **2026-10-13** — Md Asiful Islam, Fahmida Alam, Mihai Surdeanu — [Efficient Safety Guardrails through Latent Dual-Hypothesis Reasoning with On-Demand Trace Reconstruction](http://arxiv.org/abs/2610.18304v1)
  <details><summary>📄 Abstract</summary>
  Guardrail approaches that rely on reasoning-based large language models (LLM) improve safety decisions, but come with substantial inference overhead due to the explicit reasoning. We introduce LR-Guard (Latent Reasoning Guardrail), an efficient and explainable guardrail that jointly learns structured latent reasoning and on-demand reasoning reconstruction. Our method distills a frozen teacher's analysis of safe and unsafe prompt interpretations and their comparison into compact latent representa...
  </details>

- **2026-10-13** — Cheng Hua, Taro Tsuchiya, Nicolas Christin et al. — [Holding Agents Accountable with Verifiable Agent Insurance](http://arxiv.org/abs/2610.18230v1)
  <details><summary>📄 Abstract</summary>
  While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI), a framework for agent providers to commit financially to promises, a list of programmatically-specified policies that an agent is meant to follow. These promises are embedded in a smart contract on an immutable ledger ...
  </details>

- **2026-10-13** — Pawel Olszowiec, Paulina Tomaszewska, Maciej Żelaszczyk et al. — [Monitoring latent reasoning in looped language models](http://arxiv.org/abs/2610.18127v1)
  <details><summary>📄 Abstract</summary>
  Looped language models (LMs) reuse one block of layers several times per token generation, promising more latent computation at no additional storage cost. Despite their rising popularity, the analysis of looped LMs is still in its infancy: little is known about whether the iterative transformations actually improve their capabilities, or whether these models remain stable under prompt perturbation. We construct an inspection protocol rooted in Mechanistic Interpretability comprising five divers...
  </details>

- **2026-10-13** — Zhan Yang, Tiancheng Shen, Weijie Lyu et al. — [COMPASS: Contextual Moment Prior Alignment for Generalizable AIGI Detection](http://arxiv.org/abs/2610.18034v1)
  <details><summary>📄 Abstract</summary>
  Generalizable AI-generated image (AIGI) and deepfake detection remain challenging due to the asymmetry phenomenon, where adaptation to limited training distributions can degrade the transferable representations of Vision Foundation Models (VFMs). Recent subspace adaptation methods mitigate this issue by freezing high-magnitude principal components while adapting the residual subspace. However, such magnitude-based decomposition is data-agnostic and does not explicitly account for target-relevant...
  </details>

- **2026-10-13** — Faruk Alpay, Taylan Alpay — [Provenance and Authorization in Autobiographical Language Models](http://arxiv.org/abs/2610.17935v1)
  <details><summary>📄 Abstract</summary>
  Autobiographical language models may draw on archives containing observations, quotations, emotional reports, and earlier model outputs. Cryptographic authentication can preserve an archive while leaving these sources semantically conflated. We formulate this gap as a computer-security problem: narrative content must not silently become consent or alter an authorized decision rule. We define typed records, authenticated attestations, a separate policy channel, and admissible views. Under explici...
  </details>

- **2026-10-13** — Subaru Kimura, Jun Suzuki — [Text-Only vs. Image-Aware VLM Judges for Manga Translation Evaluation](http://arxiv.org/abs/2610.17908v1)
  <details><summary>📄 Abstract</summary>
  In manga translation, visual context outside speech-bubble text, including speaker identities, referents, and scene tone, is depicted in page images, making it natural to refer to images during translation evaluation. However, most conventional manga translation evaluations rely solely on text-only automatic metrics, leaving the impact of image input insufficiently explored. We propose a practical validation framework that employs the same vision-language model (VLM) as both a text-only judge (T...
  </details>

- **2026-10-13** — Jingyue Cong, Estrid He, Zhuang Li et al. — [LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents](http://arxiv.org/abs/2610.17685v1)
  <details><summary>📄 Abstract</summary>
  Enterprise agents face safety risks that cannot be determined from individual actions alone. Existing safety benchmarks largely evaluate action-local risks, overlooking failures whose safety depends on workflow state. In such state-dependent risks, the same action may be safe in one context but violate policy in another. Hence, we introduce LatentRiskBench for evaluating such state-dependent risks in enterprise settings. It pairs risky trajectories with benign counterparts that share the same te...
  </details>

- **2026-10-13** — Rajmeet Singh, Manveen Kaur, Yusuf Adamu et al. — [MARTS: A Modular Agricultural Robot for Targeted Spraying of Diseased Tomato Plants in Greenhouses](http://arxiv.org/abs/2610.18123v1)
  <details><summary>📄 Abstract</summary>
  Broadcast spraying remains the dominant method of disease control in greenhouse tomato production, yet it treats healthy and diseased tissue alike, exposes workers to hazardous aerosols, and depends on operator skill. This paper presents MARTS (Modular Agricultural Robot for Targeted Spraying), a low-cost robotic platform that closes the loop from plant-level disease detection to leaf-localised spray delivery in commercial greenhouses. MARTS integrates a Clearpath Husky A200 mobile base, a UR5 m...
  </details>

- **2026-10-13** — Abdelrahman Yassin Eljamal, Abdeltawab Hendawi — [Bytes to Threats: Byte-Sequence Transformer For Malware Detection](http://arxiv.org/abs/2610.18787v1)
  <details><summary>📄 Abstract</summary>
  Existing malware detection approaches heavily rely on handcrafted features derived from static or dynamic analysis of the executable files. These methods require specialized domain expertise, dedicated analysis tools, and time-consuming analysis, which limits their scalability and robustness in the face of the increasing complexity and diversity of modern malware. Consequently, there is a growing interest in approaches that operate directly on raw bytes, which contain rich semantic and structura...
  </details>

- **2026-10-13** — Anton Altenbernd, Dylan Everingham, Philipp Wiesner et al. — [Revisiting Cauchy-Schwarz Norm Bounds for SDC Detection in LLM Inference](http://arxiv.org/abs/2610.18557v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) execute billions of floating-point operations per output token across many hardware accelerators. At this scale, hardware-induced faults can bypass system-level detection mechanisms and cause Silent Data Corruption (SDC). Algorithm-Based Fault Tolerance (ABFT) is the state-of-the-art technique for protecting matrix multiplication from such faults, but it incurs non-negligible computational overhead and requires thresholds to distinguish hardware-induced errors from f...
  </details>

- **2026-10-13** — Alejandro D. Mousist — [Behavioural self-monitoring for autonomous earth observation agents: The attribute reliability monitor (ARM)](http://arxiv.org/abs/2610.18548v1)
  <details><summary>📄 Abstract</summary>
  Language and vision language models can support autonomous systems, but changing operating conditions may compromise the reliability of their semantic outputs. This work introduces the Attribute Reliability Monitor (ARM), a framework that accumulates evidence of suspicion over time to assess individual semantic attributes. ARM accommodates different detectors and temporal monitoring methods, while leaving intervention policies to the consuming system. An initial implementation was evaluated usin...
  </details>

- **2026-10-13** — Ufuk Efe, Alptekin Temizel — [Robust Logical Anomaly Detection under Capture Shifts via Synthetic Anomalies](http://arxiv.org/abs/2610.18295v1)
  <details><summary>📄 Abstract</summary>
  Detectors of logical anomalies, such as missing, extra or wrongly combined parts, usually score a test image by its distance from normal (good) images. They achieve near-perfect image-level AUROC on standard industrial anomaly detection benchmarks such as MVTec LOCO, but their robustness to changes in capture conditions remains largely unexamined. Under a heterogeneous perturbation protocol in which each test image is randomly kept unaltered or subjected to a brightness reduction or a zoom-out t...
  </details>

- **2026-10-13** — Yingxuan Cheng, Tong Li, Yayong Li et al. — [How Reliable Are Large Language Models for Soil Organic Carbon Assessment? An Australian Benchmark](http://arxiv.org/abs/2610.18201v1)
  <details><summary>📄 Abstract</summary>
  Soil organic carbon (SOC) is an indicator of agricultural soil condition and carbon storage, but numerical outputs from large language models (LLMs) require validation before use in monitoring or management. We evaluated seven general-purpose LLM configurations on three direct-response tasks: estimating 0--10 cm SOC concentrations for 308 Australian paddocks under two information conditions, calculating SOC stock in 120 matched scenarios, and comparing 300 paddock pairs. References were measured...
  </details>

- **2026-10-13** — Oriol Rabasseda, Zenjie Li, Kamal Nasrollahi et al. — [Benchmarking Multimodal Large Language Models for Zero-Shot Human-Object Interaction](http://arxiv.org/abs/2610.18161v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated strong zero-shot reasoning across diverse domains, but their potential for Human-Object Interaction (HOI) remains unexplored. Unlike traditional HOI approaches that rely on extensive labeled datasets and fixed interaction taxonomies, MLLMs offer flexible reasoning, making them well-suited for dynamic, real-world scenarios. In this work, we present the first systematic study of MLLMs for HOI recognition and detection within a pipeline tha...
  </details>

- **2026-10-13** — Shalini Dangi, Divya Teja, Omkar Kabde et al. — [Uncertainty-Aware Semi-Supervised Framework with Supervised Contrastive Learning for Sugarcane Leaf Disease Detection](http://arxiv.org/abs/2610.17996v1)
  <details><summary>📄 Abstract</summary>
  Sugarcane leaf diseases severely impact crop yield and quality, making accurate and timely detection critical for sustainable agriculture. Conventional deep learning models for plant disease detection depend on large annotated datasets, which are expensive to obtain and challenging to prepare due to challenges commonly observed across crop disease detection tasks, including (i) high intra-class variation caused by diverse symptom expressions across growth stages, (ii) subtle inter-class similari...
  </details>

- **2026-10-13** — Anubhav Kataria, Shreya Ghosh, Jingwen Ye et al. — [When, Where, and Why: Hierarchical Causal Explainability for Video Face Understanding with MLLMs](http://arxiv.org/abs/2610.17791v1)
  <details><summary>📄 Abstract</summary>
  Understanding facial behaviour in video requires answering three fundamental questions: when a key facial expression occurs, where the model attends on the face at that moment, and why that evidence is necessary rather than merely correlated. Today's multimodal large language models (MLLMs) can label and describe video, but they rarely provide faithful explanations, especially for small facial movements that change over time. We present VideoFace-X-LLM, a framework for explainable facial video u...
  </details>

- **2026-10-13** — Swapnaneel Bhattacharyya, Soham Bonnerjee — [textGrain watermarking is harder to detect: can sum-tests still do it optimally?](http://arxiv.org/abs/2610.17655v1)
  <details><summary>📄 Abstract</summary>
  Watermarking embeds an imperceptible signal in text from large language models that is statistically detectable with a secret key. The recent textGrain watermark (Li et. al. (2026b)) calibrates this signal against the model's sampling entropy through an explicit entropy budget, combining the stochasticity of Red-Green and the unbiasedness of Gumbel-max watermarks, and its accompanying report proposes a detector that sums pivotal statistics. We study when, and how efficiently, textGrain can be de...
  </details>

- **2026-10-12** — Ramya Sundaram, Muhammad Aslam Jarwar, M Uma et al. — [Towards Modality-Agnostic Seizure Classification: A Unified Deep Learning Framework for Heterogeneous EEG and Intracranial EEG Signals](http://arxiv.org/abs/2610.16596v1)
  <details><summary>📄 Abstract</summary>
  Seizure prediction and detection, essential for clinical treatment of epilepsy, remain the crucial task of this neurological disease. EEG and iEEG are widely used to analyze epilepsy due to its capability of capturing discriminative brain activities at high time resolution. However, existing works generally analyze either EEG or iEEG seizure activity separately, where EEG analysis has been well-researched, while more and more works consider iEEG for its higher specificity at the spatial level an...
  </details>

- **2026-10-12** — Jincheng Ying, Li Wenlin, Wencheng Yang et al. — [CircuitBreak: Pruning a Sparse Safety Circuit of Neurons](http://arxiv.org/abs/2610.16470v1)
  <details><summary>📄 Abstract</summary>
  White-box neuron pruning has shown that refusal in large language models (LLMs) can depend on a small, removable set of feed-forward (FFN) channels. Existing attacks either need carefully paired ``twin'' prompts or score each neuron in isolation. Pruning also has an unavoidable capability cost, so over-removal compounds the loss. TwinBreak removes $1\%$--$5\%$ of parameters and NeuroStrike removes $0.3\%$--$0.7\%$ of neurons in targeted layers. We model safety as a small \emph{circuit} whose neu...
  </details>

- **2026-10-12** — Shangbin Feng, Yulia Tsvetkov, Jan Kautz et al. — [Compositional RL: Evaluating and Training LLMs for Collaborative Reasoning](http://arxiv.org/abs/2610.17456v1)
  <details><summary>📄 Abstract</summary>
  Language models are often evaluated alone but increasingly deployed together, routed between, made to debate, ensembled, or collaboratively trained. For a model inside a system, what matters most is not how well it performs on its own, but how much the system gains from its presence. We call this a model's compositional strength and formalize it using the Shapley value of a cooperative game over coalitions of a model pool, and use a model's leave-one-out contribution to the full coalition as a t...
  </details>

- **2026-10-12** — Adib Sakhawat, Fardeen Sadab, Tamjid Hasan Fahim et al. — [Evaluating Temporal Reasoning in Large Language Models: Event Temporal Relation Extraction with Allen's Interval Algebra, Logical Consistency, and Relative Time in Narratives](http://arxiv.org/abs/2610.17402v1)
  <details><summary>📄 Abstract</summary>
  Understanding a narrative means knowing how every event relates in time to every other, yet large language models (LLMs) are mostly tested on isolated event pairs or coarse labels. We ask five LLMs to reconstruct the complete network of Allen's 13 interval relations for 360 English narratives whose events are placed relative to one another rather than by dates, and evaluate the outputs under a pre-registered protocol for agreement with our gold annotations, converse consistency and logical satis...
  </details>

- **2026-10-12** — Saloni Gupta, Sébastien Krier, Glenn Matlin — [When Goals Leak Across Relationships: How Cached Goal Representations Shape Cross-Client Decisions](http://arxiv.org/abs/2610.17365v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents take on more autonomous roles, they may interact with multiple clients and counterparties whose goals and incentives conflict. If an agent maintains shared inference state across these interactions, information associated with one relationship may influence decisions made for another. We test OLMo-3-7B-Instruct in a controlled two-client environment with 20 market scenarios, where each client is assigned an opposing objective. With shared conversational memory, the model deviates f...
  </details>

- **2026-10-12** — Daniel Shao, Dongmin Bang, Luca L. Weishaupt et al. — [Beyond Sparse Captions: Aligning Slide-Level Text and Patch-Level Vision in Pathology](http://arxiv.org/abs/2610.17233v1)
  <details><summary>📄 Abstract</summary>
  Contrastive vision-language (VL) pretraining in computational pathology has generally relied on curated image-caption datasets sourced from social media, educational videos, and research publications. These corpora are sparse relative to the diversity of tissue morphology and difficult to scale further, as pathologists do not routinely produce descriptive captions in clinical practice. We propose to instead leverage slide-level pathology reports which can be generated during routine diagnostic w...
  </details>

- **2026-10-12** — Zhe Sun, Liang An, Jiayu Yao et al. — [UA-Bench: Benchmarking Large Audio-Language Models on Underwater Acoustic Recognition](http://arxiv.org/abs/2610.16942v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) are fast becoming a general interface to sound, yet how far their broad pretraining carries into specialized domains remains largely open. Vessel monitoring, maritime safety, and ocean sensing all depend on recognizing underwater signals, but to our knowledge LALMs have not been systematically evaluated on them. Annotated recordings are costly to collect, and a faithful synthetic alternative has to bring together many interacting factors: the structure of dete...
  </details>

- **2026-10-12** — Xing Liu, Yifan Guo, Hongtai Lv et al. — [FOCUS: A Subspecialty Foundation Model for Intraoperative Central Nervous System Pathology](http://arxiv.org/abs/2610.16914v1)
  <details><summary>📄 Abstract</summary>
  Intraoperative frozen-section diagnosis of central nervous system (CNS) lesions guides surgical decisions but is challenged by artefacts, diagnostic complexity and time constraints. Most pathology foundation models have limited exposure to CNS frozen tissue. Here we present FOCUS, a subspecialty foundation model pretrained on 27,930 frozen-sections enriched for CNS tissue. FOCUS led 11 internal diagnostic and 12 biomarker-prediction tasks, with mean AUCs of 0.969 and 0.877, respectively, retaini...
  </details>

- **2026-10-12** — Hongsen Cao, Mona Jaber, Shanxin Yuan et al. — [Mining Cross-Modal Perception Gaps in Autonomous Driving: When Camera and LiDAR Disagree](http://arxiv.org/abs/2610.16906v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal fusion for 3D object detection assumes that cameras and LiDAR are broadly complementary. In practice, how much each modality is trusted at a given location is decided by learned weights that are neither characterized nor auditable. We label every ground-truth object by which modalities detected it, then mine the resulting 0.4M-object database across nuScenes, KITTI, and Waymo. Because the patterns shift with distance from the ego vehicle, we read the mined model through Spatially Str...
  </details>

- **2026-10-12** — Ali Baheri, Peng Wei — [Controller-Agnostic Runtime Safety Certificates for Tool-Using AI Agents via Data-Driven Robust Reachability](http://arxiv.org/abs/2610.16865v1)
  <details><summary>📄 Abstract</summary>
  Software agents built on large language models act by issuing tool calls, some of which cannot be undone. To control theory the model is an opaque feedback controller, replaced every few months, whose closed loop cannot be analyzed directly. We propose a runtime filter, or shield, between any such controller and its environment that certifies a bound on the probability of reaching an unsafe condition during a bounded task. Given a predicate abstraction and candidate successor sets, everything el...
  </details>

- **2026-10-12** — Huihao Jing, Shaojin Chen, Wenbin Hu et al. — [Same Operation, Different Permission: Evaluating Whether Guardrails Honor Authorization](http://arxiv.org/abs/2610.16838v1)
  <details><summary>📄 Abstract</summary>
  As language-model agents write code, move money and change records on behalf of users, deciding whether an action is authorized has become a central safety problem. Guardrails are often placed in front of these actions, yet few evaluations ask whether their decisions follow authorization: blocking unauthorized actions while still allowing the same actions under valid permission. We introduce \bench{}, a benchmark that contrasts authorization evidence for the same operation in its language track....
  </details>

- **2026-10-12** — Chenxi Zhang, Youwei Pang, Xiaoqi Zhao et al. — [Code-Interactive Visual Reasoning for Financial Candlestick Understanding](http://arxiv.org/abs/2610.16587v1)
  <details><summary>📄 Abstract</summary>
  Financial candlestick understanding requires locating visual elements, aligning them across trading dates and panels, and combining observations through numerical and financial reasoning. Answer accuracy alone does not reveal whether predictions are supported by chart evidence. We introduce Code-Interactive Financial Candlestick Reasoning and present Fin-Thinker, a model based on Qwen3.5-9B that generates and executes code to acquire evidence and perform computations. The model uses the returned...
  </details>

- **2026-10-12** — Lei Zhu, Mujie Lin, Ruochong Zheng et al. — [Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration](http://arxiv.org/abs/2610.16448v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models, particularly Diffusion Transformers, achieve strong image and video generation quality but remain expensive at inference time due to repeated denoiser evaluations. Feature caching offers a deployment-friendly acceleration strategy by reusing or predicting intermediate representations without retraining the generator or modifying the sampler. However, existing cache-then-forecast methods often rely on Taylor-style finite-difference extrapolation, which can become unstable over l...
  </details>

- **2026-10-12** — Hangil Park, Seungheon Kim, Tae-Kyun Kim — [Learning Temporal Evidence Selection for Video Anomaly Understanding](http://arxiv.org/abs/2610.16299v1)
  <details><summary>📄 Abstract</summary>
  Video anomaly understanding (VAU) aims to generate language-level interpretations of anomalous events in long videos, requiring visual evidence that supports explanation beyond anomaly detection alone. Existing VAU pipelines commonly rely on anomaly-centric or predefined temporal sampling strategies, which efficiently emphasize suspicious moments but overlook contextual cues, object interactions, and temporally distributed evidence needed for reasoning. Motivated by recent progress in learnable ...
  </details>

- **2026-10-12** — Yue Zhao, Zixiang Xu, Angela Huyue Zhang et al. — [agent-risk: Risk Assessment for Changes to AI Agents](http://arxiv.org/abs/2610.16280v1)
  <details><summary>📄 Abstract</summary>
  Before changing a deployed AI agent (a stricter safety gate, a new model), organizations must approve the change, starting from existing logs. Extending classical risk analysis to partial records and partial changes to running systems, agent-risk replays logged episodes, assuming nothing else changes and the agent does not anticipate the change. The log settles episodes acting as before, a declared stop value settles stopped ones, and the rest need logged support, a saved-state rerun, or a bound...
  </details>

- **2026-10-12** — Bilal Jawaid, Hamza Hanif, Muhammad Maaz Uddin et al. — [Geometric Parrots: Rule Absence vs. Rule Fragility in Spatial and Physical Reasoning for Vision-Language Models](http://arxiv.org/abs/2610.16170v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can answer many geometric and physical reasoning questions correctly, yet still behave inconsistently in interaction, for example, abandoning a correct answer when confronted with a confident but incorrect user assertion. Standard single-turn accuracy cannot distinguish such capitulations from beneficial corrections because it scores each response in isolation. We introduce GRIP, a controlled benchmark with 34 procedurally generated reasoning domains, 100,000 images...
  </details>

- **2026-10-12** — Tristan J. B. Cann, Arjun Biswas — [Contrastive learning for video reuse detection](http://arxiv.org/abs/2610.17098v1)
  <details><summary>📄 Abstract</summary>
  The incorporation of footage from other sources has long been a concern from a copyright perspective, as such usage can harm the interests of rights holders. Recent trends in the ``remixing'' of social media content and the development of bespoke stock libraries for specialist causes mean that methods to identify content reuse will have a range of applications. In this paper, we develop a framework based on a Siamese network fine tuned using contrastive learning to identify potential sources for...
  </details>

- **2026-10-12** — Jiuyao Jing, Xuanyu Yi, Yu Zheng et al. — [EviStress: Evidence Stress Learning for Generalizable Face Forgery Detection with Textual Explanations](http://arxiv.org/abs/2610.16879v1)
  <details><summary>📄 Abstract</summary>
  The rapid spread of face forgeries on the Web challenges the credibility of visual content. In practical Web environments, manipulated media originate from evolving generation pipelines and undergo diverse processing during dissemination, making reliable authenticity assessment under unseen manipulations and visual changes a critical challenge. We observe that a standard LoRA-adapted CLIP detector exhibits uneven patch-level decision dependence, concen trating a disproportionate share of class-s...
  </details>

- **2026-10-12** — Siyu Zhou, Jialin Ouyang, Fan Xia et al. — [Learning to Detect Shifts in Unstructured Data Streams via Monitoring-by-Betting](http://arxiv.org/abs/2610.17399v1)
  <details><summary>📄 Abstract</summary>
  Continuous monitoring of generative AI systems requires detecting distribution shifts in the unstructured data they ingest and generate. Existing monitoring methods typically control false alarms by requiring the discrepancy measure used to detect shifts to be *pre-specified*. However, for unstructured data, pre-specification creates a sensitivity--breadth trade-off: a narrowly defined measure is sensitive to the anticipated shift but may miss unexpected changes, whereas a broadly defined measur...
  </details>

- **2026-10-09** — Meriem Terki, Nouhaila Innan, Minghao Shao et al. — [QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code](http://arxiv.org/abs/2610.13811v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but...
  </details>

- **2026-10-09** — Yan Luo, Laibin Chang, Zefan Feng et al. — [State-Isolated Vision Mamba via Update-Tendency Routing for Underwater Image Enhancement](http://arxiv.org/abs/2610.13720v1)
  <details><summary>📄 Abstract</summary>
  Vision Mamba has recently emerged as an efficient alternative to convolutional and Transformer-based architectures by modeling long-range spatial dependencies through recurrent state evolution. Existing studies primarily improve token serialization, scanning strategies, or expert routing, yet largely overlook a state level question question: how should recurrent states be organized for spatially heterogeneous visual restoration? In this paper, we show that forcing tokens with heterogeneous updat...
  </details>

- **2026-10-09** — Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev et al. — [A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models](http://arxiv.org/abs/2610.13663v1)
  <details><summary>📄 Abstract</summary>
  Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the en...
  </details>

- **2026-10-09** — Sangpil Youm, Annabel Stocks Natalias, Hayden Heninger et al. — [REFLECT: Role-Aware Detection of Sentiment, Emotion, Politeness, and Formality](http://arxiv.org/abs/2610.13797v1)
  <details><summary>📄 Abstract</summary>
  Detecting communicative meaning in dialogue requires modeling not only lexical content but also the participant-role structures through which sentiment, emotion, politeness, and formality (SEPF) are expressed. Existing approaches rely on contextual language representations while leaving semantic roles implicit. We introduce a role-aware transformer architecture that maps the four SEPF dimensions to theory-grounded Semantic Role Labeling (SRL) configurations, incorporating these configurations di...
  </details>

- **2026-10-09** — Nazar Andrushko, Vera Schmitt, Veronika Solopova — [UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes](http://arxiv.org/abs/2610.13783v1)
  <details><summary>📄 Abstract</summary>
  Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that preserves original visual ...
  </details>

- **2026-10-08** — Shihab Ahmed, Md Sajidul Islam Sajid, Teryl Taylor et al. — [ORCAGen: Orchestrating Context-Aware Malware Deception with RAG-Guided Generative AI](http://arxiv.org/abs/2610.12415v1)
  <details><summary>📄 Abstract</summary>
  Malware defenses often remove or isolate suspicious programs as quickly as possible. While effective for containment, this approach can also waste an opportunity to observe attacker behavior and deploy targeted countermeasures. ORCAGen takes a different approach: it uses GenAI to build malware-specific deception playbooks offline, validates them before deployment, and enforces only the verified logic at runtime. ORCAGen combines Retrieval-Augmented Generation (RAG) with structured prompt enginee...
  </details>

- **2026-10-08** — Ines Ortega-Fernandez, Mateusz Kowalczyk, Keri Warr — [Anytime-valid detection of LLM weight exfiltration](http://arxiv.org/abs/2610.11843v1)
  <details><summary>📄 Abstract</summary>
  A compromised LLM inference server can leak model weights by encoding payload bits in otherwise plausible token choices. A replay of the same prompt in a trusted server can expose such deviations, but benign numerical nondeterminism also causes token mismatches. Patient attackers can therefore hide within normal variation unless evidence is combined across responses. We introduce a prompt-level e-process that calibrates whole-response mismatch events on trusted benign traffic and accumulates evi...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 66 papers

- **2026-10-13** — Ruixiao Dong, Jianmin Bao, Bozhi Luan et al. — [PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts](http://arxiv.org/abs/2610.18857v1)
  <details><summary>📄 Abstract</summary>
  Pixel-space diffusion models provide an appealing alternative to latent-space diffusion models by directly modeling raw images without relying on a learned tokenizer. However, scaling pixel-space models has predominantly followed dense strategies, tightly coupling model capacity with active computation. In this work, we show that standard LLM-style Mixture-of-Experts (MoE) architectures can be effectively transferred to pixel-space diffusion. Building on this finding, we introduce PixelMoE, a pi...
  </details>

- **2026-10-13** — Ziheng Wang, Yanming Shao, Ting Mao et al. — [EgoMatrix: Physically Faithful Dexterous Robot Demonstrations from Egocentric Human Videos](http://arxiv.org/abs/2610.18822v1)
  <details><summary>📄 Abstract</summary>
  Egocentric human videos offer a scalable alternative to robot teleoperation for collecting dexterous manipulation data. However, two challenges limit their use as reliable training data: accurate hand-object interaction (HOI) reconstruction from monocular RGB and high-quality robot demonstrations, especially visual observations. We present EgoMatrix, an end-to-end data engine that converts monocular egocentric human videos into bimanual dexterous trajectories and paired robot observation videos,...
  </details>

- **2026-10-13** — Neel Dey, Adrian V. Dalca — [Registration is a Representation Problem: Solving Whole-Body PET/CT Registration](http://arxiv.org/abs/2610.18804v1)
  <details><summary>📄 Abstract</summary>
  Raw image intensities are a poor surrogate for similarity across images in correspondence problems. Further, while auxiliary segmentation labels can provide semantic identification and improve matching, they can assign only coarse identities to fine-grained anatomy and often cover only a subset of structures, particularly in whole-body settings. We present an approach that instead establishes correspondence using complementary representations of anatomy and demonstrate its utility for longitudin...
  </details>

- **2026-10-13** — Rong Li, Shijie Li, Jiangyong Huang et al. — [GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models](http://arxiv.org/abs/2610.18694v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features. Capturing geometry, however, does not ensure its use: zeroing the aligned latents of a released feature-alignment model leaves its accuracy uncha...
  </details>

- **2026-10-13** — Fabian Gröger, Petar Damjanović, Maria Brbić — [To Align or Not To Align: Check Your COMPASS Before You Train](http://arxiv.org/abs/2610.18638v1)
  <details><summary>📄 Abstract</summary>
  Combining pretrained models is a common strategy for building AI systems, whether by aligning a vision encoder with a language model or merging fine-tuned checkpoints. However, finding compatible pairs typically requires costly empirical search, as compatibility is known only after alignment or merging. We propose COMPASS (COMPatibility ASsessment Score), a theoretically motivated diagnostic that estimates whether a model pair will be compatible prior to alignment or merging. Building on the obs...
  </details>

- **2026-10-13** — Jason Ken Adhinarta, Raina Wu, Ashutosh Sharma et al. — [Does self-distillation improve reasoning?](http://arxiv.org/abs/2610.18613v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation is an emerging approach that trains a model to imitate its own predictions when conditioned on privileged information, such as correct answers or environmental feedback. Recent methods have reported better sample efficiency and generalization than reinforcement learning (RL), but it remains unclear whether these gains extend beyond in-distribution evaluations and whether they stem from privileged distillation. In this paper, we revisit two representative methods, Self-Distillat...
  </details>

- **2026-10-13** — Haotian Liu, Yingjian Chen, Xiaohang Xu et al. — [Beyond Answer Voting: Fine-Grained Correction of LLM Reasoning through Graph Alignment across Sampled Traces](http://arxiv.org/abs/2610.18606v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly tackle tasks that require multi-step reasoning, where errors in intermediate claims can affect the final answer. Self-consistency (SC) improves reasoning by voting over sampled final answers, but its vote leaves intermediate disagreements unresolved. To address this problem, we introduce DDRG (Disagreement-Driven Verification Guided by Reasoning Graphs), a framework for selective correction from a frozen bank of reasoning traces. Our insight is that graph align...
  </details>

- **2026-10-13** — Fabian Gröger, Naël Ouerghemi, Shuo Wen et al. — [Rethinking Projector Training in Multimodal LLMs](http://arxiv.org/abs/2610.18598v1)
  <details><summary>📄 Abstract</summary>
  Multimodal LLMs are typically trained by first aligning a vision encoder with a language model via projector training on large image-caption datasets, followed by joint training of the full multimodal model. Despite its widespread use, the role of the projector training stage remains poorly understood. We find that (i) using only $10$ to $20\%$ of the data for training the projector already recovers most downstream performance gains, and (ii) projectors trained on different datasets can be linea...
  </details>

- **2026-10-13** — Mehdi Makni, Natalia Ponomareva, Rahul Mazumder — [Two For The Price Of One: Curvature-Aware Pruning Preserves Influence Functions Too](http://arxiv.org/abs/2610.18516v1)
  <details><summary>📄 Abstract</summary>
  Post-training pruning enables efficient deployment, but conventional methods do not explicitly preserve internal-gradient alignment between sparse and dense models. We study novel connections between downstream performance of compressed models and the ability to retain gradient information via influence-function preservation. Central to this connection is a curvature-aware objective that accounts for both layer activations and backpropagated gradients. Despite its promise, this objective remains...
  </details>

- **2026-10-13** — Xueyao Wei, Yifei Wang, Delun Li et al. — [MemoryVLN: From Ego-Aware Memory Representation to Cross-Context Memory Reuse in Vision-Language Navigation](http://arxiv.org/abs/2610.18478v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have shown strong potential for embodied vision-language navigation (VLN), yet their performance degrades on long-horizon trajectories due to context-length limits, redundant historical observations, and unstable spatial alignment across time. These issues make it difficult to both compress long navigation histories and reliably reuse past spatial experience. To address these limitations, we propose \textbf{MemoryVLN}, a unified memory-driven navigation syste...
  </details>

- **2026-10-13** — Pratuat Amatya, Vinay Setty, V Venktesh et al. — [Do Factuality Methods Make LLMs More Factual? Reproducibility and Fair Comparison](http://arxiv.org/abs/2610.18415v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are aligned to human preferences, after pre-training and supervised fine-tuning steps. However, standard RL alignment steps such as RLHF do not focus on factuality of LLMs, hence they may generate non-factual information, which could result in unintended consequences. In response, a number of factuality alignment approaches have been proposed in the literature which claim to improve factuality of LLMs on their own benchmarks. However, these methods have not been repr...
  </details>

- **2026-10-13** — Pablo Loyola, Edison Marrese-Taylor, Andrés Hoyos-Idrobo — [Probing the Geometry of Color Representations in Multilingual Language Models](http://arxiv.org/abs/2610.18331v1)
  <details><summary>📄 Abstract</summary>
  Do multilingual language models learn a universal internal geometry for color, and is it perceptually grounded or primarily linguistic? We decompose color representations into two geometric axes: (P1) alignment to perceptual color space, and (P2) cross-lingual symmetry. Analyzing layerwise embeddings across models and multilingual datasets, we find that perceptual grounding is weak: alignment to CIE-LAB peaks in intermediate layers, then collapses toward output layers. Cross-lingual symmetry deg...
  </details>

- **2026-10-13** — Hui Huang, Jie Zhou, Hongli Zhou et al. — [LegalRewardBench: Benchmarking Reward Models for Legal Preference Evaluation](http://arxiv.org/abs/2610.18299v1)
  <details><summary>📄 Abstract</summary>
  Reward models are central to preference alignment for legal tasks, yet existing reward model benchmarks are still primarily centered on general-domain preferences. In this work, we introduce LegalRewardBench, the first human-verified benchmark for evaluating reward models in the legal domain. The benchmark organizes legal preference evaluation into five capability levels: knowledge, understanding, analysis, decision, and writing, and preference examples are constructed through rubric-guided auto...
  </details>

- **2026-10-13** — Guanghao Wu, Zhuo Cai, Zhidong Li et al. — [When and How Order-Flow Interventions Work After Dealers Adapt](http://arxiv.org/abs/2610.18158v1)
  <details><summary>📄 Abstract</summary>
  Learning dealer agents can settle on persistently wide quotes, raising what customers pay to trade. A venue can route more orders to tighter quotes, but a wide quote may reflect real risk, and once dealers adapt, an end-to-end comparison cannot show why a rule works: because it intervenes more, picks better moments, is announced in advance, or rewards the right quote. We propose SOFA (State-aligned Order-Flow Allocation), a public order-flow contract with three parts: a State Scorer ranks market...
  </details>

- **2026-10-13** — Yibo Wang, Senjie Jin, Yansong Ning et al. — [LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](http://arxiv.org/abs/2610.18092v1)
  <details><summary>📄 Abstract</summary>
  Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life and professional productivity settings insufficiently evaluated. To bridge this gap, we introduce LifeSearch, a challenging benchmark comprising 203 Chinese and English tasks derived from real-user query seeds across 7 co...
  </details>

- **2026-10-13** — David Otte, Jörg K. H. Franke, Frank Hutter — [Improving Neural Symbolic Regression with a Diverse Prior and Post-training Alignment](http://arxiv.org/abs/2610.17994v1)
  <details><summary>📄 Abstract</summary>
  Symbolic regression is the problem of finding an expression that fits a dataset. Solving it requires searching a combinatorial space of candidate expressions. Neural symbolic regression can amortize that search by training a model once on synthetic data and then predicting expressions for a new dataset. But existing models still underperform genetic programming on real, noisy data. We argue that the deficit lies in the training rather than in the paradigm, and present RASR (Reinforced Amortized ...
  </details>

- **2026-10-13** — Xu Yang, Jiapeng Zhang, Zhiwei Zuo et al. — [AlignPred: Error-Controlled KV Cache Compression via Alignment and Predictive Coding](http://arxiv.org/abs/2610.17970v1)
  <details><summary>📄 Abstract</summary>
  Long-running agents retain KV caches across turns and sessions for hours or days. Compressing these persistent caches requires reducing storage while controlling reconstruction error. We present AlignPred, a codec that combines local alignment with predictive coding under a configurable KV reconstruction-error budget. Local orthogonal transforms align related heads or layers into a common coordinate frame, allowing AlignPred to combine token-wise prediction with same-token prediction across head...
  </details>

- **2026-10-13** — Lingyi Long, Congyue Zhao, Xiaoou Li et al. — [LinMorph: Learning to Morph Weights for Efficient Video DiT Linearization](http://arxiv.org/abs/2610.17914v1)
  <details><summary>📄 Abstract</summary>
  Post-hoc linearization is an attractive way to accelerate pretrained Video Diffusion Transformers (Video DiTs), yet existing methods largely treat the quality loss induced by attention replacement as a recovery problem. We show that a more fundamental bottleneck lies upstream: \emph{initialization}. Random initialization discards pretrained knowledge, whereas manual weight reuse transfers it through rigid and incomplete source--target correspondences. We introduce \textbf{LinMorph}, which recast...
  </details>

- **2026-10-13** — Minjun Kim, Hyunmin Song, Changwon Lim — [Visual Dependence Does Not Imply Answerability: A Systematic Analysis of Answerability Signals in Frozen InstructBLIP](http://arxiv.org/abs/2610.17902v1)
  <details><summary>📄 Abstract</summary>
  Visual question answering models often produce plausible responses even when the available visual evidence is insufficient to support a valid answer. Although prior work has introduced benchmarks and abstention mechanisms for unanswerable visual questions, it remains unclear which signals derived from a frozen vision-language model reliably indicate answerability on unseen image-question pairs. We systematically evaluate answerability signals on a stratified 10K subset of UNK-VQA using frozen In...
  </details>

- **2026-10-13** — Wayne Chi, I-Hung Hsu, Li Chen et al. — [Interaction-as-a-Judge](http://arxiv.org/abs/2610.17895v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are tasked with producing sophisticated interactive applications such as websites, desktop applications, and games. While humans assess these applications interactively, current automated LLM evaluations primarily focus on code analysis and unit tests. This mismatch can cause LLM judges to miss failures that are immediately apparent to human users. We study Interaction-as-a-Judge, an evaluation paradigm where computer-use agents (CUAs) directly interact with an application. We demo...
  </details>

- **2026-10-13** — Yifan Li, Lishuai Gao, Tong Zhang et al. — [Diagnose-to-Generate: Eliminating Structural Distortions in Flow Models via Patch-Level Grounded Alignment](http://arxiv.org/abs/2610.17882v1)
  <details><summary>📄 Abstract</summary>
  Flow-based image generators achieve strong semantic synthesis but still produce localized structural distortions, such as malformed hands and limbs. Existing post-training methods typically optimize global scalar rewards, which provide weak spatial credit assignment and may alter well-formed regions while correcting local defects. We present \textit{Diagnose-to-Generate (D2G)}, a grounded alignment framework that separates visual diagnosis from generative optimization. We construct \textbf{Achil...
  </details>

- **2026-10-13** — Zipeng Wang, Anping Xiong, Jing Zhang et al. — [LoopREG: Representation Supervision Enables Test-Time Recurrent Depth in Diffusion Transformers](http://arxiv.org/abs/2610.17877v1)
  <details><summary>📄 Abstract</summary>
  Reusing Transformer blocks offers a way to increase diffusion-model computation at test time, but naive recurrence can degrade generation beyond its training depth. We introduce LoopREG, a representation-supervised recurrent diffusion Transformer that repeatedly applies a shared block at the state supervised by a pretrained visual encoder. Alignment is applied after the final recurrent visit during training; inference extends the same learned operator to additional visits. On ImageNet 256 x 256,...
  </details>

- **2026-10-13** — Yanran Ruan, Zhixiang Wei, Shiyao Hong et al. — [MicroCLIP: Connecting Text and Microscopy Images via Contrastive Language--Image Pretraining](http://arxiv.org/abs/2610.17866v1)
  <details><summary>📄 Abstract</summary>
  Understanding fluorescence microscopy images is fundamental to automating biological research. However, existing methods typically learn predefined concepts from closed-set data, limiting transfer across tasks and biological contexts. In this work, we introduce MicroCLIP, a vision-language model that learns generalizable cellular and subcellular representations from natural language supervision for open-set image classification and retrieval. To pretrain MicroCLIP, we construct MicroPool-2M, a d...
  </details>

- **2026-10-13** — Ziyang Zhang, Shenyi Li, Yilin Wang et al. — [MMTA: Benchmarking Multimodal Temporal Analysis with Time Series, Text, and Vision](http://arxiv.org/abs/2610.17856v1)
  <details><summary>📄 Abstract</summary>
  Time-series analysis is increasingly studied in multimodal settings, yet most benchmarks pair temporal signals with text or with visualizations derived from the same signal. This leaves open whether multimodal large language models (MLLMs) can integrate time series with real-world visual evidence. We introduce MMTA (multimodal temporal analysis), a benchmark of tri-modal tasks with diverse cross-modal complementarity patterns among time series, text, and vision. MMTA spans nine domains -- roboti...
  </details>

- **2026-10-13** — Sangkwon Park, Dongwook Lee, Youngho Cho et al. — [SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data](http://arxiv.org/abs/2610.17813v1)
  <details><summary>📄 Abstract</summary>
  End-to-end speech-to-text retrieval is becoming an important capability for voice agents, allowing spoken queries to retrieve relevant documents without intermediate transcription. Training these retrievers typically depends on large collections of spoken query-document pairs that are costly to acquire and difficult to extend across domains and languages. We introduce \ours, which replaces such task-specific supervision with speech-transcript pairs from standard ASR corpora. A lightweight adapte...
  </details>

- **2026-10-13** — Husein Zolkepli — [Where Words Begin and End](http://arxiv.org/abs/2610.17782v1)
  <details><summary>📄 Abstract</summary>
  Forced aligners locate each word of a known transcript in the audio, and many speech pipelines depend on them. In our own data, a widely used CTC aligner inserts a pause at nearly every word boundary, and we found almost no aligner evaluated on telephone audio. We compare nine aligner configurations against human word boundaries on read, conversational and telephone English. The Montreal Forced Aligner (MFA) is the most precise, while CTC aligners consistently start words late, because most fram...
  </details>

- **2026-10-13** — Kaiming Liu, Yuxuan Liu, Jinrui Ju et al. — [Instructions Are Evidence, Not Objectives: Measuring Outcome Alignment of Agents](http://arxiv.org/abs/2610.17757v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can follow complex human instructions to solve real-world tasks. In practice, however, initial instructions are often incomplete. In our analysis of 100 user-agent trajectories from SWE-chat, 56\% of initial instructions omit requirements that later emerge as necessary, and 52\% of the useful follow-up requirements could have been inferred from the project. A user states requirements from their own understanding of the task, and these \textbf{stated requirements} ofte...
  </details>

- **2026-10-13** — Kaishen Wang, Yucheng Pan, Xuehao Cui et al. — [Understanding Machine Taste: Aesthetic Agreement Across Foundation Models in K-pop](http://arxiv.org/abs/2610.17731v1)
  <details><summary>📄 Abstract</summary>
  As foundation models enter creative industries, understanding their aesthetic preferences becomes an important step toward AI-assisted creative decision making. In this work, we investigate how foundation models evaluate creative content and characterize their ``machine taste'' using K-pop songs and music videos as a testbed. We formulate aesthetic evaluation as a pairwise ranking problem and systematically examine pairwise inter-model agreement, group-level consensus, and cross-modal preference...
  </details>

- **2026-10-13** — Yewon Han, Jisu Jeon, Suhyun Choi et al. — [Safety for Whom? Benchmarking Understanding Beyond Refusal in Egocentric Multimodal Assistants](http://arxiv.org/abs/2610.17728v1)
  <details><summary>📄 Abstract</summary>
  Egocentric multimodal assistants see through the user's eyes and guide what the user does next, so their outputs directly shape physical actions, including those that affect bystanders. Yet existing safety evaluations do not distinguish whom a response would harm, and score only whether a model refuses. Pooling all harms into one refusal rate hides two failures: a model may protect one target but not another, and it may refuse without understanding the risk, or understand it and comply anyway. W...
  </details>

- **2026-10-13** — Mostafa Abbasi, Homayoun Najjaran — [A Node Embedding Framework for Model-Centric Conformance Checking in Process Mining](http://arxiv.org/abs/2610.17702v1)
  <details><summary>📄 Abstract</summary>
  Evaluating the quality of process models discovered from event logs is a fundamental challenge in process mining. Traditional evaluation relies on conformance metrics such as fitness and precision, which are highly sensitive to noise and deviations in event logs and therefore often fail to give a consistent assessment of discovery algorithms. We introduce a model-centric evaluation framework that combines node embeddings with Procrustes alignment to enable cross-graph comparability, since embedd...
  </details>

- **2026-10-13** — Qingchuan Ma, Yuexiao Ma, Xiang Meng et al. — [RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment](http://arxiv.org/abs/2610.17665v1)
  <details><summary>📄 Abstract</summary>
  Can vision-language models turn 2D observations into 3D understanding that supports precise action? This requires inferring object geometry, anticipating the effects of rotation, and refining actions through visual feedback. We introduce RoTA-Bench to evaluate these abilities through interactive 3D-to-2D projection alignment. Given a target silhouette, a model observes a rotated object and chooses successive rotations to recover the target projection within a limited action budget. Our automated...
  </details>

- **2026-10-13** — Yongcan Yu, Jian Liang, Lingxiao He et al. — [Facts Don't Speak Louder than Words: The Behavioral Essence of Long-CoT Distillation](http://arxiv.org/abs/2610.17607v1)
  <details><summary>📄 Abstract</summary>
  While long chain-of-thought (CoT) distillation significantly improves the reasoning abilities of language models, its underlying mechanism remains poorly understood. Current pipelines generally rely on rejection sampling to gather reasoning traces across diverse prompts, assuming that factual correctness and broad problem coverage are indispensable. Surprisingly, we find that training exclusively on flawed reasoning trajectories or a restricted prompt set yields nearly comparable performance. Dr...
  </details>

- **2026-10-13** — Yuchen Liang, Xian Yu — [Risk-Averse Inference-Time Diffusion Model Alignment with Finite-Sample Guarantees](http://arxiv.org/abs/2610.17579v1)
  <details><summary>📄 Abstract</summary>
  Inference-time alignment steers diffusion models toward downstream objectives without costly fine-tuning, but existing methods typically optimize expected cost (or reward) without explicitly controlling tail risk. In this work, we propose a risk-averse framework for inference-time alignment of diffusion models that balances expected cost and Conditional Value-at-Risk (CVaR) under trajectory-level Kullback-Leibler regularization. We characterize the optimal path distribution and reverse transitio...
  </details>

- **2026-10-13** — Reza Sanayei, Razvan-Gabriel Dumitru, Sunjie Hou et al. — [Evidence-First Agentic Verification](http://arxiv.org/abs/2610.17724v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent's own reports of success. When rubric verdicts serve as reinforcement-learning rewards, such errors can reinforce undesirable behavior. We introduce Sauron, an evidence-first agentic verifier that investigates both stat...
  </details>

- **2026-10-13** — Kakei Yamamoto, So Kuroki — [PRISM: Calibrating Black-Box Judges with Counterfactual Probes](http://arxiv.org/abs/2610.18389v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as judges to reduce reliance on costly human evaluation, yet their scores can systematically disagree with human judgments. We ask whether responses to an explicitly imposed evaluative bias can help correct a judge's implicit scoring biases. We introduce PRISM (Probe-based Residual Inference of Scoring Misalignment), which holds the evaluated content fixed and measures score changes when attributes are emphasized or de-emphasized. A local sensitivity m...
  </details>

- **2026-10-12** — Zhaoliang Zhang, Chenhao Yu, Zhimin Shao et al. — [Act4R: Action-conditioned 4D reconstruction for kinematics-free control](http://arxiv.org/abs/2610.17462v1)
  <details><summary>📄 Abstract</summary>
  Precise control of movement across various robotic embodiments is a longstanding challenge. Modeling complex robotic structures requires significant time, dedicated sensors, and manual labeling. Recent advancements in 4D representation learning offer an interesting alternative: can we leverage 4D features lifted from 2D observations to densely map a robot's spatial movement based on the action signal? To this end, we propose Act4R, a framework that builds on 3D foundation model to predict a robo...
  </details>

- **2026-10-12** — Li-Ching Chen, Andrés Franco Valiente, Yuta Ishiyama et al. — [Reinforcement Learning In Partially Verifiable Environments for Colon Cancer Treatment Planning](http://arxiv.org/abs/2610.17426v1)
  <details><summary>📄 Abstract</summary>
  Clinical decision-making is a sequential process of information collection, clinical inference, and forecasting under partial observability, often without a uniquely correct treatment decision. Large language models (LLMs) have demonstrated strong medical question-answering capabilities but extending these advances to clinical reasoning remains challenging because many clinical tasks are only partially verifiable. Recent clinical reinforcement learning (RL) work has therefore largely focused on ...
  </details>

- **2026-10-12** — Zikun Zhang, Jiayuan Sheng, David D. Yao et al. — [JustOPD: On-Policy Distillation from Autoregressive to Diffusion Language Models](http://arxiv.org/abs/2610.17397v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) is a post-training approach for large language models (LLMs) that enables a student model to learn a teacher model's distribution from sequences sampled from the student's own policy. Despite its promising capability, OPD for diffusion language models (DLMs) remains underexplored and existing studies primarily focuses on DLM-to-DLM distillation. The limited availability of strong teacher DLMs and the flexible generation order of DLMs impose additional technical chall...
  </details>

- **2026-10-12** — Fabrice Lamarche, Amal Zouaq — [UMCR: Universal Medical Concept Recognition through Guideline Integration and Agentic Linking](http://arxiv.org/abs/2610.17363v1)
  <details><summary>📄 Abstract</summary>
  Medical Concept Recognition is the task of extracting and grounding spans in medical text to entries in a standard ontology. Current methods are generally developed towards a single ontology and source text type (clinical notes, drug labels, etc.) The central challenge is therefore to build methods that adapt to any target ontology without requiring ontology-specific retraining. More recent approaches like REAL and AutoPCR make direct use of Large Language Models and can theoretically adapt to a...
  </details>

- **2026-10-12** — Hiroki Naganuma, Laura Gomezjurado, Mahdi Ghaznavi et al. — [Which Geometry on Which Layer? Measured Sign-Spectral Assignment in Mixed-Optimizer Training](http://arxiv.org/abs/2610.17285v1)
  <details><summary>📄 Abstract</summary>
  Modern neural-network training uses mixed recipes, assigning AdamW-like or sign-based updates to embedding and output layers and spectral updates to hidden matrices. These assignments are usually fixed by layer type, without a clear criterion for selecting the appropriate geometry. We turn sign-versus-spectral assignment into a measurable, layerwise decision problem. For ideal memoryless steps, we derive a finite-batch ratio of conservative descent-lemma lower bounds for spectral and sign update...
  </details>

- **2026-10-12** — Claire Schlesinger, Wolfgang Gatterbauer, Robin Walters — [Measuring Learned Equivariance: An Information Theoretic Approach](http://arxiv.org/abs/2610.17269v1)
  <details><summary>📄 Abstract</summary>
  Learning symmetries through data augmentation offers an alternative to architectural equivariance, but does not guarantee that a network respects those symmetries. Measuring learned equivariance is especially difficult for intermediate representations, whose group actions are not specified. In a finite discrete setting, we show that equivariance requires representations of original and transformed inputs to determine one another exactly, yielding a test based on normalized mutual information (NM...
  </details>

- **2026-10-12** — Guangming Wang, Zhishuo Liu, Haibing Wu et al. — [Physical SLAM: Physics-aware Simultaneous Localisation and Mapping](http://arxiv.org/abs/2610.17260v1)
  <details><summary>📄 Abstract</summary>
  To reconstruct a predictive 4D representation of the physical world from monocular video captured by a moving camera, we jointly reconstruct dynamic Gaussian radiance fields and infer their underlying physical dynamics. This paper proposes \emph{Physical SLAM}, a physics-aware method for constructing 4D Gaussian fields of deformable objects and predicting their future state when subjected to external actions, given a sequence of RGB-D images. Our method separates the scene into a static backgrou...
  </details>

- **2026-10-12** — Chong Cheng, Ran Zhang, Xinyuan Li et al. — [When Left Is Right? Camera-Motion Understanding beyond Screen](http://arxiv.org/abs/2610.17242v1)
  <details><summary>📄 Abstract</summary>
  Can a vision-language model tell left from right? Modern VLMs solve visual puzzles and follow hour-long videos, yet when asked whether the camera moved left or right, most do no better than a coin flip. Adding camera-motion data or geometric representations has been tried, separately, and neither closes the gap. We argue that camera-motion understanding needs two conditions at once: the representation must couple off-screen camera motion with on-screen flow dynamics, and it must be interpreted b...
  </details>

- **2026-10-12** — Farhad Pashakhanloo, Venkatesh N. Murthy — [Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors](http://arxiv.org/abs/2610.17164v1)
  <details><summary>📄 Abstract</summary>
  The relationship between odor chemistry and perception remains incompletely understood. Many existing studies focus on the perception of single molecules, whereas natural odors contain tens to hundreds of components, adding extra layer of complexity to percept formation. Here, we explore the relationship between molecular composition and perceived similarity in natural odor objects. We study this using a database of more than 1,200 volatile-compound-in-food mixtures containing more than 8,000 mo...
  </details>

- **2026-10-12** — Hayeon Bang, Hounsu Kim, Joonyong Park et al. — [PitchIn: Natural-Language Vocal Coaching from Unstructured Community Feedback](http://arxiv.org/abs/2610.17036v1)
  <details><summary>📄 Abstract</summary>
  Effective vocal coaching connects performance issues with corrective advice, but recordings paired with expert diagnoses and advice are scarce. Online singing communities provide a potential source of supervision, but observations and advice are scattered across unstructured comments. We introduce PitchIn, audio-language models for natural-language vocal coaching, and the PeerCoach Dataset: 14,445 instruction examples covering Focused QA, Overall Feedback, and Recognition QA. We compare target c...
  </details>

- **2026-10-12** — Yanhang Shi, Xiaoyu Wang, Houwei Cao et al. — [MODAIC: Coordinated Asynchrony for Decentralized Multimodal Learning](http://arxiv.org/abs/2610.16987v1)
  <details><summary>📄 Abstract</summary>
  Multimodal decentralized learning enables collaboration across heterogeneous edge devices without sharing raw data, but differing modality sets create coupled computation and communication bottlenecks. Multimodal agents support cross-modal alignment while training more model components and sharing bandwidth across multiple modality overlays. Under bandwidth limits, these agents can become hot spots: transfers miss aggregation windows, and their updates become stale or underrepresented, degrading...
  </details>

- **2026-10-12** — Lei Yang, Yuner Zhang, Ziyang Liu et al. — [UniMetric: Universal Metric Scale Recovery for Visual Geometry Foundation Models](http://arxiv.org/abs/2610.16945v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal foundation models, exemplified by GPT-6 Astra, raise the prospect of general-purpose embodied reasoning and planning. Using Internet videos for embodied pretraining calls for reliable physical-scale annotations. Yet visual geometry foundation models often recover scene structure and camera motion without reliable metric scale. We show that uncertain size priors of familiar objects can jointly constrain a reconstruction's shared scale. Building on this insight, we pr...
  </details>

- **2026-10-12** — Yingtao Ren, Aolin Li, Cheng Cheng et al. — [WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search](http://arxiv.org/abs/2610.16927v1)
  <details><summary>📄 Abstract</summary>
  Short-video search requires compact query rewriters that infer personalized intent from brief, ambiguous queries under strict latency constraints. The challenge is to decide when personalization is warranted and generate a reformulation that preserves the user's immediate information need. A rewriter optimized for fluency or engagement may still introduce unsupported details and redirect the search toward a different intent. Existing methods often underutilize users' actual reformulations and be...
  </details>

- **2026-10-12** — Huan Luo, Na Lu, Xiaopeng Wang et al. — [Time Window Optimization for Motor Imagery Classification via Temporal Structure Embedded Reinforcement Learning](http://arxiv.org/abs/2610.16921v1)
  <details><summary>📄 Abstract</summary>
  Online motor imagery-based brain-computer interfaces (MI-BCIs) typically decode continuous EEG using fixed-length sliding windows that may be misaligned with neural events. Existing window optimization methods often evaluate windows independently, overlooking temporal dependencies and potentially producing fragmented or physiologically implausible selections. We propose Temporal Structure Embedded Reinforcement Learning (TSE-RL), a framework that incorporates prior knowledge of MI event structur...
  </details>

- **2026-10-12** — Mattias Brännström, Themis Dimitra Xanthopoulou, Lili Jiang — [Transparent Information Flow Modeling for Role-Aware AI Act Assessment](http://arxiv.org/abs/2610.16916v1)
  <details><summary>📄 Abstract</summary>
  The European Union's Artificial Intelligence Act introduces a structured framework for governing high-risk AI systems, emphasizing transparency, risk management, and role-specific accountability. However, current assessment practices often rely on monolithic system views or disconnected checklists, limiting their ability to capture the socio-technical complexity of real-world deployments. We explore the use of the Information Flow Methodology (IFM), a modeling-based approach to AI Act compliance...
  </details>

- **2026-10-12** — Haichen He, Weibin Liu, Weiwei Xing — [Revisiting Natural Language Prompts from Large Language Models for Open-Vocabulary Video Recognition](http://arxiv.org/abs/2610.16666v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) like CLIP have shown great success in image tasks, however, applying CLIP to open-vocabulary video recognition poses challenges. Due to the limited text information, directly fine-tuning CLIP on video recognition datasets may lead to overfitting and hinder its generalizability. A prevalent method is to enrich text information by generating prompts using Large Language Models (LLMs). However, limited efforts have been made to explore how to generate higher-quality pr...
  </details>

- **2026-10-12** — Pratik Rakesh Singh, Mohammadi Zaki, Akash Saha et al. — [Making LoRA Identifiable: Orthogonal Alignment for Continual Learning](http://arxiv.org/abs/2610.16664v1)
  <details><summary>📄 Abstract</summary>
  There is growing interest in applying Parameter-Efficient Fine-Tuning (PEFT) to Continual Learning, as it enables faster training, mitigates catastrophic forgetting, and facilitates better adaptation to new tasks. Prior approaches have explored a range of strategies, including extending new LoRA branches for each incoming task, training under orthogonal loss objectives across all task-specific LoRA modules, and employing gating mechanisms to integrate new and existing LoRA modules. However, thes...
  </details>

- **2026-10-12** — Raffaele Scaringi, Alejandro Sierra-Múnera, Gennaro Vessio et al. — [KARAMEL: Knowledge-Aware Ranking for Multimodal Entity Linking in the Arts via Heterogeneous Graphs](http://arxiv.org/abs/2610.16502v1)
  <details><summary>📄 Abstract</summary>
  Discovering and disambiguating entities from multimodal and heterogeneous data is a key challenge in discovery science, where relevant knowledge is often implicit and distributed across modalities. We present KARAMEL, a framework for multimodal entity linking (MEL) - the task of aligning visual and textual mentions to entities in a knowledge base - in the cultural heritage domain. Unlike prior vision-language models that primarily rely on surface-level multimodal alignment, our approach incorpor...
  </details>

- **2026-10-12** — Yansong Liu, Litong Gong, Weijie Li et al. — [MiMaAlign: Hierarchical Micro-Macro Alignment for Physically Plausible Video Generation](http://arxiv.org/abs/2610.16482v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) diffusion models have made remarkable progress in generating high-fidelity visuals, yet their outputs still often exhibit physically implausible phenomena, including discontinuous dynamics and implausible event interactions. Existing representation alignment methods mainly transfer generic video features or short-range motion cues, treating physical plausibility as a single-level representation problem. To address this issue, we propose MiMaAlign, a hierarchical micro-macro a...
  </details>

- **2026-10-12** — Nabuat Zaman Nahim, Fairoz Nower Khan, Peizhong Ju — [A Survey of Flow Matching in Reinforcement Learning](http://arxiv.org/abs/2610.16275v1)
  <details><summary>📄 Abstract</summary>
  Flow Matching (FM) has recently emerged as a principled and efficient generative modeling framework for reinforcement learning (RL), enabling expressive, multimodal policy parameterizations via deterministic probability transport. Compared to diffusion-based policies that rely on stochastic denoising chains, FM uses sampling based on ordinary differential equations (ODEs), with learned velocity fields, which can substantially reduce inference latency and simplify the incorporation of RL objectiv...
  </details>

- **2026-10-12** — Yiyang Li, Tianyi Ma, Zehong Wang et al. — [EgoAlign: Situated 3D Understanding without Situation Descriptions](http://arxiv.org/abs/2610.16176v1)
  <details><summary>📄 Abstract</summary>
  Situated 3D Question Answering requires models to interpret a 3D scene relative to an agent's pose. Existing methods commonly convey that pose through a natural-language situation description, which may be unavailable or costly to obtain in real-world deployments. While some methods additionally incorporate numerical pose, we find that randomly shuffling the agent pose causes little performance degradation, indicating limited functional dependence on the numerical pose. To address this gap, we i...
  </details>

- **2026-10-12** — Na Min An, Taekyung Kim, Jaemyung Yu et al. — [Omni-Modal LLMs Know More Than They Say](http://arxiv.org/abs/2610.16135v1)
  <details><summary>📄 Abstract</summary>
  Omni-modal large language models (Omni-LLMs) extend LLMs to process heterogeneous modalities (e.g., vision, audio, and IMU signals) alongside language, enabling a broader range of multimodal tasks. Yet we find that these models often fail to express information from non-textual modalities even when they perceive it correctly. We term this disconnect knows-but-cannot-say. To investigate this phenomenon, we introduce Token-level Modality Alignment (TMA), which measures the alignment between indivi...
  </details>

- **2026-10-12** — Yuanfan Lin, Jie Di, Xujin He et al. — [GUIDE: Computationally Augmented Consensus for Trustworthy Clinical Practice Guidelines](http://arxiv.org/abs/2610.16108v1)
  <details><summary>📄 Abstract</summary>
  Maintaining up-to-date clinical practice guidelines (CPGs) is essential for evidence-based medicine, but rapid evidence growth and complex expert consensus formation limit timely updates. We developed GUIDE, a multi-agent copilot system for human-AI collaborative guideline generation and updating. GUIDE delegates labor-intensive tasks to specialized AI agents while preserving expert judgment and final arbitration. In 12 NICE ophthalmology datasets, GUIDE achieved 88.85% literature recall, 86.06%...
  </details>

- **2026-10-12** — Boyi Wei, Ruta Desai, Peter Henderson et al. — [Understanding and Reducing Misalignment in Persuasion Optimization](http://arxiv.org/abs/2610.16070v1)
  <details><summary>📄 Abstract</summary>
  Frontier models are now trained for complex multi-agent tasks, from running a company to engaging in negotiations. These tasks necessitate training models to be persuasive. But what does this optimization pressure mean for model alignment? In this work, we study how reinforcement learning (RL) training for persuasion affects models' use of misaligned strategies such as evidence fabrication and belief coercion, and what techniques can reduce such misalignment. We find that optimizing sender model...
  </details>

- **2026-10-12** — Soojong Kim, Hye Min Kim, Kwanho Kim et al. — [AI Representations of Mental Health Stigma: Quantifying the Gap Between AI Estimations and Human Perceptions Across Gender Groups Using GPT-Based LLMs](http://arxiv.org/abs/2610.16042v1)
  <details><summary>📄 Abstract</summary>
  The increasing use of artificial intelligence (AI) in mental health applications raises concerns about its potential to internalize and perpetuate societal biases. This research evaluates both disparities and misalignment in how large language models (LLMs), GPT-4 and GPT-5, represent perceptions of mental health across gender groups. The research comprises two studies. Study 1 applied widely adopted measures of Social Distance, Stereotypes, and Attitudes Toward Seeking Help to assess whether th...
  </details>

- **2026-10-12** — Jake Ward, Shawn Hu, Aria Wong et al. — [Gradient Routing Localizes and Removes Unintended Behaviors in RL](http://arxiv.org/abs/2610.17062v1)
  <details><summary>📄 Abstract</summary>
  We propose a mitigation to reward hacking in reinforcement learning. Our setup involves a misspecified reward function that gives rise to unintended behavior, and a monitor used to detect unintended behavior. As with frontier AI systems, the monitor makes systematic errors. Consequently, using the monitor for data filtering or to apply a reward penalty fails to prevent the model from learning unintended behavior ("reward hacking"). To address this problem, we introduce GRAFT: Gradient Routing Ad...
  </details>

- **2026-10-11** — Ronghe Qiu, Teli Ma, Jiaming Zhou et al. — [Look Before You Move: Agent-Interface-Aligned Supervision for Open-World Mobile Manipulation](http://arxiv.org/abs/2610.15572v1)
  <details><summary>📄 Abstract</summary>
  Open-world mobile manipulation requires a robot to find an object, approach it, and move it to a target receptacle from a language instruction. Training vision-language model (VLM) agents for these tasks requires demonstrations of both action selection and active vision. Existing pipelines often convert planned trajectories into high-level action labels, but shortest-path progress provides limited supervision for deciding where to look. We introduce Agent-Interface Data Alignment (AIDA), a data ...
  </details>

- **2026-10-09** — Yucheng Yang, Xiaoxiao Sun, Shusheng Yang et al. — [Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](http://arxiv.org/abs/2610.13941v1)
  <details><summary>📄 Abstract</summary>
  Multimodal diffusion transformers (MMDiTs) allow the evolving image to update internal text representations through joint attention. These representations then guide subsequent image updates, raising a question: does this feedback help correct deviations from the prompt, or preserve them? We find that image-to-text (I2T) feedback can preserve the objects and attributes already represented in the evolving image, including errors. Transplanting I2T messages can rescue failures or disrupt successes...
  </details>

- **2026-10-09** — Shaheer U. Saeed, Zion Tse, Gregory Slabaugh et al. — [Can machines reason non-verbally?](http://arxiv.org/abs/2610.13925v1)
  <details><summary>📄 Abstract</summary>
  Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems such as DeepSeek, ChatGPT and Gemini, which remain limited on visual tasks such as completing abstract patterns or delineating ambiguous regions-of-interest. Unlike explicit intermediate steps in verbal reasoning which can be verified through logic or automated tests, visual reasoning involves impli...
  </details>

- **2026-10-09** — Hajira Amjad, Valerii Serpiva, Viacheslav Liubimov et al. — [HorizonNav: Geometry-Guided Video Diffusion for Anticipatory 3D Robot Navigation](http://arxiv.org/abs/2610.13849v1)
  <details><summary>📄 Abstract</summary>
  We present HorizonNav, a video diffusion-based framework for anticipatory robot navigation that transforms a single RGB image and a text prompt into a geometrically aligned representation of plausible surrounding 3D space. Given the initial observation and a textual description of the reconstruction objective, a vision-language model, guided by designed instructions, interprets the scene and constructs structured prompts for a video diffusion model. The resulting video sequence provides plausibl...
  </details>

- **2026-10-09** — Amit Kumar Jaiswal, Sagar Uprety, Prayag Tiwari — [Tracing and Taming Hallucinated Terms via Subsequence-Association Filtering and Breadth-Aware Selection for LLM Query Expansion](http://arxiv.org/abs/2610.13810v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are now a standard source of query expansion terms but they hallucinate. They inject non existent entities and off-topic terms that add ranking noise and can hurt strong retrievers. Existing remedies such as corpus grounding, mutual verification and preference alignment treat hallucinated terms as an undifferentiated nuisance to be filtered by agreement heuristics, without a mechanistic account of why a given term appears or a principled criterion for how many terms ...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 58 papers

- **2026-10-13** — Savyasachi Gupta, Aniruddha Srinivas Joshi — [Checking the Checkers: A Synthesis of Verifier Noise and Robustness in RLVR](http://arxiv.org/abs/2610.17824v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has become a principal recipe for improving the reasoning of large language models (LLMs). It rests on the assumption that the checker scoring each response is itself correct. In practice, rule-based checkers reject correct answers in unexpected formats, unit tests accept incorrect programs, and LLM judges can be led to approve empty or adversarial responses. This work surveys 58 studies that measure, analyze, or mitigate such verifier errors...
  </details>

- **2026-10-13** — Baihong Chen, Wen Li — [AegisAsync: Symbolic Async-Event Simulation for Risks in Python Asynchronous Programs](http://arxiv.org/abs/2610.18831v1)
  <details><summary>📄 Abstract</summary>
  Security and robustness risks in Python async programs depend on event order, object identity, and execution after exceptions or cancellation. Detecting these risks requires connecting related operations across function calls and tracking their effects along execution paths. We present AegisAsync, a bytecode-based analysis of Python async risks for CPython 3.10-3.14. Its Async Event Transition Graph combines bytecode control flow, resolved calls, async events, and symbolic object relations. Boun...
  </details>

- **2026-10-13** — Chuyang Wei, Haoxiang Guan, Minghang Zhu et al. — [Self-Evolving Agent Harness](http://arxiv.org/abs/2610.18813v1)
  <details><summary>📄 Abstract</summary>
  Harness self-evolution revises an agent's software scaffolding, including prompts, memory, workflows, and executable components, while keeping model weights fixed. We formalize a feedback-driven process in which accepted revisions persist across runs. The framework separates update targets from proposal and admission mechanisms. It distinguishes changes to interpreted state from revisions to tools and code, repository-level control logic, and plugin composition. We characterize search through ev...
  </details>

- **2026-10-13** — Nutan Kumar Naik, Vijay Prasad Poudel, Aditya Kumar Saroj et al. — [AgentStripes: An Evidence-Graded Maturity Model for AI Agents](http://arxiv.org/abs/2610.18603v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks report what an Artificial Intelligence (AI) agent can do on a task suite, but not whether one released version has been engineered with the controls that make it reliable, safe and observable, or how strongly that is shown. This paper proposes AgentStripes, an evidence-graded maturity model for AI agents. It defines levels (0 to 7 stripes), process areas (12 areas holding 40 capabilities), three gates (basic, safety, proof) that hold an agent at a level however high its score, and evi...
  </details>

- **2026-10-13** — Letian Shi, Kanwal Mehreen, Deheng Zhang et al. — [Empathy Is Not the Scapegoat for Declines in Factuality and Reliability](http://arxiv.org/abs/2610.18541v1)
  <details><summary>📄 Abstract</summary>
  Language models are increasingly expected to support users in stressful or uncertain situations, where warmth and empathy are desirable. While recent work associates warmer models with reduced reliability, we show that this conclusion is incomplete. Prior studies often train primarily on empathetic dialogue, making it difficult to separate tone effects from SFT-induced distribution shift. We revisit this issue at both the model and evaluation levels. We study prompting, SFT, and RL for inducing ...
  </details>

- **2026-10-13** — Andrei Velichko — [Beyond RMSE and Granger Gain: Multi-Horizon Forecast-Error Entropy for Nonlinear Predictive Coupling](http://arxiv.org/abs/2610.18390v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether the past of an auxiliary time series provides predictive information about a target beyond that contained in the target's own history. We compare matched out-of-sample target-only and target-plus-source forecasts and introduce the forecast-error distribution entropy (FEDE) predictive-causality framework, where predictive causality is understood in the Granger sense: auxiliary history is informative when it improves prediction beyond the target's own past. FEDE quantifies h...
  </details>

- **2026-10-13** — Jophin John, Michael Hoffmann, Piroska Lendvai et al. — [Lightweight but Linguistically Fair? Quantisation Robustness across Bavarian, German, and English](http://arxiv.org/abs/2610.18343v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantisation reduces the memory cost of large language models, but it remains unclear whether compression preserves language skills of regional varieties as reliably as their standard-language counterparts. We study this question for Bavarian, Standard German, and English using BAVGROUND, a multiple-choice benchmark, where 206 source questions are aligned across all three languages. Across 14 open-weight 7B--10B instruction models, we compare BF16 with 8-bit GPTQ and two 4-bit sett...
  </details>

- **2026-10-13** — Shuqi Wang, Yiwei Zheng, Pingrui Zhang et al. — [CoSMO: Conformal Semantic Mapping for Open-World Safe Robot Navigation](http://arxiv.org/abs/2610.18321v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous navigation requires not only geometric obstacle avoidance but also semantic awareness. Different object categories demand different safety clearances, and the set of relevant categories may expand as the robot explores novel environments. Vision-language models (VLMs) offer rich semantic representations for building maps of unknown scenes, yet their confidence scores are poorly calibrated, making raw predictions unreliable for safety-critical planning. Conformal prediction (CP) c...
  </details>

- **2026-10-13** — Mengke Zhang, Tianyi Yang, Xinzhuo Li et al. — [OpenDepth: Repurposing Image Editing Priors for Robust Open-World Monocular Depth Estimation](http://arxiv.org/abs/2610.17610v1)
  <details><summary>📄 Abstract</summary>
  Recently, the integration of generative priors has revolutionized Monocular Depth Estimation (MDE), achieving state-of-the-art (SOTA) performance with remarkably high data efficiency. However, although methods based on Text-to-Image (T2I) models excel in general scenes, their efficacy degrades sharply when confronted with open-world environmental perturbations, such as illumination variations and adverse weather. Since T2I priors are optimized for semantic synthesis rather than preserving pixel-...
  </details>

- **2026-10-13** — Haodong Yang, Runhan Huang, Bowen Zhang et al. — [EqC: Equilibrium Energy Control for Introspective Lifelong Robot Learning](http://arxiv.org/abs/2610.18790v1)
  <details><summary>📄 Abstract</summary>
  Long-term robot autonomy depends on more than effective action generation: a policy must recognize when its behavior is no longer sufficiently supported and use assistance to improve. We introduce Equilibrium Energy Control (EqC), a framework for introspective lifelong robot learning built around an explicit conditional energy landscape. EqC casts generative action refinement as equilibrium-seeking optimization, while the geometry of the refinement process reveals whether the generated behavior ...
  </details>

- **2026-10-13** — Xiyin Zeng, Xuewei Huang, Yi Lu et al. — [ReEnvision: Future-Guided Selective Action Repair for Long-Horizon Manipulation](http://arxiv.org/abs/2610.17977v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic manipulation requires robust execution over sequences of interdependent actions. Existing methods typically handle execution deviations by replanning the remaining action chunk or correcting actions step by step as new observations arrive. However, a local deviation may affect only a few actions under distribution shift, yet replanning regenerates the entire chunk from an unfamiliar state, potentially introducing errors into otherwise valid actions. Step-wise correction may ...
  </details>

- **2026-10-13** — Gennady Sidorov, Valerii Kornilov, Denis Grankin et al. — [GreenWAM: A World Foundation Model for Robotics](http://arxiv.org/abs/2610.18774v1)
  <details><summary>📄 Abstract</summary>
  A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both roles across different bodies, and what makes this work. We present GreenWAM, a world foundation model for robotics, together with the recipe that produces it: (1) a shared anatomical action space that de...
  </details>

- **2026-10-13** — Bowen Ding, Mingda Wan, Yuhan Chen et al. — [ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning](http://arxiv.org/abs/2610.18683v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has emerged as the primary paradigm for optimizing Large Language Model (LLM) agents, yet efficient critic-free algorithms (e.g., GRPO) suffer from a fundamental uniform credit assignment dilemma that broadcasts trajectory-level advantages equally to all actions. Our analysis reveals that this uniformity inherently reinforces structurally invalid actions in preferred trajectories and ignores the downstream cascading influence of early pivotal deviations in unpreferred...
  </details>

- **2026-10-13** — Ziyang Song, Lia Shen, Yixuan Li et al. — [SMI: Ontology-Grounded Semantic IDs for Hierarchy-Aware Medical Concept Representation](http://arxiv.org/abs/2610.18672v1)
  <details><summary>📄 Abstract</summary>
  Biomedical language models (LMs) provide strong representations for clinical tasks, but they often fail to capture the hierarchical structure among medical concepts. This limitation is especially pronounced for rare and fine-grained clinical codes in long-tailed vocabularies, where hierarchy-agnostic LM representations become less informative as concept frequency decreases. We introduce Semantic Medical Identifier (SMI), a training-free framework for constructing ontology-grounded Semantic IDs a...
  </details>

- **2026-10-13** — Tommaso Salvatori, Matteo Forasassi, Alexis Toumi et al. — [Tiny Recursive Message Passing](http://arxiv.org/abs/2610.18649v1)
  <details><summary>📄 Abstract</summary>
  Message passing neural networks have shown remarkable performance in algorithmic and constraint reasoning, due to their ability to encode the structure of the task directly in the architecture. Recent work has shown that better results can be achieved using recursive transformers trained with deep supervision and truncated recursions, which make extremely deep loops stable to train, and equipped with test-time procedures such as discrete deduction lattices. In this work, we apply the same proced...
  </details>

- **2026-10-13** — Yifan He, Sofie Goethals, Manon Reusens et al. — [A Global View of How LLMs Value Human Time](http://arxiv.org/abs/2610.18515v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly act as personal assistants; however, little is known about how they capture national-level preferences on a global scale. Given that "time" is a universal and representative concept, we examine LLMs' time preferences by varying only users' country and measuring the compensation LLMs deem appropriate for a 60-minute appointment delay. We then compare LLMs' responses with GDP per capita on Purchasing Power Parity (GDP_PPP), Mean Income, and a literature-ba...
  </details>

- **2026-10-13** — Yu Wang, Rui Dai, Wei Chen et al. — [Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](http://arxiv.org/abs/2610.18356v1)
  <details><summary>📄 Abstract</summary>
  City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-scale 3D scene as an interactive multi-view environment, allowing a VLM agent to query landmarks, zoom into local regions, render oblique views, and commit a grounded bounding box. We optimize this tool...
  </details>

- **2026-10-13** — Jing Liu, Yongxing Qi, Ping Yao et al. — [Output Discipline Sets the Floor: A Falsification-Guided, Model-Agnostic Agent Protocol for Auditable Hypothesis-Driven Decision Making](http://arxiv.org/abs/2610.18298v1)
  <details><summary>📄 Abstract</summary>
  What binds large language models on auditable, hypothesis-driven decision tasks, where every candidate can be checked against the evidence? On the public TCMEval-SDT benchmark for Traditional Chinese Medicine syndrome differentiation (200 cases), the binding constraint is output discipline and reasoning structure, not model capability alone: two years of model scaling move zero-shot scores by only -0.03 to +0.08, while output-discipline failures (non-terminating reasoning, format non-compliance,...
  </details>

- **2026-10-13** — Guoming Ling, Yupei Lin, Zhongzhan Huang et al. — [Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models](http://arxiv.org/abs/2610.18248v1)
  <details><summary>📄 Abstract</summary>
  Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and findings. We review 119 papers to explain how methods choose what to evaluate, reco...
  </details>

- **2026-10-13** — Alexander Stromberger, Christoph Hochrainer, Valentin Wüstholz et al. — [Soliduzz: Finding Miscompilations in Smart-Contract Compilers with Assertion-Driven Equivalence Oracles](http://arxiv.org/abs/2610.18165v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts compiled to the Ethereum Virtual Machine (EVM) can manage high-value assets and are difficult to patch after deployment. Compiler miscompilations are therefore especially dangerous: compilation succeeds, but the generated bytecode does not preserve the semantics of the source program. Existing smart-contract compiler fuzzers either focus on robustness failures or rely on differential oracles that compare compiler configurations.   We present Soliduzz, an approach for finding misc...
  </details>

- **2026-10-13** —  Vatsal, Soumil Malhotra, Priyanshu Chahal et al. — [Scaling Vision Transformers Without Training: Prune-and-Merge Token Compression](http://arxiv.org/abs/2610.18039v1)
  <details><summary>📄 Abstract</summary>
  Vision Transformers achieve strong performance but incur high computational costs from quadratic token interactions. Training-free token reduction methods improve efficiency, but their robustness remains underexplored. We propose Prune-and Merge ViT, a training-free framework for off-the-shelf models. It combines class attention-based pruning with similarity-based merging to reduce redundancy while preserving semantic information. To evaluate robustness we introduce two metrics. Relative Accurac...
  </details>

- **2026-10-13** — Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa et al. — [Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation](http://arxiv.org/abs/2610.17969v1)
  <details><summary>📄 Abstract</summary>
  Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensiona...
  </details>

- **2026-10-13** — Xi Zhu, Yijie Li, Xiaofan Wang et al. — [dMRI-F: A Foundation Model for Generalizable Diffusion MRI Analysis from Sparse Acquisitions](http://arxiv.org/abs/2610.17968v1)
  <details><summary>📄 Abstract</summary>
  Diffusion MRI (dMRI) probes water diffusion within the brain, providing unique information about tissue microstructure and white matter connectivity. High-quality dMRI enables advanced and accurate analyses but demands dense acquisitions, resulting in long scan times and hardware constraints that are often infeasible. Further, dMRI requires dedicated computational methods to support diverse analysis tasks (e.g., parcellation, registration, and synthesis) for both neuroscientific and clinical app...
  </details>

- **2026-10-13** — Guanting Dong, Xinyu Yang, Jiajie Jin et al. — [Agent-Reflex: Teaching Language Agents to Act Reflectively](http://arxiv.org/abs/2610.17953v1)
  <details><summary>📄 Abstract</summary>
  Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure recovery. To bridge this gap, we propose Agent-Reflex, a general training framework for incentivizing proactive reflection in agents. Specifically, Agent-Reflex comprises three stages....
  </details>

- **2026-10-13** — Haojie Li, Xinlong Sun, Xiaohaoyang Lei et al. — [Frequency Routing and Identity Conditioning for Thermal-to-Visible Face Translation](http://arxiv.org/abs/2610.17859v1)
  <details><summary>📄 Abstract</summary>
  Thermal-to-visible (T2V) face translation has important applications in nighttime biometric recognition, low-light surveillance, and human interpretation of thermal observations. The task remains challenging because thermal images do not directly record visible appearance, while the cross-spectral cues useful for reconstruction vary across frequency components and semantic roles. Existing spatially conditioned models tend to process these cues through a homogeneous adaptation path and do not exp...
  </details>

- **2026-10-13** — Zongsheng Li, Shengyuan Zhu, Zimo Zhang et al. — [GeoNIRS: Geometry-Aware Pretraining for Heterogeneous fNIRS Representation Learning](http://arxiv.org/abs/2610.17845v1)
  <details><summary>📄 Abstract</summary>
  Functional near-infrared spectroscopy (fNIRS) provides portable and spatially localized measurements of cortical hemodynamics, but differences in channel count, probe layout, signal distribution, and task type hinder joint pretraining across datasets. We introduce GeoNIRS, a geometry-aware framework that uses source-detector locations as a shared spatial reference across heterogeneous probe layouts. GeoNIRS compresses variable-size channel sets into a fixed-size latent representation and employs...
  </details>

- **2026-10-13** — Sampath Balaji Masabathula, Srija Vanapalli, Gangadhar Kanchi et al. — [Smartphone-Based, Field-Deployed AI Inspection System for Power Distribution Infrastructure](http://arxiv.org/abs/2610.17620v1)
  <details><summary>📄 Abstract</summary>
  Routine inspection of power distribution infrastructure remains challenging for utilities operating geographically dispersed networks, where conventional manual inspection can be difficult to perform consistently and at scale. This work presents a smartphone-based AI inspection system for assessing targeted distribution-infrastructure conditions from images captured by field personnel. The proposed workflow integrates image-quality and viewing-perspective validation with AI-assisted assessment o...
  </details>

- **2026-10-13** — Fabian Spaeh, Sean Jaffe, Shandian Zhe et al. — [Foundation Models for Event Prediction Across Heterogeneous Event Logs](http://arxiv.org/abs/2610.17503v1)
  <details><summary>📄 Abstract</summary>
  Event logs are ubiquitous across real-world domains, including business processes, manufacturing workflows, healthcare, and many other operational systems. Yet event logs can differ substantially in their event semantics, label spaces, interaction patterns, and temporal scales, making it difficult to build a single foundation model that generalizes directly to previously unseen systems. We address this challenge with the Foundation Event Predictor (FEP), a simple and scalable in-context architec...
  </details>

- **2026-10-12** — Riccardo De Santi, Federico Di Gennaro, Angelo Gnazzo et al. — [LLM-to-Flow Distillation: Teaching Natural Language Goals to Scientific Generators](http://arxiv.org/abs/2610.17246v1)
  <details><summary>📄 Abstract</summary>
  Generative discovery in science requires coupling high-level scientific reasoning with the ability to generate samples respecting the structure of a design space. Yet these capabilities remain largely separated: foundation LLMs encode broad chemical and biological knowledge, while domain-specific flow- and diffusion-based generators capture the priors needed to produce valid sequences and geometries. We study how to align such scientific generators to high-level natural-language discovery goals ...
  </details>

- **2026-10-12** — Le Qiu, Zhuan Anne Zhang, Hok Ming Adeline Chan et al. — [Towards a Benchmark for Fire Safety Code Interpretation in the Hong Kong AEC Industry](http://arxiv.org/abs/2610.16127v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly explored in the Architecture, Engineering, and Construction (AEC) domain, yet their reliability in regulatory compliance remains uncertain. In this study, we evaluate the performance of LLMs on Hong Kong fire safety codes. In collaboration with domain experts, we create a localized benchmark dataset comprising both multiple-choice questions (MCQs) and open-ended questions (OEQs) to evaluate 12 widely used proprietary and open-source models. Our findi...
  </details>

- **2026-10-12** — Yan Rui Tan, Praveen Krishnapur, Zeyu Feng et al. — [Constrained Differentiable Policy Learning for Safe Quadrotor Navigation](http://arxiv.org/abs/2610.16119v1)
  <details><summary>📄 Abstract</summary>
  Differentiable simulation enables efficient policy optimization through analytic gradients, yet safety is commonly incorporated as a weighted penalty, requiring manual tuning of the trade-off between task performance and constraint satisfaction. We instead formulate obstacle avoidance as an explicit constraint and train quadrotor policies using primal--dual gradient descent--ascent through a differentiable simulator. We introduce two key components to enable effective constrained training. First...
  </details>

- **2026-10-12** — Marcos Lima Romero, Ricardo Suyama — [When LLM Agents See a Conflict but Still Proceed: Cross-Domain Dependencies in Network Slicing](http://arxiv.org/abs/2610.17118v1)
  <details><summary>📄 Abstract</summary>
  Future AI-native networks are being designed to apply autonomous agents built on large language models (LLMs) in network management through intents. When intents from different domains meet on the same resource, an agent must recognize the cross-domain dependency before taking an irreversible action. We investigate this problem through a smart-grid use case, in which a power utility holds an active intent on a backup slice for protection traffic. This slice appears idle by design, which is preci...
  </details>

- **2026-10-12** — Jun Xiao, Rui Ye, Dong Cao et al. — [VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models](http://arxiv.org/abs/2610.16567v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable ta...
  </details>

- **2026-10-12** — Xinyu Guo, Chao Jing, Li Yi et al. — [PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation](http://arxiv.org/abs/2610.16355v1)
  <details><summary>📄 Abstract</summary>
  Generalist robot manipulation can benefit from pretrained vision-language models (VLMs) for semantic reasoning and video generation models (VGMs) for world modeling. However, existing unified models that directly fuse them through shared attention at multiple layers can make it harder to draw on their specialized capabilities. We introduce PINT, a unified model that coordinates semantic reasoning, world modeling, and action generation through a shared chunk-level Predictive Intent while preservi...
  </details>

- **2026-10-12** — Xin Li, Rami Bahsoon, Tao Chen — [Why Agentic Workflows Fail: A Taxonomy Derived from Literature and Empirical Data](http://arxiv.org/abs/2610.17418v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows combine large language models with planning, memory, tools, execution environments, and iterative feedback. Their failures are difficult to diagnose because the same user-visible symptom may originate from model behavior, workflow orchestration, external tools, infrastructure, or their interaction. This paper presents a source-aware taxonomy of agentic workflow failures and applies it to evidence from academic literature and GitHub. The taxonomy combines source attribution with...
  </details>

- **2026-10-12** — Jerry Yao-Chieh Hu, Yu-An Chen, Maojiang Su et al. — [On the Statistical Mechanics of Attention](http://arxiv.org/abs/2610.17347v1)
  <details><summary>📄 Abstract</summary>
  We revisit the statistical mechanics of Transformer attention via modern Hopfield models. We present a free-energy formalism to characterize parameter regimes and critical thresholds for robust attention inference. The resulting free-energy landscape incorporates randomness in query states and attention weights. Attention then emerges as the equation of motion of the corresponding statistical-mechanical system (i.e., modern Hopfield model) through the standard free-energy minimization principle....
  </details>

- **2026-10-12** — Paul Duetting, Michal Feldman, Inbal Talgam-Cohen — [An Introduction to Contract Theory for Computer Scientists](http://arxiv.org/abs/2610.17336v1)
  <details><summary>📄 Abstract</summary>
  This survey introduces contract design to computer scientists: using outcome-based payments to incentivize effort. We discuss applications that motivate a computational approach to contract design, ranging from online labor markets, to incentive-aware algorithmic classification, to emerging ecosystems of AI agents. We present the classic principal-agent model and introduce basic concepts. We show how optimal contracts are computable via linear programming, and why they can be opaque and brittle....
  </details>

- **2026-10-12** — Lovedeep Gondara, Jekaterina Novikova, Sagarika Suresh et al. — [The Format is the Filter: Scoring Format Fixes What an LLM Judge Can Express](http://arxiv.org/abs/2610.17158v1)
  <details><summary>📄 Abstract</summary>
  When an LLM judge filters instruction-tuning data, its scoring format (binary verdict, 1--5 rating, 0--100 score, or comparison) is rarely justified or ablated. Holding the candidate pool, judge prompt, decoding and selection budget fixed, we score 15,406 UltraFeedback candidates under five formats with three judges, curate, fine-tune 66 models, and evaluate them with four judges. A 0--100 scale is worth only 7--12 equally used levels, two to three times a 1--5 scale rather than twenty, and a bi...
  </details>

- **2026-10-12** — Haolin Yang, Zhiqiang Qian, Chutian Chen et al. — [EvoQuantLab: Training-Free Dual-Loop Evolution for Auditable Quantitative Research](http://arxiv.org/abs/2610.17130v1)
  <details><summary>📄 Abstract</summary>
  Automated alpha factor discovery is critical for modern quantitative research. While large language models (LLMs) have increasingly been integrated into quantitative workflows, existing agent-based approaches remain highly susceptible to severe backtest overfitting. To address this challenge, we propose EvoQuantLab, a training-free, dual-loop self-evolving framework for robust factor discovery. Instead of relying entirely on LLM generation, EvoQuantLab deploys an inner genetic-programming (GP) l...
  </details>

- **2026-10-12** — Ankit Bhattacharjee, Indrasabarna Hari, Krityapriya Bhaumik et al. — [Beyond Model Bias: Cross-Entropy Based Rankings in Literary and Academic Texts Remain Stable across Small Language Models](http://arxiv.org/abs/2610.17040v1)
  <details><summary>📄 Abstract</summary>
  While language models provide powerful mechanisms for evaluating textual predictability, it remains unclear whether the relative extents of LM surprisal remain stable across models. This study presents empirical evidence of the invariance of ranking based on cross-entropy related measures (e.g. mean, variance of each data-point), across four distinct small scale transformer-based models, for a given dataset of text sources. We consider two stylistic environments: a corpus of contemporary poetry ...
  </details>

- **2026-10-12** — Ashwani Anand, Ivi Chatzi, Ritam Raha et al. — [MENTOR: Procedural Shielding of Tool-Using LLM Agents](http://arxiv.org/abs/2610.17039v1)
  <details><summary>📄 Abstract</summary>
  Tool-using LLM agents are increasingly used to automate workflows governed by procedural manuals, such as company rules for booking travel or procuring hardware. These manuals are written in natural language for humans and describe general requirements over such complex workflows. Ensuring compliance of LLM agents with these manuals is difficult, and state-of-the-art techniques use either LLM judges or manually written rules to forbid problematic tool-calls locally at runtime. This is insufficie...
  </details>

- **2026-10-12** — Shu Zhao, Tan Yu — [The Value of Being Wrong: Self-Mined Visual In-Context Learning from Errors](http://arxiv.org/abs/2610.16977v1)
  <details><summary>📄 Abstract</summary>
  Visual in-context learning (ICL) enables vision-language models (VLMs) to adapt at test time via demonstration examples, but its effectiveness depends critically on the examples selected. Recent counterfactual selection methods improve ICL by constructing demonstrations that expose how individual attribute changes affect the answer. However, they require multi-stage pipelines involving attribute extraction, caption engineering, and composed image matching. We propose a simpler alternative ground...
  </details>

- **2026-10-12** — Arnab Phani, Elias Strauss, Tim Schuster et al. — [ML Engineering Agents - A Data Management Perspective](http://arxiv.org/abs/2610.16919v1)
  <details><summary>📄 Abstract</summary>
  Machine learning engineering (MLE) agents are emerging as a new paradigm for automating end-to-end ML pipeline development. Using large language models for code generation and predictive performance as a machine-gradable feedback signal, these agents iteratively synthesize, execute, and refine pipeline code. Yet current systems are largely evaluated on pre-built, single-table benchmarks that abstract away key data management challenges. This tutorial introduces the foundations of MLE agents and ...
  </details>

- **2026-10-12** — Renjie Chen, Huifu Xu — [A Composite Bayesian Risk--Distributionally Robust Optimization Model for Stochastic Programming with Elliptical Distribution Ambiguity](http://arxiv.org/abs/2610.16883v1)
  <details><summary>📄 Abstract</summary>
  We study a stochastic optimization problem in which the random vector follows a semiparametric elliptical distribution with unknown location and shape parameters and an unspecified radial distribution. Assuming that the decision maker only has access to samples of the random vector, we develop a framework to jointly address parameter uncertainty and distributional ambiguity arising from this composite structure. To update the posterior distribution of the parameters, a key challenge is that the ...
  </details>

- **2026-10-12** — Ziye Guo, Ye Yuan — [Label Collapse in Diffusion Language Model In-Context Learning](http://arxiv.org/abs/2610.16839v1)
  <details><summary>📄 Abstract</summary>
  In-context learning (ICL) applies large language models to new tasks by prepending a few labeled demonstrations to a query. Prior work has studied how demonstration ordering affects ICL, but the interaction between label arrangement patterns and model biases has not been systematically examined. We define label collapse as the failure mode in which the model generates query-independent labels, and show that it is architecturally universal at the tested 8-9B scale: five models spanning autoregres...
  </details>

- **2026-10-12** — Pietro Richelli, Natalia Chepiga — [Quantum Ising transition on the Cayley tree: boundary criticality, universality, and an effective Bethe line](http://arxiv.org/abs/2610.16774v1)
  <details><summary>📄 Abstract</summary>
  We investigate quantum criticality in the transverse-field Ising model on finite Cayley trees and demonstrate that their extensive boundary fundamentally changes the nature of the quantum phase transition compared with the infinite, boundary-free Bethe lattice. Using tree tensor-network simulations for systems with up to $N=12286$ sites, we identify a boundary-driven continuous transition at $h_x^c\approx1.76$, distinct from the mean-field Bethe-lattice transition at $h_x^c\approx2.23$. We chara...
  </details>

- **2026-10-12** — Ole Beißwenger, Jan-Niklas Dihlmann, Hendrik Lensch — [Image Tokenizers Should Be Trained Between Images](http://arxiv.org/abs/2610.16759v1)
  <details><summary>📄 Abstract</summary>
  Latent diffusion models generate images as codes of an image tokenizer, whose decoder turns them into the pixel image. Recent tokenizers improve how well these codes reconstruct an image and how easily a generator learns them. Yet a generator does not reproduce the codes of training images, and when a generated code lands outside what the decoder expects, the decoded image contains imperfections. Current methods make the decoder more robust to generated codes by adding noise during training. How...
  </details>

- **2026-10-12** — Ramzi Idoughi, Radouan Boukharfane, Peter Wonka — [Learning Incompressible 3D Flows from Sparse Samples: A Set Transformer Approach to Divergence-Free Kernel Fitting](http://arxiv.org/abs/2610.16645v1)
  <details><summary>📄 Abstract</summary>
  Recovering divergence-free velocity fields from sparse and corrupted observations requires reconciling physical consistency, expressive representations, and robustness to missing data. We introduce DFK-Former, a set-to-field transformer that reconstructs divergence-free velocity fields from sparse, noisy, and irregularly sampled 3D observations. The model is inherently invariant to the number and ordering of input samples and predicts the parameters of a divergence-free kernel representation, pr...
  </details>

- **2026-10-12** — Sayantan Nag Chowdhury, Srilena Kundu — [How Mobile Oscillators Reshape Dynamical Robustness in Complex Networks](http://arxiv.org/abs/2610.16608v1)
  <details><summary>📄 Abstract</summary>
  While the robustness of collective dynamics in static networks is well established, how agent mobility and network topology jointly shape dynamical robustness remains largely unexplored. In this letter, we investigate the robustness of mobile Stuart-Landau oscillators performing random walks on networks and interacting diffusively when co-located. In the rapid-mobility regime, we reduce the dynamics to a mean-field framework linking network degree statistics to an effective global coupling stren...
  </details>

- **2026-10-12** — Haifeng Qian, David Mosallanezhad, Christian Munley et al. — [Double-Rollout Reinforcement Learning with Sampling-based Reward Estimation](http://arxiv.org/abs/2610.16593v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) implemented with Group Relative Policy Optimization (GRPO) has driven substantial progress in training reasoning language models. However, verifiable outcome rewards provide an imperfect measure of reasoning quality: a correct final answer may not be supported by the reasoning trace, whereas an incorrect rollout may contain a nearly correct reasoning trajectory. We present empirical evidence for this mismatch and hypothesize that the resultin...
  </details>

- **2026-10-09** — Hongrui Zheng, Aditya Singh, Rahul Mangharam — [SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2610.13737v1)
  <details><summary>📄 Abstract</summary>
  Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation thr...
  </details>

- **2026-10-09** — Alexander Hickey, Joanna Knight, James Bishop — [Can Language Models Play the Wikipedia Game?](http://arxiv.org/abs/2610.13948v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We const...
  </details>

- **2026-10-09** — Changhao Wang, Jaden Clark, Shuran Song — [Chronos Policy: Learning Robot Policies on Physical Time](http://arxiv.org/abs/2610.13929v1)
  <details><summary>📄 Abstract</summary>
  Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes. We introduce Chronos Policy, which makes physical time explicit by conditioning on observation capture times and desired action execution times. We study two ways to incorporate time into a diffusion transformer: adding timestamp embeddings to token featu...
  </details>

- **2026-10-09** — Weiliang Chen, Song Liao — [RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics](http://arxiv.org/abs/2610.13889v1)
  <details><summary>📄 Abstract</summary>
  As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightw...
  </details>

- **2026-10-09** — Luka Paljk, Johannes Schmidt, Vladislav Popkov — [Robust Golden Ratio universality as a consequence of a circulant symmetry](http://arxiv.org/abs/2610.13842v1)
  <details><summary>📄 Abstract</summary>
  We find a robust scenario for the emergence of the Golden Ratio (GR) dynamical universality class, characterized by the dynamical exponent $z \equiv \varphi=\frac{1}{2}(1+\sqrt{5})$. Previously, its emergence required fine-tuning of system parameters. Here, the GR universality class appears generically in a wide class of Markov processes as a consequence of a global, circulant symmetry of the flux Jacobian. This symmetry leads to GR universality in systems where the total number of conservation ...
  </details>

- **2026-10-09** — Ali Shibli, Andrea Nascetti, Yifang Ban — [Shortcut Learning in Geospatial Foundation Model Embeddings for Cross-Disaster Damage Assessment](http://arxiv.org/abs/2610.13766v1)
  <details><summary>📄 Abstract</summary>
  Geospatial foundation models can support disaster damage assessment, but high accuracy on familiar disasters may hide shortcut learning: prediction from event or scene characteristics rather than evidence that transfers to a new disaster. We study embeddings from TerraMind, Prithvi-EO-2.0, DOFA, and DINOv3 on the multi-disaster datasets xView2 and BRIGHT. Holding out an entire disaster, instead of randomly splitting image tiles, reduces mean balanced accuracy from 0.807 to 0.638 on xView2 and fr...
  </details>

- **2026-10-09** — Ibrahim Siddig, Sviatoslav Tugeev, Munir Georges — [Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge Graph](http://arxiv.org/abs/2610.13695v1)
  <details><summary>📄 Abstract</summary>
  Any automation within reliability-critical contexts such as medicine or law has to be transparent and verifiable. Despite their advantages, current LLM-based systems do not meet these requirements due to their inherent black-box nature. Retrieval Augmented Generation (RAG) attempts to ground the generative process in the relevant interpretable documents, thereby reducing the risk of AI 'hallucinations' and potentially enabling verification of the initial generation context. However, as the numbe...
  </details>

- **2026-10-08** — Vineet Kumar, Darshita Rathore, Anindya Moitra — [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](http://arxiv.org/abs/2610.12083v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-a-Judge is the standard paradigm for NLP evaluation, yet its systemic reliability remains poorly understood despite being widely treated as a deterministic ground truth. We present a comprehensive reliability audit, stresstesting six frontier models across four benchmarks, five prompt formats, two presentation orders, three sampling temperatures, and ten repetitions per condition. Our empirical analysis reveals severe vulnerabilities: verdicts change across identical replications at tempe...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 26 papers

- **2026-10-13** — Dibyajyoti Nath, Nitya Sathyavageeswaran, Ziran Min et al. — [Evidence-Governed Deployment Readiness for Networked Agents on Industrial OT Infrastructure](http://arxiv.org/abs/2610.18426v1)
  <details><summary>📄 Abstract</summary>
  Deploying a workload on a cyber-secure industrial operational-technology (OT) network requires many cross-layer prerequisites to hold at once, including persistent addressing, name resolution, time synchronization, certificate trust, proxy traversal, and reachable industrial-protocol endpoints. These are owned by different teams, yet current tools treat pre-deployment checking, fault attribution, remediation, and ongoing compliance as separate problems, so evidence is rarely reused across stages...
  </details>

- **2026-10-13** — Junkai Lin, Ge Xu, Zheng Xu et al. — [Can Agents Truly Forget? Explore Machine Unlearning for LLM Agents](http://arxiv.org/abs/2610.17659v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents have shown strong capabilities in interactive problem solving, tool use, and long-horizon task execution. However, they may also acquire sensitive or private knowledge during training and expose it during deployment. Retraining a model from scratch to remove such knowledge is prohibitively costly, making machine unlearning a more practical approach. Machine unlearning aims to remove targeted undesirable knowledge from trained models without retraining from scrat...
  </details>

- **2026-10-13** — Xiaoguang Guo, Yaohao Long, Chuxu Zhang — [BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems](http://arxiv.org/abs/2610.18780v1)
  <details><summary>📄 Abstract</summary>
  Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent and decisive error step. Recent methods trace dependencies, but knowing where information came from is not the same as knowing where it went wr...
  </details>

- **2026-10-13** — Sachin Kumar — [Looking Complete Is Not Being Grounded: Evaluating LLM Sitreps Against Human-Authored Situation Reports](http://arxiv.org/abs/2610.18762v1)
  <details><summary>📄 Abstract</summary>
  Evaluation for automatic crisis reporting should measure what practitioners need, not what is convenient to compare. Through LLM-assisted, author-approved content analysis, we derive a 15-slot information schema from professional humanitarian situation reports using qualitative content analysis, then evaluate 121 human and 261 LLM-generated reports across five disasters and three hazard types. Under google/gemini-3.7-flash on Cyclone Idai, the best machine arm is nominally above the empirical hu...
  </details>

- **2026-10-13** — Sitong Wu, Haoru Tan, Bin Xia et al. — [Unlocking Token Rewards via Training-Free Reward Attribution](http://arxiv.org/abs/2610.18704v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we propose an extremely efficient, training-free method to extract token-level reward signals directly from an existing deep reward model. Our core idea is to attribute the overall process reward to individual tokens by estimating each token's influence. This influence is defined as the change in the final macroscopic reward (e.g., the process reward) when a token is replaced with a semantically null token. Naively calculating this influence is computationally infeasible, requirin...
  </details>

- **2026-10-13** — Yunuo Chen, Xiuyu Wu, Qinhong Yang et al. — [LensErase: A Foundation Model for Erase Anything](http://arxiv.org/abs/2610.18072v1)
  <details><summary>📄 Abstract</summary>
  We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale dataset containing 101.07 million paired source-mask-target examples spanning dive...
  </details>

- **2026-10-13** — Ilie Sarpe, Theofanis Georgakopoulos, Aristides Gionis — [Exact power indices for plurality-voting ensembles](http://arxiv.org/abs/2610.17980v1)
  <details><summary>📄 Abstract</summary>
  Plurality-voting ensembles aggregate the predictions of multiple base classifiers and output the most voted class, with ties typically broken at random. Despite the simple aggregation rule, attributing the impact of each base classifier to the ensemble's predictions is far from straightforward. That is, a single base classifier's impact depends on how it interacts with the votes of all other classifiers in the ensemble, for example, in resolving ties, and not only on its own predictions. We addr...
  </details>

- **2026-10-13** — Samuel Xie, Noura Al-Moubayed — [Evaluating the Causal Faithfulness of SHAP as a Candidate Attribution Method for SAE Features](http://arxiv.org/abs/2610.17898v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders decompose language model representations into interpretable features, but feature interpretation in this literature remains predominantly correlational. Attribution methods offer more direct estimates of feature influence, yet their faithfulness to actual causal effects has not been systematically evaluated in the SAE setting. We apply SHAP-based attribution to SAE latent features and evaluate it against direct causal intervention, using sentiment classification on SST-2 with...
  </details>

- **2026-10-13** — Haochen Zhao, Minsheng Hao, Zheng Li et al. — [Benchmarking and Training Reward Models for Cross-Source Evidence Grounding in Search Agents](http://arxiv.org/abs/2610.17827v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to training and evaluating search agents focus heavily on final-answer quality, largely neglecting how generated answers map back to retrieved evidence. Recent methods track citations to enforce grounding, but citation support alone does not establish source independence or whether an answer appropriately handles conflicting evidence. We argue that credibility in open-web retrieval depends on principled cross-source evidence grounding that accounts for source independence and...
  </details>

- **2026-10-13** — Encheng Su, Pengze Li, Ziheng Hua et al. — [BRIDGE: Selective Boundary Repair with Dependency Graph Evidence in Multi-Agent Systems](http://arxiv.org/abs/2610.17805v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent collaboration has emerged as a critical paradigm for tackling complex, long-horizon tasks; however, while coordination protocols continue to advance, systemic failures at the inter-agent collaboration interface remain a pervasive bottleneck. In collaborative workflows, systems frequently suffer from \emph{broken handoffs}---where critical task context is omitted, misrouted, or ignored despite each agent emitting locally plausible responses. To address this challenge, we present \meth...
  </details>

- **2026-10-13** — Yufeng Li, Sheng Yao, Peng Zeng et al. — [Memory Echo in Single-Agent Long-Term Memory: Lifecycle Evaluation and Provenance-Guided Mitigation](http://arxiv.org/abs/2610.17763v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory supports agents across sessions. Repeated retrieval and write-back can let one historical claim occupy multiple retrieval positions and influence current answers without independent evidence. Existing work examines retrieval, updating, and question answering, leaving same-source record accumulation and post-correction persistence underexplored. Motivated by research in social cognition and memory psychology on repeated exposure, retrieval, and revision, we define \emph{Memory Ec...
  </details>

- **2026-10-13** — Tianyang Xu, Jing Gao — [Auditing Failure Attribution: Label Predictability and Judge Behavior](http://arxiv.org/abs/2610.17747v1)
  <details><summary>📄 Abstract</summary>
  Failure-attribution benchmarks ask an LLM judge which step or agent caused a failure. A high score should mean the judge checked the faulty step against the run (a cross-step check). However, spurious signals (surface cues) that predict the annotation can produce a high score. In this paper, we propose four tests to separate checking from cue use. Input restriction asks whether partial input predicts the annotation. Cue following checks whether moved cues change answers. Residual accuracy scores...
  </details>

- **2026-10-13** — Hehai Lin, Zixuan Wang, Ming Yan et al. — [MAS-Gate: Unlocking Multi-Agent System Lifecycle via Node-Centric Quantification](http://arxiv.org/abs/2610.17613v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based multi-agent systems (MAS) can solve complex problems beyond the reach of a single agent by decomposing tasks and coordinating complementary capabilities. Despite extensive research on MAS, existing work largely focuses on specific aspects or individual phases of their development and operation, resulting in fragmented perspectives with objectives and signals that are difficult to reconcile across these different settings. To bridge these disconnected perspectives...
  </details>

- **2026-10-12** — Hanyi Yu, Jiaming Cui — [Origin Attribution for Unsafe Behavior in Self-Evolving Multi-Agent Coding Systems](http://arxiv.org/abs/2610.17488v1)
  <details><summary>📄 Abstract</summary>
  As language-model-based coding agents evolve their programs and reuse code from one another, safety failures can acquire a history that extends beyond the agent in which they are detected. An unsafe change may originate in one agent, propagate through intermediate recipients, and survive subsequent revisions before an audit reveals it. Understanding this history is important for identifying the introducing change and distinguishing inherited behavior from independently occurring failures. We stu...
  </details>

- **2026-10-12** — Chia-Ming Lee, Chia-Yu Lin, Hung-Kai Huang et al. — [Doctor Trigger: A Framework for Release-Bound Face Verification](http://arxiv.org/abs/2610.16336v1)
  <details><summary>📄 Abstract</summary>
  Face swapping and generative editing enable realistic facial manipulation, while online redistribution complicates publisher oversight of circulating face images. Existing approaches establish provenance, detect manipulation, recover embedded watermarks, verify image integrity, or disrupt unauthorized face manipulation. These capabilities do not necessarily establish consistency with a specific publisher-enrolled release, limiting the evidence available for verification and human review. To addr...
  </details>

- **2026-10-12** — Aotian Chen, Frazier N. Baker, Reza Averly et al. — [ChemExplain: A Multimodal Benchmark for Explanatory Chemical Reasoning](http://arxiv.org/abs/2610.17183v1)
  <details><summary>📄 Abstract</summary>
  Current chemistry benchmarks primarily evaluate outcome prediction or reaction pathway generation, but rarely test whether a model can explain why an observed chemical effect occurs. We introduce ChemExplain, a benchmark of 1,180 multiple-choice chemistry questions drawn from 383 peer-reviewed papers. Each question pairs a molecular or reaction image with an observed chemical effect and four candidate explanations, each associated with a different structural feature visible in the image. Answeri...
  </details>

- **2026-10-12** — Ahammod Munim Ramil, Khalid Al Kafi, M. A. Abdullahis Sany et al. — [Who is the 'I' in AI? Establishing Decentralized Identity and Accountability for Autonomous Agents](http://arxiv.org/abs/2610.17126v1)
  <details><summary>📄 Abstract</summary>
  The rapid proliferation of autonomous AI agents in decentralized ecosystems challenges existing identity paradigms. While human identity is traditionally anchored in biological and/or self-asserted attributes and government credentials, AI agents lack a standardized definition of selfhood, creating critical gaps in trust and accountability. This paper introduces a novel framework for establishing Decentralized AI Identity rooted in Self-sovereign identity (SSI) principles. We propose a formal mo...
  </details>

- **2026-10-12** — D. Kochetkov — [Governing Copyright Responsibly in the Era of Generative AI](http://arxiv.org/abs/2610.17002v1)
  <details><summary>📄 Abstract</summary>
  Large language models are trained on collections that may include scholarly works, while authors generally lack work-level information about whether and how their works were used. This paper asks how copyright governance frames and operationalises the protection of such authors, and what a responsible alternative would require. Forty legislative, judicial and soft-law instruments issued between 2019 and 2026 were coded deductively against a framework derived from Responsible Research and Innovat...
  </details>

- **2026-10-12** — Ruijia Yang, Bing Xu, Zulong Chen et al. — [EHR-Bench: A Chinese Multi-Task Benchmark for Recruitment AI](http://arxiv.org/abs/2610.16689v1)
  <details><summary>📄 Abstract</summary>
  Recruitment applications span diverse operations, from drafting job descriptions and interpreting queries to organizing profiles, assessing fit, and recommending candidates and jobs. Systematic LLM evaluation therefore requires task coverage that reflects this range of business needs. We introduce EHR-Bench, an open Chinese benchmark comprising twelve tasks across six capability families and five recruitment scenarios. The tasks cover generation, extraction, classification, retrieval, semantic s...
  </details>

- **2026-10-12** — Yifan Le — [Support or Magnitude? Characterizing Neuron Relevance for Instruction Data Selection](http://arxiv.org/abs/2610.16531v1)
  <details><summary>📄 Abstract</summary>
  Model-internal signals, such as neuron activations and gradients, have been used for instruction data selection, yet how neuron relevance should be characterized remains underexplored. In particular, should selection prioritize the magnitude of relevance or how broadly it is distributed across neurons? To investigate this question, we construct sample-level relevance profiles using AttnLRP-guided attribution and introduce two complementary criteria: Effective Relevance Support (ERS), which measu...
  </details>

- **2026-10-11** — Qingzhe Han, Fan Dang, Shengqi Chen et al. — [Visually Legible but Adversarial: Watermark-Constrained Attacks on End-to-End VLMs for Document Understanding](http://arxiv.org/abs/2610.15728v1)
  <details><summary>📄 Abstract</summary>
  Visible watermarks convey document ownership, confidentiality, and status, but can also carry adversarial signals. We introduce Auto-Regional Adversarial Watermarking (AR-AWM), a model-aware white-box attack on end-to-end visual language models (VLMs) for document understanding. AR-AWM constructs a small, spatially distributed watermark-text support and optimizes only its pixels to disrupt visual representations. The attack is untargeted and question-agnostic: generation uses no questions, answe...
  </details>

- **2026-10-11** — Yue Yu, Bin Zhu, Junhui Li et al. — [ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation](http://arxiv.org/abs/2610.15814v1)
  <details><summary>📄 Abstract</summary>
  General-purpose multimodal foundation models are increasingly capable of directly controlling robots, yet improving their manipulation capabilities through autonomous interaction remains challenging. A key challenge to such self-improvement is learning from failures in complex manipulation tasks involving cross-stage dependencies, where an action may succeed locally but cause a later stage to fail. To address this challenge, we introduce ReTrace, a self-improvement framework for robotic manipula...
  </details>

- **2026-10-09** — Bhanu Tokas, Rahul Nair, Rockwell Jackson et al. — [Hide and Seek: HIDE Concepts to SEEK explanations for black box models](http://arxiv.org/abs/2610.13935v1)
  <details><summary>📄 Abstract</summary>
  Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that...
  </details>

- **2026-10-09** — Jingwei Song, Zhisheng Chen, Bingfan Zeng et al. — [MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents](http://arxiv.org/abs/2610.13829v1)
  <details><summary>📄 Abstract</summary>
  A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capability was acquired; evaluation must separate capability change from carried-over resources, unequal source exposure, and early execution failures. We construct MC-EvoBench as a controlled Minecraft benchmark with a fixed c...
  </details>

- **2026-10-09** — Tom Philipp Backert, Mohammad D. Soorati, Javad Ghofrani — [MARGoS: A Configuration-Driven Platform for Reproducible MARL Experiments in ARGoS](http://arxiv.org/abs/2610.13772v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent reinforcement learning (MARL) has become a prominent research direction, particularly within collective robotics, where the ARGoS simulator is widely used to study emergent swarm behavior. Yet despite this growth, systematic support for reuse and reproducibility in MARL-based swarm robotics remains limited and insufficiently standardized: a single experiment is assembled from manually aligned simulator files, training scripts, configuration values, paths, seeds, and environment detai...
  </details>

- **2026-10-09** — Alexander Kreusel, Maximilian Beichter, Alexandra Nikoltchovska et al. — [On the Encoding of Calendar Features in Covariate-Informed Time Series Foundation Models](http://arxiv.org/abs/2610.13676v1)
  <details><summary>📄 Abstract</summary>
  Time series foundation models (TSFMs) increasingly offer covariate support, with calendar information being the most common type of categorical covariate in practice, as it is available for every point in time. However, how these features are encoded is largely treated as an implementation detail rather than as an object of study, despite encoding being one of the few design choices left for pretrained models at inference time. With the present study, we demonstrate that the way information is p...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-13** — Bofan Xie, Chaokun Wang, Guanchen Ge et al. — [Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents](http://arxiv.org/abs/2610.18052v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval, and organization, so whether agents can forget at the user's explicit request remai...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-10-13** — Christoph Schwab, Josephine Westermann, Jakob Zech — [Operator Surrogates](http://arxiv.org/abs/2610.18210v1)
  <details><summary>📄 Abstract</summary>
  This chapter provides a mathematical introduction to operator surrogates, which are finite-parametric maps approximating complex (typically nonlinear) operators between infinite-dimensional (function) spaces.   A typical approach to constructing operator surrogates is the encoder-approximator-decoder paradigm, whereby infinite-dimensional inputs are mapped to a finite-dimensional latent space, processed, and then mapped back to the infinite-dimensional output space. We discuss various methods fo...
  </details>

- **2026-10-12** — Asad Ikram, Ella Haig — [Is the Platform Part of the Measurement? A Protocol and Simulation Study for Cross-Platform Equivalence of Machine-Labelled Policy Sentiment](http://arxiv.org/abs/2610.16757v1)
  <details><summary>📄 Abstract</summary>
  Comparing machine-labelled sentiment across social media platforms is now routine: differences in classifier scores between platforms are read as differences in public opinion. These comparisons rest on an assumption that the classifier measures the same construct, on the same scale, on every platform. Some studies check a classifier's validity platform by platform, but to our knowledge none has modelled the platform as a facet of the classifier's measurement. We adapt the psychometric equivalen...
  </details>

- **2026-10-11** — Anoop Mishra, Joshua Moore, Aly Sabri Abdalla et al. — [AutoSec-RAN: Specification-Grounded LLM Fine-Tuning for Automated Security Analysis of O-RAN](http://arxiv.org/abs/2610.15995v1)
  <details><summary>📄 Abstract</summary>
  This paper presents AutoSec-RAN, a specification-grounded large language model (LLM) framework for automated security triage of Open Radio Access Network (O-RAN) testing. Unlike approaches relying on static rule sets or privileged access to raw packet captures, AutoSec-RAN fine-tunes Mistral-7B-Instruct through two Low-Rank Adaptation (LoRA) stages over a curated corpus of 69 O-RAN, 3GPP, and adjacent standards documents, then selectively augments inference with retrieval-augmented generation (R...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 153 papers

- **2026-10-13** — Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz et al. — [Choosing LLMs for Strategic Agent Interactions](http://arxiv.org/abs/2610.18354v1)
  <details><summary>📄 Abstract</summary>
  Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM routers pick models under quality-cost trade-offs, but with no notion of a strategic structure. They do not account for an opponent that might be unknown, and that can adapt over time and shift the feedback signal. To add...
  </details>

- **2026-10-13** — Marcel Petran, Stefan Edelkamp — [When Does Opponent Modeling Pay Off? Spatial Inference Stabilises Reinforcement Learning under Partial Observability](http://arxiv.org/abs/2610.18229v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning agents in partially observable competitive games must act on beliefs about an unseen opponent's intent. We study a spatial opponent model: a transformer trained with hindsight-relabelled opponent goals that outputs a subgoal heatmap from the opponent's observed trajectory, fused early into a dueling double DQN. In symmetric constant-sum foraging games with partial observability, the module stabilises training. Plain TD(0) DQN suffers degenerate seeds in three of four ...
  </details>

- **2026-10-13** — Sophia Conrad, Fatma-Zohra Rezkellah, Christina Niklaus et al. — [Swiss4Arg: A Parallel Dataset for Multilingual Argument Mining across Swiss National Languages](http://arxiv.org/abs/2610.17894v1)
  <details><summary>📄 Abstract</summary>
  We present Swiss4Arg, a multilingual dataset for argument mining based on official Swiss voting brochures, covering all four national languages: German, French, Italian, and Romansh (a Romance minority language exclusively spoken in Switzerland). The brochures contain explicitly formulated arguments systematically organized into pro and con sections, resulting in a cross-lingually aligned resource with balanced argumentative stance. We create a dataset that comprises 53 federal voting issues col...
  </details>

- **2026-10-13** — Shikun Ban, Shohei Nagai, Qingyang Song et al. — [Learning Robot Policies for Whole-Body Mobility Assistance via Dynamic Human Motion Generation](http://arxiv.org/abs/2610.17750v1)
  <details><summary>📄 Abstract</summary>
  Robotic assistance for human mobility could benefit care recipients and reduce caregiver burden during physically demanding tasks such as Sit-to-Stand (STS) and Lift-and-Transfer (L&T). Learning robot policies for these whole-body assistive tasks is challenging: real-world data collection for human-robot interaction is costly and safety-critical, making simulation an attractive alternative. Prior work, however, typically treats the human as static or minimally responsive and thus fails to captur...
  </details>

- **2026-10-13** — Chun-Yu Hsu, Lun-Wei Ku, Chung-Chi Chen — [Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains](http://arxiv.org/abs/2610.17723v1)
  <details><summary>📄 Abstract</summary>
  People act on evaluative judgments produced by LLM agents, and in multi-agent systems those judgments pass through several agents before reaching a person. We show that a workflow's information architecture---source access, handoff format, and which model reads the untrusted content---governs how much of a coordinated manipulation reaches the end. On 32 Taiwan~2025 recall cases, ten authentic Threads comments shown to one agent move its stance by $+0.171$ toward the injected position, and a mirr...
  </details>

- **2026-10-13** — Mingxuan Yan, Litian Gong, Dihong Huang et al. — [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](http://arxiv.org/abs/2610.18869v1)
  <details><summary>📄 Abstract</summary>
  How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Ac...
  </details>

- **2026-10-13** — Trieu Nguyen, Frazier N. Baker, Ruoxi Gao et al. — [MFG: Multi-turn Feedback Guided Molecular Optimization](http://arxiv.org/abs/2610.18851v1)
  <details><summary>📄 Abstract</summary>
  Multi-objective molecular optimization is a critical process in drug discovery that aims to modify a given molecule to simultaneously improve multiple properties while maintaining a similar overall structure. This process often requires iterative modifications guided by computational or experimental feedback. Recent large language model (LLM)-based methods have begun to explore this iterative approach; however, these methods are not explicitly trained to leverage such feedback, while existing ap...
  </details>

- **2026-10-13** — Juntong Feng, Qingan Liu, Jingru Dong et al. — [Plan-Bench: Can Existing VLMs Go Well Beyond Perception to Reason and Plan in Embodied Worlds?](http://arxiv.org/abs/2610.18836v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have achieved strong performance in visual perception and spatial reasoning, leading to growing interest in using them as high-level planners for embodied AI. However, physical tasks require models to integrate spatial information, reason over temporal states, and generate multi-step plans under various constraints, raising the question of whether current VLMs can reliably support such reasoning and planning independently of execution. We introduce Plan-Bench, a ben...
  </details>

- **2026-10-13** — Qingan Liu, Juntong Feng, Yue Zhu et al. — [Game2Real-Bench: Do Toy Games Reveal and Transfer to Real-World Visual Reasoning?](http://arxiv.org/abs/2610.18834v1)
  <details><summary>📄 Abstract</summary>
  Visual reasoning is an important capability for vision-language models (VLMs) to understand visual evidence, spatial structure, constraints, and state changes. Existing evaluations mainly rely on real-world data or procedurally generated tasks. Real-world data preserve natural complexity, while procedural games provide controllable generation and verifiable solutions. However, it remains unclear whether abilities measured in toy games correspond to real-world visual reasoning and whether game ex...
  </details>

- **2026-10-13** — Farzin Salek, Masahito Hayashi — [Relative-Entropy Geometry and Convergence in Nonconvex Wiretap Optimization](http://arxiv.org/abs/2610.18785v1)
  <details><summary>📄 Abstract</summary>
  We develop and analyze an entropic descent method for a nonconvex optimization problem on probability simplices arising in classical and quantum secure communication. The optimization variables describe a randomized encoder, allowing its input distribution and stochastic preprocessing to be optimized jointly. An exact relative-entropy identity yields a channel-independent majorization bound and an explicit mirror-descent iteration with a fixed unit step size. We establish quantitative descent, c...
  </details>

- **2026-10-13** — Weida Liang, Kenji Kawaguchi — [Bayesian Test-Time Inference of Task-Aligned Similarity from Weak Interactive Feedback](http://arxiv.org/abs/2610.18656v1)
  <details><summary>📄 Abstract</summary>
  Language model systems repeatedly make test-time decisions by comparing similarity: they retrieve exemplars, rank candidates, and revise responses. Yet similarity is not unique: lexical, semantic, structural, and stylistic resemblance can point to different candidates, and the task-aligned notion can change across instances. We introduce BASIS (Bayesian Axis Selection via Interactive Signals), a training-free Bayesian method that uses weak test-time feedback to infer which criterion in a supplie...
  </details>

- **2026-10-13** — Kérian Fiter, Angelica Portocarrero, Bentley Oakes — [DTScribe: Generating Models for Digital Twin Reporting using Local Large Language Models](http://arxiv.org/abs/2610.18635v1)
  <details><summary>📄 Abstract</summary>
  The development of a digital twin brings together many stakeholders and technical components. We have previously investigated the reporting of the conceptual architecture for these digital twins as an artifact for discussion. However, we find that the activity of modeling the digital twin for visualization and consensus-building can be quite tedious and time-consuming.   In this article, we explore the automation of model generation using large language models, targeting the model required for d...
  </details>

- **2026-10-13** — Soumya Shamarao Jahagirdar, Anna Kukleva, Vishaal Udandarao et al. — [Meta-Video: Efficient Standardized Evaluation for Video Understanding](http://arxiv.org/abs/2610.18535v1)
  <details><summary>📄 Abstract</summary>
  Video understanding benchmarks are the primary yardstick for measuring progress in video-language modeling, and a growing body of work relies on them to claim improvements. The reported benchmark scores in these works, however, are almost always produced by frameworks (e.g., lmms eval) used as black boxes: certain evaluation choices like frame sampling, preprocessing, and input formatting are inherited from preset defaults and seldom inspected carefully. We show these unexamined choices are a ma...
  </details>

- **2026-10-13** — Yuming Feng, Tadd Mao, Dhruva Arekar et al. — [Aligning Faithfulness for Theory-Scale Autoformalization](http://arxiv.org/abs/2610.18498v1)
  <details><summary>📄 Abstract</summary>
  Autoformalization (AF) requires more than compilation: formal statements must preserve the meaning of their informal sources, a property known as faithfulness. An emerging frontier is the automated evaluation of this property, yet most existing methods operate at the statement level and produce whole-item verdicts, failing to reveal how individual expressions correspond or which contextual interpretations support the judgment. This omission is consequential because AF is inherently theory-scale:...
  </details>

- **2026-10-13** — Zixuan Xing, Lancheng Gao, Shengyan Li et al. — [EmoGenie: Benchmarking and Evaluating Expressed and Evoked Emotion in T2I Generation with MLLMs](http://arxiv.org/abs/2610.18455v1)
  <details><summary>📄 Abstract</summary>
  Rapid advances in artificial intelligence-generated content (AIGC) have significantly promoted using text-to-image (T2I) models to generate images with specific affective intentions. However, the emotional effects conveyed by generated images frequently deviate from target expectations, and it remains unclear whether multimodal large language models (MLLMs) can reliably interpret the emotion of AI-generated visual content. Existing affective benchmarks are predominantly built on natural images, ...
  </details>

- **2026-10-13** —  Thinker Team, Peng Gao, Jichao Jiao et al. — [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](http://arxiv.org/abs/2610.18447v1)
  <details><summary>📄 Abstract</summary>
  World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented and evolved within a shared dynamics model. In this work, we present Thinker-WM, a unified multimodal world model that jointly models and gener...
  </details>

- **2026-10-13** — Mikhail Aleksandrov, Nail Bashirov, Maksim Ivanov et al. — [Not All Drift Is a Mechanism: Tracing Prompt Adaptation in LLMs](http://arxiv.org/abs/2610.18412v1)
  <details><summary>📄 Abstract</summary>
  Prompt-based adaptation offers several ways to specialize a frozen language model, ranging from natural-language prompt optimization to learned continuous prompts. These methods are usually compared through downstream performance, although similar outputs need not arise from similar internal computations. We study how discrete prompt optimization, prompt tuning, and prefix tuning alter the processing of dense and mixture-of-experts language models. Our analysis shows that the location of the ada...
  </details>

- **2026-10-13** — Jun Tian, Yingjie Niu, Ruo Chen et al. — [DR-VLA: Learning Human-Like Quadruped Navigation from Egocentric Web Videos via Domain-Invariant Scene Representations](http://arxiv.org/abs/2610.18373v1)
  <details><summary>📄 Abstract</summary>
  Quadruped robots performing outdoor deliveries must interpret complex scenes, anticipate changes, and navigate in socially compliant ways. Robot demonstrations are costly to collect at the scale needed for generalization. Egocentric web videos offer abundant human navigation experience, but differences in viewpoint and motion make this experience difficult to transfer to robots. We introduce DR-VLA, a Mixture-of-Transformers framework that transfers human navigation experience through a domain-i...
  </details>

- **2026-10-13** — Yi Liu, Jing Zhang, Xiang Feng et al. — [Hallucination-aware Faithful Reasoning in Remote Sensing](http://arxiv.org/abs/2610.18369v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have demonstrated promising capabilities for remote sensing reasoning, yet they frequently generate visually unsupported reasoning that contradicts the visual evidence. Existing post-training methods optimize primarily for final-answer correctness, providing limited supervision for identifying and correcting hallucinations that arise during the reasoning process. To address this limitation, we propose \textbf{FaithRS}, a hallucination-aware self-reflectio...
  </details>

- **2026-10-13** — Zhengjie Shu, Wanyu Li, Di Xiao et al. — [I2O2I-Nav: A Benchmark with a Modular Agent for Long-Horizon Indoor-to-Outdoor-to-Indoor Navigation](http://arxiv.org/abs/2610.18307v1)
  <details><summary>📄 Abstract</summary>
  Service and delivery robots often need to complete long-horizon navigation missions spanning indoor and outdoor environments. Existing embodied navigation benchmarks primarily evaluate isolated stages or partial cross-domain journeys, providing limited support for assessing how heterogeneous navigation capabilities compose under continuous execution. We introduce I2O2I-Nav, a physics-enabled benchmark of 20 real-world composite scenes spanning over 115,000 square meters across multiple buildings...
  </details>

- **2026-10-13** — Yasheng Sun, Yanning Dai, Yimeng Chen et al. — [JevGPT: Thinking Fast and Slow in Autonomous Research](http://arxiv.org/abs/2610.18272v1)
  <details><summary>📄 Abstract</summary>
  Autonomous research agents must acquire and reason over evidence within a limited budget. Yet relevant sources can remain uninspected or unused, leaving a gap between retrieval coverage and the evidence that informs research. The challenge is to align fast local judgments with changing evidence needs and feed their findings back into research decisions. We introduce JevGPT, a dual-system architecture for autonomous research that couples fast evidence processing with deliberative research plannin...
  </details>

- **2026-10-13** — Zepeng Zhai, Meilin Chen — [Teach Me After You Learn It: Lookahead Self-Distillation for RLVR](http://arxiv.org/abs/2610.18256v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) has emerged as a popular training paradigm for LLMs, providing dense, token-level supervision by aligning a model's own distribution with the distribution induced by privileged information. However, existing OPSD methods derive supervision solely from privileged information of the same instance, leaving inter-instance supervision largely unexplored. We propose Lookahead Self-Distillation (LEAD), which introduces inter-instance distillation by allowing the teach...
  </details>

- **2026-10-13** — Tianyu Huai, Jie Zhou, Bo Mao et al. — [TextualRL: Textual Reinforcement Learning for Context Management](http://arxiv.org/abs/2610.18216v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can adapt to task feedback by revising the textual context that guides their behavior, without changing their model parameters. However, turning execution rewards into reusable context updates is challenging: individual trajectories offer limited comparative evidence about what to change, while task-specific fixes may overgeneralize when incorporated into a shared context. We introduce TextualRL, a gradient-free reinforcement learning framework that treats a group of rollouts from the...
  </details>

- **2026-10-13** — Jean Seo, Pepa Atanasova, Isabelle Augenstein — [Claim Framing as a Driver of LLM Sycophancy](http://arxiv.org/abs/2610.18159v1)
  <details><summary>📄 Abstract</summary>
  Sycophancy in Large Language Models, the tendency to align responses with user preferences over ground truth, has largely been studied using questions without a clear ground truth and with a single, plainly stated user opinion. We present a systematic study of which framings of a user's claim trigger sycophancy in factual question answering, where every answer is objectively verifiable without extra context. Evaluating 14 models on 42K questions, we express correct and incorrect user opinions th...
  </details>

- **2026-10-13** — Peng Jiang, Dongyang Li, Quanying Liu et al. — [ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](http://arxiv.org/abs/2610.18088v1)
  <details><summary>📄 Abstract</summary>
  Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of autoresearch systems, however, typically score isolated tasks or final artifacts, leaving these process-level capabilities largely unmeasured. We therefore introduce ResearchFlow-Eval, a fine-grained framework for assessing ...
  </details>

- **2026-10-13** — Feng Lin, Xiaotian Yu, Yifan Yang et al. — [From Agents to Edges: Paired Optimization for Multi-Agent Collaboration](http://arxiv.org/abs/2610.18069v1)
  <details><summary>📄 Abstract</summary>
  Strong individual agents do not guarantee effective collaboration. Communication must align what one agent conveys with how another interprets and uses it. This dependency makes the communication edge a natural unit of optimization. We introduce Paired Automated Communication Optimization (PACO), which jointly optimizes the instructions at both ends of each edge and their shared communication convention in systems built on black-box language models. PACO keeps model weights, agent roles, and wor...
  </details>

- **2026-10-13** — Hang He, Linting Wang, Guanming Liu et al. — [WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](http://arxiv.org/abs/2610.18067v1)
  <details><summary>📄 Abstract</summary>
  Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing construction pipelines offer limited support for such iterative refinement while keeping these components aligned. We introduce WorkRover, a framework for training long-horizon cowork agents ...
  </details>

- **2026-10-13** — Petko Petkov, Giuliano Albanese, Nikolay Nikolov et al. — [LADDER: A Long-Horizon Robot Manipulation Benchmark](http://arxiv.org/abs/2610.18053v1)
  <details><summary>📄 Abstract</summary>
  General-purpose robot manipulation policies learn short-horizon skills effectively, but degrade rapidly on long-horizon tasks. Existing benchmarks cannot isolate failures because task horizon is either too short or entangled with scene and object variations. We propose LADDER, a long-horizon robot manipulation benchmark scaling from 1 to 10 subgoals within the same environment over three suites (SimplerEnv-Long, RobotArena-$\infty$-Long, and RoboLab-Long), 145 tasks, eight categories, two embodi...
  </details>

- **2026-10-13** — Peirui Zhu, Shijie Hao, Jingxi Liao et al. — [Dynamic Interpolation for Training-Time Prediction Reshaping in Low-Light Image Enhancement](http://arxiv.org/abs/2610.18018v1)
  <details><summary>📄 Abstract</summary>
  Low-light image enhancement (LLIE) is an important image/video processing problem for reliable visual systems under poor illumination, yet it remains challenging due to the strong coupling among insufficient illumination, noise amplification, and structural degradation. Existing methods typically rely on sophisticated network architectures or engineered objective functions. While effective, the former increases model complexity and deployment burden, whereas the latter relies on empirically tune...
  </details>

- **2026-10-13** — Qingyu Lan, Zhihao Tian, Zifan Wang et al. — [TRACE: Efficient Transfer Learning for Neural Whole-Body Control Across Humanoid Embodiments](http://arxiv.org/abs/2610.17999v1)
  <details><summary>📄 Abstract</summary>
  Humanoid behavior foundation models (BFMs) enable diverse whole-body control, but adapting a pretrained controller to a new embodiment remains challenging because of kinematic and dynamic mismatch. We present TRACE, a framework for efficient cross-embodiment adaptation that preserves pretrained motion representations while specializing feedback control to the target robot.TRACE first injects kinematic priors into input and output projection layers and aligns nominal joint dynamics to reduce embo...
  </details>

- **2026-10-13** — Anand Singh, Shubham Singh, Anjali Tiwari et al. — [Enforcing a Strict Safety Margin in LLM Text Generation via Barrier Lyapunov Control](http://arxiv.org/abs/2610.17929v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed without formal guarantees against toxic text generation. Existing control barrier function (CBF) based safety filters can keep the generation trajectory within a toxicity-free region, but do not enforce a positive distance from its boundary, allowing formally safe trajectories to approach the toxicity threshold arbitrarily closely and leaving little buffer against modelling errors or disturbances. We address this limitation with a Barrier Lyapunov ...
  </details>

- **2026-10-13** — Shirong Yang, Zheyi Pan, Ying Cao — [Content-Edited Layout Generation for Graphic Design](http://arxiv.org/abs/2610.17905v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we formulate a novel form of conditional layout generation   for graphic design, termed content-edited layout generation(CELG).   CELG extends conventional content-aware layout generation (CLG), which   generates a foreground layout for a fixed background image. The key   distinction is that CELG treats the input image as an editable visual asset   and, conditioned on a textual design intention and a foreground requirement   that may be empty, produces an adapted background togeth...
  </details>

- **2026-10-13** — Shuzheng Wang, Haoxuan Li, Shengzhen Li et al. — [DriveWLA: Unifying Future Dynamics and Scene Semantics through World-Language-Action Modeling for Autonomous Driving](http://arxiv.org/abs/2610.17903v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) and world models have demonstrated strong capabilities in semantic understanding and future scene evolution for autonomous driving. However, effectively integrating both capabilities for trajectory generation remains challenging. In this work, we propose DriveWLA, a unified World-Language-Action model based on Mixture-of-Transformers (MoT) that jointly models semantic understanding, future scene dynamics, and trajectory generation. DriveWLA consists of three experts...
  </details>

- **2026-10-13** — Haolan Wei, Jiahui Wang, Junli Zha et al. — [DVTR-KD: Distilling Vision-Language Models via Intermediate Visual Token Reconstruction](http://arxiv.org/abs/2610.17853v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have achieved strong performance on diverse vision-language tasks, but their computational demands limit deployment under constrained budgets, particularly on edge devices. Many works focus on Knowledge Distillation (KD) and try to transfer knowledge from powerful teacher models to students. In addition to reducing model size, visual token compression provides a complementary route to efficiency, but introduces mismatched visual token counts that complica...
  </details>

- **2026-10-13** — Zeqiao Li, Yijing Wang, Haoyu Wang et al. — [Beyond Safe Execution: Safe Online Reinforcement Learning for Autonomous Driving with Value Calibration and Adaptive Guidance](http://arxiv.org/abs/2610.17799v1)
  <details><summary>📄 Abstract</summary>
  Online reinforcement learning (RL) enables driving policies to adapt to changing deployment conditions, but requires safe exploration throughout training. Safety filtering alone does not ensure stable policy improvement or reduced dependence on corrections. We propose Safe Online Adaptive Refinement (SOAR-Flow), a framework for safe and stable online fine-tuning of offline-initialized Flow-based driving policies. A control barrier function (CBF)--model predictive control (MPC) filter corrects po...
  </details>

- **2026-10-13** — Xu Liu, Hanshu Yan, Taha Aksu et al. — [GIFT-Eval-CTX: A Benchmark For Contextual Forecasting Model Evaluation](http://arxiv.org/abs/2610.17794v1)
  <details><summary>📄 Abstract</summary>
  Contextual forecasting seeks to improve time series forecasting by incorporating forward-looking information, such as planned events, external conditions, and expert expectations. However, reliable evaluation remains difficult: existing benchmarks often have limited domain coverage, lack standardized history-future splits, or provide text that is not guaranteed to inform the future. We introduce GIFT-Eval-CTX, a benchmark that isolates whether forecasting methods can translate verified future in...
  </details>

- **2026-10-13** — Honghao Xu, Hao Wang, Xiang Liu et al. — [TempFit: Panoptic Symbol Spotting via Template Fitting](http://arxiv.org/abs/2610.17776v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we introduce TempFit, a novel approach for the problem of Panoptic Symbol Spotting on CAD drawings. Existing methods treat symbol spotting as a per-primitive classification or mask-prediction task, with no explicit constraint enforcing that the primitives assigned to one instance form a spatially connected group. As a result, predictions may erroneously merge primitives from distant symbols into a single instance or fragment a coherent symbol across multiple predictions. Motivated...
  </details>

- **2026-10-13** — Vishisht Choudhary — [Keep Your Receipts: Trustworthy Cleanup of Agent-Built Knowledge Graphs](http://arxiv.org/abs/2610.17719v1)
  <details><summary>📄 Abstract</summary>
  Agents build knowledge graphs as memory, and building them has become easy. Maintaining them has not. When a source is retracted, overruled, or erased, everything built on top of it (entity merges, entailed edges, community summaries) must be re-examined, and the maintainer must choose between deleting too much and too little. Deployed pipelines delete only the directly extracted facts: on our corpus that reduces contaminated queries from 32.2% to 28.0% under a real retraction and changes nothin...
  </details>

- **2026-10-13** — Jinuk Kim, Rajarshi Saha, Muhammed Fatih Balin et al. — [Mixed Precision Scaling Laws for Quantized Pretraining](http://arxiv.org/abs/2610.17637v1)
  <details><summary>📄 Abstract</summary>
  Since scaling laws were introduced for modern LLMs (Kaplan et al., 2020), several works have extended them to account for quantization, tracking the emerging low-precision data types supported on AI accelerators. We develop a more accurate scaling law for quantized pretraining with mixed precision across the forward and backward passes, grounded in optimization theory and validated empirically. Our formulation separates the effects of quantization on model capacity and on optimization efficiency...
  </details>

- **2026-10-13** — Jianghong Zhou, Hao Rong, Chen Lin et al. — [Many Steps into One: Reasoning Contraction and the Limits of Safe Memory Reuse for LLM Agents](http://arxiv.org/abs/2610.17544v1)
  <details><summary>📄 Abstract</summary>
  Thought templates, skill libraries, agent memories and caches turn many reasoning steps into one. We call this reasoning contraction. A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong. Most systems trust memories by counting successes and failures. We prove that such counters are badly tuned change detectors: a symmetric counter notices a partial change only after a power of its false-alarm horizon, and an unclipped one may never notice it. O...
  </details>

- **2026-10-13** — Kaiyuan Chen, Shuangyu Xie, Uksang Yoo et al. — [RoboSimStudio: An Interactive Toolkit for Rapid Real2Sim of Robot Manipulation Tasks](http://arxiv.org/abs/2610.18835v1)
  <details><summary>📄 Abstract</summary>
  It is difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choices of solver, contact model, and physical parameters explicit and editable, allowing both humans and coding agents to iteratively refine simulations based on observed physical behavior. We implement RSS with the open Newt...
  </details>

- **2026-10-13** — Yunfu Deng, Sangwoo Shin, Brahma S. Pavse et al. — [RoboFQE: Rollout-Free Evaluation of Visual Robot Policies from Offline Trajectories](http://arxiv.org/abs/2610.18699v1)
  <details><summary>📄 Abstract</summary>
  Evaluating robot policies before deployment typically requires producing new trajectories through real-world execution, simulators, or learned world models. These rollout-based approaches impose infrastructure requirements; simulator and world-model evaluators additionally face prediction errors that can compound over the evaluation horizon. In this paper, we study off-policy evaluation as an alternative to rollout-based robot-policy evaluation methods. Specifically, we introduce RoboFQE, an eva...
  </details>

- **2026-10-13** — Eduardo Perez-Richet, Vasiliki Skreta — [Falsification-proof non-market allocation mechanisms](http://arxiv.org/abs/2610.18625v1)
  <details><summary>📄 Abstract</summary>
  Relying on manipulable characteristics to target the allocation of resources is fraught with difficulties. Naively optimal rules lead to falsification and allocative inefficiency. Optimizing the rule for allocative efficiency while accounting for falsification typically induces falsification, at a heavy cost to the agents. Moreover, falsification generates negative externalities. We characterize optimal falsification-proof rules under a broad range of falsification technologies. We also provide ...
  </details>

- **2026-10-13** — Jiaxi Huo, Petre Ricioppo, Fausto Francesco Lizzio — [CALM: Decentralized Control of Cooperative Aerial Manipulation with Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2610.18425v1)
  <details><summary>📄 Abstract</summary>
  Cooperative aerial manipulation is difficult under wind, payload motion, and noisy goal broadcasts because multiple Unmanned Aerial Vehicles (UAVs) are coupled through a shared payload. We present CALM (Cooperative Aerial Learned Manipulation), a decentralized controller for aerial manipulators carrying a basket while tracking a moving ground robot. CALM combines a parameter-shared Multi-Agent Reinforcement Learning (MARL) policy, trained using Multi-Agent Proximal Policy Optimization (MAPPO), w...
  </details>

- **2026-10-13** — Zhibo Duan, Hanlin Kong, Tianran Ma et al. — [Benchmarking Interaction-Oriented Aerial Mobility across Heterogeneous Environments](http://arxiv.org/abs/2610.18381v1)
  <details><summary>📄 Abstract</summary>
  Aerial mobile manipulation requires unmanned aerial vehicles (UAVs) to traverse heterogeneous environments such as indoor and outdoor domains, and connect navigation with subsequent physical interaction within the same trajectories. Existing aerial benchmarks are typically confined to single-environment settings, limiting evaluation of agents across continuous environmental transitions. When interaction is evaluated, agents are often initialized near the target, leaving the transition from navig...
  </details>

- **2026-10-13** — Gábor Homa, Richárd Balka, Nikolett Német et al. — [Beyond Gaussian Entanglement: Practical Criteria for Polynomially Excited Quantum States](http://arxiv.org/abs/2610.18365v1)
  <details><summary>📄 Abstract</summary>
  Polynomial excitations consisting of creation and annihilation operators are studied. Subsystem entanglement is proven produced and preserved by such manipulations. NPT entanglement already present between any two subsystems of a general pure or mixed multipartite Gaussian state is preserved under all polynomial excitations. Nevertheless, these excitations can create NPT entanglement between initially separable subsystems, implying that the number of NPT entangled pairs cannot decrease. Polynomi...
  </details>

- **2026-10-13** — Yiwei Zhang, Yantai Yang, Jin Gao et al. — [Acting Through Registers](http://arxiv.org/abs/2610.17638v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood. We identify persistent high-norm spatial outliers in WAM representations and find that their action relevance persists even after normalization and K/V projection attenuate their extreme magnitude. Motivated by this observation, we introduce RegisterWAM, which adds learnable non-spatial registers to the world mo...
  </details>

- **2026-10-13** — Xin Gao, Yifan Yang, Xin Li et al. — [AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](http://arxiv.org/abs/2610.18860v1)
  <details><summary>📄 Abstract</summary>
  Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and aesthetic quality. Image generators excel at visual design but can misrender requested content, making their outputs unreliable targets for direct reproduction. We therefore introduce AesCode, which gen...
  </details>

- **2026-10-13** — Mahsa Khoshnoodi, Sarah Adel Bargal — [RepProbe: Can Video Language Models Count Repeated Actions? A Diagnostic Benchmark](http://arxiv.org/abs/2610.18844v1)
  <details><summary>📄 Abstract</summary>
  Repetition counting requires identifying and enumerating action cycles over time. While state-of-the-art video language models describe actions fluently, they fail to reliably count how many times an action repeats. To investigate this limitation, we introduce RepProbe, a benchmark of 42K real and synthetic video clips containing exactly k in [1, 20] complete repetitions, with controls for clip position, temporal coverage, and duration. These controls allow us to study the counting failure direc...
  </details>

- **2026-10-13** — Muyao Kong, Zhihao Lin — [Read the Room Before Your Model Generates](http://arxiv.org/abs/2610.18820v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) generally rely on sampling temperature to regulate the amount of randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed, heuristic global settings and context or token-level calibration, rather than a geometrically interpretable representation of the communicative scenario. In this work, we introduce a simple and interpretable temperature selection framework, the \textbf{Scenario-Actor}, which adapts decoding to the inferred...
  </details>

- **2026-10-13** — Donghwan Kim — [Where Do LLM Ensemble Gains Come From? Decomposing Candidate Value, Diversity, and Aggregation](http://arxiv.org/abs/2610.18786v1)
  <details><summary>📄 Abstract</summary>
  LLM ensemble gains are often measured against a single baseline, but the value attributed to additional candidates can change with the comparison used. We study an LLM aggregator under four matched conditions: Direct (no candidates), Single-slot (one candidate in a multi-slot interface), Duplicate (one candidate repeated), and Multi-candidate (separately generated candidates). Under either non-diverse control, overall candidate gain (CIV) splits algebraically into an additional-candidate contras...
  </details>

- **2026-10-13** — Tianci Liu, Haoyu Wang — [Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges](http://arxiv.org/abs/2610.18766v1)
  <details><summary>📄 Abstract</summary>
  Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges provide only relative preferences, complicating their direct use for policy optimization. We propose ReVeR, a pointwise rubric RM that derives h...
  </details>

- **2026-10-13** — David Herrera-Poyatos, Carlos Peláez-González, Cristina Zuheros et al. — [What Human-AI Interaction Leaves Behind: Residual Human States -- A Trajectory-Based Framework and Multi-Study Analysis](http://arxiv.org/abs/2610.18765v1)
  <details><summary>📄 Abstract</summary>
  Human-AI Interaction is commonly evaluated by what an artificial agent enables during use, yet interaction can also alter the human who acts next. We introduce Residual Human States, a trajectory-based framework for representing the potentially multidimensional human state carried forward after interaction with AI, relative to a relevant alternative trajectory. The framework distinguishes assisted output from human-state transition and derives four empirical propositions: multidimensionality, in...
  </details>

- **2026-10-13** — Meir Feder, Ruediger Urbanke — [Learning Source Structure: Bayesian Prediction with Transformers](http://arxiv.org/abs/2610.18725v1)
  <details><summary>📄 Abstract</summary>
  A transformer trained on sequences whose source parameters are drawn afresh each time can learn only what the sequences share: the source family and its prior. The Bayesian predictor that knows both, which we call informed Bayes, is the unique minimizer of the training loss and is computable from the family alone; we use it as a quantitative, falsifiable reference. Where earlier work compared transformers with Bayes on sources whose contexts can be learned independently, we build Markov sources ...
  </details>

- **2026-10-13** — Nikos Frantzikinakis, Davide Sclosa — [Multidimensional Szemerédi Theorem for Pairwise Independent Jointly Intersective Polynomials](http://arxiv.org/abs/2610.18657v1)
  <details><summary>📄 Abstract</summary>
  We develop a new approach to the Joint Intersectivity Conjecture of Bergelson, Leibman, and Lesigne for commuting transformations. The conjecture asserts that the necessary divisibility condition is the only obstruction to polynomial multiple recurrence and, consequently, to the multidimensional polynomial Szemerédi theorem. We establish the conjecture for pairwise independent polynomials, obtaining the first general result for sequences of arbitrary length beyond the classical one-transformatio...
  </details>

- **2026-10-13** — Justin McMillen, Yasin Yilmaz — [Grid or Nodes? Probing Object Memory in World Models Under Partial Observability](http://arxiv.org/abs/2610.18637v1)
  <details><summary>📄 Abstract</summary>
  A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also sco...
  </details>

- **2026-10-13** — Andrew Piper, Edie Pearman — [The Many Morals of AI: The cautionary bias of North American news narratives in global perspective](http://arxiv.org/abs/2610.18573v1)
  <details><summary>📄 Abstract</summary>
  The stories told about artificial intelligence (AI) play a central role in shaping public understanding, policy debates, and expectations about technological change. News media are especially influential in this process. Using a cross-regional corpus of 12,924 English-language news articles about AI published since 2022, we examine how storytelling about AI varies across media systems in four regions: North America, China, India, and the Middle East. Leveraging large language models, we extract ...
  </details>

- **2026-10-13** — Ziqing Yang, Anubhav Jangra, Smaranda Muresan — [CREATE: Creativity Evaluation of VLMs using the Visual Remote Associates Test](http://arxiv.org/abs/2610.18569v1)
  <details><summary>📄 Abstract</summary>
  Vision language models (VLMs) are used in creative tasks such as visual storytelling, design ideation, art interpretation, and advertising. Yet we lack principled ways to measure the lateral reasoning of these models compared to human potential. We introduce CREATE, a semi-automatically constructed benchmark containing 155 visual Remote Associates Test problems. These problems require a solver to find an underlying connection among three seemingly dissimilar images. We conduct a human study (N=2...
  </details>

- **2026-10-13** — Michalis Pistos, Bartłomiej W. Papież — [Beyond the Encoder: Object-Centric Representations Emerging from Segmentation Foundation Models](http://arxiv.org/abs/2610.18543v1)
  <details><summary>📄 Abstract</summary>
  Foundation models are increasingly used as feature extractors for downstream tasks with limited data, typically through representations obtained from their encoders. However, foundation models trained for structured tasks such as segmentation also form object-specific representations during task execution, whose transferability remains largely unexplored. We investigate Segment Anything Model 2 (SAM2) object pointers, compact object-level representations produced through the segmentation pathway...
  </details>

- **2026-10-13** — Jinlin Liu, Wei Chen, Xiaojin Zhang — [Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale](http://arxiv.org/abs/2610.18522v1)
  <details><summary>📄 Abstract</summary>
  Reusable skills let LLM agents load task-specific instructions on demand, but they make execution depend on implicit routing over skill metadata. We test whether this design scales by holding SkillsBench tasks and their golden skills fixed while adding irrelevant skills. We find skill routing collapse: agents increasingly load fewer or no skills, even though the relevant skills remain available. With 1,000 irrelevant skills, loaded-skill recall falls from 73.6% to 27.4% and the zero-load rate ri...
  </details>

- **2026-10-13** — Swathi Shree Narashiman, Aravind Ramana Venkatramanan, Nambi Seshadri — [The Geometry of Language Model Logits: Generic Structure and Learned Departures](http://arxiv.org/abs/2610.18520v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive language models produce, at every prediction step, a vocabulary-sized logit vector whose structure determines the conditional next-token distribution. We empirically identify that the ordered vocabulary-head logits follow a remarkably consistent log-linear relation   \[ z_{(r)} \approx μ- α\log r. \] across prediction contexts, architectures, and scales, emerging progressively during pretraining. To our knowledge, this is the first systematic analysis of the logit geometry underly...
  </details>

- **2026-10-13** — Hai Lu, Yichen Luo, Luping Yu — [How Well Do LLMs Perform in Peer Review? Evidence from Finance and Accounting](http://arxiv.org/abs/2610.18435v1)
  <details><summary>📄 Abstract</summary>
  Referees increasingly use large language models (LLMs), while finance and accounting journals disagree about whether to allow it. We ask which part of a referee's job the models can do. GPT-4o, whose training data end before the 2024 conference season, referees the papers presented at the 2024 AFA and NBER finance meetings, and we compare its verdicts with publication in the top-three finance journals over the next two years. Papers the model scores one standard deviation higher are 44\% more li...
  </details>

- **2026-10-13** — Fardeen Sadab, Alif Hasnain, Afsana Shehrin et al. — [Receiver Decides Agent-to-Agent Negotiations](http://arxiv.org/abs/2610.18424v1)
  <details><summary>📄 Abstract</summary>
  When one language-model agent asks another for money, which of the two decides how much changes hands? We ran a round-robin tournament of 1,049 negotiations among fifteen agents. In each game a requester tries to raise money from a holder that has been told to keep a $100 endowment. Knowing which agent holds the money explains 47% of the variance in the amount transferred; knowing which agent asks explains 2%. Dropping the most extreme agents narrows the split to 22% against 4%. Changing the req...
  </details>

- **2026-10-13** — Ekaterina Alimaskina, Suren Kazarian, Gleb Molodtsov et al. — [Multi-Stream Residual Computation in Diffusion Language Models](http://arxiv.org/abs/2610.18407v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models reconstruct masked tokens in parallel, offering an alternative to autoregressive generation. Yet their Transformer backbones typically carry visible evidence and evolving masked predictions through a single residual stream. We equip masked diffusion models with multiple residual streams that persist through depth and adaptive routing between them, then investigate how they support these complementary roles. On the pretraining task, two streams reduce reconstruction perp...
  </details>

- **2026-10-13** — Reilly Tom, Paolo Desiati, Juan Carlos Díaz-Vélez et al. — [Reconstruction of Interstellar Cosmic Ray Anisotropy via Heliospheric Propagation Modeling and SVD Inversion](http://arxiv.org/abs/2610.18384v1)
  <details><summary>📄 Abstract</summary>
  Ground-based experiments such as the IceCube Neutrino Observatory and the High-Altitude Water Cherenkov Gamma-Ray Observatory detect cosmic-ray anisotropy on Earth, but magnetic deflections within the heliosphere complicate interpretation. Understanding the original spatial distribution of cosmic rays in the interstellar medium requires modeling particle propagation across the heliospheric boundary. We constructed a simulated transport model that backtracks antiprotons from Earth to the interste...
  </details>

- **2026-10-13** — Jiahui Sun, Ran Bi, Yifei Liu et al. — [CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations](http://arxiv.org/abs/2610.18342v1)
  <details><summary>📄 Abstract</summary>
  Urban spatial intelligence calls for 3D cities that agents can measure, interpret, and modify across successive tasks. Maintaining such cities as persistent, code-based states requires lightweight acquisition and support for consistent state updates without repeated dense reconstruction. We therefore formulate a new setting for grounded urban world construction: generating large-scale, instance-level parameterized 3D cities from one low-altitude aerial RGB image per region and known camera param...
  </details>

- **2026-10-13** — Adam T. Stevenson, Yasmin T. Davis, Daniel Sebastian et al. — [The EBLM project - XX. Absolute dynamical masses of five low-mass eclipsing binaries, and an evaluation of mass estimation methods](http://arxiv.org/abs/2610.18339v1)
  <details><summary>📄 Abstract</summary>
  Eclipsing binaries consisting of a solar-type primary and an M dwarf secondary are key laboratories to study objects at the bottom of the main sequence. Fundamental parameters of such stars have a direct impact upon exoplanetary studies, as searches for temperate Earth-sized planets focus on M dwarf hosts. Eclipsing binaries are essential to measure these parameters. However for stellar masses $<$ 0.35 M$_\odot$ , few double-lined eclipsing systems are known. Thus, stellar evolution models and e...
  </details>

- **2026-10-13** — Ben Chugg, Michael I. Jordan, Aaditya Ramdas — [Strategic Multi-Agent Resource Allocation via Statistical Contracts](http://arxiv.org/abs/2610.18336v1)
  <details><summary>📄 Abstract</summary>
  We study a class of strategic hypothesis testing problems in which a principal aims to allocate resources among competing agents who possess data or data-generating mechanisms that may be relevant to the principal's goals. Each agent can pay a participation cost to opt into a statistical contract, in which case they generate data from a private distribution and receive an allocation based on a predetermined (and publicly known) mechanism. Each agent is either "null" or "non-null" and the princip...
  </details>

- **2026-10-13** — Andrei Niculae, Adrian Cosma, Emilian Radoi — [Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators](http://arxiv.org/abs/2610.18309v1)
  <details><summary>📄 Abstract</summary>
  Choosing the right physician is a key challenge for patients seeking medical care. Physician recommendation systems identify relevant doctors, but patients still find it difficult to compare their profiles to make a decision. We formulate slate presentation optimization: given a patient's medical case and a fixed, ranked list of physicians, we generate short, case-specific summaries that make doctors easier to compare, while remaining grounded in the information in their profiles. To optimize ph...
  </details>

- **2026-10-13** — Erfan Shahabi, Amirhossein Roshandel, Mohammad Sadegh Sadeghi et al. — [SimInter: Evidence-Grounded User Simulation with Interview-Based Profile Enrichment for Conversational Recommender Systems](http://arxiv.org/abs/2610.18308v1)
  <details><summary>📄 Abstract</summary>
  Conversational Recommender Systems (CRSs) require reliable user simulators for cost-effective evaluation. LLM-based simulators have made realistic simulation possible but typically condition on profiles derived from explicit ratings, demographics, and static sources capturing surface preferences while omitting implicit behavioral characteristics such as decision-making style, aspect-level preferences, and domain expertise. We propose SimInter, a pipeline that elicits these attributes via synthet...
  </details>

- **2026-10-13** — Boya Zhang, Yuanchao Ma, Jiageng Wu et al. — [PAINT: A Framework for Multilingual Pain Representation from Medical Licensing Exams to Real-World Clinical Texts](http://arxiv.org/abs/2610.18269v1)
  <details><summary>📄 Abstract</summary>
  Pain is one of the most common and clinically important symptoms, reflecting disease onset, progression, and treatment response. However, pain is difficult to accurately capture and interpret from medical text, as its expression varies across languages, documentation types, and patient demographics, and is often embedded in terminology, negation, temporality, and contextual descriptions. Existing pain-related studies remain largely monolingual or limited to narrow clinical settings. In this stud...
  </details>

- **2026-10-13** — Yichi Wang, Wangjin Zhou, Yizhou Zhang et al. — [Collapse, Repair, and Drift: Dissecting Fine Tuning Dynamics in Speech Language Models](http://arxiv.org/abs/2610.18192v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine tuning (SFT) is commonly monitored through training and evaluation loss, but loss does not fully characterize how model functionality evolves along the same trajectory. We study this gap through dialect adaptation of Qwen3-ASR, MiMo-Audio, and FireRed-LLM across learning rates from $10^{-5}$ to $10^{-3}$. Character error rate (CER) reveals pronounced transient collapse and recovery whose severity and temporal structure are only weakly reflected by loss. Bidirectional layer patchi...
  </details>

- **2026-10-13** — Fabian Lukassen, Christoph Weisser, Alexander Silbersdorff — [Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges](http://arxiv.org/abs/2610.18122v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models (TDMs) return a probability for each allowed answer instead of generating text, which makes them candidates for cheaply replacing LLM judges that compare two answers. Whether they share the biases of LLM judges is untested. We run the CALM benchmark's bias tests on eight TDMs and seven LLM judges of 2024 and 2026. Every TDM is biased, in three to eight of twelve tests. Emotional tone affects them most, and rewriting the better answer in such a tone lowers the accuracy of a ...
  </details>

- **2026-10-13** — Donghoon Jung, Min Kim, Seojin Choi et al. — [Narrative Lookahead in LLMs: Event-Level Decodability, Predictive Advantage, and Steering](http://arxiv.org/abs/2610.18121v1)
  <details><summary>📄 Abstract</summary>
  Do language models carry information about narrative events before writing them, and how far ahead? We examine narrative lookahead through salient, state-changing events rather than tokens or response-level attributes. We extract 23,355 LLM-annotated events from 2,000 stories generated by four open-weight LLMs, labeling them along three nonexclusive dimensions of change: within agents, between agents, and in the story world, with human validation on a subset. Event segmentation and plot-independ...
  </details>

- **2026-10-13** — Cesare Barbera, Luca Stradiotti, Lorenzo Cascioli et al. — [A CaLLM Judge is a Better Judge: Mitigating Bias in LLM-as-a-judge](http://arxiv.org/abs/2610.18108v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used as judges to predict which of two candidate answers a human evaluator would prefer, providing a scalable alternative when human evaluation is too costly. Unfortunately, LLM judgments can exhibit systematic biases. Prior work has documented position, verbosity or model family of the candidate answers influencing the judge decision rather than their quality, while additional biases may remain undocumented. $\textit{Multicalibration}$ provides a na...
  </details>

- **2026-10-13** — Haowei Li, Yi Bu — [Interpreting Paper-to-Patent Citations in AI-Related PMC Articles](http://arxiv.org/abs/2610.18109v1)
  <details><summary>📄 Abstract</summary>
  Paper-to-patent citations connect scientific and technological documents, but their interpretability depends on how patents are used in the citing text. This study examines citation contexts and paper-level outcome associations in AI-related articles in PubMed Central (PMC). Screening 189,073 articles identified 746 with explicitly tagged patent references (0.395%), including 713 with 1,544 identifiable in-text patent-citation instances. Three large language models classified these instances by ...
  </details>

- **2026-10-13** — Ziqi Zhang, Chandan Mondal, Siqi Xu et al. — [Color Lorentz force on a transversely polarized quark in the nucleon](http://arxiv.org/abs/2610.18063v1)
  <details><summary>📄 Abstract</summary>
  The $x^2$ moment of the genuine twist-3 component of the unpolarized scalar parton distribution function $e(x)$ is related to the average transverse color Lorentz force experienced by a transversely polarized quark in an unpolarized nucleon. This higher-twist quantity probes quark--gluon correlations and provides unique insight into the nonperturbative dynamics of quantum chromodynamics. For the first time, we study the corresponding off-forward matrix element and derive its Lorentz-covariant de...
  </details>

- **2026-10-13** — Slimane Larabi — [Beyond Black Boxes: Visual Grounding for Text Embeddings](http://arxiv.org/abs/2610.18047v1)
  <details><summary>📄 Abstract</summary>
  In this paper, our goal is to represent text embeddings as sketches for three main reasons. First, to visualize text representation and to explore their potential their potential for AI explainability. Second, to investigate the potential benefits of the sketch-based representation for information retrieval. Third, to explore their potential for reasoning, drawing inspiration from the concept of mental imagery. We propose a sketch-based visual grounding framework that transforms text representat...
  </details>

- **2026-10-13** — Kaipeng Fang, Hangxu Liu, Chaojian Shi et al. — [Data-Free Continual Learning for World Action Model with Rectified Generative Replay](http://arxiv.org/abs/2610.18038v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) built on pretrained video generation models adapt quickly to new robotic tasks, but they forget previously learned tasks under sequential fine-tuning. Experience replay (ER) mitigates such forgetting by rehearsing data of previous tasks, yet this data is often unavailable in robotics, where a policy is deployed as weights only and its training data is not shared along with it. In this work, we ask whether a WAM can achieve data-free continual learning by regenerating i...
  </details>

- **2026-10-13** — Harshit Joshi, Priyank Shethia, Monica S. Lam — [SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces](http://arxiv.org/abs/2610.18025v1)
  <details><summary>📄 Abstract</summary>
  Test-time scaling has enabled LLMs to solve increasingly complex reasoning, discovery, and optimization tasks. However, existing approaches often gather observations while seeking evidence for current hypotheses, then generate new hypotheses conditioned on those hypotheses and their associated evidence. This couples observation discovery to existing hypotheses, favoring local refinements over exploration of unknown hypotheses regions. Inspired by the hypothetico-deductive method (Hempel, 1945) a...
  </details>

- **2026-10-13** — Zhiwei Chen, Zhongtao Rao, Waikit Xiu et al. — [LatentRemedy: Efficient Remedy For Non-Prefix KV Cache Reuse in Multi-Agent Systems](http://arxiv.org/abs/2610.18014v1)
  <details><summary>📄 Abstract</summary>
  Non-prefix KV cache reuse is a promising approach for improving inference efficiency in multi-agent systems as agents share the same context blocks. However, when agents have conflicting tasks, directly reusing non-prefix KV caches across agents can severely degrade model performance, causing up to a 90% drop. Existing remedies, including selective recomputation and offset-based calibration, recover a limited fraction of this loss. We argue that the problem lies not only in contaminated KV repre...
  </details>

- **2026-10-13** — Sadif Ahmed, Soumya Swagata Biswas, Rifat Shahriyar et al. — [Seeing Through the Forgery Is Not Enough: Regressive Sycophancy under Fabricated Evidence in Medical Vision-Language Models](http://arxiv.org/abs/2610.17989v1)
  <details><summary>📄 Abstract</summary>
  A medical vision-language model may analyze a given CT scan and correctly detect both kidneys in view. Continuing this conversation, if a user provides a prescription with an opposite direction, medical VLMs often sycophantically choose to realign their diagnosis. In this work, we study regressive sycophancy under fabricated evidence, where a model abandons a correct answer when pushback comes with a fake document. We test four open VLMs on 400 VQA-RAD yes/no questions in 19,200 multi-turn conve...
  </details>

- **2026-10-13** — Zhengtao Zou, Pekka Marttinen — [Seeing Depth but Choosing Cues in Vision-Language Models](http://arxiv.org/abs/2610.17976v1)
  <details><summary>📄 Abstract</summary>
  Do vision-language models use depth information to judge which object is closer, or rely on image-plane cues? We investigate this question through controlled depth--cue conflicts, representation analysis, and interventions. Among the many image-plane cues relevant to depth perception, we focus on apparent size and vertical position. We compare depth judgments under cue-consistent and cue-conflict conditions in both rendered scenes and real-world photographs. Across model families and scales, dep...
  </details>

- **2026-10-13** — Hanzhi Zhang, Anxuan Che, Hang Qi et al. — [Quota-Based Aging for Prediction-Guided Scheduling in LLM Serving](http://arxiv.org/abs/2610.17795v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) serving systems use token-level continuous batching to improve resource utilization, but heterogeneous response lengths complicate request scheduling. Prediction-guided short-first scheduling reduces average latency but can severely delay long requests, while unrestricted aging may over-promote delayed long requests under congestion. We propose Quota-Based Aging (QBA), a lightweight policy that combines predicted short-first admission with quota-bounded, debt-enforced ...
  </details>

- **2026-10-13** — Nam V. Nguyen, Hoang Van Truong, Hieu D. D. et al. — [Agentic4PDM: Host-Governed Evidence Admissibility for Industrial Fault Diagnosis](http://arxiv.org/abs/2610.17786v1)
  <details><summary>📄 Abstract</summary>
  We study industrial fault diagnosis as a classification task that assigns sensor time-series windows to predefined health states or fault types. Scarce labels and changing operating conditions make repeated training of specialized classifiers costly. Yet structures such as periodicity, trends, and transients can remain diagnostically informative and be examined through reusable analytical tools. LLM agents can select and interpret these tools, but fixed rules or training-derived guidance may not...
  </details>

- **2026-10-13** — Haoyu Zhang, Siming Li, Zeyu Zhang et al. — [Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation](http://arxiv.org/abs/2610.17651v1)
  <details><summary>📄 Abstract</summary>
  Recent coding large language models (LLMs) can synthesize dynamic 4D worlds from natural language, but the resulting content remains a visual artifact. It lacks physical semantics such as the collision geometry, mass, friction, inertia, and joint structure, required to enable it to simulate the physical world, and its dynamics are scripted to look plausible rather than designed to execute. What is needed is an executable world: one that a physics engine can load and step, resolving contact physi...
  </details>

- **2026-10-13** — Baolin Chong, Fuhui Zhou, Qihui Wu et al. — [Low-Altitude Agentic Networks: From UAV Connectivity to Workflow-Driven Capability Orchestration](http://arxiv.org/abs/2610.17642v1)
  <details><summary>📄 Abstract</summary>
  Low-altitude platforms are evolving from connected sensing nodes into autonomous agents capable of bounded task interpretation, skill invocation, and local decision making. Increasing the intelligence of individual unmanned aerial vehicles (UAVs), however, does not resolve the organization problem that arises when mission workflows depend on capabilities distributed across multiple platforms and provider feasibility changes with network, resource, and mobility conditions. We propose low-altitude...
  </details>

- **2026-10-13** — Weitong Li, Donglin Song, Junkai Lin et al. — [Beyond Bias Scores: Answerability Confounds in Activation Steering with Gradient-Constrained Direction Design (GCD)](http://arxiv.org/abs/2610.17641v1)
  <details><summary>📄 Abstract</summary>
  Bias scores in language-model evaluations often conflate what a model prefers with whether it answers at all. We identify this confound in \textsc{BBQ}, whose ambiguous score factorizes into answerability and signed preference. Across 11 categories, 28,}824 items, and five models, contrastive steering lowers the signed ambiguous score in 11/11 categories but lowers the signed disambiguated preference score in only 8/11. Across 99 configurations, the answerability channel exceeds half of the obse...
  </details>

- **2026-10-12** — Shiqi Liu, Yihang Yao, Peide Huang et al. — [MIRROR: Reflecting Hidden Symmetries from Offline Robot Interaction Data](http://arxiv.org/abs/2610.17422v1)
  <details><summary>📄 Abstract</summary>
  Symmetry-aware robot policy learning requires coupled observation-action transformations. For pixel observations, even simple physical symmetries can induce complex, viewpoint-dependent image transformations that are difficult to specify by hand. Existing symmetry-aware methods often rely on representations with predefined transformations, requiring preprocessing tailored to the sensing setup and task. We introduce MIRROR, a framework that learns how a known symmetry group operates jointly on ob...
  </details>

- **2026-10-12** — Ian Foster — [Agency as a New Organizing Abstraction for Computer Science](http://arxiv.org/abs/2610.17410v1)
  <details><summary>📄 Abstract</summary>
  Advances in large-scale machine learning have enabled agentic AI systems: persistent, autonomous computational entities that pursue goals, initiate actions, and interact with open environments. These systems are often framed as applications of foundation models. We argue that this framing is incomplete: agency is also a candidate new organizing abstraction for computer science. What is new is not the concept of an agent, nor runtime policy generation per se, but its general-purpose, open-ended f...
  </details>

- **2026-10-12** — Maor Ben Shahar, Jonathan Morag, Dirk Englund et al. — [Quantum Cryptography and Autoformalization in Lean](http://arxiv.org/abs/2610.17286v1)
  <details><summary>📄 Abstract</summary>
  Quantum key distribution provides secure communication by relying on physics principles and mathematical reasoning. Security proofs across the field can contain gaps, often between individually valid theorems integrated under mismatched assumptions. We produce an end-to-end security theorem formalized in the Lean proof assistant, eliminating hidden hypotheses by building only on Lean's standard axioms. Our proof covers composable security of the entanglement-based qubit BB84 protocol against coh...
  </details>

- **2026-10-12** — Alexey Tuzikov — [RoboBugBench: Benchmarking Automated Repair of Real Robot Software Under an Audited Behavioral Oracle](http://arxiv.org/abs/2610.16369v1)
  <details><summary>📄 Abstract</summary>
  Language agents increasingly modify robot software, but whether they can repair it is unmeasured, because the domain supplies no oracle to inherit: a robot bug manifests as behavior, and robot repositories ship almost no tests that capture it. We present RoboBugBench, a benchmark of 33 real, execution-validated defects in a pinned ROS 2 navigation stack, in which a candidate patch is graded by compiling it and driving the robot through a physics simulation rather than by running a unit test. Thr...
  </details>

- **2026-10-12** — Yating Wang, Kui Wu, Ran Yi et al. — [HairFlow: Modeling 3D Hair Strands with Multi-Modal Conditioned Diffusion](http://arxiv.org/abs/2610.17348v1)
  <details><summary>📄 Abstract</summary>
  Modeling 3D hair strands is challenging due to complex hairstyle geometry, scarce high-quality training data, and incomplete or noisy input observations. Foundation models offer broader hairstyle priors, but their outputs are not directly usable for strand-based rendering and simulation. Existing approaches require costly per-instance optimization to fit hair priors to meshes from foundation models and 2D orientations from specialized predictors trained on limited hair data, restricting efficien...
  </details>

- **2026-10-12** — Han Yu, Wenhui Zhu, Jincheng Cao et al. — [Budgeted KV-Cache Repair for Evolving Contexts](http://arxiv.org/abs/2610.17338v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents revise their working context as information becomes obsolete, but deleting text does not erase its influence on cached computation. Later key-value (KV) states remain conditioned on the deleted content, while recomputing the entire retained suffix can be costly. We introduce budgeted KV-cache repair: recovering task performance by recomputing a user-chosen fraction of the retained suffix. Comparing repair allocations under identical relevance scores and token budgets, we fi...
  </details>

- **2026-10-12** — Thomas Bartz-Beielstein — [Deleting Code Without Losing Knowledge: Regenerative Software for Python Libraries](http://arxiv.org/abs/2610.17197v1)
  <details><summary>📄 Abstract</summary>
  In the age of "Software 3.0", when a complete program can be rewritten in minutes by an agent, the traditional approach of relying on code as the sole source of truth becomes questionable. Fowler advocated for a set of seven primitives, which lay the framework for regenerative software, so that programs can be deleted and rebuilt without losing their knowledge. The knowledge lives in machine-readable records in a tracked directory, from which a *regeneration bundle* is built for each unit. The r...
  </details>

- **2026-10-12** — Matthew Rendall, Max Hellrigel-Holderbaum, Leonard Dung — [Superintelligence and the Triple Risk of an AI Race](http://arxiv.org/abs/2610.17085v1)
  <details><summary>📄 Abstract</summary>
  On many estimates, artificial general intelligence (AGI) is likely to emerge within the next few decades or even sooner. Once it does, it may quickly surpass human intelligence, possibly by a huge margin. Some believe that the country that develops AGI first could attain global dominance. This prospect risks setting off intense competition between the United States and China. Indeed, a narrative has already developed that the superpowers are locked in an AI race, with the Trump administration pr...
  </details>

- **2026-10-12** — Sergei Polezhaev, Saba Anjum, Michael Gormish — [SpectralBridge: Adding High-Frequency Capability to Large Audio-Language Models](http://arxiv.org/abs/2610.17048v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have become highly capable on a wide range of tasks spanning speech, music, and environmental sound. However, many modern LALMs resample input audio to 16 kHz mono, making all frequencies above 8 kHz unobservable. We present SpectralBridge, a lightweight extension that gives such a model access to the 8-16 kHz band by joining low- and upper-band representations with time-aligned paired cross-frequency attention. Applied to Audio Flamingo Next, the method train...
  </details>

- **2026-10-12** — Qian Li, Yuxiao Hu, Qihao Duan et al. — [Learning to Design SR Solvers: Harness Optimization for Symbolic Regression](http://arxiv.org/abs/2610.16966v1)
  <details><summary>📄 Abstract</summary>
  Symbolic regression (SR) seeks explicit equations that explain observed data, and recent methods increasingly employ large language models (LLMs) and agents for equation discovery. However, these systems typically rely on manually designed workflows and prompts. We argue that the SR agent harness should itself be an optimization target: its design shapes search priors and how numerical feedback guides subsequent equation refinement. We therefore propose HarnessSR, a framework for jointly optimiz...
  </details>

- **2026-10-12** — Wenjing Bian, Ranran Huang, Andreas Geiger — [ViewStruct: View-Grounded Articulation and Connectivity Inference](http://arxiv.org/abs/2610.16793v1)
  <details><summary>📄 Abstract</summary>
  Interacting with unfamiliar objects requires understanding how their parts connect and move. We introduce ViewStruct, a framework for jointly predicting connectivity and articulation in objects and scenes. Given an RGB image with aligned part segmentation and depth, optionally supplemented by images or video, ViewStruct predicts rigid-body groupings, attachments, and joint parameters. Its view-grounded representation links predictions to observed regions and expresses joint geometry in a gravity...
  </details>

- **2026-10-12** — Chiheng Lou, Xiangwei Deng, Bangjun Xiao et al. — [Prorsa: Unleashing the Potential of Prefill-Decode Disaggregation in Agentic Reinforcement Learning](http://arxiv.org/abs/2610.16592v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) is commonly used to enhance the capabilities of large language models (LLMs) in solving complex multi-turn tasks. During rollout, agentic RL exhibits a workload pattern distinct from that of traditional RL: multi-turn interactions repeatedly introduce prefill requests, causing prefill and decode workloads to coexist throughout rollout. This workload makes prefill-decode (PD) disaggregation, a design widely used for online LLM serving, promising for speeding up...
  </details>

- **2026-10-12** — Jialei Wang, Zehan Wang, XiaoYang Wu et al. — [CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](http://arxiv.org/abs/2610.16577v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing reference videos as editable dynamic 3D scenes is an important path toward controllable video generation for filmmaking: these scenes provide modifiable, renderable visual proxies that enable explicit control over scene layout, subject actions, and camera behavior. To evaluate agents' ability to reconstruct editable dynamic 3D scenes from dynamic reference videos, we introduce CineRecon, a benchmark comprising 50 reference videos and 360 annotated evaluation clips. The reference v...
  </details>

- **2026-10-12** — Zhixiong Zhao, Zukang Xu, Xing Hu et al. — [LoopQuant: Accurate and Efficient Post-Training Quantization for Looped Transformers](http://arxiv.org/abs/2610.16368v1)
  <details><summary>📄 Abstract</summary>
  Looped Language Models (LoopLMs) improve parameter efficiency by recursively reusing shared Transformer modules, yet their repeated computation over evolving recurrent states poses new challenges for low-bit deployment. Existing post-training quantization (PTQ) methods, largely designed for feed-forward Transformers, fail to account for cross-loop activation dynamics, heterogeneous loop sensitivity, and recursive error propagation, leading to substantial performance degradation at low precision....
  </details>

- **2026-10-12** — Jialu Sui, Hongsheng Zhang, Rui Liu et al. — [Building age estimation based on widely available multi-source1 geospatial data](http://arxiv.org/abs/2610.16320v1)
  <details><summary>📄 Abstract</summary>
  Building age is fundamental for urban infrastructure safety, operation, and planning, as it directly affects structural safety, and sustainable development. Existing methods mostly rely on detailed building information such as street view, function, or materials, which are harder to obtain than geospatial data like satellite imagery and Digital Surface Models (DSMs). However, existing methods based on those geospatial data mainly rely on optical imagery and local texture features, limiting their...
  </details>

- **2026-10-12** — Yike Wu, Keyan Chen, Qixiong Wang et al. — [ReTAC: Residual Test-Time Agentic Computation for Video Spatial Reasoning](http://arxiv.org/abs/2610.16315v1)
  <details><summary>📄 Abstract</summary>
  Test-time agentic computation can improve multimodal large language models (MLLMs) through planning, tool use, iterative perception, and reflection, but indiscriminate computation may duplicate resolved work, introduce noisy evidence, and perturb correct predictions. We propose that such computation should be residual: allocate additional computation only to requirements unresolved by the base model and, after a localized failure, recompute only the affected states. We instantiate this formulati...
  </details>

- **2026-10-12** — Helong Hu, Hongdan Pan, Shuiqing Hu — [FON: A Draft-Revise Dual-Organ Language Model without Sequence-Level Quadratic Attention](http://arxiv.org/abs/2610.16301v1)
  <details><summary>📄 Abstract</summary>
  Self-attention assigns two functions to one mechanism-where to read and how to mix-at the price of O(L^2) training, an O(T) decode state, and position signals bound to the training length. Existing attention-free alternatives all optimize the single function of generation. We propose FON (Fusion-Organ Network), which differentiates one weight stack into a drafting organ (multi-tap learnable delays + content-adaptive recursion; causal, O(S) training, O(1) decode state, no sequence-level quadratic...
  </details>

- **2026-10-12** — Jinwoo Chung, Jangho Kim — [Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution](http://arxiv.org/abs/2610.16261v1)
  <details><summary>📄 Abstract</summary>
  Mamba-based super-resolution models are efficient alternatives to Transformer-based restoration backbones, but their low-bit post-training quantization remains challenging because selective scan, Mamba's input-dependent state-space operator, induces different activation ranges across spatial tokens. Thus, a single layer-wise clipping range poorly matches all tokens. We propose Token-Group Quantization, a hardware-friendly activation PTQ framework that statically approximates a hardware-unfriendl...
  </details>

- **2026-10-12** — Ziyi Liu, Tzu-Sheng Kuo, Jiale Liu et al. — [Learning to GUIDE the Group: Self-Learning LLM Facilitation Across Multi-Party Tasks](http://arxiv.org/abs/2610.16231v1)
  <details><summary>📄 Abstract</summary>
  As large language models are increasingly adopted as multi-party communication facilitators, there is a growing demand for agents capable of balancing diverse group dynamics across contexts. However, existing LLM facilitators are often fine-tuned for task-specific objectives; generalized LLM-based facilitation methods that can adapt to different types of tasks and diverse group dynamics are underdeveloped. To address this gap, we present GUIDE (Generalized Unified Intervention for Dynamic Exchan...
  </details>

- **2026-10-12** — Zhifan Zeng, Wenbo Xiao, Arcot Sowmya et al. — [DIGS: Distribution-Informed Gaussian Splatting for Training-Free Open-Vocabulary 3D Segmentation](http://arxiv.org/abs/2610.16177v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D Gaussian segmentation typically binds semantic features to the per-Gaussian state via per-scene gradient training (1-4 h) or the more recent closed-form distillation. Both commit each primitive to a single feature; therefore, boundary Gaussians spanning multiple 2D instances are forced into a hard decision that degrades retrieval accuracy and yields unstable mask boundaries at render time. We present DIGS, a training-free framework with two stages, class-agnostic mapping and m...
  </details>

- **2026-10-12** — Zhaoyu Fan, Bowen Han, Jincheng Ou et al. — [ProCARE: Real-World Study Automation via Profile-Grounded Evidence Contracts](http://arxiv.org/abs/2610.16175v1)
  <details><summary>📄 Abstract</summary>
  Real-world studies (RWS) analyze routinely collected healthcare data, such as electronic health records and insurance claims, to estimate treatment effects, monitor safety, and identify risk factors outside randomized trials. Automating RWS with large language model agents is appealing but brittle: valid analyses depend on dataset-specific clinical semantics, including index dates, follow-up windows, patient/event-level units, and outcome boundaries that are often implicit in observational data....
  </details>

- **2026-10-12** — Wei Shan, Tianyi Zhang, Yuan Zong et al. — [Cross-Protocol Personality Assessment with LLMs: Aligning Behavioral Evidence with Human Ratings](http://arxiv.org/abs/2610.16050v1)
  <details><summary>📄 Abstract</summary>
  Personality assessment from asynchronous video interviews (AVIs) plays a crucial role in recruitment by enabling standardized and behaviorally grounded evaluation for job applicants. However, most of the previous works are confined to a single interview protocol. Independently collected protocols differ in question sets and question-trait mapping. Thus, the human-rated evidence from one protocol cannot be used directly under another. To address this limitation, we propose the Cross-protocol Evid...
  </details>

- **2026-10-12** — Jack B. Jedlicki, Amish Sethi, Heng Yang — [Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?](http://arxiv.org/abs/2610.17350v1)
  <details><summary>📄 Abstract</summary>
  We use a frozen frontier vision-language model, GPT-6-Astra, directly as the robot policy on RoboMME, a benchmark of 16 memory-dependent manipulation tasks spanning temporal, spatial, object, and procedural memory. The model keeps the whole episode in context and outputs every end-effector waypoint and gripper command, with no RoboMME-specific training. On the 800 test episodes it succeeds in 92.1%, above the previously reported human score of 90.5%, which was obtained with an oracle skill inter...
  </details>

- **2026-10-12** — Xinzhe Chen, Liqi Huang, Sihua Ren et al. — [Phase-Conditioned Affordance Fields for SE(3)-Equivariant Visuomotor Policies](http://arxiv.org/abs/2610.17281v1)
  <details><summary>📄 Abstract</summary>
  SE(3)-equivariance provides a useful geometric inductive bias for visuomotor policies, encoding that actions covary with rigid transformations of the observation. However, existing SE(3)-equivariant visuomotor policies build this bias on a global equivariance assumption that treats the entire observation as governed by a single rigid transformation, which breaks down in real-world manipulation tasks where the task-relevant region changes across different objects. We address this by learning a ph...
  </details>

- **2026-10-12** — Yixiang Liu, Ruizhe Deng, Bibhas Chakraborty et al. — [When Repeated Measurements Hurt Tabular Foundation Models](http://arxiv.org/abs/2610.16801v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) achieve state-of-the-art performance on IID benchmarks, but how do they respond to repeated measurements at the same inputs? Across six TFMs, synthetic and semi-synthetic experiments show that additional measurements can improve predictions at measured inputs while degrading them elsewhere. Harm is most frequent at low noise, and irrelevant features amplify it in several models; real repeated-measurement datasets show similar patterns. Statistically, the IID rule...
  </details>

- **2026-10-12** — Ming Shin Cindy Sung, Duan Leijiahao, Haoxiang Wang et al. — [LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints](http://arxiv.org/abs/2610.16782v1)
  <details><summary>📄 Abstract</summary>
  Industrial manipulation in flexible manufacturing, e.g., high-mix, low-volume (HMLV) electronics assembly, requires robot policies to adapt to changing products and production conditions. Such settings impose industrial process constraints, including product variants, moving material flows, finite execution windows, and tight geometric tolerances. However, existing evaluation frameworks do not systematically capture these constraints when assessing generalist robot policies. To address this gap,...
  </details>

- **2026-10-12** — Yutong Zhi, Jie Zhang, Xiuqi Lu et al. — [TRAP: Tool-result Replay Attack for Probing Misbinding in LLM Agents](http://arxiv.org/abs/2610.16333v1)
  <details><summary>📄 Abstract</summary>
  As AI agents increasingly act through external tools, tool results are no longer simple outputs but execution artifacts that must remain correctly associated with the context that produced them. Yet as results persist across caches, recovery mechanisms, and shared runtime state, this association can break, causing a real and unmodified result to be consumed in an incompatible execution context and lead the agent to an unsafe action. We characterize this failure as tool-result misbinding. To syst...
  </details>

- **2026-10-12** — Will Sandholtz, Andrew Tai — [Continuity of stable marriage correspondences](http://arxiv.org/abs/2610.17460v1)
  <details><summary>📄 Abstract</summary>
  We study a continuum version of the stable marriage problem, in which each agent has a variable mass to be paired to the opposite side. An agent's mass is interpretable as the divisible time of a single atomistic agent, or as a mass of infinitesimal agents of a particular type. Our object of interest is the mapping between the vector of masses to the set of stable matches. As in the canonical stable marriage model, the set of stable matches can be multi-valued, so this mapping is a correspondenc...
  </details>

- **2026-10-12** — Ayse Sila Okcu, Weisheng Wang, Tongmeng Xie et al. — [The belief-action gap in language model agents](http://arxiv.org/abs/2610.17444v1)
  <details><summary>📄 Abstract</summary>
  Language model (LM) agents can fail for different reasons, requiring different explanations and interventions. We study how state beliefs, action values, and action preferences interact as LM agents reason and commit to decisions in text-rendered grid worlds. We estimate task-relevant beliefs using report-based and representation-based probes, and action values using inverse reinforcement learning. We find that task-relevant state and value information is often represented more reliably than it ...
  </details>

- **2026-10-12** — Alexander Miasnikov, Ruslan Kabirov, Gleb Molodtsov et al. — [Monarch-Muon: Structure-Aware Muon for Fast and Memory-Efficient Pretraining](http://arxiv.org/abs/2610.17429v1)
  <details><summary>📄 Abstract</summary>
  Training large language models is constrained by both wall-clock time and memory footprint, and recent matrix-aware optimizers sharpen this tradeoff: Muon can improve optimization but its dense polar update remains expensive. We propose Monarch-Muon, a structured matrix-aware optimizer for weights parameterized by Monarch factors. The resulting structure reduces weights, gradients, and optimizer state, and exposes small independent update subproblems in place of a single dense orthogonalization;...
  </details>

- **2026-10-12** — Saleh Assadi, Zachary T. White, Fay Salmon et al. — [Meso-scale modeling of cohesive cavitation in polymer networks](http://arxiv.org/abs/2610.17360v1)
  <details><summary>📄 Abstract</summary>
  Cavitation influences the failure of elastomers and soft adhesives, but connecting its microscopic initiation to subsequent cavity growth remains challenging. Here, we develop a discrete mesoscale framework that combines finitely extensible, breakable strands with local van der Waals interactions to examine how cohesion and network heterogeneity transform distributed dilation into localized damage. In the simulations, local cohesive instability produces a network-scale precursor whose subsequent...
  </details>

- **2026-10-12** — Akos Hajnal — [A Geometrical Approach to Constructing Neural Networks for Perfect Training-set Classification](http://arxiv.org/abs/2610.17312v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a method for constructing a neural network that achieves perfect classification of all samples in a given training set, without taking regularization into account. The network is constructed on-demand, with its layer sizes and neuron parameters determined through a geometrical analysis of the input data, in which separating hyperplanes are created and mapped to neurons with step activation functions. The proposed architecture consists of two hidden layers with distinct roles:...
  </details>

- **2026-10-12** — Raghu Venkat, Tricha Anjali — [Does a Governed Confidence Score Know When a Text-to-SQL Answer Is Right? An Exploratory Study on BIRD and a Pre-registered Confirmation on Spider](http://arxiv.org/abs/2610.17256v1)
  <details><summary>📄 Abstract</summary>
  Conversational analytics lets people ask questions of records spread across many systems and get answers in plain language; it is useful only if each answer can be trusted and explained. A production system of this kind attaches a confidence score to every answer it writes over a database and uses it to show the answer, show it with a warning, or withhold it. The score's weights, caps and thresholds were set by design. This paper audits that design. On the 1,534 questions of BIRD dev, answered b...
  </details>

- **2026-10-12** — Yinzhu Quan, Zefang Liu, Frederick Benaben et al. — [AutoMARS: Automatic and Scalable Multi-Agent Large Language Model Framework for Supply Chain Risk Assessment](http://arxiv.org/abs/2610.17206v1)
  <details><summary>📄 Abstract</summary>
  We propose AutoMARS (Automatic Multi-Agent Risk Assessment), an agentic framework for automatic and scalable comparative risk assessment in supply chain networks. The framework enables end-to-end execution of analytical workflows by automatically planning tasks, coordinating specialized agents, invoking external analytical tools, and synthesizing domain-specific results into integrated risk evaluations. AutoMARS further supports scalable risk comparison across multiple locations by parallelizing...
  </details>

- **2026-10-12** — Félix Lefebvre, David Holzmüller, Gioia Blayer et al. — [TILE: Bridging LLMs and Table Foundation Models for Tabular Learning with Strings](http://arxiv.org/abs/2610.17065v1)
  <details><summary>📄 Abstract</summary>
  Real-world tables are often heterogeneous, combining numerical features with free-form string columns. Table foundation models (TFMs) excel on numerical tables but require strings to be encoded numerically, while large language models (LLMs) hold semantic knowledge but are not designed for tabular predictions. Most existing bridges use LLMs as plug-in encoders for cell strings, yet how to extract representations effectively for tabular learning remains underexplored. We show that the interface b...
  </details>

- **2026-10-12** — Omar G. Younis, Joseph D. Viviano, Chirayu Anant Haryan et al. — [Mixture of GFlowNets](http://arxiv.org/abs/2610.17007v1)
  <details><summary>📄 Abstract</summary>
  Generative Flow Networks (GFlowNets) learn a policy that samples compositional objects in proportion to an unnormalized reward $R(x)$. This makes them useful wherever many diverse, high-reward candidates are needed and oracle queries are expensive. In practice, a single GFlowNet often fails to cover all modes of a complex distribution, and the obvious ways to scale compute saturate: larger batches and data-parallel gradient averaging draw every trajectory from one, possibly biased, policy, so ex...
  </details>

- **2026-10-12** — Natkamon Tovanich, Célestin Coquidé — [Tracing Money Flows in the Multi-Token Cryptocurrency Network](http://arxiv.org/abs/2610.16981v1)
  <details><summary>📄 Abstract</summary>
  Tracing money flows in cryptocurrency transaction networks is challenging because funds can move across accounts, transactions, and token layers. We propose a transaction-aware graph in which nodes represent account--asset states within transactions, while edges encode observed transfers, inferred asset transformations, and temporal inter-transaction sequences. Applied to Aave borrow--repay flows, we compare graph construction and edge-pruning strategies and extract shortest paths using a heuris...
  </details>

- **2026-10-12** — Roksana Goworek, Haim Dubossarsky — [Lexical Redefinition Reveals Context-Sensitive Instruction Following](http://arxiv.org/abs/2610.16952v1)
  <details><summary>📄 Abstract</summary>
  How do language models reconcile conflicting contextual evidence within a prompt? We study this question using lexical redefinition, where an explicit instruction specifies how a word should be interpreted and a subsequent sentence provides additional evidence through its usage. Across 870 word pairs, we find that lexical redefinitions are not applied as fixed rules. Instead, the behaviour depends systematically on the relationship between the explicit instruction and the intervening sentence: t...
  </details>

- **2026-10-12** — Yichen Huang, Nicholas Teh — [Online Fair Division with Upgrade Recourse](http://arxiv.org/abs/2610.16943v1)
  <details><summary>📄 Abstract</summary>
  We study the online fair division of indivisible goods. In the standard model, where assignments are irrevocable, no algorithm can guarantee any positive fraction of the maximin share (MMS). Reassigning earlier goods can restore fairness, but it may take value away from agents who already hold them. We ask how much fairness can be maintained if every reassignment must leave each affected agent at least as well off. We consider two forms of such upgrade recourse. Under item-level upgrades, each g...
  </details>

- **2026-10-12** — Giovanni Briglia, Marco Lippi, Stefano Mariani et al. — [Neural Bayesian Networks for Modular and Scalable Decision-Making Under Uncertainty](http://arxiv.org/abs/2610.16902v1)
  <details><summary>📄 Abstract</summary>
  Bayesian Networks (BNs) are established tools for letting agents reason under uncertainty in sequential decision-making. They split a joint distribution into local conditional mechanisms arranged on a directed acyclic graph, which makes them modular, interpretable, and ready to perform probabilistic inference. Their classical formulation, however, has limitations in both expressiveness and scale: each conditional is usually stored as a table or a linear-Gaussian form, and inference evaluates the...
  </details>

- **2026-10-12** — Tom Jacobs, Rebekka Burkholz — [From Parallel to Sequential: Small-Batch Noise Restores Simplicity Bias of Muon](http://arxiv.org/abs/2610.16868v1)
  <details><summary>📄 Abstract</summary>
  Simplicity bias, which can arise from sequential feature learning during training, has been proposed as a general explanation for the success of deep learning. An important driver of this phenomenon is saddle-to-saddle behavior, in which the gradient flow trajectory remains close to a sequence of saddle manifolds while learning one feature at a time. However, Muon, a state-of-the-art optimizer based on spectral descent, does not exhibit such dynamics in the full-batch setting and instead learns ...
  </details>

- **2026-10-12** — Yuxiang Zeng, Kun Xie, Yang Wang et al. — [DTA-GT: Direction- and Topology-Aware Graph Transformer for Neural Network Representation Learning](http://arxiv.org/abs/2610.16822v1)
  <details><summary>📄 Abstract</summary>
  Architecture attribute predictors reduce the cost of neural architecture search by estimating accuracy or latency from a small set of evaluated candidates. The key difficulty is that neural architectures are operation-labeled DAGs: edge direction defines computational flow, but existing predictors often treat direction as a local structural cue. We propose DTA-GT, a Direction- and Topology-Aware Graph Transformer based on encoder-wide directional consistency, which preserves directed computation...
  </details>

- **2026-10-12** — Gabriel Singer, Reda Arab, Maïssa Frikha et al. — [On the Calibration of Crowdsourcing Aggregators](http://arxiv.org/abs/2610.16815v1)
  <details><summary>📄 Abstract</summary>
  Calibration has been extensively studied for classifiers, but remains largely unexplored for crowdsourcing aggregation methods, which are increasingly used for making probabilistic decisions. To the best of our knowledge, we provide the first theoretical and empirical study of calibration in label aggregation. To our great surprise, we find that widely used aggregation methods can be severely miscalibrated, and in opposite directions: Majority Vote is underconfident while model-based aggregators...
  </details>

- **2026-10-12** — Yuxiao Hu, Qian Li, Ding Wang et al. — [DASS: A Solver-Adaptable Dynamic Auxiliary Search Strategy for Symbolic Regression](http://arxiv.org/abs/2610.16812v1)
  <details><summary>📄 Abstract</summary>
  Symbolic regression (SR) aims to discover interpretable mathematical expressions from data and plays a key role in scientific discovery. However, existing methods face a common bottleneck: the enormous search space and severe combinatorial explosion make it difficult to achieve a favorable trade-off between accuracy and algorithmic efficiency. We argue that, in addition to designing increasingly complex solver-specific SR strategies, an equally promising direction is to equip them with a shareab...
  </details>

- **2026-10-12** — Yi Wang, Zhenlong Yuan, Yuchan Guo et al. — [X-Ragent: Tool-Augmented Reinforcement Learning for Evidence-Grounded Chest X-Ray Reasoning](http://arxiv.org/abs/2610.16811v1)
  <details><summary>📄 Abstract</summary>
  Chest X-ray (CXR) interpretation often requires integrating visual findings with task-specific evidence rather than relying on direct visual recognition alone. While tool-augmented medical agents can supply such evidence via external modules, they often lack explicit mechanisms for learning when auxiliary evidence is needed and for preventing inapplicable quantitative evidence from entering diagnostic reasoning. To address this, we propose X-Ragent, a post-training framework for tool-augmented r...
  </details>

- **2026-10-12** — Yuchen Li, Zongqi Fan, Xintong Li et al. — [What Is the "Self" of a Large Language Model?](http://arxiv.org/abs/2610.16717v1)
  <details><summary>📄 Abstract</summary>
  What could the "self" of a large language model be, if it is neither a particular word nor a single privileged layer? We propose a relational account: a functional self is an actor-centered organization of information that distinguishes the model's recorded actions from externally supplied material while content and reasoning operations change. Its representational candidate is a family of layer-specific source-binding components, rather than one unchanged vector throughout the network. Prelimin...
  </details>

- **2026-10-12** — Guojun Zhu, Xinyou Chen, Kejian Zhang et al. — [AgentCue: Statistical Summaries for Guiding Decentralized Multi-Agent Self-Organization](http://arxiv.org/abs/2610.16621v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) combine multiple agents to solve complex tasks, and recent MAS scale to more than a thousand agents. At this scale, decentralized MAS remove the central orchestrator that assigns sub-tasks, and the agents, which we call workers, self-organize through their own choices of sub-tasks and collaborators on a shared board. As workers keep adding participation and collaboration records, however, the information explodes: workers spend more and more effort on reading the record...
  </details>

- **2026-10-12** — Eugenio Cainelli, Lorenzo Luccioli, Alessandro Iraci et al. — [AI Discovery in Combinatorics: From Problems to Solutions and Back to Bigger Problems](http://arxiv.org/abs/2610.16555v1)
  <details><summary>📄 Abstract</summary>
  We introduce $qt$Bench, a benchmark of 29 open problems in algebraic combinatorics. These problems ask for a simple combinatorial algorithm that explains given polynomial coefficients or identities. To help AI agents search for such algorithms, we provide a scaffold for playing with combinatorial objects, countering cheating attempts, and testing candidate solutions. To explore how far frontier AI systems can go on these problems, we collaborated with OpenAI, whose researchers obtained proposed ...
  </details>

- **2026-10-12** — Vance Faber, Jarek Liesen, Jörg Liesen et al. — [On the cyclic limiting behavior of the restarted Arnoldi algorithm for real symmetric matrices with restart length $s=2$](http://arxiv.org/abs/2610.16492v1)
  <details><summary>📄 Abstract</summary>
  We prove that the restarted Arnoldi algorithm for real symmetric matrices with restart length $s=2$ has a cyclic limiting behavior. In the terminology established in (arXiv:2209.14579), this is a proof of the ACI($s$) conjecture for $A=A^T\in \mathbb{R}^{n\times n}$ and $s=2$. As explained in (arXiv:2209.14579), this also proves the Forsythe conjecture (Numerische Mathematik, 11 (1968), pp. 57-76) about the limiting behavior of the conjugate gradient method and positive definite $A=A^T\in\mathbb...
  </details>

- **2026-10-11** — Adi Silberschein, Megan Wei, Tamar Rott Shaham — [Harmonic Representations in Symbolic Music Transformers are Localized and Controllable](http://arxiv.org/abs/2610.15957v1)
  <details><summary>📄 Abstract</summary>
  Transformer models trained on symbolic music have become remarkably capable. However, it is yet unclear how they represent music structure, and whether understanding their internal representations can be used to unlock methods for model control. We examine this through a case study of harmonic analysis: when a music transformer navigates a cadence, what does it internally "know" about its harmonic context, and can that knowledge be used to affect the generation? Using Aria, a LLaMA-based symboli...
  </details>

- **2026-10-11** — Angen Ye, junjie xie, Yujia Song et al. — [SurgiCLAW: An Interpretable Atomic-Skill Agent for Precision Robotic Micromanipulation](http://arxiv.org/abs/2610.15766v1)
  <details><summary>📄 Abstract</summary>
  Recent multimodal large language models (MLLMs) and vision--language--action models have provided robots with new capabilities for long-horizon task understanding and planning. In surgical robotics, however, end-to-end prediction of low-level actions remains limited by insufficient precision, opaque decisions, and scarce data. This paper presents SurgiCLAW, a hierarchical skill-based framework for precision surgical manipulation. SurgiCLAW confines an MLLM to intraoperative visual understanding,...
  </details>

- **2026-10-11** — Tianyu Jin, Liuyu Xiang, Chaowen Yang et al. — [FARL: A Fully Automated Pipeline of RL Interface and Solver Design](http://arxiv.org/abs/2610.15691v1)
  <details><summary>📄 Abstract</summary>
  Existing reinforcement learning (RL) largely focuses on optimizing learning algorithms within a pre-defined task formulation, while applying RL to new tasks still relies heavily on human expertise to design the learning pipeline: what an agent observes, how it is rewarded, which algorithm it uses, and how training is configured. Automating these choices is challenging because they are tightly coupled. We introduce FARL (Fully Automated Reinforcement Learning), a framework that automates RL desig...
  </details>

- **2026-10-09** — Jasin Cekinmez, Addison J. Wu, Ryo Mitsuhashi et al. — [OccludeBench: Can VLMs Find What's Missing?](http://arxiv.org/abs/2610.13790v1)
  <details><summary>📄 Abstract</summary>
  How well can vision-language models (VLMs) reason about what is missing from an image? We study this question with OccludeBench, a manually curated benchmark for recovering fully occluded objects from the visual evidence that remains. OccludeBench distinguishes direct cases, where the hidden object must be recovered from a specific physical cue such as a shadow or reflection, from inferential cases, where it can be inferred from broader scene context. Across five VLMs, accuracy averages 42.7% on...
  </details>

- **2026-10-09** — Finn Klatt, Luca Di Grazia, Johannes Schneider — [A-SAW: The Agentic Software Architecture Workflow](http://arxiv.org/abs/2610.13647v1)
  <details><summary>📄 Abstract</summary>
  AI assistance in software engineering focuses on implementation and verification, leaving the design phase, and in particular the maintenance of architecture documentation, comparatively underserved. Architecture as Code makes architectural artifacts versionable, diffable, and machine-readable, but it does not reduce the effort of keeping them updated, so design documentation still ends up as a fragmented, author-dependent, and only partially trusted record of why a system looks the way it does....
  </details>

- **2026-10-09** — Xiaomeng Ye, Krishna Jaganathan, Gyubeum Lim et al. — [Splat2Act: From Captured Scenes to Personalized VLA Manipulation](http://arxiv.org/abs/2610.13945v1)
  <details><summary>📄 Abstract</summary>
  A user who brings a generalist manipulation policy into their home or office wants it to pick up their objects from their shelves, counters, and tables. Yet even a strong generalist like $π_{0.5}$ achieves 0% pickup success in our captured deployment scenes without adaptation, and collecting real demonstrations in every user's environment is prohibitively expensive. We present Splat2Act, an automated real-to-sim-to-real pipeline that personalizes a pretrained vision-language-action (VLA) policy ...
  </details>

- **2026-10-09** — Xuanye Wu, Yue Shi, Yongcan Yang et al. — [AutoBio+: Benchmarking Dexterous Manipulation with Dynamic Experimental Phenomena in Realistic Laboratories](http://arxiv.org/abs/2610.13643v1)
  <details><summary>📄 Abstract</summary>
  Automating biological laboratories requires robots to perform dexterous tool interactions under realistic visual conditions while handling dynamic experimental phenomena, presenting significant challenges for robotic manipulation. To enable systematic evaluation under these conditions, we introduce AutoBio+, a simulation benchmark and framework for dexterous manipulation in realistic biological laboratory environments. AutoBio+ comprises 14 tasks across 4 robot embodiments, spanning functional t...
  </details>

- **2026-10-09** — Xudong Cai, Ruijie Zhu, Haoliang Shang et al. — [Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](http://arxiv.org/abs/2610.13947v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we study physically grounded articulated 3D asset generation---moving the goal from reproducing how objects look to capturing how they move and function. Inspired by the literature on procedural and agentic generation, we present Artisan, a system that extends the latest method Articraft by introducing a multi-agent pipeline with physical simulation feedback, enabling comprehensive attributes beyond geometry, appearance, and physically plausible articulation, such as collision-fre...
  </details>

- **2026-10-09** — Sovesh Mohapatra, Dani S Bassett — [Task Context Shapes Component Roles in Language Models](http://arxiv.org/abs/2610.13895v1)
  <details><summary>📄 Abstract</summary>
  Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention ...
  </details>

- **2026-10-09** — Tirthankar Chakraborty, Arnab Maity — [Information-Weighted Distributed Kalman Filter for Multi-Target Tracking over Switching Sensor Networks](http://arxiv.org/abs/2610.13893v1)
  <details><summary>📄 Abstract</summary>
  Target tracking over wide areas using a network of sensor agents is a challenging problem when agents have limited sensing coverage and communication topologies vary over time. Existing distributed filtering approaches commonly assume that each agent, or at least one of its neighbors, can directly observe the target, and further rely on fixed network topologies, global network parameters, or multiple consensus rounds per time step. These requirements limit their applicability in wide-area networ...
  </details>

- **2026-10-09** — Emilio Ferrara — [Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga](http://arxiv.org/abs/2610.13840v1)
  <details><summary>📄 Abstract</summary>
  Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parse...
  </details>

- **2026-10-09** — Sheng Zhao, Yuhao Zhu — [Specialists Learn Faster: Knowledge Organization in Pre-training Shapes Knowledge Update Efficiency](http://arxiv.org/abs/2610.13835v1)
  <details><summary>📄 Abstract</summary>
  An ideal (language) model must continually update its knowledge. Existing work largely focuses on making these updates efficient after training. We investigate how the organization of time-varying knowledge during pre-training shapes the efficiency of subsequent updates. Models trained on chronologically ordered knowledge specialize in the most recently encountered knowledge; we call them specialists. In contrast, models trained on the same knowledge in randomly shuffled order perform well acros...
  </details>

- **2026-10-09** — Bastian Schäfer, Dominika Matus, Lennart Purucker et al. — [SelectArena: A Modern Benchmark for Feature Selection on Real-world Tabular Data](http://arxiv.org/abs/2610.13644v1)
  <details><summary>📄 Abstract</summary>
  Selecting a subset of features (columns) from a tabular dataset is a ubiquitous challenge in real-world applications. Industry experts seek to minimize model training costs, climate scientists require an interpretable subset of factors to understand extreme weather events, and clinicians need to choose among diagnostic tests due to financial and time constraints. When looking at the scientific literature to determine which feature selection method to use, practitioners across domains face an unr...
  </details>

- **2026-10-08** — Jiawei Chi, Shangchen Miao, Zhiyuan Shi et al. — [AgentGarten: Code Worlds for Evolving Agents](http://arxiv.org/abs/2610.12374v1)
  <details><summary>📄 Abstract</summary>
  Interactive virtual worlds allow agents to learn through exploration and interaction. What agents can learn is bounded by the environments they practice in, which must be faithful, with consistent state, rules, and dynamics, and realistic, with observations that follow the real-world visual distributions. Achieving both across diverse worlds remains a bottleneck. We introduce AgentGarten, a framework that couples simulators and game engines with a shared neural renderer to build real-time intera...
  </details>

- **2026-10-08** — Kaisen Yang, Qingle Liu, Kejin Wang et al. — [Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition](http://arxiv.org/abs/2610.12341v1)
  <details><summary>📄 Abstract</summary>
  Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AA...
  </details>

- **2026-10-08** — Edward Chen, Yuntao Du — [Poster: A Preliminary Study of LLM Distillation Inference](http://arxiv.org/abs/2610.12137v1)
  <details><summary>📄 Abstract</summary>
  Unauthorized model distillation, in which a model is trained on the outputs of a proprietary large language model (LLM), is a growing threat to model providers. We study distillation inference: determining whether a suspect model was distilled from another model or trained independently. We formulate this problem as a hypothesis test and estimate the behavior expected under each hypothesis by training shadow models: distilled shadow models learn from the teacher's reasoning traces, whereas indep...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 676 |
| prompt-injection | 615 |
| memory-poisoning | 55 |
| tool-use-attack | 154 |
| backdoor | 513 |
| adversarial-attack | 633 |
| privacy-leakage | 4362 |
| steganography | 77 |
| misuse | 1169 |
| red-teaming | 140 |
| vulnerability | 3570 |
| defense | 3426 |
| alignment | 3216 |
| robustness | 3466 |
| watermark | 601 |
| unlearning | 113 |
| agent-safety | 64 |
| benchmark | 67 |
| survey | 398 |
| other | 9327 |

---

📚 **全部 32642 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-14 16:21:12*