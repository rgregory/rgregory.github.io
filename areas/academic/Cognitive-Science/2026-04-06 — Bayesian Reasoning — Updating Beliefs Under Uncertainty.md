---
type: note
date: 2026-04-06
tags: [statistics, probability, epistemology, philosophy, bayesian-reasoning, inference, reasoning, frequentist]
status: filed
created: 2026-04-06T00:00:00
filed-date: 2026-04-07
location: 02-Areas/Learning/Self-Study/Cognitive-Science/
aliases: [Bayesian Reasoning, "2026-04-06 — Bayesian Reasoning"]
---

# Bayesian Reasoning — Updating Beliefs Under Uncertainty

## What It Is

Bayesian reasoning is a formal framework for updating beliefs in light of new evidence. It is named for Thomas Bayes (1701–1761), whose theorem was published posthumously in 1763 and later extended by Pierre-Simon Laplace.

**Bayes' theorem:**

$$P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}$$

| Term | Name | Meaning |
|------|------|---------|
| $P(H)$ | **Prior** | Probability of hypothesis before seeing evidence |
| $P(E\|H)$ | **Likelihood** | Probability of observing the evidence if the hypothesis is true |
| $P(H\|E)$ | **Posterior** | Updated probability after seeing evidence |
| $P(E)$ | **Marginal likelihood** | Total probability of evidence across all hypotheses (normalizing constant) |

The posterior becomes the prior for the next update. Bayesian reasoning is sequential updating.

---

## The Frequentist–Bayesian Debate

Frequentists define probability as the long-run frequency of events in repeated trials — probability is a property of the world, not of beliefs. Bayesians define probability as a degree of belief — subjective but disciplined.

The practical difference: frequentists cannot assign probability to one-off events ("what is the probability this specific patient has cancer?"); Bayesians can.

The **p-value** is a frequentist construct. It does not answer "what is the probability the hypothesis is true?" — it answers "how surprising would this data be if the null hypothesis were true?" Bayesians consider this the wrong question.

---

## Prior Sensitivity and Critique

Bayesian conclusions depend on priors, which can be subjective. Critics argue this introduces arbitrariness. Defenders respond:

1. Explicit priors are better than hidden assumptions.
2. With sufficient data, priors wash out — likelihood dominates.

Uninformative or reference priors are used when strong prior knowledge is absent.

---

## Applications

- **Spam filters** — naive Bayes classifiers
- **Medical diagnosis** — base rate × test sensitivity = posterior diagnosis probability
- **Intelligence analysis** — updating threat assessments with new signals
- **Machine learning** — Bayesian neural networks, Gaussian processes
- **Scientific inference** — Bayesian model comparison, credible intervals vs. confidence intervals

---

## Cross-Domain Connections

- **[[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis]]** — DDx is applied Bayesian inference. Prior = disease prevalence; likelihood = test sensitivity/specificity; posterior = updated diagnosis probability. Base rate neglect — the most common diagnostic error — is a failure to use the prior correctly. See [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — Ignoring the Prior — Base Rate Neglect|Ignoring the Prior — Base Rate Neglect]] for the full worked analysis including the confusion matrix, the prosecutor's fallacy, and Gigerenzen's frequency-format fix.
- **[[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]]** — The frequentist–Bayesian debate is the intellectual context for everything wrong with p-value interpretation. A p-value is not $P(H|data)$; a Bayesian credible interval is not a frequentist confidence interval.
- **[[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]]** — Bayesian updating is the principled solution to the aggregation problem: it provides a mathematically coherent method for combining multiple imperfect evidence sources into a single posterior belief.
- **[[02-Areas/Learning/Self-Study/Linguistics/2026-03-21 — Evidentiality in Linguistics|Evidentiality in Linguistics]]** — Bayesian priors can be read as formalized evidential weights. Different evidence types (direct observation vs. hearsay vs. inference) receive different likelihoods, mirroring evidential grammar distinctions.
- **[[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics]]** — Heuristics are fast approximations to Bayesian inference. The Gigerenzer–Kahneman debate: are heuristics adaptive shortcuts that approximate Bayes in natural environments, or systematic biases?
- **[[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Dual Process Theory System 1 and System 2|Dual Process Theory]]** — System 2 reasoning approximates Bayesian updating (deliberate, sequential, revision-capable); System 1 uses heuristics that sometimes violate Bayes.
- **[[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Clathrus archeri Octopus Stinkhorn|Clathrus archeri Octopus Stinkhorn]]** — The insect fails to Bayesian-update because it has only one evidential channel (olfactory); with no cross-channel prior, the posterior is fully determined by the false signal. A single-channel Bayesian agent is maximally vulnerable to deception.
- **[[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — What Follows from the Aggregation Problem|What Follows from the Aggregation Problem?]]** — Bayesian reasoning operates within a specified model; it does not select the right level of description. The aggregation problem is "the prior to the prior": before specifying likelihoods, you must ask whether your level of description even contains the phenomenon you are trying to predict. A perfectly calibrated Bayesian reasoner operating at the wrong level produces confident, coherent, and systematically wrong predictions.
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Agent Architecture Patterns|Agent Architecture Patterns]] — the feedback loop in the agent-as-process pattern is operationalized Bayesian updating: skill reliability metrics are a running posterior over "how much should I trust this skill?"; each execution is a new data point; the Learn step is the update step
- **[[02-Areas/Learning/Self-Study/Statistics/2026-05-13 — Kalman Gain|Kalman Gain]]** — the engineering instantiation of sequential Bayesian updating: the Kalman gain $K$ is the mathematically optimal weight that fuses a prior model prediction with a noisy measurement, minimizing MSE at every step; it is Bayesian updating made mechanically explicit and real-time
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-06-23 — Memory Decay and Cognitive Decline|Memory Decay and Cognitive Decline]] — spaced-repetition scheduling (SM-2, FSRS) is operationalized Bayesian updating over memory traces: each retrieval success is evidence that updates the posterior estimate of trace durability, driving a longer inter-repetition interval. The note also provides a worked medical case: estimating AD risk from plasma p-tau217 is exactly a base-rate × likelihood-ratio calculation, and the Bayesian structure of the preclinical detection problem (DIAN; A/T/N cascade) is explicit
