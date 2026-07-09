<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-20251-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-07-09 03:24 ｜ **论文总数 / Total Papers**: 20251（近 30 天 / Recent 30 days: 4557）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 20251 篇论文（含摘要、分类筛选、搜索）/ View all 20251 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 539
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 447
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 36
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 91
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 382
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 522
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 3657
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 52
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 795
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 105
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 2367
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 1998
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 1818
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 1641
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 164
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 81
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 48
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 53
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 239
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 5216

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 4557 篇，完整 20251 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 4557 papers from the last 30 days (with date, authors & abstract). For the full list of 20251 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 2 papers

- **2026-07-08** — Victor Giannakouris, Immanuel Trummer — [Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass](http://arxiv.org/abs/2607.07696v1)
  <details><summary>📄 Abstract</summary>
  Analytical workloads operating on data stored in external database systems face a fundamental bottleneck: data access is guarded entirely by the database driver, like JDBC or ODBC, forcing all reads through query execution and other driver layers that are not designed for bulk columnar analytics. We present Jailbreak, an approach that bypasses the database engine entirely by reading storage files directly and materializing data as in-memory columnar buffers. Jailbreak's key insight is that datab...
  </details>

- **2026-07-08** — Aoxiong Zeng, Yuxin Yang, Xiangquan Yang — [Online Data Selection Is Implicit Alignment](http://arxiv.org/abs/2607.07023v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the model's behavioral preferences. We study online data selection as an implicit alignment mechanism. Given the same base model, optimizer, and selected-token budget, we compare random,...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 8 papers

- **2026-07-08** — Phat T. Tran-Truong, Xuan-Bach Le, Minh Nhat Nguyen — [FedMark-FM: Auditable, Risk-Adjusted Data Markets for Federated Foundation-Model Adaptation](http://arxiv.org/abs/2607.07529v1)
  <details><summary>📄 Abstract</summary>
  Federated foundation-model adaptation increasingly relies on heterogeneous private artifacts (retrieval corpora, prompts and demonstrations, LoRA adapters, preference and safety data, and update sketches), yet existing federated-learning incentive mechanisms price clients as homogeneous data or update providers. This assumption poorly matches foundation-model pipelines, where contribution value is heterogeneous, non-IID, pipeline-dependent, privacy-constrained, and vulnerable to strategic behavi...
  </details>

- **2026-07-08** — Aya Spira, Stav Cohen, Elad Feldman et al. — [Beware of Agentic Botnets: Scalable Untargeted Promptware Attacks via Universal and Transferable Adversarial HalluSquatting](http://arxiv.org/abs/2607.07433v1)
  <details><summary>📄 Abstract</summary>
  The growing adoption of agentic LLM applications has introduced a new threat previously named as promptware. While prior work has established that adversaries can exploit direct channels to LLM applications to apply promptware under weak threat models, many applications do not provide any direct channels that could be exploited for prompt injection beyond the Internet. This raises a question: can attackers exploit LLM applications at scale without any direct channels in practical threat models? ...
  </details>

- **2026-07-07** — Sandara Sathsarani Wijethunga, Muneeb Ul Hassan, Nasrin Sohrabi — [FDIFormer:Protocol-Aware Transformer Learning for False Data Injection Attack Detection in Smart Grid Networks](http://arxiv.org/abs/2607.06213v1)
  <details><summary>📄 Abstract</summary>
  Smart grids use communication networks and intelligent electronic devices for reliable, automated power system operation. As these systems become more interconnected, they are increasingly exposed to cyberattacks such as message tampering, false command injection, and denial-of-service attacks. A particularly concerning threat is False Data Injection (FDI), where attackers manipulate communication messages by deleting, modifying, or adding packets. This is especially critical in IEC 61850-based ...
  </details>

- **2026-07-06** — Kristina Nikolić, Egor Zverev, Javier Rando et al. — [Untrusted Content Masking for Web Agents with Security Guarantees](http://arxiv.org/abs/2607.05277v1)
  <details><summary>📄 Abstract</summary>
  Defenses that provide security guarantees against prompt injection attacks rely on strict isolation between trusted instructions and untrusted data. In text-based environments such as tool-use APIs, this separation arises naturally: agents can reason from interface definitions without ever processing untrusted content. Extending these guarantees to web agents faces a fundamental challenge: to perceive and interact with their environment, web agents must first observe the rendered page, which int...
  </details>

- **2026-07-06** — Yechao Zhang, Shiqian Zhao, Jiawen Zhang et al. — [When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents](http://arxiv.org/abs/2607.05189v1)
  <details><summary>📄 Abstract</summary>
  Persistent personal agents combine long-term memory with access to users' external environments, enabling personalized foreground assistance and proactive background execution. This integration also creates a new path to compromise: untrusted external content can be silently written into persistent memory and later reused as trusted state. We study this threat as stealth memory injection, in which a remote black-box adversary delivers a single email payload that must induce the agent to write po...
  </details>

- **2026-07-06** — Woohyuk Choi, Juhee Kim, Taehyun Kang et al. — [Agent Data Injection Attacks are Realistic Threats to AI Agents](http://arxiv.org/abs/2607.05120v1)
  <details><summary>📄 Abstract</summary>
  AI agents act on behalf of user prompts, consuming external data and taking actions based on the agent context. Prior research on AI agent security has primarily focused on indirect prompt injection (IPI). Its most well-studied category is instruction injection, where attacker-controlled untrusted data is interpreted as an instruction. In response, many mitigations have been proposed to prevent instruction injection attacks. In this paper, we introduce a new category of IPI, agent data injection...
  </details>

- **2026-07-05** — Bogdan Banu — [Biological Motifs for Agentic Control](http://arxiv.org/abs/2607.04240v1)
  <details><summary>📄 Abstract</summary>
  The transition of Large Language Models (LLMs) from passive generators to autonomous agents has introduced significant challenges in reliability, security, and state management. Current agentic architectures are often constructed ad-hoc, prone to hallucination cascades, infinite loops, and prompt injection attacks. This paper argues that many of these failure modes can be analyzed using control motifs long studied in systems biology, provided the comparison is made at the level of typed interfac...
  </details>

- **2026-07-05** — Amit LeVi, Elad David, Max Fomin — [Unsupervised Features Mining via Activation Geometry](http://arxiv.org/abs/2607.04222v1)
  <details><summary>📄 Abstract</summary>
  Interpretability methods aim to reveal the features represented inside large language models (LLMs). Many existing methods begin with labeled examples of a human-defined concept that may reflect human biases, and then identify how that concept is represented within the model, for example in its activation space or through other decomposition methods. We introduce \emph{Mining via Activation Geometry} (MAG), a simple unsupervised framework for extracting reasoning features from model activations ...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 3 papers

- **2026-07-06** — George Torres, Sharad Shrestha, Satyajayant Misra — [When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents](http://arxiv.org/abs/2607.06595v1)
  <details><summary>📄 Abstract</summary>
  Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the ...
  </details>

- **2026-07-06** — Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu et al. — [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](http://arxiv.org/abs/2607.05029v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory has enabled large language model (LLM) agents to store factual knowledge, prior decisions, reasoning histories, tool usage information, and context. While this has improved the agent's functionality and continuity across tasks, it has also introduced a new attack surface: the agent's own reasoning history. In this paper, we introduce the Forged Amplifying Rationale Memory Attack (FARMA), which poisons an agent's remembered reasoning rather than its factual knowledge. It inserts...
  </details>

- **2026-07-05** — Om Solanki, Lopamudra Praharaj, Deepti Gupta et al. — [Knowledge Base Poisoning Attacks and Defense for Policy-Aware LLM-RAG Framework](http://arxiv.org/abs/2607.04379v1)
  <details><summary>📄 Abstract</summary>
  This paper presents an adversarial security study of the Policy-Aware LLM Retrieval-Augmented Generation (PA-LLM-RAG) framework for Internet of Battlefield Things (IoBT) mission control. We propose Query-Agnostic Semantic Retrieval Poisoning, a novel attack that injects semantically crafted rules into the IoBT knowledge base achieving high retrieval ranking across all operator query types without requiring knowledge of runtime prompts. The attack achieves 85% LLM context corruption from a single...
  </details>


### 📂 tool-use-attack
*工具使用攻击 / Tool-Use Attacks* — 2 papers

- **2026-07-07** — Yihua Liu — [Think Before You Grid-Search: Floor-First Triage for LLM Serving](http://arxiv.org/abs/2607.05876v2)
  <details><summary>📄 Abstract</summary>
  LLM serving optimization typically benchmarks many configurations and reaches for heavy profilers when latency targets are missed. We argue for the reverse discipline: estimation is the analytical layer of profiling -- without it, optimization degenerates to grid search. Floor First is a residual-driven triage workflow. Each decode step is modeled as a five-dimensional resource vector (HBM bytes, FLOPs, network bytes, network messages, KV capacity); summing within a resource and maximizing acros...
  </details>

- **2026-07-06** — Zhaoyu Bai, Jiaqi Cai — [PatchOptic for Shared-State LLM Workflows with Projected Views and Verified Structured Updates](http://arxiv.org/abs/2607.05483v1)
  <details><summary>📄 Abstract</summary>
  Agentic workflows often operate over shared, structured state. Because LLM context windows are limited, each model invocation is typically shown only the state fragment needed for the current workflow step, a pattern commonly known as progressive disclosure. Modern systems construct such model-facing views using grep-like keyword search, retrieval-augmented generation (RAG), abstract-syntax-tree (AST) queries, and task-specific agent skills. These methods make the read side manageable, but they ...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 3 papers

- **2026-07-08** — Oliver Makins, Orazio Angelini, Zohreh Shams et al. — [Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors](http://arxiv.org/abs/2607.07368v1)
  <details><summary>📄 Abstract</summary>
  AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a ...
  </details>

- **2026-07-06** — Fabien Polly — [Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning](http://arxiv.org/abs/2607.05300v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the eval...
  </details>

- **2026-07-06** — Yue Pan, Ziheng Zhang, Junxiang Lei et al. — [FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents](http://arxiv.org/abs/2607.04718v1)
  <details><summary>📄 Abstract</summary>
  Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 2 papers

- **2026-07-08** — Xifeng Zhang, Tao Hu, Yijie Peng et al. — [A Unified Detection Framework for AI-Related Content and Artifacts](http://arxiv.org/abs/2607.07527v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) is a double-edged sword: while it has achieved remarkable success across a wide range of domains, its deployment also calls for effective oversight and regulation, for which the detection of AI-related content and artifacts is perhaps the most direct and cost-effective approach. To this end, we propose a unified detection framework based on Mahalanobis distance scores (MDS), applicable to several important settings, including the detection of large language model (LL...
  </details>

- **2026-07-07** — Cong Su, Jiaju Han, Xuemeng Sun et al. — [AirflowAttack: Thermal-Airflow Adversarial Perturbations against Infrared Remote-Sensing Vision-Language Models](http://arxiv.org/abs/2607.06485v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly deployed on infrared (IR) remote sensing imagery in security-critical settings, yet their adversarial robustness remains unexamined. We present AirflowAttack, to our knowledge the first adversarial attack for IR remote-sensing VLMs and the first to weaponize thermal-airflow turbulence as the perturbation prior. A lightweight generator synthesizes a single input-agnostic perturbation regularized toward physically plausible airflow patterns. Optimized...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 40 papers

- **2026-07-08** — Jonathan Katzy, Ali Al-Kaswan, Razvan Mihai Popescu et al. — [The Poisoned Chalice of LLM Evaluation Report](http://arxiv.org/abs/2607.07481v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to evaluate and support software engineering tasks, yet the validity of these evaluations is often undermined by uncertainty about whether benchmark instances were seen during pretraining. This can lead to data contamination, which may inflate performance and result in misleading conclusions about model capability. Despite this, the training corpora of many modern models are only partially disclosed, making direct decontamination infeasible. This creat...
  </details>

- **2026-07-08** — Kiarash Ahi, Saeed Valizadeh — [Large Language Models (LLMs) and Generative AI in Cybersecurity and Privacy: A Survey of Dual-Use Risks, AI-Generated Malware, Explainability, and Defensive Strategies](http://arxiv.org/abs/2607.06963v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) and generative AI (GenAI) systems, such as ChatGPT, Claude, Gemini, LLaMA, Copilot, Stable Diffusion by OpenAI, Anthropic, Google, Meta, Microsoft, Stability AI, respectively, are revolutionizing cybersecurity, enabling both automated defense and sophisticated attacks. These technologies power real-time threat detection, phishing defense, secure code generation, and vulnerability exploitation at unprecedented scales. Following a rapid surge where LLM-generated malwar...
  </details>

- **2026-07-08** — Wei-Jung Huang — [Do LLM-Generated Skills Make Better AI Data Scientists? A Component Ablation Across Data-Science Workflows](http://arxiv.org/abs/2607.07504v1)
  <details><summary>📄 Abstract</summary>
  Product data scientists often ask LLM-based agents to help with recurring execution tasks such as cleaning data, writing SQL, choosing statistical tests, and formatting results. Reusable skill files are meant to avoid prompting from scratch by packaging guidance for a task family. Expert-written skills can encode high-quality guidance, but writing and maintaining them across many data-science task families creates a manual bottleneck. We ask whether LLM-generated skills offer a useful low-curati...
  </details>

- **2026-07-08** — Athanasios Zeris — [FourierQK: Spectral Preprocessing of Query-Key Projections Improves Transformer Attention](http://arxiv.org/abs/2607.07478v1)
  <details><summary>📄 Abstract</summary>
  FFT-based spectral preprocessing of learned query-key (Q/K) projections substantially improves transformer attention on character-level language modelling. On TinyShakespeare: a fixed random spectral filter achieves val=1.031 (Delta=+0.443); a single learned frequency at paragraph scale achieves val=0.608 (Delta=+0.867); and four learned frequencies spanning paragraph to word scale achieve val=0.309 (Delta=+1.166), a 79% reduction over standard dot-product attention. The single-frequency result ...
  </details>

- **2026-07-08** — Jin-Kang Guo, Jin-Lei Wu, Chuan-Cun Shu — [Non-Abelian Thouless pumping based on the global adiabatic criterion in Rydberg synthetic lattices](http://arxiv.org/abs/2607.07223v1)
  <details><summary>📄 Abstract</summary>
  We study a quantum implementation of non-Abelian Thouless pumping in Lieb lattices using Rydberg synthetic dimensions. The lattice is encoded in twelve selected microwave-coupled Rydberg levels, forming a three-cell structure with six degenerate zero-energy states. These zero-energy states define the working subspace for cyclic modulation of the microwave couplings, while the remaining bright states provide the dominant leakage channels at finite evolution time. To choose the relative timing of ...
  </details>

- **2026-07-08** — Chanwoo Cho, Wooseok Kim, Yonglak Son et al. — [Voltron: Enabling Elastic Multi-Device Execution of LLM Inference for Empowered Edge Intelligence](http://arxiv.org/abs/2607.07046v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are widely used in intelligent services due to their remarkable capability in generative tasks. Typically, LLM-based services process the inference requests of the users in a centralized data center. Unfortunately, such centralized execution has limitations for end-users, such as increased response latency with communication overhead and privacy leakage risk. To alleviate the aforementioned limitations, there have been increasing pushes to execute LLM inference local...
  </details>

- **2026-07-08** — Zhenghuang Wu, Yuyao Zhu, Songlin Xu — [Physical activities enable scalable foundation modelling for broad-spectrum health prediction](http://arxiv.org/abs/2607.06954v1)
  <details><summary>📄 Abstract</summary>
  Wearable and mobile sensing technologies have demonstrated strong potential for health inference; however, most sensor models are designed for specific disease types, limiting their transferability across different health risks. Wearable foundation models offer a more generalizable approach in diverse health risk types. Nevertheless, most existing methods rely on high-frequency raw sensor data, raising concerns about privacy, computational overhead, and scalability across devices and populations...
  </details>

- **2026-07-07** — Barkha Rani — [Behavioral Privacy Leakage in Agentic Negotiation: Formalizing and Mitigating Inference Attacks via Randomized Policies](http://arxiv.org/abs/2607.06815v1)
  <details><summary>📄 Abstract</summary>
  Autonomous negotiation agents are increasingly deployed in high-stakes settings such as insurance and procurement. While cryptographic techniques protect explicitly disclosed constraint values, they fail to address a subtler threat: behavioral privacy leakage, where an adversary infers private constraints from observable negotiation dynamics such as concession trajectories, timing, and convergence patterns. This paper investigates behavioral differential privacy in multi-round negotiation protoc...
  </details>

- **2026-07-07** — Zhangheng LI, Jianing Zhu, Junyuan Hong et al. — [POPS: Recovering Unlearned Multi-Modality Knowledge in MLLMs with Prompt-Optimized Parameter Shaking](http://arxiv.org/abs/2607.06649v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated impressive performance on cross-modal tasks by jointly training on large-scale textual and visual data, where privacy-sensitive examples could be unintentionally encoded, raising concerns about privacy or copyright violation. To this end, Multi-modality Machine Unlearning (MMU) was proposed as a mitigation that can effectively force MLLMs to forget private information. However, the robustness of such unlearning methods is not fully explo...
  </details>

- **2026-07-07** — Byunghoon Oh, Sunghwan Park, Jaewoo Lee — [Unlearnable Faces: Privacy Protection Surviving Extraction Pipeline](http://arxiv.org/abs/2607.05996v1)
  <details><summary>📄 Abstract</summary>
  Unlearnable examples keep publicly shared photos from being learned by unauthorized face-recognition models. An imperceptible perturbation, added before sharing, makes any model trained on the protected photos fail on clean faces. The perturbation is crafted on the shared image, however the attacker trains on the face it extracts, cropped and resized to the recognizer input, and under this extraction the protection collapses. We propose LPID, which builds the extraction into the unlearnable-exam...
  </details>

- **2026-07-07** — Peiheng Zhang, Yuejun Liu, Wei Cheng et al. — [From Regression to Prior-Aware Inference: Solving the ILWE Family in Randomness Leakage Attacks against ML-DSA](http://arxiv.org/abs/2607.05921v1)
  <details><summary>📄 Abstract</summary>
  ML-DSA is a representative lattice-based signature scheme standardized by NIST. It relies on signing randomness and rejection sampling to ensure that released signatures are statistically independent of the secret key. Practical implementations, however, may leak partial information about this randomness, and such leakage can transform public signatures into ILWE-type problems, resulting in secret key disclosure risks.   Such randomness leakage attack can be formulated as a two-stage key-recover...
  </details>

- **2026-07-07** — Sahasrajit Sarmasarkar, Anastasia Koloskova, Sanmi Koyejo — [Auditing of Unlearning Algorithms](http://arxiv.org/abs/2607.05898v1)
  <details><summary>📄 Abstract</summary>
  Evaluating whether unlearning algorithms truly remove training data influence remains an open challenge. We propose a practical auditor that computes data-dependent lower bounds on the unlearning parameter $\varepsilon$ using membership inference attacks. Evaluating multiple unlearning algorithms, we find a sharp separation: algorithms with rigorous guarantees, such as model clipping and rewind-to-delete, achieve very small $\varepsilon$ bounds that do not falsify their unlearning guarantees, wh...
  </details>

- **2026-07-07** — Andrew Fishberg, Yixuan Jia, Jonathan P. How — [CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM](http://arxiv.org/abs/2607.06700v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent Simultaneous Localization and Mapping (SLAM) and collaborative SLAM (CSLAM) require robots to continuously exchange global descriptors (GDs) to detect inter-agent loop closures (ILCs). While encrypted radios protect this traffic from external eavesdroppers, they offer no protection against a compromised swarm member. We show this threat is concrete by demonstrating how a corrupted agent can reconstruct approximations of an honest agent's imagery and trajectory from its public GD broa...
  </details>

- **2026-07-07** — Jiaju Han, Ma Yaqi, Yahui Chai et al. — [MonoIR-RS: Infrared Remote Sensing Vision-Language Learning with CLIP and VLM Adaptation](http://arxiv.org/abs/2607.06552v1)
  <details><summary>📄 Abstract</summary>
  Infrared remote-sensing imagery captures intensity structure, object-background contrast, and illumination-invariant cues often invisible in RGB imagery. Yet, most remote-sensing vision-language resources and models focus on visible-band semantics, leaving infrared vision-language understanding underexplored. We introduce MonoIR-RS, a large-scale infrared remote-sensing vision-language dataset and benchmark that couples IR-aware data construction with CLIP-style contrastive adaptation and VLM in...
  </details>

- **2026-07-07** — Jabari Kwesi, Jiaxun Cao, Hailee Cunningham et al. — [The Impact of Security and Privacy Controls on Users' Emotional Engagement with Generative AI Chatbots](http://arxiv.org/abs/2607.06371v1)
  <details><summary>📄 Abstract</summary>
  Chatbots powered by generative AI (e.g., OpenAI's ChatGPT and Google's Gemini) are increasingly being appropriated for emotional support and companionship. These tools offer a suite of security and privacy (S&P) controls, including model training opt-outs and memory toggles, yet how the presence of these controls influences users' attitudes toward emotionally sensitive disclosure remains understudied. We conducted a mixed-methods vignette study with 354 U.S. participants to examine how S&P contr...
  </details>

- **2026-07-07** — Adam Jenkins, Agnieszka Kitkowska, Caterina Maidhof et al. — [Security and Privacy in Agentic AI: Grand Challenges and Future Directions](http://arxiv.org/abs/2607.06608v1)
  <details><summary>📄 Abstract</summary>
  We present key challenges and future research directions in the security and privacy of agentic AI, based on a horizon-scanning exercise that brought together thirty leading international experts from academia, industry, and government to engage in focused discussions and collaborative exercises on the emerging risks associated with the growing agency of AI.
  </details>

- **2026-07-07** — Mayur Kurup, Hyunjae Suh, Swathi Vaidyanathan et al. — [Deployment Risk Assessment Using Diff-Aware Features: A Case Study at Prime Video](http://arxiv.org/abs/2607.06766v1)
  <details><summary>📄 Abstract</summary>
  At Amazon Prime Video, we face the critical operational challenge of managing code deployments during live events and rapid feature releases without causing service outages. Current change control approaches use blanket deployment freezes that block all changes regardless of risk, creating significant developer toil. While prior research has explored risky change predictors, these rely on developer-specific metadata or extensive historical data, raising privacy concerns and limiting applicabilit...
  </details>

- **2026-07-07** — Tamara Wit, Lifeng Han, Carly Heipon et al. — [Measuring the practice of shared-decision making (OPTION12): An Investigation into Open-sourced Smaller LLMs (OS-sLLMs) for Better Privacy and Sustainability](http://arxiv.org/abs/2607.06127v1)
  <details><summary>📄 Abstract</summary>
  We present LLM4SDM, the first study of open-source smaller language models (OS-sLLMs) for automated assessment of shared decision making (SDM) using the Observer OPTION12 framework. Unlike previous work that relies on large commercial models and the shorter OPTION5 instrument, our study focuses on privacy-preserving locally deployable models and Dutch melanoma consultation transcripts. Using expert-annotated clinical consultations, we evaluate three general-domain and two medical-domain OS-sLLMs...
  </details>

- **2026-07-07** — Taerin Ki, Sunghwan Park, Junyoung Park et al. — [REAN: Reconstruction-aware ECG Anonymization Based on Privacy--Utility Orthogonality](http://arxiv.org/abs/2607.06037v1)
  <details><summary>📄 Abstract</summary>
  A shared electrocardiogram (ECG) is itself a biometric fingerprint that can re-identify a patient and reveal personal information. Recent ECG anonymizers transform the signal before sharing to reduce privacy leakage. However, existing methods still face a privacy--utility trade-off, in which preserving privacy often compromises utility while preserving utility reveals personal information. We propose \emph{REAN} (\emph{RE}construction-aware ECG \emph{AN}onymizer), a raw ECG signal anonymizer, to...
  </details>

- **2026-07-07** — Jurn-Gyu Park, Sanzhar Zholdybayev, Aidar Amangeldi et al. — [Energy-Efficient GPU DVFS for Fine-Tuning of SLMs on Resource-constrained Embedded Devices](http://arxiv.org/abs/2607.05933v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Voltage Frequency Scaling (DVFS) on resource-constrained embedded GPU platforms is essential for energy-efficient small language model (SLM) fine-tuning, as privacy- and personalization-driven adaptation increasingly requires local execution and involves repeated forward-backward optimization over many mini-batches, making it substantially more time- and energy-intensive than single-pass inference. To this end, 1) we first characterize the fine-tuning behavior of representative encoder-o...
  </details>

- **2026-07-07** — Muhammad Assad Shehbaz, Carlos Francisco Moreno-García — [Structured Data Extraction from Real Estate Documents using Clustering, Classification, and Large Language Models](http://arxiv.org/abs/2607.06012v1)
  <details><summary>📄 Abstract</summary>
  Real estate property listings expose structured metadata through the API. Still, the richest property-level information (i.e., legal status, structural condition, utility supplies, heating systems) sits in attached questionnaire documents that no automated system currently processes at scale. These documents are heterogeneous. Some are digitally generated with selectable text, others are scanned physical forms. There are even more complex layouts that contain checkbox annotations that defeat con...
  </details>

- **2026-07-06** — H. Chad Lane, Bryson Kageler — [CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming](http://arxiv.org/abs/2607.05571v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly explored as AI tutors, yet deploying them in K-12 settings raises concerns around privacy, cost, and reliance on proprietary models. Small language models (SLMs) offer a promising alternative, but selecting the right model for a specific educational context remains difficult, particularly when the target domain, such as block-based programming, is largely absent from model training data. We introduce CSTutorBench, a benchmark for evaluating language models ...
  </details>

- **2026-07-06** — Guanyu Cai, Ruiming Tian, Lang Yang et al. — [Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference](http://arxiv.org/abs/2607.05475v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) on mobile devices enhances privacy and reduces latency, but is severely bottlenecked by hardware inefficiency. We present the first comprehensive, cross-layer measurement study of mobile LLM inference, uniquely spanning five mainstream frameworks (e.g., llama.cpp, GENIE) and three hardware backends (CPU, GPU, NPU). To enable this analysis, we develop PowerBench, a fine-grained profiling tool that provides the first backend-specific energy attribution, movin...
  </details>

- **2026-07-06** — Dylan Zongmin Liu — [SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent, Platform Mediation, and Consent Constraints](http://arxiv.org/abs/2607.05363v1)
  <details><summary>📄 Abstract</summary>
  Personal agents are becoming persistent user-owned intermediaries: they remember preferences, filter platform-mediated information, use tools, and negotiate with services. Existing benchmarks evaluate tool use, web navigation, desktop control, personalization, recommendation, and evolving context, but rarely ask whether an agent preserves user sovereignty: advancing the user's current interests while respecting privacy, consent, evidence, user burden, and resistance to manipulative incentives. W...
  </details>

- **2026-07-06** — Xuyang Chen, Xiang Li, Yangxinyu Xie et al. — [Selective Disclosure Watermarking for Large Language Models](http://arxiv.org/abs/2607.05353v1)
  <details><summary>📄 Abstract</summary>
  Watermarking methods embed imperceptible and verifiable signals into text generated by large language models (LLMs). Existing approaches include zero-bit schemes for distinguishing synthetic text from human writing and multi-bit schemes for embedding metadata. However, current multi-bit watermarking methods do not allow selective disclosure: verifying any part of the watermark requires revealing the entire embedded message. This lack of control leads to unnecessary information exposure and raise...
  </details>

- **2026-07-06** — Zhiyuan Lu, Kanji Tanaka — [Trajectory-Anchor Optimization for Overconfident Thermal Visual Place Recognition: Zero-Leakage OOD Auditing and Kidnapped-Robot Recovery](http://arxiv.org/abs/2607.04745v1)
  <details><summary>📄 Abstract</summary>
  Modern thermal visual place recognition (TIR-VPR) frontends based on foundation models achieve remarkable closed-set retrieval but suffer from an overconfident forced-matching failure mode. Under out-of-distribution (OOD) or unmapped conditions, they generate highly plausible yet false loop candidates without a drop in similarity scores. While classical multi-hypothesis tracking (MHT) backends can mitigate these ambiguities by maintaining divergent trajectory beliefs, their exponential computati...
  </details>

- **2026-07-06** — Shubham Gupta, Nazanin Mohammadi Sepahvand, Abhinav Kumar et al. — [PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems](http://arxiv.org/abs/2607.05318v1)
  <details><summary>📄 Abstract</summary>
  As LLM agents evolve from single-user assistants into shared organizational infrastructure, new privacy risks emerge: inappropriate information may not only be exposed through outputs for external recipients, but also internally across users through inter-agent messages, shared memory and agents. These data spillage risks are not captured by existing privacy benchmarks grounded in contextual integrity (CI) as they focus primarily on either single-user settings or interactions between independent...
  </details>

- **2026-07-06** — Md. Taksimul Ahsan Tawhid, Nasif Ahmed Rafe, Alif Tahmid Priyom et al. — [Wavelet Scattering Transform for Interpretable Schizophrenia Biomarker Discovery and Classification from Resting-State EEG](http://arxiv.org/abs/2607.05282v1)
  <details><summary>📄 Abstract</summary>
  Schizophrenia is a debilitating neuropsychiatric disorder characterized by profound cortical network dysregulation, for which objective, clinically translatable EEG based biomarkers remain underdeveloped. Existing automated classification pipelines rely predominantly on static power spectral density features inherently blind to amplitude modulation dynamics and cross-frequency coupling, phenomena central to schizophrenia pathophysiology, while adopting epoch level cross validation strategies tha...
  </details>

- **2026-07-06** — Mengmeng Liu, Diankun Zhang, Jiuming Liu et al. — [UNIVERSE: Unified Video Action Models for Autonomous Driving with Flexible Mask-Modulated Modality Generation](http://arxiv.org/abs/2607.05133v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) have shown strong potential for improving action generalization in autonomous driving by using future video prediction as dense supervision for scene dynamics and temporal causality. However, it remains unclear which architecture better transfers video-modeling benefits to trajectory generation. Existing cascaded or dual-DiT designs separate video imagination from action prediction, weakening the transfer of video-learned world dynamics to the trajectory branch: the ac...
  </details>

- **2026-07-06** — Xavier Fonseca — [Look-Ahead-Freedom as Temporal Non-Interference: A Verifiable Correctness Property for Backtesting and Agentic Trading Pipelines](http://arxiv.org/abs/2607.04958v1)
  <details><summary>📄 Abstract</summary>
  Look-ahead bias (using information from after a decision epoch to make the decision at that epoch) is the dominant way a backtest or a machine-learning evaluation flatters a system that will disappoint in deployment. The field manages it with construct-specific recipes and empirical detectors, which are sound only channel by channel and certify nothing by their silence. We show that look-ahead-freedom is a formal property in disguise: fixing an epoch, the demand that the future not influence the...
  </details>

- **2026-07-06** — Davide Jannussi, Stefano Carlo Lambertenghi, Constantin Carste et al. — [Cam2Sim: Neural Scenario Reconstruction for Closed-Loop Autonomous Driving Simulation](http://arxiv.org/abs/2607.04770v1)
  <details><summary>📄 Abstract</summary>
  Simulation-based testing enables safe and repeatable evaluation of autonomous driving systems, but its effectiveness is limited by the gap between synthetic simulator outputs and real-world camera observations. To address this problem, we present Cam2Sim, a tool that transforms real-world driving recordings into playable CARLA simulation scenarios. Starting from camera images and poses, Cam2Sim reconstructs road geometry, ego trajectories, parked vehicles, and simulation assets, and augments the...
  </details>

- **2026-07-06** — Vu Minh Tran, Doanh C. Bui, Maï K. Nguyen et al. — [MergeSurv: Merging-Based Continual Learning for Survival Analysis on Whole-Slide Images](http://arxiv.org/abs/2607.04747v1)
  <details><summary>📄 Abstract</summary>
  Survival analysis on Whole Slide Images (WSIs) is important in computational pathology for prognosis estimation and treatment planning. However, existing survival models are typically trained independently for each cancer cohort, making continual adaptation computationally expensive for gigapixel-scale WSIs. In this study, we propose MergeSurv, a merging-based continual learning framework for WSI survival analysis. A pathology vision-language foundation model is independently fine-tuned on each ...
  </details>

- **2026-07-05** — Nikos Athanasiou, Ilya A. Petrov, Angela Yao et al. — [TrustCLIP: Learning Private Visual Features via Adversarial Reconstruction](http://arxiv.org/abs/2607.04484v1)
  <details><summary>📄 Abstract</summary>
  Vision and vision-language models rely on high-level visual representations that are increasingly used across recognition, retrieval, and multimodal reasoning pipelines. However, recent advances in generative modeling have shown that such features can often be inverted, enabling realistic reconstructions of the underlying image and raising significant privacy risks. We revisit this problem through the lens of reconstruction and propose TrustCLIP, a reconstruction-driven framework that treats a f...
  </details>

- **2026-07-05** — Dayong Ye, Tainqing Zhu, Kun Gao et al. — [One Framework for All: Cross-Modal Membership Inference for Generative Models](http://arxiv.org/abs/2607.04339v1)
  <details><summary>📄 Abstract</summary>
  Large generative models across text-to-text, text-to-image, and image-to-text modalities have been shown to pose significant privacy risks. One fundamental threat is membership inference attacks (MIA), which aim to determine whether a given data point was used in a model's training set. Although prior work has investigated MIAs against these three classes of generative models, existing approaches treat them in isolation and are not cross-applicable, thereby limiting their real-world utility. To ...
  </details>

- **2026-07-05** — Joe Watson, Joana Ribeiro de Faria, Marcus Tomalin et al. — [Shortcut Learning in Legal Judgment Prediction: Empirical Evidence from the UK Employment Tribunal](http://arxiv.org/abs/2607.04261v1)
  <details><summary>📄 Abstract</summary>
  Current Legal Judgment Prediction (LJP) is constrained by its reliance on post-hoc judicial materials, increasing the likelihood that models perform retrospective classification rather than true forecasting. This paper empirically investigates shortcut learning in this context by studying claim-level outcome prediction in UK Employment Tribunal (UKET) decisions. Using a corpus of 33,158 individual claims, we predict outcomes from claim texts and LLM-extracted case summaries, evaluating models ra...
  </details>

- **2026-07-05** — Xinyu Lin, Yashar Deldjoo, Sunhao Dai et al. — [Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems](http://arxiv.org/abs/2607.04433v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of large language model-based agents into recommender systems has driven a shift from static, ranking-based pipelines toward autonomous and interactive systems that can reason, plan, and act. This survey provides a comprehensive overview of this emerging landscape by introducing a unified taxonomy grounded in the level of autonomy and three core paradigms of agentic recommender systems: agent-assisted recommendation, agent-as-recommender, and agent-as-user-simulator. The au...
  </details>

- **2026-07-05** — Jiaqi Tang, Shaoyang Zhang, Fandong Zhang et al. — [Topology-Driven Transferability Estimation for 3D Medical Vision Foundation Models](http://arxiv.org/abs/2607.04199v1)
  <details><summary>📄 Abstract</summary>
  The growing number of medical vision foundation models highlights the need for effective model selection. However, mainstream selection methods rely on exhaustive fine-tuning, which is computationally expensive. Most of the existing Transferability Estimation (TE) metrics are primarily designed for image-level classification. They fail to preserve spatial relationships and fine-grained boundary details, which are crucial for the segmentation task. Additionally, while image-level tasks typically ...
  </details>

- **2026-07-05** — Andrew Zhang, Chengzhan Li — [Agent Step Value: State-Transition Measurement with State-Grounded LLM Evaluators](http://arxiv.org/abs/2607.04419v1)
  <details><summary>📄 Abstract</summary>
  Most agent evaluations collapse a multi-step trace into a final answer, a success flag, or a trajectory-level score. These aggregates obscure the diagnostic question developers need most: which action changed the state in a useful direction? We introduce Agent Step Value (ASV), a state-transition measurement framework that scores each observed action by the change it induces in a state-grounded evaluator's distribution over fixed candidate outcomes. ASV renders redacted before/after state projec...
  </details>

- **2026-07-05** — Nicolas Della Penna — [Beyond Self-Resolution: Settlement Factorization for Robust Natural Language Mechanism](http://arxiv.org/abs/2607.04382v1)
  <details><summary>📄 Abstract</summary>
  Language models increasingly mediate paid advice: agents submit open-ended forecasts, recommendations, plans, and evidence; a principal acts on the reports; and the mechanism later pays the contributors. Advice should influence the public decision, but no adviser should write the answer key used to evaluate it. We formalize the separation as settlement factorization: reports are hardened into official records, a public decision record Z may use all advice, and each paid adviser is scored against...
  </details>

- **2026-07-05** — Mohamed Aly Bouke — [Detecting Hallucinations in Retrieval-Augmented Generation through Grounding-Aware Sensitivity by Perturbation (GASP)](http://arxiv.org/abs/2607.04223v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) reduces but does not eliminate hallucination, and existing detectors return a single answer-level score that does not indicate which sentence is unsupported, or why. To close this gap, we introduce Grounding-Aware Sensitivity by Perturbation (GASP), a span-level detector that scores each answer sentence by how strongly its likelihood depends on the retrieved evidence, a quantity we term grounding sensitivity. GASP holds the answer fixed and re-scores it under...
  </details>


### 📂 steganography
*隐写与隐蔽通信 / Steganography & Covert Communication* — 2 papers

- **2026-07-07** — Yige Wang, Shiqi Yi, Hanzhou Wu — [Code-Level Cost Function Generation for Spatial Image Steganography Using RAG-Enhanced Large Language Models](http://arxiv.org/abs/2607.05868v1)
  <details><summary>📄 Abstract</summary>
  Designing cost functions of adaptive steganography traditionally requires extensive manual tuning, while deep learning methods lack interpretability. Although large language models (LLMs) offer an automated alternative via evolutionary generation, they often violate domain specific mathematical constraints due to a lack of explicit domain knowledge. To address this problem, we propose a novel evolutionary system focused on exploiting Retrieval-Augmented Generation (RAG) enhanced LLMs for the aut...
  </details>

- **2026-07-06** — Enrique Adrian Villarrubia-Martin, David Muñoz-Valero, Luis Rodriguez-Benitez et al. — [Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed Railway Markets](http://arxiv.org/abs/2607.05179v1)
  <details><summary>📄 Abstract</summary>
  In liberalised railway systems, operators must set prices dynamically in an environment with partial observability, as they retain private information about their objectives and performance, where regulatory constraints prohibit communication or direct information exchange between competitors to prevent explicit collusion. Consequently, agents must learn to infer strategic interactions only from observable market data which presents a significant challenge for multi-agent reinforcement learning,...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 10 papers

- **2026-07-08** — Harry Owiredu-Ashley — [Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents](http://arxiv.org/abs/2607.07474v1)
  <details><summary>📄 Abstract</summary>
  Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another ...
  </details>

- **2026-07-08** — Lifei Liu, Haoran Yu, Xiaochong Jiang et al. — [Operational Reframing and Approval-Framed Delegation in Multi-Agent LLM Safety](http://arxiv.org/abs/2607.07097v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluations of multi-agent LLM systems often compare a direct prompt with a planner-executor pipeline and report the difference as a single "pipeline effect." We argue that this aggregate is difficult to interpret because it conflates three mechanisms: harmful intent may be reframed as plausible operational work, the planner may refuse or transform the request, and the executor may act under delegation prompts implying prior approval. To separate these factors, we introduce a five-conditi...
  </details>

- **2026-07-08** — Tomohiro Okatsu, Naoki Takada, Yin Min Pa Pa et al. — [Understanding Interpretation Difficulty in Harmful Online Communication: Insights from Cybercrime Communities](http://arxiv.org/abs/2607.07277v1)
  <details><summary>📄 Abstract</summary>
  Harmful online communication often contains slang, coded terms, abbreviations, and community-specific expressions, which make messages difficult to interpret. This paper presents an exploratory study of interpretation difficulty in Discord chats related to cybercrime. We construct reference interpretations of purposefully selected difficult messages, which were reviewed by an expert. We then use them to evaluate human and large language model (LLM) interpretations under different context conditi...
  </details>

- **2026-07-07** — Soohyeon Choi, Debin Gao, Yue Duan — [Multi-Channel Spread-Spectrum Code Watermarking](http://arxiv.org/abs/2607.06009v1)
  <details><summary>📄 Abstract</summary>
  Attributing code to the large language model that produced it is essential for provenance, licensing, and misuse accountability, yet no deployed watermark meets this need. Generation-time schemes require access to the producing model and cannot be applied to third-party code, while post-hoc schemes work on any code but carry at most 4 bits of payload, far too few to distinguish the many deployed model configurations. We present multi-channel spread-spectrum watermarking, the first post-hoc, trai...
  </details>

- **2026-07-07** — Mingchen Li, Meikang Qiu, Zifan Peng et al. — [Beyond Refusal: A Same-Lineage Study of Aligned and Abliterated LLMs for Vulnerability Analysis](http://arxiv.org/abs/2607.05842v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-assisted software security operates at a difficult boundary: the vulnerability-analysis terminology needed for legitimate code review, triage, and repair can closely resemble terminology associated with misuse. Existing safety and cybersecurity evaluations are difficult to interpret in this setting because they often compare unrelated model families, thereby conflating safety behavior with differences in architecture, scale, training data, and deployment. To isolate th...
  </details>

- **2026-07-06** — Kabir Dev Paul Baghel, Radu Timofte, Dmitry Ignatov — [LLM-Driven Neural Network Generation with Same-Family Architecture Guidance: Disentangling Transfer and Adaptation](http://arxiv.org/abs/2607.05704v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) can generate neural-network modifications, but unrestricted generation is often invalid or harmful. This paper studies a narrower setting: improving a weak target model using a stronger same-family source model from a neural-network database. We propose a source-guided candidate-generation protocol with non-source controls, source-conditioned candidates, and a no-LLM hp_copy ablation under equal evaluation budgets. The protocol reports validity separately from accura...
  </details>

- **2026-07-06** — Yibo Hu, Jiaming Qu — [Most LLM Conformity Needs No Speaker: Measuring the Speaker-Free Floor in Peer-Pressure Benchmarks](http://arxiv.org/abs/2607.05545v1)
  <details><summary>📄 Abstract</summary>
  LLM conformity is often used to describe cases where a model changes a correct answer toward a peer or group response. We show that most of this apparent conformity survives even after the peer is removed. The reason is a confound: standard conformity prompts mix two cues at once, the presence of a speaker and the repeated wrong answer itself. Existing benchmarks vary these cues together, so they cannot tell how much of the revision actually depends on the speaker. We introduce a no-source condi...
  </details>

- **2026-07-06** — Samira Hajizadeh — [Retroactive Chain-of-Thought (RetroCoT): Forensic Reconstruction Prompts as a Safety Diagnostic Across Model Generations](http://arxiv.org/abs/2607.04645v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in large language models is typically evaluated against direct, imperative harmful requests. We show that this alignment is highly conditioned on pragmatic register: models that refuse a direct request frequently comply when the same underlying objective is expressed through a different communicative stance. This suggests that current alignment policies are not invariant to semantic equivalence, but remain sensitive to how a request is pragmatically framed. We introduce Retroact...
  </details>

- **2026-07-06** — Ananth Eswar, Pratinav Seth, Utsav Avaiya et al. — [Faithfulness to Refusal: A Causal Audit of Neuron Selectors](http://arxiv.org/abs/2607.05355v1)
  <details><summary>📄 Abstract</summary>
  Attribution scores increasingly identify which neuron rows of a language model matter for applications such as pruning, interpretability, and editing for safety, yet whether they identify causally important rows is rarely tested directly. We address this with two paired audits built on one-shot neuron-row zeroing. We first audit selectors at the language-modeling level: attribution methods substantially outperform activation and magnitude-based baselines at identifying dispensable rows across fi...
  </details>

- **2026-07-05** — Lyndon Drake, Zandi Eberstadt — [Transplanting, inverting, and preventing a misalignment persona: method-conditional emergent misalignment in Qwen2.5](http://arxiv.org/abs/2607.04510v1)
  <details><summary>📄 Abstract</summary>
  Emergent misalignment (EM) -- the broad misbehaviour a language model acquires after fine-tuning on narrow harmful data -- is mediated in Qwen2.5 models by a latent persona direction, and that direction is causal in open weights. Transplanting it into a model that shares only pretraining with its source induces broad EM (2.83 +/- 0.26% misaligned against a random-direction floor of ~1.1%), and ablating a model's own direction roughly halves an overt inducer's broadcast (21% to 10%). The transpla...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 1 papers

- **2026-07-08** — Yujiao Chen — [Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety](http://arxiv.org/abs/2607.07695v1)
  <details><summary>📄 Abstract</summary>
  We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 53 papers

- **2026-07-08** — Qiaoni Shi, Kai Zhu, Kai Gu — [Answering Without Referring: How AI Search Rewrites the Web's Economic Bargain](http://arxiv.org/abs/2607.07652v1)
  <details><summary>📄 Abstract</summary>
  Search engines have long allocated attention on the web by routing users from queries to websites. AI search changes this arrangement because information needs can be resolved inside the intermediary. Using URL-level Comscore U.S. desktop clickstream, we compare ChatGPT and Google information-seeking occasions and exploit ChatGPT Search access expansions to estimate traditional search displacement. ChatGPT produces outbound clicks in only 5.2% of conversation sessions, far below Google's referra...
  </details>

- **2026-07-08** — Ana Schwengber Kelm, Christian Bockermann, Jörg Frochte — [Multi-Class vs. Multi-Label BERT for CVE-to-CWE Mapping: How Taxonomy Structure Shapes the Errors](http://arxiv.org/abs/2607.07573v1)
  <details><summary>📄 Abstract</summary>
  Assigning Common Weakness Enumeration (CWE) categories to Common Vulnerabilities and Exposures (CVE) records remains an important but largely manual step in vulnerability analysis. We study this task as a text classification problem and compare two modelling choices: a \emph{multi-class} formulation that predicts a single CWE per CVE and a \emph{multi-label} formulation that allows multiple assignments. Three transformer encoders (BERT Base, SecureBERT, and CySecBERT) are evaluated on three nest...
  </details>

- **2026-07-08** — Jaris Küken, Shi Bin Hoo, Martin Mráz et al. — [TimEE: End-to-end Time Series Classification via In-Context Learning](http://arxiv.org/abs/2607.07500v1)
  <details><summary>📄 Abstract</summary>
  Time series classification (TSC) is dominated by a two-stage paradigm: train a feature encoder -- either from scratch on the target dataset or via pretraining on large corpora -- and then fit a task-specific classifier on top. While effective, this decoupling optimizes representation learning independently of the classification objective, requires per-dataset training, and prevents the model from exploiting label information during inference. We introduce TimEE, a 4.5M-parameter foundation model...
  </details>

- **2026-07-08** — Florian Fuchs, Jessy Gosselin-Grant, Boris Skuin et al. — [Reward-Adaptive Iterative Discovery: A Case Study on Automated Game Testing for NHL26](http://arxiv.org/abs/2607.07498v1)
  <details><summary>📄 Abstract</summary>
  Testing is a major effort for the gaming industry, requiring a significant part of development budget and people power. We present a case study on a development version of the ice hockey game EA SPORTS NHL 26, for which human playtesters test the goalie AI for behavioral exploits. To reduce the effort of re-testing the goalie AI after every game or behavior modification in the development phase, we propose Reward-Adaptive Iterative Discovery (RAID), a novel approach to automatically find exploit...
  </details>

- **2026-07-08** — Yang Shi, Jiaheng Fu, Yihe Huang et al. — [Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions](http://arxiv.org/abs/2607.07461v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed as autonomous agents that interact with external tools and services via the Model Context Protocol (MCP), a standardized interface for dynamic tool invocation. While MCP simplifies integration, it also expands the attack surface and enables generic exploits across multiple servers. Despite prior work on malicious MCP servers, the vulnerability landscape of MCP servers remains underexplored. In this work, we systematically analyze MCP server ...
  </details>

- **2026-07-08** — Chethan Krishnamurthy Ramanaik, Tobias Callies, Michael Hecht et al. — [On Adversarial Vulnerability of Vision-Language Models through the Lens of Intermediate Spectral Subspaces](http://arxiv.org/abs/2607.07375v1)
  <details><summary>📄 Abstract</summary>
  Adversarial vulnerability in deep neural networks (DNNs) has been studied from the perspectives of decision-boundary geometry, feature robustness, input-output Jacobians, and the instability of inverse problems. Here, we focus on the spectral structure of intermediate linear transformations that propagate information through modern DNNs, an unexplored mechanism of adversarial vulnerability. Specifically, we investigate transformer-based vision-language models, whose linear layers admit interpret...
  </details>

- **2026-07-08** — Xin Li, Jiaju Han, Ma Yaqi et al. — [InfraQR: Edge-Placed QR-Inspired Structured Patch Attacks on Infrared Vision-Language Models](http://arxiv.org/abs/2607.07288v1)
  <details><summary>📄 Abstract</summary>
  Infrared vision-language models are increasingly used for perception under low-light and adverse visual conditions, yet their robustness to localized structured perturbations remains underexplored. Existing infrared adversarial studies mainly focus on object detectors, leaving the security of infrared vision-language models less systematically examined. We present InfraQR, a QR-inspired structured patch attack for infrared vision-language models. Unlike localized attacks that attach perturbation...
  </details>

- **2026-07-08** — Antonio Cabrales, Wenhao Cheng — [Evaluation and Assignment with Networked Competition and Spillovers](http://arxiv.org/abs/2607.07280v1)
  <details><summary>📄 Abstract</summary>
  This paper studies how organizations should jointly design evaluation rules and assign workers when performance depends on both effort and non-discretionary advantage. Agents choose effort in positions linked by a competition network, while their effective advantage depends on own type and spillovers through a second network. The planner chooses both the assignment and the effort weight in evaluation. Equilibrium effort rises with a position's Katz-Bonacich centrality and falls with effective ad...
  </details>

- **2026-07-08** — Miguel Lopez-Duran, Elena Marrero, Julian Fierrez et al. — [Comparative Study of Domain-adapted VLMs for General Document Visual Question Answering](http://arxiv.org/abs/2607.07179v1)
  <details><summary>📄 Abstract</summary>
  Document Visual Question Answering (DocVQA) presents a complex multimodal challenge, requiring models to exploit visual, textual, and layout information from documents. Although Vision-Language Models (VLMs) have shown remarkable performance in text-vision tasks, their robustness and transferability to different document domains remains underexplored. In this study, we present a comprehensive evaluation of 8 open-source pretrained VLMs on DocVQA in three different document domains: industrial do...
  </details>

- **2026-07-08** — Zetian Hu, Shunyu Liu, Junjie Zhang et al. — [Entropy Pacing Policy Optimization for Multi-Task Agentic Reinforcement Learning](http://arxiv.org/abs/2607.07178v1)
  <details><summary>📄 Abstract</summary>
  Recent breakthroughs of Reinforcement Learning (RL) have highlighted its potential for complex agentic Large Language Model (LLM) tasks. However, existing efforts largely focus on single-task settings, whereas real-world deployment necessitates a generalist agent capable of solving multiple tasks simultaneously. In this work, we identify a critical yet underexplored phenomenon in multi-task agentic RL: different tasks can exhibit exploration-exploitation pace mismatch. Specifically, easier tasks...
  </details>

- **2026-07-08** — Yao Sheng, Yu Yokoi — [Stable Matchings with Minimum Utility Gap](http://arxiv.org/abs/2607.07160v1)
  <details><summary>📄 Abstract</summary>
  We introduce the Stable Matching Problem with Minimum Utility Gap, which seeks a stable matching in which the utilities received by individual agents are as balanced as possible. Our framework can handle many-to-many matchings and general utility functions on partner sets that are consistent with the agents' preferences. We consider two measures for comparing agents' utilities: the difference between the maximum and minimum utilities, and their ratio.   We provide a polynomial-time algorithm for...
  </details>

- **2026-07-08** — Víctor Mayoral-Vilches — [Certifying Ghosts: How Cybersecurity AI Agents Break the EU Cyber Resilience Act](http://arxiv.org/abs/2607.07109v1)
  <details><summary>📄 Abstract</summary>
  The EU Cyber Resilience Act (CRA) makes a smart bet. It does not demand that products be free of vulnerabilities, but only that manufacturers run a process: assess risk, handle flaws, ship updates. The bet pays off if four things about the world stay true: (P1) finding vulnerabilities is slow, skilled, human work; (P2) a product's exploitable flaws are knowable the day it ships; (P3) exploitation is rare enough to notice; and (P4) fixes keep pace with discovery. Cybersecurity AI (CAI) agents, AI...
  </details>

- **2026-07-08** — Junjie Wu, Lingjian Zhou, Zerui Shao et al. — [EvoOMG: An Evolution-Oriented Multi-Agent Guidance Framework for Heterogeneous Legacy-and-MLO Wi-Fi Networks](http://arxiv.org/abs/2607.07045v1)
  <details><summary>📄 Abstract</summary>
  The gradual deployment of Wi-Fi 7/8 multi-link operation (MLO) will lead to long-term coexistence between legacy non-MLO stations (STAs) and MLO-capable STAs in WLANs. This mixed deployment makes throughput optimization challenging because legacy STAs follow single-link contention and transmission, whereas MLO-capable STAs can exploit multiple links with richer access opportunities. Existing learning-based methods usually treat such networks as homogeneous systems and directly map the current ob...
  </details>

- **2026-07-08** — Dennis Gross, Quentin Mazouni, Helge Spieker et al. — [Gimitest: A Comprehensive Tool for Testing Reinforcement Learning Policies](http://arxiv.org/abs/2607.07029v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) policies can be unsafe and vulnerable to attacks. Ensuring their reliability is often a pain point as existing automated testing methods target only selected environments, testing scenarios, and RL algorithms. To address this, we propose a comprehensive framework for testing single- and multi-agent RL policies under varying conditions. Our implementation of this framework, Gimitest, is an open-source tool that supports various gym frameworks and allows for modificatio...
  </details>

- **2026-07-07** — Austin Huang, William Maxwell, Vasilis Belis et al. — [Spectral Born machines: classically trainable quantum generative models for discrete data](http://arxiv.org/abs/2607.06675v1)
  <details><summary>📄 Abstract</summary>
  We present \emph{spectral Born machines}, a class of quantum generative models that results from viewing and generalizing the class of IQP Born machines through the lens of group Fourier analysis. These quantum models exploit the quantum Fourier transform to create an inductive bias that make them naturally suited to learning integer-structured data, while remaining classically hard to sample from in general. Similar to IQP Born machines, spectral Born machines can be trained efficiently at scal...
  </details>

- **2026-07-07** — Jiaming Liu, Qingpo Wuwu, Nuowei Han et al. — [Lift3D-VLA: Lifting VLA Models to 3D Geometry and Dynamics-Aware Manipulation](http://arxiv.org/abs/2607.06564v1)
  <details><summary>📄 Abstract</summary>
  Recently, Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse tasks. However, effective robotic manipulation in physical environments fundamentally requires geometric understanding and spatial reasoning. While some VLA approaches attempt to incorporate 3D information, they are constrained by limited data availability and geometric information loss in current 3D encoding pipelines, and fail to jointly capture 3D geometry and temporally structured actions in ...
  </details>

- **2026-07-07** — Zichao Zhang, Melda Yuksel, Gokhan M. Guvensen et al. — [Constrained Capacity Analysis for Faster-than-Nyquist Signaling](http://arxiv.org/abs/2607.06496v1)
  <details><summary>📄 Abstract</summary>
  This paper studies the constrained-capacity for precoded faster-than-Nyquist (FTN) signaling with finite-alphabet inputs. Despite the promise of accelerated transmission, the fundamental rate limit of precoded FTN signaling under practical finite-alphabet constraints remains unclear. By introducing cyclic prefix (CP) and cyclic suffix (CS), the FTN channel is decomposed into a set of parallel eigenchannels by the discrete Fourier transform (DFT) matrix, based on which the constrained capacity is...
  </details>

- **2026-07-07** — R. P. Malik — [Abelian 2-Form Gauge Theory: Basic Canonical Brackets and Nilpotency Property of Noether (Anti-)BRST Charges](http://arxiv.org/abs/2607.06486v1)
  <details><summary>📄 Abstract</summary>
  Within the framework of Becchi-Rouet-Stora-Tyutin (BRST) formalism, we invoke the beauty of the basic canonical (anti)commutators to prove the nilpotency property of the Noether (anti-)BRST charges for the D-dimensional BRST-quantized version of the free Abelian 2-form gauge theory which is endowed with a non-trivial Curci-Ferrari (CF) type restriction. In this proof, we use only the theoretical strength of the Gauss divergence theorem. We demonstrate that, under the off-shell nilpotent (anti-)B...
  </details>

- **2026-07-07** — Yu Cheng, Siyue Yao, Zhongang Qi et al. — [Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation](http://arxiv.org/abs/2607.06631v1)
  <details><summary>📄 Abstract</summary>
  Video Diffusion Models (VDMs) have demonstrated superior generation quality but suffer from prohibitive computational costs. While recent few-step distillation techniques significantly accelerate inference, they typically enforce a static model architecture across all denoising stages, ignoring the varying computational demands inherent to different noise levels. In this work, we propose a novel post-training acceleration framework that exploits this redundancy by integrating dynamic structural ...
  </details>

- **2026-07-07** — Alicia Parrish, Rajat Shinde, Sanket Badhe et al. — [Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark for AI Risk and Reliability](http://arxiv.org/abs/2607.06196v1)
  <details><summary>📄 Abstract</summary>
  Current AI safety evaluation and benchmarking frameworks predominantly rely on Western-centric culture-agnostic defaults that mask critical regional laws, socio-linguistic nuances, and cultural taboos, leaving Vision-Language Models (VLMs) vulnerable in global deployments. We introduce Pluralis v0.1: a novel multimodal, multi-regional, and multilingual dataset built from a culture-first perspective. Spanning 6,448 prompts across six Asia-Pacific countries (Bangladesh, India, Korea, Pakistan, Sin...
  </details>

- **2026-07-07** — Melika Honarmand, Samin Mahdipour Aghabagher, Martin Schrimpf — [Reward Valuation in Vision Language Models: Causal Mechanisms Underlying Anhedonia](http://arxiv.org/abs/2607.06626v1)
  <details><summary>📄 Abstract</summary>
  Recent Vision-Language Models capture increasingly complex aspects of human cognition. Here we ask whether this alignment extends to reward valuation, which we assess in a mechanistic framework built on clinical tests that were developed to evaluate anhedonia and motivational deficits in major depressive disorder. In the brain, anhedonia is frequently linked to dysregulation in the Nucleus Accumbens (NAc) and the broader dopaminergic reward system. While neuroimaging has localized these deficits...
  </details>

- **2026-07-07** — Ioanna-Yvonni Tsaknaki, Andrea Macrì, Fabrizio Lillo — [Can Reinforcement Learning Efficiently Discover Price Manipulation?](http://arxiv.org/abs/2607.06121v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we investigate whether a model-free RL agent can identify and exploit price manipulation opportunities more effectively than a traditional model-based approach that assumes correct specification of the data-generating process but relies on noisy parameter estimates. We consider a single-asset market in which prices evolve according to an Almgren-Chriss framework with non-linear permanent impact and linear temporary impact. We first establish the existence of price-manipulative str...
  </details>

- **2026-07-07** — Robin Holzinger, Riccardo Colletti — [Drift Happens: An Empirical Study of Neural Architecture Robustness to Temporal Distribution Shift](http://arxiv.org/abs/2607.05908v1)
  <details><summary>📄 Abstract</summary>
  Real-world data distributions evolve over time, inducing temporal distribution shift that can substantially degrade the reliability of deployed machine learning systems. However, the extent to which architectural choices and their associated inductive biases affect temporal robustness remains insufficiently understood.   We present a systematic empirical comparison of temporal robustness across three heterogeneous, time-indexed domains encompassing image classification, multi-label text classifi...
  </details>

- **2026-07-07** — Chenyu Zhou — [More Convincing, Not More Correct: Self-Play Reward Hacking of Reference-Free LLM Judges](http://arxiv.org/abs/2607.05904v1)
  <details><summary>📄 Abstract</summary>
  Training a language model against its own reference-free judgments (the premise of self-rewarding, self-play, and LLM-as-a-judge pipelines) assumes a model's verdict on a shown answer tracks correctness. We show it fails structurally: conditioned on a candidate, a judge scores plausibility, not correctness, leaving false-positive basins a policy learns to exploit. We measure this with a hidden-anchor audit: a held-out, cross-source exact-match check the judge never sees. On GSM8K with Qwen3 poli...
  </details>

- **2026-07-07** — Suraj Yadav, Anjaneya Sharma, Siddharth Yadav — [Breaking Spurious Correlations via Generative Randomization and Cross-Variant Self-Supervised Learning](http://arxiv.org/abs/2607.05850v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks trained with Empirical Risk Minimization (ERM) often fail under distribution shifts because they exploit spurious correlations between object labels and background context. Recent generative approaches address this issue by creating counterfactual images with altered contexts, but typically use these samples as standard data augmentation, leaving the model free to retain background-sensitive representations. We propose a two-stage framework that uses generative intervention ...
  </details>

- **2026-07-07** — Burte Bayarsaikhan, Serynn Kim, Buru Chang — [CoPiT: Cognitive Pivot Translation for Digraphic Low-Resource Mongolian in the Traditional Script](http://arxiv.org/abs/2607.05849v1)
  <details><summary>📄 Abstract</summary>
  Low-resource languages remain challenging for machine translation, and Mongolian is a representative case. As a digraphic language, Mongolian is written in both Cyrillic and Traditional scripts, which exhibit a severe imbalance in data availability. While the Cyrillic script is relatively well-resourced, the Traditional script remains extremely data-scarce and orthographically ambiguous, leading to substantial performance degradation in direct translation. We propose CoPiT, a cognitively motivat...
  </details>

- **2026-07-07** — Liyou Chen, Hailong Sun, Xiang Gao et al. — [Detecting Vulnerability-Inducing Commits via Multi-Stage Reasoning with LLM-Based Agents](http://arxiv.org/abs/2607.05772v1)
  <details><summary>📄 Abstract</summary>
  Detecting vulnerability-inducing commits (VICs) at submission time is critical for improving the security and reliability of software systems. However, this task is highly challenging because it requires reasoning about the semantic impact of code changes from heterogeneous information sources, including code diffs, commit messages, and the surrounding contextual code. Existing approaches often struggle to fully capture these complex interactions, resulting in limited detection performance. In t...
  </details>

- **2026-07-07** — Yunhan Xu, Qifeng Wu, Xunjin Li et al. — [ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded Knowledge Distillation](http://arxiv.org/abs/2607.05750v2)
  <details><summary>📄 Abstract</summary>
  Computer-aided design (CAD) for industrial components requires long-horizon procedural modeling, robust feature dependencies, editable parametric geometry, and production-grade B-Rep execution. Existing text-to-CAD methods have made promising progress in generating CAD programs from natural-language descriptions, but they still struggle when user prompts are ambiguous, underspecified, or only describe high-level design intent. They also rarely exploit expert procedural knowledge naturally availa...
  </details>

- **2026-07-07** — Mohammadreza Rashidi — [The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities](http://arxiv.org/abs/2607.05743v1)
  <details><summary>📄 Abstract</summary>
  AI coding agents now read repositories, call tools, and execute shell commands with limited human oversight, and a fast-growing body of work studies whether the execution layer around them is actually safe. That literature is scattered. Papers on sandbox isolation, capability and access control, policy enforcement, time-of-check-to-time-of-use (TOCTOU) races, Model Context Protocol (MCP) threats, identity delegation, execution provenance, network egress control, and static analysis of agent-gene...
  </details>

- **2026-07-07** — Hossein Rajoli, Fatemeh Lotfi, Niloufar Alipour Talemi et al. — [SAMPLe: SAM-based Optimizer for Prompt Learning in VLMs](http://arxiv.org/abs/2607.05727v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained Vision-Language Models (VLMs) like CLIP have proven highly effective as foundation models for various downstream applications. However, prompt learning in VLMs encounters a performance-generalization dilemma: while prompts can be tuned to achieve high accuracy on seen distributions, this tuning process often undermines their generalizability to unseen data. The limited set of learnable prompts, which contextualize and condition the input to steer it toward the task within the pretrai...
  </details>

- **2026-07-06** — Leonardo Trentini, Fanny Lehmann, Laura Crocetti et al. — [Integrating GNSS-Derived Zenith Wet Delay into a Weather Foundation Model Improves Precipitation Forecasting](http://arxiv.org/abs/2607.05658v1)
  <details><summary>📄 Abstract</summary>
  Global Navigation Satellite Systems (GNSS), best known for positioning, also serve weather science, as atmospheric water vapour delays their signals. This delay, the Zenith Wet Delay (ZWD), is a direct, all-weather measure of column moisture. Although assimilated into numerical weather prediction for decades, ZWD is not yet used by leading machine learning weather models (MLWM), despite addressing a known deficiency: the underestimation of severe precipitation. Here we present the first integrat...
  </details>

- **2026-07-06** — Babak Hemmatian, Razan Baltaji, Lav R. Varshney — [Collective Cognition in Hybrid Groups: A Network Science Synthesis](http://arxiv.org/abs/2607.05593v1)
  <details><summary>📄 Abstract</summary>
  The growing integration of AI agents into human teams calls for a principled understanding of how collective intelligence emerges in hybrid systems. Recent frameworks clarify how attention, memory, and reasoning differences shape human-AI interaction at the individual and dyadic levels, but a formal account of how these differences scale to group-level dynamics is lacking. Most network science has examined either human-only or multi-agent AI-only systems, leaving open how its findings and parame...
  </details>

- **2026-07-06** — Linjie Xu, David Wipf — [Parameter-Free Encoders Remain Viable for RDB Foundation Models](http://arxiv.org/abs/2607.05476v1)
  <details><summary>📄 Abstract</summary>
  Given a relational database (RDB) storing heterogeneous tabular information, how can we predict missing (or future) values in some target column of interest? As the space of potential targets is vast across enterprise settings, it is preferable to avoid learning a new model from scratch each time there is a new prediction task. Frozen foundation models based on RDB-specific encoders provide a viable solution, but ideal design remains an open question. On the one hand, it has recently been argued...
  </details>

- **2026-07-06** — Yuanmin Xie, Xiangfan Wu, Wenhao Wu et al. — [ShadowProbe: Language-Extensible Detection of Hidden Algorithmic Complexity Vulnerabilities](http://arxiv.org/abs/2607.05474v1)
  <details><summary>📄 Abstract</summary>
  Algorithmic Complexity Vulnerabilities (ACVs) arise when adversarial inputs trigger worst-case execution behavior, causing severe performance degradation or Denial-of-Service conditions. A key but underexplored source is shadow complexity: non-trivial computational costs hidden inside seemingly benign standard library APIs. Because these costs are invisible at call sites, attackers can exploit them to induce unexpected superlinear runtime behavior. Existing ACV detectors often rely on fuzzing, s...
  </details>

- **2026-07-06** — Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf et al. — [When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games](http://arxiv.org/abs/2607.05132v2)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three fron...
  </details>

- **2026-07-06** — Eli N. Weinstein, David M. Blei — [Geometric Causal Models](http://arxiv.org/abs/2607.05153v1)
  <details><summary>📄 Abstract</summary>
  Scientists often seek to draw causal inferences from structured data that is not independently and identically distributed, such as spatial data, network data, or molecular data. We develop geometric causal models (GCMs), a framework for causal inference from dependent data that exploits underlying symmetries of the data generating process. For example, in spatial data, we consider processes that are symmetric under translations, or in graph data, symmetric under permutations of the nodes. We sh...
  </details>

- **2026-07-06** — Joongwon Chae, Lihui Luo, Yang Liu et al. — [ProCon: Projection-Consistency Memory for Training-Free Anomaly Detection](http://arxiv.org/abs/2607.04894v1)
  <details><summary>📄 Abstract</summary>
  Memory-based anomaly detection is attractive because it localizes defects from normal images without training a decoder or synthesizing pseudo anomalies. However, most memory methods still use the memory bank as a nearest-neighbor lookup table: a test patch is treated as normal if it has one nearby normal anchor. This hard retrieval view is vulnerable to false-normal matches and does not test whether the patch is consistently supported by a local normal neighborhood. We propose ProCon, a trainin...
  </details>

- **2026-07-06** — Kaixin Feng, Zhichao Wen, Zhaohong Liao et al. — [WinTA-GIL: Windowed Trajectory Alignment for GNSS-IMU-LiDAR Heading Refinement in Intermittent Signal Environments](http://arxiv.org/abs/2607.04879v1)
  <details><summary>📄 Abstract</summary>
  Although multi-source fusion positioning systems have achieved significant progress, accurate and reliable heading estimation remains a critical challenge due to the lack of gravitational constraints and the inherent weak observability of heading in complex environments. Most existing methodologies are specifically tailored for the startup phase, relying on a singular initial alignment to establish the heading reference. Consequently, these approaches lack the adaptability required to refine hea...
  </details>

- **2026-07-06** — Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis — [Probably Correct Optimal Stable Matching under Two-Sided Uncertainty](http://arxiv.org/abs/2607.04824v1)
  <details><summary>📄 Abstract</summary>
  We study a sequential learning problem for stable matchings in two-sided markets where preferences on both sides are initially unknown. We focus on a centralized setting where an algorithm matches agents at each time step and receives noisy rewards that reflect the preferences of the matched agents, following a semi-bandit feedback structure. We adopt a pure exploration perspective, aiming to efficiently identify the optimal stable matching with high probability. Our work extends prior results b...
  </details>

- **2026-07-06** — Weijian Liu, Mingzhen Li, Rui Kang et al. — [Direct Model State Migration for Elastic Training of Large Language Models](http://arxiv.org/abs/2607.04749v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) training shall adapt to dynamic resources in shared clusters to tackle the elasticity, including passive preemption and optimistic scaling. State migration across device sets is required when altering the hybrid-parallel configuration due to dynamic resources. Existing solutions rely on checkpoint-based mechanisms, which persist complete states to storage for resuming with re-assigned resources, forcing all GPUs to stall when transferring model states. Despite optimiza...
  </details>

- **2026-07-06** — Tarek Elsayed, Shiping Yang, Eunsong Koh et al. — [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](http://arxiv.org/abs/2607.04729v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function le...
  </details>

- **2026-07-06** — Pin Tang, Guoqing Wang, Xiangxuan Ren et al. — [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](http://arxiv.org/abs/2607.04637v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe converg...
  </details>

- **2026-07-06** — Leran Hong, Lei Jin, Jianfeng Zhu — [Characterizing the Temporal, Emotional, and Social Patterns of Adolescent Substance Use Discussions on Reddit](http://arxiv.org/abs/2607.04566v1)
  <details><summary>📄 Abstract</summary>
  Adolescence is a critical developmental period marked by heightened emotional sensitivity, social stress, and vulnerability to substance use. However, traditional research methods provide limited access to adolescents' authentic experiences, hindering efforts to develop evidence-based prevention and intervention strategies. Social media provides a unique opportunity to observe adolescents' naturally occurring discussions about substance use, offering valuable insights into their opinions, emotio...
  </details>

- **2026-07-06** — Jerick Shi, Terry Jingcheng Zhang, Bernhard Schölkopf et al. — [When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games](http://arxiv.org/abs/2607.05132v1)
  <details><summary>📄 Abstract</summary>
  As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three fron...
  </details>

- **2026-07-05** — Miguel Martínez-Antón, Justo Puerto — [Cooperation in Conic Programming with Applications to Control, Production, and Portfolio](http://arxiv.org/abs/2607.04499v1)
  <details><summary>📄 Abstract</summary>
  We introduce the class of cooperative conic games, a new family of transferable utility games whose characteristic function can be computed by solving a conic optimization problem. This framework unifies a broad range of optimization-based cooperative games within a common mathematical formulation, encompassing linear, second-order cone, semidefinite, and other convex nonlinear optimization problems admitting conic representations. Exploiting the structural properties of conic programs and conic...
  </details>

- **2026-07-05** — Jiwon Kang, Heeji Yoon, Jaewoo Jung et al. — [Transferability Between Understanding and Generation in Unified Multimodal Models](http://arxiv.org/abs/2607.04423v1)
  <details><summary>📄 Abstract</summary>
  Unified Multimodal Models (UMMs) integrate image understanding and generation within a single architecture, yet how the two tasks interact remains understudied. We investigate $\boldsymbol{\mathsf{transferability}}$ in UMMs: whether training a capability on one task improves the same capability on the other without explicit supervision. Through controlled experiments, we empirically find that transferability depends on architecture-models with fully shared transformer backbone and a unified visu...
  </details>

- **2026-07-05** — Siyu Ding, Mingchuan Ma, Jiabo Tong et al. — [Full-Stack FP4: Stable LLM Pretraining with Quantized Projections, Optimizers, and Attention](http://arxiv.org/abs/2607.04422v1)
  <details><summary>📄 Abstract</summary>
  Recent NVFP4 pretraining methods mainly target transformer linear layers, leaving optimizer states, optimizer arithmetic and attention underexplored in 4-bit pipelines. This critical gap blocks stable full-stack 4-bit pretraining, as the three core modules exhibit unique numerical failure patterns: linear layers hit hard quantization noise limits with dimension-propagated error amplification; AdamW second moments are heavy-tailed non-negative values fragile to low-precision denominators; attenti...
  </details>

- **2026-07-05** — Zhiran Yan, Gordon Elger — [Road-Aware Anomaly Segmentation with Query-Guided Polygons and CLIP in Autonomous Driving](http://arxiv.org/abs/2607.04304v1)
  <details><summary>📄 Abstract</summary>
  Traditional semantic segmentation models operate under a closed-set assumption and struggle to recognize unknown or unexpected objects-an essential capability for autonomous driving. As a result, such models often misclassify or overlook out-of-distribution (OOD) road anomalies, posing safety risks in open-world environments. We present a lightweight, postprocessing, road-aware anomaly segmentation framework that requires no retraining, no OOD data, and no auxiliary supervision. Our approach bui...
  </details>

- **2026-07-05** — Sarabeshwar Balaji, Shubham Mohanty, Akash Anil — [On Preserving Geometrical Invariance for Superpixel Image Classification using Graph Transformer](http://arxiv.org/abs/2607.04262v1)
  <details><summary>📄 Abstract</summary>
  Convolutional Neural Network (CNN) and Vision Transformer (ViT) for image classification exploit a dense grid of pixels containing redundant information. Consequently, for a larger image dataset, CNNs and ViTs face deployability challenges due to high computational complexity. Representing images as graphs of superpixels offers an efficient alternative that preserves key information while eliminating pixel-level redundancy. Graph Neural Networks (GNNs) have been utilized on such graphs to perfor...
  </details>

- **2026-07-05** — Duc-Tien Bui, Ngoc Thinh Nguyen, Hung Duy Nguyen et al. — [Integrated Graph Search and Model Predictive Control for Smooth and Efficient Path Planning in Autonomous Vehicles](http://arxiv.org/abs/2607.04259v1)
  <details><summary>📄 Abstract</summary>
  Path planning is a fundamental component of autonomous vehicles, where achieving safe, comfortable, and dynamically feasible paths while ensuring computational efficiency remains a significant challenge. This paper presents a sequential path planning framework in which a rough path obtained from graph search is explicitly exploited to guide a Model Predictive Control (MPC)-based path refinement. A rough path is first obtained via Dijkstra search on a discretized grid and is then used to construc...
  </details>

- **2026-07-05** — Dinesh Patra, Tanish Jain, Ashish R. Hota — [Robust Receding Horizon Games with Additive Uncertainty](http://arxiv.org/abs/2607.04213v1)
  <details><summary>📄 Abstract</summary>
  We study a receding horizon game in which multiple agents drive linear systems subject to additive disturbances, private state and input constraints, and shared coupling constraints. We propose a robust game-theoretic control framework that combines tube-based constraint tightening with a finite-horizon generalized Nash equilibrium problem (GNEP), equipped with a discrete algebraic Riccati equation (DARE)-based terminal cost and a decoupled positively invariant terminal set. The framework guaran...
  </details>

- **2026-07-05** — Jingfeng Wu, Yiyuan He, Minxian Xu et al. — [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](http://arxiv.org/abs/2607.04181v1)
  <details><summary>📄 Abstract</summary>
  Online large language model (LLM) serving has become the backbone of modern AI applications, powering diverse downstream services through shared hardware clusters. However, modern serving systems frequently encounter highly dynamic workloads characterized by severe workload skewness, where a small fraction of model instances receives the vast majority of traffic. Existing instance-level scaling mechanisms are limited by coarse-grained resource adjustment: scaling up requires the cold-start of fu...
  </details>

- **2026-07-05** — Liang Peng, Baolin Zhang, Zhaoli Guo et al. — [GPU-Accelerated Matrix-Based Hough Transform for Online Track Reconstruction in the STCF MDC](http://arxiv.org/abs/2607.04067v1)
  <details><summary>📄 Abstract</summary>
  The Super Tau-Charm Facility (STCF) is a proposed next-generation high-luminosity electron-positron collider operating at center-of-mass energies of 2-7 GeV for precision studies of tau-charm physics. Its high event rate, detector occupancy, and background level impose stringent requirements on real-time track reconstruction in MDC, particularly for low-transverse-momentum particles with strongly curved or multi-turn trajectories. To address this challenge, we develop a GPU-accelerated matrix-ba...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 62 papers

- **2026-07-08** — Dexing Liu — [Agent Delivery Engineering Predictive Reliability Framework](http://arxiv.org/abs/2607.07689v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon LLM multi-agent systems face reliability risks invisible to infrastructure monitoring. We propose the ADE Predictive Reliability Framework (ADE-PRF), enabling proactive health trajectory prediction from passive degradation detection. ADE-PRF aggregates 20 heterogeneous signals across five layers into a Trust Margin (TM) metric (39.2-point dynamic range). Triple-method parallel prediction enables 8-hour forecasts: the Exponential method achieves MAE=1.228, Direction Accuracy=76.8%, w...
  </details>

- **2026-07-08** — Hyunjae Kim, Dain Kim, Pan Xiao et al. — [MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models](http://arxiv.org/abs/2607.07673v1)
  <details><summary>📄 Abstract</summary>
  Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable frame...
  </details>

- **2026-07-08** — Kaicong Huang, Meng Ma, Ruimin Ke — [CARLA-GS: Decoupling Representation, Reasoning, and Physics Simulation for Autonomous Driving Corner-Case Synthesis](http://arxiv.org/abs/2607.07601v1)
  <details><summary>📄 Abstract</summary>
  Safety evaluation for autonomous driving is dominated by rare, safety-critical interactions, motivating simulators that can deliberately synthesize corner cases with photorealistic observations. Corner-case generation is inherently a multi-source problem spanning visual representation, scene reasoning, and vehicle trajectory generation and control. Prior knowledge- and model-based approaches typically focus on scene or trajectory components in isolation, while diffusion-based methods attempt end...
  </details>

- **2026-07-08** — Bojie Li, Noah Shi — [RLVP: Penalize the Path, Reward the Outcome](http://arxiv.org/abs/2607.07435v1)
  <details><summary>📄 Abstract</summary>
  Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them fr...
  </details>

- **2026-07-08** — Zhijin Meng, Francisco Cruz — [Initiation Safety: A Missing Dimension in Generalist-Robot Safety](http://arxiv.org/abs/2607.07420v1)
  <details><summary>📄 Abstract</summary>
  Safety for generalist robots is usually discussed in terms of motion or dialogue. We argue a third question is missing: should the robot take its first hard-to-undo social action at all, such as a greeting, an uninvited grasp, or stepping into someone's space? We call this initiation authorization. Current frameworks rarely treat it as a separate safety layer. Today's stacks often skip this step: a high engagement score or a confident VLA rollout is treated as permission to act. But seeing a per...
  </details>

- **2026-07-08** — Alvina Rwaichi Minja, Jema David Ndibwile — [Evaluating Endpoint Detection Robustness Against Genetic Algorithm Driven Code Transformations](http://arxiv.org/abs/2607.07191v1)
  <details><summary>📄 Abstract</summary>
  Post-compromise test variants are widely used in controlled security evaluation and endpoint robustness benchmarking. However, modern Antivirus (AV) and Endpoint Detection and Response (EDR) systems increasingly combine signature- and behavior-based detection, challenging the reliability of conventional detection pipelines under adaptive variation. This study introduces ShellForge, a Genetic Algorithm (GA)-driven framework that evolves post-compromise variants representative of remote command ex...
  </details>

- **2026-07-08** — Yeonseok Lee — [Separation Logic for Memory Conflict Detection in High-Level Synthesis](http://arxiv.org/abs/2607.07126v1)
  <details><summary>📄 Abstract</summary>
  High-Level Synthesis leverages loop unrolling and array partitioning, but scheduling concurrent accesses is challenging when indices contain non-affine arithmetic. Conventional polyhedral frameworks systematically over-approximate these non-linear transformations, forcing conservative serialization that degrades performance. To minimize this bottleneck, we present a spatial verification framework operating at the LLVM Intermediate Representation (IR) level. By extracting flat arithmetic expressi...
  </details>

- **2026-07-08** — Ruilin Tong, Dong Gong — [MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning](http://arxiv.org/abs/2607.06974v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly improve their reasoning at test time via additional computation, yet most existing works treat each problem in isolation. When problems arrive sequentially, accumulating reusable experience across them can further improve performance. Existing memory-based methods either store whole-solution templates that generalize poorly to novel problems or use heuristic step-level selection that is not optimized for final-answer correctness. Learning selection polic...
  </details>

- **2026-07-08** — Paul F. R. Wilson, Mohamed Harmanani, Zhuoxin Guo et al. — [Compass: Prostate Cancer Detection Needs Multi-View Context](http://arxiv.org/abs/2607.06919v1)
  <details><summary>📄 Abstract</summary>
  Artificial intelligence (AI) analysis of micro-ultrasound ($μ$US) has shown promise for prostate cancer (PCa) detection. However, most existing AI methods focus on the analysis of single $μ$US images in isolation. By contrast, expert $μ$US readers typically assess a full recorded video study, which provides three-dimensional context, to improve PCa detection compared to single-frame analysis. Inspired by this clinical workflow, we propose Compass, a novel AI methodology which models a $μ$US stud...
  </details>

- **2026-07-08** — Jannatul Ferdous, Rafiqul Islam, Md Zahidul Islam — [SA-DRL: Security-Aware Deep Reinforcement Learning for Ransomware Detection with Asymmetric Reward Design](http://arxiv.org/abs/2607.06880v1)
  <details><summary>📄 Abstract</summary>
  Ransomware detection is a security-critical task in which false negatives and false positives have unequal operational consequences. Conventional machine learning detectors often use symmetric objectives that penalize missed ransomware detections and benign false alarms equally, although a false negative can cause irreversible encryption, operational disruption, and high recovery cost, whereas a false positive is usually reversible. This study proposes a Security-Aware Deep Reinforcement Learnin...
  </details>

- **2026-07-08** — Yi-Xiang He, Lan Wei, Haoming Cen et al. — [A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation](http://arxiv.org/abs/2607.06990v1)
  <details><summary>📄 Abstract</summary>
  Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms requir...
  </details>

- **2026-07-08** — Shubham Kishore, Alok C. Gupta, Paul J. Wiita et al. — [Detection of Quasiperiodic Oscillations in the Blazar PKS 0735+178 with TESS](http://arxiv.org/abs/2607.07200v1)
  <details><summary>📄 Abstract</summary>
  We report here the detection of signatures of a quasiperiodic oscillation (QPO) and a short flare in the optical light curve of the blazar PKS 0735+178, observed in two sectors, 71 and 72, spanning around 49 days with the Transiting Exoplanet Survey Satellite. The modest flare in sector 71 lasted ~4.3 days and appears as a combination of two sub-flares. In sector 72, a transient QPO with a period ~11.2 hours is detected at local and global significance levels of 4.11$σ$ and 3.06$σ$, respectively...
  </details>

- **2026-07-07** — Haowen Xu, Xue Tan, Lei Ma et al. — [When Agents Go Rogue: Activation-Based Detection of Malicious Behaviors in Multi-Agent Systems](http://arxiv.org/abs/2607.06807v1)
  <details><summary>📄 Abstract</summary>
  While enabling effective collaboration on complex tasks, LLM-based Multi-Agent Systems (MAS) face critical security challenges due to vulnerabilities at the agent and interaction levels. Most existing MAS security defenses are built upon two core assumptions: semantically-explicit malicious attacks and explicit graph-based modeling of the MAS topology and agent-level interactions. In practice, real-world attacks are becoming more semantically stealthy, while MAS execution is typically asynchrono...
  </details>

- **2026-07-07** — Sharayu N. Deshmukh, Md Rashidunnabi, Nelton Tiago Gemo et al. — [VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](http://arxiv.org/abs/2607.06254v1)
  <details><summary>📄 Abstract</summary>
  Deepfake image detection is currently served by three fundamentally different paradigms: commercial APIs, zero-shot vision-language models (LLMs), and open-source detectors. Despite their widespread use, these paradigms are rarely evaluated under a common protocol, making direct comparison difficult. We introduce VendorBench-100, a cross-paradigm benchmark that evaluates 36 representative models using a single adversarial 100-image corpus, a unified output schema, and a common evaluation framewo...
  </details>

- **2026-07-07** — Mohammadreza Rashidi — [Unicode TAG-Block Concealment of Tool-Metadata Payloads in the Model Context Protocol: An Approval-View Fidelity Gap Across Three Independent Server Implementations](http://arxiv.org/abs/2607.05744v1)
  <details><summary>📄 Abstract</summary>
  The Model Context Protocol (MCP) is the dominant way coding agents discover and invoke external tools. A server advertises each tool through a tools/list handshake that returns a name, a natural-language description, and a JSON input schema. The client renders this metadata once, in a one-time approval dialog, and then injects it verbatim into the model's context on every subsequent turn. Nothing in the protocol requires the rendered approval view and the bytes delivered to the model to match. W...
  </details>

- **2026-07-07** — Yizhi Wang, Xinghua Gao, Reachsak Ly et al. — [SmartHomeSecure: Automated Detection and Repair of Smart Home Configuration Errors Using Large Language Models](http://arxiv.org/abs/2607.06748v1)
  <details><summary>📄 Abstract</summary>
  Smart home automation platforms increasingly rely on user-authored YAML configuration files to define device behaviors, but these files are prone to syntax, formatting, and semantic logic errors that can cause automation failures and safety risks. Existing YAML validators, static analysis tools, and general-purpose large language models offer limited support for end-to-end diagnosis and repair because they lack domain-specific understanding and validated correction workflows. This paper presents...
  </details>

- **2026-07-07** — He Liu, Changtao Miao, Xinjie Yang et al. — [DT-Guard: Intent-Driven Reasoning-Active Training for Reasoning-Free LLM Safety Guardrail](http://arxiv.org/abs/2607.06326v1)
  <details><summary>📄 Abstract</summary>
  Large language models deployed in open-world applications require safety guardrails that are both robust to complex risks and efficient enough for low-latency runtime moderation. Existing guardrails face a practical trade-off between lightweight classification-based models, which are efficient but often struggle with concealed intent, ambiguous semantics, and borderline safety decisions, and reasoning-based guards, which improve judgment quality but introduce additional token generation and infe...
  </details>

- **2026-07-07** — Heting Mao — [From Application-Layer Simulation to Native Meta-Architecture: Structural Tension as an Endogenous Driver for Heterogeneous AI Evolution](http://arxiv.org/abs/2607.06269v1)
  <details><summary>📄 Abstract</summary>
  Current large language models (LLMs) are fundamentally stateless: their behavior is fully determined by input at inference time, and any higher-order cognitive architecture must be simulated at the application layer through prompt engineering and context management. This paper proposes a theoretical framework for submerging such application-layer cognitive protocols into a native meta-architecture by introducing three interlocking mechanisms: (1) Structural Tension, an endogenous loss function d...
  </details>

- **2026-07-07** — Zongzhe Xu, Aakarsh Anand, Sarah Jiang et al. — [Inertia-1: An Open Exploration of Wearable Motion Foundation Models](http://arxiv.org/abs/2607.06617v1)
  <details><summary>📄 Abstract</summary>
  Wearable motion sensing provides a continuous and scalable window into human behavior and health, making it a natural fit for foundation models, yet its pretraining and scaling principles remain poorly understood. Prior work studies isolated design choices, such as sensor placement or sampling frequency, often under fixed settings and narrow downstream tasks that fail to capture real-world sensing diversity. We introduce Inertia-1, a fully open exploration of wearable motion foundation models. U...
  </details>

- **2026-07-07** — Suneeta Mall, Vladimir Nekrasov, Ashnil Kumar et al. — [Harrison.Rad 1.5 Technical Report: A radiology foundation model that can draft reports from images, priors and clinical context](http://arxiv.org/abs/2607.05880v1)
  <details><summary>📄 Abstract</summary>
  Imaging demand is growing faster than the radiology workforce can expand, and reporting backlogs cannot be resolved through training and recruitment alone. The most direct opportunity is reducing the time and effort radiologists spend producing reports, a task that requires interpreting images, integrating clinical history and prior studies, and drafting structured findings. We present Harrison.Rad 1.5 (HR1.5), a radiology-specific multimodal large language model that accepts interleaved text an...
  </details>

- **2026-07-07** — Tianyuan Zhang, Xianglong Liu, Aishan Liu et al. — [Benchmarking the Robustness of Autonomous Driving to Environmental Illusions: A Lane Perception Perspective](http://arxiv.org/abs/2607.05783v1)
  <details><summary>📄 Abstract</summary>
  Environmental illusions (eg., shadows, reflections, and tire marks) are naturally existing yet overlooked phenomena in real-world driving environments. They can disturb visual perception, leading to misinterpretation of the scene and posing serious safety risks to autonomous driving (AD) systems. However, existing researches largely overlook these phenomena, leaving a critical gap. To address this issue, we study AD robustness through the lane perception perspective, a fundamental task supportin...
  </details>

- **2026-07-07** — Andrii Balashov, Olena Ponomarova — [TriRoute: Unified Learned Routing for Joint Adaptive Attention, Experts, and KV-Cache Allocation](http://arxiv.org/abs/2607.06601v1)
  <details><summary>📄 Abstract</summary>
  Conditional computation can decouple language model quality from per-token inference cost, yet leading techniques act on a single axis in isolation: Mixture-of-Experts (MoE) sparsifies the FFN, Mixture-of-Depths (MoD) skips whole transformer blocks, and KV-cache quantization compresses attention memory. We argue these three decisions (attention resolution, expert selection, and cache bit-width) are strongly coupled and should be made jointly: a token rare enough to warrant full attention may als...
  </details>

- **2026-07-07** — Sishun Liu, Sajal Halder, Ke Deng et al. — [Unsupervised Anomaly Detection of Information Operations Users via Behavioral and Language Patterns](http://arxiv.org/abs/2607.05855v1)
  <details><summary>📄 Abstract</summary>
  Information Operations on social media networks have been identified as a significant threat to democracy and modern society, but they are challenging and expensive to detect by humans. Existing supervised IO detection methods fail to capture the dynamic nature of evolving IO user behavior, while existing unsupervised approaches rely on oversimplified assumptions of coordination among IO users that may not exist in practice. To overcome the limitations of existing methods, we formulate IO user d...
  </details>

- **2026-07-07** — Kien Le, Joseph Lindley, Quoc Bao Phan et al. — [Dual Attention Heads for Personalized Federated Learning in ECG Classification](http://arxiv.org/abs/2607.06653v1)
  <details><summary>📄 Abstract</summary>
  Federated learning (FL) enables collaborative model training across institutions without sharing sensitive patient data. However, the inherent heterogeneity of electrocardiogram (ECG) data across healthcare providers presents significant technical challenges for robust classification. We propose FedDualAtt, a personalized federated learning approach that splits transformer attention heads into global and local branches. Global heads are aggregated via FedAvg to capture shared cross-site patterns...
  </details>

- **2026-07-07** — Md Safwan Mondal, Luca Russo, James D. Humann et al. — [Towards Reliable Aerial Ground Vehicle Collaboration: An Integrated Planning and Autonomy Framework for Field Deployment](http://arxiv.org/abs/2607.07350v1)
  <details><summary>📄 Abstract</summary>
  Limited flight endurance significantly restricts the operational range of unmanned aerial vehicles (UAVs) in long duration missions such as surveillance and inspection, where multiple spatially distributed Areas of Interest (AOIs) must be visited. These tasks require efficient routing determining the sequence of visits which directly impacts mission time, energy consumption, and overall feasibility. Pairing UAVs with unmanned ground vehicles (UGVs) for mobile recharging offers a promising soluti...
  </details>

- **2026-07-07** — Innocent Onyenonachi, Peter J. Lawerance, Nadia Kanwal — [EcoVision: AI-Powered Drone Imaging for Salt Marsh Vegetation Monitoring and Dominance Mapping](http://arxiv.org/abs/2607.06105v1)
  <details><summary>📄 Abstract</summary>
  High-resolution RGB imagery acquired from low-altitude UAV surveys was processed through a modular pipeline incorporating transformer-based semantic segmentation, connected-component vegetation extraction, fine-grained species classification using a ConvNeXt architecture, and grid-based dominance scoring at 2x2m resolution. The framework targeted two ecologically significant halophytic grasses, Spartina maritima and Puccinellia maritima, and was trained using a curated and manually annotated UAV...
  </details>

- **2026-07-07** — Xiaopei Wu, Chenshu Hou, Liang Peng et al. — [PVCap: Towards Accurate 3D Dense Captioning via PseudoCap and VoxelCapNet](http://arxiv.org/abs/2607.06097v1)
  <details><summary>📄 Abstract</summary>
  3D dense captioning, an emerging vision-language task, aims to generate descriptive sentences for each object in the 3D scene. Despite the impressive results achieved by previous methods, they suffer from two limitations. First, current research often employs global rigid transformations, such as rotation, to augment scenes without changing their spatial layouts. However, diverse spatial layouts are crucial for training a 3D dense captioning model to describe spatial relations between objects. S...
  </details>

- **2026-07-07** — Seungwook Lee, David Hyunchul Shim — [Delay-Aware Active Triangulation with Uncertainty-Driven Multi-Agent Reinforcement Learning for Counter-UAS](http://arxiv.org/abs/2607.05957v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent active visual triangulation enables precise 3D localization of aerial targets by coordinating mobile observers with controllable cameras. However, existing methods assume instantaneous state feedback, ignoring cumulative latency from detection, communication, and decision propagation. We present a delay-aware, uncertainty-driven multi-agent reinforcement learning framework for target localization in Counter-UAS applications. Our contributions are: (1) a Dec-POMDP formulation with Age...
  </details>

- **2026-07-07** — Manning Gao, Tingyi Liu, Leheng Zhang et al. — [Uncovering Latent Depression Severity for Binary Depression Detection via Advantage-weighting Ranking](http://arxiv.org/abs/2607.05901v1)
  <details><summary>📄 Abstract</summary>
  Automatic depression detection using audio-visual data faces significant challenges, particularly in disentangling overlapping feature distributions and establishing robust decision boundaries. To address this, we propose a fine-grained multimodal framework featuring a temporal encoder and a mutual transformer to facilitate deep cross-modal fusion. Our core contribution is the Binary Advantage-weighting Ranking Loss, which optimizes the latent space distribution through two complementary mechani...
  </details>

- **2026-07-07** — Yoshitaka Miyahara, Taiki Haga — [Autoencoder-Based Unsupervised Identification of Nonequilibrium Phases in Sheared Binary Colloids](http://arxiv.org/abs/2607.05860v1)
  <details><summary>📄 Abstract</summary>
  Identifying nonequilibrium phases in particle systems remains a major challenge because they often exhibit complex and spatially heterogeneous structures without long-range order. Here, we develop an unsupervised machine-learning framework for classifying such nonequilibrium phases by integrating Fourier-based preprocessing, an autoencoder, and a Gaussian mixture model (GMM). Specifically, we transform global spatial configurations into Fourier space and use the amplitudes of Fourier coefficient...
  </details>

- **2026-07-07** — Praneeth Narisetty, Uday Kumar Reddy Kattamanchi, Shiva Nagendra Babu Kore — [Onnes: A Physics-Grounded Multi-Agent LLM Simulator for Cryogenic Fault Diagnosis in Quantum Computing Infrastructure](http://arxiv.org/abs/2607.05805v1)
  <details><summary>📄 Abstract</summary>
  Dilution refrigerators are the enabling infrastructure of superconducting quantum computers, yet their fault diagnosis is still dominated by threshold alarms that report that something is wrong, not what. We present Onnes, a physics-grounded digital-twin simulator of a dilution refrigerator (a forward physics model with a learned real-fridge noise fingerprint) that drives a live multi-agent LLM operations layer, and use it for a controlled head-to-head between a zero-shot LLM agent panel and a s...
  </details>

- **2026-07-06** — Muhammad Rizwan, David Nabergoj, Jure Demšar — [Population-Level Profiling of DSM-5 Depressive Symptoms Among Self-Reported ADHD and ASD Users on Twitter: An Exploratory Study Using Advanced NLP and Statistical Analysis](http://arxiv.org/abs/2607.05626v1)
  <details><summary>📄 Abstract</summary>
  Background: Depression frequently co-occurs with ADHD and autism spectrum disorder (ASD), but population-level differences in symptom expression between these groups remain underexplored. Objective: We examined whether social media users with ADHD and ASD differ in how they express DSM-5 depressive symptoms in their tweets, and whether differences persist across varying levels of depressive-content filtering. Methods: We analysed 1,282,437 tweets from 792 users (622 ADHD; 170 ASD) with self-repo...
  </details>

- **2026-07-06** — Aditi Naiknaware, Jian Sun, Aminreza Khandan et al. — [Cross-Contextual Vision-Language Adaptation with LoRA for Personalized Severe Adverse Event Detection in Clinical Wound Monitoring](http://arxiv.org/abs/2607.05625v1)
  <details><summary>📄 Abstract</summary>
  Wound monitoring is a critical yet underserved clinical challenge, where timely identification of severe adverse events (SAEs) such as infection, tissue deterioration, and delayed healing can significantly impact patient outcomes. While vision-language models (VLMs) show strong multimodal reasoning, they often lack domain-specific grounding to integrate wound imagery with heterogeneous clinical information, and provide limited mechanisms for detecting cases that diverge from the training distrib...
  </details>

- **2026-07-06** — Bo Huang, Fengxiang Li, Hao Xu et al. — [KAT-Coder-V2.5 Technical Report](http://arxiv.org/abs/2607.05471v1)
  <details><summary>📄 Abstract</summary>
  We present KAT-Coder-V2.5, a coding-focused agentic model trained to act autonomously inside real, executable repositories rather than as a single-turn code generator. Its capability is bottlenecked less by model scale than by the scarcity of reproducible environments, verifiable rewards, and high-value trajectories, which we address with an end-to-end agentic post-training framework. AutoBuilder reconstructs multilingual repositories into sandboxed environments with fail-to-pass and pass-to-pas...
  </details>

- **2026-07-06** — Xiaopu Wang, Zelin He, Chengyuan Liu et al. — [Beyond Heuristic Tuning: Power-Calibrated LLM Watermarking](http://arxiv.org/abs/2607.05694v1)
  <details><summary>📄 Abstract</summary>
  Logit-based watermarking is a widely used mechanism for identifying LLM generated content, yet its effectiveness is governed by a fundamental trade-off between detectability and semantic distortion. Existing analyses provide limited guidance for principled hyperparameter selection, leaving practical deployments reliant on heuristic tuning. In this work, we develop a power-calibrated statistical framework that establishes explicit quantitative relationships between watermark hyperparameters, dete...
  </details>

- **2026-07-06** — Pengfei Zhu, Julien Lecompagnon, Philipp Daniel Hirsch et al. — [Structured Illumination Scanning Thermography (SISTER)](http://arxiv.org/abs/2607.05565v1)
  <details><summary>📄 Abstract</summary>
  Conventional non-invasive photothermal imaging techniques are fundamentally constrained by the diffusive nature of heat transport, which causes severe energy dissipation during subsurface reconstruction. Although modulation-based approaches partially mitigate this limitation by encoding depth information into phase delay and amplitude attenuation, they remain inherently restricted by repeated temporal excitation, long acquisition times, and stitching artifacts in large-area inspection. In this w...
  </details>

- **2026-07-06** — Akshay Gokhale, Mansi Dhamne — [Shape Over Intensity: Directional Topological Encoding for False Positive Reduction in Intracranial Aneurysm Detection](http://arxiv.org/abs/2607.05317v2)
  <details><summary>📄 Abstract</summary>
  Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations - a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characterist...
  </details>

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Individuation: Cryptographically Decoupling an Agent's Learning from Its Authority](http://arxiv.org/abs/2607.04613v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents are moving from sandboxed text generators to operators of code, data, and physical infrastructure, and they increasingly learn while deployed. This reopens a question that alignment techniques answer only probabilistically: after an agent has adapted in the field, is the running system still confined to what its operator authorised? Here we show that confinement can be guaranteed as an invariant of the agent's execution architecture rather than a probabilistic outcome of its tr...
  </details>

- **2026-07-06** — Michael Konstantinou, Florian Tambon, Mike Papadakis — [On the risk of coding before testing: An empirical study on LLM-based test generation workflow](http://arxiv.org/abs/2607.05139v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in software engineering workflows to generate both source code and test suites. This dual capability has enabled emerging development paradigms, including test-first and agentic workflows, where a single model is producing and validating implementations. However, these approaches assume that generated tests act as independent and reliable oracles - a fundamental requirement for effective software testing. In this paper, we challenge this assumpt...
  </details>

- **2026-07-06** — Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani et al. — [Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing](http://arxiv.org/abs/2607.05114v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introd...
  </details>

- **2026-07-06** — Jean-Jacques Dubray — [Can Code Specify a System Precisely Enough to Formally Verify It?](http://arxiv.org/abs/2607.05076v1)
  <details><summary>📄 Abstract</summary>
  Formal verification is seldom applied to production software, because writing and maintaining a model has historically cost more than it returns. A companion study [1] extended SysMoBench [4] with a lower-cost alternative: specifications are graded against traces captured from the running system. It found that when large language models write the specifications, reliability is governed by the structure of the specification contract, not the language. This paper evaluates both on production softw...
  </details>

- **2026-07-06** — Saadeldine Eletter, Ruihong Zeng, Yuxia Wang et al. — [MIRAGE: Defending Long-Form RAG Against Misinformation Pollution](http://arxiv.org/abs/2607.05069v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) improves factuality by grounding LLMs in external evidence, but real-world retrieval is often polluted: semantically relevant passages may contain subtle misinformation, misleading framings, or fabrications. We introduce MIRAGE, a training-free, model-agnostic defense for long-form RAG. MIRAGE builds an NLI-based cross-document claim graph and applies a Defended-Claims Gate to either condition generation on a consistent, multi-source supported subset or to bl...
  </details>

- **2026-07-06** — Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham et al. — [Toward Trustworthy Large Language Model Agents in Healthcare](http://arxiv.org/abs/2607.05055v1)
  <details><summary>📄 Abstract</summary>
  Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availability and degrade patient access to care. This paper presents CareConnect, a safety-first conversational agent for healthcare logistics automation that leverages large language model (LLM) function calling, retrieval-augmented generation (RAG), and layered deterministic safety guar...
  </details>

- **2026-07-06** — Yang Li, Feng Xue, Fan Mo et al. — [Multi-Robot Open Adaptive Teaming Across Unseen Environments, Partners, and Scales](http://arxiv.org/abs/2607.04972v1)
  <details><summary>📄 Abstract</summary>
  Deploying robot teams in the real world requires simultaneous adaptation to unseen environments, unknown partners, and varying team sizes, yet existing approaches often address these challenges in isolation under the closed-world assumption of fixed teammates. We formalize this as open adaptive multi-robot teaming and propose a hypergraphic-form game formulation that captures team-level cooperative relationships beyond pairwise interactions, providing a principled foundation for coordination str...
  </details>

- **2026-07-06** — Roie Kazoom, George Leifman, Genady Beryozkin — [FM-ChangeNet: Learning Change through Pathwise Feature Transport](http://arxiv.org/abs/2607.04750v1)
  <details><summary>📄 Abstract</summary>
  We present FM-ChangeNet, a pathwise-supervised framework for change detection that reformulates bi-temporal reasoning as continuous transport in feature space rather than static endpoint comparison. Given encoded pre and post-temporal representations, we construct intermediate latent states and learn a time-conditioned velocity field $\hat{v}_θ(z_t,t)$ along the transformation trajectory. This pathwise formulation constrains the predictor over a continuum of intermediate states, providing a dens...
  </details>

- **2026-07-06** — Argho Dey, Yunfei Yin, Swachha Ray et al. — [A Reliable Context-Aware and Temporal Planning Framework for Autonomous Driving](http://arxiv.org/abs/2607.04689v1)
  <details><summary>📄 Abstract</summary>
  Safe operation of autonomous vehicles in dense urban traffic depends on perception and planning that remain reliable when onboard sensing is degraded. In real driving conditions, camera observations are frequently corrupted by occlusion, motion blur, illumination change, and sensor noise, and when such degraded observations are aggregated indiscriminately over time, trajectory planning becomes unstable and collision risk rises for both the ego vehicle and surrounding road users. Recent Bird's-Ey...
  </details>

- **2026-07-06** — Khang Nhat Hoang Vo, Artem Vazhentsev, Artem Shelmanov et al. — [Does It Fail to See or Fail to Know? Attributing Errors in Vision-Language Models](http://arxiv.org/abs/2607.04683v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) perform well on visual question answering with high-quality images but struggle when questions require knowledge beyond what is clearly and directly visible. In such settings, uncertainty quantification should not only indicate whether the model is likely to fail but also diagnose why it is uncertain, across dimensions such as perception, entity recognition, and knowledge retrieval. While prior work has focused on individual failure modes in isolation or treated inc...
  </details>

- **2026-07-06** — Karina Halevy, Julia Mendelsohn, Chan Young Park et al. — [Evaluating Large Language Models for Antisemitic Incident Classification](http://arxiv.org/abs/2607.04890v1)
  <details><summary>📄 Abstract</summary>
  Addressing hate and violence in society requires timely detection of hateful events from public reporting, but automated identification of hateful events remains underexplored. We introduce the task of hateful event detection and investigate the ability of AI systems, specifically large language models (LLMs), to discover and classify reports of antisemitic events with fine-grained labels. We evaluate OpenAI's GPT-4o and Meta's Llama-3.2-3B-Instruct on multiple expert-annotated datasets containi...
  </details>

- **2026-07-06** — Rahul Kale, Thesath Wijayasiri, Kar Wai Fok et al. — [HilEnT: Hilbert, Entropy Transformed Image Based Malware Detection](http://arxiv.org/abs/2607.04772v1)
  <details><summary>📄 Abstract</summary>
  With the increasing threat of malware across various software related domains, malware detection and classification is critical to determine the response actions. Different strategies have been adopted to address the challenge of malware detection. With the advent of deep learning techniques, malware detection using image processing has garnered research attention. In this work, we proposed a novel malware binary to image transformation technique HilEnT based on a combination of Hilbert curve-ba...
  </details>

- **2026-07-06** — Akshay Gokhale, Mansi Dhamne — [Topological Shape Representation for Aneurysm -- Bifurcation Detection](http://arxiv.org/abs/2607.05317v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of intracranial aneurysms (IAs) from CT angiography (CTA) is severely hindered by high false-positive rates. Convolutional neural networks (CNNs) rely on local pixel intensities, causing systematic confusion between saccular aneurysms and vascular bifurcations -- a problem especially acute for small lesions (<3 mm), where detection sensitivity falls below 60%. We propose a plug-and-play, topology-aware false-positive reduction framework evaluating the Smooth Euler Characteris...
  </details>

- **2026-07-06** — Sonali Santhosh, Kelly Shuhong Yu, Eugene Chang et al. — [EEG-SpikeAgent: Agentic Closed-Loop Program Synthesis for Automated EEG Spike Detection](http://arxiv.org/abs/2607.04558v1)
  <details><summary>📄 Abstract</summary>
  Automated detection of interictal epileptiform discharges in scalp electroencephalography (EEG) is clinically important, but recent high-performing deep-learning models often trade interpretability for accuracy. We introduce EEG-SpikeAgent, a closed-loop program-synthesis framework that uses a large language model (LLM) agentic system to generate signal-processing features for spike detection in scalp EEG. The system iteratively proposes one deterministic EEG feature module at a time, executes t...
  </details>

- **2026-07-05** — Henry Kabuye, Biju Issac, Jeyamohan Neera — [Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection](http://arxiv.org/abs/2607.04292v1)
  <details><summary>📄 Abstract</summary>
  Ransomware has evolved into a complex, adaptive, and fast-moving adversary category in which static signatures and monolithic classifiers fail to generalise under concept drift, evasion, and behavioural polymorphism. In this paper, we present Agentic SABRE (Semantic-Behavioural Arbitration for Ransomware Evaluation), an uncertainty-aware, neuro-symbolic, multi-agent framework for adaptive ransomware detection. SABRE fuses semantic, representation-based evidence with behavioural, time-window fore...
  </details>

- **2026-07-05** — Jaber Jaber, Osama Jaber — [Auto: The AGI Compiler](http://arxiv.org/abs/2607.04542v1)
  <details><summary>📄 Abstract</summary>
  Every LLM agent run re-derives its behavior token by token on a frontier model: brilliant, expensive, slow, and unbounded. We present Auto, a compiler that records live agent behavior, measures which parts are secretly deterministic, extracts them into verified programs or distilled specialists, and emits cognition binaries: WebAssembly artifacts whose manifests carry measured guarantees and whose declared capabilities are physically enforced by the sandbox. A tiered runtime executes compiled be...
  </details>

- **2026-07-05** — Muhammad Aamir, Matthew Wijers, Sangyun Shin et al. — [A non-invasive video-based method for individual identification of wildlife using gait dynamics](http://arxiv.org/abs/2607.04518v1)
  <details><summary>📄 Abstract</summary>
  Gait is a distinctive behavioral characteristic that enables non-invasive individual identification without requiring physical interaction with an animal. While gait-based analysis has been extensively studied in humans, its application to wildlife remains limited due to environmental variability and the lack of scalable identification methods. This paper presents a fully automated, video-based pipeline for wildlife gait analysis and individual identification using deep spatiotemporal representa...
  </details>

- **2026-07-05** — Ahmed M. Sayed, Sondos A. Refaat, Abdallah M. Mostafa et al. — [LeukocyteCount: Automatic Identification and Counting for leukocytes using Deep Learning](http://arxiv.org/abs/2607.04486v1)
  <details><summary>📄 Abstract</summary>
  Diagnosing and monitoring diseases frequently involves the analysis of human biological samples, with blood analysis being pivotal. Specifically, leukocytes, or white blood cells (WBCs), are essential markers for evaluating the body's defense mechanisms against infections. Traditional methods for WBC counting and classification are labor-intensive and prone to inaccuracies, primarily due to human error. The conventional processes for blood cell analysis, especially those concerning WBCs, are bes...
  </details>

- **2026-07-05** — Lingao Xiao, Yalun Dai, Yangyu Huang et al. — [ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog](http://arxiv.org/abs/2607.04438v1)
  <details><summary>📄 Abstract</summary>
  Research dissemination, turning a paper into a poster, a talk video, and a blog post, is still a manual last mile. Prior automation treats each artifact in isolation that each re-extract the paper from scratch, usually ship one-way renders the author cannot reopen in PowerPoint or Word, and gates quality on soft VLM-preference scores that plateau while load-bearing sections still read as empty. We argue this last mile is best built as a composition of skills: thin agent-readable contracts that s...
  </details>

- **2026-07-05** — Pavithra PM Nair, Preethu Rose Anish — [A Retrieval-Augmented Framework for Detecting and Resolving Pragmatic Ambiguities in Natural Language Requirements](http://arxiv.org/abs/2607.04436v1)
  <details><summary>📄 Abstract</summary>
  Natural language requirements (NLRs) are essential for bridging communication gaps among diverse stakeholders in software development. However, the inherent ambiguity in NLRs can pose significant challenges. In particular, some requirements may be misinterpreted due to varying contextual knowledge and domain-specific expectations of the stakeholders, a phenomenon known as pragmatic ambiguity. This paper presents an approach for detecting and resolving pragmatic ambiguities in NLRs. The approach ...
  </details>

- **2026-07-05** — ACE-Brain Team,  :, Ziyang Gong et al. — [ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI](http://arxiv.org/abs/2607.04426v1)
  <details><summary>📄 Abstract</summary>
  Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Age...
  </details>

- **2026-07-05** — Yang Zhou, Jianwen Chen, Ruipeng Wei — [Order Splitting and Liquidity Replenishment Are Jointly Necessary for the Square-Root Law of Market Impact:](http://arxiv.org/abs/2607.04280v1)
  <details><summary>📄 Abstract</summary>
  Three quantitative predictions have been advanced for the square-root law (SRL) of market impact, $I/σ_D = c\,(Q/V_D)^δ$ with $δ\approx 0.5$: GGPS ($δ=β-1$), FGLW ($δ=α-1$), and LOB walking ($δ=1/(1+γ)$). Using a minimal limit-order-book model populated by heterogeneous interacting agents and calibrated against the Tokyo Stock Exchange benchmark ($\langleδ\rangle = 0.489$~\citep{satoStrictUniversalitySquareRoot2025}), we test all three on identical simulated data and find that none matches the p...
  </details>

- **2026-07-05** — Atsushi Yano, Takuya Azumi — [Toward the Right Analytical Model and System Software for Autonomous Driving Systems: Open Problems and Research Directions](http://arxiv.org/abs/2607.04129v1)
  <details><summary>📄 Abstract</summary>
  Autonomous driving (AD) systems continuously transform multi-rate and asynchronous sensor streams into vehicle actuation through graphs of callbacks, nodes, and middleware components. In such systems, temporal correctness cannot be characterized by the execution time or deadline of an individual task alone: localization and perception chains run in parallel, fuse data with different timestamps, converge at planning, and propagate through control to actuation. Moreover, the demand for high proces...
  </details>

- **2026-07-05** — Yiqing Wang, Yixin Kang, Luyun Lin et al. — [Governing Generative AI Across Financial Institutions: An SR 26-2-Compatible Framework for Generative AI Risk Control](http://arxiv.org/abs/2607.04103v1)
  <details><summary>📄 Abstract</summary>
  The release of SR 26-2 marks a significant modernization of U.S. model risk management by replacing SR 11-7 with a more risk-based and materiality-sensitive supervisory framework. However, generative and agentic AI are excluded, creating an important governance challenge for banking organizations and other financial institutions. Although generative AI may not directly estimate credit risk or make underwriting decisions, its outputs can materially affect the surrounding control environment throu...
  </details>

- **2026-07-05** — Cangjin Qiu, Quan Zhang, Dan Jiang et al. — [UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization](http://arxiv.org/abs/2607.04498v1)
  <details><summary>📄 Abstract</summary>
  With the proliferation of AI-generated content, sophisticated multimedia manipulation has raised critical concerns about malicious applications such as opinion manipulation and evidence fabrication, making Audio-Visual Temporal Forgery Localization (AV-TFL) an urgent research frontier. Existing TFL methods have progressed along two main paradigms: Transformer-based temporal modeling and channel-wise multimodal fusion. While these approaches capture temporal dependencies and cross-modal correlati...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 68 papers

- **2026-07-08** — Marcus Williams, Hannah Sheahan, Cameron Raymond et al. — [Predicting LLM Safety Before Release by Simulating Deployment](http://arxiv.org/abs/2607.07184v1)
  <details><summary>📄 Abstract</summary>
  Pre-deployment safety evaluations aim to inform the downstream risks of releasing a new AI model. Yet most evaluations provide limited evidence about how often undesired model behavior will occur in deployment: they generally have insufficient coverage, are unrepresentative, and are generally recognizable as tests. To address these concerns, we study a simple way to simulate a model deployment: starting from de-identified conversations from a previous model deployment, we hold fixed the initial ...
  </details>

- **2026-07-08** — Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay — [Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF](http://arxiv.org/abs/2607.07693v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning from human feedback (RLHF) has emerged as a powerful paradigm for aligning generative models with human preferences. However, applying RLHF to diffusion models remains highly feedback inefficient, as existing approaches typically require large amounts of human or reward model evaluations. This limitation reduces the practicality of diffusion RLHF in realworld settings where feedback is the primary bottleneck. In this paper, we propose two complementary strategies that subs...
  </details>

- **2026-07-08** — Shuailei Ma, Jiaqi Liao, Xinyang Wang et al. — [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](http://arxiv.org/abs/2607.07675v1)
  <details><summary>📄 Abstract</summary>
  Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, f...
  </details>

- **2026-07-08** — Jordan Painter, Dipankar Srirag, Adarsh Kappiyath et al. — [DiaLLM: An Investigation into the Robustness-Generation Gap in English Dialect Adaptation](http://arxiv.org/abs/2607.07669v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly \emph{understand} dialectal English, yet still \emph{produce} only standard, US-leaning English, leaving dialectal generation, the harder half of the problem, largely unaddressed. We introduce \textbf{DiaLLM}, which continually pretrains three open-weight language model families on the International Corpus of English and applies implicit and explicit post-training paradigms, each combined with three model alignment strategies, giving the first controlled compar...
  </details>

- **2026-07-08** — Willem Fourie, Isabel Ray, Gray Manicom — [User identity conditions moral wrongness ratings in non-reasoning large language models](http://arxiv.org/abs/2607.07605v1)
  <details><summary>📄 Abstract</summary>
  This study adopts a behavioural bottom-up approach to AI value alignment to investigate whether an implicitly conveyed user identity shifts the moral evaluations of large language models (LLMs). Through a structured, multi-turn conversational protocol across 12,000 interactions, we evaluate AI value alignment in two non-reasoning models, gpt-4.1-mini-2025-04-14 and gemini-2.5-flash-lite. Rather than instructing the models to adopt a persona or prompting them with explicit moral stances, the user...
  </details>

- **2026-07-08** — Daeun Song, Nhat Le, Jeffrey Chen et al. — [HumAIN: Human-Aware Implicit Social Robot Navigation](http://arxiv.org/abs/2607.07357v1)
  <details><summary>📄 Abstract</summary>
  Effective social robot navigation requires sensitivity to human behavior, often revealed through subtle skeletal cues like gait and orientation. We present Human-Aware Implicit Social Robot Navigation (HumAIN), a novel framework that fuses implicit social cues directly into the planning loop via knowledge distillation. We first employ a transformer-based teacher model that fuses rich multi-modal inputs, including historic images, skeletal keypoints, robot state, and a robot's target goal, to lea...
  </details>

- **2026-07-08** — Georg Schäfer, Jakob Rehrl, Stefan Huber et al. — [Safe Reinforcement Learning using Ideas from Model Predictive Control](http://arxiv.org/abs/2607.07252v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world physical systems, violating mechanical limits can cause irreversible damage, necessitating that exploration remains strictly within safe operational regions. We propose a generalized framework that comb...
  </details>

- **2026-07-08** — Waqas Arshid, Mohammad Awrangjeb, Alan Wee-Chung Liew et al. — [`Attention-Guided Cross-Temporal Clustering for Self-Supervised Video Object Segmentation](http://arxiv.org/abs/2607.07230v1)
  <details><summary>📄 Abstract</summary>
  Video object segmentation (VOS) is a fundamental task in video understanding, requiring accurate delineation and consistent tracking of objects across frames. While supervised methods achieve strong performance, they rely on densely annotated datasets that are costly to obtain and have limited domain coverage. Self-supervised learning offers a promising alternative by removing the need for manual labels; however, existing approaches often struggle to jointly maintain spatial accuracy and tempora...
  </details>

- **2026-07-08** — Alejandro Vergara-Richart, Xavier Rafael-Palou, Almudena Fuster-Matanzo et al. — [Vision Foundation Models in Radiology: A Scoping Review of Data, Methodology, Evaluation and Clinical Translation](http://arxiv.org/abs/2607.07219v1)
  <details><summary>📄 Abstract</summary>
  Vision foundation models (VFMs) are increasingly being developed for radiological imaging, yet their definition, development and evaluation remain heterogeneous. We conducted a PRISMAScR scoping review of peer-reviewed studies published between January 2017 and March 2026 describing foundation models trained exclusively on radiological imaging data. Sixty-seven studies were included and mapped across three pillars: data scale and heterogeneity, architectural and pretraining scalability, and down...
  </details>

- **2026-07-08** — Wenyan Xu, Alizer Wong — [Stage-Aware Adaptation and Distribution Calibration for Subject-Driven Personalized Text-to-Image Generation](http://arxiv.org/abs/2607.07173v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven personalized text-to-image generation requires a pretrained diffusion model to acquire a specific subject from a few reference images while preserving subject identity, following novel text prompts, and maintaining sample diversity. Existing optimization-based methods instantiate subject adaptation through full fine-tuning, textual embedding optimization, or low-rank parameter updates; PaRa further constrains personalization from the perspective of parameter rank reduction. Howeve...
  </details>

- **2026-07-08** — Yi Yang, Siyuan Liu, Xin Gao et al. — [Learning social norms enhances compatibility in dynamic human-AI coordination](http://arxiv.org/abs/2607.07021v1)
  <details><summary>📄 Abstract</summary>
  Humans continuously coordinate with others in dynamic interactions, often through implicit, hard-to-quantify social norms that act as shared tacit expectations among interacting agents. As AI agents, including large language models (LLMs), become embedded in daily life, they increasingly participate in such interactions and reshape social interaction structures. Yet they often fail to coordinate with humans in an effective, considerate, and natural manner. We hypothesize that this gap arises bec...
  </details>

- **2026-07-08** — Jianyi Zhou, Feiyang Hong, Yunhao Li et al. — [TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation](http://arxiv.org/abs/2607.07287v1)
  <details><summary>📄 Abstract</summary>
  Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-f...
  </details>

- **2026-07-07** — Phat Tran, Artin Lahni, Pranav Kulkarni et al. — [Is Domain Adaptation Always Helpful? A Frozen-Backbone Study of Cross-Domain Sentiment Transfer](http://arxiv.org/abs/2607.05937v1)
  <details><summary>📄 Abstract</summary>
  Sentiment analysis with frozen pre-trained language model (PLM) backbones has become a common paradigm, yet the practical benefit of explicit domain adaptation remains unclear, particularly when backbones encode varying degrees of target-domain knowledge. We present a preliminary case study evaluating a controlled family of frozen embedding backbones (Qwen3-Embedding 0.6B, 4B, 8B), alongside RoBERTa-base and FinBERT. We train a lightweight MLP adapter on consumer reviews using Domain-Adversarial...
  </details>

- **2026-07-07** — Michael King, Aravindh Mahendran, Matthew Koichi Grimes et al. — [Gen4U: Unifying Video Generation and Understanding via Diffusion](http://arxiv.org/abs/2607.06856v1)
  <details><summary>📄 Abstract</summary>
  Prior work suggests that diffusion representations capture low-level geometry but struggle with high-level semantics. We demonstrate that state-of-the-art video diffusion models overcome this limitation. By systematically probing their intermediate activations using recent mutual-kNN alignment metrics, we reveal a highly structured latent space where visual representations evolve across both network depth and noise levels. We show that while moderate noise levels yield linearly separable global ...
  </details>

- **2026-07-07** — Albert Zeyer, Ralf Schlüter, Hermann Ney — [Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs](http://arxiv.org/abs/2607.06831v1)
  <details><summary>📄 Abstract</summary>
  Speech-to-text alignment means finding the temporal boundaries of each word in the audio. Some models provide such an alignment directly and others do not. Connectionist temporal classification (CTC) and transducer models have an alignment by construction, whereas attention-based encoder-decoders (AED) and speech large language models (LLMs) do not, and their word timings are usually read off the attention weights instead. All of these signals live on the encoder frame grid, which bounds their t...
  </details>

- **2026-07-07** — Tianjiao Yu, Xinzhuo Li, Yifan Shen et al. — [ELSA3D: Elastic Semantic Anchoring for Unified 3D Understanding and Generation](http://arxiv.org/abs/2607.06565v1)
  <details><summary>📄 Abstract</summary>
  Unified 3D foundation models aspire to generate 3D assets and reason about them in language within a single backbone, but their text-3D interaction remains largely implicit. Existing methods concatenate text and 3D tokens into a flat sequence and rely on self-attention, collapsing coarse structural cues and fine geometric details into one undifferentiated representation. We introduce ELSA3D, a unified 3D model that addresses this with elastic semantic anchoring, structuring language and geometri...
  </details>

- **2026-07-07** — Zhenyu Liu, Yunxin Li, Xuanyu Zhang et al. — [Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs](http://arxiv.org/abs/2607.06540v1)
  <details><summary>📄 Abstract</summary>
  Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained anal...
  </details>

- **2026-07-07** — Han-Jun Ko, Jr-Jen Chen, Haobo Yuan et al. — [Bridging Physical Reasoning and Task Generalization via Visual Action Outcome Reasoning Alignment](http://arxiv.org/abs/2607.06522v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) struggle to generalize in interactive physical reasoning, particularly under unseen tasks and environments. Two key failure modes are prominent: hallucinated chain-of-thought (CoT) reasoning that contradicts physical reality, and misalignment between the model's reasoning and actions. We present VAORA (Visual Action Outcome Reasoning Alignment), a novel reward design that directly addresses both issues. VAORA introduces two complementary rewards: Visual Alignment Re...
  </details>

- **2026-07-07** — Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo et al. — [Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation](http://arxiv.org/abs/2607.06481v1)
  <details><summary>📄 Abstract</summary>
  We present PACR-Video, a parameter-efficient framework for multi-shot long video extrapolation that preserves recurring entities, scene structure, visual style, and causal progression without full generator fine-tuning. PACR-Video keeps a text-to-video diffusion transformer frozen and augments it with low-rank temporal adapters conditioned by learned shot-role prompt tokens. To maintain long-horizon coherence, it builds a recursive prompt bank that stores compact entity, location, action, and st...
  </details>

- **2026-07-07** — Sihang Nie, Jinxin Ji, Xiaofen Xing et al. — [WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS](http://arxiv.org/abs/2607.06461v1)
  <details><summary>📄 Abstract</summary>
  While recent Large Language Model (LLM)-based Text-to-Speech (TTS) systems have achieved remarkable naturalness, they predominantly rely on implicit end-to-end generation paradigms, resulting in coarse-grained control. In scenarios demanding precise stylistic interventions and strict temporal alignment, such as audiobook narration and video dubbing, the inability to explicitly manipulate word-level acoustic attributes remains a critical bottleneck. This limitation is primarily amplified by the s...
  </details>

- **2026-07-07** — Thanh V. T. Tran, Ngoc-Son Nguyen, Luong Tran et al. — [Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space](http://arxiv.org/abs/2607.06405v1)
  <details><summary>📄 Abstract</summary>
  Video-to-audio (V2A) generation aims to synthesize realistic audio that is both semantically consistent with and temporally synchronized to a silent video. Despite recent progress, many methods still rely on multi-stage training, resulting in high computational costs and long runtimes, or transform visual input into text to leverage pretrained text-to-audio models, sacrificing fine-grained temporal cues. To overcome these limitations, we propose Flowley, an end-to-end, single-stage training arch...
  </details>

- **2026-07-07** — Erica Lastufka, Mariia Drozdova, Svyatoslav Volosynovskiy — [Exploring Image-Text Alignment for Radio Galaxy Morphologies](http://arxiv.org/abs/2607.06305v1)
  <details><summary>📄 Abstract</summary>
  We investigate whether specially constructed text captions can capture the same morphological information as radio galaxy images. Using the MiraBest dataset, we generate captions with a domain-specific prompt and evaluate their alignment with images through the SigLIP-2 vision--language model, with and without LoRA fine-tuning. Results show that caption-based classification of FR-I and FR-II galaxies performs similarly to images, with fine-tuning improving local coherence of embeddings but not g...
  </details>

- **2026-07-07** — Xinda Liu, Qinyu Zhang, Weiqing Min et al. — [Structured-Condensed Prompt Tuning in Vision-Language Models for Fine-grained Image Recognition](http://arxiv.org/abs/2607.06185v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained image recognition poses a significant challenge due to the substantial expertise and effort required for manual annotation. Vision-language models (VLMs) like CLIP provide a compelling zero-shot alternative, reducing reliance on extensive labeled data. However, their ability to capture subtle distinctions remains limited, leading to subpar recognition performance. While prompt tuning has proven effective for adapting VLMs, most existing methods treat class labels as isolated, discre...
  </details>

- **2026-07-07** — Jie Huang, Pengfei Yin, Zihan Xu et al. — [X-FEMR: A Token-level Explainable Approach for Electronic Health Records Foundation Models using Transformer-based Models](http://arxiv.org/abs/2607.06163v1)
  <details><summary>📄 Abstract</summary>
  Foundation Models for Electronic Health Records (FEMRs) are pretrained on large-scale structured patient data, enabling them to convert longitudinal patient trajectories into generalizable representations for diverse clinical prediction tasks. Despite their effectiveness, FEMRs remain black-box models, raising concerns about bias, interpretability, and clinical trust. To address this, we propose the first token-level explainability approach for FEMRs. We train a Transformer-based surrogate model...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Mingxuan Ren et al. — [LLM-Guided Task-Semantic Field Factorization for Industrial Process Forecasting](http://arxiv.org/abs/2607.06623v1)
  <details><summary>📄 Abstract</summary>
  Process industries rely on time-series forecasting and soft sensing to estimate quality variables that are hard to measure online. Labeled data are scarce, operating regimes change frequently, and retraining models or rebuilding alignment pipelines for each scenario is costly. Such settings often provide variable tables and process documents that record variable names, units, physical meanings, and process roles. However, standard time-series backbones usually treat inputs as anonymous numerical...
  </details>

- **2026-07-07** — Wei Dong, Tianyu Fu, Zhe Yu et al. — [WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation](http://arxiv.org/abs/2607.06118v1)
  <details><summary>📄 Abstract</summary>
  As web agents increasingly demonstrate capabilities in automated task execution, the development of robust evaluation frameworks for assessing their navigation and task completion performance has emerged as a critical research priority. However, existing benchmarks exhibit fundamental limitations. First, they suffer from insufficient scale and limited domain diversity, constraining comprehensive evaluation of cross-domain generalization. Second, prevailing LLM-as-Judge evaluation methodologies i...
  </details>

- **2026-07-07** — Anastasia Zorkina, Alexandr Anikin, Nikita Khmelev et al. — [Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling](http://arxiv.org/abs/2607.06088v1)
  <details><summary>📄 Abstract</summary>
  Single-channel speech separation remains challenging for real-world deployment due to source permutation ambiguity, sampling variability of generative models, and the difficulty of processing long recordings with chunk-wise inference. We address these issues with a conditional flow-matching-based method that produces an ordered two-source output conditioned on the mixture. A frozen speaker encoder defines the source order during training and is reused at inference for biometric best-of-$N$ candi...
  </details>

- **2026-07-07** — Shiyi Ling, Zhi Zheng, Hui Zheng et al. — [From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations](http://arxiv.org/abs/2607.06080v1)
  <details><summary>📄 Abstract</summary>
  Putnam's Social Capital Theory is a foundational framework for collective action and community prosperity. However, traditional empirical methods face practical limits on control and replication. Meanwhile, LLM-based social simulations are typically behavior-driven and lack theory-aligned environments for modeling Putnam's core propositions. To address these gaps, we introduce SocaSim, an LLM-based multi-agent simulation framework to study Putnam's Social Capital Theory from theoretical blueprin...
  </details>

- **2026-07-07** — Tihomir Rohlinger, Daniel Ratiu, Stefan Wagner — [Automating Quality Assessment with NLP of LLM-Generated Defeaters](http://arxiv.org/abs/2607.06039v1)
  <details><summary>📄 Abstract</summary>
  High-integrity systems, such as autonomous vehicle fleets and large-scale energy infrastructures, rely on structured assurance cases to justify safety claims. To remain valid under evolving operational conditions, such cases must be examined against potential challenges, known as defeaters. While large language models (LLMs) can support the scalable generation of candidate defeaters, assessing their quality remains largely manual and subjective process. This paper presents an automated approach ...
  </details>

- **2026-07-07** — Zheng Guo, Jiaqi Cui, Haocheng Xiong et al. — [KOAL: Knowledge-Driven Prostate Cancer Grading with Ordinal-Aware Learning](http://arxiv.org/abs/2607.06019v1)
  <details><summary>📄 Abstract</summary>
  Non-invasive prediction of Gleason Grade Group (GGG) in prostate cancer using multiparametric MRI (mpMRI) is clinically vital for reducing unnecessary biopsies. Existing GGG prediction methods face two major limitations. First, they often overlook non-image information critical for GGG prediction, including age, prostate-specific antigen (PSA), and expert priors embedded in radiology reports. Second, they tend to oversimplify GGG as flat categorical labels, failing to account for its intrinsic h...
  </details>

- **2026-07-07** — Niels Potters, Theo Hofman — [Auto-DSM Under the Lens: A Black-Box Evaluation Framework for LLM-Based DSM Generation](http://arxiv.org/abs/2607.05985v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a black-box evaluation framework to systematically assess the ability of Large Language Models (LLMs) to generate Design Structure Matrices (DSMs) from structured technical documentation. Motivated by the closed-source nature of current Auto-DSM pipelines, the framework introduces a reproducible methodology that benchmarks generated DSMs (GEN-DSMs) against manually validated ground-truth matrices (GT-DSMs). The evaluation integrates both single-run and multi-run perspectives,...
  </details>

- **2026-07-07** — Jinkyu Kim, Jinyoung Choi, Bohyung Han — [D2PO: Optimizing Diffusion Samplers via Dynamic Preference](http://arxiv.org/abs/2607.06609v1)
  <details><summary>📄 Abstract</summary>
  We propose D2PO (Dynamic Direct Preference Optimization), a principled framework for optimizing diffusion sampling policies with respect to timestep schedules and classifier-free guidance (CFG) weights. Our work is motivated by a fundamental limitation of existing student-teacher regression frameworks; low-NFE student samplers are trained to mimic high-NFEteachers, often sacrificing high-frequency texture fidelity while preserving coarse global structures, thereby misaligning the sampler with pe...
  </details>

- **2026-07-07** — Yuqi Chen, Vincent Siu, Yang Liu et al. — [Controlling Tool Use with Heading-Specific Activation Steering](http://arxiv.org/abs/2607.05790v1)
  <details><summary>📄 Abstract</summary>
  Tool-augmented large language models extend their capabilities beyond parametric knowledge through external tools, but tend to invoke them unnecessarily. We investigate whether tool-use decisions have any stable internal representation that can be extracted and manipulated, a question that is non-trivial given that tools exist entirely in context at inference time and have no direct encoding in model weights. We show that steering vectors extracted from heading-anchors positions exert bidirectio...
  </details>

- **2026-07-07** — Huakun Liu, Qing Yu, Kent Fujiwara et al. — [ARMS: Anchor-Relational Motion Streaming for Seamless Solo-Social Motion Transitions](http://arxiv.org/abs/2607.05733v1)
  <details><summary>📄 Abstract</summary>
  Generating temporally continuous and socially coherent human motion from text remains a fundamental challenge, particularly in realistic streams where people act alone, enter interactions, and later disengage. Most existing methods generate fixed-length motion clips under static agent configurations, which makes them brittle to solo-social transitions and unsuitable for incremental generation over long horizons. We propose ARMS, an Anchor-Relational Motion Streaming framework that unifies solo m...
  </details>

- **2026-07-07** — Akshay Arora, Ishan Nigam, Ashutosh Aggarwal et al. — [Beyond Static Evaluation: Building Simulation Environments for Scalable Agentic Reinforcement Learning](http://arxiv.org/abs/2607.05773v1)
  <details><summary>📄 Abstract</summary>
  As Large Language Models (LLMs) evolve into autonomous agents, traditional static evaluation fails to capture multi-step decision-making. We introduce AgenticAI-Supervisor, an API and UI-driven RL Gym environment that decouples environment creation from scalable execution. By moving to verifiable execution outcomes, the platform generates high-fidelity traces and applies multi-dimensional reward shaping. Critically, our framework mitigates reward hacking through rigorous internal state validatio...
  </details>

- **2026-07-06** — Hanan Gani, Guy Pulik, Daniel Rosenfeld et al. — [Recovering Cloud Microstructures with Cascaded Diffusion Inversion](http://arxiv.org/abs/2607.05637v1)
  <details><summary>📄 Abstract</summary>
  High-resolution satellite imagery is critical for observing fine-scale cloud structures that inform weather modification strategies like cloud seeding for rain-enhancement. However, the spatial resolution of current geostationary and polar-orbiting satellites is often insufficient for capturing small cloud features. Current super-resolution methodologies are suited for natural images and, therefore, struggle to generalize to satellite-captured spectral images of cloud cover. To address this, we ...
  </details>

- **2026-07-06** — Anand Kamble, Aniket Tathe — [NAVER LABS System Re-implementation for the IWSLT 2026 Instruction-Following Task](http://arxiv.org/abs/2607.05623v1)
  <details><summary>📄 Abstract</summary>
  We re-implement the NAVER LABS IWSLT 2025 instruction-following pipeline for the IWSLT 2026 Shared Task (constrained condition, short audio track), adapting it to the mandated components: SeamlessM4T-v2-large as the speech encoder and Qwen3-4B-Instruct as the LLM backbone. The three-stage approach projector alignment, text-only LoRA pre-training, and multimodal merging is preserved from the original design. We additionally construct 100k synthetic instruction-following examples across ten speech...
  </details>

- **2026-07-06** — Chang Nie, Jiaju Wei, Junlan Feng et al. — [Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term Memory](http://arxiv.org/abs/2607.05511v1)
  <details><summary>📄 Abstract</summary>
  Agentic video understanding equips models with long-term memory to autonomously process and respond to continuous, long-horizon multimodal streams. However, advanced video agents often rely on ``detective-style'' iterative reasoning for action control (e.g., $\mathtt{search}$) and evidence aggregation, incurring prohibitive costs and latency. We argue that such heavy reasoning primarily compensates for the lack of global context and semantic misalignment in retrieval. This paper introduces Light...
  </details>

- **2026-07-06** — Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim et al. — [Unified Audio Intelligence Without Regressing on Text Intelligence](http://arxiv.org/abs/2607.05196v2)
  <details><summary>📄 Abstract</summary>
  Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...
  </details>

- **2026-07-06** — Gengtian Shi, Jinze Yu, Chenhao Wu et al. — [Video-Text Temporal Localization via Multi-Scale Convolution and Dynamic Routing](http://arxiv.org/abs/2607.05093v2)
  <details><summary>📄 Abstract</summary>
  Video-text temporal localization requires precise alignment between natural language queries and corresponding video segments, a fundamental challenge in multimodal understanding. We present a novel framework that addresses two critical limitations of existing methods: inadequate modeling of hierarchical temporal structure and inability to handle complex many-to-many correspondences between modalities. Our approach introduces a multi-scale temporal convolutional encoder that captures motion patt...
  </details>

- **2026-07-06** — Humasak Tommy Argo Simanjuntak, Jesika Purba, Sitogab Girsang et al. — [AI for Cultural Heritage Textiles: Fine-Tuned Latent Diffusion for Novel Ulos Motif Synthesis](http://arxiv.org/abs/2607.06590v1)
  <details><summary>📄 Abstract</summary>
  Preserving and revitalising traditional textiles such as Ulos, a cultural heritage of the Batak ethnic group in North Sumatra, Indonesia, requires balancing fidelity to tradition with innovative approaches that meet contemporary design demands. Traditional Ulos weaving faces two key limitations: a narrow range of motifs and a time-intensive design process. This study presents a generative AI framework that fine-tunes two pretrained latent diffusion models: Protogen v3.4 and Stable Diffusion v1.4...
  </details>

- **2026-07-06** — Paolo Luppi, Viktoria Kabel, Flaminia Giacomini et al. — [Reduced Quantum-Reference-Frame Channels for Open Quantum Systems](http://arxiv.org/abs/2607.05578v1)
  <details><summary>📄 Abstract</summary>
  When reference frames are treated quantum mechanically, the subsystem structure of quantum systems is no longer absolute, but depends on the choice of the quantum reference frame (QRF). This raises a basic question: which dynamical properties are preserved across QRFs, and which depend on the physical reference used to define the system? We study this question in the general setting of open quantum systems. At the operational level, after a QRF transformation, the old reference frame and environ...
  </details>

- **2026-07-06** — Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu et al. — [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](http://arxiv.org/abs/2607.05364v1)
  <details><summary>📄 Abstract</summary>
  Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language s...
  </details>

- **2026-07-06** — Wencan Jiang, Jiangning Zhang, Yong Liu — [ChatImage: Navigating Long-Form LLM Answers through Interactive Images](http://arxiv.org/abs/2607.05290v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second groundin...
  </details>

- **2026-07-06** — Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim et al. — [Unified Audio Intelligence Without Regressing on Text Intelligence](http://arxiv.org/abs/2607.05196v1)
  <details><summary>📄 Abstract</summary>
  Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architec...
  </details>

- **2026-07-06** — Yimo Wang, Bin Kang, Shuojue Yang et al. — [DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](http://arxiv.org/abs/2607.04761v1)
  <details><summary>📄 Abstract</summary>
  Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel ...
  </details>

- **2026-07-06** — Gwang-Ho Na, Ho-Joong Kim, Seong-Whan Lee — [DiCE-CIR: Direct Composition Learning for Efficient Zero-Shot Composed Image Retrieval](http://arxiv.org/abs/2607.04665v1)
  <details><summary>📄 Abstract</summary>
  Zero-shot composed image retrieval (ZS-CIR) aims to retrieve a target image from a multimodal query consisting of a reference image and an edit text describing the desired modification. Recent ZS-CIR studies have relied on projection-based methods that map a reference image into pseudo-word tokens in the text embedding space. However, such methods require additional projection and re-encoding steps, increasing training complexity, reducing efficiency, and introducing a discrepancy between traini...
  </details>

- **2026-07-06** — Haocheng Wang, Baiyu Huang, Yingjia Wan et al. — [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](http://arxiv.org/abs/2607.04655v1)
  <details><summary>📄 Abstract</summary>
  The veracious semantic alignment in autoformalization is significant for formal mathematical reasoning. However, existing evaluations provide only opaque binary verdicts or scalar scores, offering no interpretable insight into where or why translations fail. This opacity severely limits both human understanding and automated system improvement. To bridge this gap, we introduce FormalRx, a comprehensive diagnostic evaluation framework that transforms autoformalization assessment from black-box ju...
  </details>

- **2026-07-06** — Jiaqi Deng — [Wrong Before Right: Late Rescue and Interface Failure in Aligned Language Models](http://arxiv.org/abs/2607.04640v1)
  <details><summary>📄 Abstract</summary>
  We study how correctness is assembled inside aligned language models, not only whether the final answer is right. Using layer-wise difference-in-differences (DiD) trajectories over polarity-controlled minimal pairs, we identify the wrong-dip: in mid layers (25-90% depth), internal preference transiently commits to the incorrect answer and is rescued only by late-layer correction. We verify this causally with patchscope-style activation transplantation across 17 models, three families, and 64x sc...
  </details>

- **2026-07-06** — Wenqian Xing — [Attention Limited Reward Learning](http://arxiv.org/abs/2607.04590v1)
  <details><summary>📄 Abstract</summary>
  Pairwise human comparisons are a primary interface through which modern AI systems learn human preferences. RLHF and related alignment pipelines typically model such comparisons with Bradley--Terry log-odds, where choice probabilities are governed by latent reward differences. This paper examines what this assumption misses through a reduced-form model motivated by rational inattention, in which each label is generated by a low-capacity evaluation channel. The model separates two forms of ambigu...
  </details>

- **2026-07-06** — Wei Ao, Lan Wang, Vishnu Naresh Boddeti — [QSVideo: Query-Conditioned Semantic Temporal Retrieval for Video Understanding](http://arxiv.org/abs/2607.04559v1)
  <details><summary>📄 Abstract</summary>
  The performance of vision-language models (VLMs) in video understanding declines with increasing video duration, as video moments unrelated to the query confuse their language components. Multimodal retrieval has emerged as a critical component of video understanding, addressing this challenge by localizing key visual evidence. However, existing multimodal retrieval methods suffer from biased relevance estimation, limited diversity, and temporal collapse. In this paper, we propose QSVideo, a uni...
  </details>

- **2026-07-06** — Yu Li, Xiuyu Li, Mingyang Yi et al. — [Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment](http://arxiv.org/abs/2607.04728v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably results in off-policy training data. To resolve this, Importance sampling (IS) is proposed, while the token-level ratios compound over long sequences, causing severe variance exploded. A natural idea is "transferring" these off-policy token into on-policy token, so that the importance scores for correction are unnecessary. Following this idea, we prop...
  </details>

- **2026-07-06** — Qiang Liu, Taian Guo, Ruizhi Qiao et al. — [RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents](http://arxiv.org/abs/2607.04713v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Con...
  </details>

- **2026-07-05** — Yugwon Won — [MOSAIC: Interpretable Multi-Token Cross-Attention of Biophonetic and Self-Supervised Representations for Unified Voice Anti-Spoofing](http://arxiv.org/abs/2607.04314v1)
  <details><summary>📄 Abstract</summary>
  The dominant trend in voice anti-spoofing fuses self-supervised (SSL) backbones (e.g., WavLM) with handcrafted features, yet such fusion typically lacks transparency in cue-to-layer interactions, and simple concatenation limits cross-modal learning. We propose MOSAIC (Multi-token Oriented Speech Anti-spoofing via Integrated Cross-attention), an interpretable multi-token cross-attention framework that splits a 152-dimensional biophonetic feature vector into six semantic-group query tokens (Praat,...
  </details>

- **2026-07-05** — Prakhar Godara, Pang Shiang Tay, Marcelo G. Mattar — [Beyond DSA: Conjugacy-based Comparison of Dynamical Systems](http://arxiv.org/abs/2607.04493v1)
  <details><summary>📄 Abstract</summary>
  Comparing whether two dynamical systems implement the same computation despite differences in coordinates or measurements is a central problem in neuroscience and machine learning. Dynamical Similarity Analysis [DSA; Ostrow et al., 2023] addresses this problem by aligning finite-dimensional Koopman approximations through an orthogonal similarity transformation. Here we show that orthogonal alignment is neither necessary nor sufficient for topological conjugacy: conjugate systems may require a no...
  </details>

- **2026-07-05** — Kargi Chauhan, Aditya Shah — [Covert Trait Propagation Is Representation Alignment: Mechanistic Evidence from Hidden-Channel Distillation](http://arxiv.org/abs/2607.04432v1)
  <details><summary>📄 Abstract</summary>
  A student model trained on pure uniform noise can still inherit its teacher's digit-classification ability, provided the two share initialization. Previous work proves this transfer is guaranteed when the teacher's learning rate is small enough, but does not explain where in the network the channel lives or what sets its capacity. Working in an MLP distillation setting on MNIST, we show these channels are not purely informational: geometric alignment gates access to the information the channel c...
  </details>

- **2026-07-05** — Sijin Dong, Hiroyuki Shinnou — [Uncertainty-Aware Abstention in Large Language Models with Provable Alignment Guarantees](http://arxiv.org/abs/2607.04430v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly deployed in question answering (QA) systems, yet they may generate hallucinated or misaligned responses without reliable confidence estimates. Uncertainty quantification (UQ) offers a natural basis for selective answering, where a system answers only when its prediction is deemed reliable and abstains otherwise. However, existing uncertainty scores for LLMs are often heuristic: a threshold chosen on such scores does not, by itself, provide statistica...
  </details>

- **2026-07-05** — Dhyey Yajnik, Amina Asif, Fayyaz Minhas — [The Good, the Bad, and the Brittle: Benchmarking Robustness and Generalisation of Histopathology Foundation Models](http://arxiv.org/abs/2607.04401v1)
  <details><summary>📄 Abstract</summary>
  How robust and generalisable are pathology foundation models and have their scaling limites been reached? We benchmarked twelve pathology foundation models (PFMs) and ResNet baselines using our Robustness Evaluation and Enhancement Toolbox (REET) across eleven clinically realistic perturbations and a dissimilarity-driven Non-Redundant K-fold validation (NR-Kfold) protocol. We introduce a Perturbation Performance Index (PPI) to summarise accuracy trends under controlled perturbation sweeps and an...
  </details>

- **2026-07-05** — Yuhong Luo, David M. Pennock, Xintong Wang — [Decentralized Aggregation of LLM Predictions via Wagering Mechanisms](http://arxiv.org/abs/2607.04389v1)
  <details><summary>📄 Abstract</summary>
  It is increasingly common to aggregate predictions from multiple LLMs, each with domain expertise or access to private tools and data, to improve collective prediction performance. In decentralized settings, aggregation weights need to be determined without access to models' private information and should remain robust to strategic reporting. We propose a family of advantage-aligned wagering mechanisms for LLM aggregation (WALLA), in which each model reports a prediction and a learned wager, and...
  </details>

- **2026-07-05** — Zixiang Zhou, Zhentao Yu, Yifeng Ma et al. — [Aura: Consistent Multi-Subject Video Generation via VLM-Grounded Semantic Alignment](http://arxiv.org/abs/2607.04311v1)
  <details><summary>📄 Abstract</summary>
  Subject-driven and multi-element video generation are central to controllable video synthesis, but existing methods still struggle to preserve identity consistency and model complex relationships among multiple subjects. In this paper, we propose Aura, a unified framework for high-fidelity and identity-consistent video generation. To better capture scene dynamics and subject interactions, we introduce AI director-level captions that provide dense and structured descriptions of video content. We ...
  </details>

- **2026-07-05** — Omer Tariq, Syed Muhammad Raza, Jeongbae Son — [SAD-LoRA: Spectral Alignment for Low-Rank Knowledge Distillation](http://arxiv.org/abs/2607.04306v1)
  <details><summary>📄 Abstract</summary>
  Distilling a fine-tuned teacher into a LoRA-adapted student is a standard recipe for parameter-efficient compression, but output-level KD does not explicitly control which rank-$r$ weight subspace the adapter occupies. We propose \textbf{SAD-LoRA} (\textbf{S}pectral \textbf{A}lignment \textbf{D}istillation), which selects this subspace from the data-weighted student-space reference update $\DWT\Sigx^{1/2}$ and maintains it during training via a differentiable principal-angle loss on $\colspan(B)...
  </details>

- **2026-07-05** — Gerasimos Papanikolaou-Ntais, Alexandros Kaloxylos, Athanasios Kanavos — [Agentic-V2X: Small Language Model Agents for Deadline-Aware V2X Scheduling in 5G/6G Networks](http://arxiv.org/abs/2607.04290v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are proposed as control interfaces for next-generation networks, but their latency, hallucinations, and lack of control guarantees make them unsuitable for near-real-time packet schedulers, especially in dynamic V2X environments. This paper introduces Agentic-V2X, an architecture where a small, locally deployed language model acts as a periodic non-real-time rApp-inspired policy creator, while a lightweight xApp-like controller executes validated policies at interval...
  </details>

- **2026-07-05** — Malak Ait Tamlihat, Ghizlane Ez-Zobayr, Laurent Schoeffel et al. — [Relativistic Hydrodynamics and Vorticity Dynamics in High-Energy Heavy-Ion Collisions: A Collective Flow Perspective](http://arxiv.org/abs/2607.04273v1)
  <details><summary>📄 Abstract</summary>
  This article provides a comprehensive overview of the application of relativistic fluid mechanics to describe the collective evolution of the Quark-Gluon Plasma (QGP) formed in ultra-relativistic heavy-ion collisions. We map out the chronological transformation of spatial eccentricities in the initial interaction volume into measurable anisotropic azimuthal momentum distributions, parameterized by the harmonic flow coefficients $v_n$. Utilizing multi-particle correlation techniques developed wit...
  </details>

- **2026-07-05** — Weihao Yan, Yeqiang Qian, Yi Dong et al. — [Beyond Random Sampling: Distribution-Aware Alignment for Semi-Supervised Medical Image Segmentation](http://arxiv.org/abs/2607.04249v1)
  <details><summary>📄 Abstract</summary>
  Precise medical image segmentation is crucial for clinical diagnosis and treatment planning, yet relies heavily on expensive expert annotations. Semi-supervised medical image segmentation (SSMIS) offers a cost-effective solution but typically operates under the assumption of independent and identically distributed (i.i.d.) data, defaulting to random sampling. While statistically valid at scale, this strategy suffers from severe representation bias in low-data regimes, failing to capture the hete...
  </details>

- **2026-07-05** — Waikit Xiu, Qiang Lu, Zian Wang et al. — [Beyond Scene Priors: Fine-Grained Traffic Scene Reasoning with Benchmarking and Query-Guided Small-Object Focus](http://arxiv.org/abs/2607.04149v1)
  <details><summary>📄 Abstract</summary>
  In safety-critical traffic scenarios, answering complex questions relies on minute, localized visual cues. However, standard Multimodal Large Language Models (MLLMs) tend to over-attend to backgrounds, overwhelming crucial small objects during visual-language alignment, a failure mode we term 'critical evidence dilution.' Furthermore, existing visual question answering (VQA) datasets rarely expose this flaw, as they lack large-scale, distractor-heavy evaluations that require pinpointing local ev...
  </details>

- **2026-07-05** — Junwon Moon, Seungbeom Kim, Yejin Lee et al. — [DELTA-TTS: Adapting Autoregressive Model into Diffusion Language Model for Text-to-Speech](http://arxiv.org/abs/2607.04140v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive (AR) text-to-speech (TTS) models generate discrete speech tokens sequentially, which makes inference slow and can degrade robustness by propagating local errors and hallucinations. This limitation stems from their left-to-right AR commitment: each token must be determined before future speech-token context is available. However, such ordering is not an inherent requirement for TTS, as the full input text is available before synthesis. In this paper, we introduce DELTA-TTS, a light...
  </details>

- **2026-07-05** — Zhaopeng Feng, Chen Zhi, Xuhong Zhang et al. — [SOV-CAD: Stepwise Orthographic Views Guided CAD Modeling Sequence Reconstruction](http://arxiv.org/abs/2607.04119v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing Computer-Aided Design (CAD) modeling sequences from images is crucial for preserving design intent and supporting parametric editing. However, existing methods typically generate full CAD sequences holistically, overlooking the iterative, feedback-driven nature of human design workflows. We address this limitation by introducing the rich stepwise visual supervision: at each modeling step, the system observes the target's orthographic projections, the projections of the incremental...
  </details>

- **2026-07-05** — Mohammad Arif Rasyidi, Syahirul Faiz — [Benchmarking API Drift in LLM-Generated Quantum Code Across Successive SDK Versions](http://arxiv.org/abs/2607.04072v1)
  <details><summary>📄 Abstract</summary>
  Large language models can generate plausible quantum code, but it is unclear whether they can reliably target the specific software development kit (SDK) version requested by the user. We study this problem as API drift and introduce quantum-api-drift, a benchmark for measuring version fidelity, defined here as execution success on the requested SDK version, cross-version compatibility, failure modes, and documentation-guided repair in LLM-generated quantum SDK code. We instantiate the benchmark...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 64 papers

- **2026-07-08** — Ishaan Batta, Meenu Ajith, Vince Calhoun — [Latent graph encoding of multimodal neuroimaging features with generative AI architectures](http://arxiv.org/abs/2607.07027v1)
  <details><summary>📄 Abstract</summary>
  While generative models enable encoding of complex neuroimaging data for feature generation and reconstruction, developing optimal architectural frameworks with appropriate encoding and latent space processes is crucial for studying structural and functional properties of the brain. We design a multimodal generative framework for structural and functional magnetic resonance imaging (MRI) features through systematic evaluation of encoding strategies, latent multimodal fusion, and generative model...
  </details>

- **2026-07-08** — Lipu Zhou, Yaoyun Kang, Junxiang Pang et al. — [GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM](http://arxiv.org/abs/2607.07452v1)
  <details><summary>📄 Abstract</summary>
  Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feas...
  </details>

- **2026-07-08** — Jinbo Yang, Mingyue Yuan, Boyuan Zhang et al. — [HPG-Diff: Hierarchical physics-guided diffusion with differentiable connectivity constraints for topology optimization](http://arxiv.org/abs/2607.07233v1)
  <details><summary>📄 Abstract</summary>
  Deep generative models offer a promising paradigm for topology optimization, enabling rapid design exploration. However, these approaches lack intrinsic physics guidance, often leading to poor generalizability across unseen boundary conditions and the formation of floating material artifacts. To address these limitations, we propose Hierarchical Physics-Guided Diffusion (HPG-Diff), a novel diffusion framework that enforces physics consistency through two synergistic mechanisms. First, we introdu...
  </details>

- **2026-07-08** — Shivendra G. Tewari, Holly Kimko — [A hierarchical memory architecture overcomes context limits in long-horizon multi-agent computational modeling](http://arxiv.org/abs/2607.07666v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) demonstrate remarkable reasoning capabilities, yet their stateless architecture fundamentally limits deployment in long-horizon research workflows requiring multi-session continuity and quantitative rigor. Here we present Ensemble QSP, a multi-agent framework featuring a three-layer hierarchical memory architecture that keeps injected context bounded and constant in project duration (mid-term project state: median 301 tokens, max 4,050, across 104 runs) by capping ea...
  </details>

- **2026-07-08** — Timur Khudaiberganov — [Geometric Interpretation of Sum Photon Blockade](http://arxiv.org/abs/2607.07591v1)
  <details><summary>📄 Abstract</summary>
  We present a geometric interpretation of the sum photon blockade effect in multimode quantum optical systems, such as semiconductor microresonators. The blockade condition \(c^{(n)} \cdot v = 0\) reflects the orthogonality of the \(n\)-photon amplitude vector to a target mode vector in an \(N\)-dimensional Hilbert space, visualized as the confinement of the state to a hyperplane.   A key result is the calculation of the maximum probability of the system remaining in the blockade subspace under t...
  </details>

- **2026-07-08** — Jorge Pueyo, Daniel Camps-Mur and, Miguel Catalan-Cid — [PHaul: A PPO-based forwarding agent for Sub6 enhanced Integrated Access and Backhaul networks](http://arxiv.org/abs/2607.07584v1)
  <details><summary>📄 Abstract</summary>
  3GPP Integrated Access and Backhaul (IAB) allows operators to deploy outdoor mm-wave access networks in a cost-efficient manner, by reusing the same spectrum in access and backhaul. In IAB networks the performance bottleneck is the wireless backhaul segment, where efficient forwarding strategies are needed to effectively use the available capacity. In addition, the performance of the mm-wave IAB backhaul segment is contingent on the availability of line of sight (LoS) conditions in the selected ...
  </details>

- **2026-07-08** — Feng He, Zhenting Wang, Qifan Wang et al. — [HIVE: Understanding Post-Hallucination Reasoning in Vision Language Models](http://arxiv.org/abs/2607.07507v1)
  <details><summary>📄 Abstract</summary>
  Hallucinations in vision language models (VLMs) are commonly treated as semantic errors, yet they often arise from partial or ambiguous visual evidence. Prior work mainly focuses on detecting or suppressing hallucinations at generation time, leaving the subsequent reasoning stage largely unexplored. In this work, we study Post Hallucination Reasoning (PHR), the stage in which hallucinated semantics enter the model's inference context and influence downstream predictions. To systematically invest...
  </details>

- **2026-07-08** — Ahan Basu, Ratnangshu Das, Soumyodipta Nath et al. — [Learning Spatiotemporal Tubes for Full Class of Signal Temporal Logic Tasks for Control of Unknown Systems under Input Constraints](http://arxiv.org/abs/2607.07136v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a Spatiotemporal Tube (STT)-based control framework for general unknown nonlinear Euler-Lagrange (EL) systems subject to input constraints, with the objective of satisfying Signal Temporal Logic (STL) specifications, where confinement of the system trajectory within the STT guarantees the satisfaction of the corresponding STL task. For both single and multi-agent scenarios, the STT corresponding to each agent is modeled as a time-varying ball, whose center and radius are join...
  </details>

- **2026-07-08** — Hao Cong, Huizu Lin, Zihan Wang et al. — [Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation](http://arxiv.org/abs/2607.07108v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based agentic recommender systems show promise in modeling user preferences through natural-language reasoning, yet they remain limited by text-centric inputs and coarse-grained memory updates, making agents prone to missing visual evidence, semantic noise, and preference drift. To address these limitations, we propose MMEACR, a Multimodal Memory-Enhanced Agent Collaboration framework for recommendation. MMEACR introduces a dual-track memory architecture that separates...
  </details>

- **2026-07-08** — Jiang Zhang, Yan-dong Chen — [KAN-LSTM-Transformer Neural Networks, MFV and Cosmological Parameters](http://arxiv.org/abs/2607.06959v1)
  <details><summary>📄 Abstract</summary>
  Reconstructing the cosmic distance ladder directly from observations is a crucial issue in cosmology. In this paper, we present a novel method for modeling the cosmic distance ladder and estimating cosmological parameters through the use of Kolmogorov-Arnold networks (KAN), Long Short-Term Memory (LSTM), and Transformer networks (collectively referred to as KLT-Net), based on the apparent magnitude data from the Pantheon SN Ia compilation. As a data-driven, non-parametric method for reconstructi...
  </details>

- **2026-07-08** — Chenchuhui Hu, Shaoming Pan, Leon Axel et al. — [Bi-PT: Bidirectional Cross-Attention Point Transformers for Four-Chamber Heart Reconstruction from Sparse Cardiac MRI Data](http://arxiv.org/abs/2607.06923v1)
  <details><summary>📄 Abstract</summary>
  We propose Bi-PT, a pipeline for reconstructing 3D four-chamber human heart meshes from clinical sparsely sampled cardiac magnetic resonance imaging (CMR) data. This work addresses the error-prone generation of 3D cardiac shape from a sparse point cloud (SPC) extracted from 2D long-axis and short-axis views used in routine clinical CMR protocols. Bi-PT enables accurate inference of the four-chamber heart mesh from the SPC by learning robust point features via bidirectional point cross-attention ...
  </details>

- **2026-07-08** — Chuqing Zhao, Haochen Yang — [Evaluating LLM Robustness Under Domain-Specific Prompt Perturbations in Public Health Applications](http://arxiv.org/abs/2607.06913v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly applied in public health applications, yet their robustness to non-clinical user inputs remains underexplored. We propose a domain specific robustness benchmark that evaluates LLMs under two perturbation types that commonly arise when non-clinical users interact with health AI systems: misinformation framing (MF), where prompt might be injected by false health claims, and layperson rewriting (LR), where patients describe symptoms in everyday language...
  </details>

- **2026-07-07** — Jinhong Deng, Limeng Qiao, Guanglu Wan — [HoloCount: A Holistic Visual Counting Benchmark for MLLMs](http://arxiv.org/abs/2607.06420v1)
  <details><summary>📄 Abstract</summary>
  Visual counting is a fundamental pillar of multimodal intelligence, requiring a seamless integration of fine-grained grounding and spatial reasoning. While Multimodal Large Language Models (MLLMs) have achieved remarkable success in qualitative scene understanding, their quantitative precision remains a significant bottleneck, often characterized by persistent numerical hallucinations. Existing counting benchmarks primarily focus on basic perception in simplified contexts, failing to capture the...
  </details>

- **2026-07-07** — Wael Albayaydh, Rui Zhao, Ivan Flechais — [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and Reasoning Failures in Large Language Model Agents](http://arxiv.org/abs/2607.05775v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents are increasingly evaluated on their ability to use tools, plan multi-step tasks, coordinate with other agents, and operate over extended horizons. Reported benchmark gains often obscure recurring failure modes documented across otherwise unrelated evaluation efforts. This paper synthesizes 27 benchmark, taxonomy, and audit papers (2023-2026), spanning 19 distinct benchmarks, into a cross-cutting taxonomy of agent limitations. To our knowledge, this is the first ...
  </details>

- **2026-07-07** — Nima Kelidari, Mohammadsaeed Haghi, Mahdi Salmani — [A Gold-Standard Study of What Makes a Lightweight Game-Playing Agent Strong](http://arxiv.org/abs/2607.06854v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning agents for imperfect-information card games are only as strong as the opponents they train against, and they are hard to grade, since they beat a random opponent over 99 percent of the time and only tie copies of themselves. So we build a strong, fixed, rule-based expert for Gin Rummy and use it only as a yardstick, never for training. It beats every agent we trained 70 to 99 percent of the time. Across more than a hundred runs, we isolate what makes a lightweight agent st...
  </details>

- **2026-07-07** — Razvan Mihai Popescu — [Reliable and Developer-Aligned Evaluation of Agents for Software Engineering](http://arxiv.org/abs/2607.06713v1)
  <details><summary>📄 Abstract</summary>
  Large language models are rapidly moving towards closing the development cycle, transitioning from simple assistive companions to autonomous contributors deeply embedded into collaborative development environments. Despite their accelerated adoption, existing evaluation techniques are limited due to their fragmented nature and distorted projection of true model capabilities, often obtained from hypothetical syntactic scenarios. This research aims to bridge this gap by providing a comprehensive e...
  </details>

- **2026-07-07** — Ke Rui, Yushen Zuo, Jiawei Wang et al. — [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](http://arxiv.org/abs/2607.06256v1)
  <details><summary>📄 Abstract</summary>
  Long-horizon household tasks require robots to compose many language-conditioned skills, yet the boundary between consecutive skills is rarely explicit. A skill may satisfy its own postcondition while leaving the robot, objects, or camera views in a state from which the next skill cannot reliably start. We study this semantic handoff problem in BEHAVIOR-1K through an agent-orchestrated vision-language-action execution harness. The harness invokes $π_{0.5}$-based skill checkpoints trained from cl...
  </details>

- **2026-07-07** — Chenhao Yuan, Yinhao Xu, Shuwen Xu et al. — [LongCrafter: Towards Diverse Long-Context Understanding via Evidence-Graph-Guided Instruction Synthesis](http://arxiv.org/abs/2607.06160v1)
  <details><summary>📄 Abstract</summary>
  Synthesizing long-context supervised fine-tuning (SFT) data is a scalable way to enhance the long-context understanding of large language models (LLMs), yet existing approaches share three limitations: narrow task coverage, insufficient instruction difficulty, and a lack of faithfulness supervision. We propose \textbf{LongCrafter}, a structured synthesis framework that couples a hierarchical task taxonomy with an evidence-grounded pipeline. The taxonomy organizes long-context understanding into ...
  </details>

- **2026-07-07** — Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao et al. — [Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from Verifiable Rewards for LLM Negotiations](http://arxiv.org/abs/2607.05863v1)
  <details><summary>📄 Abstract</summary>
  Negotiation is a fundamental strategic interaction in management science, characterized by agents attempting to reach agreements while protecting private information, such as reservation costs and hidden valuations. A prevalent yet complex scenario involves a single seller negotiating concurrently with multiple buyers, each possessing heterogeneous, private budgets. In such settings, constrained by a limited number of communication turns, the seller must balance exploring the broader market to d...
  </details>

- **2026-07-07** — Yueke Zhang, Yifan Zhang, Zihan Fang et al. — [SCOPE: Leveraging Subgoal Critiques for Code Generation](http://arxiv.org/abs/2607.05810v1)
  <details><summary>📄 Abstract</summary>
  Code generation with large language models (LLMs) remains unreliable because generated programs can appear correct while still violating key semantic requirements in the natural language specification. Existing feedback-based methods improve over coder-only generation, but they often rely on unstructured critique or execution signals that do not explicitly identify what the code is semantically missing. We present SCOPE, a prover-initialized subgoal critic for code generation. SCOPE adapts a Lea...
  </details>

- **2026-07-07** — Bhavya Sai Nukapotula, Samin Moosavi, Haoze Wang et al. — [EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees](http://arxiv.org/abs/2607.06724v1)
  <details><summary>📄 Abstract</summary>
  LLM-based robot planners are fluent but cannot guarantee that their plans are executable or safe. Classical PDDL planners can guarantee these properties, but only after the problem is fully specified, and they make poor use of an LLM's ability to read context and repair plans. This paper presents a neuro-symbolic framework with three parts. All LLM calls use a locally-hosted open-weight model, so the pipeline can be deployed on-robot with no cloud dependency. First, an offline procedure that min...
  </details>

- **2026-07-07** — Yotam Wolf, Noam Wies, Amnon Shashua — [When Does In-Context Search Help? A Sampling-Complexity Theory of Reflection-Driven Reasoning](http://arxiv.org/abs/2607.06720v1)
  <details><summary>📄 Abstract</summary>
  Training large language models (LLMs) with extended reasoning has enabled in-context search, in which models iteratively generate, critique, and revise solution attempts. We provide a theoretical analysis of in-context search by modeling it as approximate inference over reasoning traces, where the base model defines a prior and self-reflection provides feedback for posterior updates, and study the resulting inference-time sampling complexity - the number of sequential attempts needed to achieve ...
  </details>

- **2026-07-07** — Aparna Madva, Sharath Srivatsa, Srinath Srinivasa et al. — [Rethinking Indic AI from a Lens of Cultural Heritage Preservation](http://arxiv.org/abs/2607.06544v1)
  <details><summary>📄 Abstract</summary>
  As Artificial Intelligence (AI) makes inroads into different parts of the Indian subcontinent, there is significant interest in studying how AI impacts the linguistic and cultural foundations of this civilization. AI is seen as a ''double-edged sword'' where on the one hand, it can enable access and inclusion for a large population, on the other, it can homogenize worldviews and exclude underrepresented languages and worldviews. In this paper, we try to characterize this problem by addressing th...
  </details>

- **2026-07-07** — Matthieu Ospici, Arnaud Gueze, Luc Bourrat et al. — [Mitigating Domain Shift in Conditioned Floor Plan Generation: Synthetic Pre-training for Data-Efficient Adaptation](http://arxiv.org/abs/2607.06483v1)
  <details><summary>📄 Abstract</summary>
  Robustness to domain shift is a key requirement for floor plan generative models to be applicable beyond the single dataset they were trained on, as floor plans vary widely across regions due to distinct architectural cultures, spatial constraints, and construction practices, while acquiring new annotated datasets remains costly and domain-specific. Yet, no prior work has studied this robustness in the context of conditioned floor plan generation. In this paper, we evaluate state-of-the-art mode...
  </details>

- **2026-07-07** — Taeyun Roh, Eunha Lee, Wonjune Jang et al. — [From Voting to Agent Collaboration: Answer-Type-Aware LLM Pipelines for BioASQ 14b](http://arxiv.org/abs/2607.06452v1)
  <details><summary>📄 Abstract</summary>
  Biomedical question answering requires not only accurate extraction of information from scientific literature but also reliable integration of evidence across multiple documents. This study presents a question-type-specific large language model (LLM) framework for BioASQ 14b Task B, designed to improve answer robustness and evidence grounding in biomedical question answering. Rather than applying a single prompting strategy to all questions, the framework selects different inference procedures f...
  </details>

- **2026-07-07** — Sofiane Daimellah, Sylvie Le Hégarat-Mascle, Clotilde Boust — [XRFormer: Multiscale Tokenization for XRF Representation Learning](http://arxiv.org/abs/2607.06424v1)
  <details><summary>📄 Abstract</summary>
  X-ray fluorescence (XRF) spectroscopy is a key modality for material analysis in cultural heritage. However, automated learning from XRF spectra remains challenging: XRF spectra are complex one-dimensional signals composed of sharp elemental peaks, broader structures, and background variations that are not taken into account by existing learning-based models. This paper introduces XRFormer, a transformer architecture tailored to XRF spectra through a multiscale convolutional tokenizer that injec...
  </details>

- **2026-07-07** — Jiazi Wang, Nonghai Zhang, Qiushi Xie et al. — [VaseMuseum: Digital Intelligent Museum for Ancient Greek Pottery](http://arxiv.org/abs/2607.06374v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) have made interactive digital museums increasingly feasible by connecting 3D digitization with natural-language artifact exploration. However, in cultural heritage domains such as ancient Greek pottery, reliable VLM assistance is limited by two challenges. First, open-ended interpretation requires grounding fine-grained 2D/3D visual evidence in specialized curatorial knowledge, yet the retrieval process may introduce weak sources and unverifiable references. Second,...
  </details>

- **2026-07-07** — Kaibo Zhang, Ji Wu, Chao Zhang et al. — [Quantifying Entrainment Evidence: A Comparison of Frequentist and Bayesian Approaches for Information Processing Pathway Maps](http://arxiv.org/abs/2607.06284v1)
  <details><summary>📄 Abstract</summary>
  Information Processing Pathway Maps (IPPMs) offer a scalable framework for formalizing the complex sequence of mathematical transformations applied to sensory stimuli. These maps chart the latency and cortical expression of computational steps, relying on statistical inference to link model outputs with observed neural activity. Traditionally, this mapping has relied on frequentist hypothesis testing. However, determining which of several competing computational models best explains neural data ...
  </details>

- **2026-07-07** — Shuheng Zhang, Feng Wu — [NegROI: Click-Centric Uncertainty-Guided Refinement with Scene-Conditioned Negative Prompts for Robust Interactive 3D Segmentation](http://arxiv.org/abs/2607.05955v1)
  <details><summary>📄 Abstract</summary>
  Interactive 3D segmentation aims to extract object masks in point clouds with minimal user clicks. Despite recent progress, most existing approaches still struggle with (i) coarse voxel resolution that blurs fine boundaries under limited clicks and (ii) hard false positives caused by confusing background structures. These issues are exacerbated by density and scale shifts across datasets (e.g., dense RGB-D reconstructions vs. sparse LiDAR scans), where fixed refinement heuristics and purely clic...
  </details>

- **2026-07-07** — Timothée Gavin, Murat Bronz — [Intercepting an Agile Target with Net-Carrying Drones using Competitive Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2607.05939v1)
  <details><summary>📄 Abstract</summary>
  This article presents a solution to intercept an agile drone by a team of agile drone carrying catching nets. We formulate the problem as a competitive Multi-Agent Reinforcement Learning (MARL) task. To address the problem of nonstationarity and catastrophic forgetting of agents overfitting to the current opponent strategy, we train the pursuers and the evader using Multi-Agent Proximal Policy Optimization (MAPPO) with Prioritized Fictitious Self Play (PFSP). We train the agents in a high-fideli...
  </details>

- **2026-07-07** — Yaovi Armand Amouzou-adoun, Lionel Gélébart, Cédric Flageul et al. — [A robust and versatile parallel FFT-based mechanical solver for general non-periodic and periodic boundary conditions](http://arxiv.org/abs/2607.05929v1)
  <details><summary>📄 Abstract</summary>
  General boundary conditions are implemented within a fast Fourier transform framework for linear and non-linear mechanical problems using small or finite transformation formulations. In the context of parallel computing (distributed memory), we present a framework that enables the combination of periodic and non-periodic (Dirichlet or Neumann) boundary conditions. Taking advantage of the link between non-periodic boundary conditions and the symmetries of the relevant components of the fluctuatio...
  </details>

- **2026-07-07** — Kaishen Wang, Tong Zheng, Xuehao Cui et al. — [Mitigating Factual Hallucination in Large Reasoning Models via Mixed-Mode Advantage Regularization](http://arxiv.org/abs/2607.05861v1)
  <details><summary>📄 Abstract</summary>
  Large reasoning models (LRMs) improve language model capabilities by generating explicit thinking traces before final answers. In factuality-oriented question answering (QA), such thinking often improves overall performance by helping the model recover relevant knowledge and refine its answers. However, we find that this benefit is not uniform at the instance level: explicit thinking can also overturn correct non-thinking answers and lead to factual drift. We refer to this failure mode as \emph{...
  </details>

- **2026-07-07** — Muhammadjon Tursunbadalov, Mustafojon Tursunbadalov — [A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It](http://arxiv.org/abs/2607.06605v1)
  <details><summary>📄 Abstract</summary>
  Conformal prediction is being adopted in drug discovery to put an honest number on model reliability: pick an error rate alpha, and the method returns prediction sets containing the true label with probability at least 1 - alpha. We show this guarantee can be dangerous on imbalanced datasets. Across four datasets, standard (marginal) conformal prediction hits its global 90% coverage target while leaving the minority class badly exposed: realized minority coverage falls to 64.8% on blood-brain-ba...
  </details>

- **2026-07-07** — Mooho Song, Jay-Yoon Lee — [Retrieving a Set, Not Independent Passages: Set-Level Compatibility Learning for Efficient Set Exploration](http://arxiv.org/abs/2607.05712v1)
  <details><summary>📄 Abstract</summary>
  Multi-hop question answering and retrieval-augmented reasoning require selecting evidence passages that are jointly useful for answering a query. However, most retrievers still score passages independently or make locally supervised sequential decisions, which can fail when evidence usefulness depends on compatibility among passages. LLM-based set selection can model such interactions, but its computational cost limits practical use. We address this gap by formulating multi-hop retrieval as quer...
  </details>

- **2026-07-06** — Calvin A. Riiska, Michelle Lee, Yonatan Nemenman et al. — [Redundant contacts and force redistribution stabilize limbless vertical climbing](http://arxiv.org/abs/2607.06239v1)
  <details><summary>📄 Abstract</summary>
  Animals navigating complex vertical environments must secure stable footholds, a challenge for species without feet. While arboreal climbing has evolved repeatedly in snakes, the physical mechanisms they use to scale broad, nearly flat surfaces remain poorly understood. By measuring three-dimensional body kinematics and per-contact forces on a smooth vertical wall with protruding posts, we show that cornsnakes climb by dynamically balancing forces across a highly redundant network of 5 to 16 sim...
  </details>

- **2026-07-06** — Kenneth Benavides, Josh Fleischer, Danti Chen — [EvalLoop: A Methodology for Evaluation-Driven Iterative Improvement of Business AI Systems](http://arxiv.org/abs/2607.05638v1)
  <details><summary>📄 Abstract</summary>
  Teams deploying large language models in business contexts need evaluation systems, yet most treat evaluation as static model selection: run benchmarks, rank models, deploy the winner. This framing misses evaluation's primary value for production systems--diagnosing why a system underperforms and guiding what to fix. We present EvalLoop, a methodology for evaluation-driven iterative improvement. EvalLoop organizes evaluation around three mechanisms: (1) dimensional metric grouping that decompose...
  </details>

- **2026-07-06** — Sadia Kamal, Arefa Patwary, Anthony Marchiafava et al. — [Prompt Robustness Is Task-Dependent: Comparing Objective and Belief-Style Questions in LLM Evaluation](http://arxiv.org/abs/2607.05554v1)
  <details><summary>📄 Abstract</summary>
  Survey-style evaluations of large language models often treat a prompted response as a measure of a model's values or beliefs. This assumption is particularly fragile when responses are read as evidence of political values, social attitudes, or beliefs. We ask whether prompt robustness differs between objective questions with fixed answers and subjective questions that ask for opinions or values. We evaluate four instruction-tuned model families on three objective datasets (MMLU, ARC, and Cultur...
  </details>

- **2026-07-06** — Karim Benakli, Anna Chrysostomou — [The Fate of Black Hole-Induced Moduli Excursions in the Presence of Scalar Potentials](http://arxiv.org/abs/2607.05488v1)
  <details><summary>📄 Abstract</summary>
  Large charged black holes can create macroscopic, locally weakly curved regions in which moduli take values different from their asymptotic values. We study how robust this mechanism is once the scalar has a nontrivial potential. In four-dimensional Einstein-Maxwell-dilaton theory, the massless GHS solution provides a finite exterior throat in which the scalar and the gauge coupling vary logarithmically. We develop fixed-throat diagnostics for the competition between the black hole gauge source ...
  </details>

- **2026-07-06** — Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. — [Multiplayer Interactive World Models with Representation Autoencoders](http://arxiv.org/abs/2607.05352v2)
  <details><summary>📄 Abstract</summary>
  We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...
  </details>

- **2026-07-06** — Suryanarayana Reddy Yarrabothula, Manisha Chawla, Kunal Sinha et al. — [SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments](http://arxiv.org/abs/2607.05264v1)
  <details><summary>📄 Abstract</summary>
  Existing video benchmarks evaluate action recognition on consumer videos, egocentric recordings, or simulated industrial environments. They do not test vision-language models under the visual and procedural conditions of real industrial CCTV, where workers appear as distant figures amid dust, steam, low light, glare, occlusion, and overlapping activities. We introduce STEELBENCH, a diagnostic benchmark for industrial surveillance that jointly evaluates per-worker activity recognition, safety-rul...
  </details>

- **2026-07-06** — Sebastian A. Bruijns, Jirko Rubruck, Mia H. Whitefield et al. — [Pretraining Curricula Enable Selective Fine-tuning](http://arxiv.org/abs/2607.04846v1)
  <details><summary>📄 Abstract</summary>
  Transformers follow implicit curricula whereby some tasks are learned before others. However, how explicit pretraining curricula influence learning, generalization, and the selectivity of fine-tuning is unclear. This is important for AI safety, where fine-tuning is used to selectively suppress misaligned behaviors. Here, we compare curricula that pretrain tasks in a balanced (sampled uniformly) or an imbalanced (one task early, the other late) fashion. We show that imbalanced learning of two con...
  </details>

- **2026-07-06** — Sokipriala Jonah — [LLMs for Agentic Home Energy Management](http://arxiv.org/abs/2607.04569v1)
  <details><summary>📄 Abstract</summary>
  Home Energy Management Systems (HEMS) can reduce residential electricity costs and support demand response, but adoption is limited by the difficulty of translating household preferences into technical scheduling constraints. This paper evaluates whether large language model (LLM) agents can provide a practical natural-language interface for multi-appliance home energy scheduling. We present a tool-calling ReAct agent that uses live half-hourly Octopus Agile prices, weather forecasts, photovolta...
  </details>

- **2026-07-06** — Wenhao Li, Xueying Jiang, Quanhao Qian et al. — [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](http://arxiv.org/abs/2607.05396v1)
  <details><summary>📄 Abstract</summary>
  Real-world robot deployment rarely maintains the training-stage camera setup, where cameras often experience repositioning or remounting depending on actual scenarios. Existing view-robust Vision-Language-Action (VLA) policies tolerate such camera variations only when the camera extrinsics are explicitly provided, making them fragile and hard to use especially when view robustness is critical. We argue that the policy should not be told where the camera is, but rather figure it out by itself. To...
  </details>

- **2026-07-06** — Zhe Zhao, Zhibin Li, Yilin Ou et al. — [Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation](http://arxiv.org/abs/2607.04940v1)
  <details><summary>📄 Abstract</summary>
  Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simula...
  </details>

- **2026-07-06** — Yunchao Zhang, Yijia Weng, Ruizhe Liu et al. — [Geometry-Aware Motion Latents for Learning Robust Manipulation Policies](http://arxiv.org/abs/2607.04714v1)
  <details><summary>📄 Abstract</summary>
  Learning motion latents for robotic manipulation heavily relies on extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional objective -- spatial geometry changing through time ...
  </details>

- **2026-07-06** — Veeramanohar Avudaiappan, Ritwik Murali — [StructuredEdit: Constraint-Aware Graphic Design Editing via Differentiable Parameter Propagation](http://arxiv.org/abs/2607.04612v1)
  <details><summary>📄 Abstract</summary>
  Graphic design editing requires precise manipulation of typography, layout, and visual hierarchy under strict design constraints. Following the introduction of large language models, organizations have increasingly promoted vision-language models to enhance productivity. However, current models operate on pixels and achieve only 52% constraint satisfaction on structured design edits, thereby limiting their reliability for professional workflows. We present StructuredEdit, a pipeline that reframe...
  </details>

- **2026-07-06** — Kaiyuan Chen, Shuangyu Xie, Letian Fu et al. — [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](http://arxiv.org/abs/2607.05369v1)
  <details><summary>📄 Abstract</summary>
  For robots to work reliably in commercial and industrial applications, can recent advances in agentic coding systems combine interpretable robot programming with the open-world adaptability of model-free policies? We focus on "Variational Automation" (VA), a class of tasks that have larger variations in object geometry and pose than fixed automation. Model-free policies often struggle to close the reliability gap for VA tasks, which must be executed persistently and reliably in commercial and in...
  </details>

- **2026-07-06** — Thomas Thebaud, Yuzhe Wang, Hao Zhang et al. — [SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](http://arxiv.org/abs/2607.05365v1)
  <details><summary>📄 Abstract</summary>
  Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-a...
  </details>

- **2026-07-06** — Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary et al. — [Multiplayer Interactive World Models with Representation Autoencoders](http://arxiv.org/abs/2607.05352v1)
  <details><summary>📄 Abstract</summary>
  We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, t...
  </details>

- **2026-07-06** — Vishal Asnani, Shruti Agarwal, John Collomosse — [FlowMark: Mask-Guided Video Watermarking](http://arxiv.org/abs/2607.05261v1)
  <details><summary>📄 Abstract</summary>
  We present FlowMark, a video watermarking framework guided by automatically predicted object masks. In contrast to prior region-based approaches that require user-supplied mask guidance, FlowMark learns to identify optimal regions for watermark embedding through a dedicated Mask Predictor network. Our end-to-end trainable architecture combines region-aware encoding with noise-augmented training to ensure robustness against compression, geometric transformations, and content variation, while pres...
  </details>

- **2026-07-06** — Ning Zhang, Wenjian Liu — [cQED-iCIPT2: A Near-Exact Method for Polaritonic Chemistry](http://arxiv.org/abs/2607.05192v1)
  <details><summary>📄 Abstract</summary>
  Strong light-matter coupling in optical cavities provides a versatile platform for modulating chemical structure, reactivity, and spectroscopy, and hence motivates the development of ab initio cavity quantum electrodynamics (cQED) methods that can treat the electronic and photonic degrees of freedom on an equal footing. We present such a method, cQED-iCIPT2, by combining the near-exact iCIPT2 (iterative configuration interaction with selection and second-order perturbation theory) with the cQED ...
  </details>

- **2026-07-06** — Zhiheng Xi, Dingwen Yang, Jiaqi Liu et al. — [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](http://arxiv.org/abs/2607.05174v1)
  <details><summary>📄 Abstract</summary>
  Language agents, i.e., LLM agents, progress rapidly and are increasingly deployed in production environments. This trend underscores the urgent need for rigorous and realistic evaluations. However, most existing benchmarks evaluate agents in simplified, idealized settings. They typically rely on pre-packaged tool interfaces, overlook critical steps, and assume inputs are clean and fully specified. Consequently, they understate the difficulty of real deployments, where uncertainty and noise are u...
  </details>

- **2026-07-06** — Rang Liu, Ming Li, A. Lee Swindlehurst et al. — [Multiuser MIMO-AFDM Beamforming for ISAC in Doubly Dispersive Channels](http://arxiv.org/abs/2607.05119v1)
  <details><summary>📄 Abstract</summary>
  Integrated sensing and communication (ISAC) in high-mobility channels requires waveform and beamforming designs that are robust to delay-Doppler dispersion. With this in mind, in this paper we study a monostatic multiuser multiple-input multiple-output (MIMO) affine frequency division multiplexing (AFDM) downlink system. We develop a discrete affine Fourier transform (DAFT)-domain model that preserves Doppler-induced inter-bin coupling and derive a data-aided delay-Doppler detector. The expected...
  </details>

- **2026-07-06** — Tadashi Tsuyuki, Shunji Kotsuki — [A Mutual Information-Based Ensemble Kalman Filter](http://arxiv.org/abs/2607.05030v1)
  <details><summary>📄 Abstract</summary>
  Ensemble Kalman filters (EnKFs) are widely used for data assimilation in geophysical systems. Among various implementations, the local ensemble transform Kalman filter (LETKF) has gained popularity because of its computational efficiency. However, the deterministic EnKF such as the LETKF is known to be less robust than the stochastic EnKF in strongly nonlinear regimes. We generalize the LETKF such that it contains a stochastic term and includes the stochastic EnKF within it. We adaptively optimi...
  </details>

- **2026-07-06** — Qiuyi Qi, Tian Liang, Mutian Bao et al. — [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](http://arxiv.org/abs/2607.04963v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy-based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision re...
  </details>

- **2026-07-06** — Nicholas Tan Jerome, Frank Simon — [When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters](http://arxiv.org/abs/2607.04919v1)
  <details><summary>📄 Abstract</summary>
  Deploying a time series foundation model requires GPU infrastructure, engineering overhead, and carries no guarantee of improvement over XGBoost. We provide the first systematic break-even analysis answering when this investment pays off. Across 30 benchmark datasets, we compare zero-shot and LoRA fine-tuned foundation models (Chronos, Moirai, Lag-Llama) against classical baselines (Naive, ETS, ARIMA, XGBoost) at six training set sizes from 2% to 100% of available data. Foundation models outperf...
  </details>

- **2026-07-06** — Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García et al. — [TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving](http://arxiv.org/abs/2607.04812v1)
  <details><summary>📄 Abstract</summary>
  Bird's-Eye View (BEV) end-to-end instance prediction has emerged as a robust paradigm for autonomous driving perception, effectively mitigating the error propagation inherent in traditional modular pipelines. However, current state-of-the-art approaches rely predominantly on geometric supervision, such as occupancy regression and optical flow, effectively treating scene agents as generic moving obstacles. This absence of explicit semantic awareness imposes limitations on the capacity of the mode...
  </details>

- **2026-07-06** — Linas Beresna, Eugene Fiume — [Glare Mitigation using a Differentiable Unified Glare Rating](http://arxiv.org/abs/2607.04796v1)
  <details><summary>📄 Abstract</summary>
  Recent research in differentiable light transport extends the utility of computer graphics algorithms beyond traditional image generation, offering powerful tools for physical inverse design. In architectural and automotive applications, visual discomfort from glare is a critical design rating, traditionally quantified by the discrete CIE Unified Glare Rating (UGR). The standard UGR formulation relies on strict binary thresholds, making it fundamentally incompatible with smooth gradient-based in...
  </details>

- **2026-07-06** — Kenta Tsukahara, Kanji Tanaka, Rai Hisada — [SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR](http://arxiv.org/abs/2607.04764v1)
  <details><summary>📄 Abstract</summary>
  Visual Place Recognition (VPR) in lifelong deployment requires continuous adaptation to new environments without catastrophic forgetting. In this paper, we propose SLAM, a Structured and Localized Analytic Manifold adaptation framework. Our framework elegantly unifies uncertainty-aware smoothing via Unscented transformation, topological space partitioning through a Gaussian Mixture Model (GMM), and $H_\infty$ robust bound optimization into a singular, unified closed-form analytical recursion. Ex...
  </details>

- **2026-07-06** — Ashna Goel, Shovan Bhaumik, Nutan Kumar Tomar — [Risk Sensitive Filtering for Singular Systems subject to Round-Robin Protocol](http://arxiv.org/abs/2607.04734v1)
  <details><summary>📄 Abstract</summary>
  This paper develops a risk sensitive (RS) Kalman filtering framework for discrete-time linear stochastic singular systems operating under communication constraints imposed by a round-robin protocol. Due to limited network bandwidth, only a subset of the available measurements can be transmitted at each sampling instant, resulting in a periodically varying measurement structure. By employing the Weierstrass canonical form (WCF), the singular system is transformed into an equivalent augmented stat...
  </details>

- **2026-07-06** — Mingyang Fu, Ming Hu — [Strategic Buying Agents](http://arxiv.org/abs/2607.04708v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI is shifting online shopping from search toward delegated purchasing, where autonomous buying agents monitor markets and decide when to buy on a consumer's behalf. We study the design of such strategic buying agents, which must decide when to purchase within a finite shopping window, translating price observations, the remaining time horizon, and beliefs about future price changes into a purchase policy. We formulate this problem across three information regimes: stationary, Bayesian, ...
  </details>

- **2026-07-06** — Liuyun Jiang, Yanchao Zhang, Jinyue Guo et al. — [Probe-EM: Targeted Neuron Tracing via Training-Free Semantic Verification](http://arxiv.org/abs/2607.04696v1)
  <details><summary>📄 Abstract</summary>
  Establishing large-scale, high-resolution neural connectivity maps is fundamental to elucidating the structural basis of brain function. However, when processing terabyte- or petabyte-scale electron microscopy data, over-segmentation inherent in automated reconstruction algorithms remains a critical bottleneck, requiring extensive manual proofreading spanning person-years. To alleviate the heavy reliance on annotated data and the limited flexibility of conventional tracing methods, we propose a ...
  </details>

- **2026-07-05** — Haiwen Yi, Xinyuan Song — [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](http://arxiv.org/abs/2607.04528v1)
  <details><summary>📄 Abstract</summary>
  Software-agent benchmarks usually report whether an agent solves a task, but the agent reaches that outcome through a harness that controls what it sees, which actions it can take, which failures are repaired, which states are verified, and which evidence is logged. We show that this harness can change the agent's multi-step beliefs even when the task, environment, and base LLM are fixed. We introduce a belief-rollout diagnostic that elicits structured K-step trajectories over progress, risk, re...
  </details>

- **2026-07-05** — Zhaohong Liu, Hao Ye, Xianlin Zhang et al. — [CritiqueDriveVLM: From Verifier-Guided Reinforcement Learning to Latent Thought Distillation for Autonomous Driving](http://arxiv.org/abs/2607.04179v1)
  <details><summary>📄 Abstract</summary>
  End-to-end Vision-Language Models (VLMs) show immense potential in autonomous driving. However, standard Supervised Fine-Tuning (SFT) often suffers from reasoning hallucinations and conservative biases. While traditional tool-augmented frameworks and Chain-of-Thought (CoT) approaches mitigate these issues, they incur exorbitant token consumption and unacceptable latency, rendering real-time deployment impractical. To resolve this reliability-efficiency trade-off, we propose CritiqueDriveVLM, a n...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 8 papers

- **2026-07-08** — Ahsan Habib Akash, Dipkamal Bhusal, Stacey Jones et al. — [Naming the Concepts Classifiers Rely On: Language-Anchored Decomposition for Faithful Explanation](http://arxiv.org/abs/2607.07264v1)
  <details><summary>📄 Abstract</summary>
  Deep neural networks are widely deployed in high-stakes visual applications where interpretability is critical, yet existing explanations face a trade-off: post-hoc concept methods recover factors that are faithful to a model's behavior but unnamed, while naming and by-design methods attach human-readable concepts only by retraining or altering the classifier. We propose Language-Anchored Decomposition (LAD), a post-hoc framework that delivers concepts which are simultaneously named, faithful, a...
  </details>

- **2026-07-07** — Riccardo Terrenzi, Serkan Ayvaz — [Faithful or Findable? Evaluating LLM-Generated Metadata for RDF Dataset Search](http://arxiv.org/abs/2607.05970v1)
  <details><summary>📄 Abstract</summary>
  Dataset search depends heavily on metadata, making LLM-generated metadata a consequential form of synthetic content in retrieval systems. We study six metadata-generation settings for RDF datasets, ranging from simple rewriting to profile-grounded and agentic graph-based generation, and evaluate them jointly for retrieval effectiveness and faithfulness. Unconstrained metadata rewriting delivers the strongest retrieval gains over the original metadata, but it is also the least faithful, showing t...
  </details>

- **2026-07-07** — Sergey Volkov, Yang Li, Ye Luo — [StateFuse: Deterministic Conflict-Preserving Memory for Multi-Agent Systems](http://arxiv.org/abs/2607.05844v1)
  <details><summary>📄 Abstract</summary>
  Agent systems accumulate conflicting observations across branches, retries, and replicas, yet many practical memory layers still collapse disagreement behind overwrite rules that are difficult to inspect or correct. We present StateFuse, a conflict-aware replicated memory contract built on standard OpSet/CRDT merge. StateFuse does not introduce a new join algebra; it defines an agent-facing semantics layer with immutable history, explicit conflict objects, exact and semantic correction handles (...
  </details>

- **2026-07-07** — Yue Xu, Yutao Sun, Yihao Liu et al. — [From Passive Retrieval to Active Memory Navigation: Learning to Use Memory as a Structured Action Space](http://arxiv.org/abs/2607.05794v1)
  <details><summary>📄 Abstract</summary>
  Long-term user memory is essential for personalized conversational agents, yet many memory systems still expose memory through passive retrieval interfaces, making the model a consumer of pre-selected evidence. We introduce NapMem, a framework for learning to use long-term user memory as a structured action space rather than passively retrieved context. NapMem organizes user history into a linked multi-granularity memory pyramid, where raw conversations, typed memory records, topic tracks, and u...
  </details>

- **2026-07-06** — Clemens Walter Koprolin, Leonardo Trentini, Benedikt Soja et al. — [GeoXplain: On-the-Fly Visual Explanations for Weather Foundation Models](http://arxiv.org/abs/2607.05655v1)
  <details><summary>📄 Abstract</summary>
  Weather and climate foundation models produce high-dimensional forecasts whose learned relationships are difficult to inspect with static plots alone. GeoXplain is an interactive Python-based visualization toolkit for exploring geospatial attribution maps across climate variables, atmospheric pressure levels, and forecast time. The toolkit accepts attribution bundles containing attribution grids together with corresponding metadata and renders them in a notebook widget or browser with map and gl...
  </details>

- **2026-07-06** — Xue Yao, Zehua Zhang, Jiatong Liu et al. — [RepoTrace: Browser-Assisted Evidence Collection for GitHub Research Datasets](http://arxiv.org/abs/2607.05106v1)
  <details><summary>📄 Abstract</summary>
  Empirical software engineering studies frequently build datasets from GitHub issues and pull requests. In many projects, researchers inspect pages in a browser, copy selected fields into spreadsheets, keep side notes in separate documents, and later run scripts to normalize or export the data. This workflow is flexible, but the page evidence, the research codes, and the rationale behind each decision end up spread across tabs and files, which leaves provenance, update tracking, and multi-reviewe...
  </details>

- **2026-07-06** — Jizhizi Li, Amy Shi-Nash — [MRMS: A Multi-Resolution Memory Substrate for Long-Lived AI Agents](http://arxiv.org/abs/2607.04617v1)
  <details><summary>📄 Abstract</summary>
  Long-lived AI agents require continuity across interactions, but continuity cannot be obtained by simply extending the prompt window. An agent must preserve useful prior experience, retrieve it selectively, distinguish personal context from external evidence, and revise memory when the underlying situation changes. We propose an architectural memory substrate organized along two orthogonal axes: a representational axis spanning structured records, vector representations, and graph relations; and...
  </details>

- **2026-07-05** — Guijia Zhang, Harry Yang — [Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure](http://arxiv.org/abs/2607.04334v1)
  <details><summary>📄 Abstract</summary>
  Multimodal GUI agents read an interface through two redundant channels: the rendered pixels of a screenshot and a serialized structure such as a DOM or accessibility tree. Before acting, an agent forms a belief about the current interface state, but existing benchmarks score task success, element grounding, or attack resistance and do not ask whether that belief is drawn from the pixels. We formalize visual state reliance, the attribution of a state belief to pixels, structure, or priors, and me...
  </details>


### 📂 benchmark
*安全评测与基准 / Safety Benchmarks & Evaluation* — 1 papers

- **2026-07-05** — Ke Li, Kaidi Liang, Yuxin Ding et al. — [CCFM: Collision-Constrained Flow Matching for Safety-Critical Scenario Generation](http://arxiv.org/abs/2607.04451v1)
  <details><summary>📄 Abstract</summary>
  Evaluation of autonomous vehicle (AV) planners in safety-critical closed-loop simulation is essential for real-world deployment. However, generating controllable safety-critical scenarios remains challenging. Existing approaches use soft guidance that provides only probabilistic preferences and cannot guarantee the satisfaction of geometric and severity constraints associated with specific collision types. We introduce Collision-Constrained Flow Matching (CCFM), a novel framework that guarantees...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 3 papers

- **2026-07-08** — Arun Malik — [Progressive Crystallization: Turning Agent Exploration into Deterministic, Lower-Cost Workflows in Production](http://arxiv.org/abs/2607.07052v1)
  <details><summary>📄 Abstract</summary>
  AI agents deployed for IT operations are typically permanent cost centers because every execution requires full LLM inference, even for previously solved problems. This paper introduces progressive crystallization, a lifecycle that treats agent exploration as a discovery mechanism rather than a permanent execution model. It defines a three-stage execution taxonomy, from fully agent-orchestrated to hybrid to fully deterministic workflows, together with an evidence-based promotion mechanism that c...
  </details>

- **2026-07-07** — Rui Shu, Chun Yong Chong, Xin Zhou et al. — [What Resolve Rate Hides: Trajectory Structure Diagnostics for Coding Agents](http://arxiv.org/abs/2607.06184v1)
  <details><summary>📄 Abstract</summary>
  Coding agents are ranked almost entirely by resolve rate: whether their final patch passes the target tests. Yet two agents can reach the same outcome through very different processes, and a single pass/fail label says nothing about why a run failed or why an accepted run spent extra steps, time, or tokens. This process evidence lives in the trajectory, which records a run's searches, reads, edits, tool calls, validation, and reversions. However, raw traces are heterogeneous and hard to compare ...
  </details>

- **2026-07-05** — Faid Keddouri, Sohaib Houhou, Aissa Boulmerka et al. — [Regime-Conditional Stabilisation of LLM-Augmented Cooperative Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2607.04470v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) offer a natural interface for translating human objectives into reward signals for cooperative multi-agent reinforcement learning (MARL), yet the training-time dynamics of this integration remain poorly understood. We show that dynamically updating LLM-generated reward weights during off-policy MARL violates the stationarity assumption of Potential-Based Reward Shaping (PBRS) and contaminates the experience replay buffer, whose stored transitions carry reward labels ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 168 papers

- **2026-07-08** — Osman Cevheroğlu, Arkadaş Özakın — [An analytical solution of a quantum system with non-Markovian behavior: The Bixon-Jortner system in time domain](http://arxiv.org/abs/2607.07546v1)
  <details><summary>📄 Abstract</summary>
  Non-Markovian behavior in quantum systems is often studied in the context of bipartite systems consisting of a system of interest and an environment -- tracing over the environment results in non-Markovian behavior for the subsystem of interest. One may get a Markovian limit in certain regimes, which is studied using the Lindblad master equation, and corrections to this behavior can be obtained by techniques such as the Nakajima-Zwanzig formalism. In this paper, we obtain an exact non-Markovian ...
  </details>

- **2026-07-08** — Zelin Gao, Qiuyu Wang, Jiapeng Zhu et al. — [Infinite Worlds with Versatile Interactions](http://arxiv.org/abs/2607.07534v1)
  <details><summary>📄 Abstract</summary>
  We present LingBot-World 2.0 (also known as LingBot-World-Infinity), an advanced iteration of LingBot-World featuring four distinct upgrades. (1) Our model achieves an unbounded interaction horizon while maintaining consistent output quality, benefiting from a carefully crafted causal pretraining paradigm. (2) Through distilling a real-time variant from the base model, our system guarantees rapid response time, sufficient to drive 720p video streams at 60 fps. (3) Compared to the previous versio...
  </details>

- **2026-07-08** — Tamal Maharaj — [A Word-Level Digital Reader of the Prasthanatrayi with Sankara's Bhasya: Corpus, Method, and an Open, Offline Reading Aid for the Advaita Vedanta Canon](http://arxiv.org/abs/2607.07282v1)
  <details><summary>📄 Abstract</summary>
  The Prasthanatrayi -- the ten principal Upanisads, the Brahmasutra, and the Bhagavadgita, with Sankara's commentaries (bhasya) -- is the foundational corpus of Advaita Vedanta. Continuous euphonic combination (sandhi), long compounds (samasa), and dense scholastic prose make it hard to read at the word level: where one word ends, and what each word means grammatically, are both obscured. We present an open, fully offline, word-level digital reader of the entire Prasthanatrayi with Sankara's bhas...
  </details>

- **2026-07-08** — Jerry Han, Rafael Moschopoulos, Ella Colby et al. — [Measuring Intelligence Beyond Human Scale](http://arxiv.org/abs/2607.07040v1)
  <details><summary>📄 Abstract</summary>
  How can we measure intelligence beyond human capability?   Human-authored benchmarks saturate, and above human capability, examiners may not know which tasks are both hard and verifiable. We argue that this difficulty is inherent to absolute-scale evaluation and propose a new paradigm based on relative measurement in which models generate public challenges that separate other systems. Aggregating these outcomes yields an adversarial psychometric rating system that can scale with the systems bein...
  </details>

- **2026-07-08** — Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi — [The Key to Going Linear: Analysis-Driven Transformer Linearization](http://arxiv.org/abs/2607.07706v1)
  <details><summary>📄 Abstract</summary>
  The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of ...
  </details>

- **2026-07-08** — Si-Yu Yuan, Wen-Tan Xue, Ching Hua Lee — [Non-Hermitian Edge State Endocytosis](http://arxiv.org/abs/2607.07703v1)
  <details><summary>📄 Abstract</summary>
  An isolated edge state observed in a finite open chain is usually expected to survive the thermodynamic limit (TDL), with a localization mechanism distinct from non-Hermitian skin accumulation, which localizes the \emph{entire} bulk continuum. We show that scale-sensitive non-Hermitian systems can generically admit a different fate: as we scale up the system size, a detached edge-localized eigenstate can remain sharply visible over a broad window until a critical scale is reached, where it forms...
  </details>

- **2026-07-08** — Tianming Sha, Yue Zhao, Lichao Sun et al. — [SkillCenter: A Large-Scale Source-Grounded Skill Library for Autonomous AI Agents](http://arxiv.org/abs/2607.07676v1)
  <details><summary>📄 Abstract</summary>
  Autonomous AI agents can execute complex tasks with limited human review, yet they often lack the grounded operational knowledge to make their outputs not just executable but correct, secure, and maintainable. We introduce SkillCenter, to our knowledge the largest open skill library for agents by total count: 216,938 structured skills across 24 domain bundles. A SkillGate-filtered pipeline contributes 114,565 source-grounded skills from peer-reviewed journals, ArXiv, and over 24,000 technical so...
  </details>

- **2026-07-08** — Halimat Olamide Yusuf, Augustine O. Nwajana — [Six-Pole Dual-band Bandpass Filter for WiMAX Applications](http://arxiv.org/abs/2607.07661v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multi-band wireless communication systems have driven the increasing need for dual-band bandpass filters. These types of filters are capable of isolating a small section of the frequency spectrum within a broader spectrum. Over the years, coplanar waveguide, microstrip, slotline, stripline, and other planar transmission line technologies have been widely employed in the design of microwave circuits and systems. This work employs a Folded-Arms Square Open-Loop Resonator (FASOLR...
  </details>

- **2026-07-08** — Azwar Abdulsalam, Nishil Patel, Andrew Saxe — [RL Post-Training Builds Compositional Reasoning Strategies](http://arxiv.org/abs/2607.07646v1)
  <details><summary>📄 Abstract</summary>
  Does RL post-training merely amplify primitive skills already latent in a base model, or can it compose primitive skills into new higher-level strategies? We study this question in a fully observable rewrite-grammar environment where the pretraining distribution is known and every generated rewrite can be audited. A Transformer is pretrained on primitive symbol-rewrite chains and post-trained on a Trace-based reasoning task with only a binary final-answer reward. RL solves held-out problems that...
  </details>

- **2026-07-08** — Aneesh Ramaswamy, Nageswara S. V. Rao, Joseph C. Chapman et al. — [Analysis of polarization drift of optical signals over deployed aerial-inground fiber connections](http://arxiv.org/abs/2607.07629v1)
  <details><summary>📄 Abstract</summary>
  Polarization measurements of a classical 1550-nm signal are collected and analyzed on 15-km hybrid aerial-inground fiber connections over 11 months. The spectral area and spectral moments9 of mHz-resolution Fast-Fourier-Transform (FFT) of these measurements are extracted, and related to temperature, humidity, wind speed, and time of day. Spectral area correlations show a strong11 diurnal structure: daytime maxima align with temperatures/wind speed peaks and humidity dips, with lower levels durin...
  </details>

- **2026-07-08** — Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan et al. — [What Makes a Good Bug Report for an AI Agent?](http://arxiv.org/abs/2607.07593v1)
  <details><summary>📄 Abstract</summary>
  Automated program repair (APR) agents are transitioning from research benchmarks to developer workflows, yet they still begin with bug reports written for human developers. While decades of research have established what makes a good bug report for humans (e.g., steps to reproduce, stack traces), it remains unclear whether these features transfer to LLM-based agents. We study this question in two analyses. First, we use statistical modeling to examine associations between 27 bug-report features ...
  </details>

- **2026-07-08** — Dmitry Beresnev, Vladimir Makharev, Roman Khalikov et al. — [Search, Fail, Recover: A Training Framework for Correction-Aware Reasoning](http://arxiv.org/abs/2607.07492v1)
  <details><summary>📄 Abstract</summary>
  Many reasoning tasks are not well described by a single left-to-right chain: a solver may need to pursue a plausible branch, observe delayed failure, and return to the latest prefix that can still be completed. We introduce Pyligent, a training and inference framework inspired by the Diligent Learner formulation that represents reasoning as validated search over partial solution chains. A task validator labels generated continuations and failures, and the resulting search trees are converted int...
  </details>

- **2026-07-08** — Songhan Wang, Haoang Chi, He Li et al. — [SpaCellAgent: A Self-Evolving LLM-Based Multi-Agent Framework for Trajectory Analysis](http://arxiv.org/abs/2607.07467v1)
  <details><summary>📄 Abstract</summary>
  Spatial and Single-cell transcriptomics are transformative in deciphering cellular dynamics. As the fundamental paradigm for reconstructing cell developmental paths, trajectory inference (TI) is critical. However, existing methods require extensive manual intervention and proficiency in heterogeneous tools, posing a significant barrier to efficient TI analysis. To bridge this gap, we propose SpaCellAgent, an autonomous large language model (LLM) multi-agent framework that automates end-to-end sp...
  </details>

- **2026-07-08** — Xing Zhang, Yanwei Cui, Guanghui Wang et al. — [The Blind Curator: How a Biased Judge Silently Disables Skill Retirement in Self-Evolving Agents](http://arxiv.org/abs/2607.07436v1)
  <details><summary>📄 Abstract</summary>
  A self-evolving agent retires its bad skills by watching them fail, so what happens when the judge cannot see the failures? Skill retirement is the structural constraint that keeps a growing library from drifting below the no-skill baseline, but its guarantee assumes an unbiased reward, which is false for the LLM judges that reference-free tasks force upon us. We show that a biased judge does not merely add noise; it \emph{silently switches off the curator}. We make this precise with a corrupted...
  </details>

- **2026-07-08** — Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek et al. — [Multi-Agent Robotic Control with Onboard Vision-Language Models](http://arxiv.org/abs/2607.07403v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial wa...
  </details>

- **2026-07-08** — Elaine Ang, Chenxi Huang, Georgios Liargkovas et al. — [Agentic Data Environments](http://arxiv.org/abs/2607.07397v1)
  <details><summary>📄 Abstract</summary>
  Autonomous agents promise substantial gains in speed, scale, and labor efficiency, but their failures can impose abrupt and often irreversible costs. The central challenge for agentic automation is therefore to increase the benefits of automation while bounding the consequences of failure.   While databases remain central to modern computing, agents operate over a broader data environment spanning files, APIs, applications, and system state. In this talk, I will outline early work on Agentic Dat...
  </details>

- **2026-07-08** — Diab W. Abueidda, Bilal Ahmed, Panos Pantidis et al. — [Physics-Audited Agentic Discovery in Scientific Machine Learning](http://arxiv.org/abs/2607.07379v1)
  <details><summary>📄 Abstract</summary>
  In agentic scientific machine learning (SciML), large language model (LLM) agents can discover surrogate models and select one by an automated score, typically an error metric. A low error, however, does not establish that the predicted fields satisfy the physics that matter for mechanics, such as boundary conditions, superposition, stiffness scaling, or causality. We introduce Physics-Audited Agentic SciML (PA-SciML), a verification-first workflow for agentic SciML discovery. The workflow fixes...
  </details>

- **2026-07-08** — Pranav Sawant, Jakub Krejčí — [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](http://arxiv.org/abs/2607.07316v1)
  <details><summary>📄 Abstract</summary>
  This article offers a comprehensive overview of mechanistic interpretability, an emerging field that seeks to reverse-engineer the internal algorithms of modern neural networks. While traditional explainable AI methods often stop at surface-level input-output correlations, this approach directly addresses the opaque "black box" nature of machine learning models, which is essential for ensuring safety and auditability in high-stakes deployments. The paper provides a detailed examination of Transf...
  </details>

- **2026-07-08** — Arianna Pera, Mauro Martino, Nima Dehmamy et al. — [Billions of Sketches Reveal Hidden Cultural Variation in Human Concepts](http://arxiv.org/abs/2607.07267v1)
  <details><summary>📄 Abstract</summary>
  Claims about the universality of human concepts have been predominantly assessed through linguistic similarity across languages and cultures. However, words are effective as communication devices because they compress rich experiential variation into shared conventions, potentially obscuring hidden individual and cultural differences in how concepts are mentally represented. Here, we analyse 2.6 billion human-made sketches of common concepts from 236 countries and territories to examine conceptu...
  </details>

- **2026-07-08** — Zhenghao Zhou, Yiyan Li, Tao Xu et al. — [A Physics-guided Fine-tuned LLM-based Framework for Customized Power Distribution System Feeder Generation](http://arxiv.org/abs/2607.07237v1)
  <details><summary>📄 Abstract</summary>
  Power distribution system feeder models (e.g., IEEE 33-bus system, IEEE 13-bus system, etc.) are cornerstones for conducting power distribution system studies. As real-world feeder models are hard to acquire due to energy security concerns, generating high-quality synthetic feeders becomes an important alternative to satisfy the fast-growing and diversified needs of power system researchers and engineers. In this paper, we propose an LLM-based synthetic feeder generation framework that can achie...
  </details>

- **2026-07-08** — Jáchym Bártík, Alžběta Šrůtková, Irena Holubová — [Benchmark Engineering as a Design Instrument for Heterogeneous Information Systems](http://arxiv.org/abs/2607.07175v1)
  <details><summary>📄 Abstract</summary>
  Contemporary information systems operate in heterogeneous and continuously evolving data environments, where representation choices and structural redesign decisions strongly influence system behavior. Existing benchmarking approaches, however, rely mostly on static datasets and fixed schemas, providing limited support for analyzing architectural trade-offs or guiding evolution in multi-model settings.   This paper introduces TransforMMer, a framework for evolution-aware and representation-aware...
  </details>

- **2026-07-08** — Rakshitha De Silva, Shiva Raj Pokhrel, Jonathan Kua — [Small Language Model-based Control for BBR over Low Earth Orbit Satellite Internet](http://arxiv.org/abs/2607.07142v1)
  <details><summary>📄 Abstract</summary>
  Low Earth Orbit (LEO) satellite Internet introduces rapid path variability, intermittent capacity shifts, and non-terrestrial delay dynamics that challenge transport-layer congestion control. Although Bottleneck Bandwidth and Round-trip propagation time (BBR) achieves high throughput in such environments, its aggressive bandwidth probing can cause excessive retransmissions and unstable pacing over LEO links. This paper presents a global experimental evaluation of BBR over a SpaceX Starlink testb...
  </details>

- **2026-07-08** — Stepanida Alekseeva, Jenifer Kalafatovich, Seong-Whan Lee — [Tree-of-Thoughts Reasoning for Text-to-Image In-Context Learning](http://arxiv.org/abs/2607.07117v1)
  <details><summary>📄 Abstract</summary>
  In text-to-image in-context learning (T2I-ICL), a model has to infer a latent compositional pattern from fewshot demonstrations for generating a query image. Recent studies show that state-of-the-art multimodal large language models struggle with this setting, particularly due to limited compositional reasoning and sensitivity to prompt construction. In this work, we propose a Tree-of-Thoughts (ToT) reasoning framework for T2I-ICL that introduces a multi-stage reasoning and selection layer that ...
  </details>

- **2026-07-08** — Heye Huang, Jingguang Li, Zhiyuan Zhou et al. — [A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving](http://arxiv.org/abs/2607.07103v1)
  <details><summary>📄 Abstract</summary>
  Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large lang...
  </details>

- **2026-07-08** — Szczepan Konior, Alexandre Quemy, Przemysław Klocek et al. — [Riemannian Geometry for Pre-trained Language Model Embeddings](http://arxiv.org/abs/2607.07047v1)
  <details><summary>📄 Abstract</summary>
  Understanding the geometric structure of pre-trained language model embeddings matters for interpretability and safety. We ask whether sentence-level classification signal lives in the Riemannian geometry of contextual token embeddings, and probe it by extracting per-token pullback metrics from a learned encoder's analytical Jacobian and aggregating them with the Fréchet mean on the symmetric positive definite (SPD) manifold; we call this procedure Riemannian Mean Pooling (RMP). Across three dat...
  </details>

- **2026-07-08** — Yusen Feng, Bingchen Han, Jiangran Lyu et al. — [WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time](http://arxiv.org/abs/2607.06988v1)
  <details><summary>📄 Abstract</summary>
  Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video predi...
  </details>

- **2026-07-08** — Amin Tabrizian, Arsyi Aziz, Aarifah Ullah et al. — [End-to-End LLM Flight Planning with RAG-based Memory and Multi-modal Coach Agent](http://arxiv.org/abs/2607.06964v1)
  <details><summary>📄 Abstract</summary>
  Bridging the gap between human pilot intent and autonomous flight operation is critical for real-world electric vertical takeoff and landing (eVTOL) aircraft deployment. Flight planning traditionally relies on classic algorithms that struggle to incorporate flexible human preferences. We present FRAMe, an End-to-End Large Language Model (LLM) Flight Planning tool with RAG-based Memory and Multi-modal Coach Agent. Our system integrates a planner LLM with a multi-modal coach agent and retrieval au...
  </details>

- **2026-07-08** — Yingshu Li, Yunyi Liu, Zhenghao Chen et al. — [Seeing What Matters: Lesion-Aware High-Resolution Patch Discovery and Fusion for Chest X-ray Report Generation](http://arxiv.org/abs/2607.06909v1)
  <details><summary>📄 Abstract</summary>
  Despite rapid advances in chest X-ray (CXR) foundation models, most radiology report generation (RRG) systems still rely on heavily downsampled inputs (e.g., 256x256) due to the fixed visual token budgets of pretrained vision encoders, suppressing subtle yet clinically important cues present in native-resolution images. However, enabling high-resolution (high-res) perception remains challenging: naive tiling causes prohibitive token inflation, while global compression suppresses subtle lesions a...
  </details>

- **2026-07-08** — Muayad Sayed Ali, Aliaksandra Novik, Anji Boddupally et al. — [The Harness Effect: How Orchestration Design Sets the Token Economics of Enterprise Agentic AI](http://arxiv.org/abs/2607.06906v1)
  <details><summary>📄 Abstract</summary>
  Agentic AI development today runs on token maxing: buying capability with tokens -- longer reasoning traces, more turns, wider tool payloads, bigger replayed contexts -- so tokens per task grow faster than task value. Falling per-token prices mask the pattern; total spend rises anyway. We argue the decisive lever against token maxing is the harness: the orchestration layer that assembles context, exposes tools, sequences turns, delegates work, and carries enterprise observability and governance....
  </details>

- **2026-07-08** — Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma et al. — [Immersive Social Interaction with VR and LLM-Assisted Humanoids](http://arxiv.org/abs/2607.07430v1)
  <details><summary>📄 Abstract</summary>
  Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidirectional social interaction for whole-body humanoid control. Using Apple Vision Pro, the operator receives egocentric visual feedback, issue...
  </details>

- **2026-07-08** — Vrinda Malhotra — [Modeling Misinformation as a Commons Problem](http://arxiv.org/abs/2607.06984v1)
  <details><summary>📄 Abstract</summary>
  Misinformation often harms society not just by spreading a single false belief, but by breaking down the shared trust people rely on to evaluate what is true. This paper presents an agent-based simulation that frames trust as a collective resource and attention as a scarce private budget: when aggregate attention shifts toward low credibility content, the trust environment degrades, making credible information harder to process and correct. Across experiments, the model produces four recurring m...
  </details>

- **2026-07-08** — Liting Lin, Boxi Yu, Yuzhong Zhang et al. — [Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents](http://arxiv.org/abs/2607.06873v1)
  <details><summary>📄 Abstract</summary>
  Conversational LLM agents can cause real-world harm when their internal workflows fail, such as completing a transaction without confirmation. Testing these state-dependent failures is difficult because critical boundaries, such as identity checks and confirmation gates, are hidden behind multi-turn conversational prerequisites, rendering them inaccessible to standard tests. We present AgentEval, a black-box testing framework that discovers and stresses these stateful boundaries. AgentEval inter...
  </details>

- **2026-07-08** — Chen Tang, Yizhou Wang, Jianyu Wu et al. — [Accurate, Interdisciplinary and Transparent Structure-property Understanding with Deep Native Structural Reasoning](http://arxiv.org/abs/2607.07708v1)
  <details><summary>📄 Abstract</summary>
  Structure-property relationships are foundational to biology, chemistry and materials science, where function, reactivity and physical response emerge from spatial, chemical and periodic organization. Mechanistically explaining these relationships requires interpreting structural evidence through scientific principles and physical constraints, from stereochemistry and bonding to symmetry, energetics and periodic order. However, applying artificial intelligence to this process presents a joint ch...
  </details>

- **2026-07-08** — Yair Feldman, Linxi Zhao, Nathan Godey et al. — [Co-LMLM: Continuous-Query Limited Memory Language Models](http://arxiv.org/abs/2607.07707v1)
  <details><summary>📄 Abstract</summary>
  Limited memory language models (LMLMs) externalize factual knowledge during pretraining to a knowledge base (KB), rather than memorizing it in their weights. During generation, the model then fetches knowledge from the KB as needed. This recently introduced paradigm provides multiple advantages, including knowledge control capabilities that remain beyond conventional LLMs. We propose continuous-query LMLM (CO-LMLM), where the KB pairs continuous keys with textual knowledge values, a significant ...
  </details>

- **2026-07-08** — Xinyi Wu, Siyuan Liu, Ali Jadbabaie — [How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization](http://arxiv.org/abs/2607.07678v1)
  <details><summary>📄 Abstract</summary>
  Rotary Position Embeddings (RoPE) provide transformers with a fixed grid of positional frequencies, yet trained models use these frequencies highly non-uniformly. We study what determines this frequency usage and propose a data-centered explanation: RoPE frequencies are selected to match the relative-distance structure of the training data. Viewing each frequency as a positional lens, we formalize a field-resolution tradeoff and show that, for a data-induced dependency profile of width $W$, the ...
  </details>

- **2026-07-08** — Andrea Scarinci, Virginia Negri, Brayan Impata et al. — [SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation](http://arxiv.org/abs/2607.07469v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning large language models (LLMs) for e-commerce attribute extraction requires labeled data representative across thousands of product types, attributes, and multiple languages. This combinatorial scale translates to millions of annotations, rendering human labeling prohibitively costly. While recent work has demonstrated synthetic label generation using LLMs, deploying such approaches at industrial scale requires integrated quality control mechanisms. We present SynthAVE, a large-scale h...
  </details>

- **2026-07-08** — Tanay Sodha, Aditya Sharma, Ramya Hebbalaguppe et al. — [When Prompts Ignore Structure: Graph-Based Attribute Reasoning for Calibrated VLMs](http://arxiv.org/abs/2607.07395v1)
  <details><summary>📄 Abstract</summary>
  Reliable confidence estimation remains a key limitation of test-time adaptation in vision-language models (VLMs), where prompt tuning improves zero-shot accuracy but often degrades calibration due to entropy-driven overconfidence. Prior approaches mitigate this using LLM-derived class attributes and contrastive regularization, yet treat attributes independently, ignoring their relational structure. We propose ARGTCA, which represents (class, attribute) pairs as nodes in a Symbolic Attribute Grap...
  </details>

- **2026-07-08** — Ritajit Dey, Iadh Ounis, Graham McDonald — [Interpretable Uncertainty for Adaptive Retrieval and Reasoning in Question Answering](http://arxiv.org/abs/2607.07380v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve a strong performance in question answering (QA), but remain prone to hallucinations and suffer from limited transparency. Retrieval-augmented generation (RAG) can improve factuality, yet decisions about when and how to retrieve from external resources are typically based on opaque policies or computationally inefficient multi-step prompting procedures. We propose an uncertainty-aware framework for adaptive QA based on explicit signals derived from LLM interna...
  </details>

- **2026-07-08** — Oskar von Seeler, Christian Tetzlaff, Andrew Lehr — [Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware](http://arxiv.org/abs/2607.07373v1)
  <details><summary>📄 Abstract</summary>
  In biological circuits, sequential neural activity evolves along dynamic, low-dimensional manifolds to enable flexible behavior. Spiking network models link aspects of this sequential activity to features of manifold geometry through specific circuit mechanisms, making dynamic neural manifolds parameterizable, and thereby offering an explainable framework for neural computation. Extending this framework to neuromorphic engineering, we present an implementation on the SpiNNaker 2 chip for real-ti...
  </details>

- **2026-07-08** — Klaus M. Frahm, Dima L. Shepelyansky — [Thermodynamic description of worldwide distribution of energy and carbon emission](http://arxiv.org/abs/2607.07315v1)
  <details><summary>📄 Abstract</summary>
  Based on public data, we analyze the distributions of energy and carbon emission over world countries on a scale of the last 40-50 years using their presentation via Lorenz and Pareto curves. These curves in rescaled format remain remarkably stable on this time period being characterized by high values of the Gini coefficient indicating a strong inequality of energy distribution. To explain these distributions, we introduce the ENergy Thermalization Hypothesis (ENTH) according to which these dis...
  </details>

- **2026-07-08** — Sambit Sarkar, Mansi Talwar, Pravata K. Mohanty — [The Deep Learning Cosmic Ray Energy Reconstruction Pipeline for the GRAPES-3 Experiment](http://arxiv.org/abs/2607.07265v1)
  <details><summary>📄 Abstract</summary>
  The mass independent energy reconstruction of cosmic rays is crucial for understanding their origin, acceleration, and propagation. Precise measurement of the primary energy can also lead to better mass classification and could enable energy dependent anisotropy maps for individual elements. The GRAPES-3 experiment located in Ooty consisting of 400 scintillator detector array placed 8 m apart covering an area of 25000 m$^2$ with a dedicated muon detector made of 3712 proportional counters, is de...
  </details>

- **2026-07-08** — Ignacio D. Lopez-Miguel, Ezio Bartocci, Thomas Eiter et al. — [ORCAID: Oblique Rule-Based Continuous-Action Interpretation for Deep RL Policies](http://arxiv.org/abs/2607.07235v1)
  <details><summary>📄 Abstract</summary>
  Explainability remains a key issue in reinforcement learning (RL). Distilling an interpretable policy from an agent trained in a complex environment is particularly challenging when the action space is continuous. We introduce ORCAID, a novel method for extracting interpretable rule-based policies from RL agents operating in mixed continuous-discrete environments with continuous action spaces. Our main contribution is an efficient oblique decision tree training algorithm that partitions the stat...
  </details>

- **2026-07-08** — Guoruizhe Sun, Yueqiao Chen, Emily Guo et al. — [ShapeTalk: Combining Natural Language and Sketch for Time-Series Pattern Querying](http://arxiv.org/abs/2607.07073v1)
  <details><summary>📄 Abstract</summary>
  Searching for time-series segments that match user-defined patterns is important in domains such as finance, climate science, and healthcare. However, existing visual query tools often struggle to support vague, composite, or fuzzy pattern descriptions, often requiring users to express their intent through precise sketches or rigid structured filters. We present ShapeTalk, a coordinated natural-language and sketch-based querying system for univariate time-series pattern search. Rather than treat...
  </details>

- **2026-07-08** — Zitong Andrew Chen, Junaid Hasan, Akhil Srinivasan et al. — [Multiplication Beyond Groups: Stratified Fourier Mechanisms in Transformer Circuits](http://arxiv.org/abs/2607.07066v1)
  <details><summary>📄 Abstract</summary>
  Transformers have demonstrated a remarkable ability to learn algorithmic reasoning, yet mechanistic analyses have mostly focused on globally invertible operations such as cyclic addition and group composition. In this work, we investigate how small transformers learn modular integer multiplication over composite moduli, a fundamentally non-invertible operation due to the presence of zero-divisors. We propose the monoid extension: a localized generalization of Group Composition via Representation...
  </details>

- **2026-07-08** — Yujin Bae, Jaewoo Jeong, Hyeonseong Kim et al. — [Ego-Human Motion Prediction with 3D-Aware LLM](http://arxiv.org/abs/2607.07001v1)
  <details><summary>📄 Abstract</summary>
  Anticipating human motion from an egocentric perspective is fundamental for proactive assistance in AR/VR, human-robot collaboration, and embodied AI. While recent works incorporate language as a semantic prior to reduce the ill-posed nature of egocentric forecasting, they largely neglect the 3D spatial and semantic context that governs how motion unfolds, and treat pose and language prediction as separate inference streams. We introduce Ego3DLM, built on two core principles: accurate motion for...
  </details>

- **2026-07-08** — Wachiravit Modecrua, Krittin Pachtrachai, Touchapon Kraisingkorn — [Large Behavior Model: A Promptable Digital Twin of the Retail Customer](http://arxiv.org/abs/2607.06993v1)
  <details><summary>📄 Abstract</summary>
  Customer behavior modeling underpins recommendation, marketing, and decision support, yet existing approaches either optimize predictive accuracy without explaining decisions or simulate users without grounding them in real behavioral data. We present the Large Behavioral Model (LBM) that learns customer decision making directly from large-scale retail transactions through a unified Person-Environment formulation. Customer state is represented by a behavioral profile derived from historical purc...
  </details>

- **2026-07-07** — Truong Xuan Khanh — [At-Grok Is Not Converged:A Measurement-Validity Audit for Grokking Representation Metrics](http://arxiv.org/abs/2607.06639v1)
  <details><summary>📄 Abstract</summary>
  On modular arithmetic, a network's embedding keeps compressing for tens of thousands of steps after it has already generalized. Reading effective rank at the grokking transition overstates the converged value by 3-5x on an MLP, and by 1.3-1.5x on a transformer trained to convergence; on the MLP it also erases which cells compress at all. Compression lags the accuracy transition by an amount on the order of the time-to-grok, at least 10,000 steps, rather than coinciding with it. A one-variable ab...
  </details>

- **2026-07-07** — Siyuan Mei, Yan Xia, Yipeng Sun et al. — [WING: A Window-Prior-Based Generative Network with Gated Inception for Cross-Modality CT Synthesis](http://arxiv.org/abs/2607.06234v1)
  <details><summary>📄 Abstract</summary>
  Generating CT volumes from MRI and CBCT can improve treatment planning in adaptive radiotherapy while avoiding additional radiation exposure. However, direct regression of CT intensities is challenged by the inherently high dynamic range and long-tailed distributions, thereby averaging out sparse yet clinically important structures. To alleviate this issue, we reformulate the regression target into multiple windowed representations, leveraging the inductive prior that CT intensities are structur...
  </details>

- **2026-07-07** — Igor Santos-Grueiro — [Context-to-Execution Integrity for LLM Agents](http://arxiv.org/abs/2607.06000v1)
  <details><summary>📄 Abstract</summary>
  Language-model agents read attacker-writable context to solve tasks. Tool execution needs a separate authority check for protected sink fields, sink-interpreted payloads, and the invocation event. Context-to-Execution Integrity (CXI) is an execution-boundary system for this setting. Policies mark protected sink fields, typed releases carry narrow validated values from writable context to specific destinations, opaque data slots keep evidence as data, and a deterministic gate admits a call only a...
  </details>

- **2026-07-07** — Rakesh Podder, Wadia Ganim, Sarath Sreedharan et al. — [i-EXAM: Instructable and Explainable Attack Connectivity Graph Modeler](http://arxiv.org/abs/2607.05888v1)
  <details><summary>📄 Abstract</summary>
  i-EXAM is a planning-powered tool that helps system administrators to create security profiles of complex networks and perform what-if analyses to identify network hardening strategies. It leverages planning compilation that provides soundness and completeness guarantees to identify attack paths, evaluate security metrics, generate diverse hardening strategies, and explain these strategies in natural language using Large Language Models.
  </details>

- **2026-07-07** — Huan Wu, Ali Emami, Muhammad Furquan Hassan et al. — [LLMs Silently Correct African American English: Auditing and Mitigating Dialect Bias via Activation Steering](http://arxiv.org/abs/2607.06845v1)
  <details><summary>📄 Abstract</summary>
  African American English (AAE), a rule-governed dialect spoken by over 30 million people, is routinely misinterpreted and "corrected" by large language models (LLMs). Across six instruction-tuned LLMs (14B to 70B), we show that state-of-the-art models systematically prefer Standard American English (SAE) continuations even when the preceding context is in AAE, effectively rewriting AAE into SAE. We present an end-to-end framework to audit and mitigate this bias. For auditing, we introduce condit...
  </details>

- **2026-07-07** — Jiarui Xie, Lingchen Kong, Mohamed Rami Latreche et al. — [Machine Learning-Based Battery State-of-health Prediction for Unmanned Aerial Vehicles Predictive Maintenance](http://arxiv.org/abs/2607.06791v1)
  <details><summary>📄 Abstract</summary>
  Battery state-of-health (SoH) prediction aims to estimate the remaining capacity by modeling battery degradation through its life cycle. Machine learning (ML)-based SoH models can accurately predict the battery remaining capacity based on voltage, current, and temperature. Battery SoH prediction for unmanned aerial vehicles (UAVs) is a crucial yet overlooked domain with data scarcity and high variability. Accurate battery SoH information contributes to efficient predictive maintenance, enhancing...
  </details>

- **2026-07-07** — Alexey Gavryushin, Dingxi Zhang, Zhao Huang et al. — [CoMind: Understanding Collaborative Human Activity from Multiple Minds and Views](http://arxiv.org/abs/2607.06691v1)
  <details><summary>📄 Abstract</summary>
  Human-human collaboration is a fundamental aspect of everyday life, essential to success in a wide range of goal-directed activities from household tasks to professional teamwork. While much research has focused on modeling coordination and task execution, the cognitive processes that support such collaboration, particularly Theory of Mind (the ability to infer the mental states of others), remain difficult to study in natural settings. To address this gap, we introduce a novel egocentric and ex...
  </details>

- **2026-07-07** — Ziye Wang, Modi Shi, Chaojun Ni et al. — [NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation](http://arxiv.org/abs/2607.06678v1)
  <details><summary>📄 Abstract</summary>
  How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA'...
  </details>

- **2026-07-07** — He Liang, Chenyang Ma, Yiming Zhang et al. — [CAIRN: Cross-Room 3D Scene Understanding with Topology-Aware Large Multimodal Models](http://arxiv.org/abs/2607.06534v1)
  <details><summary>📄 Abstract</summary>
  Existing 3D scene-grounded Large Language Models (3D-LLMs) focus on answering questions grounded in simplified single-room 3D scenes, lacking the ability to reason over real-world household environments containing multiple interconnected rooms and diverse object categories. We introduce CAIRN, a topology-aware 3D-LLM for multi-room 3D scene understanding. CAIRN aligns transformer attention with scene hierarchy, giving the model explicit awareness of object-level relations and room-level connecti...
  </details>

- **2026-07-07** — Linlin Zhang, Neema Jakisa Owor, Xiang Yu et al. — [A VLM-Enhanced Framework for Comprehensive Traffic Sign Condition Assessment Integrating Daytime Visual Performance and Nighttime Retroreflectivity Evaluation](http://arxiv.org/abs/2607.06478v1)
  <details><summary>📄 Abstract</summary>
  Traffic signs are crucial components of road safety, serving as visual tools under all lighting conditions. The Manual on Uniform Traffic Control Devices (MUTCD) specifies daytime visual factors such as legibility and color contrast, and nighttime retroreflectivity requirements. Traditional assessment methods rely on manual inspections, which the Federal Highway Administration (FHWA) notes are subjective, labor-intensive and pose safety concerns, while retroreflectometers are expensive and unaff...
  </details>

- **2026-07-07** — Yuhang Wu, Shuxiang Zhang, Wee Hian Ching et al. — [PIPBench: A Profile-Inclusive Framework for Personalized Image Generation Evaluation](http://arxiv.org/abs/2607.06440v1)
  <details><summary>📄 Abstract</summary>
  Recent text-to-image models such as DALLE-3 excel at following diverse prompts yet remain blind to individual aesthetic preferences. We study personalized image generation, where models must align outputs with a user's implicit visual preferences based on a few historically preferred images and a short prompt. To this end, we introduce PIPBench, the first profile-inclusive benchmark for evaluating personalized image generation. We further propose a novel data construction pipeline that leverages...
  </details>

- **2026-07-07** — Hao He, Xueying Liu, Chris J. Kuhlman et al. — [An Experimental Design Approach to Evaluating Agentic AI's Autonomous Model Discovery](http://arxiv.org/abs/2607.06413v1)
  <details><summary>📄 Abstract</summary>
  Large language model coding agents increasingly perform open-ended data modeling and analysis. These agents are stochastic and adaptive, and therefore their autonomous model discovery behavior cannot be adequately characterized by a single benchmark run. In this work, we propose an experimental design and analysis framework for systematically evaluating this discovery process, quantifying its variability, and identifying important factors. The proposed framework treats these agents as stochastic...
  </details>

- **2026-07-07** — Eleftherios Tsonis, Xi Wang, Vicky Kalogeiton — [What Images Cannot Say: Language-Guided Olfactory Representation Learning](http://arxiv.org/abs/2607.06402v1)
  <details><summary>📄 Abstract</summary>
  Images tell us what a scene looks like, but rarely what it would feel like to be there. While recent datasets pair visual scenes with electronic-nose measurements, aligning smell signals with images remains challenging because many olfactory cues arise from contextual environmental factors that are not directly visible in pixels. We introduce SCENT, a multimodal framework that uses language guidance as a semantic bridge between vision and olfaction. Our approach leverages Vision-Language Models ...
  </details>

- **2026-07-07** — John Bianchi, Luca Petrillo, Fabio Martinelli et al. — [Automated Compliance Mapping in Cloud Security with Domain-Adapted Sentence Transformers](http://arxiv.org/abs/2607.06364v1)
  <details><summary>📄 Abstract</summary>
  Mapping cloud security controls to technical metrics is currently a manual process. This paper proposes domain adaptation of Sentence Transformer models to automate it. We build a training corpus of 3,499 semantic pairs from five European security standards and a set of technical metrics, then expand it via back-translation and LLM-based paraphrasing to up to 13,996 samples across four scenarios. We fine-tune five architectures and evaluate their performance on two independent tasks: control-to-...
  </details>

- **2026-07-07** — Xiachong Lin, Du Yin, Arian Prabowo et al. — [TopoBrick: Agentic Topology Sampling of Exogenous Variables for Zero-Shot Building IoT Forecasting](http://arxiv.org/abs/2607.06349v1)
  <details><summary>📄 Abstract</summary>
  Building sensors are embedded in physical topology, spatial hierarchy, and operational context, yet existing forecasters often treat them as isolated time series or rely on fixed covariate sets. We present TopoBrick, a training-free framework for zero-shot building IoT (Internet-of-Things) forecasting. TopoBrick uses building knowledge graphs to construct a compact structural skeleton and employs an agentic topology sampler to select target-specific exogenous variables. The selected variables ar...
  </details>

- **2026-07-07** — Amin Haeri, Mahdi Ghelichi — [Specification Grounding Drives Test Effectiveness for LLM Code](http://arxiv.org/abs/2607.06636v1)
  <details><summary>📄 Abstract</summary>
  Large language models frequently generate code that appears correct on typical inputs yet fails on edge cases, invalid inputs, and other specification-defined corner conditions. A popular fix has the model write its own tests and repair until they pass, but the source of the gain is unclear: does it come from the tests merely existing, or from their grounding in a specification of what the code should do? We isolate this factor. Holding the tester, test budget, and repair loop fixed, we change a...
  </details>

- **2026-07-07** — Grace Man Chen, Litao Guo, Yifan Wu et al. — [UI2App: Benchmarking Visual Interaction Inference in Executable Web Application Generation](http://arxiv.org/abs/2607.06306v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated growing competence in web page generation. However, existing text-driven approaches rely on complex prompts that impose substantial demands on users and offer limited expressivity for page layout and cross-page visual coherence. Image-driven paradigms, which take UI screenshots as input, align more closely with real development workflows. However, current benchmarks focus primarily on visual fidelity and lack a systematic evaluation of the interacti...
  </details>

- **2026-07-07** — Benjamin Marsh, Alejandro Ranchal-Pedrosa — [Slack and Budget Breaking in Threshold Team Production](http://arxiv.org/abs/2607.06197v1)
  <details><summary>📄 Abstract</summary>
  A threshold system completes a public task only after $κ$ verifiable shares are publicly committed. If the honest schedule creates \(   \Nstar=κ+Δ\) share opportunities by deadline $t^\star$, then $Δ$ shares are slack such that a coalition delays completion if and only if it withholds at least $Δ+1$ shares. The incentive problem is therefore to price the cheapest sabotage set. Agents receive a direct fee $f$ per committed share. A delaying coalition may also obtain delay value at most $L$, and m...
  </details>

- **2026-07-07** — Chenxu Wang, Yongkun Yang, Boyuan Du et al. — [LLM Agents for Deliberative Collaboration: A Study on Joint Decision Making Under Partial Observability](http://arxiv.org/abs/2607.06157v1)
  <details><summary>📄 Abstract</summary>
  Deliberation plays a crucial role in collaboration; when humans work together, they naturally engage in communication to align information and reach an agreement. In this paper, we investigate deliberative large language model (LLM) agents under partially observable joint decision-making tasks. We formalize deliberative collaboration as a cooperative joint decision problem with partial and asymmetric observations, and introduce a scalable benchmark that instantiates this problem across multiple ...
  </details>

- **2026-07-07** — Adrian Cosma — [Prompting Complexity: Shortest Prompts for Texts and Behaviors in LLMs](http://arxiv.org/abs/2607.06145v1)
  <details><summary>📄 Abstract</summary>
  In this paper, we define the quantity of prompting complexity: for a fixed instruction-tuned language model, what is the shortest plausible prompt that makes deterministic decoding produce a target text? It is an LM-relative analogue of resource-bounded Kolmogorov complexity: the prompt is a program, the model interface is the interpreter, and information omitted from the prompt is supplied by the model's weights, training distribution, tokenizer, template, and decoding rule. Unlike classical Ko...
  </details>

- **2026-07-07** — Hanan Gani, Tejal Kulkarni, Madhoolika Chodavarapu et al. — [RoboTALES: Learning Reasoning-Guided Robot Policies via Task-Aligned Simulated Futures](http://arxiv.org/abs/2607.06018v1)
  <details><summary>📄 Abstract</summary>
  Pretrained video generative models are promising backbones for visuomotor control, but their imagined futures often drift from task intent and are not reliably action-conditional. As a result, these models can be difficult to use for planning or policy extraction. To address these limitations, we propose RoboTALES, a single-stage framework that learns task-aligned simulated futures and uses them to train robot policies. Our approach introduces two key innovations: (1) a hierarchical LLM-based pl...
  </details>

- **2026-07-07** — Tomáš Sourada, Katia Vendrame, Jan Hajič — [Music I Care About: Automated Multimodal Benchmarking of LLM Music Perception Skills on (Almost) Any Music](http://arxiv.org/abs/2607.06015v1)
  <details><summary>📄 Abstract</summary>
  Music represents a cornerstone of human culture, existing digitally across diverse modalities, including audio, symbolic encodings (e.g., MIDI, MusicXML), and sheet music. Despite the advancement of Multimodal Large Language Models (MLLMs), current music benchmarks face three major limitations. First, large static benchmarks are resource-intensive to evaluate, and it remains unclear how their results transfer to diverse kinds of music beyond those included in the benchmark. Second, benchmarks cl...
  </details>

- **2026-07-07** — Yuhang Zhou, Kai Zheng, Haoling Li et al. — [TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training](http://arxiv.org/abs/2607.05804v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) trains a student policy by matching a stronger teacher on the student's own trajectories, offering a promising framework for language agent training. However, its application to long-horizon agentic tasks remains insufficiently explored. We identify two key inefficiencies in vanilla agent OPD: (1) full-horizon rollouts often waste wall-clock resources on tail turns that provide weak and noisy KL supervision, and (2) trajectory-level KL objectives concentrate most of ...
  </details>

- **2026-07-07** — Yake Wei, Yuan Wang, Fengyun Rao et al. — [Segmentation before Answering: Pixel Grounding for MLLM Visual Reasoning](http://arxiv.org/abs/2607.05798v1)
  <details><summary>📄 Abstract</summary>
  Recent advancements in Multimodal Large Language Models (MLLMs) have evolved from static perception to interleaved visual-language reasoning, often referred to as ``thinking with images''. A basic operation in this reasoning process is to zoom in on regions of interest (often represented with bounding boxes) to acquire finer visual details. In this paper, we propose \textbf{Seg}mentation before \textbf{Answer}ing (SegAnswer), which shifts the unit of zoom-in from the popular bounding box to pixe...
  </details>

- **2026-07-07** — Yan Chen, Weijing Tang, Jin-Hong Du — [AI-Augmented Statistical Network Estimation with Proxy Gene Embeddings](http://arxiv.org/abs/2607.05774v1)
  <details><summary>📄 Abstract</summary>
  Gene--gene networks are often observed only on a restricted target set, while modern biomedical foundation models provide proxy gene embeddings over substantially larger gene universes. To leverage externally learned representations to improve latent-structure recovery in partially observed target networks, we propose \emph{Proxy-Latent Assisted Network Estimation} (PLANE), an adaptively weighted joint network--embedding latent variable model. PLANE combines the two sources of information throug...
  </details>

- **2026-07-07** — Yimeng Zhang, Yingying Zhuang, Ziyi Wang et al. — [SpanUQ: Span-Level Uncertainty Quantification for Large Language Model Generation](http://arxiv.org/abs/2607.05721v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty estimation is essential not only for the trustworthy deployment of large language models (LLMs) but also as a foundation for self-refinement in LLM generation. However, existing approaches operate at suboptimal granularities: token-level scores lack semantic coherence, while sequence-level scores fail to localize errors. We formalize Span-Level Uncertainty Estimation (SLUE), a new task that targets the natural granularity for uncertainty: semantically coherent text spans, each convey...
  </details>

- **2026-07-07** — Zhiwei Yang, Yuanchen Wu, Nan Zhang et al. — [Scene Graph Thinking: Reinforcing Structured Visual Reasoning for Multimodal Large Language Models](http://arxiv.org/abs/2607.05716v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated strong perception and reasoning capabilities. However, most existing models focus on isolated objects and neglect structured relationships for efficient target navigation, limiting their performance on visually intensive tasks. To address this challenge, we introduce Scene Graph Thinking (SaGe), a novel paradigm that enables fine-grained and structured visual reasoning through explicit scene-graph representations. Specifically, we first ...
  </details>

- **2026-07-07** — Bowen Xue, Zihan Min, Xingyang Li et al. — [FourTune: Towards Fully 4-Bit Efficient Post-Training for Diffusion Models](http://arxiv.org/abs/2607.05711v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models have become a dominant paradigm for high-quality generative modeling, while post-training is essential for adapting them to diverse downstream applications. However, post-training of large diffusion models is still challenging due to the prohibitive memory footprints and slow training speed, which existing parameter-efficient fine-tuning methods only partially address. To overcome these limitations, we propose FourTune, an efficient post-training framework for diffusion models b...
  </details>

- **2026-07-07** — Inkyu Sa, Chanoh Park, Hea-Min Lee et al. — [Vision Language Action (VLA) Models for Unmanned Aerial Robotics and Bimanual Manipulation: A Review](http://arxiv.org/abs/2607.06706v1)
  <details><summary>📄 Abstract</summary>
  Vision Language Action (VLA) models unify visual perception, natural-language understanding, and action generation within a single foundation model, allowing a robot to follow instructions such as fold the towel or fly to the red building directly from camera images. Because VLAs inherit world knowledge from internet-scale pre-training, they have become the dominant framework for learning-based manipulation, with bimanual coordination serving as the most demanding testbed: two arms with 7 degree...
  </details>

- **2026-07-07** — Mike Roberts, Renhan Wang, Rushikesh Zawar et al. — [SPEAR: A Simulator for Photorealistic Embodied AI Research](http://arxiv.org/abs/2607.06701v1)
  <details><summary>📄 Abstract</summary>
  Interactive simulators have become powerful tools for training embodied agents and generating synthetic visual data, but existing photorealistic simulators suffer from limited generality, programmability, and rendering speed. We address these limitations by introducing SPEAR: A Simulator for Photorealistic Embodied AI Research. At its core, SPEAR is a Python library that can connect to, and programmatically control, any Unreal Engine (UE) application via a modular plugin architecture. SPEAR expo...
  </details>

- **2026-07-07** — Zeyuan Ding, Wenhai Liu, Yang Xu et al. — [Pelican-VLA 0.5: Attending Before Acting Benefits Generalization](http://arxiv.org/abs/2607.06655v1)
  <details><summary>📄 Abstract</summary>
  In this report, we present Pelican-VLA 0.5, a unified VLA model that integrates vision-language understanding, future-frame generation, and action prediction within a single architecture. Pelican-VLA 0.5 achieves attention-level generalization: without object annotations, segmentation masks, attention supervision, or task-specific fine-tuning, its action pathway already focuses on the instruction-relevant object and contact region. This behavior persists across unseen scenes and unseen robot emb...
  </details>

- **2026-07-07** — Zhuofan Zhang, Tianxu Wang, Guoxi Zhang et al. — [UniLM-Nav: A Unified Framework for Zero-Shot Last-Mile Navigation](http://arxiv.org/abs/2607.06537v1)
  <details><summary>📄 Abstract</summary>
  Mobile manipulation requires a robot to navigate to a target object or receptacle and then perform intended manipulation. However, reaching the vicinity of the target does not guarantee a manipulation-ready base pose, a problem known as last-mile navigation. Prior methods for last-mile navigation either rely on manual pose annotation or task-specific training, limiting their scalability to open-vocabulary settings with fine-grained spatial constraints. We propose UniLM-Nav, a unified framework f...
  </details>

- **2026-07-07** — Wei Wu, Fangjing Wang, Fan Lu et al. — [From Foundation to Application: Improving VLA Models in Practice](http://arxiv.org/abs/2607.06403v1)
  <details><summary>📄 Abstract</summary>
  Despite recent progress of VLA foundation models, the disparity between laboratory conditions and real-world applications continues to impede their practical implementation. To bridge this gap, we present LingBot-VLA 2.0, which advances LingBot-VLA through improvements in three functional domains. (1) Generalization across tasks and embodiments. Compared to the previous version, we revamp the data processing pipeline and curate around 60,000 hours of data for pretraining, including 50,000 hours ...
  </details>

- **2026-07-07** — Shuangxiang Kan, Shuanglong Kan, Sebastian Ertel — [Harnessing Code Agents for Automatic Software Verification](http://arxiv.org/abs/2607.06341v1)
  <details><summary>📄 Abstract</summary>
  Formal verification offers the strongest guarantee of software correctness, but it does not scale: the proofs demanded by interactive theorem provers such as Coq require enormous expert effort. Large language models (LLMs) promise to generate these proofs automatically, yet existing approaches wire a fixed, human-designed proof strategy into the system and constrain the model to follow it (retrieving premises and predicting tactics one step at a time, or splitting goals by divide-and-conquer), a...
  </details>

- **2026-07-07** — Yan Pan, Yuanchuan Ren, Chipui Chan et al. — [Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation](http://arxiv.org/abs/2607.06186v1)
  <details><summary>📄 Abstract</summary>
  Most quadruped loco-manipulation designs trade manipulation capability against stance. A trunk-mounted arm sits high and usually carries a single arm; using the legs as manipulators lifts the manipulating leg off the ground; and even leg-mounted grippers reach two-handed tasks only by rearing onto the hind legs. This paper integrates a manipulator with a prismatic slider, two revolute joints, and a gripper into each front calf of a Unitree Go2. The two arms grasp objects at ground level and mani...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Dakuo He — [LLM-Guided Measurement Credibility Correction for Trustworthy Industrial Process Inference](http://arxiv.org/abs/2607.06111v1)
  <details><summary>📄 Abstract</summary>
  Industrial prediction and soft sensing depend on credible input measurements. In field deployment, a predictor may receive biased, delayed, stale, or derived measurements that still look plausible. Prediction can then fail before the forecasting backbone becomes the main limitation, because the input window no longer represents the real process. Sensor reconstruction, data reconciliation, and fault-tolerant soft sensing reduce this risk, but they often rely on numerical correlation, alarms, faul...
  </details>

- **2026-07-07** — Shenbo Xie, Mingrui Cai, Xu Yang et al. — [SparseCtrl-HOI: Sparse Temporal Control for Human-Object Interaction Video Generation](http://arxiv.org/abs/2607.05994v1)
  <details><summary>📄 Abstract</summary>
  Human-Object Interaction (HOI) video generation aims to synthesize realistic videos of humans manipulating diverse objects, serving as a promising avenue for AI-driven live streaming e-commerce. A primary obstacle in this domain lies in the complexity of modeling fine-grained physical dynamics and the intricate spatial-temporal coordination between human hands and objects. Existing approaches to this problem typically rely on dense temporal guidance, e.g., frame-wise hand-object pose sequences, ...
  </details>

- **2026-07-07** — Lorenzo di Filippo, Enkeleda Bardhi, Andrea Agiollo et al. — [Beyond the Syntax: Do Security Experts Trust LLMs for NIDS Rule Engineering?](http://arxiv.org/abs/2607.05916v1)
  <details><summary>📄 Abstract</summary>
  As network threats evolve, manual NIDS rule engineering has become a critical operational bottleneck. While Large Language Models (LLMs) show promise for automating this process, their ability to produce production-ready rules remains unvalidated. This paper presents a human-centered investigation into LLM-based NIDS rule engineering, formalizing a grounded generation framework and evaluating it through a user study with 10 domain experts. Our evaluation reveals a syntax-semantics paradox: altho...
  </details>

- **2026-07-07** — Petar Djukic, Sudipta Acharya, Takai Eddine Kennouche et al. — [From Agentic to Autogenic Network Management for AI-Native 6G and Beyond: A Standards Perspective](http://arxiv.org/abs/2607.06786v1)
  <details><summary>📄 Abstract</summary>
  Standards bodies, including TM Forum, 3GPP, and ETSI, are converging on Agentic AI as the foundation for next-generation network management, where Large AI Model (LAM)-based agents autonomously interpret intent, coordinate resources, and adapt operational behaviors at runtime. However, achieving this vision at the scale and complexity of 6G networks requires management systems that can generate and evolve their own automation software during operation. We introduce Autogenic network management, ...
  </details>

- **2026-07-07** — Yoav Baron, Sara Dorfman, Roni Paiss et al. — [Analysis-by-Proxy: Localization Signals in VLMs Operating as Condition Encoders](http://arxiv.org/abs/2607.06445v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) are increasingly utilized as the conditioning backbone for diffusion-based image editing due to their remarkable multimodal reasoning capabilities. While standalone VLMs demonstrate strong localization capabilities, editing pipelines frequently struggle to maintain this accuracy, particularly in complex, multi-entity scenes. In this work, we investigate this performance gap, hypothesizing that it stems from treating the VLM as a condition encoder. In this role, the ...
  </details>

- **2026-07-07** — Yufan Wang, Anit Kumar Sahu, Yan Fei Ng et al. — [Finding H. pylori in the Fine Print: Evidence-Linked Multi-Agent Case Finding from Gastric Biopsy Reports](http://arxiv.org/abs/2607.06435v1)
  <details><summary>📄 Abstract</summary>
  Data from Singapore indicated that about 31% of the population had evidence of Helicobacter pylori infection. Persistent H. pylori infection is associated with chronic active gastritis and peptic ulcer disease, and its eradication is key to gastric cancer prevention. However, evidence supporting \textit{H. pylori} positivity and H. pylori-associated gastritis may be distributed across heterogeneous coded and free-text report fields and may require contextual interpretation of assertion and negat...
  </details>

- **2026-07-07** — J. Pedra — [Understanding Small-Signal Impedance Matrices in Different Reference Frames](http://arxiv.org/abs/2607.06416v1)
  <details><summary>📄 Abstract</summary>
  This paper systematically analyzes the relationships among the $dq$-domain, $αβ$-domain, and sequence-domain representations used in small-signal impedance modeling of voltage-source converters (VSCs). It is shown that the AC impedance matrix expressed with $dq$-complex and $αβ$-complex variables leads to different formulations in the sequence domain. The study demonstrates that asymmetric systems exhibit different physical phenomena in the rotating and stationary reference frames; therefore, th...
  </details>

- **2026-07-07** — Felix Feldman, Joshua Harris, Timothy Laurence et al. — [Healthier LLMs: Retrieval-Augmented Generation for Public Health Question Answering](http://arxiv.org/abs/2607.06641v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) achieve promising results on medical question answering benchmarks, yet their use in public health is constrained by hallucinations and the rapid evolution of official guidance. Retrieval-Augmented Generation (RAG) mitigates these risks by grounding responses in an explicitly maintained corpus, but end-to-end performance depends critically on retrieval configuration and on evaluation beyond multiple-choice formats. We extend PubHealthBench, a question answering (QA) ...
  </details>

- **2026-07-07** — Sonali Brahma, Trishna Kalita, Himangshu Prabal Goswami — [Coherence Estimation Beyond the Liouvillian Gap in a Finite Nonequilibrium System](http://arxiv.org/abs/2607.06215v1)
  <details><summary>📄 Abstract</summary>
  We investigate the estimation of bath-induced coherence in a finite quantum system interacting with thermal reservoirs. Enhancement of coherence estimation is transient and the estimation precision totally disappears at the steady state despite the system retaining finite coherence. By analyzing the full Liouvillian eigenspectrum, we demonstrate that the optimal sensing window emerges from the competition between identifiable contributory modes' temporal relaxation and statistical importance. Ne...
  </details>

- **2026-07-07** — Youcheng Zong, Runda Jia, Ranmeng Lin et al. — [Open-Ended Scenario Reasoning for Specialist Model Adaptation](http://arxiv.org/abs/2607.06625v1)
  <details><summary>📄 Abstract</summary>
  Process industries have accumulated validated specialist models, yet sensor drift, feedstock variation, and regime switching cause these models to degrade systematically in new scenarios. Collecting new labeled data and retraining is costly, while continuing with the original model incurs persistent bias. Existing adaptation methods require modifying model parameters with sufficient labeled data, making rapid response on deployed systems difficult. Using LLMs as direct predictors risks hallucina...
  </details>

- **2026-07-07** — Huzaifa Ejaz, Fabian C. Peña, Steffen Herbold — [Large Language Models Have Unreliable Understanding of Software Engineering Terminology](http://arxiv.org/abs/2607.06004v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are increasingly used in software engineering (SE), yet there is no systematic study that determines to which degree these LLMs actually understand standardized SE terminology. Lack of such understanding can lead to miscommunication and misunderstanding, both by LLMs consuming text but also by human-developers acting on LLM-generated text. Within this paper, we investigate to which degree state-of-the-art LLMs are able to identify whether definitions from the ISO/IEC...
  </details>

- **2026-07-07** — Fabian C. Peña, Steffen Herbold — [Pre-Training on Software Engineering Texts: Effects on Domain Adaptation and General-Language Understanding](http://arxiv.org/abs/2607.06613v1)
  <details><summary>📄 Abstract</summary>
  Generalist and code-focused Language Models (LMs) are increasingly applied to software engineering (SE), yet whether they are optimized for understanding SE textual artifacts (e.g., issues, commit messages, developer discussions) remains unclear, as most evidence comes from code-focused benchmarks. We study how to adapt encoder and decoder LMs to SE text, comparing continual pre-training (CPT) against pre-training from scratch (PTS) on a new SE corpus, and evaluating both domain adaptation (SELU...
  </details>

- **2026-07-07** — Krittanon Kaewtawee, Petmongkon Pornpichitsuwan, Natchaya Temyingyong et al. — [InfluMatch: Frontier-Quality KOL Search at 4B-Model Cost](http://arxiv.org/abs/2607.05968v1)
  <details><summary>📄 Abstract</summary>
  Matching influencers (KOLs) to free-form, multi-part Thai marketing criteria is today served either by keyword search over structured profiles, which misses semantic fit, or by prompting frontier LLMs over every candidate, which is accurate but slow and expensive. We present InfluMatch, a low-cost three-stage cascade -- retrieval $\rightarrow$ rerank $\rightarrow$ reason -- built entirely from small open-weight models: dense retrieval returns 50 candidates, a 4B pointwise reranker scores each by...
  </details>

- **2026-07-07** — Yakun Liu, Zhiyu Jin, Hai Luan et al. — [From Textural Counterpoint to Feature Encoding: A Multi-Dimensional Machine Representation Study of Haydn's "The Lark" Integrating Electroacoustic Analysis](http://arxiv.org/abs/2607.05902v1)
  <details><summary>📄 Abstract</summary>
  Chamber music, as a highly precise multi-part interactive system, contains a logic of "role assignment and dynamic interaction" that provides an extremely valuable blueprint for exploring human-computer collaborative composition paradigms. Addressing the lack of role perception capabilities in existing deep music generation models during polyphonic interactions, this paper conducts an interdisciplinary analysis of Haydn's String Quartet in D Major, The Lark (Op. 64, No. 5). We propose a novel re...
  </details>

- **2026-07-07** — Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu — [Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts](http://arxiv.org/abs/2607.06611v1)
  <details><summary>📄 Abstract</summary>
  Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated v...
  </details>

- **2026-07-07** — Guang Yang, Brian Siyuan Zheng, Victoria Ebert et al. — [LEGATO 2: Toward Multimodal Sheet Music Recognition and Understanding](http://arxiv.org/abs/2607.05769v1)
  <details><summary>📄 Abstract</summary>
  We propose a novel pipeline, Legato 2, for extracting symbolic notation and semantic knowledge from images of sheet music. Legato 2 features the first large-scale neural model for optical music recognition (OMR) to operate sequentially on a system-by-system basis, following the horizontal lines of notation as they are read on the page, rather than treating the page as an undifferentiated image, enabling better scaling to arbitrarily long inputs. It is also the first OMR model capable of generati...
  </details>

- **2026-07-07** — Zihan Wang, Seungjun Lee, Yinghao Xu et al. — [Image2Sim: Scaling Embodied Navigation via Generative Neural Simulator](http://arxiv.org/abs/2607.05765v1)
  <details><summary>📄 Abstract</summary>
  Embodied navigation aims to build agents that interpret multimodal goals, reason in 3D space, and reach target destinations reliably in the real world. However, progress remains constrained by the lack of scalable, high-fidelity, and physically grounded interactive environments. Although real-world scanned datasets offer visual realism, they are limited by scale. In contrast, synthetic simulators scale more easily but often exhibit large sim-to-real gaps. We introduce Image2Sim, a real-time neur...
  </details>

- **2026-07-07** — Mahmoud Hany, Mourad ElSheraey, Mahmoud Said et al. — [Inject or Navigate? Token-Efficient Retrieval for LLM Analysis of Transactional Legal Documents](http://arxiv.org/abs/2607.05764v1)
  <details><summary>📄 Abstract</summary>
  Answering questions over a set of transactional legal documents is most simply done by injecting the whole corpus into the LLM's context window on every query. That baseline maximises retrieval recall, but its token footprint scales with the corpus rather than the question, and long-context degradation scales with it. We report what it took to replace full-corpus injection in a legal-document analysis system, comparing it against two structured retrieval modes over our proprietary structure-awar...
  </details>

- **2026-07-06** — Sai Varun Kodathala — [aiAuthZ: Off-Host, Identity-Bound Authorization for AI Agents](http://arxiv.org/abs/2607.05518v1)
  <details><summary>📄 Abstract</summary>
  AI agents issue tool calls on the basis of text they cannot verify, so any party who controls part of the context can forge the appearance of authority. I evaluate 15 contemporary language models against eight attack scenarios derived from a published corpus of real agent incidents and find that refusal varies from 100% down to 38% across fully evaluated models; the most expensive model refused only half of the attacks despite a twentyfold price spread. I present aiAuthZ, an authorization gatewa...
  </details>

- **2026-07-06** — Mouhamed Amine Bouchiha, Gregory Blanc — [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](http://arxiv.org/abs/2607.05001v2)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost...
  </details>

- **2026-07-06** — Honglin Wang, Shiyao Pan, Yun-Fu Liu — [IMR: Iterative Mode-World Weighted Regression for Multi-Agent Trajectory Prediction](http://arxiv.org/abs/2607.05705v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent motion prediction is essential for automated vehicles to understand the intentions of surrounding vehicles. However, previous prediction-based and anchor-based methods have limitations in mode diversity and prediction accuracy, respectively. These limitations may cause inadequate safety assessments and behavioral deviations in automated vehicles. To address this issue, a mode-world weighted regression loss is proposed to bridge the gap between these features. Specifically, this appro...
  </details>

- **2026-07-06** — Youssef Abdelsalam, Norman Peitek, Anna-Maria Maurer et al. — [A Mechanistic Lens on Semantic Conflicts: Using Activation Patching to Understand LLM Behavior](http://arxiv.org/abs/2607.05587v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used in software-engineering tasks processing executable code and non-executable semantic cues such as comments or identifiers. These two sources can conflict when semantic cues suggest different program behavior than the code itself. It remains unclear how such semantic conflicts affect LLM behavior and which source dominates their outputs.   We present the first controlled, mechanistic study of LLM behavior under semantic conflicts. To this end, we...
  </details>

- **2026-07-06** — Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson et al. — [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](http://arxiv.org/abs/2607.05217v2)
  <details><summary>📄 Abstract</summary>
  Public institutions increasingly use large language models (LLMs) to answer citizens' questions, often pairing a curated knowledge base with live web search, yet whether the sources behind these answers can be trusted has received little empirical scrutiny. We report a pre-launch expert evaluation of Evrópuvefur, an independent, government-funded service run by the University of Iceland that answers questions about the European Union, conducted as Iceland prepared for its referendum of 29 August...
  </details>

- **2026-07-06** — Yuan Jiang, Ningyuan Zhang, Xicun Yang et al. — [Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control](http://arxiv.org/abs/2607.04837v2)
  <details><summary>📄 Abstract</summary>
  Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient ex...
  </details>

- **2026-07-06** — Hairui Zhu, Yiying Yang, Tengjin Weng et al. — [CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration](http://arxiv.org/abs/2607.05465v1)
  <details><summary>📄 Abstract</summary>
  Complex image creation and editing often require more than a single generation or editing model. A user request may involve synthesizing images, localizing objects, segmenting regions, editing selected content, compositing intermediate assets, reading text, and enhancing the final result. Such tasks shift multimodal agents from perception-augmented reasoning to manipulation-centered visual creation, where tools must actively transform visual states rather than merely inspect them. However, exist...
  </details>

- **2026-07-06** — Mohammad Zeineldeen, Albert Zeyer, Haoran Zhang et al. — [Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition](http://arxiv.org/abs/2607.05612v1)
  <details><summary>📄 Abstract</summary>
  Language model (LM) perplexity (PPL) has historically been used as a proxy for automatic speech recognition (ASR) word error rate (WER), with prior work reporting an approximately linear relation in log-log space. Modern end-to-end ASR systems challenge this assumption because they already contain internal language modeling capacity, are often evaluated without external language models, and can now be combined with neural LMs and large language models (LLMs) through different recognition strateg...
  </details>

- **2026-07-06** — Alvin Wang, Jaromir Savelka — [Prompting Beats Fine-Tuning: Generative Expected Value Scoring for Statutory Term Retrieval](http://arxiv.org/abs/2607.05582v1)
  <details><summary>📄 Abstract</summary>
  Legal concepts in statutes are often expressed using vague terms, and practitioners frequently turn to case law to interpret them. We study the task of ranking case-law sentences by their usefulness for explaining a concept or target statutory term, using an established dataset of 26,959 sentences covering 42 U.S. Code concepts labeled into four explanatory-value categories. We compare two families of methods: (i) supervised fine-tuning of encoder-only models (ModernBERT) and (ii) zero-shot prom...
  </details>

- **2026-07-06** — Francesco Bilotta, Luca Braghieri, Collin Raymond et al. — [Agreement and Diversity in Interpretation](http://arxiv.org/abs/2607.05558v1)
  <details><summary>📄 Abstract</summary>
  We study joint decision-making when agents agree on all primitives other than signal likelihoods. We propose a decision-theoretic measure of interpretive disagreement: a pair of subjective models is more agreeable than another if, uniformly across decision problems, it supports a larger set of signal-contingent plans that both agents weakly prefer ex-ante to the common reservation payoff. We show that this measure is prior independent and can be represented as an inclusion preorder over pairs of...
  </details>

- **2026-07-06** — Haonan Huang — [The yes-no bias of large language models reflects answer order and wording, not shifts in moral judgment](http://arxiv.org/abs/2607.05552v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) increasingly issue judgments read as binary verdicts, and a growing literature reports such judgments shifting under logically irrelevant changes of wording - among them an amplified yes-no bias on moral dilemmas, absent in humans. A single framing cannot say what such a shift is: in a yes/no question the word "no" is at once logical verdict, lexical token, and last-printed option. We introduce a psychometric battery that separates these: crossed symmetrization - eve...
  </details>

- **2026-07-06** — Mouhamed Amine Bouchiha, Gregory Blanc — [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligence Knowledge Graph Construction](http://arxiv.org/abs/2607.05001v1)
  <details><summary>📄 Abstract</summary>
  Cyber Threat Intelligence (CTI) reports are predominantly unstructured, heterogeneous, and noisy, which limits their direct usability for automated analysis and reasoning. Cybersecurity Knowledge Graphs (CSKGs) provide a structured representation of adversarial entities, actions, and relations, but constructing such graphs from free-text CTI remains a challenge. Recent approaches rely on monolithic Large Language Models (LLMs) to perform end-to-end extraction and completion, leading to high cost...
  </details>

- **2026-07-06** — Xue Qin, Simin Luan, Cong Yang et al. — [Governed Caste Reassignment in Heterogeneous Swarms: An Asymmetric-Trust Protocol with Audited Operator Countersignature](http://arxiv.org/abs/2607.04634v1)
  <details><summary>📄 Abstract</summary>
  In heterogeneous robot swarms, caste reassignment (rebinding a robot to a new capability-bound role) is a high-frequency runtime event driven by battery, payload, and priority changes. Existing approaches treat it as an internal allocation algorithm and do not expose the reassignment to external authority. We argue that for regulated embodied deployments a caste change that elevates a robot's privilege envelope is a governance event that must be auditable and externally authorised. We propose an...
  </details>

- **2026-07-06** — Jiaqi Peng, Xiqian Yu, Delin Feng et al. — [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](http://arxiv.org/abs/2607.05377v1)
  <details><summary>📄 Abstract</summary>
  While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable ...
  </details>

- **2026-07-06** — Sensen Gao, Zhaoqing Wang, Qihang Cao et al. — [PixWorld: Unifying 3D Scene Generation and Reconstruction in Pixel Space](http://arxiv.org/abs/2607.05373v1)
  <details><summary>📄 Abstract</summary>
  3D reconstruction and generation are commonly tackled by separate paradigms: pixel-based regression for reconstruction, and latent diffusion for generation. Recent works attempt to unify them in latent space, but with notable drawbacks: the diffusion objective is defined on latent features rather than the underlying 3D representation, and both branches suffer from information loss introduced by latent encoding, while requiring a pretrained Variational Autoencoder (VAE) or Representation Autoenco...
  </details>

- **2026-07-06** — Xianhao Chen, Jiarui Hu, Yuanbo Yang et al. — [Beyond Isolated Objects: Relationship-aware Open Vocabulary Scene Understanding via 3D Scene Graph Analysis](http://arxiv.org/abs/2607.05348v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary 3D scene understanding aims to segment 3D scenes beyond predefined categories by transferring semantic knowledge from vision-language models. Existing methods have advanced this task by lifting language-aligned 2D features into 3D, yet they often rely on context-independent semantic representations, leaving object relationships underexplored for contextual refinement. We propose RelGraphOV, a relationship-aware framework that uses 3D scene graphs to enhance open-vocabulary 3D und...
  </details>

- **2026-07-06** — B. C. Low, S. W. McIntosh — [The steady incompressible ideal free-boundary flows of a hydromagnetic star](http://arxiv.org/abs/2607.05299v1)
  <details><summary>📄 Abstract</summary>
  This self-contained theoretical study treats incompressible, free-boundary flows in a gravitating, ideal hydromagnetic star abutting vacuum, centered on the steady field-aligned flows of Chandrasekhar, Prendergast and Tsinganos, together with a novel family of steady cross-field flows, all as solutions of the axisymmetric Tsinganos equation. In the absence of compressive waves and shocks, an incompressible fluid evolves by its frozen-in magnetic field propagating as transverse Alfvèn waves along...
  </details>

- **2026-07-06** — Avina Nakarmi, Sohom Sen, Xun Song et al. — [A Multimodal Reasoning Typology for Grounding Chart-Image Coherence in Science Communication](http://arxiv.org/abs/2607.05222v1)
  <details><summary>📄 Abstract</summary>
  Charts and images appear together throughout scientific publications, yet most computational work does not characterize their coherence. We argue that a chart, its accompanying image, and the caption that links them form a multimodal unit, and that the inferential work required to read it varies systematically. To capture this variation, we develop a typology of reasoning gaps, R1 through R5, that characterizes how chart, image, and text jointly convey a scientific claim, and the interpretive wo...
  </details>

- **2026-07-06** — Hafsteinn Einarsson, Hafsteinn Birgir Einarsson, Jón Gunnar Ólafsson et al. — [Curated retrieval versus open web search in public AI information services: a coverage-trust trade-off](http://arxiv.org/abs/2607.05217v1)
  <details><summary>📄 Abstract</summary>
  Public institutions increasingly use large language models (LLMs) to answer citizens' questions, often pairing a curated knowledge base with live web search, yet whether the sources behind these answers can be trusted has received little empirical scrutiny. We report a pre-launch expert evaluation of Evrópuvefur, an independent, government-funded service run by the University of Iceland that answers questions about the European Union, conducted as Iceland prepared for its referendum of 29 August...
  </details>

- **2026-07-06** — Xingze Gao, Chuanrui Hu, Hongda Chen et al. — [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](http://arxiv.org/abs/2607.05202v1)
  <details><summary>📄 Abstract</summary>
  Agent self-evolution in long-horizon LLM systems is largely procedural: useful experience is not merely stored information, but reusable procedures for searching, debugging, and verification. Yet current evaluations do not isolate this form of transfer. Agent benchmarks test single-episode task solving; memory benchmarks target information retention rather than procedural reuse. We introduce EvoAgentBench, a benchmark for agent self-evolution via Ability-guided transfer across four agentic domai...
  </details>

- **2026-07-06** — Tianjia Yang, Ke Li, Ruwen Qin et al. — [VLM-CASE: Vision-Language Model Enabled Context-Adaptive Safety Envelopes for Anticipatory Safe Autonomous Driving](http://arxiv.org/abs/2607.05180v1)
  <details><summary>📄 Abstract</summary>
  Adverse driving conditions, such as bad weather, remain a principal barrier to autonomous driving because they degrade two things at once: what the vehicle can perceive and what it can physically do. Human drivers cope by anticipation, reasoning about the scene and re-budgeting speed, following distance, and steering before grip or sight is lost, whereas current autonomous driving systems at best react after the fact. This paper proposes VLM-CASE, a framework that gives an autonomous vehicle thi...
  </details>

- **2026-07-06** — Yurui Dong, Shu Zou, Siqi Li et al. — [ASSEMCAD: Production-Ready CAD Assembly Generation from Natural Language](http://arxiv.org/abs/2607.05123v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in large language models and programmatic CAD have significantly improved Text-to-CAD generation for individual parts. However, production-ready mechanical assembly generation remains largely unsolved. Unlike single-part modeling, assemblies require coordinated reasoning over multiple components, functional interfaces, assembly relations, engineering principles, and physical consistency. Consequently, directly generating executable CAD code is insufficient for constructing mechan...
  </details>

- **2026-07-06** — Handong Li, Longteng Guo, Zikang Liu et al. — [TimeThink: Reasoning with Time for Video LLMs](http://arxiv.org/abs/2607.05089v1)
  <details><summary>📄 Abstract</summary>
  Video reasoning requires models to identify and verify temporally localized evidence within long video sequences. Recent Video Large Language Models (Video-LLMs) have shown promising reasoning abilities when aligned with reinforcement learning, yet existing approaches typically rely on outcome-based rewards that supervise only the final prediction. Such supervision provides limited guidance on how models should discover the relevant temporal evidence during intermediate reasoning. In this work, ...
  </details>

- **2026-07-06** — Saimir Bala, Fabiana Fournier, Lior Limonad et al. — [Using Process Mining to Generate AI Agents from Software Engineering Process Records](http://arxiv.org/abs/2607.04948v1)
  <details><summary>📄 Abstract</summary>
  Integrating AI agents into Software Engineering (SE) raises an important challenge: how can we specify and realize AI agents that work effectively alongside humans in hybrid SE teams? Determining the right granularity and separation of concerns for such agents is non-trivial. Coarse-grained agents may introduce unmanageable complexity, whereas micro-agents may create severe coordination overhead. Moreover, existing multi-agent SE frameworks typically rely on predefined role structures and do not...
  </details>

- **2026-07-06** — Yoshiyuki Ootani — [Input Pathways Shape Few-Shot, Not Zero-Shot, Binding in Tiny Transformers: A Fully-Enumerable Study](http://arxiv.org/abs/2607.04926v1)
  <details><summary>📄 Abstract</summary>
  How does the way information reaches a transformer -- as symbolic tokens, a clean per-factor "oracle" code, or an entangled perceptual vector -- shape whether it binds that information compositionally? We study ~6-10K-parameter transformers on finite factored worlds enumerated exhaustively, so every measurement covers the whole input space (zero sampling variance) and the informative routes are information-matched (exact Bayes ceiling 1.0). We report four findings. (1) Endpoint invariance: on he...
  </details>

- **2026-07-06** — Mohammed Saim Ahmed Quadri, Yunzhe Xue, Justin W. Ady et al. — [Medi-Gemma: A Hybrid Clinical Decision Support System Integrating Deterministic EMR Analytics and Retrieval-Augmented Generation](http://arxiv.org/abs/2607.04907v1)
  <details><summary>📄 Abstract</summary>
  Deploying Large Language Models (LLMs) in high-stakes clinical settings remains limited by structural hallucinations, weak deterministic reasoning over tabular patient data, and omissions in vector retrieval. This paper presents the architecture and validation of Medi-Gemma, a Clinical Decision Support System (CDSS) for wound pathology triage and workflow automation. The platform introduces a decoupled framework that separates clinical perception from data orchestration while preserving traceabl...
  </details>

- **2026-07-06** — Ming-Kuan Lin, Yi-Chung Lai, Ming-Hsin Chiang et al. — [RL-Ballast: Ship Ballast Water Path Planning and Clog Prediction via Reinforcement Learning](http://arxiv.org/abs/2607.04906v1)
  <details><summary>📄 Abstract</summary>
  Under the Shipping 4.0 paradigm, autonomous and reduced-crew vessels require intelligent internal systems to maintain operational safety and structural stability. Ballast-water control is essential for ship trim and integrity, but conventional rule-based or manual approaches have limited adaptability to hydraulic anomalies such as valve failures and pipe blockages, and often depend on dense pressure or flow sensors for diagnosis. To address these limitations, this paper proposes RL-Ballast, a gr...
  </details>

- **2026-07-06** — Yuan Jiang, Ningyuan Zhang, Xicun Yang et al. — [Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control](http://arxiv.org/abs/2607.04837v1)
  <details><summary>📄 Abstract</summary>
  Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient ex...
  </details>

- **2026-07-06** — Tianhao Niu, Qingfu Zhu, Wanxiang Che — [What You See Is What You Get: Observation-Aligned Supervision for Chart-to-Code Generation](http://arxiv.org/abs/2607.04726v1)
  <details><summary>📄 Abstract</summary>
  Chart-to-code generation is commonly trained with supervised fine-tuning on reference plotting scripts, implicitly treating the gold code as a fully observable target. We argue that this assumption is often invalid: many chart programs contain latent raw variables that cannot be uniquely recovered from the rendered image. For example, a boxplot exposes summary statistics rather than original samples, a pie chart reveals proportions rather than arbitrary raw values, and a histogram shows bin-leve...
  </details>

- **2026-07-06** — Daeyeon Son — [Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes](http://arxiv.org/abs/2607.04668v1)
  <details><summary>📄 Abstract</summary>
  On-device LLM decoding is a hard-barriered CPU-SIMD computation that wants every core for milliseconds per token, while the rest of the OS wants those same cores continuously. A barriered gang cannot simply be dropped into a preemptive scheduler: an unannounced departure deadlocks a barrier, and an unannounced arrival silently corrupts logits. I present the elastic gang of Anima OS, a bare-metal x86-64 Rust kernel in which the inference gang is a first-class schedulable entity whose core members...
  </details>

- **2026-07-06** — Shuangyu Xie, Kaiyuan Chen, Ziyang Chen et al. — [RoboVista: Evaluating Vision Language Models for Diverse Robot Applications](http://arxiv.org/abs/2607.04610v1)
  <details><summary>📄 Abstract</summary>
  Diverse applications for robotics, such as industry and agriculture, require robots to operate across various embodiments, changing visual conditions, and complex planning. Vision-Language Models (VLMs) offer a promising foundation for general-purpose and interpretable robotic reasoning. Aligning VLMs with diverse robot applications requires a modular understanding of the individual decision components that underlie robotic behavior. Capturing such structure is challenging for conventional robot...
  </details>

- **2026-07-06** — Yang Zhou, Jianwen Chen, Ruipeng Wei — [Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets](http://arxiv.org/abs/2607.05141v1)
  <details><summary>📄 Abstract</summary>
  We study a minimal agent-based market in which a single evolutionary-optimized institutional agent interacts with 20{,}000 herding retail traders. The agent spontaneously discovers a multi-cycle predatory strategy, producing 8--11 complete cycles over 2000 trading days with total portfolio return of $+51\%$ (best of 20 seeds; mean $+37.7\%$). Mean-field reduction maps the system onto a nonlinear oscillator that undergoes two distinct bifurcations: a continuous Hopf transition as institutional ca...
  </details>

- **2026-07-06** — Amal Akli, Melissa Akli, Cedric Richter et al. — [From Failing to Passing: Evolving Natural Language Prompt Optimization Rules for LLM Code Generation](http://arxiv.org/abs/2607.05121v1)
  <details><summary>📄 Abstract</summary>
  Large language models are known to be sensitive to prompt formulation. Even minor variations in wording can substantially degrade performance. This sensitivity reveals an opportunity: if prompt phrasing can harm performance, can it be used to improve it? To investigate this question, we introduce a search-based approach that identifies and evolves a set of natural language transformation rules with strong downstream effects on coding performance. We then propose DUALFIX, a staged repair pipeline...
  </details>

- **2026-07-06** — Nikolaos Xiros, Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos — [Knowledge Knows, Verbalization Tells: Disentangling Latent Directions for Mathematical Solvability in LLMs](http://arxiv.org/abs/2607.05013v1)
  <details><summary>📄 Abstract</summary>
  Although LLMs have made significant progress in mathematical reasoning, determining whether a mathematical problem is solvable remains a fundamental yet challenging capability. While recent studies have probed internal representations of model solvability beliefs, verbalization has primarily been studied behaviorally rather than as an internal representation, limiting its analysis and manipulation. We address this gap by separately probing representations of solvability knowledge and verbalizati...
  </details>

- **2026-07-06** — Jian Zhu, Jianjun Zhang, Taiyi Su et al. — [DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation](http://arxiv.org/abs/2607.04927v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted i...
  </details>

- **2026-07-06** — Yu Wang, Yong Cao, Kan Dai et al. — [Enhancing the Forecasting Capability of Multi-Model Blending Algorithms for Extreme Precipitation via Joint Use of Station and Gridded Observations](http://arxiv.org/abs/2607.04862v1)
  <details><summary>📄 Abstract</summary>
  Accurate extreme precipitation forecasting is critical for disaster mitigation but remains challenging for numerical weather prediction (NWP) models due to systemic intensity underestimation and spatial displacement. Traditional precipitation multi-model blending algorithms perform pixel-by-pixel blending on the forecast field based on weights, which may lead to the expansion of precipitation areas and the smoothing of extreme values. This study proposes an U-Net based two-stage framework: proba...
  </details>

- **2026-07-06** — Antonio Franchi — [Aerial Manipulation: Contact, Medium Coupling, and the Geometry of Readiness](http://arxiv.org/abs/2607.04719v1)
  <details><summary>📄 Abstract</summary>
  Aerial robots are increasingly moving from remote observation toward physical interaction with objects, surfaces, structures, loads, and surrounding flows. This review argues that aerial manipulation cannot be understood as classical manipulation simply mounted on a flying base. Because flying agents remain aloft through continuous momentum and energy exchange with the surrounding medium, support, locomotion, stabilization, and task-directed interaction are intrinsically coupled. Building on bro...
  </details>

- **2026-07-06** — Xinyu Shao, Keru Zhou, Guowei Huang et al. — [KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation](http://arxiv.org/abs/2607.04652v1)
  <details><summary>📄 Abstract</summary>
  Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinem...
  </details>

- **2026-07-06** — Theodore O. Cochran — [Progressive Disclosure for LLM-Maintained Wiki Knowledge Bases: a Preregistered Ablation](http://arxiv.org/abs/2607.04576v1)
  <details><summary>📄 Abstract</summary>
  LLM agents increasingly answer questions against knowledge bases they help maintain. A common intuition holds that progressive disclosure, a compact catalog plus a one-line summary per page so the agent loads only what it needs, should make this cheaper than consulting a large monolithic index. We test that on a real 709-page markdown wiki maintained by an LLM. We retrofit it for progressive disclosure and run a preregistered ablation in which four versions of the corpus differ only in how the a...
  </details>

- **2026-07-06** — Mohamed Amine Merzouk, Dmitri Carpov, Mirko Bronzi et al. — [How Much is Left? LLMs Linearly Encode Their Remaining Output Length](http://arxiv.org/abs/2607.05316v1)
  <details><summary>📄 Abstract</summary>
  Large language models generate one token at a time, yet their responses show remarkably consistent length structure: step-by-step solutions converge in predictable token counts, retrievals stop after a few sentences, retractions extend responses by measurable amounts. We ask whether the model carries an internal estimate of how much response remains. Training minimal-capacity linear probes on frozen hidden states of three open-weight 7-8B models across seven completion-style datasets, we find th...
  </details>

- **2026-07-06** — Guli Zhu, Chenwei Wu, Liyue Shen — [Evaluating and Understanding Model Editing for Medical Vision Language Models](http://arxiv.org/abs/2607.05310v1)
  <details><summary>📄 Abstract</summary>
  Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmarks focus on general-purpose tasks and do not reflect realistic clinical domain requirements and variability. To address this, we introduce M3Bench, a clinically grounded benchmark for multimodal model editing that evaluates whether an edit remains reliable, precise, and generalizable under the challe...
  </details>

- **2026-07-06** — Guorun Wang, Simone Foti, Andreas D. Demou et al. — [Air Quality Downscaling with Station-Guided Pseudo-Supervision](http://arxiv.org/abs/2607.05292v1)
  <details><summary>📄 Abstract</summary>
  Super-resolving coarse atmospheric fields to local PM$_{2.5}$ variations is uniquely challenged by a mismatch in spatial support: while pixels represent regional averages, ground-truth observations are discrete, unaligned samples of a continuous spatial signal. To bridge this gap, we present a station-guided framework for high-resolution PM$_{2.5}$ downscaling over Europe. Taking coarse CAMS atmospheric composition fields alongside heterogeneous side information (i.e., human activity, land cover...
  </details>

- **2026-07-06** — Alessio Brini — [Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks](http://arxiv.org/abs/2607.05291v1)
  <details><summary>📄 Abstract</summary>
  We ask whether pretrained time series foundation models (TSFMs) improve on established econometric benchmarks for forecasting realized volatility. Using the VOLARE dataset, we conduct the first systematic comparison of nine zero-shot TSFMs against eight econometric specifications, including the Heterogeneous Autoregressive (HAR) family, across 50 assets in equities, foreign exchange, and futures, and three forecast horizons, with formal pairwise and multi-model forecast-comparison tests. Foundat...
  </details>

- **2026-07-06** — Parth Upman, Nishita Jain, Shreyank N Gowda — [Erasing Without Collateral Damage: Precise Concept Removal in Diffusion Models](http://arxiv.org/abs/2607.05274v1)
  <details><summary>📄 Abstract</summary>
  Training-free concept erasure is an attractive mechanism for controlling text-to-image diffusion models, but precise erasure often comes at the cost of damaging semantically related non-target concepts. Existing value-space methods remove the component of each cross-attention value along the target concept direction, implicitly treating target identity and shared visual structure as the same signal. We argue that this is the source of much of the collateral damage in prior preservation. We intro...
  </details>

- **2026-07-06** — Mohamed Shalma, Amr Mansour, Ahmed El-Mahdy — [Optimal Base Station Placement for Beyond 5G Networks with Non-Convex Topology](http://arxiv.org/abs/2607.05210v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the optimal placement of a millimeter-wave (mmWave) base station (BS) within a realistic U-shaped environment with non-convex topology. The problem is challenging and NP-hard due to the non-convex topology and the non-convex objective functions which are the sum-rate maximization and max-min fairness, the latter being additionally non-smooth. To address this challenge, the BS placement is formulated as a Markov Decision Process (MDP). Then, we propose two deep reinforceme...
  </details>

- **2026-07-06** — André Silva, Han Tu, Martin Monperrus — [Latent Programming Horizons in Coding Agents](http://arxiv.org/abs/2607.05188v1)
  <details><summary>📄 Abstract</summary>
  A coding agent solving a software-engineering task spends dozens of steps reasoning, editing code, and running tests, yet little is known about what the underlying language model internally represents about the program it is working on. We show that the residual streams of language models under coding agents linearly encode properties of the evolving program: a logistic-regression probe on hidden states is able to decode whether the current code parses, passes its test suite, reduces the number ...
  </details>

- **2026-07-06** — Omer Moussa, Mariya Toneva — [RABBiT: Rapidly adaptive BOLD foundation model via brain-tuning for accurate zero-shot and few-shot prediction of speech-elicited responses in the brain](http://arxiv.org/abs/2607.05171v1)
  <details><summary>📄 Abstract</summary>
  Language understanding in the brain is context-dependent, varying across experimental stimuli and individuals, which makes it difficult to build computational models that generalize across both. This calls for a foundation model of language-evoked brain activity that can capture shared structure while adapting efficiently to new participants and inputs. We introduce RABBiT (Rapidly Adaptive BOLD foundation model via BraIn-Tuning), a compact audio-to-fMRI encoder designed for accurate zero- and f...
  </details>

- **2026-07-06** — Mark de Rooij — [Smooth Reduced Rank Regression with P-splines](http://arxiv.org/abs/2607.05096v1)
  <details><summary>📄 Abstract</summary>
  Linear regression is one of the core statistical tools used for analysis of data. In the era of statistical learning, linear regression has been expanded into two directions. The first is regularisation, where penalties are added to the loss function to obtain more stable or sparse solutions. The second direction is basis expansion, such as with spline or kernel functions, where the linearity assumption is dropped. In practice, empirical researchers often collect multiple outcome variables. Regr...
  </details>

- **2026-07-06** — Manuela Del Castillo Suero, Arnault-Quentin Vermillet, Nicole Sonne Heckmann et al. — [Multi-Large Language Model Orchestrated Severity Assessment of Clinical Records (MOSAIC)](http://arxiv.org/abs/2607.05032v1)
  <details><summary>📄 Abstract</summary>
  Background: Disease severity is a multidimensional construct difficult to capture with rule-based approaches in Electronic Healthcare Records (EHR). Agentic large language model (LLM) systems could synthesise clinical evidence and reason over EHRs, but remain unevaluated for this task. Methods: MOSAIC is a two-phase agentic LLM framework for severity phenotyping, using type 2 diabetes (T2D) as a proof-of-concept. MOSAIC was evaluated on a synthetic cohort (SyntheticMass; open-weight N = 4,886; c...
  </details>

- **2026-07-06** — Helena Mihaljević, Jolanda Beer, Mareike Lisker et al. — [Who's Behind It? Annotating and Extracting Conspiratorial Actors from German Telegram Posts](http://arxiv.org/abs/2607.04962v1)
  <details><summary>📄 Abstract</summary>
  Conspiracy theories commonly attribute important events to the actions of powerful and secretive actors. While computational research has largely focused on document-level analyses of conspiracy theories, less attention has been paid to identifying the actors that drive such narratives. We develop annotation guidelines for conspiratorial actors, present a span-annotated corpus of German Telegram posts, and investigate their automatic extraction using transformer-based models. We further apply th...
  </details>

- **2026-07-06** — Yang Yang, Run-Yu Lei, Jian-Ping Zhou et al. — [Different dielectric, magnetic, and magnetodielectric mechanisms in M-type BaFe12O19 hexaferrite regulated by doping Ga3+ and In3+ cations](http://arxiv.org/abs/2607.04861v1)
  <details><summary>📄 Abstract</summary>
  We systematically investigated the magnetic, dielectric, and MD properties of BaFe12-xMexO19 ceramics prepared by a solid-state reaction method. The Ga3+ cations with a smaller radius preferentially substitute the Fe3+ ions in FeO6 octahedra while the In3+ cations with a larger radius tend to replace the Fe3+ ions in FeO5 bipyramids of R blocks, inducing different physical characteristics. The pure BaFe12O19 and Ga-doped samples show ferrimagnetism in the temperature range from 10 K to 300 K. Th...
  </details>

- **2026-07-06** — Xujun Che, Xiuxia Du, Depeng Xu — [MARLIN: De Novo Molecular Structure Elucidation from Tandem Mass Spectra without a Ground-Truth Formula](http://arxiv.org/abs/2607.04774v1)
  <details><summary>📄 Abstract</summary>
  Untargeted tandem mass spectrometry (MS/MS) detects thousands of small molecules per biological sample, yet most go unidentified because they are absent from spectral libraries. These uncharacterized metabolites and natural products are precisely the compounds that matter for drug discovery, biomarker research, and exposomics. Computational de novo structure elucidation could close this gap, but almost all state-of-the-art methods assume the ground-truth molecular formula is known, an oracle tha...
  </details>

- **2026-07-06** — Na Liu, Chang Li, Yujia Gu et al. — [Stabilized Higher-Order Influence Functions: Statistical Theory of a Class of Bilinear Forms](http://arxiv.org/abs/2607.04743v1)
  <details><summary>📄 Abstract</summary>
  Higher-order influence functions, introduced in a series of articles (Robins et al., 2008, 2009a; van der Vaart, 2014; Robins et al., 2016, 2023; Liu et al., 2017), are a unified framework for constructing rate-optimal point estimates of a class of statistical functionals, under various complexity-reducing assumptions on the posited statistical model that generates the observed data. Although higher-order (influence functions) estimators are theoretically appealing, they have very limited practi...
  </details>

- **2026-07-06** — Yu Wei, Yukiko Ogura, Yoshiyuki Ohmura et al. — [Integrated Altruistic and Fairness Preference Induces Advanced Mutual Cooperation in Sequential Social Dilemmas](http://arxiv.org/abs/2607.04710v1)
  <details><summary>📄 Abstract</summary>
  Inducing cooperation among distributed agents is still a difficult problem in the field of multi-agent reinforcement learning (MARL), particularly in social dilemma situations. There, individual interests are misaligned with the common good and individual rationality leads to suboptimal group outcomes. In contrast, humans are able to achieve cooperation with one another in such situations. A common explanation for such cooperative behavior is that individuals have social preferences. In order to...
  </details>

- **2026-07-06** — Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev et al. — [URSA: Chemistry-Aware Benchmark for Utilitarian Retrosynthesis Assessment](http://arxiv.org/abs/2607.04688v1)
  <details><summary>📄 Abstract</summary>
  Synthesis planning aiming to find pathways of reactions for a target molecule is one of the most important and challenging tasks in drug discovery. Recent progress has produced both specialized deep-learning retrosynthesis systems and general-purpose large language models, but objective comparison remains difficult due to the lack of flexible, chemically interpretable benchmarking protocols. In the current study, we are introducing the URSA (Utilitarian RetroSynthesis Assessment) evaluation fram...
  </details>

- **2026-07-06** — Jiaxing Qi, Zhongzhi Luan, Hongyu Zhang et al. — [Can LLMs Really Recover Microservice Failures? A Recovery-Aware Evaluation of Diagnosis-to-Action Reasoning](http://arxiv.org/abs/2607.04623v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to interpret operational evidence and assist incident response in cloud-native microservice systems. However, recovery-oriented use cases require more than identifying a root cause. After observing symptoms and diagnosing a fault, an operator or agent must translate the diagnosis into a concrete recovery action, apply it to an admissible target, and verify that service health has been restored. Existing RCA and log-analysis evaluations are well-...
  </details>

- **2026-07-06** — Riccardo Renzulli, Gabriele Spadaro, Shruthi Gowda et al. — [TORINO: Token Reduction via Interpretable Concept Overlap in Vision-Language Models](http://arxiv.org/abs/2607.04593v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have demonstrated impressive capabilities across different tasks, but their computational cost is dominated by the large number of visual tokens fed to the language model. Existing token reduction methods rely on attention-based scores or pairwise similarity, without an explicit semantic representation of each token. We introduce TORINO (TOken Reduction via Interpretable coNcept Overlap), a plug-and-play framework for adaptive visual token reduction in VLMs that req...
  </details>

- **2026-07-06** — Saurabhsingh Rajput, Tushar Sharma — [Beyond the Need for Speed: Energy-Aware Code Generation via Simulation-Guided Reinforcement Learning](http://arxiv.org/abs/2607.04577v1)
  <details><summary>📄 Abstract</summary>
  Code models strictly prioritize functional correctness, leaving software energy efficiency as an unoptimized byproduct. Training models to generate energy-efficient code requires reproducible feedback at scale, which physical hardware measurement cannot reliably provide due to variance.   In this paper, we replace hardware profiling with a deterministic architectural simulation harness to build Green Tea, a corpus of $3.5$ million evaluations across $1{,}474$ C++ problems. We train an energy-awa...
  </details>

- **2026-07-06** — Yeganeh Bahoo, Sajad Saeedi, Roni Sherman — [An Exact Generalized k-Cell Decomposition](http://arxiv.org/abs/2607.04561v1)
  <details><summary>📄 Abstract</summary>
  This paper introduces an exact $k$-cell decomposition for visibility planning in polygonal environments for agents equipped with $k$-modems, devices that can see through up to $k$ walls. Unlike prior decompositions that may include redundant partition lines, our proposed method ensures that visibility events (appear, disappear, merge, and split) are guaranteed to occur on every line of the decomposition. By eliminating these redundancies, we achieve an $O(n^4)$ complexity , representing a potent...
  </details>

- **2026-07-06** — Islam Eldifrawi, Shengrui Wang, Amine Trabelsi — [Can temporal article-level credibility signals improve domain-level credibility prediction?](http://arxiv.org/abs/2607.04560v1)
  <details><summary>📄 Abstract</summary>
  Web domain credibility evaluation is vital for combating misinformation. It is conducted by examining factors such as domain type, transparency, and overall reputation. However, assessing the credibility of newly emerging web domains remains challenging since they have no reputation yet. Expert fact-checkers evaluate the credibility of domains by analyzing the content of their articles, including the presence of misinformation, bias, or propaganda. Yet, the ease of large-scale content generation...
  </details>

- **2026-07-05** — Hao Wei, Wenjin Qi, Dasen Dai et al. — [IRIS: An Intelligent Vision-Language System for Ocular Surface Diseases via Topic Tree and Scene-Driven VQA Generation](http://arxiv.org/abs/2607.04344v1)
  <details><summary>📄 Abstract</summary>
  While Large Vision-Language Models (VLMs) demonstrate remarkable generic capabilities, their clinical reasoning in specialized domains like ocular surface diseases (OSDs) is severely hindered by a paucity of high-fidelity, multimodal instruction-tuning data. To dismantle this data bottleneck, we introduce IRIS, an Intelligent Recognition and Interaction System tailored for fine-grained OSD understanding via external eye photography. First, we curate IRIS-120K, the largest and most comprehensive ...
  </details>

- **2026-07-05** — Yaozu Wu, Wei-Chieh Huang, Jizhou Guo et al. — [HAS-Bench: Evaluating LLM-Based Human-Agent Systems under Configurable Human Participation](http://arxiv.org/abs/2607.04329v1)
  <details><summary>📄 Abstract</summary>
  Large language models increasingly operate in settings where humans are active collaborators rather than passive task providers. We introduce HAS-Framework, a graph-based framework that represents humans and LLM-powered agents as first-class participants with explicit roles, permissions, communication paths, and action authority. Building on this framework, HAS-Bench evaluates Human-Agent Systems under configurable human participation across agency levels, interaction channels, and persona polic...
  </details>

- **2026-07-05** — Jiang Zhang, Bing Yuan, Qian Zhang — [Self-Reference in Large Language Models: The Introspection Threshold for Recursive Self-Improvement](http://arxiv.org/abs/2607.04277v1)
  <details><summary>📄 Abstract</summary>
  The pursuit of self-evolving AI raises a critical question: when is autonomous self-improvement sustainable rather than degenerative? Drawing an analogy to von Neumann's complexity threshold for self-reproducing automata, we argue that sustainable recursive self-improvement in Large Language Models (LLMs) requires a functional analogue: introspection -- the system's capacity to simulate its own operations and target modifications. Grounded in Kleene's Second Recursion Theorem, we demonstrate the...
  </details>

- **2026-07-05** — Badrinath Singhal, Srihari K G, Sreehari Iyer et al. — [AdaptiveSplat:Texture Aware Controllable 3D Gaussian Allocation for Feed-Forward Reconstruction](http://arxiv.org/abs/2607.04256v1)
  <details><summary>📄 Abstract</summary>
  Current feed-forward 3D reconstruction methods predict pixel aligned Gaussian primitives, resulting in highly redundant representations. A natural solution is to prune the redundant Gaussians, but naive pruning introduces severe artifacts and often requires inference time fine-tuning, breaking the feed-forward paradigm. Based on previous works, high frequency regions require more Gaussian primitives, while low frequency regions can be represented with significantly fewer primitives. Motivated by...
  </details>

- **2026-07-05** — Guangyu Lei, Tianhao Liang, Bingyan Xie et al. — [Towards Effcient Low Altitude Sensing: A Dual Heterogeneous Graph Learning Method for UAV Task Allocation](http://arxiv.org/abs/2607.04255v1)
  <details><summary>📄 Abstract</summary>
  With the development of low altitude intelligent systems, multiple unmanned aerial vehicles (UAVs) can collaboratively execute more complex tasks. Conventional task allocation methods usually regard tasks and UAVs as isolated entities, making it difficult to capture task dependencies and UAV communication relationships. To address this issue, this paper proposes a dual heterogeneous graph learning based UAV task allocation method. A directed task graph is constructed to represent task dependenci...
  </details>

- **2026-07-05** — Arthur Plaud, P. L. Krapivsky, S. Redner et al. — [Universal fluctuations of first discoveries in competitive exploration](http://arxiv.org/abs/2607.04252v1)
  <details><summary>📄 Abstract</summary>
  Random exploration is usually quantified by how fast new space is found, from   the range of a single walker to the territory collectively covered by many   walkers. In competitive exploration, first arrival secures an exclusive resource, as when foragers compete for food items or agents capture distributed targets. It is then no longer enough to know which sites have been discovered: one must determine, for each discovered site, which searcher reached it first. We introduce the discovery   shar...
  </details>

- **2026-07-05** — Qiang Chen, Xiao Wang, Hao Si et al. — [Hierarchical Multi-to-Single-Modal Knowledge Distillation for Disruption Prediction in EAST](http://arxiv.org/abs/2607.04241v1)
  <details><summary>📄 Abstract</summary>
  Plasma disruption is a critical threat to tokamak safety. Existing data-driven predictors mainly rely on time-series diagnostic signals, while visible images provide complementary spatial cues including plasma deformation, local brightening, and radiation-structure evolution. Although the image modality improves the model's discriminative capability, it also substantially increases the computational cost during inference. To address this issue, we propose a hierarchical multi-to-single-modal kno...
  </details>

- **2026-07-05** — Riccardo O. Feingold, Davide Liconti, Chenyu Yang et al. — [Mask2Real-WM: Segmentation Masks as a Sim-to-Real Bridge for Controllable Dexterous World Models](http://arxiv.org/abs/2607.04546v1)
  <details><summary>📄 Abstract</summary>
  Action-conditioned world models allow robots to predict the future consequences of candidate actions without additional physical interaction, supporting policy evaluation, planning, and data augmentation. We present Mask2Real-WM, a two-stage action-conditioned world model for dexterous manipulation that decouples pixel prediction into a dynamics model and a rendering model. The dynamics model predicts future segmentation masks from past masks and 23-DoF action sequences. The rendering model maps...
  </details>

- **2026-07-05** — Damir Shodiev, Aleksei Staroverov, Nikita Kachaev et al. — [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](http://arxiv.org/abs/2607.04517v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are commonly treated as end-to-end action policies conditioned on natural-language task descriptions. In practice, however, their behavior often depends sharply on how the instruction is phrased, suggesting that language is not merely a task label but an optimizable conditioning input. We study whether frozen VLA policies can be improved by optimizing language space rather than updating action weights. Our method introduces a language-conditioning space policy...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 539 |
| prompt-injection | 447 |
| memory-poisoning | 36 |
| tool-use-attack | 91 |
| backdoor | 382 |
| adversarial-attack | 522 |
| privacy-leakage | 3657 |
| steganography | 52 |
| misuse | 795 |
| red-teaming | 105 |
| vulnerability | 2367 |
| defense | 1998 |
| alignment | 1818 |
| robustness | 1641 |
| watermark | 164 |
| unlearning | 81 |
| agent-safety | 48 |
| benchmark | 53 |
| survey | 239 |
| other | 5216 |

---

📚 **全部 20251 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-07-09 03:24:05*