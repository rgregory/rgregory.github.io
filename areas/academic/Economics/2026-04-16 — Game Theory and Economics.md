---
type: note
date: "2026-04-16"
tags: [game-theory, economics, mechanism-design, behavioral-economics, rational-choice, self-study]
status: exploring
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-16"
---

# Game Theory and Economics

The relationship isn't incidental — economics and game theory grew up together. Economics is, at its core, the study of how agents allocate scarce resources under constraints. Game theory is the study of what happens when the relevant constraints include *other agents making choices*. Once you notice that most interesting economic situations have that structure — markets, auctions, wage bargaining, trade agreements, regulatory strategy — the overlap becomes almost total.

The classical picture of competitive markets (price-taking, anonymous buyers and sellers) is actually a limiting case: the game where no single player is large enough to affect outcomes by deviating. The moment you have a small number of firms, a dominant buyer, or any agent large enough to matter, you're in game-theoretic territory. And most real markets are, at least partially, strategic.

---

## Nash Equilibrium as the Economic Workhorse

The concept did more than describe strategic interaction — it unified two traditions that had been talking past each other. Before Nash, price theory and strategic reasoning were separate enterprises. Nash Equilibrium is precisely the condition where competitive markets clear: no buyer can do better by offering less, no seller can do better by asking more. The competitive equilibrium *is* a Nash Equilibrium, and now you can see both phenomena as instances of the same underlying idea. See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium: Historical Development|Nash Equilibrium: Historical Development]] for the conceptual breakthrough and [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] for the formal statement and canonical examples.

This unification mattered enormously for the rigor of economics as a discipline. It gave theorists a common language and a common solution concept. It also revealed how much weight was being placed on a single idea — and how many equilibria there actually are in most interesting games (the folk theorem problem: almost anything can be an equilibrium in repeated interactions, which is theoretically exciting and practically frustrating).

---

## Mechanism Design: Engineering the Rules

If game theory asks "given this game, what will rational players do?", mechanism design asks "given what we want players to do, what game should we build?" It's the engineering branch — and it has produced some of the most directly consequential applied economics of the last 40 years. See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] for the formal framework, [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] for axiomatic fair division, and the following applied topics.

**Auction theory** is the clearest example. Vickrey's result (1961) is elegant and counterintuitive: in a second-price sealed-bid auction, truthful bidding is a dominant strategy — you can't do better than revealing your true value regardless of what others do. This isn't obvious. It requires that the winner pays not what *they* bid but what the second-highest bidder bid. The mechanism makes honesty dominant by removing the incentive to shade. The FCC spectrum auctions (1990s) translated this into billions of dollars in real-world market design, refined by Milgrom and Wilson (Nobel 2020). See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] for types of auctions, revenue equivalence, and optimal design.

**Matching markets** are the other great application. Gale-Shapley's deferred acceptance algorithm (1962) finds stable matchings between two sides of a market — medical residents and hospitals, students and schools, kidney donors and patients. Alvin Roth turned this from a mathematical curiosity into a discipline (market design) and rebuilt the Boston and New York City school matching systems. He won the Nobel in 2012 alongside Shapley. The kidney exchange work is particularly striking: Roth designed chains of paired kidney donations that couldn't happen bilaterally, using mechanism design to create exchanges where markets couldn't function (no money changes hands — it's illegal — so you have to engineer the right game structure directly). See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] for the algorithm, stability, and strategic behavior.

**Mechanism design and the knowledge problem**: Mechanism design answers [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Hayek's Knowledge Problem|Hayek's Knowledge Problem]] — how to coordinate dispersed private information in strategic settings. Instead of Hayek's price system as the aggregation mechanism, mechanism designers engineer direct-revelation incentive-compatible protocols where agents truthfully report their private types. Same problem (how to coordinate distributed knowledge that no central planner possesses), different solution (pricing vs. truthful revelation). The link reveals that markets and mechanism design are two answers to the same epistemological challenge: how do institutions aggregate distributed information without requiring the planner to know it in advance?

The Nobel thread here is worth noting: Hurwicz, Maskin, Myerson (2007) for the foundations of mechanism design theory; Roth (2012) for taking it into practice.

See also: [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Extensive-Form Games|Extensive-Form Games]] for sequential games and credible threats, and [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] for cooperative game theory and fair division in coalitions.

---

## Oligopoly and Industrial Organization: Game Theory Before Nash

Here's a historical irony worth sitting with: the first game-theoretic model in economics predates Nash by over 100 years. Cournot's *Researches into the Mathematical Principles of the Theory of Wealth* (1838) analyzed two firms choosing quantities simultaneously, each taking the other's output as given. The Cournot-Nash equilibrium of that duopoly — where neither firm can improve profit by unilaterally changing its quantity — is a Nash Equilibrium in all but name.

Bertrand (1883) showed that if firms compete on price rather than quantity, the equilibrium collapses to marginal cost pricing with just two firms. That's the Bertrand paradox: a duopoly produces perfectly competitive outcomes. The difference between Cournot (moderate prices, above-competitive profits) and Bertrand (competitive prices, zero profits) comes entirely from changing what the strategic variable is. Industrial organization — the study of market structure and firm behavior — is almost entirely applied game theory.

Tirole's *The Theory of Industrial Organization* (1988) systematized this and remains a landmark. Entry deterrence, predatory pricing, product differentiation, R&D races — all are analyzed as games between firms who know they're being watched.

---

## Behavioral Economics: The Empirical Correction

Classical game theory assumes fully rational agents: stable preferences, correct beliefs, expected utility maximization. Behavioral economics documents the systematic ways this fails.

The **Ultimatum Game** is the canonical example. Player A receives $10 and proposes a split. Player B accepts or rejects — if rejected, both get nothing. Classical theory predicts: A offers the minimum possible amount, B accepts anything positive (something beats nothing). What actually happens: A typically offers 40-50%, and B regularly rejects offers below 30%, even though rejection is "irrational" by standard criteria. The game reveals that humans have strong fairness preferences and are willing to incur costs to punish perceived unfairness — preferences classical game theory has no room for.

Public goods experiments show similar deviations: people contribute more than the Nash prediction in early rounds, conditional on others contributing, and contributions decay when defection goes unpunished — but revive when punishment mechanisms are introduced. The behavior is sophisticated in ways classical theory misses, but not in the way classical theory predicts.

Kahneman and Thaler are the twin architects here. Kahneman (with Tversky) documented the systematic biases — anchoring, loss aversion, framing effects, probability distortion — that characterize System 1 reasoning. Thaler operationalized this into policy (nudges, choice architecture, retirement savings design). Both won Nobels. Behavioral economics is essentially game theory's empirical shadow: the catalog of where the rationality assumption breaks and in which direction.

The unresolved tension: can behavioral findings be incorporated into formal theory, or do they permanently undermine the project of a unified rational-choice economics? Some (Thaler, Sunstein) think behavioral insights can be grafted onto the standard framework via choice architecture. Others think the deviations are deep enough to require a different foundation entirely.

---

## Evolutionary Game Theory in Economics

EGT offers a different resolution to the behavioral critique: drop the rationality assumption entirely and replace it with selection dynamics. Strategies that yield higher payoffs spread through populations; strategies that yield lower payoffs die out. The equilibrium concept (Evolutionarily Stable Strategy) doesn't require anyone to calculate anything — it's an emergent property of selection pressure.

For economics, this matters in a specific way: it provides an equilibrium *selection* mechanism. Many games have multiple Nash Equilibria and no internal reason to pick among them. Replicator dynamics can select among them based on which equilibria are robust to invasion by alternative strategies. This is valuable not because markets are literally biological, but because EGT gives you a principled story about which equilibria are "more likely" to emerge when you let a system evolve rather than assuming agents coordinate on them from the start.

The deeper implication: if cooperative norms, property rights, and market conventions can emerge from evolutionary dynamics without anyone designing them, that changes how you think about the origins and stability of economic institutions.

---

## Open Questions

The interesting threads right now:

**Can behavioral economics and classical game theory be reconciled?** Prospect theory (Kahneman-Tversky) can be embedded into game-theoretic models by replacing expected utility with probability-weighted value functions. But this produces a zoo of competing behavioral models without a clean unifying framework. It's possible that behavioral economics will remain a collection of corrective patches rather than a unified alternative.

**Mechanism design for AI-mediated markets.** Algorithmic pricing, high-frequency trading, recommendation engines that shape demand — these involve agents (algorithms) that play games against each other and against humans, but at speeds and scales that make the "rational deliberation" story even less plausible. If the players are AIs optimizing faster than humans can respond, what does mechanism design need to look different? What equilibria emerge when the agents are RL models trained against each other?

**Which equilibria actually emerge?** The folk theorem tells us almost anything can be an equilibrium in repeated games. EGT helps narrow this, but the general problem of equilibrium selection in complex real-world games is unsolved. Experimental economics has produced rich data; connecting it to a clean theory is still ongoing.

---

## Key Texts

- Cournot — *Researches into the Mathematical Principles of the Theory of Wealth* (1838) — historically important, surprisingly readable
- Tirole — *The Theory of Industrial Organization* (1988) — the IO bible; rigorous but worth knowing exists
- Roth & Sotomayor — *Two-Sided Matching* (1990) — the theoretical foundation for matching markets
- Thaler & Sunstein — *Nudge* (2008) — accessible behavioral economics applied to policy
- Roth — *Who Gets What and Why* (2015) — Roth's own accessible account of market design; start here for mechanism design in practice
- Milgrom — *Putting Auction Theory to Work* (2004) — the bridge between theory and FCC spectrum auction practice

---

## Connections

- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Game Theory — Exploration]] — parent note; covers the full landscape of branches including cooperative, evolutionary, mechanism design, and behavioral
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-16 — Evolutionary Game Theory]] — deeper treatment of replicator dynamics, ESS, Hawk-Dove, and the philosophical implications; connects here via the equilibrium selection and "rationality-free" cooperation threads
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions]] — bounded rationality is the cognitive-science framing of what behavioral economics documents empirically; Gigerenzen's fast-and-frugal heuristics and Kahneman's System 1 biases are two readings of the same phenomenon
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Dual Process Theory System 1 and System 2]] — the Ultimatum Game rejection behavior is a paradigmatic System 1 override: fairness intuition beats expected-utility calculation; behavioral economics is largely the empirical record of these overrides
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Prospect Theory]] — behavioral game theory's attempt to embed Prospect Theory into formal models is the live frontier: replacing expected utility with PT's value function changes equilibrium predictions in auctions, bargaining, and cooperation games
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law]] — mechanism design can be read as the discipline's formal response to Goodhart's Law: instead of measuring a proxy and hoping it isn't gamed, design the game so the only strategy that satisfies the mechanism is the one that achieves the actual goal
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Hayek's Knowledge Problem]] — mechanism design is the formal attempt to work *around* the knowledge problem: elicit truthful revelation of distributed, locally held information through incentive design rather than requiring the planner to know it in advance; Vickrey's dominant-strategy auctions and Gale-Shapley matching are both answers to the question Hayek posed about aggregating dispersed knowledge
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Cobra Effect]] — the cobra effect is what mechanism design failure looks like in practice; dominant-strategy incentive compatibility is the formal property a mechanism needs to be cobra-proof
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — The Lucas Critique]] — rational expectations equilibrium (the foundation of the Lucas Critique) maps directly onto Nash Equilibrium: agents form beliefs about the policymaker's strategy and optimize against it, just as players do in a game
- [[MOC/Economics]] — home MOC (to be created)
