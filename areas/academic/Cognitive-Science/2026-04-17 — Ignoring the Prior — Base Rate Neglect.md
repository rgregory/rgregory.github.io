---
type: note
date: "2026-04-17"
tags: [bayesian-reasoning, base-rate-neglect, cognitive-bias, probability, epistemology, mental-models]
status: filed
created: "2026-04-17"
---

# Ignoring the Prior — Base Rate Neglect

A deep-dive companion to [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — The 20% of Bayesian You Need to Know|The 20% of Bayesian You Need to Know]].

Base rate neglect is the most common and most consequential failure mode in probabilistic reasoning. It is the mistake of treating $P(H|E)$ as though $P(H)$ does not exist — updating solely on the strength of the evidence and forgetting how rare (or common) the hypothesis was to begin with.

In Bayesian terms: you compute the posterior using only the likelihood and ignore the prior entirely.

---

## The canonical example: disease screening

**Setup:**
- A disease affects **1 in 10,000** people in the general population. $P(\text{disease}) = 0.0001$
- A diagnostic test has **99% sensitivity** (true positive rate): $P(\text{positive} | \text{disease}) = 0.99$
- The same test has **99% specificity** (true negative rate): $P(\text{negative} | \text{no disease}) = 0.99$, which means $P(\text{positive} | \text{no disease}) = 0.01$

**The intuitive answer:** You test positive. Most people immediately think: "99% accurate test — I probably have it." That answer is wrong by roughly two orders of magnitude.

**The correct calculation — build the confusion matrix first:**

Imagine testing **1,000,000** people from the general population.

|  | Has disease | Does not have disease | Total |
|--|--|--|--|
| Tests positive | **100** (true positives) | **9,999** (false positives) | **10,099** |
| Tests negative | 1 (false negative) | 989,900 (true negatives) | 989,901 |
| **Total** | **100** | **999,900** | **1,000,000** |

- True positives: $1,000,000 \times 0.0001 \times 0.99 \approx 100$
- False positives: $1,000,000 \times 0.9999 \times 0.01 \approx 9,999$

**Posterior:**

$$P(\text{disease} | \text{positive}) = \frac{100}{100 + 9{,}999} \approx \frac{100}{10{,}099} \approx 0.0099 \approx 1\%$$

A 99%-accurate test, applied to a condition with a 0.01% base rate, yields a result that is correct only about 1% of the time. The false positive problem is not a flaw in the test — it is the mathematical consequence of a tiny prior.

**Why the intuition fails:** The test result is vivid and specific. The base rate is abstract and statistical. The brain discards the abstract number and anchors on the concrete one.

---

## Why humans do this

### The representativeness heuristic (Kahneman & Tversky)

People judge the probability of an event by how closely it *resembles* a prototype or stereotype — not by its actual frequency. A positive test result "looks like" a sick person. The inference feels valid because of similarity, not because of base-rate reasoning.

This is a systematic cognitive shortcut, not a random error. The representativeness heuristic is efficient in many everyday contexts (if something looks like a dog, it probably is a dog), but it catastrophically misfires when base rates are extreme.

See [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics — Fast Rules for Good-Enough Decisions]] for the broader taxonomy of heuristics and their failure modes.

### Vividness dominates abstraction

The test result is *this specific patient*, *right now*. The prevalence rate is an aggregate statistic from a population the patient may not even identify with. The brain is wired to process concrete, narrative, individual cases with greater weight than statistical summaries — a feature that serves storytelling and social cognition but is lethal in diagnostic reasoning.

### Denominator neglect

People are worse at reasoning with percentages than with natural frequencies. "1 in 10,000" is easier to reason about than "0.01%". Expressing base rates as frequencies rather than percentages is not just a communication trick — it engages different and more reliable cognitive machinery.

---

## Where base rate neglect causes real damage

### Medical diagnosis

Screening programs for low-prevalence conditions (rare cancers, uncommon infectious diseases) produce enormous numbers of false positives even with excellent tests. Physicians who anchor on test sensitivity and ignore prevalence will over-diagnose, trigger unnecessary follow-up procedures, and cause iatrogenic harm. The correct question before ordering any test is: *"Given this patient's prior probability of having this condition, what will a positive result actually tell me?"*

See [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis — Reasoning Under Uncertainty]].

### Criminal justice — the prosecutor's fallacy

The prosecutor's fallacy is a direct application of base rate neglect in legal reasoning. The prosecutor presents $P(\text{evidence} | \text{innocent})$ as though it equals $P(\text{innocent} | \text{evidence})$. These are not the same.

Example: "The probability of a DNA match occurring by chance is 1 in a million." True. But the probability that the defendant is innocent *given* the match depends critically on the prior — how many people were in the suspect pool, how was the match discovered, was it a database trawl? A 1-in-a-million match in a database of 10 million people means you expect 10 innocent matches. The match is evidence, not proof.

$P(E|H)$ is not $P(H|E)$. Confusing the two has sent innocent people to prison.

### Security and threat detection

This is the domain most directly relevant to security operations. Every detection system — intrusion detection, fraud scoring, insider threat models, TSA screening — operates under base rate constraints. The base rate of actual threats is typically tiny. A detection algorithm with 99% accuracy applied to a population where 0.1% are actual threats will produce roughly 100 false positives for every true positive.

The operational consequence: alert fatigue, wasted analyst time, desensitization to real signals. Improving specificity (reducing false positive rate) often delivers more practical value than improving sensitivity (reducing false negative rate) in low-base-rate threat environments.

### Venture investing

A compelling pitch activates representativeness reasoning. The founders look like successful founders. The market narrative is clear. The technology is impressive. None of this changes the base rate: the vast majority of startups fail. Updating heavily on the strength of the pitch without anchoring to base rates produces systematic over-confidence in individual deals.

---

## The fix: three habits

**1. Always ask: "What's the base rate?"**

Before updating on any evidence, name the prior. How common is this condition, this event, this claim, in the relevant population? If you cannot answer this question, you do not yet have enough information to reason probabilistically about the evidence.

**2. Use natural frequencies, not percentages**

"1 in 10,000" is cognitively easier to reason about than "0.01%". When working through a base rate problem, reframe both the prior and the likelihood as frequencies applied to a concrete population of, say, 100,000 imaginary people. Build the confusion matrix. Count the cells. The posterior falls out naturally.

This reframing — called the *frequency format* — was shown by Gerd Gigerenzen to dramatically improve Bayesian reasoning performance in experimental subjects, including physicians.

**3. Build the 2x2 confusion matrix before concluding**

|  | H is true | H is false |
|--|--|--|
| E observed | True positives | False positives |
| E not observed | False negatives | True negatives |

Fill in the numbers using the base rate and the test's sensitivity and specificity. The posterior is simply: TP / (TP + FP). This mechanical step prevents the intuitive shortcut from firing.

---

## The deeper principle

Base rate neglect is not just a cognitive bias to be corrected. It is a window into a deeper epistemological failure: treating evidence as self-interpreting. Evidence never speaks for itself. Every observation arrives with a prior that gives it meaning. The same positive test result means something entirely different in a screening context (low prior) versus a diagnostic workup triggered by symptoms (higher prior). The evidence is the same; the inference differs because the starting point differs.

This is why Bayesian reasoning is not merely a statistical technique — it is an epistemological framework that forces the reasoner to make their assumptions explicit and to understand that the strength of an inference depends on where you started, not just what you observed.

---

## Connections

- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — The 20% of Bayesian You Need to Know|The 20% of Bayesian You Need to Know]] — the compressed reference card; base rate neglect is Idea #4
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning — Updating Beliefs Under Uncertainty]] — the full formal framework; base rate neglect is the most common failure mode in applying Bayes' theorem in practice
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics — Fast Rules for Good-Enough Decisions]] — the representativeness heuristic is the cognitive mechanism behind this error; Gigerenzen's frequency-format fix addresses the same failure
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Dual Process Theory System 1 and System 2|Dual Process Theory — System 1 and System 2]] — base rate neglect is a System 1 failure: vivid, specific evidence (the test result) crowds out abstract statistical priors; System 2 intervention is the correction
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition — Thinking About Thinking]] — the fix for base rate neglect is metacognitive: noticing that the representativeness heuristic is running and deliberately asking "what's the prior?" before updating
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis — Reasoning Under Uncertainty]] — the clearest applied domain; pre-test probability is the prior
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — the frequentist framework that cannot express P(H|data) directly; p-values are also routinely misread as posteriors, the same base rate error in a different costume
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Prospect Theory|Prospect Theory]] — Kahneman and Tversky's probability weighting function shows that people distort small and large probabilities systematically; the base rate neglect pattern (treating likelihoods as posteriors) and the probability weighting error (overweighting small probabilities) are both products of the same underlying non-Bayesian intuitive machinery
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-14 — The Reid Technique — Interrogation Psychology and False Confessions|The Reid Technique — Interrogation Psychology and False Confessions]] — the prosecutor's fallacy (confusing P(E|innocent) for P(innocent|E)) is base rate neglect in a legal institutional context; the BAI's high false-positive rate in deception detection is the same math as a low-specificity diagnostic test applied to a low-prevalence population
- [[02-Areas/Learning/Self-Study/Legal-US/Constitutional-Law/2026-03-21 — Why Ask for a Lawyer If You Are Innocent|Why Ask for a Lawyer If You Are Innocent]] — the prosecutor's fallacy is the formal statement of why match-to-prototype reasoning ("he acted guilty") is not posterior probability; the practical and legal implications of the same confusion
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] — anomaly detection via Benford deviation faces the same false-positive problem: a statistically significant departure from the distribution is a positive test result, not a confirmed fraud; the posterior (P(fraud|Benford deviation)) depends on the base rate of fraud in the population being screened
