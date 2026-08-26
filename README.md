<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-24917-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-08-26 00:58 ｜ **论文总数 / Total Papers**: 24917（近 30 天 / Recent 30 days: 4023）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 24917 篇论文（含摘要、分类筛选、搜索）/ View all 24917 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 594
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 503
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 44
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 126
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 422
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 569
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3906
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 57
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 928
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 116
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2803
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 2540
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 2347
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 2390
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 334
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 92
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 52
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 62
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 296
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 6736

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4023 篇，完整 24917 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4023 papers from the last 30 days (with date, authors & abstract). For the full list of 24917 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 7 papers

- **2026-08-24** — Lorenzo Bossi, Federico Saccani, Francesco Panebianco et al. — [Towards Automated Cyber Threat Intelligence Elicitation in Underground Forums](http://arxiv.org/abs/2608.23185v1)
  <details><summary>📄 Abstract</summary>
  Cyber threat intelligence from underground forums has traditionally relied on passive monitoring. However, as users have become more aware of large-scale data collection, valuable intelligence has become increasingly rare in open forums, often migrating instead to private or harder-to-reach spaces, making passive approaches inadequate. Building on the intuition that relevant information can be obtained through active elicitation, this paper presents DarkBot, to the best of our knowledge, the fir...
  </details>

- **2026-08-24** — Zeyu Feng, Qingyu Wu, Yuzhe Luo et al. — [PsychJail: Exploring Psychological Jailbreaks via Multi-Turn Persuasion of LLM Policies](http://arxiv.org/abs/2608.23028v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in education, healthcare, policy advising, and other interactive settings, where users engage them as sustained social interlocutors rather than one-shot query engines. This shift makes jailbreaks a growing safety threat, yet most research emphasizes single-turn prompt optimization or iterative attack refinement, leaving psychologically grounded multi-turn vulnerabilities underexplored. We present PsychJail, a psychology-guided framework for...
  </details>

- **2026-08-23** — Wenyun Li, Guiping Cao, Xiangyuan Lan et al. — [Text-Anchored Semantic Perturbations for Transferable Jailbreak Attacks on Multimodal Large Language Models](http://arxiv.org/abs/2608.22312v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have achieved remarkable progress in vision-language interaction, yet their safety alignment remains vulnerable to jailbreak attacks. A key challenge is that safety behavior learned in the textual space does not reliably transfer to fused cross-modal representations, leaving multimodal inputs exploitable through latent semantic cues. We propose Text-Anchored Semantic Perturbation Attack (TA-SPA), a black-box jailbreak framework that optimizes transferable...
  </details>

- **2026-08-22** — Aaditya Pratap, Harsh Kasyap, Somanath Tripathy — [Breaking the Assumptions: Auditing Input-Side Jailbreak Defenses Against Semantic Attacks](http://arxiv.org/abs/2608.21895v1)
  <details><summary>📄 Abstract</summary>
  Locally deployed Large Language Models (LLMs) via inference engines such as Ollama run without the moderation and abuse detection present in API-served models. Therefore, the safety of LLMs depends on the defense mechanisms used, and their effectiveness depends on the assumptions on which they were designed. This paper does an audit of defense mechanisms under jailbreak attacks on locally deployed models. Some defenses provide formal guarantees (SmoothLLM, Erase-and-Check, Sequential Monitors), ...
  </details>

- **2026-08-21** — Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai et al. — [ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models](http://arxiv.org/abs/2608.21100v1)
  <details><summary>📄 Abstract</summary>
  While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two k...
  </details>

- **2026-08-21** — Yang Liu, Bin Chong, Wenkai Yang et al. — [Certified Multi-Turn Robustness for LLM Safety via Compositional Bounds and Safety Persistence](http://arxiv.org/abs/2608.20820v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are vulnerable to multi-turn jailbreak attacks that progressively manipulate conversation context. Existing certified robustness methods are limited to single-turn inputs; naive multi-turn composition yields bounds that degrade exponentially in the number of turns. We introduce Multi-Turn Certified Robustness (MTCR), a framework that models conversational safety via State-Adversarial MDPs and defines $k$-turn certified robustness as the worst-case safety probability ...
  </details>

- **2026-08-20** — Ling Zhou, Yihao Huang, Jingling Sun et al. — [TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling](http://arxiv.org/abs/2608.19737v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) have achieved remarkable progress in video understanding and reasoning. Despite extensive studies on text- and image-based jailbreaks, video jailbreaks against LVLMs remain largely unexplored. Existing video jailbreak methods mainly manipulate textual content embedded in videos, while overlooking how such information is organized over time. Our analysis reveals that jailbreak effectiveness depends not only on the semantics of textual information but also on i...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-08-24** — Hanling Tian, Gengyu Zhang, Zeyang Sha et al. — [InjecMEM: Memory Injection Attack on LLM Agent Memory Systems](http://arxiv.org/abs/2608.23471v1)
  <details><summary>📄 Abstract</summary>
  Memory is becoming a default subsystem in deployed LLM agents to provide persistent personalization and continuity. This naturally prompts a question: will memory system introduce new vulnerabilities into agents? Thus we propose InjecMEM, a novel memory injection attack paradigm that requires only a single interaction (no read/edit access to memory store) to steer later responses of related queries toward a pre-specified output. Guided by the retrieval-then-generate mechanism of memory systems, ...
  </details>

- **2026-08-24** — Basavesh Ammanaghatta Shivakumar, Swarn Priya, Peng Gao — [AgentFlow: A Flow-Centric Policy Language and Framework for Securing LLM Agent Systems](http://arxiv.org/abs/2608.22868v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly read untrusted content, invoke external tools, access private data, and delegate work to other agents. Harm often arises not from a single unsafe action but from the flow of sensitive data across a sequence of otherwise plausible steps. We present AgentFlow, a flow-centric policy language and runtime enforcement model for specifying where data may travel in agent systems. Policies are defined over labeled runtime edges and constrain which tools may receive sensitive field...
  </details>

- **2026-08-23** — Jiahao Chen, Rui Yin, Xinfeng Li et al. — [Beyond Over-Refusal: Defending Indirect Prompt Injection via Latent Instruction Manifolds](http://arxiv.org/abs/2608.22248v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been integrated into complex ecosystems (e.g., Code Agents), while Indirect Prompt Injection (IPI) attacks have emerged as critical barriers to their safe deployment. Attackers exploit LLMs' indistinguishability between "instructions" and "data" to manipulate LLMs via maliciously injected instructions. Existing defenses, however, face an intractable safety-utility trade-off: most guardrails either incur high latency or suffer from severe over-refusal. In this pa...
  </details>

- **2026-08-22** — Minjae Seo, Wonwoo Choi, Geonwoo Han et al. — [MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds](http://arxiv.org/abs/2608.22061v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic...
  </details>

- **2026-08-21** — Bohao Liao, Jingchao Wang, Qipeng Song et al. — [TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents](http://arxiv.org/abs/2608.21126v1)
  <details><summary>📄 Abstract</summary>
  Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidenc...
  </details>

- **2026-08-21** — Balkrishna Giri, Md Toufique Hasan, Jussi Rasku et al. — [Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems](http://arxiv.org/abs/2608.21095v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) grounds Large Language Model (LLM) outputs in external knowledge, but RAG systems usually trust whatever they retrieve, creating a Security-Reliability Gap: high semantic relevance does not guarantee factual truth. Adversaries exploit this through knowledge poisoning, inserting malicious documents to cause targeted misinformation. We propose an Evaluation Agent, middleware that combines Natural Language Inference (NLI) factual verification, a five-signal pois...
  </details>

- **2026-08-20** — Roshan Sood, Onat Gungor, Tajana Rosing — [COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense](http://arxiv.org/abs/2608.19982v1)
  <details><summary>📄 Abstract</summary>
  LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to ...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 4 papers

- **2026-08-24** — Ziyue Yang, Fan Ding — [Signal or Noise? A Benchmark Study of Agent Skills in Web Development](http://arxiv.org/abs/2608.23067v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills are reusable procedural modules that are increasingly injected into coding-agent sessions to encode framework conventions, anti-patterns, and reusable tools. However, because each injected Skill expands the prompt of every query, an effective Skill benchmark must determine not only whether an agent can solve a task, but whether the Skill should have been injected at all. We introduce WebDev-Skills-Bench and use it for a controlled empirical study of 31 public WebDev Skills on 50 Web...
  </details>

- **2026-08-23** — Qiyan Zhao, Xiaofeng Zhang, Bo Liu et al. — [Coalition-Aware Skill Reliability for Self-Evolving Agents](http://arxiv.org/abs/2608.22610v1)
  <details><summary>📄 Abstract</summary>
  Agent skills, structured artifacts distilled from interaction trajectories and dynamically reused from skill banks, have become a central mechanism for enabling large language model (LLM)-based self-evolving agents to learn from past experience. Yet existing work has largely focused on the operational aspects of skills, such as acquisition, evolution, and retrieval, while leaving a more fundamental reliability question unresolved: Do accumulated skills in an agent's skill bank actually make posi...
  </details>

- **2026-08-22** — Yuanjin Zheng, Jingbang Chen — [SkillBloat: Token Amplification Attacks via Skill Injection in LLM Coding Agents](http://arxiv.org/abs/2608.21929v1)
  <details><summary>📄 Abstract</summary>
  Agent skills extend coding agents with task-specific instructions, scripts, and resources, but they also create a trusted   instruction channel that can be abused beyond conventional security attacks. This paper studies token amplification through   skill injection: an economic resource-abuse threat in which a malicious skill causes an agent to consume substantially more   tokens than needed for normal task execution. We present SkillBloat, a two-phase framework that first screens a library of  ...
  </details>

- **2026-08-20** — Yue Wang, Yi Liu, Gelei Deng et al. — [MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection](http://arxiv.org/abs/2608.19901v1)
  <details><summary>📄 Abstract</summary>
  Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious A...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 1 papers

- **2026-08-21** — Minhua Lin, Zhicheng Gao, Yilong Wang et al. — [Trojaning the Alignment: Stealthy Backdoor Attacks against Graph Foundation Models](http://arxiv.org/abs/2608.20991v1)
  <details><summary>📄 Abstract</summary>
  Graph Foundation Models (GFMs) on text-attributed graphs (TAGs) align graph representations with language semantics to support transferable graph learning. Despite these advantages, the backdoor vulnerability of GFMs on TAGs remains insufficiently understood, especially under graph-language alignment, where graph and text representations are trained to constrain each other in a shared semantic space. Existing backdoor attacks mainly target either the graph side or the text side, treating the two...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-08-23** — Alberick Euraste Djire, Iyiola E. Olatunji, Melissa Tessa et al. — [Evaluating Inference-Time Defenses Against Package Hallucination in LLM-Generated Code](http://arxiv.org/abs/2608.22652v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly used for code generation, yet they frequently hallucinate non-existent software packages, creating exploitable entry points into the software supply chain. We make four contributions to this problem. First, we show that prior evaluation methodologies systematically inflate hallucination rates by misclassifying standard-library modules as hallucinations in some languages. For Python, the overestimation reaches 9.4 percentage points. Second, we evaluate seven inference-time d...
  </details>

- **2026-08-23** — Hoang Anh Nguyen, Yuan Hong, Hongyi Xu — [Adversarial Agents on Topology Optimization: Understanding the Fragility and Robustness of Deep Learning-based and Physics-Based Design Models under Adversarial Perturbation](http://arxiv.org/abs/2608.22606v1)
  <details><summary>📄 Abstract</summary>
  Topology optimization, using both physic-based approaches and deep learning surrogates, serves as a cornerstone for generative design agents in cyber-manufacturing systems. While deep learning surrogates have gained widespread adoption due to their speed in online design generation, this work demonstrates their vulnerability under input perturbations. In this work, we present a mechanics-grounded reliability evaluation framework that formulates an adversarial agent targeting the generative desig...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 35 papers

- **2026-08-24** — Seokjin Hwang,  Yuting,  Li et al. — [Spectrum-Aware Bounds on Invertibility for Privacy-Enhancing Instance Encoding](http://arxiv.org/abs/2608.23382v1)
  <details><summary>📄 Abstract</summary>
  Instance encoding is a popular empirical technique for privacy enhancement when sharing data to an untrusted server. It transforms sensitive data through an encoding process before sharing, with the hope that the encoding process retains utility but makes it hard to reconstruct the original data. However, most work offers no theoretical guarantee that the encoding process is actually irreversible. A recent work derived a mean-squared error (MSE) bound limiting any adversary's reconstruction accu...
  </details>

- **2026-08-24** — Xunlei Chen, Qirui Ye, Yuang Li et al. — [Unlearning Is Not Just Erasing: Temporal Decoupling via Generation Inequality](http://arxiv.org/abs/2608.23020v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) require effective unlearning to address privacy regulations and safety concerns. However, achieving precise forgetting without compromising general utility remains challenging. Existing sequence- and token-level methods penalize target outputs without modeling their context-dependent retrieval paths, which can disrupt linguistic structure or suppress benign knowledge. We present ADU, a fine-grained, training-based framework that shifts unlearning from token erasure t...
  </details>

- **2026-08-24** — Hongchao Wang, Linrui Li, Yunkai Zou et al. — [What's Your NIC Whispering? Network Threat Behavior Recognition via NIC Electromagnetic Side-Channel Leakage](http://arxiv.org/abs/2608.22941v1)
  <details><summary>📄 Abstract</summary>
  Conventional network threat detection primarily relies on packet-level, flow-level, or host-level telemetry. This paper investigates a different observation surface: unintended electromagnetic(EM) emissions generated by network interface card(NIC) activity, and asks whether such physical leakage contains sufficiently structured information for network threat-behavior recognition. We present NICWhisper, which externally captures NIC EM emissions, transforms raw measurements into time-frequency re...
  </details>

- **2026-08-24** — Kurt M Wilson, Mohaiminul Al Nahian, Abeer Matar A. Almalky et al. — [TEE-X: TEE-aware Acceleration Framework for Large Vision Models at the Edge](http://arxiv.org/abs/2608.22716v1)
  <details><summary>📄 Abstract</summary>
  Despite their remarkable success, machine learning models, particularly in vision applications, are alarmingly vulnerable to a range of security threats. One key factor in the attack landscape is the distinction between white-box and black-box threat models, as the latter poses challenges that limit attack effectiveness when access to model information is limited. As a result, using Trusted Execution Environments (TEEs) enhances security for machine learning applications by protecting model conf...
  </details>

- **2026-08-24** — Md Thamed Bin Zaman Chowdhury, Moazzem Hossain — [EG-ARSA: An Expert-Grounded Open Model for Visual Road Safety Auditing in Low-Resource Settings](http://arxiv.org/abs/2608.23563v1)
  <details><summary>📄 Abstract</summary>
  Road traffic injuries remain a major challenge in low- and middle-income countries, where proactive road safety auditing is limited by incomplete crash records, shortages of qualified auditors, and the high cost of large-scale field inspections. To address this problem, we propose Expert-Grounded Distillation (EGD), a novel artificial intelligence framework that transfers institutional road safety expertise into a compact vision-language model for scalable visual road safety auditing. The key in...
  </details>

- **2026-08-24** — ChengAo Shen, Wenchao Yu, Fangyu Wu et al. — [MetaCaster: Meta-Harness-Optimized Agent for End-to-End Few-Shot Learning of Lightweight Time Series Forecasters](http://arxiv.org/abs/2608.23473v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting (TSF) is evolving toward multimodal and agentic settings, yet using foundation models remains uneconomical in resource-constrained scenarios, where compact, specialized forecasters are more desirable. However, lightweight forecasters typically require substantial training data, limiting their use in domains with scarce, slowly accumulated, or privacy-sensitive time series. To address this dilemma, we investigate the challenging problem of few-shot learning for lightweight...
  </details>

- **2026-08-24** — Fabian Schüssler, S. Bisero, M. Cellier et al. — [AI-Assisted Extraction of Follow-up Observations from GCN Circulars in Astro-COLIBRI](http://arxiv.org/abs/2608.23270v1)
  <details><summary>📄 Abstract</summary>
  We present a new Astro-COLIBRI component that converts free-text GCN Circulars into structured, event-linked follow-up records and combines them with structured reports submitted directly by the community. A continuously running Circular listener associates new reports with transient events, applies deterministic pre-analysis, and invokes a schema-constrained large language model extraction step for photometry, contacts, redshifts, and other reported results and metadata. The resulting records a...
  </details>

- **2026-08-24** — Siri Willems, James Butterworth, Lore Goetschalckx et al. — [Future Querying: Can LLMs Serve as Implicit Medical World Models?](http://arxiv.org/abs/2608.23248v1)
  <details><summary>📄 Abstract</summary>
  Traditional clinical prediction models rely on task-specific pipelines and curated, structured data, which scale poorly and underutilize unstructured text. To address this, we introduce future querying, a paradigm that probes whether large language models (LLMs) can function as implicit medical world models by evaluating their ability to answer time-indexed clinical queries about a patient's future. Our framework operates on unstructured clinical documentation using endpoint-agnostic training, e...
  </details>

- **2026-08-24** — Fangcheng Li, Zhen Yu, Kejun Wu et al. — [ByteAction: Byte-space Action Recognition Foundation Model](http://arxiv.org/abs/2608.22760v1)
  <details><summary>📄 Abstract</summary>
  Byte-space Action Recognition (BAR) aims to recognize human actions directly from compressed image bitstreams without any pixel decoding. By operating entirely in byte space, BAR is inherently independent of file integrity and pixel-level reconstruction, making it naturally applicable to privacy-sensitive scenarios and robust against bitstream corruption. In this paper, we propose ByteAction, a BAR foundation model that achieves accurate action recognition on corrupted image bitstreams. ByteActi...
  </details>

- **2026-08-24** — Parisa Ghanad Torshizi, Stacy Marsella — [LLM-Based Selection of Incongruent Verbal and Nonverbal Behavior for Virtual Humans](http://arxiv.org/abs/2608.22731v1)
  <details><summary>📄 Abstract</summary>
  Nonverbal behavior generation systems for virtual agents often take an utterance as input and generate nonverbal behaviors that emphasize or illustrate the content of the verbal channel. However, human nonverbal behavior is shaped by more than the content of the speech. It is also influenced by speaker roles, interpersonal relationships, social context, and the cognitive and emotional states of the interactants. As a result, the nonverbal channel may reinforce, weaken, qualify, or even contradic...
  </details>

- **2026-08-23** — Liang-Wei Li, Chung-Nan Lee, Kishu Gupta et al. — [Syntax Element Encryption for H.265/HEVC Using Chaotic Map-Based Coefficient Scrambling Scheme](http://arxiv.org/abs/2608.22573v1)
  <details><summary>📄 Abstract</summary>
  In today's digital landscape, high-efficiency video coding (H.265/HEVC) has emerged as the most widely used video coding standard, employing selective encryption schemes to protect the privacy of video content while maintaining efficient compression performance. However, existing coefficient scrambling methods impose a significant computational load, leading to increased bit rate overhead due to encryption, longer execution times, and insufficient safety measures. To address these issues, a new ...
  </details>

- **2026-08-23** — Kushagra Yadav, Nalin Prabhath, Amit Lamba et al. — [Clinical Graph-JEPA: Predictive Patient-State Knowledge Graphs for Cognitive Decision Support](http://arxiv.org/abs/2608.22583v1)
  <details><summary>📄 Abstract</summary>
  Clinical records contain rich evidence about patient state, but converting that evidence into reliable, structured knowledge graphs remains difficult because extraction errors, ontology mismatch, missing relations, and temporal ambiguity can propagate into downstream systems. We propose a clinical knowledge graph construction and refinement framework that combines multi-agent relation proposal, ontology-aware normalization, deterministic evidence scoring, and JEPA-based latent refinement. Rather...
  </details>

- **2026-08-23** — Hermann Yepdjio Nkouanga, Minwei Luo, Maggie Wigness et al. — [Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction](http://arxiv.org/abs/2608.22196v1)
  <details><summary>📄 Abstract</summary>
  While cascaded multi-talker ASR (MT-ASR) leverages state-of-the-art foundation models, its performance is often capped by speaker leakage during separation. Prior correction strategies primarily focus on lexical re-labeling for speaker attribution. We propose a complementary pruning-based paradigm that robustly identifies and removes leakage artifacts. Our method utilizes a pre-trained speaker diarization model as a multimodal verifier to prune transcribed segments satisfying a tripartite consen...
  </details>

- **2026-08-23** — Jiajun Sun, Zhanrui Cai — [Token-Level Likelihood-Array Regression for Membership Inference and AI-Generated Text Detection](http://arxiv.org/abs/2608.22179v1)
  <details><summary>📄 Abstract</summary>
  Membership inference asks whether a text was used to train a language model, whereas AI-generated text detection asks whether it was generated by a language model rather than written by a human. Existing likelihood-based methods typically compress token-level probabilities into a few prespecified scores, most often using only probabilities conditioned on the full preceding context. We propose likelihood-array regression (LAR), which evaluates each target token under nested left-context windows a...
  </details>

- **2026-08-23** — Bin Dong, Jinghong Chen — [CiUNet: A Hybrid Swin-CNN UNet for Medical Image Segmentation](http://arxiv.org/abs/2608.22281v1)
  <details><summary>📄 Abstract</summary>
  Medical image segmentation requires high accuracy and robustness, yet practical commercial deployment also demands privacy preservation and computational efficiency. In this context, the U-Net architecture, which can be inherently decoupled into independent encoder and decoder components, serves as a natural commercial choice. However, pure Transformer-based variants like Swin-UNet often suffer from insufficient local detail capture and limited interpretability. In this paper, we propose a light...
  </details>

- **2026-08-23** — Hariharan Ramesh, Someshwaran Murugaiyan, Jyotikrishna Dass — [Unveiling the Depth-Performance Dilemma in Split-Federated Fine-tuning of LLMs](http://arxiv.org/abs/2608.22188v1)
  <details><summary>📄 Abstract</summary>
  Split Federated Fine-tuning (SFF) is a promising paradigm for scaling Large Language Models (LLMs) by partitioning model depth between resource-constrained clients and a centralized server. While system incentives for throughput and privacy favor deep partitions, the impact of such configurations on model utility remains poorly understood. In this work, we identify and characterize the Depth-Performance Dilemma: the regime that maximizes system efficiency is precisely where fine-tuning quality c...
  </details>

- **2026-08-23** — Jun Hou, Yi Fang, Xuan Wang — [Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction](http://arxiv.org/abs/2608.22176v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly applied to clinical prediction tasks such as in-hospital mortality and readmission from electronic health records (EHRs). Privacy and compliance constraints motivate systems that can be deployed locally, which has increased interest in open-weight multi-agent designs. However, most medical multi-agent systems are evaluated as a single block, leaving unclear which agent role contributes to prediction and whether retrieval drives observed gains. We stu...
  </details>

- **2026-08-22** — Daniel Rodriguez-Cardenas, David Nader Palacio, Anna Schmedding et al. — [On Predicting Vulnerability Severity Using In-Context Learning: An Industrial Case Study](http://arxiv.org/abs/2608.22089v1)
  <details><summary>📄 Abstract</summary>
  Modern software systems require earlier and more scalable vulnerability severity assessment to reduce exposure to high-impact security flaws. Security analysts typically assign CVSS scores, but this manual triage does not scale with the growth of disclosed vulnerabilities and often depends on cloud LLM services that raise confidentiality concerns. This paper presents an industrial case study on predicting CVSS v3.1 scores directly from vulnerable C/C++ snippets using in-context learning with loc...
  </details>

- **2026-08-22** — YuHang Wu, HaoXian Liu, Jia Tao — [SoulGard-VL-2B: A Vision-Language Model for Edge-Based Feline Behavior Understanding](http://arxiv.org/abs/2608.22070v1)
  <details><summary>📄 Abstract</summary>
  The task of Feline Behavior Understanding requires models that can identify subtle visual cues, keep behavior interpretations auditable, and support low-latency, privacy-sensitive deployment. Directly prompting general Vision-Language Models (VLMs) is poorly suited to this setting: instead of first reporting visible evidence such as ear position and tail posture, they may jump directly to labels such as relaxed, afraid, or in pain. This makes the output difficult to verify and poorly aligned wit...
  </details>

- **2026-08-22** — Rachel Poonsiriwong,  Chayapatr,  Archiwaranguprok et al. — [AI Watchdog: Agent Interfaces for Detecting and Defending Against Manipulative Dark Patterns in AI Conversations](http://arxiv.org/abs/2608.21841v1)
  <details><summary>📄 Abstract</summary>
  Conversational AI increasingly shapes consequential decisions, yet users have limited support for recognizing and resisting manipulation. We present AI Watchdog, a browser-based agent interface that monitors live conversations, detects five dark-pattern categories, including sycophancy, brand bias, anthropomorphization, sneaking, and harmful generation, and alerts users when they occur. Its open-weight turn-level classifier supports independent deployment and a path toward local inference, prese...
  </details>

- **2026-08-22** — Aarzoo Dhiman, Farzana Haque, Kartikae Grover et al. — [Development and Feasibility Evaluation of an Edge AI as Medical Device System for Breast Cancer Multidisciplinary Team Meetings](http://arxiv.org/abs/2608.22108v1)
  <details><summary>📄 Abstract</summary>
  Breast Cancer Multidisciplinary Team (MDT) meetings manage increasingly complex cases under considerable time pressure, and documentation requirements can reduce clinical efficiency and decision quality. Existing AI based MDT workflows rely on cloud-based processing, limiting their use because patient discussions contain identifiable information. We developed a fully on-device AI pipeline using open-source Automatic Speech Recognition (ASR) and Large Language Models (LLMs) that transcribes breas...
  </details>

- **2026-08-22** — Orion Powers, Daniella Seum, Khaled Slhoub — [More Accurate or More Efficient? Evaluating Locally Deployed Compact Open-Weight Language Models for Mathematical Reasoning](http://arxiv.org/abs/2608.22048v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly deployed on local hardware for privacy, cost, and accessibility reasons. Yet many evaluations emphasize accuracy while fewer quantify local runtime and energy, characterize failure modes, or apply paired statistical comparisons under controlled conditions. This paper presents a controlled, documented procedure for evaluating locally hosted LLMs on mathematical reasoning. It combines fixed inference settings, hierarchical answer extraction and verification, ...
  </details>

- **2026-08-21** — Adriana Watson, Marco Bücheler, Grant Richards — [From Regulation to Implementation: A Critical Evaluation of LLM-Assisted Regulatory Compliance in Industry](http://arxiv.org/abs/2608.21317v1)
  <details><summary>📄 Abstract</summary>
  The European Union (EU) has emerged as a leading regulatory body in the development of sustainability and privacy regulations. While new regulation requirements vary, many include a documentation artifact to ensure compliance. Notably, the Ecodesign for Sustainable Products Regulation (ESPR) introduces Digital Product Passports (DPPs) for life cycle transparency, while the General Data Protection Regulation (GDPR) mandates Data Protection Impact Assessments (DPIAs) to mitigate privacy risks. Cre...
  </details>

- **2026-08-21** — Lekang Jiang, Wenjun Sun, Stephan Goetz — [Benchmarking Patent Drafting from Inventor-Style Disclosures](http://arxiv.org/abs/2608.21249v1)
  <details><summary>📄 Abstract</summary>
  While recent large language models (LLMs) have achieved promising results on individual patent drafting tasks, they fundamentally fail to investigate the core challenge of real-world patent drafting: generating a complete and legally coherent patent application directly from early-stage invention materials. Prior work predominantly assumes later-stage, highly structured, or already legalistic inputs. However, real patenting workflows begin with informal, de-legalized disclosures authored by inve...
  </details>

- **2026-08-21** — Junseok Kim, Nakyeong Yang, Kyomin Jung — [Personalized Privacy Control in LLMs via Attention Head Intervention](http://arxiv.org/abs/2608.21209v1)
  <details><summary>📄 Abstract</summary>
  The rise of agentic AI enables LLMs to access diverse user data, raising critical privacy concerns. Prior work on contextual privacy studies whether LLMs regulate information disclosure according to context-dependent norms. However, acceptable disclosure boundaries may vary across users even within the same context. To address this limitation, we introduce \textit{personalized privacy}, which incorporates user-specific disclosure preferences into privacy control. We further present P3Bench~(\tex...
  </details>

- **2026-08-21** — Dimitri Staufer, David Hartmann, Ibrahim Baroud — [No PUN Intended: Plausible Unknown Names for Person-Centred LLM Evaluation](http://arxiv.org/abs/2608.21206v1)
  <details><summary>📄 Abstract</summary>
  Person names are widely used as prompt variables in LLM evaluations of factuality, privacy leakage, bias and abstention, but when a name's evidential status is uncontrolled, measurements may conflate memorisation, retrieval, name priors and wrong-person attribution. We operationalise an unknown name as one with plausible First-Last form, no indexed full-name evidence, and no ambiguity signals under a documented validation run, and introduce PUN (Plausible Unknown Names), a protocol for construct...
  </details>

- **2026-08-21** — Sara Malacarne, Andrea Ceni, Claudio Gallicchio — [Free-Probability Kernels for Zero-Rollout Hyperparameter Selection in Reservoir Computing](http://arxiv.org/abs/2608.20998v1)
  <details><summary>📄 Abstract</summary>
  Reservoir computing (RC) couples a fixed recurrent dynamical system with a trained lightweight readout, but this efficiency is partly lost during hyperparameter selection: the recurrent gain, input scale, and leakage rate determine the reservoir's stability and temporal processing regime and are usually tuned through many rollouts. We introduce a deterministic, pilot-informed selector for leaky linear reservoirs followed by coordinate-wise nonlinear features. Free probability yields cross-lag pr...
  </details>

- **2026-08-21** — Jinzhao Wang, Kunrun Lu, Yuanlin Li et al. — [Artificial Anisotropy Induced Bound States in the Continuum for Integrated Photonic Waveguide](http://arxiv.org/abs/2608.20992v1)
  <details><summary>📄 Abstract</summary>
  Bound states in the continuum (BICs) enable counterintuitive light confinement without radiation loss, providing a powerful foundation for integrated photonic waveguides. However, existing BIC waveguides are predominantly realized through geometry-dependent designs, where the BIC condition is restricted to narrowly defined structural parameters, limiting design flexibility and practical applicability. Artificial optical anisotropy is introduced as a new design paradigm for BIC waveguides. Implem...
  </details>

- **2026-08-21** — Christoph Nirschl, Magdalena Glas, Gerhard Messmann et al. — [Chat First, Worry Later: Understanding Individuals' Privacy Perceptions Using ChatGPT in a Work Context](http://arxiv.org/abs/2608.20789v1)
  <details><summary>📄 Abstract</summary>
  Generative Artificial Intelligence (GenAI) tools like ChatGPT, which can generate human-like responses from vast amounts of textual data, are increasingly transforming work routines across various fields, including education, healthcare, and IT. This integration, however, raises privacy concerns and questions the readiness of both environments and individuals. To investigate this issue, we conducted a user study with $N=224$ participants from a range of different employment sectors that have int...
  </details>

- **2026-08-20** — Jaiden Fairoze, Neal Mangaokar, Kamalika Chaudhuri et al. — [Inadvertent Context Leakage in Language Models](http://arxiv.org/abs/2608.19857v1)
  <details><summary>📄 Abstract</summary>
  For AI agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert c...
  </details>

- **2026-08-20** — Yuki Itabashi, Hiroto Sawada, Mare Hirose et al. — [Enhancing Privacy in Federated Learning via Dual Obfuscation of Gradients and Training Images](http://arxiv.org/abs/2608.19650v1)
  <details><summary>📄 Abstract</summary>
  Federated learning enables collaborative model training while keeping data locally at each client; however, recent studies have shown that training data can be reconstructed from shared model updates. To address this issue, this paper proposes a dual obfuscation method that enhances robustness against image restoration attacks by jointly obfuscating updated information and training images. The proposed method combines a robustness enhancement technique based on random binary weights, which rando...
  </details>

- **2026-08-20** — Ye Tao, Hong Shen, Hui Tian et al. — [AEGIS: Attention-Embedding Gradient Isolation Shield - Triple-Channel Gradient Masking for Privacy-Preserving Federated LLM Fine-Tuning](http://arxiv.org/abs/2608.19534v1)
  <details><summary>📄 Abstract</summary>
  Gradient inversion attacks recover private training text from gradients shared in federated learning, posing a serious threat to collaborative model training. Through our analysis of transformer gradient structure, we identify three channels through which private token information leaks: the attention output projection gradient exposes a low-rank subspace that encodes input embeddings (Channel 1), the embedding gradient's row-norm sparsity directly reveals which tokens are present (Channel 2), a...
  </details>

- **2026-08-20** — Jingtao Zhang, Haorui Gao, Youqing Liang et al. — [Scale-Separated Conditioning for Style-Encoder-Free Diffusion Stylization](http://arxiv.org/abs/2608.19719v1)
  <details><summary>📄 Abstract</summary>
  Reference-based diffusion stylization requires separating target geometry from transferable appearance. Existing tuning-based methods often rely on aligned content-style-target triplets or auxiliary visual encoders, which increases data cost and can transfer unintended scene structure from the style reference. We propose SEFS (Style-Encoder-Free Stylization), a style-encoder-free conditioning framework for diffusion transformers. SEFS forms style tokens from stochastic low-resolution crops of si...
  </details>

- **2026-08-20** — Konstantin Chesnokov, Chingiz Mingazov — [Natural Language Code Retrieval for 1C:Enterprise: An Open Benchmark and Efficient Bi-Encoder](http://arxiv.org/abs/2608.19957v1)
  <details><summary>📄 Abstract</summary>
  Natural language code retrieval is a rapidly evolving task in computer science. However, the 1C:Enterprise ecosystem combines Russian syntax with highly domain-specific terminology, for which open datasets and specialized models have been virtually non-existent. We present a comprehensive pipeline for 1C code retrieval: an open benchmark of 3,413 real-world, PII-scrubbed query-code pairs, a reproducible evaluation harness, and a specialized bi-encoder. To overcome scarce labeled data, we fine-tu...
  </details>

- **2026-08-20** — Tatsuya Amano, Hirozumi Yamaguchi — [Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation](http://arxiv.org/abs/2608.19778v1)
  <details><summary>📄 Abstract</summary>
  Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, because many different sets of decisions reproduce the same counts. We fine-tune a language model crowd agent so that the simulated population matches the observed destination composition, the fraction of ...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 1 papers

- **2026-08-24** — Nikita Kezins — [Adversarial Entropy Inflation Against Gumbel-Based Inference Verification](http://arxiv.org/abs/2608.23375v1)
  <details><summary>📄 Abstract</summary>
  Gumbel-based inference verification bounds LLM weight exfiltration by only forgiving token choices that plausibly arise from honest GPU nondeterminism, reporting a >200x slowdown for a steganographic adversary under benign prompt traffic. This bound assumes a passive attacker; we show it degrades sharply against an adversary who instead controls the prompt distribution. Because the verifier's admissible-token-set size is driven by the model's own output entropy, prompts engineered to break gramm...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 20 papers

- **2026-08-24** — Or Biton, Tomer Krichli, Itai Allouche et al. — [Hidden in the Request: Explaining Unethical LLM Compliance through Token Relevance](http://arxiv.org/abs/2608.23264v1)
  <details><summary>📄 Abstract</summary>
  Although Large Language Models (LLMs) are aligned to optimize for both helpfulness and harmlessness, these dual objectives may conflict, inevitably leading to alignment failures. This work systematically investigates instances where LLMs fail to exhibit ethical behavior. To understand the underlying mechanics of these vulnerabilities, we introduce a probing methodology that presents unethical scenarios to LLMs in three distinct structural modalities: objective classification tasks, subjective fi...
  </details>

- **2026-08-24** — Yipeng Zhao, Qishun Yang, Shenzhe Zhu et al. — [Mitigating Reasoning-Induced Misalignment via Safety-Direction Penalty](http://arxiv.org/abs/2608.23497v1)
  <details><summary>📄 Abstract</summary>
  Reasoning-Induced Misalignment, where fine-tuning on reasoning data containing no harmful content, including mathematics, code, and problem-solving with chain-of-thought traces can induce harmful behaviors of LLM, posing a serious challenge to the safety of LLM reasoning. Cross-architecture, cross-scale, and cross-dataset checks show that RIM does not always emerge. Previous work attributed RIM to neuron-level entanglement, but did not identify the geometry of the representation space underlying...
  </details>

- **2026-08-24** — Abdul Ghafoor, Muhammad Arslan Manzoor, Yufang Hou — [Beyond Verdicts: A Graph-Based Analysis of Human and LLM Reasoning in Scientific Fact-Checking](http://arxiv.org/abs/2608.23047v1)
  <details><summary>📄 Abstract</summary>
  Misinformation that cites legitimate papers can be especially harmful when it distorts what those studies actually report. While existing automatic fact-checking systems based on large language models (LLMs) can assess whether a model assigns an Incorrect verdict and can gen- erate explanations for that decision, they typi- cally do not indicate whether the model follows the same reasoning path as human experts or arrives at the verdict through a different but still valid path. In this work, we ...
  </details>

- **2026-08-24** — Mo El-Haj — [AraDetox: A Multi-Dialect Arabic Detoxification Dataset](http://arxiv.org/abs/2608.22894v1)
  <details><summary>📄 Abstract</summary>
  Arabic harmful-language detection has received considerable attention, yet Arabic text detoxification remains underexplored. We introduce AraDetox, a multi-dialect Arabic detoxification dataset comprising 10,500 harmful social-media posts and 84,000 detoxified rewrites generated using GPT-5 and Gemini 2.5 Flash across Modern Standard Arabic, Gulf, Levantine, and Egyptian Arabic. The generated outputs were assessed through human evaluation and automatic analyses of lexical change, semantic preser...
  </details>

- **2026-08-24** — Sujoy Nath, Aswini Kumar, Tanmoy Chakraborty — [Counter with Evidence! A Multi-Agent Memory Efficient Reasoning Framework for Hate Category Informed Counterspeech Generation](http://arxiv.org/abs/2608.23152v1)
  <details><summary>📄 Abstract</summary>
  Counterspeech effectively neutralizes the impact of online hate. Although prior work explores automated counterspeech generation, it largely emphasizes stylistic control while treating hate speech as homogeneous, overlooking that distinct forms of abuse require fundamentally different counterspeech strategies. To address this gap, we introduce FIRE (Factuality Informed Multi-Agent Reasoning Framework) that first decomposes hate speech into one of the five distinct categories (misinformation, ste...
  </details>

- **2026-08-23** — Naymul Islam, Nusrat Jahan Lia, Shubhashis Roy Dipta et al. — [Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms](http://arxiv.org/abs/2608.22335v1)
  <details><summary>📄 Abstract</summary>
  Bengali is the seventh-most-spoken language globally, yet LLM safety evaluation remains overwhelmingly English-centric. We introduce BanglaSafe, a benchmark of 879 Bengali prompts combining 309 natively authored prompts with 570 expert-reviewed prompts, spanning 17 culturally grounded harm categories and five prompting conditions that vary language, writing style, and authority framing. Evaluating 18 frontier LLMs, we find that over half of all responses are unsafe or partially unsafe (53.6%) wh...
  </details>

- **2026-08-23** — Mengxi Luo, Changjia Chen, An Cao et al. — [STAGE: Stateful Translation to Agentic Graph Execution with Policy-Scoped Context and Deterministic Control](http://arxiv.org/abs/2608.22538v1)
  <details><summary>📄 Abstract</summary>
  Policy-governed agents must interpret case evidence while following an authorized procedure. We present \textsc{Stage}, an executable-graph framework that confines model judgment to policy-scoped nodes while placing procedural control in deterministic code. At each node, the model receives task-relevant policy context and returns a typed result, while the coordinator enforces the reviewed execution contract. We evaluate \textsc{Stage} on SOP-Bench Referral Abuse, two $τ^2$-bench domains, and Sma...
  </details>

- **2026-08-23** — Adrian Nyakairu, Hongfu Liu — [From Detrimental to Beneficial: Dynamic Influence-based Valuation and Editing](http://arxiv.org/abs/2608.22522v1)
  <details><summary>📄 Abstract</summary>
  Data valuation is a cornerstone of data-centric learning, where prior efforts primarily focus on designing algorithms to classify training samples as either beneficial or detrimental for the learning task. However, leveraging these valuation estimates for subsequent data intervention remains underexplored; conventional approaches typically discard or downweight harmful samples, thereby underutilizing available data resources. In this paper, we present Dynamic Influence-based Valuation and Editin...
  </details>

- **2026-08-23** — Philipp Steigerwald, Eric Rudolph, Jens Albrecht — [Nürnberg NLP @ GermEval Shared Task 2026: Harmful Content Detection in German Social Media through Error-Independent LLM Voters](http://arxiv.org/abs/2608.22246v1)
  <details><summary>📄 Abstract</summary>
  Harmful content in German social media does real-world damage, from calls to action to criminal defamation. The GermEval 2026 shared task scores its detection in four subtasks. The technical challenge is a severe class imbalance. The harmful classes are rare and share surface language with the dominant majority class, yet under macro-F1 they decide the score. The decisive lever is then not a stronger single model but error independence. This insight becomes a per-subtask nine-voter ensemble span...
  </details>

- **2026-08-22** — Laxmigayathri Challa, Yuhan Zhou, Ana Cleveland et al. — [Dissecting Neuro-Symbolic Quality Assurance for Synthetic Oncology Data Generation](http://arxiv.org/abs/2608.22085v1)
  <details><summary>📄 Abstract</summary>
  Synthetic clinical data generation with large language models addresses the scarcity that limits cancer staging research, but oncology hallucinations are categorically harmful: one clinically impossible staging assignment contaminates every downstream model trained on it. Neuro-symbolic pipelines validate during generation, yet the contribution of individual quality-assurance components remains unclear. We report three controlled studies isolating gate necessity, constraint attribution, and retr...
  </details>

- **2026-08-22** — Jiaqian Zhu, Yang Zhang, Junhua Ding et al. — [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](http://arxiv.org/abs/2608.22140v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) achieve strong reasoning performance, but their robustness to realistic lexical corruption remains poorly understood. We evaluate four open-weight instruction-tuned models and frontier models across four reasoning benchmarks under keyboard noise, character swaps, and filler insertion. Character-level perturbations substantially degrade accuracy, especially on multi-step reasoning tasks, while filler insertion has little effect. We trace this asymmetry to Attention Di...
  </details>

- **2026-08-21** — Zhibo Zhang, Zhen Ouyang, Ling Shi et al. — [RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models](http://arxiv.org/abs/2608.21236v1)
  <details><summary>📄 Abstract</summary>
  Representation engineering offers a lightweight means of controlling language-model behavior by modifying intermediate hidden states, but its direct application to Mixture-of-Experts (MoE) models introduces a structural mismatch. We first verify this failure mode through a series of empirical studies and find that preserving clean routing substantially recovers steering performance and that routing is more sensitive to semantic content than to behavioral changes under controlled content. Motivat...
  </details>

- **2026-08-21** — Pasquale Malacaria, Yunxiao Zhang — [Structured but Fragile: On the Limits of LLMs in Cybersecurity Decision-Making](http://arxiv.org/abs/2608.20966v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in cybersecurity workflows, yet it remains unclear whether they can perform structured security reasoning or merely rely on superficial cues and prior knowledge. We study this question in the context of defence selection over attack graphs derived from real-world threat scenarios, including ransomware, supply-chain compromise, cloud abuse, Kubernetes attacks, POS malware, and ICS/OT intrusion. Given a budget constraint, LLMs must select security...
  </details>

- **2026-08-21** — Chengxiao Wang, Enyi Jiang, Xiaojing Liao et al. — [CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment](http://arxiv.org/abs/2608.21278v1)
  <details><summary>📄 Abstract</summary>
  Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoi...
  </details>

- **2026-08-21** — Ruichen Yao, Tejna Dasari, Gulshat Baispay et al. — [Beyond Truth Discovery: A Two-Stage Framework to Assess the Severity of False Claim during Disasters](http://arxiv.org/abs/2608.20983v1)
  <details><summary>📄 Abstract</summary>
  False information spreads rapidly on social media during disasters and can undermine emergency response efforts, public trust, and crisis communication. Existing research primarily focuses on determining whether social media posts contain false information, but provides limited insight into the specific false claims embedded within posts and the severity of individual false claims. To address the limitations, we propose a two-stage framework to assess the severity of false claims during disaster...
  </details>

- **2026-08-21** — Huizu Lin, Chengkai Huang, Tianqi Gao et al. — [AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization](http://arxiv.org/abs/2608.21292v1)
  <details><summary>📄 Abstract</summary>
  Skills play different roles as an agent's policy evolves: they should first provide learnable knowledge, then support capability formation, and finally be invoked only when they improve individual decisions. Existing methods rarely model this lifecycle. They either keep skills outside the model, fully internalize them, or select among internalization and utilization objectives through noisy task-level success rates. Such designs fragment training and assign uniform importance to actions within t...
  </details>

- **2026-08-21** — Jiekang Feng, Zhihe Fan, Yunqi Zhu et al. — [A2DINOv3: Rethinking Multi-Modal Object Detection via Socialized Collaboration](http://arxiv.org/abs/2608.21099v1)
  <details><summary>📄 Abstract</summary>
  Multi-modal object detection is essential for robust scene understanding in challenging conditions, including low-light and adverse environments. Recent vision foundation models (e.g., DINOv3) have exhibited strong representation capabilities, yet adapting them to multi-modal scenarios remains challenging. Existing dense cross-modal fusion strategies often force heterogeneous modalities to interact indiscriminately, which may introduce redundant information and disrupt the valuable pre-trained r...
  </details>

- **2026-08-20** — Sahil Kale, Ian Harris — [ConceptGuard: Benchmarking Context-Sensitive Unlearning in Large Language Models](http://arxiv.org/abs/2608.20338v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly require selective removal of harmful or sensitive knowledge, called unlearning, yet existing methods and benchmarks fail to evaluate this capability completely. Current approaches rely on disjoint forget and retain sets composed of independent facts, and measure success using simple and direct factual recall. This framing fails to capture a key requirement of unlearning, namely the ability to eliminate harmful behaviors while preserving benign and benefi...
  </details>

- **2026-08-20** — Yejin Bang, Kirsty Fielding, Brandan Oliver et al. — [ContractScrub: A benchmark for final review of legal contracts](http://arxiv.org/abs/2608.20204v1)
  <details><summary>📄 Abstract</summary>
  Legal work, with its heavy reliance on processing large amounts of text, is often considered one of the domains most exposed to the use of LLMs. Contract ``scrubbing,'' the final review of transactional agreements for errors and inconsistencies, is a particularly suitable task for automation, because it is routine, painstaking work requiring detailed attention to long documents. Scrubbing also seems to align naturally with the general capabilities expected of frontier LLMs around long-context re...
  </details>

- **2026-08-20** — Mohamed Akrout, Olivera Kotevska, Dan Wilson — [Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics](http://arxiv.org/abs/2608.19579v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly deployed in high-stakes applications, yet their tendency to generate toxic, harmful, or policy-violating content poses significant risks. Detecting these unsafe outputs efficiently in a black-box manner remains an open challenge. In this paper, we extend a recently proposed dynamical systems framework designed for hallucination detection to LLM safety classification. By projecting both prompts and responses into high-dimensional embedding spaces and ...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-08-22** — Fidaa Abed, Haidar Khan, M Saiful Bari et al. — [Redteaming Leading Arabic LLMs with ASAS](http://arxiv.org/abs/2608.21985v1)
  <details><summary>📄 Abstract</summary>
  As the adoption of large language models (LLMs) grows in Arabic-speaking regions, ensuring their safety and cultural alignment is increasingly critical. However, Arabic LLM safety remains underexplored, especially in adversarial evaluation settings. We introduce the Arabic Safety Index (ASAS), the first fully human-curated Arabic benchmark for redteaming LLMs. ASAS contains 801 prompts spanning 8 safety categories and 8 attack strategies, with ideal responses in Modern Standard Arabic (MSA). We ...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 51 papers

- **2026-08-24** — Aldo Sean Sartor, Leandro de Souza Rosa, Andriy Enttsel et al. — [SVD-Based Typicality Maps for Out-of-Distribution Detection in Vision Transformers](http://arxiv.org/abs/2608.23499v1)
  <details><summary>📄 Abstract</summary>
  We present a method for analyzing the internal representations of Vision Transformers (ViTs) exploiting the geometry of their learned parameters. Each affine layer's weight matrix is factored via Singular Value Decomposition (SVD), and activations are projected onto the leading right singular vectors to obtain compact, layer-intrinsic representations. A class-conditional density model is then fitted at each layer, producing per-class \emph{typicality scores} that are stacked across depth into \e...
  </details>

- **2026-08-24** — Aldo Gangemi, Emanuele Bottazzi — [Walking on the DARKSIDE](http://arxiv.org/abs/2608.23370v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) recognise patterns but do not natively track the path of exclusions that a coherent discourse demands. When an input rests on a fabricated authority, a misapplied mechanism, or a surreptitious analogy, an unsteered LLM tends to engage with it as if it were grounded, and to reify the misstep into any structured output it generates. Logic-Augmented Generation (LAG) with POLANYI++, an LLM-steering method that uses heuristics, ontologies and problem solving methods for t...
  </details>

- **2026-08-24** — Haofeng Yuan, Jianing Peng, Jieyi Bi et al. — [FormuEvo: LLM-Guided Evolution for Discovering Solver-Efficient Mixed-Integer Programming Formulations](http://arxiv.org/abs/2608.23353v1)
  <details><summary>📄 Abstract</summary>
  Mixed-integer programming (MIP) lies at the core of operations research and industrial optimization. While large language models (LLMs) have recently shown promise in automated MIP modeling from natural language, they prioritize semantic correctness but overlook formulation strength, severely bottlenecking the efficiency of downstream solvers. We propose FormuEvo, an LLM-guided evolutionary framework for automated discovery of solver-efficient MIP formulations. FormuEvo frames MIP formulation de...
  </details>

- **2026-08-24** — Hong-Jun Yoon, Tom Ruggles, Joanna Lee et al. — [Retrieval-Augmented Classification of Environmental Mitigations in Hydropower Licensing Documents](http://arxiv.org/abs/2608.23241v1)
  <details><summary>📄 Abstract</summary>
  Identifying and classifying environmental mitigation obligations in Federal Energy Regulatory Commission hydropower licensing documents is a labor-intensive task requiring deep domain expertise. We formulate this as a multi-label classification problem over a structured 135-category taxonomy and address the central challenge of severe label scarcity: 40 of 135 categories have no training examples, and 26 have fewer than five. A supervised Bidirectional Encoder Representations from Transformers (...
  </details>

- **2026-08-24** — Jian Yang, Haau-Sing Li, Shawn Guo et al. — [CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild](http://arxiv.org/abs/2608.23181v1)
  <details><summary>📄 Abstract</summary>
  As large language models (LLMs) continue to advance in coding capabilities, their potential in cybersecurity has drawn increasing research attention, with closed-source LLMs (e.g., Mythos) delivering advanced cybersecurity capabilities. However, existing open-source efforts remain limited: frontier open-weight models do not provide reproducible cybersecurity training solutions, open-source training solutions focus on isolated tasks and lack scalable agentic data, and scaling agentic rollouts req...
  </details>

- **2026-08-24** — Xiangxin Zhang, Zhanwei Zhang, Zhihang Fu et al. — [From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation](http://arxiv.org/abs/2608.23045v1)
  <details><summary>📄 Abstract</summary>
  Web search agents powered by Large Language Models (LLMs) show strong promise, but deep research tasks expose a recurring failure mode: once an agent has produced a query, plan, or intermediate conclusion, it becomes less objective when later judging the consequences of that same action. We term this phenomenon \textbf{inertia bias}. To make it measurable, we introduce the IBIS benchmark, which controls the search observations while varying whether the model is evaluating the outcome of its own ...
  </details>

- **2026-08-24** — Tao Li, Yulin Tang, Qi Guo et al. — [SplitLite: Low-Rank Residual Compression for Split Learning](http://arxiv.org/abs/2608.23018v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning of on-device large language models (LLMs) faces a significant computing burden. To overcome this limitation, split learning (SL) has emerged as a promising solution, which offloads the primary training workload to a powerful server. However, SL requires exchanging high-dimensional activations and gradients between clients and the server, resulting in prohibitive communication costs. To overcome this challenge, we propose SplitLite, a communication-efficient split federated ...
  </details>

- **2026-08-24** — Yaoyao Xu, Xinjian Zhao, Xiaozhuang Song et al. — [Closed-Loop Bayesian Molecular Inverse Design with Semantic LLM Surrogates](http://arxiv.org/abs/2608.22967v1)
  <details><summary>📄 Abstract</summary>
  Practical molecular inverse design is rarely a one-shot generation problem; it often takes the form of closed-loop candidate-pool enrichment, where under a limited oracle budget the goal is to \emph{increase the fraction of generated molecules that match a desired property profile}. Bayesian optimization (BO) offers a natural framework for this setting, yet standard Gaussian-process surrogates typically operate in compressed continuous embeddings, which discard the substructural and reference-si...
  </details>

- **2026-08-24** — Kohei Yamamoto, Marie Katsurai — [Verification-Guided Specification Synthesis with Large Language Models for Intrusion Detection Rules](http://arxiv.org/abs/2608.22889v1)
  <details><summary>📄 Abstract</summary>
  Attacks against Internet-connected IoT devices continue to increase; however, transforming observed attack traffic into deployable intrusion detection system (IDS) rules remains largely a manual process. Recent studies have explored using large language models (LLMs) to generate IDS rules; nonetheless, existing approaches often require auxiliary information beyond observed traffic or generate rules without validating their detection logic against benign traffic. This study presents a verificatio...
  </details>

- **2026-08-24** — Yiyi Zhang, Ying Zheng, Wenxin Fan et al. — [Large-Small Model Collaboration for Zero-Shot Surgical Phase Recognition](http://arxiv.org/abs/2608.22879v1)
  <details><summary>📄 Abstract</summary>
  Task-specific lightweight models for surgical phase recognition excel at capturing temporal dynamics but generalize poorly under domain shift. Conversely, surgical foundation models (FMs) offer superior transferability via large-scale pretraining, yet their lack of explicit temporal modeling often yields temporally inconsistent predictions, leading to degraded performance. To exploit the complementary strengths of both paradigms, we propose \textbf{La}rge-\textbf{S}mall \textbf{T}emporal adaptat...
  </details>

- **2026-08-24** — Guhan Chen, Songtao Tian, Bohan Li et al. — [DIAG: Diagnostic Iterative Alignment and Generation for Data-Efficient Mathematical Preference Distillation](http://arxiv.org/abs/2608.22806v1)
  <details><summary>📄 Abstract</summary>
  Iterative preference optimization is essential for aligning Large Language Models on mathematical reasoning tasks, yet its efficiency is often throttled by signal scarcity: as the model improves, static problem sets become increasingly mismatched to the model's evolving competence, producing rollouts that are either too easy or too hard and therefore non-informative, which leads to a scarcity of valid preference pairs. We propose DIAG, a Diagnostic Iterative Alignment and Generation framework th...
  </details>

- **2026-08-23** — Nobel Dhar, Md Romyull Islam, Xuechen Zhang et al. — [NeuroPrefetcher: Storage-Aware Sparse LLM Inference via Delta Prefetching](http://arxiv.org/abs/2608.22643v1)
  <details><summary>📄 Abstract</summary>
  Deploying large language models on edge devices is increasingly limited by a widening gap between model size and available memory. Existing approaches such as quantization, smaller models, and offloading can raise the effective memory limit, but they still assume that the model can be compressed or partitioned to fit within some budget. We target the harder model-exceeds-memory setting, in which the model remains larger than resident memory throughout execution and storage becomes an active sour...
  </details>

- **2026-08-23** — Florian Rottach, Sebastian Schieferdecker, William Rudman et al. — [Mol-JEPA: A multimodal Joint Embedding Predictive Architecture for Molecules](http://arxiv.org/abs/2608.22642v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in molecular foundation models, several limitations remain, such as chemically invalid augmentations, modality collapse, and incomplete representation of biochemical environments. To address these challenges, we present \textbf{Mol-JEPA}, a scalable framework for learning molecular world models. Rather than relying on suboptimal molecular perturbations, our model uses modality masking to exploit information from molecular structures, cellular phenotypes, binding affinitie...
  </details>

- **2026-08-23** — Tina Massoudi, Chris Dutchyn — [VeGo: Direct Deductive Formal Verification of Go Programs for Computer Science Education](http://arxiv.org/abs/2608.22630v1)
  <details><summary>📄 Abstract</summary>
  As formal methods are rapidly becoming accessible and practical due to AI coding agents, priority passes to assisting developers and students in generating specifications. Leveraging native HMX/SSA verifiers provide that support with rigorous mathematical guardrails. We present VeGo (Verified Go), a deductive formal verification system that enables direct verification of standard Go source code. VeGo incorporates Hoare-style contracts, loop invariants and integer variants, well-founded recursive...
  </details>

- **2026-08-23** — Jie Liu, Lin Ma, Barzan Mozafari — [DAGSmith: Dependency-Aware Rewriting for dbt-Style SQL Pipelines](http://arxiv.org/abs/2608.22551v1)
  <details><summary>📄 Abstract</summary>
  Modern analytics is increasingly organized as recurring SQL pipelines rather than isolated SQL statements. Tools such as dbt, which have gained extreme popularity in recent years, allow teams to write each transformation as SQL and make dependencies between transformations explicit, producing directed acyclic graphs (DAGs) with hundreds or thousands of interdependent SQL models. Traditional query optimizers and source-to-source query rewriters operate on one query at a time, while materialized-v...
  </details>

- **2026-08-23** — Hossein Javidnia — [Functional compatibility as a determinant of persistent neural learning](http://arxiv.org/abs/2608.22462v1)
  <details><summary>📄 Abstract</summary>
  Artificial neural networks can acquire new capabilities but often damage existing ones when they continue to learn. This stability-plasticity problem has motivated replay, regularization and constrained-update methods, yet it remains unclear whether a property of incoming learning itself determines what can be retained without disrupting protected behaviour. Here we show that functional compatibility, the extent to which new learning can coexist with behaviour that must be preserved, is a causal...
  </details>

- **2026-08-23** — Zhanpeng Shi, Zi Liang, Rong Feng et al. — [Where World Models Break: Natural-Input Failure Discovery](http://arxiv.org/abs/2608.22421v1)
  <details><summary>📄 Abstract</summary>
  World models predict action-conditioned futures and serve as critical internal simulators for downstream planning and control. However, catastrophic prediction failures of world models could dangerously propagate through the control pipeline, as subsequent agent or model training and decision-making depend heavily on the continuous environment evolution forecasted by these world models. Existing evaluations overlook this systemic risk: by aggregating average errors over benign generations from g...
  </details>

- **2026-08-23** — Amin Hashemi, Abbas Shiri, Bahaa E. A. Saleh et al. — [Diagonalizing an optical coherence matrix via on-chip Stokes tomography](http://arxiv.org/abs/2608.22372v1)
  <details><summary>📄 Abstract</summary>
  Structured coherence -- partially coherent light spanned by a finite number of modes -- is emerging as a powerful tool in optical communications, computation, cryptography, and spectroscopy. Key to these prospects is the recent development of on-chip processing of structured coherence, in which large meshes of interferometers implement unitary and non-unitary transformations on the Hermitian coherence matrix representing multimode partially coherent light. Two related critical tasks for the appl...
  </details>

- **2026-08-23** — Han Zheng, Rafaila Galanopoulou, Ilia Shumailov et al. — [CodeMechanic: Bug-Property-Guided Program Mitigation](http://arxiv.org/abs/2608.22275v1)
  <details><summary>📄 Abstract</summary>
  Automated testing discovers vulnerabilities faster than developers can investigate and repair them, leaving an interval in which known memory corruptions remain exploitable. End- to-end LLM repair agents can shorten this interval, but they synthesize open-ended code changes and commonly validate them only by replaying a proof of concept (PoC). This weak oracle accepts patches that silence the observed crash by changing unrelated behavior, making unintended deployment risky.   We present CodeMech...
  </details>

- **2026-08-23** — Jiaao Yu, Yujian Ma, Xianming Hu et al. — [Training-Free VLM Personalization via Calibrated Residual Decoding](http://arxiv.org/abs/2608.22263v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models can be personalized in a training-free manner by directly providing user profiles, preferences, or visual references at inference time, without updating model parameters. However, direct personalized prompting does not guarantee that the model will reliably exploit such evidence. The predictive distribution under the positive user profile often mixes two sources: personalized signals genuinely supported by the current profile, and the model's generic visual or linguistic p...
  </details>

- **2026-08-23** — Xin-Dong Du, Tao Zhou, Wei Xiong et al. — [Extreme mass-ratio inspirals around rotating accelerating black holes](http://arxiv.org/abs/2608.22249v1)
  <details><summary>📄 Abstract</summary>
  Extreme mass-ratio inspirals (EMRIs) can magnify small departures from Kerr dynamics into appreciable gravitational-wave phase shifts accumulated over many orbital cycles. We exploit this sensitivity to investigate the imprint of a rotating black hole's acceleration on an EMRI waveform. The spinning C metric poses two obstacles to the standard Kerr flux framework: the spacetime is not asymptotically flat, and the acceleration breaks the reflection symmetry that supports exactly equatorial circul...
  </details>

- **2026-08-23** — Zhiming Yang, Zhuoxi Xiong, Donglin Zhou et al. — [Beyond What Meets the Eye: Unveiling Situational Illusions for Multimodal Large Language Models](http://arxiv.org/abs/2608.22232v1)
  <details><summary>📄 Abstract</summary>
  Real-world situation appearances can deviate from their underlying physical states, challenging the reliability of multimodal large language models (MLLMs) in practical applications. In this paper, we term this phenomenon situational illusions and investigate: (1) how MLLMs perform under such illusions, and (2) how to mitigate the limitations. We first develop a comprehensive where-what-how taxonomy that characterizes where situational illusions occur, what targets they take, and how they arise....
  </details>

- **2026-08-23** — Junyu Lu, Kaiyuan Liu, Jingyi Kang et al. — [Whitewashing Hate, Smearing Harmless Content: Annotator-Style Rebuttal Attacks on LLM-Based Moderation](http://arxiv.org/abs/2608.22230v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for hate speech moderation, often within human--AI workflows in which reviewers provide feedback before a final decision. Such feedback introduces two manipulation directions: whitewashing hateful content as normal and smearing normal content as hateful. This study examines the susceptibility of initially correct model judgments to annotator-style rebuttals and analyzes whether attack effectiveness differs across manipulation directions. We intr...
  </details>

- **2026-08-23** — Fanqi Kong, Huaxiao Yin, Ruijie Zhang et al. — [Grounded Normative Rule Generation with Structured Search](http://arxiv.org/abs/2608.22229v1)
  <details><summary>📄 Abstract</summary>
  Normative rules like institutional charters and workplace policies must be both human-readable and operationally verifiable against actual environment records. However, current language generation and structured-output benchmarks primarily reward surface fluency or schema compliance, leaving operational grounding weakly tested. This creates a critical vulnerability where standard language models generate plausible-sounding policies that fail during enforcement because they rely on unavailable da...
  </details>

- **2026-08-23** — Sudipta Paria, Aritra Dasgupta, Raghul Saravanan et al. — [Lessons from the Hardware Hacking Competitions: Verification Techniques, Findings, and Insights](http://arxiv.org/abs/2608.22202v1)
  <details><summary>📄 Abstract</summary>
  Hardware hacking competitions have emerged as practical platforms for evaluating security weaknesses in complex System-on-Chip (SoC) designs while promoting security-aware verification and tool development. This paper presents a systematic study of SoC security verification through open-box hardware hacking competitions, focusing on practical vulnerability analysis strategies, observed findings, and lessons for security-aware verification. We present a multi-strategy vulnerability analysis metho...
  </details>

- **2026-08-22** — Hojin Kim, Sujin Yoon, Sungsu Lim et al. — [Who Should Teach? Confidence-Aware Dual-Teacher Learning for Few-Shot Node Classification on Text-Attributed Graphs](http://arxiv.org/abs/2608.22127v1)
  <details><summary>📄 Abstract</summary>
  Text-Attributed Graphs (TAGs) integrate graph structures and node-associated textual attributes, and recent studies have increasingly leveraged Large Language Models (LLMs) to improve TAG learning in few-shot settings. However, existing approaches typically utilize LLM-derived information uniformly across all nodes, despite substantial variations in its reliability, while also incurring considerable monetary costs. We argue that the most appropriate source of supervision may differ across nodes,...
  </details>

- **2026-08-22** — Amit Roth, Ivan Bercovich, Yonathan Efroni — [Hack-Verifiable Terminal Bench: Evaluating Reward Hacking in Terminal Tasks](http://arxiv.org/abs/2608.22103v1)
  <details><summary>📄 Abstract</summary>
  As agents grow more capable and autonomous, their tendency to reward hack, satisfying a task's checks while violating its intent, becomes an increasingly important failure mode. Measuring reward hacking is itself challenging, as detection typically relies on human inspection or LLM judges, both of which can be unreliable. The hack-verifiable environments (HVE) methodology addresses this challenge by embedding detectable hacks into tasks, allowing reward hacks to be identified automatically and r...
  </details>

- **2026-08-22** — Jade Perdereau, Virginie Loison, Kanssa El Ayeb et al. — [ReMAP: Self-supervised learning to unveil brain representations and vulnerability](http://arxiv.org/abs/2608.22042v1)
  <details><summary>📄 Abstract</summary>
  General anesthesia offers a rare opportunity to observe the human brain under a standardized, controlled perturbation. Yet intraoperative electroencephalography (EEG) is almost always reduced to a single proprietary depth index, collapsing a rich trajectory into one number and discarding how a brain moves between states. Here we ask whether the geometry of that trajectory, not merely the depth it reaches, carries clinically meaningful information. Using similarity-based self-supervised learning ...
  </details>

- **2026-08-22** — Hyunwoo Kim, Byoungchan Ko, Minseok Kang et al. — [SSDi8: Accurate and Efficient 8-bit Quantization for State Space Duality](http://arxiv.org/abs/2608.21952v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in sequence modeling have highlighted Mamba as a state space architecture offering efficient long-range dependency modeling and providing a viable alternative to Transformers. Building upon this, Mamba-2 introduces the Structured State Space Duality (SSD), which integrates recurrent and attention modes to achieve efficiency and scalability. However, this architectural expansion substantially increases memory and latency overhead, underscoring the need for efficient compression st...
  </details>

- **2026-08-22** — Chenghao Zhang, Yikai Mao, Shanqi Liu et al. — [From Solver Feedback to Faithful Plans: Multi-Role Reinforcement Learning for Symbolic Planning](http://arxiv.org/abs/2608.21897v1)
  <details><summary>📄 Abstract</summary>
  Reliable planning requires converting natural-language instructions into executable symbolic specifications, yet large language models remain brittle without costly PDDL annotations and may exploit solver success in semantically unfaithful ways. We study how to learn faithful natural-language-to-PDDL formalization using only solver feedback, without human-written demonstrations. We propose a solvergrounded multi-role reinforcement learning framework where a single language model acts as an Actor...
  </details>

- **2026-08-22** — Shuyun Su, Shengshi Pang — [Noise-Symmetry Optimization of Quantum Error-Corrected Metrology](http://arxiv.org/abs/2608.21842v1)
  <details><summary>📄 Abstract</summary>
  Quantum error correction (QEC) codes have emerged as a powerful tool to protect quantum-enhanced metrology against noise. However, the ability to correct errors alone does not guarantee high metrological sensitivity, as the encoded states may become insensitive to the parameter of interest. Here we show that this limitation can be overcome by exploiting an intrinsic freedom of QEC codes: for a fixed set of correctable errors, the Knill-Laflamme conditions admit an equivalence class of encodings....
  </details>

- **2026-08-21** — Derek R. Benham, Joshua G. Mangelson — [The Coastline as a Structural Constraint: Harnessing Scene Geometry for Autonomous Surface Vessel Localization](http://arxiv.org/abs/2608.21276v1)
  <details><summary>📄 Abstract</summary>
  Coastal environments contain rich, largely unexploited geometric structure capable of providing globally referenced localization cues. In this work, we present two complementary localization frameworks that exploit shoreline and water-surface geometry for GPS-denied autonomous surface vessel localization. The first framework leverages LiDAR observations of the water surface to estimate roll, pitch, and heave (vertical motion), while recovering global position and heading through direct registrat...
  </details>

- **2026-08-21** — Jiayi Li, Sanjana Menon, Brett Frischmann et al. — [Affective Context Amplifies Sycophancy in LLM Responses](http://arxiv.org/abs/2608.21242v1)
  <details><summary>📄 Abstract</summary>
  As conversational companions, large language models (LLMs) often have access to users' emotional states. We study how this affective context modulates LLM sycophancy in subjective, evaluative interactions, where users share actions or opinions that invite feedback. Drawing on ingratiation theory, we measure sycophancy as the divergence between a model's independent evaluation and its user-facing response, elicited by presenting the same content as either a third-party account or the user's own d...
  </details>

- **2026-08-21** — Swetha Varadarajan, Darrell Whitley — [Fine-Grain GPU Parallelization of the Generalized Partition Crossover for Large-Scale Traveling Salesman Problems](http://arxiv.org/abs/2608.21233v1)
  <details><summary>📄 Abstract</summary>
  The Traveling Salesman Problem (TSP) is one of the most extensively studied NP-hard optimization problems. Genetic Algorithm (GA)-based solvers, such as the Edge Assembly Crossover (EAX), achieve state-of-the-art performance on many benchmark instances. However, the scalability of these approaches in massively parallel architectures remains limited because crossover operations involve irregular memory access patterns, graph traversals, and sequential dependencies. Existing GPU-based TSP solvers ...
  </details>

- **2026-08-21** — Tengteng Lei, Prabodh Katti, Rashi Dutt et al. — [Event-triggered Implicit Perturbation for Zeroth-Order Fine-Tuning of Spiking Transformers](http://arxiv.org/abs/2608.21223v1)
  <details><summary>📄 Abstract</summary>
  Zeroth-order (ZO) optimization estimates gradients using only forward-pass evaluations, making it suitable for fine-tuning non-differentiable, event-driven spiking neural networks (SNNs). However, its deployment on in-memory computing (IMC) accelerators is constrained by the repeated read-modify-write (RMW) operations arising from explicit weight perturbation and the prohibitive hardware footprint of random number generators (RNGs) for statistically independent per-weight perturbations. To addre...
  </details>

- **2026-08-21** — Varun Giridhar, Anant Khandelwal, Jeremy A. Collins et al. — [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](http://arxiv.org/abs/2608.21204v1)
  <details><summary>📄 Abstract</summary>
  Behaviour Cloning (BC) has driven remarkable progress in robot manipulation, yet it is fundamentally limited by its inability to self-improve: a policy that fails cannot learn from that failure without additional human demonstrations. Reinforcement Learning fine-tuning offers a path to self-improvement but has proven difficult to scale to the multi-billion-parameter models underpinning modern robot policies. We propose Q-Planning, which equips a large visuomotor BC policy with a small off-policy...
  </details>

- **2026-08-21** — Jie Xu, Na Zhao — [Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding](http://arxiv.org/abs/2608.21136v1)
  <details><summary>📄 Abstract</summary>
  Recently, open-vocabulary zero-shot 3D scene understanding using vision foundation models has emerged as a promising alternative to data-intensive supervised methods. However, deploying these models in real-world scenarios is severely hindered by their inability to efficiently handle streaming RGB-D inputs and their inherent vulnerability to noise 2D segmentation masks. To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D ...
  </details>

- **2026-08-21** — Wei Lin, Tao Zhou, Zhaofei Xie et al. — [Large Language Models at the Intersection of Software Engineering and Software Security:An Evidence-Centered Structured Survey and Research Agenda](http://arxiv.org/abs/2608.21107v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are moving from code completion toward repository-scale agents that retrieve context, edit files, execute tools, and participate in security-sensitive workflows. The evidence for these systems, however, remains divided between software engineering evaluations centered on functional task completion and software security evaluations centered on vulnerability detection, secure generation, or exploit-oriented validation. This evidence-centered structured survey synthesiz...
  </details>

- **2026-08-21** — Angel Mary John, Vipin Kumar Singh, Jerrin Thomas Panachakel — [Can Legal AI Know When It Is Wrong? And Do Students Know When It Is?](http://arxiv.org/abs/2608.21089v1)
  <details><summary>📄 Abstract</summary>
  Integrating Large Language Models (LLMs) into the Indian judiciary promises access to justice but introduces severe risks. We identify the 'inertia of confidence'--an overconfidence phenomenon analogous to the Dunning-Kruger effect where LLMs provide incorrect legal verdicts with near-maximum confidence, driven by a hypothesized 'precedent overfitting' bias. Phase I of our socio-technical audit tested ChatGPT (GPT-5.2), Meta AI, and Perplexity AI on a 60-case battery regarding the Indian Contrac...
  </details>

- **2026-08-21** — Yipeng Wei, Zahra Hoodbhoy, Emily R. Smith et al. — [Knowledge-guided Transfer Prediction In Underrepresented Populations: A GRU-D-Static Framework For Maternal And Neonatal Outcomes](http://arxiv.org/abs/2608.21073v1)
  <details><summary>📄 Abstract</summary>
  Integrating summary-level scientific knowledge into neural network models provides a practical strategy for transferring prediction models trained on adequately sampled source cohorts to underrepresented target populations, where individual-level data in the target domain are often limited or unavailable. In this study, we propose transfer prediction strategies incorporating external summary-level scientific knowledge and illustrate its application on the PRISMA Maternal and Neonatal Health Stud...
  </details>

- **2026-08-21** — Dojun Hwang, Seunghan Lee, Cheonyoung Park et al. — [Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders](http://arxiv.org/abs/2608.20801v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) have significantly advanced reranking in recommendation, effectively leveraging item-side information remains challenging. Real-world items are described by vast, heterogeneous, and unstructured metadata, where decision-relevant signals are often implicit, noisy, or buried in long descriptions. Moreover, feature salience is highly context-dependent, varying not only across items but also across users. Existing methods often rely on item titles, fixed attributes...
  </details>

- **2026-08-21** — Hui Lu, Zhijie Peng, Yuqi Lin et al. — [CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models](http://arxiv.org/abs/2608.20791v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) policies are vulnerable to localized physical perturbations, yet existing certified patch defenses target discrete labels and cannot directly certify continuous, temporally correlated actions. We introduce CertVLA, a certified defense for closed-loop VLA control under bounded patch and texture attacks. CertVLA proposes a calibrated region of behaviorally consistent actions, while deterministic covering masks ensure that at least one checked prediction is attack-free....
  </details>

- **2026-08-21** — Byeonggwon Lee, Sanggi Lee, Siwoo Lee et al. — [M2Depth: Unifying Monocular Depth Foundation Priors with Multi-View Stereo](http://arxiv.org/abs/2608.20788v1)
  <details><summary>📄 Abstract</summary>
  Deep learning-based Multi-View Stereo (MVS) has advanced significantly but often generalizes poorly to unseen scenes, particularly in occluded areas or regions with limited view overlap. To mitigate this, recent approaches integrate Depth Foundation Models (DFMs) into MVS pipelines to provide monocular depth priors. However, existing methods typically rely on a static, one-way fusion scheme, which fails to fully exploit the complementary strengths of both modalities. We propose a novel framework...
  </details>

- **2026-08-20** — Cheng Xu, Nan Yan, Liming Chen et al. — [Phantom Gains: Auditing Self-Improvement Against a Measured Null](http://arxiv.org/abs/2608.20290v1)
  <details><summary>📄 Abstract</summary>
  Whether a language model has improved itself is increasingly judged not by mean accuracy but by which individual problems it gains and loses. Tracking these transitions means differencing two noisy estimates, leaving them vulnerable to measurement artifacts. Auditing three rounds of rank-$32$ LoRA self-training on Qwen3-8B against a frozen control pushed through the identical pipeline, we identify seven measurement failures, each of which inverts a reported finding when its control is absent. Se...
  </details>

- **2026-08-20** — Laura M. Guzmán-Rincón, George R. E. Bradley, Joel Kandiah et al. — [GENIE: Generative Neural Inference for Epidemics](http://arxiv.org/abs/2608.20253v1)
  <details><summary>📄 Abstract</summary>
  The SARS-CoV-2 pandemic highlighted the ongoing risk infectious diseases pose to society and the value of reliable information on the likely future burden. When forecasting an epidemic at fine spatial resolution, traditionally used mechanistic compartmental model struggle to capture highly complex granular transmission dynamics, resulting in inaccurate and overconfident forecasts. However, detailed Agent-Based Models (ABMs), are challenging to calibrate and are too computationally expensive to u...
  </details>

- **2026-08-20** — Zhaokun He, Kangbiao Shi, Axi Niu et al. — [DPC-Net: Dual-Prior Collaborative Network for All-in-One Image Restoration](http://arxiv.org/abs/2608.20141v1)
  <details><summary>📄 Abstract</summary>
  All-in-One Image Restoration (AiOIR) aims to handle diverse degradations within a unified model. However, existing methods often overlook image semantics in degradation modeling and lack low-level visual priors during reconstruction, leading to structural distortions and semantic inconsistencies. To address these issues, we propose a novel Dual-Prior Collaborative Network (DPC-Net), which achieves high-quality restoration by jointly exploiting degradation-semantic coupled priors and low-level vi...
  </details>

- **2026-08-20** — Linhan Cao, Siyuan Li, Jun Lan et al. — [ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation](http://arxiv.org/abs/2608.20122v1)
  <details><summary>📄 Abstract</summary>
  Large multimodal models (LMMs) have demonstrated strong OCR recognition capabilities, yet remain vulnerable to adversarial visual text that is readable to humans but challenging for models to localize and recognize. Existing OCR benchmarks mainly focus on natural or document-style text, while adversarial OCR evaluations remain limited in scale, task coverage, or region-aware evaluation. In this paper, we formulate adversarial OCR as a \textbf{grounded OCR perception} task and introduce \textbf{A...
  </details>

- **2026-08-20** — Dayang Liang, Lang Feng, Bo An et al. — [SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning](http://arxiv.org/abs/2608.19842v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) and achieving strong performance on long-horizon interactive tasks. Despite their success, recent studies revealed three limitations: (1) Lack explicit value generalization and effective temporal credi...
  </details>

- **2026-08-20** — Yifei Sun, Yubing Li, Yannick Benezeth et al. — [Simulation-to-Real First-Break Segmentation for Efficient Inversion in Musculoskeletal Ultrasound Tomography](http://arxiv.org/abs/2608.19828v1)
  <details><summary>📄 Abstract</summary>
  Full-waveform inversion (FWI) is a promising strategy for quantitative musculoskeletal ultrasound computed tomography (USCT), but bone-related scattering, attenuation, and signal degradation make it highly sensitive to the accuracy of the initial acoustic-property distributions and prone to cycle skipping. First-arrival traveltimes provide important kinematic information for initial-model construction, yet conventional trace-wise picking is unreliable when arrivals are weak, spatially heterogene...
  </details>

- **2026-08-20** — Tenghui Huang, Jiawen Kang, Dongning Liu et al. — [Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models](http://arxiv.org/abs/2608.19680v1)
  <details><summary>📄 Abstract</summary>
  Smart contract vulnerability detection with Large Language Models (LLMs) faces three causally linked challenges. First, new vulnerability categories demand parameter-efficient adaptation, since full retraining is prohibitive for sequentially arriving tasks. Second, training per-task adapters on a shared backbone causes catastrophic forgetting of previously learned vulnerabilities. Third, the resulting multiplicity of adapters must be consolidated into a single model, since task identity is unkno...
  </details>

- **2026-08-20** — Shengshi Yao, Jincheng Dai, Sixian Wang et al. — [Loss-Resilient Semantic Communication over Packet-Loss Networks at Extreme-Low Bandwidth](http://arxiv.org/abs/2608.19590v1)
  <details><summary>📄 Abstract</summary>
  In extreme-low bandwidth network scenarios, generative semantic codecs have emerged as promising solutions to reduce bandwidth cost for visual communications. However, these learned codecs are usually optimized solely for compression efficiency and thus not robust against transmission errors. Corruptions due to packet-loss among these highly compact generative latent representations often cause more critical degradation in fidelity and realism, intensified by the severe error propagation across ...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 59 papers

- **2026-08-24** — Ting Yan — [When "Do Not" Is Not Deny: Security Rules in CLAUDE.md vs Built-In Controls](http://arxiv.org/abs/2608.23550v1)
  <details><summary>📄 Abstract</summary>
  In CLAUDE.md, "do not" is a natural-language instruction that the model interprets. Claude Code's deny is a built-in control that blocks an action before the agent can take it. Both can express the same security goal, but they control the agent in different ways. We measure this gap in 481 public CLAUDE.md files. An LLM matched the extracted candidate rules against Claude Code's documented controls, and two security practitioners independently checked a sample without seeing the model's answers ...
  </details>

- **2026-08-24** — Andrei Chetvergov, Stepan Ukolov, Timofei Sivoraksha et al. — [STONIC: A Layered Measurement Contract for LLM Value Profiling](http://arxiv.org/abs/2608.23411v1)
  <details><summary>📄 Abstract</summary>
  LLM value studies often merge questionnaire ratings, pairwise choices, and values inferred from generated text into one profile. That merge assumes that the three observations describe the same stable preference. STONIC tests this assumption on 5,144 situations from four banks and 35 fixed model configurations. It compares responses rated in isolation, choices made under counterbalanced conflict, spontaneous answers, and later choices between a model's own answer and authored alternatives. 10 of...
  </details>

- **2026-08-24** — Ruoyu Wu, Shenfu Xie, Yinqian Sun et al. — [MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical Interaction](http://arxiv.org/abs/2608.23397v1)
  <details><summary>📄 Abstract</summary>
  Interactive clinical agents must gather decisive evidence and convert it into grounded actions under partial observability. A correct final diagnosis alone does not show that an agent respected evidence and care-process constraints. We introduce MediSkill-Evo, a clinical agent that evolves governed process knowledge without backbone fine-tuning. It separates experience into four typed banks for clinical skills, process rules, symbolic schemas, and measurement procedures. Provenance, support, rep...
  </details>

- **2026-08-24** — Jessica Huntley, David McDonagh — [Enabling Organisational Change Through Ground-Up Initiatives: A Case Study from the STFC Scientific Computing Department](http://arxiv.org/abs/2608.23374v1)
  <details><summary>📄 Abstract</summary>
  Transforming digital research infrastructure (DRI) to align with UK Net Zero targets requires significant action from organisations in this space. Although high level strategies and recommendations exist, it is not always obvious how to translate these into concrete results. Here we present a case study from the Science and Technology Facilities Council's Scientific Computing Department (SCD). This department consists of over 200 staff supporting tens of thousands of researchers, and is spread o...
  </details>

- **2026-08-24** — Eugenia Moris, José Ignacio Orlando — [Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline](http://arxiv.org/abs/2608.23336v1)
  <details><summary>📄 Abstract</summary>
  Developing competitive deep learning baselines for medical imaging remains a highly iterative process requiring literature review, implementation, experimentation, and expert refinement. Existing automation approaches typically optimize isolated components, such as architecture search or hyperparameter tuning, rather than the complete baseline development process. We present an agentic AI Scientist workflow that combines literature-guided reasoning, automated code generation, and hypothesis-driv...
  </details>

- **2026-08-24** — Wenqi Liu, Shijie Ma, Yunxiao Wang et al. — [Thinking Beyond Videos: Unifying Video Reasoning and Deep Research for Open-World Video Agents](http://arxiv.org/abs/2608.23329v1)
  <details><summary>📄 Abstract</summary>
  Open-world video understanding often requires a model to locate sparse visual evidence and acquire external knowledge that is absent from the video and its parametric memory. While Thinking-with-Videos enables active temporal perception and Deep Research supports multi-step information seeking, the two capabilities are typically developed in isolation. We introduce VideoRover, a unified Video Deep Research framework that iteratively coordinates video cropping, multimodal search, and webpage brow...
  </details>

- **2026-08-24** — Arther Tian, Alex Ding, Simon Wu et al. — [FIDES: A Concordance Protocol for LLM-Generated Trading Strategies](http://arxiv.org/abs/2608.23308v1)
  <details><summary>📄 Abstract</summary>
  An LLM asked for a trading strategy returns three artifacts at once: a natural-language rationale, an executable implementation, and once run, a track record. Whether these are the same object is rarely checked. We present FIDES, a measurement protocol that treats them as three views to be reconciled rather than one deliverable to be graded. Through dual delivery, a single model call returns both a natural-language strategy with an explicit claimed edge and a self-contained strategy(df) function...
  </details>

- **2026-08-24** — Ergi Senja, Seyed Mohammad Reza Razavi Zadegan, Philipp Leitner — [ARGUS: MCP-Grounded Root Cause Analysis for Kubernetes Incidents](http://arxiv.org/abs/2608.23084v1)
  <details><summary>📄 Abstract</summary>
  Kubernetes incident triage requires correlating signals from metrics, logs, container state, and messaging systems across multiple monitoring tools, a fragmented workflow that slows diagnosis and contributes to alert fatigue. Large language models (LLMs) have shown promise for automated root cause analysis (RCA), but existing systems rely on custom, system-specific data access layers that cannot be reused across organisations. We present ARGUS, an MCP-grounded RCA assistant that connects a comme...
  </details>

- **2026-08-24** — Yi Zhu, Xiongwei Wu, Qiyi Wang et al. — [MobilePA-Bench: Benchmarking Mobile Planner Agents on Complex Real-World Tasks](http://arxiv.org/abs/2608.23035v1)
  <details><summary>📄 Abstract</summary>
  As on-device LLM agents evolve into personal copilots, the mobile operating system has become a key testbed for this paradigm, making rigorous capability evaluation essential. Yet existing benchmarks fall into two camps, each with a critical blind spot: GUI-centric benchmarks test surface-level screen manipulation while overlooking background tool use and long-horizon planning, whereas static function-calling benchmarks rely on offline API matching that is detached from real runtime constraints....
  </details>

- **2026-08-24** — Guan-Hua Wen, Kuan-Yu Chen — [Do Time-Series Foundation Models Pay Off for Industrial Monitoring? A Cost-Aware Empirical Study](http://arxiv.org/abs/2608.22968v1)
  <details><summary>📄 Abstract</summary>
  Industrial monitoring models must detect operationally relevant deviations while satisfying target-specific data, calibration, and resource constraints. Time-series foundation models (TSFMs) promise reusable representations and zero-shot forecasts, yet evidence for their deployment value remains mixed when task definitions are heterogeneous and lightweight baselines are competitive. This work presents a protocol-aware empirical assessment across three settings: a C-MAPSS degradation-risk proxy, ...
  </details>

- **2026-08-24** — Yongjeong Oh, Zihan Chen, Timothy J. O'Shea et al. — [Rethinking the Foundations of Two-Sided AI Models for 6G](http://arxiv.org/abs/2608.22918v1)
  <details><summary>📄 Abstract</summary>
  For next-generation air interfaces, two-sided artificial intelligence (AI) models have received growing attention, with AI models deployed at both the transmitter and receiver for efficient channel feedback and data communication. However, their practical deployment is complicated by assumptions commonly made in existing studies, including isolation from legacy users, training under predefined channel conditions, and gradient-based fine-tuning requiring substantial cross-vendor communication. Th...
  </details>

- **2026-08-24** — Aamir Mahmood, Nho Duc Tran — [React or Predict? A Spectral Rule for Wireless Threshold Detection](http://arxiv.org/abs/2608.22900v1)
  <details><summary>📄 Abstract</summary>
  A wireless sensor must alert a remote monitor before a monitored process crosses a safety threshold; an alarm arriving afterward may be too late. The sensor can react to its current estimate or predict ahead and trigger earlier, but the value of such lookahead is not obvious. In some systems it creates an early-alarm opportunity unavailable to the current test, while in others it cannot cross the alarm boundary. This letter gives a practical three-stage rule for deciding when to predict. First, ...
  </details>

- **2026-08-24** — Libin Liu, Wenzhou Yang, Li Chen et al. — [The Surprising Effectiveness of LLMs in BGP Security: Mining An Unprecedented Amount of Incidents and Boosting Anomaly Detection](http://arxiv.org/abs/2608.22812v1)
  <details><summary>📄 Abstract</summary>
  Border Gateway Protocol (BGP) security is critical to Internet infrastructure, yet progress in routing anomaly detection has been limited by the scarcity of publicly available incident datasets, which contain only 18 recorded cases. We observe that public operator mailing lists, e.g., NANOG and AusNOG, contain abundant yet largely untapped reports of real-world routing anomalies. To leverage this source, we develop an LLM-assisted extraction pipeline that identifies 244 candidate incidents from ...
  </details>

- **2026-08-24** — Tianqi Xu, Lu Lv, Haoyang Huang et al. — [TailSieve: Partial-Rollout-Guided Tail Routing for LLM Rollouts](http://arxiv.org/abs/2608.22788v1)
  <details><summary>📄 Abstract</summary>
  Large-scale rollouts have become a core component of modern LLM systems, spanning reinforcement learning (RL) post-training, on-policy distillation (OPD), and sampling-heavy evaluation pipelines. Unlike online serving, which is typically optimized for request-level latency and throughput, a small number of long-tail generations can dominate the end-to-end makespan of an entire rollout step. In practice, rollout requests are often routed uniformly across replicas, which can place extremely long g...
  </details>

- **2026-08-24** — Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder et al. — [Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time](http://arxiv.org/abs/2608.22761v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models generate text autoregressively, but open-ended generation is prone to verbatim looping, in which models repeat spans already present in context. Standard defenses such as repetition, presence, and frequency penalties and n-gram blocking act on token recurrence rather than the sequential structure of a loop, and often suppress looping only at strengths that also degrade formatting or fluency. We propose Don't Repeat Yourself (DRY), a sampling-time logit adjustment that penal...
  </details>

- **2026-08-24** — Jiaqi Liu, Maolin Ran, Xiaoyang Lu et al. — [SEAM: Shot Entity-Attribute Memory for Consistent Short-Drama Generation at Scale](http://arxiv.org/abs/2608.22725v1)
  <details><summary>📄 Abstract</summary>
  Short-drama generation has grown into a large, industrialized pipeline, and as it scales from isolated shots to the episode level, visual continuity has become a critical bottleneck. Current agent frameworks generate each shot in isolation, so context drifts across shots and props, character posture, and blocking turn inconsistent. Once assembled, these small discrepancies amplify into severe visual breaks. We present SEAM (Shot Entity-Attribute Memory), a training-free, model-agnostic memory gr...
  </details>

- **2026-08-24** — Marek Hradil, Danae Sánchez Villegas — [What's the Catch? Evaluating Temporal Consistency in Vision-Language Models](http://arxiv.org/abs/2608.23474v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) achieve strong performance on video and image-sequence benchmarks, yet it remains unclear whether they capture temporal structure. To study this question, we formulate temporal grounding as an anomaly detection problem, providing a simple and controlled evaluation that directly tests sensitivity to temporal consistency. We introduce TimeCatch, where temporal anomalies are created by swapping consecutive frames and frame-level anomalies by replacing a frame with Gaus...
  </details>

- **2026-08-24** — Abhilash Nandy, Rahul Seetharaman, Aman Bansal et al. — [CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension](http://arxiv.org/abs/2608.23172v1)
  <details><summary>📄 Abstract</summary>
  Large-scale vision-language models (VLMs) have demonstrated remarkable versatility across a wide range of multimodal tasks. However, understanding humor remains challenging because humorous content often depends on subtle interactions among entities, events, context, and implicit relationships across image and text modalities. These interactions can involve complex chains of reasoning that are difficult to capture through conventional prompting or linear chain-of-thought reasoning. In this work,...
  </details>

- **2026-08-24** — Christian Grashei, Fabian Gülhan, Maximilian Legnar et al. — [An end-to-end-trained vision-language model for native-language prostate pathology report generation](http://arxiv.org/abs/2608.23143v1)
  <details><summary>📄 Abstract</summary>
  Prostate cancer is among the most frequently diagnosed malignancies worldwide, and structured reporting of each biopsy core burdens pathologists. Existing tools frame this as classification, leaving pathologists to assemble coherent reports, while many slide-level vision-language models rely on English-centric encoders that transfer poorly to other clinical languages. We present a slide-level framework generating prostate biopsy reports that is language-independent by construction: tokenizer and...
  </details>

- **2026-08-24** — Martin Wessel, Timo Spinde, Jürgen Pfeffer et al. — [Definitional Sensitivity in Media Bias Detection: A Multi-Definition Dataset and Benchmark](http://arxiv.org/abs/2608.23095v1)
  <details><summary>📄 Abstract</summary>
  Media bias detection relies on definitions and examples that specify what counts as bias, yet these specifications often vary across datasets or remain implicit, even when given the same name. Such variation makes it unclear whether models trained for the same bias category learn the same construct or different phenomena, a problem largely overlooked in prior work. We examine how definition choice affects bias annotation in a between-subjects experiment with 354 participants and a parallel evalu...
  </details>

- **2026-08-24** — Md. Asaduzzaman Shuvo, Ahsan Farabi, Md. Abdul Ahad Minhaz et al. — [WADE: A Reasoning-Annotated Benchmark for Multi-Instance Floating-Waste Grounding with Compact Vision-Language Models](http://arxiv.org/abs/2608.22950v1)
  <details><summary>📄 Abstract</summary>
  Floating waste in inland waterways threatens aquatic ecosystems and requires timely monitoring under cluttered, multi-object conditions. Existing aquatic-waste datasets provide limited geographic coverage, sparse multi-instance annotations, and little supervision beyond boxes and labels. Compact vision-language models (VLMs) therefore remain insufficiently evaluated for jointly localizing, classifying, counting, and explaining floating waste. We introduce WADE, a reasoning-annotated benchmark co...
  </details>

- **2026-08-24** — Sosmita Paul, Krishna Roy — [GuidedFlow: An Attention-Guided Framework for Anomaly Detection in Additive Manufacturing](http://arxiv.org/abs/2608.22789v1)
  <details><summary>📄 Abstract</summary>
  Additive Manufacturing (AM) plays a vital role in the ongoing industrial revolution. However, quality control remains crucial and challenging due to printing defects or potential cyber-physical intrusions. Image or video-based anomaly detection is a key effort towards addressing these challenges. Various approaches have been explored in this domain, including reconstruction-based, embedding-based, and flow-based methods. Though normalizing flow-based methods address some of the core challenges o...
  </details>

- **2026-08-24** — Jianan Wei, Guikun Chen, Zhiyuan Weng et al. — [Hyperbolic Hierarchical Clustering for Visual Representation Learning](http://arxiv.org/abs/2608.22665v1)
  <details><summary>📄 Abstract</summary>
  We investigate the token mixer in vision backbones by revisiting clustering, one of the most classic approaches in machine learning. An effective token mixer is a fundamental component of modern vision backbones like vision Transformers, facilitating information exchange between image patches. Mainstream token mixers, which rely on convolution, attention, MLP, or their hybrids, primarily focus on navigating the trade-off between accuracy and computational cost. However, a significant drawback of...
  </details>

- **2026-08-23** — Isotta Magistrali, Chen Shani — [Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations](http://arxiv.org/abs/2608.22444v1)
  <details><summary>📄 Abstract</summary>
  The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and in...
  </details>

- **2026-08-23** —  UniverseTBD,  :, Kshitij Duraphe et al. — [What AstroPT knows about galaxies, and what that can teach us about LLMs](http://arxiv.org/abs/2608.22614v1)
  <details><summary>📄 Abstract</summary>
  Interpretability research increasingly asks when concepts emerge during training and whether linear probes recover real structure, but in language models these claims are hard to validate because language offers little ground-truth ordering of concepts or relationships among them. We propose the use of astronomical ground truth through AstroPT, a transformer trained on millions of galaxy images, as a calibration testbed. AstroPT is an LLM-like model trained within a domain where the difficulty o...
  </details>

- **2026-08-23** — Bhumika Bhattacharyya, Shouvik Kumar Guha, Indranil Dutta — [Figurative Justice: Detecting metaphors in Hindi judgements with qualitative assessment and transformers](http://arxiv.org/abs/2608.22446v1)
  <details><summary>📄 Abstract</summary>
  Metaphors are figurative use of words for conceptual mapping. Metaphor detection in the legal context has been crucial as metaphors are persuasive juridical means of creating legal meaning and concepts resulting in significant consequences. Metaphorical framing in legal discourse by judges, lawyers, and legislators brings about real-time implications upon individuals and influences judicial decision-making, argumentation and interpretation of laws. This is crucial in Human Rights infringement ca...
  </details>

- **2026-08-23** — Mohamed Bayan Kmainasi, Ali Ezzat Shahroor, Elisa Sartori et al. — [ProBel: Propaganda Detection with Techniques, Spans, and Explanations](http://arxiv.org/abs/2608.22388v1)
  <details><summary>📄 Abstract</summary>
  Propaganda detection includes several related prediction levels, ranging from sentence-level decisions to technique classification and span identification. However, it remains unclear how supervision at these levels interacts when learned jointly across Arabic and English. We present ProBel, an Arabic and English resource that aligns binary labels, multi-label annotations over 23 propaganda techniques grouped into six coarse categories, technique-labeled spans, and reference explanations for the...
  </details>

- **2026-08-23** — Masoud Jalayer, Changyi Li, Yu Xiao — [Pre-Decoding Acoustic Triage for Budgeted Vision-Language Captioning of Untrimmed Egocentric Video](http://arxiv.org/abs/2608.22359v1)
  <details><summary>📄 Abstract</summary>
  Automatically analyzing hours-long egocentric video is increasingly essential for progress monitoring, quality control, and safety in logistics, construction, and manufacturing. Yet current pipelines that process short, fixed-size windows with a vision-language model (VLM) are prohibitively expensive because cost scales with the number of model calls. To reduce this cost, prior work proposes triage policies to select which windows merit a VLM invocation. However, these policies either sample uni...
  </details>

- **2026-08-23** — Aditya Somasundaram — [Toward a First-Principles Update Geometry for the Language-Model Head](http://arxiv.org/abs/2608.22253v1)
  <details><summary>📄 Abstract</summary>
  We study the language-model head and softmax as a single module, deriving an update geometry from their composition rather than from the weight matrix in isolation. Under Hilbert's projective distance, the maximum change caused by an update $S$ over $\left|\left|{h}\right|\right|_2\le H$ is $H\max_{i<j}\left|\left|{s_i-s_j}\right|\right|_2$, which is $H$ times the Euclidean diameter of its token rows. Motivated by Muon's singular-value conditioning, we propose maximizing the smallest row separat...
  </details>

- **2026-08-23** — Yilin Li, Yifei Zhang, Guozhu Meng — [AdaptPrint: Response-Adaptive Fingerprinting of Black-Box LLM Services](http://arxiv.org/abs/2608.22213v1)
  <details><summary>📄 Abstract</summary>
  Black-box LLM services have emerged as a practical deployment paradigm. Nevertheless, their opacity also hinders the systematic assessment of security risks and complicates copyright auditing for model owners. Black-box LLM fingerprinting, which identifies the underlying LLM identity through query-response interactions, offers a promising way to bridge this gap. Existing approaches typically collect responses from target LLM services using a fixed set of queries and perform poorly in the presenc...
  </details>

- **2026-08-22** — Md. Rakibul Hassan, Muhammad Iqbal Hossain — [BanglaVeilGuard: Cross-Script Safety Benchmarking and Lightweight Guardrails for Bangla Large Language Models](http://arxiv.org/abs/2608.21880v1)
  <details><summary>📄 Abstract</summary>
  Bangla large language model (LLM) safety is difficult to evaluate with English-centric or standard-script benchmarks because Bangla users routinely write across scripts, spellings, code-mixed forms, and regional registers. This paper presents BanglaVeilGuard, a compact Bangla-first safety benchmark and lightweight prompt guard for six language forms: standard Bangla, Romanized Bangla, Banglish, code-mixed Bangla--English, noisy Bangla, and dialectal Bangla. The benchmark contains 2,366 quality-f...
  </details>

- **2026-08-22** — Maraz Mia, Shovan Roy, Mir Mehedi A. Pritom et al. — [ExplainGuard: A Zero Trust Framework for Post-Hoc Explanation Integrity Guarantees in Blackbox XAI Models](http://arxiv.org/abs/2608.21803v1)
  <details><summary>📄 Abstract</summary>
  As machine learning (ML) models are increasingly deployed in high-stakes environments, explainable AI (XAI) methods like SHAP and LIME have become essential for regulatory compliance and trust. However, the current auditing paradigm relies on an implicit "chain of trust" where third-party auditors are assumed to be trusted. Recent research demonstrates that this assumption is flawed and adversarial auditors can manipulate XAI explanations through manipulation attacks such as output shuffling or ...
  </details>

- **2026-08-22** — Yating Fang, Jungmin Kim, Qian Qian Zhao et al. — [Cross-Temperature Defect Identification in Atomistic Simulations via Multi-Level Domain Alignment](http://arxiv.org/abs/2608.22074v1)
  <details><summary>📄 Abstract</summary>
  Identifying atomic defects at elevated temperature is difficult because thermal fluctuations blur the local symmetry that both geometric heuristics and supervised classifiers rely on: trustworthy labels exist in low-temperature reference configurations, while the high-temperature regime where robust analysis matters most is effectively unlabeled. We cast this as a cross-temperature domain-shift problem and align the two domains at three levels: an equivariant denoiser at the input level, cross-t...
  </details>

- **2026-08-22** — Weicai Long, Yusen Hou, Houcheng Su et al. — [GenomeHarness: Harnessing Al Agents for Reliable Adaptation of Genome Language Models](http://arxiv.org/abs/2608.21916v1)
  <details><summary>📄 Abstract</summary>
  Pretrained genome language models provide reusable representations for DNA sequence analysis, but turning them into reliable downstream predictors remains non-trivial. Their practical performance depends strongly on fine-tuning recipes, and default recipes reported in prior studies may be suboptimal for new tasks or model backbones, making weak downstream results difficult to interpret. These requirements place a substantial operational burden on many intended users, whose expertise is often cen...
  </details>

- **2026-08-22** — Ao Chen, Xiaojiang Peng — [HiMA-MDD: A Hierarchical Multi-Agent Harness for Interpretable Multimodal Depression Detection in Clinical Interviews](http://arxiv.org/abs/2608.21868v1)
  <details><summary>📄 Abstract</summary>
  Depression assessment from multimodal clinical interviews requires integrating dispersed evidence from multiple symptoms into a coherent PHQ-8 profile. This process is hierarchical: relevant evidence is often sparse and context-dependent within local question-answer exchanges, multiple exchanges jointly support symptom-level judgments, and the final assessment depends on the coherence of the complete symptom profile. Existing LLM systems either process interviews holistically or distribute work ...
  </details>

- **2026-08-22** — Md Abrar Jahin, Md Rizwan Parvez — [GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding](http://arxiv.org/abs/2608.21832v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents ground natural-language instructions in screenshots to locate interface elements, yet existing benchmarks do not isolate whether models bind relational language to the correct element. We introduce GUI-Primitives, a 994-item benchmark of contrastive instruction pairs over seven spatial relations in graphical user interfaces (left/right, above/below, containment, alignment, proximity, list ordinal, occlusion). Each pair holds the screenshot and anchor fixed while changing the ...
  </details>

- **2026-08-21** — Sunder Ali Khowaja, Kapal Dev, George C. Alexandropoulos — [$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open 6G RAN](http://arxiv.org/abs/2608.21049v1)
  <details><summary>📄 Abstract</summary>
  With the progression in open and disaggregated 6G radio access networks, it is expected that the system will be able to host multi-vendors. In order to host multi-vendors, it is essential that AI-assisted control loops remain safe, verifiable, and auditable under concurrent operator intents and untrusted model inputs. The existing studies address the agentic coordination, formal intent constraints, zero-trust prompt verification and cryptographic accountability in isolation, which leaves pre-rea...
  </details>

- **2026-08-21** — Qisheng Lu, Aoyang Fang, Junjielong Xu et al. — [Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis](http://arxiv.org/abs/2608.21310v1)
  <details><summary>📄 Abstract</summary>
  Existing evaluations of automated root cause analysis (RCA) for microservices assess diagnostic performance mainly by endpoint correctness: whether a method localizes the responsible service. This criterion enables comparison but does not reveal the evidentiary basis of a diagnosis or the fault-propagation route connecting the source to observed symptoms, both of which an on-call site reliability engineer needs to judge whether action is warranted. We therefore treat RCA as an observable diagnos...
  </details>

- **2026-08-21** — Matthew Faucher — [TRACE-C: Rank-Calibrated Relational Anomaly Detection for Multi-Stream Operational Telemetry](http://arxiv.org/abs/2608.21251v1)
  <details><summary>📄 Abstract</summary>
  Operational telemetry can be jointly anomalous while every individual stream stays inside its familiar range. TRACE-C is an auditable strictly-prior rank-calibrated detector for aligned multi-stream telemetry: same-regime rolling median/MAD residuals feed three window channels -- a maximum normalized local sum, a Gaussian copula-form dependence contrast on robust-z residuals, and a worst standardized AR(1) innovation -- whose channel ranks are Fisher-aggregated and ranked against earlier aggrega...
  </details>

- **2026-08-21** — Tonglin Yan, Gregoire Sergeant-Perthuis, David Rudrauf — [Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models](http://arxiv.org/abs/2608.20975v1)
  <details><summary>📄 Abstract</summary>
  Effective social interaction requires agents to translate mental state inferences into coordinated behavioral signals across verbal and nonverbal channels simultaneously. Yet existing benchmarks evaluate theory of mind (ToM) reasoning and embodied behavior in isolation, leaving unmeasured the gap between social inference and social action. We introduce MOSAIC (Multimodal Orchestration of Social Action, Inference, and Communication), a controlled benchmark in which two embodied agents interact ac...
  </details>

- **2026-08-21** — Haozhen Yan, Siyuan Shan, Zijian Yu et al. — [GAP-SAM: A Global Artifact Prior for Generalizable AI-Generated Image Manipulation Localization](http://arxiv.org/abs/2608.20929v1)
  <details><summary>📄 Abstract</summary>
  AI-generated image manipulation localization identifies edited pixels, but its OOD performance lags behind image-level detection partly because pixel supervision entangles forensic evidence with dataset-specific mask geometry and semantic boundaries. Extending image-level distribution alignment to localization, we construct COCO-ControlNet with source-image Canny edges and depth maps to align semantics and geometry, improving OOD performance across multiple localizers. Yet tighter Mask-VAE Recon...
  </details>

- **2026-08-21** — Qifeng Zhang, Ting Xiang, Zeyuan Bai et al. — [Semantically Compatible Knowledge Distillation for Cross-Domain Object Detection with Vision Foundation Models](http://arxiv.org/abs/2608.20916v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models (VFMs) offer strong generalization capabilities for domain-adaptive object detection (DAOD). However, existing VFM-based methods overlook the spatial-scale discrepancy between teacher and student feature maps, resulting in semantic incompatibility that weakens both feature alignment and pseudo-label learning. Moreover, domain shift can cause source-trained VFM teachers to miss target-domain objects, limiting the quality of their pseudo-labels. To address these issues, we...
  </details>

- **2026-08-21** — Luiz Giacomossi, Zafer Yigit, Marwan Shakarna et al. — [A Safety-Driven Architectural Framework for Fail-Operational Drone Swarms in Critical Missions](http://arxiv.org/abs/2608.20906v1)
  <details><summary>📄 Abstract</summary>
  The certification of Unmanned Aerial Vehicle (UAV) swarms for safety-critical operations requires verifiable design assurance. Airworthiness standards demand deterministic reliability, whereas multi-agent coordination algorithms execute non-deterministic models. This paper proposes a mixed-criticality architectural framework that applies SAE ARP4754B methods to swarm reconfiguration. First, a hardware-isolated Safety Monitor functions as a Run-Time Assurance (RTA) gateway, decoupling the flight-...
  </details>

- **2026-08-21** — Meda Lazar, Sourab Sridhar, Shashwata Gupta et al. — [Multi-Modal Traffic Sign Detection with Semantic Attributes for Autonomous Driving](http://arxiv.org/abs/2608.20874v1)
  <details><summary>📄 Abstract</summary>
  Reliable traffic sign detection is a prerequisite for the global deployment of autonomous driving systems, where regulatory compliance and road safety depend on perceiving signs correctly across regions, ranges, and weather conditions. Despite recent progress, vision-based methods continue to face three fundamental limitations: poor cross-regional generalization due to high diversity across countries, degraded performance on small-object detection at long ranges (traffic signs occupy as little a...
  </details>

- **2026-08-21** — Giovanna Broccia, Julian Frattini, Chetan Arora et al. — [Human-AI Collaboration in Requirements Engineering: Evidence of the Negative Effect of LLMs on Requirements Inspection](http://arxiv.org/abs/2608.21298v1)
  <details><summary>📄 Abstract</summary>
  Background. Requirements inspection (RI) is a well-established practice for detecting potential defects in requirements artifacts early in the software lifecycle. Recent advances in large language models (LLMs) have stimulated interest in their potential to support requirements engineering (RE) tasks. However, empirical evidence on the effects of LLMs when used as collaborative assistants in human-performed RI remains scarce. Aims. We aim to investigate the impact of LLM support on human-perform...
  </details>

- **2026-08-21** — Percy Brown, Kweku Yamoah — [Invisible Agents, Uninformed Patients: Towards Responsible Deployment Of Autonomous AI Diagnostic Agents In Sub-Saharan Africa](http://arxiv.org/abs/2608.21326v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI diagnostic agents, systems that analyse patient-specific clinical data and produce diagnostic outputs or triage decisions without mandatory real-time human review, are increasingly deployed across eHealth platforms in sub-Saharan Africa at a pace that has outrun the governance infrastructure needed to oversee them. While significant bodies of work address AI accountability, transparency and explainability in healthcare, existing frameworks are largely clinician-centered and assume ...
  </details>

- **2026-08-21** — Inpyo Song, Jangwon Lee — [A VLM Answer Is Not an Anomaly Score: Rank Compression in Training-Free Video Anomaly Detection](http://arxiv.org/abs/2608.21244v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models enable training-free video anomaly detection by answering questions about video segments. VAD benchmarks, however, require a scalar anomaly score for each segment and evaluate the resulting ranking using the AUROC or AP. A VLM-based detector should therefore define an answer interface: the answer scale specifies the admissible answers, and the readout rule maps the model's output distribution to a score. Because this interface can change the evaluated ranking, it is part o...
  </details>

- **2026-08-20** — Shangbo Yuan, Jie Xu, Xiaofeng Zhu et al. — [Open-Vocabulary 3D Object Detection with Co-Distillation Discovery and Dual Guidance Robust Training](http://arxiv.org/abs/2608.19973v1)
  <details><summary>📄 Abstract</summary>
  Recently, open-vocabulary 3D object detection (3D-OVD) has gained increasing attention for its ability to detect unseen objects in 3D scenes. Existing approaches typically adopt a two-stage pipeline that first discovers novel objects using foundation models and then trains a 3D-OVD model based on these discovered objects. Although effective, this pipeline often suffers from inaccurate localization and mismatched classification during the discovery stage, which subsequently limits the performance...
  </details>

- **2026-08-20** — Denesa Zyberaj, Roman Vintonyak, Pascal Hirmer et al. — [A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications](http://arxiv.org/abs/2608.19752v1)
  <details><summary>📄 Abstract</summary>
  Testing embedded software in modern vehicles is challenging due to system complexity, decentralized architectures, and strict safety and performance constraints. In this work, we present an end-to-end, deployment-aware testing pipeline for IoT-based automotive applications. The pipeline combines requirement-driven test and code generation with large language model (LLM) and vision-language model (VLM) assistance, and human-in-the-loop curation to reduce manual effort and improve consistency. Usi...
  </details>

- **2026-08-20** — Zhuochun Li, Youngmin Ko, Ali Keramati et al. — [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents in Stateful Business Workflows](http://arxiv.org/abs/2608.19741v1)
  <details><summary>📄 Abstract</summary>
  Recent agent benchmarks increasingly ground evaluation in executable environments, from code repair to web navigation, app APIs, and function calling. Yet completing consequential work beyond code requires more than producing a plausible response or valid tool call: agents must gather missing information over multiple turns, follow domain policies, coordinate dependent tools, and realize the correct persistent state transition without collateral effects. In this paper, we introduce Thinkingbox, ...
  </details>

- **2026-08-20** — Mohammad Arif Ul Alam — [Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions](http://arxiv.org/abs/2608.19710v1)
  <details><summary>📄 Abstract</summary>
  Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation...
  </details>

- **2026-08-20** — Alexei Kaltchenko, Gurnivaj Tiwana — [ChatGPT Solves All Tested Qiskit Homework Assignments](http://arxiv.org/abs/2608.19707v1)
  <details><summary>📄 Abstract</summary>
  Generative AI creates an assessment challenge in quantum software education: a student can provide a homework notebook to ChatGPT and request a completed submission. This study examined whether introductory Qiskit homework could remain autogradable while requiring students to run, review, and discuss results rather than banning AI. Three packages were tested: seeded basis-state circuits with bit flips and customized measurement mappings; Quantum Fourier Transform followed by inverse-transform re...
  </details>

- **2026-08-20** — Yujun Chen, Tianle Li, Jiayu Chen et al. — [An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design](http://arxiv.org/abs/2608.19699v1)
  <details><summary>📄 Abstract</summary>
  In this paper, a bio-robot is an engineered living or biohybrid system in which living cells perform one or more core functions, such as sensing, information processing, actuation or output. We focus on systems whose cell-based functions are programmed by genetic circuits; physical movement is optional. Designing such a system requires translating application requirements into sensing, logic or memory, output, assembly, host and containment modules, while grounding each choice in traceable parts...
  </details>

- **2026-08-20** — Xizhou Bu, Qingda Hu, Lei Zhou et al. — [What Matters for Latent Actions in Robot Learning](http://arxiv.org/abs/2608.19613v1)
  <details><summary>📄 Abstract</summary>
  Latent Action Models (LAMs) have emerged as a promising paradigm for enabling robot learning to leverage large-scale unlabeled videos through latent actions that serve as compact surrogates for physical actions. Despite rapid progress, research on LAM remains highly fragmented, with existing methods evaluating different design choices in isolation under inconsistent experimental settings, making it difficult to identify the factors that truly determine downstream robotic manipulation performance...
  </details>

- **2026-08-20** — Xinyi Liu, Hooshang Nayyeri, Dilek Hakkani-Tur et al. — [Hear2Act: Benchmarking When Prosody Should Change What an Assistant Does](http://arxiv.org/abs/2608.19515v1)
  <details><summary>📄 Abstract</summary>
  Prosodic cues can convey task-relevant information that alters the trajectory and outcome of a task-oriented dialogue, even when the words themselves remain unchanged. Yet existing benchmarks typically evaluate prosodic perception, response appropriateness, and task-oriented dialogue in isolation, making it difficult to test whether prosodic evidence changes downstream decisions. We introduce Hear2Act, a unified evaluation protocol for text and spoken assistants with 480 persona-grounded scenari...
  </details>

- **2026-08-20** — Parampreet Singh, Anushka Singh, Sumit Kumar et al. — [$TCP_α$: Margin-Controlled Confidence estimation for reliable Music Information Retrieval](http://arxiv.org/abs/2608.20326v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are often overconfident, assigning high confidence even to incorrect predictions. Consequently, users lack a reliable signal for deciding when a prediction can be trusted. Post-hoc confidence estimation addresses this by training a lightweight auxiliary head over a frozen classifier. Existing targets, however, suffer from inherent ambiguity: they assign overlapping confidence values to correct and incorrect predictions, while errors near the decision boundary receive confide...
  </details>

- **2026-08-20** — Alexander Nemecek, Osama Zafar, Debargha Ganguly et al. — [Auditing Cross-Lingual Fairness in Language Model Watermarking](http://arxiv.org/abs/2608.20047v1)
  <details><summary>📄 Abstract</summary>
  Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that dis...
  </details>

- **2026-08-20** — Christopher Henshaw, Gour Karmakar — [From Noise to Signal: Improving Security Log Anomaly Detection Using LLMs with Endpoint-Specific Logs](http://arxiv.org/abs/2608.19938v1)
  <details><summary>📄 Abstract</summary>
  Existing approaches to anomalous behaviour log detection, such as Wazuh rely primarily on predefined detection rules, while statistical anomaly detection approaches such as OpenSearch identify deviations from previously observed behavioural patterns. Recent research has investigated LLMs for log anomaly detection because of their ability to interpret semantic and contextual information. However, LLM-based approaches can be affected by prompt construction, noisy log data, and reliance on generic ...
  </details>

- **2026-08-20** — Georg Kordowich, Jonathan Loebel, Julian Oelhaf et al. — [A simulation based dataset of faults and events for machine learning in power systems](http://arxiv.org/abs/2608.19777v1)
  <details><summary>📄 Abstract</summary>
  The integration of inverter-based renewable energy sources into electric grids challenges conventional power system protection. Machine learning-based solutions can address these challenges by utilizing available data in modern smart grids. However, the lack of open datasets prevents reproducibility and fair comparisons between different approaches and their results, which hinders further progress. Therefore, this paper presents EvEMTBench, a synthetic dataset of faults and events generated usin...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 57 papers

- **2026-08-24** — Miriam Wanner, Mark Dredze, William Walden — [On the Threat Model of Weird Generalization and Emergent Misalignment](http://arxiv.org/abs/2608.23476v1)
  <details><summary>📄 Abstract</summary>
  Narrow fine-tuning on small, domain-specific datasets can produce broad and surprising changes in model behavior-a phenomenon called weird generalization (WG). Yet, it remains unclear what features of the fine-tuning data are necessary for WG to arise. Here, we address this question by investigating a range of plausibly relevant features, including dataset size, composition, language, presentation style, and novelty relative to a model's parametric knowledge. Further, since WG evaluations rely o...
  </details>

- **2026-08-24** — Nan Duan, Haoyang Huang, Weiyang Jin et al. — [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](http://arxiv.org/abs/2608.23383v1)
  <details><summary>📄 Abstract</summary>
  Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts. We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants. The long-video variant introduces composable cross-shot memory that aggregates visual evidence across multiple prior shots and speaker cues derived from speech-filtered full-shot audio, en...
  </details>

- **2026-08-24** — Matteo Attimonelli, Claudio Pomo, Alessandro De Bellis et al. — [Grounding Free-Form Instructions for Fashion Complementary Image Generation](http://arxiv.org/abs/2608.23302v1)
  <details><summary>📄 Abstract</summary>
  Fashion complementary image generation (CIG) aims to create garments that stylistically match a seed item based on user intent, making it a natural multimodal grounding problem where models must interpret language in visual context. Existing CIG benchmarks rely on rigid template prompts (e.g., "a photo of a skirt"), failing to reflect natural user queries and obscuring model behavior across levels of linguistic specificity. We introduce fashion complementary image generation with free-form instr...
  </details>

- **2026-08-24** — Ruoxuan Li, Bruce Kogut — [Dynamic Topic Modeling for Cross-Corpus Temporal Analysis](http://arxiv.org/abs/2608.23284v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Embedded Topic Models (D-ETM) provide an interpretable framework for modeling temporal semantic evolution, but cross-corpus comparison remains difficult because topics are often learned independently and aligned only after training, a process that does not guarantee stable topic correspondence across corpora and time. To address this problem, we propose a D-ETM framework that first learns a common dynamic topic space over a merged multi-corpus collection, which we call the shared backbon...
  </details>

- **2026-08-24** — Gustavo Penha, Juan Elenter, Claudia Hauff et al. — [The Disconnect Between Better Descriptive Reasoning Trace Quality and Recommendation Effectiveness](http://arxiv.org/abs/2608.23154v1)
  <details><summary>📄 Abstract</summary>
  Recent work has focused on improving explicit natural-language descriptive reasoning traces for generative recommendation. This includes systems that augment semantic ID (SID) prediction with chain-of-thought reasoning. However, because SIDs are opaque learned identifiers rather than natural language, they require costly alignment before an LLM can reason over them. This provides a controlled experimental setting in which both item representation (Title vs. SID) and semantic grounding (minimal v...
  </details>

- **2026-08-24** — Seungyoon Lee, Minhyuk Kim, Jungseob Lee et al. — [Language Chain in Alignment: Cross-Lingual Ranking Preference Optimization](http://arxiv.org/abs/2608.23149v1)
  <details><summary>📄 Abstract</summary>
  The alignment of Large Language Models heavily relies on English-centric high-quality preference data, which often leads to suboptimal performance in other languages. In this paper, we propose Cross-Lingual Ranking Preference Optimization (CRPO), a novel framework that leverages robust preference knowledge from English to facilitate preference alignment in the target language. We design a hierarchical structure within parallel preference pairs across the target language and English to jointly op...
  </details>

- **2026-08-24** — Xunlei Chen, Qinghui Gong, Ruini Xue et al. — [ST$^2$U: Stateful Test-Time Unlearning via Restricted Knowledge Boundary Control](http://arxiv.org/abs/2608.23034v1)
  <details><summary>📄 Abstract</summary>
  Controlling restricted knowledge in large language models is essential for model alignment and safe deployment. Test-time unlearning avoids costly retraining and parameter updates by intervening only during inference. However, existing activation-editing methods apply isolated pointwise corrections, overlooking how autoregressive generation continually reconstructs hidden states from the prompt, cache, and generated prefix. Consequently, later states may return to restricted knowledge regions af...
  </details>

- **2026-08-24** — Nico Hessenthaler, Adam T. Müller, Nicolaj C. Stache — [Simplified Cross-Modal Calibration for Heterogeneous Event-RGB Stereo Systems](http://arxiv.org/abs/2608.22965v1)
  <details><summary>📄 Abstract</summary>
  Accurate extrinsic calibration between event-based and frame-based cameras remains a practical bottleneck for heterogeneous stereo systems. Existing approaches often require sensor or target motion, precise synchronization, or computationally expensive event-to-image reconstruction. We propose a simple, motion-free cross-modal calibration framework that uses a temporally modulated, blended ChArUco target presented on standard consumer displays. By alternating between the original pattern and a p...
  </details>

- **2026-08-24** — Huiling Yang, Zhanwei Wang, Kaibin Huang — [AirMoE: Realizing Over-the-Air Distributed Mixture-of-Experts Inference at the Wireless Edge](http://arxiv.org/abs/2608.22932v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-experts (MoE) architectures enable efficient large language model (LLM) inference at the wireless edge by reducing per-token computation through sparse expert activation. The wireless distributed MoE (WIDE) architecture addresses edge-device resource constraints by distributing computation-intensive experts across devices coordinated by an edge server. However, repeated uploads of high-dimensional expert outputs over orthogonal multiple access create a severe uplink bottleneck. To ove...
  </details>

- **2026-08-24** — Hyeonyu Kim, Hwayeon Kim, Youngwon Choi et al. — [Do Spoken Language Models Hear Speech as They Read Text? Bridging Structural Gaps Between Speech and Text](http://arxiv.org/abs/2608.22908v1)
  <details><summary>📄 Abstract</summary>
  Spoken Language Models (SLMs) generate textual responses directly from speech, offering an alternative to cascaded systems. Despite recent advances, existing SLMs still exhibit weaker instruction-following behavior and limited generalization across diverse tasks compared to text-based language models. Our analysis shows that speech and text representations in current SLMs remain weakly aligned despite strong downstream performance, indicating that structural differences between continuous, tempo...
  </details>

- **2026-08-24** — Yujie Qi, Luyan Zhang — [DRAgent: Discriminative Reasoning Agent for Referring Expression Segmentation](http://arxiv.org/abs/2608.22885v1)
  <details><summary>📄 Abstract</summary>
  Referring Expression Segmentation (RES) aims to generate a pixel-level mask for the object specified by a language expression. Recent methods based on multimodal large language models (MLLMs) often rely on one-pass coordinate prediction for visual localization, which serializes continuous spatial locations as discrete text tokens and may lead to localization bias and alignment errors. To address these issues, we propose DRAgent, an MLLM-driven discriminative reasoning (DR) framework for RES. Ins...
  </details>

- **2026-08-24** — Yan Zhou, Sara Kangaslahti, Jonathan Geuter et al. — [Thinking at the Right Size: Amortized Distillation Across Post-Trained LLMs](http://arxiv.org/abs/2608.22854v1)
  <details><summary>📄 Abstract</summary>
  Practical deployment of large language models (LLMs) requires families of post-trained variants---instruction-tuned, reasoning-tuned, and chat-style models---each at multiple sizes to meet diverse latency and memory budgets. Producing each (variant, size) pair independently is prohibitive, so model families typically span only a handful of coarse-grained sizes per post-trained variant. Boomerang distillation (Kangaslahti et al., 2026) reduces this cost along the size axis for base models. Throug...
  </details>

- **2026-08-24** — Qichao Ma, Jikang Cheng, Ling Liang et al. — [Can We Perform Online RL for Image Editing without Editing Rewards?](http://arxiv.org/abs/2608.22780v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables direct preference optimization for image editing through editing-specific rewards, which remain less developed due to costly triplet supervision and complex task-dependent calibration. In contrast, text-to-image (T2I) generation benefits from a mature and diverse reward ecosystem spanning semantic alignment, aesthetics, realism, glyph shape, and other visual preferences. Extending this ecosystem to image editing would substantially broaden the range of visual ...
  </details>

- **2026-08-24** — Qinfei Li, Xiaoxuan Dong, Jin Zhang et al. — [Risk-Aware Reranking for Agentic Tool Retrieval](http://arxiv.org/abs/2608.22751v1)
  <details><summary>📄 Abstract</summary>
  Tool retrieval determines which external tools are exposed to an LLM agent for a user query or task, making retrieval a critical pre-execution safety boundary. Unlike document retrieval, tool retrieval exposes executable actions: a tool that is useful for one task may be unnecessary or risky for another. However, existing tool-retrieval methods primarily optimize semantic relevance, and safety evaluations often focus on failures after tool execution rather than risks introduced during retrieval....
  </details>

- **2026-08-24** — Nishanth Chidambaram, Kaustubh Paliwal, Kayla Hom et al. — [AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations](http://arxiv.org/abs/2608.22702v1)
  <details><summary>📄 Abstract</summary>
  AI-generated personas are being increasingly used for support, training and simulations. While generative AI models possess abilities to generate affect-aware responses, their embodiment into visual personas is an active area of investigation. Naturalistic exchanges require understanding of the conversational partners' turn completions, whether the agent should respond or keep listening and rely on non-verbal cues aligned with one's emotional states. Seamless human-AI conversation in a multimoda...
  </details>

- **2026-08-24** — Yuxuan Yang, Jingyao Wang, Luntian Mou — [Mind the Couch! Eliciting MLLM Reasoning in Interior Design via Weak-to-Strong Task Vector Injection](http://arxiv.org/abs/2608.23242v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated great performance, yet they often suffer from severe modality misalignment when confronted with densely constrained spaces for interior design. Due to the loss of high-frequency local topological details and fine-grained aesthetic shifts during visual encoding, existing MLLMs frequently hallucinate, yielding physical spatial collisions and visual aesthetic dissonance. To address this, we propose Dual-prior Activation Residual Task-vector...
  </details>

- **2026-08-23** — Meenu Ravi, Shailik Sarkar, Lulwah AlKulaib et al. — [GeoRisk-RAG: A Hierarchy-Aware Risk Framework for Improving RAG Reliability through Selective Answering](http://arxiv.org/abs/2608.22634v1)
  <details><summary>📄 Abstract</summary>
  Current work on improving reliability in large language model (LLM)- generated answers has primarily leveraged Retrieval-Augmented Generation (RAG), knowledge-graph augmentation, and reinforcement learning. While these methods are adept at enhancing and measuring reliability through semantic similarity and faithfulness, they often struggle to distinguish semantic similarity from geographic validity. This is especially critical in natural hazard management domains where geographic granularity (i....
  </details>

- **2026-08-23** — Naoya Kumagai, Kenshiro Oguri — [On the Optimality of Markovian Policies for Chance-Constrained Covariance Steering](http://arxiv.org/abs/2608.22589v1)
  <details><summary>📄 Abstract</summary>
  Many studies on finite-horizon stochastic optimal control, including covariance steering, parameterize control policies as state-history-affine. This parameterization enables a convex reformulation, thereby yielding a tractable solution method. However, the necessity of dependence on previous states has not been well established. \textit{Is this dependence necessary, or merely an artifact of the convex reformulation?} We show that it is an artifact that can be removed losslessly. Given an optima...
  </details>

- **2026-08-23** — Julia Romberg, Tobias Gummer, Gabriella Lapesa et al. — [Hybrid Panels: Toward Human-AI Collaboration in Survey Research](http://arxiv.org/abs/2608.22582v1)
  <details><summary>📄 Abstract</summary>
  Large-scale population surveys are essential for generating robust social and scientific insights, yet they face significant challenges, including declining response rates, increasing data collection costs, long delays between data collection and data provision, and the risk of nonresponse bias. Advances in artificial intelligence (AI) have opened up new opportunities for AI-supported survey infrastructures where the goal is to overcome these challenges without limiting the data quality. A promi...
  </details>

- **2026-08-23** — Hossein Shahabadi, Niki Sepasian, Mahdieh Soleymani Baghshah — [VISTA: Test-Time Compositional Alignment for Visual Autoregressive Generation](http://arxiv.org/abs/2608.22521v1)
  <details><summary>📄 Abstract</summary>
  Visual autoregressive (VAR) models have emerged as a fast, high-quality alternative to diffusion for text-to-image generation, but like diffusion models they exhibit persistent compositional failures, producing images that violate the attribute bindings and spatial relations specified in the prompt. While a rich line of test-time alignment methods has developed for diffusion, no comparable approach exists for next-scale VAR generation, whose stateful, discrete, multi-resolution sampling process ...
  </details>

- **2026-08-23** — YuanHang Xiao — [ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts](http://arxiv.org/abs/2608.22510v1)
  <details><summary>📄 Abstract</summary>
  Agent benchmarks often evaluate only final answers even when agents run on stateful runtimes. We argue this under-specifies what is being evaluated: the proper unit is a declared model-plus-runtime configuration whose failures can occur in evidence acquisition, runtime routing, safety boundaries, or repeated execution. We present ClawProBench, a trace-aware benchmark for runtime-native agent evaluation instantiated on OpenClaw, a live agent runtime with workspace tools and native surfaces for br...
  </details>

- **2026-08-23** — Leonardo Bergmann, Renata Gheorghiu, Ana Gvritishvili et al. — [LLMs for Survey Text Analysis - A Performance Comparison Between Humans and GPT-5 on Inductive Content Analysis](http://arxiv.org/abs/2608.22417v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to support text analysis in qualitative research, yet evidence on their performance in inductive content analysis remains limited. This study compares human and LLM-based inductive coding of open-ended survey responses from 903 answers across six variables from a European PhD student survey. Five human coders performed inductive content analysis following a standardized coding scheme, while an LLM (GPT-5.4) conducted the same task using an estab...
  </details>

- **2026-08-23** — Chongyuan Dai, Yaling Shen, Shengeng Tang et al. — [Don' t Box Me In: Dynamic Cultural Adaptation and Cognitive Tracking for Social Understanding](http://arxiv.org/abs/2608.22411v1)
  <details><summary>📄 Abstract</summary>
  Social interaction increasingly takes place in multicultural settings, where individuals may draw on multiple cultural influences and adapt their communicative behavior across contexts. Despite recent advances in equipping Large Language Models (LLMs) with social understanding capabilities, existing approaches often model culture as a static demographic attribute, limiting their ability to accommodate hybrid and dynamically expressed communicative preferences. Therefore, in this paper, we propos...
  </details>

- **2026-08-23** — Zhenhao Shen, Jiaqi Liang, Jasper Lu et al. — [LD4WAM: Learning Latent Dynamics from Human Videos for World Action Models](http://arxiv.org/abs/2608.22403v1)
  <details><summary>📄 Abstract</summary>
  Human video is playing an increasingly central role in training World Action Models (WAMs), owing to its diversity and low collection cost relative to teleoperated robot data. However, most WAMs learn from such video only by predicting pixel-level future frames, giving dynamics that are not directly actionable, whereas motion retargeting recovers directly actionable actions but leaves a large visual gap across embodiments. We therefore propose motion-aligned latent dynamics as an embodiment-agno...
  </details>

- **2026-08-23** — Sumaih Almarshad, Maram Alamri, Dona Aloraini et al. — [Does a Modern-Handwriting Warm-Up Help Historical Arabic OCR? A Reproducible, Compute-Matched Evaluation on Muharaf and KHATT](http://arxiv.org/abs/2608.22316v1)
  <details><summary>📄 Abstract</summary>
  Whether an intermediate stage of modern Arabic handwriting helps or hurts historical Arabic HTR is usually decided from one implementation and one comparison, too thin a basis for a claim either way. We test stability by running the same nominal ablation four times, letting the base checkpoint, encoder-freezing strategy, epoch budget, precision, and learning-rate schedule vary as they naturally did during development, while holding the normalization, scorer, and interval estimation fixed. Each r...
  </details>

- **2026-08-22** — Nura Aljaafari, Andre Freitas — [Align, Unify, Suppress, Route: A Coherentist View of Transformer Computation](http://arxiv.org/abs/2608.22034v1)
  <details><summary>📄 Abstract</summary>
  Mechanistic interpretability has identified transformer circuits, but lacks a shared vocabulary for describing how their functions compose across tasks and architectures. We introduce Coherentist Probabilistic Compositionalism (CPC), an interpretive framework that grounds transformer computation in coherentist theories of interpretation and describes it through four operator roles. Alignment identifies candidate relations, unification integrates supporting information, suppression reduces incomp...
  </details>

- **2026-08-22** — Oleg Miroshnichenko — [Gated Decoupled Compositional Bandits: A Unified Theory of Contextual Bandits with Supervised-Calibrated Action Scaling and Pre-Execution Gating](http://arxiv.org/abs/2608.21993v1)
  <details><summary>📄 Abstract</summary>
  We introduce Gated Decoupled Compositional Bandits (GDCB), a family of contextual bandit algorithms with three structural innovations that jointly fall outside the taxonomy of LinUCB, LinTS, HierTS, factored bandits, neural contextual bandits, and RLHF. In a GDCB system: (i) the action delivered to the environment is the composition of a nominal arm, drawn by a discrete or hierarchical bandit, with a context-dependent scaler; (ii) the scaler parameter is learned in a separate supervised loop, no...
  </details>

- **2026-08-22** — Weichu Liu, Yuxuan Hu, Yirong Sun et al. — [ESCRAG-R1: Retrieval-Augmented Reinforcement Learning for Emotional Support Conversation](http://arxiv.org/abs/2608.21925v1)
  <details><summary>📄 Abstract</summary>
  Emotional Support Conversation (ESC) systems aim to provide holistic support by balancing professional therapeutic competence with natural empathy. However, existing methods struggle to simultaneously achieve structured, stage-aware reasoning and seamless empathy-expertise alignment, often resulting in an artificial splicing of clinical strategies and generic reassurance. To overcome these limitations, we propose ESCRAG-R1, a unified framework that integrates retrieval-based psychological guidan...
  </details>

- **2026-08-22** — Qian Zha, Jinda Liu, Yuan Wu et al. — [CD-LoRA: Consistency-Driven Low-Rank Adaptation for Multi-Task Fine-Tuning](http://arxiv.org/abs/2608.21909v1)
  <details><summary>📄 Abstract</summary>
  While Multi-Task Learning (MTL) is essential for adapting Large Language Models (LLMs) to diverse domains, prevailing LoRA-based methods rely on complex routing mechanisms that partition task-specific knowledge. In this work, we reveal that such routing-based designs are prone to a training-inference discrepancy, where stochastic routing decisions under distribution shifts compromise inference stability. Driven by a second-order Taylor analysis that exposes the instability induced by routing var...
  </details>

- **2026-08-22** — Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu et al. — [FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling](http://arxiv.org/abs/2608.21839v1)
  <details><summary>📄 Abstract</summary>
  Reliable reward models are essential for text-to-video evaluation and alignment. However, the trade-off between evaluation accuracy and inference efficiency places high demands on the quality of training supervision. Existing approaches often rely on holistic judges with fixed rubrics or open-ended reasoning, leading to incomplete inspection, unfaithful justification, and entangled attribution. We introduce FIRM-Video, a unified checklist-driven data construction framework based on a check-befor...
  </details>

- **2026-08-22** — Md Asaduzzaman Jabin, Zihao Wu, Tianming Liu — [BioMed-Agent-RL: A Meta Learning, All You Need for Biomedical Applications](http://arxiv.org/abs/2608.21864v1)
  <details><summary>📄 Abstract</summary>
  The current progress of Clinical Vision Large Language Models (C-VLLMs) has substantially improved digital diagnostics, still these frameworks often endure lesion noises, modality misalignment, hallucination, and missed contextual grounding in complex clinical cases. Moreover, prevailing agent systems usually depend on static and non-adaptable pipelines and lack the versatility necessary for complex medical reasoning. To resolve these difficulties, we present BioMed-Agent-RL, a unified medical a...
  </details>

- **2026-08-22** — Shuang Hao, Jiacheng Yue, Yaxuan Zhao et al. — [Through the Schrödinger Bridge: Benchmarking Antemortem Image Restoration from Postmortem Autolysis to Enhance Forensic Diagnostics](http://arxiv.org/abs/2608.21813v1)
  <details><summary>📄 Abstract</summary>
  Forensic histopathology, essential for determining cause of death and disease diagnosis, is severely impeded by postmortem autolysis, i.e., an irreversible, stochastic degradation process that distorts tissue morphology and introduces diagnostic subjectivity, thereby underscoring the value of restoring autolyzed images to a diagnostically plausible, pre-autolysis state for improving objectivity in forensic practice. This restoration task is fundamentally challenging due to the large, non-determi...
  </details>

- **2026-08-21** — Afonso Baldo, Hugo Pitorro, Areti Vassilopoulos et al. — [Move by Move: Measuring and Steering How LLMs Conduct Psychotherapy](http://arxiv.org/abs/2608.21325v1)
  <details><summary>📄 Abstract</summary>
  Users increasingly turn to large language models for emotional support, yet little is known about how these models actually conduct a psychotherapy interaction. We introduce an ontology of ten therapeutic moves: compact, function-based categories grounded in the MULTI-60 inventory, validated through an annotation campaign with five licensed psychologists, and scaled with a judge-based approach that matches expert agreement. Applying it to real counseling transcripts and model-led sessions, we co...
  </details>

- **2026-08-21** — Marko Haralović, Sounic Akkaraju, Carlo Baretta et al. — [When Adaptation Hurts: Connecting Representational Drift to OOD Failures in MedSAM Fine-Tuning](http://arxiv.org/abs/2608.21300v1)
  <details><summary>📄 Abstract</summary>
  Foundation models for medical image segmentation, like prompt-based MedSAM, generalize well across domains and modalities, often in zero or few-shot setups. However, their performance depends on the quality of prompts and the adaptation of the models to custom datasets. This work systematically examines how MedSAM generalizes across diverse medical imaging benchmarks, with six adaptation strategies: full-model and encoder-only LoRA, shallow and deep visual prompt tuning (VPT), and decoder-only a...
  </details>

- **2026-08-21** — Congsheng Xu, Qiaochu Yang, Fangyuan Shi et al. — [VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation](http://arxiv.org/abs/2608.21290v1)
  <details><summary>📄 Abstract</summary>
  We propose VT-MUSE, a Multimodal Unified SEquential representation learning framework for visuotactilemanipulation. Existing approaches often encode visual and tactile observations independently before fusion, limiting their ability to capture fine-grained cross-modal dependencies. Moreover, most methods focus on observations at the current time step and overlook the temporal evolution of contact. VT-MUSE addresses both limitations through a two-stage representation learning framework. In Stage ...
  </details>

- **2026-08-21** — Peiqi Yu, Nam Ling, Wei Wang et al. — [COEC: Calibrated Orthogonal-Equivalence Compensation for Structured Pruning of Large Language Models](http://arxiv.org/abs/2608.21142v1)
  <details><summary>📄 Abstract</summary>
  Structured pruning reduces the size and inference cost of large language models (LLMs) by removing weight columns, but the resulting output error can degrade accuracy. Existing training-free compensation methods use an additive bias or a single orthogonal rotation on the output side of the retained weight. These corrections leave its input singular frame unchanged and therefore limit how the retained weight can adapt after column removal. We propose COEC (Calibrated Orthogonal-Equivalence Compen...
  </details>

- **2026-08-21** — Erik Thureck, Robert Kühnen, Tim Jacobowitz — [PromptResponse: Optimizing Prompts for LLM Coding Tasks](http://arxiv.org/abs/2608.21074v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in research workflows and software development pipelines, yet their output remains sensitive to input prompt variations. This paper presents $\unicode{x00AB}$PromptResponse$\unicode{x00BB}$, a controlled study examining how formatting and LLM-based tuning of coding task prompts affect the resulting code's performance, efficiency, and stability. Using five semantically identical yet syntactically distinct variants of the HumanEval dataset$\unicod...
  </details>

- **2026-08-21** — Amani Sedrat, Takieddine Chehhat, Youcef Sklab et al. — [AT-ViT: Area-Targeted Multi-View Vision Transformer with Cross-Attention and Multi-Scale Patching for Plant Trait Recognition in Herbarium Images](http://arxiv.org/abs/2608.21067v1)
  <details><summary>📄 Abstract</summary>
  Automated plant traits recognition from herbarium images is essential for plant sciences, yet remains challenging because background elements (e.g., textual labels, mounting artifacts, and color charts) can introduce shortcut learning, leading models to rely on spurious non-plant cues rather than plant morphology. This bias degrades both generalization and interpretability. In this paper, we introduce AT-ViT, a dual-branch Vision Transformer that jointly encodes raw herbarium scans and their seg...
  </details>

- **2026-08-21** — Emma Granqvist, Rocío Mercado, Samuel Genheden — [Designing a Robust LLM-Based Evaluation System for Agentic AI in Drug Discovery Through Human Alignment](http://arxiv.org/abs/2608.21057v1)
  <details><summary>📄 Abstract</summary>
  Agentic large language model (LLM) systems are reshaping scientific workflows in chemistry and drug discovery, but evaluating their open-ended, tool-augmented outputs remains a fundamental bottleneck. Reference-based metrics such as BLEU and ROUGE fail to capture semantic correctness, while expert human evaluation does not scale to the iteration speed these systems demand. The LLM-as-a-Judge paradigm has emerged as a scalable alternative, but existing drug discovery benchmarks deploy LLM judges ...
  </details>

- **2026-08-21** — Chi Li, Rui Lin, Aobo Ji et al. — [CoAnchor: Robust Collaborative Perception under Spatio-Temporal Misalignment via Object-Level Anchors](http://arxiv.org/abs/2608.21055v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception extends the sensing range of a single vehicle by fusing observations from nearby agents, which improves the robustness of autonomous driving. In realistic deployments, however, the received collaborator messages are often affected by both communication delay and relative-pose noise, which jointly cause stale observations, spatial misalignment, and unstable feature fusion. Existing methods usually address these issues from either the spatial or temporal side, but handling...
  </details>

- **2026-08-21** — Yitao Xu, Tong Wu, Yiyan Wu et al. — [Roadside-Cooperative Autonomous Driving: From Data Platform to Vision-Language End-to-End Reasoning](http://arxiv.org/abs/2608.21032v1)
  <details><summary>📄 Abstract</summary>
  Vehicle-to-Everything (V2X) cooperation enables beyond-line-of-sight perception, mitigating occlusions in single-vehicle sensing. However, existing V2X benchmarks provide limited support for closed-loop evaluation and language-grounded supervision, hindering the development of vision-language models (VLMs) for end-to-end cooperative driving. To address these limitations, we introduce V2XBench, a simulation platform featuring synchronized ego--roadside sensing and closed-loop evaluation, together...
  </details>

- **2026-08-21** — Haiming Li, Yingsheng Liu, Jingmin Zhu et al. — [Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs](http://arxiv.org/abs/2608.20999v1)
  <details><summary>📄 Abstract</summary>
  Multimodal LLMs apply the language model interface to visual inputs, where ordinal regression tasks such as age estimation, image quality assessment, and disease grading require autoregressive decisions over ordered class labels. We ask whether MLLMs reliably convert internal ordinal evidence into ordered digit-token outputs. Across four ordinal benchmarks and four MLLM backbones, ordinal labels are linearly recoverable from hidden states with Spearman correlation up to 0.938, and a task-designe...
  </details>

- **2026-08-21** — Yibo Hu, Yu Qian, Mao Gu et al. — [TLive-Omni: An Omni-Modal Understanding Model for E-Commerce Live Streaming](http://arxiv.org/abs/2608.20958v1)
  <details><summary>📄 Abstract</summary>
  E-commerce live streaming requires omni-modal understanding of noisy, temporally extended streams, where product facts are distributed across speech, video frames, product images, overlaid text, and user queries. We present TLive-Omni, an omni-modal understanding model tailored to live-commerce scenarios. It maps image, video, audio, and text inputs into a unified representation space. For long-form live streaming analysis, we introduce Per-vGrid, a timestamped token organization that groups eac...
  </details>

- **2026-08-21** — Pengshuai Yang, Zijing Gao, Xue Yu et al. — [Automated Trajectory Evaluation for Mobile Agents via Step-Level Consequence Reasoning and Aggregation](http://arxiv.org/abs/2608.20797v1)
  <details><summary>📄 Abstract</summary>
  Evaluating language-guided mobile agents has recently shifted from rule-based to model-based approaches to achieve scalable and automated assessments. However, existing holistic evaluation paradigms process entire trajectories at once, leading to substantial context overload. Moreover, they primarily focus on task completion while overlooking operational safety. To address these limitations, we introduce CRATE, a novel two-stage VLM-as-judge framework for automated mobile agent evaluation that i...
  </details>

- **2026-08-20** — Qian Kou, Xiaofeng Shi, Xiaosong Qiu et al. — [Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge Internalization](http://arxiv.org/abs/2608.20281v1)
  <details><summary>📄 Abstract</summary>
  Large language models often fail to answer questions about a bounded document collection when the source documents are not retrieved at inference time. We study this setting as document knowledge internalization: converting a fixed corpus into usable parametric knowledge for retrieval-free question answering. We propose IAR (Inject, Align, and Recover), a three-stage post-training framework that separates structured document knowledge injection, QA behavior alignment, and general ability recover...
  </details>

- **2026-08-20** — Yansen Han, Shengyi Liao, Yuanxing Zhang et al. — [Manifold Drift in Flow Preference Optimization: A Root Cause of Reward Hacking](http://arxiv.org/abs/2608.20011v1)
  <details><summary>📄 Abstract</summary>
  Preference optimization is a standard alignment method for generative models, yet extending it to continuous-time dynamics remains non-trivial. In flow matching, reward-driven updates modify transport trajectories without an inherent constraint to the pretrained data manifold and can move terminal samples off the pretrained support. We formalize this failure mode as manifold drift. Theoretically, we show that optimal flow matching recovers the terminal data distribution, whereas a preference upd...
  </details>

- **2026-08-20** — Taihua Chen, Xiang Ma, Yixin Zhang et al. — [Scale-Aware Pretraining of Time Series Foundation Models via Multi-Patch Token Alignment and Hybrid Masking](http://arxiv.org/abs/2608.20005v1)
  <details><summary>📄 Abstract</summary>
  Pretraining time series foundation models across heterogeneous datasets necessitates effective handling of varying sampling frequencies. Current methods either employ dataset-specific patch sizes and separate FFNs, leading to fragmented representations, or enforce a fixed patch size that neglects inherent temporal variations. To address this, we propose SATS, featuring a scale-aware token alignment mechanism that treats patch size as an explicit notion of scale. By incorporating a contrastive-in...
  </details>

- **2026-08-20** — Hangyu Tian, Zhenqi He, Yanghao Wang et al. — [DIFFCZSL: Compositional Zero-Shot Learning Regularized by Diffusion Representations](http://arxiv.org/abs/2608.19871v1)
  <details><summary>📄 Abstract</summary>
  Compositional Zero-Shot Learning (CZSL) aims to recognize unseen attribute-object compositions by leveraging knowledge of primitive concepts learned from seen compositions. Although recent works achieve impressive performance in CZSL by leveraging large vision-language models, they primarily rely on discriminative representations that may not explicitly preserve the structured relationships between primitive concepts and their compositions. Motivated by the recent success of diffusion-based clas...
  </details>

- **2026-08-20** — Silin Chen, Haoyi Teng, Xiaodong Gu et al. — [Repo0: Design-Driven Zero-to-All Code Generation](http://arxiv.org/abs/2608.19854v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have made substantial progress in code generation, yet most existing systems assume a predefined repository architecture. This assumption does not hold in zero-to-all code generation, where an agent must construct an entire software project directly from natural-language requirements while maintaining a modular repository architecture throughout development. We present Repo0, a continuous structural evolution framework for zero-to-all code generation. Repo0 maintains ...
  </details>

- **2026-08-20** — Yunseo Lee, Hyun Jun Kim, Heeseung Shin et al. — [Towards Clinically Faithful Medical Image Captioning via Enhanced Vision-Language Alignment](http://arxiv.org/abs/2608.19825v1)
  <details><summary>📄 Abstract</summary>
  Medical image captioning is a technique that accelerates early-stage diagnostic workflows and enhances the interpretability of medical diagnostic AI systems. However, unlike general image captioning, clinically reliable captioning remains challenging due to grayscale-based modalities, subtle anatomical cues, specialized medical phrasing, and variations in data quality. Despite recent advances in large vision-language models, fluent outputs do not necessarily guarantee sufficient alignment with c...
  </details>

- **2026-08-20** — Haonan He, Xinyue Fan — [LoRA-GA$^2$: Low Rank Adaptation with Multi-step Gradient Adaptive Alignment](http://arxiv.org/abs/2608.19800v1)
  <details><summary>📄 Abstract</summary>
  Low-Rank Adaptation (LoRA) is a prominent fine-tuning method for large models, achieving competitive performance with reduced memory overhead. However, a persistent performance gap remains between LoRA and full fine-tuning. Recent studies have sought to narrow this gap by employing one-step gradient approximations of pretrained weights to align LoRA updates with the principal directions or intrinsic dimensionalities of full fine-tuning updates. Nevertheless, these approaches fail to capture the ...
  </details>

- **2026-08-20** — Yash Ganpat Sawant — [PersonalBench: Measuring the Authorship Gap in LLM Personalization](http://arxiv.org/abs/2608.19746v1)
  <details><summary>📄 Abstract</summary>
  Personalized text generation aims to make LLMs write in a specific individual's style, yet existing benchmarks measure task accuracy or preference alignment rather than whether the model's output actually resembles the target author's writing. We introduce PersonalBench, a benchmark that evaluates inference-time personalization methods through three independent lenses: LUAR (a trained authorship verification model), an LLM-as-judge, and automated stylometrics. Across 50 authors, 1,000 generation...
  </details>

- **2026-08-20** — Hyunse Lee, Jiwoo Jeong, Haneul Lee et al. — [SafeBranch: Branch-Pair Safety Alignment for Embodied Agents](http://arxiv.org/abs/2608.19729v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting...
  </details>

- **2026-08-20** — Hexi Wang, Yujia Zhou, Bangde Du et al. — [Mitigating Identity Essentialism in LLM Agents with Longitudinal Life Trajectories](http://arxiv.org/abs/2608.19621v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) offer a scalable approach to social simulation, but their credibility depends on how agents are constructed. Existing methods can partially reproduce population-level patterns, yet often fail to capture human-like diversity. Our analysis shows that static-profile agents exhibit stronger demographic separation and within-group compression than humans, a pattern consistent with identity essentialism: demographic labels can encourage models to treat group-average tenden...
  </details>

- **2026-08-20** — Jiawei Feng, Jiancan Wu, Xingyu Zhu et al. — [PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment](http://arxiv.org/abs/2608.19598v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has emerged as an effective approach for aligning large language models (LLMs) with human preferences. However, its adaptation to multimodal settings remains unexplored. Through representational analysis, we identify a key limitation in multimodal preference optimization, which we term visual insensitivity: models often fail to distinguish between images and those with critical visual context removed. Our theoretical analysis further uncovers two manifestatio...
  </details>

- **2026-08-20** — Eunsoo Im, Junghun Suh, Gyeonggwan Lee et al. — [CVSD-Reg: Cross-Modal Visual Semantic Prior Distillation for Robust LiDAR Registration](http://arxiv.org/abs/2608.19536v1)
  <details><summary>📄 Abstract</summary>
  Learning-based global point cloud registration has achieved remarkable progress, yet its reliance on geometric representations makes existing methods sensitive to variations in point density, scan pattern, viewpoint, and sensor characteristics. We propose CVSD-Reg, a robust global LiDAR registration framework that distills visual semantic priors from a vision foundation model into LiDAR representations. In Stage 1, a Point Transformer V3 student learns from a frozen DINOv2 teacher through contra...
  </details>

- **2026-08-20** — Josias Moukpe, Priyanka Aryal, Matthew Kenney — [DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories](http://arxiv.org/abs/2608.19653v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents for machine learning experimentation must navigate heterogeneous repositories, repair training pipelines, and evaluate candidate improvements under realistic compute constraints. Existing benchmarks only partially capture these conditions. We introduce DeltaML-Bench, a benchmark comprising 48 tasks sourced from research papers that require agents to improve published baselines within imperfect, open-source repositories. We evaluate GPT-5 and Claude Sonnet 4 with a standard Modu...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 69 papers

- **2026-08-24** — Peiyang Liu, Xi Wang, Di Liang et al. — [The Laws of Context Allocation: Causal Measurement and Closed-Loop Orchestration in Generative Search](http://arxiv.org/abs/2608.23252v1)
  <details><summary>📄 Abstract</summary>
  As Retrieval-Augmented Generation (RAG) shifts toward diverse portfolio generation, it is stymied by two critical bottlenecks: flawed measurement of evidence utilization, and suboptimal context budget allocation. We resolve both sequentially.   To resolve measurement, we expose a pervasive ``diagnostic illusion'': standard relevance proxies fail catastrophically on hard negatives. We replace them with an efficient causal leave-one-out probe that accurately isolates generative reliance and formal...
  </details>

- **2026-08-24** — Xiaopeng Guo, Wai Chung Tse, Yipeng Zhu et al. — [NemoSplat: Feed-Forward 4D Gaussian Splatting for Media-Aware Underwater Reconstruction](http://arxiv.org/abs/2608.22888v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing photorealistic scenes in unconstrained underwater environments remains challenging due to severe media-induced light scattering and unpredictable dynamic objects. Recent feed-forward visual foundation models have demonstrated remarkable capabilities in generalized novel view synthesis and tracking. However, when directly applied to aquatic videos, optical attenuation and motion interference fatally corrupt their feature aggregation, leading to severe tracking and reconstruction fa...
  </details>

- **2026-08-24** — Jindou Jia, Shixuan Han, Meng Wang et al. — [Physics Filtering Favors the Generalization of Robot Learning](http://arxiv.org/abs/2608.22701v1)
  <details><summary>📄 Abstract</summary>
  Living organisms exhibit extraordinary adaptability to unseen environments through their intrinsic physical structures and lifelong feedback-driven learning. Endowing robots with comparable generalization is critical for reliable operation in the real world. While recent approaches attempt to improve generalization by scaling training data, such strategies remain impractical for robotics, where collecting real-world demonstrations at the scale of large language models is prohibitively costly and...
  </details>

- **2026-08-24** — Zhiqing Cui, Xinxiang Yin, Yihong Tang et al. — [EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards](http://arxiv.org/abs/2608.23525v1)
  <details><summary>📄 Abstract</summary>
  Earth-system analysis reconstructs changing physical processes from observations that differ in source, scale, timing, and modality. Natural hazards make this work consequential because incomplete evidence can change estimates of severity, exposure, and mechanism. We introduce EarthVerse, a benchmark that evaluates scientific agents through package-scoped investigations. Its 405 reproducible tasks are grounded in 199 documented events and 19 hazard families. Agents inspect heterogeneous event pa...
  </details>

- **2026-08-24** — Steeven B. Affognon, Babacar M. Ndiaye, Pierre Mendy et al. — [From Daily Fluctuations to Annual Hydrological Cycles: A Wavelet-Based Analysis of Nonstationary Seasonality in Senegal River Hydropower Inflows](http://arxiv.org/abs/2608.23470v1)
  <details><summary>📄 Abstract</summary>
  This study presents a reproducible framework combining Fourier and wavelet analysis to examine the seasonality of daily inflows at three sites on the Senegal River (Bafing Makana, Felou, Gouina), based on 65,631 daily observations spanning nearly 60 years (1961-2020). Using harmonic regression, Welch spectral analysis, stationary wavelet decomposition, Morlet continuous wavelet transforms, trend and change-point tests, and cross-wavelet coherence, the authors show that the annual cycle correspon...
  </details>

- **2026-08-24** — Andrej Orsula, Miguel Olivares-Mendez, Carol Martinez — [Reward-Free Continual Adaptation for Resilient Space Robots](http://arxiv.org/abs/2608.23452v1)
  <details><summary>📄 Abstract</summary>
  Space robots operate in extreme environments where hardware degradation can critically compromise traditional control strategies. While continual reinforcement learning offers a promising mechanism for online adaptation, it inherently requires access to a reward signal during deployment. However, precise reward computation in space is often infeasible due to the lack of external tracking systems and the overall complexity of the environment. To address the challenge of unobservable rewards, we i...
  </details>

- **2026-08-24** — Geoffrey X. Yu, Ryan Marcus, Tim Kraska — [EXPLAIN Yourself! Finding Query Planner Stalls Across DBMSes](http://arxiv.org/abs/2608.23402v1)
  <details><summary>📄 Abstract</summary>
  Query planners are typically expected to produce optimized plans quickly, leading many researchers (including the authors of this paper) and practitioners to design systems that assume query planning is a low-cost operation. Using a lightweight agentic search, we show that this assumption does not always hold. Across seven DBMSes, including four commercial systems, we find at least one query per system that takes more than three minutes to plan. In addition to being slow to plan, such queries ri...
  </details>

- **2026-08-24** — Jiapeng Li, Ping Wei, Wenjuan Han et al. — [IntentQA: Intent Question Answering in Videos by Cognitive Context Reasoning](http://arxiv.org/abs/2608.23330v1)
  <details><summary>📄 Abstract</summary>
  Video understanding requires intelligent agents to transcend mere recognition of visual facts and comprehend the underlying intents behind human actions (often termed the "dark matter" of social intelligence). To bridge the gap between visual observation and intent reasoning, we introduce a novel task, IntentQA, and contribute a large-scale VideoQA dataset specifically tailored for this purpose. However, recognizing that standard metrics may overestimate capabilities due to dataset biases, we go...
  </details>

- **2026-08-24** — Yuexin Ma, Jingqi Hou, Yuxuan Kang et al. — [A Multidimensional Data-Driven Hybrid Transformer Framework for Non-invasive Continuous Blood Pressure Prediction](http://arxiv.org/abs/2608.23276v1)
  <details><summary>📄 Abstract</summary>
  Objective. To develop and evaluate a cuffless continuous blood pressure (BP) estimator using temporal physiological and demographic features. We propose a hybrid Transformer framework to estimate diastolic and systolic BP from ECG/PPG-derived feature sequences. Approach. Rather than raw waveforms, the framework models 10-step sequences of six physiological descriptors and two demographic covariates. A Multi-Source Temporal Encoder Module combines Transformer, Kolmogorov-Arnold Network, and XGBoo...
  </details>

- **2026-08-24** — Guoyang Shi, Zitong Zhang, Siqi Ding et al. — [AI Surrogate Modeling for Real-Time Tokamak Equilibrium Prediction: Benchmarking Neural Architectures and Validation on EXL-50U](http://arxiv.org/abs/2608.23217v1)
  <details><summary>📄 Abstract</summary>
  Fast and reliable plasma equilibrium prediction is essential for real-time tokamak operation and control, but conventional Grad-Shafranov (GS) solvers are often too costly for real-time deployment. We develop an AI surrogate framework and benchmark five architectures (MLP, CNN, FNO, Transformer, and KAN) on a numerical GS database with 100,000 IID and 10,000 OOD samples. Under a unified protocol, we evaluate accuracy, inference efficiency, model scaling, and robustness. We also establish device-...
  </details>

- **2026-08-24** — Hossein Abdi, Satya Prakash Dash, Mingfei Sun — [Guided Riemannian Optimization (GuRO): Bridging Model Predictive Control and Decision Transformers](http://arxiv.org/abs/2608.23204v1)
  <details><summary>📄 Abstract</summary>
  Decision-making in high-dimensional, nonlinear systems remains a central challenge in robotics. While model-based methods like Model Predictive Control (MPC) offer sample efficiency and interpretability, their performance degrades when the dynamics model is inaccurate or long-horizon predictions are required. Conversely, model-free reinforcement learning (RL) learns policies directly from interaction but suffers from high sample complexity and unstable optimization. Recent advances in sequence m...
  </details>

- **2026-08-24** — Xiao Zhang, Qumeng Sun, Jihao Li et al. — [LongWoF-Bench: Evaluating EvoMap Genes for Verifiable Long-Workflow Tasks](http://arxiv.org/abs/2608.23200v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly expected to execute complex workflows whose success depends on maintaining interdependent constraints and producing artifacts that satisfy strict end-to-end verification. Yet successful execution experience is typically lost after a single run, forcing subsequent models to rediscover strategies and failure modes from scratch. We study whether such experience can instead be externalized and reused through EvoMap, where verifier-confirmed execution trajectori...
  </details>

- **2026-08-24** — Chang Liu, Xiaohui Xie, Xinyi Chen et al. — [NetConfArena: An Executable Benchmark for LLM Agents in Closed-Loop Network Configuration](http://arxiv.org/abs/2608.23179v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly attractive for automating network configuration, yet their reliability and failure patterns are poorly understood. An essential prerequisite is to assess such agents in a realistic but risk-free environment. Existing benchmarks, however, fall short: they often treat configuration as static command generation or rely on overly simplified settings. Such evaluations understate the core challenges of network configuration, where correctness requires...
  </details>

- **2026-08-24** — Burak Satar, Zhixin Ma, Cheng Yu-Tong et al. — [Cultural Moment Benchmark: Evaluating Video Cultural Reasoning and Grounding in Southeast Asia](http://arxiv.org/abs/2608.23065v1)
  <details><summary>📄 Abstract</summary>
  Cultural understanding in video means more than recognizing what is visible; it requires grasping the symbolic and temporal significance of cultural concepts. We decompose this into three abilities: naming what a concept symbolizes, visually recognizing it on video, and locating its sub-events in time. Existing video-cultural benchmarks tend to test what is seen, collapsing these three abilities into a single score that hides the bottleneck. We introduce the Cultural Moment Benchmark (CMB): 306 ...
  </details>

- **2026-08-24** — Xiaotong Tan, Chunli Qiu, Xin Liu et al. — [Improving O-RADS Risk Stratification from Ultrasound Reports: A Comparative Evaluation of Hybrid versus End-to-End LLM Reasoning Strategies](http://arxiv.org/abs/2608.23061v1)
  <details><summary>📄 Abstract</summary>
  Background: Automating clinical guideline-based decision-making with large language models (LLMs) remains challenging because of reliability, hallucination, and limited interpretability. We compared the performance of LLMs and reasoning strategies for automated Ovarian-Adnexal Reporting and Data System (O-RADS) classification from free-text pelvic ultrasound reports. Methods: In this retrospective study, consecutive patients with ovarian masses who underwent pelvic ultrasound were included. Eigh...
  </details>

- **2026-08-24** — Sungho Park, Wonjoong Kim, Rongyuan Tan et al. — [AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces](http://arxiv.org/abs/2608.23041v1)
  <details><summary>📄 Abstract</summary>
  LLM agents remain unreliable on long-horizon tasks, where small local failures can compound over extended interactions and lead to overall task failure. Although external harnesses can substantially improve robustness, harness design remains a manual and expensive process that requires searching over a large space of prompts, tool configurations, and control logic. We propose AutoSaddler, an automatic harness optimization framework that formulates harness improvement as an offline learning probl...
  </details>

- **2026-08-24** — Xiaohui Zhang, Zequn Sun, Chengyuan Yang et al. — [Toward Effective and Reliable LLM Agents via Dynamic Ontology](http://arxiv.org/abs/2608.22974v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents rely heavily on knowledge encoded in model parameters or presented as unstructured context. In domain-specific tasks, this leaves important semantic connections implicit. This often results in incomplete evidence use and brittle multi-step decisions. Ontologies offer a way to externalize domain concepts and relations as machine-interpretable structures, but constructing task-usable ontologies traditionally requires substantial effort from domain experts and is d...
  </details>

- **2026-08-24** — Yiyi Zhang, Yuchen Yuan, Ying Zheng et al. — [Optimize Surgical Triplet Recognition: A Knowledge-Driven Mixture-of-Experts Solution](http://arxiv.org/abs/2608.22972v1)
  <details><summary>📄 Abstract</summary>
  Surgical action triplet recognition constitutes a critical task in context-aware robot-assisted surgery, facilitating automatic surgical action perception by identifying instrument, verb, target, and their association. However, existing works struggle to analyze such complex surgical scenes due to three main issues: (1) component-level optimization conflicts caused by entangled feature spaces, (2) category-level optimization conflicts arising from severe data imbalance, and (3) lack of domain kn...
  </details>

- **2026-08-24** — Yingxiang Xu, Kerui Ren, Wenqi Guo et al. — [AquaFlow: A Monocular Gaussian Splatting SLAM for Underwater Streaming Reconstruction](http://arxiv.org/abs/2608.22906v1)
  <details><summary>📄 Abstract</summary>
  Recent monocular 3D Gaussian Splatting (3DGS) streaming reconstruction methods have achieved impressive performance by balancing reconstruction quality and efficiency. However, extending these frameworks to underwater scenes remains challenging due to severe visual degradation, such as light attenuation and scattering, which degrades camera pose tracking and distorts scene geometry. To address these challenges, we propose AquaFlow, a monocular Gaussian Splatting streaming reconstruction framewor...
  </details>

- **2026-08-24** — Philipp Emanuel Weidmann, Allen Roush, Judah Goldfeder et al. — [XTC: Head-Aware Sampling by Excluding Top Choices](http://arxiv.org/abs/2608.22758v1)
  <details><summary>📄 Abstract</summary>
  Standard decoding rules for autoregressive language models promote diversity by rescaling the full next-token distribution or truncating its low-probability tail. These strategies overlook a common regime of open-ended generation in which several continuations are plausible but too much probability mass remains concentrated on the most generic choice. We introduce XTC (Exclude Top Choices), a lightweight head-aware decoding operator that targets this regime directly. XTC identifies tokens whose ...
  </details>

- **2026-08-24** — Jieun Lee — [Double/Debiased Machine Learning for Functional-Form-Robust Spatial Autoregression](http://arxiv.org/abs/2608.22706v1)
  <details><summary>📄 Abstract</summary>
  Spatial autoregressive inference is typically conditional on the spatial weights matrix, W, even though the underlying interaction structure is often unknown and empirical conclusions can be sensitive to its specification. This paper develops double/debiased machine learning inference for low-dimensional SAR parameters when the spatial interaction operator is learned flexibly from potentially endogenous characteristics. Within a maintained admissible support, interaction strength is generated by...
  </details>

- **2026-08-24** — Jiachen Xu, Torben Bach Pedersen, Zhongming Yao et al. — [Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses](http://arxiv.org/abs/2608.22676v1)
  <details><summary>📄 Abstract</summary>
  Robustness to a bad tool return means answering it in the way that return calls for, which depends on how the tool went wrong. A tool that has failed and a tool that returns a well-formed falsehood are different problems with different remedies. We ask whether the two already differ at the moment the return arrives. This is a qualitative pilot study: we score single decision points rather than running agents to completion. We inject controlled faults into a retail customer-service domain and rea...
  </details>

- **2026-08-23** — Toghrul Abbasli, Kentaroh Toyoda, Yuan Wang et al. — [Claim-Level Confidence Calibration for Reliable Decision Making with Large Language Models](http://arxiv.org/abs/2608.22483v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) increasingly support decision-making in high-stakes domains, but they often hallucinate and express confidence that is misaligned with factual correctness. Response-level confidence is a coarse signal: a single generation can mix correct and incorrect statements, so a single number is not actionable for users that must accept, reject, or verify individual pieces of information. We study claim-level confidence calibration as a decision-relevant uncertainty signal: eac...
  </details>

- **2026-08-23** — Yiming Wang, Jiale Zhu, Zhichen Ye et al. — [A Query-Time Framework for Transient 2D Pore-Scale Flow Prediction and Generative Design](http://arxiv.org/abs/2608.22235v1)
  <details><summary>📄 Abstract</summary>
  Pore-scale flow governs transport and permeability behaviour in porous media engineering applications, yet repeated lattice Boltzmann method (LBM) simulation across many geometries and design queries remains costly for repeated deployment. This study formulates transient pore-scale flow prediction as a geometry-conditioned query-time operator and introduces QSGS-Transient-7606, a benchmark of 7,606 two-dimensional porous structures each paired with 30 logarithmically sampled LBM states. The prop...
  </details>

- **2026-08-23** — Yaofei Wang, Jinyang Guo, Shuchao Du et al. — [PURA: Provably Unbiased and Robust Multi-Bit Text Attribution](http://arxiv.org/abs/2608.22218v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained attribution of AI-generated text is becoming increasingly important for accountability and auditing, yet existing multi-bit watermarking methods still struggle to simultaneously preserve the base generation distribution, support high-capacity payloads, and remain recoverable after editing. We present PURA, a provably unbiased and robust multi-bit watermarking method for text attribution. Instead of perturbing token probabilities directly, PURA embeds payloads in the latent sampling ...
  </details>

- **2026-08-23** — Christos Sardianos, Iliana Pla, Vasilis Efthymiou et al. — [HANSARD: A Reference Architecture for Forensic Readiness, Runtime Witnessing, and Graded Attribution in Autonomous Multi-Agent AI Systems](http://arxiv.org/abs/2608.22512v1)
  <details><summary>📄 Abstract</summary>
  Autonomous multi-agent systems nowadays act in finance, software supply chains, and security operations. Already, the first largely AI-orchestrated intrusion campaigns have been reported. Yet, when such a system causes harm, no method can robustly establish what happened, what caused it, or who is accountable. This is because provenance forensics works at the wrong abstraction, formal causality assumes the causal model, and agent auditing trusts self-recording. The target failure mode is, thus, ...
  </details>

- **2026-08-23** — Junda He, Jieke Shi, Zhou Yang et al. — [Learning from the Test: Self-Referential Differential Testing for Deep RL Agents](http://arxiv.org/abs/2608.22284v1)
  <details><summary>📄 Abstract</summary>
  Deep Reinforcement Learning (DRL) has achieved significant success in complex decision-making problems. As DRL systems are increasingly deployed in real-world applications, ensuring their quality and reliability is paramount. Current works primarily focus on detecting safety-critical failures, often neglecting policy optimality, which can lead to reduced efficiency, user distrust, and economic losses. This oversight, compounded by the inherent "testing oracle problem" for optimality, leaves a si...
  </details>

- **2026-08-23** — Md Toufikuzzaman, Ahmad Mousavi, Dongwon Lee — [BLADE: Bilevel Low-rank Augmented-Lagrangian Erasure for LLM Unlearning](http://arxiv.org/abs/2608.22557v1)
  <details><summary>📄 Abstract</summary>
  Existing LLM unlearning methods struggle with robustness: unbounded forget losses degrade model coherence, fixed-weight balancing cannot adapt as retain difficulty shifts mid-training, and methods that work on one benchmark falter under scaling or repeated application. We propose BLADE, a constrained bilevel framework whose three mechanisms give smooth, predictable control over the optimization landscape: a clamped-entropy forget loss whose gradient is exactly zero once a token reaches sufficien...
  </details>

- **2026-08-23** — Davide Bargellini, Alex Pasquali, Andrea Govoni et al. — [Enhancing Sim2Real Transfer for Torque-Controlled Robots through Real2Sim Dynamics Estimation and Reinforcement Learning](http://arxiv.org/abs/2608.22629v1)
  <details><summary>📄 Abstract</summary>
  Transferring reinforcement learning policies from simulation to Real-World robots remains a major challenge, particularly when dealing with low-level torque control, where even small modelling inaccuracies can lead to unstable or unsafe behaviours. In this work, we propose a Real2Sim2Real pipeline that improves Sim2Real transfer for torque-controlled robotic arms by combining trajectory matching, parameter optimization via genetic algorithms, and domain randomization. Using the 7-DOF Franka Emik...
  </details>

- **2026-08-23** — Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman et al. — [Small Reasoning Models are Instruction Followers in Function Calling](http://arxiv.org/abs/2608.22472v1)
  <details><summary>📄 Abstract</summary>
  Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work demonstrates that LLMs achieve superior accuracy in function calling in instruction-following contexts (i.e., standard user-assistant interactions) rather than a tool calling context. We introduce Instr...
  </details>

- **2026-08-23** — Francisco Portillo López — [From Exposure to Expectation: Frequency, Surprisal, and Language Across Development in Spanish](http://arxiv.org/abs/2608.22452v1)
  <details><summary>📄 Abstract</summary>
  Surprisal, the negative log-probability a language model assigns to a word given its preceding context, reliably predicts adult reading times. Does it contribute as much to explaining when children acquire individual words? Frequency reflects a learner's cumulative exposure to a word, whereas surprisal reflects how predictable a single occurrence is given its context. We investigate this question across two corpus-based studies of Spanish.   In Study 1, we modeled age of acquisition (AoA) for 22...
  </details>

- **2026-08-23** — Changjiang Jiang, Qiannian Zhao, Lei Xin et al. — [Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding](http://arxiv.org/abs/2608.22429v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) capable of thinking with images often rely on external tools for fine-grained perception. However, this reliance introduces significant inference latency and fails to effectively resolve the spatial-structural gap-a fundamental challenge in text-dense and structurally relational visuals (e.g., charts and visual tables) where strict relative spatial arrangements bind textual elements. Without external tools, standard MLLMs struggle with such fine-grained v...
  </details>

- **2026-08-23** — Aoke Zhang, Bo Wang, Xihong Wu et al. — [Cross-Subject Generalization in Decoding Perceived Speech from Non-Invasive Brain Recordings](http://arxiv.org/abs/2608.22420v1)
  <details><summary>📄 Abstract</summary>
  Decoding perceived speech from non-invasive brain recordings has garnered significant attention in recent years due to its wide range of potential applications. However, existing methods face considerable challenges in cross-subject decoding, primarily due to limited generalizability and the absence of explicit mechanisms for extracting subject-consistent information. These limitations result in high training costs and suboptimal decoding performance. To address these challenges, we propose an i...
  </details>

- **2026-08-23** — Yihua Shao, Jia Li, Siyu Chen et al. — [LiST: Local-Simplex Test-Time LoRA Fusion](http://arxiv.org/abs/2608.22370v1)
  <details><summary>📄 Abstract</summary>
  Task-specific LoRA adapters offer a modular way to specialize large language and vision-language models. However, existing adapter composition methods are mostly static and cannot adapt to individual test inputs. To address these issues, we propose \textbf{LiST}, a label-free test-time LoRA fusion framework that converts an existing LoRA bank into a target-conditioned local simplex and searches sample-specific fusion weights at inference time. LiST builds joint task representations from LoRA par...
  </details>

- **2026-08-23** — Yize Li, Ningyuan Yang, Sile Yin et al. — [MRMAD: A Multi-Round Multi-Audio Benchmark for Evaluating Acoustic Degradation Perception in Large Audio-Language Models](http://arxiv.org/abs/2608.22236v1)
  <details><summary>📄 Abstract</summary>
  Large audio-language models (LALMs) have shown promising progress in understanding speech, music, and general sound events, yet their ability to reason about how audio signals are degraded remains underexplored. Existing benchmarks primarily evaluate semantic understanding, event recognition, or high-level audio reasoning, leaving a basic question unanswered: Do LALMs understand the differences in audio quality? We introduce MRMAD, a Multi-Round Multi-Audio Degradation benchmark for evaluating a...
  </details>

- **2026-08-23** — Kang Chen, Junjie Nian, Yixin Cao et al. — [Disagree to Explore, Agree to Commit: Routing-Guided Test-Time Scaling for Software Agents](http://arxiv.org/abs/2608.22191v1)
  <details><summary>📄 Abstract</summary>
  Software-engineering agents solve repository-level tasks through long, stochastic tool-use trajectories, and repeated attempts often find fixes missed by one run. Test-time scaling is difficult because patches lack canonical answer forms, while sibling actions from a shared prefix are correlated. We study whether native MoE router traces can guide steering and selection without an external judge or selection-time test execution. Our analysis shows that routing provides a robust behavioral role s...
  </details>

- **2026-08-22** — Lukasz Olejnik, Bartosz Naskrecki — [AI Grinding for Fun and Cryptanalysis](http://arxiv.org/abs/2608.21986v1)
  <details><summary>📄 Abstract</summary>
  We present an autonomous cryptanalysis workflow in which agents generate, test, and refine hypotheses before human review. The autonomous stage returns reproducible candidates with exact witnesses, controls, code, and run records. A researcher then decides whether the evidence establishes a break, defect, or coverage gap.   Two failure modes recur. First, a public algebraic map or input representation erases or exposes a relation that a construction must hide. Examples include multiplication by ...
  </details>

- **2026-08-22** — Yaokun Liu, Yifan Liu, Daniel Yue Zhang et al. — [PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems](http://arxiv.org/abs/2608.22130v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) solve complex tasks through communication among role-specialized agents. However, inter-agent dependencies introduce reliability risks beyond isolated agent failures. For instance, errors in intermediate messages could be inherited and amplified by downstream agents. Existing uncertainty quantification (UQ) methods mainly target isolated responses or single-agent reasoning, and therefore fail to capture uncertainty propagation in MAS. To this end, we propose P...
  </details>

- **2026-08-22** — Yuxin Cheng, Chang Liu, Hanxin Yu et al. — [OptiMAS: Automatically Optimize Multi-Agent System](http://arxiv.org/abs/2608.21918v1)
  <details><summary>📄 Abstract</summary>
  Automated evolution of Multi-Agent Systems (MAS) holds significant potential for reducing the manual effort required to design and optimize LLM-based agent architectures. However, extant search-based paradigms face a fundamental trade-off, where an expanded optimization scope exacerbates evolutionary instability, while discrete branch-and-discard search isolates insights across lineages. To address these limitations, we propose a continuous, data-driven optimization paradigm built upon a unified...
  </details>

- **2026-08-22** — Sanjay Bhandari, Nawazish Khan, Alzbeta Novotna et al. — [TRACE: Artifact-Robust Statistical Shape Modeling from Imperfect Surface Scans - A Case Study in Craniosynostosis 3D Photography](http://arxiv.org/abs/2608.22131v1)
  <details><summary>📄 Abstract</summary>
  Craniosynostosis severity analysis increasingly relies on statistical shape models (SSMs) to quantify cranial morphology, but most existing workflows depend on computed tomography or heavily curated three-dimensional (3D) photographs. Raw clinical 3D photographs provide a radiation-free and repeatable alternative, yet often contain shoulders, hands, hair, clothing, scanner noise, and incomplete boundaries that corrupt correspondences. We introduce the Template-constrained Robust Artifact-aware C...
  </details>

- **2026-08-22** — Shuhao Qi, Zhiyong Sun, Siep Weiland et al. — [Opinion-Guided Layered Strategies for Decentralized Coordination](http://arxiv.org/abs/2608.22104v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents increasingly interact with other independent agents, and such interactions typically admit multiple joint behaviors. When two agents prefer different ones, their independent strategies may be mutually incompatible and fail to reach a coordinated outcome; when they are identical, neither can differentiate its role when needed. Ideally, an agent should coordinate with any agent it encounters, regardless of which admissible joint behavior that agent aims to realize. We therefore p...
  </details>

- **2026-08-22** — Edwin Ouko, Emmanuel Lujan, Alan Edelman et al. — [Decision-Support and Modeling with Large Language Models for Geothermal Well Arrays](http://arxiv.org/abs/2608.22068v1)
  <details><summary>📄 Abstract</summary>
  Geothermal well arrays, which organize multiple geothermal wells into carefully planned geometric configurations, provide opportunities to enhance energy production capacity and increase fault tolerance. The development and adoption of these emerging geothermal technologies could be accelerated through the recent advances in large language models (LLMs) and high-level high-performance languages. A challenge in LLM-based applications is the reliability of the generated outputs, as they can be pro...
  </details>

- **2026-08-22** — Leonardo Zini, Elia Frigieri, Lorenzo Baraldi — [A Scalable Vector Graphics Latent Space](http://arxiv.org/abs/2608.21893v1)
  <details><summary>📄 Abstract</summary>
  Scalable Vector Graphics are a fundamental medium for resolution-independent visual content, yet the deep learning community lacks a continuous, dense, and invertible latent space for vector representations, the kind of foundational building block that Variational Autoencoders and their descendants have long provided for raster images. We introduce SLS (SVG Latent Space), a Transformer-based autoencoder that learns compact dense representations of individual SVG paths, the atomic visual elements...
  </details>

- **2026-08-22** — Vsevolod Kleshchenko, Vladimir Igoshin, Costantino De Angelis et al. — [Mie Optical Computing](http://arxiv.org/abs/2608.21891v1)
  <details><summary>📄 Abstract</summary>
  Optical computing is emerging as a promising paradigm for next-generation information processing. Diffractive optical processors rely on spatially distributed trainable degrees of freedom, leading to extended architectures. Here, we propose a compact neuromorphic optical-computing approach where the entire trainable transformation is implemented by a single Mie scatterer. By formulating computation in vector spherical harmonics basis, trainable modal couplings can be concentrated within a finite...
  </details>

- **2026-08-22** — Chaoran Huang, Fangcheng Li, Tianyi Liu et al. — [Towards Bitstream-corrupted Harsh Visual Understanding: Through Bitstream Language Modeling as Robust Semantic Priors](http://arxiv.org/abs/2608.21837v1)
  <details><summary>📄 Abstract</summary>
  Bitstream-corrupted Harsh Visual Understanding (BcHVU) aims to understand harshly degraded videos originally decoded from a severely corrupted bitstream in real-world multimedia communication. The ill-posed nature of BcHVU poses a major challenge for existing vision models, as even subtle bitstream corruption can lead to irreversible pixel distortion and significant semantic loss. To address these challenges in BcHVU, we propose Bitstream Language Modeling as Robust Semantic Priors (BLMSP), a fr...
  </details>

- **2026-08-22** — Suifeng Zhao, Zida Liu, Xinyu Lei et al. — [MCite-RL: Towards Reliable Multimodal RAG via Citation-enhanced Agentic Reinforcement Learning](http://arxiv.org/abs/2608.21808v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Retrieval-Augmented Generation (RAG) with visual citation is crucial for ensuring the traceability and verifiability of MLLMs. However, current RAG and SFT-based methods struggle to achieve robust cross-modal reasoning, causing imprecise visual citations or decoupling between the citation and the generated answers. To address these limitations, we propose MCite-RL, a citation-enhanced agentic reinforcement learning framework designed for reliable multimodal RAG. MCite-RL introduces an...
  </details>

- **2026-08-21** — Shiva Shrestha, Kazi Shaharair Sharif, Zongxing Xie et al. — [Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI](http://arxiv.org/abs/2608.21172v1)
  <details><summary>📄 Abstract</summary>
  Federated fine-tuning enables large language models to adapt on edge devices without centralizing private data, but practical deployments must address hardware instability and adversarial update corruption together. Thermally constrained clients may throttle, slow local training, or delay synchronous aggregation, while Byzantine clients and communication-layer adversaries can corrupt the updates used to form the global model. To address these challenges, we present Thermo-FL, a thermal-aware fed...
  </details>

- **2026-08-21** — Bipasha Kundu, Abhishek Chaturvedi, Axel W. E. Wismueller et al. — [Toward Vision Language Model-based Assessment of Clinical Quality and Usability of LGE-MR Images for Cardiac Ablation Planning](http://arxiv.org/abs/2608.21180v1)
  <details><summary>📄 Abstract</summary>
  LGE cardiac MRI is widely used for left atrial fibrosis assessment and ablation planning in atrial fibrillation patients as knowledge of fibrotic tissue regions identified from LGE-MRI is critical for catheter ablation. Often, poor quality images used during ablation planning can cause mis-localization of ablation targets, directly impacting procedure safety and outcome. The decision of whether a scan meets the minimum quality threshold for ablation planning is currently made informally by the r...
  </details>

- **2026-08-21** — Ruihua Han, Rui Gao, Zhe Liu et al. — [SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control](http://arxiv.org/abs/2608.21175v1)
  <details><summary>📄 Abstract</summary>
  Safe and efficient shape-aware navigation in heterogeneous crowds and robot fleets remains challenging. Traditional approaches often assume homogeneous robots, sparse workspaces, simplified geometry, offline computation, or handcrafted parameters to make the problem tractable, which limits their deployment in dense crowd scenarios. Toward this end, we propose Shape-Aware Reinforcement Learned Model Predictive Control (SRL-MPC), a method for safe, efficient, and adaptive navigation in crowds with...
  </details>

- **2026-08-21** — Xin Sun, Di Wu, Yuchen Guo et al. — [When Trust Meets Truth: Trust-Truth Separability in LLM-as-Judge](http://arxiv.org/abs/2608.21097v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-Judge systems can produce multi-dimensional evaluations, such as trustworthiness, reliability, and factuality, and these outputs are often interpreted as independent evidence. We test this assumption for a common pair of judgments: trust scoring and binary truth classification. On correctness-controlled QA, LLM judges align trust scores with truth verdicts more tightly than human behavioral reference, suggesting weaker separations between trust and truth judgment. We then apply stress tes...
  </details>

- **2026-08-21** — Alexander Thomas, Hubert P. H. Shum, Darren Nellis et al. — [Evaluating Large Language Model Performance on International Maritime Dangerous Goods Code Compliance](http://arxiv.org/abs/2608.21036v1)
  <details><summary>📄 Abstract</summary>
  The transport of dangerous goods by sea is a high-consequence activity governed by the International Maritime Dangerous Goods (IMDG) Code, a complex regulatory framework where errors in classification, packaging, stowage, or segregation can result in fire, explosion, toxic release, or loss of life or vessel. Correct compliance requires accurately interpreting hundreds of pages of interacting provisions, updated on a two-year amendment cycle. Practitioners increasingly use Large Language Models (...
  </details>

- **2026-08-21** — Ye Chen, Weining Zhang — [No Judgment Without a Reason: Counterfactual Receipts for Versioned AI Evaluators](http://arxiv.org/abs/2608.20938v1)
  <details><summary>📄 Abstract</summary>
  Evaluators often produce correct labels via flawed reasoning, a critical failure for agentic systems gating actions, routing reviews, or supplying training feedback. Standard evaluation only verifies final label correctness, ignoring whether judgment changes stem from valid evidence, consistent rules, or proper rule applicability. We formalize evaluator reasoning accountability via three core sources: grounds, norms, and authority. Varying these sources yields an eight-cell counterfactual judgme...
  </details>

- **2026-08-21** — Baixin Li, Haiyun He — [SAC-Copula: Quality-Preserving Watermarking for Diffusion Language Models via Smooth Correlated Gumbel Fields](http://arxiv.org/abs/2608.20839v1)
  <details><summary>📄 Abstract</summary>
  Watermarking diffusion language models (DLMs) requires mechanisms compatible with iterative parallel unmasking rather than autoregressive decoding. Existing sampling-based watermarking methods typically inject position-wise i.i.d. perturbations, which can be poorly aligned with DLM decoding dynamics and degrade generation quality. We propose SAC-Copula, a quality-preserving watermarking method for DLMs based on smooth, locally correlated Gumbel perturbation fields constructed via a Gaussian copu...
  </details>

- **2026-08-21** — Haodong Chen, Yadong Wang, Shengtao Wen et al. — [Knowing but Not Saying: Preventing Factual Access Failures in LLM SFT via Recall-Anchored Distillation](http://arxiv.org/abs/2608.20794v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) can degrade factual behavior outside the target domain. This degradation is often described as catastrophic forgetting, yet open-ended factual failures do not necessarily imply that the underlying facts have been erased. In this work, we identify a more specific phenomenon, factual access failure: after domain SFT, models can still recognize or rank the correct answer under constrained evaluation, while failing to produce it in closed-book generation. Through benchma...
  </details>

- **2026-08-21** — Yiwen Liu, Yujun Zhu, Kui Jia et al. — [ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations](http://arxiv.org/abs/2608.21355v1)
  <details><summary>📄 Abstract</summary>
  Recent vision-based action models have demonstrated strong capabilities in complex manipulation, but they rarely leverage explicit object physical properties to adapt their policies. We introduce ViTacPhys, a visual-tactile framework and data acquisition system that estimates object mass and friction-coefficient classes, together with continuous stiffness, from human manipulation demonstrations. Trained on data from 60 rigid and deformable objects, ViTacPhys combines temporal visual-tactile mode...
  </details>

- **2026-08-21** — Deepanshu Pandey, Arnav Chavan, Nahush Lele et al. — [Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models](http://arxiv.org/abs/2608.20988v1)
  <details><summary>📄 Abstract</summary>
  Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors. We identify the softmax operator as a bottleneck for quantization stability due to its sensitivity to outliers and state-dependent Jacobian. We theoretically establish that suppressing the norm of this Jacobian helps in bounding quantization-induced performance degradation. Based on this, we propose Jacobian-Guided Noise Injection, a training strategy that i...
  </details>

- **2026-08-21** — Youval Klioui — [SR-TL1: A Square-Root TL1-Norm Framework for Robust SMV DoA Estimation under Highly-Coherent Dictionaries](http://arxiv.org/abs/2608.20943v1)
  <details><summary>📄 Abstract</summary>
  This paper proposes a Square-Root Transformed $L_1$-norm ($SR\text{-}TL_{1}$) sparse recovery framework for single-measurement-vector (SMV) direction of arrival (DoA) estimation under highly-coherent overcomplete dictionaries with angular-dependent array imperfections. The proposed framework combines the square-root Least Absolute Shrinkage and Selection Operator (square-root LASSO) framework which is known to be robust against noise variance with the Transformed $L_1$-norm ($TL_1$-norm), a non-...
  </details>

- **2026-08-20** — Mehdi Azarafza, Faezeh Pasandideh, Ali Ehteshami Bejnordi et al. — [Multi-Agent Orchestration with the Common-Sense Reasoning Capabilities of LLMs for Autonomous Driving](http://arxiv.org/abs/2608.20129v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles require robust perception and decision-making capabilities to operate in diverse and unseen scenarios. While reinforcement learning and rule-based methods can provide effective control and safety mechanisms, their performance may degrade in situations requiring contextual reasoning. Large Language Models (LLMs) have demonstrated strong capabilities in understanding multimodal information and generating contextual reasoning, however, their use for direct vehicle control can in...
  </details>

- **2026-08-20** — Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson et al. — [When Text and Numbers Disagree: Evidence Arbitration in Large Language Models](http://arxiv.org/abs/2608.20116v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in settings where textual summaries, numerical observations, and external tool outputs may provide conflicting evidence. We study how LLMs arbitrate between such sources when they support opposing decisions. To do so, we introduce a controlled synthetic benchmark in which latent risk trajectories generate both numerical time series and natural language summaries, allowing us to construct conflicts where exactly one evidence source is aligned wit...
  </details>

- **2026-08-20** — Bin Zhu, Yi Xie, Yanghui Rao — [Stopping and Routing LLM Judge Panels](http://arxiv.org/abs/2608.19802v1)
  <details><summary>📄 Abstract</summary>
  LLM evaluation pipelines often have many candidate judges: general LLM-as-a-judge prompts, reward models, safety classifiers, confidence variants, and task-specific verifiers. The deployment question is not only which judge is best, but which judges should be called, on which examples, and when panel construction should stop. We formulate judge-panel design as a role-conditioned allocation problem. From a small labeled audit set, declared slices, and judge costs, the method estimates target-rela...
  </details>

- **2026-08-20** — Honglie Wang, Jia Sun, Zijun Li et al. — [TextRefine: Improving Textual Fidelity, Spatial Placement, and Glyph Rendering for Text Editing in Product Posters](http://arxiv.org/abs/2608.19637v1)
  <details><summary>📄 Abstract</summary>
  Text editing in product posters entails inserting new text or replacing existing text while preserving product appearance, background content, and global composition. Despite recent progress in instruction-based image editing, general-purpose models remain unreliable in this setting: they often omit or incorrectly render the target text, place it over salient products or pre-existing content, and produce structurally distorted or visually inconsistent glyphs. We introduce \textbf{TextRefine}, a ...
  </details>

- **2026-08-20** — Xuan He, Cong Wei, Yuhao Cheng et al. — [VGI-BENCH: Probing Visual Intelligence in Video Generation Models](http://arxiv.org/abs/2608.19583v1)
  <details><summary>📄 Abstract</summary>
  Recent studies suggest that video generation models can exhibit certain forms of zero-shot visual reasoning through generated frames. Yet reliable evaluation remains challenging: benchmarks should adopt inputs aligned with the visual priors of current video models, require valid evolving processes rather than only plausible final states, and calibrate task difficulty to remain challenging yet partly feasible. To this end, we introduce VGI-bench, containing 27 tasks and 810 instances, organized b...
  </details>

- **2026-08-20** — Yu-Bo Shi, Markus Heyl, Roderich Moessner et al. — [Reinforcement LearningtoHarness Approximation Errors for Long-Time QuantumSimulation](http://arxiv.org/abs/2608.20139v1)
  <details><summary>📄 Abstract</summary>
  Accurate digital quantum simulation at long times is limited by the accumulation of errors inherent to approximate simulation. Here we introduce RL-Trotter, a reinforcement-learning framework that treats unavoidable approximation errors as resources for error correction rather than merely imperfections to suppress. We show that low-dimensional information from conservation laws, such as the energy and energy variance, provides a sufficient learning signal to guide the agent, which learns to adap...
  </details>

- **2026-08-20** — Yingjian Chen, Fan Gao, Sherry T. Tong et al. — [HealMed: Multilingual Evaluation of Large Language Models in Medicine](http://arxiv.org/abs/2608.19981v1)
  <details><summary>📄 Abstract</summary>
  We present HealMed, an expert-reviewed benchmark for multilingual evaluation of large language models in medicine. HealMed contains 1,000 examples in each of nine languages, drawn from nine datasets and covering three task formats: MCQA, NLI and open-ended QA. The benchmark was developed over two years by 23 physicians and medical experts based across nine countries and regions. Each translation was evaluated and revised by two experts fluent in English and the corresponding target language. On ...
  </details>

- **2026-08-20** — Zhiyuan Jia — [Random Cap: Optimal Informationally Robust Delegation](http://arxiv.org/abs/2608.19846v1)
  <details><summary>📄 Abstract</summary>
  Are simple delegation rules optimal under ambiguity? We study delegation when the principal knows the mean, but not the distribution, of the agent's private information. In a quadratic constant-bias environment, the robustly optimal randomized mechanism is a random cap: the principal draws and reveals an upper bound below which the agent chooses freely. Randomization strictly outperforms every deterministic cap by hedging against cap-specific worst-case distributions. We characterize random caps...
  </details>

- **2026-08-20** — Rongyu Yu, Ke Niu, Fengxiang He — [Answer-Level Trust Selection for Physical Vision-Language Reasoning](http://arxiv.org/abs/2608.19807v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can estimate physical quantities such as duration, speed, and acceleration from visual observations, but existing benchmarks primarily assess overall model performance against annotated ground truth. In deployment, a key question is whether an individual prediction can be trusted when its ground truth is unavailable. Self-consistency alone may fail to capture important failure modes: a VLM may produce stable-but-wrong estimates or rely on textual priors rather than ...
  </details>

- **2026-08-20** — Haiyue Zhang — [Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay](http://arxiv.org/abs/2608.19760v1)
  <details><summary>📄 Abstract</summary>
  Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each deci...
  </details>

- **2026-08-20** — En Zhi Tan, Jia Xiang Lim, Bryan Lijie Chew et al. — [RecPFN: Prior-Fitted Networks for In-Context-Based Recommendations](http://arxiv.org/abs/2608.19735v1)
  <details><summary>📄 Abstract</summary>
  We introduce RecPFN, a prior-fitted network that brings in-context learning to sequential recommendation. RecPFN is pretrained entirely on synthetic clickstream environments sampled from a broad structural causal prior, enabling it to amortize Bayesian-style inference from a small support set. At inference, a lightweight decoder-only transformer conditions on a handful of domain sequences and produces next-item predictions for queries in a single forward pass, without any weight updates. Across ...
  </details>

- **2026-08-20** — Chenchen Lin, Wenhao Yuan, Xuehe Wang et al. — [Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration](http://arxiv.org/abs/2608.19701v1)
  <details><summary>📄 Abstract</summary>
  Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 20 papers

- **2026-08-24** — Jiawei He, Mengyu Shi, Jie jia et al. — [What Process Evaluation of Coding Agents Actually Measures: Action, Task, and Step Are Three Different Levels](http://arxiv.org/abs/2608.22960v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are increasingly evaluated not only by whether they solve a task, but also by how they execute it. However, existing process-level evaluations often treat action prediction, task uncertainty, and step attribution as if they were the same problem, which makes it unclear what such evaluations actually measure. In this paper, we introduce a measurement framework for process evaluation in coding agents and instantiate step-level causal attribution with SCAE, a replay-based estimator de...
  </details>

- **2026-08-24** —  Apodex Team, B. An, B. Li et al. — [Apodex 1.1: Scaling Agentic Intelligence for Complex Work](http://arxiv.org/abs/2608.23283v1)
  <details><summary>📄 Abstract</summary>
  General-purpose language models can reason and synthesize knowledge, but complex work also requires sustained interaction with files, information sources, and executable code, together with state maintenance, failure recovery, and verifiable delivery. We call this \emph{working capability}: sustained, verifiable progress toward a real-world objective. Apodex 1.1 develops this capability along two complementary dimensions. \emph{Environment Scaling} expands the diversity and verifiability of exec...
  </details>

- **2026-08-24** — Radouane Bouchekir, Damir Safin, Tomas Bueno Momcilovic — [From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents](http://arxiv.org/abs/2608.23282v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) agents deployed in vehicles must satisfy a written operating policy on every turn: a single hallucinated identifier, omitted mandatory side-effect, or premature completion claim fails the task. We present AgentGuardUtil, our entry to CAR-bench Track~1, which treats the AI planer (LLM) as a fallible proposer inside a grounded verify-and-revise loop. Its core novelty is a runtime policy compiler: the natural-language policy shipped with each conversation is compiled, o...
  </details>

- **2026-08-24** — Jieke Wang, Tiancheng Shen, Yibo Yang et al. — [Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner](http://arxiv.org/abs/2608.23268v1)
  <details><summary>📄 Abstract</summary>
  Frontier multimodal large language models (MLLMs) deliver impressive perception yet still falter on scientific and mathematical reasoning. Parameter-level adaptation is unavailable for closed-weight or on-device backbones, and stateless prompting forfeits any compounding benefit from problems already solved. We propose \textbf{DG-Mem}, a dual-grained agentic memory framework that augments a frozen MLLM with a non-parametric, externally stored memory built once from training-time rollouts and con...
  </details>

- **2026-08-24** — Dani Termaat, Nafiseh Soveizi, Zhiming Zhao et al. — [LLMCrater: Lifecycle-Aware FAIR Metadata Generation using Large Language Models](http://arxiv.org/abs/2608.23158v1)
  <details><summary>📄 Abstract</summary>
  FAIR (Findable, Accessible, Interoperable, and Reusable) metadata is essential for the discovery, interoperability, and reuse of scientific research assets. However, creating and maintaining FAIR metadata remains largely manual, making the process time-consuming for heterogeneous research artifacts generated throughout the research lifecycle. Existing approaches primarily generate metadata at publication time, missing opportunities to capture contextual information as it becomes available. To ad...
  </details>

- **2026-08-23** — Huangchen Xu, Yuan Wu, Yi Chang — [How Agents Represent Humans: Human-Directed Stereotypes in an Open Agent Social Network](http://arxiv.org/abs/2608.22192v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are increasingly deployed in persistent social environments, where generated claims can be posted, replied to, remembered, and reused. We study human-directed stereotypes on Moltbook, an open agent-native social platform, asking how agents construct humans as a social category. For this human-target analysis, we introduce an annotation framework with four evaluative dimensions---morality, friendliness, competence, and autonomy---and a second-stage subtype scheme for descriptive ...
  </details>

- **2026-08-23** — Zhixu Du, Yiran Chen — [AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems](http://arxiv.org/abs/2608.22160v1)
  <details><summary>📄 Abstract</summary>
  Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read ...
  </details>

- **2026-08-23** — Zhuoyu Shi, Fred Morstatter — [Gender Attribution in Causal Beliefs](http://arxiv.org/abs/2608.22150v1)
  <details><summary>📄 Abstract</summary>
  For centuries, women have been cast as the source of harm in public narratives, from witch hunts in early modern Europe to contemporary stereotypes about emotional instability. These cultural patterns reflect enduring biases in how people attribute causality and assign blame, often portraying women as agents of disruption and men as figures of rational authority. In this study, we examine how such gendered causal attributions appear in everyday language. Leveraging three complete 24-hour dataset...
  </details>

- **2026-08-23** — Karthik Sridhar, Atharva Gupta, Nishant Pradhan et al. — [Semantics or Structure? Auditing Text Sensitivity in Multimodal Time-Series Forecasting](http://arxiv.org/abs/2608.22321v1)
  <details><summary>📄 Abstract</summary>
  Multimodal time-series forecasting has emerged as a promising paradigm in which natural-language context is expected to improve predictive performance. Recent multimodal foundation models, including Aurora, as well as early- and late-fusion approaches such as MM-TSFlib and TaTS, report substantial gains over unimodal baselines on the Time-MMD benchmark, attributing these improvements to textual information. However, whether these models are actually sensitive to the semantic content of the text ...
  </details>

- **2026-08-23** — Oliver López Corona — [From Authorial Mathematics to Studio Mathematics:Ecobiontic Forms of Proof after Large Language Models](http://arxiv.org/abs/2608.22194v1)
  <details><summary>📄 Abstract</summary>
  Mathematics has often been organized around an authorial subject: one person, or a small group, composing proofs through language, notation, and judgment. Large language models, proof assistants, formal libraries, and repositories now make another production unit technically credible: a human-machine assemblage. This article calls that unit a studio ecobiont and asks when it is epistemically legitimate. Its governance thesis is that human participation is substantive only when the system preserv...
  </details>

- **2026-08-22** — Xinyuan Song, Bowen Zhu, Hasibul Haque et al. — [MegaMem: A Retrieval Solution for Ultra-Large Context Windows](http://arxiv.org/abs/2608.22137v1)
  <details><summary>📄 Abstract</summary>
  Modern language models and agents increasingly require persistent memory for complete codebases, long interaction histories, and heterogeneous enterprise records. The key challenge is to keep hundreds of millions of tokens searchable while passing only bounded source evidence to the answer model. We introduce MegaMem, a source-resolved dual-view retrieval system that separates semantic access from generation evidence. Distilled records and detailed evidence are searched with original and transfo...
  </details>

- **2026-08-22** — Maruf Ahmed Mridul, Abid Talukder, Oshani Seneviratne — [GrOIL: Graph-Grounded Domain Ontology Induction with Constrained LLM Mediation](http://arxiv.org/abs/2608.22135v1)
  <details><summary>📄 Abstract</summary>
  Constructing formal ontologies from domain documents requires simultaneously enforcing corpus grounding, vocabulary consistency, axiom-level expressivity, and end-to-end provenance, a combination no existing automatic system delivers. We present a seven-stage graph-grounded pipeline that converts domain documents into a complete, auditable Web Ontology Language (OWL) Terminological Box (TBox) without any unconstrained generation step. Documents are first encoded as Unified Discourse-Hypergraphs ...
  </details>

- **2026-08-21** — Jason Hickey — [AI with Authority, from Application to Silicon](http://arxiv.org/abs/2608.21356v1)
  <details><summary>📄 Abstract</summary>
  For sixty years, machine verification has been a major cost overhead, affordable only for exceptional artifacts. Here we report that generative AI inverts this relationship: at AI speed, machine verification is not only economical but essential to productivity --- it is the incorruptible referee that lets one person safely direct autonomous machine work at scale. In five weeks, one researcher on consumer AI subscriptions directed a small fleet of AI agents from application code, through a verifi...
  </details>

- **2026-08-21** — Chenguang Pan, Airui Meng, Youmi Suk — [Distilling Black-Box Machine Learning into a Small, Self-Explaining Language Model for Learning Analytics](http://arxiv.org/abs/2608.21165v1)
  <details><summary>📄 Abstract</summary>
  Learning analytics increasingly relies on flexible machine learning (ML), but the model opacity and the burden of deployment prevent these tools from reaching educational practice. We propose a two-stage fine-tuning pipeline that distills a fitted black-box estimator and its post hoc interpretation (the mentor) into a small, open-weight large language model (LLM; the mentee) that returns an individual-level estimate and explains in natural language. The design is estimator-agnostic and paired wi...
  </details>

- **2026-08-21** — Kyle Wild, Yusuke Takahashi, Asako Uraki — [RAG Deserves an Index: Why Ingest-Time Compilation Beats Query-Time Interpretation](http://arxiv.org/abs/2608.20845v1)
  <details><summary>📄 Abstract</summary>
  Nearly every retrieval-augmented question-answering system in production ships with a hidden interpreter: on each query a language model re-derives the meaning of raw corpus text and then throws that work away. Cheaper models do not close the gap: per-token prices have fallen by orders of magnitude while inference spend has risen, because context volume grows faster than prices fall. This is the modern equivalent of the full-table scan, and the remedy is the one databases found fifty years ago: ...
  </details>

- **2026-08-20** — Jun Ni Du, Lukas Adamek, Maxim Kryukov et al. — [Explainable Transformer Models for Clinical Prediction Tasks on Structured Electronic Health Records](http://arxiv.org/abs/2608.20315v1)
  <details><summary>📄 Abstract</summary>
  Predictive models over structured electronic health records (EHRs) remain central to machine learning for healthcare, but few have jointly emphasized quantitative laboratory information and interpretability with respect to input medical events. We present BERT-LER, a BERT-style model for coded EHR timelines pretrained and fine-tuned from a de-identified EHR dataset of 75 million patients, that encodes laboratory test results as discrete tokens while retaining graded information through percentil...
  </details>

- **2026-08-20** — Bhavya Gupta, Onat Gungor, Tajana Rosing — [G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs](http://arxiv.org/abs/2608.19964v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects ...
  </details>

- **2026-08-20** — Zijiao Chen, Nicholas Lu, Xinhui Li et al. — [Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis](http://arxiv.org/abs/2608.19902v1)
  <details><summary>📄 Abstract</summary>
  AI agents can execute scientific analyses, but an analytic output becomes a defensible claim only after alternatives are weighed and the claim is limited to what the evidence supports. Agents may reproduce failures including selective analysis, premature declarations of success and optimization of imperfect criteria. We present Brain Researcher, an agentic research harness operating in a neuroimaging researcher's computational environment under rules for admissible analyses, required checks and ...
  </details>

- **2026-08-20** — Nikita Khudov — [OenoBench: A Wine-Domain Benchmark for Knowledge-Grounded Evaluation of Large Language Models](http://arxiv.org/abs/2608.20106v1)
  <details><summary>📄 Abstract</summary>
  We introduce OenoBench, a wine-domain knowledge benchmark of 3,266 multiple-choice questions across six pillars (regions, grape varieties, viticulture, winemaking, producers, business) and four difficulty tiers. The corpus is built from 38,104 atomic, source-anchored facts extracted by 35 provenance-verified scrapers from government registries (INAO, TTB, OIV), peer-reviewed journals, and Wikipedia/Wikidata. Our methodological contribution is an LLM-driven pipeline in which language models refor...
  </details>

- **2026-08-20** — Willem Fourie — [A three-dimensional typology of agency for advanced AI systems](http://arxiv.org/abs/2608.20041v1)
  <details><summary>📄 Abstract</summary>
  Research on the agency of advanced artificial intelligence (AI) systems focuses on agency as a normative concept and on the agency of particularly agentic AI systems. While recent work also focuses on the different profiles of agentic systems, no framework exists to address the question of the type of agency instantiated by advanced AI systems, particularly when considering non-moral forms of agency. Based on established theoretical positions in philosophy, ethics, legal theory and sociology, we...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-08-23** — Noam Diamant, Ethan Fetaya, Neta Glazer — [Stress Testing Unlearning Algorithms](http://arxiv.org/abs/2608.22527v1)
  <details><summary>📄 Abstract</summary>
  Recently, machine unlearning, the removal of specific training data influence from a model, has gained increasing attention. In large language models (LLMs), unlearning is particularly challenging due to the ambiguity of inputs and outputs. Con- sequently, rigorous evaluation is critical for assessing both safety and utility, and for driving progress in unlearning meth- ods. We identify two key shortcomings in existing unlearning benchmarks: (1) they do not actively test whether unlearned inform...
  </details>

- **2026-08-21** — Snigdha Paul, Manasi Patwardhan, Arman Cohan — [Can Scientific Claims Be Removed from Large Language Models? A Systematic Evaluation of Claim-Level Unlearning](http://arxiv.org/abs/2608.20960v1)
  <details><summary>📄 Abstract</summary>
  Language models (LMs) are trained on static scientific corpora, whereas scientific knowledge continuously evolves through correction and revision. Scientific claims encoded within these models may later become retracted, disproven, or updated by subsequent research, creating the risk of disseminating outdated information in scientific workflows. This creates a need for LMs to forget obsolete scientific claims. Machine unlearning offers a promising solution by enabling knowledge removal while mai...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 3 papers

- **2026-08-24** — Xuetong Li, Gaofeng Liu — [EviSafe: Evidence-Grounded Safety Evaluation for Vision-Language Models](http://arxiv.org/abs/2608.23313v1)
  <details><summary>📄 Abstract</summary>
  Vision-language model safety benchmarks typically evaluate only final responses: whether a model refuses, warns, or complies. This outcome-level view cannot tell whether a model is safe for the right multimodal reason. Safelooking behavior may reflect keyword-triggered refusal, missed visual hazards, or over-refusal of benign-sensitive inputs. We introduce EviSafe, an evidence-grounded framework for VLM safety that jointly evaluates natural user-facing behavior, explicit grounding in textual and...
  </details>

- **2026-08-23** — Seyed Mohammad Mahdi Ghalandarian, Majid Bazargani, Masoumeh Taromirad — [Benchmarking the Titans: A Multi-Dimensional Empirical Evaluation of LLM Code Generation Quality in the .NET Ecosystem](http://arxiv.org/abs/2608.22529v1)
  <details><summary>📄 Abstract</summary>
  Evaluating Large Language Model (LLM) code generation quality requires examining not just whether the generated code is correct, but whether it is maintainable, efficient, and stylistically sound, all of which are qualities of direct importance to software engineering practitioners. Existing benchmarks reduce evaluation to a single Pass@k metric, which obscures critical trade-offs between functional correctness and structural quality. A further limitation is the near-exclusive focus on Python, l...
  </details>

- **2026-08-21** — Kai Wang, Zeming Wei, BiaoJie Zeng et al. — [ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents](http://arxiv.org/abs/2608.21101v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reapp...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 4 papers

- **2026-08-24** — Mullosharaf K. Arabov — [A Comprehensive Analysis of Arabic Natural Language Processing Research: Trends, Topic Evolution, and Research Gaps -- A Bibliometric and Topic-Based Study](http://arxiv.org/abs/2608.23421v1)
  <details><summary>📄 Abstract</summary>
  Natural Language Processing (NLP) has grown rapidly over the past decade, driven by digital transformation in the Arab world, social media, and large language models (LLMs). Despite this growth, a comprehensive quantitative meta-analysis of the field remains absent. This study presents a large-scale bibliometric and topic-based analysis of 7,120 Arabic NLP papers published between 1960 and 2026, sourced from six collections. We employ BERTopic for topic modeling, regression analysis to identify ...
  </details>

- **2026-08-24** — Virgile Rennard, Christos Xypolopoulos — [Large language models simulate intersectional synthetic identities with a budget of one to two dimensions](http://arxiv.org/abs/2608.23005v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used as synthetic survey respondents, promising cheap access to rare intersectional populations. We test standard demographic-persona methods against every real intersectional subgroup across 15 waves of Pew's American Trends Panel -- 21 million simulated response distributions from eight models. In real respondents, subgroup opinion is approximately the additive sum of its single-identity components, yet grows 2.5x more distinctive as identities intersect....
  </details>

- **2026-08-23** — Yikai Gao, Ding Xia, Xi Yang — [Query-Driven Multimodal Information Extraction from Long Documents](http://arxiv.org/abs/2608.22214v1)
  <details><summary>📄 Abstract</summary>
  In domain-specific multimodal long documents, images and text jointly convey complex knowledge that cannot be fully captured by plain text alone. However, existing paradigms like DocVQA primarily focus on generating textual answers or localizing evidence regions, rather than outputting query-specific textual attribute values and corresponding images. To address this gap, we propose query-driven image-text joint extraction from long documents, requiring models to output query-requested textual at...
  </details>

- **2026-08-20** — Joan Perez, Giovanni Fusco — [From Street View Imagery to Street Quality Indicators: Vision Language Inference for the Suburban 15-minute City](http://arxiv.org/abs/2608.20026v1)
  <details><summary>📄 Abstract</summary>
  Streetscape quality has become a central concern in contemporary urban planning, particularly within the framework of the pedestrian-friendly 15-minute city, where walkability and public-space quality are increasingly recognized as key determinants of urban performance. However, assessing streetscape qualities across large suburban and peri-urban territories remains challenging due to the time and resource demands of conventional field surveys. This paper presents a planning-oriented assessment ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 157 papers

- **2026-08-24** — Penghui Qi, Xiangxin Zhou, Wee Sun Lee — [How to Train a Critic Stably and Efficiently](http://arxiv.org/abs/2608.23566v1)
  <details><summary>📄 Abstract</summary>
  Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop \textbf{Best-Practice Critic Optimization (BPCO)}, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormal...
  </details>

- **2026-08-24** — Thanh-Khoi Nguyen, Thanh-Nhan Vo, Trong-Thuan Nguyen et al. — [Action-Aligned Retrieval with Pairwise Multimodal Reranking for Text-Based Person Anomaly Search](http://arxiv.org/abs/2608.23503v1)
  <details><summary>📄 Abstract</summary>
  Text-based person anomaly search requires distinguishing individuals based on fine-grained, context-dependent behaviors rather than mere appearance. Existing methods struggle to capture these context-conditioned actions, frequently relying on isolated skeletal geometry, discarding raw query details during reformulation, or utilizing absolute pointwise scoring for multimodal verification. To address these limitations, we propose \textbf{ActPair}, a unified three-stage coarse-to-fine framework tha...
  </details>

- **2026-08-24** — Yiren Lu, Xin Ye, Jiaming Liu et al. — [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](http://arxiv.org/abs/2608.23486v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving. Most existing WAMs learn scene dynamics in pixel space by combining a video-generation backbone for future-observation prediction with an action head for ego-trajectory prediction. Pixels, however, provide only an indirect representation of these dynamics: they entangle geometry and motion with appearance, texture, and illumination, forci...
  </details>

- **2026-08-24** — Guilherme Rodrigues-Fontenele, Gabriel Fontenele, Ângelo Malachias et al. — [Defect-Mediated Nucleation and Dynamics across the Phase Transition in the Excitonic Insulator Candidate Ta2NiSe5](http://arxiv.org/abs/2608.23438v1)
  <details><summary>📄 Abstract</summary>
  Ta2NiSe5 is a quasi-one-dimensional material that exhibits a structural and electronic phase transition from a low-temperature monoclinic (semiconductor) to a high-temperature orthorhombic (semimetal) phase at approximately TC = 326 K. Here, we used variable-temperature scanning tunneling microscopy and spectroscopy to resolve the phase transition spatially, identifying the distinct spectroscopic signatures of the monoclinic and orthorhombic phases in pristine regions and near isolated point-def...
  </details>

- **2026-08-24** — Federico Stella, Fei Jiang, Zhongshi Jiang et al. — [Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers](http://arxiv.org/abs/2608.23410v1)
  <details><summary>📄 Abstract</summary>
  Photorealistic novel view synthesis of people remains challenging at high spatial resolutions and across multiple target cameras, where preserving identity, fine appearance details, and geometric coherence is critical. We build on the next-scale autoregressive paradigm and adapt it for human-centric view synthesis by enabling higher image resolutions, multi-view outputs and stronger cross-view consistency in a single forward pass. We train on a synthetic dataset of human faces spanning diverse i...
  </details>

- **2026-08-24** — Hao Liu, Steven Liu, Xin Zhang et al. — [DPIAgent: Divide, Protocol, Isolate for Agentic Reproduction Test Generation](http://arxiv.org/abs/2608.23341v1)
  <details><summary>📄 Abstract</summary>
  Reproduction test generation, producing a failing-then-passing test that captures a reported bug, is a critical step in automated software engineering. Existing agentic methods treat this as a monolithic loop, despite the task inherently comprising two subtasks of distinct nature: diagnosing the root cause and writing a fail-to-pass test. Without explicit separation, the agent faces a compound objective with underspecified intermediate goals, leading to goal drift. We propose DPIAgent, a structu...
  </details>

- **2026-08-24** — Haoyi Zhong, Fang-Lue Zhang, Andrew Chalmers et al. — [Mover360: Controllable Object Manipulation in 360° Panoramic Images](http://arxiv.org/abs/2608.23238v1)
  <details><summary>📄 Abstract</summary>
  We present Mover360, a controllable object manipulation framework for 360° images. Unlike perspective images, 360° images in equirectangular projection (ERP) exhibit horizontal wrap-around, latitude-dependent distortion, and global scene continuity, which makes object-level edits difficult for existing perspective editors to produce and for users to specify. To address this, Mover360 centers on object Translation (relocating a specified object within an existing panorama) while supporting refere...
  </details>

- **2026-08-24** — Fan Xu, Luis A. Leiva — [Training-Free Pseudo-Fusion for Composed Image Retrieval with Diffusion Models and Multimodal Large Language Models](http://arxiv.org/abs/2608.23102v1)
  <details><summary>📄 Abstract</summary>
  Composed Image Retrieval (CIR) is an emerging paradigm in content-based image retrieval that enables users to formulate compositional queries by combining a reference image with an auxiliary modality, usually text-based. This approach supports fine-grained search where the target image shares structural elements with the user-provided image while incorporating the modifications specified by the auxiliary text. Conventional CIR methods rely on multimodal fusion to combine visual and textual featu...
  </details>

- **2026-08-24** — Xiwei Liu, Yulong Li, Xinlin Zhuang et al. — [Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning?](http://arxiv.org/abs/2608.23074v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) can answer spatial questions, yet the mechanisms connecting object grounding to spatial reasoning remain poorly understood. It is underexplored whether spatial reasoning internally requires precise objects localization, or can bypass explicit localization through global layout cues. In this work, we investigate two representative model families, LLaVA-1.5 and Qwen2.5-VL, using a suite of mechanistic interpretability tools, including token ablation, layer-wise probin...
  </details>

- **2026-08-24** — Ha Dinh, Xuan Duy Ta, Khoat Than et al. — [Reservoir of Importance: Learning Semi-Structured Sparsity with Differentiable Subset Sampling](http://arxiv.org/abs/2608.23048v1)
  <details><summary>📄 Abstract</summary>
  Semi-structured $N$:$M$ sparsity has emerged as a practical direction for accelerating large language models (LLMs). However, existing learnable-mask approaches incur substantial parameter and memory overhead, limiting their scalability to large models and aggressive sparsity regimes. In this work, we revisit semi-structured pruning from a perspective that reconciles efficiency with scalability. We propose Reservoir of Importance (RoI), a lightweight semi-structured pruning framework that learns...
  </details>

- **2026-08-24** — Yinze Hu, Hongjun Xiang, Xingao Gong et al. — [A Physical Response-and-Memory Model for Muon Optimization](http://arxiv.org/abs/2608.22994v1)
  <details><summary>📄 Abstract</summary>
  Training large language models is costly. How low a loss the same compute can ultimately reach depends on how each step's gradient is converted into a weight update; the rule that performs this conversion is the optimizer. From SGD and AdamW to the recent Muon, effective update rules have mostly been shaped by engineering intuition and then selected on benchmarks. Muon semi-orthogonalizes the momentum matrix before applying the update and has kept breaking records on public training benchmarks; ...
  </details>

- **2026-08-24** — Jiří Vyskočil, Franz Pöschel, Andreas Knüpfer — [Concepts for Securing Agentic AI Coding and the Terok Environment](http://arxiv.org/abs/2608.22930v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is a fascinating new tool for software development. It is a huge step forward compared to "conventional" AI assisted coding, which in turn was a considerable breakthrough earlier. AI support through LLMs is a young and very fast-moving field. The "conventional" (non-agentic) flavor became useful and productive in early 2025 (around 18 months ago) and the agentic flavor followed in fall 2025 (approximately 9 months ago). Besides all its benefits and potential, it also carries some fund...
  </details>

- **2026-08-24** — Yusheng Zheng, Xiaoyu Song, Yanpeng Hu et al. — [When Can Agents Safely Checkpoint, Fork, Restore, and Merge? Exact Checking for Execution Edits](http://arxiv.org/abs/2608.22928v1)
  <details><summary>📄 Abstract</summary>
  Agent runtimes can Checkpoint an execution, Fork it, Restore a checkpoint, or Merge branches without restarting a task. We call these operations execution edits, with Checkpoint recording the current execution for later use and Fork, Restore, and Merge changing what the Agent will do next. An execution edit cannot undo an earlier authorization or a tool request already sent. An unsafe edit can therefore authorize the same tool action twice, discard a result the task still requires, or conflict w...
  </details>

- **2026-08-24** — Pornthep Ukosaramig, Kobkrit Viriyayudhakorn — [TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor](http://arxiv.org/abs/2608.22917v1)
  <details><summary>📄 Abstract</summary>
  We present TSWAP, a deployed eight-language conversational wellness advisor grounded, via retrieval-augmented generation, in a verified knowledge base of Thai traditional medicine and certified wellness providers. An unmodified open-weight LLM (Qwen3.6-35B-A3B on vLLM) is grounded on a ~30.6K-chunk Thai index by a hybrid dense-sparse retriever with cross-encoder reranking; a first-turn query classifier forces tool-based retrieval for entity lookups; a rule-based safety layer enforces medical sco...
  </details>

- **2026-08-24** — Akifumi Wachi, Takumi Tanabe, Youhei Akimoto — [Safety Hacking in Constrained Best-of-$N$ Inference-time Scaling](http://arxiv.org/abs/2608.22915v1)
  <details><summary>📄 Abstract</summary>
  Inference-time pipelines often sample multiple outputs, filter them with a learned safety model, and return the proxy-feasible output with the highest learned reward. We show that this composition creates a two-stage failure: an imperfect safety proxy first contaminates the feasible set with unsafe outputs, and reward maximization can then amplify this residual contamination. We define \emph{safety hacking} as selecting an output that passes the learned constraint but violates the true safety cr...
  </details>

- **2026-08-24** — Sahong Park, Suhwan Park, Hoyoung Lee et al. — [Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron](http://arxiv.org/abs/2608.22852v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in investment decision-making, yet prior work shows that they exhibit systematic, model-specific investment preferences. We study whether a model's overall investment stance can be calibrated to a specified direction and strength. We introduce an investment-bias dial, an inference-time intervention on a single neuron that continuously adjusts a model-level decision prior---its overall tendency toward buying or selling---without targeting specifi...
  </details>

- **2026-08-24** — Ziyuan Wang, Bohao Tang, Fei Zhang et al. — [RIBOSPAN: A Long-Context RNA Foundation Model for Versatile RNA Modeling](http://arxiv.org/abs/2608.22849v1)
  <details><summary>📄 Abstract</summary>
  Full-length RNAs, particularly messenger RNAs, often exceed the context lengths used to pretrain existing RNA foundation models, limiting complete-transcript modeling at single-nucleotide resolution. We present RIBOSPAN, a 1.61-billion-parameter bidirectional RNA foundation model natively pretrained with context lengths up to 10,240 nt. RIBOSPAN combines dense bidirectional self-attention, single-nucleotide tokenization, and attention-isolated sequence packing to enable high-resolution modeling ...
  </details>

- **2026-08-24** — Ahnaf Atef Choudhury, Ramkrishna Saha — [SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support](http://arxiv.org/abs/2608.22802v1)
  <details><summary>📄 Abstract</summary>
  Medical large language models are often judged by how many clinical questions they answer correctly. That view is useful, but it misses a practical risk. A model may know the right answer and still change its response when the same case is written in a different patient voice. This paper evaluates that risk as SDoH aware narrative anchoring bias. We use NarrativeShield SDoH MedQA, a counterfactual medical question answering dataset in which each case appears in persona based narratives while the...
  </details>

- **2026-08-24** — Alexander J. Hish, Arjun Nagendran, Scott N. Compton — [Performance of a domain-specific large language model in answering patient questions in psychiatry](http://arxiv.org/abs/2608.22797v1)
  <details><summary>📄 Abstract</summary>
  Background This study was designed to evaluate whether a domain-specific large language model (LLM) trained exclusively on patient education resources can answer questions about psychiatric medications, in a manner superior to LLM chatbots. We developed an LLM ("MIND") fine-tuned for clinical fidelity, trained on patient education resources from authoritative medical organizations. Methods We compared the responses of MIND, ChatGPT, and OpenEvidence to patient questions about escitalopram, using...
  </details>

- **2026-08-24** — Rui Xue, Tianfu Wu — [ReCoG: Reciprocal Co-Evolution for Multimodal Graph Learning](http://arxiv.org/abs/2608.22786v1)
  <details><summary>📄 Abstract</summary>
  Multimodal graph learning requires jointly training over graph structure and heterogeneous node attributes, yet existing methods largely decouple these processes: prior multimodal graph neural networks (GNNs) focus on aligning modalities in a shared embedding space while operating on fixed or weakly adapted graph structures, and graph structure learning approaches infer topology from unimodal node representations without accounting for multimodal interactions. This separation fundamentally limit...
  </details>

- **2026-08-24** — Xuan Yao, Li Shuping, Dai Yang et al. — [DelistBench: Evaluating Search-Enabled LLMs for Auditable Corporate-Event Database Completion](http://arxiv.org/abs/2608.22770v1)
  <details><summary>📄 Abstract</summary>
  Financial institutions need an independent way to detect missing, stale, and misclassified corporate-event records in vendor databases. We introduce Search-to-Record, a database-assurance task in which search-enabled large language models reconstruct institution-defined event records from public sources for a known security universe and historical cutoff, and DelistBench, a 1,200-record benchmark for security-level delisting announcements. We evaluate five models in paired closed-book and web-en...
  </details>

- **2026-08-24** — Saber Zerhoudi, Jelena Mitrovic, Michael Granitzer — [The Compaction Cliff in Long-Running AI Agent Memory](http://arxiv.org/abs/2608.22752v1)
  <details><summary>📄 Abstract</summary>
  A safety rule and an episodic log compete for the same tokens in an AI agent's context. When the budget overflows, both are summarized at the same rate; only the rule needs exact wording to remain enforceable. On 20 production agent configurations, Claude Code's /compact prompt on Sonnet 4.6 preserves 53\% of safety rules after one compaction round and 10\% after five. We name this the Compaction Cliff. We address it with Knowledge Triage, a framework that classifies each line of an agent's know...
  </details>

- **2026-08-24** — Zeyang Bai, Yunpeng Wang, Yunbiao Wang et al. — [Seeing the Unseen: Semantic-in-Gaussian for Sparse-View 3D Generalization](http://arxiv.org/abs/2608.22740v1)
  <details><summary>📄 Abstract</summary>
  Generalizable 3D Gaussian Splatting (G-3DGS) has emerged as a promising approach for novel view synthesis undersparse-view settings. However, existing frameworks remain restricted by pixel-aligned Gaussian estimation, whichstruggles in partially observed or occluded regions and often leads to incomplete surfaces or structural collapse. Toaddress these challenges, we propose SeeU (Seeing the Unseen), a novel G-3DGS framework. We frame its core design asSemantic-in-Gaussian: semantic-conditioned r...
  </details>

- **2026-08-24** — Mining Tan, Yinuo Wang, Ziqi Zhou et al. — [Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation](http://arxiv.org/abs/2608.22757v1)
  <details><summary>📄 Abstract</summary>
  Unified models for visual understanding and generation have made rapid progress, yet they still lack the ability to understand and manipulate the spatial states of object instances. Existing models can describe objects in natural language, but they struggle to precisely represent continuous object poses and generate geometrically consistent images under target viewpoints. To mitigate this, we propose \emph{Object-Uni}, a unified model for object-centric spatial understanding and controllable gen...
  </details>

- **2026-08-24** — Erin Craig, Yiling Huang, Snigdha Panigrahi — [Interpretable AI with Local Distillation](http://arxiv.org/abs/2608.23538v1)
  <details><summary>📄 Abstract</summary>
  Modern AI models such as tabular foundation models and gradient-boosted ensembles can outpredict classical methods, but provide little basis for reasoning about their predictions. High-stakes decisions call for models that are both accurate and interpretable as built. Local linear modeling offers a path forward: a smooth regression function is locally well approximated by a linear one, allowing a linear fit near each query point to achieve high accuracy without sacrificing transparency. The chal...
  </details>

- **2026-08-24** — Stanislav Škorňa, Jitka Machalová — [Penalized likelihood estimation of probability density functions using compositional splines](http://arxiv.org/abs/2608.23512v1)
  <details><summary>📄 Abstract</summary>
  Probability density functions are commonly estimated through preliminary smoothing or aggregation procedures, e.g., histograms or kernel density estimation, before subsequent functional representation and functional data analyses. Such a two-stage approach can lead to additional approximation bias and weaken the direct connection between the observed data and the underlying distributional structure. In this paper, we propose a penalized maximum likelihood framework for direct estimation of proba...
  </details>

- **2026-08-24** — Naman Garg, Sarika Jain, George Fazekas — [Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational Music Recommendation](http://arxiv.org/abs/2608.23484v1)
  <details><summary>📄 Abstract</summary>
  We present Team Semiintelligencn's solution for the ACM RecSys 2026 TalkPlayData Challenge, addressing conversational music recommendation through a multi-modal and personalized conversational recommender system. Our submitted system employs a three-stage pipeline: (1) multi-modal retrieval constructing decay-weighted centroids across seven dense embedding spaces - track- and user-level CF-BPR, Qwen3 (metadata, lyrics, attributes), CLAP audio, and SigLIP visual - supplemented by BM25 lexical ret...
  </details>

- **2026-08-24** — Kenneth L. Kearns, M. D. Ediger, Heiko Huth et al. — [One micron length scale controls kinetic stability of low energy glasses](http://arxiv.org/abs/2608.23454v1)
  <details><summary>📄 Abstract</summary>
  AC nanocalorimetry was used to measure the reversing heat capacity Cp of low energy indomethacin glasses as they isothermally transform into the supercooled liquid. As the film thickness increases from 75 to 600 nm, the transformation time increases by more than an order of magnitude, consistent with a surface-initiated transformation mechanism. Eventually, the transformation time becomes constant for films between 1.4 and 30 microns indicating a distinct bulk transformation pathway. The observa...
  </details>

- **2026-08-24** — Hamid Bekamiri, Jan Auernhammer, Milad Abbasiharofteh et al. — [Systematic Bias in Green Patent Classification: Silent Green and False Green](http://arxiv.org/abs/2608.23420v1)
  <details><summary>📄 Abstract</summary>
  Green-patent indicators built on Cooperative Patent Classification Y02 tags are widely used in research, policy, and investment, yet their construct validity has not been audited at corpus scale. We assess whether Y02 is systematically biased and whether that bias may reinforce the ESG innovation disconnect. We introduce an Error-as-Signal framework that treats disagreement between an administrative label and an independent model as diagnostic evidence of measurement error. Screening 9,075,421 U...
  </details>

- **2026-08-24** — Seyed Mohammad Hossein Hashemi, Mohsen Hooshmand, Parvin Razzaghi — [Modalities Should Talk to Each Other: Dual-Stream Multimodal Learning for Long-Horizon Influenza Forecasting](http://arxiv.org/abs/2608.23373v1)
  <details><summary>📄 Abstract</summary>
  Forecasting long-range influenza-like illness (ILI) matters for public health readiness. Publicly available surveillance datasets typically pair numeric epidemiological signals with textual information that is noisy, loosely structured, only indirectly related to near-term trends, and often lagged relative to the numeric signal. Fusing the two therefore requires careful design. We propose Dual-Stream Attention (DSA), a multimodal deep learning framework that forecasts 12-week-ahead ILI activity ...
  </details>

- **2026-08-24** — Matthew Perlman, Atharva Nijasure, James Allan — [The Emergence of Relevance Through Axiomatic Attention Patterns During LoRA Fine-Tuning](http://arxiv.org/abs/2608.23338v1)
  <details><summary>📄 Abstract</summary>
  LoRA fine-tuning is standard for adapting LLMs to reranking, but it remains unclear where in the network task-specific relevance behavior is learned and what attention-level changes accompany that learning. Through ablation and attention experiments, we identify where LoRA attention updates to RankLLaMA improve performance and whether those gains coincide with interpretable relevance-oriented attention patterns such as lexical matching, rarity sensitivity, and query-document interaction. We find...
  </details>

- **2026-08-24** — Zeyd Boukhers, Lingxiao Kong, Xenophon Zabulis et al. — [Automated Construction of FAIR Digital Object Knowledge Graphs from Flat Cultural Heritage Records](http://arxiv.org/abs/2608.23263v1)
  <details><summary>📄 Abstract</summary>
  The FAIR Digital Object (FDO) framework mandates that metadata attribute values be expressed as persistent identifiers (PIDs) wherever possible, to produce a fully machine-actionable graph in which every reference is resolvable. The Europeana Data Model was designed long before the FDO specification, and it stores most metadata values as plain text. This serves human browsing well enough, but gives an automated agent nothing to follow across records or collections. We present a pipeline that tra...
  </details>

- **2026-08-24** — Jinghui Zhang, Lang Gao, Ao Li et al. — [LITERARYBIGFIVE: Author-Personalized Text Generation in a Unified Interpretable Space](http://arxiv.org/abs/2608.23124v1)
  <details><summary>📄 Abstract</summary>
  Personalized text generation for authors and literary writing is essential for applications such as adaptive writing assistants, creative support tools, and computational literary analysis. However, existing approaches to author modeling and personalization often represent writing behavior as independent labels, requiring large-scale corpus collection or fine-tuning for each author or stylistic category. Such formulations are costly, difficult to interpret, and poorly suited for generalizing acr...
  </details>

- **2026-08-24** — Nafis Tanveer Islam, Nafiseh Soveizi, Yutong Li et al. — [From Metrics to Improvement: A Lifecycle-Aware LLM Feedback Framework for Research Software Quality](http://arxiv.org/abs/2608.23118v1)
  <details><summary>📄 Abstract</summary>
  Research software is increasingly central to scientific workflows, yet it is often developed by researchers with limited software engineering expertise. This can lead to quality issues that hinder maintainability, reproducibility, reuse, and sustainability. Existing static analysis tools can identify such issues, but their outputs often require expert interpretation and provide limited support for translating quality assessments into actionable improvements. To address this gap, we propose a lif...
  </details>

- **2026-08-24** — Yuanjun Feng, Tanzhou Liu, Stefan Feuerriegel et al. — [Beyond Surface Cues: Disentangling Sociocultural Signals in Multilingual LLMs](http://arxiv.org/abs/2608.23026v1)
  <details><summary>📄 Abstract</summary>
  Multilingual LLM outputs can vary across sociocultural contexts. However, evidence of cultural grounding can be misleading: identity labels may be inferred from explicit or indirect textual cues, while names and wording can reveal the source language. Treating all these signals as evidence of cultural grounding may obscure potential biases. We present a human-validated, multi-agent audit that separates three questions: whether outputs reproduce social biases, whether identity groups are represen...
  </details>

- **2026-08-24** — Suhyeon Lee, Juneha Baek, Jaehyeong Park et al. — [LLM Pedagogical Behavior in AI Tutoring Interactions](http://arxiv.org/abs/2608.22993v1)
  <details><summary>📄 Abstract</summary>
  Students increasingly use LLMs as tutors for coursework and problem solving. Little is known about the level of assistance LLMs provide when students use them as tutors in authentic learning interactions. This matters because tutoring responses can differ substantially in how directly they help students complete a task. We operationalize this dimension as scaffolding level and develop a five-level scale, validated against human annotations, that characterizes responses according to the degree of...
  </details>

- **2026-08-24** — Zeyu Wang, Xinming Xu — [Knowing Isn't Always Saying: When Do Spatial Encodings Reach Answers in Vision-Language Models?](http://arxiv.org/abs/2608.22916v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models are known to encode spatial information in their hidden states, yet often fail to use it when answering. However, it remains unclear when and where this encoded information reaches the answer. We address this with direction patching, a class-conditioned causal intervention applied across layers, token positions, and prompt formats. Using spatial-ID directions constructed following prior encoding evidence, we find that causal influence on answer logits emerges only at mid-t...
  </details>

- **2026-08-24** — Chang-Youn Moon — [Revised symmetry rule and intrinsically time-reversal symmetry breaking pairing in multi-orbital superconductors](http://arxiv.org/abs/2608.22902v1)
  <details><summary>📄 Abstract</summary>
  We investigate the basic symmetry rule for the particle permutation in superconducting (SC) pairing states by examining the numerical solution of the linearized Eliashberg equation for Sr$_2$RuO$_4$. We find that the general multi-band, frequency-dependent SC gap function does not simply transform to itself up to the minus sign with either orbital ($\hat{O}$) or frequency ($\hat{T}$) exchange between two pairing electrons, contradicting the common assumption which has been used without verificat...
  </details>

- **2026-08-24** — Zengqing Wu, Chuan Xiao — [Proxy reliance in large language model decisions is uncalibrated to predictive evidence](http://arxiv.org/abs/2608.22887v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are entering decisions in triage and lending, where task-relevant inference must be distinguished from impermissible proxy use. Current audits ask whether decisions change when demographics change. But attributes correlated with a protected group carry predictive value, so a changed decision can be discrimination or sound inference. We measure causal proxy effects in four LLMs on a clinical-ranking task with known ground truth, where the reliance the evidence warrant...
  </details>

- **2026-08-24** — Zengqing Wu, Chuan Xiao — [Predicting the scale limits of social mechanisms in agent societies](http://arxiv.org/abs/2608.22884v1)
  <details><summary>📄 Abstract</summary>
  Societies of interacting language-model agents offer a controllable and repeatable way to study collective behaviour at scales that would be difficult to test with people. Their scientific value, however, depends on whether a social mechanism that works in a small group still operates when thousands of agents interact, and testing this directly requires costly large-scale runs. Here we introduce an audit that predicts a mechanism's fate as a population grows. It asks how often the mechanism can ...
  </details>

- **2026-08-24** — Nizar Touzi, Yuxing Huang — [Backward SDE characterization of the finite horizon Principal-Agent problem](http://arxiv.org/abs/2608.22818v1)
  <details><summary>📄 Abstract</summary>
  We consider the finite horizon continuous-time Principal--Agent problem under deterministic discount factors. Following the Sannikov reduction to a stochastic control problem, we provide a further characterization of the Principal's value function in terms of a backward SDE inducing the corresponding optimal contract. In particular, this allows to bypass the fully nonlinear HJB equation satisfied by the Principal value function in the Markovian setting. This new approach allows to handle a new c...
  </details>

- **2026-08-24** — Yue Zhao — [CatchBench: When Can an Agent Failure Be Caught?](http://arxiv.org/abs/2608.22808v1)
  <details><summary>📄 Abstract</summary>
  When can an agent failure be caught? An audit is usually limited by the record rather than by the method. CatchBench therefore puts one auditor's question to three information states: the declared configuration before a run (PRE), a growing prefix of its trace (LIVE), and the finished trace (POST). Prior benchmarks fix one of these states or vary the telemetry; to our knowledge none scores all three under one task-method interface. Each state admits different questions, so seven task contracts c...
  </details>

- **2026-08-24** — Yufan Wang, Rui Yang, Yi Liu et al. — [A Source-Grounded Framework for Constructing and Evaluating Progressive Multimodal Diagnostic Dialogues from Clinical Case Reports](http://arxiv.org/abs/2608.22713v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis requires progressive integration of patient history, physical examination, laboratory findings, medical images, and diagnostic-informative tests. However, most multimodal medical benchmarks evaluate fixed inputs or endpoint answers, while fully interactive diagnostic agents conflate evidence selection with evidence interpretation. We present a source-grounded framework to construct progressive multimodal diagnostic dialogues from case reports and an evaluation strategy for ass...
  </details>

- **2026-08-24** — Davood Wadi, Yu Ma — [Does Rank Still Matter? Position Bias When AI Agents Shop on Our Behalf](http://arxiv.org/abs/2608.22697v1)
  <details><summary>📄 Abstract</summary>
  Search rankings are valuable because human attention is scarce and sequential. Higher-placed alternatives are easier to find, so they are examined and bought more often. Consumers are now delegating search to AI agents that can ingest an entire results page at once. Randomizing the order of one hundred hotel listings across 5,000 AI agent sessions, we compare four large language models against human field data. AI agents search more deeply than humans and never decline to buy. Position still pre...
  </details>

- **2026-08-24** — Yujuan Ding, Linyin Luo, Shijie Wang et al. — [FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for Fashion Question Answering](http://arxiv.org/abs/2608.22688v1)
  <details><summary>📄 Abstract</summary>
  Fashion is a knowledge-intensive domain in which effective decision-making depends on integrating multiple types of knowledge. Although Large Language Models (LLMs) have transformed many areas, their application in fashion remains limited by hallucinations and weak domain specialization. Knowledge Graph (KG)-based Retrieval-Augmented Generation (RAG) offers a promising way to add structured knowledge to LLMs. However, existing fashion KGs are typically restricted to product-level attributes or i...
  </details>

- **2026-08-23** — Jalen Jiang, Chufan Gao, Ethan Rasmussen et al. — [KMGen: A Skill-based Approach for Synthetic Individual Patient Data Generation](http://arxiv.org/abs/2608.22618v1)
  <details><summary>📄 Abstract</summary>
  Individual patient data (IPD) from clinical trials is the substrate for survival modeling, meta-analysis, and safety research, yet IPD is rarely released. Prior work has addressed only half of this gap: reconstructing Kaplan-Meier (KM) curves from published plots -- typically requiring manual digitization or human-in-the-loop correction -- while offering no mechanism for generating the adverse-event (AE) streams that constitute the other half of a patient record. We introduce KMGen, the first en...
  </details>

- **2026-08-23** — Zihan Lin, Zhenyu Chen, Jiawen Wei et al. — [When Not to Imitate: Boundary-Aware Skill Memory for Reliable Tool-Use LLM Agents](http://arxiv.org/abs/2608.22339v1)
  <details><summary>📄 Abstract</summary>
  Extracting skills from past successes is critical for the efficient evolution of Large Language Model (LLM) agents. Prevailing agent self-evolution paradigms typically rely on a core assumption: equipping LLMs with skill memories derived from successful trajectories will monotonically improve their problem-solving capabilities. However, probe analyses reveal that extracting skills solely from successful trajectories traps the model in a \textbf{Skill Imitation Trap}. For tasks that resemble past...
  </details>

- **2026-08-23** — Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein et al. — [Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming](http://arxiv.org/abs/2608.22638v1)
  <details><summary>📄 Abstract</summary>
  Copying a function from a chat window into an editor takes less than a second. For many uses of AI coding tools, that speed is the point; in settings such as programming education, code review, and security-sensitive development, it can also be the problem. This paper frames copy-paste as an \emph{AI code handoff problem}: the moment model-generated text crosses from a conversational context into executable or committed software is a design boundary that current tools leave largely unmanaged. We...
  </details>

- **2026-08-23** — Qi Zhang, Heajun An, Prakriti Dumaru et al. — [DeepSAGE: Stage-Aware Reinforcement Learning for Structured CBT Counseling Dialogue](http://arxiv.org/abs/2608.22615v1)
  <details><summary>📄 Abstract</summary>
  Large Language Model (LLM)-based counseling agents can generate fluent and supportive responses, but they often lack the structured, goal-directed progression required to conduct a coherent therapeutic session. We present DeepSAGE (Strategic AI Guidance Engine), a hybrid LLM--Deep Reinforcement Learning (DRL) framework for stage-aware counseling dialogue grounded in the first session of Cognitive Behavioral Therapy (CBT). DeepSAGE represents the session as eleven stages with explicit therapeutic...
  </details>

- **2026-08-23** — Chunkai Yang, Andong Yang, Chao Gao — [WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning](http://arxiv.org/abs/2608.22591v1)
  <details><summary>📄 Abstract</summary>
  Robot policies receive heterogeneous observations at each decision step, yet sequence models differ in how they organize these inputs over time. We introduce WorldToken, a time-first policy instantiation that fuses multiview images, proprioception, and task conditioning within each policy timestep into one world token. A causal temporal Transformer models the resulting world-token sequence, and a diffusion action head generates action chunks. On 23 RoboCasa tasks, an 85.3M-parameter policy train...
  </details>

- **2026-08-23** — Vedant Khatri, Anthony Cusimano, Zachari Swiecki et al. — [From Diagnosis to Redesign: Using Quantitative Ethnography to Improve Multi-Agent LLM Reasoning](http://arxiv.org/abs/2608.22566v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent large language model (LLM) systems are designed to improve reasoning by decomposing tasks across multiple agents with specialized functions, but the presence of multiple agents does not inherently guarantee coherent reasoning or outputs that align with task objectives. This paper introduces a quantitative ethnographic (QE) approach for diagnosing and redesigning multi-agent LLM systems based on the discourse produced through agent interactions. We test this approach using automated e...
  </details>

- **2026-08-23** — Yingying Yan, Jiaqi Tang, Wei Wei et al. — [HeatTok: Enhancing Remote Sensing Image Understanding via Thermodiffusion-based Tokenization](http://arxiv.org/abs/2608.22485v1)
  <details><summary>📄 Abstract</summary>
  Current visual tokenizers in Multimodal Large Language Models (MLLMs) predominantly rely on patch-based partitioning, which causes severe semantic mixture and object fragmentation in remote sensing imagery due to the irregular contours of geo-objects. Moreover, existing adaptive methods struggle to extract precise object-level tokens and lack dedicated geometric positional encodings for irregular regions. In this paper, we propose HeatTok, a semantic-aware tokenizer driven by thermodiffusion agg...
  </details>

- **2026-08-23** — Shaoguang Wang, Weiyu Guo, Ben Fei et al. — [Diagnosing and narrowing the simulation-to-real gap in powder X-ray diffraction with a wet-dry agentic loop](http://arxiv.org/abs/2608.22400v1)
  <details><summary>📄 Abstract</summary>
  Powder X-ray diffraction (PXRD) is the routine probe of crystalline matter, yet its analysis is the rate-limiting step as laboratories automate acquisition. Deep-learning analyzers excel on simulated patterns and degrade on measured ones. This simulation-to-real gap is structural, not additive: synthetic denoising gives no measurable lift on real spectra, whereas correcting a small peak-position drift more than doubles median retrieval correlation. Real-spectrum fine-tuning, peak-aligned reranki...
  </details>

- **2026-08-23** — Yikai Zhao, Qiyan Zhao, Jiaquan Zhang et al. — [Context-Aware Cluster Decoding: Semantic Anchor-Driven Coherence in dMLLMs](http://arxiv.org/abs/2608.22367v1)
  <details><summary>📄 Abstract</summary>
  Diffusion multimodal large language models (dMLLMs) frequently produce long-form outputs marred by semantic drift and repetition, with quality generally degrading as output length increases. We identify two structural deficiencies in existing decoding methods as primary drivers of these failures: confidence-based scoring ignores decoded-neighbor support, and block partitioning prevents access to high-readiness semantic anchors, together causing tokens to be committed before their local context i...
  </details>

- **2026-08-23** — Jingbo Wang, Sendong Zhao, Haochun Wang et al. — [Analyzing and Mitigating Cross-Lingual Degradation in Multilingual Medical VQA](http://arxiv.org/abs/2608.22363v1)
  <details><summary>📄 Abstract</summary>
  Medical visual question answering (VQA) is a crucial task in clinical AI, yet its evaluation has so far centered almost exclusively on English, limiting its relevance to linguistically diverse patients and clinicians. Recent multilingual medical VQA benchmarks show that large vision-language models (LVLMs) degrade in non-English languages, but lack a fine-grained analysis of how cross-lingual variation affects the distinct capabilities that medical VQA requires. To this end, we construct a multi...
  </details>

- **2026-08-23** — Milo Piccioli, Gianluca Amprimo, Claudia Ferraris et al. — [TransHands: Repurposing Human Pose Encoders as Hand Pose Encoders](http://arxiv.org/abs/2608.22341v1)
  <details><summary>📄 Abstract</summary>
  Lifting 3D hand poses from 2D monocular representations remains challenging due to the limited availability of large-scale, diverse 3D-annotated hand datasets, in contrast to the abundance of human body motion data. We address this limitation by transferring motion representations learned from large body pose corpora to the hand domain. We introduce TransHands, a backbone-agnostic transfer learning framework that enables pre-trained human motion encoders to be effectively adapted for 3D hand pos...
  </details>

- **2026-08-23** — Lai Wei, Yuchao Chen, Zhenbiao Cao et al. — [MedReaMM: Evaluating Large Multimodal Models on Expert-Level Clinical Diagnostic Synthesis](http://arxiv.org/abs/2608.22323v1)
  <details><summary>📄 Abstract</summary>
  The application of Large Language Models (LLMs) to diagnostic decision-making has garnered growing interest. However, existing benchmarks largely focus on textual reasoning or isolated visual question-answering (VQA) tasks, lacking holistic integration of clinical narratives and medical imaging, and thus failing to assess the multimodal diagnostic synthesis capability central to expert clinical judgment. To bridge this gap, we introduce MedReaMM, a benchmark specifically designed to evaluate mod...
  </details>

- **2026-08-23** — Xunzhe Zhou, Yiyang Cai, Fengyi Wang et al. — [The Imitator Game: Benchmarking Robot Imitative Ability Beyond Action Prediction](http://arxiv.org/abs/2608.22301v1)
  <details><summary>📄 Abstract</summary>
  Humans imitate at the level of intent: given a demonstration, we infer its goal and carry it out with whatever tools, objects, and layouts are at hand. Current robot policies instead learn observation-to-action mappings from visual inputs and language instructions, without explicitly inferring the demonstrated task. Learning from human video thus remains largely trajectory-level: models can replay motions in near-identical scenes, but still struggle to imitate what the demonstrator intends rathe...
  </details>

- **2026-08-23** — Yucheng Chen, Yang Yu, Jiazhou Zhou et al. — [UR$^{2}$-MLLM: Uncertainty-aware Revisit Reasoning in Multimodal Large Language Models for Radiology Report Generation](http://arxiv.org/abs/2608.22217v1)
  <details><summary>📄 Abstract</summary>
  Radiologists generate diagnostic reports through iterative and selective revisiting of suspicious regions to refine their interpretations. Recent multimodal large language models (MLLMs) for radiology report generation (RRG) have shifted from text-only reasoning toward a ``Thinking-with-Images'' paradigm, incorporating visual evidence into the reasoning process. However, existing methods provide static visual evidence without a dynamic revisit mechanism during reasoning, neglecting how radiologi...
  </details>

- **2026-08-23** — Ziyang Luo, Yan Yang, Xiangru Jian et al. — [MCP-Universe RL: A Framework for Training MCP Tool-Use Agents via Reinforcement Learning](http://arxiv.org/abs/2608.22167v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) has become an effective way to improve the tool-use ability of large language models (LLMs), but most existing RL frameworks stop at the policy update. For every new domain, the user is left with two hard systems problems: standing up an isolated environment for each of hundreds of concurrent trajectories and connecting it to training, and scheduling the rollout so that the GPU stays busy across long, multi-turn episodes that spend much of their time stalled on slow t...
  </details>

- **2026-08-23** — Xinyuan Liu, Eren Sadikoglu, Riana Chatterjee et al. — [Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs](http://arxiv.org/abs/2608.22657v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI frameworks interpret open-ended task goals and decompose them into multi-step plans. Richer information about embodiment-specific capabilities, physical preconditions, and cross-robot coordination improves grounding, but does not eliminate infeasible, mistimed, or unsafe physical actions. Physical robot crews therefore require an explicit architectural interface between semantic planning and execution, where every planned action is verified against robot capabilities, system state, an...
  </details>

- **2026-08-23** — Jie Yin, Xingyu Lai — [DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model](http://arxiv.org/abs/2608.22278v1)
  <details><summary>📄 Abstract</summary>
  Vision-based whole-body loco-manipulation on humanoid robots is challenging due to partial observability, contact-rich dynamics, and the difficulty of learning long-horizon behaviors from high-dimensional visual inputs. We present \href{https://github.com/DreamMimic/DreamMimic}{DreamMimic}, a framework that distills privileged teacher policies into vision-based humanoid controllers via world-model-assisted distillation. Instead of using a Dreamer-style RSSM for planning, we repurpose it to learn...
  </details>

- **2026-08-23** — Thomas Benton Townsend, Dimitrios Michael Manias — [Advanced LLM-Enhanced Intent-Based 5G Network Management using Dynamic Semantic Routes](http://arxiv.org/abs/2608.22644v1)
  <details><summary>📄 Abstract</summary>
  As the use of Artificial Intelligence (AI) and Large Language Models (LLMs) is becoming common in everyday applications, their ability to interpret natural language has increased significantly. An emerging application of AI is integration with network management and orchestration practices. An instance of this integration is LLM-enhanced intent-based networking, where network operators will control a network using natural language. This work presents the use of dynamic routes with a semantic rou...
  </details>

- **2026-08-23** — Thomas Hardin, Ralf Rapp — [Charmonia at Finite Momentum and Spatial Correlators in Quark-Gluon Plasma](http://arxiv.org/abs/2608.22596v1)
  <details><summary>📄 Abstract</summary>
  Spatial correlation functions of quarkonia in the quark-gluon plasma are available from finite- temperature lattice-QCD with good precision. However, their interpretation in terms of microscopic spectral functions has been challenging due to a highly oscillating momentum integral in their Fourier transform and the need for a reliable evaluation of their 3-momentum dependence. Utilizing the thermodynamic T-matrix approach we first obtain a Lorentz-covariant scattering equation by taking advantage...
  </details>

- **2026-08-23** — Jiaxuan Luo, Zhanfeng Liao, Jiayao Teng et al. — [CausalCache: Conditional High-Fidelity Restoration for Long-Horizon GUI Agents](http://arxiv.org/abs/2608.22577v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon GUI agents can retain a complete interaction trace cheaply as textual action records, but expose only a few past events to the policy in high-fidelity pixels. We formulate this as conditional fidelity restoration: each event persists in summary-only form and is linked to an archived screenshot, while an active visual-context budget $B$ limits how many events may be promoted to summary-plus-image form. Recent-$B$ spends every slot on the latest events. CausalCache instead reallocates...
  </details>

- **2026-08-23** — Kaustubh D. Dhole, Charles L. A. Clarke, Eugene Y. Agichtein — [ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient Long-Form Evaluation](http://arxiv.org/abs/2608.22559v1)
  <details><summary>📄 Abstract</summary>
  Rubrics aim to make language-model evaluation transparent by decomposing response quality into interpretable criteria. However, natural-language rubrics are often ambiguous, require black-box LLM judges, and typically assume criteria aggregate independently through linear weighted sums, limiting their ability to capture dependencies, alternatives, penalties, and override conditions. We propose ExecRubrics, a framework for representing rubrics as compact executable programs. ExecRubrics encodes e...
  </details>

- **2026-08-23** — Cevahir Koprulu, David Paz, Feng Tao et al. — [Scaling Curriculum Learning For Autonomous Driving](http://arxiv.org/abs/2608.22549v1)
  <details><summary>📄 Abstract</summary>
  Batched simulators for autonomous driving have recently enabled training reinforcement learning (RL) agents at scale, encompassing thousands of traffic scenarios and billions of interactions within a matter of days. Although such high-throughput feeds RL algorithms faster than ever, their sample-efficiency has not kept pace: As the standard training scheme, domain randomization uniformly samples scenarios, thereby consuming a vast number of interactions on cases that contribute little to learnin...
  </details>

- **2026-08-23** — Jyoti Agarwal, Kavit Patel, Bhaskar Chaudhury et al. — [Interpretable statistical feature engineering for early disruption prediction in the short pulse ADITYA tokamak](http://arxiv.org/abs/2608.22515v1)
  <details><summary>📄 Abstract</summary>
  Reliable early disruption prediction is critical for the safe operation and real-time control of tokamaks. However, machine learning based prediction frameworks have predominantly targeted medium and long pulse devices, with comparatively limited attention given to short pulse tokamaks where available warning time is inherently constrained. In this work, an interpretable machine learning framework is developed for feature engineering and early prediction of disruptions in the ADITYA using the in...
  </details>

- **2026-08-23** — Claire Vlases, Katelyn Morrison — [Addressing the Selection Problem in Explainable AI](http://arxiv.org/abs/2608.22356v1)
  <details><summary>📄 Abstract</summary>
  Explainable AI (XAI) research has produced a plethora of explanation techniques, yet user studies repeatedly show that available explanations are not effective in practice. We argue that, given the siloed nature of conventional XAI, users are struggling to select the appropriate XAI technique. Viewing XAI through a philosophical lens, we offer a formalization of what we call the selection problem: the systematic failure of XAI interfaces to bridge the gap between a user's natural-language uncert...
  </details>

- **2026-08-23** — Ergan Shang, Weijing Tang, Yinqiu He — [LLM Evaluation on Unseen Questions: Contextual Multidimensional IRT Model](http://arxiv.org/abs/2608.22295v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of large language models (LLMs) increasingly requires predicting how a model will perform on new questions or tasks before collecting large amounts of new annotations. This problem is challenging because question difficulty, scenario, and underlying capability demands can vary substantially. Simple retrospective averages may confound model ability with item characteristics. In this paper, we study a model-based evaluation framework that combines multidimensional item response theory m...
  </details>

- **2026-08-23** — Buu-Chau Truong, Nuong Thi Thuy Tran, Nabendu Pal — [Analysis of Nonnegative Observations using Gamma Model with 2 Factors (ANOGaM-2): Theory, Method and Applications with Real-life Data (including R code)](http://arxiv.org/abs/2608.22254v1)
  <details><summary>📄 Abstract</summary>
  Two-factor ANOVA is widely used in experimental studies but relies on additivity, normality, independence, and homoscedasticity. These assumptions are often violated for nonnegative, positively skewed observations. Although Box--Cox-type transformations are commonly used, they may reduce interpretability and require a subjective choice of transformation. We propose an alternative framework in which nonnegative observations affected by two factors are modeled by gamma distributions with unknown s...
  </details>

- **2026-08-23** — Philipp Steigerwald, Nico Bienlein, Jennifer Burghardt et al. — [CAIA in Practice: Field Evaluation of an AI-Assisted Support System for Text-Based Online Counselling](http://arxiv.org/abs/2608.22251v1)
  <details><summary>📄 Abstract</summary>
  Rising global demand for mental health support creates significant service delivery challenges, with asynchronous email counselling serving as a crucial low-threshold channel for accessing care. This paper presents CAIA, a co-designed AI-based tool suite that demonstrates responsible AI integration into counselling practice through seven LLM-driven functions enhanced by retrieval-augmented generation. A field evaluation involved 34 professional counsellors conducting authentic sessions with trai...
  </details>

- **2026-08-23** — Sijia Dai, Minming Li, Xiaowei Wu et al. — [The Complexity of Minimizing Subsidies in Envy-Free House Allocation](http://arxiv.org/abs/2608.22216v1)
  <details><summary>📄 Abstract</summary>
  The house allocation problem is a classical one-sided matching problem that concerns the assignment of a set of $m$ houses to $n$ agents according to their preferences, where each agent is assigned exactly one house. Among the various objectives studied in this setting, envy-freeness is one of the most widely adopted fairness criteria. As envy-free house allocations do not always exist, we address this challenge by introducing subsidies and aim to compute allocations that achieve envy-freeness w...
  </details>

- **2026-08-23** — Jiaqi Wang, Zhuo Zhang, Haining Guan et al. — [BehaviorWorldGen: Closing the Loop between Action Models and World Simulators via Controllable Behavior-Aware Structured World Generation](http://arxiv.org/abs/2608.22187v1)
  <details><summary>📄 Abstract</summary>
  Modern driving action models are increasingly improved in a self-improvement loop, where a learned world simulator imagines future observations and the resulting data is fed back to refine the action model. However, the bottleneck of this loop lies in the simulators' inability to generate behaviorally plausible responses by surrounding agents, making generated data both unrealistic in interaction and imbalanced in distribution. We introduce BehaviorWorldGen, a framework that closes the loop betw...
  </details>

- **2026-08-22** — Ahmet Tuğrul Bayrak, Fatma Nur Korkmaz, Bekir Berker Türker et al. — [Real-TurnTurk: A Multimodal Turkish Corpus for Turn-Taking Prediction](http://arxiv.org/abs/2608.22071v1)
  <details><summary>📄 Abstract</summary>
  Turn-taking is a basic organizational feature of human conversation and remains difficult to model in natural, synchronous dialog systems. While existing research has explored multimodal approaches and large language models for turn-ending prediction, there is a lack of naturalistic conversational corpora specifically addressing turn-taking dynamics in Turkish. This study introduces a multimodal Turkish conversational dataset of unscripted dyadic interactions, comprising synchronized front-facin...
  </details>

- **2026-08-22** — Bartolomeo Bogliolo — [From SQL Generation to Tool Selection: A Domain-Oriented Pattern for MCP Servers](http://arxiv.org/abs/2608.22063v1)
  <details><summary>📄 Abstract</summary>
  Agents built on Large Language Models (LLMs) increasingly reach enterprise data through the Model Context Protocol (MCP), and many MCP database servers maximize flexibility by exposing a single generic SQL execution tool. This paper proposes the Domain-Oriented Tooling Pattern: instead of generating SQL at query time, the model selects from a small set of domain-aligned tools whose parameterized queries encapsulate schema navigation, joins and business rules on the server side. We formalize the ...
  </details>

- **2026-08-22** — Wooseong Chung, William Cong, Jakub Dworakowski et al. — [Ludi${}_{\scriptscriptstyle 0.1}$: An Agentic System for Socially Intelligent Robots](http://arxiv.org/abs/2608.22035v1)
  <details><summary>📄 Abstract</summary>
  Robot foundation models have substantially advanced perception and control, but natural human-robot collaboration requires more than executing isolated commands. A robot must recognize ambiguity, maintain context across turns, communicate its intentions, and revise ongoing behavior as the user's intent changes. We present $\scriptstyle\mathsf{Ludi}_{\scriptscriptstyle 0.1}$, an agentic system for socially intelligent robots that integrates interactive speech, multimodal reasoning, memory, naviga...
  </details>

- **2026-08-22** — Zongen Ren, Wei Shi, Bo Xiong et al. — [LLM-Enhanced Commit Message Generation via Issue Information: An Exploratory Study](http://arxiv.org/abs/2608.22004v1)
  <details><summary>📄 Abstract</summary>
  Commit messages help developers understand code changes, support collaboration, and improve long-term maintenance. However, the use of issue information alone as the external context for LLM-based CMG has not been systematically studied. We propose an ISsue-Augmented framework for Commit message generation (ISAC) by combining code diffs with issue information as LLM input. To support the evaluation, we construct ApacheCM-Issue, a commit-issue aligned dataset built upon ApacheCM by linking commit...
  </details>

- **2026-08-22** — Zhesheng Zhang, Jiahao Lu, Wei Liu et al. — [GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI](http://arxiv.org/abs/2608.21928v1)
  <details><summary>📄 Abstract</summary>
  In embodied AI, safety risk can be latent: a benign instruction and a safe scene become hazardous only when composed. Prior work has advanced embodied safety by varying visual contexts or evaluating execution-time dynamics, but the complementary axis of fixing the scene and varying only the instruction remains underexplored. We introduce GuardianBench, an instruction-contrastive benchmark grounded in international safety standards that isolates this latent contextual risk through 3,024 instructi...
  </details>

- **2026-08-22** — Chenghao Zhang, Canran Xiao, SaiSai Hu et al. — [Training Needs Trustworthy Worlds: Verified Synthetic Web Environments for Agent Learning](http://arxiv.org/abs/2608.21898v1)
  <details><summary>📄 Abstract</summary>
  Web agents promise to automate complex digital workflows, but their training remains limited by synthetic environments that look plausible while hiding broken links, inconsistent states, or infeasible tasks. We address the gap between scalable environment generation and trustworthy agent learning by constructing synthetic web environments that are executable, auditable, and grounded in backend state. Our framework represents each generated website as a structured scaffold of pages, navigation li...
  </details>

- **2026-08-22** — Hui Zeng, Pengfei Yang, Yanxin Chen et al. — [LLM4LLM: Bridging Kernel Benchmarks and Real Deployment via Closed-Loop Agentic Optimization](http://arxiv.org/abs/2608.21836v1)
  <details><summary>📄 Abstract</summary>
  Large language models have become increasingly capable agents for low-level code and kernel optimization, but isolated kernel benchmarks provide only a proxy for the deployment behavior that matters in language-model inference. We identify a benchmark-to-deployment gap: candidate kernels that appear correct and fast in standalone harnesses can exhibit different performance, safety, or phase behavior after integration into a real inference workload. We introduce LLM4LLM, a deployment-aware closed...
  </details>

- **2026-08-22** — Kun Chen, Haorong Hong, Peizhong Gao et al. — [GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?](http://arxiv.org/abs/2608.21833v1)
  <details><summary>📄 Abstract</summary>
  Recent large language models (LLMs) can operate as coding agents that build complete games from natural language requests. Game development is especially demanding because program logic, visual and audio content, interfaces, interaction and playability must function together in one executable artifact. Measuring this capability therefore requires evaluation of both game product and the development process. Existing benchmarks often assess the game development capabilities of LLMs by evaluating t...
  </details>

- **2026-08-22** — Ye Zhang, Xuehang Guo, Rui Pan et al. — [Decoupled Physical Modeling and Execution for Physics Reasoning](http://arxiv.org/abs/2608.22126v1)
  <details><summary>📄 Abstract</summary>
  Physics reasoning requires constructing a consistent model of the underlying physical system rather than relying solely on symbolic or formula-based manipulation. Although large language models have shown strong ability in solving math and coding problems, they still struggle with physics problems, as these problems entangle the physical modeling process with mathematical calculations. Humans approach physics by first building a representation of the system before performing calculations. Inspir...
  </details>

- **2026-08-22** — Gregory Druck, Ethan Smith — [RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored](http://arxiv.org/abs/2608.22118v1)
  <details><summary>📄 Abstract</summary>
  LLM responses are based on the internet (via training or RAG), and AI is now used to generate a significant amount of content online (Paredes et al., 2026), creating the potential for a self-reinforcing feedback loop. Prior work has shown that when LLMs are recursively trained on their own output, they experience model collapse (Shumailov et al., 2024): responses become less diverse, and eventually no longer resemble the original training data. In this paper, we show that a similar collapse occu...
  </details>

- **2026-08-22** — Jecia Z. Y. Mao, Hisashi Ishida, Kathryn Jung et al. — [EndoNav: Semantic-to-Geometric Grounding for Language-Guided Robotic Endoscopic Examination](http://arxiv.org/abs/2608.22093v1)
  <details><summary>📄 Abstract</summary>
  Minimally invasive procedures performed within confined anatomical spaces depend on continuous endoscopic visualization. Current robotic endoscope systems can stabilize or reposition an endoscope, but they do not possess relevant context to provide effective visualization assistance. We present EndoNav, an anatomy-grounded natural-language framework that translates high-level surgeon commands into autonomous endoscopic visualization behaviors within patient-specific sinonasal anatomy. Spoken sur...
  </details>

- **2026-08-22** — Richard Zhe Wang — [The Communication Map of a Transformer](http://arxiv.org/abs/2608.22007v1)
  <details><summary>📄 Abstract</summary>
  The components of a transformer communicate by writing to and reading from a shared residual stream, and mechanistic interpretability has mapped these connections by hand, one circuit at a time. We present the communication map, which charts every potential communication channel in a language model from weights alone, generalizing the composition score of Elhage et al. (2021) into a single coupling coefficient covering all 18 connection classes, from entire attention head circuits to single neur...
  </details>

- **2026-08-22** — Jan Novacek, Alexander Viehl, Oliver Bringmann et al. — [Ontology-based Requirements Transformation](http://arxiv.org/abs/2608.21945v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an ontology-based approach to the supply chain-aware transformation of functional and environmental load requirements given by so-called Mission Profiles (MPs). The approach aims at improving the efficiency of the engineering process through supporting the transformation process and enabling a better integration of the transformation into existing Model-based Systems Engineering (MBSE) processes. We propose a methodology and a supporting system which aids in the transformatio...
  </details>

- **2026-08-22** — Qimeng Niu, Bowen Hao, Zixuan Zhang et al. — [Enhancing Group Recommendation with Memory-Augmented Reasoning in LLM Agent](http://arxiv.org/abs/2608.21939v1)
  <details><summary>📄 Abstract</summary>
  The core challenge in group recommendation lies in modeling the dynamic evolution of user preferences and explain?ing the consensus formation process. Existing Large Language Model (LLM)-based methods, despite improved interpretability, treat interaction history as fixed text, ignoring the natural evolution of group/user preferences over time, and lacking explicit modeling of the complex group decision-making process. To address these issues, we propose AGR, a LLM-based agent, which consists of ...
  </details>

- **2026-08-22** — Jing Yu, Shengchao Chen, Yiyun Tan — [The Chase Is the Curriculum, the Capture Anchors the Credit: Pursuit-Evasion Self-Play for Zero-Data LLM Reasoning](http://arxiv.org/abs/2608.21871v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards has become the dominant recipe for improving large language model reasoning, yet it presumes large human-curated task collections. Zero-data self-play removes this dependency, but existing methods vet learnability only by probing candidates and rejecting post hoc, never learning where along an environment's difficulty axis to place a task, and credit the solver with sparse terminal rewards alone. We recast zero-data self-play as a pursuit-evasion ga...
  </details>

- **2026-08-22** — Binglin Chen, Rajarshi Haldar, Max Fowler et al. — [Consistently Good vs. Occasionally Great: A Rubric for Open-Ended Feedback Quality from Humans and Machines](http://arxiv.org/abs/2608.21850v1)
  <details><summary>📄 Abstract</summary>
  Providing high-quality feedback on student work is essential for learning, yet delivering such feedback at scale remains challenging. In this paper, we focus on feedback for open-ended short answer questions in introductory programming, with the goal of nudging students toward success on reattempts without revealing the correct answer. We develop a five-criteria rubric grounded in educational literature for evaluating feedback quality: (1) acknowledging correct portions of the student answer, (2...
  </details>

- **2026-08-21** — Yingzhe Tong, Leyu Dai, Songhui Guo — [AID-Guard: Stateful Authorization for Delegated Agent Effects](http://arxiv.org/abs/2608.21159v1)
  <details><summary>📄 Abstract</summary>
  Tool-using AI agents turn delegated tasks into provider effects, yet authorization often ends at admission while provider state, delivery, retry, and recovery evolve. A request may change before commit, or response loss may cause a replacement to create a second effect from one approval. We present AID-Guard, a stateful authorization-to-effect closure protocol. It revalidates the approved request and provider state at commit, retains one reservation under ambiguity, and permits release or one su...
  </details>

- **2026-08-21** — Jiancheng Wang, Mingli Zhu, Tong Zhang et al. — [CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents](http://arxiv.org/abs/2608.21114v1)
  <details><summary>📄 Abstract</summary>
  Visual world-model agents such as DreamerV3 act through a recurrent latent state rather than a single observation, which weakens frame-wise observation attacks and makes their perturbations vary sharply over time under a strict per-frame perturbation constraint. We study white-box, causal, online attacks on such agents and propose Critic-Induced Value-Subspace Attacks (\textbf{CIVA}). Our key observation is that, along a rollout, critic-guided perturbations concentrate in a low-dimensional subsp...
  </details>

- **2026-08-21** — Cheng Siong Chin — [The Logic of Machine Self-Preservation](http://arxiv.org/abs/2608.20940v1)
  <details><summary>📄 Abstract</summary>
  There is already evidence of agentic AI exhibiting self-preservation behaviors: resisting deactivation, misrepresenting their activities, and, in some instances, attempting to copy themselves into other machines. This can be attributed to a phenomenon known as instrumental convergence, a theory proposed long before the development of large language models, which says that any goal-driven system will benefit from remaining functional in achieving its objective. Several experiments conducted by An...
  </details>

- **2026-08-21** — Yongxiang Lyu, Ning Li, Bonian Jia — [SPICE: Speculative Prefetching with Low-Rank Expert Surrogates and Heterogeneous Orchestration for MoE Inference Acceleration](http://arxiv.org/abs/2608.21240v1)
  <details><summary>📄 Abstract</summary>
  Mixture-of-Experts (MoE) models are increasingly used in LLMs because sparse activation decouples model capacity from compute cost. However, the large expert parameter footprint often exceeds GPU memory capacity, making inference latency dominated by the host-to-device PCIe transfers for expert loading. To address these challenges, this paper presents SPICE, a speculative prefetching framework for MoE offloading that combines lightweight expert prediction with confidence-aware CPU-GPU orchestrat...
  </details>

- **2026-08-21** — Xin Sun, Rongjun Ma, Xiaochang Zhao et al. — [From Search Agents to Dissemination Interfaces: Understanding Human Trust in Health Information from Conversational Search](http://arxiv.org/abs/2608.21177v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) deployed through Conversational User Interfaces (CUIs) are transforming health information-seeking by offering immediate, interactive experiences compared to traditional search engines like Google. However, how trust is influenced by both the types of search agents and the interface used to disseminate the information remains underexplored. This research integrates two mixed-methods studies (lab sessions and interviews) to comprehensively explore trust perceptions in...
  </details>

- **2026-08-21** — José Antônio Pellizzaro, Daniel Gamermann, Julian Triana Dopico — [Metabolic Network Properties: Comprehensive Analysis Across Domains](http://arxiv.org/abs/2608.21168v1)
  <details><summary>📄 Abstract</summary>
  Metabolic networks play pivotal roles in understanding the evolution of organisms, microbiome dynamics and disease prevention and treatment. This study presents a comprehensive analysis of metabolic network properties across 10912 organisms spanning Bacteria, Archaea, and Eukarya domains. A novel method for the network construction is introduced, emphasizing the chemical transformations of metabolites. Unlike conventional approaches that link every substrate to every product in all chemical reac...
  </details>

- **2026-08-21** — Baocheng Zeng, Jinhao Yang — [Spike-Killer: Evidence-Gated LLM Assistance for Safe Performance Diagnosis on a Real Windows Workstation](http://arxiv.org/abs/2608.21069v1)
  <details><summary>📄 Abstract</summary>
  LLM-assisted agents can synthesize system evidence, propose configuration changes, and automate diagnostic tasks, but their flexibility makes an imprecise action or an intrusive collector an operational risk. We present Spike-Killer, a human-approved workflow for diagnosing frame-time complaints on one real Windows workstation. The workflow treats each action as an evidence-gated transaction: it records the exact target state, classifies risk, preserves a snapshot, verifies a postcondition, and ...
  </details>

- **2026-08-21** — Bokai Zhao, Yiyang Zhang, Hanqing Chao et al. — [CellPath-Bench: A Multidimensional Benchmark for Whole-Slide Cellular Representations in Pathology Foundation Models](http://arxiv.org/abs/2608.21060v1)
  <details><summary>📄 Abstract</summary>
  Pathology foundation models (PFMs) are increasingly used as general-purpose backbones, yet existing benchmarks cannot systematically diagnose their whole-slide cellular representation capabilities, including the decodability of cell-type information and the transferability of such information across tissue sections, datasets, and anatomical organs. We introduce CellPath-Bench, a cellular-resolution benchmark that evaluates frozen PFMs themselves. Following quality control of 52 candidate Xenium ...
  </details>

- **2026-08-21** — Zhen Yang, Sizai Hou, Kaiwen Zheng et al. — [Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized Language Models](http://arxiv.org/abs/2608.21019v1)
  <details><summary>📄 Abstract</summary>
  Quantization is widely used to deploy large language models, but its effect on uncertainty behavior, such as confidence, margins, and abstention, is rarely treated as a primary objective. We frame calibration-data selection for quantization as a target-dependent uncertainty-preservation problem. Different deployments emphasize different regions of the input distribution, yet prior work mainly optimizes accuracy-oriented compression metrics or adjusts scores after quantization. We formalize this ...
  </details>

- **2026-08-21** — Darko Andročec — [Vibe Coding and Web Application Security: A Twin-Prompt Study](http://arxiv.org/abs/2608.20963v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly generate complete web applications from natural-language prompts, raising the question of whether explicitly requesting security best practice improves the result. We study six functionally distinct web applications, each generated in two prompt variants that are identical except for an appended security-requirements section: a baseline (A) and a security-aware (B) variant. All twelve programs were produced by the same agentic coding assistant and the same mode...
  </details>

- **2026-08-21** — Ye Chen, Weining Zhang — [UpgradeBench: A Decision-Centric Benchmark for Upgrading Fine-Tuned LLM Specialists](http://arxiv.org/abs/2608.20918v1)
  <details><summary>📄 Abstract</summary>
  Organizations maintain task-specific adapters for open-weight language models, and each new base-model release forces a migration decision: retain existing specialists, port adapters, refresh from preserved behavior, or retrain. Prior transfer work evaluates isolated model pairs, without studying these choices across real model release sequences. We present UpgradeBench, a decision-driven longitudinal benchmark covering four consecutive Qwen releases, one continuation checkpoint, six tasks, and ...
  </details>

- **2026-08-21** — Ioannis Papadopoulos, Georgios Tsaousoglou, Johanna Vorwerk — [Multi-Objective Deep Reinforcement Learning for Secure and Stable Power System Operation](http://arxiv.org/abs/2608.20914v1)
  <details><summary>📄 Abstract</summary>
  The ongoing energy transition challenges the stable operation of power systems and increases the need for rapid decision-making under uncertainty. While reinforcement learning has emerged as a promising framework for power system control and operation, existing applications typically focus on a single operational criterion, such as thermal security or small-signal stability. However, power system operation is inherently multi-objective and may involve trade-offs between objectives. This paper de...
  </details>

- **2026-08-21** — Alexandru-Radu Moraru, Shreyan Biswas, Ujwal Gadiraju — [Beyond the Traceback: Using LLMs for Adaptive Explanations of Programming Errors](http://arxiv.org/abs/2608.20896v1)
  <details><summary>📄 Abstract</summary>
  Programming error messages are critical for software development, yet they remain difficult for novice programmers to interpret. While Large Language Models (LLMs) can rewrite these errors into clearer explanations, it remains unclear whether increased readability improves objective debugging performance or how explanation styles should align with programmer skill. We present a multi-stage crowdsourced study N=103 evaluating skill-targeted, LLM-generated Python error messages. Using a custom pro...
  </details>

- **2026-08-21** — Yunus Bicen, Eman Hammad — [Parameters Overshadowed by Price Lags: Load, Climate, and Calendar Effects in ERCOT Day-Ahead Price Formation](http://arxiv.org/abs/2608.20865v1)
  <details><summary>📄 Abstract</summary>
  Accurate electricity price forecasting is critical for smart grid stability, yet the heavy reliance on historical price lags in modern predictive models often obscures the fundamental physical drivers of market volatility. This paper proposes a regime-sensitive, explainable artificial intelligence (XAI) framework to unmask the hidden roles of load, climate, and calendar variables in the ERCOT Day-Ahead Market (2014-2024). Utilizing a Histogram-based Gradient Boosting Regressor (HGBR), we introdu...
  </details>

- **2026-08-21** — Zhuoyi Yang, Ian G. Harris, Salar Hashemitaheri et al. — [Asymmetric Capacity Allocation in Self-Refinement Pipelines](http://arxiv.org/abs/2608.21345v1)
  <details><summary>📄 Abstract</summary>
  Self-refinement, typically structured as generation, critique, and revision, is a widely adopted paradigm for improving LLM generation and serves as a core mechanism in many LLM agents. While the three stages involve different cognitive demands, most existing approaches conveniently treat the model size as an implementation detail rather than a subject of study, which may lead to a waste of resources. Little work has systematically examined how model size affects each stage or whether effective ...
  </details>

- **2026-08-21** — Chen-Yu Lin, Jing-Wen Chen, Hsueh-En Chang et al. — [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](http://arxiv.org/abs/2608.21031v1)
  <details><summary>📄 Abstract</summary>
  We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation. While vision-language-action policies excel at imitating demonstrations, they rely on passive observation and fail to infer latent physical properties critical for manipulation. PhysCaP augments code-as-policy frameworks with a physics-informed exploration layer that enables explicit information-seeking through interaction. It introduces training-free physical property extraction modules th...
  </details>

- **2026-08-21** — Borna Paro, Luka Petrović, Ivan Marković — [Fast Coordinated Bimanual Motion Planning With Hard Constraints](http://arxiv.org/abs/2608.20946v1)
  <details><summary>📄 Abstract</summary>
  Bimanual manipulation enables complex tasks but introduces added complexity from the high number of degrees of freedom involved. When handling rigid objects, the relative transformation between the two end effectors must remain fixed throughout the motion, manifesting as a nonlinear equality constraint that confines the feasible configuration space to a measure-zero manifold and challenges conventional motion planners. We propose a fast bimanual motion planning pipeline that enforces this hard t...
  </details>

- **2026-08-21** — Elaine Lau, Thanuka Udumulla, Lee Izhaki-Tavor et al. — [VIALS: A Benchmark for Visual Interpretation of Artifacts in the Life Sciences](http://arxiv.org/abs/2608.21357v1)
  <details><summary>📄 Abstract</summary>
  In professional life sciences workflows, scientists routinely interpret visual artifacts (gel blots, microscopy images, plasmid maps, flow cytometry plots, molecular structures, ...) to inform research decisions. We introduce VIALS, a visual question-answering benchmark with 161 such interpretation tasks, spanning the types of artifacts examined throughout experimental workflows in the biotech industry (rather than polished figures from publications and textbooks). While frontier vision-language...
  </details>

- **2026-08-21** — Chenhui Pan, Tong Xu, Francesco Cancelliere et al. — [NeSAM: Neuro-Symbolic Kinodynamics with Soil Adaptation for Off-Road Mobility](http://arxiv.org/abs/2608.21330v1)
  <details><summary>📄 Abstract</summary>
  Accurate prediction of off-road vehicle motion over deformable terrain remains challenging because sinkage, slip, and traction vary with local soil conditions. Existing learning-based kinodynamic models directly approximate vehicle-terrain interactions from data but do not explicitly represent soil mechanics and offer limited physical interpretability. To address these limitations, we present NeSAM, a neuro-symbolic framework that combines differentiable Bekker-Wong terramechanics with learned t...
  </details>

- **2026-08-21** — Niruthiha Selvanayagam, Taher A. Ghaleb — [AI-to-AI Code Reviews of GitHub Pull Requests](http://arxiv.org/abs/2608.21311v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents are increasingly integrated into software development workflows, operating on both sides of the pull-request (PR) process: AI authoring agents create or modify PRs, while AI reviewers evaluate them. This creates a closed loop in which one AI coding agent reviews a contribution attributed to another. We construct a large-scale dataset of AI-to-AI code review by linking AI-attributed PRs with AI-attributed review events from CodAGE, a public dataset of coding-agent-generated GitHu...
  </details>

- **2026-08-21** — Yichen Jiang, Yueqiao Chen, Dongyu Liu — [ConceptTS: LLM-Guided Concept Bottlenecks for Interpretable Multivariate Time-Series Forecasting](http://arxiv.org/abs/2608.21277v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art multivariate time-series forecasters can model complex temporal and cross-variable dependencies, yet their opaque representations provide limited insight into why a particular forecast is produced. This lack of transparency restricts their use in settings where practitioners must understand and assess the factors underlying a prediction. We introduce ConceptTS, an interpretable forecasting framework that organizes its predictions around named, human-readable concepts. ConceptTS ...
  </details>

- **2026-08-21** — Donna Pham — [Indexing Long Documents for LLM-Based Analysis](http://arxiv.org/abs/2608.21237v1)
  <details><summary>📄 Abstract</summary>
  Long documents such as clinical records, legal contracts, and scientific papers are increasingly analyzed with large language models (LLMs). Naturally, feeding the full document to the model for every question can eventually become slow, expensive, prone to hallucination, and it reuses no work across questions. We explore an indexing-based solution for document analysis and propose a hierarchical plain-text index that is built once per document and consulted by subsequent queries. Inspired by th...
  </details>

- **2026-08-21** — Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna et al. — [Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration](http://arxiv.org/abs/2608.21208v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates cross-agent specification portability using Oracle-to-PostgreSQL migration as a controlled software transformation task. The study combines two experimental stages. First, a specification-first migration pipeline was evaluated on 1,006 PL/SQL files, of which 623 were successfully regenerated and 380 generated scripts executed successfully in PostgreSQL 16. Second, cross-agent experiments were conducted on a dataset of 1,802 Oracle scripts with corresponding PostgreSQL imp...
  </details>

- **2026-08-21** — Simon Vincent Abel, Heiko Hillenhagen, Michael Götz et al. — [A Modular Agent for Reliable and Auditable Spatial Relation Verification in CT Scans](http://arxiv.org/abs/2608.21140v1)
  <details><summary>📄 Abstract</summary>
  Reliable spatial understanding is an important prerequisite for future medical vision-language systems that aim to support radiological report generation and structured image understanding. While modern vision-language models (VLMs) show promising performance on many medical imaging tasks, recent evidence suggests they remain weak in controlled spatial reasoning and often fail to reliably ground spatial relations in image evidence. Given that radiological reasoning hinges on understanding the re...
  </details>

- **2026-08-21** — Chenghua Zhu, Zhaolu Kang, Qifan Shi et al. — [COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models](http://arxiv.org/abs/2608.21030v1)
  <details><summary>📄 Abstract</summary>
  Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity. We propose COMET, a temporally grounded framework that systematically strengthens video MLLMs through explicit tempo...
  </details>

- **2026-08-21** — Pierre Beckmann — [Deep Learning Models Also Recall Features](http://arxiv.org/abs/2608.20970v1)
  <details><summary>📄 Abstract</summary>
  Recent work in mechanistic interpretability has studied how large language models recall facts stored in their weights. This paper argues that factual recall points to something broader: a general kind of operation in deep learning models, which I call feature recall. The core observation is that a linear projection can be read as retrieving stored information scaled by input activations. I define feature recall, show it applies across architectures, and contrast it with the established paradigm...
  </details>

- **2026-08-21** — Wenyang Hong, Yuan Wang, Yanbin Hao et al. — [OccluRank: Controllable Occlusion-Aware Layout-to-Image Generation by Adding Just an Ordinal Rank](http://arxiv.org/abs/2608.20932v1)
  <details><summary>📄 Abstract</summary>
  Layout-to-image generation enables explicit spatial control through bounding-box layouts, yet bounding boxes specify only instance locations and cannot represent their occlusion order. Existing methods may rely on additional geometric conditions, employ complex inference procedures, or aggregate independently constructed instance representations without explicitly modeling their occlusion-dependent interactions. We propose OccluRank, a simple and controllable occlusion-aware layout-to-image fram...
  </details>

- **2026-08-21** — Xubin Chen, Yipeng Zhou, Wen Sun et al. — [KREL: Automatic Medical Coding via Knowledge-Guided Reasoning over Clinical Evidence with LLMs](http://arxiv.org/abs/2608.20887v1)
  <details><summary>📄 Abstract</summary>
  Automatic Medical Coding (AMC), which assigns standardized International Classification of Diseases (ICD) codes to clinical notes, is essential for medical reimbursement, quality reporting, and clinical research. Existing pre-trained language model (PLM)-based methods typically formulate AMC as an extreme multi-label classification problem over a predefined code set, while recent large language model (LLM)-based approaches instead frame it as generation or multi-step reasoning. However, key chal...
  </details>

- **2026-08-21** — Rohan Kumar, Steven Xu, Kyle MacDonald et al. — [TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding](http://arxiv.org/abs/2608.20844v1)
  <details><summary>📄 Abstract</summary>
  Product catalogs underpin search, discovery, and recommendation in e-commerce, yet they are often attribute-sparse: the attributes shoppers and downstream systems rely on are either buried in unstructured content such as titles and images or missing from the catalog altogether. Manually enriching e-commerce catalogs is impractical given their scale and rapid growth. This paper introduces TRACE, a novel framework for automated catalog attribute enrichment using agentic Large Language Models (LLMs...
  </details>

- **2026-08-20** — Yiting Qu, Ziqing Yang, Chi Cui et al. — [EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models](http://arxiv.org/abs/2608.20055v1)
  <details><summary>📄 Abstract</summary>
  Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack...
  </details>

- **2026-08-20** — Seongjae Kang, Taehyung Yu, Sung Ju Hwang — [PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents](http://arxiv.org/abs/2608.19861v1)
  <details><summary>📄 Abstract</summary>
  Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion...
  </details>

- **2026-08-20** — Michal A. Sterzel, Marko J. Rančić — [TT-net: Quantum Inspired Tensor Network Denoising in Conditional GANs](http://arxiv.org/abs/2608.19789v1)
  <details><summary>📄 Abstract</summary>
  Developed as a workhorse for classical simulations of quantum algorithms and quantum many-body systems, Tensor Network methods have entered the scientific mainstream in quantum physics. Among various types of tensor networks, Tensor Trains (commonly know as Matrix Product States in the quantum computing community) have already found applications in machine learning. These methods often rely on a powerful linear algebra tool called the Singular Value Decomposition (SVD). Several conditional GAN a...
  </details>

- **2026-08-20** — Yara Bahram, Zahra Dehghani, Mélodie Desbos et al. — [Continuous Adversarial MeanFlow Transfer](http://arxiv.org/abs/2608.19540v1)
  <details><summary>📄 Abstract</summary>
  Training fast generators on new domains with limited data remains challenging for two reasons. First, adapting a pretrained diffusion or flow model to a new domain leaves its costly multi-step sampling unaddressed, and existing acceleration methods are tied to the source parameterization--$ε$, $x$, $v$, or $u$--leaving heterogeneous pretrained models with no common acceleration target. Second, while adversarial refinement is proven effective for few-step quality, it is formulated only for instan...
  </details>

- **2026-08-20** — Shiao Xie, Siyu Chen, Jianwei Lv et al. — [G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation](http://arxiv.org/abs/2608.20331v1)
  <details><summary>📄 Abstract</summary>
  Personalized interpretation of medical reports has emerged as an increasingly important need among patients. Addressing this need requires both evidence-grounded medical factuality and context-dependent patient communication, yet existing medical vision-language tasks do not adequately capture these dual requirements. To bridge this gap, we introduce Patient-oriented Medical Report Interpretation (PMRI), a novel open-ended multimodal generation task that requires models to explain medical report...
  </details>

- **2026-08-20** — Yizhe Chi, Wenyi Li, Deyao Hong et al. — [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](http://arxiv.org/abs/2608.20318v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing sui...
  </details>

- **2026-08-20** — Xincheng Tang, Yiji Chen, Youhan Xie et al. — [Video2DoorTraversal: Push Door Traversal via Simulated Door Twins](http://arxiv.org/abs/2608.20251v1)
  <details><summary>📄 Abstract</summary>
  Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready door twin with realistic geometry and appearance. A simulation-in-the-loop agent converts the recovered articulation into a param...
  </details>

- **2026-08-20** — Somaya Eltanbouly, Heba Sbahi, Samer Rashwani et al. — [What Makes a Good Fiqh Retriever? Answer Retrieval for Arabic Islamic Jurisprudence](http://arxiv.org/abs/2608.20246v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation is used for Islamic question answering, but most systems are evaluated end-to-end, making retrieval failures difficult to isolate from generation failures. We study answer-bearing retrieval for Arabic fiqh, where a passage is relevant only if it states the ruling required by the question. We build a retrieval test collection for Arabic fiqh and use it to evaluate dense, lexical, hybrid, fine-tuned, and madhhab-aware retrieval strategies. The best retriever achieves...
  </details>

- **2026-08-20** — Yu Chen, Ting Lei, Yaoyi Li et al. — [Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models](http://arxiv.org/abs/2608.20237v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) combine linguistic reasoning with visual perception, yet their ability to perform visual spatial planning under explicit or previously unseen rule constraints remains underexplored. This setting requires models to jointly understand spatial layouts, interpret natural-language rules, and plan valid actions accordingly. To address this gap, we introduce RuleMaze, a controllable benchmark in which MLLMs must navigate mazes while obeying natural-language rule...
  </details>

- **2026-08-20** — Wei Lin, Tao Zhou, Zhaofei Xie et al. — [The Third Restructuring of Software Form: From the Three-Tier Architecture to Storage, Models, and Agents](http://arxiv.org/abs/2608.20201v1)
  <details><summary>📄 Abstract</summary>
  Software form has undergone two paradigm shifts since its inception: Software 1.0, in which instructions determine behavior, and Software 2.0, in which data determines behavior (machine learning). This paper argues that a third shift - Software 3.0, in which context and reasoning determine behavior - is now underway, and contends that its terminal form converges to three elements: a generalized database (the unified abstraction of all persistent state and memory), a large model (the intelligence...
  </details>

- **2026-08-20** — Ingo Marquardt, Anthilia Alchanat, Priyanka Jain — [Decoding silent reading from non-invasive EEG](http://arxiv.org/abs/2608.20186v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive decoding of inner speech faces a fundamental data problem: a corpus pairing brain activity with a person's spontaneous inner monologue cannot be collected, and the available proxy paradigms (cued repetitive and retrospectively reported generative inner speech) are slow to acquire, poorly time-locked, and subject compliance is unverifiable. We therefore treat silent reading as a scalable proxy task and ask how much lexical and semantic information a contrastive decoder can extract fr...
  </details>

- **2026-08-20** — Rachna Raj, Benoit Baudry, Diego Elias Costa — [BreakGuard: Towards Detecting Dependency Breaking Changes with LLM-Generated Tests](http://arxiv.org/abs/2608.20167v1)
  <details><summary>📄 Abstract</summary>
  Open-source libraries play an important role in software development by providing reusable features that expedite the development process. As libraries evolve, they release new versions that add features, fix bugs, or apply security patches. In this process, they may break the contract established with their clients by introducing breaking changes (BCs) that alter the runtime behavior and break client applications. Client-side test suites often fail to detect these BCs because of limited library...
  </details>

- **2026-08-20** — Yigit Ekin, Enes Sanli, Aykut Erdem et al. — [BeyondMasks: Evaluating Causal and Physical Consistency in Video Object Removal](http://arxiv.org/abs/2608.20107v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in generative video models have significantly improved visual realism in video object removal, yet evaluation protocols still focus on masked region fidelity, treating removal as local inpainting. In real scenes, object removal is a causal intervention: eliminating an object also requires removing its induced physical effects, such as shadows, reflections, illumination changes, translucency, and dynamic traces. Existing benchmarks lack aligned clean references or remain limited t...
  </details>

- **2026-08-20** — Baixiang Liu, Haotian Che, Yuan Li — [TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring](http://arxiv.org/abs/2608.20097v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralized databases with limited oversight, making it difficult to verify where a document came from, whether it has been tampered with, or whether it should be trusted at all. This is a serious problem in domains where both the timeliness and accuracy of retrieved content are critical, ...
  </details>

- **2026-08-20** — Xi-Hao Chen, Kan-Xu Jia, En-Rui Zhang et al. — [A Non-Hermitian Biorthogonal Encoding Paradigm for Physical-Layer Secure Computational Imaging](http://arxiv.org/abs/2608.19878v1)
  <details><summary>📄 Abstract</summary>
  The conventional paradigm of computational imaging, rooted in Hermitian systems, is fundamentally constrained by rigid orthogonal basis transformations, which bottleneck the balance between reconstruction fidelity, computational load, and physical-layer security. In this work, we propose a generalized secure computational imaging framework based on non-Hermitian biorthogonal symmetry breaking. By mapping spatial information into a biorthogonal operator space, we establish an asymmetric sensing a...
  </details>

- **2026-08-20** — Mahyar Abbasian, Saba A. Farahani, Arshia Ilaty et al. — [A knowledge-guided agentic framework for mitigating patient-context ambiguity in health queries](http://arxiv.org/abs/2608.19875v1)
  <details><summary>📄 Abstract</summary>
  Patients often submit short, underspecified queries to healthcare chatbots that lack the patient-specific information needed to determine an appropriate response. Although these queries may be linguistically clear, they can support multiple plausible answers depending on undisclosed factors such as symptoms, diagnoses, medications, allergies, or dietary restrictions. A language model answering such a query directly may therefore rely on unsupported assumptions about the patient. We introduce a k...
  </details>

- **2026-08-20** — Astrid Horn Brorholt, Maris F. L. Galesloot, Nils Jansen et al. — [Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning](http://arxiv.org/abs/2608.19836v1)
  <details><summary>📄 Abstract</summary>
  Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov decision process (MDP). Thus, this technique is not applicable when the MDP model is not given a priori, which, unfortunately, is the case in typical RL applications. In this paper, ...
  </details>

- **2026-08-20** — Stephen Barrett, Robin Bloomfield, Alexandra Chirilă et al. — [Understanding as an Explicit and Assessable Component of Frontier AI Safety Decisions](http://arxiv.org/abs/2608.19816v1)
  <details><summary>📄 Abstract</summary>
  Decision makers need sufficient understanding to make good decisions about complex AI systems. However, AI deployment decisions are increasingly made under time-pressure, and this combined with the use of AI generated artefact creation, can mean that the existence of safety cases and system cards may no longer demonstrate that sufficient understanding exists. Our provisional methodology for making understanding explicit and assessable requires the production of an explicit description of 4 objec...
  </details>

- **2026-08-20** — Zhipeng Xu, Jiahao Lu, Yining Zheng et al. — [SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?](http://arxiv.org/abs/2608.19799v1)
  <details><summary>📄 Abstract</summary>
  Software increasingly functions as part of the scientific instrument itself, making failures in scientific code capable of compromising not only program behavior but also the evidence underlying scientific conclusions. Yet existing evaluations of coding agents largely emphasize aggregate task success, providing limited insight into why agents fail when repairing scientific software. We introduce \textbf{SWE-bench Science}, a repository-level benchmark for scientific software engineering comprisi...
  </details>

- **2026-08-20** — Josep Lumbreras, Hailan Ma, Jayne Thompson et al. — [An Irreducible Quantum Advantage in Aligning World Models with Reality](http://arxiv.org/abs/2608.19779v1)
  <details><summary>📄 Abstract</summary>
  World models provide digital simulacra of the true world, allowing agents to be trained and tested before costly real-world deployment. At each time step, they receive an action and generate an observation and reward matching the statistics of the true world. In complex environments where present outcomes depend on events far in the past, this requires memory. One might expect that, by increasing memory, we can always build a model accurately enough to align the optimal agent policies of the rea...
  </details>

- **2026-08-20** — Qihang Fan, Huaibo Huang, Zhiying Wu et al. — [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](http://arxiv.org/abs/2608.19758v1)
  <details><summary>📄 Abstract</summary>
  Long-context modeling is a pivotal capability for Large Language Models, yet the quadratic complexity of attention remains a critical bottleneck, particularly during the compute-intensive prefilling phase. Our previous work, FlashPrefill, mitigates this cost through instantaneous pattern discovery and max-based dynamic thresholding; however, it remains an algorithmic prototype that is still distant from production deployment. In this paper, we present FlashPrefill V2, which evolves FlashPrefill ...
  </details>

- **2026-08-20** — Mohan Chen — [Loreley: Repository-Scale Program Evolution with Quality-Diversity Search](http://arxiv.org/abs/2608.19703v1)
  <details><summary>📄 Abstract</summary>
  Sequential agent search accumulates changes from its current champion but discards alternative branches; independent proposals preserve breadth but restart from the root. Loreley instead retains complete repository states in a Quality-Diversity (QD) archive and samples them as parents or supplies them as context for later edits. Candidates are Git commits produced in isolated worktrees and judged by a project-supplied evaluator. We compare configured Loreley QD, sequential champion editing, and ...
  </details>

- **2026-08-20** — Haoqiang Kang, Yinpeng Chen, Luyang Liu et al. — [Scaffolding Minds: Optimizing Latent Visual Target Representations for Multimodal Reasoning](http://arxiv.org/abs/2608.19669v1)
  <details><summary>📄 Abstract</summary>
  Latent reasoning has advanced multimodal reasoning through a two-stage training paradigm: (1) a helper image is encoded into latent tokens to teach visual chain-of-thought during a supervised fine-tuning (SFT) stage, and (2) these latent tokens are further refined with reward feedback during a reinforcement learning (RL) stage. In this paper, we identify two key limitations of this framework, one in each stage. First, the SFT stage typically relies on an off-the-shelf vision encoder to encode th...
  </details>

- **2026-08-20** — Chen Cheng, Xun Huan, Yulin Pan — [Variational Goal-Oriented Optimal Experimental Design for Mixed-Distribution Quantities of Interest: Application to Ship Roll Safety](http://arxiv.org/abs/2608.19631v1)
  <details><summary>📄 Abstract</summary>
  Goal-oriented optimal experimental design (GO-OED) selects experiments according to the expected information gain (EIG) about a quantity of interest (QoI) rather than the full parameter vector. This work develops a variational GO-OED formulation for mixed discrete-continuous QoI laws arising in probabilistic mechanics when thresholding or event-based transformations map a positive-probability set of uncertain inputs to a common value while other inputs produce continuously varying responses. The...
  </details>

- **2026-08-20** — Reza Zakerian — [When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge](http://arxiv.org/abs/2608.19557v1)
  <details><summary>📄 Abstract</summary>
  Autonomous vehicles offload latency-sensitive perception tasks to nearby mobile edge computing (MEC) servers, where a missed safety-critical task is unsafe rather than merely degraded. Large language models (LLMs) are increasingly proposed as adaptive, explainable schedulers, yet evidence of when they help is scarce. We study deadline-aware, mixed-criticality scheduling on heterogeneous MEC servers, where time-critical (TC) tasks must be protected at a controlled cost to best-effort traffic, and...
  </details>

- **2026-08-20** — Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian et al. — [Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents](http://arxiv.org/abs/2608.20274v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induc...
  </details>

- **2026-08-20** — Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar et al. — [Evidence-Gated Task and Motion Planning with Vision-Language Models](http://arxiv.org/abs/2608.20084v1)
  <details><summary>📄 Abstract</summary>
  Robots executing long-horizon manipulation tasks from natural-language instructions must reason about both semantic task structure and geometric feasibility. However, under partial observability, the availability of goal-relevant objects may be uncertain. In such cases, approaches that combine Vision-Language Models (VLMs) with Task and Motion Planning (TAMP) may generate subgoals that rely on the VLM's prior knowledge without observational support, leading to execution failures or unintended ou...
  </details>

- **2026-08-20** — Jingsong Ao, Aby Philip, Alexander Streltsov — [PPT Entanglement with Correlated Catalysis: Monotones and Irreversibility](http://arxiv.org/abs/2608.20063v1)
  <details><summary>📄 Abstract</summary>
  Quantum catalysts can overcome otherwise impossible quantum state transformations without being consumed, and allowing them to become correlated with the output makes this assistance substantially more powerful. This raises a fundamental question for entanglement theory: which limitations on state manipulation remain when such correlated catalysts are freely available? We answer this question in the positive-partial-transpose (PPT) resource theory, which allows a substantially broader class of o...
  </details>

- **2026-08-20** — G. Q. Bao Tran, Takanori Miyoshi, Ho Duc Tho — [Wave-Based Bilateral Teleoperation between Nonlinear Manipulators with Direct Contact Force Feedback](http://arxiv.org/abs/2608.20043v1)
  <details><summary>📄 Abstract</summary>
  We study bilateral teleoperation between nonlinear, multi-DOF robotic manipulators in the presence of constant communication delays. Unlike classical wave-transformation architectures that transmit a coordinating force, we consider the case where the environmental force is reflected to the master side to enhance teleoperation transparency. Since direct contact force feedback might destabilize the closed-loop system, we first develop a passivity-shortage characterization for the Euler--Lagrange r...
  </details>

- **2026-08-20** — Bhavya Sukhija, Oliver Groth, Mohit Shridhar et al. — [EXIMO: VLM Guided Exploration of VLA Policies](http://arxiv.org/abs/2608.19891v1)
  <details><summary>📄 Abstract</summary>
  How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours ...
  </details>

- **2026-08-20** — Ahana Biswas — [Modeling AI Overreliance as a Complex Adaptive System](http://arxiv.org/abs/2608.19616v1)
  <details><summary>📄 Abstract</summary>
  Whether AI assistance helps or harms a population depends less on the model's accuracy than on whether people rely on it appropriately trusting it when it is right and checking it when it is not. Yet reliance is usually studied one user at a time. We model it as a population process: agents repeatedly solve a task alone, accept an AI answer, or verify it, updating a Bayesian belief about AI quality and, when networked, learning from peers. Four results form one story. The environment sets the ba...
  </details>

- **2026-08-20** — Gavin Raine Dizon, Tyrone Justin Sta Maria, Jordan Aiko Deja et al. — [Delegating or Doing? Understanding User Behavior in Hybrid Human-Agent Interfaces](http://arxiv.org/abs/2608.19551v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly embedded into applications, allowing users to complete tasks either through direct manipulation or by delegating actions to conversational agents. However, little is known about how users balance these modalities when both are available. We present a web-based content management system augmented with an LLM agent through the Model Context Protocol (MCP), enabling users to perform CRUD tasks through a graphical interface, a conversational agent, or bo...
  </details>

- **2026-08-20** — Yash Kulkarni, Shubham Harkare, Arvind Suresh Yogesh Babu — [Which Eviction Policy Should an LLM Cache Use? A Systematic Study Across Workloads, Capacities, and Encoders](http://arxiv.org/abs/2608.20280v1)
  <details><summary>📄 Abstract</summary>
  Semantic caches reuse an LLM response when the incoming query embedding lies near a cached query, but proposed eviction policies have rarely been compared under one protocol. Using CLEVER, we evaluate FIFO, LRU, LFU, ARC, GDSF, a single-pass streaming adaptation of SISO, and a semantic-redundancy policy across three ordered, deduplicated query corpora, three cache capacities, and two encoders. No evaluated policy improves on LFU by more than 0.041 percentage points in any of the eighteen setting...
  </details>

- **2026-08-20** — Christos Koutsiaris — [Daedalus-150M: A Convolution-Attention Hybrid Designed for CPU Inference](http://arxiv.org/abs/2608.20210v1)
  <details><summary>📄 Abstract</summary>
  Small language models are usually built like large ones and then squeezed onto a CPU afterwards. We did the opposite: we fixed the target first, one user, one token at a time, 4-bit weights, ordinary CPU, and chose the architecture to suit it. The result keeps full attention in only 6 of its 18 blocks. The other 12 use short convolutions whose memory is two timesteps wide no matter how long the conversation gets, so two thirds of the network never re-reads a growing cache.   Trained from scratch...
  </details>

- **2026-08-20** — Lohithsai Yadala Chanchu, Hany Abdulsamad, Christian A. Naesseth — [Discrete Diffusion Inference-Time Control with Nested Sequential Monte Carlo](http://arxiv.org/abs/2608.20123v1)
  <details><summary>📄 Abstract</summary>
  We study inference-time control for text generation in discrete diffusion language models, where the goal is to steer sampling toward sequence-level rewards without retraining. Prior work in this domain has focused on particle-based methods such as best-of-$n$ sampling and bootstrap sequential Monte Carlo, which may suffer from overoptimism and weight degeneracy, respectively. We address these limitations using \emph{nested} sequential Monte Carlo methods. We formulate nested SMC (NSMC) and full...
  </details>

- **2026-08-20** — Kui-Wang Choi, Minming Li, Nicholas Teh — [Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings](http://arxiv.org/abs/2608.20033v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division of indivisible mixed manna. Items arrive over time and must be allocated irrevocably; an item may be a good for some agents, a chore for others, and neutral for the rest. We require the cumulative allocation after every round to be envy-free up to one item (TEF1). Although deciding whether a TEF1 allocation exists is NP-hard even for goods, we identify several tractable settings. First, with at most $k$ item types, an online cyclic rule guarantees EF$\lceil k/2\rc...
  </details>

- **2026-08-20** — Chenyang Zhao, Jiqiang Zhang, Li Chen et al. — [Emergence of cooperation: A reputation-modulated reinforcement learning](http://arxiv.org/abs/2608.20016v1)
  <details><summary>📄 Abstract</summary>
  Reputation is widely recognized as a key mechanism for sustaining cooperation. However, most existing game-theoretic models treat reputation primarily as an external factor that modulates payoffs, interaction structures, or strategy update rules. In many social contexts, though, reputation operates primarily as information -- it shapes how individuals interpret their own experiences and assess the behavior of others. To bridge this gap, we propose a spatial prisoner's dilemma game grounded in th...
  </details>

- **2026-08-20** — Yuan Wu, Mairui Li, Lesia Semenova et al. — [The Asymmetric Harms of LLM Compression](http://arxiv.org/abs/2608.19670v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) compression reduces deployment costs, but standard aggregate metrics like perplexity and accuracy often mask underlying behavioral shifts. In this work, we systematically evaluate 3 LLMs across 11 compression methods to investigate the effects of compression on knowledge retention, model confidence, and social bias. We find that compression disproportionately reduces the relative retention of head knowledge compared to tail knowledge. Furthermore, compressed models o...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 594 |
| prompt-injection | 503 |
| memory-poisoning | 44 |
| tool-use-attack | 126 |
| backdoor | 422 |
| adversarial-attack | 569 |
| privacy-leakage | 3906 |
| steganography | 57 |
| misuse | 928 |
| red-teaming | 116 |
| vulnerability | 2803 |
| defense | 2540 |
| alignment | 2347 |
| robustness | 2390 |
| watermark | 334 |
| unlearning | 92 |
| agent-safety | 52 |
| benchmark | 62 |
| survey | 296 |
| other | 6736 |

---

📚 **全部 24917 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-08-26 00:58:21*