---
type: note
title: ADAS — Automated Design of Agentic Systems
tags:
  - ai
  - agents
  - meta-learning
  - program-synthesis
  - self-evolving
  - iclr-2025
  - agentic-systems
status: active
created: 2026-04-19
---
# ADAS — Automated Design of Agentic Systems

ADAS (Automated Design of Agentic Systems) is a meta-learning framework presented at ICLR 2025 that automatically discovers powerful agentic system designs by learning to program better agents in code. The core insight: just as hand-designed neural network architectures were eventually replaced by learned architectures (AutoML), hand-designed agent designs can be learned automatically.

**Authors**: Shengran Hu, Cong Lu, Jeff Clune  
**Publication**: ICLR 2025

## Core Insight

In the history of machine learning, hand-designed solutions are eventually superseded by learned solutions:
- 1990s: Hand-crafted features → Learned representations (deep learning)
- 2010s: Hand-designed architectures → Learned architectures (NAS, AutoML)
- 2020s: Hand-designed agents → **Learned agent designs** (ADAS)

ADAS automates what researchers have traditionally done manually: invent novel agent components and combine them in new ways.

## The Approach: Meta Agent Search

### Core Mechanism
A **meta agent** (powered by an LLM) programs ever-better agents in code. Given that programming languages are Turing Complete, this theoretically enables learning of **any possible agentic system**:
- Novel prompts
- Tool use strategies
- Workflow structures
- Combinations of the above

### Workflow
1. **Meta agent receives**: task, current best agent, performance metrics
2. **Meta agent generates**: Python code for a new/improved agent design
3. **New agent tested** against benchmark
4. **If improved**: becomes new baseline
5. **Repeat**: meta agent generates further improvements, learns what works

### Key Property: Code-Based Representation
- Agents are defined in code, not in discrete hyperparameter spaces
- Enables fine-grained control and novel combinations
- Interpretable: humans can read and understand discovered designs
- Turing-complete expressiveness: no architectural constraints

## Experimental Results

### Domains Tested
1. **Coding tasks** (e.g., LeetCode, HumanEval)
2. **Science tasks** (e.g., protein structure prediction, chemical discovery)
3. **Mathematics** (e.g., competition math problems)

### Key Findings
- **Discovered agents outperform hand-designed SOTA** across all three domains
- **Cross-domain transfer**: Agents discovered in one domain maintain superior performance when transferred to others
- **Robustness**: Agents generalize well to new domains and models
- **Novelty**: Discovered designs include combinations and patterns not previously hand-designed

## What ADAS Discovers

The learned agents exhibit surprising design choices:

### Novel Building Blocks
- Non-standard prompting strategies (beyond "chain-of-thought" or "few-shot")
- Unusual tool use patterns and sequencing
- Creative feedback loops and self-correction mechanisms

### Workflow Innovations
- Agents that branch into multiple parallel reasoning paths
- Agents that explicitly model uncertainty and explore different hypotheses
- Agents that perform meta-reasoning (reasoning about their own reasoning)

### Emergent Complexity
- Simple individual components combine into sophisticated agents
- Similar to how neurons → networks → cognition
- Composition enables rapid capability growth

## Implications & Significance

### For AI Research
- **Paradigm shift**: Agent design becomes a learning problem, not a research problem
- **Automation of research**: Reduces manual engineering burden
- **Benchmark proliferation**: As new tasks emerge, learned agents auto-adapt

### For AI Capability
- **Capability ceiling raised**: Hand-designed agents have limits; learned agents may exceed them
- **Generalization**: Learned agents transfer across domains and models
- **Robustness**: Discovered designs may be more robust than hand-crafted ones

### For AI Safety & Alignment
- **Interpretability challenge**: Discovered agent designs may be hard to understand
- **Controllability**: How do we constrain what agents are discovered?
- **Scalability concern**: Meta agent learning scales; so does potential for misalignment

## Limitations & Open Questions

- **Computational cost**: Training the meta agent is expensive
- **Black-box optimization**: Why do certain designs work? Limited interpretability of the discovery process itself
- **Benchmark dependency**: Learned agents optimize for specific benchmarks; unclear how they generalize to truly novel domains
- **Safety & alignment**: What happens when the meta agent discovers powerful but unsafe agent designs?
- **Reproducibility**: Depends on LLM capabilities and prompting; sensitive to model version and temperature

## Connections to Vault

### Emergence & Composition
- ADAS agents exhibit [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|emergence]]: simple code building blocks combine into complex intelligent behaviors — the same dynamic described in [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Simple Rules Complex Behavior|simple rules, complex behavior]]
- No top-down design; intelligent patterns arise from bottom-up agent search — a case of [[02-Areas/Learning/Self-Study/Emergence/2026-04-04 — Complex Adaptive Systems|Complex Adaptive Systems]] dynamics, where adapting agents produce global capabilities no individual component encodes
- The discovered agent designs parallel what happens in [[02-Areas/Learning/Self-Study/Emergence/2026-04-01 — Ant Colony Intelligence — Intentional or Merely Functional|ant colony intelligence]]: Dennett's intentional stance question applies here too — do the discovered agents "understand" what they're doing, or are they sophisticated syntax machines?

### Meta-Cognition & Recursion
- Meta agent that learns to program agents is a form of **recursion**: cognition applied to cognition
- Directly instantiates the question raised by [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|metacognition]]: the meta agent monitors agent performance and adjusts — a computational version of metacognitive control
- Analogous to [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — First-Person Epistemology — Can Inner Experience Produce Knowledge|first-person epistemology]] — agents reasoning about their own reasoning
- Connects to [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — The Semantics Problem — Can Mechanism Produce Mind|the semantics problem]]: can mechanism (code synthesis) produce genuine understanding? ADAS is the sharpest empirical challenge to Searle's intuition — if the discovered agents outperform human-designed ones, the argument from Chinese Room becomes harder to sustain
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — Alan Turing|Alan Turing]]'s Church-Turing thesis is the foundation of ADAS's core claim: because programming languages are Turing-complete, the meta-agent's search space in principle covers any computable agent design
- The intentional stance question from [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — Searle Chinese Room|Searle's Chinese Room]]: when the meta-agent "discovers" a novel agent design, is it understanding the task domain, or running a powerful syntactic optimization?

### Search & Optimization
- ADAS is a form of **program synthesis via search**
- Relates to [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory — Exploration|exploration-exploitation tradeoff]]: meta agent balances trying new designs vs. refining known good ones
- Maps to [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian reasoning]]: each iteration updates the meta-agent's implicit prior over which agent architectures are worth exploring

### Convergence to Optimality
- Over many iterations, does the meta agent converge to the "globally optimal" agent design?
- Related to [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's results]]: even with infinite search, some designs may be undiscoverable from first principles — the Halting Problem places a hard ceiling on what the meta-agent can know about its own discovered agents

### Self-Improvement & Recursive Improvement
- ADAS is a step toward **recursive self-improvement**: agents that learn to improve themselves
- Extreme version: meta agent discovers an agent that itself learns to discover even better agents (recursive loop)
- Safety implications: if recursion is unbounded, capability growth becomes exponential

## Comparison to Voyager

| Aspect | Voyager | ADAS |
|--------|---------|------|
| **Domain** | Embodied agent (Minecraft, UI) | Task-agnostic (coding, science, math) |
| **Learning mechanism** | Skill library + iterative refinement | Meta-agent program synthesis |
| **Representation** | Code (skills) + LLM reasoning | Code (agents) + LLM reasoning |
| **Scalability** | Per-agent lifelong learning | Meta-level search across agents |
| **Transferability** | Skills may transfer within domain | Agents transfer across domains |
| **Interpretability** | High (skills are readable code) | Medium (agent code readable, discovery process opaque) |

## Sources

- [ADAS Paper (arXiv 2408.08435)](https://arxiv.org/abs/2408.08435)
- [ADAS GitHub](https://github.com/ShengranHu/ADAS)
- [ADAS Official Website](https://www.shengranhu.com/ADAS/)
- [ICLR 2025 Proceedings](https://proceedings.iclr.cc/)
- [OpenReview (ADAS)](https://openreview.net/forum?id=t9U3LW7JVX)

## Related Topics

- Program synthesis
- Meta-learning
- Agentic AI systems
- Recursive self-improvement
- AI alignment and safety
- Emergence and composition
