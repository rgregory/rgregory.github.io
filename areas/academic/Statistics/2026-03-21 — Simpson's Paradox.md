---
type: note
date: 2026-03-21
tags: [statistics, critical-thinking, evidence-based-thinking, cognitive-bias, research-literacy, statistical-reasoning]
status: active
created: 2026-03-21
---

# Simpson's Paradox

Simpson's Paradox is one of the most disorienting results in statistics: a trend that appears consistently across every subgroup of a dataset can reverse — or completely disappear — when those subgroups are combined. It is not a flaw in the data. It is a structural feature of how aggregation interacts with hidden variables. Understanding it is essential for anyone reading research, evaluating policies, or interpreting data.

---

## The Core Idea

When you combine groups that have different underlying compositions, the aggregate can mislead. The direction of a relationship can flip simply because the groups being pooled are of different sizes, or because a third variable is distributed unevenly across them.

In plain terms: **the whole can lie even when every part tells the truth.**

---

## A Classic Example: Hospital Survival Rates

Suppose two hospitals report survival rates for surgical patients:

| | Hospital A | Hospital B |
|---|---|---|
| Overall survival | 80% | 90% |

Hospital B looks clearly better. But now break it down by patient condition on arrival:

| Condition | Hospital A | Hospital B |
|---|---|---|
| Good condition | 95% | 98% |
| Poor condition | 70% | 75% |

In *both* subgroups, Hospital B has a higher survival rate. And yet Hospital A's overall rate is lower. How?

Hospital A receives far more patients in poor condition (trauma centre, complex cases). Hospital B handles mostly routine cases. When you aggregate without accounting for this, the mix of patients distorts the comparison. Hospital A may actually be the better hospital — it is achieving 70% survival in cases that Hospital B rarely sees.

**The confounding variable here is patient severity on arrival.**

---

## The UC Berkeley Admissions Case (1973)

The most famous real-world instance of Simpson's Paradox.

The University of California Berkeley was sued for gender bias in graduate admissions. The aggregate data appeared damning:

| | Applied | Admitted |
|---|---|---|
| Men | 8,442 | 44% |
| Women | 4,321 | 35% |

A 9-percentage-point gap in favour of men. Apparent discrimination.

But when researchers broke the data down by department, the picture reversed:

> In the majority of departments, women were admitted at *higher* rates than men, or at roughly equal rates.

The paradox arose because women disproportionately applied to departments with low overall acceptance rates (humanities, social sciences), while men disproportionately applied to departments with high acceptance rates (engineering, hard sciences). The aggregate masked this entirely.

**The confounding variable: which department applicants chose.**

---

## Why It Happens: The Geometry

Simpson's Paradox is not a statistical glitch — it has a clean geometric explanation.

When you draw separate regression lines for each subgroup, they slope in one direction. When you combine all the data points without distinguishing the subgroups, the resulting aggregate cloud slopes in the opposite direction.

This happens when:
1. The subgroups differ substantially in their baseline rates (e.g., one department has 10% acceptance, another has 60%)
2. The subgroups are differently sized, or the cases are unequally distributed between them
3. A third variable is correlated with both the grouping variable and the outcome

The arithmetic works out such that the weighted average of two slopes can have a different sign than either individual slope. This is not intuitive — which is exactly why the paradox bites so often.

---

## A Medical Example: Treatment Efficacy

Simpson's Paradox appears regularly in clinical data. Consider a drug trial:

| | Treated | Recovered | Recovery Rate |
|---|---|---|---|
| Men | 120 | 96 | 80% |
| Women | 80 | 64 | 80% |
| **Total** | **200** | **160** | **80%** |

Now add a control group with a different gender distribution:

| | Control | Recovered | Recovery Rate |
|---|---|---|---|
| Men | 40 | 34 | 85% |
| Women | 160 | 128 | 80% |
| **Total** | **200** | **162** | **81%** |

The treatment group recovers at 80%. The control group recovers at 81%. The treatment appears *harmful* overall. But within each sex, the treatment either matches or performs better than control.

The difference: the control group has far more women (who have a lower baseline recovery rate), inflating the control group's aggregate.

---

## The Confounding Variable: Why It Matters

The mathematical mechanism behind Simpson's Paradox is always **confounding**: a variable that is correlated with both the grouping factor and the outcome, but is not accounted for in the analysis.

In the hospital example: patient severity confounds the hospital-survival relationship.
In the Berkeley case: department choice confounds the gender-admissions relationship.
In the drug trial: sex confounds the treatment-outcome relationship.

The paradox is a symptom of inadequate stratification — of failing to control for a relevant third variable. This is why:

- Randomised controlled trials are so valuable: proper randomisation distributes confounders evenly across groups
- Observational studies are so prone to misleading aggregations
- Subgroup analysis is not optional — it is often the only way to see what is actually happening

---

## How to Detect and Avoid It

Practical steps when reading research or interpreting data:

1. **Always ask: are these groups truly comparable?** If the groups differ in composition, aggregating them is dangerous.
2. **Break data into subgroups before drawing conclusions.** Does the trend hold within each subgroup? If not, you may be seeing Simpson's Paradox.
3. **Identify potential confounders.** What third variable might be correlated with both your grouping variable and your outcome?
4. **Weight by subgroup size, not by raw totals.** When comparing rates across groups with different Ns, the raw aggregate is often misleading.
5. **Be suspicious of aggregate statistics when groups are heterogeneous.** This applies to company-wide averages, national statistics, and pooled study results alike.

---

## Simpson's Paradox Beyond Statistics

The paradox has implications well beyond academic research:

- **Business analytics**: A product's overall conversion rate can drop even as it improves in every customer segment, if the customer mix shifts toward harder-to-convert segments.
- **Sports**: A batter can have a higher batting average than a rival in each individual season, yet a lower career average overall (Wade Boggs vs. David Justice — a famous real case).
- **Education policy**: Test scores can rise in every demographic subgroup while the national average falls, if the proportion of lower-scoring demographic groups increases.
- **Security and fraud detection**: A fraud rate can appear to improve across all transaction types while the aggregate rate rises, if fraud concentrates in high-volume channels.

In each case, the error is the same: aggregating without controlling for a compositional shift.

---

## The Deeper Lesson: Causation vs Correlation in Aggregate Data

Simpson's Paradox is a vivid demonstration of why correlation in aggregate data cannot be interpreted causally without asking about structure.

Which level of analysis is the "right" one — the aggregate or the subgroups — depends entirely on your causal question. If you want to know "which hospital has better outcomes for trauma patients?", you need subgroup data. If you want to know "where should I send my routine case?", aggregate data may serve you.

The statistician Judea Pearl, in his work on causal inference, uses Simpson's Paradox as the central illustration of why we need explicit causal models — not just correlational data — to answer questions about interventions. The same data can justify opposite decisions depending on which causal model you assume.

---

## Summary

| Concept | Plain English |
|---|---|
| Simpson's Paradox | A trend present in all subgroups reverses when groups are combined |
| Confounding variable | A hidden variable that distorts the apparent relationship |
| Aggregation bias | The error of treating a combined group as if it were homogeneous |
| Why it matters | It can make effective treatments look harmful, good hospitals look bad, fair institutions look discriminatory |
| The fix | Stratify. Identify confounders. Ask whether the groups are compositionally comparable. |

The paradox is not just a statistical curiosity — it is a warning about how easily aggregate numbers mislead, even when every individual data point is accurate. The whole does not always tell you what the parts do.

---

## Connections

- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Absolute vs Relative Risk|Absolute vs Relative Risk]] — Simpson's Paradox often hides inside relative risk comparisons; pooling groups with different base rates produces misleading relative risks for the same reason it produces misleading aggregate trends; the "doubles your risk of cancer" headline trap is a milder version of the same aggregation error
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — p-values computed on aggregate data can be highly significant while concealing a Simpson reversal within subgroups; subgroup analysis and stratified testing are the methodological response; the replication crisis is partly a story of aggregate analyses that did not survive disaggregation
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-03-21 — Continuity of Care|Continuity of Care]] — the 22/22 studies finding on continuity and mortality is notable precisely because it holds across diverse subgroups and study designs; Simpson's Paradox reasoning makes the consistency of that pattern more impressive, not less
- [[MOC/Learning]] — filed under Self-Study / Statistical Reasoning / Critical Thinking
- [[MOC/Work — Teaching|Teaching MOC]] — classroom-ready illustration of why levels of description matter; the Berkeley admissions and hospital survival cases make the Aggregation Problem visceral; pairs with Goodhart's Law for a lecture on how aggregate metrics mislead
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — the sample size composition of subgroups is exactly what drives Simpson reversals; a subgroup with a small N gets swamped in aggregation, producing a misleading overall average; understanding power and sample size is a prerequisite for detecting this paradox in practice
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] — both Simpson's Paradox and Benford's Law are counter-intuitive properties of aggregated numerical data; Benford's Law describes unexpected digit distributions in natural datasets, Simpson's Paradox describes unexpected trend reversals — both are tools for fraud detection and data forensics when individual-level data is being masked by aggregation
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Normal Distribution|Normal Distribution]] — understanding how subgroup distributions interact with aggregation requires a mental model of how the normal distribution's summary statistics (mean, SD) behave when groups with different sizes and baseline rates are pooled; Simpson's Paradox is what happens when this interaction is ignored
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Student's t-Distribution|Student's t-Distribution]] — t-tests applied to pooled, compositionally heterogeneous data can produce significant results that mask a Simpson reversal; stratified t-tests — running the analysis separately within each subgroup — are the statistical remedy
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — a structural parallel: in both cases a formally valid local system (every subgroup tells a consistent story; every axiom is valid) produces a globally misleading or incomplete result when treated as a complete account; Judea Pearl's note that Simpson's Paradox requires explicit causal models echoes Gödel's insight that formal derivation alone cannot capture all truth
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem — Levels of Description]] — the synthesis note that elevates Simpson's Paradox from a statistics curiosity to a general epistemological result: the level of aggregation chosen determines the conclusion reached, and the paradox cannot be resolved by more data alone but requires an explicit causal model — a precise instance of the broader argument that every level of description has structural blind spots
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] — parallel structure: Goodhart's Law says that when a metric becomes a target the aggregate correlation between proxy and goal breaks down; Simpson's Paradox says that aggregate correlations can misrepresent what is happening at the subgroup level; both are warnings that operating purely at the aggregate level produces systematically misleading conclusions; together they explain why governance-by-metric fails even when the data is accurate
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Lucas Critique|The Lucas Critique]] — econometric policy models are built on aggregate behavioral regularities that break down when the policy environment changes — exactly a Simpson's Paradox-style aggregation error: the aggregate correlation (Phillips Curve) was driven by uncontrolled compositional factors (expectational regime) that only became visible when the subgroup structure was made explicit; the Critique is the macroeconomic instantiation of aggregating across hidden confounders
- Related concepts to explore: [[Confounding Variables]], [[Causal Inference]], [[Judea Pearl and the Do-Calculus]], [[2026-04-17 — Ignoring the Prior — Base Rate Neglect]]
