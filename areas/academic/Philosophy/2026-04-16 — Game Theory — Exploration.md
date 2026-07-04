---
type: note
date: "2026-04-16"
tags: [game-theory, economics, philosophy, decision-theory, rationality, self-study]
status: exploring
area: "[[02-Areas/Learning/Self-Study/Philosophy]]"
created: "2026-04-16"
---

# Game Theory — Exploration

Game theory is the formal study of strategic interaction — situations where the outcome for any one agent depends not just on their own choices, but on the choices of others. Born in mathematics (von Neumann & Morgenstern, 1944), it quickly colonized economics, evolutionary biology, political science, philosophy, and now computer science and AI alignment. Its central question is deceptively simple: *what does it mean to act rationally when others are also acting rationally?*

---

## Branches Worth Exploring

### Classical / Non-Cooperative Game Theory
The dominant tradition. Players are rational, self-interested, and choose strategies to maximize their payoff. Key concepts: Nash Equilibrium, dominant strategies, zero-sum vs. positive-sum games, mixed strategies.
- Why it matters: the mathematical backbone of most formal social science
- Where it breaks: assumes hyper-rational agents; real humans deviate systematically

### Cooperative Game Theory
Players can form binding coalitions. Focuses on how gains are distributed rather than individual strategy. Key concepts: the core, Shapley value, bargaining solutions (Nash bargaining, Rubinstein).
- Relevant to: contract theory, labor unions, international agreements, multi-party negotiations

### Evolutionary Game Theory
No rational agents — just populations whose strategies spread or die based on fitness. Replicator dynamics replace payoff maximization. Key concepts: Evolutionarily Stable Strategy (ESS), hawk-dove games, altruism puzzles.
- Philosophical payoff: shows cooperation and norms can emerge *without* intentionality or rational design
- Connects to: [[Biology]], emergence, Dawkins-style selectionism vs. group selection debates

### Mechanism Design (Reverse Game Theory)
Instead of analyzing a given game, *design* the rules to produce a desired outcome. Key concepts: incentive compatibility, revelation principle, Vickrey-Clarke-Groves mechanism, auction theory, matching markets, cooperative fair division.
- Real-world stakes: spectrum auctions, organ matching, voting systems, school choice, AI alignment
- Nobel thread: Hurwicz, Maskin, Myerson (2007); Roth (2012)
- See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] for the formal framework
- Four applied pillars:
  - [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Auction Theory|Auction Theory]] — revenue extraction and truthful bidding
  - [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] — stable allocations and preference revelation
  - [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] — cooperative game theory and fair division
  - [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Extensive-Form Games|Extensive-Form Games]] — sequential mechanisms and credible commitment

### Behavioral Game Theory
Empirical correction to classical theory. How do real humans actually play? Incorporates bounded rationality, fairness preferences, spite, reciprocity, and social norms. Key figures: Kahneman, Thaler, Camerer.
- Connects to: [[Cognitive-Science]] (dual-process theory, heuristics)
- Key experiment: the Ultimatum Game — people reject unfair offers they "should" accept

---

## Open Questions / Threads to Pull

1. **Is Nash Equilibrium a normative or descriptive concept?** If no one can improve by deviating *unilaterally*, that tells us about stability, not optimality. Lots of terrible equilibria are Nash equilibria (e.g., everyone defecting in Prisoner's Dilemma).

2. **The folk theorem and indeterminacy**: in repeated games, almost anything can be an equilibrium. This is a feature (cooperation is sustainable) and a bug (the theory loses predictive power). Does game theory explain behavior or just accommodate it post-hoc?

3. **Common knowledge of rationality**: classical results require not just that players are rational, but that each knows the other is rational, knows the other knows this, ad infinitum. How realistic is this? What breaks when it fails?

4. **Game theory and moral philosophy**: Can game theory ground ethics? Gauthier's *Morals by Agreement* tries. Where does it succeed and where does it fail against Kantian or virtue-based accounts?

5. **Evolutionary game theory vs. rational choice**: If cooperative norms can evolve without rationality, what work does the rationality assumption do? Is classical game theory just evolutionary game theory with a convenient fiction?

6. **AI and game theory**: Multi-agent reinforcement learning, mechanism design for AI alignment, and the problem of coordinating AI systems that are also "players." What's the current state?

---

## Foundational Synthesis Notes (2026-04-28)

Start here for grounded understanding of game theory foundations:

- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium: Historical Development|Nash Equilibrium: Historical Development]] — Context for why Nash's 1950-51 work unified economics and strategic reasoning
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Strategic Games Foundations|Strategic Games: Foundations & Assumptions]] — Prerequisites (players, actions, payoffs, rationality, best response)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Precise definition with four canonical examples
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Existence Proof|Nash Equilibrium: Existence Proof & Mathematical Foundations]] — Brouwer fixed-point theorem and existence proof
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Prisoner's Dilemma|Prisoner's Dilemma: Structure, Discovery, & Significance]] — Tucker's 1950 formulation and free-rider problem
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Bargaining Solution|Nash Bargaining Solution]] — Axiomatic approach to fair division and bargaining

## Key Texts (to investigate)

- von Neumann & Morgenstern — *Theory of Games and Economic Behavior* (1944) — the founding text
- Nash — original equilibrium papers (1950-51) — short and worth reading directly
- Axelrod — *The Evolution of Cooperation* (1984) — iterated Prisoner's Dilemma, accessible entry point
- Maynard Smith — *Evolution and the Theory of Games* (1982) — evolutionary branch
- Gauthier — *Morals by Agreement* (1986) — philosophy/ethics application
- Camerer — *Behavioral Game Theory* (2003) — empirical corrections
- Osborne & Rubinstein — *A Course in Game Theory* — free online; rigorous but readable

---

## Connections

- [[Philosophy]] — rationality, decision theory, ethics grounding
- [[Cognitive-Science]] — behavioral deviations, bounded rationality, dual-process theory
  - [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Dual Process Theory System 1 and System 2|Dual Process Theory]] — behavioral game theory is the empirical record of what happens when System 1 overrides the expected-utility calculations classical game theory assumes; the Ultimatum Game is a paradigmatic System 1 intervention (fairness intuition overriding payoff maximization)
  - [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics]] — bounded rationality in behavioral game theory is the same phenomenon as Gigerenzen's fast-and-frugal heuristics; real players use rules-of-thumb, not expected-utility maximization
- [[MOC/Social-Science.md]] — social norms, cooperation, collective action
  - [[02-Areas/Learning/Self-Study/Social-Science/2026-03-22 — The Dunbar Number|The Dunbar Number]] — cooperation below the Dunbar threshold (~150) can be sustained by reputation and personal knowledge alone, which maps directly onto game-theoretic conditions for cooperative equilibrium in repeated games; above that threshold, formal mechanisms (contracts, institutions) are required — exactly what mechanism design addresses
- [[Biology]] — evolutionary game theory, ESS, altruism
  - [[02-Areas/Learning/Self-Study/Emergence/2026-04-01 — Ant Colony Intelligence — Intentional or Merely Functional|Ant Colony Intelligence]] — ant foraging and colony coordination are real-world instantiations of evolutionary game theory: cooperation and efficient resource allocation emerge from local rules with no rational agent, demonstrating that cooperative equilibria can be stable without the rationality assumptions classical game theory requires
- [[MOC/Economics]] — the economics application of every branch covered here; see [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] for how Nash Equilibrium unifies price theory with strategic reasoning, mechanism design produces auction and matching markets, and behavioral economics documents the empirical failures of the rationality assumption
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-18 — The Dark Forest Theory|The Dark Forest Theory]] — Liu Cixin's cosmological prisoner's dilemma: a non-cooperative game at civilizational scale with no repeated interaction, no communication, and asymmetric detection costs that lock the equilibrium into permanent defection; a vivid applied case for teaching the conditions under which Nash cooperation fails
- [[03-Resources/Articles/2026-05-06 — Reading — Miscellanea — The War in Iran|The War in Iran (Devereaux, 2026)]] — The U.S.–Iran conflict as a concrete commitment-problem case study: escalation trap where domestic politics make backing down worse than fighting, collapsing the cooperative equilibrium that backward induction would predict rational actors to seek


---

## MOCs
- [[MOC/Work — Teaching|Teaching MOC]]
