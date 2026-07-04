---
type: note
date: "2026-04-17"
status: active
tags: [statistics, probability, mathematics, statistical-reasoning, self-study]
area: "[[02-Areas/Learning/Self-Study/Statistics/_index|Statistics]]"
---

# Central Limit Theorem

The **Central Limit Theorem (CLT)** states that the sampling distribution of the mean of a sufficiently large number of independent, identically distributed random variables approaches a normal distribution — regardless of the underlying distribution of the original variable.

This is why the normal distribution appears so pervasively in statistics: means of large samples are approximately normal even when the underlying data are skewed, bimodal, or bounded.

## Formal Statement

Let X₁, X₂, ..., Xₙ be independent and identically distributed random variables with mean μ and finite variance σ². Define the sample mean X̄ₙ = (X₁ + ... + Xₙ) / n. Then:

`√n · (X̄ₙ − μ) / σ → N(0, 1) as n → ∞`

In plain terms: the standardised sample mean converges in distribution to a standard normal, regardless of what the original distribution looked like. The convergence is in distribution, not in value — individual draws can still come from a wildly non-normal distribution.

## Key Conditions

- **Independence of observations**: the theorem fails if observations are correlated (e.g., time series with autocorrelation, clustered data)
- **Identical distribution**: all draws come from the same population; if the distribution shifts, the mean of the means need not be normal
- **Finite variance**: this is the critical and often overlooked requirement — if σ² is infinite (as with many power-law distributions with exponent α ≤ 2), the CLT does not apply and the sum does not converge to a normal
- **Sufficient sample size**: the n ≥ 30 rule of thumb is deeply context-dependent; for near-symmetric, light-tailed distributions, convergence is rapid (n = 10 may suffice); for highly skewed distributions, n = 100 or more may be needed

## Why the Normal Distribution Is Everywhere

The CLT explains what would otherwise be a mystery: why does the bell curve appear across domains as different as measurement error, human height, test scores, and molecular velocities? Because all of these are sums or averages of many small, independent contributing factors. Height is the additive result of hundreds of genetic and environmental influences. Measurement error is the sum of many tiny, independent instrument and observer errors.

This is the additive CLT. There is also a **multiplicative CLT**: when many small independent factors multiply together, the result is not normally distributed but log-normally distributed — which is why income, city sizes, and species abundances have that characteristic right-skewed shape.

## Where It Breaks Down

Two failure modes matter most in practice:

**Heavy-tailed distributions (power laws)**: When the underlying distribution has infinite variance — e.g., a Pareto distribution with exponent α ≤ 2 — sample means do not converge to a normal. Instead, the sum converges to a **Lévy stable distribution**. This matters for financial returns, internet traffic, and earthquake magnitudes. Using CLT-based tests on such data produces drastically wrong confidence intervals and p-values.

**Dependence**: If observations are correlated, the effective sample size is smaller than the actual sample size. Clustered data, time series, spatial data — all violate the independence assumption. The CLT can be extended to cover some dependence structures (martingale CLT, mixing conditions), but the standard result does not apply off-the-shelf.

## Practical Implications

The CLT is the theoretical justification for the most common statistical procedures:
- **z-tests and t-tests**: rely on the normality of sample means, not of raw data
- **Confidence intervals for means**: valid for large n even with skewed raw distributions
- **ANOVA and linear regression**: residuals need not be normally distributed for large n; the sampling distributions of coefficients are still approximately normal

It also underlies the logic of polling: a sample of ~1,000 from a population of millions gives approximately the same precision regardless of population size, because the width of the CI depends on √n, not on the population size. This surprises many people but follows directly from the CLT.

## The Generalised Central Limit Theorem

The classical CLT is a special case. The **generalised CLT** states that the only stable limiting distributions for sums of iid variables are the Lévy stable family, of which the normal is the special case with finite variance. Understanding the generalised CLT explains why power-law distributions are not merely exceptions to normality — they are the signature of a different convergence regime entirely.

## Connections
- [[2026-03-21 — Normal Distribution|Normal Distribution]] — the CLT explains why the natural limiting shape for sample means is the bell curve
- [[2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — the CLT is the theoretical foundation for why larger samples give better estimates
- [[2026-03-21 — Power Law|Power Law]] — power-law distributions are a regime where the CLT fails because variance is undefined; means diverge
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — the CLT reveals a structural limit: while individual samples can be wildly non-normal (complete and irregular at the micro level), their aggregate must be normal; just as Gödel showed that complete formal systems have unprovable truths, the CLT shows that the behavior of the whole (the sampling distribution of means) cannot be reduced to or predicted from the local behavior of parts (the original distribution); order at the macro level emerges necessarily from chaos at the micro level, but this emergent property is a kind of asymptotic incompleteness — individual samples never achieve full normality
- [[MOC/Statistics|Statistics MOC]]
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-18 — Statistics as Philosophy|Statistics as Philosophy]] — the bridge note treats the CLT as the canonical statistical expression of emergence: individual random variation aggregates into the orderly bell curve; this is the additive version of emergence — order arising without design at the macro level
