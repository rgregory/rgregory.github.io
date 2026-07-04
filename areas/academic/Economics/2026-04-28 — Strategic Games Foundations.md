---
type: note
date: "2026-04-28"
tags: [game-theory, definitions, economics, foundations]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Strategic Games: Foundations & Assumptions

Before you can analyze a game or predict what rational players will do, you need to agree on what the game *is*. This requires specifying players, available actions, payoff consequences, and the information structure. These foundational building blocks shape every prediction that follows.

## Core Elements of a Game

A **strategic game** (or **normal-form game**) consists of:

1. **A set of players**: $N = \{1, 2, \ldots, n\}$
2. **For each player $i$, a set of available actions**: $A_i$ (also called "strategies" in normal form; we'll distinguish pure vs. mixed below)
3. **An outcome function**: each combination of actions $(a_1, a_2, \ldots, a_n)$ determines an outcome
4. **A payoff function for each player**: $u_i(a_1, a_2, \ldots, a_n) \in \mathbb{R}$

The payoff function maps action profiles to real numbers, representing utility. The game is **simultaneous-move** if each player chooses their action without observing others' choices. It's **sequential-move** if players move in a specified order and observe prior choices (analyzed in extensive form, not normal form).

### Why These Matter

**Players**: Who has agency? In markets, both buyers and sellers are players. The "market" itself is not a player — it's a mechanism. In chess, two players. In a public goods game with $n$ contributors, all $n$ are players.

**Actions**: What's actually available? A firm can choose to produce more or less. It can choose which features to include in a product. It *cannot* unilaterally choose the market price (unless it has monopoly power). The action set constraints what strategies are possible.

**Payoffs**: What does each player care about? Firms care about profit. Consumers care about utility (consumption bundle and price). Politicians care about votes (and possibly other things, but votes are a primary payoff in models). Payoffs are *ordinal utilities* — the ranking is what matters, not cardinal magnitudes.

## Pure Strategies vs. Mixed Strategies

A **pure strategy** is a choice of a single action in the action set: $a_i \in A_i$.

A **mixed strategy** is a probability distribution over pure strategies: $\sigma_i \in \Delta(A_i)$, where $\Delta(A_i)$ is the probability simplex over $A_i$.

### Why Mixed Strategies?

In some games, there is no pure-strategy Nash Equilibrium. Example: **Matching Pennies**:
- Player 1 chooses Heads or Tails
- Player 2 chooses Heads or Tails
- If they match, Player 1 gets 1 and Player 2 gets -1
- If they don't match, Player 1 gets -1 and Player 2 gets 1

This is a zero-sum game with no pure-strategy NE. In any pure-strategy outcome:
- If 1 plays Heads and 2 plays Heads (match), then 2 wants to deviate to Tails
- If 1 plays Heads and 2 plays Tails (no match), then 1 wants to deviate to Tails

The only equilibrium is **mixed**: each player randomizes 50-50 between Heads and Tails. This keeps the opponent indifferent between their actions (so they're willing to randomize too).

The interpretation: mixed strategies represent either:
1. **Literal randomization**: the player genuinely flips a coin, or
2. **Population mixture**: in a large population, a fraction $p$ play action 1 and fraction $1-p$ play action 2

The second interpretation is often more natural in applied contexts. You don't think of firms literally randomizing; you think of a population of firms in some playing one strategy and others playing another.

## Best Response

Given the other players' strategies, what's the best thing *you* can do?

**Best response of player $i$ to strategy profile $\sigma_{-i}$ of the other players**:
$$BR_i(\sigma_{-i}) = \arg\max_{a_i \in A_i} u_i(a_i, \sigma_{-i})$$

This is the set of actions (or mixed strategies) that maximize your payoff given what others are doing.

### Key Property

If player $i$ is playing a **best response**, then:
- They can't unilaterally improve their payoff by changing their action
- They have no incentive to deviate
- They're doing as well as possible given the others' play

## Rationality Assumptions

The standard game-theoretic framework assumes:

1. **Players are rational**: they choose actions that maximize their payoffs given their beliefs about others' choices
2. **Players have complete information**: they know the payoff structure (who the players are, what actions are available, what payoffs result from each outcome)
3. **Rationality is common knowledge**: each player knows others are rational, knows that others know they're rational, and so on

These assumptions are **strong** and often unrealistic:
- People don't always maximize payoffs; they have bounded rationality, emotions, social preferences
- Payoff structures are often unknown or partially revealed
- Players might not even know who the other players are (as in anonymous market interactions)

But they provide a baseline model. Deviations from these assumptions are where behavioral economics lives.

## Normal Form Representation

A game is represented in **normal form** (or **strategic form**) as:
$$G = \langle N, (A_i), (u_i) \rangle$$

For a 2-player game, this is often a payoff matrix:

|  | Left | Right |
|---|---|---|
| **Up** | $(2, 1)$ | $(0, 2)$ |
| **Down** | $(3, 0)$ | $(1, 1)$ |

The first number in each cell is Player 1's payoff; the second is Player 2's payoff. The rows are Player 1's actions; the columns are Player 2's actions.

This representation is **compact** for finite games but loses some information: it doesn't indicate the *order* of moves (simultaneous vs. sequential). That's captured in the **extensive form**, which uses a game tree.

## Finite vs. Infinite Action Sets

Most textbook games use finite action sets (e.g., Prisoner's Dilemma has 2 actions per player). But real games often have infinite (or continuous) action sets:

- **Price competition**: a firm can choose any price in $[0, \infty)$
- **Quantity competition**: a firm can produce any quantity in $[0, \infty)$
- **Resource allocation**: a player can allocate a budget across many goods

With continuous action sets, payoff functions are typically differentiable, and best responses are found using calculus (first-order conditions). The structure is the same, just the tools are different.

## Dominant Strategies

A strategy is a **dominant strategy** for player $i$ if it's a best response to *any* strategy played by the opponents:
$$a_i^* \in BR_i(\sigma_{-i}) \quad \text{for all } \sigma_{-i}$$

In the Prisoner's Dilemma, **Defect** is dominant: no matter what the other player does, Defect is your best response.

Dominant strategies are rare. When they exist, the prediction is clean: rational players play them regardless of beliefs about others.

## Symmetric Games

A game is **symmetric** if all players have the same action set and payoffs are symmetric: $u_i(a_i, a_{-i}) = u_j(a_j, a_{-i})$ (up to relabeling).

In symmetric games, you can look for **symmetric equilibria**: profiles where all players use the same strategy. This reduces complexity dramatically — instead of solving for $n$ different strategies, you solve for one.

Example: **Symmetric Cournot Competition** with $n$ identical firms. In a symmetric equilibrium, all firms produce the same quantity $q$. The equilibrium is found by solving for the quantity that makes a firm indifferent at the margin.

---

## Sources

- **Osborne, Game Theory, nash.pdf** — Formal treatment of normal-form games, best response, and mixed strategies
- **nash-lecture.pdf** — Nash's own exposition of the foundational concepts

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Applies these foundations to define equilibrium precisely
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Prisoner's Dilemma|Prisoner's Dilemma: Structure, Discovery, & Significance]] — A canonical example showing dominant strategies and equilibrium in a finite game
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Philosophical parent note; foundational concepts applied across branches of game theory
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Broader context of how these foundations apply to economic problems
- [[MOC/Economics]] — Economics MOC
