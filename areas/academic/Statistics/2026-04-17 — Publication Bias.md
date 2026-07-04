---
type: note
date: "2026-04-17"
status: active
tags: [statistics, research-literacy, evidence-based-thinking, critical-thinking, self-study]
area: "[[02-Areas/Learning/Self-Study/Statistics/_index|Statistics]]"
---

# Publication Bias

**Publication bias** is the tendency for studies with positive or statistically significant results to be published at higher rates than studies with null or negative results. This distorts the published literature and inflates apparent effect sizes.

Consequence: if 20 studies test a false hypothesis at p < .05 threshold, ~1 will produce a false positive by chance. If only that study gets published, readers see "evidence" for an effect that does not exist.

## The Mechanism

Publication bias operates through several interlocking incentives:

1. **Journal editorial preference**: journals historically prefer positive results. Editors view null results as less interesting or as failures of methodology.
2. **Researcher file drawer**: researchers abandon or never write up studies that did not "work." The unpublished set of null results is called the **file drawer problem** (Rosenthal, 1979).
3. **Funding and career pressure**: researchers face incentives to produce significant results. Null findings do not advance careers or attract follow-on funding.
4. **HARKing (Hypothesising After Results are Known)**: presenting post-hoc hypotheses as a priori, which inflates type I error rates.

The combined effect: the published literature systematically overestimates effect sizes and overrepresents significant results. Meta-analyses built on this literature inherit and amplify the bias.

## The Mathematics of the Problem

Consider the file drawer scenario. Suppose 20 independent labs each test the same false null hypothesis at α = .05. By definition, each has a 5% chance of a false positive. On average, one will produce p < .05 by chance. If only that lab publishes, a reader sees one positive result with no context — and has no way to know 19 null results are unpublished. This is the **multiple comparisons problem at the literature level**.

More formally: if the probability of a study being published given a significant result is Ppub(sig) and given a null result is Ppub(null), and Ppub(sig) >> Ppub(null), then the published literature is a biased sample. The expected published effect size will be larger than the true effect size by an amount that depends on statistical power and the publication probability ratio.

## Detection Methods

**Funnel plots**: Plot effect size (x-axis) against standard error or sample size (y-axis). Under no bias, studies should scatter symmetrically around the true effect — a symmetric funnel. Asymmetry, particularly missing small studies in the bottom-left (small n, null result), suggests publication bias. Interpretation is visual and subjective; asymmetry can also arise from true heterogeneity.

**Egger's test**: Formal regression test for funnel plot asymmetry. Regresses the standardised effect (z-score) on precision (1/SE). A non-zero intercept indicates asymmetry. Underpowered for fewer than ~20 studies in a meta-analysis.

**Trim and fill**: Imputes missing studies to produce a symmetric funnel, then recalculates the pooled effect estimate. Gives a "corrected" effect size under the assumption that asymmetry is due to bias — but this assumption may not hold.

**p-curve analysis**: Examines the distribution of significant p-values (those between 0 and .05). If there is a real underlying effect, p-values should cluster near 0 (right-skewed). If results are produced by p-hacking or are false positives, p-values cluster just below .05. A flat or left-skewed p-curve is a red flag.

**Registered Reports**: A pre-registration model where journals commit to publish regardless of outcome once the methodology is approved. Eliminates publication bias at the source rather than correcting for it post hoc.

## Real-World Consequences

**The replication crisis**: A major driver of the widespread failure to replicate findings in psychology, medicine, and nutrition is that the original published effects were inflated by publication bias. When replication studies are adequately powered and unbiased, effect sizes consistently come in smaller than published.

**Medical evidence**: A systematic review of clinical trials found that industry-funded drug trials are more likely to report positive results than independently funded trials, even when controlling for design quality. The implication: drug approval evidence may be based on a biased sample of the total evidence.

**Ioannidis (2005)**: "Why Most Published Research Findings Are False" formalised the argument. With low prior probability of an effect being real, high type I error rates, and publication bias combined, the positive predictive value of a published finding can fall below 50% — even with p < .05.

## Partial Solutions

- **Pre-registration**: Researchers register hypotheses and analysis plans before data collection. Separates confirmatory from exploratory research and prevents HARKing.
- **Trial registries**: Mandatory registration of clinical trials (ClinicalTrials.gov) before patient enrolment. Allows tracking of registered-but-unpublished studies.
- **Open data and open materials**: Reduces incentive to selectively report analyses.
- **Multi-site replication by design**: Large collaborative projects (e.g., Many Labs) run the same study across many sites simultaneously, making suppression impractical.

## Connections
- [[2026-03-21 — Why Sample Sizes Matter|Why Sample Sizes Matter]] — small studies are especially subject to publication bias; underpowered studies that find effects are more likely published
- [[2026-03-21 — P-values and Statistical Significance|P-values and Statistical Significance]] — the .05 threshold creates incentives to cross it; publication bias is partly a consequence of binary significance thinking
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — a structural parallel: publication bias creates a system (the published literature) that appears internally consistent but is systematically incomplete; just as Gödel showed a formal system cannot prove all true statements about itself, the published literature cannot audit itself and cannot reveal the hidden file drawer of unpublished null results; both reflect a fundamental limit to self-contained systems
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] — publication bias is measurement gaming at scale; when p < .05 becomes the target metric, the correlation between research findings and truth breaks down; complementary to Simpson's Paradox as an illustration of how aggregate outcomes diverge from component-level reality
- [[MOC/Statistics|Statistics MOC]]
