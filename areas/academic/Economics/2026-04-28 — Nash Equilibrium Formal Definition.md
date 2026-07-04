---
type: note
date: "2026-04-28"
tags: [game-theory, nash-equilibrium, formal-definitions]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Nash Equilibrium: Formal Definition & Core Examples

Nash Equilibrium is simultaneously the simplest and most powerful concept in game theory. Its definition is elementary: a profile of strategies where no player regrets their choice. But this simple idea unifies almost all of strategic economics.

## Formal Definition

Given a game $G = \langle N, (A_i), (u_i) \rangle$:

A **Nash Equilibrium** is a strategy profile $\sigma^* = (\sigma_1^*, \sigma_2^*, \ldots, \sigma_n^*)$ such that for all players $i$ and all alternative strategies $\sigma_i$:

$$u_i(\sigma_i^*, \sigma_{-i}^*) \geq u_i(\sigma_i, \sigma_{-i}^*)$$

**In words**: each player's strategy is a best response to the other players' strategies. Given what the others are doing, no player can unilaterally deviate and improve their payoff.

### Equivalent Formulation via Best Response

$\sigma^*$ is a Nash Equilibrium if and only if for each player $i$:

$$\sigma_i^* \in BR_i(\sigma_{-i}^*)$$

where $BR_i(\sigma_{-i}^*)$ is the set of best responses for player $i$ to the other players' strategies $\sigma_{-i}^*$.

Geometrically: in a 2-player game, plot Player 1's best response as a curve in strategy space, and Player 2's best response as another curve. The intersections are Nash Equilibria.

## Why This Definition?

The definition encodes a concept of **strategic stability**:

1. **No incentive to deviate unilaterally**: if only you change your strategy and everyone else doesn't, you're worse off (or at least not better off)
2. **Mutual consistency**: each player's belief about others' play is correct — others are indeed doing what you think they're doing
3. **Self-reinforcing**: if everyone is playing a Nash Equilibrium, there's no reason for anyone to change

This is not a claim about how players *get to* the equilibrium. It's a claim about what happens *once* you're there.

## Pure vs. Mixed Strategy Equilibria

A **pure-strategy Nash Equilibrium** is a profile where each player chooses a single action with certainty (no randomization).

A **mixed-strategy Nash Equilibrium** is a profile where at least one player randomizes over multiple actions.

**Key insight from Nash (1951)**: Every finite game has at least one Nash Equilibrium, possibly in mixed strategies. You might not have a pure-strategy equilibrium (e.g., Matching Pennies), but you're guaranteed an equilibrium exists if you allow mixing.

## Four Canonical Examples

### 1. Prisoner's Dilemma

|  | Cooperate | Defect |
|---|---|---|
| **Cooperate** | $(3, 3)$ | $(0, 4)$ |
| **Defect** | $(4, 0)$ | $(1, 1)$ |

**Pure-strategy NE**: (Defect, Defect), with payoffs $(1, 1)$

**Why**: 
- For Player 1: if Player 2 cooperates, 1's payoff is 0 (cooperate) vs. 4 (defect) → defect is better. If Player 2 defects, 1's payoff is 4 (cooperate) vs. 1 (defect) → defect is better. Defect is dominant.
- Symmetrically for Player 2
- No pure-strategy NE where both cooperate, because each has incentive to deviate

**Pareto inefficiency**: (Cooperate, Cooperate) gives payoffs $(3, 3)$, which are better for both players than the equilibrium $(1, 1)$. But it's not a Nash Equilibrium because each player wants to defect.

### 2. Bach or Stravinsky (Battle of the Sexes)

A couple wants to spend the evening together, but disagree on whether to go to a Bach concert or a Stravinsky concert. Both prefer being together more than their preferred concert.

|  | Bach | Stravinsky |
|---|---|---|
| **Bach** | $(2, 1)$ | $(0, 0)$ |
| **Stravinsky** | $(0, 0)$ | $(1, 2)$ |

**Pure-strategy NE**: Two equilibria:
- (Bach, Bach): payoffs $(2, 1)$. If one player deviates, both get 0 → no incentive to deviate
- (Stravinsky, Stravinsky): payoffs $(1, 2)$. If one player deviates, both get 0 → no incentive to deviate

**Mixed-strategy NE**: There also exists a mixed-strategy equilibrium where each player randomizes. Player 1 plays Bach with probability $2/3$ and Stravinsky with probability $1/3$; Player 2 plays Bach with probability $1/3$ and Stravinsky with probability $2/3$. Each player is indifferent between their two actions given the opponent's mix.

**Multiplicity and coordination**: This game illustrates the **equilibrium selection problem**. Multiple equilibria exist; rational play alone doesn't determine which one occurs. Coordination (communication, focal points, history) matters.

### 3. Matching Pennies

Two players simultaneously reveal a coin. If both show Heads or both show Tails, Player 1 wins $1 and Player 2 loses $1. Otherwise, Player 2 wins $1 and Player 1 loses $1.

|  | Heads | Tails |
|---|---|---|
| **Heads** | $(1, -1)$ | $(-1, 1)$ |
| **Tails** | $(-1, 1)$ | $(1, -1)$ |

**Pure-strategy NE**: None. In any pure strategy, one player is better off deviating.

**Mixed-strategy NE**: Each player plays Heads and Tails with probability $1/2$. 
- Given Player 2 plays 50-50, Player 1 is indifferent between Heads and Tails (expected payoff is 0 either way)
- Given Player 1 plays 50-50, Player 2 is indifferent between Heads and Tails (expected payoff is 0 either way)
- Both players are willing to mix, so the mixed profile is indeed an equilibrium

**Zero-sum games**: Matching Pennies is a zero-sum game (payoffs sum to 0). In zero-sum games, every Nash Equilibrium is mixed (unless one player is indifferent).

### 4. Stag Hunt

Two hunters can cooperate to hunt a stag (large payoff if both hunt, nothing if only one tries) or hunt hare alone (small guaranteed payoff). If one hunts stag and the other hunts hare, the stag hunter gets nothing (the stag escapes).

|  | Stag | Hare |
|---|---|---|
| **Stag** | $(4, 4)$ | $(0, 3)$ |
| **Hare** | $(3, 0)$ | $(3, 3)$ |

**Pure-strategy NE**: Two equilibria:
- (Stag, Stag): payoffs $(4, 4)$. Best response: if the other hunts Stag, you should hunt Stag (payoff 4 vs. 3). This is an equilibrium. ← **Efficient equilibrium**
- (Hare, Hare): payoffs $(3, 3)$. Best response: if the other hunts Hare, you should hunt Hare (payoff 3 vs. 0). This is an equilibrium. ← **Safe equilibrium**

**Mixed-strategy NE**: There also exists a mixed equilibrium.

**Assurance problem**: Unlike Prisoner's Dilemma (where both prefer mutual defection to be avoided but individual incentives push toward defection), Stag Hunt has:
- Both players prefer the cooperative outcome (4, 4) to the defection outcome (3, 3)
- But each fears the other won't cooperate, so choosing the safe action (Hare) is prudent

This is not a free-rider problem. It's a **trust problem**: players want to cooperate but fear being exploited if the other doesn't cooperate.

## Symmetric Equilibria

In a **symmetric game**, all players have the same action set and the payoff function is symmetric: $u_i(a_i, a_{-i})$ depends only on the profiles, not on player indices.

A **symmetric equilibrium** is a profile where all players use the same strategy: $\sigma^* = (\sigma, \sigma, \ldots, \sigma)$.

In the two examples above that have pure-strategy symmetric equilibria:
- Prisoner's Dilemma: (Defect, Defect) is the unique symmetric pure-strategy equilibrium
- Stag Hunt: (Stag, Stag) and (Hare, Hare) are both symmetric pure-strategy equilibria; there's also a symmetric mixed equilibrium

Symmetric equilibria are analytically convenient when you have many players (e.g., $n$ firms in Cournot competition) because you only need to solve for one strategy instead of $n$ different ones.

## Best Response Correspondence and Graphical Analysis

In 2-player games, you can visualize equilibria:

1. **Compute best response functions** for each player as a function of the other's (mixed) strategy
2. **Plot both best response correspondences** on the same diagram
3. **Intersections are Nash Equilibria**

For Prisoner's Dilemma:
- Player 1's best response: if P2 plays any probability mix, P1's best response is Defect (always)
- Player 2's best response: if P1 plays any probability mix, P2's best response is Defect (always)
- Intersection: both play Defect

For Matching Pennies:
- Player 1's best response to P2 playing 50-50: indifferent between Heads and Tails
- Player 2's best response to P1 playing 50-50: indifferent between Heads and Tails
- Intersection: both play 50-50 (the entire 1-dimensional set of mixed strategies where P1 plays 50-50 is a best response to P2 playing 50-50)

## Existence and Uniqueness

**Existence (Nash 1951)**: Every finite game has at least one Nash Equilibrium (in mixed strategies).

**Uniqueness**: No guarantee. Games can have 1, 2, many, or infinitely many equilibria.

**Refinements**: When multiple equilibria exist, economists have developed **refinements** to narrow the set:
- **Subgame perfect equilibrium**: for sequential games, eliminate equilibria sustained by non-credible threats "off the equilibrium path"
- **Perfect Bayesian equilibrium**: add consistency of beliefs as players move through the game tree
- **Evolutionary stability**: eliminate strategies that are vulnerable to invasion by alternative strategies in a population

These refinements are important when equilibrium selection matters — i.e., when different equilibria lead to different outcomes and players care which one is selected.

---

## Sources

- **Osborne, Game Theory, nash.pdf** — Detailed analysis of all four canonical games
- **nash51.pdf** — Nash's 1951 paper on existence and mixed strategies
- **nash-lecture.pdf** — Nash's own exposition of equilibrium concepts

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Strategic Games Foundations|Strategic Games: Foundations & Assumptions]] — Foundational concepts (players, actions, payoffs, rationality)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium: Historical Development|Nash Equilibrium: Historical Development]] — Why Nash's definition was revolutionary
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Existence Proof|Nash Equilibrium: Existence Proof & Mathematical Foundations]] — The fixed-point proof underlying existence
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Prisoner's Dilemma|Prisoner's Dilemma: Structure, Discovery, & Significance]] — Deeper treatment of one canonical example
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Philosophical context; open questions on whether NE is normative or descriptive, the folk theorem, and equilibrium selection
- [[MOC/Economics]] — Economics MOC
