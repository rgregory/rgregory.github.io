---
type: note
date: "2026-04-28"
tags: [mechanism-design, game-theory, incentive-compatibility, social-choice, economics]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Mechanism Design Foundations

Mechanism design is the engineering branch of game theory. If game theory asks "given the rules of interaction, what will rational agents do?", mechanism design asks "given what we want agents to do, what rules should we design?"

It's called the "inverse problem" of game theory: instead of analyzing outcomes from rules, you work backwards from desired outcomes to rules that produce them.

---

## The Central Problem

**Setup**:
- A planner (or society) wants to allocate resources, choose policies, or organize transactions
- The planner doesn't have direct information about agents' preferences, costs, or valuations
- Agents do know their own preferences, but might have incentive to misrepresent them
- The planner wants to design a mechanism that:
  1. Elicits truthful information from agents (incentive compatibility)
  2. Makes decisions that are feasible and respect individual rationality (agents don't lose by participating)
  3. Achieves some desired outcome (social welfare maximization, revenue maximization, fairness, etc.)

**Example**: A government wants to procure a bridge. It doesn't know construction firms' costs. Each firm knows its own costs but has incentive to overstate them (to get a higher price). The government wants to elicit truthful cost information and allocate the project to the lowest-cost firm. What mechanism achieves this?

---

## Key Concepts

### Mechanism

A **mechanism** (or institution) is a formal system that:
1. Collects messages (announcements of preferences, costs, types) from agents
2. Produces a decision (allocation of goods, choice of policies, distribution of payoffs)
3. Produces payment obligations

**Formal definition**: A mechanism is a pair $(x, t)$ where:
- $x: M \to X$ is an **outcome function** (maps messages to allocations)
- $t: M \to \mathbb{R}^n$ is a **payment function** (maps messages to transfers)

where $M$ is the message space (what agents report).

### Incentive Compatibility

A mechanism is **incentive compatible** (or truthful) if agents' dominant strategy is to report truthfully.

**Formal definition**: For agent $i$ with true type $\theta_i$, truthful reporting is a dominant strategy if:

$$u_i(x(\theta_i, \theta_{-i}^*), t_i(\theta_i, \theta_{-i}^*), \theta_i) \geq u_i(x(\theta'_i, \theta_{-i}^*), t_i(\theta'_i, \theta_{-i}^*), \theta_i)$$

for all $\theta'_i$ and all $\theta_{-i}^*$ (regardless of what others report).

**Intuition**: You can't do better by lying than by telling the truth, no matter what others do.

### Individual Rationality

A mechanism is **individually rational** (or feasible) if agents are willing to participate:

$$u_i(x(\theta_i, \theta_{-i}^*), t_i(\theta_i, \theta_{-i}^*), \theta_i) \geq u_i(\text{outside option})$$

**Intuition**: Participation should make you at least as well off as not participating.

---

## The Revelation Principle

**Revelation Principle (Gibbard-Satterthwaite)**: Any allocation rule that can be achieved by some (possibly complex) mechanism can also be achieved by a **truthful mechanism** where agents' dominant strategy is to report their true type.

**Significance**: This means the mechanism designer can restrict attention to truthful mechanisms without loss of generality. Any allocation you can imagine achieving, you can achieve with a mechanism where truth-telling is optimal.

**Why?** If agents are playing optimally in some mechanism (following their best responses), the planner can extrapolate what their true types are from their optimal messages, then design a simpler mechanism that elicits those types truthfully.

---

## Constraints and Tradeoffs

Not all desirable properties can be satisfied simultaneously.

### Incentive Compatibility Constraint

If you want agents to report truthfully, you must pay them for doing so. Truthful reporting might be risky (others might behave unexpectedly) or require them to forgo profit from lying.

The **IC constraint** quantifies this: the payment must be high enough to induce truth-telling.

### Individual Rationality Constraint

Agents won't participate if they're worse off than their outside option. The **IR constraint** limits how much you can extract in payments.

### Feasibility Constraint

The total value to be allocated is limited by the resources available or the gains from trade.

These constraints often conflict:
- **Revenue maximization** (pay agents as little as possible) conflicts with **allocation efficiency** (give goods to those who value them most)
- **Truth-telling** (incentive compatibility) conflicts with **fairness** (equal treatment)
- **Optimal allocation** conflicts with **budget balance** (revenue = costs)

---

## The Principal-Agent Problem

A **principal** (employer, government, buyer) wants an **agent** (employee, citizen, seller) to take a desired action. The principal can't observe the agent's action directly but can observe an outcome correlated with the action.

**Setup**:
- Principal offers a contract specifying payment as a function of observed outcome
- Agent chooses effort (hidden action), which stochastically determines outcome
- Principal observes outcome, pays agent according to contract
- Agent's effort is unobservable (hidden action); agent might shirk

**Example**: You hire someone to work on a project. Their effort is unobservable, but project quality is. You design a contract (payment as a function of quality) to incentivize effort.

**Solution**: Pay the agent based on observed outcome. But outcomes are noisy (luck affects quality beyond effort), so the agent bears risk from this noise. Risk-averse agents require compensation for bearing this risk.

**Tradeoff**: Better incentives (higher payment for better outcomes) induce more effort but expose the agent to more risk. The optimal contract balances incentive and risk considerations.

---

## Truthful Mechanisms: VCG and Vickrey

### Vickrey's Second-Price Auction

The simplest truthful mechanism: a second-price sealed-bid auction where the highest bidder wins and pays the second-highest bid.

**Incentive compatibility**: Bidding truthfully (revealing true valuation) is a dominant strategy. No matter what others bid, you maximize your surplus by bidding your true valuation.

**Individual rationality**: The winner gets positive surplus (they value the item more than what they pay). The losers get zero surplus (they don't pay).

**Outcome**: The item goes to the highest-valuation agent; the mechanism collects the second-highest valuation in revenue.

### Vickrey-Clarke-Groves (VCG) Mechanism

Generalization of Vickrey to multiple items and public decision-making.

**Setup**:
- Choose an allocation that maximizes total welfare (sum of valuations)
- Charge each agent a payment equal to the harm they impose on others

**Formally**:
- Allocation: $x^* = \arg\max_x \sum_i v_i(x_i)$
- Payment for agent $i$: $t_i = \max_{x_{-i}} \sum_{j \neq i} v_j(x_j) - \sum_{j \neq i} v_j(x_j^*)$

**Intuition**: The payment is "the welfare the others lose because you're in the game." If removing you makes others better off, you pay (compensating them). If removing you makes others worse off, you get paid.

**Properties**:
- **Truthful**: Truthful reporting is a dominant strategy
- **Efficient**: Allocates resources to maximize total welfare
- **Individual rational**: Each agent gets non-negative surplus

**Limitation**: The mechanism might run a deficit (not enough revenue to cover costs). It's not budget-balanced.

---

## Impossibility Results

Not everything is possible. Several fundamental impossibility results constrain mechanism design.

### Arrow's Impossibility Theorem (Related)

Arrow's theorem applies to social choice (aggregating individual preferences into a collective decision). While focused on voting, it has implications for mechanism design:

**Statement**: No voting rule that aggregates individual ordinal preferences into a social ordering can satisfy:
1. **Non-dictatorship**: Outcome doesn't depend only on one voter's preference
2. **Pareto efficiency**: If everyone prefers A to B, society prefers A to B
3. **Independence of irrelevant alternatives (IIA)**: Society's ranking of A and B depends only on individuals' rankings of A and B

**Mechanism design implication**: You can't design a mechanism that is both efficient and fair without violating some basic property.

### Gibbard-Satterthwaite Theorem

If a mechanism is strategy-proof (agents' best response is truth-telling) and onto (can produce any outcome), then it's **dictatorial**: one agent's preferences determine the outcome.

**Mechanism design implication**: You can't have a strategy-proof mechanism that is both efficient and non-dictatorial without restricting the domain of preferences.

### Budget Balance vs. Efficiency

The VCG mechanism is efficient and truthful but might run a deficit. There's no mechanism that is simultaneously:
- Truthful (dominant strategy truth-telling)
- Efficient (maximizes total welfare)
- Budget-balanced (revenue = costs)

(in general settings with more than 2 agents and non-identical preferences)

**Tradeoff**: Choose two; you must sacrifice the third.

---

## Applications: Auction Design and Matching

### Auctions (Mechanism Design for Allocation)

Auctions are mechanisms for allocating a good when the planner doesn't know valuations.

**Second-price auction** (Vickrey): Truthful mechanism; highest bidder wins; pays second price. Revenue = second-highest valuation.

**First-price auction**: Not truthful (bidders shade bids), but achieves same revenue in equilibrium (revenue equivalence theorem). See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]].

**Optimal auction** (Myerson): Combines a reserve price with second-price mechanism to maximize seller's expected revenue subject to IC and IR constraints.

### Matching Markets (Mechanism Design for Allocation with Preferences on Both Sides)

In two-sided matching, you want stable allocations (no blocking pairs). This requires a different approach than auctions.

**Gale-Shapley algorithm**: Not incentive-compatible (proposees can benefit from lying), but generates stable matchings. The algorithm is optimal for the proposing side; optimal for proposers means non-optimal for proposees. See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]].

**Market design trade-off**: Do you want incentive compatibility (truth-telling is optimal) or stability (no blocking pairs)? You often can't have both; the choice determines outcomes.

---

## Goodhart's Law and Mechanism Design Failures

[[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] states: "When a measure becomes a target, it ceases to be a good measure."

**Mechanism design perspective**: When you design a mechanism optimizing for a certain outcome (target), agents will optimize for the mechanism you designed (the measure), not the underlying objective.

**Example**: You want to incentivize school performance, so you pay teachers based on student test scores. Teachers then optimize for test scores (teaching to the test), not learning. The mechanism works (test scores improve) but achieves the wrong goal (learning might not improve).

**Connection to [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Cobra Effect|The Cobra Effect]]**: This is mechanism design failure. The colonizer wanted to reduce cobra numbers; they paid for cobra skins. People then bred cobras to collect payments. The mechanism succeeded at increasing dead cobra skins but failed at the actual goal (reducing cobra populations).

**Implication**: Mechanism design can produce perverse incentives if the optimization target diverges from the true goal. Designers must carefully align the mechanism with the underlying objective.

---

## Truth-Telling and the Dominant-Strategy Equilibrium

**Why is dominant-strategy truth-telling desirable?**

1. **Robustness**: True regardless of others' play. You don't need to forecast others' behavior.
2. **Stability**: Equilibrium is self-reinforcing. If everyone is truthful, no one benefits from lying.
3. **Simplicity**: Agents can follow a simple rule (report truthfully) without complex reasoning about others.

**When is dominant-strategy truth-telling possible?**

Not always. Truthful mechanisms must satisfy strong properties (especially VCG for multiple items). In many settings (matching, public goods provision), there's no truthful mechanism with desirable properties.

**Alternative**: Bayesian Nash Equilibrium truth-telling. Truth-telling is optimal given a belief about others' behavior, but not optimal against all possible deviations. This is weaker but more widely applicable.

---

## Key Insights

1. **Rules determine outcomes**: The mechanism you design directly determines what agents do and what outcomes result. Institutional design matters.

2. **Information and incentives are central**: The hardest part of mechanism design is extracting truthful information from self-interested agents. Every mechanism faces tradeoffs between incentive compatibility, efficiency, budget balance, and fairness.

3. **Impossibility is fundamental**: You can't satisfy all desiderata (truth-telling, efficiency, budget balance, fairness). Mechanism design is about choosing which properties matter most and sacrificing others.

4. **Applications are concrete**: Auctions, matching markets, organ donation, school choice — mechanism design directly improves real-world outcomes when done well. The FCC spectrum auctions and kidney exchange programs demonstrate the value of careful mechanism design.

5. **Goodhart's Law is ever-present**: When you optimize a mechanism for a measurable target, agents optimize for the mechanism, not the underlying goal. Designers must ensure the mechanism aligns with true objectives.

---

## Sources

- **Myerson — Design of Efficient and Durable Supply Contracts (1981)** — Foundational paper on mechanism design
- **Mas-Colell, Whinston, and Green — Microeconomic Theory (1995)** — Comprehensive chapters on mechanism design
- **Auctions and Mechanism Design** — A Modern Introduction (Klijn & Yenmez) — Accessible modern treatment

---

## Connections

### Applied Mechanism Design (The Four Pillars)

The following four notes are the primary applications of mechanism design foundations. Each applies the IC/IR framework to a specific allocation problem:

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] — Application: designing auctions to extract revenue and allocate truthfully; when a single item is divided among many agents with unobservable valuations
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] — Application: designing two-sided matching mechanisms (Gale-Shapley, school choice); when agents on both sides have preferences and the goal is stability, not revenue
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] — Fairness in cooperative games; axiomatic approach to determining how gains from cooperation should be split; related to VCG mechanism design for dividing coalitional surplus
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Extensive-Form Games|Extensive-Form Games]] — Sequential mechanisms and information revelation over time; backward induction as the solution method; subgame perfect equilibrium as the stability concept; commitment and credible threats as mechanisms

### Theoretical Foundations

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Equilibrium analysis in mechanisms; the equilibrium concept underpinning all mechanism design
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Parent context; mechanism design as the engineering branch; synthesis of mechanism design as solving the knowledge problem through incentives

### Design Failure Modes and Lessons

- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] — The canonical mechanism design failure: when a measure becomes a target, it ceases to be a good measure; agents optimize for the mechanism, not the underlying goal
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Cobra Effect|The Cobra Effect]] — Mechanism design failure in practice; perverse incentives when the mechanism diverges from the true objective
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Hayek's Knowledge Problem|Hayek's Knowledge Problem]] — The foundational problem mechanism design solves: aggregating distributed, locally-held knowledge through incentive design rather than central planning; revelation principle as the formal answer

### Related Concepts

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] — Axiomatic characterization of fair division; shares the axiomatic approach with mechanism design
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration|Game Theory — Exploration]] — Mechanism design as one of the five major branches of game theory; philosophy of incentives, truthfulness, and institutional design

### Real-World Mechanisms (Tax Law)

- [[00-Inbox/2026-05-17 — What Is an S-Corporation|What Is an S-Corporation]] — Subchapter S of the IRC is a textbook applied mechanism: the IRS wanted to incentivize small domestic business formation (desired outcome) without double taxation, so it designed pass-through tax treatment (the mechanism), with eligibility constraints (IC/IR conditions) to prevent gaming by large or foreign-controlled entities
- [[00-Inbox/2026-05-17 — S-Corporation Pros and Cons|S-Corporation — Pros and Cons]] — Every S-Corp disadvantage (reasonable compensation rule, one class of stock, 100-shareholder cap) is an IC constraint: the IRS adding requirements that make truth-telling (running a genuine small business) the dominant strategy, while making gaming (minimizing salary to zero, bringing in institutional capital) infeasible within the mechanism
