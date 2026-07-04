---
type: note
date: "2026-04-17"
status: active
tags: [statistics, probability, mathematics, self-study]
area: "[[02-Areas/Learning/Self-Study/Statistics/_index|Statistics]]"
---

# Log-Normal Distribution

A variable is **log-normally distributed** if its logarithm is normally distributed. Equivalently: it is the distribution of a random variable whose log is normal. Characteristic shape: right-skewed, bounded at zero, with a long upper tail.

Arises naturally from **multiplicative processes**: when many small random factors multiply together (rather than add), the result is log-normal by the multiplicative CLT.

## Mathematical Definition

If X ~ LogNormal(μ, σ²), then ln(X) ~ Normal(μ, σ²). The parameters μ and σ are the mean and standard deviation of the *logarithm* of the variable, not the variable itself. From these, the statistics of X are:

- **Mean**: e^(μ + σ²/2)
- **Median**: e^μ
- **Mode**: e^(μ − σ²)
- **Variance**: (e^(σ²) − 1) · e^(2μ + σ²)

The mean > median > mode ordering follows from the right skew. For small σ, the log-normal approaches a normal (the skew is mild). For large σ, the right tail becomes very heavy and the mean is pulled far above the typical value.

## Why Multiplicative Processes Generate Log-Normality

The [[2026-04-17 — Central Limit Theorem|Central Limit Theorem]] for sums explains the normal distribution. The analogous result for products explains the log-normal. If a quantity grows through many small multiplicative shocks — each one multiplying the current value by a random factor — then by taking logs, we convert the product to a sum:

`ln(X₁ · X₂ · ... · Xₙ) = ln(X₁) + ln(X₂) + ... + ln(Xₙ)`

By the additive CLT, this sum of logs approaches normality. Exponentiating gives a log-normal. This is why log-normality appears wherever accumulation is multiplicative rather than additive.

## Common Examples

- **Income and wealth**: wage growth is roughly multiplicative (percentage raises), producing log-normal lower and middle portions of the distribution (the very top follows a power law)
- **City and firm sizes**: growth rates of cities and firms are approximately multiplicative; Gibrat's Law states that growth rate is independent of size, directly implying log-normality
- **Biological measurements**: body weight, organ size, metabolic rates — all products of many multiplicative developmental processes
- **Latency and response times**: network latency, reaction times, and software response times are often log-normally distributed; this is why geometric means and percentile monitoring (p99, p999) are standard in systems engineering
- **Stock prices over time**: daily returns are approximately normal; prices (which are cumulative products of return factors) are approximately log-normal

## Key Properties

- **Mean > median > mode** (right-skewed): the arithmetic mean is substantially above the typical (median) value; this distinction matters for policy — average income is a poor representation of typical income
- **Multiplicative analogue of the normal**: operations that are natural for normals (addition, arithmetic mean) correspond to multiplication and geometric mean for log-normals; the **geometric mean** e^μ is the natural "central tendency"
- **Scale invariance within reason**: ratios of log-normal quantities are log-normal; this is why percentage changes (rather than absolute differences) are the right unit for log-normal variables

## Log-Normal vs Power Law: A Practical Distinction

Both distributions are right-skewed with heavy upper tails, and both arise in similar empirical domains (wealth, city sizes, network degree). In small-to-moderate samples, they can be almost indistinguishable. The key difference:

- **Log-normal**: the tail eventually becomes thin (super-exponential decay in log-log space); the distribution has all moments finite
- **Power law**: the tail decays as x^−α; if α ≤ 2, variance is infinite; if α ≤ 1, even the mean is infinite; extremely large values occur far more often

One practical test: on a log-log plot, a power law appears as a straight line. A log-normal appears as a downward-curving line (accelerating decay). But finite-sample noise makes this test unreliable. More robust is the Clauset-Shalizi-Newman statistical testing framework, which fits both distributions and uses a likelihood ratio test.

The distinction matters: a log-normal wealth distribution implies that inequality, while real, is bounded in a certain sense. A power-law distribution implies that a tiny fraction can control a disproportionate share that grows without bound as the population grows.

## Working with Log-Normal Data

The key practical implication: do not use arithmetic means and standard deviations with log-normal data. They will be heavily influenced by outliers in the right tail and will misrepresent the typical value. Instead:

- Report **geometric mean** and **geometric standard deviation** (multiplicative standard deviation)
- Work in log space for regression and modelling
- Use log-transformation before applying normal-distribution-based tests
- Interpret percentage changes (multiplicative) rather than absolute differences (additive)

## Connections
- [[2026-03-21 — Normal Distribution|Normal Distribution]] — the log-normal is derived from the normal via exponentiation
- [[2026-03-21 — Power Law|Power Law]] — both are heavy-tailed, but distinguishable: log-normal tails thin faster; hard to distinguish empirically in finite samples
- [[2026-04-17 — Central Limit Theorem|Central Limit Theorem]] — the CLT for multiplicative processes produces log-normality
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — the log-normal distribution illustrates a formal asymmetry: while the underlying log-space follows the normal distribution (complete, symmetric), the observable space (the exponentiated variable) becomes skewed and asymmetric; this parallels Gödel's insight that the same formal system can be complete in one representation yet reveal incompleteness in another; the limits of measurement emerge from the limits of the transformation itself
- [[MOC/Statistics|Statistics MOC]]
