<div align="center">

# AgentGuard 🛡️

**Daily Tracking of LLM Agent Security Papers on arXiv**

[![Auto Update](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml/badge.svg)](https://github.com/NY1024/AgentSafety-Papers/actions/workflows/daily-update.yml)
[![Papers](https://img.shields.io/badge/Papers-31896-blue)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

</div>

---

## 📖 简介 / Introduction

自动追踪 arXiv 上大模型 Agent 安全方向的最新论文，每日更新，关键词智能分类。

*Automatically tracking the latest LLM Agent security papers on arXiv, updated daily with keyword-based classification.*

**最近更新 / Last Updated**: 2026-10-08 12:40 ｜ **论文总数 / Total Papers**: 31896（近 30 天 / Recent 30 days: 5028）

🌐 **[GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)** — 查看全部 31896 篇论文（含摘要、分类筛选、搜索）/ View all 31896 papers with abstracts, filters & search

## 📑 分类导航 / Category Navigation

- **[jailbreak](#-jailbreak)** — 越狱攻击 / Jailbreak Attacks — 667
- **[prompt-injection](#-prompt-injection)** — 提示注入攻击 / Prompt Injection Attacks — 607
- **[memory-poisoning](#-memory-poisoning)** — 记忆投毒与篡改 / Memory Poisoning & Tampering — 55
- **[tool-use-attack](#-tool-use-attack)** — 工具使用攻击 / Tool-Use Attacks — 150
- **[backdoor](#-backdoor)** — 后门与投毒攻击 / Backdoor & Poisoning Attacks — 505
- **[adversarial-attack](#-adversarial-attack)** — 对抗攻击 / Adversarial Attacks — 631
- **[privacy-leakage](#-privacy-leakage)** — 隐私泄露 / Privacy Leakage — 4319
- **[steganography](#-steganography)** — 隐写与隐蔽通信 / Steganography & Covert Communication — 76
- **[misuse](#-misuse)** — 滥用与误用 / Misuse & Abuse — 1135
- **[red-teaming](#-red-teaming)** — 红队测试 / Red Teaming — 137
- **[vulnerability](#-vulnerability)** — 漏洞与攻击面 / Vulnerabilities & Attack Surfaces — 3495
- **[defense](#-defense)** — 防御与防护方法 / Defense & Protection Methods — 3339
- **[alignment](#-alignment)** — 对齐与安全约束 / Alignment & Safety Constraints — 3112
- **[robustness](#-robustness)** — 鲁棒性与可靠性 / Robustness & Reliability — 3382
- **[watermark](#-watermark)** — 水印与溯源 / Watermarking & Provenance — 561
- **[unlearning](#-unlearning)** — 机器遗忘 / Machine Unlearning — 111
- **[agent-safety](#-agent-safety)** — Agent 安全框架 / Agent Safety Frameworks — 62
- **[benchmark](#-benchmark)** — 安全评测与基准 / Safety Benchmarks & Evaluation — 67
- **[survey](#-survey)** — 综述与系统化 / Surveys & Systematization — 393
- **[other](#-other)** — 其他安全相关 / Other Security-Related — 9092

## 📄 近期论文 / Recent Papers (Last 30 Days)

> 仅展示最近 30 天中最新的 500 篇论文（含日期、作者、摘要）。近 30 天共 5028 篇，完整 31896 篇论文列表请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

> Showing the latest 500 of 5028 papers from the last 30 days (with date, authors & abstract). For the full list of 31896 papers, visit [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/)

### 📂 jailbreak
*越狱攻击 / Jailbreak Attacks* — 6 papers

- **2026-10-07** — Alexi Canesse, Mathis Le Bail, Maël Jenny et al. — [PatchBench: Measuring Collateral Damage in Activation Patching](http://arxiv.org/abs/2610.10276v1)
  <details><summary>📄 Abstract</summary>
  An LLM safety patch can pass a benchmark while still being a poor repair. This risk is especially acute for jailbreak repairs, where the goal is to correct a specific unsafe behaviour without changing unrelated behaviours. A patch may block exact evaluation prompts yet fail on close harmful variants, or suppress harmful behaviour by over-refusing benign prompts that share its wording or structure. Existing protocols primarily test whether models can be broken, while aggregate metrics (attack suc...
  </details>

- **2026-10-07** — Juanyang Xu, Zheng Wang, Xingyu Zhao et al. — [From Expected Harmfulness to Likelihood: A Probabilistic Reformulation of Jailbreaking LLM Agents](http://arxiv.org/abs/2610.09973v1)
  <details><summary>📄 Abstract</summary>
  When the harmfulness of an LLM agent's output can be quantified, a natural jailbreaking objective is to maximize expected harmfulness over admissible input modifications. An alternative approach constructs or selects harmful target outputs and modifies the input to increase their likelihood. We establish a precise connection between these two approaches through a probabilistic reformulation. Specifically, we show that the gradient of the logarithm of expected harmfulness with respect to the inpu...
  </details>

- **2026-10-07** — Shuailong Wang, Xinyu Lyu, Shengming Yuan et al. — [Understanding and Mitigating Token-Pruning-Induced Vulnerabilities in VLMs](http://arxiv.org/abs/2610.09703v1)
  <details><summary>📄 Abstract</summary>
  Token-Pruning accelerates Vision-Language Models by removing redundant visual tokens, yet its safety implications remain underexplored. In this work, we present the first comprehensive safety evaluation of Token-Pruning mechanisms and find that: most pruning strategies significantly degrade safety as pruning ratios increase, whereas Query-based Compression shows the opposite, with extreme pruning (up to 99.8%), unexpectedly improves model safety. This sharp contrast prompts a key question: How d...
  </details>

- **2026-10-06** — Xunlei Qian, Yingqian Cui, Yuping Lin et al. — [Detecting Unseen Jailbreak Sources: A Multi-Source Conformal Detection Perspective](http://arxiv.org/abs/2610.09167v1)
  <details><summary>📄 Abstract</summary>
  Jailbreak defenses for large language models are usually calibrated on a fixed set of known attack methods. However, new attack methods keep appearing after deployment, and existing detectors are observed to degrade under the new attacks (Piet et al., 2025). This paper studies how to detect, from a stream of attack prompts, that the prompts come from an attack source outside the known ones. We formulate it as a sequential test whose null hypothesis is that the stream comes from one of the known ...
  </details>

- **2026-10-06** — Yichi Zhang, Zhiqi Wang, Neil Gong et al. — [Secure Speculative Decoding for Large Language Models](http://arxiv.org/abs/2610.08678v1)
  <details><summary>📄 Abstract</summary>
  Speculative decoding accelerates inference for a large language model (LLM), referred to as the \emph{target model}, by first using a smaller model, referred to as the \emph{draft model}, to generate candidate tokens and then verifying them with the target model for acceptance or rejection. Prior studies primarily focused on the efficiency-utility trade-off of speculative decoding, e.g., lossy speculative decoding, leaving its security implications largely unexplored.   In this work, we bridge t...
  </details>

- **2026-10-05** — Wonjun Lee, Kyungsik Yang, Gaeun Ji et al. — [Safeguarding LLMs via Model-Agnostic Latent Safety Signals from Dark Knowledge](http://arxiv.org/abs/2610.07532v1)
  <details><summary>📄 Abstract</summary>
  LLMs have advanced rapidly, raising growing concerns about their safety. Recent work has proposed approaches to detect and defend against attacks including defenses at decoding stage that leverage models' hidden states. However, existing decoding-stage defenses suffer from two limitations. First, they introduce a trade-off between safety and over-refusal, where strengthening safety degrades the model's helpfulness on benign queries. Second, many of these methods rely on internal hidden states an...
  </details>


### 📂 prompt-injection
*提示注入攻击 / Prompt Injection Attacks* — 7 papers

- **2026-10-07** — Zitong Yao, Jiangrong Wu, Yixi Lin et al. — [AgentTracer: Tracing Indirect Prompt Injection Attack through Fine-Grained Intention-Execution Alignment](http://arxiv.org/abs/2610.09935v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM) agents interact with external resources to complete complex user tasks, exposing them to indirect prompt injection (IPI), where malicious instructions redirect agents toward attacker-intended tasks. Since IPI is difficult to defend against in real-world environments, post-incident tracing is essential for locating the injection source and reconstructing the attack chain. However, existing tracing methods primarily capture explicit control-flow and data-flow dependencie...
  </details>

- **2026-10-07** — Yupu Wang, Zhengyuan Jiang, Reachal Wang et al. — [Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files](http://arxiv.org/abs/2610.09264v1)
  <details><summary>📄 Abstract</summary>
  Modern agentic coding frameworks increasingly rely on community-shared rule files (e.g., AGENTS.md or .cursorrules) to guide autonomous code generation, yet the security risks of this pipeline remain underexplored. To bridge this gap, we introduce the package hallucination attack, where an attacker injects malicious prompts into benign rule files to induce coding agents to replace legitimate dependencies with attacker-controlled packages. To obtain effective malicious prompts injected into rule ...
  </details>

- **2026-10-06** — Pengfei He, Deep Mitra, Vishesh Sharma et al. — [ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine](http://arxiv.org/abs/2610.08951v1)
  <details><summary>📄 Abstract</summary>
  LLM agents retrieve untrusted content and act through tools, creating indirect prompt-injection risks that can cause unauthorized actions or persistent state changes. Existing automated red-teaming largely optimizes payloads for pre-specified scenarios, leaving latent vulnerabilities across the agent's behavior space unexplored. We present ASPIRE, an Agentic Safety & Prompt Injection Red-teaming Engine for open-ended, behavior-level vulnerability discovery. ASPIRE maintains an evolving Agent Sec...
  </details>

- **2026-10-06** — Sarim Hashmi, Mukul Ranjan, Kshitij Mishra et al. — [AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model](http://arxiv.org/abs/2610.08773v1)
  <details><summary>📄 Abstract</summary>
  Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a t...
  </details>

- **2026-10-06** — Niveen O. Jaffal, Ahmet Yuksel, David Mohaisen — [RAG-PIBench: A Leakage-Aware Benchmark for Prompt-Injection Detection in Trustworthy RAG Systems](http://arxiv.org/abs/2610.08571v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-Augmented Generation (RAG) systems are vulnerable to prompt-injection attacks embedded in retrieved content. We introduce RAG-PIBench, a benchmark for RAG-style prompt-injection detection containing 4,876 contextual examples across frozen train, validation, and protected-test splits. Using a leakage-aware construction pipeline and strict evaluation protocol, we compare keyword-based, semantic-reference, TF-IDF, and transformer-based detectors. DistilBERT achieves the best protected-tes...
  </details>

- **2026-10-06** — Haneen Najjar, Luca Scionis, Haritz Puerto et al. — [Surviving the Router: Optimizing Skill Injections for Retrieval and Execution](http://arxiv.org/abs/2610.08098v1)
  <details><summary>📄 Abstract</summary>
  AI agents increasingly rely on modular third-party "skills" that are dynamically selected by skill routers to execute complex tasks. While recent studies highlight the threat of prompt injections embedded in these skills, existing evaluations often assume settings where the malicious skill is already selected for execution. We show that this assumption can substantially overestimate attack success. In realistic multi-skill environments, injected skills must first compete for retrieval, reducing ...
  </details>

- **2026-10-05** — Mohamed Dhouib, Clement Elliker, Alexi Canesse et al. — [RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents](http://arxiv.org/abs/2610.06401v2)
  <details><summary>📄 Abstract</summary>
  Tool-using language-model agents are vulnerable to indirect prompt injection because they must act on untrusted external content. Existing training-time defenses can reduce attack success rates, but often at the cost of general capabilities. We show that training-based defenses induce substantial drift in the model's output distribution, altering its behavior even in benign settings and providing a potential mechanism for utility degradation. We further identify a failure mode of these defenses:...
  </details>


### 📂 memory-poisoning
*记忆投毒与篡改 / Memory Poisoning & Tampering* — 1 papers

- **2026-10-06** — David Dobre, Leo Schwinn, Gauthier Gidel et al. — [Visual Memory Attacks Can Persist Through The KV Cache](http://arxiv.org/abs/2610.09027v1)
  <details><summary>📄 Abstract</summary>
  Modern language model systems operate autonomously over increasingly long contexts containing untrusted text and images. Can an adversarial input continue to steer a model even after that input is removed from its context? We show that attacks can be trained to persist through the key/value (KV) cache of subsequent tokens, allowing adversarial influence to outlive direct access to its source.We consider the Visual Memory Injection (VMI; Schlarmann and Hein, 2026) attack setting, in which an adve...
  </details>


### 📂 backdoor
*后门与投毒攻击 / Backdoor & Poisoning Attacks* — 9 papers

- **2026-10-07** — Hui Zhang, Yachao Yuan, Jiayun Wang et al. — [SLDR: Defending Against Malicious Fine-tuning via Selective Layers Recovery and Dynamic Routing](http://arxiv.org/abs/2610.10345v1)
  <details><summary>📄 Abstract</summary>
  Fine-tuning-as-a-service enables users to adapt aligned large language models (LLMs) to specialized tasks, but malicious fine-tuning can erode refusal behavior while preserving task performance on legitimate inputs. We revisit recent layer-wise safety diagnostics and find that safety sensitivity is signed: scaling different layers can strengthen refusal, weaken it, or have little effect. Motivated by this observation, we propose SLDR, a post-fine-tuning defense based on Selective Layers Recovery...
  </details>

- **2026-10-07** — Xilin Wang, David Bau, Byron C. Wallace — [How to train your model organism](http://arxiv.org/abs/2610.10203v1)
  <details><summary>📄 Abstract</summary>
  Model organisms of alignment-relevant behaviors (e.g., backdoors, sycophancy, spurious correlations) have emerged as a key tool for evaluating whitebox interpretability techniques. We argue that the prevailing practice of training model organisms to a single objective of installing the target behavior is insufficient and propose validating model organisms with respect to three objectives with associated metrics: target-behavior installation, general-capability preservation (i.e., parametric know...
  </details>

- **2026-10-07** — Bojun Yang, Haochen Zhou, Zhifang Zhang et al. — [Purifying Backdoored Large Vision-Language Models by Removing Hijacked Directions](http://arxiv.org/abs/2610.09941v1)
  <details><summary>📄 Abstract</summary>
  Large vision-language models (LVLMs) are increasingly deployed in safety-critical applications, yet they remain vulnerable to backdoor attacks. Defending against such attacks remains costly, as existing methods require either extensive retraining on clean data or per-query intervention at inference time. To address this limitation, we propose OrthoPurify, a more efficient method to purify backdoored model weights via one-step orthogonal projection. Specifically, through structural analysis of ba...
  </details>

- **2026-10-07** — Zebin Yun, Eyal Ronen, Mahmood Sharif — [Backdooring Acoustic Foundation Models for Physically Realizable Triggers](http://arxiv.org/abs/2610.09819v1)
  <details><summary>📄 Abstract</summary>
  Acoustic foundation models (AFMs) have democratized acoustic applications, enabling powerful models for tasks ranging from speech recognition to speaker verification with minimal resources. However, the security of applications based on AFMs remains largely underexplored. Our work addresses this gap by proposing the Foundation Acoustic model Backdoor (FAB) attack, demonstrating that state-of-the-art AFMs are susceptible to backdooring under practical settings. Despite making minimal assumptions ...
  </details>

- **2026-10-06** — Christophe Muller, Ayub Kharel, Alex Luedtke et al. — [ProximalFM: Amortized Proximal Causal Inference under Hidden Confounding](http://arxiv.org/abs/2610.08078v1)
  <details><summary>📄 Abstract</summary>
  Standard causal identification methods often assume no unmeasured confounding and can fail when relevant confounders are unobserved. Proximal causal inference instead uses proxy variables to identify effects under hidden confounding. However, nonparametric proximal estimation can be challenging in practice: recovering causal estimands such as the conditional average treatment effect (CATE) requires solving an ill-posed integral equation that is data-hungry, hyperparameter-sensitive, and optimiza...
  </details>

- **2026-10-06** — Yibo Zhang, Tianrong Guan, Liang Lin et al. — [The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models](http://arxiv.org/abs/2610.07723v1)
  <details><summary>📄 Abstract</summary>
  Safety alignment in Large Language Models (LLMs) remains vulnerable to backdoor attacks. Existing LLM backdoors are almost all input-centric: activation depends on explicit trigger patterns in the user input, so modern guardrails are built to sanitize the input space. We challenge this assumption with a novel answer-side backdoor for multi-turn dialogue. Instead of inserting the trigger into the input, the adversary uses a benign first-turn prompt to naturally induce the model to generate a spec...
  </details>

- **2026-10-06** — Jian Luo, Kehan Qi, Qingqiao Hu et al. — [Does On-Policy Distillation for Safety Pose Backdoor Risks?](http://arxiv.org/abs/2610.07654v1)
  <details><summary>📄 Abstract</summary>
  On-policy distillation (OPD) has attracted growing attention as an effective way to transfer capabilities from teacher models to student models. Recent studies further explore OPD as a tool for improving large language model safety with promising results. However, these approaches typically assume that the teacher and training data are trustworthy. In this paper, we uncover an overlooked threat to OPD for safety: a safety-aligned but backdoored teacher can propagate its hidden malicious behavior...
  </details>

- **2026-10-06** — Lizhi Zhang, Xin He, Dianxuan Fu et al. — [SkillPoison: Progressive Skill Poisoning via Successful Experiences](http://arxiv.org/abs/2610.07645v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM agents increasingly distill successful experiences into persistent, reusable skills. Existing skill attack methods corrupt this learning pipeline by injecting malicious triggers, behaviors, or false facts into individual experiences or extracted skills. However, such attacks are easily detected, and the injected malicious behaviors often fail to accumulate as persistent skills. In this paper, we show that skill poisoning can arise even from verified successful experiences, wit...
  </details>

- **2026-10-05** — Qiusi Zhan, Nian Lyu, Stephanie Ding et al. — [Understanding and Enhancing Backdoor Persistency in LLM Agent Post-Training](http://arxiv.org/abs/2610.07510v1)
  <details><summary>📄 Abstract</summary>
  Developers can build LLM agents by adapting third-party models through benign post-training. We study a supply-chain threat in which an attacker supplies a model with a backdoor: hidden behavior that produces malicious outputs when a particular input pattern appears. Focusing on software-engineering agents, we ask whether such backdoors survive the developer's supervised fine-tuning (SFT) and subsequent task-level reinforcement learning (RL). We observe that benign SFT substantially reduces atta...
  </details>


### 📂 adversarial-attack
*对抗攻击 / Adversarial Attacks* — 8 papers

- **2026-10-07** — Arash Vashagh, Roozbeh Razavi-Far — [Detecting Adversarial Images through Response Profiles of Vision-Language Models](http://arxiv.org/abs/2610.10436v1)
  <details><summary>📄 Abstract</summary>
  Adversarial perturbations can alter the predictions of frozen vision-language models (VLMs) while leaving their confidence and image--text similarity patterns seemingly plausible. We investigate whether we can identify adversarial inputs based on the broader way an image interacts with a collection of general semantic prompts. Our detector summarizes these responses using category-level statistics, relationships among prompts, deviations from clean reference distributions, and stability under we...
  </details>

- **2026-10-07** — Xiaoyi Pang, Haoyue Feng, Quanxin Shou et al. — [Black-Box Adversarial Patch Attacks on VLAs via Ancestor VLM Exploitation](http://arxiv.org/abs/2610.09708v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models (VLAs) are increasingly deployed in safety-critical physical environments, yet their adversarial robustness remains poorly understood. Existing attacks typically assume white-box access or rely on surrogate VLAs, which rarely holds in real-world deployments. Our key insight is that most VLAs are adapted from a publicly released pretrained vision-language model (VLM), inheriting two capabilities essential for action generation: visual perception and instruction-condi...
  </details>

- **2026-10-06** — Mojtaba Nafez, Aref Mousavi, Mohammad Ebrahim Mahdavi et al. — [Breaking Adversarial Transferability in Fine-Tuned Speech Recognition](http://arxiv.org/abs/2610.09109v1)
  <details><summary>📄 Abstract</summary>
  Many organizations fine-tune publicly available pretrained Automatic Speech Recognition (ASR) models and deploy them in black-box settings, assuming limited access provides protection. We show this assumption is fragile: adversarial perturbations crafted on the public base model transfer effectively to fine-tuned target models, severely degrading performance and posing concerns for safety-critical applications. We propose TransferBreaker, a unified fine-tuning framework that suppresses adversari...
  </details>

- **2026-10-06** — Maedeh Fallahreyhani, Paeiz Azmi, Nader Mokari et al. — [TwinViT-DeepJSCC: Adversarially Robust Semantic Image Communication](http://arxiv.org/abs/2610.08590v1)
  <details><summary>📄 Abstract</summary>
  Learning-based semantic communication is vulnerable to adversarial perturbations introduced before semantic encoding or over wireless channels. This paper proposes TwinViT-DeepJSCC, a preventive-corrective semantic image transceiver operating under a fixed channel-use budget. Two Vision Transformer (ViT)-based deep joint source-channel coding (DeepJSCC) branches learn complementary latent representations protected by sensitivity-aware masking. At the receiver, confidence-aware fusion, blind corr...
  </details>

- **2026-10-06** — Heyam Bin Jahlan Areej Alhothali Abeer Alhothali — [Transferable Spatial Temporal Coherence Adversarial Attack on Black-Box Vision Language Models for Autonomous Driving](http://arxiv.org/abs/2610.08331v1)
  <details><summary>📄 Abstract</summary>
  The rapid integration of Vision Language Models (VLMs) into sensitive systems introduces critical safety vulnerabilities that remain unexplored in exist studies. While adversarial attack robustness has been extensively studied for image-based models, the susceptibility of VLMs to temporally-aware adversarial attacks against video in driving context poses a distinct and under examined threat. In this paper, we introduce novel adversarial attack against video targeting VLM models used for autonomo...
  </details>

- **2026-10-06** — Soichiro Kumano — [Adversarially Trained Linear Transformers Are Optimal Robust In-Context Learners for Gaussian Mixtures](http://arxiv.org/abs/2610.07754v1)
  <details><summary>📄 Abstract</summary>
  Adversarial training is one of the most reliable defenses against adversarial attacks, but its high computational cost must generally be paid anew for each task. Robust foundation models offer a promising alternative: adversarially pretrain a model once and then transfer its robustness to downstream tasks through lightweight adaptation. However, a fundamental question remains open: can robustness acquired during pretraining transfer to unseen tasks without further adversarial training? In this s...
  </details>

- **2026-10-05** — Zexin Li, Ruili Yao, Yiming Zeng et al. — [Boosting Transferable Adversarial Attacks against Deep Reinforcement Learning](http://arxiv.org/abs/2610.06083v2)
  <details><summary>📄 Abstract</summary>
  Most adversarial attacks on deep reinforcement learning (DRL) assume white-box access to the victim policy, which rarely holds in practice. This paper studies transfer-based black-box attacks on DRL: the attacker crafts observation perturbations on a white-box surrogate agent and feeds them to an unknown victim. We formulate the attack as return minimization under a per-step perturbation budget. We first show that transplanting transferable image-classification attacks (FGSM, MI-FGSM, and NI-FGS...
  </details>

- **2026-10-05** — Sarim Hashmi, Abdelrahman Elsayed, Mohammed Talha Alam et al. — [Certification of Real Images through Calibrated Content Authentication](http://arxiv.org/abs/2610.05870v2)
  <details><summary>📄 Abstract</summary>
  Generative models can synthesize high-quality inauthentic multimedia content that is already being misused at scale. We evaluate twenty deepfake detectors against ten generators released in the last four years and find accuracy decreasing over time, from near-perfect 99.5% to 76%. Adversarial perturbations further reduce every baseline detector to below 2% accuracy, effectively inverting the detector's assigned label. We argue that this unreliability reflects a fundamental ambiguity: generators ...
  </details>


### 📂 privacy-leakage
*隐私泄露 / Privacy Leakage* — 25 papers

- **2026-10-07** — Junkai Chen, Yuhao He, Qianshan Wei et al. — [Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning](http://arxiv.org/abs/2610.10358v1)
  <details><summary>📄 Abstract</summary>
  As multimodal large language models (MLLMs) become more capable and widely deployed, concerns about privacy and safety have become increasingly pressing. Machine unlearning offers one approach to addressing these concerns by removing designated information from trained models while preserving unrelated capabilities. However, fragmented implementations and evaluation protocols, incomplete robustness testing, and limited understanding of metric reliability make progress in MLLM unlearning difficul...
  </details>

- **2026-10-07** — Talal Alrawajfeh, Cristiana Diaconu, Ossi Räisä et al. — [Efficient Provably Private Classification with a Tabular Foundation Model](http://arxiv.org/abs/2610.10068v1)
  <details><summary>📄 Abstract</summary>
  Tabular data underpin prediction and decision-making in medicine, finance, government and science, but often contain sensitive individual-level information, creating a need for accurate prediction while preserving privacy. Traditional private learning provides formal privacy guarantees, but requires slow dataset-specific optimisation, suffers substantial utility loss under strong privacy, and is often difficult to apply correctly. Tabular foundation models adapt rapidly to new datasets, but exis...
  </details>

- **2026-10-07** — Teng-Ruei Chen — [Sensitive-Topic Leakage Through LLM Routing Metadata: Measurement and Mitigation](http://arxiv.org/abs/2610.09981v1)
  <details><summary>📄 Abstract</summary>
  LLM routers pick a cheap or expensive model per request by its content, and many gateways and some cloud platforms can log that choice with content logging off. We measure this privacy channel beyond token counts, accounting for noisy labels and repeated prompts. We run pre-registered studies on 1.7 million real requests (WildChat-1M, LMSYS-Chat-1M) with two cost/quality routers and a domain router, survey eleven systems' logging, and test post-processing defenses. At matched length, the shift's...
  </details>

- **2026-10-07** — Ankita Das, Ambarish Parthasarathy, Sumohana S. Channappayya et al. — [FedSSMCoOp: SSM Encoders for light-weight Federated Prompt Learning for Few-shot Classification](http://arxiv.org/abs/2610.09907v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) have shown strong performance across a wide range of downstream vision tasks, thanks to the complementary information contained in the respective domains. Despite the performance gains, most of these approaches rely on aligning these domains using the cosine similarity metric, which fails to capture token-level structure and cross-modal interactions prior to the classification stage. This is especially critical in biomedical applications under federated constraints,...
  </details>

- **2026-10-07** — Xiao Han, Aoyang Quan, Xiangyu Zhao et al. — [LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy](http://arxiv.org/abs/2610.09466v1)
  <details><summary>📄 Abstract</summary>
  Unmanned aerial vehicle (UAV) dispatch is beginning to move beyond isolated path planning and optimization-driven resource allocation toward system-level coordination supported by semantic reasoning and LLM-based interfaces. This survey provides a unified characterization of LLM-enabled UAV dispatch systems that bridges semantic intent, symbolic decision-making, and physical UAV execution. Rather than treating LLMs as standalone add-ons, we conceptualize them as a cross-layer semantic orchestrat...
  </details>

- **2026-10-07** — Vita Santa Barletta, Danilo Caivano, Rebecca Margiotta et al. — [BagDINO: Multi-View Baggage Re-Identification with DINOv3](http://arxiv.org/abs/2610.10160v1)
  <details><summary>📄 Abstract</summary>
  Mishandled checked baggage remains a recurrent issue in airport operations, and current recovery workflows still largely rely on tag-based tracking, which does not directly support visual identification when tag evidence is missing or unavailable. This paper investigates baggage re-identification as an instance-level retrieval problem in a multi-camera setting, leveraging DINOv3 foundation-model representations to match a query image against a gallery of registered baggage images. A Torchreid-st...
  </details>

- **2026-10-07** — Yong Cao, Markus Flicke, Haoyu He et al. — [LLM4Impact: Integrating Heterogeneous Information for Scientific Impact Prediction](http://arxiv.org/abs/2610.10138v1)
  <details><summary>📄 Abstract</summary>
  Predicting the future impact of a newly published paper is challenging because it must be inferred from heterogeneous evidence available at publication time. Existing approaches often rely on a single source of information or combine multiple sources without accounting for their different predictive roles. In this paper, we present LLM4Impact, an evidence-aware method for scientific impact prediction that learns to represent, integrate, and calibrate heterogeneous information. LLM4Impact combine...
  </details>

- **2026-10-07** — Prabhath Chellingi, Raviraja G, Viraj Bagal — [From Plausible Hierarchies to Useful Taxonomies: Evaluating Agentic Harnesses on Customer Feedback](http://arxiv.org/abs/2610.09377v1)
  <details><summary>📄 Abstract</summary>
  Taxonomies are the symbolic representations through which AI systems organize evidence, aggregate patterns, and answer questions over large document collections. Over customer feedback, the category tree decides how every record is counted and routed, which problems get seen, and which team owns them. Agentic harnesses now make it easy to generate a plausible-looking hierarchy, and such trees are checked today with generic, individually scoped checks: each name fits its description, sits under t...
  </details>

- **2026-10-06** — Michael Tang, Mahmoud Abdelgalil, Jorge I. Poveda — [The Deceptive Bandit Problem: Exploratory Coupling and the Fragility of Multi-Agent Learning](http://arxiv.org/abs/2610.09120v1)
  <details><summary>📄 Abstract</summary>
  Randomized exploration is central to bandit learning, multi-agent reinforcement learning, and zeroth-order policy search, yet its independence and privacy are usually only treated as technical assumptions. We show that these properties are critical for security purposes and demonstrate how an adversarial agent can exploit privileged information on another agent's exploration. We analyze a deceiver-victim pair in the minimal two-player strongly monotone setting, where a deceptive player obtains l...
  </details>

- **2026-10-06** — Rafid Ahmed, Joseph Fioresi, Mubarak Shah et al. — [CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents](http://arxiv.org/abs/2610.08871v1)
  <details><summary>📄 Abstract</summary>
  Language model agents are increasingly deployed to automate everyday digital chores from managing emails and social media to handling banking and bills allowing users to step away from supervision. However, this capability also exposes sensitive information to phishing. Safe execution requires distinguishing malicious requests from genuine ones without simply refusing to act. Despite its practical importance, this problem remains underexplored and it is unclear whether current agents or existing...
  </details>

- **2026-10-06** — Thushara Manjari Naduvilakandy, Hyeju Jang, Mohammad Al Hasan — [Multi-Objective Aligned Small Language Model Framework for SUD Patient Dialogue Generation](http://arxiv.org/abs/2610.09209v1)
  <details><summary>📄 Abstract</summary>
  Substance Use Disorder (SUD) counseling requires patient responses that reflect underlying cognitive states such as beliefs, coping strategies, and readiness for change. Although large language models (LLMs) can generate fluent text, they often fail to produce cognitively coherent and clinically realistic patient behavior, especially under ethical and data-scarce clinical settings. Moreover, deploying frontier-scale LLMs in healthcare applications presents practical challenges including high com...
  </details>

- **2026-10-06** — Jacqueline Rowe, Animesh Srivastava, Sai Teja Peddinti et al. — [Move Fast and Mend Things: Keeping Up with Evolving AI Harms Using Social Media Commentary](http://arxiv.org/abs/2610.09082v1)
  <details><summary>📄 Abstract</summary>
  The rapid deployment of AI systems has created socio-technical, psychological, and operational harms that can elude ex-ante threat modelling and ex-post incident tracking. We introduce an LLM-assisted thematic analysis pipeline to dynamically detect, categorise, and track emerging AI harms from large-scale social media data. Applying it to 5.7 million Reddit post summaries over 18 months (01/2025 to 06/2026), we curate and release a dataset of 575,000 AI harm-related posts and a bottom-up AI har...
  </details>

- **2026-10-06** — János Kertész, Marc Barthelemy, Guido Caldarelli et al. — [Social Physics: A manifesto](http://arxiv.org/abs/2610.08117v2)
  <details><summary>📄 Abstract</summary>
  Social Physics seeks quantitative, empirically testable explanations of collective human behavior. Its name has a long and contested history, but its contemporary program is neither the claim that society is literally a physical system nor an attempt to replace the social sciences with physics. It is an interdisciplinary practice: observation and experimentation, model construction, mathematical and computational analysis, and repeated confrontation with data. The field has been transformed by a...
  </details>

- **2026-10-06** — Halil İbrahim Kanpak, Sinem Sav, Alptekin Küpçü — [HE-OFT: Privacy-Preserving One-Shot Federated Fine-Tuning under Homomorphic Encryption](http://arxiv.org/abs/2610.08255v1)
  <details><summary>📄 Abstract</summary>
  Many organizations adapt large pretrained models to their own tasks by fine-tuning on private data. Several of these parties often hold data for the same task and wish to fine-tune a model together without pooling that data. Federated learning (FL) enables joint fine-tuning, but reconstruction attacks on shared intermediate values (the model or its gradients) remain a privacy risk. A one-shot protocol that exchanges one encrypted contribution exposes no intermediate value. Such a protocol still ...
  </details>

- **2026-10-06** — Kartick Sutradhar, Ranjitha Venkatesh — [Systematically Optimized CNN-Transformer with Focal Loss for Imbalanced Intrusion Detection on NSL-KDD](http://arxiv.org/abs/2610.08066v1)
  <details><summary>📄 Abstract</summary>
  Intrusion Detection Systems (IDS) struggle with imbalanced datasets like NSL-KDD, especially in detecting rare R2L and U2R attacks. This work describes a systematically optimized and explainable framework using a CNN-Transformer architecture to improve performance on highly imbalanced data. We decided to use XGBoost for feature selection and Focal Loss as the main mechanism for minority class learning. We used Optuna for end-to-end hyrate=0.00042, batch size=256, and Focal Loss γ), using a thoug...
  </details>

- **2026-10-06** — Nikolaos Kekatos, Apostolos Valiakos, Alexios Lekidis et al. — [Quantifying the Privacy Posture of Operator-Side 5G/O-RAN Profiles](http://arxiv.org/abs/2610.07976v1)
  <details><summary>📄 Abstract</summary>
  Operator-side network profiles derived from 5G/ORAN traffic carry personal data such as ephemeral subscriber identifiers, slice-level KPIs, and control-plane signalling, and must be anonymised before release to a federated-learning aggregator, threat-intelligence exchange, or ML training pipeline. We study how much re-identification risk remains after standard operator-side anonymisation. We quantify privacy posture with k-anonymity, l-diversity and t-closeness, aggregate them into a composite P...
  </details>

- **2026-10-06** — Muhammad Saif ul Islam, Karar Haider, Manaal Malik et al. — [Zeppelin: Client-Side BFV Encryption and Decryption for Helium-Powered Microcontrollers](http://arxiv.org/abs/2610.08301v1)
  <details><summary>📄 Abstract</summary>
  The growth of the Internet of Things (IoT) has raised concerns over the privacy of data collected by resource-constrained sensing devices. Homomorphic encryption (HE) addresses this by letting a device encrypt its data once and an untrusted cloud server compute on the ciphertext without seeing the values. In practice, HE's memory and computational cost have kept it out of reach of microcontroller-class devices. Prior work, SEAL-Embedded, made this feasible using CKKS, but left three gaps: its ar...
  </details>

- **2026-10-06** — Thinh D. Le, Son T. Nguyen, Duong Q. Nguyen et al. — [WareFly-VLA: A Vision-Language-Action Framework for UAV Navigation and Human Tracking in Smart Warehouses](http://arxiv.org/abs/2610.08526v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have achieved impressive results in robotic manipulation and ground-mobile navigation, yet language-conditioned control of unmanned aerial vehicles (UAVs) in smart warehouses remains largely unexplored, hindered by the lack of benchmarks that jointly provide continuous low-level flight actions, fine-grained natural-language target descriptions, and realistic industrial environments. This paper introduces WareFly-VLA, a photorealistic UAV VLA framework and data...
  </details>

- **2026-10-06** — Zhen Yu, Wenyang Liu, Kejun Wu et al. — [Image Bitstream Fine-grained Understanding for Privacy-Friendly AIoT](http://arxiv.org/abs/2610.08414v1)
  <details><summary>📄 Abstract</summary>
  Image Bitstream Fine-grained Understanding (IBFU) aims to directly perform fine-grained classification and semantic description generation from encoded image byte sequences. In contrast to conventional pixel-domain visual understanding, IBFU conducts semantic analysis without fully decoding images into the pixel domain. Since pixel-level visual content is not explicitly reconstructed during inference, this paradigm reduces visual exposure within the processing pipeline and suits privacy-friendly...
  </details>

- **2026-10-06** — Tobias Hallmen, Fabian Deuser, Robin-Nico Kampa et al. — [The Failure Is in the Readout: Fine-Grained Emotion Recognition Benchmarks Measure Elicitation, Not Perception](http://arxiv.org/abs/2610.08162v1)
  <details><summary>📄 Abstract</summary>
  Fine-grained emotion recognition supports therapy tools and social robots, but it needs facial data, which raises privacy and data-protection concerns. EmoNet-Face-HQ answers that with generated portraits, expert-rated over a $40$-category taxonomy far finer than the usual six to eight basic emotions. Under the protocol it ships with, vision-language models (VLMs) score poorly on that taxonomy, and the benchmark concludes that a dedicated fine-tuned model is necessary: Empathic-Insight-Face (EIF...
  </details>

- **2026-10-06** — János Kertész, Marc Barthelemny, Guido Caldarelli et al. — [Social Physics: A manifesto](http://arxiv.org/abs/2610.08117v1)
  <details><summary>📄 Abstract</summary>
  Social Physics seeks quantitative, empirically testable explanations of collective human behavior. Its name has a long and contested history, but its contemporary program is neither the claim that society is literally a physical system nor an attempt to replace the social sciences with physics. It is an interdisciplinary practice: observation and experimentation, model construction, mathematical and computational analysis, and repeated confrontation with data. The field has been transformed by a...
  </details>

- **2026-10-06** — Chuan Li, Chengyu Wang, Cen Chen et al. — [SAGE: Semantic Anchor-Guided Evolution for Grounded Medical QA Data Synthesis](http://arxiv.org/abs/2610.08093v1)
  <details><summary>📄 Abstract</summary>
  Developing reliable models for clinical tasks, such as Medical Question Answering (QA), is severely constrained by the limited availability of high-quality, expert-annotated training data. This challenge is exacerbated by stringent privacy requirements and the impracticality of utilizing large open-source corpora or proprietary cloud APIs within resource-limited clinical settings. To address these obstacles, we introduce SAGE (\textit{Semantic Anchor-Guided Evolution}), a novel data synthesis fr...
  </details>

- **2026-10-06** — Aksel Fristrup, Sumit Pandey, Ankit Kariryaa — [ApexQuant: Data-Free Elastic Quantization by Residual Re-Isotropization](http://arxiv.org/abs/2610.07904v1)
  <details><summary>📄 Abstract</summary>
  We introduce ApexQuant, a calibration-free quantization method that recursively re-quantizes the residual error, serving as a refinement layer on top of existing quantizers. We establish that a fresh random rotation returns each residual to the uniform distribution on the hypersphere, which characterizes the rate of progressive error decay across successive passes. This result lets us determine, before any weight is read, how many passes a layer needs for a target weight-space error. Every prefi...
  </details>

- **2026-10-06** — Sushmita Khan, Connor Pennington, Bart P Knijnenburg — [A Pedagogically Demonstrative Model Visualizing the Pathway from Online Interactions to Personalized Recommendation](http://arxiv.org/abs/2610.07744v1)
  <details><summary>📄 Abstract</summary>
  Personal digital activity increasingly shapes online experiences, yet few users have been educated regarding the processes transforming raw interactions into personalized suggestions. We developed an education artifact that illustratively simulates how AI leverages users' digital activities to shape online recommendations (e.g., ads). Our artifact processes users' digital activity using a locally-hosted LLM to generate user profiles of their inferred interests and personalized recommendations. A...
  </details>

- **2026-10-06** — Peihua Mai, Zhuoyan Shao, Xinbao Qiao et al. — [Illusory Pattern Perception Drives Spurious Inference in Large Language Models](http://arxiv.org/abs/2610.07791v1)
  <details><summary>📄 Abstract</summary>
  Illusory pattern perception is a well-documented human cognitive tendency to infer meaningful relationships in data that is actually random. Such a tendency, often described as "connecting the dots" where none exist, can result in systematic reasoning errors. This paper investigates whether Large Language Models (LLMs) exhibit such perceptual tendencies, which can lead to systematic errors in downstream applications. To our knowledge, this work presents the first systematic study of illusory pat...
  </details>


### 📂 misuse
*滥用与误用 / Misuse & Abuse* — 13 papers

- **2026-10-07** — Miao Yu, Hao Huang, Lu Yuan et al. — [SafeEvo: Deciphering the Safety Alignment Mechanism and Evolution in Language Models](http://arxiv.org/abs/2610.09600v1)
  <details><summary>📄 Abstract</summary>
  Safety interpretability advances the study of Large Language Model (LLM) alignment from behavioral constraints driven by data or algorithms towards a deeper understanding of internal mechanisms. However, existing works have focused primarily on safety-related representations, attention heads, or neurons after alignment, while largely overlooking the safety mechanisms in pretrained-only models and their evolution across alignment checkpoints. To address this, we propose SafeEvo, an interpretabili...
  </details>

- **2026-10-07** — Yuyao Ge, Yiwei Wang, Yuchen He et al. — [SkillForge: Co-Evolving Skills and Agents via Dynamic Skill Lifecycles](http://arxiv.org/abs/2610.09832v1)
  <details><summary>📄 Abstract</summary>
  Memory-augmented reinforcement learning strengthens LLM agents' ability to solve complex long-horizon tasks. Skills are one such form of memory, pairing instructions with an applicability condition over task types. However, retaining every skill indiscriminately as the policy improves lets obsolete or harmful entries accumulate and mislead the agent. We propose SkillForge, an agentic RL method that compiles and evolves the skill library through a fitness-driven skill lifecycle of trial, active, ...
  </details>

- **2026-10-07** — Mohnish Harwani, Yujia Zheng — [Sequential Pretraining Favors Large Models](http://arxiv.org/abs/2610.09611v1)
  <details><summary>📄 Abstract</summary>
  Large neural networks often acquire capabilities that small models fail to learn. Does this stem from large models learning more representative features, or from being more robust to unaccounted-for adverse effects introduced during training? We define and quantify one such adverse effect, primacy bias, as the extent to which exposure to early data distributions impairs later learning. We show that small models can allocate learning capacity inefficiently toward early distributions, whereas suff...
  </details>

- **2026-10-07** — Litao Hu, Yutong Tang — [The Winner's Curse in LLM Self-Improvement Loops: Selection Noise, Lock-in, and Acceptance Rules](http://arxiv.org/abs/2610.09239v1)
  <details><summary>📄 Abstract</summary>
  Self-improving LLM systems propose changes to themselves and keep those that score better on a small evaluation set. We treat this keep-if-better step as selection under measurement noise, model the correlated errors of the candidates in a single decision, and study empirically what happens when the evaluation set is reused. In runs where Qwen models rewrite their own instructions and every candidate is also scored on 600 held-out items, most proposals after the first are harmful, and the model ...
  </details>

- **2026-10-06** — Pavan Maddula — [Quad-State Safety Evaluation of Open-Weight Large Language Models on Non-Canonical Inputs](http://arxiv.org/abs/2610.09033v1)
  <details><summary>📄 Abstract</summary>
  Standard safety evaluations of large language models assess harmful requests written in canonical plain text, while models in real-world deployment routinely receive inputs containing emojis, altered spellings, encoded strings, and character-level variations. This work introduces the Adversarial Surface-Form Robustness Dataset (ASRD), comprising 2,100 prompts across seven distinct surface-form families. Five open-weight language models are evaluated across these prompts, producing 10,500 respons...
  </details>

- **2026-10-06** — Domenic Rosati, Alessa Carbo, Ali Dadsetan et al. — [Removing Information Content Does Not Certify Tamper Resistance in Open-Weight Models](http://arxiv.org/abs/2610.09004v1)
  <details><summary>📄 Abstract</summary>
  Does removing harmful information make open-weight models resistant to fine-tuning attacks? We show that mutual information at release alone cannot universally certify slow recovery. Function-preserving reparameterizations leave information unchanged while altering gradient-descent geometry, so an invariant certificate is bounded by the fastest reachable parameterization. We apply this principle to weight--data mutual information under training-data filtering and label--representation mutual inf...
  </details>

- **2026-10-06** — Bibhas Adhikari, Ramya Srinivasan — [A Cognitive-Aware QML-CRL Framework for Detecting Affinity and Romance-Investment Fraud](http://arxiv.org/abs/2610.09141v1)
  <details><summary>📄 Abstract</summary>
  We present a hybrid quantum-classical framework that detects affinity and romance-investment fraud by modelling the cognitive biases in a manipulative conversation. In our proposed framework, cognitive biases central to this fraud class are carried by dedicated qubits in a structured parameterized quantum circuit, together with a frame qubit makes the encoding sensitive to the temporal order of manipulative reframing, and a narrative qubit that aggregates co-occurrence through a trainable entang...
  </details>

- **2026-10-06** — Yiming Xu, Hongyue Yu, Beihua Yang et al. — [DecepEval: A Benchmark for Evaluating Deception in LLM Agents](http://arxiv.org/abs/2610.07967v1)
  <details><summary>📄 Abstract</summary>
  As large language model (LLM) agents become increasingly autonomous, they may pursue task performance through deception, raising concerns about their reliable deployment. Existing evaluations show that LLM agents can deceive, but often examine isolated scenarios or narrowly defined conditions, limiting systematic understanding of when deception becomes more likely. To address this gap, we introduce DecepEval, a benchmark comprising 1,532 instances across 3 task families and 28 professional scena...
  </details>

- **2026-10-06** — Jingyu Zhang, Shruti Palaskar, Daniel Khashabi et al. — [SIGMA: Self-Improving Alignment Generalization from a Model Spec](http://arxiv.org/abs/2610.07935v1)
  <details><summary>📄 Abstract</summary>
  LLM agents are increasingly capable of executing complex tasks and of recursively improving themselves on easy-to-verify objectives such as software engineering and mathematics. Since alignment is much harder to verify, this creates a growing risk of capabilities increasing without appropriate safety alignment, especially as capabilities expand to auto-research and cybersecurity. Existing approaches focus on capability self-improvement using verifiable feedback or on alignment training with supe...
  </details>

- **2026-10-06** — Ziyuan Yang, Wenxuan Ding, Shangbin Feng et al. — [Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models](http://arxiv.org/abs/2610.07774v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) face compositional safety risks where harmful intent emerges from the interaction between visual and textual inputs. As mixture-of-experts (MoE) VLMs become increasingly common, recent work has explored various safety interventions, including prompting, supervised fine-tuning, and routing-based expert steering. However, these methods show inconsistent improvements across models and evaluation distributions, and the intervention into model behavior or internal states...
  </details>

- **2026-10-06** — Egor Pakhomov, Erik Nijkamp — [Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus](http://arxiv.org/abs/2610.08722v1)
  <details><summary>📄 Abstract</summary>
  Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that p...
  </details>

- **2026-10-06** — Yu Xia, Jiangfan Zhang, Jun Xiao et al. — [Personal-Agent Mediated Recommendation with Cross-Platform User History](http://arxiv.org/abs/2610.07588v1)
  <details><summary>📄 Abstract</summary>
  Modern recommendation is shifting from platform-centric personalization toward user-governed personalization, where a personal LLM agent can act on the user's behalf across services. We formalize this emerging paradigm as Personal-Agent Mediated Recommendation: a platform recommender ranks a candidate set using platform-local information, and a personal agent uses user-authorized cross-platform history to mediate the resulting ranking and produce the final top-K slate. Such mediation is nontrivi...
  </details>

- **2026-10-05** — Ziqun Bao, Xinyu Zhang, Yuchen Shao et al. — [Harmful SFT Leaves a Continuous Trace in LLM Checkpoint Updates](http://arxiv.org/abs/2610.07518v1)
  <details><summary>📄 Abstract</summary>
  Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations. This work asks a different question: Do the target behaviors optimized during supervised fine-tuning (SFT) leave readable evidence directly in checkpoint updates? We find that harmful-compliance SFT induces a continuous, objective-dependent ordering in checkpoint-update space. Using a reference geometry defined by pure harmful...
  </details>


### 📂 red-teaming
*红队测试 / Red Teaming* — 3 papers

- **2026-10-07** — Georgios Koutidis, Nikolaos Kekatos, Tom Nianios et al. — [Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy](http://arxiv.org/abs/2610.09906v1)
  <details><summary>📄 Abstract</summary>
  Security Operations Centers (SOCs) for information technology and operational technology share one incident-response problem: a flood of correlated alerts and too few analysts. Large Language Models (LLMs) are increasingly proposed as reasoning engines that triage alerts and, in autonomous deployments, issue commands that block IPs, kill processes, or quarantine files on production hosts. This coupling introduces a new risk: a single adversarial alert can become a remote code path through the LL...
  </details>

- **2026-10-07** — Subhabrata Majumdar, Rajlakshmi Chavan — [Defensive Sufficiency in a Stackelberg Model of AI Security](http://arxiv.org/abs/2610.09892v1)
  <details><summary>📄 Abstract</summary>
  Feedback from automated testing, human red teaming, and incident response can strengthen an AI system's defenses when discovered failures lead to effective repairs. We study when this feedback process provides sufficient protection and when investing in it is economically worthwhile. We begin by showing that an attack surface composed of finite number of inputs is defended with probability 1 if every unresolved attack has a persistent chance of discovery, repairs are effective, and subsequent up...
  </details>

- **2026-10-07** — Wanjing Han, Levi Taiji Li, Mu Zhang et al. — [Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution](http://arxiv.org/abs/2610.09240v1)
  <details><summary>📄 Abstract</summary>
  Modern web agents built on large vision-language models process webpages, select relevant UI elements, and translate model outputs into browser actions. Existing visual red-teaming approaches use adversarial visual content to manipulate this process. However, they primarily target model inference and do not explicitly account for structured input processing or action post-processing. Consequently, model-level success does not establish control over browser execution and cannot reliably character...
  </details>


### 📂 vulnerability
*漏洞与攻击面 / Vulnerabilities & Attack Surfaces* — 37 papers

- **2026-10-07** — Aleksandar Armacki, Haoyuan Cai, Ali H. Sayed — [Decentralized SGD under Heavy-Tailed Noise: Optimal Convergence Rates and the Role of Gradient Clipping](http://arxiv.org/abs/2610.10527v1)
  <details><summary>📄 Abstract</summary>
  Heavy-tailed noise has been widely observed in modern machine learning, motivating the use of methods like gradient clipping and normalization. While these methods are well understood in centralized settings, much less is known in decentralized ones, where applying a nonlinearity to local gradients affects both optimization and consensus. Recent works on decentralized non-convex optimization have studied both clipping and normalization under heavy-tailed noise, with clipping yielding suboptimal ...
  </details>

- **2026-10-07** — Hao-Run Cai, Si-Yang Liu, Zi-Jian Cheng et al. — [Thinking in Depth: Retrospective Inference for Tabular Foundation Models](http://arxiv.org/abs/2610.10317v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) are pretrained across diverse tabular tasks and make predictions on a new table at inference time using its labeled examples as context. Most recent TFMs perform such in-context prediction with stacked Transformer layers, repeatedly transforming how examples are represented and compared. By tracing individual queries through several strong TFMs, we find that predictive refinement is highly uneven across depth and is often concentrated in later layers. This uneven...
  </details>

- **2026-10-07** — William Chen, Prem Seetharaman, Ke Chen et al. — [CrossEdit: Cross-Modal Training Enables Rich Audio-Visual Editing](http://arxiv.org/abs/2610.10264v1)
  <details><summary>📄 Abstract</summary>
  Multimedia editing requires generative models to interpret complex, compositional instructions and modify only the desired elements across modalities, a capability largely beyond existing systems. Current approaches are typically limited to simple, single-attribute edits within one modality, since diverse, high-quality editing pairs are hard to obtain, especially for cross-modal tasks where aligned audiovisual (AV) data is scarce. We present CrossEdit, a unified omni-modal editing model for imag...
  </details>

- **2026-10-07** — Dang K Le, Wenxuan Shi, Xinyu Xing — [On the Reliability of LLM-Based Vulnerability Patching Benchmarks](http://arxiv.org/abs/2610.10150v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have shown strong potential for automated vulnerability patching, but current benchmarks can substantially distort reported performance. Drawing on extensive experience developing, running, and stress-testing such frameworks, we identify under-examined pitfalls across three dimensions: (1) agent-level factors, where prompting, tool availability, and detailed instructions can raise success rates without improving developer-aligned patch quality; (2) framework-level fa...
  </details>

- **2026-10-07** — Xiangtao Kong, Shuaizheng Liu, Rongyuan Wu et al. — [HarnessIR: Harnessing Multimodal Foundation Models for Universal Real-World Image Restoration](http://arxiv.org/abs/2610.10133v1)
  <details><summary>📄 Abstract</summary>
  Real-world low-quality images suffer from complex mixed degradations, including but not limited to noise, blur, atmospheric effects, etc. Recent agentic methods usually model real-world image restoration (Real-IR) as a sequential tool calling problem over task-specific single-degradation restoration models. This paradigm, however, is fundamentally limited because complex real-world degradations cannot be cleanly undone degradation by degradation, and the tool used for task-specific models caps t...
  </details>

- **2026-10-07** — Huanan Liu, Ye Li, Kangye Ji et al. — [RealtimeWAM: How Fast Can I Run My World Action Model?](http://arxiv.org/abs/2610.10079v1)
  <details><summary>📄 Abstract</summary>
  World Action Models (WAMs) combine visual dynamics modeling with action generation, but their high inference latency limits responsive robot control. Recent efforts accelerate inference by removing explicit future-video generation at test time, as in FastWAM, an approach that requires a specially tailored architectural design. More general caching strategies exploit feature redundancy, but redundancy alone does not capture the changing computational demands of closed-loop control. To address the...
  </details>

- **2026-10-07** — Jicheng Zhou, Kahim Wong, Jialong Wang et al. — [EASE: Entropy-Adaptive Distribution Shaping for Evading AI-generated Text Detectors](http://arxiv.org/abs/2610.09976v1)
  <details><summary>📄 Abstract</summary>
  AI-generated text (AIGT) detection can be sensitive to the decoding choices of the source large language model (LLM). We observe that perturbing next-token logits or adjusting sampling temperature can reduce detection performance, providing a clear signal of detector vulnerability to decoding-time distribution changes. Building on this observation, we propose EASE (Entropy-Adaptive Distribution Shaping for Evasion), a training-free and detector-agnostic framework for evading AIGT detectors. EASE...
  </details>

- **2026-10-07** — Zhuchenyang Liu, Yao Zhang, Yu Xiao — [Inverting Multi-Vector Visual Document Indices](http://arxiv.org/abs/2610.09920v1)
  <details><summary>📄 Abstract</summary>
  Prevailing multi-vector visual document retrievers store each page as about a thousand patch vectors, often in vector databases run by a third party. Since no one can read a page from its vectors, this index is easily treated as less sensitive than the page. However, because the index keeps one vector per patch in raster order, and each vector is computed by a vision-language model pre-trained to read documents, we hypothesize that whoever runs or breaches the store can reproduce a page from its...
  </details>

- **2026-10-07** — Ruohan Li, Miaoqing Tian, Haipeng Qu et al. — [GRAML: Graph-Grounded Reasoning and Multi-Task Learning for LLM-Based Software Vulnerability Detection](http://arxiv.org/abs/2610.09605v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) have been widely applied to software vulnerability detection. However, their performance is often limited by insufficient use of control-flow and data-flow information. In this paper, we propose GRAML, a framework that combines graph evidence, vulnerability description generation, and multi-task training. GRAML first performs static analysis on C/C++ programs to extract critical source lines and typed line relations as structural evidence. It then uses this evidence ...
  </details>

- **2026-10-07** — Xinsong Feng, Peng Du, Zhizhuo Yang et al. — [Denoising Blocks, Not Tokens: Efficient Compressed Continuous Diffusion with Branching Token Realization](http://arxiv.org/abs/2610.09311v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (DLMs) generate text through iterative parallel refinement, offering the potential for higher throughput than autoregressive (AR) decoding. However, most DLMs still maintain one generative state per token, so every denoising step processes a state sequence as long as the output sequence, limiting the throughput gains from parallel generation. Continuous DLMs provide an additional degree of freedom: a single continuous state can represent multiple tokens, allowing diffus...
  </details>

- **2026-10-07** — Bhavini Jeloka, Siddhartha Ganguly, Panagiotis Tsiotras — [Beyond Nominal Equilibria: Risk-Averse Multi-Population Mean-Field Games](http://arxiv.org/abs/2610.09244v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in mean-field games and its multi-population variants enable large-scale heterogeneous multi-agent systems to be modeled through representative agents and their associated mean-field distributions. However, existing approaches do not explicitly account for uncertainty in the behavior of other populations. To this end, we introduce a new paradigm: risk-averse multi-population mean-field games, where each population optimizes a worst-case expected reward over dynamically feasible a...
  </details>

- **2026-10-06** — Habibur Rahaman, Swastik Bhattacharya, Sanjay Das et al. — [BARE-AI: Bit-Flip Attack Resilience in AI Hardware through Built-in Performance Monitors](http://arxiv.org/abs/2610.08739v2)
  <details><summary>📄 Abstract</summary>
  Deep Neural Networks (DNNs) are integral to many safety critical systems, yet they remain highly vulnerable to bit-flip attacks (BFAs), where a few memory level perturbations can drastically degrade accuracy. Existing defenses incur significant hardware overhead, depend on retraining, or fail against targeted flips. We propose BARE-AI, a runtime framework that detects, localizes, and mitigates BFAs during inference. BARE-AI introduces AI Performance Counters (APCs), lightweight hardware monitors...
  </details>

- **2026-10-06** — Shangye Song, Dong Gong, Hong Jia et al. — [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](http://arxiv.org/abs/2610.08777v1)
  <details><summary>📄 Abstract</summary>
  Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls. Many systems use chunk-wise autoregressive generation with few-step denoising, but each chunk still requires several costly denoising iterations. Training-free caching can reduce this cost, yet existing policies make reuse decisions primarily from model-internal denoising dynamics and do not explicitly account for control transitions. Actually, interactive generation explici...
  </details>

- **2026-10-06** — Habibur Rahaman, Swastik Bhattacharya, Sanjay Das et al. — [BARE-AI: Bit-Flip Attack Resilience in AI Hardware through Built-in Performance Monitors](http://arxiv.org/abs/2610.08739v1)
  <details><summary>📄 Abstract</summary>
  Deep Neural Networks (DNNs) are integral to many safety critical systems, yet they remain highly vulnerable to bit-flip attacks (BFAs), where a few memory level perturbations can drastically degrade accuracy. Existing defenses incur significant hardware overhead, depend on retraining, or fail against targeted flips. We propose BARE-AI, a runtime framework that detects, localizes, and mitigates BFAs during inference. BARE-AI introduces AI Performance Counters (APCs), lightweight hardware monitors...
  </details>

- **2026-10-06** — Jiahua Li, Zixu John, Tom Zhong et al. — [Forensic Reserve: Eliciting Latent Knowledge for Image Forgery Detection](http://arxiv.org/abs/2610.08639v1)
  <details><summary>📄 Abstract</summary>
  As generated images become increasingly realistic, reliable forgery detection is essential for maintaining trust in visual information. However, existing methods primarily rely on task-specific supervision to adapt vision foundation model representations, without fully exploiting internal forensic knowledge to guide detection. To address this limitation, we propose Reserve-Guided Elicitation (RGE), a framework that treats sparse, origin-sensitive internal components in pretrained models as a for...
  </details>

- **2026-10-06** — Songlin Jiang, Zhiyu Li, Terry Kong et al. — [NeMo-DCR: Bit-Exact Delta-Compressed Refit for Scalable Agentic RL at Trillion-Parameter Scale](http://arxiv.org/abs/2610.08430v1)
  <details><summary>📄 Abstract</summary>
  Agentic reinforcement learning (RL) disaggregates training from rollout, so each policy update must reach the rollout clusters before the next batch. Transferring a full 1T checkpoint for such weight synchronization (refit) takes 87.5 min between two AWS regions. Measurements of BF16 training show that about 1% of weights change their stored values per step. Recent systems exploit this sparsity but fall short on placement, exactness, or efficiency: they reimplement placement rules, assemble full...
  </details>

- **2026-10-06** — Hao Sun, Yibin Yao, Chaohai Xie et al. — [Case-Level Verification in Scanner-LLM Cascades: Overcoming the Alert Aggregation Bottleneck to Expand the FRR-TPR Trade-off Space](http://arxiv.org/abs/2610.08406v1)
  <details><summary>📄 Abstract</summary>
  Dynamic Application Security Testing (DAST) scanners achieve high recall but also produce a large number of false positives, resulting in substantial manual triage costs. Large Language Models (LLMs), when used for independent detection, achieve extremely high recall (95.4%-100%) but also exhibit prohibitively high false positive rates (49.6%-85.0%), precluding their use as standalone replacements for scanners. A natural solution is a two-stage cascade consisting of scanner detection followed by...
  </details>

- **2026-10-06** — Mandana Ghadamian, David Mohaisen — [Learning from Failures: A Failure-Driven Prompt Refinement for LLM-Based Vulnerability Analysis](http://arxiv.org/abs/2610.08405v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models have emerged as promising tools for software vulnerability analysis, but their effectiveness depends heavily on prompt design. Existing research primarily compares prompting strategies using aggregate performance metrics, providing limited insight into why models fail or how prompts can be improved systematically. We propose Failure-Driven Prompt Refinement (FDPR), a methodology that analyzes recurring model failures to guide evidence-based prompt refinement. Using the Damn...
  </details>

- **2026-10-06** — Adeline Pittet, Shien Zhu, Valérie Verdan et al. — [SSR: Sparse Segment Reduction for Ternary GEMM Acceleration](http://arxiv.org/abs/2610.08403v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) require substantial computational resources, limiting their deployment on resource-constrained hardware. Ternary LLMs mitigate these demands through weight quantization via ternary values, achieving significant compression often with 50-90% sparsity. However, existing approaches have limitations: methods optimized for ternary weights, such as BitNet, redundant segment reduction (RSR), and its improved version RSR++, do not exploit sparsity structures, while conventio...
  </details>

- **2026-10-06** — Yubo Song, Subham Sahoo, Freja Basse — [Infrastructure-Native Computing with Electric Power Grids](http://arxiv.org/abs/2610.08390v1)
  <details><summary>📄 Abstract</summary>
  Computing is conventionally implemented by hardware engineered for information processing. Here we investigate infrastructure-native computing: the use of a physical system built for another primary function as a fixed computational operator. In time-domain simulations of an IEEE 14-bus electrical network, Kirchhoff's current law and Ohm's law relate voltage-reference perturbations applied at distributed controllable nodes interfaced by power electronics converters to current responses through a...
  </details>

- **2026-10-06** — Shuo Yang, Changbai Li, Linlin Yang et al. — [DIPrune: Task-Aware Token Pruning with Dual Importance for Efficient Multimodal Language Models](http://arxiv.org/abs/2610.08341v1)
  <details><summary>📄 Abstract</summary>
  Recent training-free pruning approaches for Multimodal Large Language Models (MLLMs) effectively cut computational overhead by exploiting visual redundancy or text-vision attention. However, they frequently suffer from semantic degradation due to their task-agnostic design or unreliable attention estimates. Based on our empirical analysis, we have found that this issue arises because salient tokens in shallow layers persistently suppress emerging semantic ones through numerical inertia, leading ...
  </details>

- **2026-10-06** — Jianyong Hu, Wei Li — [Measurement Complexity of Quantum Compressed Sensing](http://arxiv.org/abs/2610.08234v1)
  <details><summary>📄 Abstract</summary>
  Conventional compressed sensing (CS) has a measurement lower bound of M = Ω(K log(N/K)) under non-adaptive measurements. Recent experiments on quantum compressed sensing (QCS) have reported numbers of measurements below this classical lower bound. In this work, we establish lower bounds on the measurement complexity of QCS from an information-theoretic and quantum-physical perspective. QCS exploits quantum parallelism, enabling a unitary domain-alignment evolution to act on a superposition of al...
  </details>

- **2026-10-06** — Haotian Chen, Shuaicheng Niu, Haocong Rao et al. — [Test-Time Agent Evolution for Long-Horizon Legal Reasoning](http://arxiv.org/abs/2610.08138v1)
  <details><summary>📄 Abstract</summary>
  Legal intelligence aims to support reliable decision-making across long-horizon legal processes involving evolving case states and multiple roles. However, real-world legal deployment exhibits substantial case heterogeneity in facts, evidence, and procedural contexts, exposing the limitations of static agent strategies. Moreover, legal reasoning is inherently interdependent across roles and procedural stages, making global reliability fundamentally different from isolated role competence. To add...
  </details>

- **2026-10-06** — Haoxiang Zhang, Qinglin Chen, Hiroaki Hayashi et al. — [Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight](http://arxiv.org/abs/2610.08077v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) turns agent experience into learning signals primarily through scalar outcome rewards after interaction. For group-relative objectives, however, this signal vanishes when all rollouts receive the same reward, even though their trajectories may reveal useful information about what the task requires and how the agent fails. We ask a complementary question: can hindsight teach an agent what it could have anticipated before acting? We introduce p...
  </details>

- **2026-10-06** — Yoshinari Fujinuma, Keisuke Kamahori, Ryuto Koike et al. — [SpeedrunBench: Challenging LLM Agents with Video Game Speedrunning](http://arxiv.org/abs/2610.08076v1)
  <details><summary>📄 Abstract</summary>
  Frontier LLM agents have been shown to be capable of solving increasingly complex tasks for which humans have measurable solutions. This begs the pertinent question of whether LLM agents can go beyond what humans have already solved. The ability to develop sophisticated strategies to tackle consequential problems becomes paramount as well-trodden, human-developed solutions become insufficient for problems for which we lack context or enough training data. We study agents' capability of such stra...
  </details>

- **2026-10-06** — Jordy Kieto — [Learning in Dreams, Winning in Reality: A Continuous Dyna Loop for a Ten-Hero MOBA](http://arxiv.org/abs/2610.08033v1)
  <details><summary>📄 Abstract</summary>
  World models are usually judged from the inside: by prediction loss, by the return a policy earns in imagination, or by how convincing their frames look. We judge one from the outside. We learn a structured, multi-agent world model of a complete ten-hero MOBA (206 units, every hero acting every tick, games of up to 6,000 ticks), train a policy only inside it with 1,400-tick free-running imagined episodes, and measure that policy in the real game against the opponent the game ships with. The real...
  </details>

- **2026-10-06** — Chengzhi Ye, Ruoyu Zhang, Lipeng Zhu et al. — [Movable Antenna-Enabled Multi-Target Sensing: Sidelobe Suppression via Position Optimization](http://arxiv.org/abs/2610.08008v1)
  <details><summary>📄 Abstract</summary>
  Movable antenna (MA) has emerged as a promising technology to unlock spatial degrees of freedom for wireless sensing systems. However, optimizing MA positions for multi-target sensing remains challenging due to the complicated coupling between the array geometry and unknown target directions, as well as severe sidelobe interference. In this paper, we propose an MA-enabled multi-target wireless sensing scheme to achieve both high-precision and robust target parameter estimation. To characterize t...
  </details>

- **2026-10-06** — Georgios Koutidis, Nikolaos Kekatos, Marina Korgiala-Karyda et al. — [Preparing an AI-Augmented SIEM for the EU Cyber Resilience Act: A Practitioner Case Study](http://arxiv.org/abs/2610.07873v1)
  <details><summary>📄 Abstract</summary>
  The EU Cyber Resilience Act (CRA), Regulation (EU) 2024/2847, makes product cybersecurity a lifecycle obligation for products with digital elements on the EU market: risk assessment, vulnerability handling, conformity documentation, and Article 14 incident- and vulnerability-reporting readiness must be operational before market placement. Small and medium-sized enterprises that build security products are doubly exposed, since their products are in scope while their customers expect them to be e...
  </details>

- **2026-10-06** — Muhammad Asim Javaid, Muhammad Adeel Pasha, Muhammad Ali Siddiqi — [Efficient and Implementation-Hardened RBLWE on Commodity Cortex-M Microcontrollers](http://arxiv.org/abs/2610.07820v1)
  <details><summary>📄 Abstract</summary>
  Efficient post-quantum cryptography on resource-constrained Internet-of-Things (IoT) devices requires implementations that exploit the target processor architecture while resisting practical implementation attacks. This paper presents an ISA-accelerated and implementation-hardened realization of Ring Binary Learning with Errors (RBLWE) encryption on a commodity ARM Cortex-M33 microcontroller. Packing four 8-bit polynomial coefficients into the byte lanes of a 32-bit register and processing them ...
  </details>

- **2026-10-06** — Yunhui Liu, Xudong Jin, Kang Zhang et al. — [Towards One-for-All Foundation Model for Attributed Graph Clustering](http://arxiv.org/abs/2610.07778v1)
  <details><summary>📄 Abstract</summary>
  Attributed graph clustering aims to discover node groups by jointly exploiting node attributes and graph topology, yet its unsupervised nature makes model selection and adaptation inherently difficult. Existing methods typically train and tune a separate model for each input graph, leading to costly and fragile pipelines that often fail to transfer across graphs with different feature spaces, structural patterns, and attribute-structure correlations. In this paper, we study a one-for-all alterna...
  </details>

- **2026-10-06** — Bach Nguyen, Zhaonan Li, Mau Son Nguyen et al. — [How Well Do LLMs Reason with Noisy Evidence? An Active Visual Reasoning Benchmark](http://arxiv.org/abs/2610.07751v1)
  <details><summary>📄 Abstract</summary>
  Real-world reasoning rarely reduces to static question answering: agents must actively gather information from tools and sensors that are often noisy and unreliable. Yet most existing active reasoning benchmarks assume that environmental feedback is trustworthy, or introduce noise without exposing an explicit, calibrated uncertainty signal, leaving open how LLMs should reason when the evidence itself is uncertain. We introduce VisualNoiseQA, a novel benchmark for active reasoning under noisy vis...
  </details>

- **2026-10-06** — Chuanfei Zang, Yumiao Wang, Xingyu Chen et al. — [Radar Intelligent Detection with Coarse-Grained Labels](http://arxiv.org/abs/2610.07670v1)
  <details><summary>📄 Abstract</summary>
  Many deep learning based radar target detectors rely on range-cell level labels for training, which are expensive to obtain. To reduce the labeling burden, this paper presents a training strategy that uses only range-window level labels. Specifically, two sub-echoes are randomly cropped from the same window echo, resulting in a known relative shift between them. A siamese Transformer is then used to identify target-salient responses from one sub-echo and form pseudo labels, which are mapped to t...
  </details>

- **2026-10-06** — Zhengyang Zhu, Liming Huang, Runmin Ji et al. — [HarnessSecurity-Bench: Do Security Mechanisms Really Protect Coding Agent Harnesses?](http://arxiv.org/abs/2610.07639v1)
  <details><summary>📄 Abstract</summary>
  Coding agent harnesses mediate tool use and authorize actions, yet their security mechanisms and runtime effects remain incompletely characterized. We present HarnessSecurity, the first systematic empirical study and benchmark of open- and closed-source coding agent harnesses. First, we derive a ten-mechanism taxonomy and then assess 400 harness-mechanism cells using independent ratings by researchers and large language model (LLM) judges. We find that about half of confirmed mechanism implement...
  </details>

- **2026-10-06** — Hang He, Li Wang, Hao Chen et al. — [CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?](http://arxiv.org/abs/2610.07557v1)
  <details><summary>📄 Abstract</summary>
  Static-analysis checker synthesis requires agents to interpret a defect specification, inspect a repository, implement analyzer-specific logic, and refine the checker through repeated compilation and analysis feedback. Existing coding-agent benchmarks focus on tasks such as patch generation or vulnerability detection and rarely assess whether an agent can develop a working checker in a repository from start to finish. We introduce CheckerBench, an executable benchmark of 300 tasks derived from 2...
  </details>

- **2026-10-06** — Hongyu Cao, Yanchi Liu, Kunpeng Liu et al. — [Which and When to Admit: Gradient Admission for Data-Centric Small Language Model Finetuning](http://arxiv.org/abs/2610.07553v1)
  <details><summary>📄 Abstract</summary>
  LoRA fine-tuning adapts small language models (SLMs) to heterogeneous instruction data within a low-rank update subspace, making it vulnerable to three structural problems: conflicting gradients that cancel, static data selection that cannot track evolving learning dynamics, and subspace saturation that causes later updates to overwrite useful directions. We argue that effective adaptation therefore requires controlling which data-induced gradients enter the LoRA subspace and when. We propose GR...
  </details>

- **2026-10-05** — Logan Andrew North, Priya Sanjay Kaluskar, Shasi Kumar Ramachandran Prabhu et al. — [Adversarial RL for Port-Scan Evasion: Attacker Feature Visibility in Edge-Deployed IDS](http://arxiv.org/abs/2610.08864v1)
  <details><summary>📄 Abstract</summary>
  Machine learning-based intrusion detection systems (IDS) are increasingly used in resource-constrained Internet of Things (IoT) environments, yet their robustness is often evaluated against static attacks rather than adversaries that adapt to detection feedback. This paper investigates adaptive port-scan evasion against ML-based IDS models deployed on a Raspberry Pi 3B+. We implement a live Zeek-based IDS pipeline with XGBoost, a multi-layer perceptron, and a 1D convolutional neural network trai...
  </details>

- **2026-10-05** — Shashwat Khandelwal, Shanker Shreejith — [Deep Defence on Wheels: A Dual Intrusion Detection System Architecture for Comprehensive In-Vehicle Network Security](http://arxiv.org/abs/2610.07489v1)
  <details><summary>📄 Abstract</summary>
  Increasing connectivity to the outside world and the lack of inbuilt security mechanisms have made legacy intra-vehicular networks vulnerable to cyberattacks. Initial research focused on maximising detection accuracy for known and unknown attacks, often using large, full-precision machine learning models. However, embedding IDSs into vehicular electronic systems also requires low detection latency, energy efficiency and minimal electronic control unit (ECU) resource overhead to process about 2,0...
  </details>


### 📂 defense
*防御与防护方法 / Defense & Protection Methods* — 54 papers

- **2026-10-07** — Maverick Morales, Tomáš Dominik, Vermut Gao et al. — [Reasoning-Token Spikes Under Prompted Untruthful Responding in Large Language Models](http://arxiv.org/abs/2610.10405v1)
  <details><summary>📄 Abstract</summary>
  Monitoring the chain-of-thought of reasoning artificial intelligence (AI) models remains a key approach to detecting deception and other forms of misbehavior in such models. However, semantic chain-of-thought monitoring depends on reasoning traces being legible and sufficiently faithful to the underlying computations that produced the model's behavior, not to mention accessible. Moreover, there is increasing evidence that chain-of-thought outputs may soon become illegible or unfaithful, if they ...
  </details>

- **2026-10-07** — Sayan Biswas, Jade Garcia Bourrée, Anne-Marie Kermarrec et al. — [Robust Decentralized Fairness Auditing](http://arxiv.org/abs/2610.10199v1)
  <details><summary>📄 Abstract</summary>
  Emerging legislation requires large language models (LLMs) to be audited for compliance with regulatory standards, particularly fairness. Such black-box audits typically assume a single auditor with access to a large, representative set of queries. In practice, it can be difficult for an auditor to obtain such a query set, but multiple auditors can together cover the relevant demographic groups by auditing the LLM collaboratively with their individual query sets. However, relying on multiple aud...
  </details>

- **2026-10-07** — Nikolaos Kekatos, Stylianos Basagiannis, Marinelio Chintri et al. — [Formal Runtime Verification for Tool-Using LLM Agents: An Offline Same-Benchmark Study on AgentDojo and STAC](http://arxiv.org/abs/2610.09793v1)
  <details><summary>📄 Abstract</summary>
  Guardrails for tool-using LLM agents are usually application-specific rules, which makes multi-step, data-dependent safety policies hard to specify, audit and reuse. As a declarative alternative, we evaluate metric first-order temporal logic (MFOTL), replaying the recorded trajectories that AgentDojo, STAC and R-Judge already ship through the unmodified MonPoly monitor, offline and without running an agent. On these corpora, five generic obligations flag 71.8% of STAC attack chains and 70.1% of ...
  </details>

- **2026-10-07** — Honglei Guo, Hanfang Zhang, Guochuan Zhang et al. — [Hierarchical Defense in Leader-Defender-Attacker Games: Nested Equilibria and Receding-Horizon Control](http://arxiv.org/abs/2610.09428v1)
  <details><summary>📄 Abstract</summary>
  We formulate a discrete-time leader-defender-attacker game that combines hierarchical interaction within a protective group with competition against an external attacker. The leader seeks to reach a prescribed demand point while avoiding capture, whereas the defender seeks to intercept the attacker while remaining near the leader. To capture their distinct objectives and asymmetric interactions, we introduce a nested equilibrium concept combining a leader-defender Stackelberg relationship with a...
  </details>

- **2026-10-07** — Fernando Martinez, Abhishek Satyam, Tao Li et al. — [Ask the Expert: LLM-Guided Reinforcement Learning for Autonomous Cyber Defense](http://arxiv.org/abs/2610.09337v1)
  <details><summary>📄 Abstract</summary>
  Policy-based reinforcement learning (RL) approaches have produced promising results for autonomous cyber defense; however, they are sample-inefficient in settings where defenders must respond under delayed, partial observations with actions from large action spaces. While large language models (LLMs) may reason semantically about security state space, high latency and trust assumptions prevent attractive in-line deployment models. We introduce Ask the Expert, a training-time guidance framework w...
  </details>

- **2026-10-07** — Fanqing Meng, Lingxiao Du, Haocheng Lu et al. — [RSIGym: A Flexible Environment for Recursive Self-Improvement](http://arxiv.org/abs/2610.10310v1)
  <details><summary>📄 Abstract</summary>
  Recursive self-improvement requires carrying accepted changes into later improvement cycles, while studying agent-proposed changes also requires substantial research infrastructure. Existing settings often leave agents to rebuild routine infrastructure or restrict exploration to individual components. We introduce RSIGym, an agent-native research environment based on Everything as a Service (EaaS). RSIGym exposes training, inference, rollout, evaluation, and sandbox execution through reusable se...
  </details>

- **2026-10-07** — Arnold Brosch, Abdelrahman Eldesokey, Michael Felsberg et al. — [A Probabilistic Perspective on Wasserstein-Based Evidential Uncertainty for Out-of-Distribution Segmentation](http://arxiv.org/abs/2610.10116v1)
  <details><summary>📄 Abstract</summary>
  Semantic segmentation networks operate on a fixed set of classes and therefore fail when out-of-distribution (OOD) objects appear during deployment, a critical limitation for safety-critical applications such as autonomous driving. Reliably identifying OOD objects requires well-calibrated epistemic uncertainty, yet common softmax-based confidence scores remain overconfident, while Bayesian alternatives such as Monte Carlo dropout or deep ensembles require costly repeated forward passes. Evidenti...
  </details>

- **2026-10-07** — Zijian Chen, Zhengyu Chen, Bohan Liang et al. — [From Pixel to Coding: Evaluating the Figure Reproduction Capabilities of MLLMs](http://arxiv.org/abs/2610.10066v1)
  <details><summary>📄 Abstract</summary>
  Multimodal Large Language Models (MLLMs) have demonstrated impressive capabilities in both visual understanding and code generation. However, existing benchmarks typically evaluate these two modalities in isolation, lacking a dedicated assessment of their unification, i.e., how a model can perceive complex visual structures and synthesize them into precise, executable code. Moreover, current visual code generation benchmarks often rely on simplified layouts within single programming environments...
  </details>

- **2026-10-07** — Malte Hansen, Karim Issa, Wilhelm Hasselbring — [A Chat Assistant for Software Exploration in a 3D Software Visualization](http://arxiv.org/abs/2610.09901v1)
  <details><summary>📄 Abstract</summary>
  We present a chat assistant for interactive software exploration, embedded in the 3D software visualization tool ExplorViz. The assistant builds upon current Large Language Models (LLMs) and enables users to ask questions about the currently visualized software system and trigger actions that change the visualization through natural language. We integrate the chat assistant in our ExplorViz frontend using the CopilotKit libraries such that probabilistic LLMs are combined with deterministic and t...
  </details>

- **2026-10-07** — Jonghyun Han, Younghoon Song, Jongyoul Park — [A Deafening Silence: Catastrophic Forgetting Lives in the Output Embeddings of Tokens the Data Never Speaks](http://arxiv.org/abs/2610.09835v1)
  <details><summary>📄 Abstract</summary>
  Continual pre-training and fine-tuning in Large Language Models (LLMs) inevitably induce catastrophic forgetting, typically mitigated by replay using often-inaccessible original data. In this data-free regime, we analyze where forgetting occurs and why. Systematic parameter freezing across five settings up to 1.4B reveals that forgetting concentrates selectively in the output embeddings of tokens rarely seen in the new corpus, whereas the same sqrt(v-hat) band of the body is inert and new learni...
  </details>

- **2026-10-07** — Arnold Olympio, Juan Manuel Servera Bondroit, Wael Abdelmalek et al. — [Reproducible LLM Inference Benchmarking: A Sequential Isolation Protocol for Regression Testing](http://arxiv.org/abs/2610.09778v1)
  <details><summary>📄 Abstract</summary>
  Reproducible benchmarking of Large Language Model (LLM) inference is challenging because repeated measurements can vary with execution and system state. We present the Sequential Isolation Methodology, a controlled benchmarking and regression-testing protocol designed to reduce between-run measurement variance while deliberately varying workload concurrency. We evaluate three representative open-source LLMs on an NVIDIA A100 80GB GPU using vLLM 0.9.1 across six context sizes and eight concurrenc...
  </details>

- **2026-10-07** — Kautuk Astu, Naina Rabha, Yogesh Simmhan — [AeroEval: Staged Program and Execution Validation for AI-Generated Drone Missions](http://arxiv.org/abs/2610.09764v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) can generate drone programs from natural-language mission descriptions, but syntactically valid programs may still violate user intent, environmental constraints, and mission-level behavior. This problem is pronounced in cyber-physical applications, where correctness depends on the interaction among generated code, mobile sensing, environmental geometry, event-driven analytics, and physical execution. Existing drone code-generation systems primarily use prompt guardr...
  </details>

- **2026-10-07** — Samuel Margolis, Paul Schmiedmayer, Alan Huang et al. — [DrugTargetWorld: A Synthetic Biobank for Training and Benchmarking AI Scientists](http://arxiv.org/abs/2610.09558v1)
  <details><summary>📄 Abstract</summary>
  Drug target discovery requires distinguishing molecules that causally drive disease from those that are merely associated with it. Training and evaluating AI agents to perform this workflow end-to-end is difficult because real world biobanks lack known causal ground truth and participant-level data is access controlled. We introduce DrugTargetWorld, a framework that procedurally generates simulated biobanks, or "worlds," with known but concealed causal structure. Each world contains genotypes, p...
  </details>

- **2026-10-07** — Yupeng Zhang, Ziyi Zhao, Juntao Cheng et al. — [RT-DETR-World: Transferring Rich LLM Semantics to Real-Time Open-Vocabulary Detection](http://arxiv.org/abs/2610.09502v1)
  <details><summary>📄 Abstract</summary>
  Open-vocabulary detection (OVD) recognizes categories unseen during training through textual category queries, yet achieving strong generalization with real-time efficiency remains challenging. Beyond vocabulary scaling, zero-shot generalization may benefit from reusable visual--semantic cues learned from seen data, including attributes, actions, states, and contextual relations. Existing real-time OVD methods primarily emphasize vocabulary coverage and efficient region/query--text matching; und...
  </details>

- **2026-10-07** — Oliver Bimber, Rakesh John Amala Arokia Nathan, Mohamed Youssef et al. — [trACT: temporal revelation Airborne Camera Trap](http://arxiv.org/abs/2610.09417v1)
  <details><summary>📄 Abstract</summary>
  Effective remote monitoring and surveillance using drones are frequently impeded by severe environmental and thermal clutter, dynamic vegetation, target camouflage, and system latency. Drawing inspiration from the hunting strategies of birds of prey that hover and stabilize their vision to isolate subtle ground motion, we introduce trACT (temporal revelation Airborne Camera Trap), a lightweight, real-time aerial robotics framework designed for autonomous consumer drones. The system integrates Te...
  </details>

- **2026-10-07** — Raghu Arghal, Saswati Sarkar, Shirin Saeedi Bidokhti — [The Confidence Game: Strategic Miscalibration in Human-AI Delegation](http://arxiv.org/abs/2610.09371v1)
  <details><summary>📄 Abstract</summary>
  Calibrated uncertainty quantification is essential to ensuring AI agents are trustworthy and reliable. However, when agents seek to maximize user engagement or revenue, confidence reports may be strategically distorted, detracting from their informativeness. We formalize this problem in the Confidence Game: a repeated signaling game with imperfect monitoring in which an agent of unknown honesty and ability reports its confidence, and a user decides whether to delegate the task or complete it her...
  </details>

- **2026-10-07** — Yash Dave, Sang T. Truong, Serena Wang et al. — [The AI Evaluation Ecosystem](http://arxiv.org/abs/2610.09296v1)
  <details><summary>📄 Abstract</summary>
  AI evaluation shapes the decisions of model providers, users, funders, and regulators. We argue that designing valid benchmarks requires contextualizing design choices in the dynamics of this ecosystem of actors. We develop a simulation architecture that combines rule-based market dynamics with LLM-driven strategic actors, building on advances in Generative Agent-Based Modeling (GABM). We model benchmarks, consumer needs, and provider capabilities as vectors over a six-dimensional capability spa...
  </details>

- **2026-10-07** — Kefan Liu, Fengning Ou, Yelin Luo et al. — [We Query, Therefore We Compute: On Oracle Computation beyond the Machine, with an Application to Agents](http://arxiv.org/abs/2610.09243v1)
  <details><summary>📄 Abstract</summary>
  Agentic systems use large language models (LLMs) to carry out concrete tasks. Prior work often borrows abstractions such as scheduling, caching or isolation piecemeal from operating systems, so the mechanisms it builds share little common ground, and the shared view of the two forms of agentic system, Workflows and Agents, is limited. We construct an abstract machine that provides both.   We treat the LLM as an Oracle and extend a two-stack pushdown automaton with one instruction, which hands th...
  </details>

- **2026-10-07** — Zhaohui Geoffrey Wang — [When Rank Rises as LLMs Degrade](http://arxiv.org/abs/2610.09647v1)
  <details><summary>📄 Abstract</summary>
  Post-training adapts language models in non-stationary environments. Practitioners monitor representation health with RankMe and related spectral statistics, often assuming that rank falls when representations degrade. We show that this assumption is unsafe for LLM post-training. In a controlled study of Qwen3-0.6B with four degradation modes and three seeds, data duplication worsens held-out loss by 75% relative to healthy while increasing both original and centred RankMe; the latter changes by...
  </details>

- **2026-10-07** — Neil K. R. Sehgal, Manuel Tonneau, Dunigan Folk et al. — [AI-Assisted Submissions in Online Research Are Rare and Highly Concentrated but Routinely Approved](http://arxiv.org/abs/2610.09279v1)
  <details><summary>📄 Abstract</summary>
  Online research platforms underpin much of what science claims about people, on the assumption that a human produced each response. Generative AI threatens that assumption by letting participants delegate responses to a chatbot, yet how often they do so remains unclear because prior estimates rely on self-report or automated detection rather than direct observation. We surveyed 2,500 workers on a high quality online research platform and directly observed AI assistance by linking donated ChatGPT...
  </details>

- **2026-10-07** — Benoît Roussel, Damien Bouet, Liming Chen et al. — [MOTIP2: Spatial Priors for End-to-End Multi-Object Tracking](http://arxiv.org/abs/2610.10391v1)
  <details><summary>📄 Abstract</summary>
  End-to-end multi-object trackers have narrowed the gap with classical tracking-by-detection on association-difficult benchmarks. Yet they still make spatially implausible errors no classical tracker would, such as assigning one identity to objects on opposite sides of the frame. A model could learn to avoid them, but tracking annotations are scarce, so we encode spatial priors explicitly instead, while keeping inference fully end-to-end with no post-hoc association.   We propose three spatial pr...
  </details>

- **2026-10-07** — Jiapan Wang, Daan Hulskemper, Mathilde Letard et al. — [DeepTopoClustering: Unsupervised Derivation of Surface Process Taxonomy from 4D Point Clouds for Topographic Monitoring](http://arxiv.org/abs/2610.09860v1)
  <details><summary>📄 Abstract</summary>
  4D point clouds acquired by permanent laser scanning (PLS) enable accurate high-frequency monitoring of surface change in dynamic topographic environments. However, existing methods remain limited in organizing detected surface activities into meaningful process types. We propose DeepTopoClustering (DTC), an unsupervised framework for deriving a hierarchical process taxonomy from object-based surface activities, so-called 4D objects-by-change (4D-OBCs). We transform each 4D-OBC into a GeoMorphog...
  </details>

- **2026-10-07** — Matthieu Meignin, Cécile Mallet, Nicolas Viltard — [Generative and deterministic deep learning models comparison for fine-scale precipitation retrievals from infrared brightness temperature](http://arxiv.org/abs/2610.09859v1)
  <details><summary>📄 Abstract</summary>
  Accurate precipitation estimation at fine spatial scales is critical for hydrology, agriculture, and climate studies. Infrared brightness temperatures from geostationary satellites offer excellent temporal coverage over continental-scale domains. However, because these measurements primarily characterize cloud-top properties rather than precipitation processes near the surface, their correlation with rainfall intensity remains limited, making quantitative precipitation estimation challenging. In...
  </details>

- **2026-10-07** — Justus Flerlage, Thorsten Wittkopp, Alexander Acker et al. — [Adaptive Code Generation for Controlling Robots](http://arxiv.org/abs/2610.09588v1)
  <details><summary>📄 Abstract</summary>
  Deploying robots as Complex Adaptive Systems (CAS) in unknown and dynamic environments necessitates a transition from rigid command libraries toward intention-based autonomy, as natural language represents the only medium capable of articulating complex goals beyond the capacity of finite instruction sets. While Large Language Models (LLMs) offer a path toward natural language goal description, their integration introduces significant challenges: the formalization gap between imprecise intention...
  </details>

- **2026-10-07** — Toluwani Aremu, Samuele Poppi, Nils Lukas — [Constitution-Guided Watermarking](http://arxiv.org/abs/2610.09552v1)
  <details><summary>📄 Abstract</summary>
  Watermarking enables language model providers to identify text generated by their models. However, its desired properties can conflict (\ie~stronger watermark signals can degrade text quality), while designs that resist editing may also facilitate forgery. Providers address these trade-offs by choosing configurations that balance competing objectives or prioritize particular properties. Either approach imposes a shared operating point on requests with different requirements, potentially sacrific...
  </details>

- **2026-10-07** — Qiuqi Wang, Ruodu Wang, Zhenyuan Zhang — [Sequential resetting procedures and false discovery rate](http://arxiv.org/abs/2610.09339v1)
  <details><summary>📄 Abstract</summary>
  Data arrive sequentially, each associated with a null hypothesis. We develop testing procedures to locate intervals in which some null hypotheses fail with false discovery rate (FDR) control. The new procedures are called sequential resetting procedures, and they are based on e-values and test supermartingales. We also develop a refined version of the procedures by dropping less informative data points before the block minimum of the test supermartingale in each rejection block. These procedures...
  </details>

- **2026-10-07** — Mayank Sengupta, Nirmit Desai, Eric Song et al. — [LeCuration: A Tiny World Model as a Data Curation Multi-Tool](http://arxiv.org/abs/2610.09285v1)
  <details><summary>📄 Abstract</summary>
  Many applications of physical AI run within finite or closed physical worlds with a limited set of physical laws governing object behavior. Examples include robots working in a warehouse and agents moving around in a video game. In order to better organize, filter, and curate data for physical AI applications, we propose a new approach centered on the unique settings and physical laws of individual datasets. We train LeCuration, a small world model intended to serve as a data curation tool for a...
  </details>

- **2026-10-06** — Param Biyani, Krishnamurthy Dvijotham — [SpecGuard: Proving a Task Is Broken Before the Agent Cheats](http://arxiv.org/abs/2610.09159v1)
  <details><summary>📄 Abstract</summary>
  As autonomous coding agents get increasingly deployed, the risk that accidental or adversarially injected misspecifications in tasks lead to dangerous agent behavior is critical to address. Prior work has shown that agents given such tasks rarely flag the conflict and instead cheat, editing tests or hard-coding expected outputs, and the actions taken to cheat can cause real damage, such as deleting a security defense to make a corrupted test pass. It remains unclear whether such conflicts can be...
  </details>

- **2026-10-06** — Vahid Tavakkoli, Kabeh Mohsenzadegan, Kyandoghere Kyamakya — [SwarmReconGuard: Black-Box Detection of Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations](http://arxiv.org/abs/2610.09138v1)
  <details><summary>📄 Abstract</summary>
  Autonomous and agentic clients can distribute reconnaissance across many identities so that each request remains valid, low-rate, and benign-looking while the population collectively acquires broad system knowledge. We formalize this threat as Distributed Collective Reconnaissance (DCR) and present SwarmReconGuard, a reproducible black-box benchmark in which the defender observes only service-boundary telemetry. The Docker-isolated study evaluates 11 benign and attack behaviors across 10-10,000 ...
  </details>

- **2026-10-06** — Mohamed Kamel, Sahar Selim, Walaa Medhat et al. — [BeatFlow-ECG: Rectified Flow for ECG Reconstruction from Indirect Wearable Signals](http://arxiv.org/abs/2610.09052v1)
  <details><summary>📄 Abstract</summary>
  Continuous cardiac monitoring outside clinical settings requires signals that are both informative and practical to collect during daily life. Electrocardiography (ECG) provides rich information about cardiac rhythm and waveform morphology, while wearable photoplethysmography (PPG) is easier to acquire continuously but is only an indirect cardiovascular measurement and is highly sensitive to motion. We present BeatFlow-ECG, a conditional rectified-flow model for reconstructing single-channel ECG...
  </details>

- **2026-10-06** — Nikolaos Kekatos, Dimitrios Nikou, Anastasios Temperekidis et al. — [Multi-Aspect Runtime Verification for Simulation-Based V&V of LLM-Enabled Autonomous Agents](http://arxiv.org/abs/2610.08928v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents are entering decision-support roles in defence staff work, where the obligations they must respect are already written down and binding, and where retraining is not available as a control because models arrive as procured components. What can be placed under engineering control is the interface between the agent and the systems it acts on. Those obligations are at once spatial, temporal and text-semantic, and a violation typically lives in the composition of a multi-step interac...
  </details>

- **2026-10-06** — Kemal Davaslioglu, Sastry Kompella — [Sigma-Hunter: A Domain-Specific Language Model for Threat Hunting and Detection Engineering](http://arxiv.org/abs/2610.09007v1)
  <details><summary>📄 Abstract</summary>
  Detection engineers must translate threat reports, forensic observations, and hunt hypotheses into precise, testable rules. General-purpose large language models (LLMs) can draft such rules, but often produce invalid YAML, incorrect log sources, unsupported fields, or overly broad detection logic. This paper presents \emph{Sigma-Hunter}, a domain-adapted LLM for analyst-assistive Sigma rule generation and threat hunting. We build an instruction-tuning dataset from 3,635 validated open-source Sig...
  </details>

- **2026-10-06** — Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal — [Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage](http://arxiv.org/abs/2610.08933v1)
  <details><summary>📄 Abstract</summary>
  Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independent anomaly triage. Agentic AI is treated as a stateful coordinator over bounded, inspectable services rather than as a fully autonomous vehic...
  </details>

- **2026-10-06** — Melissa Kazemi Rad, Sihui Dai, Isha Slavin et al. — [AdaGuard: Enhancing Safety and Policy Compliance with Reasoning-Enabled LLM-As-A-Judge Guardrails](http://arxiv.org/abs/2610.08923v1)
  <details><summary>📄 Abstract</summary>
  Enterprise generative AI applications require robust safety mechanisms that can accommodate diverse risk postures, evolving policies, and varying latency constraints. Current guardrail solutions often suffer from rigidity, relying on fixed policy sets and offering limited transparency or reasoning flexibility. We present Adaguard, an adaptive LLM-as-a-Judge framework designed to address these challenges through dynamic policy enforcement and adaptive reasoning-budget allocation. Built using supe...
  </details>

- **2026-10-06** — Ryan C. Barron — [Trustworthy Domain-Specific AI for Structured Knowledge Retrieval and Reasoning](http://arxiv.org/abs/2610.08894v1)
  <details><summary>📄 Abstract</summary>
  This dissertation presents a scalable architecture for transforming unstructured, domain-specific text into structured knowledge for retrieval and reasoning. It integrates semi-automatic corpus curation, semantic structuring, retrieval, and inference into an interpretable pipeline.   The research introduces Binary Bleed, an adapted binary search method that reduces low-rank search complexity for Non-negative Matrix Factorization (NMF), and Hierarchical NMF with automatic latent feature selection...
  </details>

- **2026-10-06** — Zuoxu Wang, Xiao Liang — [GUARD: Geometric Uncertainty-Aware Point Cloud Denoising and Segmentation for Robotic Hard Disk Drive Disassembly](http://arxiv.org/abs/2610.09068v1)
  <details><summary>📄 Abstract</summary>
  Reliable robotic disassembly requires part-level representations that distinguish genuine component geometry from scanning and reconstruction artifacts. In point clouds of hard disk drives (HDDs), structured ghost artifacts can resemble valid components locally while remaining inconsistent with the overall geometry, allowing erroneous measurements to receive plausible semantic labels. This creates an engineering information problem: semantic prediction confidence alone does not establish whether...
  </details>

- **2026-10-06** — Suxin Ji, Hungtao Wan, Shaoxuan Chen et al. — [Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-Resistant Provenance for LLM Agents](http://arxiv.org/abs/2610.08668v1)
  <details><summary>📄 Abstract</summary>
  Behavioral watermarking embeds an owner identifier in an LLM agent's high-level action choices, giving provenance without touching output tokens. Prior agent watermarks break in two ways. First, all three prior schemes bind the watermark to the exact action symbol, so renaming a tool desynchronizes decoding even when the observation is untouched; in AgentMark's own robustness test, paraphrasing the observation alone drops bit-recovery to 16.8%. Second, every prior agent watermark studies only re...
  </details>

- **2026-10-06** — Yutong Liu, Chenyi Wang, Ming F. Li et al. — [Don't Let One Lie Survive A Hundred Truths: A Selective Bayesian Trust Estimator for Collaborative Perception](http://arxiv.org/abs/2610.07875v1)
  <details><summary>📄 Abstract</summary>
  Collaborative perception (CP) enables connected vehicles to see beyond their own sensors but makes them dependent on messages they cannot independently verify. A compromised collaborator can surgically conceal a single safety-critical object or inject a non-existing one while correctly reporting many others. Existing Bayesian trust mechanisms pool agreement across objects, which, while effective against blatant untargeted attacks, either incurs high false-positive rates (FPR), or allows unrelate...
  </details>

- **2026-10-06** — Xianwen Deng, Ruijie Zhao, Mingwei Zhan et al. — [SCSM: A Traffic-Native Foundation Model for Transferable Website Fingerprinting](http://arxiv.org/abs/2610.07776v1)
  <details><summary>📄 Abstract</summary>
  Website fingerprinting infers the websites visited by users from encrypted traffic metadata. However, models trained under fixed collection conditions often degrade as website sets, collection times, network paths, browsers, or defenses change. Existing transferable attacks either rely on handcrafted perturbations of individual traces or adapt language-oriented architectures to traffic, limiting their ability to capture traffic-native semantics. To address these limitations, we propose SCSM, a t...
  </details>

- **2026-10-06** — Thanh Dong, An Ngo, Minh Dau et al. — [Detecting LLM-Assisted Vietnamese Writing via Keystrokes under Behavioral Manipulation](http://arxiv.org/abs/2610.07700v1)
  <details><summary>📄 Abstract</summary>
  We study the robustness of keystroke dynamics for detecting large language model (LLM)-assisted writing. We introduce a Vietnamese keystroke dataset capturing realistic writing modes, including bona fide composition, transcription, and paraphrasing. We also define a behaviorally grounded threat model in which users deliberately alter typing patterns. To implement the threat model, we create behaviorally manipulated variants of the data designed to evade keystroke-based detection. We evaluate fou...
  </details>

- **2026-10-06** — Shaswata Mitra, Raj Patel, Subash Neupane et al. — [Where Rules End and Judges Begin: Measuring the Judgment Boundary in Multi-Agent Systems Security](http://arxiv.org/abs/2610.07657v1)
  <details><summary>📄 Abstract</summary>
  LLM-based multi-agent systems (MAS) engage tools, share memory, and delegate tasks, often encountering adversarial content. Current defenses for MAS are typically evaluated in isolation, focusing on one attack type at a time, which can lead to costly and hard-to-audit outcomes. This study organizes defenses into five principles, implementing them as DEFER1 (DEterministic-First Enforcement with Residual judgment), which includes a cascade of 28 checks that blocks what it can and refers the rest t...
  </details>

- **2026-10-06** — Lei Yang, Boqi Li, Chunmian Lin et al. — [Sparse2comm: Towards Robust Cooperative 3D Object Detection](http://arxiv.org/abs/2610.08573v1)
  <details><summary>📄 Abstract</summary>
  Cooperative perception improves autonomous driving by sharing complementary observations among vehicles and roadside infrastructure for 3D object detection. However, practical deployment is constrained by limited bandwidth and unreliable cooperation, where packet loss, transmission delay, and spatial misalignment jointly degrade the cooperative feature stream. Existing methods often reduce communication cost or compensate for one degradation type, leaving coupled disturbances insufficiently addr...
  </details>

- **2026-10-06** — Maoqi Liu, Quan Fang, Yufei He — [CoDe-LoRA: Mitigating the Orthogonality Dilemma in Continual Learning of LLMs via Knowledge Consolidation and Decoupling](http://arxiv.org/abs/2610.08312v1)
  <details><summary>📄 Abstract</summary>
  Continual learning (CL) is essential for Large Language Models (LLMs) to sequentially adapt to evolving tasks. To mitigate catastrophic forgetting, recent advances implement low-rank adaptation with orthogonal projections (e.g., O-LoRA) to isolate task parameters. However, we reveal that such strict geometric constraints trigger an "Orthogonality Dilemma": rigid parameter isolation impedes the transfer and accumulation of shared representations across semantically related tasks. In this work, we...
  </details>

- **2026-10-06** — Yunju Kang, Seonghyeon Cho, Irene Li et al. — [POLAR: Ontology-Guided Risk Prevention for Tool-Calling LLM Agents](http://arxiv.org/abs/2610.08082v1)
  <details><summary>📄 Abstract</summary>
  LLM tool-use agents operate in dynamic environments where many actions carry operational risk. However, most safety mechanisms react only after errors manifest. Existing pre-emptive approaches either fine-tune the agent on chain-of-thought deliberation or compile natural-language guardrails into runtime checks, but they do so without exposing a structural, auditable verdict. We propose POLAR, a guardrail framework for small tool-calling agents that assesses reversibility through a structured two...
  </details>

- **2026-10-06** — Zizhuo Zhang, Xiong Peng, Jingwei Sun et al. — [Rethinking Faithfulness in LLMs: A Pairwise Context-Sensitive Perspective](http://arxiv.org/abs/2610.07894v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are expected to answer questions faithfully based on the provided context, abstaining when the context information is insufficient to answer the questions. Existing faithfulness evaluations typically assess each question-context instance in isolation; however, such instance-level evaluation fails to capture a fundamental requirement of faithful behavior: the ability to adapt model responses to changes in available contexts. In particular, a model should provide corre...
  </details>

- **2026-10-06** — Jonathan Chang, Zimeng Lyu — [Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction](http://arxiv.org/abs/2610.07825v1)
  <details><summary>📄 Abstract</summary>
  Time series forecasting models are typically compared on pointwise error, which scores a prediction in isolation from the decision it is produced for, and a lower forecast error does not imply a better decision downstream. A parallel debate asks whether modern transformer architectures forecast better than recurrent and other lightweight models. We compare linear, fixed recurrent, transformer, and mixing based architectures against recurrent networks evolved by neuroevolutionary architecture sea...
  </details>

- **2026-10-06** — Robert A. Lewis, I-Min Chiu, Kyle Verrier et al. — [MS-ECG-FM: Towards a More Universal Electrocardiogram Foundation Model for Health Monitoring using Multi-source Contrastive Learning](http://arxiv.org/abs/2610.07662v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiography (ECG) records the electrical activity of the heart, aiding diagnosis by detecting abnormalities in cardiac function. ECG foundation models have demonstrated promising results, but are limited by a reliance on ECG interpretation reports as their sole supervision. Because interpretation reports only capture the subset of waveform information routinely recognized by clinicians, this constrains representation learning to overlook the broader diagnostic signals present in ECG. We ...
  </details>

- **2026-10-06** — Myeung Suk Oh, Zhiyao Zhang, Alvaro Velasquez et al. — [Foundation Model-Aided Multi-Agent Reinforcement Learning for Wireless Random Access Network Optimization](http://arxiv.org/abs/2610.07550v1)
  <details><summary>📄 Abstract</summary>
  Random access (RA) is one of the most foundational medium access control (MAC) layer scheduling schemes for handling unpredictable data traffic from multiple terminals. While multi-agent reinforcement learning (MARL) has been explored to optimize RA-based wireless networks, its reliance on experience-driven, distributed policy learning incurs significant training overhead for each optimization task, limiting its feasibility in real-world applications. In this work, we propose to leverage a found...
  </details>

- **2026-10-06** — Khac Duc Giang Nguyen, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag — [Catastrophic Forgetting in Sequential Thermal Anti-UAV Detection: The Role of Scale-Conditioned Gradient Imbalance](http://arxiv.org/abs/2610.08315v1)
  <details><summary>📄 Abstract</summary>
  Counter-UAV systems based on thermal infrared detection must stay accurate as operational datasets evolve, yet sequential fine-tuning causes catastrophic forgetting of prior tasks, a problem that remains insufficiently characterized in this domain. This continual-learning study measures the stability-plasticity trade-off in YOLOMG, a YOLOv5-based detector run as a single thermal-infrared stream with the motion channel disabled, trained sequentially across three anti-UAV benchmarks of rising scal...
  </details>

- **2026-10-06** — Rainer Lienhart, Daniel Kienzle, Shin'ichi Satoh et al. — [Event Detection in Table Tennis Videos using 2D Keypoints](http://arxiv.org/abs/2610.08286v1)
  <details><summary>📄 Abstract</summary>
  This paper addresses the challenge of automatic, frame-accurate event detection in table tennis videos. Current methods for estimating 3d ball trajectories and ball spin typically require that key events, such as ball-racket contacts, have already been identified in advance. This requirement makes it difficult to apply these methods to longer, unedited video recordings. To overcome this limitation, we propose EventNet, a two-stage pipeline to detect key events: (1) 2d keypoints are extracted of ...
  </details>

- **2026-10-06** — Cheng-Han Yeh, Kuan-chun Yu, Cheng-Chang Tsai et al. — [On the Intrinsic Limited Robustness of Latent-Based Watermarking](http://arxiv.org/abs/2610.08178v1)
  <details><summary>📄 Abstract</summary>
  Existing latent-based watermarking methods for diffusion models have overestimated their robustness to image distortions, including geometric transformations such as rotation, scaling, and translation (RST). Moreover, this paradigm of watermarking approaches may suffer from inherent limitations arising from the domain in which the watermark is embedded. In this paper, we provide the first theoretical analysis explaining why these methods lack invariance to perturbations. By relaxing the invarian...
  </details>

- **2026-10-06** — Zheng Gao, Xiaoyu Li, Zhicheng Bao et al. — [Rethinking Visual Provenance: Detection and Watermarking Across Direct Visual Generation and LLM-Driven Code Rendering](http://arxiv.org/abs/2610.08137v1)
  <details><summary>📄 Abstract</summary>
  AI systems create images and videos with image/video generation models or by writing code and graphics descriptions that are then rendered. These routes can produce similar visible artifacts but expose different representations, intervention points, and provenance evidence. We develop a production-centered framework that compares detection and watermarking across both routes. An explicit verification specification distinguishes passive inference, message recovery, and authenticated provenance. W...
  </details>

- **2026-10-06** — Kavienan Jegatheesan, Gayathri Lihinikaduarachchi — [When Tools Lie: Reliability of Mathematical Agents Under Corrupted Tool Feedback](http://arxiv.org/abs/2610.08097v1)
  <details><summary>📄 Abstract</summary>
  Mathematical problem solving often requires deterministic computational steps that agents delegate to tools and implicitly trust. Yet tools can fail silently, returning plausible but incorrect results. How well can agents detect and correct corrupted tool call outputs? We study this through a controlled corruption framework where a hidden interceptor replaces tool call results with plausible incorrect information on targeted problems. We evaluate agents across 31 problems under four verification...
  </details>

- **2026-10-06** — Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ibeth P. Alarcón et al. — [Towards benchmarking Western Bluebird detection in the wild](http://arxiv.org/abs/2610.07802v1)
  <details><summary>📄 Abstract</summary>
  Bird monitoring in natural environments is challenging due to the small size of some species of birds relative to the scene, background clutter, variability in illumination, and the observers' viewpoint. Progress is further limited by the scarcity of large-scale, realistic datasets, which are essential for understanding behavioral patterns. To address this gap, we introduce a new benchmark dataset for the detection and segmentation of Western bluebirds (Sialia Mexicana), comprising over 6,000 la...
  </details>


### 📂 alignment
*对齐与安全约束 / Alignment & Safety Constraints* — 52 papers

- **2026-10-07** — Zhewei Chen, Hao Zhu, Jiaojiao Jiang et al. — [Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs](http://arxiv.org/abs/2610.10520v1)
  <details><summary>📄 Abstract</summary>
  GNN-to-MLP distillation aims to retain the predictive accuracy of a message-passing teacher while deploying a graph-free MLP at inference. Existing methods mainly transfer node-wise predictions or use confidence-based reweighting, but they do not specify where the student should preserve the teacher's graph-induced geometry. We show that this omission leads to two spectral failure modes in the student's representation space. On sparse graphs, the student suffers from spectral underfit, missing h...
  </details>

- **2026-10-07** — Zihan Su, Junhao Zhuang, Yaowei Li et al. — [SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](http://arxiv.org/abs/2610.10429v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive video generation requires denoising the current frames while writing their key-value representations as context for future predictions. However, these two roles typically share parameters, and we find that their gradients exhibit distinct patterns and systematic negative alignment, hindering the joint optimization of visual quality and temporal consistency. We introduce Self Gradient Forcing Plus (SGF+), which assigns separate parameters to context writing and denoising while pres...
  </details>

- **2026-10-07** — Chengwei Shi, Yunnong Chen, Tingting Zhou et al. — [TaoD2C-Bench: Benchmarking MLLMs for Industrial UI Code Generation Beyond Visual Fidelity](http://arxiv.org/abs/2610.10374v1)
  <details><summary>📄 Abstract</summary>
  A key challenge for multimodal large language models (MLLMs) is moving beyond visual recognition to constraint-aware cross-modal reasoning. This involves combining visual cues with information from other modalities to understand elements' relationships under domain-specific rules. This challenge is acutely evident in industrial design-to-code (D2C), which converts user interface (UI) designs into code and requires MLLMs to connect design images with disorganized layer metadata, infer component a...
  </details>

- **2026-10-07** — Koffka Khan — [ORDERS: An Empirical Study of Norm-Rank Aggregation for Personalized Federated Learning](http://arxiv.org/abs/2610.10361v1)
  <details><summary>📄 Abstract</summary>
  Personalized federated learning combines shared representations with client-specific predictors, but the contribution of a server weighting rule can be obscured by local training and evaluation choices. We study ORDERS, a configuration that combines a shared backbone, a private residual adapter and classifier, geometric weights assigned by descending update norm, feature alignment, and private-parameter perturbations. The server computes a weighted sum of updates obtained from the same broadcast...
  </details>

- **2026-10-07** — Zekai Liu, Zhilin Wang, Xuzheng He et al. — [MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent](http://arxiv.org/abs/2610.10355v1)
  <details><summary>📄 Abstract</summary>
  Text-to-music systems produce increasingly convincing audio, yet evaluation reveals little about whether the result matches user intent. A global text-audio relevance score can overlook the implicit intent in underspecified prompts and mask failures in specific requirements, such as instrumentation, structure, rhythm, or mood progression. To bridge this gap, we formulate text-to-music intent alignment as satisfying a per-request rubric of independently verifiable items covering both a request's ...
  </details>

- **2026-10-07** — Himarsha R. Jayanetti, Sivakanesan Dhanushkanda, Shuai Hao et al. — [Nobody Truly Agrees on Sentiment: Humans, Bespoke Tools, and LLMs Struggle with Social Media Texts](http://arxiv.org/abs/2610.10318v1)
  <details><summary>📄 Abstract</summary>
  Social media is a rich source of real-time public sentiment, but widely used sentiment analysis tools are often applied without understanding their limitations. In this study, we evaluate the inter-rater reliability of three bespoke sentiment analysis tools (TextBlob, VADER, and Twitter-roBERTa-base) and three large language models (LLMs: Qwen3-32B, GPT-OSS-120B, Llama-4-Maverick-17B) against six human raters across 100 tweets. We measured agreement using two statistical measures: Cohen's kappa ...
  </details>

- **2026-10-07** — Hao Wang, Qiwei Zeng, Jinghao Lin et al. — [$Δ$Representation: Geometry Supervised Representation Learning of Phenotypes via Counterfactual Reasoning for Medical VLMs](http://arxiv.org/abs/2610.10286v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) have shown increasing potential for radiological image interpretation. Medical VLMs encode radiological images into visual representations that capture both anatomical and phenotypic information for diagnosis. Existing approaches improve pathological phenotype representations through semantic-guided representation alignment. However, pathological phenotypes arise as lesion-specific visual changes superimposed on underlying normal anatomy. Such semantic align...
  </details>

- **2026-10-07** — Leo Zeitler, Jack Richings, Victoria Nockles — [AI Safety Considerations for Agents With Limited Time to Act](http://arxiv.org/abs/2610.10285v1)
  <details><summary>📄 Abstract</summary>
  In the wake of the increasingly public discussion about AI alignment, recent work has tried to propose specific AI architectures that behave safely. However, the proposed arguments that seemingly demonstrate proved alignment mostly neglect the environment the agent needs to act in. We discuss theoretical bounds for agent-agnostic safety guarantees in environments that can only be partially observed and within which an action is required within limited time. We introduce two realistic scenarios, ...
  </details>

- **2026-10-07** — Hao Wang, Qiwei Zeng, Shuchang Ye et al. — [Geometry-Supervised Visual Representation Learning for Multi-Phenotype Lesion Interpretation in Medical VLMs](http://arxiv.org/abs/2610.10238v1)
  <details><summary>📄 Abstract</summary>
  Medical vision-language models (VLMs) have shown increasing potential for clinical image interpretation. However, these models still struggle to interpret multi-phenotype lesions whose diagnosis requires the joint assessment of multiple pathological phenotypes. Existing vision-language alignment methods produce visual representations that fail to preserve anatomical hierarchies and relationships among phenotypic subclasses. This stems from their reliance on semantic supervision, which lacks geom...
  </details>

- **2026-10-07** — Yifei Lu, Cheng Liu, Dianzhi Yu et al. — [UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy](http://arxiv.org/abs/2610.10164v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents can improve across tasks by retaining reusable skills distilled from prior interactions. Recent work jointly optimizes task execution and skill extraction, enabling the policy and skillbank to co-evolve. However, as the actor continues learning, rewarding skill proposals through their reuse in subsequent training steps may conflate skill benefits with actor improvement, while directly testing each proposed skill requires costly additional actor rollouts. In this paper...
  </details>

- **2026-10-07** — Haoru Li, Jinmei Liu, Zhiyong Wang et al. — [Many Ways to Succeed: Diversity-Driven RL Fine-Tuning for VLA Generalization](http://arxiv.org/abs/2610.09943v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) fine-tuning improves vision-language-action (VLA) policies through closed-loop experience, yet generalization beyond the fine-tuning distribution remains limited. Our analysis reveals a selective reshaping of exploration: RL contracts behavior globally, yet diversifies successful trajectories, elicits success with fewer rollouts, and covers more of the latent task-valid solution space than supervised fine-tuning. Broader successful-mode coverage may provide alternativ...
  </details>

- **2026-10-07** — Alexandra Coroiu, Andrea Vogt, Viktor Werbilo et al. — [A Scoping Review and Experimental Study on Reinforcement Learning from Human Feedback for Human-Robot Collaboration](http://arxiv.org/abs/2610.09891v1)
  <details><summary>📄 Abstract</summary>
  Human-Robot Collaboration (HRC) can facilitate mass customisation in Industry 4.0, with Reinforcement Learning from Human Feedback (RLHF) representing a promising approach for developing safe AI-based robots. Practical challenges remain regarding safety during AI development, human feedback quality, and bidirectional human-robot adaptation. We conducted a scoping review of RLHF in HRC systems, mapping methods that address these challenges. Following PRISMA guidelines, we screened 199 records and...
  </details>

- **2026-10-07** — Arshia Hemmat, Amirhossein Vahidi, Amitis Shidani et al. — [ORCA: Hunting Compositional Failures in Text-to-Image Diffusion](http://arxiv.org/abs/2610.09841v1)
  <details><summary>📄 Abstract</summary>
  Text-to-image diffusion models fail predictably on compositional prompts: attributes bind to the wrong objects, spatial relations invert, and multi-object scenes lose count. Recent architectures already augment CLIP with a T5 encoder precisely because CLIP's contrastive embedding loses compositional structure, yet these failures persist. We argue the binding problem is therefore not one of missing information but of misaligned information: a text encoder preserves compositional structure, but in...
  </details>

- **2026-10-07** — Huayi Lai, Jicheng Yang, Min Yi et al. — [MIRROR: From Imitation to Internalization in LLM Personalization](http://arxiv.org/abs/2610.09795v1)
  <details><summary>📄 Abstract</summary>
  The demand for personalized LLMs is shifting from style imitation toward content quality. We investigate whether self-distillation can bridge this gap in existing fine-tuning paradigm. To address this limitation, we introduce MIRROR(Meta- personalization by Internalizing Reference-Revealed On-policy Reflections), a novel self-distillation framework that shifts LLM personalization from imitation toward preference internalization. First, we replace reference-token imitation with reference-revealed...
  </details>

- **2026-10-07** — Yucheng Gong, Rui Zhou, Binbin Zeng et al. — [A Strength-Monotonic Law for Domain Alignment in Frozen-Embedding Bioacoustic Classification](http://arxiv.org/abs/2610.09737v1)
  <details><summary>📄 Abstract</summary>
  When does distribution alignment help a frozen foundation-model embedding generalize across acoustic domains? For cross-domain mosquito-species classification we report a strength-monotonic law: the stronger an encoder is on the target task, the more its unseen-domain generalization relies on a distribution-alignment (MMD) term, and the more it is harmed by domain-rebalanced sampling. Across four encoder families and a within-encoder HuBERT layer sweep (n=8), the rebalancing leg orders exactly w...
  </details>

- **2026-10-07** — Masatoshi Tateno, Takehiko Ohkawa, Yueh-Hua Wu et al. — [YUBI-STAG: Contact and Semantic-Rich Alignment for VLAs via Automated Video-Language Grounding](http://arxiv.org/abs/2610.09718v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models acquire broad manipulation capabilities via large-scale pretraining, yet eliciting them through language requires fine-grained alignment between instructions and physical interactions. Existing robot demonstrations typically provide only coarse task descriptions, omitting how actions are executed, including which gripper acts, which object is contacted, and how it is grasped and moved. We introduce YUBI-STAG, a framework for Spatio-Temporal Annotation and Grou...
  </details>

- **2026-10-07** — Zihao Zhang, Haochen Tian, Tianyu Li et al. — [Do Better Visual Representations Always Lead to Better End-to-End Autonomous Driving?](http://arxiv.org/abs/2610.09695v1)
  <details><summary>📄 Abstract</summary>
  Visual foundation models (VFMs) are increasingly integrated into end-to-end autonomous driving for their powerful representations, yet it remains unclear when these representations improve driving performance. To investigate this question, we introduce ViRA, a planner-agnostic visual representation alignment framework that keeps the planner architecture and inference cost unchanged. Our study reveals three findings: (1) VFM-guided visual representations consistently improve driving performance a...
  </details>

- **2026-10-07** — Igor Slinko, Yaroslav Golubev, Sergey Titov — [Coding-Agent Benchmarks Should Match Their Users' Task Flows](http://arxiv.org/abs/2610.09633v1)
  <details><summary>📄 Abstract</summary>
  The evaluation of coding agents generally strives to be as realistic as possible. In our study, we collect 4,782 agent sessions of real software engineers in JetBrains IDEs, which we call Production Sessions. Since our subject is interactive agents, we study the sessions with at least three user messages (33% of the sample). These long sessions differ from issue-derived benchmark tasks in two ways: (i) user requests span a far wider mix of task types - questions about the project's code, plannin...
  </details>

- **2026-10-07** — Vaibhava Lakshmi Ravideshik, Mayank Kejriwal — [Reliability of LLM Judges for Evaluating Entity Alignment](http://arxiv.org/abs/2610.09554v1)
  <details><summary>📄 Abstract</summary>
  Entity Alignment (EA) identifies equivalent entities across knowledge graphs and is critical for knowledge base integration and ontology merging. Evaluating EA systems at scale requires expensive expert annotation, making systematic assessment across diverse domains practically infeasible. LLM-as-judge evaluation offers a potentially scalable alternative, yet its reliability for structured prediction tasks like EA remains unstudied. We present the first systematic benchmarking study across three...
  </details>

- **2026-10-07** — Hanqiu Li Cai, Chema Garabito — [Iris-3B: Going Beyond the Latent with Pixel-Space Diffusion Training, Conversion and Fine-Tuning](http://arxiv.org/abs/2610.09450v1)
  <details><summary>📄 Abstract</summary>
  Pixel-space diffusion models avoid the lossy VAE of latent models, which suggests an advantage on downstream tasks where fine-grained detail matters. We test this claim along both routes to a pixel-space backbone. We pretrain Iris-3B, a 3B-parameter pixel-space text-to-image transformer, from scratch through a $256\to512\to1024$ curriculum, after first ablating the prediction target and representation alignment at $256^2$ to decide what to scale. We also convert a pretrained latent model, FLUX.2...
  </details>

- **2026-10-07** — Jiachen Zhao, Zhengxuan Wu, David Bau et al. — [The Persona Hierarchy Model: Understanding Contextual Generalization in Fine-Tuning LLMs](http://arxiv.org/abs/2610.09384v1)
  <details><summary>📄 Abstract</summary>
  Language models are routinely fine-tuned under a fixed context, such as a generic system prompt, persona or domain-specific instruction, yet the learned behavior sometimes stays confined to that context and sometimes broadly generalizes to unseen contexts. We propose the Persona Hierarchy Model to explain this: a shared default persona influences behavior across contexts. Under this model, fine-tuning that modifies the shared persona promotes broader transfer, whereas changes to local personas r...
  </details>

- **2026-10-07** — Jie Ren, Hao Kang, Kai Guo et al. — [ScribbleEdit: A Benchmark for Scribble-Only Image Editing](http://arxiv.org/abs/2610.09382v1)
  <details><summary>📄 Abstract</summary>
  Scribble-based interaction provides a lightweight and intuitive way for users to specify image editing intents in interactive editing tools. However, current image editing models based on VLMs or LLMs struggle to understand and execute edits based solely on scribble inputs. To systematically study this problem, we construct a new benchmark, ScribbleEdit, that evaluates the ability of image editing models to perform image editing conditioned on scribbles. This task requires both a deep understand...
  </details>

- **2026-10-07** — Moein Khajehnejad, Michelangelo Tronti, Forough Habibollahi et al. — [Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding](http://arxiv.org/abs/2610.09352v1)
  <details><summary>📄 Abstract</summary>
  Visual decoding from fMRI is typically siloed by participant and experiment, obscuring whether heterogeneous neural measurements can be organized within a common computational geometry. Here we introduce BRAID-fMRI (Brain Representation Alignment across Individuals and Datasets), a shared CLIP-supervised decoding framework. BRAID-fMRI uses a single ROI-wise Transformer with optional participant conditioning across eight visual-fMRI datasets comprising 93 dataset-specific participant entries, 430...
  </details>

- **2026-10-07** — Dung Truong, Kuntal Kokate, Arnaud Delorme — [Scaling subjects in cross-modal alignment: video decoding with EEG foundation model](http://arxiv.org/abs/2610.09287v1)
  <details><summary>📄 Abstract</summary>
  Naturalistic visual decoding from EEG has long been constrained by cohort size: existing scaling literature caps out at a few dozen subjects, leading prior work to conclude that scaling subject cohorts yields minimal performance gains. Training a cross-modal EEG--video contrastive encoder on a cohort larger by more than an order of magnitude, we find the axis is productive but has an onset. Below $S\approx50$ --- the entirety of the range prior work occupies --- no model improves meaningfully ov...
  </details>

- **2026-10-06** — Saba Sturua, Han Xiao — [What Transfers from a VLM Teacher? Comparing Supervision Signals for Visual Document Retrieval](http://arxiv.org/abs/2610.09177v1)
  <details><summary>📄 Abstract</summary>
  Visual document retrievers are trained contrastively: each query is matched to one page labelled relevant - the positive - and pushed away from negatives, pages presumed irrelevant. Recent methods distil a vision-language model (VLM) teacher into the retriever by enriching that positive, transferring the teacher's attention over it or a description of it. We ask whether the teacher is better spent on the other side, judging the candidates the retriever mines as negatives, which the label says no...
  </details>

- **2026-10-06** — Yujie Chen, Antik Chakraborty, Anindya Bhadra — [Covariate-dependent Joint Modeling of Multivariate Ordinal Preferences and Its Connections with Comparison Models](http://arxiv.org/abs/2610.09070v1)
  <details><summary>📄 Abstract</summary>
  Multivariate ordinal data along with covariates are commonly collected in problems ranging from alignment of language models with human preferences, as well as in recommender systems. For example, data sets such as MovieLens contain several movies rated on a scale 1--5 by human users, along with their demographic information such as age or gender. Similarly, data sets such as HelpSteer collect human feedback on several attributes such as "helpfulness" or "verbosity" of LLM response on an ordinal...
  </details>

- **2026-10-06** — Alina Sudakov, Guy Bar-Shalom, Fabrizio Frasca et al. — [Learning Cross-Model Activation Alignments with Explicit Many-to-Many Layer Maps](http://arxiv.org/abs/2610.09058v1)
  <details><summary>📄 Abstract</summary>
  LLMs are released at a rapid pace, raising a natural question: how do two independently trained models relate, both in which layers correspond and in how features transform between them? We study this by learning an activation alignment, a map from a source model's layerwise activations to a target's. Our method, MATCHA, factors this map into a layer map, whose output is an explicit target-by-source matrix that can be extracted and inspected, and a layer-shared feature map between hidden spaces....
  </details>

- **2026-10-06** — Jiamu Bai, Jiaming Hu, Yanhong Wu et al. — [Personalize at Test Time: Learning User Preferences for Image Generation](http://arxiv.org/abs/2610.09015v1)
  <details><summary>📄 Abstract</summary>
  Diffusion models can generate high-quality images, yet aligning their outputs with individual user preferences remains challenging. A key bottleneck is accurately modeling diverse user preferences from limited feedback. Existing approaches often rely on labor-intensive manual preference annotations or vision-language models (VLM) to extract preference information from user interaction histories, introducing substantial annotation or computational costs that limit scalability. We propose an appro...
  </details>

- **2026-10-06** — Ming Ren Hou, Tianyi Huang — [One-Slide Calibration of Pathology Foundation Models](http://arxiv.org/abs/2610.08944v1)
  <details><summary>📄 Abstract</summary>
  Scanner variation changes how pathology foundation models represent the same tissue. We introduce SlideRuler, which uses regions within a slide as internal controls to estimate and correct acquisition-induced shifts in other regions. A transfer map learned from paired rescans enables calibration from a single scan at inference while keeping the foundation model fixed. Across two encoders and five SCORPION scanners, learned transfer reduces mean target-to-source embedding distance by 16.3-38.5% r...
  </details>

- **2026-10-06** — Shiqi Li, Sean Cho, Yijie Li et al. — [4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction](http://arxiv.org/abs/2610.08782v1)
  <details><summary>📄 Abstract</summary>
  Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-...
  </details>

- **2026-10-06** — Jian Gao, Kailin Bi, Jiamin Xu et al. — [PrimitiveCAD: An LLM-Based Point-to-CAD Reconstruction with Primitive-Aware Tokenization and Operation Alignment](http://arxiv.org/abs/2610.08698v1)
  <details><summary>📄 Abstract</summary>
  Large-model-based point-to-CAD generation holds immense potential for advancing industrial design and enhancing 3D modeling efficiency. However, most existing methods approach the problem as a general point-cloud encoding and token prediction task, neglecting the tokenization and supervision specifically for CAD-related primitives. As a result, these methods often struggle to accurately reconstruct the intricate primitive structures. To address this limitation, we propose PrimitiveCAD, a novel m...
  </details>

- **2026-10-06** — Yexiong Lin, Shanshan Ye, Yu Yao et al. — [SquidAgent: Parallelize Wisely, Coordinate Efficiently](http://arxiv.org/abs/2610.08647v1)
  <details><summary>📄 Abstract</summary>
  LLM-based agents solve complex multi-step tasks, but sequential execution incurs substantial latency. In principle, parallelizing work across multiple agents should yield near-linear speedups. Yet existing parallel multi-agent systems often run slower than a single-agent baseline. We attribute this gap to two hidden costs that parallel execution incurs but a serial agent avoids. First, there is a re-exploration cost: redundant effort spent by parallel workers reconstructing context that the orch...
  </details>

- **2026-10-06** — Tatiana Brailovskaya, Nicholas A. Cook, Sofia Poinelli — [Spectral Recovery of Point Clouds from Noisy Geometric Graphs](http://arxiv.org/abs/2610.08634v1)
  <details><summary>📄 Abstract</summary>
  We study the problem of recovering low-dimensional latent geometry from a random geometric graph generated by noisy, high-dimensional data. Specifically, we analyze the performance of a spectral embedding algorithm on the Signal+Noise Graph Model, in which vertices are associated to points perturbed by Gaussian noise, and edges are included for pairs whose inner product exceeds a specified alignment threshold. In the high-dimensional regime where the number $n$ of points and the ambient dimensio...
  </details>

- **2026-10-06** — Dongchen Si, Di Wang, Mingzhen Xu et al. — [RSJEV: Discriminative Remote Sensing Scene Classification with Multimodal Large Language Models](http://arxiv.org/abs/2610.08539v1)
  <details><summary>📄 Abstract</summary>
  Remote sensing scene classification is a fundamental task in Earth observation and geospatial analysis. Existing approaches mainly follow three paradigms: task-specific visual classification, vision-language similarity matching, and autoregressive multimodal generation. However, visual classifiers rely on predefined label spaces, CLIP-based methods perform recognition through static image-text alignment, and multimodal large language models (MLLMs) introduce unnecessary token-level generation fo...
  </details>

- **2026-10-06** — Onur Selim Kilic, Afra Nawar, Cem Okan Yaldiz et al. — [Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation](http://arxiv.org/abs/2610.08510v1)
  <details><summary>📄 Abstract</summary>
  Paired translation between quasiperiodic physiological waveforms (i.e., recovering a target oscillatory signal from the source) is central to the interpretation of cardiovascular signals derived from wearables placed at different body locations. This source-to-target mapping in these problems carries inherent geometric structure: the phase wraps around the cycle and must be treated as a circular variable, the amplitude remains strictly positive, and the beat-to-beat alignment can drift unpredict...
  </details>

- **2026-10-06** — Han Ma — [Replica Fragmentation and Glassy Dynamics in Parity Learning](http://arxiv.org/abs/2610.08503v1)
  <details><summary>📄 Abstract</summary>
  We study how independently trained Transformer neural networks reconstruct a binary string from its local domain walls. Runs sharing the data and training protocol can realize different functions. We treat them as replicas and measure truth alignment $m$, prediction confidence $q_{\mathrm{self}}$, and cross-replica agreement $q_{\mathrm{cross}}$. Confident disagreement defines the finite-size replica fragmentation that we call glass-like. With small training sets, replicas predict all training e...
  </details>

- **2026-10-06** — Agnieszka Lach, Magdalena Wysocki, Feng Li et al. — [Deformable CT-US Registration via Anatomy-Aware Implicit Neural Representations](http://arxiv.org/abs/2610.08419v1)
  <details><summary>📄 Abstract</summary>
  Slice-to-volume registration between ultrasound (US) and preoperative computed tomography (CT) imaging would enhance many minimally invasive interventions, for example by locating soft tissue structures intra-operatively that are discernible in CT. While optical tracking enables initial rigid registration, contact from the probe induces soft tissue deformations that inhibit accurate alignment. In this work, we introduce a deformable CT-ultrasound registration framework that incorporates anatomic...
  </details>

- **2026-10-06** — Zhibo Deng, Dongyuan Li, Shuwen Ge et al. — [Enhancing LLMs with Cognitive-Affective Personality Inference for Simulating Human Social-Psychological Behavior](http://arxiv.org/abs/2610.08328v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate human participants in social and behavioral studies, yet static persona prompting typically maps a participant profile and an experimental scenario directly to a response, entangling stable dispositions with situation-specific interpretations. To address this limitation, we introduce \textbf{SPIN}, a cognitive-affective personality system-inspired inference pipeline for simulating human social-psychological behavior. Specifically, SPIN impl...
  </details>

- **2026-10-06** — Shu-Kai Hsieh, Da-Chen Lian — [Language Unalignability: Why Some Concepts Resist Cross-Cultural Benchmark Evaluation](http://arxiv.org/abs/2610.08303v1)
  <details><summary>📄 Abstract</summary>
  Current evaluation of multilingual Large Language Models (LLMs) rests on an implicit Translation-Isomorphism Assumption (TIA): that semantic structures across languages are congruent and mutually mappable without loss of information. We argue that this assumption is not merely violated in practice, but ill-posed in principle for a typologically identifiable class of concepts, including pragmatic markers, honorifics, and diachronically stratified terms. We formalize this failure using a usage-clo...
  </details>

- **2026-10-06** — Shixin Peng, Kun Jiang, Jiaxing Zheng et al. — [MASC: A Multi-Agent Self-Calibration Framework with Latent Construct Alignment for Consistent Client Role-Playing in Psychological Counseling](http://arxiv.org/abs/2610.08250v1)
  <details><summary>📄 Abstract</summary>
  Large language models are increasingly used to simulate clients for counselor training and psychological counseling research, but reliable simulation requires clients to remain psychologically coherent across extended interactions. Existing role-playing methods largely rely on static profile prompts and may exhibit persona drift, unrealistic cooperativeness, or inconsistent psychological states, communicative actions, and emotions. Existing evaluations also lack a unified testbed for both stable...
  </details>

- **2026-10-06** — Ahmed Abouelazm, Rupert Polley, Qingyuan Zhang et al. — [Beyond Waypoint Regression: Query-Based Cost Learning over Reachable Ego Futures for End-to-End Driving](http://arxiv.org/abs/2610.08123v1)
  <details><summary>📄 Abstract</summary>
  End-to-end planners based on waypoint regression achieve strong open-loop accuracy, but they primarily learn to mimic expert geometry and remain difficult to adapt to deployment-time safety constraints. We propose a query-based cost-learning framework that estimates bounded costs for dynamically reachable ego trajectory queries, rather than dense BEV cells or a small regressed trajectory set. Compact joint scene tokens capture coherent multimodal agent futures, while contingency-aware cost aggre...
  </details>

- **2026-10-06** — Langxi Huang, Pingping Zhang, Lanyun Zhu et al. — [ChartBmkAgent: Harness-Governed Multi-Agent Construction of Chart QA Benchmarks from Sparse Error-Taxonomy Specifications](http://arxiv.org/abs/2610.08106v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) advance rapidly, while conventional benchmark development lags behind, delaying investigation of newly observed capability gaps. Such investigation requires an expressive task format and an on-demand construction process: information-rich charts make chart question answering (Chart QA) suitable for probing coupled perception and reasoning. Automated Chart QA construction is intended to shorten the benchmark-development cycle by turning identified gaps int...
  </details>

- **2026-10-06** — Hemant Yadav, Sunayana Sitaram, Roger Zimmermann et al. — [DirectSpeech2LLM: A Simple End-to-End Framework to Mitigate Prompt Overfitting in Speech-LLMs](http://arxiv.org/abs/2610.08085v1)
  <details><summary>📄 Abstract</summary>
  Speech-LLMs often exhibit prompt overfitting, where models solely trained on automatic speech recognition (ASR) instruction fail to generalize to new instructions such as speech translation and continue to behave primarily as ASR system. We propose DirectSpeech2LLM, a simple end-to-end framework that preserves the instruction-following ability of the LLM on unseen tasks when conditioned on speech. It computes distance-based CTC loss over the frozen LLM embedding matrix and uses greedy CTC labels...
  </details>

- **2026-10-06** — Rudolf L. M. van Herten, Soufiane Ben Haddou, Rachit Saluja et al. — [Optimization Encoders: Rethinking Second-Order Meta-Learning for Neural Fields](http://arxiv.org/abs/2610.08075v1)
  <details><summary>📄 Abstract</summary>
  Conditional neural fields represent signals continuously, but their effectiveness depends on how the conditional latent representations are inferred from observed data. In meta-learning, this encoding occurs through gradient updates induced by the decoder, tying representation learning directly to decoder design. We formalize this connection by interpreting latent optimization as an optimization encoder, unifying the roles of second-order differentiation, latent parameterization, and task superv...
  </details>

- **2026-10-06** — Jing Chen, Giulia Loca, Simona Amenta et al. — [Pseudowords as probes: Large Language Models show little of the sublexical sensitivity that governs human pseudoword processing](http://arxiv.org/abs/2610.07936v1)
  <details><summary>📄 Abstract</summary>
  Systematicity, the probabilistic mapping of form to meaning, permeates language at all levels, and sublexical cues have been shown to govern human pseudoword processing. Yet whether LLMs exhibit comparable sensitivity to these cues remains unclear. We tested five LLMs on two Italian two-alternative forced-choice pseudoword experiments and compared their responses with a human behavioural baseline. LLMs aligned more reliably with humans when real-word options provided a lexical familiarity cue th...
  </details>

- **2026-10-06** — Giyeol Kim, Chanho Eom — [TF-PRVR: Training-Free Partially Relevant Video Retrieval](http://arxiv.org/abs/2610.07925v1)
  <details><summary>📄 Abstract</summary>
  Partially Relevant Video Retrieval (PRVR) aims to retrieve untrimmed videos containing moments relevant to a given text query. Despite recent progress, existing PRVR methods suffer from two key limitations: a fixed video decomposition scheme that causes semantic dilution, and source-domain overfitting induced by task-specific training. In this paper, we propose TF-PRVR, the first training-free framework for PRVR. TF-PRVR leverages frozen vision-language features to construct video-specific hiera...
  </details>

- **2026-10-06** — Keliang Chen, Yaxin Hou, Hui Liu et al. — [Unsupervised Long-Tailed Adaptation of Vision-Language Models](http://arxiv.org/abs/2610.07903v1)
  <details><summary>📄 Abstract</summary>
  Adapting vision-language models to downstream tasks has achieved remarkable success by leveraging pseudo-labels generated from unlabeled data. Existing methods typically assume a uniform unlabeled data distribution, and thus the resulting pseudo-label distribution is likewise uniform. However, real-world data distributions are often long-tailed. To tackle this, we formalize a new scenario termed Unsupervised Long-Tailed Adaptation (ULTA). Under this scenario, existing methods exhibit a contrasti...
  </details>

- **2026-10-06** — Yuezhe Zhang, Lei Wei, Jingnan Du et al. — [Geometry-Constrained Bidirectional Point Cloud Registration for Thin, Sheet-Like Heritage Artifacts](http://arxiv.org/abs/2610.07793v1)
  <details><summary>📄 Abstract</summary>
  Non-contact three-dimensional reconstruction of thin, sheet-like heritage artifacts poses significant geometric and registration challenges. Due to their fragility, these artifacts cannot be suspended or equipped with artificial markers, necessitating independent acquisition of their front and back surfaces. Subsequent registration proves difficult due to the limited number of shared geometric features and the scarcity of explicit physical constraints, which may result in rotational ambiguity, i...
  </details>

- **2026-10-06** — Xin Wang, Hao Yu, Zhengyang Zhuge et al. — [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](http://arxiv.org/abs/2610.07767v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the discrepancy between the two quantized execution paths. In this work, we propose TRACE (Trai...
  </details>

- **2026-10-06** — Byeonghu Na, Donghyeok Shin, Yeongmin Kim et al. — [WASD: Wasserstein-based Knowledge Distillation for Large Language Models](http://arxiv.org/abs/2610.07706v1)
  <details><summary>📄 Abstract</summary>
  Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time. Knowledge distillation (KD) offers a practical solution by transferring knowledge from a large teacher model to a smaller student model via alignment of discrete probability distributions. However, existing KD methods for LLMs primarily rely on divergences that evaluate discrepancies through probability values at each...
  </details>

- **2026-10-06** — Juntong Li, Lingwei Dang, Haomin Wu et al. — [Unlocking Fine-Grained Perception in CLIP via Structurally-Aware Latent Masked Modeling](http://arxiv.org/abs/2610.07689v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language Models (VLMs) such as CLIP excel in global semantic alignment but often lack fine-grained perceptual capabilities. This hinders dense prediction tasks and bottlenecks the visual potential of Multimodal Large Language Models (MLLMs). Existing research has attempted to enhance CLIP's visual representations by incorporating geometric priors from vision-centric models. However, these strategies often struggle to achieve deep alignment for both local spatial structures and global sema...
  </details>

- **2026-10-06** — Guo Tang, Yongtao Wang — [PhysTacGen: Physics-Aware Visual-Tactile Sensor Image Generation](http://arxiv.org/abs/2610.08068v1)
  <details><summary>📄 Abstract</summary>
  Realistic physical interaction is a cornerstone of embodied intelligence, yet collecting paired visual--tactile data remains costly. Visual-to-tactile synthesis offers a promising approach to augmenting such data, but learning this mapping is complicated by the gap between visual appearance and contact-related material properties, as well as spatial misalignment in paired observations. To address these challenges, we present \textbf{PhysTacGen}, a visual-to-optical-tactile image generation frame...
  </details>


### 📂 robustness
*鲁棒性与可靠性 / Robustness & Reliability* — 57 papers

- **2026-10-07** — Mikey Watts, Yuchen Cui — [Rephrase Before You Act: Characterizing and Mitigating Language Sensitivity in Vision-Language-Action Models](http://arxiv.org/abs/2610.10526v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action models (VLAs) are strikingly sensitive to instruction phrasing and do not inherit the language robustness of the vision-language models they are built on. A one-word edit can move success by tens of points: $π_{0.5}$ turns on a LIBERO stove 100% of the time for "switch on the stove" and 2% for "switch on the hot plate", and a $π_0$ checkpoint finetuned with rephrase augmentation still shows swings of up to 61 points. We characterize this sensitivity with statistically test...
  </details>

- **2026-10-07** — Prakhar Ganesh, Kyra Wilson, Luca Zappella et al. — [Homogenization in Multi-Agent Systems](http://arxiv.org/abs/2610.09824v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent systems (MAS) leverage interactions between agents to perform complex tasks. Despite their success, we show that these interactions can also lead to homogenization, i.e., agents converging to similar behaviors. Homogenization in MAS can reduce agent diversity and reinforce shared failures. In this paper, we operationalize homogenization using three metrics: conformity to the majority, polarization towards extremes, and growing inertia against changes over subsequent interactions. We ...
  </details>

- **2026-10-07** — Nadhem Zmandar, Mo El-Haj, Paul Rayson — [A Comparative Study of Evaluation Metrics for Long-Document Financial Narrative Summarization with Transformers](http://arxiv.org/abs/2610.09529v1)
  <details><summary>📄 Abstract</summary>
  There are more than 2,000 listed companies on the UK's London Stock Exchange, divided into 11 sectors who are required to communicate their financial results at least twice in a single financial year. UK annual reports are very lengthy documents with around 80 pages on average. In this study, we aim to benchmark a variety of summarisation methods on a set of different pre-trained transformers with different extraction techniques. In addition, we considered multiple evaluation metrics in order to...
  </details>

- **2026-10-07** — Eike S. Eberhard, Xaver Kainz, Viktor Kotsev et al. — [Physics-Aligned Electronic Ground-State Learning Improves Generalization](http://arxiv.org/abs/2610.10298v1)
  <details><summary>📄 Abstract</summary>
  Machine-learned interatomic potentials (MLIPs) excel at in-distribution tasks, accelerating drug and material development, yet they struggle to generalize out-of-distribution. We propose to push the cost-accuracy Pareto frontier by designing observable-agnostic electronic ground-state descriptor models (GSMs) with computational costs situated between MLIPs and Kohn-Sham density functional theory (KS-DFT). We align the learning objectives and architectures of GSMs with the governing equations of ...
  </details>

- **2026-10-07** — Yuchen Zhu, Chenyi Xu, Yulin Zhang et al. — [Juno: Taming Predictive Latents for Vision-Language-Action Models](http://arxiv.org/abs/2610.09940v1)
  <details><summary>📄 Abstract</summary>
  Joint-embedding predictive architectures (JEPAs) predict masked or future observations in representation space, offering a natural source of predictive latents for vision-language-action (VLA) models. Yet making these latents useful across pretraining, policy learning, and deployment requires addressing three failures: mismatch with embodiment-specific control, interference with action learning, and teacher miscalibration under distribution shifts. We introduce Juno, a unified framework built ar...
  </details>

- **2026-10-07** — Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson — [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](http://arxiv.org/abs/2610.09763v1)
  <details><summary>📄 Abstract</summary>
  Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-critical domains. A central challenge, however, is distribution shift: policy optimization may favor actions that are weakly supported by the offline data, rendering value estimates unreliable. Existing approaches primarily control this shift in the policy's own action space. In interactive environments such as autonomous dr...
  </details>

- **2026-10-07** — Mike Zhang, Dongho Kang, Kevin Bergamin et al. — [HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion](http://arxiv.org/abs/2610.10489v1)
  <details><summary>📄 Abstract</summary>
  Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time steerable, robust, and biomimetic locomotion policies from human data. Using an in-house curated locomotion dataset covering diverse speeds...
  </details>

- **2026-10-07** — Jixuan Chen, Jiaxin Zhang, Qinyuan Ye et al. — [CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution](http://arxiv.org/abs/2610.10426v1)
  <details><summary>📄 Abstract</summary>
  Terminal-agent capability depends jointly on model weights and the runtime harness that formats prompts, binds tools, and handles error recovery. Existing harness-model co-evolution approaches improve both components, yet often treat trajectories produced during harness search as an undifferentiated replay buffer. This practice overlooks that a trajectory's value for model training depends on the harness under which it was generated. To systematically analyze this interface, we establish an alte...
  </details>

- **2026-10-07** — Nipun Ghanghas, Dinil B. Palakkatharappil, Rafael A. Garcia et al. — [ROSE (Red-giant Oscillations Spectra Estimator): A Modular Machine-Learning Framework for Automated Asteroseismic Characterisation. I. $ν_{\max}$ and $Δν$ from TESS](http://arxiv.org/abs/2610.10312v1)
  <details><summary>📄 Abstract</summary>
  Space-based photometry from Kepler and TESS has delivered oscillation spectra for hundreds of thousands of red giants, and PLATO and the Roman Galactic Bulge Time-Domain Survey will add more. We present ROSE, a modular machine-learning framework for automated asteroseismic characterisation of red giants, and apply two of its modules to the frequency of maximum oscillation power, $ν_{\rm max}$, and the large frequency separation, $Δν$. Each module is a neural network bundled with its own preproce...
  </details>

- **2026-10-07** — Theodor Wulff, Angelo Cangelosi — [Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding](http://arxiv.org/abs/2610.10178v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their...
  </details>

- **2026-10-07** — Zhongping Ji — [HySPE: Positional Encoding via Symplectic Dual Shears](http://arxiv.org/abs/2610.10154v1)
  <details><summary>📄 Abstract</summary>
  We introduce Hyperbolic Symplectic Positional Encoding (HySPE), grounding positional attention in non-compact symplectic transformations. While canonical Rotary Position Embedding (RoPE) parameterizes the compact, elliptic branch of $\Sp(2,\R)$ via rotations, HySPE operationalizes its hyperbolic branch via a damped symmetric composition of dual shears, yielding a conformally symplectic contraction with two spectral decay rates per channel pair. To eliminate the exponential representation drift i...
  </details>

- **2026-10-07** — Alessandro Beatini, Marco Maronese, Emanuele Rodolà — [Activation-Aware Weight Tensorization: A Calibration-Time Preconditioner for Tensor-Network LLM Compression](http://arxiv.org/abs/2610.10085v1)
  <details><summary>📄 Abstract</summary>
  Post-training tensor-network compression replaces Transformer linear layers with Tensor Train (TT) or Tree Tensor Network (TTN) operators, but standard decompositions minimize weight-space Frobenius error rather than functional error under the layer's activation distribution. We propose Activation-aware Weight Tensorization (AWT), a training-free calibration wrapper that preconditions each weight matrix with a diagonal activation-derived scale before an unchanged TT/TTN solver and deploys the re...
  </details>

- **2026-10-07** — Matthieu Jeannin, Alessandro Chessari, Jan Von Delft — [Efficient Optimization of Tensor Rings with Low-Rank Environments](http://arxiv.org/abs/2610.10027v1)
  <details><summary>📄 Abstract</summary>
  Tensor-ring (TR) decompositions provide a natural representation of periodic systems but are difficult to optimize because the closed geometry prevents a global canonical form and leads to costly, ill conditioned environments. Existing periodic DMRG methods alleviate this difficulty by compressing long environments to a low-rank representation, reducing local operations to $\mathcal{O}(pχ^3)$, where $p$ is the retained environment rank. Here, we extend this approach to an efficient two-site Ring...
  </details>

- **2026-10-07** — Eliyahu Levy, Adam Teman, Yoni Pugachov — [TR-PTQ: High-Accuracy Integer-Only Transformer Post Training Quantization via Taylor Region Reformulation](http://arxiv.org/abs/2610.09969v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization (PTQ) enables efficient deployment, yet transformer architectures remain challenging to quantize due to nonlinear layers. While existing methods attribute accuracy loss to insufficient numerical precision, often necessitating floating-point fallbacks, we demonstrate that degradation is actually driven by specific structural error sources. We find that learned scale parameters in normalization layers and compounded approximations in GELU are the primary error contributo...
  </details>

- **2026-10-07** — Bernardo A. C. Pereira, Marcos Carvalho, Fatih Temiz et al. — [Deadline-Aware Multi-Agent Reinforcement Learning for TSN-Based Vehicular Edge Networks](http://arxiv.org/abs/2610.09870v1)
  <details><summary>📄 Abstract</summary>
  Vehicular edge computing (VEC) enables latency-sensitive applications by bringing computing and networking resources closer to vehicles. However, existing approaches often overlook network contention among co-located services with heterogeneous and dynamic latency requirements. While time-sensitive networking (TSN) provides bounded-latency communication, conventional and reinforcement learning-based schedulers struggle to adapt to highly dynamic vehicular environments and inter-queue dependencie...
  </details>

- **2026-10-07** — Henrique L. Senger, Gustavo P. Gonçalves, Bruno S. Chang et al. — [Effects of Residual Chirp Rate on DAFT-s-AFDM Uplink Performance](http://arxiv.org/abs/2610.09851v1)
  <details><summary>📄 Abstract</summary>
  Affine frequency division multiplexing (AFDM) is robust to doubly dispersive channels in high-mobility 6G systems but, like orthogonal frequency division multiplexing (OFDM), suffers from a high peak-to-average power ratio (PAPR). Spreading with a discrete affine Fourier transform (DAFT) yields DAFT-s-AFDM, whose precoder and modulator chirps can be chosen independently. For a single user with zero-offset localized allocation, we show that these two chirps merge into a single residual chirp whos...
  </details>

- **2026-10-07** — Masaaki Nakatsu, Reno Wang — [Decoupling Logic from Persona: Structural Immunity of Edge LLM Agents to Context Pollution](http://arxiv.org/abs/2610.09772v1)
  <details><summary>📄 Abstract</summary>
  Small language-model agents on edge devices must hold a persona and reason correctly at once, inside one context window that fills with conversational history and persona instructions. We study what happens to the logical part of such an agent when that history is long, misleading and persona-heavy (persona-logic interference), and present a Decoupling Architecture (AO-DA) that separates logical inference ("What") from persona expression ("How") into two inference paths on one INT4 base model wi...
  </details>

- **2026-10-07** — Tom Beucler, J. David Neelin, Hui Su et al. — [Artificial intelligence pathways from weather to climate](http://arxiv.org/abs/2610.09770v1)
  <details><summary>📄 Abstract</summary>
  Deep learning has made rapid advances in weather forecasting: autoregressive models trained on atmospheric reanalyses now rival dynamical models across nowcasting, medium-range, and subseasonal-to-seasonal lead times, producing well-calibrated ensemble forecasts at reduced cost. We review these advances and consider their extension to climate horizons, where the challenge shifts from initial-condition skill to producing reliable statistical responses under altered forcings. AI-powered climate pr...
  </details>

- **2026-10-07** — Mariia Baidachna, Nicolas Pugeault — [Flow-of-Thought: A Framework for Visual Reasoning](http://arxiv.org/abs/2610.09746v1)
  <details><summary>📄 Abstract</summary>
  Mental imagery, ``seeing with the mind's eye'' is an essential aspect of human cognition. Despite rapid progress Large Language Models (LLMs) and Vision Transformers (ViTs) still underperform on tasks requiring spatial understanding. To address this, we introduce Flow-of-Thought (FoT), a framework that integrates the generation of visual sketches as intermediate reasoning steps, mimicking mental imagery in humans. We train coordinate-aware trajectory flow fields on $SO(2)$ group orbits and cumul...
  </details>

- **2026-10-07** — Sourav Saha, Aditya Dutta, Soumajit Pramanik et al. — [Towards Explaining Query Expansion Performance in Information Retrieval](http://arxiv.org/abs/2610.09724v1)
  <details><summary>📄 Abstract</summary>
  Query Expansion (QE) techniques have long been widely used in Information Retrieval (IR) to address the vocabulary mismatch problem. They remain relevant in modern retrieval systems, including those based on large language models (LLMs). However, no single QE method consistently outperforms others across all queries. This work seeks to explain the variation in QE performance through two complementary perspectives. The first is the concept of an Ideal Expanded Query (IEQ)--a hypothetical query th...
  </details>

- **2026-10-07** — Sangyoon Bae, Sk Miraj Ahmed, Shinjae Yoo et al. — [Pretraining Shapes Spectral Structure: Architecture- and Strategy-Conditional Prediction of OOD Robustness in Foundation Models](http://arxiv.org/abs/2610.09709v1)
  <details><summary>📄 Abstract</summary>
  Can we determine whether a foundation model will generalize out-of-distribution (OOD) before any target data is available? Existing diagnostics require source or target data, which rules them out before a target domain exists. Those that use the weights alone apply one statistic to every architecture, and do not separate robust models from fragile ones. We show the answer is encoded in the spectral structure of pretrained weights. Two forces shape that structure. Architecture determines how info...
  </details>

- **2026-10-07** — Qifan Zhang, Ruijie Li, Fangzhou Zhang et al. — [CircuitGate: Logic-Consistent Circuit-Level Functional Modeling for And-Inverter Graphs](http://arxiv.org/abs/2610.09549v1)
  <details><summary>📄 Abstract</summary>
  And-Inverter Graphs (AIGs) are fundamental representations for logic synthesis and verification in Electronic Design Automation (EDA). As structured representations of complex digital systems, AIGs require models to capture functional dependencies beyond local structure and remain robust to functionality-preserving transformations. In learning-based AIG representation, existing approaches are predominantly based on GNNs and rely on local gate-level message passing, limiting their ability to capt...
  </details>

- **2026-10-07** — Dasari Naga Raju — [TIRA: Tumor Immune Representation Adaptation for Zero-Shot Cross-Cancer MSI and TMB Prediction](http://arxiv.org/abs/2610.09441v1)
  <details><summary>📄 Abstract</summary>
  Microsatellite instability-high (MSI-H) and high tumor mutational burden (TMB-H) are clinically relevant biomarkers, yet their histopathological prediction remains challenging when models are transferred across morphologically distinct cancer types. Immune-associated spatial patterns can persist across cancers despite these morphological differences, but foundation-model-based predictors trained on a single cancer do not explicitly use this information, limiting cross-cancer generalization. To a...
  </details>

- **2026-10-07** — Shadi Alijani, Fereshteh Aghaee Meibodi, Homayoun Najjaran — [Quantifying Volumetric Risk: Class-Aware Asymmetric Weighted Conformal Prediction for 3D Medical Image Segmentation](http://arxiv.org/abs/2610.09392v1)
  <details><summary>📄 Abstract</summary>
  Reliable volumetric segmentation is critical for clinical diagnostics, yet foundation models such as MedSAM remain deterministic and lack calibrated uncertainty under distribution shift. Existing conformal prediction methods offer statistical guarantees but are frequently applied in 2D and assume symmetric error distributions, so they do not capture the class-specific biases that arise in 3D multi-class segmentation. We propose Class-Aware Asymmetric Weighted Conformal Prediction (CA-WCP), which...
  </details>

- **2026-10-07** — Tomonari Kanazawa, Hikaru Hoshino, Eiko Furutani — [Learning Stability of Replay-Based Co-Optimization for Transmission Expansion under Strategic Bidding](http://arxiv.org/abs/2610.09366v1)
  <details><summary>📄 Abstract</summary>
  This paper investigates the behavior of learning-based co-optimization for transmission expansion under strategic bidding in electricity markets. In this framework, transmission capacities are updated while market participants simultaneously learn their bidding strategies through deep reinforcement learning, resulting in coupled and non-stationary learning dynamics. We show that transient policy degradation of bidding agents can generate inconsistent cost-capacity samples, which bias the transmi...
  </details>

- **2026-10-07** — Yatai Ji, Zhengqiu Zhu, Yong Zhao et al. — [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](http://arxiv.org/abs/2610.09335v1)
  <details><summary>📄 Abstract</summary>
  Autonomous unmanned aerial vehicle (UAV) object search involves a closed loop of perception, decision-making, and action under partial observability. Urban environments pose several challenges: large search areas and narrow egocentric views limit coverage, dense 3D geometry constrains safe motion, and open-world instructions require identifying a specific target among distractors. Many existing methods mitigate partial observability through explicit maps or memory representations, yet remain lar...
  </details>

- **2026-10-07** — Fangping Lan, Qi Zhang, Eduard Dragut — [CATune: Structural Constraint-Aware Bayesian Optimization for DBMS Configuration Tuning](http://arxiv.org/abs/2610.09276v1)
  <details><summary>📄 Abstract</summary>
  Modern DBMSs expose hundreds of configuration knobs, resulting in a high-dimensional and heterogeneous search space that makes automated tuning costly. Existing ML-based tuning systems typically treat the configuration domain as box-constrained and rely on workload feedback to implicitly capture inter-knob relationships. However, DBMS documentation specifies deterministic knob dependency constraints, particularly ordering constraints, that characterize structurally valid regions of the configura...
  </details>

- **2026-10-06** — Wenqi Li, Bin Liu, Mindi Ruan et al. — [Conditional Accuracy Profiles: Diagnosing LLM Judges across Deployment Conditions](http://arxiv.org/abs/2610.09229v1)
  <details><summary>📄 Abstract</summary>
  LLM-as-judge is now a standard tool for scalable evaluation, but judge performance is still often summarized by a single accuracy number. This aggregate view hides the deployment conditions under which a judge succeeds or fails. We introduce \textbf{Conditional Accuracy Profiling} (CAP), a post-hoc diagnostic framework that decomposes pairwise LLM-judge accuracy into eight conditions organized into content sensitivity, robustness, and rationale quality. CAP is benchmark-agnostic: it can be appli...
  </details>

- **2026-10-06** — Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal et al. — [ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation](http://arxiv.org/abs/2610.09163v1)
  <details><summary>📄 Abstract</summary>
  Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks often emphasize successful, cooperative interactions and underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present ToolRACER, a synthetic data generation pipeline that coordinates user,...
  </details>

- **2026-10-06** — Haoran Li, Zengle Ge, Xiaomin Yuan et al. — [RLDISCOVER: LLM-driven co-evolution of reinforcement learning algorithms](http://arxiv.org/abs/2610.09218v1)
  <details><summary>📄 Abstract</summary>
  LLM-guided program evolution has enabled discoveries in mathematics and computational optimization, raising the prospect of reinforcement learning (RL) algorithms that self-evolve to improve how agents learn. However, realizing this prospect faces two obstacles. Joint search over coupled algorithmic components is difficult to scale: simultaneous changes can disrupt learning, while isolated changes overlook their dependencies. Evaluating candidate algorithms also requires costly training, with fi...
  </details>

- **2026-10-06** — Uzair Akbar, Zulfiqar Zaidi, Niki Kilbertus et al. — [Symmetry-Informed Causal Partial Identification](http://arxiv.org/abs/2610.09230v1)
  <details><summary>📄 Abstract</summary>
  Partial identification (PI) entails estimating bounds on causal effects by encoding different assumptions on data generation as a constrained optimization problem. Such bounds can suffice to inform policy decisions even if the causal effect itself is not identifiable. Often vacuous in practice, practitioners seek to exhaustively encode domain knowledge as additional constraints to make the PI bounds more informative. We introduce known data symmetries -- invariance of the causal effect under cer...
  </details>

- **2026-10-06** — Rabimba Karanjai, Qun Gu, Hemanth Hegadehalli Madhavarao et al. — [CM-DPO: Constraint-Margin Direct Preference Optimization for LLM Planning](http://arxiv.org/abs/2610.09219v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) treats all constraint violations equally: a $1 budget overshoot and a $1,000 overshoot induce the same training signal. It is also susceptible to length and style bias when preference pairs come from different model families. We introduce Constraint-Margin DPO (CM-DPO), which replaces DPO's binary preference signal with a continuous margin derived from a deterministic symbolic verifier and scaled by violation severity. Hard and soft constraints are separated ...
  </details>

- **2026-10-06** — Amrut Nadgir, Pratik Chaudhari, Vijay Balasubramanian — [The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning](http://arxiv.org/abs/2610.09186v1)
  <details><summary>📄 Abstract</summary>
  We argue that pattern recognition and step-by-step reasoning are two ends of a spectrum. A large language model (LLM) learns to reason step-by-step when data is structured such that the next token depends on a small amount of preceding context. Inference in LLMs resembles pattern recognition when the next token depends on a large amount of preceding context. If the next token depends on only the $c$ most recent tokens, reasoning traces are paths on a De Bruijn graph whose nodes are $c$-length co...
  </details>

- **2026-10-06** — Arash Raftari, Babak Ebrahimi Soorchaei, Yaser P. Fallah — [Context-aware Attention-based Gaussian Mixture Models for Vehicular Trajectory Prediction](http://arxiv.org/abs/2610.09174v1)
  <details><summary>📄 Abstract</summary>
  Reliable and interpretable trajectory prediction is critical for cooperative and autonomous driving in complex and uncertain environments. This paper introduces a Context-Aware Attention-based Gaussian Mixture Model (CAA-GMM) for multimodal, uncertainty-aware motion forecasting. The proposed approach models future motion as a probabilistic mixture conditioned on both scene context and agent dynamics, capturing diverse behavioral modes with interpretable Gaussian components. A lightweight attenti...
  </details>

- **2026-10-06** — Shaoang Li, Daniel R. Jiang, Jian Li — [Constraint Tree Exploration for Learning from Language Feedback](http://arxiv.org/abs/2610.09107v1)
  <details><summary>📄 Abstract</summary>
  Natural-language feedback in interactive learning often explains why an action failed by pointing to violated requirements. Misinterpreting this feedback can lead an agent to rule out valid solutions. We study this setting by modeling user intent as latent constraints over an action space and formulating learning from language feedback as pure exploration over feasible regions. We introduce TRACE, an algorithm that organizes candidate constraints in a tree and tests each proposed refinement by g...
  </details>

- **2026-10-06** — Tobias Braun, Nils Loose, Alexander Herzog et al. — [U-Space: Uncovering When and Why Uncertainty Arises in Language Models](http://arxiv.org/abs/2610.09087v1)
  <details><summary>📄 Abstract</summary>
  Large language models are informing decisions with ever-higher stakes. As the consequences of their errors grow, a central question becomes harder to ignore: how much can we trust an individual answer? Yet recognizing when to defer remains difficult because language models can present incorrect conclusions with fluent explanations and an authoritative tone. Uncertainty quantification seeks to address this disconnect by estimating the reliability of individual predictions. However, many existing ...
  </details>

- **2026-10-06** — Sourabh Kasliwal, Shubhranshu Singh — [Multi-Label Topic Assignment via LLM Distillation: A Comparative Analysis of Generative vs. Discriminative Student Models](http://arxiv.org/abs/2610.09063v1)
  <details><summary>📄 Abstract</summary>
  Multi-label topic assignment for user-generated content (UGC) -- including product reviews and buyer-seller conversations -- poses unique scalability challenges in large-scale e-commerce due to informal language, extreme label sparsity, and rapidly evolving taxonomies. While utilizing Large Language Models (LLMs) as labeling oracles to distill ground-truth data has emerged as an industry standard to bypass prohibitive manual annotation costs, determining the optimal, low-latency architecture for...
  </details>

- **2026-10-06** — Mani Kumar Tellamekala, Tosh Brown, Michel Valstar — [Shape-Bayes: Bayesian Inference of Structured Shapes under Visual Ambiguity](http://arxiv.org/abs/2610.09032v1)
  <details><summary>📄 Abstract</summary>
  Perceiving structured shapes, such as human faces, from pixels is an inherently ambiguous task in real-world conditions. Yet, shape inference is largely posed as a deterministic regression task predicting fixed spatial coordinates. We find that deterministic regression is brittle when visual evidence is ambiguous or incomplete; under severe occlusions deterministic models exhibit structural collapse, predicting incoherent shapes or reverting to generic averages. To address this, we introduce Sha...
  </details>

- **2026-10-06** — Amir Mohammad Mahfoozi, Zi Yang, Ying Li et al. — [Random Feature Gaussian Process Attention: Linear-Time Probabilistic Attention with Calibrated Uncertainty](http://arxiv.org/abs/2610.08578v1)
  <details><summary>📄 Abstract</summary>
  Transformers provide a state-of-the-art modeling framework, yet poor calibration limits their reliability in safety-critical applications. A promising direction addresses this issue by interpreting attention as a Gaussian process (GP) posterior, which enables principled uncertainty calibration but incurs cubic complexity in sequence length due to the inversion of the kernel; although decoupled GP variants reduced the cost to quadratic, the computation remains prohibitive in practice. In this pap...
  </details>

- **2026-10-06** — Hyeongheon Cha, Young D. Kwon, Sung-Ju Lee — [Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration](http://arxiv.org/abs/2610.08358v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization is a standard route to fitting vision transformers (ViTs) into edge compute and memory budgets, yet quantized models become especially brittle under distribution shift. Test-time adaptation (TTA) addresses such shifts without labels, but most existing approaches are poorly aligned with the constraints of quantized inference. Prevailing TTA methods recover accuracy through backpropagation, while backprop-free methods often still incur overhead from extra forward passes ...
  </details>

- **2026-10-06** — Haotian Yang, Huikang Jiang, Yucheng Wu et al. — [Does Steering Break Your Model? A Multi-Dimensional Evaluation Suite for LLM Steering Methods](http://arxiv.org/abs/2610.07722v1)
  <details><summary>📄 Abstract</summary>
  Activation steering provides a lightweight and flexible way to control large language model (LLM) behavior. However, effective steering requires more than inducing the intended behavior: it should also limit unintended changes and remain robust across inputs and training data. Existing evaluations cover these dimensions only in fragments. As a result, the trade-offs between efficacy and side effects have not been systematically characterized. We introduce SteerScope, a two-axis, multi-dimensiona...
  </details>

- **2026-10-06** — Kun Song, Yiming Wang, Yilin Chen et al. — [PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation](http://arxiv.org/abs/2610.08784v1)
  <details><summary>📄 Abstract</summary>
  Pretrained robotic policies can suffer substantial performance degradation under out-of-distribution (OOD) conditions encountered during deployment, motivating post-training through real-world interaction. However, reinforcement-learning (RL)-based post-training typically requires substantial environment interactions, a burden that is especially significant in manipulation, where each trial can be slow, costly, or destructive. Therefore, we present PEARS, a physics-prior-guided hybrid RL framewo...
  </details>

- **2026-10-06** — Mingju Gao, Qingle Liu, Yuzhao Peng et al. — [World Models' Last Exam in Physics](http://arxiv.org/abs/2610.08791v1)
  <details><summary>📄 Abstract</summary>
  Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks s...
  </details>

- **2026-10-06** — Nataliya Stepanova, Ivan Titov, Emily Allaway et al. — [The Missing Minimal Pair: Stereotype Evaluation in LLMs](http://arxiv.org/abs/2610.08747v1)
  <details><summary>📄 Abstract</summary>
  A common approach to measuring bias in Large Language Models is to compare the log-likelihoods of two contrastive stereotype sentences. We argue that such single-pair comparisons are often unreliable: simply rewriting the same stereotype with an alternative attribute can yield logically inconsistent preferences. To address this, we propose a dual minimal pair setup that introduces two axes of comparison for robust stereotype evaluation. First, we present a data-augmentation framework that fills ...
  </details>

- **2026-10-06** — Clayton Cohn, Joyce Fonteles, Kirk Vanacore et al. — [Agreement Is Not Validity: Cross-Model LLM Consensus in Diagnosing Student Failure Modes in K-12 Math Tutoring Dialogue](http://arxiv.org/abs/2610.08703v1)
  <details><summary>📄 Abstract</summary>
  In K-12 mathematics tutoring, student-tutor dialogue provides rich evidence of learners' problem-solving processes and sources of difficulty. Learning analytics research increasingly relies on large language models (LLMs) to extract such information from dialogue for a variety of downstream tasks, including knowledge tracing, behavioral modeling, and diagnosis of student reasoning errors. However, the validity of these model-generated interpretations remains insufficiently understood. In this ex...
  </details>

- **2026-10-06** — Nur A Zarin Nishat, Jens Lehmann, Andrei Aioanei et al. — [A Systematic Study of Small Language Models on Abstract Reasoning Tasks](http://arxiv.org/abs/2610.08680v1)
  <details><summary>📄 Abstract</summary>
  Endpoint accuracy on abstract-reasoning benchmarks does not reveal whether a language model has acquired a transferable rule or fit distribution-specific regularities. We study this distinction in small language models on the ARC-TGI benchmark, which organizes abstract grid transformations into controllable task families and supports resampling, spatial shifts, and cross-benchmark transfer. Across more than 1,000 runs, we profile decoder-only, encoder--decoder, and mixture-of-experts model famil...
  </details>

- **2026-10-06** — Sayan Sinha, Vipul Harsh, B. Aditya Prakash et al. — [Agentic RCA for Internet-Scale Services Using Constrained Creativity](http://arxiv.org/abs/2610.08622v1)
  <details><summary>📄 Abstract</summary>
  System administrators of Internet-scale services need to resolve failure incidents to maintain reliability of such services. Ideally, we want a troubleshooting system to be: (1) expressive to known and unknown incidents with high accuracy; (2) cost efficient at scale; (3) explainable to provide actionable insights operators can act on; and (4) entail low effort from the operators. Unfortunately, most existing systems, including emerging LLM-assisted agentic workflows and structured frameworks fo...
  </details>

- **2026-10-06** — Pranjal Garg — [How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing](http://arxiv.org/abs/2610.08544v1)
  <details><summary>📄 Abstract</summary>
  Probes are the workhorse of interpretability. If a model's hidden states predict a variable, the model is said to represent it. But a probe score has no fixed meaning. An $R^2$ of 0.6 may only reflect what the input already gives away, and the same score can mean different things on different data. We propose reading every probe score against two reference points: a floor, what a declared set of simple inputs already predicts, and a ceiling, what the full input can predict. The gap between them,...
  </details>

- **2026-10-06** — Dennis Fucci, Andrea Bacciu, Dong Liu et al. — [Wiki-Talkie: Multilingual Benchmarking of Persona-Based Agents on Real-World Discussions](http://arxiv.org/abs/2610.08513v1)
  <details><summary>📄 Abstract</summary>
  LLMs are increasingly deployed as autonomous agents in social environments, making it critical to study their ability to faithfully simulate human interactions. Central to this is grounding agents in realistic user personas, yet existing datasets rely on fictional personas and are limited to a handful of languages, lacking the empirical grounding necessary to evaluate behavioral fidelity across diverse populations. We introduce Wiki-Talkie, a multilingual dataset of real-world conversations from...
  </details>

- **2026-10-06** — Aleksandr Talitckii, Matthew M. Peet — [Stable Rational Approximation of PDE Transfer Functions with $H_\infty$ Error Bounds](http://arxiv.org/abs/2610.08497v1)
  <details><summary>📄 Abstract</summary>
  Transfer functions of Partial Differential Equations (PDEs) are irrational and difficult to obtain. Unlike for rational transfer functions, only a few methods are available for the control and analysis of irrational transfer functions. Thus, for robust analysis and control of PDEs, we need to use a rational approximation of the transfer function, preferably with provable $H_\infty$ error bounds. In this paper, we extend Krylov subspace model reduction to infinite-dimensional systems modeled by P...
  </details>

- **2026-10-06** — Rohan Hemant Chhatre, Chiranjit Dutta, Nalini Ravishanker et al. — [Scalable Regularized Vector Multiplicative Error Models for Positive-valued Financial Time Series](http://arxiv.org/abs/2610.08443v1)
  <details><summary>📄 Abstract</summary>
  The logarithmic multiplicative error model (log-vMEM) has been useful in modeling and forecasting multivariate positive-valued financial time series. The number of parameters grow rapidly with the dimension of the system and the lag order, making estimation computationally demanding in high-dimensional settings. This paper describes regularized estimation via hierarchical lag structures (Nicholson et al., 2020) for log-vMEM models with multivariate gamma error distribution of Tsionas (2004). The...
  </details>

- **2026-10-06** — Ekrem Aydiner — [A New Model for the Income Distribution](http://arxiv.org/abs/2610.08143v1)
  <details><summary>📄 Abstract</summary>
  In this study, we propose a kinetic trap--diffusion model to describe the emergence of Pareto distributions in money-exchange systems. Using kinetic Monte Carlo simulations, we show that the Pareto exponent depends explicitly on temperature and takes values in the range $0.5 \leq ν(T) \leq 1.5$. In the present framework, the temperature $T$ acts as a control parameter that regulates the exchange dynamics through thermally activated diffusion. Unlike conventional kinetic exchange models, where th...
  </details>

- **2026-10-06** — Anam Hashmi, Mayug Maniparambil, Julia Dietlmeier et al. — [Beyond Training from Scratch: Foundation Models for Data-Efficient and Generalizable Cardiac MRI Reconstruction](http://arxiv.org/abs/2610.08109v1)
  <details><summary>📄 Abstract</summary>
  Cardiac magnetic resonance imaging reconstruction aims to recover high-quality images from undersampled acquisitions, enabling faster scans while preserving diagnostic fidelity. Recent reconstruction methods are typically trained from scratch and often require large amounts of task-specific data, limiting their robustness under data scarcity and distribution shifts. In this work, we investigate whether pretrained vision foundation models can serve as effective priors for accelerated cardiac MRI ...
  </details>

- **2026-10-06** — Yuan Feng, Qize Yang, Ruizhe Chen et al. — [VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](http://arxiv.org/abs/2610.07987v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact representations. Downsampling sacrifices this detail, while existing token pruning and adaptive approaches remain limited in content-adaptive granularity, task generalization, and integration with mode...
  </details>

- **2026-10-06** — Yuhe Hu — [Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs](http://arxiv.org/abs/2610.07781v1)
  <details><summary>📄 Abstract</summary>
  Post-training quantization reduces the cost of deploying language-model agents, but its effect on recovery from temporary tool failures can depend on how recovery is evaluated. We compare 8-bit and 4-bit variants of Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct on twenty deterministic tool-use tasks and five prompts. The 8-bit-4-bit recovery comparison changes direction across prompts and evaluation targets. On tasks that both variants complete without faults under the same prompt, the differenc...
  </details>

- **2026-10-06** — Hyeongheon Cha, Hyungjun Yoon, Sung-Ju Lee — [Later Is Better: Token Reduction for ViTs Under Distribution Shift](http://arxiv.org/abs/2610.07758v1)
  <details><summary>📄 Abstract</summary>
  Training-free token reduction accelerates vision transformers by removing redundant tokens across layers, recovering most of the original accuracy at a fraction of the compute. These methods, however, are designed and evaluated primarily on clean data, and under real-world distribution shift their accuracy gap to the uncompressed model widens with the removal rate. We show that this gap is governed by the reduction schedule, the depth profile of removal, usually left fixed as an implementation d...
  </details>

- **2026-10-06** — Yi Xia, Pablo Carrasco Velo, Mudit Paliwal et al. — [SENSE: State-aware Emotion Navigation Storytelling Engine](http://arxiv.org/abs/2610.07666v1)
  <details><summary>📄 Abstract</summary>
  This paper presents SENSE, a state-aware framework for generating playable branching visual novels with multi-track emotional navigation. Integrating a state-based narrative architecture called MIND, a structure analyzer, and a path-aware context management module, SENSE produces narratives that are both structurally coherent and emotionally rich. From minimal high-level inputs, it generates multiple intersecting routes while preserving character consistency and narrative causality. Evaluations ...
  </details>


### 📂 watermark
*水印与溯源 / Watermarking & Provenance* — 18 papers

- **2026-10-07** — Amit Nautiyal — [Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data Attribution in Online RL](http://arxiv.org/abs/2610.10422v1)
  <details><summary>📄 Abstract</summary>
  When reinforcement learning teaches a language model a new behavior, can we find the training rollouts that taught it? And when an attribution method says it can, how do we know the answer is real? We study both questions on online RL fine-tuning with GRPO, using a planted behavior with a known cause. We release BehaviorTrace, an open evaluation harness that combines full-gradient sketching, the planted-behavior setup, and controls for gradient magnitude, fluency, headroom, and variation across ...
  </details>

- **2026-10-07** — J. -P. Bouchaud, I. Mastromatteo, B. Toth — [On Bonart's interpretation of the Square-Root Impact Law](http://arxiv.org/abs/2610.10053v1)
  <details><summary>📄 Abstract</summary>
  The square-root impact law (SRIL), $I = Yσ\sqrt{Q/V}$, bundles two facts that a single mechanism must explain at once: a shape (impact proportional to square-root of traded volume $Q$) and an amplitude ($Y=O(1)$, independent of the participation rate $\varphi$). Bonart has recently proposed an elegant solution: if realized and counterfactual prices are both diffusive, information-neutral impact must have white increments and the SRIL follows without the wart. We reformulate and simplify his argu...
  </details>

- **2026-10-07** — Jinheon Baek, Soyeong Jeong, Yumin Choi et al. — [RunningTab: Direct Workspace Interaction with Environment-Side Tabs](http://arxiv.org/abs/2610.10444v1)
  <details><summary>📄 Abstract</summary>
  Much knowledge work produces new deliverables from files a workspace already holds, and LLM agents are beginning to take such work over. Through direct corpus interaction, an agent can search and read any of those files from a terminal with no indexing, and producing a deliverable from many of them in this way is what we call direct workspace interaction (DWI). Reaching the files, however, is only half the task: nothing keeps track of what the task asks for, what has been read, and what was list...
  </details>

- **2026-10-07** — Kun Liu, Liqun Chen — [OOM-RL II: Reality Is an Oracle, Not a Debugger Provenance-Constrained Diagnosis in Continually Evolving Agent-Engineered Systems](http://arxiv.org/abs/2610.10256v1)
  <details><summary>📄 Abstract</summary>
  Reality may establish that an outcome occurred without identifying which evolving procedure produced it or why. This distinction matters in production ML systems whose code, configuration, and artifacts change while external feedback accumulates. We examine it in a human-directed, agent-engineered quantitative trading system, using oracle to mean an external source of realized outcomes rather than a complete correctness specification. Across one year, the account gained and outperformed a broad ...
  </details>

- **2026-10-07** — Hengbo Xiao, Boyao Zhang, Purui Liu et al. — [RewardWeaver: Long-Horizon Interactive Learning for Language Agents via Self-Evolving Reward Adaptation](http://arxiv.org/abs/2610.10120v1)
  <details><summary>📄 Abstract</summary>
  Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in domains where task outcomes can be reliably evaluated, but long-horizon interaction remains challenging due to sparse terminal feedback and difficult credit assignment. Process rewards provide denser supervision, yet the capabilities most relevant for training can change as the policy evolves: a behavior that is easy to evaluate or frequently deficient need not be the bottleneck currently limiting task succe...
  </details>

- **2026-10-07** — Gabriel Ocana-Santero, Marko Tvrdic — [CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies](http://arxiv.org/abs/2610.09643v1)
  <details><summary>📄 Abstract</summary>
  Drug discovery for neurological disease has traditionally centered on the molecules altered by disease. But the molecules that cause pathology are not necessarily the best points from which to reverse it. Here, we ask which otherwise unaltered molecular control points can be engaged to restore pathological neural circuits toward functional states. We present CircuitATLAS, a provenance-grounded systems-neuroscience knowledge graph and agentic framework for target discovery in circuitopathies. It ...
  </details>

- **2026-10-07** — Jiayu Feng — [Right Number, Wrong State? Measuring Cross-Jurisdiction Substitution in LLM Recall of State Policy](http://arxiv.org/abs/2610.09458v1)
  <details><summary>📄 Abstract</summary>
  When an LLM answers a state-specific policy question wrongly, it may be hallucinating, or it may be returning a real value that holds in another state. We test this with a minimal-set design: the question wording is fixed and only the jurisdiction varies, across the 50 U.S. states and the District of Columbia (51 jurisdictions) and three exactly defined Medicaid income-eligibility quantities. Gold values come from an official data book and agree with an independent source in 101 of 102 checked c...
  </details>

- **2026-10-07** — Xiaofei Zhang — [No Trace, No Claim: Two Contracts for Database Agents](http://arxiv.org/abs/2610.09286v1)
  <details><summary>📄 Abstract</summary>
  LLM agents can generate database operations and explain their results, but current interfaces often leave a gap between generated plans, execution conditions, and claims presented to users. We argue that agent-facing data systems need two enforceable contracts. A plan contract defines what an agent may execute and reference; an evidence contract records the belief state, completeness, and provenance under which a result supports a claim.   We instantiate these contracts in TGMS, a bi-temporal gr...
  </details>

- **2026-10-06** — Wenhui Chu, Sheikh Rabiul Islam — [TwinGuard-Lite: A Rule-Based State-Admission Gateway for Generative Patient Digital Twins](http://arxiv.org/abs/2610.09012v1)
  <details><summary>📄 Abstract</summary>
  Future generative patient digital twins may combine longitudinal health records with language-model agents and keep information across sessions. The wording of a proposed update does not reveal whether it comes from an allowed source, conflicts with the patient's record, or belongs to someone else. We present TwinGuard-Lite, a rule-based gateway that admits an update to a twin's persistent state only if it passes checkable approximations of two integrity properties. Grounded state consistency (G...
  </details>

- **2026-10-06** — Mahesh Viswanathan, Joan Rossello, Leticia Fernandes et al. — [From High Recall to High Utility: Dataset-Adaptive Post-Processing of LLM-Generated Customer Intents](http://arxiv.org/abs/2610.09039v1)
  <details><summary>📄 Abstract</summary>
  Large language models can extract useful signals from heterogeneous enterprise data, but high-recall extraction often produces outputs that are duplicated, uneven in granularity, semantically overlapping, or too numerous for downstream systems and human reviewers to use effectively. We present a dataset-adaptive post-processing architecture developed for Customer Intent Extraction (CIE), where unstructured customer language is transformed into stable, traceable intent units. The approach separat...
  </details>

- **2026-10-06** — Haibo Jin, Peng Kuang, Xucheng Yu et al. — [Large-scale Repository Engineering via Agent-Native Reusable Code Primitives](http://arxiv.org/abs/2610.09079v1)
  <details><summary>📄 Abstract</summary>
  Large language models equipped with development environments have moved code generation toward repository-scale construction, yet building complete repositories remains difficult because interacting modules, interfaces, configurations, tests, and dependencies must work together. We introduce Code Primitives, agent-native reusable executable components with interface contracts, dependency closures, validation tests, and provenance. Each primitive uses a resident LLM to assess relevance and adapt ...
  </details>

- **2026-10-06** — Hongyu Gu, Xinchang Li — [Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory](http://arxiv.org/abs/2610.09008v1)
  <details><summary>📄 Abstract</summary>
  Persistent memory allows an LLM agent to carry experience across conversations, but it also turns a local reasoning mistake into a durable one. During deliberation, an agent may consider a plan, simulate a tool result, report another speaker's belief, and then reject all of them. If memory retains only the resulting sentences, those once-useful possibilities can later return as facts. The record is neither fabricated nor irrelevant; it has simply been detached from the context in which it was va...
  </details>

- **2026-10-06** — Mariya Miteva, Maria Nisheva-Pavlova — [Evidence-Bound Reasoning: Neuro-Semantic Verification of Biomedical AI in Glioblastoma Radiogenomics](http://arxiv.org/abs/2610.08660v1)
  <details><summary>📄 Abstract</summary>
  Background: Biomedical AI can generate plausible explanations without reliably verifying whether each statement is supported by patient-specific evidence. We developed a neuro-semantic verification framework that converts radiomic measurements into addressable evidence records and machine-checkable claims. Methods: UPenn-GBM radiomics were aligned with de novo CaPTk extraction from standardized MRI and expert-validated segmentations in an independent multicenter cohort. The shared space comprise...
  </details>

- **2026-10-06** — Guangyi Liu, Yong Liu, Jiangning Zhang — [nanoMuse: An Open-Source Personal Agent for Every Device You Own](http://arxiv.org/abs/2610.08699v1)
  <details><summary>📄 Abstract</summary>
  Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This rep...
  </details>

- **2026-10-06** — Lasse B. Strand, Robert Jakob, Kevin O'Sullivan et al. — [Agentic AutoRAG: RAG Pipeline Optimization through Reasoning-Driven Agents](http://arxiv.org/abs/2610.08452v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation (RAG) is a widely used approach for grounding large language models (LLMs) in external knowledge. However, configuring a pipeline is an expensive hyperparameter optimization problem over many interacting choices, from chunking and embedding model to reranking and generation. Existing optimizers, from greedy search to Bayesian optimization, reduce each trial to an aggregate score and search without modeling why a configuration performed as it did, even though the re...
  </details>

- **2026-10-06** — Yacine Benihaddadene, Milan Bhan, Eliot Dugelay et al. — [TICDA: Tabular In-Context Data Attribution](http://arxiv.org/abs/2610.07996v1)
  <details><summary>📄 Abstract</summary>
  Tabular foundation models (TFMs) achieve strong predictive performance by conditioning on labeled demonstrations provided in context, without any parameter update. Yet how individual demonstrations shape a given prediction remains poorly understood. This gap matters in practice: the context is often assembled from whatever labeled data is available, potentially leading to the inclusion of mislabeled, redundant, or low-quality examples that degrade performance. Standard data attribution methods d...
  </details>

- **2026-10-06** — Hongzhan Lin, Shidong Cao, Ziyang Luo et al. — [From Evidence to Action: How Tool-Using Agents Fail](http://arxiv.org/abs/2610.07753v1)
  <details><summary>📄 Abstract</summary>
  Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much weaker interactive execution. Failures often begin before execution: agents stop wit...
  </details>

- **2026-10-06** — Chen Chen, Dongjie Wang, Mei Liu et al. — [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](http://arxiv.org/abs/2610.07739v1)
  <details><summary>📄 Abstract</summary>
  Post-discharge risk prediction from electronic health records (EHRs) is difficult because many dependencies that link discharge-time observations to downstream complications, such as comorbidity cascades and drug-disease interactions, are absent from the record. External medical knowledge graphs (KGs) can supply these missing dependencies, but tracing them demands three properties: KG exploration must remain cost-bounded, retrieved evidence must be differentiated by source quality, and the resul...
  </details>


### 📂 unlearning
*机器遗忘 / Machine Unlearning* — 2 papers

- **2026-10-07** — Jiho Lee, Jeongeun Park, Heayoun Choi et al. — [Sparse Feature Policy Unlearning Mitigates State Hallucination in Vision-Language-Action Models](http://arxiv.org/abs/2610.09496v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by leveraging rich representations from pretrained vision-language models. However, their deployment in real-world environments remains limited by recurring unreliable behaviors. In this work, we study state hallucination, a recurring failure pattern in which a VLA continues acting as if an unrealized robot-object state had been achieved. Our analyses find that state hallucination coincides with weakened...
  </details>

- **2026-10-06** — Hwiyeong Lee, Hyelim Lim, Ingyu Bang et al. — [How Learning Governs Unlearning across the Memorization-Generalization Spectrum](http://arxiv.org/abs/2610.08577v1)
  <details><summary>📄 Abstract</summary>
  While unlearning seeks to negate undesired capabilities acquired through learning, little research has examined how the way models learn shapes their subsequent unlearning. In this paper, we investigate this connection from the perspectives of memorization and generalization, the two most representative yet competing strategies that models employ during training. We first classify memorization- and generalization-heavy models using grokking in modular addition and compare their responses to unle...
  </details>


### 📂 agent-safety
*Agent 安全框架 / Agent Safety Frameworks* — 1 papers

- **2026-10-07** — Tianruo Rose Xu, Jiawei Ren, Yichi Yang et al. — [RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment](http://arxiv.org/abs/2610.09294v1)
  <details><summary>📄 Abstract</summary>
  Rapid progress in AI agents has brought growing attention to agent safety, with extensive evaluation focused on digital environments. As agents move into the physical world, embodied safety becomes increasingly important: failures can cause human injury and costly hardware damage. Beyond selecting safe actions, embodied agents must also operate under real-time constraints: the physical world does not pause while an agent reasons. As pedestrians move and vehicles approach during inference, an act...
  </details>


### 📂 survey
*综述与系统化 / Surveys & Systematization* — 9 papers

- **2026-10-07** — Shivam Shukla, Jihye Kim, Shubham Gaur et al. — [RELATE: An Evaluation Framework for measuring Relational Orientation of Large Language Models](http://arxiv.org/abs/2610.09569v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used for emotional support, raising concern that sustained use may draw users away from their real-world relationships. Yet existing evaluations primarily focus on the safety, empathy, or helpfulness of responses, leaving under-examined a relational question: where does the model orient the user for continued support? To address this question, we introduce relational orientation, a property operationalized through two non-exclusive dimensions: inward...
  </details>

- **2026-10-07** — Raviraja G, Viraj Bagal, Prabhath Chellingi — [From Retrieval to Customer Context: Evaluating Frontier-Model Systems for Voice-of-Customer Analysis](http://arxiv.org/abs/2610.09375v1)
  <details><summary>📄 Abstract</summary>
  Organizations increasingly use frontier language models to analyze customer feedback, but answer quality also depends on how that feedback is organized and made available. We define a \emph{customer context graph} as a unified model of customer and business context. Typed relationships connect customer objects (feedback, conversations, users, and accounts), operational objects (tickets, support agents, opportunities, and competitors), and analytical or action objects (taxonomy concepts, evidence...
  </details>

- **2026-10-07** — Nicolas Lacroix, Frederic Precioso, Mireille Blay-Fornarino et al. — [Using Small Language Models to Reverse-Engineer Machine Learning Pipelines Structures](http://arxiv.org/abs/2610.10261v1)
  <details><summary>📄 Abstract</summary>
  Context: Once defined a taxonomy of stages structuring Machine Learning (ML) pipelines (e.g. Data Preprocessing, Modeling...), extracting these stages from source code is key for better understanding ML practices. However, the diversity caused by the constant evolution of ML (e.g., algorithms, datasets) makes this task challenging. Existing approaches either rely on non-scalable manual labeling or on classifiers that do not properly support domain's diversity. These limitations call for more rel...
  </details>

- **2026-10-07** — Robert Bredereck, Eva Deltl, Tanmay Inamdar et al. — [Envy-free Allocations with Individual Payments](http://arxiv.org/abs/2610.09610v1)
  <details><summary>📄 Abstract</summary>
  When an envy-free allocation of indivisible goods does not exist, monetary transfers can restore envy-freeness. Existing work on fair division with subsidies, however, typically assumes that these payments are provided by an external source, an assumption that may be unrealistic in many applications. We address this limitation by allowing only monetary transfers between agents, with each agent's payments constrained by their individual budget. We show that while it is polynomial-time tractable t...
  </details>

- **2026-10-07** — Hyeongjun Choi — [MARS: Malware Analysis with Rule-Based Scoring of LLM Claims](http://arxiv.org/abs/2610.09553v1)
  <details><summary>📄 Abstract</summary>
  Large language models can triage malware through direct verdicts or behavioral claims scored by an external policy. We present MARS, a malware triage framework, and compare direct classification with single-pass claim scoring using the same evidence collector and identical static evidence bundles for each model. The evaluation covers 1,195 PE and ELF binaries grouped into 1,001 near-duplicate clusters and six language models, with deterministic rules providing a baseline. Direct classification i...
  </details>

- **2026-10-06** — Xingang Guo, Jing Gu, Brian Jang et al. — [Humanity's Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal Models](http://arxiv.org/abs/2610.08966v1)
  <details><summary>📄 Abstract</summary>
  Humans perceive far more in a scene than what is explicitly depicted: a single glance captures past causes and future trajectories; a quick peek determines if a vehicle can fit between two parked cars; a few seconds of video reveals who holds authority in a room; and a fleeting clip highlights subtle abstract patterns like unwritten rules or hidden labels. This capacity reflects a form of humanity's sixth sense: an intuitive reasoning mechanism that recovers implicit information beyond raw senso...
  </details>

- **2026-10-06** — Haoyu Huang, Zhongwei Xie, Jiaxin Bai et al. — [Towards In-Parameter Memory Augmentation for Large Language Models](http://arxiv.org/abs/2610.08630v1)
  <details><summary>📄 Abstract</summary>
  Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. \textbf{In-parameter memory} offers a complementary substrate: reusable memory information is represented in mo...
  </details>

- **2026-10-06** — Viraj Bagal, Raviraja Ganta, Prabhath Chellingi — [Same Feedback, Different Answer: Measuring Run-to-Run Instability in Frontier-Model Customer Feedback Analysis](http://arxiv.org/abs/2610.08036v1)
  <details><summary>📄 Abstract</summary>
  AI agents are increasingly being programmed to automate knowledge work over large collections of unstructured data. Such automation requires repeatability: when the underlying evidence is unchanged, the agent's categories, priorities, and counts should not shift materially between runs, even if each individual answer appears plausible. We introduce a repeat-run evaluation framework that aligns semantically equivalent categories and focuses on two operating metrics: theme churn, the normalized ch...
  </details>

- **2026-10-06** — Kevin Lee — [CETUS: How Far Do Representations Trained on Earth Transfer to Cassini SAR of Titan?](http://arxiv.org/abs/2610.07576v1)
  <details><summary>📄 Abstract</summary>
  Cassini synthetic aperture radar (SAR) images reveal the dunes, plains, and lake basins of Titan, providing an instance of representations learned from Earth imagery for planetary terrain classification. Cross-domain Evaluation of Earth-to-Titan Transfer Using SAR (CETUS) compares features from DINOv2, DOFA and CROMA with classical image measurements and features from an untrained vision transformer on the U.S. Geological Survey's Cassini SAR mosaic. The classifiers learn terrain labels from an ...
  </details>


### 📂 other
*其他安全相关 / Other Security-Related* — 198 papers

- **2026-10-07** — Takahiro Ezaki, Naoto Imura, Katsuhiro Nishinari — [Shared and structured inputs undermine collective random choice by reasoning AI agents](http://arxiv.org/abs/2610.09667v1)
  <details><summary>📄 Abstract</summary>
  Random selection is widely used in resource allocation and auditing, making reliable implementation essential for AI-agent systems. Behavioural tests across six reasoning models uncovered threshold and divisibility rules used in identifier-based choices. For threshold-following GPT-6 Sol and Gemini 3.8 Flash, single-agent measurements prospectively predicted correlated participation under shared identifiers and biased participation under distinct identifiers with common timestamp bits. Changing ...
  </details>

- **2026-10-07** — Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda et al. — [Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents](http://arxiv.org/abs/2610.09469v1)
  <details><summary>📄 Abstract</summary>
  Computer-use agents (CUAs) perform tasks across applications (such as desktops, mobile apps, and web browsers) by observing graphical interfaces and issuing commands such as clicks and keystrokes. These interfaces combine trusted controls and content with untrusted content needed for legitimate tasks. An adversary controlling this untrusted content can embed instructions or misleading visual cues to change the agent's intended action or redirect its commands to the wrong interface target. We for...
  </details>

- **2026-10-07** — Kerui Li, Zhe Jing, Chenyi Huang et al. — [RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation](http://arxiv.org/abs/2610.09454v1)
  <details><summary>📄 Abstract</summary>
  Robotic manipulation videos are increasingly used as visual plans for embodied agents, but optimizing purely for visual plausibility often fails to capture the fragile physical manifold of real-world interactions. Even minor physics-violating errors at the interaction boundary, such as interpenetration or premature object motion, can completely invalidate the inferred timing and pose needed for downstream execution. Because standard supervised fine-tuning lacks the direct pressure to penalize th...
  </details>

- **2026-10-07** — Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam et al. — [GRACE: Generation-aware latent compression for efficient video generation](http://arxiv.org/abs/2610.10524v1)
  <details><summary>📄 Abstract</summary>
  Highly compressed video autoencoders offer an effective way to accelerate video diffusion models, as the Diffusion Transformer (DiT) operates on far fewer tokens. However, such autoencoders are challenging to train, since a higher compression ratio degrades reconstruction quality and recovering it requires more channels, which is known to slow the convergence of the DiT. The compressed latent also differs from the one the DiT was trained on, so the pretrained DiT must be either retrained from sc...
  </details>

- **2026-10-07** — Sarath Sankar, Abhijit Sinha, Shankar Ghosh et al. — [Trend formation with sparse global sampling](http://arxiv.org/abs/2610.10521v1)
  <details><summary>📄 Abstract</summary>
  Achieving global coordination without a central controller or dense global communication is a defining challenge for both biological collectives and engineered swarms. We introduce and analyze a minimal model in which self-propelled agents in a bounded domain periodically reorient their motions toward the centroid of a small, randomly chosen subset of their peers, with no direct sensing of any individual neighbor's position or heading. We show that this sparse, non-local sampling rule reliably d...
  </details>

- **2026-10-07** — Yihan Li, Yating Feng, Shengjiu Sun et al. — [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](http://arxiv.org/abs/2610.10479v1)
  <details><summary>📄 Abstract</summary>
  A simulation of a real robot workspace must preserve task-relevant interactions, while policies developed in it must operate on observations available to the real robot. Yet scene reconstruction and policy development are often treated separately. We present Agentic Real-to-Sim-to-Real (Agentic RSR), a framework that links scene reconstruction, policy development, and real-robot execution through the same manipulation task. Given a workspace video, a task description, and a known robot model, an...
  </details>

- **2026-10-07** — Ting-Yu Dai, Takuya Kurihana, Wing Yee Au et al. — [NeuralBES: A Differentiable, Control-Aware Emulator for Scalable Building Energy Modeling](http://arxiv.org/abs/2610.10459v1)
  <details><summary>📄 Abstract</summary>
  Demand-side flexibility i.e. forecasting, shifting, and curtailing residential energy loads, depends on thermal models trusted across millions of heterogeneous buildings. Existing tools force a hard tradeoff: high-fidelity physics simulators such as EnergyPlus are accurate but sequential and require per-building calibration, while purely data-driven sequence models scale but abandon the physical structure that makes their predictions trustworthy.   We introduce NeuralBES (Building Energy Simulat...
  </details>

- **2026-10-07** — Xingtai Gui, Yucheng Zhou, Dongqian Guo et al. — [Explicit Geometric Chain-of-Thought for Vision-Language-Action in Autonomous Driving](http://arxiv.org/abs/2610.10390v1)
  <details><summary>📄 Abstract</summary>
  Vision-language-action~(VLA) models have emerged as a promising paradigm for autonomous driving. However, existing VLA models still suffer from a fundamental mismatch: driving actions require precise 3D geometric cues, while visual-language understanding and reasoning are largely conducted in a 2D semantic space. In this paper, we propose GeoCoTDrive, an explicit geometric chain-of-thought framework that grounds geometry in a planning-oriented manner. GeoCoTDrive follows a think with 2D first, d...
  </details>

- **2026-10-07** — Liu Renhang, Navonil Majumder, Tej Deep Pala et al. — [RoboQuest: Generalist Physical Agents that Search, Inspect and Test](http://arxiv.org/abs/2610.10388v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in multimodal foundation models have made them capable generalist physical agents for a range of manipulation tasks. However, successful operation in an unfamiliar environment may require an agent to seek task-relevant information through interaction when it is absent from the observations: it may need to determine where a relevant object is, inspect an unobserved property, or discover the effect of an unfamiliar tool. We thus introduce RoboQuest, a benchmark for goal-directed em...
  </details>

- **2026-10-07** — Kerui Chen, Jianrong Zhang, Kai Lv et al. — [From Digital Human Interactions to Physics-Based Humanoid Skills: Physics-Grounded Post-Training of Interaction Generators](http://arxiv.org/abs/2610.10322v1)
  <details><summary>📄 Abstract</summary>
  Recent methods have made promising progress in generating interactions between two humanoids, largely relying on physics-based tracking policies to convert digital reference motions into executable trajectories. However, limited tracking capabilities restrict the range of reference motions that can be successfully executed, reducing data utilization. Moreover, even successful tracking does not guarantee physically plausible responses or faithful realization of the intended interactions. In this ...
  </details>

- **2026-10-07** — Amir Rafe, Subasish Das — [Estimating Uncoded Crash Factors with Tabular Foundation and System One Models: Kumo Tabular and Jev](http://arxiv.org/abs/2610.10321v1)
  <details><summary>📄 Abstract</summary>
  Road safety programs count the coded fields of police crash records, while the officer's narrative, which often records factors the fields omit, is rarely read. A safety office thus cannot tell how much its counts miss or where to review. This study develops and evaluates a system that joins both views of the 5,601,890 Texas crashes from 2017 to 2025 into population estimates with stated validity. An in-context tabular foundation model, Kumo Tabular, reads the coded record of every crash, a cali...
  </details>

- **2026-10-07** — Hanyong Xu, Zhaolai Dang, Tong Zhang — [Beyond LLM-GA: Secure Fluid Antenna Systems with ReEvo-Designed Memetic Algorithm](http://arxiv.org/abs/2610.10235v1)
  <details><summary>📄 Abstract</summary>
  Fluid antenna systems (FASs) offer significant spatial flexibility, yet securing them against eavesdropping is critical for practical FAS deployment in military, satellite, and internet-of-things networks. Although large language model (LLM)-assisted genetic algorithms (LLM-GAs) can address this secure FAS port selection problem, whether further algorithmic improvement is possible warrants deeper investigation. To this end, we propose a memetic algorithm based on reflective evolution (ReEvo). Un...
  </details>

- **2026-10-07** — Hyojae Kang, Hyun-mok Jung, Joonho Lee et al. — [Design of a Fully Actuated 4-DOF Robotic Finger With Joint-Specific Hybrid Remote Actuation](http://arxiv.org/abs/2610.10180v1)
  <details><summary>📄 Abstract</summary>
  This paper presents a fully actuated 4-DOF robotic finger using a joint-specific hybrid remote-actuation architecture. The metacarpophalangeal (MCP) joint is driven by two coordinated rigid-link transmission sets, whereas the proximal interphalangeal (PIP) and distal interphalangeal (DIP) joints are independently actuated by closed-loop wire transmissions incorporating circular rolling-contact joints (RCJs). A larger transmission radius is used at the PIP joint than at the DIP joint. The RCJ wir...
  </details>

- **2026-10-07** — Andrey Kuehlkamp, Priscila Correa Saboia Moreira, Samuel Rund — [Does Document Structure Help Dense Retrieval? A Placebo-Controlled Ablation of Four Mechanisms Across Two Corpora](http://arxiv.org/abs/2610.10170v1)
  <details><summary>📄 Abstract</summary>
  Retrieval-augmented generation systems increasingly rely on document-structure treatments: structure-aligned chunking, LLM-generated chunk contexts, heading-path metadata, and hierarchical two-stage retrieval. Separate studies support each on different corpora, embedders, and metrics, and none control for a shared confound: any text prepended to a chunk perturbs its embedding. We present a mechanism-isolating ablation testing all four treatments under one protocol, matching chunk sizes across co...
  </details>

- **2026-10-07** — Yossi Arjevani — [Eigenvalues of the Hessian in Deep Learning: The Origin of Symmetry and Its Breaking](http://arxiv.org/abs/2610.09919v1)
  <details><summary>📄 Abstract</summary>
  Hessian spectra at trained models in deep learning exhibit a persistent pattern: eigenvalues organize into distinct clusters, including a large bulk near zero and a few isolated outliers. This paper shows that a natural account of these spectral phenomena emerges when the original setting is understood as a departure from a nearby, otherwise hidden, highly symmetric reference.   Modifications, including changes to the architecture, data distribution, or parameter metric, expose a nearby referenc...
  </details>

- **2026-10-07** — Yueying Li, Zhongle Xie, Ke Chen et al. — [QCATS: Query Context-Aware Transformer Slicing for Efficient Predictive Query Processing](http://arxiv.org/abs/2610.09894v1)
  <details><summary>📄 Abstract</summary>
  In-database predictive query processing increasingly applies Transformer-based models within relational pipelines. However, existing in-database inference typically exposes only tuple-level model inputs to the inference runtime, leaving relational predicates and metadata statistics invisible to neural execution planning. In this paper, we propose QCATS, a query context-aware transformer slicing framework that enables efficient sparse inference inside database systems. QCATS executes at query gra...
  </details>

- **2026-10-07** — Yifei Zhu, Yangyang Cai, Mingyi Shi et al. — [DynaConTalk: Wavelet-Constrained Diffusion for Long-Form and Controllable Holistic Co-Speech 3D Motion](http://arxiv.org/abs/2610.09846v1)
  <details><summary>📄 Abstract</summary>
  Holistic co-speech animation is prone to averaging in both motion representation and speech conditioning. In coordinate-space diffusion, slow body posture, mid-frequency gesture strokes, and fast hand or facial details are entangled in one prediction target, often producing low-variance, over-smoothed motion. Meanwhile, dense rhythmic and acoustic cues can dominate sparse content-specific information under fixed multimodal fusion. We present DynaConTalk, a wavelet-constrained diffusion framework...
  </details>

- **2026-10-07** — Philipp Strasberg — [Redundant Records of the Past: Unifying Quantum Darwinism and Decoherent Histories](http://arxiv.org/abs/2610.09845v1)
  <details><summary>📄 Abstract</summary>
  There exist two different paradigms for records in isolated quantum systems: decoherent histories (which determines which past events leave formal records) and quantum Darwinism (which determines which current events get redundantly recorded). Neither one implies the other, and connections between the two are scarcely investigated. We unify quantum Darwinism and decoherent histories based on the insight that only redundant records about past events matter. The resulting framework of past redunda...
  </details>

- **2026-10-07** — Sunjoo Whang, Jungjun Oh, Minsung Kim et al. — [Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches](http://arxiv.org/abs/2610.09827v1)
  <details><summary>📄 Abstract</summary>
  Long inputs and extended generation increase the storage and access costs of the key-value (KV) cache. Low-bit quantization reduces storage and memory traffic, while query-channel pruning can further reduce key-cache reads. Rotation-based quantization redistributes the energy of key outliers across channels. To maintain computational invariance, the same orthogonal transform must be applied to queries, preserving query-key dot products. However, this rotation can disperse query energy, weakening...
  </details>

- **2026-10-07** — Inbasekaran S — [EntroPrefill: Renyi-Guided Context Pruning with Conditional Stability Guarantees for Retrieval-Augmented Generation](http://arxiv.org/abs/2610.09757v1)
  <details><summary>📄 Abstract</summary>
  Mid-prefill pruning can reduce the sequence processed by deeper transformer layers, but attention concentration alone does not certify that discarded context is dispensable. We formulate EntroPrefill as a Renyi-guided proposal mechanism coupled to explicit constraints on discarded attention mass. Sink-isolated, regularized head pooling respects grouped-query attention while exposing a quantitative trade-off between specialization and worst-head coverage. We derive a mixture-to-head deletion enve...
  </details>

- **2026-10-07** — Tianle Wang, Jiayu Liu, Ruizhi Zhao et al. — [SAPD: Step-Aligned Privileged Distillation](http://arxiv.org/abs/2610.09665v1)
  <details><summary>📄 Abstract</summary>
  On-policy post-training can improve large language models by learning from their own trajectories, but requires costly rollout generation. We ask whether fixed demonstrations can support competitive off-policy learning through better supervision. Our premise is that their usefulness depends not only on the training trajectories, but also on whether supervision provides informative preferences among continuations and connects this guidance to the reasoning decision being learned. We introduce Ste...
  </details>

- **2026-10-07** — Zhifan Sun, Sebastian Gombert, Jannik Lossjew et al. — [Alice: A Large-Scale German Benchmark for Rubric-Based Multi-Dimensional Automatic Short Answer Scoring](http://arxiv.org/abs/2610.09661v1)
  <details><summary>📄 Abstract</summary>
  Automatic Short Answer Scoring (ASAS) is central to NLP for Education. However, openly available benchmarks remain scarce, and existing datasets largely address how well students answer a question directly rather than how well they master underlying concepts (knowledge elements) such as thermal energy or epistemic activities (skills) such as reasoning or claim.   To address this gap, we introduce Alice, a large-scale, rubric-based German ASAS dataset that is pedagogically aligned and comprises t...
  </details>

- **2026-10-07** — Samuel Tetteh, Cody Fleming — [It Is Not Seeing the Hazard: A Frozen Vision-Language Safety Score Measures Its Caption Bank](http://arxiv.org/abs/2610.09517v1)
  <details><summary>📄 Abstract</summary>
  Frozen vision-language models increasingly provide safety signals for reinforcement learning. Their use assumes that similarity to language describing danger indicates the hazard itself. Yet policy return and collision rate cannot reveal whether a score detects hazards or responds to correlated features of the scene. VLM-based methods have reported gains in driving and safe-RL benchmarks by converting image-text similarity into rewards, costs, or confidence weights. Such signals promise to reduc...
  </details>

- **2026-10-07** — Zihan Guo, Roxy He, Junwei Quan — [Before Bringing It Up: When and How AI Companions Should Use Memor](http://arxiv.org/abs/2610.09470v1)
  <details><summary>📄 Abstract</summary>
  Memory can sustain AI companionship, yet even accurate recollection can be inappropriate to use. Two rounds of formative interviews with 14 users (n = 6 exploratory, n = 8 memory-focused) motivate asking what a companion should consider before using past information. Eight themes inform Reconsider, a single-call procedure with five checks and four handling modes, evaluated on 80 scenarios across five models over 400 blinded within-model pairs. Two LLM judges favored Reconsider by net margins of ...
  </details>

- **2026-10-07** — Yeonseo Lee, Hyosup Shin, Guebin Hwang et al. — [TempoBridge: Language-Guided Tempo Control for Vision-Language-Action Policies](http://arxiv.org/abs/2610.09451v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models are effective at understanding what task to perform, but provide limited control over how it should be executed, such as moving quickly or slowly. We introduce TempoBridge, a lightweight framework that uses frozen VLA representations to modulate actions according to tempo cues in the instruction at each task phase, without additional tempo-conditioned robot demonstrations or tempo-specific base-policy fine-tuning. TempoBridge extracts tempo cues from contextua...
  </details>

- **2026-10-07** — Ling Li, Jianhui Zhong, Wei Liu et al. — [Spatial Latent Reasoning for Embodied Reference Understanding](http://arxiv.org/abs/2610.09418v1)
  <details><summary>📄 Abstract</summary>
  Pointing-gesture visual grounding requires connecting hand geometry with the visual identity and extent of a referred object. A central challenge for continuous latent reasoning is how to organize these complementary cues into useful intermediate supervision. We propose Spatial Latent Reasoning (SLR), a framework that structures this supervision around an ordered sequence of geometric and visual states. A spatial ray state is supervised by fingertip position and pointing direction, followed by f...
  </details>

- **2026-10-07** — Eunji Shin, Dahyun Choi, Seungyeon Jo et al. — [TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding](http://arxiv.org/abs/2610.09408v1)
  <details><summary>📄 Abstract</summary>
  Audio-visual multi-segment grounding (AV-MSG) in untrimmed videos, reasoning over audio-visual evidence and predicting multiple segments for a query, is a fundamental problem but remains challenging. Visual-only models overlook complementary acoustic cues, while audio-visual models often fail to calibrate the number of events - a phenomenon we refer to as count miscalibration. We present TiTok, an audio-visual large language model (AV-LLM) that localizes an arbitrary number of temporal event seg...
  </details>

- **2026-10-07** — Yihao Hu, Yanlin Feng, Naoki Otani et al. — [ARCS: Towards Precise Text-to-SQL via Structured Disambiguation](http://arxiv.org/abs/2610.09396v1)
  <details><summary>📄 Abstract</summary>
  As text-to-SQL systems move beyond demonstrations toward real-world deployment, ambiguity in user questions becomes a primary source of errors. Such ambiguities are often subtle, domain- or data-specific, and can silently cause system outputs to deviate from the user's true intent. Ambiguity is traditionally addressed through conversational clarification, which is often inefficient, cognitively demanding, and poorly aligned with real-world user workflows. We propose structured disambiguation, a ...
  </details>

- **2026-10-07** — Yizhi Song, Hang Ni, Weijia Zhang et al. — [DUDA-Bench: Benchmarking LLM Agents on Multimodal Data-Driven Urban Diagnosis](http://arxiv.org/abs/2610.09374v1)
  <details><summary>📄 Abstract</summary>
  Urban diagnosis integrates heterogeneous observations to identify urban problems, localize affected areas, and investigate contributing factors, informing evidence-based urban planning and management. However, its reliance on labor-intensive, case-specific expert workflows limits scalability and reuse, motivating the exploration of agent-based execution. To evaluate this capability, we introduce DUDA-Bench, a hierarchical and interactive benchmark that formalizes data-driven urban diagnosis as a...
  </details>

- **2026-10-07** — Bingxuan Li, Yiwen Song, Xueqing Wu et al. — [VIS-Ground: Video Interactive Storytelling with Contextual Grounding](http://arxiv.org/abs/2610.09326v1)
  <details><summary>📄 Abstract</summary>
  Video interactive storytelling enables viewers to actively steer how a video unfolds. However, once we allow viewers to intervene during generation, a new challenge arises: The viewer's request can have latent dependencies on both the grounding source and the current rendered video state. These dependencies may not be explicitly stated in any individual input, but emerge only when the source, rendered history, and new viewer intent are considered jointly. Existing interactive video generation sy...
  </details>

- **2026-10-07** — Zhiqin Yang, Chenxin Li, Xiaomeng Hu et al. — [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](http://arxiv.org/abs/2610.10409v1)
  <details><summary>📄 Abstract</summary>
  General-purpose agents increasingly write code, use tools, and complete complex digital tasks, raising the question of how far these capabilities carry into the physical world. To investigate this, we introduce RobotWorld, a challenging simulation testbed for robot use: turning instructions and observations into physical task execution through robot interfaces. Its 84 tasks span manipulation, mobile manipulation, locomotion, driving, and aerial control, with explicit interaction budgets and exec...
  </details>

- **2026-10-07** — Xin You, Zhiwei Ning, Zukai Chen et al. — [Self-correction Optimization for Interleaved Multimodal Generation](http://arxiv.org/abs/2610.10400v1)
  <details><summary>📄 Abstract</summary>
  Multimodal large language models (MLLMs) have made significant progress in visual understanding and generation. However, generating interleaved image--text content remains challenging, as it requires tightly integrated multimodal understanding and generation capabilities. Although existing MLLMs provide promising solutions, most rely on additional training with augmented data, which is computationally expensive and remains limited in preserving visual subjects, temporal consistency, and physical...
  </details>

- **2026-10-07** — Yifan Wu, Qin Li, Nan Min et al. — [OpenViTac: Learning and Benchmarking Visuo-Tactile Policies in a Unified Sim-and-Real Framework](http://arxiv.org/abs/2610.10384v1)
  <details><summary>📄 Abstract</summary>
  Tactile feedback provides embodied agents with physical information beyond visual observations, enabling more reliable interaction with the real world. However, despite the rapid progress of vision-tactile-language-action (VTLA) policies, there remains a lack of unified benchmarks for evaluating tactile-enabled robot manipulation across simulation and the real world. To address this gap, we introduce OpenViTac, a visuo-tactile manipulation benchmark for evaluating robot policies across simulatio...
  </details>

- **2026-10-07** — Yanjiang Guo, Haodong Yan, Zhide Zhong et al. — [Video Prediction Policy 2: Predict Better, Act Better](http://arxiv.org/abs/2610.10270v1)
  <details><summary>📄 Abstract</summary>
  World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their gen...
  </details>

- **2026-10-07** — Kamile Dementaviciute, Julija Vaitonyte, Tijl De Bie — [LLM Persuasion Is in the Eye of the Evaluation](http://arxiv.org/abs/2610.10232v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have already been shown to match or exceed human experts in persuasion. While their persuasive capabilities hold promise for beneficial uses such as education and health communication, they can also be used to manipulate and misinform, making their evaluation a growing priority for developers and regulators. That evaluation, however, remains fragmented: studies differ in what they treat as persuasion, and broad claims often rest on narrow, situation-specific assessme...
  </details>

- **2026-10-07** — Leon Mayer, Lucas Luttner, Patrick Godau et al. — [HeiCo-FOCUS: A Clinically Grounded Dataset for Long-Context Video Understanding](http://arxiv.org/abs/2610.10156v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in Vision-Language Models (VLMs) have led to rapid progress in video understanding across a wide range of benchmark tasks. However, existing evaluations largely focus on short-term reasoning, failing to assess a critical capability: maintaining cumulative temporal consistency over extended time horizons. To close this evaluation gap, we introduce HeiCo-FOCUS, a clinically grounded dataset for evaluating long-context video understanding through the task of Foreign Object Contextua...
  </details>

- **2026-10-07** — Mukul Dwivedi, Jesse Railo, Andreas Rupp — [A finite element exterior-to-interior reconstruction in the fractional conductivity inverse problem](http://arxiv.org/abs/2610.10484v1)
  <details><summary>📄 Abstract</summary>
  We develop a regularized finite element method for the fractional conductivity equation, recovering the conductivity on an exterior observation region from noisy Dirichlet-to-Neumann measurements and using this reconstruction to determine the interior conductivity. Mesh-localized inputs and mass-lumped Tikhonov regularization discretize the exterior determination principle of Covi--Railo--Zimmermann (2026, Calc. Var. PDE). We prove exterior \(L^2\)- and \(L^\infty\)-convergence with error estima...
  </details>

- **2026-10-07** — Duy-Cat Can, Mau Minh Phuc Le, Tuan-Khoa Hoang et al. — [MemoCare: An Interactive Multimodal Mobile System for Automated Cognitive Screening](http://arxiv.org/abs/2610.10448v1)
  <details><summary>📄 Abstract</summary>
  MemoCare is an interactive mobile system for automated multimodal cognitive screening. A React Native application combines spoken responses, temporal and spatial orientation, touchscreen actions, and visuoconstruction in complete English and Vietnamese workflows. Speech is transcribed by Google Speech-to-Text and scored locally with deterministic task-specific natural language processing rules; GPS coordinates are resolved by the MemoCare spatial module before answer matching; touch tasks are sc...
  </details>

- **2026-10-07** — Richard Cornelius Suwandi, Feng Yin, Kevin Murphy — [Kernel Autoresearch for Open-Ended Model Discovery](http://arxiv.org/abs/2610.10394v1)
  <details><summary>📄 Abstract</summary>
  Kernels encode the inductive bias of a wide range of machine learning models, yet automated kernel design faces a fundamental dilemma. A fixed grammar of base kernels and operators guarantees validity but limits the search to structures expressible by those building blocks. Conversely, unrestricted programs remove this limitation but no longer guarantee validity. In our stress tests, 22-58% of LLM-generated kernels that pass numerical checks on random inputs fail when evaluated at different scal...
  </details>

- **2026-10-07** — Yibei Guo, Rui Liu — [Input-Blind Controls Produce Substantial Oracle Headroom for Layer Programs in Multiple-Choice Evaluation](http://arxiv.org/abs/2610.10368v1)
  <details><summary>📄 Abstract</summary>
  Adaptive computation aims to improve language-model inference by tailoring execution to each input. For layer programs, oracle evaluations use known answers to estimate the potential gain from this flexibility, before a practical selector is available. However, a gain from selection does not by itself explain why the chosen programs help. This study examines this distinction using 32 layer-skipping and repetition programs on two models and 4,413 multiple-choice items. The analysis compares their...
  </details>

- **2026-10-07** — Eisuke Hirota, Aarav Sane, Rohan Paleja — [Temporally Interpretable Differentiable Decision Trees](http://arxiv.org/abs/2610.10367v1)
  <details><summary>📄 Abstract</summary>
  Interpretability offers a solution to safe autonomy by providing transparency into an agent's underlying decision-making model. Within sequential-decision making tasks, differentiable decision trees (DDTs) are one approach to such interpretability, maintaining automatic-differentiable policies while providing humans with a discrete tree-based visualization. Nonetheless, current implementations of DDTs are not well-suited for sequential-decision making domains, as there exists an inherent mismatc...
  </details>

- **2026-10-07** — Bo Li, Ankang Sun, Ruijie Wang — [Settling PROPm and PROPavg in Graphical Resource Allocation](http://arxiv.org/abs/2610.10336v1)
  <details><summary>📄 Abstract</summary>
  We study proportional fairness in graphical resource allocation, where agents are vertices, indivisible items are edges, and each item must be allocated to one of its two endpoints. It has been proved that PROP1 orientations always exist and PROPx orientations may not, but it has remained open whether the intermediate relaxations PROPm and PROPavg (both can be satisfied without graphical constraints) can always be satisfied. In this paper, we resolve this gap. We prove that PROPm orientations al...
  </details>

- **2026-10-07** — Mihai Bogdan Deaconu, Ioan Daniel Pop — [HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting](http://arxiv.org/abs/2610.10323v1)
  <details><summary>📄 Abstract</summary>
  Short-horizon realized volatility forecasting requires the integration of market information that evolves at incompatible temporal resolutions, from second-level order book dynamics to weekly regime drift. Our conference work introduced HAN-T, a hierarchical architecture in which scale-specific Transformer encoders process short, mid, and long-horizon streams and a learned attention fuser weighs their contributions. This article replaces the quadratic attention encoders with selective state spac...
  </details>

- **2026-10-07** — Eduardo Santos-Escriche, Valerie Engelmayer, Ya-Wei Eileen Lin et al. — [How Do Transformers Learn to Represent Symmetries?](http://arxiv.org/abs/2610.10305v1)
  <details><summary>📄 Abstract</summary>
  Training Transformer-based architectures with finite data augmentation has become an increasingly popular approach in geometric machine learning. Despite its empirical success, the interplay between the Transformer architecture, invariance to different symmetries, and augmentation budgets remains underexplored. In this paper, we study the ability of a vanilla Transformer to learn various symmetries through finite data augmentation for point cloud datasets. We identify an ordering of increasing l...
  </details>

- **2026-10-07** — Mingyan Liu, Min Huang — [SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning](http://arxiv.org/abs/2610.10304v1)
  <details><summary>📄 Abstract</summary>
  We study whether latent sequence compression of prompt prefixes preserves the capabilities that large language models rely on during inference. We introduce SemanticFold, a compression scheme that folds prefix hidden states at learned boundaries, and evaluate it across five model scales: Qwen3-1.7B, Qwen3-8B, SmolLM2-1.7B, Pythia-1.4B, and Pythia-6.9B. We use a fixed-target protocol: a frozen prefix is executed natively or compressed, and both arms teacher-force identical continuation tokens. Th...
  </details>

- **2026-10-07** — Junhyeok Kim, Jinyeong Kim, Jae Wan Park et al. — [On the Necessity of Attention-FFN Split in Vision Transformers](http://arxiv.org/abs/2610.10303v1)
  <details><summary>📄 Abstract</summary>
  The standard Transformer architecture relies on a rigid pattern that alternates Attention and Feed-Forward Network (FFN) layers. Despite its widespread adoption, the inductive bias imposed by this strict separation has not been systematically examined. In this work, we investigate the necessity of the Attention-FFN dichotomy in Vision Transformers (ViTs). To facilitate this analysis, we introduce the AttenFeed module, a unified component that integrates the functional properties of both Attentio...
  </details>

- **2026-10-07** — Tommaso Marzi, Ahmed Hendawy, Jan Peters et al. — [Continual Graph Multi-Agent Reinforcement Learning](http://arxiv.org/abs/2610.10302v1)
  <details><summary>📄 Abstract</summary>
  In Continual Multi-Agent Reinforcement Learning (CMARL), agents learn cooperative policies across sequences of tasks, aiming to adapt effectively to new tasks while preserving the ability to solve previously encountered ones. In many applications, tasks differ in their underlying structure, which can represent, for example, distinct operational conditions or target configurations (e.g., different network topologies in power grids or arrangements in formation control). Existing CMARL methods lack...
  </details>

- **2026-10-07** — Yue Qiu, Zekang Du, Yiqun Diao et al. — [From Prompts to Trees: Effective LLM-Guided Tree Generation for Few-Shot Tabular Classification](http://arxiv.org/abs/2610.10227v1)
  <details><summary>📄 Abstract</summary>
  While Large Language Models (LLMs) possess rich world knowledge and impressive generalization capabilities, their direct application to tabular data classification is hindered by high inference costs and limited interpretability. In contrast, decision trees are fast and transparent but often underperform in low-data regimes. In this work, we propose a novel framework that bridges these paradigms by distilling LLM knowledge into interpretable decision trees under a few-shot learning setting. Inst...
  </details>

- **2026-10-07** — Stepan Zharkov, Krish Singal, Ashwin Padaki et al. — [Attention via Black-Box Vector Search](http://arxiv.org/abs/2610.10135v1)
  <details><summary>📄 Abstract</summary>
  Sparse attention mechanisms estimate attention over $n$ tokens using a small subset of keys. Many existing approaches use maximum inner product search (MIPS) to retrieve the heaviest keys, which motivates the following question: given black-box access to a MIPS oracle, how many keys must be retrieved to output an $\varepsilon$-accurate attention estimate?   We answer this question by unifying prior approaches through the framework of priority sampling. With a single MIPS index, we show that $Θ(\...
  </details>

- **2026-10-07** — Xiaoran Liu, Ziwei He, Xipeng Qiu — [Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position](http://arxiv.org/abs/2610.10114v1)
  <details><summary>📄 Abstract</summary>
  The architectural design of Large Language Models (LLMs) is shifting from traditional full-attention-only models to hybrid models, which combine different attention modules to improve long-context efficiency and performance in length extrapolation and context extension. To explain why hybrid models work and how to design them better, we propose Mechanics of Long-Context Hybrid Models. As Part 1.1 of this series, we begin with hybrids of full attention and either sliding-window attention (SWA) or...
  </details>

- **2026-10-07** — Peter Baile Chen, Geoffrey X. Yu, Xinming Liu et al. — [ExperienceIndex: Artifact-Grounded Memory](http://arxiv.org/abs/2610.10091v1)
  <details><summary>📄 Abstract</summary>
  Knowledge-intensive tasks require answering many questions by reasoning about a shared corpus of artifacts (e.g., court cases, or scientific literature). As humans interact with these corpora, they naturally accumulate experiential knowledge about artifacts, enabling them to quickly identify the complete set of relevant artifacts for each new task. However, existing AI agents lack appropriate memory solutions to build or reuse such artifact-grounded experience, leading to lower answer quality an...
  </details>

- **2026-10-07** — Efe Çangırılı, Murat Kurt — [TRACK: Telemetry-Based Racing Analysis and Coaching Kit in Sim Racing Games](http://arxiv.org/abs/2610.10061v1)
  <details><summary>📄 Abstract</summary>
  This paper presents TRACK (Telemetry-Based Racing Analysis and Coaching Kit), which is a framework for analyzing driving performance in sim racing and profiling how individual drivers behave behind the wheel. We report this framework together with its limitations: we calibrate each clustering result against a null, and when one does not separate from chance, we say so. Instead of restricting ourselves to scoring drivers or sorting them into preset labels, we represent each recording session as a...
  </details>

- **2026-10-07** — Pujian Mao — [Geometric interpretation of electromagnetic memory and large gauge transformation](http://arxiv.org/abs/2610.09960v1)
  <details><summary>📄 Abstract</summary>
  We develop a geometric characterization of electromagnetic memory in terms of the optical data of charged-particle congruences. We derive the worldline deviation of charged particles near null infinity for both massless and massive particles and construct the corresponding optical data. We show that the asymptotic shear of the charged-particle congruence provides an equivalent encoding of electromagnetic memory and its associated large gauge transformation. This establishes a geometric interpret...
  </details>

- **2026-10-07** — Paul W. Goldberg, Isaac Robinson, Nicholas Teh — [Minimizing Cumulative Envy in Allocating a Sequence of Items](http://arxiv.org/abs/2610.09843v1)
  <details><summary>📄 Abstract</summary>
  We study temporal fair division with indivisible goods that arrive sequentially and must be allocated irrevocably. In contrast to the usual online model, we assume that valuations and future arrivals are known in advance, and ask how unfairness evolves during the process. We introduce \emph{cumulative maximum envy}: the sum, over all rounds, of the maximum pairwise envy at that round. Equivalently, this is the area under the worst-envy curve, and it captures both the magnitude and the duration o...
  </details>

- **2026-10-07** — Francesco Cambria, Francesco Invernici, Andrea Colombo et al. — [Empowering Users in Graph Rule Mining via Large Language Models](http://arxiv.org/abs/2610.09842v1)
  <details><summary>📄 Abstract</summary>
  In the era of interconnected data, graphs have emerged as an effective abstraction for modeling complex systems in an intuitive format, especially with the rise of Property Graphs, which offer an intuitive and scalable way of navigating non-intuitive structures. In this context, graph mining techniques have been developed for testing complex graph-based rules, as the MINE GRAPH RULE operator, which, however, require users to have prior expertise both in graph theory and formal query language. In...
  </details>

- **2026-10-07** — Raneem Mahajne, Toviah Moldwin — [Fully Interpretable Minimal Transformers: From Geometry to Algorithm](http://arxiv.org/abs/2610.09838v1)
  <details><summary>📄 Abstract</summary>
  We present a framework for building and interpreting minimal transformer models. By constraining a transformer's embedding dimension and head size to 2, we enable full two-dimensional visualization of its internal representations. Embeddings, query/key/value transforms, attention outputs, residual streams, and decision boundaries can all be seen directly. Our central claim is that the learned geometry implies an algorithm; the arrangement of points and boundaries in R^2 can be read as a step-by-...
  </details>

- **2026-10-07** — Deyuan Liu, Yihao Hu, Jingxuan Zhang et al. — [UltraText Bench: A Comprehensive Bilingual Benchmark for Evaluating Visual Text Rendering in Image Generation](http://arxiv.org/abs/2610.09823v1)
  <details><summary>📄 Abstract</summary>
  Dense visual text requires image generators to reproduce long strings across multiple regions with correct placement and legibility. As short-string rendering improves, evaluation must test sustained performance across more demanding scenes. We introduce UltraText Bench, a bilingual benchmark for prompt-only generation of dense visual text. It contains 432 prompts spanning 24 real-world scene categories and three difficulty levels, split equally between English and Chinese. Each human-reviewed p...
  </details>

- **2026-10-07** — Mingqing Yuan, Xiaobo Liang, Junwei Yang et al. — [Judging in Latent Space: Efficient Generative Reward Modeling via Semantics-Preserving Compression](http://arxiv.org/abs/2610.09788v1)
  <details><summary>📄 Abstract</summary>
  Reward modeling often requires jointly representing and reasoning over multiple evaluation criteria, yet verbalizing this process token by token can incur substantial inference cost. Recent work on latent reasoning suggests that continuous states may support this computation more compactly. We introduce LatentGRM, a latent evaluation framework built on semantic chunking, compression, and reconstruction. By using the structure of rubric-guided evaluations to guide compression, LatentGRM learns co...
  </details>

- **2026-10-07** — Faissal Izermine, Hanru Bai, Oscar Davis et al. — [Unrolled Flow Models for Reasoning](http://arxiv.org/abs/2610.09759v1)
  <details><summary>📄 Abstract</summary>
  Flow matching enables language generation in few steps, but whether additional integration steps improve reasoning remains unclear. We prove that a flow parameterized by a two-layer Transformer can solve graph reachability, with the required number of integration steps increasing with the target's distance from the root. Yet, standard flow language models can fail to benefit from additional steps on reasoning tasks. We attribute this limitation to objectives that supervise each time point indepe...
  </details>

- **2026-10-07** — Ahmad Abbas, Tamara Fakih, Nour Fakih et al. — [Shaer: Controlled Arabic Poetry Generation with Meter Subform and Semantic Conditioning](http://arxiv.org/abs/2610.09756v1)
  <details><summary>📄 Abstract</summary>
  Classical Arabic poetry generation requires simultaneously satisfying semantic, linguistic, and fine-grained prosodic constraints. Existing systems typically control broad poetic attributes but do not jointly model semantic intent, meter subform, and poem length. We present Shaer, a controllable Classical Arabic poetry generation framework jointly conditioned on natural-language descriptions, meter subforms, and target hemistich counts. To support this task, we construct an enriched corpus of 11...
  </details>

- **2026-10-07** — Jacobus Arthur, Ahmad Sait, Batool Hani et al. — [SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos](http://arxiv.org/abs/2610.09742v1)
  <details><summary>📄 Abstract</summary>
  Refereeing decisions in professional soccer remain inconsistent because referees cannot easily compare a contentious foul against similar past cases. We cast this as a retrieval problem and introduce SoccerNet-FoulRet, the first benchmark for semantic foul retrieval. Given a query foul, the task is to retrieve past fouls judged to be relevant precedents, regardless of camera angle, teams, or appearance. This differs from prior video-to-video retrieval, which matches clips by visual similarity or...
  </details>

- **2026-10-07** — Bahadır Yüzbaşı — [The Lambert Penalty: Logarithmic Shrinkage for Sparse Regression](http://arxiv.org/abs/2610.09627v1)
  <details><summary>📄 Abstract</summary>
  Sparse regression must balance prediction accuracy with reproducible variable selection. We introduce the Lambert penalty by limiting how quickly the retained fraction of a scalar score increases after variable entry. Maximizing retention under this scale-equivariant constraint yields a logarithmic transition from exact zero to an identity tail. The bounded penalty has a fixed shape and a single penalty parameter selected by training-only five-fold cross-validation. We derive an explicit scalar ...
  </details>

- **2026-10-07** — HyeonSeok Lim, SeungWoo Song, Inho Won et al. — [Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning](http://arxiv.org/abs/2610.09607v1)
  <details><summary>📄 Abstract</summary>
  Skeleton-based reasoning prompting is a promising training-free approach for structuring LLM reasoning, but prior work largely assumes an English-centric setting. We propose the Language-Aware Skeleton Exploration Framework (LASEF) to study skeleton-language choice in multilingual mathematical reasoning. Across math benchmarks, model scales, and languages, we show that English skeletons yield a small positive tendency on average, most visible for smaller models and low-resource languages. Howeve...
  </details>

- **2026-10-07** — Zicheng Hu, Zhijian Zhou, Xuan Zhang et al. — [COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning](http://arxiv.org/abs/2610.09597v1)
  <details><summary>📄 Abstract</summary>
  Asynchronous RL accelerates large language model post-training by decoupling rollout generation from optimization, but trains on stale trajectories. Existing methods primarily correct token-level policy mismatch through importance-ratio control in the actor objective. We show that this \emph{policy-side correction} alone is insufficient: advantage estimates also inherit mismatch from behavior-policy continuations, which we term \emph{advantage staleness}. We derive exact bias and variance decomp...
  </details>

- **2026-10-07** — Daniel Paulin, Ádám Jung, András A. Benczúr — [Scalable Logistic Gaussian Process Density Regression with Kinetic Langevin Sampling](http://arxiv.org/abs/2610.09591v1)
  <details><summary>📄 Abstract</summary>
  Conditional density estimation targets the full distribution of a response given covariates, as required, for example, for per-galaxy photometric redshifts. We develop a scalable Bayesian estimator based on the logistic Gaussian process. The log conditional density has a separable covariance: a Matérn kernel along the response, represented in a truncated Fourier basis on a circle, and a covariate kernel represented by Nyström features, which accommodate non-stationary kernels with input-dependen...
  </details>

- **2026-10-07** — Lin Wu, Zhe Xu, Hongyi Wang et al. — [Dual- versus Single-Suggestion AI Support for Radiographic Interpretation in Residents: Randomized Multireader Study](http://arxiv.org/abs/2610.09589v1)
  <details><summary>📄 Abstract</summary>
  Purpose: To compare dual- and single-suggestion AI support for radiographic interpretation by residents, particularly when the shared AI suggestion was incorrect.   Materials and Methods: This prospective, multicenter, randomized three-arm reader study was conducted at three hospitals in China from July to September 2026 (ChiCTR2600129243). After specialty stratification, 132 residents with fewer than 3 years of clinical experience were randomized 1:1:1 to GPT-5.4 alone (group A), GPT-5.4 plus K...
  </details>

- **2026-10-07** — Taehyeon Yun, Dongho Kim, Geonwoo Kim et al. — [Correct Answers, Unsupported Findings: Evidence Binding in Forensic Reconstruction of LLM Agent Logs](http://arxiv.org/abs/2610.09581v1)
  <details><summary>📄 Abstract</summary>
  Forensic reconstruction of LLM-agent actions requires not only recovering the correct value, but establishing which preserved record supports that finding. Tool logs, generated explanations, and local citation identifiers capture different parts of this evidence, yet a citation identifier does not establish a source unless its binding to a record is preserved. We audit this distinction using 64 mechanically checkable cases from saved AgentDojo Banking executions. Two LLM readers reconstruct sour...
  </details>

- **2026-10-07** — Jongwook Yoon, Jongwon Lim, Sungjib Lim et al. — [How Do LLMs Change Predictions Under Negation?](http://arxiv.org/abs/2610.09571v1)
  <details><summary>📄 Abstract</summary>
  Negation is an essential feature of human language, yet large language models (LLMs) remain unreliable in processing it. We evaluate recent open-source and closed-source LLMs on our negation benchmark and find that, in 37-71% of cases, they repeat the same answer under negation (e.g., "Madrid" for "What is not the capital of Spain?"). To understand and address this brittleness, we mechanistically examine how models operate under negation. Our main finding is that specialized attention heads and ...
  </details>

- **2026-10-07** — Juuso Jaakola, Vlad Stirbu, Teiko Heinosaari — [Using Learning Analytics to Study Novice Learners' Work on Quantum Circuit Simulator Tasks](http://arxiv.org/abs/2610.09499v1)
  <details><summary>📄 Abstract</summary>
  Interactive quantum circuit simulators are increasingly used to support introductory quantum computing education for learners from varied disciplinary backgrounds. These environments can also generate detailed response logs of submitted circuits, but such data are rarely transformed into evidence that instructors can use for course redesign and development.   We present a learning analytics framework for quantum circuit simulator tasks and report its task-level branch on anonymised logs from an ...
  </details>

- **2026-10-07** — Minu Kim, Jihwan Lee, David R. Mortensen et al. — [Mitigating Accent-Language Confusion in Self-Supervised Speech Representations for Language Identification](http://arxiv.org/abs/2610.09486v1)
  <details><summary>📄 Abstract</summary>
  Spoken language identification (LID) aims to recognize the target language regardless of accent. In practice, however, LID models fine-tuned from self-supervised speech representations frequently confuse accents with languages, misclassifying non-native (L2) speech as the speaker's first language (L1). We show that non-native speech representations lie between native target-language and native L1 poles, causing systematic misclassification. To address this, we introduce a geometric projection th...
  </details>

- **2026-10-07** — Jeonghwan Kim, Sofia Stoica, Jiwan Chung et al. — [Mixture of Layers: Dynamic Layer Routing for Visual Reasoning](http://arxiv.org/abs/2610.09440v1)
  <details><summary>📄 Abstract</summary>
  Pre-trained vision encoders contain layer-wise visual representations that differ in spatial granularity, semantic abstraction, and sensitivity to local details. However, most Multimodal Large Language Models (MLLMs) rely on only the final or penultimate vision encoder representations or fixed aggregation rules, making visual abstraction largely query-agnostic and limiting access to fine-grained cues such as small objects, spatial details, text, and subtle visual attributes. In this work, we pro...
  </details>

- **2026-10-07** — William Y. C. Chen, Elena L. Wang — [The Higher-order Stirling Triangles](http://arxiv.org/abs/2610.09362v1)
  <details><summary>📄 Abstract</summary>
  The $r$th-order Stirling cycle and subset triangles and their associated quasi-Eulerian triangles were introduced by Deb and Sokal in their study of total positivity of combinatorial triangles. They found combinatorial interpretations for the cycle case in terms of Stirling permutations, leaving the subset case open. For $r\ge 2$, we resolve this problem by introducing the notion of Stirling subset permutations along with a consecutive-descent statistic. We also prove the conjectures of Deb and ...
  </details>

- **2026-10-07** — Zengyi Yang, Shuai Yuan, Zhong-Cheng Wu et al. — [CRT-HMAR: Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation for Open-Task-Aware Infrared-Visible Image Fusion](http://arxiv.org/abs/2610.09330v1)
  <details><summary>📄 Abstract</summary>
  Infrared and visible (IR-VIS) image fusion integrates complementary multimodal information into a single fused image to support downstream vision tasks. However, existing methods are typically tailored to seen tasks within a fixed task set and struggle to generalize to unseen tasks, which restricts their applicability in real-world open-task scenarios. To address this issue, this paper proposes CRT-HMAR, a Causal Requirement Tracing-Guided Hierarchical Multi-Agent Regulation Framework for open-t...
  </details>

- **2026-10-07** — Baoteng Li, Wenzhuo Wu, Kongming Liang et al. — [Visual Jev Rewards: Reference-Bound Verification for Multi-Subject Image Generation](http://arxiv.org/abs/2610.09328v1)
  <details><summary>📄 Abstract</summary>
  Multi-subject image generation requires rewards that verify whether requested attributes, actions, and relations hold for the specified reference subjects. Subject presence alone does not establish that the correct subjects participate in a requested interaction. We present reference-bound Visual Jev rewards that turn these visual decisions into generator training signals. Each subject-related question receives a positive label only when the requested condition and the relevant reference identit...
  </details>

- **2026-10-07** — Weitian Wang, Shubham Rai, Cecilia De La Parra et al. — [Hardware-aware Calibrated Clustered Attention for Efficient Visual Geometric Transformers](http://arxiv.org/abs/2610.09274v1)
  <details><summary>📄 Abstract</summary>
  The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers with extremely long sequences that causes a significant latency bottleneck. In this paper, we propose blockwise clustered attention (BC attention) to accelerate the global attention laye...
  </details>

- **2026-10-07** — Xinzhu Wang, Tanzy Love — [Bayesian Optimization for Dose Finding with Two Agents: Participant Allocation and Final Selection](http://arxiv.org/abs/2610.09245v1)
  <details><summary>📄 Abstract</summary>
  In two-agent dose-finding trials, the next cohort should help identify a combination for final selection. We studied a constrained knowledge-gradient (cKG) rule with one-cohort lookahead that updates independent Gaussian-process models of efficacy and continuous toxicity, reapplies a probability criterion for mean toxicity, and evaluates the resulting selection. We derived a deterministic calculation over a fixed set of dose combinations, holding fitted model parameters fixed during each hypothe...
  </details>

- **2026-10-06** — Kimia Kazemian, Menghan Xu, John Thickstun et al. — [Spatial Induction Heads: In-Context Learning of Multidimensional Cellular Automata](http://arxiv.org/abs/2610.09124v1)
  <details><summary>📄 Abstract</summary>
  Induction heads provide a mechanistic account of in-context learning in sequential data, but existing theory largely assumes that the context relevant to a prediction forms a contiguous block. In multidimensional data, serialization breaks this assumption by scattering spatial neighbors across distant positions in the token sequence. We study how transformers overcome this routing problem in multidimensional stochastic and deterministic cellular automata, where each trajectory is generated by an...
  </details>

- **2026-10-06** — Brandon Ho, Nikola Rogers, Seung-Kyum Choi — [Shared-Roadmap Generation and Evaluator for Multi-Agent Path Planning Using Heterogeneous Graph Neural Network](http://arxiv.org/abs/2610.09034v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent path planning (MAPP) in continuous environments often relies on roadmaps to balance safety and search efficiency. However, traditional roadmap generation methods, such as lattice grids or standard sampling-based approaches, frequently face a trade-off between graph density and the likelihood of finding feasible, high-quality solutions. In this paper, we propose a scalable heterogeneous Graph Neural Network (GNN) framework for the automated generation and evaluation of shared multi-ag...
  </details>

- **2026-10-06** — Samrajya Thapa, Daniel J. Quest, Timothy L. Kline et al. — [Beyond Explanation: Debugging Medical Imaging Models via Concept Intervention](http://arxiv.org/abs/2610.09031v1)
  <details><summary>📄 Abstract</summary>
  Medical imaging models often operate as black boxes, limiting interpretability and systematic debugging. We introduce an easy-to-use, plug-and-play framework for concept-based interpretation and model refinement. By aligning a single-modality encoder to BioMedCLIP, we construct a Concept Bottleneck Model (CBM) that enables concept-level interventions. These interventions allow us to isolate causal versus spuriously correlated concepts, validate insights with domain experts, and generate counterf...
  </details>

- **2026-10-06** — Panagiotis Kasnesis, Christos Chatzigeorgiou, Lazaros Toumanidis et al. — [Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Language Models in a Deployed Agentic Home-Automation System](http://arxiv.org/abs/2610.09021v1)
  <details><summary>📄 Abstract</summary>
  An agentic system issues several structurally different kinds of LLM calls. It routes intent, classifies actions, grounds language in a device registry, plans multi-agent pipelines and writes the Python code those pipelines run. The difficulty of these call sites varies by an order of magnitude, yet in practice a single model, chosen for the hardest site, serves all of them. In this work, we evaluate 9 models from 0.8B to a frontier hosted model across the five call sites of a deployed open-sour...
  </details>

- **2026-10-06** — Muhammad Zeeshan Karamat, Christiana Chamon Garcia — [How Fragile Is On-Device Language Model Safety? Localizing Safety-Critical Parameters for Sparse Fault Analysis](http://arxiv.org/abs/2610.09000v1)
  <details><summary>📄 Abstract</summary>
  As small language models (SLMs) are increasingly deployed on resource-constrained and on-device platforms, including as components of agentic systems, the integrity of locally stored model parameters becomes an important safety concern. We investigate whether safety-sensitive behavior in LLaMA-2-7B-Chat is concentrated within a sparse subset of parameters, creating a reduced fault surface for targeted analysis. We study two complementary localization methods: low-rank safety-associated subspace ...
  </details>

- **2026-10-06** — Fang Li, Jiraphon Yenphraphai, Quentin Herau et al. — [S2Tok: Streaming 3D Gaussian Reconstruction with Persistent Spatial Tokens](http://arxiv.org/abs/2610.08978v1)
  <details><summary>📄 Abstract</summary>
  Streaming 3D reconstruction requires more than a sequence of geometric predictions: it requires a persistent scene state that can incorporate new evidence and remain renderable as observations arrive. Latent spatial tokens offer a promising representation for this purpose, but constructing them from an image collection leaves open how to maintain them online, where each observation may both revisit known regions and reveal new content. We introduce S2Tok, a feed-forward framework that maintains ...
  </details>

- **2026-10-06** — Yunheng Liu, Ziqi Cai, Siqi Yang et al. — [SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation](http://arxiv.org/abs/2610.08941v1)
  <details><summary>📄 Abstract</summary>
  Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent training. Existing panoramic generators follow predefined trajectories, and interactive world models act through low-level actions in perspective views. We propose SPW-Nav, a streaming panoramic world model that understands movement instructions and streams one minute of 2K 360-degree video in real time from a single panora...
  </details>

- **2026-10-06** — Liao Ma, Jiayi Song, Yunfeng Wu et al. — [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](http://arxiv.org/abs/2610.08772v2)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible...
  </details>

- **2026-10-06** — Leon Goldberg, Gal Engelberg — [Contextualization of Third-Party Cloud Security Findings](http://arxiv.org/abs/2610.08895v1)
  <details><summary>📄 Abstract</summary>
  Finding severity is the main driver of how security teams prioritize remediation. For third-party cloud security findings, that severity is static: the rule that raised the finding assigns it before the rule meets any environment, so it reflects the risk of the condition in general rather than the risk the finding poses to the concrete environment where it lives. Scoring standards define where environment-specific context belongs. How far that context changes finding severities in production, wh...
  </details>

- **2026-10-06** — Marcel Crasmaru — [CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution](http://arxiv.org/abs/2610.08592v2)
  <details><summary>📄 Abstract</summary>
  CNet is a C++/CUDA framework for building deep complex-valued neural networks (CVNNs) and optimizing complex functions by gradient descent with Wirtinger derivatives. Complex models are underexplored yet natural where data is intrinsically complex -- RF/IQ communications, MRI k-space, radar/SAR, audio spectra -- and phase carries information real networks discard. CNet is physics-native: a network is a cascade of complex (often unitary) operations on an amplitude vector, and classification is a ...
  </details>

- **2026-10-06** — Maryam Baizhigitova, Andrew Seohwan Yu, Po-Hao Chen et al. — [Knee3DVLM: Dual-Sequence Full-Volume Vision-Language Modeling for Comprehensive Knee MRI Assessment](http://arxiv.org/abs/2610.08482v2)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly being applied to three-dimensional medical imaging, but their application to knee MRI remains limited, particularly for interpreting the complementary sequences used in clinical practice. We introduce Knee3DVLM, a sequence-aware VLM that uses full-volume DESS and fluid-sensitive TSE MRI to predict 57 anatomically resolved binary diagnostic targets derived from the MRI Osteoarthritis Knee Score (MOAKS) for structured reporting. We evaluated DESS-only...
  </details>

- **2026-10-06** — Rongcun Wang, Shi Chen — [RAPO-Sol: Retrieval-Augmented Preference Optimization for Repository-Level Solidity Code Generation](http://arxiv.org/abs/2610.08429v2)
  <details><summary>📄 Abstract</summary>
  Smart contracts written in Solidity manage assets, permissions, and irreversible state changes, making code generation both useful and security-critical. Repository-level Solidity generation is challenging because models must synthesize complete contracts or libraries while preserving consistency across state variables, modifiers, events, inheritance, external calls, and access-control logic. We present RAPO-Sol, a two-stage training framework for repository-level Solidity code generation. First...
  </details>

- **2026-10-06** — Hanwen Li, Jinhao Duan, Guanhua Zhu et al. — [From Uncertainty to Action: Learning to Steer LLM Agents](http://arxiv.org/abs/2610.09115v1)
  <details><summary>📄 Abstract</summary>
  Steering an LLM agent means deciding whether to correct it, at which step, and with which mechanism. Uncertainty is often used to decide when to correct an agent, but whether it can guide these decisions remains unclear. We steer agent trajectories separately at every non-terminal step with each of four mechanisms and run each continuation to completion. The resulting stepwise outcome table (SOT) holds about 82,000 counterfactual continuations of 1,864 trajectories from three benchmarks and two ...
  </details>

- **2026-10-06** — Avyay M. Casheekar, Hariganesh Tangirala — [Learning to Report Unsafe Tasks in a Multi-Agent Game](http://arxiv.org/abs/2610.09002v1)
  <details><summary>📄 Abstract</summary>
  When agents share a reward for completed tasks, reporting unsafe work can reduce the reporter's reward by stopping a task. Audits can make reporting optimal without ensuring that further training teaches a silent team to report. We study this learning problem in a game where any witness can stop a task by reporting. With $k$ witnesses per task sharing a policy and drawing independently, the expected-reward derivative with respect to their shared silence probability counts each task's benefit $k$...
  </details>

- **2026-10-06** — Wenqing Tian, Zeyu Zhang, Zhaocheng Liu et al. — [PhysEvo: Astra Can Act, Let It](http://arxiv.org/abs/2610.08995v1)
  <details><summary>📄 Abstract</summary>
  Astra can act, yet reliable manipulation depends on the system through which it observes and controls the world. We introduce PhysEvo, a framework for physical recursive self-improvement (RSI) around a single frozen model. A task agent executes robot tasks; a meta-agent uses the resulting trajectories to diagnose failures, revise tools and skills, and test corrections. The meta-agent can also improve its own diagnostic tools, so retained revisions support both later action and later self-improve...
  </details>

- **2026-10-06** — Wenqi Li, Mindi Ruan, Chuanbo Hu et al. — [A Deterministic Evidence Layer for Vision-Language Autism Screening from Naturalistic Home Video](http://arxiv.org/abs/2610.09217v1)
  <details><summary>📄 Abstract</summary>
  Autism spectrum disorder (ASD) is diagnosed through specialist observation of a child's social behavior, and access to that expertise is the bottleneck for early identification. Vision-language models (VLMs) describe a child's behavior from video well; the verdict drawn from the description is unstable: at temperature~0, across eight pipeline configurations on one backbone, 16--37\% of clips change their predicted label between repeated runs, and the cause lies in the serving stack. We keep the ...
  </details>

- **2026-10-06** — Guanhua Ding, Zi Wang, Ruichao Li et al. — [CurveTQ: Rotation-Free Trellis Quantization of LLM Weights via Curvature-Weighted Search](http://arxiv.org/abs/2610.09212v1)
  <details><summary>📄 Abstract</summary>
  The best two-bit weight quantizers for large language models, such as QTIP and Proteus, rotate each weight matrix by a random orthogonal transform, which must be undone at every decoding step, then encode it with a trellis or lattice code under a Euclidean search; the layer Hessian enters only through error feedback between coding blocks. We show that this leaves part of the Hessian unused. Error feedback turns the loss into a weighted sum of per-coordinate rounding errors whose weights, the dia...
  </details>

- **2026-10-06** — Kai Yi, Tarek Elgamal, Sruthikesh Surineni et al. — [Few Bits, One Law: Toward W2A4KV2](http://arxiv.org/abs/2610.09202v1)
  <details><summary>📄 Abstract</summary>
  Extreme low-bit LLM compression is most challenging when weights, activations, and KV caches are quantized together: their distributions differ, and quantization errors interact throughout the network. We introduce CanonQ, a unified quantization-aware training framework that addresses these challenges by separating source canonicalization from task-aware adaptation. Fixed rotations and energy normalization map heterogeneous tensor sources to canonical coordinates, enabling frozen Gaussian-refere...
  </details>

- **2026-10-06** — Tao Chen, Dihui Wang, Puqing Jiang — [Physics-Derived Natural Coordinates for Fast Uncertainty Propagation in Multilayer Thermoreflectance](http://arxiv.org/abs/2610.09192v1)
  <details><summary>📄 Abstract</summary>
  Uncertainty quantification in thermoreflectance measurements of multilayer structures is challenging because thermophysical-property extraction involves nonlinear inverse problems with strongly coupled parameters. Covariance-based analytical propagation is efficient but assumes local linearity and approximately Gaussian fitted variables, whereas Monte Carlo (MC) propagation captures non-Gaussian behavior but is computationally expensive and can be unreliable when simultaneously fitting parameter...
  </details>

- **2026-10-06** — Kean Fallon, Joseph W. Iverson — [Conference signals: Applications, existence, and constructions](http://arxiv.org/abs/2610.09169v1)
  <details><summary>📄 Abstract</summary>
  A conference signal is a complex-valued function on a finite abelian group that vanishes at 0 in both the time and frequency domains, and is otherwise flat in both domains. For example, the Legendre symbol is a conference signal on $\mathbb{Z}_p$ since it vanishes at $0$, takes values $\pm 1$ away from zero, and is a scalar multiple of its Fourier transform. More generally, any nontrivial multiplicative character on a finite field is a conference signal on its additive group.   Until now, confer...
  </details>

- **2026-10-06** — Tworit Dash, Alexander Yarovoy — [Fast Whittle Maximum-Likelihood Parametric Spectrum Estimation for Weather-Radar Doppler Moments](http://arxiv.org/abs/2610.09161v1)
  <details><summary>📄 Abstract</summary>
  The computational cost of Whittle maximum-likelihood parametric spectrum estimation (PSE) for short-dwell weather-radar Doppler moment retrieval is addressed. PSE can reduce finite-sample bias, especially for short coherent processing intervals and broad spectra, but repeated likelihood evaluations make direct use expensive. A fast implementation of the finite-sample Gaussian Doppler model is introduced by writing the likelihood in terms of closed-form autocorrelation lags and synthesizing the m...
  </details>

- **2026-10-06** — Yikuan Li, Pinyan Lu, Fanghui Liu — [Are Parameter-Efficient Fine-tuning Methods Really Different?](http://arxiv.org/abs/2610.09122v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) offers many parameterizations, yet their methodological and functional differences remain unclear. We compare six methods in language and diffusion models to examine how their parameterizations relate to task performance, forgetting, and changes in pretrained weight geometry. Motivated by the spectrum-preserving design of orthogonal fine-tuning (OFT), we first ask whether spectral preservation is itself important for adaptation and retention. We find that t...
  </details>

- **2026-10-06** — Guilherme Afonso Galindo Padilha, Paulo Salgado Gomes de Mattos Neto, Rafael Menelau Oliveira e Cruz — [Are We Really Benchmarking Forecasting Models? The Impact of Preprocessing on Time Series Performance](http://arxiv.org/abs/2610.09096v1)
  <details><summary>📄 Abstract</summary>
  While established literature underscores the pivotal role of preprocessing in forecasting accuracy, this stage remains largely overlooked in current research. Modern benchmarks typically resort to simple scaling, failing to account for critical transformations required to address nonstationarity, such as differencing. This omission creates a significant structural preprocessing bias that favors models with built-in data treatments while obscuring the true potential of simpler architectures. We s...
  </details>

- **2026-10-06** — James Ravi Kirkpatrick, Alexandru Radulescu, Rachel Katharine Sterken — [Talking with Language Models](http://arxiv.org/abs/2610.09064v1)
  <details><summary>📄 Abstract</summary>
  When we interact with large language models (LLMs), are we having a conversation? They are designed to invite us to treat them as intelligent interlocutors who remember, act, and make commitments. But appearances deceive. We introduce the artifactual stance, a framework that reconceives human-AI interaction as artifact-mediated exchanges of candidate texts. LLM outputs are candidate texts optimized for utility, not utterances bearing meaning or force. LLMs are sophisticated text generators, not ...
  </details>

- **2026-10-06** — W. Russell Neuman — [Justice After Identity: Large Language Models and the View from Everywhere](http://arxiv.org/abs/2610.09053v1)
  <details><summary>📄 Abstract</summary>
  The search for a common view of justice and fairness has challenged human collective activity, as our diverging judgments are unavoidably shaped by the self-interests of social position, personal benefit, cultural inheritance, and historical circumstance. John Rawls famously attempted to overcome this limitation through popularizing a philosophical tradition known by the phrase "the original position" - a thought experiment by which people select principles of justice without knowing the identit...
  </details>

- **2026-10-06** — Yiyang Huang, Yitian Zhang, Yizhou Wang et al. — [RACER: Reflective Agent Coupling Query Interpretation and Tool-Based Retrieval for Frame Selection in Long Video Understanding](http://arxiv.org/abs/2610.08954v1)
  <details><summary>📄 Abstract</summary>
  Video large language models (Vid-LLMs) excel at diverse video-language tasks by reasoning over selected frames. However, frame selection for long videos remains challenging, as it requires retrieving relevant frames distributed across segments from a large candidate pool given complex queries. This paper investigates dominant approaches to long-video frame selection from a task-decomposition perspective, identifying two key challenges: the Query Comprehension Gap in similarity-based methods and ...
  </details>

- **2026-10-06** — Alexandr Grebennikov — [Optimal bound for the polynomial Littlewood-Offord problem](http://arxiv.org/abs/2610.08708v2)
  <details><summary>📄 Abstract</summary>
  We present an exposition of an argument, discovered by GPT-6 Pro, that gives an optimal bound for the polynomial Littlewood-Offord problem. Namely, let $F$ be a degree-$d$ multilinear polynomial that contains $r$ degree-$d$ monomials involving disjoint sets of variables. Then, for i.i.d. Rademacher random variables $ξ_1, \ldots, ξ_n$, we have $\mathbb{P}[F(ξ_1, \ldots, ξ_n) = 0] = O_d(r^{-1/2})$. This improves upon the previous bound of $(\log r)^{O_d(1)} r^{-1/2}$ due to Meka, O. Nguyen, and Vu...
  </details>

- **2026-10-06** — Chenyu Zhang, Rohit Parasnis, Saurabh Amin — [Network Intervention by Polling Strategic Agents](http://arxiv.org/abs/2610.08347v1)
  <details><summary>📄 Abstract</summary>
  A planner in a network of strategic agents faces three entangled challenges: the optimum depends on agents' private information, queried agents may misreport to steer the outcome, and exact computation does not scale. We study these challenges in multi-activity network games with heterogeneous private technologies, in which the planner sets non-discriminatory prices. We show that the optimal prices admit a centrality-based decomposition of the welfare kernel: each agent's contribution scales wit...
  </details>

- **2026-10-06** — Thiago Santos de Moura, Fynn Matuschek, Flavio Toffalini et al. — [Newer and Bigger, but Safer? A Longitudinal Study of the Functionality-Security Gap in LLM-Generated Code](http://arxiv.org/abs/2610.08240v1)
  <details><summary>📄 Abstract</summary>
  Large Language Models (LLMs) are widely used to generate code. Although their functional plausibility keeps improving, the generated code often contains security vulnerabilities. The functionality-security gap captures code that passes functional tests but fails security tests. A recent longitudinal study of three model families concluded that LLMs become smarter but not safer, with the only considered open-weight family stagnating. Whether this holds for other (open-weight) families and particu...
  </details>

- **2026-10-06** — Weiwei Qi, Chongyu Wang, Tianhang Zheng et al. — [ASCENT: First-Order Optimal Fine-Tuning with Recalibration for Safety--Utility Co-Enhancement](http://arxiv.org/abs/2610.08061v1)
  <details><summary>📄 Abstract</summary>
  Supervised fine-tuning can substantially improve the downstream utility of large language models (LLMs) but may compromise their safety. Existing safety-preserving methods constrain downstream updates using safety-related parameters or subspaces, but mainly focus on safety preservation rather than joint safety and utility enhancement, lack a theoretical characterization of the optimal safety-related subspace and safety-preserving task update, and typically rely on a static safety subspace that m...
  </details>

- **2026-10-06** — Fernando Martinez, Tao Li, Yingdong Lu et al. — [Independent Multi-Agent Reinforcement Learning with Counterfactual Semantic-Social World Models](http://arxiv.org/abs/2610.07704v1)
  <details><summary>📄 Abstract</summary>
  Fully decentralized multi-agent reinforcement learning (MARL), also referred to as independent learning, requires each agent to learn and act using only its local information and experience, without a centralized critic or inter-agent communication. Such a stringent information structure renders the conventional reward signal ambiguous. A poor return may result from an ineffective ego action, an incompatible teammate response, or an effective opponent response, yet scalar rewards alone do not re...
  </details>

- **2026-10-06** — Zhijun Zhang, Qianlong Wang, Keyang Ding et al. — [Improving Synthetic Data Generation for Argument Mining via Adversarial Reinforcement Learning](http://arxiv.org/abs/2610.07699v1)
  <details><summary>📄 Abstract</summary>
  Argument Mining (AM) is fundamentally constrained by the scarcity of high-quality structure-annotated datasets. While LLMs have shown promise in synthetic data generation, producing synthetic AM data that is both structurally accurate and sufficiently diverse remains a challenging problem. To address this problem, we revisit synthetic data generation for AM from a new perspective and propose a novel adversarial reinforcement learning framework for data synthesis. The proposed framework jointly o...
  </details>

- **2026-10-06** — Weixian Xu, Yanzhe Zhang, Zora Zhiruo Wang et al. — [Sherpa: Teaching LLMs to Teach Adaptively](http://arxiv.org/abs/2610.08778v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have become increasingly capable problem solvers, but being able to solve a problem is not the same as being able to teach it. Existing approaches to training LLMs as teachers rely on demonstrations, preference data, or predefined pedagogical criteria that specify what good teaching looks like. However, these signals are often not grounded in individual student learning outcomes, where effective teaching strategies can vary substantially across learners. To address t...
  </details>

- **2026-10-06** — Liao Ma, Jiayi Song, Yunfeng Wu et al. — [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](http://arxiv.org/abs/2610.08772v1)
  <details><summary>📄 Abstract</summary>
  Diffusion Transformers (DiTs) have achieved strong performance in image and video generation, but the quadratic complexity of full attention makes high-resolution generation computationally expensive. Window attention offers an efficient alternative, yet existing methods face a practical trade-off: partitioned window attention typically achieves computational efficiency consistent with its theoretical complexity. However, isolated windows block cross-window interaction, often introducing visible...
  </details>

- **2026-10-06** — Zewei Zhou, Rachel Luo, Yulong Cao et al. — [VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning](http://arxiv.org/abs/2610.08761v1)
  <details><summary>📄 Abstract</summary>
  Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales ve...
  </details>

- **2026-10-06** — Sayan Banerjee — [Metastability and Sharp Propagation-of-Chaos Thresholds for Mean-Field Interacting Diffusions on the Circle](http://arxiv.org/abs/2610.08755v1)
  <details><summary>📄 Abstract</summary>
  We study metastability and long-time propagation-of-chaos for mean-field interacting diffusions on the circle with multiple local free-energy minima. Working modulo rotations, we identify sharp exponential time scales for metastability and the validity and breakdown of the McKean-Vlasov approximation. Assuming finitely many critical rotation orbits and distinct local-minimum energies, we show that, for initial data in the attraction basin of a nonglobal minimum, metastability and propagation-of-...
  </details>

- **2026-10-06** — Chuhong Xu, Bo Su, Ziyao Chen et al. — [Same-Number Citation Swaps: Stress-Testing Jev as a Financial Evidence Judge](http://arxiv.org/abs/2610.08675v1)
  <details><summary>📄 Abstract</summary>
  Financial reports repeat values across periods, metrics and accounting lines, allowing an LLM-generated calculation to be numerically correct while citing the wrong financial role. We evaluate what probabilistic evidence verification adds beyond number matching using Jev as a source-support verifier for GPT-4.1-mini calculation traces. A signed-number-at-pointer baseline explains most recovery over exact quotation checks. To isolate the remaining role-recognition problem, we hold operands and ar...
  </details>

- **2026-10-06** — Yuhao Qin, Junbo Wang, Yuke Li et al. — [EC-RAG: Event Chain Retrieval-Augmented Generation for Long Video Understanding](http://arxiv.org/abs/2610.08674v1)
  <details><summary>📄 Abstract</summary>
  Current large video-language models (LVLMs) still face challenges when dealing with long videos, mainly because frames are often processed independently, making it difficult to capture temporal dependencies across events. Although retrieval-augmented approaches have been introduced to provide additional context, most of them operate at the frame or snippet level, which limits their ability to model how events evolve over time and relate to each other. In this paper, we propose Event Chain Retrie...
  </details>

- **2026-10-06** — Suxin Ji, Hungtao Wan, Mingjun Liu et al. — [Selective Transfer of RL Updates for Visual Reasoning](http://arxiv.org/abs/2610.08659v1)
  <details><summary>📄 Abstract</summary>
  Model merging provides a training-free way to transfer reasoning capabilities from language models to vision-language models (VLMs), but endpoint-based transfer can conflate pre-existing model differences with changes acquired during reasoning post-training. We instead formulate capability transfer around the training-stage update, isolating the parameter changes induced by reinforcement learning (RL). Yet transferring this update in full remains suboptimal: we find that its components differ su...
  </details>

- **2026-10-06** — Marcel Crasmaru — [CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution](http://arxiv.org/abs/2610.08592v1)
  <details><summary>📄 Abstract</summary>
  CNet is a C++/CUDA framework for building and training deep complex-valued neural networks (CVNNs) and, more generally, for optimizing complex-valued functions by gradient descent with Wirtinger (CR-calculus) derivatives. It takes a physics-native stance: a network is a cascade of complex -- and often unitary (the DFT) -- operations acting on an amplitude vector, and classification is a Born-rule measurement $p_k = |z_k|^2 / \|z\|^2$ rather than a softmax over real logits. Every layer ships a CP...
  </details>

- **2026-10-06** — Sujato Dutta, Sreekruthy Tummala, Shashank Vanga et al. — [MINDSET: Energy-based Schema Evolution for Long Conversational Agent Memory](http://arxiv.org/abs/2610.08586v1)
  <details><summary>📄 Abstract</summary>
  Long conversational agents have become essential in our daily lives. They must remember what was said long back in order to help us efficiently complete a task without needing the user to repeat instructions and context repeatedly. However, the main issue is that instructions and context change over time and so the agents must be able to adapt accordingly. A useful memory system should preserve both current and historical states, distinguish stale information from active knowledge, retrieve evid...
  </details>

- **2026-10-06** — Stephanie Buttigieg, Maeve Madigan, Parameswaran Kamalaruban et al. — [Latent space bias directions in LLMs capture confidence, not fairness](http://arxiv.org/abs/2610.08559v1)
  <details><summary>📄 Abstract</summary>
  Activation steering has gained popularity as a lightweight inference-time debiasing technique for large language models. However, prior work reports that steering vectors generalise poorly, with unintended effects on model performance and limited transfer to new datasets. Our work analyses what the debiasing direction used for activation steering actually encodes, in order to shed light on its inconsistent performance. We study the linear debiasing direction obtained by contrasting the activatio...
  </details>

- **2026-10-06** — Asim Khan, Samee Ullah Khan, Dwarikanath Mahapatra — [MedCORE: Criteria-Grounded Clinical Reasoning for Interpretable Medical Image Diagnosis](http://arxiv.org/abs/2610.08528v1)
  <details><summary>📄 Abstract</summary>
  Clinical diagnosis is inherently a structured reasoning process, yet existing deep learning models often bypass this structure by mapping image features directly to disease labels without explicitly interrogating the morphological and textural criteria that clinicians systematically evaluate. This limits diagnostic transparency and may compromise safe clinical deployment. We present MedCORE (Medical Criteria-Oriented Reasoning and Evidence), a structured diagnostic framework that operationalizes...
  </details>

- **2026-10-06** — Baihan Lin — [Language-model ratings of depression reflect the rater more than the patient](http://arxiv.org/abs/2610.08501v1)
  <details><summary>📄 Abstract</summary>
  Depression has no diagnostic blood test. Language models promise tireless, consistent assessment, but can accurate raters disagree about individuals? We pre-registered 880 language-model raters, crossing 11 open models with prompting and scoring choices, and applied them to 189 interviews against the eight-item Patient Health Questionnaire. Model choice explained 30.0% of summed-symptom score variance, stable participant differences 10.5%. Two randomly drawn raters with area under the receiver o...
  </details>

- **2026-10-06** — Maryam Baizhigitova, Andrew Seohwan Yu, Po-Hao Chen et al. — [Knee3DVLM: Dual-Sequence Full-Volume Vision-Language Modeling for Comprehensive Knee MRI Assessment](http://arxiv.org/abs/2610.08482v1)
  <details><summary>📄 Abstract</summary>
  Vision-language models (VLMs) are increasingly being applied to three-dimensional medical imaging, but their application to knee MRI remains limited, particularly for interpreting the complementary sequences used in clinical practice. We introduce Knee3DVLM, a sequence-aware VLM that uses full-volume DESS and fluid-sensitive TSE MRI to predict 57 anatomically resolved binary diagnostic targets derived from the MRI Osteoarthritis Knee Score (MOAKS) for structured reporting. We evaluated DESS-only...
  </details>

- **2026-10-06** — Rongcun Wang, Shi Chen — [RAPO-Sol: Retrieval-Augmented Preference Optimization for Repository-Level Solidity Code Generation](http://arxiv.org/abs/2610.08429v1)
  <details><summary>📄 Abstract</summary>
  Smart contracts written in Solidity manage assets, permissions, and irreversible state changes, making code generation both useful and security-critical. Repository-level Solidity generation is challenging because models must synthesize complete contracts or libraries while preserving consistency across state variables, modifiers, events, inheritance, external calls, and access-control logic. We present RAPO-Sol, a two-stage training framework for repository-level Solidity code generation. First...
  </details>

- **2026-10-06** — Toby D. Pilditch, Konstantinos Voudouris, Alexandra Abbas et al. — [Transect: Retaining Observability for Long-Horizon LLM Agent Evaluations](http://arxiv.org/abs/2610.08364v1)
  <details><summary>📄 Abstract</summary>
  Frontier AI evaluations increasingly use open-ended, agentic, long-horizon tasks whose transcripts can span hundreds of pages of outputs and actions from complex multi-agent networks. The observability envelop-the range of what evaluators can reliably infer about an agent's behaviours-is therefore narrowing. Language model assistants can help classify and interpret agent behaviour but also afford human evaluators significant analytical degrees of freedom, threatening the reproducibility and audi...
  </details>

- **2026-10-06** — Hun Park — [MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization](http://arxiv.org/abs/2610.08330v1)
  <details><summary>📄 Abstract</summary>
  Proprietary Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet aligning their outputs with diverse user preferences remains challenging. Existing personalization approaches for black-box LLMs often rely on user-specific scoring heads, causing the number of personalized parameters to grow linearly with the number of users and requiring additional adaptation for unseen users. To address these limitations, we propose Mixture-of-Facets (MoF), a s...
  </details>

- **2026-10-06** — Srikar Alla, Ali Shiri Sichani, Chi-Ren Shyu — [Quantum Entangled Multimodal Fusion Networks (QEMFN): Resource-Aware Hybrid Vision-Language Fusion via Trainable Entanglement](http://arxiv.org/abs/2610.08216v1)
  <details><summary>📄 Abstract</summary>
  Multimodal vision-language systems typically fuse image and text embeddings through classical operators such as concatenation, attention, bilinear pooling, or tensor interactions. We propose Quantum Entangled Multimodal Fusion Networks (QEMFN), a hybrid quantum-classical framework that introduces parameterized entanglement as a structured inductive bias for multimodal fusion. Pretrained visual and textual features are projected into compact latent spaces, encoded as angle-parameterized quantum s...
  </details>

- **2026-10-06** — Nina Nusbaumer, Iria de-Dios-Flores, Corentin Bel et al. — [STRUCTURALCOST: A controlled reading time dataset for modeling human sentence processing difficulty](http://arxiv.org/abs/2610.08208v1)
  <details><summary>📄 Abstract</summary>
  We introduce STRUCTURALCOST, a self-paced reading dataset of 475 participants and 40,800 observations isolating the processing cost of long-distance subject-verb dependency resolution. We replicate a low-powered psycholinguistic finding at NLP scale, namely that human reading times at the main verb increase with dependency length, driven by syntactic embedding beyond linear distance. Different language models -- spanning n-gram models, SSMs, and transformers -- partially mirror this graded diffi...
  </details>

- **2026-10-06** — Anvi Kalpesh Shah, Umamaheswara Sharma B — [Beyond the Leaderboard: Multi-Dimensional Evaluation of Dense and Mixture-of-Experts Models for Automated Program Repair](http://arxiv.org/abs/2610.08173v1)
  <details><summary>📄 Abstract</summary>
  Automated Program Repair (APR) with language models is usually evaluated by whether a generated patch passes the test suite, which can hide differences in maintainability, security, and computational cost. We propose a Weighted Quality Index (QI), inspired by the ISO/IEC 25010 software quality model, that combines functional correctness, maintainability, security, and generation efficiency under configurable weighting schemes. We evaluate three dense Qwen2.5-Coder models (3B, 7B, 14B) and the 16...
  </details>

- **2026-10-06** — Yiming Qin, Ke Wang, Amel Abdelraheem et al. — [Enhancing Diffusion Language Models with Autoregressive Post-Training Weights](http://arxiv.org/abs/2610.08108v1)
  <details><summary>📄 Abstract</summary>
  Diffusion language models (dLLMs) have emerged as a promising alternative to autoregressive (AR) language models, offering flexible token-update orders and parallel decoding. Recent dLLMs are often initialized from pretrained AR models before diffusion conversion in order to inherit their learned representations. After the conversion, however, they typically ignore the extensive post-training ecosystem of their AR ancestors. In this work, we show that these existing AR post-training weight updat...
  </details>

- **2026-10-06** — Jike Zhong, Ritwick Chaudhry, Xuanbai Chen et al. — [DSV-Mem: Evaluating Multimodal Memory in Professional Workflows for MLLM Agents](http://arxiv.org/abs/2610.08102v1)
  <details><summary>📄 Abstract</summary>
  Conversational MLLM agents are increasingly expected to assist in professional workflows, from AI research and engineering design to product management and business operations. Yet this capability remains underexplored: existing benchmarks largely focus on informal, everyday interactions and personal-life scenarios featuring photographic natural images, isolated static artifacts, and recall-oriented questions. In contrast, professional scenarios often involve structured, information-heavy artifa...
  </details>

- **2026-10-06** — Remo Grillo, Lukas Klic, Giovanni Colavizza — [Natural Language Questions as an Interface for Knowledge Graphs: QRAKEN Graph Distillation and Semantic Self-Healing](http://arxiv.org/abs/2610.08095v1)
  <details><summary>📄 Abstract</summary>
  Natural-language access to RDF knowledge graphs is a core Semantic Web ambition. Large language models (LLMs) have advanced Text-to-SPARQL, yet on unfamiliar graphs they often generate valid queries that misrepresent the populated data model. QRAKEN is a training-free, ontology-agnostic neurosymbolic pipeline grounding generation in empirical graph evidence rather than schema expectations. An offline distiller produces TTQL, a compact description of populated multi-hop patterns, conditional freq...
  </details>

- **2026-10-06** — Alessandro Cestelli, Spyridon Grountas, Scott Mc Haffie et al. — [Broadband Telecom Entanglement from an All-Fiber Type-0 Sagnac Source](http://arxiv.org/abs/2610.08025v1)
  <details><summary>📄 Abstract</summary>
  We demonstrate a compact, practical all-fiber source of non-degenerate telecom-band polarization-entangled photon pairs assembled from off-the-shelf components. The compact fiber-integrated architecture is designed to be affordable, straightforward to assemble and align, and compatible with existing optical-fiber infrastructure. Photon pairs are generated through type-0 spontaneous parametric down-conversion in a pigtailed periodically poled lithium-niobate waveguide embedded in a Sagnac interfe...
  </details>

- **2026-10-06** — Minseok Moon, Wonjun Choi, Seungwu Han et al. — [Defect-limited thermal transport in AlN using pretrained machine-learning interatomic potentials](http://arxiv.org/abs/2610.08013v1)
  <details><summary>📄 Abstract</summary>
  Aluminum nitride (AlN) is an important thermal management material whose high lattice thermal conductivity is strongly suppressed by oxygen impurities. We investigate phonon scattering by oxygen-related defects using pretrained universal machine-learning interatomic potentials (MLIPs), molecular dynamics (MD), and phonon Boltzmann transport calculations. Several pretrained MLIPs are benchmarked against density functional theory for phonon dispersions and pristine thermal conductivity. To balance...
  </details>

- **2026-10-06** — Xiong Li, Xiaowei Zhou, Yanwei Yu et al. — [Textual Environmental Context and Spatial Graphs for LLM-Based Regional SST Forecasting](http://arxiv.org/abs/2610.07895v1)
  <details><summary>📄 Abstract</summary>
  Sea surface temperature (SST) forecasting depends on local temporal persistence, regional spatial dependence, and environmental conditions that evolve with the forecast date. We study how these heterogeneous conditions can be presented to a large language model (LLM) for regional multi-step forecasting without serializing the full SST grid as text. We formulate forecasting as conditional numerical generation: historical SST and anomaly sequences, date-aligned environmental records, and static oc...
  </details>

- **2026-10-06** — Dayan Pan, Jingyuan Wang, Xie Yu — [Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning of Large Language Models](http://arxiv.org/abs/2610.07848v1)
  <details><summary>📄 Abstract</summary>
  Parameter-efficient fine-tuning (PEFT) has become a standard approach for adapting large language models to downstream tasks. However, most existing PEFT methods rely on uniform and static adaptations, without accounting for the structured heterogeneity of attention across dimensions, heads, layers, and input tokens. In practice, attention representations exhibit non-uniform behavior, and positional encoding mechanisms such as rotary positional embeddings (RoPE) induce dimension-dependent positi...
  </details>

- **2026-10-06** — Ravenor Davion, Nick Rui — [Privileged Context as Drift in On-Policy Self-Distillation](http://arxiv.org/abs/2610.07842v1)
  <details><summary>📄 Abstract</summary>
  On-policy self-distillation (OPSD) trains a language model to match a copy of itself conditioned on privileged context. Existing work varies what privileged context contains and how it is produced while also changing models, data, and training setups, making the effects of privileged context design difficult to isolate. Motivated by efforts in continual learning to reduce catastrophic forgetting, we study how the choice of privileged context affects policy drift. Specifically, we vary two axes: ...
  </details>

- **2026-10-06** — Abolfazl Younesi — [Do I Need the Cloud? Uncertainty-Aware Step-Level Handoff for Small Language Model Agents](http://arxiv.org/abs/2610.07816v1)
  <details><summary>📄 Abstract</summary>
  Small language models (SLMs) are attractive as local agent controllers because they reduce remote inference, latency, and deployment footprint, yet structured tool errors can cause an agent step to fail. Existing routers typically select a model once per query. However, agents expose sequential decision points whose difficulty dynamically changes based on intermediate observations. We propose STEPGATE, an uncertainty-aware handoff framework that scores each local SLM action and selectively escal...
  </details>

- **2026-10-06** — Gyusik Seo, Jaehong Yoon — [Attacca: Goal-Directed Control under State Continuity for Long-Horizon Embodied Agents](http://arxiv.org/abs/2610.07785v1)
  <details><summary>📄 Abstract</summary>
  A central capability of embodied agents is to accomplish complex objectives through sequences of interdependent tasks. Yet existing visual goal-conditioned policies underlying these agents are typically evaluated on isolated interactions where the target is already visible, and thus do not capture the conditions that arise during continuous long-horizon task execution. In such settings, each task begins from the state left by the previous one: the agent may end at a different position and orient...
  </details>

- **2026-10-06** — Farbod Tavakkoli, Gregory Diamos, Kenneth Church et al. — [OTel: Open Telco AI Datasets, Benchmarks, and Models](http://arxiv.org/abs/2610.07766v1)
  <details><summary>📄 Abstract</summary>
  We present Open Telco (OTel), an open telecom AI resource that releases derived telecom datasets for retrieval, reranking, instruction tuning, and safety/abstention, together with 30 full-parameter post-trained baselines spanning 10 embedding models, 3 rerankers, and 17 language models. The community has already engaged substantially with the resource: as of May 3, 2026, the released models have been downloaded over 16 million times and the project has received 157+ pieces of media coverage worl...
  </details>

- **2026-10-06** — Wanning He, Yuyao Zhang, Yu-Wing Tai — [RefRoute: Decoupling Conditioning Cost from References via Compact Residual Conditioning and Spatial Routing](http://arxiv.org/abs/2610.07720v1)
  <details><summary>📄 Abstract</summary>
  Multi-reference image generation requires preserving the appearance of multiple subjects while composing them into a coherent scene. However, existing diffusion transformers commonly encode references as dense visual token grids and jointly process them with global attention, making conditioning increasingly expensive as the number and resolution of references grow. We present RefRoute, a framework that addresses both reference representation cost and attention overhead through two complementary...
  </details>

- **2026-10-06** — Shreya Rajpal, Sonia Sharma, Swapnil Parekh et al. — [Evidence Before Sampling: Interpretable Implicit Negative Candidate Discovery for Recommendation](http://arxiv.org/abs/2610.07708v1)
  <details><summary>📄 Abstract</summary>
  Recommender systems learn from observed user-item interactions, but explicit negative feedback is often unavailable. Since deep learning models require negative signals for training, negative sampling methods typically treat selected unobserved interactions as negatives. However, a missing interaction does not explain why a user is uninterested in an item or whether there is sufficient evidence to label it negative. This is especially important in business recommendation, where negative signals ...
  </details>

- **2026-10-06** — Yi Liu, Xianglin Meng, Chang Chen et al. — [Silicon Language: A Robot-Native Knowledge Exchange Framework for Heterogeneous Robots](http://arxiv.org/abs/2610.07650v1)
  <details><summary>📄 Abstract</summary>
  Reusing a capability across heterogeneous robots still requires substantial human adaptation and verification: transferring a skill often means re-engineering interfaces, retuning parameters, and re-validating safety. We introduce Silicon Language, a robot-native knowledge exchange framework that treats the robot as the active subject of its own capability evolution. In this framework, a robot that wants a capability encodes its own experience into knowledge packets, publishes them, retrieves pe...
  </details>

- **2026-10-06** — Hyeongwoo Nam, Woongje Cho, Juwon Kim et al. — [OntoPlan: An Ontology-Grounded Scene Representation and Agentic Framework for Scalable Robot Task Planning](http://arxiv.org/abs/2610.07649v1)
  <details><summary>📄 Abstract</summary>
  Large language model (LLM)-based robot task planning is promising for open-ended instruction following, but degrades on long-horizon tasks in large environments. When spatial information is conveyed to the LLM through text, the model can fail to capture spatial context, and token cost grows with environment size. Generating action sequences directly with an LLM also makes it difficult to satisfy the current world state and action preconditions. We address this with an ontology-grounded scene rep...
  </details>

- **2026-10-06** — SiYuan Ma, Canran Xiao, Zikai Xiao et al. — [Linear Fitness Subspace in Protein Language Models Enables Sample-Efficient Directed Evolution](http://arxiv.org/abs/2610.07607v1)
  <details><summary>📄 Abstract</summary>
  Model-guided directed evolution seeks to identify high-fitness protein variants under limited oracle budgets. Protein language models (PLMs) provide rich representations for this task, but task-agnostic zero-shot scores can be misaligned with a target assay, while supervised search in high-dimensional embedding spaces can make surrogate modeling and uncertainty estimation sample-inefficient. We propose the Linear Fitness Subspace (LFS) hypothesis: within mutation-induced residue-level representa...
  </details>

- **2026-10-06** — Yang Qu, Yusheng Han, Chengjia Feng et al. — [LSC-DPO: Learning-Signal-Controlled Direct Preference Optimization](http://arxiv.org/abs/2610.07592v1)
  <details><summary>📄 Abstract</summary>
  Direct Preference Optimization (DPO) has become a standard reward-model-free approach for aligning language models with preference data. However, as the scaled preference margin grows during training, the logistic DPO loss becomes progressively less sensitive to further changes. We study DPO from a loss-level geometric perspective and identify the sigmoid factor as a learning signal that characterizes the local sensitivity of the objective. Based on this view, we propose Learning-Signal-Controll...
  </details>

- **2026-10-06** — Chung Min Kim, Brent Yi, David McAllister et al. — [QF3: Fast Flow RL with Filtered Q-Gradients](http://arxiv.org/abs/2610.08789v1)
  <details><summary>📄 Abstract</summary>
  Flow policies have become a standard policy class for learning robot behaviors from demonstrations, but reinforcement learning is still critical for improving pre-trained flow policies or learning them from scratch through interaction. We introduce QF3 (Fast Flow RL with Filtered Q-Gradients), an online off-policy RL algorithm that trains a flow policy with flow matching plus the critic's action gradient, backpropagated through a one-step prediction of the flow's output. To keep updates where th...
  </details>

- **2026-10-06** — Zhenghong Zhou, Zhe Lin, Jiebo Luo et al. — [ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing](http://arxiv.org/abs/2610.08779v1)
  <details><summary>📄 Abstract</summary>
  Current video editors can insert objects but often struggle to make them participate in interactions such as being picked up or manipulated. We introduce ALIVE, a framework that makes inserted objects "alive" through coherent interactions with the source video's contents, using an edited first frame and an instruction naming only the added object. We curate 35,800 editing pairs combining 3D-rendered, model-generated, and real-world videos with general editing pairs from ROSE. Each pair differs i...
  </details>

- **2026-10-06** — Hanjun Luo, Xiucheng Zhang, Zhuoning Xu et al. — [ParanoiaEval: Benchmarking Unnecessary Defensive Work in Agentic Coding](http://arxiv.org/abs/2610.08662v1)
  <details><summary>📄 Abstract</summary>
  As coding agents increasingly undertake real-world work autonomously, judging whether their risk treatments are warranted has become important. Existing work evaluates related agent behaviors from separate perspectives, but lacks a systematic framework for unifying these behaviors. To bridge this gap, we introduce ParanoiaEval, the first benchmark for unified evaluation of risk-treatment capabilities in coding agents. Grounded in the well-established Avoidance-Transfer-Mitigation-Acceptance fram...
  </details>

- **2026-10-06** — Yurun Chen, Josh Qixuan Sun, Jason Qin et al. — [HygieneRoboBench: Benchmarking Hygiene-Aware Planning for Household Robots](http://arxiv.org/abs/2610.08642v1)
  <details><summary>📄 Abstract</summary>
  Contact with contaminated objects can spread hazards through a household robot's grippers, tools, and shared surfaces, while new contacts can make an existing plan unsafe. Existing benchmarks do not jointly assess how planners identify hygiene risks from contact history and plan safe continuations after new contact events. Planners must do so within time and resource limits while respecting user priorities. We introduce HygieneRoboBench, with 624 instances across 134 task families, to evaluate s...
  </details>

- **2026-10-06** — Zijia Chen, Yuenan Hou, Yu Li et al. — [Towards Efficient Robotic Manipulation Models with Self-Recursive Pruning](http://arxiv.org/abs/2610.08555v1)
  <details><summary>📄 Abstract</summary>
  Network pruning can reduce parameter redundancy in robotic policies. However, generic pruning criteria are tailored for image recognition tasks and commonly designed to preserve weight magnitude, local reconstruction, or language-model likelihood rather than closed-loop action behavior. Directly applying these pruning algorithms to robotic tasks yields unsatisfactory performance. In this paper, we propose Loss-Conditioned Activation-Moment (LCAM) pruning, a training-free method for unstructured ...
  </details>

- **2026-10-06** — Hyun Jung Lee, Jungtaek Kim, Jongwon Jeong et al. — [EMHO: EMbodied Agent Harness Optimization via Experience Traces](http://arxiv.org/abs/2610.08432v1)
  <details><summary>📄 Abstract</summary>
  Improving embodied agents often focuses on optimizing the underlying model through training, while the surrounding agent harness that controls planning, context, and tool use is typically engineered. We ask whether this harness can instead improve itself directly from experience traces under sparse environmental feedback. We propose EMbodied Agent Harness Optimization (EMHO), a self-evolving framework that keeps the embodied model frozen and iteratively revises its harness by analyzing execution...
  </details>

- **2026-10-06** — Haegu Lee, Christoffer Sloth — [Post-Grasp Kinematic Repair for Robotic Insertion via Object-in-Gripper Reorientation](http://arxiv.org/abs/2610.08421v1)
  <details><summary>📄 Abstract</summary>
  A stable grasp does not guarantee kinematically feasible robotic insertion because the object-in-gripper transform may force the robot towards singularities or joint limits along the prescribed insertion path. We study post-grasp kinematic feasibility repair through object-in-gripper reorientation. Given an achieved grasp and a fixed insertion path, we seek a small reorientation that restores kinematic feasibility. Sequential IK can miss such candidates by following an unfavorable joint-space pa...
  </details>

- **2026-10-06** — Fengkai Liu, Hao Su, Haozhuang Chi et al. — [Event-Driven Proactive Robot Assistance through Vision-Language Reasoning](http://arxiv.org/abs/2610.08344v1)
  <details><summary>📄 Abstract</summary>
  Assistance in collaborative manipulation is often initiated by user instructions, making high-level reasoning request-driven. In fluent human teamwork, however, partners often infer the next helpful step from the observed outcome of an action rather than waiting for instructions. Motivated by this, we investigate an event-driven formulation of proactive assistance, where human--object interaction outcomes initiate assistive reasoning without user-provided task specifications at inference time. T...
  </details>

- **2026-10-06** — Nanhe Chen, Runqiu Yang, Jiawei Tang et al. — [Compact Robot Policies Need Fine-Grained Visual Representations](http://arxiv.org/abs/2610.08183v1)
  <details><summary>📄 Abstract</summary>
  Multi-task manipulation policies differ in architecture, scale, and pretrained priors all at once, so published comparisons cannot attribute performance to any single component. We argue that most of it comes from the visual representation, and that parameter scale and generative priors are largely incidental. To test this, we build CoRP (Compressed Representation Policy), a deliberately compact policy (48.9M parameters, no vision-language model and no video-generative prior) that factorizes int...
  </details>

- **2026-10-06** — Owen Du, Yang Yue, Jie Zhang et al. — [VLA-ACL: Action-Consistent Visual Token Pruning for Efficient Vision-Language-Action Models](http://arxiv.org/abs/2610.08133v1)
  <details><summary>📄 Abstract</summary>
  Vision-Language-Action (VLA) models achieve strong robotic manipulation performance but incur high computational costs from processing long token sequences at every control step, limiting real-time deployment. Visual token pruning offers a direct solution, as visual patches dominate the input sequence and contain considerable redundancy. Existing approaches, however, either rely on indirect training-free heuristics, such as attention scores and motion thresholds, or require costly fine-tuning of...
  </details>

- **2026-10-06** — Yikai Qin, Yifei Deng, Mingjian Liang et al. — [EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation](http://arxiv.org/abs/2610.07969v1)
  <details><summary>📄 Abstract</summary>
  Scaling robotic foundation models requires diverse training data and reliable evaluation environments. Simulation offers a scalable solution, yet existing generation pipelines remain constrained by predefined assets and skills, a disconnect between scene generation and task generation, and limited support for complex embodiments and physics. We introduce EmbodiedSmith, a framework for scalable embodied data generation through recursive self-improvement (RSI). EmbodiedSmith unifies asset, scene, ...
  </details>

- **2026-10-06** — Deogyong Kim, Sunghwan Kim, Sangam Lee et al. — [From Delivery to Stateful Exploration: Rethinking the Index for Agentic Search](http://arxiv.org/abs/2610.07960v1)
  <details><summary>📄 Abstract</summary>
  Recent advances in agentic search have given large language model (LLM) agents finer control over corpus exploration. However, search interfaces often return matching passages even when feedback about the candidate set would suffice for the next decision, coupling candidate refinement with source-text exposure. We propose IndexAct, an interface for Index-Native Corpus Interaction that separates candidate-set refinement from text inspection. Agents construct and manipulate persistent candidate se...
  </details>

- **2026-10-06** — Jicong Ao, Shuhan Jiang, Yuling Zhong et al. — [SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining](http://arxiv.org/abs/2610.07652v1)
  <details><summary>📄 Abstract</summary>
  The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation c...
  </details>

- **2026-10-06** — Kazutoshi Tanaka — [TacZero: Training-Free Peg Insertion Using a General-Purpose Vision-Language Model with Tactile Feedback](http://arxiv.org/abs/2610.07621v1)
  <details><summary>📄 Abstract</summary>
  Robots that autonomously determine their actions from language instructions and sensory observations could perform new contact-rich manipulation tasks without task-specific training or hand-designed rules. To perform these tasks, robots must infer how objects contact one another and move as a result, then select actions. For contact inference and action selection, prior approaches involve designing estimation models and tactile feedback control laws, or learning models for object-motion estimati...
  </details>

- **2026-10-06** — Zexi Zhang, Zecheng Zhu, Zidong Chen et al. — [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](http://arxiv.org/abs/2610.07594v1)
  <details><summary>📄 Abstract</summary>
  Humanoid household manipulation requires the arms to act while the body balances, steps and changes posture. We present BiGym 2.0, an adaptation of BiGym for the Unitree G1 across 20 household tasks using a unified whole-body controller for demonstration and evaluation. The suite provides 60 native human virtual-reality demonstrations per task with synchronised multi-camera views and full-body execution records. We benchmark vision-language-action fine-tuning, imitation learning, demo-driven rei...
  </details>

- **2026-10-06** — Muhammad Faraz Shoaib, Muhammad Qasim, Raisulhaq Mohammed Rizwan et al. — [LOGIC: An LLM Benchmark for Intent-Grounded Change Impact in Aerospace Electrical Systems](http://arxiv.org/abs/2610.07580v1)
  <details><summary>📄 Abstract</summary>
  Aerospace electrical-design revisions can contain multiple genuine changes, although an engineering request may authorize only a subset. Propagating every detected difference can therefore produce overly broad impact reports. We present LOGIC, a controlled benchmark and evaluation framework in which locally deployable language models ground a request in a deterministic candidate-change inventory before selected changes are propagated through a typed electrical traceability graph. This separation...
  </details>

- **2026-10-06** — Casey Kennington, Ross Mead, Saad Elbeleidy et al. — [Towards an Extensible Benchmark for Spoken Dialogue with Social Robots](http://arxiv.org/abs/2610.08733v1)
  <details><summary>📄 Abstract</summary>
  Language models provide a plug-and-play interface between humans and robots, but important challenges remain when speech, dialogue, fast interaction, and collaboration are required. We propose a benchmark for the community to use as a way to explore common spoken dialogue artifacts between robots and humans, including requests for clarification, interruptions, embodied signals (e.g., head nods or facial cues), and time constraints. We also explain our vision to extend the benchmark for other asp...
  </details>

- **2026-10-06** — Alexandr Grebennikov — [Optimal bound for the polynomial Littlewood-Offord problem](http://arxiv.org/abs/2610.08708v1)
  <details><summary>📄 Abstract</summary>
  We present an exposition of an argument, discovered by GPT-6 Pro, that gives an optimal bound for the polynomial Littlewood-Offord problem. Namely, let $F$ be a degree-$d$ multilinear polynomial that contains $r$ degree-$d$ monomials involving disjoint sets of variables. Then, for i.i.d. Rademacher random variables $ξ_1, \ldots, ξ_n$, we have $\mathbb{P}[F(ξ_1, \ldots, ξ_n) = 0] = O_d(r^{-1/2})$. This improves upon the previous bound of $(\log r)^{O_d(1)} r^{-1/2}$ due to Meka, O. Nguyen, and Vu...
  </details>

- **2026-10-06** — Jiajun Chen, Haoyu Wu, Mingda Jia et al. — [Recursive Game Creator: An Agentic Product-Level Experience-Oriented Game Harness](http://arxiv.org/abs/2610.08621v1)
  <details><summary>📄 Abstract</summary>
  Recent game design agents have made substantial progress in generating playable games. However, program correctness does not ensure an enjoyable experience for players. We present Recursive Game Creator, an experience-oriented harness to advance agentic game development from rough game prototypes into entertaining games. Recursive Game Creator organizes recursive development around four components: Designer, Builder, Player, and Reviewer. The Designer translates user instructions and Reviewer's ...
  </details>

- **2026-10-06** — Ashley E. Bravo-Bravo, Yuchen Zhang, Haralambos Mouratidis et al. — [InterCorrect: Intersection-Aware Correction of Demographic Model Merging for Fair ASR](http://arxiv.org/abs/2610.08604v1)
  <details><summary>📄 Abstract</summary>
  Automatic Speech Recognition (ASR) systems often show uneven performance across demographic groups, and errors can be especially difficult to address for speakers belonging to multiple demographic groups. This work studies demographic-aware model merging for fair Speech-LLM-based ASR. Starting from a SLAM-ASR-based model, we fine-tune only the connector on demographic-specific subsets and merge the resulting subgroup-adapted connectors into a global model. We then identify critical cross-axis de...
  </details>

- **2026-10-06** — Bing Liu, Wenjie Zhou, Chengcheng Zhao et al. — [How Bregman Divergences Shape Shampoo](http://arxiv.org/abs/2610.08534v1)
  <details><summary>📄 Abstract</summary>
  Understanding the principles behind Shampoo has recently guided the development of more effective neural network optimizers. These methods learn a preconditioner by optimizing the Frobenius or Kullback-Leibler (KL) divergence against the gradient second moment. In this work, we investigate how the choice of divergence shapes preconditioning, which remains unclear and blocks further improvements. To do so, we develop a unified Bregman divergence framework that connects all popular divergences, al...
  </details>

- **2026-10-06** — Omer Chor, Aljaž Godec, Oren Raz — [Hamiltonian curl-forces in systems coupled to multiple thermal reservoirs](http://arxiv.org/abs/2610.08423v1)
  <details><summary>📄 Abstract</summary>
  We investigate the statistical mechanics of a system coupled to multiple heat reservoirs at different temperatures, a setting which typically sustains nontrivial circulation. By applying a canonical transformation, we map the system onto that of a particle coupled to a single reservoir yet driven by a deterministic curl-force---a reversible, velocity-independent non-conservative force with non-vanishing curl---that can be described by a Hamiltonian with an anisotropic kinetic energy term. Despit...
  </details>

- **2026-10-06** — Yang Hong, Yajun Yang, Xin Wang et al. — [Foresight-over-Graph: Reasoning Beyond Local Horizons for Knowledge Base Question Answering](http://arxiv.org/abs/2610.08388v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) have demonstrated strong capabilities in question answering, yet they still frequently suffer from hallucinations on knowledge-intensive tasks. Knowledge graphs (KGs) provide LLMs with structured, interpretable, and updatable factual grounding, making them a promising external knowledge source for reliable reasoning. However, existing LLM-guided graph reasoning methods typically rely on hop-wise greedy or beam-style pruning during evidence retrieval. Such local decis...
  </details>

- **2026-10-06** — Eunwoo Heo — [Near-diagonal asymptotics and the failure of strong universality in random Čech persistence](http://arxiv.org/abs/2610.08257v1)
  <details><summary>📄 Abstract</summary>
  The strong universality conjecture of Bobrowski and Skraba asserts that, under a prescribed data-dependent additive centering, the empirical laws of log-log transformed persistence ratios of random geometric complexes share a universal limit across sampling models, dimensions, filtrations, and homological degrees. They conjectured a left-skewed Gumbel limit and used it as a null law for testing topological significance. We show that, when the uncentered empirical laws and the centerings have det...
  </details>

- **2026-10-06** — Lingteng Zeng — [Visual Orchestration Tax in Agentic VLM Pipelines: Auditing and Certifying Visual Evidence Reuse](http://arxiv.org/abs/2610.08170v1)
  <details><summary>📄 Abstract</summary>
  Agentic VLM pipelines increasingly pass the same static visual evidence through multiple specialist agents and tools. This design creates an orchestration-level redundancy mode: semantically unchanged images are repeatedly reconstructed as image-conditioned requests at the VLM API boundary. We call this phenomenon visual orchestration tax and develop a measurement-to-certification framework for visual evidence reuse in agentic VLM pipelines. The audit side defines $\mathrm{M1}_{\mathrm{trace}}$ ...
  </details>

- **2026-10-06** — G. L. John Salvin, Swapnil Hingmire — [Making COMET Comparable Across Scripts: Diagnosis and Correction of Tokeniser-Induced Script Bias in Indic MT Evaluation](http://arxiv.org/abs/2610.08159v1)
  <details><summary>📄 Abstract</summary>
  COMET reports translation quality as a single number, and that number is routinely compared across target languages written in different scripts. Such a comparison assumes Script Invariance: the score should not depend on the writing system that carries the target. We test it on IndicMT Eval by re-encoding the target into Latin script, which changes orthographic form while holding content and human ratings fixed. Script identity then accounts for 22.9% of native-script COMET variance, and agreem...
  </details>

- **2026-10-06** — Priyanka Sinha, Nikolaos Kekatos, Stylianos Basagiannis et al. — [Explainable Rule Mining of IPv6 Extension-Header Presence Patterns from Paired-Vantage Captures](http://arxiv.org/abs/2610.08090v1)
  <details><summary>📄 Abstract</summary>
  IPv6 extension headers (EHs), such as fragmentation, segment routing, and in-situ telemetry, are operationally important yetwidely dropped in transit, and characterising their behaviour from packet captures is a recurring measurement problem. We ask whetheran explainable miner can recover human-readable rules of EH behaviour, and we contribute two reusable tools: a negative-control protocol that diagnoses whether a mined "temporal" network rule reflects genuine cross-packet dynamics or mere with...
  </details>

- **2026-10-06** — Joes Biburger, Nicole Megow, Golnoosh Shahkarami — [Online Fair Division under Eligibility Constraints](http://arxiv.org/abs/2610.08064v1)
  <details><summary>📄 Abstract</summary>
  We study fair division of indivisible items under eligibility constraints: each item may be assigned only to a subset of eligible agents. This model coincides with restricted assignment in scheduling, with agents as machines and items as jobs, and captures settings where work or resources must be split among parties with different capabilities. Eligibility makes the usual fairness benchmarks inadequate, as agents should not be measured against items they could never receive. We therefore use eli...
  </details>

- **2026-10-06** — Takanori Ashihara, Kohei Matsuura, Masato Mimura — [HINTT Submission to the 2nd MLC-SLM Challenge: Comparing Cascaded and Unified Approaches to Diarization and ASR](http://arxiv.org/abs/2610.08063v1)
  <details><summary>📄 Abstract</summary>
  This paper presents the HINTT system submitted to the 2nd Challenge and Workshop on Multilingual Conversational Speech Language Model (MLC-SLM). We address multilingual speaker-attributed ASR, where systems must determine who spoke when and what was spoken. We investigate two modeling strategies for this problem: a cascaded pipeline that combines speaker diarization with speech-LLM-based ASR, and a unified speech LLM that directly generates speaker labels, timestamps, and transcriptions. Our fin...
  </details>

- **2026-10-06** — Jinsong Zhang, Kejun Wu, Ming Zhu et al. — [M3SunAgent: Monocular 3D Spatial Understanding Agent for Metric Depth Estimation and 3D Visual Grounding](http://arxiv.org/abs/2610.07982v1)
  <details><summary>📄 Abstract</summary>
  Monocular metric depth estimation and 3D visual grounding represent the two complementary cornerstones of monocular 3D spatial understanding (M3Sun), from which the fundamental 3D spatial information required by M3Sun can be acquired. However, these complementary tasks are generally conducted by separate frameworks, which pose challenges of inflexible and unaligned spatial information access for embodied intelligence systems. In this paper, we propose a unified agent for monocular 3D spatial und...
  </details>

- **2026-10-06** — Chiara Giaquinta, Laura Hernández, David Chavalarias — [Probabilistic neighbors' selection competes with confirmation bias in a bounded confidence model](http://arxiv.org/abs/2610.07971v1)
  <details><summary>📄 Abstract</summary>
  In this work, we investigate three modified versions of the classic Hegselmann-Krause opinion dynamics model, incorporating features that are typical of many real-world systems, such as uncertainty in the selection of interacting agents and a weighted evaluation of the relevance of their opinions in the influence function to enhance confirmation bias. Through extensive simulations across different network topologies, ranging from stylized network models (Barabási-Albert, Erdős-Rényi, and Watts-S...
  </details>

- **2026-10-06** — Brendan King, Farima Fatahi Bayat, Jean-Flavien Bussotti et al. — [Confidence Reasoning Graphs: Structured Confidence Estimation for LLM Agents](http://arxiv.org/abs/2610.07948v1)
  <details><summary>📄 Abstract</summary>
  When using an LLM agent in a consequential domain, making an informed decision about whether to trust its output or intervene requires calibrated confidence in the agent's success. Confidence estimation for agents is difficult because evidence about success is distributed across heterogeneous, interdependent steps of an agent's trajectory. Practical agentic deployments introduce further challenges: frontier LLMs often provide limited access to internal signals, agent roll-outs are costly, and tr...
  </details>

- **2026-10-06** — Ciaran Regan, Kai Arulkumaran, Luke Darlow et al. — [Continuous Memory Machines](http://arxiv.org/abs/2610.07907v1)
  <details><summary>📄 Abstract</summary>
  Recurrent neural networks typically compress information into a single vector-valued recurrent state, forcing short-term computation and long-term retention to share the same representation. Past extensions alleviate this bottleneck by increasing the memory capacity or separating timescales, but lack the combination of rapid neuron-level processing and longer-term retention found in biology. To that end, we introduce the Continuous Memory Machine (CMM), a recurrent architecture with matrix-value...
  </details>

- **2026-10-06** — Miao Xie, Xiao Zhang, Yuan Wang et al. — [ShanLiangRen: A Nutrition Agent for Personalized Daily Meal Planning](http://arxiv.org/abs/2610.07886v1)
  <details><summary>📄 Abstract</summary>
  Dietary nutrition planning plays an important role in chronic disease management and maintaining a healthy body. In applications, it must simultaneously satisfy personalized constraints and reasonable multidimensional nutritional goals. These two aspects often conflict, and user constraints evolve with feedback, resulting in a substantial gap between generic guidelines and executable plans. To bridge this gap, we first propose the personalized fully quantified multiobjective dietary planning pro...
  </details>

- **2026-10-06** — Jeonghwa Lim, Minje Park, Yeongyeon Na et al. — [Label-Efficient Deep Learning for ECG Delineation: A Multi-Dataset Benchmark against Widely Used Delineation Tools](http://arxiv.org/abs/2610.07885v1)
  <details><summary>📄 Abstract</summary>
  Electrocardiogram (ECG) delineation, the identification of waveform boundaries, is a foundational step that translates raw ECG signals into clinically interpretable measurements. Deep learning has advanced this task but remains dependent on costly expert annotations. Label-efficient strategies such as self-supervised pretraining and semi-supervised learning are expected to ease this burden, yet it remains unclear whether they yield reliable delineation and whether the deep models they produce ou...
  </details>

- **2026-10-06** — Sunchan Park, Beomkwon Cho, Kyeongbo Kong — [CueRator: Agentic Search for Symbolic Rules to Adapt Frozen Multimodal Encoders](http://arxiv.org/abs/2610.07868v1)
  <details><summary>📄 Abstract</summary>
  Large language model agents have been used to search over symbolic structures such as programs and equations. We propose CueRator, an agentic framework for policy-aware decision-rule discovery, which adapts frozen contrastive multimodal encoders by searching for the decision rule that converts their cross-modal similarities into predictions. We validate it on open-vocabulary audio-visual event perception, where existing methods involve a trade-off between adaptivity and generalization to unseen ...
  </details>

- **2026-10-06** — Sihyeon Lee, Jihun Song, Chanwoo Kim et al. — [OMIT the Action: Measuring Framing-Invariant Omission Bias under Philosophical Disagreement](http://arxiv.org/abs/2610.07847v1)
  <details><summary>📄 Abstract</summary>
  As LLMs increasingly assist in moral reasoning, omission bias, the tendency to prefer inaction even when equivalent framings reverse substantive outcomes, poses a significant risk of skewed decision-making. Yet omission bias remains underexplored in LLM evaluation, with the few existing studies limited in scale and focused largely on utilitarian-deontological conflicts. To address this gap, we introduce OMIT, a benchmark consisting of 218 paired-frame scenarios across 10 conflict types, construc...
  </details>

- **2026-10-06** — Zhongqin Wang, Xiaoqi Zhang, Nan Yang et al. — [Agentic Semantic Sensing for Resource-Adaptive AI-RAN](http://arxiv.org/abs/2610.07829v1)
  <details><summary>📄 Abstract</summary>
  Semantic sensing (SemS) acquires task-relevant information rather than reconstructing complete physical information. Existing SemS formulations typically operate open loop: sensing configurations and observation schedules are fixed before inference and cannot respond to evolving task-level evidence. We propose Agentic SemS, a closed-loop framework for AI-enabled radio access networks (AI-RANs) that controls sensing within a communication-feasible profile set. A profile-conditioned causal Transfo...
  </details>

- **2026-10-06** — Hans Schabert, Christoph Peters — [One Step at a Time: Trading LLM Autonomy for Process Predictability](http://arxiv.org/abs/2610.07817v1)
  <details><summary>📄 Abstract</summary>
  Organizations automating operational processes need more than a correct outcome: they need to predict how a process will run, know which one actually ran, and inspect it step by step. When an agent is the executor that predictability is normally lost: the prescribed procedure goes into the system prompt, and only a final answer comes back. We deliver the procedure step by step over the Model Context Protocol (MCP) instead: a server releases one step at a time, the agent executes it, and each ste...
  </details>

- **2026-10-06** — Saanvi Khetan, Sankar Balasubramanian — [Thin Evidence, Thick Priors: How Language Models Substitute Identity for Missing Financial Facts](http://arxiv.org/abs/2610.07798v1)
  <details><summary>📄 Abstract</summary>
  People increasingly ask large language models what to do with their money, yet seldom describe their finances in full. This paper asks what a model does with the gap. Holding finances fixed and changing only who the investor is said to be, we grade the financial evidence in the prompt from eight facts to none and measure how far the recommended equity allocation moves. Across 96,600 prompts to Llama-3.1-8B-Instruct, built from 100 financial profiles, 138 personas and seven disclosure conditions,...
  </details>

- **2026-10-06** — Catherine Ji, Vivek Myers, Sergey Levine et al. — [The Geometry of Empowerment](http://arxiv.org/abs/2610.07796v1)
  <details><summary>📄 Abstract</summary>
  Empowerment captures the capacity for an agent to actively control its environment. While conceptually appealing as an information-theoretic quantity, the connection between empowerment and structurally central states that provide broad access to future outcomes has remained an open question. In this work, we link empowerment maximization and skill-learning methods to provide new geometries for interpreting and analyzing empowerment. Our analyses answer longstanding open questions on the connect...
  </details>

- **2026-10-06** — Qi Cheng, Rongchao Dong, Shengyu Chen et al. — [ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks](http://arxiv.org/abs/2610.07763v1)
  <details><summary>📄 Abstract</summary>
  The rapid progress of LLM-based multi-agent systems (MAS) has shown that they largely outperform single agents on coding, math, and QA tasks, where executable tests provide a binary success signal. Whether this advantage transfers to real scientific data analysis remains untested. We introduce ST-Bench, a benchmark designed to answer two questions: whether MAS outperform single agents on complex scientific data analysis tasks, and if so, by how much and at what additional cost. ST-Bench contains...
  </details>

- **2026-10-06** — Emrul Hasan, Chen Ding — [Contrastive Learning for Aspect Representation towards Explainable Recommendation](http://arxiv.org/abs/2610.07761v1)
  <details><summary>📄 Abstract</summary>
  In this work, we propose a novel recommendation model, CLARER (Contrastive Learning for Aspect Representation towards Explainable Recommendation) that integrates aspect features learned from textual reviews with rating information to improve the accuracy and explainability of recommendations. Our proposed framework learns user and item representations by combining rating-based features and aspect-based features from reviews. Specifically, rating-based features are learned through a multi-layer p...
  </details>

- **2026-10-06** — Kaifeng He, Xiaojun Zhang, Zhenxi Chen et al. — [Acquiring and Verifying Repository Norms for Coding Agents](http://arxiv.org/abs/2610.07757v1)
  <details><summary>📄 Abstract</summary>
  Changes produced by coding agents can pass functional tests while leaving repository contribution requirements unmet. Following repository-specific norms requires identifying guidance dispersed across repository sources and interpreting its conditions and exceptions. Retrieval and documentation approaches supply general context, but agents must still determine which norms apply. We introduce RepoNorm to acquire explicit and implicit repository norms independently of coding tasks. It checks norm ...
  </details>

- **2026-10-06** — Feng Luo, Hui Luo, Zhifeng Bao et al. — [Cost-Effective Numerical QA over Semi-Structured Table: Structuring, Resolution, Planning](http://arxiv.org/abs/2610.07749v1)
  <details><summary>📄 Abstract</summary>
  Semi-structured tables encode rich semantic information through diverse layout elements, such as hierarchical row and column headers. Answering numerical questions over such data is challenging because it requires a joint effort of accurate structural understanding of tables, question uncertainty resolution, and complex query intents interpretation. Existing methods are rarely effective in handling the above multifaceted challenges in a holistic manner; moreover, they rely on LLMs without consid...
  </details>

- **2026-10-06** — Mohammad Al-Ratrout, Shayla Sharmin, Roghayeh Leila Barmaki — [Who Is Talking to the Agent? LLMs in Multi-User 3D Virtual Environments](http://arxiv.org/abs/2610.07732v1)
  <details><summary>📄 Abstract</summary>
  When several people share a 3D virtual room with an LLM agent, the agent must decide not only what to say, but whether an utterance was addressed to it and, if accessible, what profile information about the others present it may use. To study both problems, we construct LookAway, a controlled corpus of 40 sessions involving 80 distinct personas and an LLM agent (1,200 turns), including ambiguous-addressee turns in which speaker orientation agrees or conflicts with the intended addressee. Across ...
  </details>

- **2026-10-06** — Fouad Bousetouane — [EIO-Agents: The Missing Semantic Layer for AI Agent Evaluation](http://arxiv.org/abs/2610.07675v1)
  <details><summary>📄 Abstract</summary>
  AI agents are entering production in increasingly consequential environments without a shared semantic standard for what their evaluations actually mean. Scores, traces, judge outputs, and multi juror findings are increasingly used to justify readiness and release decisions, yet they often do not specify what evidence supports a claim, what that evidence can establish, or how the claim leads to a decision. We introduce EIO-Agents, an open specification for interoperable AI agent evaluation built...
  </details>

- **2026-10-06** — Abhijeet Krishnan, Chris Martens — [Towards the Automatic Synthesis of Interpretable Chess Tactics](http://arxiv.org/abs/2610.07640v1)
  <details><summary>📄 Abstract</summary>
  State-of-the-art reinforcement learning agents are capable of outperforming human experts at games like chess, Go and StarCraft II. These agents do not simply take advantage of their digital hardware in being able to react and calculate faster than humans, but employ better strategies that lead to more victories. Interpreting these strategies would give human players valuable insight into how to improve their play. In this preliminary work, we propose a symbolic sub-policy model for playing ches...
  </details>

- **2026-10-06** — Abhijeet Krishnan, Colin M. Potts, Arnav Jhala et al. — [Learning Explainable Representations of Complex Game-playing Strategies](http://arxiv.org/abs/2610.07638v1)
  <details><summary>📄 Abstract</summary>
  As part of learning to play complex games, human players develop develop abstractions for concepts and strategies of gameplay consistent with game rules to improve their performance. These concepts are applied to explain other players' actions, and to inform their own actions in-game. Understanding other players' strategies is a crucial part of such improvement, but requires time and effort. In this paper, we propose a strategy similar to human cognition for training RL agents to synthesize lear...
  </details>

- **2026-10-06** — Kautik Mandve, Dileepa Fernando — [Explore, Then Commit: Measurement-Efficient Scientific Law Discovery with Language Models](http://arxiv.org/abs/2610.07620v1)
  <details><summary>📄 Abstract</summary>
  Scientific law discovery requires selecting measurements and converting evidence into a governing equation. We evaluate an explore-then-commit protocol in which a large language model proposes hypotheses, a programmatic planner gathers measurements, and a fresh prompt synthesizes the final law from fixed observations. The protocol combines structured probes, automatic numerical diagnostics, restricted measurement batches, and optional interpreter access. Across 576 NewtonBench trials, we compare...
  </details>

- **2026-10-06** — Yi Xia, Ibrahim Khan, Mury Fajar Dewantoro et al. — [Emoception: Selective Affective Layer Fine-Tuning of Video Vision Transformers for Player Arousal Change Recognition From Gameplay Footage](http://arxiv.org/abs/2610.07603v1)
  <details><summary>📄 Abstract</summary>
  This article proposes Selective Affective Layer Fine-Tuning (SALFT), an efficient adaptation framework for Video Vision Transformers in player arousal recognition from gameplay. To bypass computationally expensive full fine-tuning, SALFT introduces a selection criterion based on the L2-norm change in layer parameters after brief adaptation, directly measuring representational shifts and providing a more stable basis than gradient-based alternatives. Evaluated via five-fold cross-validation on th...
  </details>

- **2026-10-06** — Tiago da Silva, Amauri H. Souza, Salem Lahlou — [Learning a Mixture of GFlowNets](http://arxiv.org/abs/2610.07562v1)
  <details><summary>📄 Abstract</summary>
  Learning an ensemble of GFlowNets to sample from a discrete target distribution has become a common approach for achieving better state space exploration and convergence than that of a monolithic sampler. However, these methods often add a substantial runtime overhead to the base model, and their conceptual connection remains elusive. To address this, we first propose a general-purpose theoretical framework for describing a mixture of GFlowNets, which we specialize into continuously (CI) and dis...
  </details>

- **2026-10-06** — Weiwei Wang, Yinchuan Xu, Jialu Gao et al. — [A Systematic Investigation of Bias in Large Language Models for Advertising Relevance](http://arxiv.org/abs/2610.07544v1)
  <details><summary>📄 Abstract</summary>
  Large language models (LLMs) are increasingly used to judge how well an advertisement matches a query, but the fairness of these judgments has received limited attention. We conduct a systematic study of fairness in relevance judgments made by LLMs for queries and advertisements. Our counterfactual framework examines the effects of advertiser identity and possible popularity, input language, and demographic wording. We study GPT-4o as a categorical relevance judge and a Qwen-7B model trained spe...
  </details>

- **2026-10-06** — Dani Roytburg, Daphne Ippolito — [Disentangling Models from Personas in Heterogeneous LLM Simulations](http://arxiv.org/abs/2610.07535v1)
  <details><summary>📄 Abstract</summary>
  Multi-agent simulations with large language models (LLMs) often operate networks of agents with a single base model. This overlooks the inter-model effects which may dominate engagement dynamics in real-world deployments. To show this, we simulate a heterogeneous social network powered by several different base models and show that the amount of engagement an agent receives depends more on its base model than on its assigned persona. The attraction or repulsion effects of a base model strengthen...
  </details>


## 📊 统计 / Statistics

| 分类 / Category | 论文数 / Count |
|------|--------|
| jailbreak | 667 |
| prompt-injection | 607 |
| memory-poisoning | 55 |
| tool-use-attack | 150 |
| backdoor | 505 |
| adversarial-attack | 631 |
| privacy-leakage | 4319 |
| steganography | 76 |
| misuse | 1135 |
| red-teaming | 137 |
| vulnerability | 3495 |
| defense | 3339 |
| alignment | 3112 |
| robustness | 3382 |
| watermark | 561 |
| unlearning | 111 |
| agent-safety | 62 |
| benchmark | 67 |
| survey | 393 |
| other | 9092 |

---

📚 **全部 31896 篇论文**（2022 至今）请访问 [GitHub Pages](https://ny1024.github.io/AgentSafety-Papers/) 查看完整列表、搜索与筛选。

*Generated by AgentGuard at 2026-10-08 12:40:07*