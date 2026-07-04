---
type: note
date: "2026-04-17"
status: active
tags: [statistics, research-literacy, statistical-reasoning, evidence-based-thinking, self-study]
area: "[[02-Areas/Learning/Self-Study/Statistics/_index|Statistics]]"
---

# Effect Size and Cohen's d

**Effect size** measures the practical magnitude of a relationship or difference, independent of sample size. Statistical significance tells you *if* an effect exists; effect size tells you *how big* it is.

**Cohen's d** is the most common standardised effect size for comparing two means:
`d = (M₁ − M₂) / SD_pooled`

Conventional benchmarks (Cohen 1988): d = 0.2 (small), 0.5 (medium), 0.8 (large). These are rough guides, not universal thresholds — a "small" effect in medicine may be clinically important.

## The Cohen's d Formula in Detail

`d = (M₁ − M₂) / SD_pooled`

Where `SD_pooled = √[(SD₁² + SD₂²) / 2]` (assuming equal group sizes). For unequal groups, a weighted pooled SD is used. Cohen's d is unitless — it expresses the difference in standard deviation units, making it comparable across studies measuring entirely different things.

Example: if a cognitive training intervention raises test scores by 5 points and the pooled SD is 10 points, d = 0.5 — a medium effect by Cohen's benchmarks. If the SD were 25 points, the same 5-point gain would be d = 0.2, a small effect. The raw score tells you one thing; d tells you how large the gain is relative to natural variability.

## Cohen's Benchmarks — and Their Limitations

Conventional thresholds (Cohen 1988): d = 0.2 (small), 0.5 (medium), 0.8 (large). These are widely used but frequently misapplied. Cohen himself noted they were rough operational definitions for behavioural science with no claim to universality.

Context shifts interpretation dramatically:
- In pharmacology, d = 0.2 for a drug with no side effects may be worth pursuing.
- In psychotherapy research, d = 0.8 is roughly the benchmark for a highly effective treatment.
- In educational interventions, d = 0.4 is often treated as the "hinge point" above which effects become policy-relevant (see Hattie's meta-analyses of instruction).
- In consumer psychology, effects of d = 0.1 routinely have large commercial value at scale.

The right question is not "is this small or large by Cohen's scale?" but "is this effect meaningful given the costs, context, and alternatives?"

## Why It Matters

A study can be statistically significant with a trivially small effect (large n) or non-significant with a practically important effect (small n). Effect size breaks this conflation. The significance test answers "is there evidence of any effect?" — the effect size answers "how big is the effect?" — and these are independent questions.

The canonical illustration: a dietary intervention study with n = 50,000 finds that eating a particular food reduces systolic blood pressure by 0.3 mmHg (d ≈ 0.02, p < .0001). Highly significant; clinically irrelevant. Effect size restores the question of magnitude that p-values obscure.

## Other Effect Size Measures

Cohen's d is not the only measure. Each has a domain where it is most natural:
- **r (Pearson correlation)**: for the relationship between two continuous variables; r² gives variance explained
- **η² (eta-squared)**: for ANOVA; proportion of total variance explained by the factor
- **ω² (omega-squared)**: a less biased alternative to η² for ANOVA
- **OR and RR**: for binary outcomes in medical research; convertible to d using approximate formulas
- **Glass's Δ**: uses only the control group SD rather than pooled SD — preferred when treatment changes variability itself

Converting between measures is possible: `r = d / √(d² + 4)` and `d = 2r / √(1 − r²)`.

## Effect Size in Meta-Analysis

Effect sizes are the currency of meta-analysis. To pool results across studies, raw score differences are useless because measurements differ. Standardising to d or r puts all studies on the same scale, enabling weighted averaging. A meta-analysis finding d = 0.3 across 50 well-powered studies provides far stronger evidence than a single large study finding d = 0.6.

Critically: publication bias inflates effect size estimates in meta-analyses. Funnel plot asymmetry and p-curve methods exist precisely to detect and correct this inflation. A meta-analytic d should always be read alongside an assessment of publication bias.

## Reporting Recommendations

Best practice (per APA guidelines since 2001) is to always report effect size alongside any inferential statistic, with a confidence interval around the effect size. A t-test result should look like: *t*(48) = 3.2, *p* = .002, *d* = 0.89, 95% CI [0.33, 1.43]. The CI around d communicates the precision of the effect size estimate itself.

## Connections
- [[2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — large samples detect tiny effects; always interpret p alongside effect size
- [[2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — p conflates effect size with sample size; Cohen's d separates them
- [[2026-04-17 — Confidence Intervals|Confidence Intervals]] — report CIs around effect size estimates, not just point estimates
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — just as Gödel showed that formal systems cannot be simultaneously complete and consistent, Cohen's d reveals that statistical significance and practical significance are not the same property; you cannot know both the p-value and effect size from p-value alone — they are independent sources of truth about the data, and focusing on only one gives an incomplete picture
- [[MOC/Statistics|Statistics MOC]]
