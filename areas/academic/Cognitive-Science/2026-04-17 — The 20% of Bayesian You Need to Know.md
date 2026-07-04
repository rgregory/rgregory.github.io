---
type: note
date: "2026-04-17"
tags: [bayesian-reasoning, probability, statistics, mental-models, epistemology, cognitive-science]
status: filed
created: "2026-04-17"
---

# The 20% of Bayesian You Need to Know

A compressed reference card for Bayesian reasoning. The five ideas below cover the vast majority of practical use cases. See [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning — Updating Beliefs Under Uncertainty]] for the deeper treatment.

---

## Bayes' Theorem — the engine

$$P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}$$

| Term | Name | Meaning |
|------|------|---------|
| $P(H)$ | **Prior** | Your belief before seeing evidence |
| $P(E\|H)$ | **Likelihood** | How probable the evidence is *if* H is true |
| $P(H\|E)$ | **Posterior** | Your updated belief after seeing evidence |

---

## The 5 ideas that unlock everything

**1. Beliefs are probabilities, not true/false.**
You hold degrees of confidence, not facts. Every belief is a number between 0 and 1.

**2. Updating, not replacing.**
You don't discard your prior — you multiply it by the likelihood ratio. Strong priors require strong evidence to move.

**3. Likelihood ratio is the signal.**
$P(E|H) / P(E|\neg H)$ tells you how much evidence *discriminates*. A test that's positive equally often in sick and healthy people gives you nothing.

**4. Base rates matter brutally.**
A 99%-accurate test for a 1-in-10,000 disease gives you roughly a 1% chance you're actually sick on a positive result. Ignoring the prior is the most common Bayesian error.

**5. Sequential updating.**
Each posterior becomes the next prior. Bayesian reasoning is a loop, not a one-shot calculation — you can update continuously as evidence accumulates.

---

## The practical shortcut

When someone gives you a statistic, ask:

> *"What's the base rate, and how specific is this test?"*

Those two questions catch 80% of probabilistic reasoning errors.

---

## Connections
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning — Updating Beliefs Under Uncertainty]] — deeper treatment of priors, updating, and inference
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition — Thinking About Thinking]] — calibration and epistemic humility as Bayesian virtues; knowing when to trust your own posterior
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — the frequentist alternative that cannot answer P(H|data); base rate neglect and likelihood ratio reasoning are the same error in both frameworks
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics]] — the representativeness heuristic is the cognitive mechanism behind base rate neglect (idea #4); heuristics are fast approximations to the sequential updating in idea #5
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis]] — DDx is the clearest applied domain for all five ideas: prior = disease prevalence, likelihood = test sensitivity/specificity, base rate neglect is the most common diagnostic error
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]] — Bayesian updating is the principled solution to combining multiple imperfect evidence sources; idea #5 (sequential updating) is the formal answer to the aggregation challenge
- [[MOC/Statistics|Statistics MOC]] — probability distributions, hypothesis testing, statistical paradoxes
- [[MOC/Philosophy|Philosophy MOC]] — epistemology, degrees of belief, rationality
