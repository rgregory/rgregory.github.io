---
type: note
date: "2026-04-28"
tags: [matching-markets, mechanism-design, game-theory, algorithmic-economics, stability]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Matching Markets

Matching markets solve a fundamentally different problem than auctions. Instead of allocating a single good to the highest bidder, matching markets allocate agents on one side (e.g., medical residents) to agents on the other side (e.g., hospitals) such that no pair of agents prefers each other to their current matches.

The innovation: **stability** becomes the primary design goal, not revenue maximization. A matching is stable if there is no "blocking pair" — a resident-hospital pair who would both prefer to match with each other rather than their current partners.

---

## The Matching Problem

### Two-Sided Markets

In a two-sided matching problem:
- **One side** (e.g., medical residents) has preferences over the other side (hospitals)
- **The other side** (hospitals) has preferences over the first side (residents)
- **Goal**: Create a matching (a pairing of residents to hospitals) such that:
  1. Each resident is matched to at most one hospital
  2. Each hospital is matched to at most one resident (if jobs are unit-capacity)
  3. No resident and hospital would both prefer to leave their current match and be together

**Historical context**: Gale and Shapley (1962) formalized this problem and proved that a stable matching always exists. This was a mathematical theorem with no immediate application. But within decades, it became one of the most important tools in applied microeconomics.

### Examples of Matching Markets

- **Medical education**: Residents match to hospitals for training positions
- **School choice**: Students match to schools; schools match to students
- **Labor markets**: Workers match to firms; firms match to workers
- **Organ donation**: Donor-recipient pairs match; chains of altruistic donors can donate for recipients they know
- **Marriage markets**: People match to spouses
- **Dating apps**: Users match to other users (one-sided or two-sided depending on the platform)

The structure differs: medical residencies are centralized (all matches determined by a single algorithm); labor markets are decentralized (workers apply to firms, firms hire workers, outcomes emerge from individual decisions).

---

## The Gale-Shapley Algorithm

Gale and Shapley discovered that a stable matching always exists. More importantly, they showed an algorithm that finds one.

### The Algorithm (from residents' perspective)

1. **Initialization**: All residents and hospitals are unmatched
2. **While** there exists an unmatched resident $r$:
   - $r$ proposes to the next hospital on their preference list
   - If the hospital is unmatched, they accept
   - If the hospital is matched, they compare $r$ to their current match:
     - If they prefer $r$, they dump their current match and accept $r$
     - If they prefer their current match, they reject $r$
3. **Terminate** when all residents are matched

### Properties

**Stability**: The resulting matching has no blocking pairs. If a resident $r$ and hospital $h$ are not matched:
- Either $r$ never proposed to $h$ (so $h$ is not on $r$'s preference list, so $r$ prefers their current match)
- Or $h$ rejected $r$ at some point (so $h$ prefers their current match to $r$)

Either way, no blocking pair exists.

**Termination**: The algorithm terminates in finite time because:
- Each resident proposes to each hospital at most once
- Each resident and hospital makes a finite number of decisions
- With $n$ residents and $m$ hospitals, the algorithm terminates in at most $nm$ rounds

**Optimality for proposers**: The Gale-Shapley matching is optimal for the side that proposes. Among all stable matchings, the resident-proposing algorithm gives each resident their best possible stable match (in the sense that no other stable matching makes a resident better off without making someone else worse off).

**Pessimality for proposees**: Conversely, each hospital gets their worst possible stable match — among all stable matchings, the proposing algorithm minimizes hospitals' outcomes.

This is a crucial insight: the mechanism design choice (who proposes?) directly determines the distribution of surplus. This connects to [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] and the observation that institutions determine outcomes.

---

## Stability vs. Efficiency

A central tension in matching theory: the stable matching might not be **Pareto efficient** (a reallocation where some agents are better off and none are worse off).

**Example**:

Residents: $r_1, r_2$  
Hospitals: $h_1, h_2$

Preferences:
- $r_1$: prefers $h_1 \succ h_2$
- $r_2$: prefers $h_2 \succ h_1$
- $h_1$: prefers $r_1 \succ r_2$
- $h_2$: prefers $r_2 \succ r_1$

Gale-Shapley (residents propose):
- $r_1$ proposes to $h_1$, accepted
- $r_2$ proposes to $h_2$, accepted
- Matching: $(r_1, h_1), (r_2, h_2)$

This is stable (no blocking pair) and Pareto efficient (no reallocation makes anyone better off).

Now add:
- $r_1$ has small preference intensity for $h_1$ (slightly prefers $h_1$ to $h_2$)
- $r_2$ has small preference intensity for $h_2$ (slightly prefers $h_2$ to $h_1$)
- $h_1$ has large preference intensity (strongly prefers $r_1$ to $r_2$)
- $h_2$ has large preference intensity (strongly prefers $r_2$ to $r_1$)

The stable matching is $(r_1, h_1), (r_2, h_2)$. But an alternative matching $(r_1, h_2), (r_2, h_1)$ would make $h_1$ and $h_2$ much better off and $r_1$ and $r_2$ slightly worse off. Stability ≠ Efficiency.

**Policy implication**: When designing a matching market, do you optimize for stability (no pair can break away) or efficiency (total welfare)? Different objectives lead to different mechanism designs.

---

## Strategic Behavior in Matching

### Preference Revelation

The Gale-Shapley algorithm assumes agents truthfully reveal their preferences. But what if they don't?

**Hospitals' incentives**: If you're proposing-side, you have an incentive to misreport preferences and exaggerate your preferences for high-quality residents (to increase your chances of being matched to them). But since the proposing side is optimized (gets their best stable match), they have no incentive to lie — lying only gives them a worse match.

**Residents' incentives**: If you're proposed-to, you might lie. If a hospital you'd actually prefer offers a match, but you claimed to prefer a different hospital, you might accept the lying claim if it helps you avoid this hospital.

**Medical residency**: In practice, residents are asked to rank hospitals in order of preference, but some residents might not rank all hospitals (or might strategically exclude hospitals). The NRMP algorithm uses a variant of Gale-Shapley and is strategy-proof for residents — truthful ranking is optimal for residents. But residents can still decline to list hospitals they'd accept.

### Boston School Choice

Boston schools were matched to students using a mechanism that was **not** strategy-proof. Under the old mechanism, parents had incentive to misreport preferences: listing a "safe" school first (even if you preferred another school) might increase your chance of being matched to your preferred school if that school was overdemanded.

**Abdulkadiroğlu and Pathak (2011)**: Showed that Boston's mechanism was creating perverse incentives. They redesigned the mechanism using a variant of Gale-Shapley that is **strategy-proof for students**: truthful preference revelation is a dominant strategy. After implementation, the percentage of students matched to their reported first-choice school increased (because parents could now safely report their true preferences).

**Lesson**: Mechanism design matters. A seemingly minor change to the matching algorithm (from Boston's mechanism to Gale-Shapley) can increase both efficiency and strategic stability by ensuring truth-telling is optimal.

---

## Applications: Kidney Exchange

One of the most striking applications of matching markets is kidney exchange. Kidney donation is altruistically motivated, but the biological constraint is that donors can only give to compatible recipients.

### The Problem

- Patient-donor pairs exist where the donor wants to give a kidney to "their" patient but they're biologically incompatible
- The donor might be compatible with another patient, and that patient's donor might be compatible with the first patient
- Chains can form: donor A gives to patient B, patient B's donor gives to patient C, etc.

### The Solution (Roth)

Alvin Roth designed kidney exchange programs (in partnership with hospitals) that:
1. Collect all registered incompatible donor-patient pairs
2. Identify cycles and chains of compatible pairs using matching algorithms
3. Execute simultaneous transplants (all surgeries happen at once to prevent people from reneging)

**Mechanism design innovation**: No money changes hands (illegal in the U.S.); the only "payment" is the transaction of giving a kidney. The mechanism must incentivize:
- Honest reporting of compatibility (via blood tests, not self-report)
- Truthful preferences (hospitals provide them)
- No strategic waiting or coordination among patients/donors

The matching algorithm handles the complexity: with hundreds of patients and donors, finding all beneficial cycles and chains requires computational matching (graph theory, combinatorial optimization).

**Impact**: Since implementation, kidney exchange has enabled thousands of transplants that wouldn't have happened otherwise. It's a textbook example of mechanism design as applied economics — designing institutions to achieve concrete human welfare improvements.

---

## Impossible Results: When Stability and Other Goals Conflict

Not all desiderata can be satisfied simultaneously in matching markets.

### Arrow's Impossibility Theorem (related but distinct)

Arrow's impossibility theorem applies to social choice (aggregating individual preferences into a collective decision). Matching markets have their own related impossibility results.

### Gale-Shapley's Limitations

The Gale-Shapley algorithm finds a stable matching, but:
- **Stability ≠ Uniqueness**: Many stable matchings might exist; Gale-Shapley finds one
- **Stability ≠ Efficiency**: A stable matching might not be Pareto efficient
- **Stability ≠ Fairness**: The algorithm is optimal for proposers, pessimal for proposees
- **Stability ≠ Incentive Compatibility**: Proposees have incentive to misreport preferences

**Roth's theorem (related)**: If a matching mechanism is strategy-proof for both sides and always produces a stable matching, then it's dictatorial (one side's preferences determine the outcome, and the other side's preferences are ignored).

This is an impossibility result: you can't have all of strategy-proofness, stability, and fairness simultaneously. You must sacrifice something.

**Policy design**: Practitioners choose which properties matter most. In kidney exchange, incentive compatibility matters less (no financial incentive to lie); in school choice, truth-telling matters more (parents can strategically misreport).

---

## Connections to Auction Theory and Mechanism Design

Matching markets and auctions are both applications of mechanism design, but they optimize for different properties:

- **Auctions** (see [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]]) emphasize revenue extraction and truth-telling (incentive compatibility)
- **Matching markets** emphasize stability (no blocking pairs) and allocation efficiency, trading off against perfect incentive compatibility

Both face the same fundamental problem: elicit information from agents who might have incentive to lie or manipulate. The solutions are context-specific:
- In auctions: design for dominant-strategy truth-telling (Vickrey mechanism)
- In matching: design for stable allocations, accepting that incentive compatibility may be imperfect

The formal framework: see [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] for IC/IR constraints, revelation principle, and impossibility results. The [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] provides a complementary approach to fair division in coalitional settings.

**Temporal structure**: See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Extensive-Form Games|Extensive-Form Games]] for sequential matching scenarios (e.g., dynamic matching where agents arrive over time) and the role of commitment.

---

## Key Insights

1. **Stability is not magic**: A stable matching avoids blocking pairs, but might be inefficient, unfair, or manipulable. Different goals require different designs.

2. **Mechanism design is applied**: Kidney exchange, school choice, medical residencies — matching markets are where theory meets practice most directly. The algorithm you choose determines the outcome.

3. **The proposer advantage is real**: Gale-Shapley is optimal for proposers, pessimal for proposees. Who proposes? That institution design choice matters enormously.

4. **Impossibility results constrain design**: You can't optimize for stability, incentive-compatibility, and efficiency simultaneously. Designers must choose tradeoffs.

5. **Information aggregation is hard**: Even with perfect algorithmic matching, incentivizing honest preference revelation is difficult. Boston schools showed this; kidney exchange avoids it.

---

## Sources

- **Gale and Shapley — College Admissions and the Stability of Marriage (1962)** — The foundational paper; surprisingly readable despite age
- **Roth — Who Gets What and Why (2015)** — Roth's own accessible account; excellent on kidney exchange and school choice
- **Abdulkadiroğlu and Pathak — Boston School Choice (2011)** — The redesign of Boston's matching mechanism and its welfare effects
- **Roth — Two-Sided Matching (with Sotomayor, 1990)** — The comprehensive treatment of two-sided matching theory

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Parent context; matching markets as the second major application of mechanism design (after auctions)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] — The formal framework (strategy-proofness, incentive compatibility, impossibility results)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] — Complementary mechanism design application; auctions vs. matching as two major design problems
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] — Fair division in coalitional games; connects to matching's fairness concerns (which agent "should" be matched to which?)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Equilibrium analysis of strategic behavior in matching
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Philosophical context on strategic interaction and rationality
