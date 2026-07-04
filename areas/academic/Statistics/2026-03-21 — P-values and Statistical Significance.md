---
type: note
date: 2026-03-21
tags: [statistics, p-values, statistical-significance, evidence-based-thinking, critical-thinking, research-literacy]
status: active
created: 2026-03-21
aliases: [P-values and Statistical Significance, P-values, P-value]
---

# P-values and Statistical Significance

The p-value is one of the most widely used — and most widely misunderstood — concepts in science, medicine, and data analysis. Understanding what it actually means (and what it does not mean) is essential for reading research, evaluating claims, and thinking clearly about evidence.

---

## What Is a P-value?

A **p-value** is the probability of obtaining a result at least as extreme as the one observed, *assuming the null hypothesis is true*.

The **null hypothesis** is the baseline assumption that there is no real effect — for example, "this drug has no impact on blood pressure" or "these two groups are the same."

So when a study reports p = 0.03, it means: *if the drug truly had no effect, there is only a 3% chance we would see results this extreme (or more extreme) by random chance alone.*

A low p-value means the data would be surprising if there were no real effect. It is evidence against the null hypothesis — not proof that the effect is real.

---

## The Conventional Threshold: p < 0.05

By convention (introduced by statistician Ronald Fisher in the 1920s), a result is typically called **statistically significant** if p < 0.05.

This threshold means: "I am willing to accept a 5% chance of a false positive (concluding there is an effect when there is none)."

This 5% cutoff is **arbitrary**. It has no mathematical special status. It became a standard because Fisher suggested it as a convenient reference point, and the scientific community crystallised around it. Many researchers now argue it is far too lenient for most purposes.

---

## What a P-value Is NOT

This is where most misunderstanding lives. A p-value is NOT:

| Common Misinterpretation | Why It's Wrong |
|--------------------------|---------------|
| "The probability the null hypothesis is true" | P-values tell you about data given a hypothesis, not about hypotheses given data. That's Bayesian logic, not frequentist. |
| "The probability the result occurred by chance" | Probability of observing the data *if* chance were operating is not the same as the probability that chance is the explanation. |
| "A measure of how large or important the effect is" | A massive study can produce tiny p-values for trivially small effects. Statistical significance ≠ practical significance. |
| "Proof that the hypothesis is true" | P < 0.05 means "unlikely under the null hypothesis" — it does not confirm the alternative hypothesis. |
| "A reproducibility guarantee" | A p < 0.05 result still fails to replicate roughly half the time in many fields. |

---

## The Relationship Between P-values and Effect Size

P-values are sensitive to **sample size**. With enough participants, almost any tiny difference becomes statistically significant.

Example:

| Study | Effect | Sample Size | P-value |
|-------|--------|-------------|---------|
| A | Drug lowers blood pressure by 1 mmHg | 10,000 | p = 0.001 |
| B | Drug lowers blood pressure by 15 mmHg | 30 | p = 0.08 |

Study A is statistically significant — but the effect is clinically meaningless. Study B misses the threshold — but the effect is clinically large (though measured imprecisely due to small sample).

**Always ask alongside p-values**: What is the effect size? What are the confidence intervals?

---

## Why P-values Matter (Despite Their Limits)

Used correctly, p-values serve a legitimate function:

1. **Controlling false positive rates** — they provide a systematic way to limit how often random noise gets mistaken for a signal in a large body of research.
2. **Filtering noise from data** — especially valuable in exploratory research where you are scanning many variables for potential leads.
3. **Standardised communication** — across studies, p-values give a shared language for expressing how surprising a result is under the null hypothesis.
4. **Pre-registration anchor** — when researchers declare a p-threshold before collecting data, it prevents retroactive threshold-shifting ("p-hacking").

The problem is not the p-value itself — it is using p < 0.05 as a binary "true/false" verdict instead of one input among several.

---

## P-hacking: How P-values Get Abused

**P-hacking** (also called "data dredging") is the practice of running many analyses until a p < 0.05 result appears by chance. Because the threshold is 5%, if you run 20 independent tests, you expect one false positive by pure luck.

Common p-hacking techniques (often unconscious):
- Stopping data collection early once p < 0.05 appears
- Adding or removing covariates until significance is achieved
- Testing multiple outcome variables and reporting only the significant one
- Splitting the data into subgroups until one is significant

**Solution**: pre-registration, replication, and treating p-values as one signal among many rather than a pass/fail gate.

---

## The Replication Crisis

Much of modern science has been shaken by the **replication crisis**: a large proportion of published findings with p < 0.05 cannot be reproduced when independent teams attempt them.

Key finding: In psychology, a 2015 replication project found only ~36–39% of results replicated with similar effect sizes. Similar problems have been documented in medicine, nutrition, and social science.

Root causes include:
- Overreliance on p < 0.05 as the sole criterion for publication
- Publication bias (journals prefer positive results)
- Small sample sizes with high variability
- P-hacking and selective reporting

---

## Better Complements and Alternatives

Rather than relying on p-values alone, strong statistical reporting includes:

| Tool | What It Adds |
|------|-------------|
| **Effect size** (Cohen's d, r, odds ratio) | How large is the effect in meaningful units? |
| **Confidence intervals** | A range of plausible values for the true effect |
| **Bayesian factors** | Directly compares the probability of data under two hypotheses |
| **Pre-registration** | Locks in hypotheses and analysis plan before data collection |
| **Replication** | The only true test of a finding's reality |
| **Power analysis** | Ensures the study is large enough to detect a real effect |

---

## A Practical Reading Heuristic

When you encounter a study result, run through this checklist:

1. What was the **p-value**? Is it close to 0.05 or far below it?
2. What is the **effect size**? Is the effect practically meaningful?
3. What are the **confidence intervals**? Are they narrow or wide?
4. What was the **sample size**? Was the study adequately powered?
5. Was the study **pre-registered**? Or was the analysis exploratory?
6. Has it been **replicated**?

A p-value is a starting point, not a verdict.

---

## Summary

| Concept | Plain English |
|---------|--------------|
| P-value | Probability of seeing this data (or more extreme) if there were no real effect |
| p < 0.05 | Conventional threshold for "statistically significant" — not a law of nature |
| Statistical significance | The result is unlikely under the null hypothesis |
| Practical significance | The result is large enough to matter in the real world |
| P-hacking | Manipulating analysis until a significant result appears |
| Effect size | How big the effect actually is, independent of sample size |

The p-value answers one narrow question: *How surprising is this data if nothing is happening?* It does not tell you whether the effect is real, important, or reproducible. Combine it with effect sizes, confidence intervals, and replication before drawing conclusions.

---

## Connections

- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Normal Distribution|Normal Distribution]] — foundational: p-values are computed by finding where a test statistic falls in a normal (or t-) distribution; the p < 0.05 threshold corresponds to values beyond ~1.96 standard deviations from the mean
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Student's t-Distribution|Student's t-Distribution]] — the t-test is the most common tool that produces the p-values discussed here; understanding the t-distribution explains why the critical threshold for significance shifts with sample size, and why small-sample p-values require larger t-statistics
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — foundational link: p-values are directly controlled by sample size; a p-value without knowing n is uninterpretable; the replication crisis connects both topics
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Absolute vs Relative Risk|Absolute vs Relative Risk]] — closely related: both concepts are often reported together and both are frequently misused in headlines
- [[02-Areas/Learning/Self-Study/Linguistics/2026-03-21 — Evidentiality in Linguistics|Evidentiality in Linguistics]] — a cross-domain parallel: evidentiality is a grammatical system for marking how you know something; p-values are a statistical system for marking how surprising a claim is — both are tools for epistemic accountability, one built into language, the other into method
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-03-21 — Continuity of Care|Continuity of Care]] — applied context: the consistency of evidence across 22/22 studies on continuity and mortality is an example of how to weight multiple studies; illustrates why replication matters more than any single p-value
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] — applied statistics in fraud and anomaly detection; Benford analysis uses chi-squared goodness-of-fit testing, making p-value literacy directly relevant to interpreting its results
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — a formal parallel: Gödel showed that no formal proof system can capture all mathematical truth; p-values are a formal procedure with the same structural limitation — the 0.05 threshold is a convention that leaves real effects invisible or falsely flags noise. Both are case studies in the limits of formalisation.
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Power Law|Power Law]] — p-value reasoning assumes normal distributions; applying it to power-law data (financial returns, network traffic, social media engagement) produces systematically wrong conclusions, because the probability of extreme events is vastly underestimated; this mismatch underlies some of the replication crisis in social science research
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] — p-values computed on aggregate data can be highly significant while concealing a Simpson reversal within subgroups; subgroup analysis and stratified testing are the methodological response; the replication crisis partly reflects aggregate analyses that did not survive disaggregation
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]] — the replication crisis is a direct consequence of the aggregation insight: p-values computed at the aggregate level (pooled across diverse studies, populations, and contexts) can be highly significant while the effect they measure is a statistical artefact of the aggregation rather than a real signal; the fix — pre-registration, stratified analysis, explicit causal models — is structurally the same fix Judea Pearl recommends for Simpson's Paradox
- [[MOC/Learning]] — filed under Self-Study / Critical Thinking
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Lindy Effect|The Lindy Effect]] — the replication crisis is the opposite of Lindy: published p < 0.05 results that fail to survive independent replication are anti-Lindy — they passed zero selection tests; a finding that has been replicated across independent teams over decades is doing exactly what Lindy predicts for robust phenomena; pre-registration and replication are the statistical equivalent of subjecting a claim to time-and-conditions selection pressure
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Clathrus archeri Octopus Stinkhorn|Clathrus archeri]] — the insect's false positive (identifying a resource where none exists) is a Type I error case; the fungus's presence reduces prior probability that carrion odor → actual carrion
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Hericium erinaceus Lion's Mane|Hericium erinaceus Lion's Mane]] — the Mori et al. (2009) study as a textbook small-N RCT case; modest effect sizes, effect reversal on discontinuation, limits of "statistically significant"
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Chitin Walls Fungal Cell Structure|Chitin Walls — Fungal Cell Structure]] — antifungal susceptibility testing and MICs are statistical constructs; "resistant" is defined by breakpoints set from population distributions
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis — Reasoning Under Uncertainty]] — sensitivity/specificity, likelihood ratios, and the base rate problem are direct applications of the same reasoning errors that produce misinterpreted p-values
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Treatment of Hypothyroidism|Treatment of Hypothyroidism]] — the TSH reference range is a population percentile artifact; the T3 supplementation debate is a small-N RCT interpretation problem
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Clinical Acronyms Internal Medicine Reference|Clinical Acronyms — Internal Medicine Reference]] — scoring tools (qSOFA, CHADSVASC, HAS-BLED) are statistical constructs; their cut-points are derived from population data with sensitivity/specificity tradeoffs
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Argyria Silver-Induced Skin Discoloration|Argyria]] — the colloidal silver supplement industry as pseudoscience; no RCTs, anecdotal testimonials, unfalsifiable claims; the same epistemological errors that produce misinterpreted p-values
- [[02-Areas/Learning/Self-Study/Biology/2026-04-06 — The Square-Cube Law|The Square-Cube Law]] — extrapolating drug efficacy from mouse models to humans involves non-linear scaling; physiological parameters that are surface-dominated at small scale become volume-dominated at large scale; this geometric fact is part of why mouse-to-human translation fails, independently of statistical issues
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]] — the frequentist–Bayesian debate is the intellectual backdrop for everything wrong with p-value interpretation. A p-value is not P(H|data) — it cannot answer "how probable is this hypothesis?" That is a Bayesian question. Bayesian credible intervals answer it directly; frequentist confidence intervals do not.
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — The 20% of Bayesian You Need to Know|The 20% of Bayesian You Need to Know]] — compressed reference card; the practical shortcut ("what's the base rate, and how specific is this test?") is the direct corrective to the most common p-value misinterpretation errors
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Confidence Intervals|Confidence Intervals]] — CIs are the recommended complement to p-values; the 95% CI excludes the null iff p < .05, so they are mathematically dual but CIs convey magnitude and precision that a bare p-value hides
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Effect Size and Cohen's d|Effect Size and Cohen's d]] — the note explicitly calls out the conflation of statistical and practical significance; Cohen's d is the antidote to large-n studies that find p < .001 for a clinically trivial effect
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Publication Bias|Publication Bias]] — the replication crisis discussed here is partly caused by publication bias: the ~1-in-20 false positive that gets published is the same 5% tolerance the p < .05 threshold encodes
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Central Limit Theorem|Central Limit Theorem]] — the CLT is the distributional justification for using z-tests and t-tests; p-values are computed from test statistics whose sampling distributions are normal by the CLT
