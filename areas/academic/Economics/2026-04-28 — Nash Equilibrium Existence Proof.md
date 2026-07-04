---
type: note
date: "2026-04-28"
tags: [game-theory, mathematics, fixed-points, proof]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Nash Equilibrium: Existence Proof & Mathematical Foundations

John Nash's 1951 proof that every finite game has at least one Nash Equilibrium (in mixed strategies) was not just a mathematical result. It transformed the concept of equilibrium from an interesting idea to a fundamental theorem: **equilibrium is guaranteed to exist**. This required importing a tool from topology: **Brouwer's fixed-point theorem**.

## The Existence Question

Before Nash proved it, the question was open: does equilibrium always exist? The Prisoner's Dilemma has an equilibrium. Matching Pennies has a mixed-strategy equilibrium. But was this universal?

The answer: **yes, but you need mixed strategies**. Not every game has a pure-strategy Nash Equilibrium, but every finite game has at least one Nash Equilibrium if you allow players to randomize.

## Brouwer's Fixed-Point Theorem

**Brouwer's Fixed-Point Theorem (1911)**: A continuous function from a compact, convex set to itself always has at least one fixed point.

**Mathematical statement**: Let $S$ be a non-empty, compact, convex subset of $\mathbb{R}^n$. If $f: S \to S$ is continuous, then there exists $x^* \in S$ such that $f(x^*) = x^*$.

**Intuition**: Imagine a map of your city printed on a piece of paper, placed somewhere in the city. No matter how you crumple, fold, or rotate the map (as long as it stays within the city boundaries and is continuous), there's at least one point on the map that lies exactly over the location it represents. That's the fixed point.

**Brouwer's legacy**: [[02-Areas/Learning/Self-Study/Philosophy/2026-04-28 — L.E.J. Brouwer|L.E.J. Brouwer]] (1881–1966), the Dutch mathematician and founder of intuitionism, developed this theorem as part of his larger work in topology. The theorem itself is constructively valid — it holds even in intuitionistic mathematics, where the law of excluded middle is rejected. This makes it one of the rare deep theorems that bridges classical and constructive mathematics.

### Why This Applies to Games

In a game, the "space" is the set of all possible strategy profiles. A point in this space is a complete description of what each player is doing. The "function" is the best-response correspondence: given the others' strategies, what's your best response?

The fixed point is the equilibrium: a profile of strategies where each player's strategy is a best response to the others. This is the condition for no one to want to deviate.

## Nash's Proof Strategy (1951)

**The key steps:**

### 1. Define the Strategy Space

Let $\Delta_i$ be the set of all probability distributions over player $i$'s actions. For a finite action set with $k$ actions, $\Delta_i$ is the $(k-1)$-dimensional simplex: the set of vectors $\sigma_i = (\sigma_i^1, \sigma_i^2, \ldots, \sigma_i^k)$ where $\sum_j \sigma_i^j = 1$ and $\sigma_i^j \geq 0$.

The **strategy profile space** is:
$$\Delta = \Delta_1 \times \Delta_2 \times \cdots \times \Delta_n$$

This is a non-empty, compact (closed and bounded), convex set in finite-dimensional Euclidean space.

### 2. Define the Best-Response Correspondence

For each player $i$, given the other players' strategies $\sigma_{-i}$, compute the expected payoff of each action:
$$u_i(a_i, \sigma_{-i}) = \sum_{\text{all } a_{-i}} u_i(a_i, a_{-i}) \prod_{j \neq i} \sigma_j(a_j)$$

The **best-response set** is the set of probability distributions that place weight only on actions that maximize expected payoff:
$$BR_i(\sigma_{-i}) = \left\{ \sigma_i \in \Delta_i : \sigma_i(a_i) > 0 \implies u_i(a_i, \sigma_{-i}) = \max_{a'_i} u_i(a'_i, \sigma_{-i}) \right\}$$

In words: a mixed strategy is a best response if it puts positive probability only on actions that yield the maximum expected payoff.

### 3. Construct the Fixed-Point Function

Define an auxiliary function for each player. Nash used a method called the **convex combination of best responses**:

For each player and each strategy profile, compute a "fictitious update": move a small amount toward the best-response set.

One construction:
$$f_i(\sigma) = (1 - \epsilon) \sigma_i + \epsilon \cdot \text{(projection onto } BR_i(\sigma_{-i}) \text{)}$$

This maps each strategy to a convex combination of the current strategy and a point in the best-response set. By taking a small step toward the best response (rather than jumping to it), we maintain continuity.

Define $f(\sigma) = (f_1(\sigma), f_2(\sigma), \ldots, f_n(\sigma))$.

### 4. Apply Brouwer's Theorem

The function $f: \Delta \to \Delta$ is:
- **Continuous**: the best-response correspondence is upper-hemicontinuous (the set of best responses varies continuously with the strategy profile), and we've taken a convex combination to ensure continuity
- **Maps $\Delta$ to itself**: by construction, $f(\sigma) \in \Delta$ for all $\sigma \in \Delta$

By Brouwer's Fixed-Point Theorem, $f$ has a fixed point $\sigma^* \in \Delta$ such that:
$$\sigma^* = f(\sigma^*)$$

**Philosophical connection**: Brouwer's fixed-point theorem maps game strategy spaces to themselves. This topological approach shares deep structure with [[MOC/Philosophy|philosophy of modality]] — [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — Modal Realism — David Lewis|David Lewis's Modal Realism]] asks: across all possible worlds, what equilibria exist? Both use fixed-point logic to handle infinite solution spaces. Nash's existence proof and modal realism each provide a guarantee of existence within their respective domains — Nash in games, Lewis in metaphysics of possibility.

### 5. Show the Fixed Point is a Nash Equilibrium

At a fixed point $\sigma^*$, the function doesn't move the strategy profile. This means:
$$\sigma_i^* = (1 - \epsilon) \sigma_i^* + \epsilon \cdot (\text{best response})$$

Rearranging:
$$\sigma_i^* - (1 - \epsilon) \sigma_i^* = \epsilon \cdot (\text{best response})$$
$$\epsilon \sigma_i^* = \epsilon \cdot (\text{best response})$$
$$\sigma_i^* = \text{best response}$$

So $\sigma_i^*$ is in the best-response set for all $i$. This means each player's strategy is a best response to the others' strategies — the definition of Nash Equilibrium.

## Intuition: The Graphical Approach (2-Player Case)

In a 2-player game, you can visualize the proof graphically:

1. **Horizontal axis**: Player 1's probability of playing action 1 (ranging from 0 to 1)
2. **Vertical axis**: Player 2's probability of playing action 1 (ranging from 0 to 1)
3. **Plot Player 1's best-response correspondence** as a curve (or set of curves) in this space
4. **Plot Player 2's best-response correspondence** as another curve (or set of curves)
5. **Intersections** are Nash Equilibria

For Prisoner's Dilemma:
- Player 1's best-response correspondence: always Defect (the entire bottom edge of the unit square)
- Player 2's best-response correspondence: always Defect (the entire left edge of the unit square)
- Intersection: (Defect, Defect), the bottom-left corner

For Matching Pennies:
- Player 1's best-response correspondence: if P2 plays anything other than 50-50, P1 has a pure best response (always Heads or always Tails). If P2 plays 50-50, P1 is indifferent (any mix is a best response). → The best-response curve is V-shaped with the vertex at (50, 50).
- Player 2's best-response correspondence: symmetric, also V-shaped
- Intersection: (50-50, 50-50)

## Why Existence Requires Mixed Strategies

Not every game has a pure-strategy Nash Equilibrium. This is because pure-strategy correspondences can "jump" and not intersect:

**Example: Matching Pennies**
- If Player 2 plays Heads (probability 1), Player 1's best response is Tails
- If Player 2 plays Tails (probability 1), Player 1's best response is Heads
- There's no pure action that's a best response to *both* possibilities

**But mixed strategies "smooth out" the jumps**:
- If Player 2 plays 50-50, Player 1 is indifferent between all strategies (expected payoff is 0 regardless)
- So Player 1's best response includes the 50-50 mix
- Symmetrically for Player 2
- The 50-50 profiles intersect

The geometric reason: a continuous function on a compact convex set must have a fixed point. Pure strategies jump discontinuously; mixed strategies are continuous.

## Multiple Equilibria and Refinements

Nash's proof guarantees *at least one* equilibrium. It says nothing about uniqueness. Many games have multiple equilibria:

- **Prisoner's Dilemma**: unique equilibrium (both defect)
- **Battle of the Sexes**: two pure-strategy equilibria + one mixed-strategy equilibrium
- **Coordination games**: multiple pure-strategy equilibria
- **Generic games**: often have odd numbers of equilibria (though generic is a technical term)

When multiple equilibria exist, **equilibrium selection** becomes important. Which one will players coordinate on?

**Refinements** narrow the equilibria:
- **Subgame perfect equilibrium** (for sequential games): eliminate threats that aren't credible
- **Evolutionarily stable strategy**: which equilibria are robust to invasion by nearby strategies?
- **Perfect Bayesian equilibrium**: add consistency of off-path beliefs
- **Trembling hand perfect equilibrium**: equilibria that are robust to small mistakes

## Conditions for Existence in Infinite Games

The fixed-point approach extends to infinite action sets if:
- The action space is a compact convex set (e.g., prices in $[0, \infty)$ with a bound)
- Payoff functions are continuous in strategies

Many economic models (Cournot competition, auction theory, pricing models) satisfy these. The existence theorem extends: equilibrium exists (though uniqueness requires stronger conditions).

## Philosophical Significance

The existence proof does three important things:

1. **Justifies the concept**: Nash Equilibrium isn't a arbitrary solution concept. It's *defined* by a fixed-point property that's guaranteed to exist.

2. **Separates existence from selection**: the proof shows equilibrium must exist, but doesn't determine which equilibrium. This clarifies the open problem: we still need to explain how players coordinate when multiple equilibria exist.

3. **Unifies diverse phenomena**: because the fixed-point property is guaranteed in all finite games, Nash Equilibrium provides a unified framework for analyzing economics, politics, biology (through evolutionary game theory), and psychology.

---

## Sources

- **nash51.pdf** — Nash's 1951 paper "Non-Cooperative Games"; the original proof
- **Osborne, Game Theory, nash.pdf** — Modern presentation of the proof with more detail
- **nash-lecture.pdf** — Nash's own exposition of the existence result

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — The concept being proved to exist
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium: Historical Development|Nash Equilibrium: Historical Development]] — Historical context for why the proof mattered
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Strategic Games Foundations|Strategic Games: Foundations & Assumptions]] — Foundational concepts (strategy, payoff, best response)
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Philosophical implications of existence guarantees and the equilibrium selection problem
- [[MOC/Economics]] — Economics MOC
