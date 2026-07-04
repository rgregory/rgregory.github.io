---
type: note
date: "2026-04-17"
status: active
tags: [statistics, probability, research-literacy, statistical-reasoning, self-study]
area: "[[02-Areas/Learning/Self-Study/Statistics/_index|Statistics]]"
---

# Confidence Intervals

A **confidence interval (CI)** is a range of values, derived from sample data, that is likely to contain the true population parameter with a specified probability (e.g., 95%). A 95% CI means that if you repeated the study many times, 95% of the constructed intervals would contain the true value — it does *not* mean there is a 95% chance the true value lies in *this specific* interval.

CIs convey both the estimate (center of the interval) and precision (width). Narrow intervals indicate high precision; wide intervals reflect high variability or small sample sizes.

## The Core Formula

For a large-sample CI around a mean:

`CI = x̄ ± z* · (σ / √n)`

Where `z*` is the critical value (1.96 for 95%), `σ` is the population standard deviation, and `n` is the sample size. When σ is unknown (the usual case), replace `z*` with a t-critical value and use the sample standard deviation `s`. The width of the interval is the **margin of error**: `z* · (s / √n)`.

This immediately shows why sample size matters: doubling `n` shrinks the interval width by a factor of √2. To halve the margin of error, you need four times the data.

## The Right and Wrong Way to Interpret a CI

The standard interpretation: **if you repeated this procedure many times**, 95% of the intervals constructed would contain the true parameter. This is a statement about the *procedure*, not about any single interval.

What a 95% CI does NOT mean:
- There is a 95% probability that the true value falls in this particular interval. (After the data are collected, the true value either is or isn't in the interval — probability doesn't apply.)
- 95% of the data lie in this range. (That would be a prediction interval, not a confidence interval.)
- The study result is "probably true." (A wide CI spanning null and practically large effects is maximally uninformative.)

The confusion often conflates CI with a **Bayesian credible interval**, which *does* state posterior probability. CIs require no prior; credible intervals require one.

## Key Concepts

- **Margin of error**: half-width of the interval; reflects both sample size and variability
- **Coverage probability**: the long-run proportion of intervals that capture the true parameter; a well-calibrated procedure achieves its nominal coverage (95%, 99%, etc.)
- **Relationship to p-values**: a 95% CI excludes the null value if and only if the two-sided p < .05 — they are mathematically dual, but the CI conveys more: effect size and precision simultaneously

## Reading CIs in Practice

CIs force you to confront effect size. Compare:
- Study A: RR = 2.0 (95% CI: 1.9–2.1) — high precision, the effect is real and consistently about 2×
- Study B: RR = 2.0 (95% CI: 0.5–8.0) — massive uncertainty; compatible with no effect or an 8× effect

Both have "RR = 2.0." Only the CI reveals that Study B tells you almost nothing. This is why reporting effect size with its CI is more informative than reporting a p-value alone.

The width of a CI is also a diagnostic for underpowered research. A study that fails to reach p < .05 but produces a CI whose upper bound includes a clinically meaningful effect has not ruled out that effect — it simply failed to measure it well enough.

## Confidence Intervals for Other Parameters

CIs extend beyond means. Any estimated parameter can have a CI constructed around it:
- **Proportions**: use the Wilson or Agresti-Coull interval rather than the normal approximation when n is small
- **Correlations**: Fisher's r-to-z transformation stabilises variance before constructing the interval
- **Hazard ratios and odds ratios**: exponentiate the CI on the log scale
- **Effect sizes (Cohen's d)**: the noncentral t-distribution is required; bootstrap methods are simpler

When a CI is reported on a log scale and then exponentiated, it will not be symmetric around the point estimate — this is expected and correct.

## Why Interval Width Communicates Evidence Quality

A narrow CI around a null result is genuine evidence of absence. A wide CI that includes zero is not the same thing — it is simply uninformative. This distinction matters enormously for interpreting negative findings: "no significant effect" with a tight CI rules out large effects; "no significant effect" with a wide CI does not.

## Connections
- [[2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — CIs and p-values are mathematically dual; CIs convey effect size and precision that p-values hide
- [[2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — larger samples narrow the CI; sample size determines precision
- [[2026-04-17 — Ignoring the Prior — Base Rate Neglect|Base Rate Neglect]] — CIs do not give posterior probabilities; misreading a CI as a Bayesian credible interval is a common base-rate error
- [[2026-03-21 — Absolute vs Relative Risk|Absolute vs Relative Risk]] — always report CIs around risk estimates; an RR of 2.0 with CI [0.9–4.4] is very different from RR 2.0 with CI [1.8–2.3]
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — the CI encodes a formal limit: no finite sample can produce a zero-width interval; precision has asymptotic bounds determined by the structure of randomness itself, just as Gödel showed that formal systems have structural limits to their completeness; the width of a CI is not a deficiency of data collection but a reflection of irreducible epistemic uncertainty
- [[02-Areas/Learning/Self-Study/Statistics/2026-05-13 — Kalman Gain|Kalman Gain]] — in Kalman filtering, the prior covariance $P^-$ and measurement noise covariance $R$ are the Kalman filter's equivalents of confidence intervals; $P_k^-$ encodes the filter's uncertainty about the state estimate (like the width of a CI), and $R$ encodes the sensor's noise (like the CI of a measurement); the Kalman gain $K$ derives the optimal blend of these two sources of uncertainty
- [[MOC/Statistics|Statistics MOC]]
