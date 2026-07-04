---
type: note
date: "2026-04-28"
tags: [game-theory, sequential-games, extensive-form, backward-induction, subgame-perfect-equilibrium]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Extensive-Form Games

Extensive-form games model strategic interaction with a crucial feature that normal-form games miss: **sequence**. Moves happen one after another, not simultaneously. Information unfolds over time. Players make decisions at different stages, with different information available at each stage.

The extensive form captures the temporal structure of strategic interaction: who moves when, what do they know when they move, and what happens next. This structure generates new strategic possibilities (commitment, credibility, threats) that don't exist in simultaneous-move games.

---

## Structure of Extensive-Form Games

### Game Trees

An extensive-form game is represented as a **game tree**:

- **Nodes** represent game states (decision points or chance events)
- **Branches** represent actions available at each node
- **Root** is the initial state
- **Terminal nodes** are the end of the game; each terminal node has a payoff vector $(u_1, u_2, \ldots, u_n)$

**Example: Ultimatum Game Tree**

```
          Root
           |
      [Proposer chooses]
       /    |    \
      20    40    60  (splits: Proposer takes x, Responder gets 100-x)
      |     |     |
    [Responder chooses at each node]
    Accept Reject
     |      |
    (80,20) (0,0)  [if Proposer proposed 20]
    (60,40) (0,0)  [if Proposer proposed 40]
    (40,60) (0,0)  [if Proposer proposed 60]
```

This is a **sequential game**: Proposer moves first (chooses split), Responder observes it and responds, game ends with payoffs.

### Sequential vs. Simultaneous Moves

**Sequential moves**: One player moves, then observes the outcome, then another player moves (given that observation).

**Simultaneous moves**: Players choose without observing what others chose. They form beliefs about others' actions, then choose optimally given those beliefs.

The difference is informational: in sequential games, later players have more information (they observe earlier moves). This gives later players an advantage (they can respond) but constrains earlier players' options (later players will respond optimally to your move).

### Information Sets

An **information set** groups nodes where a player can't distinguish which node they're at.

**Example**: In poker, you know your own cards and the community cards revealed so far, but you don't know opponents' hidden cards. All nodes representing "the same history from my perspective" are in the same information set.

- **Perfect information**: Each information set contains exactly one node. Whenever it's your turn, you know the full history of the game.
- **Imperfect information**: Some information sets contain multiple nodes. When it's your turn, you don't know which node you're at.

**Perfect information example**: Chess (you see all pieces). Your information set at any point in the game has one node (the current board state).

**Imperfect information example**: Poker (you don't know opponents' hole cards). When it's your turn to bet, you're in an information set with multiple nodes (different opponents' hand combinations that are consistent with your observations).

---

## Backward Induction

Backward induction is the key solution method for finite extensive-form games with perfect information.

**Idea**: Solve the game by reasoning backwards from the end.

1. **At each terminal node**: Payoff is given
2. **At each non-terminal node where a player must move**:
   - That player chooses the action that maximizes their payoff, anticipating what will happen at subsequent nodes
   - The payoff at that node is the payoff from the optimal action

**Algorithm**:
- Start at nodes one move before the end (where a player chooses knowing the game ends after)
- Determine each player's optimal action
- Move backward one level; now you know what happens if you move to any subsequent node
- Repeat until you reach the root

**Example: Simple Bargaining Game**

Player A proposes a split of \$10. Player B accepts or rejects. If rejected, both get \$0.

**Backward induction**:
- B's optimal response: Accept any split where B gets > \$0 (since rejecting gives B nothing)
- A anticipates this: A can propose to give B the minimum (say \$0.01) and keep \$9.99
- A's optimal move: Propose (\$9.99, \$0.01)
- Outcome: A gets \$9.99, B gets \$0.01

This prediction is counterintuitive empirically (see the Ultimatum Game in [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — people reject unfair offers), but the logic is sound under assumptions of perfect rationality and common knowledge.

---

## Subgame Perfect Equilibrium

Nash Equilibrium applies to extensive-form games, but it can sustain equilibria that rely on **non-credible threats**.

**Example: Entry Deterrence**

Entrant (E) decides whether to Enter or Stay Out. If E Stays Out, Incumbent (I) gets \$10, E gets \$0. If E Enters, I chooses whether to Fight or Accommodate.

- If Fight: E gets -\$2 (losses), I gets \$1 (also loses from conflict)
- If Accommodate: E gets \$5, I gets \$5

**Nash Equilibrium (naive analysis)**:
- E believes I will Fight if E Enters
- Given this belief, E chooses Stay Out
- I gets \$10, E gets \$0
- But is I's threat to Fight credible?

**Backward induction (Subgame Perfect Equilibrium)**:
- If E Enters, I will move. I chooses between Fight (\$1) and Accommodate (\$5)
- I's optimal choice: Accommodate (since \$5 > \$1)
- Anticipating this, E's optimal choice: Enter (since \$5 > \$0)
- Outcome: E Enters, I Accommodates, payoffs are (\$5, \$5)

The issue: the Nash Equilibrium relied on I's threat to Fight, but if E actually enters, I won't follow through (it's not optimal). This threat is **not credible**.

**Subgame perfect equilibrium** eliminates non-credible threats by requiring that at every node (every **subgame**), players' strategies are consistent with optimality.

**Definition**: A strategy profile is a **subgame perfect equilibrium** (SPE) if it induces a Nash Equilibrium in every subgame.

---

## Commitment and Credibility

Extensive-form games reveal the strategic value of commitment.

**First-mover advantage via commitment**: If you can move first and commit to your action, you can lock in an outcome favorable to you.

**Example**: In bargaining, the first proposer has significant advantage (can propose a very unequal split and the responder must accept or get nothing).

**Strategic commitment devices**:
1. **Reduce your own future options** to make threats credible
   - "I've publicly committed to fighting if you enter" (burning bridges)
   - "I've signed a contract that prevents me from backing down"
2. **Raise the cost of deviating** so that your threat becomes optimal
   - "I've put my reputation on the line"
   - "I've made side payments that are forfeited if I deviate"

**Example: War and Resolve**

In conflict, a country might want to signal that it will fight rather than back down. One way to signal credibility:
- Take an action that is costly and irreversible if you're bluffing (e.g., mobilize troops, make public threats)
- If your resolve is doubted, you bear the cost unless you back down
- This makes backing down more costly (lose face, lose credibility), so your threat to fight becomes credible

This connects to the concept of **equilibrium selection**: among multiple Nash Equilibria, which one is selected? Commitment can help select equilibria favorable to the committing player.

---

## Perfect vs. Imperfect Information

### Perfect Information Games

In perfect information games, every player observes the full history of moves whenever it's their turn. Chess, checkers, tic-tac-toe are examples.

**Properties**:
- Backward induction always applies
- Subgame perfection is equivalent to Nash Equilibrium
- Game can be solved by considering all possible move sequences
- Often has a dominant strategy (e.g., if chess is solved, it has a unique SPE)

### Imperfect Information Games

In imperfect information games, when it's your turn, you don't know what moves other players made (or you know some moves but not others).

**Example: Poker**
- You know your cards
- You observe bets and folds by other players
- You don't know their cards
- When it's your turn, you're in an information set with multiple possible hands for your opponents

**Solution method**: Can't use simple backward induction (you don't know the full game state). Instead:
- **Bayesian perfect equilibrium**: Extend backward induction to imperfect information by requiring players to update beliefs about the game state using Bayes' rule
- **Perfect Bayesian equilibrium**: Add consistency requirements on beliefs

**Strategic issues in imperfect information**:
- **Signaling**: You might take costly actions to reveal information about yourself
- **Bluffing**: You might claim to have good cards (or a strong position) when you don't
- **Pooling**: You might mimic the action of a different type to avoid revealing your information
- **Separating**: You might take distinct actions that reveal your type

---

## Applications and Examples

### Bargaining and Negotiation

Many bargaining situations have an extensive form:
1. One player proposes a deal
2. The other accepts or rejects
3. If rejected, there are consequences (breakdown, renegotiation, etc.)

**Rubinstein Bargaining Model**: Two players bargain over a pie. At each round, one player proposes a split; the other accepts or rejects. If rejected, the game continues (both players have slightly less patience, or the pie shrinks).

**Solution (SPE)**:
- The proposer offers the responder the minimum they'll accept
- The responder accepts any offer better than what they expect in the next round
- In equilibrium, agreement happens immediately (no delay, which is rational since delay is costly)
- The proposer's share depends on the discount rate (how much players value future payoffs)

**Insight**: Patience is a bargaining advantage. If the responder is very impatient (heavily discounts the future), the proposer can offer very little (take it or wait a long time for renegotiation, which you value almost nothing).

### Entry Deterrence and Industrial Organization

Incumbent firms might take actions to deter entry by potential competitors.

**Model**: Incumbent chooses capacity. Entrant observes capacity and decides whether to enter. If entry occurs, firms compete (Cournot or Bertrand) in the product market.

**Strategic issue**: Incumbent wants to choose capacity to deter entry. But once entry occurs, capacity is sunk — the incumbent would prefer to accommodate and share the market (lower competition is better than fighting) rather than fight and lose. Entrant knows this.

**Spence's insight**: Incumbent can deter entry by choosing large capacity (even though it's costly and would be regretted if entry occurs). This is a commitment device: large capacity signals that incumbent will fight. Entrant, seeing this signal, chooses not to enter.

**Equilibrium**: Incumbent builds excess capacity, Entrant stays out, Incumbent earns high profits despite having wasted money on capacity.

### War and Deterrence

Strategic conflict has extensive-form structure:
1. One side takes an aggressive action
2. The other side observes and chooses to escalate, accommodate, or negotiate
3. Outcomes depend on both sides' military capabilities and resolve

**Credibility of threats**: A threat is credible if it's in the threatener's interest to carry it out. But if backing down is preferable (less costly), the threat isn't credible.

**Costly signaling**: Countries might take actions (military exercises, military buildup, public threats) to signal resolve. These are costly; they signal that the country is willing to bear costs to achieve objectives. This makes threats credible (since the country is already paying a cost).

---

## Key Distinctions from Normal Form

Normal-form games represent simultaneous play; extensive-form captures sequential play. This leads to different strategic considerations:

| Property | Normal Form | Extensive Form |
|----------|------------|---|
| **Information** | All players choose simultaneously; no one observes others' choices | Players move sequentially; later players observe earlier moves |
| **Strategy** | Maps from type to action (for one decision point) | Plans for all contingencies (full decision tree) |
| **Equilibrium** | Nash Equilibrium | Subgame Perfect Equilibrium (stronger concept) |
| **Credibility** | No non-credible threats (all equilibria are "credible" given simultaneous play) | Must check credibility; threats sustained off-equilibrium might not be credible |
| **First-mover advantage** | No asymmetry from order | First-mover advantage from commitment |

---

## Connections to Other Game-Theoretic Concepts

**Nash Equilibrium vs. SPE**: Every SPE is a Nash Equilibrium (in the reduced normal form), but not vice versa. Nash Equilibrium allows non-credible threats off the equilibrium path; SPE eliminates them. See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] for the foundational concept.

**Backward induction vs. forward induction**: Backward induction (SPE) reasons from the end to the start. Forward induction reasons about what the past reveals (if a player took an action, what does this tell us about their type or beliefs about the future?).

**Sequential games in mechanism design**: Extensive-form structure is essential for [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] when agents move sequentially or information is revealed over time. The credibility of commitment (can you make a threat stick?) determines mechanism feasibility.

**Prisoner's Dilemma and repeated play**: See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Prisoner's Dilemma|Prisoner's Dilemma: Structure, Discovery, & Significance]] for how temporal structure (repeated vs. one-shot) changes the equilibrium from defection to possible cooperation (folk theorem).

---

## Key Insights

1. **Sequence matters**: Adding temporal structure to games introduces new strategic possibilities (commitment, credibility, first-mover advantage) that don't exist in simultaneous-move games.

2. **Threats must be credible**: A threat is only effective if it's in the threatener's interest to carry it out. SPE eliminates non-credible threats by requiring optimality at every node.

3. **Commitment devices are valuable**: If you can restrict your own future options, you can make threats credible and secure better outcomes. This has widespread applications in contracts, law, and policy.

4. **Information structure determines strategy**: Perfect information (observing all past moves) vs. imperfect information (uncertainty about other players' actions) leads to very different strategic problems.

5. **Bargaining power depends on patience**: In sequential bargaining, the more patient side has an advantage (can wait the other side out). Patience is a bargaining advantage.

---

## Sources

- **Osborne, Game Theory** — Excellent chapters on extensive form, backward induction, SPE
- **Osborne and Rubinstein, Bargaining and Markets** — The Rubinstein bargaining model and applications
- **Saloner, Shepard, and Podolsky** — Modern game theory applications to industrial organization

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Nash Equilibrium is the normal-form solution concept; SPE is its extensive-form refinement
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Prisoner's Dilemma|Prisoner's Dilemma: Structure, Discovery, & Significance]] — Repeated play and temporal structure affect cooperation (folk theorem)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] — Bargaining as a game; extensive-form bargaining and the Rubinstein model
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Industrial organization applications (entry deterrence, pricing, R&D races)
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Philosophical context on strategic reasoning and rationality
- [[03-Resources/Articles/2026-05-06 — Reading — Miscellanea — The War in Iran|The War in Iran (Devereaux, 2026)]] — Applied case: the U.S.–Iran escalation trap as a real-world commitment problem; neither side can credibly back down without domestic political collapse, illustrating precisely why non-credible SPE threats fail to deter
