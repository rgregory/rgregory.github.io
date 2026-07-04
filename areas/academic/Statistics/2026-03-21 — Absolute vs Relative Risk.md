---
type: note
date: 2026-03-21
tags: [statistics, risk, evidence-based-thinking, critical-thinking, health-literacy]
status: active
created: 2026-03-21
---

# Absolute vs Relative Risk

Understanding the difference between absolute and relative risk is one of the most practically important concepts in statistics, medicine, and business decision-making. Confusing them is one of the most common ways people (and headlines) mislead themselves and others.

---

## The Core Distinction

**Absolute Risk (AR)** is the plain probability that something happens to a person in a group, expressed as a percentage or fraction.

**Relative Risk (RR)** is the ratio of two absolute risks — it compares the risk in one group to the risk in another group. It tells you *how many times more likely* an outcome is, but says nothing about how common the outcome is in the first place.

---

## A Concrete Example

Suppose a study tests a new drug to prevent heart attacks:

| Group | Heart Attacks | Total People | Absolute Risk |
|-------|--------------|--------------|---------------|
| Placebo | 4 | 1,000 | 0.4% |
| Drug | 2 | 1,000 | 0.2% |

- **Absolute Risk Reduction (ARR)** = 0.4% − 0.2% = **0.2%**
  - Taking the drug reduces your chance of a heart attack by 0.2 percentage points.

- **Relative Risk Reduction (RRR)** = 0.2% / 0.4% = **50%**
  - The drug cuts heart attack risk in half, *relative to the placebo group*.

Both statements are technically true. But "50% reduction in heart attacks!" sounds dramatically more impressive than "0.2% fewer heart attacks." This is why pharmaceutical advertising, news headlines, and political arguments almost always use relative risk.

---

## Number Needed to Treat (NNT)

A third way to express the same data — often the most intuitive for real-world decisions:

**NNT = 1 / ARR = 1 / 0.002 = 500**

You would need to treat **500 people** to prevent **1 heart attack**. This reframes the decision entirely: is treating 500 people (at cost, at side-effect risk) worth preventing 1 event?

---

## Why It Matters: The Headline Trap

A classic example:

> "Eating X doubles your risk of cancer Y!"

If the baseline risk is 1 in 1,000,000 (0.0001%), "doubling" it takes it to 2 in 1,000,000 (0.0002%). Relative risk = 2x (alarming). Absolute risk increase = 0.0001% (negligible).

Always ask: *doubles from what?* The relative number is meaningless without knowing the baseline.

---

## When Each Measure Is More Useful

| Situation | Better Measure | Why |
|-----------|---------------|-----|
| Comparing drugs or interventions | ARR / NNT | Forces grounding in real-world impact |
| Screening for rare diseases | RR | Helps detect signals in low-prevalence data |
| Headlines, advertising | RR (misused) | Makes small effects look big |
| Policy / cost-benefit decisions | ARR | Requires knowing how many people are actually affected |
| Understanding causation | RR | Standardizes across populations of different base rates |

---

## Quick Mental Test

When you see a risk statistic, run through these three questions:

1. What is the **baseline risk** (the absolute risk in the control or general population)?
2. Is this number **absolute** or **relative**?
3. What is the **NNT** (or number needed to harm, NNH, if the risk is negative)?

If you can't answer question 1, the statistic is incomplete and potentially misleading.

---

## Summary

| Concept | Definition | In the example |
|---------|-----------|----------------|
| Absolute Risk (AR) | Probability of outcome in a group | 0.4% vs 0.2% |
| Absolute Risk Reduction (ARR) | Difference in absolute risk between groups | 0.2% |
| Relative Risk (RR) | Ratio of risks in two groups | 0.5 (drug vs placebo) |
| Relative Risk Reduction (RRR) | How much smaller the risk is, proportionally | 50% |
| Number Needed to Treat (NNT) | How many people need the intervention to prevent one outcome | 500 |

The relative number is not wrong — it is just incomplete. Always ground it in the absolute.

---

## Connections

- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Normal Distribution|Normal Distribution]] — connected: confidence intervals around risk estimates are built using the standard error and assume a normal sampling distribution via the CLT; the width of a confidence interval is a direct expression of spread in the normal distribution
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — closely related: both are routinely reported together and both are commonly misread in headlines; p-values tell you how surprising a result is, absolute vs relative risk tells you how large it is
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — connected: large samples make tiny absolute risk reductions statistically significant; ARR and NNT are the antidote to being misled by significance in large trials
- [[02-Areas/Learning/Self-Study/Linguistics/2026-03-21 — Evidentiality in Linguistics|Evidentiality in Linguistics]] — cross-domain link: the distinction between "I saw this effect" vs "I infer this effect from data" is exactly the direct/inferential evidential contrast — the difference between AR and RR is partly about which kind of claim you are making
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-03-21 — Continuity of Care|Continuity of Care]] — applied context: the 25% mortality reduction figure in continuity research (Pereira Gray meta-analysis) is a relative risk figure; knowing the absolute risk reduction and NNT is essential to evaluate whether policy interventions are worth their cost
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] — parallel caution: just as a striking relative risk figure can mislead without the absolute baseline, a statistically significant Benford deviation can look alarming without proper context — both are screening tools, not verdicts
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] — aggregation is at the core of both concepts; pooling groups with different base rates produces misleading relative risks for the same structural reason it produces Simpson reversals; the two are different symptoms of the same underlying problem with heterogeneous group comparison
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Student's t-Distribution|Student's t-Distribution]] — t-tests are the statistical machinery behind the group comparisons that produce the risk differences discussed in this note; the t-distribution determines whether a difference in absolute risk between a treatment and control group is statistically reliable
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]] — the absolute/relative risk distinction is a specific instance of the aggregation insight: relative risk strips away the baseline (the absolute level) and reports only the ratio, operating at a higher level of abstraction that loses the grounding information; always demanding the absolute risk is the same move as Pearl's demand for an explicit causal model before interpreting an aggregate
- [[MOC/Learning]] — filed under Self-Study / Critical Thinking
- Related concepts to explore: [[Confidence Intervals]], [[2026-04-17 — Ignoring the Prior — Base Rate Neglect]], [[2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty]]
