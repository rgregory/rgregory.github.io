---
type: note
date: 2026-03-21
tags: [statistics, sample-size, statistical-power, evidence-based-thinking, critical-thinking, research-literacy]
status: active
created: 2026-03-21
---

# Why Sample Sizes Matter

Sample size is one of the most underappreciated variables in research. It determines whether a study can actually detect what it is trying to detect — and whether the numbers it reports are trustworthy. Reading a study without understanding its sample size is like reading a thermometer without knowing whether it was calibrated.

---

## The Core Idea: Statistical Power

**Statistical power** is the probability that a study will detect a real effect *if that effect actually exists*.

It is a function of three things:

1. **Sample size** — more participants → more power
2. **Effect size** — larger true effects are easier to detect
3. **Significance threshold** — lower thresholds (e.g., p < 0.01 vs p < 0.05) demand more evidence

A well-powered study typically targets **80% power** or higher. This means: if the effect is real, there is at least an 80% chance the study will find it and report a significant result.

An underpowered study can miss a real effect entirely. This is called a **false negative**, or **Type II error**.

---

## What Happens When Sample Sizes Are Too Small

### Problem 1: Missing Real Effects (False Negatives)

A small study testing a drug with a genuine moderate effect may produce p = 0.12 and conclude "no significant effect found." The drug works — but the study was too small to see it.

This is not a quirk. It is structurally guaranteed: with 20 participants and high natural variability, only very large effects will push through the noise to reach significance.

**Consequence**: treatments, policies, and ideas that genuinely work get dismissed because the evidence was underpowered.

### Problem 2: Inflated Effect Estimates ("Winner's Curse")

Here is the paradox: when small studies *do* find a significant result, they tend to **overestimate** the effect size. This happens because only the "lucky" samples — those that happened to capture an unusually large effect by chance — crossed the significance threshold.

This is called the **Winner's Curse** in statistics. The first study to find an effect is often the most dramatic. Replications in larger samples produce smaller, more accurate estimates.

### Problem 3: High Variability = Unreliable Estimates

With a small sample, results jump around unpredictably. The confidence intervals are wide, meaning the true effect could be anywhere in a broad range. The point estimate (the headline number) is statistically unreliable.

| Sample Size | Hypothetical 95% CI for a True Effect of 5 units |
|-------------|--------------------------------------------------|
| n = 10 | [−3, 13] — includes zero; direction uncertain |
| n = 50 | [2, 8] — positive, but imprecise |
| n = 500 | [4.2, 5.8] — tight, trustworthy |

---

## What Happens When Sample Sizes Are Too Large

Large sample sizes solve underpowering — but create a different problem: **everything becomes statistically significant**.

With 100,000 participants, a drug that lowers blood pressure by 0.1 mmHg will produce p < 0.001. The result is statistically significant. It is also clinically worthless — no doctor would prescribe a drug for a 0.1 mmHg change.

This is the direct interaction between sample size and the p-value: p-values shrink as n grows, regardless of whether the effect is meaningful.

**Rule**: Statistical significance in a large study tells you almost nothing about practical importance. Always ask for the **effect size** and **absolute numbers**, not just the p-value.

---

## Power Analysis: Planning Before You Collect

A **power analysis** is a calculation done *before* a study begins to determine how many participants are needed to detect an effect of a given size with a given level of confidence.

Inputs:
- The **minimum effect size** worth detecting (defined by the researcher)
- The desired **power** (typically 80% or 90%)
- The significance threshold (typically p < 0.05)
- The expected **variability** in the outcome

Output:
- The **required sample size**

If a study does not report a power analysis, ask: how did they decide on their sample size? If the answer is "convenience" or "whatever we could afford," the results deserve extra skepticism.

---

## The Replication Crisis Connection

The replication crisis in science — where a large fraction of published findings fail to replicate — has sample size at its root.

The typical psychology study in the pre-crisis era had around **n = 20–40 per group**. These studies were severely underpowered for detecting anything smaller than large effects. Yet most true effects in human psychology are small to medium.

When independent teams tried to replicate these findings with larger, properly powered samples, many failed. The original results were noise that had been amplified by small-sample variability and publication bias (journals prefer positive results, so underpowered studies that got lucky — false positives and inflated effects — dominated the literature).

---

## A Practical Framework for Evaluating Sample Sizes

When reading a study, ask:

| Question | What You Are Checking |
|----------|-----------------------|
| What was the sample size? | Raw scale — is it even in the right order of magnitude? |
| Was a power analysis reported? | Did the researchers plan for adequate power before collecting data? |
| What was the effect size? | A large effect found in a small study may still be real; a tiny effect found in a huge study may not matter |
| How wide are the confidence intervals? | Wide CIs = imprecise estimate; a small sample will always produce wide CIs |
| Has it been replicated? | A single small study — regardless of p-value — is weak evidence |
| What is the variability in the outcome? | High natural variability demands larger samples to see a signal |

---

## Rough Rules of Thumb

These are illustrative starting points, not universal laws:

- **n < 30** per group: adequate only for very large effects; extreme caution warranted
- **n = 30–100** per group: acceptable for medium-to-large effects; check for power analysis
- **n > 100** per group: reasonable for most social/medical research; still check effect size
- **n > 10,000**: almost any effect will reach significance; focus entirely on effect size and practical significance

Different fields have different norms. Clinical drug trials require much larger samples than laboratory studies of physics.

---

## Summary

| Concept | Plain English |
|---------|--------------|
| Statistical power | The probability of detecting a real effect if it exists |
| Type II error (false negative) | Missing a real effect because the study was too small |
| Winner's Curse | Small studies that find effects tend to overestimate them |
| Power analysis | Pre-study calculation of the required sample size |
| Large n problem | Very large studies flag trivially small effects as "significant" |

Sample size is not just a methodological detail. It determines what a study can and cannot tell you. A small study that finds nothing may have simply been blind. A large study that finds something may have found something negligible. Neither the presence nor the absence of significance is meaningful without knowing whether the study had the power to see clearly.

---

## Connections

- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Student's t-Distribution|Student's t-Distribution]] — the t-distribution is the mathematical mechanism behind sample-size sensitivity: its heavier tails at low degrees of freedom are precisely why small samples require larger effects to reach significance; the convergence to the normal distribution at n > 30 is the statistical reason why "n > 30" is a common rule of thumb
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — directly linked: p-values shrink mechanically as sample size grows; a p-value without a known n is uninterpretable; the replication crisis connects both topics
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Absolute vs Relative Risk|Absolute vs Relative Risk]] — complementary lens: large samples can make tiny absolute risk differences statistically significant; ARR and NNT are the antidote to being misled by significance in large trials
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-03-21 — Continuity of Care|Continuity of Care]] — applied context: the Pereira Gray meta-analysis pools 22 studies, which is one way to compensate for individual studies being underpowered — meta-analysis is power through aggregation
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] — the composition and relative sizes of subgroups are exactly what drives Simpson reversals; a subgroup with a small N gets swamped in aggregation and produces a misleading overall average; understanding power and sample size is a prerequisite for detecting Simpson's Paradox in practice
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Normal Distribution|Normal Distribution]] — the sampling distribution of the mean is itself a normal distribution (by the Central Limit Theorem), and the standard error is its spread; this explains mechanically why larger n produces tighter estimates — the sampling distribution narrows — and why at small n the t-distribution's heavy tails correctly model the extra uncertainty
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]] — the Winner's Curse (small studies overestimate effects) and the large-n problem (trivially small effects become significant) are both instances of the aggregation insight: the level of analysis chosen — individual study vs. meta-analysis, point estimate vs. full distribution — determines what you see; power analysis is the discipline of choosing the right level before collecting data
- [[MOC/Learning]] — filed under Self-Study / Statistics / Critical Thinking
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Lindy Effect|The Lindy Effect]] — survivor bias and small-sample errors are what produce anti-Lindy findings; the Winner's Curse means the first study to report an effect has the highest chance of overestimating it — precisely because it has passed the least selection pressure; properly powered studies with pre-registered designs are more Lindy because the methodology has itself been tested; sample size is one of the main levers that determines how much selection pressure a finding has genuinely passed
- [[02-Areas/Learning/Self-Study/Biology/2026-04-06 — The Square-Cube Law|The Square-Cube Law]] — the failure of small-scale results (cell culture, mouse models) to translate to large-scale biology is partly a geometric problem, not only a statistical one; the square-cube law changes the qualitative behavior of physiological systems at different scales; sample size is the statistical dimension of a translation problem that also has a physical dimension
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Confidence Intervals|Confidence Intervals]] — CI width is the most direct read-out of precision; the table in this note (CI widths at n=10 / 50 / 500) is the concrete illustration of what "narrowing the CI" means as n grows
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Effect Size and Cohen's d|Effect Size and Cohen's d]] — Cohen's d separates effect magnitude from sample size; this note explains the mechanism by which the two get conflated in p-values; the two notes are the paired solution to the significance/magnitude confusion
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Publication Bias|Publication Bias]] — the Winner's Curse (small studies overestimate effects) and publication bias (small studies that get lucky are published) are different faces of the same structural problem; funnel plot asymmetry is partly caused by underpowered studies
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-17 — Central Limit Theorem|Central Limit Theorem]] — the CLT is the theoretical foundation this note rests on; the "n > 30" rule of thumb marks the point where the sampling distribution of the mean is approximately normal, which is why sample size thresholds exist at all
