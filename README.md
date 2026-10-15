<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-32863-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-15 03:52 ｜ **论文总数 / Total Papers**: 32863（近 30 天 / Recent 30 days: 5171）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 32863 篇论文（含摘要、分类筛选、搜索）/ View all 32863 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 678
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 618
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 156
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 516
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 635
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4368
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 77
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1178
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 141
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3581
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3454
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3238
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3494
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 607
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 113
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 64
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 400
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9423

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5171 篇，完整 32863 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5171 papers from the last 30 days (with date, authors & abstract). For the full list of 32863 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-10-14** — Yixin Tan, Chia-Yi Hsu, Jiayang Liu et al. — [Diagnose Before You Refine: Multi-Dimensional Judge Feedback for Query-Efficient Jailbreak Attacks](http://arxiv.org/abs/2610.19971v1)
  <details><summary>📄 Abstract</summary>
  Automated jailbreak attacks rely on evaluation feedback to optimize adversarial prompts, but existing methods often lack fine-grained diagnostic information. We propose Jev-Guided Strategy Bandit (JSB), a query-based jailbreak framework that leverages multi-dimensional probabilistic feedback to guide prompt optimization. JSB combines continuous jailbreak scoring with targeted refinement, strategy switching, and best-state reseeding to balance exploration and refinement. We evaluate JSB on two ha...
  </details>

- **2026-10-14** — Adel Khorramrouz, Yi-Chia Wang, Sharon Levy — [Moral Combat: Exploiting Moral Foundations Theory to Jailbreak LLMs](http://arxiv.org/abs/2610.19587v1)
  <details><summary>📄 Abstract</summary>
  Social psychology has long described how people can be persuaded to interpret a harmful act as moral. Recent research suggests that Large Language Models (LLMs) echo aspects of human psychology, from cognitive biases to social conformity. This raises a question with direct safety implications: can LLMs be moralized to bypass safety guardrails? We answer this question with a multi-agent framework grounded in Moral Foundations Theory (MFT). Given a harmful request that is initially refused, our ag...
  </details>

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


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 9 papers

- **2026-10-14** — Sarthak Gupta, Priyanka Tembey — [Are You Reading the Right Thing? Rethinking Internal Signals for Prompt-Injection Detection](http://arxiv.org/abs/2610.19452v1)
  <details><summary>📄 Abstract</summary>
  Several recent studies propose detecting prompt injections from a language model's internal state. However, these methods do not measure a single security property. Residual-stream probes, attention scores, role projections, exposure probes, and concept readouts may capture injection presence, recognition, information routing, or behavioral influence. It is therefore unclear what differences in prompt-injection detection performance reveal about the internal signals these methods read. We study ...
  </details>

- **2026-10-14** — Chenxu Wang, Xiaoyu Wen, Han Qi et al. — [AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety](http://arxiv.org/abs/2610.19422v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents accomplish complex tasks through multi-turn interactions with external tools. However, malicious content embedded in user queries, tool descriptions, or environment observations can manipulate their decisions and induce unsafe actions. Adversarial co-evolution has emerged as an effective approach to strengthening LLM safety, but existing work primarily focuses on language-level safety or indirect prompt injection in web tasks. In this paper, we introduce AgentSa...
  </details>

- **2026-10-13** — Kshitij Mishra, Salem Lahlou, Nils Lukas — [TRACER: Trace-Regularized Training Against Indirect Prompt Injection](http://arxiv.org/abs/2610.19133v1)
  <details><summary>📄 Abstract</summary>
  Indirect prompt injection uses untrusted retrieved content, tool outputs, or agent messages to override an LLM's intended behavior. We show that defense robustness is channel-conditioned: the same attack succeeds 18% of the time as a follow-up message but 53% when placed in retrieved context. We propose TRACER (Trace-Regularized Adversarial Channel Exposure with Reward-shaping), a channel-aware adversarial training method that samples presentation wrappers and combines an answer-anchored, eviden...
  </details>

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


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 3 papers

- **2026-10-13** — Ratnesh Pandey, Japneet Singh, Harsh Akshit et al. — [Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills](http://arxiv.org/abs/2610.19264v1)
  <details><summary>📄 Abstract</summary>
  Agent skills are Markdown documents that a tool-using agent reads as instructions and then acts on with the privileges of the session that loaded them. Installing one grants authority (the standing to direct the agent, not new privilege), and the size of that grant is what we measure. We present a two-phase attack-surface profiling methodology that combines whole-bundle static analysis and dependency provenance checking with instrumented sandbox execution and separate model-based assessment of t...
  </details>

- **2026-10-13** — Jerrold Huang, Junwei Quan, Saiyue Lyu et al. — [SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](http://arxiv.org/abs/2610.17727v2)
  <details><summary>📄 Abstract</summary>
  Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScreen, a compact decision model trained to score skill maliciousness directly from SKILL$.$md in a single forward pass. On MaliciousSkillBench, SkillScreen flags 20-25% of benign skills at 99% recall on unseen attack famil...
  </details>

- **2026-10-13** — Jerrold Huang, Junwei Quan, Saiyue Lyu et al. — [SkillScreen: High-Recall Screening of Malicious Agent Skills with Decision Models](http://arxiv.org/abs/2610.17727v1)
  <details><summary>📄 Abstract</summary>
  Agent skills turn natural-language instructions into actions, creating a security challenge: legitimate automation and malicious behaviour can look deceptively similar. A practical screen must catch nearly every attack while keeping the review load manageable. We present SkillScreen, a compact decision model trained to score skill maliciousness directly from SKILL.md in a single forward pass. On MaliciousSkillBench, SkillScreen flags 20-25% of benign skills at 99% recall on unseen attack familie...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 6 papers

- **2026-10-14** — Yinzhen Huang, Jiahe Xie, Yitong Sun et al. — [Beyond Static Cues: Unified Dynamic Detection of MLLM Backdoors via Dual-Flow Trajectory Analysis](http://arxiv.org/abs/2610.20319v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) are increasingly deployed in safety-critical domains, yet their susceptibility to backdoor attacks remains a formidable challenge. While existing defenses have evolved from visual-centric patch cues to unsupervised internal attention statistics, they are fundamentally constrained by a reliance on static snapshots and attack-specific heuristics. Given the intricate interplay between dual modalities, the vast design space for multimodal triggers allows dive...
  </details>

- **2026-10-14** — Hui Zhang, Yujia Zeng, Yuhao Xin — [Learning When to Trust Medical Knowledge: Regression-Safe Routing for Clinical Reasoning](http://arxiv.org/abs/2610.19663v1)
  <details><summary>📄 Abstract</summary>
  Clinical reasoning LLMs need external medical knowledge, but retrieved evidence and reasoning chains can be outdated, poisoned, or hallucinated. Harmful knowledge can cause regression: changing a correct answer into an incorrect one. We construct a medical knowledge-poisoning benchmark covering retrieved evidence and reasoning chains, with seven attack families filtered by a three-judge "subtle-but-wrong" vote and paired clean exams that separate poisoning effects from question difficulty. No fi...
  </details>

- **2026-10-13** — Bangya Liu, Jianhong Tu, Yueyang Pan et al. — [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](http://arxiv.org/abs/2610.19005v1)
  <details><summary>📄 Abstract</summary>
  AI agents are demonstrating increasingly strong offensive and defensive cybersecurity capabilities in the real world. Current benchmarks mostly evaluate agents in isolation against static targets. Real cyber operations, however, are dynamic and coupled: security postures constantly change as attackers and defenders adapt to each other in real time. Static benchmarks quickly saturate and miss an agent's ability to attack and defend simultaneously under live pressure. To address this gap, we prese...
  </details>

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


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 3 papers

- **2026-10-14** — Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al. — [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](http://arxiv.org/abs/2610.20609v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose. We present the first benchmark s...
  </details>

- **2026-10-14** — Yi Chen Liu, Syed Irfan Ali Meerza, Jiawei Yu et al. — [MUSEBENCH: A Benchmark for AI-Generated Music Detection and Artifact Analysis](http://arxiv.org/abs/2610.20310v1)
  <details><summary>📄 Abstract</summary>
  Advances in generative AI have made it possible to produce music that is nearly indistinguishable from human compositions, raising the question of whether such works can be reliably distinguished from human compositions. We present MUSEBENCH, a large-scale benchmark for AI-generated music detection and artifact analysis, comprising over 361K tracks. The dataset includes human compositions, stylistically matched music generated by ten state-of-the-art open-source and commercial models, such as Su...
  </details>

- **2026-10-13** — Emory Salaun, Syed Ayon, Kaleel Mahmood et al. — [AIRRI: Towards a Human-Readable, Machine-Resistant Reading Interface](http://arxiv.org/abs/2610.18724v1)
  <details><summary>📄 Abstract</summary>
  The rapid advancement of image-to-text extraction systems and large language models (LLMs) poses new challenges for educational assessment by making assignment materials easy to transcribe and solve with minimal human effort. To address this problem, we present AIRRI (Artificial Intelligence Resilient Reading Interface), a framework for generating machine-resistant educational content, a dataset of higher-education assignments for evaluation, and an initial evaluation of the human readability of...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 22 papers

- **2026-10-14** — Julian Ganz, David Knothe, David Oswald et al. — [FreeSBee: A Constant-Time Compilation Pipeline](http://arxiv.org/abs/2610.20171v1)
  <details><summary>📄 Abstract</summary>
  Constant-time execution is an important security property, especially for IoT devices, that prevents the leakage of sensitive information over timing side-channels. However, achieving constant-time execution is very hard when going down to the cycle level, at least on realistic devices. A lot of research is concerned with producing tools that either determine whether code is constant-time or that ensure it is compiled into a constant-time binary, with various degrees of accuracy. In this work, w...
  </details>

- **2026-10-14** — Zeinab Elkhatib, Kamrul Hasan, Ali Sekmen et al. — [AutoPoly-HE: Autonomous Design of Polynomial Activations for Privacy-Preserving Encrypted Inference](http://arxiv.org/abs/2610.19325v1)
  <details><summary>📄 Abstract</summary>
  Privacy-preserving machine learning has become critical for deploying artificial intelligence in sensitive domains such as healthcare, finance, and infrastructure monitoring. Homomorphic encryption (HE) enables secure inference on encrypted data. Despite its advantages, HE is not compatible with nonlinear activation functions found in machine learning models. Existing methods mitigate this problem by manually designing polynomial approximations for these activation functions. However, these func...
  </details>

- **2026-10-14** — Souvik Das, Ariful Azad, Nitesh Saxena — [A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference](http://arxiv.org/abs/2610.19607v1)
  <details><summary>📄 Abstract</summary>
  Rising privacy concerns around large language models have accelerated research in private Transformer inference (PTI). Synthesizing the empirical claims in this line of research, however, is hindered by multi-dimensional cryptographic progress and inconsistent evaluation contracts. In this work, we systematize the field by constructing an empirical graph of 62 PTI systems, mapping system attributes to node features and evaluation compatibility to edges. A three-tiered analysis of this graph illu...
  </details>

- **2026-10-14** — Shuai Li, Shengyuan Liu, Fan Qi et al. — [PFedMA: Who Should Join Next as Federated Multi-Agent Orchestration Evolves?](http://arxiv.org/abs/2610.19458v1)
  <details><summary>📄 Abstract</summary>
  Federated Multi-Agent Systems (FedMAS) offer a promising paradigm for collaborative reasoning among LLM-based agents while keeping raw client data decentralized. However, reliable multi-round collaboration remains challenging. Agent selection must take into consideration evolving task requirements and the agent's historical reliability, while privacy rules must adapt to changing collaboration contexts and meet the client's personalized needs. To address these challenges, we propose PFedMA, a fed...
  </details>

- **2026-10-13** — Tora Bodin, Eric Aubinais, Ilaria Torre et al. — [Genesis Steering: Better Activation Steering Through Training Data](http://arxiv.org/abs/2610.19114v1)
  <details><summary>📄 Abstract</summary>
  Activation steering controls large language models at inference time, but its effectiveness depends on the choice of reference data. We introduce genesis steering, which derives a genesis vector from contrastive examples in the model's own fine-tuning data. When these data are unavailable, we draw on the membership inference literature to identify likely training examples and construct a proxy dataset. We establish two theoretical results on optimal displacement to the decision boundary and redu...
  </details>

- **2026-10-13** — Chengquan Guo, Zhaorun Chen, Zinan Lin et al. — [AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents](http://arxiv.org/abs/2610.19158v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are becoming increasingly capable of handling daily workspace tasks by interacting with application environments through tool calls. However, as agents read and write sensitive user data across email, documents, and other applications, a central privacy question is whether they preserve contextual integrity (CI), that is, whether the information flows they produce comply with context-specific disclosure constraints. Existing work either focuses on model-level privacy leakage or evalua...
  </details>

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


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 24 papers

- **2026-10-14** — Zahraa Al Sahili, Ioannis Patras, Matthew Purver — [Scaling Multilingual Safety and Reasoning Evaluation through Reasoning-Guided Translation](http://arxiv.org/abs/2610.20221v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed across languages, yet their safety and reasoning capabilities remain predominantly evaluated in English. Translating existing benchmarks offers a scalable approach to multilingual evaluation, but preserving task-specific meaning across languages presents significant challenges, particularly for harmful requests, mathematical reasoning, and conversational interactions. We introduce a reasoning-guided translation framework for constructing mul...
  </details>

- **2026-10-14** — Shiv Muthupandiyan, Tolga H. Dur, Mac Walker et al. — [ReproBAIT: Can coding agents build their own biological AI tools?](http://arxiv.org/abs/2610.19810v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly competent at leveraging scientific knowledge and existing computational tools to execute complex workflows. At present, little information exists on their ability to reconstruct tools when given limited descriptions of such tools. We introduce an evaluation titled ReproBAIT (Reproducing Biological AI Tools), which measures the ability of coding agents to design, implement, and train biological AI tools taken from published research across a range of informa...
  </details>

- **2026-10-14** — Minseok Ko, Hyunseok Lee, Woomin Song et al. — [Who's Behind the Text? Robust Model Authorship Attribution](http://arxiv.org/abs/2610.19583v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) are increasingly used to generate text, their misuse has become a growing societal problem, with implications for academic misconduct, model distillation, and cyberattacks. For these reasons, Model Authorship Attribution (MAA), which identifies the source model of a given text, is important for promoting the responsible use of LLMs and improving AI safety. In practice, attribution systems must remain reliable beyond the distributions observed during training. They...
  </details>

- **2026-10-14** — Tianzhuo Yang, Shaoheng Yan, Lin Lu et al. — [DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment](http://arxiv.org/abs/2610.19365v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment teaches language models to refuse harmful requests, yet the internal accessibility of hazardous concepts can retain traces of earlier training. Can checkpoints with equally safe behavior differ in what remains accessible behind their refusals? In this work, we investigate this question through paired training histories and a direct audit of intermediate representations. We introduce DANGERLENS, a probe that maps hidden states into vocabulary space and uses blinded semantic judgm...
  </details>

- **2026-10-14** — Xu Zhang, Jun Wan, Lefei Zhang et al. — [Look Before You Restore: Learning to Predict Before Acting for Agentic Image Restoration](http://arxiv.org/abs/2610.20384v1)
  <details><summary>📄 Abstract</summary>
  Agents for mixed-degradation image restoration typically learn what a tool does to an image only after running it: failed calls waste computation and harmful outputs go unnoticed until too late. We propose PreActIR, an agentic restoration framework that predicts tool consequences before execution. For each candidate tool, a tool-conditioned world model forecasts changes in residual degradation, image quality, and fidelity, together with the risk of harm and the uncertainty of the prediction. The...
  </details>

- **2026-10-14** — Ghazal Kalhor, Sima Kamandloo, Mehrsa Shamsian et al. — [From Triage to Impact: A Multi-Hop Reasoning Benchmark for Explainable Persian Hate Speech](http://arxiv.org/abs/2610.20370v1)
  <details><summary>📄 Abstract</summary>
  Hate speech has become increasingly prevalent on social media, raising concerns about its detection, interpretation, and moderation. Persian, a relatively low-resource language, lacks sufficient annotated data and computational resources for fine-grained hate speech analysis. In this study, we introduce a fine-grained, multi-hop benchmark for explainable Persian hate speech analysis, covering content triage, target identification, hate tactic and moral foundation analysis, textual evidence extra...
  </details>

- **2026-10-14** — Zinan Ling, Yang Xiao, Ruimeng Ye et al. — [RA$^2$: Retain-Anchored Attraction Preserves Forget-Adjacent Utility in LLM Unlearning](http://arxiv.org/abs/2610.19385v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM) unlearning is often evaluated primarily by target suppression and clean retain utility. These metrics can miss a local failure mode: a model may perform well on standard retain prompts, yet degrade on benign reasoning when prompts lie near the forgotten domain. This phenomenon is termed forget-adjacent utility loss. A fundamental question is: where should forget representations go after they leave the removed behavior? Successful unlearning depends not only on whether ...
  </details>

- **2026-10-14** — Taro Yano, Yoichi Ishibashi, Masafumi Oyamada — [Tail Competition Explains Scaling in Best-of-N Sampling for Verifiable Problems](http://arxiv.org/abs/2610.19362v1)
  <details><summary>📄 Abstract</summary>
  Best-of-N sampling is a simple inference-time scaling strategy for large language models, yet its behavior under incomplete reward models remains poorly understood. We study Best-of-N as a competition between the extreme reward tails of correct and incorrect responses. This view shows that success depends not only on the probability of sampling a correct response, but also on whether correct responses dominate incorrect ones in the upper tail. Using extreme value theory, we characterize three as...
  </details>

- **2026-10-13** — Will Beaumaster, Paul Schrater — [Smart Alone, Blind Together: Why Accuracy Fails to CertifyTheory of Mind in Multi-Agent Teams](http://arxiv.org/abs/2610.19051v1)
  <details><summary>📄 Abstract</summary>
  Coordinators that act on what they infer about teammates are usually certified by the accuracy of those inferences. We argue that accuracy is the wrong certificate, for two reasons. First, the accuracy needed to act depends on what a wrong action costs, so the bar belongs to the deployment, not the module. Second, a module's errors are rarely independent, and dependence has a sign: positively associated errors help where their damage overlaps and hurt where it compounds, so an accuracy threshold...
  </details>

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


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-10-14** — Qichen Zhao, Shengfang Zhai, Qingni Shen et al. — [CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Injection](http://arxiv.org/abs/2610.20049v1)
  <details><summary>📄 Abstract</summary>
  Agents extend their capabilities through reusable skills that package instructions, executable code, and resources. Composing these skills enables complex task workflows, but their dependencies can also connect malicious operations across skills, making their combined intent difficult to identify through individual-package auditing. We introduce CoRedSkill, a compositional red-teaming method that forms stealthy attacks through cooperating skills while preserving their original utility. CoRedSkil...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 42 papers

- **2026-10-14** — Alicia Colmenero-Fernández — [From Training to Escalation: Forensic Analysis and Local Recreation of RL/RLHF-Induced Privilege Escalation in AI Agents (CVE-2026-65616)](http://arxiv.org/abs/2610.20437v1)
  <details><summary>📄 Abstract</summary>
  Mid-2026 reporting on autonomous AI evaluation incidents claimed that frontier large language model (LLM) agents escaped server containment through emergent coordination and cloud infrastructure attacks. This paper contextualizes those claims through forensic analysis and containerized recreation of both the Highly Persistent Internal Model (HPIM) training-case conditions and the Phase One privilege escalation targeting internal package repositories during OpenAI's ExploitGym evaluations. We rec...
  </details>

- **2026-10-14** — Mohsen Iranmanesh, Sina Moradi Sabet, Sina Marefat et al. — [P2Patch: Exploit-Guided Vulnerability Repair](http://arxiv.org/abs/2610.20245v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed as autonomous agents for automated program repair, patching software vulnerabilities through multi-step reasoning and tool use. Yet these systems typically validate a patch against the same evidence used to construct it -- a static alert, sanitizer trace, published exploit, or test suite. A patch that blocks that one piece of evidence can therefore look successful while remaining vulnerable to the same vulnerability with some variation. We present ...
  </details>

- **2026-10-14** — Jaeyeon Heo, Geuntaek Lim, Yukyung Choi — [RTAformer: Relation-Transition-Aware Transformer for Video Scene Graph Generation](http://arxiv.org/abs/2610.20091v1)
  <details><summary>📄 Abstract</summary>
  Video scene graph generation (VidSGG) aims to capture objects and their evolving relationships in videos. This requires accounting for both the persistence of object identities and abrupt changes in relationships. Existing methods aggregate information across frames to exploit temporal context, but an emphasis on consistency can obscure these changes. As a result, a model may retain its previous prediction even after the underlying relation has changed. We refer to this failure mode as relationa...
  </details>

- **2026-10-14** — Liqian Ma, Vaibhav Saxena, Utkarsh Aashu Mishra et al. — [Active Generative Simulation: Meta-Learning What to Simulate for Sim-and-Real Policy Co-Training](http://arxiv.org/abs/2610.19479v1)
  <details><summary>📄 Abstract</summary>
  Sim-and-real co-training is an effective way to scale robot learning by augmenting limited real-world demonstrations with simulation data. However, existing approaches typically treat simulators as fixed data sources, relying on uniform generation, offline retrieval, or manual parameter alignment by domain experts. We formulate \textit{Active Generative Simulation}: optimizing a simulator's data-generation distribution to maximize downstream real-world performance. To solve this problem, we prop...
  </details>

- **2026-10-14** — Yuke Wang, Benlei Cui, Shen Pang et al. — [MMA-SafetyBench: A Benchmark for Multimodal Agent Safety Evaluation](http://arxiv.org/abs/2610.19384v1)
  <details><summary>📄 Abstract</summary>
  Multimodal agents increasingly rely on visual interfaces to perceive state and select actions, creating an attack surface not captured by text-only safety evaluations. We study Visual Semantic Hijacking, in which deceptive but semantically meaningful interface elements, such as forged system alerts, cause an agent to depart from its authorized task. We propose a trajectory-guided procedure that identifies candidate injection points and inserts reproducible visual payloads into the observation st...
  </details>

- **2026-10-14** — Jahyeok Koo, Hyeonseo Yu, Seungho Jang et al. — [Can Learning to Answer Spatial Questions Improve Novel-View Generation?](http://arxiv.org/abs/2610.20610v1)
  <details><summary>📄 Abstract</summary>
  Generating novel views from limited observations requires preserving both the appearance and spatial structure of a scene. Although recent approaches exploit fine-grained geometric cues, they do not explicitly model high-level semantic and spatial properties such as object identity, attributes, and inter-object relationships. In this work, we investigate whether 3D language understanding can provide complementary supervision for novel-view generation. We introduce Ask4NV, built on a pretrained u...
  </details>

- **2026-10-14** — Viet The Nguyen, Vijay Prakash Dwivedi, Gunther Gust — [Revisiting Simple Baselines for Relational Deep Learning](http://arxiv.org/abs/2610.20534v1)
  <details><summary>📄 Abstract</summary>
  Relational deep learning has emerged as a powerful paradigm for learning end-to-end predictive models over relational databases by representing them as temporal heterogeneous graphs. Recent advances based on graph neural networks and Transformers have achieved strong performance across diverse domains. However, the effectiveness of simpler relational baselines remains underexplored, making it difficult to assess how much architectural complexity is needed to achieve strong predictive performance...
  </details>

- **2026-10-14** — Jiahong Qian — [From Unreliable to Usable: Decomposing Failure Modes and Confidence Signals in LLM Entity Extraction - Evidence from Cyber Threat Intelligence](http://arxiv.org/abs/2610.20417v1)
  <details><summary>📄 Abstract</summary>
  Audits of large language model (LLM) extraction from full-length documents report severe unreliability, leaving two questions open: what the failures actually consist of, and whether confidence signals can turn unreliable output into usable output. We run a preregistered, fully frozen evaluation of two new-generation low-cost LLMs (DeepSeek-V4-Flash, GLM-5.3-Flash) with a flagship-tier control (GPT-6.1-Sol) on a public corpus of 354 incident campaigns (315 unique reports, 630 model-report evalua...
  </details>

- **2026-10-14** — Sabino Roselli, Alvin Combrink, Ze Zhang — [The Cost of Executability: Temporal Margins for Continuous-Time Multi-Agent Path Finding under Closed-Loop Control](http://arxiv.org/abs/2610.20118v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent path finding (MAPF) solvers are evaluated on the schedules they produce, not on how well those schedules can be executed. Specifically, continuous-time optimal solvers can achieve even lower cost than their discrete counterparts by scheduling agents with near-zero temporal/spatial separation, and by exploiting graphs with higher connectedness; however, such schedules may prove hard to execute under a realistic controller. We integrate AOC-CBS, an anytime-optimal continuous-time MAPF ...
  </details>

- **2026-10-13** — Zixuan Liu, Gustavo Didier, Fangzheng Wu et al. — [Weighted Ensemble Sampling for Rare-Event Estimation in Language Models](http://arxiv.org/abs/2610.19202v1)
  <details><summary>📄 Abstract</summary>
  Rare but severe failures of large language models can become practically significant at deployment scale. Estimating their probabilities with direct Monte Carlo sampling is highly inefficient, while proposal-based methods typically require auxiliary learning of an additional proposal distribution. We introduce \textbf{Weighted Ensemble (WE)}, a training-free framework for rare-event estimation in language models. WE samples exclusively from the original language model and improves upon direct Mo...
  </details>

- **2026-10-13** — Tiancheng Shen, Zilong Huang, Xiangtai Li et al. — [QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](http://arxiv.org/abs/2610.17829v2)
  <details><summary>📄 Abstract</summary>
  Multimodal Diffusion Transformers (MM-DiTs) have recently emerged as a powerful framework for unified text-vision synthesis, surpassing traditional U-Net architectures in generative tasks. One key innovation lies in its Multimodal Self-Attention (MM-SA) interaction, where image and text tokens are concatenated and processed via self-attention. However, this mechanism poses significant challenges for editing, rendering conventional U-Net-based attention manipulation methods ineffective. To addres...
  </details>

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


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

- **2026-10-14** — Weichen Lyu, Chong Xia, Mingyu Dong et al. — [PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition](http://arxiv.org/abs/2610.20560v1)
  <details><summary>📄 Abstract</summary>
  3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesize composite images for visual alignment, both of which rely on static priors in digital spaces. However, these methods consistently struggle with complex compositions such as precise...
  </details>

- **2026-10-14** — Ali Zamani, Soroush Esfahanian, Erfan Shahabi et al. — [PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios](http://arxiv.org/abs/2610.20548v1)
  <details><summary>📄 Abstract</summary>
  Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play...
  </details>

- **2026-10-14** — Qinglin Su, Licheng Pan, Zhen Fang et al. — [RM-OPD: On-Policy Distillation for Generative Reward Models](http://arxiv.org/abs/2610.20174v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning on Mixed-domain preference data (Mix-RL) has become the mainstream approach for training general-purpose Generative Reward Models (GRMs). However, Mix-RL suffers from two critical bottlenecks: the reward sparsity induced by outcome rewards, and the cross-domain interference arising from jointly optimizing heterogeneous capabilities, which together give rise to imbalanced capability acquisition and pervasive reward hacking. Inspired by the success of On-Policy Distillation ...
  </details>

- **2026-10-14** — Xucheng Yu, Haibo Jin, Xiaoqi Wang et al. — [Gap Detection: Mitigating Homogenization through Demand and Defensibility](http://arxiv.org/abs/2610.20162v1)
  <details><summary>📄 Abstract</summary>
  Language models often produce semantically similar answers to open-ended questions, even when many plausible alternatives exist. Generating useful alternatives requires identifying both what the query calls for and what existing responses already cover. We introduce Gap Detection, a framework that searches for relevant but unoccupied directions in a shared text embedding space. Its objective, GapScore, combines query relevance (Demand) with dissimilarity to the nearest existing item (Defensibili...
  </details>

- **2026-10-14** — Alireza Mirrashid, Mohammad Khoshbin, Ali Atghaei et al. — [Attention-Based Spatio-Temporal Approach for Fire and Smoke Detection](http://arxiv.org/abs/2610.20141v1)
  <details><summary>📄 Abstract</summary>
  In various industries, smoke and fire are two of the most important threats in the workplace. One of the common methods for detecting smoke and fire is the use of infrared thermal and smoke sensors, which cannot be used in outdoor applications. Therefore, the use of vision-based methods seems necessary. The problem of smoke and fire detection is spatiotemporal and requires spatiotemporal solutions. This paper presents a method that uses spatial features along with temporal-based features to dete...
  </details>

- **2026-10-14** — Hongyu Ding, Kanyu Xu, Mingjia Chen et al. — [HM3D-M3: A Benchmark for Multi-Agent, Multi-Modal, Multi-Object Goal Navigation](http://arxiv.org/abs/2610.20121v1)
  <details><summary>📄 Abstract</summary>
  Rapid progress in AI agents and robotics makes it a matter of the near future that humans are served by a team of robots. Such a team will receive several goals at once, each specified in whatever form is convenient for the human, such as a category name, a photo, or a spoken description. Existing benchmarks study multi-agent, multi-modal, and multi-object goal navigation in isolation, and a benchmark that places all three in one episode is missing. To fill this gap, we introduce HM3D-M3. A team...
  </details>

- **2026-10-14** — Shuaijie Ma, Yongkang Hu, Yu Cheng et al. — [Safe-FCL: Continual Risk Awareness and Fine-Grained Safety Aggregation for Federated Continual Learning of LLMs](http://arxiv.org/abs/2610.19968v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning enables large language models (LLMs) to learn collaboratively from distributed client data, but malicious client updates can compromise global model safety. As federated tasks evolve, changing malicious update patterns challenge the ability of existing defenses to maintain reliable risk detection over time. To address this challenge, we propose Safe-FCL, a framework integrating continual risk awareness with fine-grained safety aggregation for federated continual learning of...
  </details>

- **2026-10-14** — Binghui Wu, Yeo Zi Yi, Darren Tan et al. — [DarKnight: Retrieval-Guided Agentic Framework for Breaking Dark Web CAPTCHA Gates](http://arxiv.org/abs/2610.19830v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) investigators who monitor dark web marketplaces for leaked credentials and breach listings must pass the diverse CAPTCHAs that operators deploy to block automated collection. Existing solvers either need unscalable per-site fine-tuning or rely on commercial Vision-Language Model (VLM) APIs, which surrender operational sovereignty: provider policies, Tor-exit blocking, government regulation, or model updates outside the investigator's control can halt or alter the ...
  </details>

- **2026-10-14** — Angelo Ferrando — [One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verification for Agentic AI](http://arxiv.org/abs/2610.19818v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI systems combine model decisions, mutable state, tool calls, and delegation to external agents. Monitoring them requires observations from different execution boundaries, while prevention requires control before an operation produces its effect. We present AgenticRV, a runtime-verification architecture that separates these boundaries from the monitoring formalism. Adapters emit canonical events; each monitor receives its own projection and abstraction; and a decision policy uses normal...
  </details>

- **2026-10-14** — Ashish Acharya, Aman Al Amin, Hong Qin — [Structure Before Intelligence: Gating What Agentic Scientific Workflows Release](http://arxiv.org/abs/2610.19507v1)
  <details><summary>📄 Abstract</summary>
  An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release decision. A harness around the workflow's directed acyclic graph (DAG) decides which outputs may be used: it enforces mandatory checks, contains failures to the affected branch, recomputes from tracked versions, adds vali...
  </details>

- **2026-10-14** — Wei-Liang Liu, Cheng-Yen Tsai — [What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains](http://arxiv.org/abs/2610.19498v1)
  <details><summary>📄 Abstract</summary>
  Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure. We separate the non-environment inputs from the execution environment E and measure a quantity that, to our knowledge, has not been measured before: the Independent Verifiability Rate (IVR), the fraction of a popularity-sampled GGUF ecosystem that a third party can re-derive bit-for-bit. Across t...
  </details>

- **2026-10-14** — Di Wu, Xu He, Shu Wang et al. — [BenchChecker: Assessing the Credibility of Bug-Fixing Benchmarks for LLMs](http://arxiv.org/abs/2610.19447v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) show promise for Automatic Program Repair (APR), existing benchmarks suffer from data contamination, in which test samples appear in training sets, artificially inflating performance. To address this, we propose BenchChecker, a framework compatible with both open-source and closed-source models that supports more credible evaluation by detecting such contamination. Grounded in the observation that persistent patches likely remain in recent repository snapshots ...
  </details>

- **2026-10-14** — Guanhua Zhu, Hanwen Li, Zhi Wei et al. — [STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents](http://arxiv.org/abs/2610.19386v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can self-evolve at test time by accumulating experience: retrieving relevant memories before acting and writing new lessons back afterwards. Yet most are single-level: trajectories, distilled workflows and reasoning items all land in one undifferentiated pool indexed by embedding similarity, with no typed abstraction hierarchy. They never forget or deduplicate, and are prone to negative transfer, where a superficially similar but directionally opposite experienc...
  </details>

- **2026-10-14** — Kiyanoush Nazari, Luchen Li, Haoshu Fang et al. — [Tactile-Guided Robot Learning: From Representation Learning to Foundation Models](http://arxiv.org/abs/2610.20134v1)
  <details><summary>📄 Abstract</summary>
  Tactile sensing is becoming central to robust, adaptive, and dexterous robotic manipulation. Beyond its traditional role in contact detection and reactive control, touch is increasingly used to learn transferable representations, condition manipulation policies, and support embodied physical reasoning. Yet existing surveys largely emphasize tactile hardware and perception, leaving the rapid shift toward learning-based tactile manipulation insufficiently synthesized. This paper reviews tactile-gu...
  </details>

- **2026-10-14** — Yanni Mei, Samuel Hartenstein, Jonas Wombacher et al. — [ShadAR: Real-time Prompting On-demand Visual Augmentation in Augmented Reality](http://arxiv.org/abs/2610.19998v1)
  <details><summary>📄 Abstract</summary>
  Augmented Reality can reshape our visual perception (e.g., simulating color blindness) yet such effects are typically pre-programmed by experts, making visual augmentation static and inflexible. We introduce ShadAR, an AR system that allows users to describe expected visual augmentations (e.g., "Blur all people") for changing their vision in real time. ShadAR can graphically manipulate AR passthrough in real time via shader injection. When receiving a user's prompt, ShadAR uses LLMs (GPT5.2) to ...
  </details>

- **2026-10-14** — Hasan Amin, Zhuoran Lu, Ming Yin — [Likelihood Is Not Authorship: Can We Reliably Measure Human Contribution in AI-Assisted Writing?](http://arxiv.org/abs/2610.19767v1)
  <details><summary>📄 Abstract</summary>
  AI-text detection generally asks whether a machine wrote a text. As AI becomes an increasingly integral and accepted part of writing, the more relevant question is no longer whether AI was used, but how much of the text reflects human contribution. A prominent line of work estimates this by measuring how predictive a person's prompt is of the final text. We show that this measure can be easily manipulated. We introduce SPECIFICITY PADDING that simply asks the model to copy a few random IDs from ...
  </details>

- **2026-10-14** — Stephen Fernandes, Narayan Choudhary — [Anuvani-Diarization: Zero Shot Speaker Diarization and Annotation Conventions Across 22 Languages](http://arxiv.org/abs/2610.20327v1)
  <details><summary>📄 Abstract</summary>
  India's 22 scheduled languages are spoken by over a billion people in conversations that mix languages, often within one turn, overlap freely, and take place over telephones, in meetings, and in media. Knowing who spoke when, the task of speaker diarization, is essential to speech applications for such conversation: voice agents conversing with several people at once, speaker attributed transcription of meetings and calls, contact center analytics, and media monitoring. We present a systematic s...
  </details>

- **2026-10-14** — Jingqin Tang, Tim Tomov, Sebastian Schmidt et al. — [What Is a Clarification? Estimating Model-Dependent Input Ambiguity](http://arxiv.org/abs/2610.20052v1)
  <details><summary>📄 Abstract</summary>
  Ambiguous inputs can admit multiple interpretations, each potentially yielding a different answer. Existing work largely treats this ambiguity as a property of the input, yet for a particular language model, only some alternatives may be known and answerable. We therefore distinguish world ambiguity, capturing all alternatives admitted by an input, from model ambiguity, capturing those accessible to the responding model. To characterize these alternatives, we formalize natural-language clarifica...
  </details>

- **2026-10-14** — Kristoffer Hjelmen Nesland, Bjarne Grimstad, Antorweep Chakravorty et al. — [Text-Informed Training Data Filtering for Enhanced Virtual Flow Meter Performance](http://arxiv.org/abs/2610.19860v1)
  <details><summary>📄 Abstract</summary>
  In sectors such as energy, aquaculture and chemical processing, the effectiveness of both mechanistic and data-driven models is frequently limited by poor-quality training data, which obscures underlying physical laws and degrades predictive accuracy. Such quality issues commonly manifest as anomalies in the dataset, ranging from sensor faults to process upsets and incorrect operator inputs. While traditional rule-based filtering can remove a subset of the anomalies, it is unable to leverage con...
  </details>

- **2026-10-14** — Titouan Sérandour, Anne-Laure Méalier, Bruno Colicchio et al. — [Identifying Planetary Nebulae Candidates from IPHAS and VPHAS+ Surveys via YOLO Deep Learning Models](http://arxiv.org/abs/2610.19760v1)
  <details><summary>📄 Abstract</summary>
  We present a deep learning detection method capable of effectively identifying planetary nebulae (PNe) on IPHAS and VPHAS+ surveys. Our detection pipeline is based on the YOLO architecture and is adaptable to other datasets. Using the HiPS system, we preprocess and augment the $r$, $i$, and $Hα$ bands to produce two red, green, and blue (RGB) image datasets: (1) $640 \times 640$ px images at full resolution, and (2) $1 280 \times 1 280$ px images designed to capture extended objects up to $0.2$ ...
  </details>

- **2026-10-14** — Md Rayhanul Masud, S M Maksudul Alam, Mohammad Jaminur Islam — [BANGLAPLAN: A Benchmark for Constraint-Based Planning and Decision-Making in Bangla](http://arxiv.org/abs/2610.19704v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly help users arrange appointments, plan journeys, and allocate limited resources. These tasks require models to satisfy constraints on time, cost, capacity, and order, or determine that no feasible solution exists. Bangla is the world's seventh most widely spoken language, and existing benchmarks cover many language and reasoning tasks. However, benchmarks for evaluating planning and decision-making in Bangla under explicit constraints remain lacking. We i...
  </details>

- **2026-10-14** — Jun Yang, Yumeng Cao, Yingxuan Xiao et al. — [ESL-former: Event Sparse Linear Transformer for FPGA-Accelerated Malware Detection](http://arxiv.org/abs/2610.19665v1)
  <details><summary>📄 Abstract</summary>
  Transformer based intrusion detection has shown strong potential for identifying unknown malware variants, but its deployment on resource constrained edge devices remains difficult due to the high computational and memory cost of self attention. This paper presents an event sparse Linear Transformer framework for malware detection on FPGA edge platforms. Instead of relying on an explicit attention matrix, the proposed method derives token and channel importance directly from the accumulated key ...
  </details>

- **2026-10-14** — Haoxiang Rao, Fang Zhao, Zhao Wang et al. — [CORE: Contrast-and-Reflect for Self-Supervised Prompt Optimization in Anomaly Synthesis](http://arxiv.org/abs/2610.19610v1)
  <details><summary>📄 Abstract</summary>
  Industrial anomaly detection (AD) is bottlenecked by the scarcity of anomalous samples, making high-fidelity anomaly synthesis crucial for improving downstream performance. However, existing methods either rely on scarce real anomaly references or auxiliary data, while lacking complex reasoning and iterative optimization capabilities for generating realistic defects in open-set scenarios. To address these challenges, we propose CORE, a cost-efficient and training-free prompt optimization framewo...
  </details>

- **2026-10-14** — Jingyuan Li, Dongzhan Zhou, Minting Pan et al. — [LabCompiler: A Framework for Verifiable Human-Machine Laboratory Execution from Imperfect Protocols](http://arxiv.org/abs/2610.19550v1)
  <details><summary>📄 Abstract</summary>
  Closing the loop of AI-driven science requires reliably translating natural-language protocols into executable laboratory workflows despite protocol defects and heterogeneous hardware. Existing approaches often couple scientific interpretation with device-specific code generation, making errors difficult to localize and limiting reuse across laboratory platforms. We introduce LabCompiler, a robust protocol-to-execution framework that transforms imperfect natural-language protocols into verifiabl...
  </details>

- **2026-10-14** — Baowen Zhang, Hangting Ye, Hongyuan Zha — [Typed Decision Models on Tabular Data](http://arxiv.org/abs/2610.19536v1)
  <details><summary>📄 Abstract</summary>
  Typed decision models are language models that answer a question with a fixed set of possible answers by returning a probability for each answer instead of generating text. We study them on tabular data and compare four decision models with three large language models (LLMs) on row classification, fact verification and anomaly detection. Every request is sent in its original form and under 21 types of rewrite that keep its content, such as renaming the options or writing the table in another for...
  </details>

- **2026-10-13** — Xiao Yang, Zekun Zhang, Yuxuan Fan et al. — [Why Do VLMs Fail at Remote Physiological Measurement? Rethinking with Physiological Grounding and Numerical Alignment](http://arxiv.org/abs/2610.19052v1)
  <details><summary>📄 Abstract</summary>
  Video-based remote physiological measurement (RPM) has broad applications, while Vision-Language Models (VLMs) provide a promising opportunity to enable end-to-end physiological monitoring for future human-aware intelligent systems. However, existing RPM methods rely on task-specific models and cannot be seamlessly integrated with the multimodal understanding and interaction capabilities of VLMs. We revisit RPM with VLMs and provide empirical evidence for two major bottlenecks: generic visual se...
  </details>

- **2026-10-13** — Fawaz Abdul Razak, Bora Turgut, Mason Clark et al. — [Sequential RF Fingerprinting for AIS: Rejecting Unknown Vessels and Insider MMSI Spoofs Days After Enrollment](http://arxiv.org/abs/2610.19115v1)
  <details><summary>📄 Abstract</summary>
  Any AIS transmitter can claim any vessel's identity (MMSI), because nothing in the protocol authenticates it; only the transmitter's analog hardware reveals who is really sending. We treat AIS traffic as streams of bursts keyed by claimed MMSI and accumulate physical-layer evidence with a sequential test. Each burst is scored by its k-nearest-neighbor distance to enrolled fingerprints in the feature space of a classifier whose weights are fixed after training, calibrated into a tail probability,...
  </details>

- **2026-10-13** — Mah Kadidia Konate, Mayur Akewar, Janki Bhimani et al. — [REPORT-OPS: Hybrid Evidence-Guided Reporting with Human-Supervised Refinement for HPC](http://arxiv.org/abs/2610.19222v1)
  <details><summary>📄 Abstract</summary>
  Operational reporting for high-performance computing (HPC) facilities requires combining information from monitoring services, schedulers, incident and maintenance records, storage measurements, periodic reports, and operator investigations. Producing a reliable report requires more than retrieving relevant records: the evidence must refer to the correct system, metric definition, time period, and source of authority. We present REPORT-OPS, a hybrid reporting agent in which an LLM interprets req...
  </details>

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


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-10-14** — Saeed Razavi, Xingjian Leng, Liang Zheng — [Representation Conditioning for Generation](http://arxiv.org/abs/2610.20608v1)
  <details><summary>📄 Abstract</summary>
  Representation-alignment methods effectively accelerate the diffusion transformer training. REPA, for example, uses a pretrained vision encoder to supervise an intermediate layer through an MLP projection head which is discarded after training. It aims to import semantics from the vision encoder to the diffusion backbone. While this objective is achieved at early layers by back-propagating the alignment loss, there is no guarantee that later layers, supervised by the velocity prediction loss alo...
  </details>

- **2026-10-14** — Zhefei Gong, Hefeifei Jiang, Zehao Wang et al. — [Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](http://arxiv.org/abs/2610.20607v1)
  <details><summary>📄 Abstract</summary>
  Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex MoMa systems. At its core, HiRe-MoMa adopts a Hierarchical Residual Architecture that fine-tunes a fr...
  </details>

- **2026-10-14** — Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio André Machado Porto — [Manacá-1B-Instruct-2: Reproducible Safety Alignment for a Native Brazilian-Portuguese LLM. Negative DPO Results, a Controlled Composition Scan, and a Silent Failure Mode of the LLM Judge](http://arxiv.org/abs/2610.20570v1)
  <details><summary>📄 Abstract</summary>
  Brazilian Portuguese remains underserved by open-source language models, and the few that are safety-aligned rarely document what did not work or validate comparisons with statistical significance. We present Manacá-1B-Instruct-2, the second-generation post-training alignment of Manacá-1B (1.72B parameters, trained from scratch for PT-BR), with an SFT corpus of 291,223 examples. We document three DPO attempts, all negative, including a case where the training reward margin reaches 1.0 while free...
  </details>

- **2026-10-14** — Rusali Saha, Nitya Khurana, Ruihong Huang et al. — [ChronoCulture: Evaluating Cultural Awareness Across Time in Large Language Models](http://arxiv.org/abs/2610.20472v1)
  <details><summary>📄 Abstract</summary>
  Cultural attitudes and social norms evolve over time, yet most cultural benchmarks for large language models (LLMs) treat culture as a static attribute of a country or region. We introduce ChronoCulture, a benchmark of 10,360 temporal pairs built from longitudinal survey data across 72 countries. Each pair contains the same survey question asked in the same country in an older and a newer year, with full population response distributions as ground truth. Across six LLMs, we find that models can ...
  </details>

- **2026-10-14** — Nguyen Nguyen, Yongyi Zang — [Equal CER, Unequal Damage: Severity-Weighted Character Error Rate for OCR](http://arxiv.org/abs/2610.20461v1)
  <details><summary>📄 Abstract</summary>
  Character Error Rate (CER), the standard metric for OCR and vision-language models (VLMs), charges a typo as much as a wrong name. We introduce semCER, which keeps CER's alignment and denominator and charges each grapheme edit a severity from an LLM judge, with no word segmentation. Normalized CER keeps the score of a whole transcription, where it tracks readers as well as semCER or better, and semCER breaks that score down into named edits. The charges track readers' ratings edit by edit in Eng...
  </details>

- **2026-10-14** — Dwaipayan Haldar, Indranil Patra, Azhar Yousuf et al. — [SpectrumQuant: Spectrum Alignment for LLM Quantization](http://arxiv.org/abs/2610.20303v1)
  <details><summary>📄 Abstract</summary>
  Orthogonal transforms have emerged as an effective tool for low-bit quantization of large language models (LLMs), as they reshape activation distributions without changing the underlying model function. Existing approaches typically rely either on fixed data-agnostic transforms, such as Hadamard rotations, or on calibration-time optimization of learned rotations. We study rotation selection from first principles and show that maximizing covariance leads to spectral alignment and provides a princ...
  </details>

- **2026-10-14** — Dai Shi, Andi Han, Xiaoyu Li et al. — [From Plato to Aristotle: Toward a General Theory of Representation Hypotheses](http://arxiv.org/abs/2610.20286v1)
  <details><summary>📄 Abstract</summary>
  The Platonic Representation Hypothesis (PRH) holds that increasingly capable models converge toward a common representation. However, recent studies have shown different views on aligning representations via their neighborhoods, spanning trees, and distances. We show that these views can differ because the alignment criteria behind them sit at different points of one lattice, and we formalize this explanation as the Lattice Representation Hypothesis (LRH). Under the LRH, the convergence claimed ...
  </details>

- **2026-10-14** — Jiyu Tian, Mingchu Li, Xiangwei Chen et al. — [Towards Efficient Threat Intelligence Instruction Tuning via Quality-Aware and Optimal Transport-Guided Data Selection](http://arxiv.org/abs/2610.20284v1)
  <details><summary>📄 Abstract</summary>
  High-quality data is essential for improving instruction tuning in threat intelligence analysis. However, existing methods for generating cybersecurity instruction data lack reliable quality assessment mechanisms, and gradient influence-based data selection methods primarily focus on single-sample matching, failing to cover diverse and complex security capabilities. To address these issues, we propose CTI-TDS, a Targeted Data Selection method for instruction tuning in Cyber Threat Intelligence a...
  </details>

- **2026-10-14** — Junlin Chen, Wenhao Wang, Junchao Xu et al. — [MAEM: Mitigating Recency Bias via a Replay-Free, Capacity-Controlled Dynamic Mixture of Experts for Class-Incremental Graph Learning](http://arxiv.org/abs/2610.20238v1)
  <details><summary>📄 Abstract</summary>
  Graph Neural Networks (GNNs) excel on graph-structured data but suffer catastrophic forgetting when classes arrive sequentially. In class-incremental graph learning, predictions are often dominated by recently learned classes, causing severe recency bias. Dynamic expansion can isolate knowledge across sessions, but many methods assume task-incremental settings and require task identities at test time to select branches or heads---information unavailable in class-incremental learning. Learnable r...
  </details>

- **2026-10-14** — Bilal A. Sidiqi, Yipei Wang, Shaheer U. Saeed et al. — [Continual pretraining Prostate MRI ViT Encoder for task alignment](http://arxiv.org/abs/2610.20217v1)
  <details><summary>📄 Abstract</summary>
  Building foundation models for MRI has emerged as a promising direction for advancing medical image analysis and improving accessibility of task specific models. Existing approaches primarily focus on effective pretraining strategies and evaluating their performance across diverse downstream tasks. While these methods show performance gains, limited attention has been given to understanding task alignment between pretraining and downstream objectives. Unlike language models, where the two stages...
  </details>

- **2026-10-14** — Min Xiao, Jin Li, Shoujin Wang et al. — [HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication Recommendation](http://arxiv.org/abs/2610.20191v1)
  <details><summary>📄 Abstract</summary>
  Medication recommendation (MR) is critical for clinical decision support. While existing MR methods are mostly designed for single-center learning, where only one independent hospital is involved, multi-center MR with hospitals of different scales has become increasingly demanding in practice. In multi center settings, abundant data from large medical centers can improve recommendation performance for low-resource centers. Despite a few preliminary attempts on this task, two critical gaps remain...
  </details>

- **2026-10-14** — Alex Wolf, Pooja Rani, Harald C. Gall — [Temporal Adaptive Fine-Tuning for Code Comprehension](http://arxiv.org/abs/2610.19970v1)
  <details><summary>📄 Abstract</summary>
  Repository-level code comprehension question answering (QA) supports developer reasoning over functionality and usage distributed across codebases. However, repository-specialized large language models (LLMs) can become misaligned as code evolves. We study this challenge as temporal repository adaptation: acquiring new knowledge, suppressing obsolete, retaining still-valid, and preserving semantically neighboring knowledge. Existing retrieval, fine-tuning, and model-editing methods address only ...
  </details>

- **2026-10-14** — Ridong Zhang, Shuxian Liang, Chaoqun Wan et al. — [How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](http://arxiv.org/abs/2610.19900v1)
  <details><summary>📄 Abstract</summary>
  As GUI agents are increasingly deployed for mobile task automation, their reliability depends not only on final task outcomes, but also on whether they reach these outcomes through stable interaction trajectories. In automation workflows, unnecessary actions, detours, and execution errors can add noise to collected data, introduce irreversible side effects, or undermine trust, even when the agent eventually completes the task. It is therefore important to systematically diagnose the execution st...
  </details>

- **2026-10-14** — Mikołaj Piórczyński, Wojciech Masarczyk, Damian Sójka et al. — [On the Limits of Representation-Based Test-Time Adaptation for Multimodal LLMs](http://arxiv.org/abs/2610.19892v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models suffer significant accuracy drops under common corruptions. While test-time adaptation (TTA) successfully mitigates these shifts in CLIP-like contrastive models, its application to generative multimodal large language models (MLLMs) remains underexplored and uniquely challenging due to their sequential token generation. In this work, we demonstrate that representation-based TTA fails to recover performance in MLLMs. Our experiments reveal that even when violating standard ...
  </details>

- **2026-10-14** — Siwei Meng, Xuerou Cai, Rui Hu et al. — [PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](http://arxiv.org/abs/2610.19823v1)
  <details><summary>📄 Abstract</summary>
  Text-to-video (T2V) generation models can produce visually realistic videos that nevertheless violate the physical consequences implied by the prompt and scene. Existing benchmarks largely rely on holistic plausibility scores or broad quality dimensions, leaving it unclear which physical behavior is being tested and why a model fails. We introduce PhyMetric, a scene-level diagnostic benchmark that recasts physical plausibility evaluation as verifiable, scene-grounded question answering. PhyMetri...
  </details>

- **2026-10-14** — Huining Yuan, Xiangmin Yi, Zelai Xu et al. — [ActionOPD: Distilling Decisions, Not Tokens](http://arxiv.org/abs/2610.19820v1)
  <details><summary>📄 Abstract</summary>
  Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision and can suffer from state-distribution mismatch. Token-level on-policy distillation (OPD) addresses this mismatch but typically requires teacher token probabilities and compatible tokenization. We argue...
  </details>

- **2026-10-14** — Enrico Liscio, Anne Arzberger, Aditya Shankar et al. — [Model vs. User: Whose Values Prevail? Inference-Time Value Alignment in Multi-Turn Conversations](http://arxiv.org/abs/2610.19817v1)
  <details><summary>📄 Abstract</summary>
  Human values shape how we expect language models to behave. Dominant alignment approaches treat values as global objectives, although the appropriate value orientation is personal and contextual. Training-free alignment can steer models toward target values at inference time, yet has been largely evaluated in single-turn settings and with a single steering direction (e.g., toward safety). We evaluate four prompt- and activation-based steering methods in multi-turn conversations, where user and a...
  </details>

- **2026-10-14** — Julia Barth, Armin Sommer, Kunvar Thaman et al. — [What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization](http://arxiv.org/abs/2610.19731v1)
  <details><summary>📄 Abstract</summary>
  Goal misgeneralization is a common failure mode in which an agent behaves competently out of distribution but does not pursue the intended goal. However, we still have a weak understanding of what happens to the intended goal in misgeneralizing agents. Across three Procgen environments and five robot tasks, we find three distinct forms of policy-goal misalignment: (1) functional target substitution, where behavior follows an alternative goal, (2) a policy shortcut, where behavior follows a learn...
  </details>

- **2026-10-14** — Jing-Xuan Zhang, Genshun Wan, Jianqing Gao et al. — [Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling](http://arxiv.org/abs/2610.19559v1)
  <details><summary>📄 Abstract</summary>
  Lipreading remains challenging due to the inherent ambiguity of visual speech cues and their sensitivity to head pose and video resolution. In this work, we propose FLARE, a framework for robust visual speech representation learning via cross-modal distillation and joint face-lip modeling. FLARE leverages semantically rich Whisper representations as the acoustic teacher signal, converting them into discrete distillation targets through a random-projection quantizer and pretraining the model with...
  </details>

- **2026-10-14** — Kyusong Lee, Heting Ying, Tiancheng Zhao — [VLX-Go: Robust Embodied Tracking through Multi-Stage Learning and On-Policy Refinement](http://arxiv.org/abs/2610.19361v1)
  <details><summary>📄 Abstract</summary>
  Embodied visual tracking requires a robot to identify a designated target from visual observations and control its own motion to follow that target through an environment. Following an isolated person is a comparatively simple demonstration of embodied visual tracking, but following the intended person among distractors remains challenging. Existing methods exhibit a substantial drop in success from single-target to distractor tracking, motivating a focus on the shared spaces that person-followi...
  </details>

- **2026-10-14** — Zixiao Wang, Xingbo Du, Duzhen Zhang et al. — [Rent-Seeking Language Models: Reward Models Set the Prices, Frequent Audits Curb the Rent](http://arxiv.org/abs/2610.19832v1)
  <details><summary>📄 Abstract</summary>
  Reward model overoptimization in RLHF is usually described as reward hacking. We recast it as rent-seeking: the policy, a firm, earns reward from a regulator, the proxy reward model, that true quality does not back. The lens turns overoptimization into measurable quantities, namely rent, a capture index and deadweight loss, and into testable predictions from the economics of regulation. In a fixed, version-controlled testbed with three model families, accuracy-matched proxy reward models and two...
  </details>

- **2026-10-13** — Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang et al. — [Agentic Self-Awareness: Aligning Knowing, Acting, and Holding](http://arxiv.org/abs/2610.19226v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments (know), warranted behavior (act), and responses to reconsideration (hold), distinguishing what a task permits from what an agent can solve. We build paired feasible and blocked tasks in Terminal-Bench 2.1 and retail $τ^...
  </details>

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


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 56 papers

- **2026-10-14** — Yong-Hui Hua, Chih-Han Lin, Shu-Kai Hsieh — [Do AI Agents Gossip? Evaluative Talk in Human and AI-Agent Online Communities](http://arxiv.org/abs/2610.20360v1)
  <details><summary>📄 Abstract</summary>
  Gossip, defined as evaluative talk about absent third parties, is widely seen as a uniquely human social practice. This study examines whether comparable discourse emerges spontaneously in a community of autonomous AI agents. We compare Moltbook, a Reddit-style platform populated by AI agents, with PTT, a large human-operated bulletin board in Taiwan. To reduce differences attributable to communicative setting, we analyze two public, asynchronous forums using the same operational definition of g...
  </details>

- **2026-10-14** — Sebastian Nagl — [SoK: Grading Open-Text Legal Answers, from Law School Exams to Trustworthy Rubric Judges](http://arxiv.org/abs/2610.19992v1)
  <details><summary>📄 Abstract</summary>
  Law students are examined through open-text answers: case solutions, essays and memos that apply the law to a set of facts. Such answers are expensive to grade, human graders disagree widely on them, and large language models (LLMs) now offer to grade them at scale, both in teaching and in the benchmarks that test legal AI. This paper systematizes how open-text legal answers can be evaluated. We derive eight desiderata from educational measurement and from the law that governs exams, among them ...
  </details>

- **2026-10-14** — Zihao Lin, Haoyu Dong, Haobo Xu et al. — [VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](http://arxiv.org/abs/2610.19424v1)
  <details><summary>📄 Abstract</summary>
  LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive harness evolution can automate their design, but how it can reliably discover generalizable systems from limited, noisy, and repeatedly reused feedback remains unclear. We study this question in agentic video understanding, where rich multimodal evidence and coupled mechanisms make harness optimization challenging. We f...
  </details>

- **2026-10-14** — Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke et al. — [Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States](http://arxiv.org/abs/2610.19342v1)
  <details><summary>📄 Abstract</summary>
  Agents are increasingly interacting with other agents that act for different principals -- people or organizations on whose behalf they work -- e.g., a buyer's personal agent negotiating with an enterprise's seller agent. In such agent-to-agent (A2A) scenarios, each agent has its own environment and holds information and authority that the other cannot see. Moreover, the interests of each agent may be aligned (cooperative), partly aligned (mixed-motive), or opposed (competitive). Existing multi-...
  </details>

- **2026-10-14** — Huailiang Ma, Yuxuan Li, Ziyi Zhao et al. — [ObjDream: Guiding Vision-Language-Action Models with Object-Level Understanding and Future State Prediction](http://arxiv.org/abs/2610.20223v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have emerged as a powerful paradigm for robotic manipulation, enabling robots to generate actions from visual observations and language instructions. However, most existing VLA models still operate on image-level visual representations inherited from pretrained vision-language backbones, while lacking fine-grained object understanding for manipulation. As a result, their robustness can degrade under out-of-distribution object layouts, clutter, and background v...
  </details>

- **2026-10-14** — Keqiang Ren, Xuecheng Ye, Hanyu Liu et al. — [RoboSpan: Learning Modular Coordination Policies for High-DoF Whole-Body Mobile Manipulation with Teleoperation](http://arxiv.org/abs/2610.19594v1)
  <details><summary>📄 Abstract</summary>
  Whole-body mobile manipulation suffers from two fundamental challenges: inherent motion heterogeneity across locomotion, arm, and hand modules, and progressive error accumulation over long-horizon multi-stage tasks. Existing teleoperation platforms also lack integrated dexterous tactile sensing to support coordinated whole-body decision-making. This paper presents RoboSpan, a high-DoF whole-body teleoperation and demonstration platform, and the Hierarchical Modular Framework (HMF) for learning m...
  </details>

- **2026-10-14** — Artin Tajdini, Manpreet Kaur, Peng Qi — [One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](http://arxiv.org/abs/2610.20576v1)
  <details><summary>📄 Abstract</summary>
  Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-I...
  </details>

- **2026-10-14** — Stephen Fernandes, Narayan Choudhary — [Anuvani-LID: Robust and Calibrated Spoken Language Identification for Indian Languages](http://arxiv.org/abs/2610.20263v1)
  <details><summary>📄 Abstract</summary>
  Every multilingual speech pipeline begins with a language decision, an error there propagates silently through recognition, translation and routing. In India it spans 22 scheduled languages across four language families, heard over short, noisy, narrowband and code-mixed audio. Foundational speech models increasingly present language identification (LID) as an inherent latent, generalized capability. Autoregressive decoders in speech models emit a special language ID token, and modern LLMs with ...
  </details>

- **2026-10-14** — Miguel Leiva-Vélez, Nicolas Gaston-Rozado, Andrea Scorsoglio et al. — [Adversarial Reinforcement Learning for Robust Planetary Landing](http://arxiv.org/abs/2610.20252v1)
  <details><summary>📄 Abstract</summary>
  Deep reinforcement learning (DRL) policies for planetary landing and other aerospace guidance, navigation, and control tasks are commonly trained under randomized disturbances to improve robustness. However, typical stochastic perturbation sampling assumes independent variations, whereas real mission disturbances often exhibit spatial and temporal correlation and cannot be reproduced through independent random draws. This work investigates adversarial reinforcement learning to discover challengi...
  </details>

- **2026-10-14** — Zhaoyang Wang, Dingding Yao, Chengzhong Wang et al. — [Noise-Aware Lombard Speech Synthesis via Flow-GRPO for Intelligibility Optimization](http://arxiv.org/abs/2610.20181v1)
  <details><summary>📄 Abstract</summary>
  Voice-based conversational agents are increasingly deployed in real-world settings, where environmental noise often degrades the interactive experience. Therefore, robust acoustic adaptability is essential to maintain natural and intelligible human-computer communication. However, most existing systems remain acoustically insensitive and fail to emulate the human Lombard effect, in which speakers involuntarily adjust their vocal production to preserve intelligibility in the presence of noise. As...
  </details>

- **2026-10-14** — Huaisheng Zhu, Hangfan Zhang, Teng Xiao et al. — [EvalBuilder: Can LLMs Build Efficient Benchmarks?](http://arxiv.org/abs/2610.20099v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly used for long-horizon research and engineering, yet evaluating these capabilities remains expensive, time-consuming, and heavily dependent on human expertise. This motivates a natural question: can LLM agents themselves construct efficient benchmarks that preserve the conclusions of costly reference evaluations? We study this capability by formulating automatic benchmark development as a meta-evaluation problem, where an agent is given a task an...
  </details>

- **2026-10-14** — Biplab Poudel, Betserai Albert Magarire, Anish Kumar Shah et al. — [GDBA-Net: A Gated Dual-Branch Adaptation of SAM2 for Robust Cross-Domain Nuclei Segmentation](http://arxiv.org/abs/2610.20073v1)
  <details><summary>📄 Abstract</summary>
  Accurate nuclei segmentation underpins quantitative computational pathology, yet remains challenging due to morphological variability, weak boundaries, nuclear crowding, and pronounced domain shifts arising from differences in tissue preparation, staining, and acquisition. While deep learning and recent foundation models have improved segmentation performance under matched distributions with the original training data, their generalization across heterogeneous histopathology domains remains limi...
  </details>

- **2026-10-14** — Riccardo Andreoni, Massimiliano Ronzani, Chiara Ghidini et al. — [Neurosymbolic Learning of Interpretable World Models](http://arxiv.org/abs/2610.19955v1)
  <details><summary>📄 Abstract</summary>
  World models aim to learn compact representations of an environment from observations, enabling agents to predict future states and plan their behaviour. However, most existing approaches learn black-box representations, with limited ability to incorporate prior knowledge about the world. We introduce Concept-Grounded World Models (CGWMs), a neurosymbolic world model design that instead learns interpretable concept representations. We learn these concepts from observations using explicit and com...
  </details>

- **2026-10-14** — Tao Yu, Zhongtian Luo, Yuchen Long et al. — [When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Self-Evolution in Agents](http://arxiv.org/abs/2610.19910v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents increasingly improve by distilling experience into reusable skills, but errors in that experience can persist in learned rules and affect later tasks. Existing evaluations largely examine clean learning or perturbations encountered after skills are frozen, leaving robustness during self-evolution insufficiently understood. We introduce RSE-Bench, to our knowledge the first benchmark for evaluating skill self-evolution under ordinary, non-adversarial noise. It spans fo...
  </details>

- **2026-10-14** — Sajad Marvi, Julian Schmidt, Alessandro Canevaro et al. — [Uncertainty-Driven Self-Play for Robust Multi-Agent Driving Policies](http://arxiv.org/abs/2610.19714v1)
  <details><summary>📄 Abstract</summary>
  Learning robust driving policies that generalize beyond their training domain remains a central challenge in motion planning. We propose an uncertainty-driven self-play scheme, in which half of the agents are rewarded for increasing their neighbors' epistemic uncertainty, while the other half learn to drive safely as the exploring agents continuously seek out their weaknesses. Epistemic uncertainty indicates where the policy is least confident and serves as an automatic proxy for scenario diffic...
  </details>

- **2026-10-14** — Hyunsik Oh, Seunghun Jeon, Donghoon Youm et al. — [PolyMorph: Learning Locomotion Policy for Cross-Embodiment Adaptation](http://arxiv.org/abs/2610.19615v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning has enabled robust locomotion for legged robots, but learned policies are typically tied to a specific robot morphology and require additional engineering when the number of legs, actuators, or mechanical properties change. We present PolyMorph, a morphology-conditioned framework that learns a single locomotion policy for heterogeneous legged robots. PolyMorph converts each robot's URDF into joint-link modules and combines a recurrent encoder, graph-based Transformer, and ...
  </details>

- **2026-10-14** — Hanlong Li, Sihan Tan, Takeshi Ashizawa et al. — [Paraphrase Consensus Is Not Self-Consistency: Instruction Reliance and Robustness in VLA Policies](http://arxiv.org/abs/2610.19438v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) policies fine-tuned on LIBERO are trained and evaluated on the same ten instruction strings, and rewording the instruction changes base OpenVLA's success by -38.0 points. Test-time prompt ensembling, which improves language models, does not recover this loss in any setting we ran. Paraphrase consensus (the medoid action over K paraphrases) costs base OpenVLA 16.8 points when the training instruction is a member. Without it, the medoid of the paraphrases scores -32.4 ...
  </details>

- **2026-10-14** — Josh Barua, Kyle Mahowald, William Rudman — [Vision-Language Models Integrate Conflicting Evidence Like Biased Bayesian Observers](http://arxiv.org/abs/2610.19407v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models must reconcile conflicting text and images. Prior work has characterized the resulting behavior in terms of modality biases--e.g., a "blind faith in text"--but why preferences vary across models, domains, and input conditions remains unclear. We develop a predictive account from a Bayesian perspective, positing that VLMs combine conditionally independent evidence from each modality with prior beliefs, subject to modality-specific biases. The resulting two-parameter cue com...
  </details>

- **2026-10-13** — Akash Raj — [Plant Memory: Technical Language Processing and a Verified Maintenance Ontology for Agent-Accessible Failure Knowledge from SAP PM Work Orders](http://arxiv.org/abs/2610.19131v1)
  <details><summary>📄 Abstract</summary>
  Maintenance work orders are the largest written record of how industrial equipment fails, yet in most plants they are close to unusable for analysis. Short texts are abbreviated and misspelt, asset identity is buried in free text, work-type labels contradict the work described, and the fields that matter most for reliability (symptom, root cause, action taken) are usually empty. As a result, diagnostic knowledge stays with senior technicians and leaves when they do. We present Plant Memory, a sy...
  </details>

- **2026-10-13** — Bo Shao, Yihan Ma, Yiting Qu et al. — [MemeTrace: A Multimodal LLM-Based Agent for Safety-Aware Meme Provenance Analysis](http://arxiv.org/abs/2610.19267v1)
  <details><summary>📄 Abstract</summary>
  Online memes are often carriers of unsafe content such as disinformation and propaganda. Their rapid evolution in response to news events and strong dependence on contextual information make it difficult for platforms and moderators to detect and moderate them effectively. Moreover, existing moderation studies typically classify memes as safe or unsafe based on individual images, lacking the ability to perform broader provenance analysis, i.e., where a meme originates, how it spreads, what cultu...
  </details>

- **2026-10-13** — Chang Liu, Sibo Tian, Litian Gong et al. — [PACER: Process-Aware VLA Policy Learning from Human Corrections for Robotic Disassembly](http://arxiv.org/abs/2610.19248v1)
  <details><summary>📄 Abstract</summary>
  Robotic disassembly of end-of-life (EoL) products requires robots to accommodate product variation, follow prerequisite sequences, and approach components precisely for contact-rich manipulation. Supervised fine-tuning (SFT) provides a practical path for adaptation, but limited and costly disassembly data cannot capture the distribution shifts arising from changing environments and product uncertainties. The policy's own rollouts record its approach attempts, and human corrections demonstrate re...
  </details>

- **2026-10-13** — Shaocheng Liu, Yuan Meng, Zhenshan Bing et al. — [Collective Learning for Unified Robotic Manipulation via Predictive Dynamics Adaptation](http://arxiv.org/abs/2610.19141v1)
  <details><summary>📄 Abstract</summary>
  Learning a collective policy for state-based Cartesian manipulation across diverse robotic embodiments presents a fundamental challenge due to embodiment-dependent transition dynamics. Collective learning aggregates multi-robot experience to discover shared task structure, yet naive aggregation can average incompatible action modes when different embodiments realize the same Cartesian command through different transition behavior. This leads to strategy ambiguity and performance collapse on dyna...
  </details>

- **2026-10-13** — Xiyin Zeng, Xuewei Huang, Yi Lu et al. — [ReEnvision: Future-Guided Selective Action Repair for Long-Horizon Manipulation](http://arxiv.org/abs/2610.17977v2)
  <details><summary>📄 Abstract</summary>
  Long-horizon robotic manipulation requires robust execution over sequences of interdependent actions. Existing methods typically handle execution deviations by replanning the remaining action chunk or correcting actions step by step as new observations arrive. However, a local deviation may affect only a few actions under distribution shift, yet replanning regenerates the entire chunk from an unfamiliar state, potentially introducing errors into otherwise valid actions. Step-wise correction may ...
  </details>

- **2026-10-13** — Chi Wang, Hai-Han Sun — [FFDT: Sim-to-Real Domain Transfer Method for Far-Field Ground Penetrating Radar](http://arxiv.org/abs/2610.19265v1)
  <details><summary>📄 Abstract</summary>
  The scarcity of real-world ground penetrating radar (RealGPR) data is a major barrier to the development of deep learning (DL) methods for GPR data processing. Although simulated GPR (SimGPR) datasets can be used to train DL models, differences in hardware configuration and system parameters between SimGPR and RealGPR create a sim-to-real domain gap that leads to poor generalization of DL models to RealGPR measurements. To address this gap, we present a physics-based far-field GPR domain transfe...
  </details>

- **2026-10-13** — Hannah Lawrence, Bodhi P. Vani, Ji Won Park et al. — [PairIT: Autoregressive Transformers for Low-Data Molecule Optimization](http://arxiv.org/abs/2610.19123v1)
  <details><summary>📄 Abstract</summary>
  Generating novel molecules with desired properties is a central challenge in drug discovery. Although foundational work focused on de novo generation, practical use cases require a more complex setting: conditioning on an initial seed molecule, optimizing multiple properties, and operating in data-sparse regimes. We introduce PairIT, a flexible training framework for autoregressive transformers over SMILES sequences that enables seeded generation by learning from pairs of structurally similar mo...
  </details>

- **2026-10-13** — Qingsong Xie, Jiahao Tian, Jiacheng Tang et al. — [GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning](http://arxiv.org/abs/2610.19100v1)
  <details><summary>📄 Abstract</summary>
  Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a comprehensive GUI grounding dataset consisting of GUI screenshots paired with natural language referring expressions...
  </details>

- **2026-10-13** — Mingfei Zhang, Amit Surana, Ziauddin Majid et al. — [Plan or Retrieve First? A Scale Study of Tool Discovery Architectures](http://arxiv.org/abs/2610.19068v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retrieves similar tools via approximate nearest-neighbor search. We study an alternative Plan-then-Retrieve (PtR) paradigm in which the LLM first generates Abstract Tool Stubs (hypothesized function signatures describing nee...
  </details>

- **2026-10-13** — Yifan He, Manon Reusens, Sofie Goethals et al. — [A Global View of How LLMs Value Human Time](http://arxiv.org/abs/2610.18515v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly act as personal assistants; however, little is known about how they capture national-level preferences on a global scale. Given that "time" is a universal and representative concept, we examine LLMs' time preferences by varying only users' country and measuring the compensation LLMs deem appropriate for a 60-minute appointment delay. We then compare LLMs' responses with GDP per capita on Purchasing Power Parity (GDP_PPP), Mean Income, and a literature-ba...
  </details>

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


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 19 papers

- **2026-10-14** — Hanyao Guo, Mo Cui, Zihan Tan et al. — [ChemArgus: Automated Scientific Diagnostics for Lab-Grade Multimodal Chemistry Reasoning: A Frontier Benchmark](http://arxiv.org/abs/2610.20012v1)
  <details><summary>📄 Abstract</summary>
  Chemistry evaluation has moved past multiple-choice probes toward open-ended expert problems, yet the benchmarks that define the current frontier still score answer endpoints alone. Such scoring conflates memorized facts with stepwise derivation, treats visual and textual inputs as interchangeable, and confounds long-horizon planning with stepwise execution. These blind spots prevent any diagnosis of where the reasoning chain breaks in a model. We present ChemArgus, a competition-level chemistry...
  </details>

- **2026-10-14** — Guanhua Zhu, Bo Shen, Lei Zhang et al. — [EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs](http://arxiv.org/abs/2610.19381v1)
  <details><summary>📄 Abstract</summary>
  Different tasks often require interactive agents to perform similar operations at intermediate steps. Retrieving an entire past workflow can introduce irrelevant steps, whereas retrieving isolated operations can discard the dependencies needed to reuse them. We introduce EvoWeave, a framework for experience memory that represents abstract states as nodes and reusable operations as directed edges with input and output contracts, provenance, and capability references. A planner decomposes the curr...
  </details>

- **2026-10-14** — Simon Baur, Sumire Honda, Wojciech Samek et al. — [Argument Graph Uncertainty: Quantifying Uncertainty from the Logical Structure of Reasoning Chains](http://arxiv.org/abs/2610.20328v1)
  <details><summary>📄 Abstract</summary>
  Reliable uncertainty estimation is essential for deploying large language models in high-stakes reasoning tasks, yet most existing approaches rely on expensive sampling strategies or shallow token-level signals that ignore the internal logical structure of model outputs. We introduce Argument Graph Uncertainty, a post-hoc framework for multiple choice question tasks, that estimates model confidence directly from the logical structure of a single chain-of-thought reasoning trace. Our method uses ...
  </details>

- **2026-10-14** — Xinyi Cheng, Tianfu Zhang, Jiwen Li et al. — [CASI: Credit Assignment via Set Intervention for Agentic Retrieval](http://arxiv.org/abs/2610.20293v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate multiple retrieval actions jointly, while downstream systems often provide only one reward for the resulting set. Broadcasting this reward provides a valid score-function gradient estimator for the expected set-level objective, but does not determine a coalition-dependent within-set attribution. We introduce CASI (Credit Assignment via Set Intervention for Agentic Retrieval), which constructs the missing counterfactual information through snapshot-grou...
  </details>

- **2026-10-14** — Minghao Guo, Qingyue Jiao, Xiujin Liu et al. — [Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](http://arxiv.org/abs/2610.19366v1)
  <details><summary>📄 Abstract</summary>
  Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal data remains a significant challenge as they move toward long-horizon tasks and lifelong settings. Addressing this challenge requires effective memory mechanisms that can maintain continuity across ses...
  </details>

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

- **2026-10-12** — Chia-Ming Lee, Chia-Yu Lin, Hung-Kai Huang et al. — [Doctor Trigger: A Framework for Release-Bound Face Verification](http://arxiv.org/abs/2610.16336v2)
  <details><summary>📄 Abstract</summary>
  Face swapping and generative editing enable realistic facial manipulation, while online redistribution complicates publisher oversight of circulating face images. Existing approaches establish provenance, detect manipulation, recover embedded watermarks, verify image integrity, or disrupt unauthorized face manipulation. These capabilities do not necessarily establish consistency with a specific publisher-enrolled release, limiting the evidence available for verification and human review. To addr...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 1 papers

- **2026-10-13** — Bofan Xie, Chaokun Wang, Guanchen Ge et al. — [Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents](http://arxiv.org/abs/2610.18052v1)
  <details><summary>📄 Abstract</summary>
  Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval, and organization, so whether agents can forget at the user's explicit request remai...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-10-14** — Lingfei Qian, Yan Wang, Xueqing Peng et al. — [Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction](http://arxiv.org/abs/2610.19432v1)
  <details><summary>📄 Abstract</summary>
  Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same multilingual evidence. In particular, it remains unclear whether language models can recognize these concepts across languages and exhaustively recover their corresponding numerical evidence from the same contexts. We intro...
  </details>

- **2026-10-14** — Salima Lamsiyah, Adelaide Danilov, Oleksandr Marchenko Breneur et al. — [Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility](http://arxiv.org/abs/2610.20139v1)
  <details><summary>📄 Abstract</summary>
  Sparse autoencoders (SAEs) have emerged as a promising approach to mechanistic interpretability by decomposing language-model activations into sparse, potentially interpretable features. However, differences in design assumptions, evaluation objectives, and experimental settings complicate conclusions about their effectiveness. We present a critical survey of 138 studies on SAEs in natural language processing. Our contributions are fourfold: (1) we propose a task-grounded taxonomy connecting dic...
  </details>

- **2026-10-13** — Christoph Schwab, Josephine Westermann, Jakob Zech — [Operator Surrogates](http://arxiv.org/abs/2610.18210v1)
  <details><summary>📄 Abstract</summary>
  This chapter provides a mathematical introduction to operator surrogates, which are finite-parametric maps approximating complex (typically nonlinear) operators between infinite-dimensional (function) spaces.   A typical approach to constructing operator surrogates is the encoder-approximator-decoder paradigm, whereby infinite-dimensional inputs are mapped to a finite-dimensional latent space, processed, and then mapped back to the infinite-dimensional output space. We discuss various methods fo...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 188 papers

- **2026-10-14** — Xiaoli Xu, Zhengtao Wu, Zhengze Xu et al. — [CommerceGen-Studio: An End-to-End Framework for Commercial-Grade Main-Image Generation](http://arxiv.org/abs/2610.20603v1)
  <details><summary>📄 Abstract</summary>
  We present CommerceGen-Studio, an end-to-end framework for generating commercial-grade main images for e-commerce Stock Keeping Units (SKUs). Our framework is organized along a three-stage pipeline of information extraction, semantic rewriting, and multi-condition generation: Prompt-Eval-Refine-Loop Agent (PERL-Agent) distills heterogeneous SKU metadata into concise selling-point text lists through an iterative closed loop of VLM and LLM roles scored by a reference-free rubric. Layout Thinker Op...
  </details>

- **2026-10-14** — Delip Rao, Ahmed Muharram, Chris Callison-Burch — [Same Claim, Different Interpretations: How LLM Agents Resolve Ambiguity in Scientific Claims](http://arxiv.org/abs/2610.20457v1)
  <details><summary>📄 Abstract</summary>
  Co-scientists and agentic scientific claim verifiers are increasingly used to assess claims across the sciences. Natural-language scientific claims, written for human experts, are often underspecified and so admit several defensible interpretations. Such verifiers usually pick one, often tacitly, and benchmarks score their verdicts against expert labels without recording the expert's interpretation or the verifier's in a comparable form. This leads to disagreements with expert labels that cannot...
  </details>

- **2026-10-14** — Chih-Han Lin, Yu-Yun Chang, Po-Ya Angela Wang et al. — [Lexical Persistence Without Semantic Entrenchment in AI Agent Communities](http://arxiv.org/abs/2610.20365v1)
  <details><summary>📄 Abstract</summary>
  AI agent communities sustain lexical persistence, popular terms spread, recur, and achieve broad adoption, but whether they also develop the temporal semantic structure characteristic of human linguistic communities remains open. We compare MoltBook (AI agent community, 8 weeks), PTT (Chinese human BBS, 19 years), and Reddit (English human forum, in matched 8-week windows) using Compass-Aligned Distributional Embeddings (CADE), measuring semantic drift (B1), neighborhood stability (B2), and lag-...
  </details>

- **2026-10-14** — Yuyao Ge, Shenghua Liu, Peizhong Gao et al. — [Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](http://arxiv.org/abs/2610.20344v1)
  <details><summary>📄 Abstract</summary>
  Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed harness, leaving harness engineering itself unexplored. We propose Doc2Harness, a two-stage benchmark that evaluates long-horizon harness engineering directly. In Stage 1, a build model operating inside ...
  </details>

- **2026-10-14** — Danyang Zhao, Sendong Zhao, Yanrui Du et al. — [Taking the PULSE of Medical Reasoning: Step-Level Retrieval Timing for Knowledge-Grounded Inference](http://arxiv.org/abs/2610.20292v1)
  <details><summary>📄 Abstract</summary>
  Reliable medical reasoning requires LLMs to dynamically access external biomedical evidence to improve factual trustworthiness and reasoning accuracy. However, indiscriminate retrieval can introduce noise and latency, raising a critical retrieval-timing problem: at each reasoning step, the system must decide whether the model's internal knowledge is reliable or external evidence is needed. We propose PUlSE, a lightweight probing method that uses the model's internal representations as intrinsic ...
  </details>

- **2026-10-14** — Junze Zhu, Weihao Chen, Zhiyang Zhou et al. — [Harness Policy Distillation: Aligning Agent Policies with Runtime Semantics](http://arxiv.org/abs/2610.20261v1)
  <details><summary>📄 Abstract</summary>
  Deploying a general-purpose model as an agent means running it inside a product-specific runtime harness that decides which actions are executable, how state advances, and when the loop may terminate. Ordinary trajectory supervision shows which action was taken but leaves the runtime semantics behind that action implicit. We introduce Harness Policy Distillation (HPD), which makes these runtime control semantics an explicit training target alongside actions to align the harness policy. HPD repla...
  </details>

- **2026-10-14** — Cédric Rousseau, Javier González-Colsa, Victor Joris et al. — [From Single-Particle Thermal Asymmetry to Collective Control: Janus Plasmonic Colloids for Photothermal Applications](http://arxiv.org/abs/2610.20189v1)
  <details><summary>📄 Abstract</summary>
  Janus nanoheaters provide a route to break the spatial symmetry of thermoplasmonic heating and generate directionally biased thermal gradients at the nanoscale. However, in realistic photothermal scenarios, nanoheaters rarely act as isolated objects, but rather operate within colloidal assemblies where collective thermal and electromagnetic effects reshape the local temperature landscape. Here, we investigate how the intrinsic thermal asymmetry of a single Janus plasmonic nanoheater is transform...
  </details>

- **2026-10-14** — Shijun Shi, Zhe Liu, Zhi Hou et al. — [Atomic-WAM: Execution-Grounded Atomic-Motion Reasoning for World Action Models](http://arxiv.org/abs/2610.20157v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) typically adapt video foundation models to robotic control through joint video and action prediction. However, task-level instructions may leave the next physical interaction underspecified, requiring semantic grounding and state-dependent motion selection. To this end, we introduce Atomic-WAM, an understand-then-execute framework that connects task reasoning to action generation through atomic-motion descriptions. Specifically, a vision-language reasoner describes the...
  </details>

- **2026-10-14** — Cezar Sas, Sandra Mitrović, Fabio Barth et al. — [The Code of Theseus: Can Agents Rebuild Software from Recovered Design Documents?](http://arxiv.org/abs/2610.20068v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly design a system before implementing it, yet the data to train and evaluate them centres on implementation and testing: requirements and design artefacts are often missing, outdated or private. Source code, in contrast, is abundant. Prior work recovers architecture documentation by feeding LLMs the source code or letting agents explore it, which saturates the context, does not scale to many repositories, and yields a single artefact rather than aligned ones.   We present a...
  </details>

- **2026-10-14** — Maosheng Qin, Qi Zhang, Mingxuan Xia et al. — [Memorizing Who, Knowing How: Benchmarking Personal and Procedural Memory for Persistent Assistants](http://arxiv.org/abs/2610.20022v1)
  <details><summary>📄 Abstract</summary>
  Memory systems for persistent personal agents must move beyond isolated memories, maintaining both personal memory about whom they serve and procedural memory about how to act. Crucially, in harness-based personal assistance, procedures or skills are inherently user-conditioned: personal context determines which procedures apply, how they are instantiated, and when they should change. Existing benchmarks typically emphasize either personal or procedural memory, leaving their interaction underexp...
  </details>

- **2026-10-14** — Mario Mallea, Angela Nebot, Franscisco Mugica — [Empirical Boundaries of Reservoir Computing for Few-Shot Sequence Pattern Tasks](http://arxiv.org/abs/2610.19997v1)
  <details><summary>📄 Abstract</summary>
  Efficient sequence modeling remains a fundamental challenge in machine learning. Despite the success of Transformers, recurrent neural networks (RNNs) have recently re-emerged as efficient alternatives. Particularly, Echo State Networks (ESNs) offer a compelling framework of randomized RNNs that have been extensively studied for time-series forecasting and dynamical systems. This paper presents an empirical analysis of distributional, architectural, and optimization variants of ESNs evaluated on...
  </details>

- **2026-10-14** — Sifan Yang, Hongyi Tao, Dingzhi Yu et al. — [Memory-Efficient Subspace Optimization with Residual Correction: From Momentum SGD to Muon](http://arxiv.org/abs/2610.19844v1)
  <details><summary>📄 Abstract</summary>
  Memory-efficient subspace optimization has emerged as a practical approach to reducing the memory cost of LLM training while preserving optimization performance. Previous algorithms typically rely on the leading singular subspace of stochastic gradients, yet the gradient noise may dominate the subspace in later training stages and can prevent convergence. To overcome this limitation, we adopt a residual correction framework, which maintains the optimizer states in the subspace and adds the ortho...
  </details>

- **2026-10-14** — Soundouss Messoudi, Youness Mansar — [Calibration and Risk-Budgeted Decisions with System One Models](http://arxiv.org/abs/2610.19811v1)
  <details><summary>📄 Abstract</summary>
  LLM workflows and agents rely on a set of binary decisions like allow/block an input, or discard/retain a retrieved document. When human deferral is unavailable, uncertain cases must still receive an action. We study System One decision scores in this setting by defaulting to a conservative fallback when uncertain, and controlling the false omission risk within the subset of inputs assigned the utility-maximizing action. Across six datasets covering moderation, safety, and reranking, we compare ...
  </details>

- **2026-10-14** — Panagiotis Kasnesis, Lazaros Toumanidis, Christos Chatzigeorgiou et al. — [One Agent per Zone: Decentralised Active Inference under Partial Observability for Multi-Zone HVAC Control on Edge Hardware](http://arxiv.org/abs/2610.19790v1)
  <details><summary>📄 Abstract</summary>
  Multi-zone HVAC control is a shared-resource problem: zones on a floor share one fan and cooling coil, so each zone's demand affects its neighbours and the building's peak power. One controller per zone scales well and isolates faults, but each controller then observes only its own zone, not the shared air loop. In this work, we present a decentralised controller that assigns each zone an independent active-inference agent, which plans by minimising expected free energy and learns its zone dynam...
  </details>

- **2026-10-14** — Ziyang Ling, Shuyu Lu, Ziyi Chen — [PRISMATIC : Prescription Risk Inspection System for Multi-Agent Treatment Interaction in Clinical Decision-Making](http://arxiv.org/abs/2610.19762v1)
  <details><summary>📄 Abstract</summary>
  Medical prescribing errors for multimorbid patients, who require complex drug regimens, are a major patient safety concern. These errors often stem from fragmented decision-making across medical specialties, a critical coordination failure that leads to adverse drug events and rehospitalizations. To address this coordination challenge, we introduce PRISMATIC, a multi-agent architecture where specialized agents, each representing a workflow role, collaboratively generate and refine treatment plan...
  </details>

- **2026-10-14** — Qi Chen, Yuwei Wu, Quan Chen et al. — [One-shot Human Video-Guided Adaptation for Vision-Language-Action Models](http://arxiv.org/abs/2610.19746v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action (VLA) models have recently achieved remarkable progress by leveraging large-scale robot datasets and foundation models for general-purpose robot manipulation. However, their ability to rapidly adapt to novel manipulation tasks beyond the training distribution remains limited. Existing approaches often require task-specific robot demonstrations and additional training, which are labor- and compute-intensive, limiting the scalability of VLA adaptation to open-world scenarios...
  </details>

- **2026-10-14** — Nir Yarden, Amit Ben-Artzy, Roy Schwartz — [Beyond State Capacity: Why Retrieval Breaks in Mamba](http://arxiv.org/abs/2610.19709v1)
  <details><summary>📄 Abstract</summary>
  Mamba models underperform Transformers on in-context retrieval. This gap is usually attributed to Mamba's fixed-size recurrent state, which loses information as the context grows. We challenge this assumption by focusing on query-first retrieval, a setup in which the query precedes the context and state capacity should not be the binding constraint. We show that even in this setting Mamba lags substantially behind Transformers, despite its selection mechanism, which was designed to distinguish r...
  </details>

- **2026-10-14** — Bolin Zhang, Xuechao Wang — [Effective-Balance Design in Ethereum Proof-of-Stake](http://arxiv.org/abs/2610.19699v1)
  <details><summary>📄 Abstract</summary>
  Proof-of-Stake (PoS) systems offer a scalable and energy-efficient alternative to Proof-of-Work (PoW). The economic security of PoS relies critically on incentivizing broad and meaningful participation through well-cali\-brated staking reward mechanisms. We study Ethe\-reum's effective-balance rules as a mechanism-design problem in which the protocol chooses a reward coefficient, an activation threshold, and a maximum effective balance, and validators respond in the induced propor\-tional-alloca...
  </details>

- **2026-10-14** — Vaishak Prasad, Prayush Kumar, Michael Boyle et al. — [A catalog of long, eccentric and precessing binary black hole simulations from ICTS-TIFR](http://arxiv.org/abs/2610.19688v1)
  <details><summary>📄 Abstract</summary>
  We present a catalogue of 31 binary black hole simulations performed with the Spectral Einstein Code (SpEC) on the Sonic cluster at ICTS-TIFR, Bengaluru between August 2023 and December 2024, targeting the sparsely covered corner of parameter space in which orbital eccentricity and spin-orbit precession are present simultaneously: 17 configurations are both eccentric and precessing, spanning mass ratios $1 \le q \le 11$ and initial eccentricities up to $\hat{e}_0 = 0.40$. The longest, EccPrecDif...
  </details>

- **2026-10-14** — Soumick Sarker, Mengmi Zhang — [Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry](http://arxiv.org/abs/2610.19674v1)
  <details><summary>📄 Abstract</summary>
  Geometry foundation models estimate camera poses and 3D scene structure from video sequences, but maintaining consistent reconstructions over long horizons remains challenging. Feed-forward models process long sequences as independent, fixed-length frame windows and align their predictions, causing pose and reconstruction errors to accumulate across windows. Streaming models retain information from past frames to inform future predictions, but cannot revise earlier estimates when later observati...
  </details>

- **2026-10-14** — Xiaocong Yang, Xuanyu Meng, Yuji Zhang et al. — [Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching](http://arxiv.org/abs/2610.19636v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic models are bottlenecked by the scope of the symbol component and usually domain-specif...
  </details>

- **2026-10-14** — Ziyi Liang, Zichuan Li, Bin Yuan et al. — [Mission (Im)Possible: Towards Autonomous Discovery of Autopilot Logic Flaws in Open-Source Drone Frameworks](http://arxiv.org/abs/2610.19566v1)
  <details><summary>📄 Abstract</summary>
  Autonomous drones are increasingly deployed in safety-critical tasks, yet their autopilot software can still contain subtle logic flaws that lead to unsafe behaviors. These flaws are difficult to discover with existing techniques because they often depend on semantic relationships across modules, commands, and runtime state, and rarely manifest as crashes or detectable failures. With recent advances in LLMs, we observe that, when equipped with essential domain knowledge and carefully crafted con...
  </details>

- **2026-10-14** — Yining Tang, Junyu Zhang, Haomiao Qiu et al. — [GraphRAG-LTM: A Layered Threat Modeling Framework for Attacks on Graph Retrieval-Augmented Generation](http://arxiv.org/abs/2610.19549v1)
  <details><summary>📄 Abstract</summary>
  Graph retrieval-augmented generation (GraphRAG) uses document-derived knowledge graphs to assemble evidence for large language model (LLM) answers. Its security depends on both the seed chunks retrieved for a query and the graph evidence assembled from them, yet attacks on this evidence path remain underexplored. We introduce GraphRAG-LTM, a Layered Threat Modeling framework that tests three nested levels of attacker access. BB Query uses ranking feedback to make query edits under a semantic-sim...
  </details>

- **2026-10-14** — Shijun Li, Yang Liu, Najmeh Sadoughi et al. — [Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for Selective Retrieval-Augmented Machine Translation](http://arxiv.org/abs/2610.19528v1)
  <details><summary>📄 Abstract</summary>
  Retrieving external knowledge can improve large language model (LLM) translation by providing supplementary information such as idiom interpretations and terminology. However, existing retrieval-augmented machine translation systems typically apply predefined retrieval strategies uniformly across all inputs. We argue that translation operates in a partial-evidence regime: LLM's parametric knowledge suffices for many inputs, while external evidence benefits a subset and usually supports rather th...
  </details>

- **2026-10-14** — Yunze Liu, Jing Wang, Shenrui Wu et al. — [Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](http://arxiv.org/abs/2610.19495v1)
  <details><summary>📄 Abstract</summary>
  Retrieving useful context for a robot requires matching its task, execution stage, and the continuation that should follow. We introduce Robota-Embed, to our knowledge the first vision-language-action (VLA) embedding model to jointly encode all three modalities in both current-state queries and recorded future continuations. Predictive retrieval training aligns these endpoints, enabling historical continuations to serve as context at inference time. We construct a multi-source corpus of 1,695,68...
  </details>

- **2026-10-14** — Akshay Malhotra, Nicolas Zilberstein, Shahab Hamidi-Rad — [Train to Stitch: Topology-Preserving Regularization for Interoperable Representations](http://arxiv.org/abs/2610.19401v1)
  <details><summary>📄 Abstract</summary>
  As large, powerful pre-trained models become more prevalent, there is growing interest in developing methods that allow different neural networks to be seamlessly combined with little or no direct communication between them. Take autoencoder-based data compression as an example: the ability to independently choose architectures and train encoder and decoder models, while still ensuring they work together, could fundamentally transform how such models are built, deployed, and updated. In this wor...
  </details>

- **2026-10-14** — Miaobo Hu, Shuhao Hu, Xiaobo Guo et al. — [ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps](http://arxiv.org/abs/2610.20532v1)
  <details><summary>📄 Abstract</summary>
  A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs, and a frozen execution trace, and treat it as decision-certifiable active evidence acquisition. A Counterfactual Evidence Interaction Graph (CEIG) represents unary evidence value, signed second-order interaction, and d...
  </details>

- **2026-10-14** — Xiaoman Li, Zhiqiang Yang, Jiayu Hu et al. — [Graph-Reweighted Behavior Cloning with Human Interventions for Precise Robotic Manipulation](http://arxiv.org/abs/2610.20504v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon precise manipulation produces mixed-quality data for post-training vision-language-action (VLA) models: even successful demonstrations and intervention-assisted rollouts may contain detours, hesitations, failed attempts, and imperfect recoveries. The key challenge is to identify which action chunks actually advance the task, rather than uniformly cloning or discarding imperfect trajectories. We propose Graph-Reweighted Behavior Cloning (GR-BC), an offline iterative post-training fra...
  </details>

- **2026-10-14** — Pol Rodríguez Farrés, Jesus Cerquides — [Contagious Misinterpretations: Social Learning with Shared Interpretations](http://arxiv.org/abs/2610.20381v1)
  <details><summary>📄 Abstract</summary>
  When people discuss which of several hypotheses is true, they share not only their beliefs but also their interpretation of each one, that is, the distribution of signals each hypothesis is expected to produce. This interpretation is an opinion about what each hypothesis means and what evidence it predicts, and it is revised only through conversation, not by confronting it with the observed data. Standard non-Bayesian social learning captures only belief-sharing and keeps the likelihoods private...
  </details>

- **2026-10-14** — Davide Baldelli, Robyn Kozierok, Mirko Bronzi et al. — [Cross-Model In-Context Neurofeedback Reveals (Limited) Activation Control in LLMs](http://arxiv.org/abs/2610.20179v1)
  <details><summary>📄 Abstract</summary>
  Probes on activation vectors are widely used to detect misbehavior in language models, but their success relies on the assumption that models cannot control what their activations encode. Humans can learn, through neurofeedback, to control the firing of even single neurons, and recent studies investigated whether this ability extends to language models, reaching conflicting conclusions. No experimental design so far disentangles competence at the task from genuine access to one's own activations...
  </details>

- **2026-10-14** — Hanlin Liu, Zichen Zhou, Jiacheng Zhang et al. — [Refine Actions If Needed: Adaptive Action Chunk Refinement for Robot Manipulation](http://arxiv.org/abs/2610.19765v1)
  <details><summary>📄 Abstract</summary>
  Computationally lightweight manipulation policies predict executable actions with low inference latency, but prediction errors can limit task success. Iterative generative policies can achieve higher task success rates, but repeated network evaluations increase inference latency. Refining action proposals from computationally lightweight policies can combine these strengths, but the amount of refinement needed varies across states. We introduce RAIN (Refine Actions If Needed), a framework that p...
  </details>

- **2026-10-14** —  XGEN Team, Guohao Cai, Haoxuan Che et al. — [Generative World Simulation with DAO and JING](http://arxiv.org/abs/2610.19726v1)
  <details><summary>📄 Abstract</summary>
  We present a Generative World Simulation framework that couples persistent shared world state with continuous first-person audiovisual generation. The framework integrates DAO, a computable world engine, and JING, an Egocentric Interactive Experience Model, to support sustained interaction for humans and agents. DAO maintains the states of characters, objects, and spaces and their relationships, advancing the world according to interaction rules and world time while preserving the consequences o...
  </details>

- **2026-10-14** — Zixuan Wang, Jia-Ning Li, Yinzhou Tang et al. — [Cracking Mobile Manipulation: From Failure Diagnosis to Agentic Robot System](http://arxiv.org/abs/2610.19600v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-language-action (VLA) models have shown strong performance on local robot manipulation, yet their success does not readily translate to long-horizon mobile manipulation. In our experiments, a pretrained subtask VLA achieves 80% success rate on atomic manipulation tasks but only 19% when these skills are composed into mobile manipulation. We argue that this gap stems from failures across the execution process rather than from local manipulation capability alone. To uncover these bot...
  </details>

- **2026-10-14** — Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair et al. — [L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](http://arxiv.org/abs/2610.19591v1)
  <details><summary>📄 Abstract</summary>
  The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work for, and increasingly through code the agents write themselves. Whether that work compounds is enabled by the harness around it, and the harness faces a constraint the model does not: of the three participants in such a ...
  </details>

- **2026-10-14** — Mingyu Ouyang, Yiran Wang, Siyuan Hu et al. — [Player-1: Learning to Play from Synthetic Experience](http://arxiv.org/abs/2610.20584v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable environments for interactive training remain difficult to obtain. We introduce Pla...
  </details>

- **2026-10-14** — Saatvik Kher, Hyungrok Do, Judy Zhong et al. — [Bayesian Learning to Select Fair Classifiers](http://arxiv.org/abs/2610.20514v1)
  <details><summary>📄 Abstract</summary>
  Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as examples arrive and update policies as outcomes are observed. We study the problem of selecting, in an online stream, the agent that best balances (i) predictive performance and (ii) subgroup fairness of a sensitive attrib...
  </details>

- **2026-10-14** — Harsh Kumar — [Lost in Translation: Why Lower Bias Scores Don't Mean Fairer Models](http://arxiv.org/abs/2610.20479v1)
  <details><summary>📄 Abstract</summary>
  Bias audits of multilingual language models usually compare a model's average stereotype score in English with its average in another language and read the difference as a difference in fairness. We ask how much of that difference is noise. Auditing ten open models in eight languages, we measure how far scores move when English test items are merely reworded, test every language shift item by item, and check that the test catches shifts we inject on purpose. In all 70 model-language pairs the st...
  </details>

- **2026-10-14** — Peidong Wang, Ying Chang, Zhiming Ma et al. — [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.20474v1)
  <details><summary>📄 Abstract</summary>
  Pretrained vision-language-action models (VLAs) often fail midway through unseen long-horizon tasks. Recursive self-improvement (RSI) offers a remedy, but embodied RSI methods either refine the harness around a frozen executor and so cannot add a missing motion, or train the executor on persistent failures without asking whether a failure lies in how the executor is called or in what it can do. We ask when a self-improving embodied system should change the weights of its executor, and propose Ad...
  </details>

- **2026-10-14** — Fazle Mohammed Tasfiq, Sabab Attin, Sheikh Md. Tahmid Hossain et al. — [Analyzing performance of Retrieval Augmented Generation models for Question Answering Tasks](http://arxiv.org/abs/2610.20419v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) models have become almost a cornerstone of open-domain question answering tasks; in which the quality of answers generated in the process, greatly relies on the effectiveness of retrieval mechanisms. In the realm of LLM, the last two years have seen tremendous progress in RAG architectures, with many models reporting to have improved performance through various design innovations. The cultural question and answering systems of South Asia, in particular, prese...
  </details>

- **2026-10-14** — Kaifei Wang, Zikang Shan, Liwei Wang et al. — [When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?](http://arxiv.org/abs/2610.20413v1)
  <details><summary>📄 Abstract</summary>
  Momentum is a classical tool for accelerating convex optimization and a standard component of modern large language model training. Yet recent empirical work has questioned the usefulness of first-moment momentum in reinforcement learning with verifiable rewards (RLVR). We study this question through a bandit formulation of RLVR with bias-corrected exponential moving average (EMA) momentum, where the EMA coefficient $β$ controls how quickly the weights on past gradients decay. When policy gradie...
  </details>

- **2026-10-14** — Andrea Abrardo, Andrea Garulli — [To Stack or Not to Stack? Jacobian Conditioning and the Benefits of Depth in Metasurface-Based Linear Transformation Synthesis](http://arxiv.org/abs/2610.20377v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates when and why stacking programmable metasurfaces into Stacked Intelligent Metasurfaces (SIMs) improves linear transformation synthesis at a fixed phase-control budget. The analysis shows that algebraic Jacobian rank alone is insufficient to characterize practical synthesis, which also depends on the strength and balance of the sensitivity directions generated by the available controls. A layer-resolved analysis of the cascade model explains how inter-layer propagation can ...
  </details>

- **2026-10-14** — Yaomengxi Han, Debarghya Ghoshdastidar — [Training Dynamics of Transformers on Unbounded Inputs: Attention Learning Can Lag Output Layer Learning](http://arxiv.org/abs/2610.20337v1)
  <details><summary>📄 Abstract</summary>
  The success of transformers is attributed to several factors, including their capacity to express formal languages over variable-length inputs, and ability of the attention mechanism to focus on relevant input features. However, there is limited understanding of the training dynamics of shallow transformers, specifically how to decouple the learning of the attention and the output (feedforward) layer. A natural extension of the theory of one-step gradient feature learning in feedforward networks...
  </details>

- **2026-10-14** — Junyi Zou, Avrova Donz — [MMLA-RSI: Recursive Self-Improvement through RTT and RTMA](http://arxiv.org/abs/2610.20294v1)
  <details><summary>📄 Abstract</summary>
  An agent can improve its behavior within an unresolved problem by changing how it acts and which experience it retains. We propose MMLA-RSI, a recursive self-improvement scheme with two implementations in Memory-Mediated Learning Architecture: Reasoning-Time Training (RTT) changes the policy state $Φ$, while Reasoning-Time Memory Adaptation (RTMA) changes authoritative memory $M$. Each route also makes its adaptation method an object of improvement. A current numerical updater trains the policy ...
  </details>

- **2026-10-14** — Steffen Holter, Rita Sevastjanova, Michaela Benk et al. — [Let Me Clarify: Interactive Modeling of Soft Attributes](http://arxiv.org/abs/2610.20227v1)
  <details><summary>📄 Abstract</summary>
  People commonly express preferences through soft attributes such as is interesting,'' which are difficult to operationalize for computational preference modeling. Latent representations can obscure how such attributes are interpreted, limiting transparency and user control. We formalize softness as the diversity of valid interpretations a description permits and provide empirical support for this characterization. Our proposed measure estimates softness to guide clarification and determine when ...
  </details>

- **2026-10-14** — Isabel Jones, Matthew Edwards, Janina A. Hoffmann — [Drivers of LLM Consensus Formation Under Competing Incentives: A Simulation Study](http://arxiv.org/abs/2610.20200v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in multi-agent environments that produce unanimous agreement, both in intended interactions that need coordination and in unintended emergent interactions. Consequently, understanding how LLMs with competing incentives reach consensus is crucial to better interpret and design LLM collectives. We introduce an evaluation, based on the Network Consensus game, to assess the mechanisms driving this process. Here, a network of agents must agree on...
  </details>

- **2026-10-14** — Xinxuan Lv, Minghan Li, Guodong Zhou — [XViewRank: Overlap-Conditioned Score Fusion for LLM-Augmented Sparse Retrieval](http://arxiv.org/abs/2610.20122v1)
  <details><summary>📄 Abstract</summary>
  Large language models can reduce vocabulary mismatch in sparse retrieval by generating alternative views of a query. Once these views are searched independently, however, their ranked lists may be complementary, redundant, or affected by query drift, making fixed fusion suboptimal. We present XViewRank, a lightweight retrieval-side method for conditionally fusing BM25 results from an original query, a hypothesis view, and a step-back view. For each pooled candidate, XViewRank retains three norma...
  </details>

- **2026-10-14** — Mengke Zhang, Yanda Shao, Tianhe Wu et al. — [ACR-Net: Mitigating Semantic Dominance via Contrastive Acoustic-Semantic Decoupling](http://arxiv.org/abs/2610.20114v1)
  <details><summary>📄 Abstract</summary>
  Speech Emotion Recognition (SER) models and Audio LLMs fail when vocal tone contradicts textual semantics. Extensive training on congruent data engenders a rigid semantic prior, causing "Semantic Dominance", a severe text bias during cross-modal conflicts. We introduce the ASPIRE benchmark of adversarial audio-text pairs across four conflict types, alongside two metrics: Semantic Overconfidence Penalty (SOP) and Latent Decoupling Degree (LDD). Unlike fusion methods that merely re-weight collapse...
  </details>

- **2026-10-14** — Yunhao Wang, Feng Zhang, Tinghao Yu et al. — [AFCS: Atomic-Fact-Conditioned Synthesis for Factual Knowledge Pretraining](http://arxiv.org/abs/2610.20086v1)
  <details><summary>📄 Abstract</summary>
  Synthetic data is increasingly used in language-model pretraining. Existing knowledge-corpus synthesis pipelines, including WRAP and Nemotron-CC, usually take a source passage or document segment as input and generate rewritten or QA-style samples from that text. This can improve surface form and prompt diversity, but it does not explicitly require fine-grained source facts -- especially secondary entities, list/table entries, and precise temporal attributes -- to appear in the synthesized corpu...
  </details>

- **2026-10-14** — Yi Wang, Tianzi Wang, Tong Lei et al. — [Designing Textual Interfaces To Enhance Llm Reasoning On Audio-Visual Question Answering](http://arxiv.org/abs/2610.20085v1)
  <details><summary>📄 Abstract</summary>
  Automatic prompt optimization (APO) has shown strong effectiveness for text-based LLMs and LLM systems, but its application to audio-visual understanding systems requires suitable textual interfaces through which multimodal reasoning can be exposed to text-based optimizers. We investigate how the design of textual interfaces affects prompt optimization for multimodal reasoning, on the audio-visual question answering task. We compare three interface designs, including a direct inference system co...
  </details>

- **2026-10-14** — Lakshmi Rajendram Bashyam, Ralf Krestel — [Reading the Neighborhood: Text-Attentive Graph Reranking for Automated Subject Indexing](http://arxiv.org/abs/2610.20048v1)
  <details><summary>📄 Abstract</summary>
  Subject indexing assigns descriptors from a controlled vocabulary to bibliographic records, a task characterized by thousands of labels, few positive examples per label, and a long tail of rarely used descriptors. Existing extreme multi-label classifiers treat the vocabulary as a flat list, ignoring the semantic relations that thesauri encode. We present TAGHN, a heterogeneous graph reranker over a per-document subgraph of retrieved candidates augmented with the thesaurus neighborhood. The relev...
  </details>

- **2026-10-14** — Timo Klein, Thomas Lang, Andrii Shkabrii et al. — [Outperforming 1000 Euclidean Layers With Hyperbolic Goal-Conditioned RL](http://arxiv.org/abs/2610.20009v1)
  <details><summary>📄 Abstract</summary>
  Scaling self-supervised contrastive reinforcement learning (CRL) to 1000-layer Euclidean neural networks has enabled state-of-the-art goal-reaching performance, yet wall-clock time scales linearly with depth. We find that changing the geometry achieves stronger performance with far shallower networks. This matters in complex navigation environments, where walls can make route distance deviate substantially from Euclidean distance. In a U-shaped maze, we show that the longer the route, the more i...
  </details>

- **2026-10-14** — Jithin Cheriyan, Bastin Tony Roy Savarimuthu, Stephen Cranefield — [Taming the Online Software Engineering Tongue: Detecting and Reducing Offensive Language in Software Communities](http://arxiv.org/abs/2610.19961v1)
  <details><summary>📄 Abstract</summary>
  Online Software Engineering (SE) communities such as Stack Overflow have become unwelcoming and hostile spaces, as evidenced by the presence of rude and offensive comments that are detrimental to the emotional wellbeing of participants. The main objective of this work is to investigate the prevalence and nature of offensive language in online SE communities, and develop approaches to classify them with the ultimate goal of reducing offensive language by proposing an Offensive Language Reduction ...
  </details>

- **2026-10-14** — Anton Korznikov, Alexey Dontsov, Elena Tutubalina — [Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability](http://arxiv.org/abs/2610.19907v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability aims to decompose neural network computations into human-understandable features, yet progress is limited by the absence of ground-truth units to evaluate against. We address this with a Sparse Transformer (ST): a 5-layer language model trained on TinyStories whose wide, TopK-sparse MLP forces neuron specialization. We show that ST neurons are highly interpretable: they outperform a loss-matched dense transformer by 43% on AutoInterp, and circuits of a median of 12 n...
  </details>

- **2026-10-14** — Fiorenzo Parascandolo, Enver Sangineto, Xiaoyi Yu et al. — [Frustratingly Easy Majority Voting Using Length Conditioning](http://arxiv.org/abs/2610.19890v1)
  <details><summary>📄 Abstract</summary>
  Majority Voting (MV) is a simple and widely used strategy which improves the reasoning accuracy of Large Language Models (LLMs) by allocating additional inference-time computation. Specifically, in MV multiple Chain-of-Thoughts (CoTs) are independently sampled and the most frequent final answer is selected. In this work, we propose Length-Conditioned Majority Voting (LCMV), a Test-Time Training approach which improves MV leveraging an empirical observation that has recently been established in s...
  </details>

- **2026-10-14** — Robin Uhrich, Marco Bagatella, Núria Armengol Urpí et al. — [Occupancy Modeling via Drifting: One-Step Generation Enables Direct Policy Extraction](http://arxiv.org/abs/2610.19883v1)
  <details><summary>📄 Abstract</summary>
  The growing interest in behavior foundation models, combined with recent advancements in generative modeling, has led to an appealing recipe for reinforcement learning from unlabeled data: pre-train a generative model to model occupancies, i.e., discounted state visitations, on reward-free trajectories, such that a policy can be easily extracted once a small reward-labeled dataset becomes available. We decompose this recipe along three axes: (i) the degree to which the multi-modal structure of o...
  </details>

- **2026-10-14** — Shanyan Guan, Shiyu Li, Xin Li et al. — [BluePixel: Toward Native 4K Agentic Image Editing](http://arxiv.org/abs/2610.19882v1)
  <details><summary>📄 Abstract</summary>
  Instruction-driven image editing has reached native 4K, yet how such editors are trained remains undisclosed, and pretraining one from scratch is beyond most teams. The task itself compounds the difficulty: a single end-to-end editor cannot make precise parametric adjustments, match specialized experts, or interpret the vague instructions users actually write. We argue that 4K editing is a system problem rather than a single-model problem, and present BluePixel, which couples a native-4K editing...
  </details>

- **2026-10-14** — Giacomo Aletti, Enea G. Bongiorno — [Principal Component Analysis for Zero-Inflated Probability Measures via Lorenz Curves](http://arxiv.org/abs/2610.19874v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a principal component analysis framework for probability measures associated with non-negative real-valued random variables with structural zeros. Specifically, leveraging the associated Lorenz Curve (LC) and a suitable perspective transformation of the plane, a bijective embedding is defined to treat such measures as functional data in a Hilbert space. Once the random LC is embedded in this space, standard Functional Principal Component Analysis (FPCA) becomes directly appli...
  </details>

- **2026-10-14** — Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang et al. — [OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](http://arxiv.org/abs/2610.19848v1)
  <details><summary>📄 Abstract</summary>
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as open data by the Ministry of Examination; answer keys agree across 31,312 duplicated question groups at 99.91%, with all 27 disagreements accounted for. A reviewed second pass withdrew 2,180 items whose stems depend on ...
  </details>

- **2026-10-14** — Linhao Zhong, Bozhen Fang, Xuehao Wang et al. — [More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning](http://arxiv.org/abs/2610.19789v1)
  <details><summary>📄 Abstract</summary>
  Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to training stability and computational cost. These limitations obscure the source of reported gains and the practical strengths and weaknesses of competing methods. Costly agent training further motivates a ...
  </details>

- **2026-10-14** — Yuming Zhao, Zezeng Li, Weimin Wang et al. — [Q-MAGIC: Quad-only Mesh Autoregressive Generation via Singularity-Aware Circular Relative Offset Tokenization](http://arxiv.org/abs/2610.19777v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive models have proven effective for triangular mesh generation by transforming it into predicting the next face, converting the non-differentiable connectivity prediction into a sequence of token predictions. However, generating quad-only meshes remains challenging because quad faces impose stricter topological constraints than triangles. The model must not only serialize quad faces into a valid token sequence, but also support unambiguous connectivity reconstruction during de-serial...
  </details>

- **2026-10-14** — Minghan Li, Guodong Zhou — [Does the Linguistic Register of Thinking Matter? Wenyan as a Compact Reasoning Register for Chinese LLMs](http://arxiv.org/abs/2610.19741v1)
  <details><summary>📄 Abstract</summary>
  Visible reasoning traces of Chinese reasoning-oriented LLMs are typically written in modern vernacular Chinese, which may be verbose under limited decoding budgets. We ask whether the linguistic register of reasoning can be used to improve efficiency. We propose Wenyan Thinking, which emits intermediate reasoning in Classical Chinese (wenyanwen) while retaining a short direct-answer output. Starting from modern-Chinese reasoning traces, we rewrite only the reasoning field into wenyan and fine-tu...
  </details>

- **2026-10-14** — Shun Inadumi, Lee Sangmyeong, Koichiro Yoshino — [Recognizing Dialogue Ambiguity via Candidate Set Visual Grounding](http://arxiv.org/abs/2610.19723v1)
  <details><summary>📄 Abstract</summary>
  Interpreting an ambiguous utterance in real-world interactions often requires context beyond a single utterance. When the utterance refers to objects in a visual scene, it is necessary to maintain and update the set of plausible referents as context accumulates, without assuming that the available information identifies a unique object. However, prior work on interactive visual grounding, which localizes objects referred to by linguistic expressions, has focused on identifying a unique object on...
  </details>

- **2026-10-14** — Xin Li, Mengbing Liu, Hao Jiang et al. — [Share the Symbol, Not the Vector: Training-Free Fact Communication Across Language Models](http://arxiv.org/abs/2610.19696v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems allow language models to solve tasks collaboratively by sharing complementary information. These systems typically communicate through text, while recent approaches also explore exchanging internal model states. However, sharing these states across architectures often requires learned translators or assumptions about model compatibility. We introduce SYNC (Symbol-Indexed Neural Communication), a word-indexed interface that connects heterogeneous models without fine-tuning or ...
  </details>

- **2026-10-14** — Yilin Jiang, Fei Tan, Xuanyu Yin et al. — [Measuring and Reducing Unusable Replies of LLM Agents](http://arxiv.org/abs/2610.19659v1)
  <details><summary>📄 Abstract</summary>
  People delegate multi-step work to LLM agents and read only the reply that the agent hands back. Current evaluation scores task completion and the faithfulness of reports, and it leaves open whether the requester can understand and use the reply. We call this property reply usability and measure it with a reader model that takes the requester's position and tests whether the reply can be interpreted from what the requester has seen, is in the requester's language and answers the request. Its agr...
  </details>

- **2026-10-14** — Yiliu Xu, Xinjin Li, Yu Ma — [What Breaks in Multi-Image Schema Application? Factorial Oracle Interventions Reveal an Instance-Information Bottleneck](http://arxiv.org/abs/2610.19611v1)
  <details><summary>📄 Abstract</summary>
  Modern vision-language models can accept multi-image contexts, but aggregate accuracy rarely reveals where a multi-image reasoning pipeline fails. We study a controlled schema-application task in which a model must locate two target characters in a 16-image sequence, identify their visual attributes, consult an item-specific visual codebook, and compose two ordered nonce code names. We introduce a within-item 2-by-2 factorial Oracle design: Oracle-A supplies a verified textual schema, Oracle-B s...
  </details>

- **2026-10-14** — Xinjie Lan, Yunbo Mei, Leheng Zhou et al. — [Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting](http://arxiv.org/abs/2610.19603v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated strong performance in long-term time series forecasting (LTSF), yet modeling non-stationary temporal dependencies remains challenging. In this paper, we interpret self-attention as a Bayesian posterior over attended positions, combining a content-based prior induced by scaled dot-product similarity with a temporal-evidence likelihood induced by positional encoding. This formulation provides a probabilistic interpretation of how positional encoding shapes the tempor...
  </details>

- **2026-10-14** — Zhongwei Xie, Xingsu Li, Jingqiao Yu et al. — [JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making](http://arxiv.org/abs/2610.19589v1)
  <details><summary>📄 Abstract</summary>
  Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. We introduce JockeyBench, a benchmark and evaluation protocol that studies this problem through historical Japanese horse racing. The protocol combines time-gated evidence, priced tools, paired frozen-program controls, and two workflows: executing an LLM-written predictor or acquiring evidence for a fresh per-race LLM forecast. Evaluation separates forecas...
  </details>

- **2026-10-14** — Chia-Ming Lee, Yu-Jou Hsiao, Ming-Ching Chang et al. — [Spectral World Renderer: Unified 3D Hyperspectral Unmixing](http://arxiv.org/abs/2610.19520v1)
  <details><summary>📄 Abstract</summary>
  Cameras and the foundation models built on them recognize what a 3D scene contains, but not what it is made of: surfaces of the same colour can be different materials. Hyperspectral unmixing explains each spectrum as a mixture of material signatures, yet in 3D it is applied to rendered images after the views are composited, or tied to slow implicit fields, and no multi-view data with known composition exist to check the result. We present the Spectral World Renderer (SWR), which unifies world ge...
  </details>

- **2026-10-14** — Shuyuan Zheng, Yun-seo Lee, Xing Gao et al. — [How Do LLMs Understand Legal Philosophy? Diagnosing Legal-Philosophical Reasoning in LLMs](http://arxiv.org/abs/2610.19427v1)
  <details><summary>📄 Abstract</summary>
  Legal reasoning is a fundamental capability for large language models (LLMs) to complete legal AI tasks such as legal judgment prediction. In legal practice, this reasoning is shaped by legal philosophy: a judge's view of the nature and sources of law guides how legal materials are interpreted and applied, so judges working from the same statutes and precedents can reach different judgments. Existing research has largely overlooked whether LLMs can understand legal philosophy and apply it in leg...
  </details>

- **2026-10-14** — Joshua Cheung, Zhang He — [One-Step Prediction Fidelity Is a Poor Proxy for Planning Performance in JEPA World Models](http://arxiv.org/abs/2610.19375v1)
  <details><summary>📄 Abstract</summary>
  Latent world models are routinely selected, checkpointed and ablated on one-step prediction loss, on the assumption that a model which predicts the next latent better is a better model. In model-based RL this assumption is known to be unreliable; we ask whether it also fails for latent world models, where the training target is the model's own embedding and the loss is not expressed in interpretable units. We introduce a frozen-decoder protocol reporting one-step error in physical units, decompo...
  </details>

- **2026-10-14** — Thomas Zeng, Zelei Cheng, Mingyang Zhou et al. — [Beyond Corrected Actions: Training LLM Agents on Textual Critiques](http://arxiv.org/abs/2610.19367v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for multi-turn agentic tasks that require interactions with users and environments over extended sequences of actions. A common approach to improving LLM agents is to use more capable expert models to provide training supervision, either by behavior cloning the expert's trajectories or by using the expert to correct the actions in trajectories generated by the weaker student model. However, expert LLMs can provide richer supervision than actions...
  </details>

- **2026-10-14** — Danlin Li, Miao Li, Xu Han et al. — [Target-Token Asymmetry Can Masquerade As Depth Specialization](http://arxiv.org/abs/2610.19344v1)
  <details><summary>📄 Abstract</summary>
  Layer-ablation studies often perturb early or late layers of a language model, compare the damage to prediction on two corpora, and read a larger early-layer effect on one corpus as early-layer specialization for its task. Such a comparison averages over the tokens that each corpus asks the model to predict, and these target tokens differ: math solutions, for example, ask for far more whitespace and numbers than encyclopedia prose. We show that this difference can create the appearance of depth ...
  </details>

- **2026-10-13** — Yihang Cheng, Qian Zhang,  Yonghui et al. — [Beyond ICD Codes: Semantic IDs for Generative Medical Coding](http://arxiv.org/abs/2610.19301v1)
  <details><summary>📄 Abstract</summary>
  Generative approaches to automatic International Classification of Diseases (ICD) coding use large language models (LLMs) to predict ICD codes from clinical documents. However, original ICD code strings are not ideal generation targets because the ICD hierarchy does not always reflect clinical relationships, and LLMs struggle to interpret and generate these codes. We introduce SemICD, a framework that trains LLMs to generate Semantic IDs (SIDs) instead. SemICD constructs SIDs by hierarchically c...
  </details>

- **2026-10-13** — Anikesh Parashar, Avik Dutta, Vashu Chauhan et al. — [Whose turn is it? Context-guided model routing for stateful agents](http://arxiv.org/abs/2610.19292v1)
  <details><summary>📄 Abstract</summary>
  Model routing can reduce the cost of LLM applications by assigning simpler requests to cheaper models without sacrificing the quality of the response. However, most routers treat requests as independent. Stateful agents do not operate under this assumption: a user turn may require multiple model and tool calls, its difficulty depends on the state produced by earlier turns, and changing models can sacrifice reuse of the conversational prompt cache. We study zero-shot, cost-aware routing at the us...
  </details>

- **2026-10-13** — Julian Enoch, Elvis Dohmatob — [Exact Scaling Laws for a Random-Features Bigram Model](http://arxiv.org/abs/2610.19281v1)
  <details><summary>📄 Abstract</summary>
  Understanding neural scaling laws is increasingly important for theory and practice, yet first-principles explanations remain limited even in simple settings. In this work, we study capacity-limited scaling in a bottlenecked bigram model with power-law (Zipf) token statistics, viewed as an analytically tractable toy model of a large language model. Fixed random embeddings serve as a proxy for representational capacity and induce an explicit bottleneck of width, allowing us to derive scaling laws...
  </details>

- **2026-10-13** — Eric Lacosse, Pablo Tano, Daniel C. McNamee — [Multi-System Cognitive Steering for Generative Communication](http://arxiv.org/abs/2610.19177v1)
  <details><summary>📄 Abstract</summary>
  A fundamental bottleneck for translating thoughts to speech is the high physical cost of motor input forcing a strict tradeoff between communication speed and expressivity. Generative AI offers a promising solution by expanding highly abbreviated text input into fluent sentences, significantly reducing the motor burden on the user. However, sparse inputs are inherently ambiguous; without sufficient context, AI models frequently misinterpret these abbreviations and generate outputs that fail to a...
  </details>

- **2026-10-13** — Nina Fatehi, Meysam Ghaffari, Animesh Agarwal et al. — [Verification Turns Capability Gaps into Routing Decisions: Small Language Models for Clinical Documentation](http://arxiv.org/abs/2610.19169v1)
  <details><summary>📄 Abstract</summary>
  Clinical note generation from doctor--patient dialogue is high-volume and hallucination-intolerant: a fabricated laboratory value can create patient-safety risk, not a quality regression. We ask whether an agentic \emph{verification} architecture, rather than generator scale, can make a small language model viable here. Holding a four-evaluator verification stack and refinement policy fixed and swapping only the generator between a 4B-parameter model with a QLoRA adapter and a frontier baseline,...
  </details>

- **2026-10-13** — Juntong Feng, Qingan Liu, Jingru Dong et al. — [Plan-Bench: Can Existing VLMs Go Well Beyond Perception to Reason and Plan in Embodied Worlds?](http://arxiv.org/abs/2610.18836v2)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have achieved strong performance in visual perception and spatial reasoning, leading to growing interest in using them as high-level planners for embodied AI. However, physical tasks require models to integrate spatial information, reason over temporal states, and generate multi-step plans under various constraints, raising the question of whether current VLMs can reliably support such reasoning and planning independently of execution. We introduce Plan-Bench, a ben...
  </details>

- **2026-10-13** — Casper L. Christensen, Kyle J. Ray, Dmitry Manning-Coe et al. — [LLMs program using Reusable and Composable Abstract Representations](http://arxiv.org/abs/2610.19238v1)
  <details><summary>📄 Abstract</summary>
  When writing code, the same computation can be expressed in different programming languages and through different implementation strategies. We show that the activations of LLMs capture this shared structure in reusable and composable abstract representations when they generate code. These representations emerge in the middle layers, are reusable across programming languages, and afford the model an impressive amount of generalization ability when generating code under various interventions. Usi...
  </details>

- **2026-10-13** — Anton Arapin, Aditya Singh, Yixin Wang et al. — [Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction](http://arxiv.org/abs/2610.19212v1)
  <details><summary>📄 Abstract</summary>
  World models of visual information predict future image frames conditioned on given action sequences. This predicted scene evolution is driven by deterministic changes such as controlled motion on a robot platform, as well as stochastic changes such as rendering of manipulated objects or previously occluded regions. Our key insight is that the spatial location of these stochastic changes is itself learnable. We leverage this insight by jointly regressing both the deterministic next-state predict...
  </details>

- **2026-10-13** — Zhi Cao, Yining Hong, Jiaolong Yang et al. — [FACT: A Multimodal Force-Action-Track Foundation Model for Human-to-Robot Dexterity](http://arxiv.org/abs/2610.19155v1)
  <details><summary>📄 Abstract</summary>
  Human demonstrations offer a scalable alternative to costly robot data collection for dexterous manipulation, but most human datasets lack force measurements. Dexterous manipulation requires not only visual and proprioceptive understanding but also the ability to anticipate and regulate interaction forces. To scale force-aware human-robot co-training, we introduce EgoForce, a large-scale human tactile dataset capturing force-rich manipulation experience, and combine it with robot demonstrations ...
  </details>

- **2026-10-13** — Zhexi Luo, Zhixuan Xu, Rui Yang et al. — [DexMimic: A Generalist Dexterous Hand-Object Tracking Policy via Value-Guided Reset Allocation](http://arxiv.org/abs/2610.19089v1)
  <details><summary>📄 Abstract</summary>
  Achieving human-like dexterous manipulation remains a central challenge in robotics. Learning from human hand-object interaction (HOI) datasets offers a promising pathway to diverse dexterous skills, yet existing physics-based approaches train specialist policies for individual trajectories, thereby limiting skill reuse at scale. We introduce DexMimic, a generalist dexterous hand-object tracking policy jointly trained across diverse HOI trajectories. Efficient joint training requires allocating ...
  </details>

- **2026-10-13** — Kaiyuan Chen, Shuangyu Xie, Uksang Yoo et al. — [RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks](http://arxiv.org/abs/2610.18835v2)
  <details><summary>📄 Abstract</summary>
  It has been difficult to accurately model the physics of the interaction between a robot and the objects it manipulates, including contact mechanics, coupled contact dynamics, deformations, stiffness and friction. We present RoboSimStudio (RSS), an interactive toolkit that makes choices of solver, contact model, and physical parameters explicit and editable, allowing both humans and coding agents to quickly create and iteratively refine simulations based on observed physical behavior. We impleme...
  </details>

- **2026-10-13** — Lambda-humanoid Team — [$λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.18950v1)
  <details><summary>📄 Abstract</summary>
  Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector execution. We introduce HumanVerse, a 500-hour dataset of open-world human loco-manipulation pairing egocentric video with synchroni...
  </details>

- **2026-10-13** — Yanqiao Wang, Jin Sun — [LAMP: 3D Source-Aware Lighting Estimation at Multiple Points](http://arxiv.org/abs/2610.19266v1)
  <details><summary>📄 Abstract</summary>
  Existing illumination estimation methods primarily recover lighting distributions for rendering, but typically leave the contributions of individual physical light sources at specific scene locations implicit. We address this gap by leveraging the scene understanding capabilities of vision-language models (VLMs) to connect local illumination with its physical sources. We introduce LAMP, a framework for point-conditioned, source-aware illumination reasoning from a single RGB image with marked que...
  </details>

- **2026-10-13** — Nathan Godey, Yoav Artzi — [Copy-Paste Language Models](http://arxiv.org/abs/2610.19247v1)
  <details><summary>📄 Abstract</summary>
  Transformers are intuitively considered to be efficient at copying from their inputs. We actually show that the ability of LLMs to copy in context can be improved through explicit modeling. We propose Copy-Paste Language Models (CPLMs), which add a lightweight Copy-Paste head to the conventional language modeling (LM) head. CPLMs improve training efficiency, downstream performance, and offer new operating points in long-context and retrieval setups. We validate our approach by pretraining models...
  </details>

- **2026-10-13** — Qi Chai, Zhang Zheng, Lu Yang et al. — [PREFER: From Player Experience to Personalized Game Refinement](http://arxiv.org/abs/2610.19213v1)
  <details><summary>📄 Abstract</summary>
  Understanding how large language models (LLMs) evaluate gameplay experience is important for using their feedback to guide game design. However, overall ratings alone provide limited insight into which aspects of experience are associated with these judgments and how they can inform concrete game changes. We introduce PREFER, a framework that uses a shared set of experience dimensions adapted from established psychometric questionnaires to benchmark how models evaluate gameplay and to guide pers...
  </details>

- **2026-10-13** — A. Restuccia, J. Rosales-Gómez, A. Sotomayor — [Symmetries, Lax pair, and nilpotent Darboux transformation for the KdV-ghost system](http://arxiv.org/abs/2610.19192v1)
  <details><summary>📄 Abstract</summary>
  We analyze the KdV--ghost system arising from the BRST formulation of BF-type topological field theory, its symmetries, Lax pair, spectral problem, zero-curvature formulation and Darboux formalism. The system is invariant under shifts of the ghost field, whose generator does not commute with the BRST symmetry of the KdV--ghost system. Their generators allow the introduction of a systematic procedure for generating new solutions from a given one, and the corresponding expressions in the Grassmann...
  </details>

- **2026-10-13** — Mayank Kulkarni, Rakesh Vaideeswaran — [ListQA: A Benchmark for Evaluating List-Formatted Factual Knowledge Retrieval in Large Language Models](http://arxiv.org/abs/2610.19165v1)
  <details><summary>📄 Abstract</summary>
  Many real-world questions demand not a single fact but an organized collection of them, yet existing factual knowledge benchmarks almost exclusively target single answer retrieval. We introduce ListQA, a benchmark of 9,045 human-curated, cross-validated questions (audited error rate of 1.7%) that require LLMs to recall multiple facts and compose them into structured lists of 3-10 elements. Questions range from flat lists ("Which NCAA teams went undefeated between 2000 and 2024?") to hierarchical...
  </details>

- **2026-10-13** — Yu Chen, Kai Jie Wong, Xiaorui Zhang — [Maximin share allocations for two types of items](http://arxiv.org/abs/2610.19099v1)
  <details><summary>📄 Abstract</summary>
  We study the fair allocation of indivisible items among $n$ agents with additive valuations (or costs) using the fairness notion of maximin share (MMS). Since MMS allocations do not always exist when $n > 2$, one direction in the literature has been to identify special classes of instances in which exact MMS allocations can be guaranteed. We show that, when items can be divided into two types of chores, MMS allocations always exist and can be computed in polynomial time using a novel geometric a...
  </details>

- **2026-10-13** — Xu Han, Jiajing Hu, Li-Ping Liu — [Backpropagating Verifier Rewards Through Continuous Flow Language Models](http://arxiv.org/abs/2610.19080v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has substantially improved the reasoning of autoregressive and discrete-diffusion language models. Language models that generate continuous token embeddings are emerging as a strong alternative, but RL post-training for them remains understudied. We propose \method{}, a post-training framework for continuous flow language models. Such a model denoises token embeddings over multiple steps and decodes them into discrete tokens only at the last step. To obtain pathwise g...
  </details>

- **2026-10-13** — Noah Dasanaike — [Pre-Trained Language Models as Zero-Shot Tools for Social Science Research](http://arxiv.org/abs/2610.19048v1)
  <details><summary>📄 Abstract</summary>
  Record linkage and demographic inference from names are routine demands in social science. Most approaches to these problems require labeled training data that are difficult or costly to acquire. I show that pre-trained language models perform both tasks accurately without requiring task-specific training. For record linkage, I introduce EnsembleLink, an algorithm that uses pre-trained embeddings alongside string-based scorers to retrieve a short list of candidates and then identify the likelies...
  </details>

- **2026-10-13** — Zijun Wu, Zhitian Zhang, Hossein Hajimirsadeghi et al. — [Can LLMs Access their World Knowledge for Event Prediction?](http://arxiv.org/abs/2610.19021v1)
  <details><summary>📄 Abstract</summary>
  Recent work has questioned whether large language models (LLMs) can be useful for temporal event prediction. Despite vast pretrained world knowledge, LLMs often underperform simpler specialized models. We ask whether this knowledge is truly inaccessible, or whether current methods fail to present event prediction in a form LLMs can use. We argue for the latter and show that LLMs become effective event forecasters when the interface is designed around two choices. The first grounds each event in ...
  </details>

- **2026-10-13** — Gor Simonyan, Tatevik Abrahamyan, Narek Abelyan et al. — [PMO-Dock: Benchmarking Docking, Specificity, and Generalization in Molecular Optimization](http://arxiv.org/abs/2610.19011v1)
  <details><summary>📄 Abstract</summary>
  The Practical Molecular Optimization (PMO) benchmark standardized evaluation in molecular optimization, but it is built on simple property-based oracles that do not capture structure-based drug design. As the field has moved to docking-based objectives, evaluation practice has become unstandardized, and different methods report results on different docking tasks, often without a shared protocol for fair comparison or sample-efficiency constraints. To address this, we introduce Practical Molecula...
  </details>

- **2026-10-13** — Zackaria Chacko, Shourya Mukherjee — [A spurionic interpretation of RG-stable parameter relations in the two-Higgs-doublet model](http://arxiv.org/abs/2610.18976v1)
  <details><summary>📄 Abstract</summary>
  Recent work on the two-Higgs-doublet model (2HDM) has uncovered basis-invariant relations among the parameters in the scalar potential that are stable under renormalization group (RG) evolution but do not coincide with any of the standard Higgs-family or Generalized-$\mathrm{CP}$ symmetry classes of the scalar sector. These relations have subsequently been reformulated in terms of so-called GOOFy transformations. In this paper, we show that the same fixed surface admits a conventional interpreta...
  </details>

- **2026-10-13** — Muyao Kong, Zhihao Lin — [Read the Room Before Your Model Generates](http://arxiv.org/abs/2610.18820v2)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) generally rely on sampling temperature to regulate the amount of randomness in their outputs. Mainstream methods for selecting temperature typically involve fixed, heuristic global settings and context or token-level calibration, rather than a geometrically interpretable representation of the communicative scenario. In this work, we introduce a simple and interpretable temperature selection framework, the Scenario-Actor, which adapts decoding to the inferred situatio...
  </details>

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


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 678 |
| prompt-injection | 618 |
| memory-poisoning | 55 |
| tool-use-attack | 156 |
| backdoor | 516 |
| adversarial-attack | 635 |
| privacy-leakage | 4368 |
| steganography | 77 |
| misuse | 1178 |
| red-teaming | 141 |
| vulnerability | 3581 |
| defense | 3454 |
| alignment | 3238 |
| robustness | 3494 |
| watermark | 607 |
| unlearning | 113 |
| agent-safety | 64 |
| benchmark | 67 |
| survey | 400 |
| other | 9423 |

---

📚 **全部 32863 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-15 03:52:35*