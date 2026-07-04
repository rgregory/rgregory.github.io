---
type: note
date: "2026-04-28"
tags: [game-theory, cooperative-games, shapley-value, fair-division, coalition-games]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Shapley Value

The Shapley Value is the answer to a deceptively simple question: **How should we divide the gains from cooperation fairly among the players who contributed to those gains?**

Unlike non-cooperative game theory (which assumes players can't make binding agreements and must be sustained by incentives), cooperative game theory assumes players **can** form binding coalitions and commit to payoff divisions. The question becomes: what division is "fair"?

The Shapley Value is the unique solution that satisfies a set of fairness axioms. It's also one of the most applied solution concepts in economics — used in cost allocation, voting, insurance, and profit distribution.

---

## Coalitional Games (Cooperative Approach)

In a **coalitional game**, players form groups (coalitions) and cooperate. The value created depends on which coalition forms.

**Formal setup**:
- **Players**: $N = \{1, 2, \ldots, n\}$
- **Coalitions**: Subsets $S \subseteq N$ (groups of players)
- **Worth function**: $v(S)$ = total value created by coalition $S$

**Constraint**: $v(\emptyset) = 0$ (the empty coalition creates no value)

**Example**: Three farmers can pool resources to irrigate:
- Farmer 1 alone can create \$10 value
- Farmer 2 alone can create \$10 value
- Farmer 3 alone can create \$15 value
- Farmers 1 and 2 together can create \$30 value (shared irrigation)
- Farmers 1 and 3 together can create \$35 value
- Farmers 2 and 3 together can create \$35 value
- All three together can create \$60 value

**The problem**: The three farmers create \$60 value together. How much should each get?

---

## Fairness Axioms

Shapley proposed four axioms that any "fair" division should satisfy:

### 1. Efficiency (Pareto Optimality)

The sum of payoffs equals the total value: $\sum_{i=1}^{n} \phi_i(v) = v(N)$

**Intuition**: All value created is distributed; nothing is left on the table, and the total doesn't exceed what the coalition can create.

### 2. Symmetry

If two players contribute identically to all coalitions, they should receive equal payoffs.

Formally: If $v(S \cup \{i\}) = v(S \cup \{j\})$ for all $S \not\ni i, j$, then $\phi_i(v) = \phi_j(v)$.

**Intuition**: Fairness requires treating symmetric players equally. If players are interchangeable, their payoffs should be.

### 3. Dummy Player Axiom

A player who contributes nothing to any coalition should receive nothing.

Formally: If $v(S \cup \{i\}) = v(S)$ for all $S$ not containing $i$, then $\phi_i(v) = 0$.

**Intuition**: A player who's marginally valuable to no coalition doesn't deserve a share. This is a "no free lunch" axiom.

### 4. Additivity

If two games are combined, the Shapley values add: $\phi(v + w) = \phi(v) + \phi(w)$.

**Intuition**: The solution is linear. Combining two allocation problems into one shouldn't change the per-problem allocation structure.

---

## The Shapley Value Formula

Shapley proved that **exactly one** solution satisfies all four axioms:

$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!(n-|S|-1)!}{n!} [v(S \cup \{i\}) - v(S)]$$

This formula can be interpreted as:

$$\phi_i(v) = \mathbb{E}_{S \sim \text{random coalition}} [v(S \cup \{i\}) - v(S)]$$

where $S$ is a uniformly random subset not containing player $i$.

**Intuition**: Player $i$'s Shapley Value is their **average marginal contribution** across all possible coalition formation orders.

### Equivalent Interpretation: Sequential Coalition Formation

Imagine players join a coalition sequentially in a random order. When player $i$ joins, they contribute $v(S \cup \{i\}) - v(S)$ to the coalition of players who joined before them (coalition $S$).

The Shapley Value is player $i$'s expected marginal contribution, averaged over all possible join orders (all $n!$ orderings).

**Why this interpretation matters**: It justifies the value as "what you can credibly claim you contributed." If players join in a random order, your contribution is what you add when you join. The Shapley Value is the average of this across all orders.

---

## Example: Three Farmers

Using the farmers' worth function from before:

| Coalition | Value |
|-----------|-------|
| $\{1\}$ | 10 |
| $\{2\}$ | 10 |
| $\{3\}$ | 15 |
| $\{1,2\}$ | 30 |
| $\{1,3\}$ | 35 |
| $\{2,3\}$ | 35 |
| $\{1,2,3\}$ | 60 |

**Marginal contributions** (what player $i$ adds to coalition $S$):

For Player 1:
- $v(\{1\}) - v(\emptyset) = 10 - 0 = 10$ (joining empty set)
- $v(\{1,2\}) - v(\{2\}) = 30 - 10 = 20$ (joining 2)
- $v(\{1,3\}) - v(\{3\}) = 35 - 15 = 20$ (joining 3)
- $v(\{1,2,3\}) - v(\{2,3\}) = 60 - 35 = 25$ (joining 2 and 3)

**Shapley Value for Player 1** (average over all 6 orderings where 1 could join 1st, 2nd, or 3rd):
- Join 1st: contribute 10 (1 ordering: 1-2-3 or 1-3-2 = 2 orderings)
- Join 2nd: contribute 20 (1 joins after either 2 or 3 = 2 orderings)
- Join 3rd: contribute 25 (1 joins last = 2 orderings)

$\phi_1(v) = \frac{1}{6}(2 \times 10 + 2 \times 20 + 2 \times 25) = \frac{1}{6}(20 + 40 + 50) = \frac{110}{6} \approx 18.33$

By symmetry, Farmer 2 also gets $\approx 18.33$ (same marginal contributions as Farmer 1).

Farmer 3 contributes more (higher values in all coalitions), so gets more: $\phi_3(v) = 60 - 2(18.33) \approx 23.34$.

Check: $18.33 + 18.33 + 23.34 = 60$ ✓

---

## Shapley Value vs. the Core

The **core** of a coalitional game is the set of allocations where no coalition can profitably defect.

An allocation $(x_1, x_2, \ldots, x_n)$ is in the core if:
1. $\sum_i x_i = v(N)$ (efficiency)
2. For all coalitions $S$: $\sum_{i \in S} x_i \geq v(S)$ (no blocking pairs)

**Difference from Shapley Value**:
- **Core**: A *set* of allocations (might be empty, might be huge)
- **Shapley Value**: A *single* allocation (always exists)

**Relationship**: The Shapley Value might or might not be in the core. If it is, it's a natural "focal point" within the core. If it's not, the Shapley Value might be unachievable (some coalition would block it).

**Example**: In the farmers' case, check if $(\phi_1, \phi_2, \phi_3) \approx (18.33, 18.33, 23.34)$ is in the core:
- Coalition $\{1,2\}$ gets 36.66, but $v(\{1,2\}) = 30$, so no blocking ✓
- Coalition $\{1,3\}$ gets 41.67, but $v(\{1,3\}) = 35$, so no blocking ✓
- Coalition $\{2,3\}$ gets 41.67, but $v(\{2,3\}) = 35$, so no blocking ✓

The Shapley Value is in the core.

---

## Applications

### Cost Allocation

A group of players shares a cost (e.g., airport landing fees split among airlines using the airport). The question: how to split the total cost fairly?

Model this as a coalitional game where $v(S)$ = cost savings from coalition $S$ sharing infrastructure (negative of shared costs).

**Example**: Three airlines share an airport with landing and operation costs. Using the Shapley Value:
- Compute the cost if only Airline 1 operates: $C_1$
- Compute the cost with 1 and 2: $C_{1,2}$ (might be less than $C_1 + C_2$ due to shared infrastructure)
- Airline 1's fair cost share: $C_1 - \phi_1(\text{savings})$

The Shapley Value gives each airline a fair "free ride" on the shared cost, proportional to their marginal contribution to infrastructure utilization.

### Voting Power

How much power does each voter have in a coalition-formation game?

Model a voting body (e.g., shareholders, committee members) where $v(S)$ = 1 if coalition $S$ can pass legislation, 0 otherwise.

The **Shapley-Shubik Index** measures voting power as the Shapley Value of this game.

**Example**: In the UN Security Council, the P5 have veto power (must be in any blocking coalition). The Shapley-Shubik Index quantifies how much more powerful they are than non-permanent members (who can't block alone but can contribute to a coalition).

### Profit Distribution

When a partnership forms (e.g., a business partnership, research collaboration), how should profits be split?

Model each partner's contribution as a coalitional game where $v(S)$ = profit the group $S$ could earn if they broke away and formed their own venture.

The Shapley Value gives each partner a fair share of the total profit, proportional to their outside option value and marginal contribution.

### Risk Pooling in Insurance

When multiple parties pool risk (self-insurance, mutual insurance, cost-sharing), the Shapley Value determines fair risk premiums.

$v(S)$ = total risk (loss potential) of coalition $S$.

Each party's fair premium is their Shapley Value contribution to total risk.

---

## Computational Complexity

Computing the Shapley Value requires summing over all $2^n$ possible coalitions, which is exponationally hard.

For $n > 20$, exact computation becomes infeasible. Approximation methods exist:
- **Monte Carlo sampling**: Sample random coalitions and estimate the average
- **Approximation algorithms**: For specific coalition structures (e.g., tree-structured coalitions), polynomial-time algorithms exist

This limits the Shapley Value's practical application in large groups, though for reasonable sizes ($n < 20$), computation is feasible.

---

## Connections to Mechanism Design and Fair Division

The Shapley Value is intimately related to mechanism design through the concept of **incentive-compatible surplus division**.

In mechanism design, if you want agents to form a coalition and share value fairly:
- Each agent should receive what they would "earn" in their best outside option
- Plus a share of the coalition's surplus, proportional to their marginal contribution
- The Shapley Value implements exactly this: each agent gets their average marginal contribution

This connects directly to [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] and the VCG mechanism (Vickrey-Clarke-Groves), which is the mechanism-design instantiation of Shapley Value thinking.

**Comparison to other mechanisms**: See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] for revenue-optimal mechanisms and [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] for stability-focused mechanisms. The Shapley Value optimizes for fairness axioms, while auctions optimize for revenue and matching optimizes for stability. [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] is another axiomatic approach to fair division, applied to two-player bargaining.

**Temporal structure**: See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Extensive-Form Games|Extensive-Form Games]] for how sequential coalition formation and information revelation affect coalitional value allocation.

---

## Key Insights

1. **Fairness is unique**: There is exactly one way to divide cooperative gains that satisfies reasonable fairness axioms (Shapley's four axioms). This provides strong normative justification.

2. **Marginal contribution justifies allocation**: The Shapley Value can be justified as "your average contribution across all coalition formation orders." This provides a process-based justification (not just axiomatic).

3. **Core vs. Shapley Value**: The Shapley Value is not always in the core, but when it is, it's a natural focal allocation. When it's not, there's tension between fairness (Shapley) and stability (core).

4. **Applicable in practice**: Voting power, cost allocation, profit distribution, and risk pooling all use Shapley Value or variants. The concept transfers to many domains.

5. **Computational complexity**: Exact computation requires summing $2^n$ terms, limiting application to moderately sized groups.

---

## Sources

- **Shapley — A Value for N-Person Games (1953)** — The foundational paper; readable despite age
- **Roth — The Shapley Value (1988)** — A comprehensive treatment with many applications
- **Osborne and Rubinstein — A Course in Game Theory** — Accessible treatment of cooperative games and Shapley Value

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] — Shapley Value and VCG mechanisms as implementations of fair surplus division
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] — Revenue division and payment mechanisms; Shapley Value for allocating auction surplus
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] — Different approach to fair division; axiomatic characterization (like Shapley)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] — Fair allocation in two-sided markets; connects to stable division
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Cooperative vs. non-cooperative game theory; mechanism design applications
