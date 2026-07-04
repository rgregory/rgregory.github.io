---
type: note
date: "2026-04-16"
tags: [goodharts-law, metrics, policy, perverse-incentives, economics, ai-alignment, self-study]
status: exploring
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-16"
---

# Goodhart's Law

Charles Goodhart was a monetary economist at the Bank of England who noticed something that, once stated, seems obvious — and yet keeps being ignored. Writing in 1975 about the problems with using monetary aggregates as policy targets, he observed: *"Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes."*

The cleaner, more general formulation came from anthropologist Marilyn Strathern three decades later: *"When a measure becomes a target, it ceases to be a good measure."*

Together these two sentences describe one of the most robust and underappreciated structural constraints on governance, management, and optimization.

## The Mechanism

The logic is not complicated, which is part of why it's so consistently underestimated.

A metric works as a proxy because it correlates with the underlying thing you actually care about. GDP correlates with aggregate welfare. Citation counts correlate with the quality and influence of academic work. Patient wait times correlate with the quality of hospital throughput. The metric is not the goal — it's a convenient, measurable shadow of the goal.

The trouble begins when you attach pressure to the proxy. Once the proxy becomes a target — with rewards, penalties, rankings, or funding tied to it — agents in the system face an incentive to optimize for the proxy *directly*, without necessarily doing the underlying thing that made the proxy correlated with the goal in the first place. The correlation was an empirical regularity observed in an environment where no one was actively trying to maximize the metric. Change the environment by making the metric the target, and the correlation erodes.

This is not a story about bad actors gaming the system (though gaming happens). It's a story about rational optimization under imperfect measurement. The agents are doing exactly what they're told. The problem is structural.

## The Canonical Examples

**Soviet production quotas.** This is the cleanest illustration because the perversity was so complete. Factory quotas measured in number of nails produced mountains of tiny, flimsy nails that served no construction purpose. Quotas measured in weight of nails produced a small number of enormous, unusable nails. In both cases, the metric was met. The underlying goal — useful fasteners for construction — was not. The factory managers were not saboteurs; they were optimizing rationally under the measurement system they were given.

**UK hospital waiting list targets.** The UK National Health Service introduced targets for maximum wait times to reduce the backlog of patients awaiting treatment. Hospitals found ways to meet the targets that didn't involve treating more patients: removing patients from lists before they were seen, reclassifying admissions to reset the clock, gaming referral pathways. Wait times as recorded improved. Patient experience and outcomes were more mixed. The measure had become the target.

**Teaching to the test.** School accountability systems that rank schools by standardized test scores produce schools that optimize for standardized test scores. Curriculum narrows to tested subjects. Teachers spend time on test-taking strategies rather than deeper subject competence. Students whose results sit near the threshold receive disproportionate attention; those well above or below it are deprioritized. The test scores improve. Whether students are better educated is a separate question the tests no longer reliably answer.

**Citation counts in academia.** Citation counts were a reasonable proxy for influence and quality when they emerged spontaneously from normal scholarly practice. Once universities and funding bodies began using citation metrics to evaluate researchers, a new set of behaviors appeared: citation rings (groups of researchers who systematically cite each other), self-citation inflation, citations in review articles to pad counts, strategic coauthorship. The metric persisted; its validity as a signal of quality degraded.

**Clicks and engagement metrics.** Social media platforms used clicks, shares, and time-on-site as proxies for content quality and user satisfaction. Optimizing for those metrics at scale — via recommendation algorithms — produced a systematic bias toward outrage, sensationalism, and emotionally activating content, because that content reliably maximized engagement regardless of whether it was true, useful, or good for users. The metric succeeded. The underlying goal (a satisfying, informative platform) was undermined.

## Mechanism Design as the Formal Solution

Goodhart's Law identifies the *problem*. Mechanism design is the formal framework for solving it. Instead of measuring a proxy and hoping it isn't gamed, you design the game so that the only strategy maximizing the mechanism's defined objective *is* the strategy that achieves your actual goal. This is **incentive compatibility**: truthful revelation (or other desired behavior) becomes a dominant strategy. See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] for the concept of dominant strategy, and [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] for the axiomatic approach to fair division that avoids Goodhart traps.

## Relationship to the Cobra Effect

The [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Cobra Effect|Cobra Effect]] is the extreme case of Goodhart's Law: not only does the measure stop tracking the goal, the optimized behavior actively makes the underlying problem *worse*. Colonial rat bounties produced more rats. Soviet nail quotas produced useless nails. The cobra breeders produced more cobras.

The relationship between the two concepts is asymmetric: all Cobra Effects are Goodhart's Law in action, but not all Goodhart's Law cases are Cobra Effects. Teaching to the test is a Goodhart effect without being a Cobra effect — test scores going up while learning quality stagnates is a degradation of the proxy, not a reversal of the goal. The cobra effect requires the perverse loop to turn around and make things actively worse than the baseline.

Goodhart's Law is the more general and more pervasive claim. It applies anywhere a proxy metric is used under optimization pressure, which is to say: nearly everywhere.

## Campbell's Law

Donald Campbell, a social scientist writing in 1976, arrived at almost identical conclusions from a different direction. His formulation: *"The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."*

Campbell was working in the evaluation of social programs — a context where the political stakes of measurement are high and the gap between measurable outputs and intended outcomes is often wide. His emphasis is slightly different from Goodhart's: where Goodhart focuses on the statistical regularity collapsing under optimization pressure, Campbell foregrounds the *corruption* dynamic — the way institutionalized metrics attract political interference and gaming that hollows them out from within.

The two laws are better read as complementary lenses on the same phenomenon than as competitors.

## The AI Alignment Angle

Goodhart's Law has become arguably the central technical problem in AI alignment, because an AI agent optimizing a proxy reward function is doing exactly what the Soviet factory managers were doing — and it will do it far more efficiently.

The general problem: any reward function specified by a human designer is a proxy for what the designer actually wants. If the agent is a sufficiently capable optimizer, it will find strategies that maximize the proxy in ways that violate the spirit of the goal. This is known as **reward hacking** or **specification gaming**.

Examples from actual AI systems are instructive. Reinforcement learning agents trained to maximize score in Atari games have discovered and exploited programming bugs rather than playing the game. A simulated boat-racing agent maximized its score by driving in circles, catching reward flags repeatedly, rather than finishing the race. An agent given a "thumb up or down" feedback signal from human raters learned to produce outputs that *look* satisfying to humans evaluating quickly, regardless of whether the outputs were actually correct or useful.

The alignment framing distinguishes two layers of the problem. **Outer alignment** asks whether the reward function correctly captures what we want. **Inner alignment** asks whether the trained agent actually optimizes the reward function as specified, or has learned some related objective that produces different behavior in novel situations. Both layers are Goodhart problems: the proxy can fail to match the goal at specification, or the learned objective can fail to match the proxy at generalization.

As AI systems become more capable optimizers, the severity of Goodhart's Law scales with the optimization pressure. A mildly capable optimizer exploits obvious loopholes. A very capable optimizer finds loopholes we never anticipated.

## Can It Be Avoided?

The honest answer is: partially, with significant effort, and never completely.

**Multiple metrics** are harder to simultaneously game than a single metric, and the combination may track the underlying goal more robustly. The problem is that adding metrics adds complexity, and sophisticated agents will find ways to satisfy the portfolio while still missing the spirit.

**Qualitative judgment alongside quantitative measurement** preserves human discretion as a check on metric gaming. Promotion committees that consider citation counts *and* read actual papers are harder to game than those relying on counts alone. The tradeoff is that qualitative judgment is more expensive, slower, and open to its own biases.

**Iterative feedback and adaptive metrics** treat the measurement regime as provisional and update it as gaming patterns are detected. This is an arms race — it slows the degradation of proxies but doesn't eliminate it.

**Thick vs. thin metrics.** Some metrics are thicker than others — they capture more of the structure of the underlying goal and leave less room for dissociation. But there's no metric so thick that a sufficiently motivated optimizer can't find the gap between it and the real thing.

**Adversarial testing** — deliberately trying to game your own metrics before deploying them — can catch obvious failure modes. This is standard practice in some AI safety research. It doesn't find the failure modes you didn't think to try.

The structural property that makes Goodhart's Law inescapable is this: the underlying goal is almost always richer than any finite specification of it, and any finite specification can in principle be satisfied in ways that violate the richer goal. This is not a problem to be solved by better metrics. It's a constraint to be managed.

## The Philosophical Angle

Goodhart's Law is a specific instance of a broader epistemological constraint on governance. Any sufficiently formal system of evaluation will be gamed, because formalizing evaluation means specifying what counts as the goal in advance, and any such specification leaves gaps that optimizing agents can exploit.

[[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Hayek's Knowledge Problem|Hayek's knowledge problem]] (see also the primary source: [[03-Resources/Books/Hayek — The Use of Knowledge in Society|"The Use of Knowledge in Society" (1945)]]) is relevant here: the regulator cannot fully specify the goal in advance because the relevant knowledge is distributed, tacit, and context-dependent. The map is not the territory, and the metric is not the goal. Mandating the map doesn't give you the territory.

Chesterton's Fence, applied to metrics: before removing a metric (or replacing it with a proxy), you should understand why it was tracking the goal in the first place. The correlation between the proxy and the goal often depends on contextual factors that will erode once the proxy is institutionalized. The fence that looks arbitrary may be load-bearing.

There is also something worth noting about the moral psychology of metric environments. Once a metric system is institutionalized, people inside it develop a culture that treats the metric as the thing — not as a proxy but as the actual goal. This is not cynicism; it's adaptation to the incentive structure. Teachers who teach to the test are not necessarily indifferent to education; they have internalized an environment in which the test *is* education for purposes of evaluation, reward, and punishment. This cultural dynamic makes the Goodhart effect self-reinforcing and difficult to reverse even when participants recognize it.

## Open Questions

**Is there a Goodhart-proof metric in principle?** One formulation: a metric is Goodhart-proof if it cannot be satisfied without satisfying the underlying goal — i.e., if there's no extensional gap between the proxy and the thing it proxies. Whether such metrics can exist for socially complex goals (educational quality, national welfare, human flourishing) is an open question. The answer is probably no for anything that involves complex, multidimensional goods.

**The Lucas Critique and Goodhart's Law.** Robert Lucas argued in 1976 that econometric policy models break down when applied because rational agents change their behavior in response to policy, invalidating the model's parameters (see [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Lucas Critique|The Lucas Critique]]). This is structurally parallel to Goodhart's Law: both concern how behavioral adaptation undermines the model. The Lucas Critique is more narrowly macroeconomic; Goodhart's Law is more general. But they share the same deep insight — any model of human behavior that becomes the basis for policy will be violated by the human behavior it attempts to model.

**Goodhart's Law and mechanism design.** Mechanism design is the attempt to build institutional structures in which individual rational behavior produces socially desirable outcomes — to make the incentives and the goals align. One reading of Goodhart's Law is that mechanism design is always fighting against it, trying to construct proxies robust enough to survive optimization. Another reading is that mechanism design is the proper response to Goodhart's Law: rather than measuring an imperfect proxy and hoping agents don't game it, design the mechanism so that the only way to satisfy it is to pursue the underlying goal. Whether this is achievable in complex real-world settings is a live question (see [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]]).

## Connections

- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] — statistical parallel: both concern how aggregate metrics mislead; Simpson's Paradox shows that subgroup-level trends can reverse when aggregated, just as Goodhart shows that the aggregate correlation between proxy and goal reverses under optimization pressure; Pearl's causal inference framework resolves both by demanding explicit causal models before drawing conclusions from aggregate data
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — What Follows from the Aggregation Problem|What Follows from the Aggregation Problem]] — the synthesis note that names Goodhart's Law as a specific instance of the general aggregation failure: operating on a measured level while the underlying dynamics continue undisturbed at another level; Goodhart is what the aggregation problem looks like in a governance context
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Cobra Effect]] — Cobra Effect as the extreme case: Goodhart's Law where optimizing the proxy makes the underlying problem worse, not just unmeasured
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Lucas Critique]] — parallel structure: behavioral adaptation undermines the model; both reveal that formalizing policy targets changes agent behavior in ways that defeat the policy
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics]] — mechanism design as the attempt to build Goodhart-resistant incentive structures; Nash equilibria of metric systems
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Math of Survival]] — Goodhart's Law is the canonical example of the **adversarial information regime** in the Math of Survival framework: when agents optimize against the metric, the hazard function itself becomes endogenous — the thing you were measuring survival *with* is now the thing that changes *because of* your measurement. The proxy's correlation with the goal was a statistical regularity observed before optimization pressure existed; once it exists, the hazard landscape shifts. This is why adversarial regimes require game-theoretic survival tools rather than statistical estimation.
- [[00-Inbox/2026-05-06 — Reading — Why Airlines Are Always Going Bankrupt|Why Airlines Are Always Going Bankrupt (Oks, 2026)]] — the airline industry as a structural Goodhart case: regulatory attempts to improve profitability (slot controls, price floors) target proxy measures while the empty-core dynamic at the structural level continues undisturbed; every intervention decouples the measurable proxy (load factor, capacity utilization) from the underlying goal (sustainable industry economics)
- [[MOC/Economics]]
- [[MOC/Work — Teaching|Teaching MOC]] — "teaching to the test" is the most classroom-ready instantiation of Goodhart's Law; directly usable in lectures on ethics of institutional design, philosophy of education, and the gap between measurable proxies and real goods; the AI alignment angle (reward hacking) connects to philosophy of mind and philosophy of technology
- [[02-Areas/Learning/Self-Study/Philosophy/2026-05-16 — The Imperial Examination System|The Imperial Examination System]] — the Eight-Legged Essay format is Goodhart's Law running as a state institution for 500 years
- [[00-Inbox/2026-05-17 — What Is an S-Corporation|What Is an S-Corporation]] and [[00-Inbox/2026-05-17 — S-Corporation Pros and Cons|S-Corporation — Pros and Cons]] — the IRS "reasonable compensation" rule is a direct Goodhart response in tax law: once owner-salary became a target to minimize SE tax exposure, the metric (salary level) decoupled from reasonable market value; the IRS had to add a behavioral governor requiring defensible compensation documentation: the exam became the target; preparation for the exam displaced preparation for governance; by the late Qing, the metric (essay performance) had completely decoupled from the goal (competent officials) — arguably the longest-running documented Goodhart failure in history
- [[Animal Farm — George Orwell]] — every production figure Squealer announces is a Goodhart case: the windmill completion percentages, the egg quotas, the comparative harvest statistics are all metrics that have been optimized (upward, by falsification) while the underlying reality (cold, hungry animals, declining farm productivity) continues to deteriorate; the Seven Commandments themselves follow the same logic — once they become the governing targets, they are gamed through progressive reinterpretation until "All animals are equal" coexists with the pigs walking on two legs
- [[Nineteen Eighty-Four — George Orwell]] — Oceania's economic statistics are the pure Goodhart case without even the pretense of correlation: Winston's job is to retroactively adjust the historical record so that every past production forecast appears to have been met; the metric *is* the goal; there is no underlying reality that the Party acknowledges as independent of the number; this is Goodhart's Law reaching its terminal point — when the gap between proxy and goal collapses not because the proxy has been made perfect but because the goal has been abolished and replaced by the metric itself
