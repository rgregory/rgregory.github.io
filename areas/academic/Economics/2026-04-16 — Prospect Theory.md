---
type: note
date: "2026-04-16"
tags: [prospect-theory, behavioral-economics, kahneman, decision-theory, loss-aversion, self-study]
status: exploring
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-16"
---

# Prospect Theory

The starting problem is simple to state: standard economic theory says people make decisions under uncertainty by maximizing *expected utility* — the probability-weighted average of outcomes, where outcomes are measured in terms of total wealth. Von Neumann and Morgenstern axiomatized this in 1944, and for decades it was taken as the normative and descriptive bedrock of rational choice under risk. The trouble is that people systematically violate it, and not randomly — the violations have structure. Kahneman and Tversky (1979) documented that structure and gave it a model. That model is Prospect Theory.

It won Kahneman the Nobel in 2002. Tversky died in 1996 and Nobels aren't awarded posthumously. The loss of Tversky is one of the recurring elegies in behavioral science — the partnership was unusually generative, and it's impossible to know what the second act would have looked like.

---

## The Problem with Expected Utility Theory

EUT makes two predictions that break empirically, again and again.

First, it predicts that preferences should be defined over *total wealth states*, not over changes. It shouldn't matter whether you gained $500 or lost $300 from a different starting point to reach the same final wealth — the utility of the outcome is the utility of the outcome. But it does matter. People are acutely sensitive to the reference point — where they started — and evaluate outcomes as gains or losses relative to that reference, not as positions on an absolute scale.

Second, EUT predicts that probability weighting is linear: twice the probability, twice the weight. But people demonstrably overweight small probabilities and underweight large ones. The result is a systematic pattern of risk attitudes that EUT cannot reproduce without ad hoc adjustments.

The classic demonstration is the Allais Paradox (1953), which showed that real choices violate the independence axiom — a foundational requirement of EUT. Kahneman and Tversky built a whole theory around why and how.

---

## The Value Function

The heart of Prospect Theory is a value function defined over *gains and losses relative to a reference point*, not over absolute wealth levels. Its shape does a lot of work.

**S-shaped**: concave for gains (each additional gain adds less value than the last — the first $100 matters more than the hundredth), and convex for losses (each additional loss hurts less than the last — the first $100 lost is more painful than the hundredth). This is diminishing sensitivity in both directions.

**Asymmetric**: the loss side is steeper than the gain side. The empirical estimate is roughly a 2:1 ratio — losing $100 hurts about twice as much as gaining $100 feels good. This is **loss aversion**, and it's the most consequential single feature of the model.

The implications are immediate. If losses loom larger than gains, then a 50-50 bet to win $100 or lose $100 is not neutral — it's negative. To accept the bet, the potential gain needs to be roughly double the potential loss. This matches what people actually require. It also explains why people hold onto losing investments too long (selling feels like locking in the loss), why employees hate wage cuts more than they love equivalent raises, and why the pain of losing a coffee mug you were just given exceeds the pleasure of winning one.

The reference point is typically the status quo — where you are now. But it can be shifted by expectations, social comparisons, or framing. This is where things get complicated and interesting.

---

## The Probability Weighting Function

EUT uses objective probabilities directly. Prospect Theory replaces them with a *weighting function* that is not linear.

The pattern: people overweight small probabilities and underweight large ones. A 1% chance gets treated as though it were 3-4%. A 99% chance gets treated as though it were somewhat less. Certainty — 100% — is treated as categorically different from near-certainty (the "certainty effect").

This single feature explains two apparently contradictory behaviors that EUT cannot jointly account for:

- **Lottery tickets**: people pay more than the expected value to play, because they overweight the tiny probability of a large win. EUT predicts this only if you assume convex utility (risk-seeking), but most people are risk-averse in most domains.
- **Insurance**: people pay more than the actuarially fair premium to insure against unlikely losses, because they overweight the small probability of a catastrophic loss.

Both behaviors, simultaneously, in the same people. EUT forces a choice between them. Prospect Theory handles both with one mechanism.

---

## The Four-Fold Pattern of Risk Attitudes

This is one of the most elegant outputs of the framework — a 2×2 grid that organizes what would otherwise look like inconsistent behavior.

|                        | **Gains**                                   | **Losses**                                    |
|------------------------|---------------------------------------------|-----------------------------------------------|
| **High probability**   | Risk-averse (take the sure gain)            | Risk-seeking (gamble to avoid certain loss)   |
| **Low probability**    | Risk-seeking (lottery ticket)               | Risk-averse (buy insurance)                   |

Each cell follows from combining the value function with probability weighting:

- **Low-probability gain**: overweighted probability + small value → dream of the jackpot → risk-seeking
- **Low-probability loss**: overweighted probability + loss aversion → fear of the disaster → risk-averse (insurance)
- **High-probability gain**: certainty effect pulls toward the sure thing → risk-averse ("take the money and run")
- **High-probability loss**: loss aversion makes the certain loss unbearable → gamble to escape → risk-seeking ("I'll double down")

The last one is the most dangerous in practice. It's the pattern behind escalation of commitment, the gambler who doubles down to chase losses, the company that keeps funding a failing project rather than take the write-down. The certain loss activates risk-seeking precisely when risk-seeking is most likely to make things worse.

EUT predicts none of this four-fold variation. It produces a single risk attitude for a given utility function, not four attitudes indexed to context.

---

## Reference Dependence and Framing Effects

If outcomes are evaluated relative to a reference point, then *how you describe the reference point changes the choice* — even when the objective situation is identical. This is a framing effect, and it is one of the most robust findings in all of behavioral science.

The classic Kahneman-Tversky example: a disease is expected to kill 600 people. Two programs are proposed.

- Program A: saves 200 lives for certain.
- Program B: 1/3 probability of saving all 600, 2/3 probability of saving no one.

Most people choose A. Now reframe:

- Program C: 400 people will die for certain.
- Program D: 1/3 probability no one dies, 2/3 probability all 600 die.

Most people choose D. A and C are identical outcomes. B and D are identical outcomes. The framing — gains (lives saved) vs. losses (deaths) — reverses the preference. EUT says this is irrational. Prospect Theory explains it: the gain frame activates risk-aversion (take the sure gain); the loss frame activates risk-seeking (gamble to avoid certain loss).

This has enormous practical implications. "90% survival rate" and "10% mortality rate" are the same number. They don't produce the same decision. This is why pharmaceutical companies, politicians, and lawyers care about framing — not as manipulation per se, but because framing is constitutive of how people evaluate options, not a gloss on top of it.

---

## The Endowment Effect and Status Quo Bias

Loss aversion applied to ownership produces the **endowment effect**: people demand significantly more to give something up than they would have paid to acquire it in the first place. Thaler's classic mug experiments showed this reliably — sellers valued mugs at roughly twice what buyers were willing to pay, even immediately after random assignment.

The implication for economic theory is uncomfortable. Standard theory predicts that initial allocation of goods shouldn't matter — people will trade until they reach the efficient allocation regardless of who started with what (the Coase theorem). The endowment effect says allocation *does* matter, because giving something up hurts more than gaining it helps. Trades that look mutually beneficial from the outside may not happen because the loss looms larger for the holder than the gain does for the potential buyer.

**Status quo bias** is the institutional version: people systematically prefer the current state of affairs and require more to change it than the change is worth. Defaults are disproportionately sticky — not because of inertia or ignorance, but because departing from the default feels like a loss. This is the mechanism behind nudge theory: if defaults are sticky because of loss aversion, choosing better defaults is a powerful policy lever that doesn't restrict choice.

---

## Critiques and Refinements

The first and most important critique: Prospect Theory is **descriptive, not normative**. It describes how people actually choose, not how they should choose. Kahneman and Tversky were explicit about this — the theory doesn't recommend that you overweight small probabilities, it explains why you do. This means it doesn't replace the need for normative rational-choice theory; it sits alongside it.

The harder problem: **what determines the reference point?** In a laboratory experiment, you can control it. In the real world, reference points shift based on expectations, social comparisons, recent events, and framing by others. A trader who was up 20% and is now up 10% is experiencing a loss, even though they're still ahead. An employee who expected a bonus and didn't get one is experiencing a loss, even though their salary is unchanged. The theory predicts *given* a reference point, but is underspecified about where reference points come from.

**Cumulative Prospect Theory** (Tversky & Kahneman, 1992) is the main refinement. The original formulation had technical problems — it could produce violations of stochastic dominance (predicting preferences for objectively worse lotteries). CPT fixes this by applying probability weighting to cumulative distributions rather than individual outcomes. This is the version that theoretical economists actually use when embedding behavioral findings into formal models.

The deeper critique is harder to dismiss: if the theory is a collection of empirical patterns rather than a unified mechanism, it risks being endlessly extensible — a patch for every anomaly — without gaining predictive power. The response is that the underlying features (loss aversion, diminishing sensitivity, probability distortion) do predict across many domains, and the framework has been tested extensively outside the original lottery experiments.

---

## Connections to Policy and Mechanism Design

Thaler and Sunstein's **nudge theory** is essentially applied Prospect Theory. If people are loss-averse and default-biased, you can improve outcomes by redesigning choice architectures: making the better choice the default (opt-out organ donation, automatic 401(k) enrollment, opt-out savings escalation). The intervention doesn't restrict freedom — it exploits the fact that loss aversion makes people inertial. Thaler won the Nobel in 2017 partly for this work.

**Behavioral mechanism design** takes this further: if you know that agents behave according to PT rather than EUT, you should design institutions that work well under those actual preferences, not under idealized ones. Auctions designed for EUT-maximizers may produce different outcomes when bidders are loss-averse. Contracts designed for standard expected utility may be systematically misread when parties weight probabilities non-linearly.

The policy implication runs in both directions. Governments can use PT to help people make better decisions (nudges). Governments can also inadvertently harm people by triggering loss aversion at the wrong moment — austerity framed as loss tends to produce different political responses than austerity framed as investment foregone.

---

## Open Questions

**Evolutionary origins of loss aversion.** The ~2:1 asymmetry may not be arbitrary. In an environment of scarcity, losses (of food, shelter, kin) are existentially more costly than equivalent gains. A system that overweights losses may have been adaptive. If so, loss aversion isn't a cognitive bug — it's a feature tuned to ancestral environments that misfires in modern ones (lotteries, insurance, financial markets). The EGT literature on risk sensitivity in foraging models makes this argument formally.

**Cultural universality.** Most Prospect Theory experiments were run on WEIRD populations (Western, Educated, Industrialized, Rich, Democratic). Cross-cultural studies show broad replication of loss aversion, but the magnitude varies. Whether the 2:1 ratio is universal or culturally contingent matters for how foundational the theory is.

**AI decision-making.** Should AI systems model human PT-style preferences (to predict behavior), or should they make decisions according to EUT (which is normatively defensible)? This is not a settled question. A recommendation engine that knows users are loss-averse can exploit that to drive engagement (framing content as "you'll miss this" rather than "here's something good"). A decision-support system should probably not amplify its users' biases. The engineering and ethics here are tangled.

---

## Key Texts

- Kahneman & Tversky — "Prospect Theory: An Analysis of Decision under Risk" (1979), *Econometrica* — the original paper; dense but worth reading the core sections directly
- Tversky & Kahneman — "Advances in Prospect Theory: Cumulative Representation of Uncertainty" (1992) — the CPT refinement
- Kahneman — *Thinking, Fast and Slow* (2011) — the accessible synthesis; Part IV covers PT and behavioral economics; System 1 framing contextualizes why these effects are so robust
- Thaler & Sunstein — *Nudge* (2008) — PT applied to policy; the practical read
- Thaler — *Misbehaving* (2015) — Thaler's intellectual autobiography; covers endowment effect, status quo bias, and the fight to get behavioral economics taken seriously

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics]] — behavioral game theory is the intersection: Ultimatum Game rejections, cooperation above Nash prediction, and the question of whether PT can be embedded in formal game-theoretic models without losing tractability
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Dual Process Theory System 1 and System 2]] — loss aversion, framing effects, and probability distortion are paradigmatic System 1 responses; Prospect Theory is largely the formal catalog of System 1's decision-making signature
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions]] — probability weighting can be read as a heuristic: treating very small probabilities as negligible or salient based on affect rather than calculation; availability heuristic inflates subjective probability of vivid rare events
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Evolutionary Game Theory]] — loss aversion may have an evolutionary explanation rooted in selection under scarcity; EGT foraging models formalize the adaptive logic of risk-sensitivity asymmetry
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — Ignoring the Prior — Base Rate Neglect|Ignoring the Prior — Base Rate Neglect]] — Prospect Theory's probability weighting (overweighting small probabilities, underweighting large ones) and base rate neglect are both systematic deviations from Bayesian calibration traceable to the same representativeness and availability machinery; the weighting function is what base rate neglect looks like formalized into a descriptive model of choice
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — What Follows from the Aggregation Problem|What Follows from the Aggregation Problem]] — framing effects in Prospect Theory are an aggregation-problem instance: the same objective situation produces opposite preferences depending on the level of description chosen (gain frame vs. loss frame); this is not irrationality in isolation — it is the aggregation problem applied to individual decision-making: the level at which options are encoded determines the conclusion reached, just as the level of statistical aggregation determines what Simpson's Paradox reveals or conceals
