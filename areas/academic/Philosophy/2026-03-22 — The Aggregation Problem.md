---
type: note
date: "2026-03-22"
tags: [philosophy, epistemology, statistics, emergence, complexity, systems-thinking, critical-thinking, meta-cognition, self-study]
status: active
created: 2026-03-22
aliases: [The Aggregation Problem, Aggregation Problem]
---

# The Aggregation Problem — Levels of Description

There is a single structural insight scattered across a surprising number of fields — in philosophy, mathematics, statistics, evolutionary biology, and political theory. Expressed plainly: **the level of description you choose determines what you can see, and every level has a blind spot that is only visible from outside it.** This is not a limitation of any particular tool or method. It is a structural feature of all formal systems.

The vault contains eight distinct notes that each arrive at this same insight from a different direction. This is a synthesis of all of them.

---

## The Core Thesis

Any framework — logical, statistical, social, biological — operates at a chosen level of description. That level enables certain kinds of reasoning and makes others impossible. The things it cannot see are not randomly distributed: they are systematically the things that exist *between* levels, or only *above* the current level, or only *visible from outside it*.

This is not a pessimistic observation about human reason. It is a navigational tool. Once you know the blind spot is structural, you can ask: *what level is this analysis pitched at? What would I see if I moved one level up or down?*

---

## Four Primary Instances

### Hume — The Blind Spot of Induction

[[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Hume An Enquiry Concerning Human Understanding|Hume's Enquiry]] contains one of the most devastating arguments in the history of epistemology. The problem of induction asks: what justifies the assumption that the future will resemble the past? The answer cannot be rational, because any rational argument for induction would have to be either deductive (and there is no logical necessity connecting past to future) or inductive (using induction to justify induction — a circular argument). The *Uniformity of Nature* — the bedrock assumption of all empirical reasoning — is a presupposition of the system, not a conclusion derivable from within it.

Hume's resolution was psychological rather than rational: custom and habit are the actual mechanism of inductive belief, not reason. But the structural point stands: **inductive reasoning cannot justify its own foundations from within the level at which it operates.** The justification for the level is invisible from inside it.

### Gödel — The Blind Spot of Formal Systems

[[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's incompleteness theorems]] proved the mathematical analogue of Hume's insight. For any consistent formal system powerful enough to express basic arithmetic, there exist true statements that cannot be proved within that system. And — the deeper blow — no such system can prove its own consistency using only its own rules.

Gödel showed this by constructing a sentence G that encodes the claim "this statement is not provable in this system." If G is provable, the system is inconsistent. If G is not provable, the system is incomplete. The only way out of contradiction is a permanent incompleteness. **Truth exceeds provability.** There are things that are genuinely true which no derivation from within the system will ever reach.

The parallel with Hume is precise: both draw a hard limit around what a method can prove about its own foundations. The mathematician Hilbert believed he could build a complete, consistent, self-certifying system of all mathematical knowledge. Gödel proved this is structurally impossible. No system can fully audit itself.

### Simpson's Paradox — The Blind Spot of Aggregation

[[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] is a result from statistics that belongs in the same family, though it is rarely discussed alongside Hume and Gödel. The paradox: a trend that appears consistently in every subgroup of a dataset can reverse — or disappear — when those subgroups are combined into an aggregate.

The Berkeley admissions case is canonical. Aggregate data suggested gender discrimination: men were admitted at higher rates than women. Department-by-department analysis reversed the finding: in most departments, women were admitted at equal or higher rates. The paradox arose because women disproportionately applied to competitive departments with low acceptance rates. The aggregate masked this compositional difference entirely.

The deeper lesson, articulated by Judea Pearl in his work on causal inference, is that Simpson's Paradox cannot be resolved by more data alone. It requires an explicit causal model — a decision about *which level of analysis is the right one for the question being asked*. **Aggregating across groups without a causal model can reverse the apparent direction of a finding.** The level of aggregation chosen determines the conclusion reached. This is not a statistical error that better methods will eliminate — it is a structural feature of how levels interact.

### Emergence — The Blind Spot of Reduction

[[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|Emergence]] is the most general form of the same insight. A system exhibits properties at the macro level that cannot be derived from — or even described in the vocabulary of — the micro level. The ant colony exhibits logistics, architecture, and adaptive strategy; individual ants do not. The properties exist at a higher level of description and are invisible from a lower one.

Philip Anderson's formulation is exact: "More is different." Each level of complexity requires its own laws. The laws of chemistry are not derivable from quantum mechanics alone; the laws of neuroscience are not derivable from chemistry alone. [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Simple Rules Complex Behavior|Simple local rules]] produce global structures that are genuinely new — not merely complicated versions of what was present at the lower level.

This is the ontological version of the problem. Hume and Gödel show that epistemological and formal systems have blind spots above their level. Emergence shows that *reality itself* is organised into levels that cannot be collapsed without information loss. **The whole is not recoverable from the parts.**

---

## Four Secondary Instances

### The Dunbar Number — The Phase Transition Between Social Levels

[[02-Areas/Learning/Self-Study/Social-Science/2026-03-22 — The Dunbar Number|The Dunbar Number]] (~150) is the cognitive ceiling on stable social relationships a human can maintain. Below this threshold, groups self-regulate through reputation and direct personal knowledge — what works at this level is trust, informal accountability, and the direct relationship between action and social consequence. Above it, something new becomes necessary: institutions, codified rules, hierarchical enforcement mechanisms.

This is a phase transition between levels of social organisation. What works at one level — reputation, personal knowledge of every member — not only fails to scale but actively does not exist at the next level. The ~150 threshold is not just a quantitative change; it marks the point at which a qualitatively different mode of organisation becomes mandatory. The coordination problem that is invisible below the threshold becomes dominant above it.

The nested structure of Dunbar layers (~5, ~15, ~50, ~150, ~500, ~1500) is itself a multi-level hierarchy, each governed by different relational rules. Each level has its own logic that cannot be inferred from the level below it. This also connects to [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Power Law|Power Law]] distributions: the roughly geometric (approximately 3x) progression of layers parallels scale-free network structures, where preferential attachment at each level produces a power-law distribution of ties.

### Benford's Law — The Invisible Structure Above Individual Numbers

[[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] states that in naturally occurring numerical datasets, the digit 1 leads roughly 30% of the time, while 9 leads less than 5% — far from the uniform distribution intuition would predict.

No individual number in the dataset "knows" it is part of a Benford distribution. The structure is a property of the aggregate, invisible at the level of individual observations. It emerges from the fact that natural processes are multiplicative rather than additive — numbers spend proportionally more time in the leading-1 range on a logarithmic scale. This regularity is invisible from the level of single data points and only becomes visible when many data points are examined together.

This makes Benford's Law a diagnostic tool: a dataset that *should* conform but does not is a signal that something at the individual level has been manipulated. The aggregate-level signature detects individual-level tampering — but only because the aggregate structure itself is invisible from the individual level. The whole monitors the parts.

### Chomsky — Manufactured Consent as an Above-Dunbar Phenomenon

[[02-Areas/Learning/Self-Study/Social-Science/2026-03-21 — Chomsky on Systems of Power|Chomsky's propaganda model]] identifies a mechanism that operates specifically in the anonymous space above the Dunbar threshold. Below ~150, direct personal knowledge and reputation make it difficult to manufacture belief: you know the people around you and can evaluate claims against lived experience. Above it, nearly all knowledge about the world arrives through mediated representation — news, expert commentary, institutional credentialing.

Chomsky's five filters (ownership, advertising, sourcing, flak, ideology) describe the structural mechanisms by which the range of thinkable thought is narrowed. But the crucial framing is a levels-of-description problem: at the individual journalist level, each person may be acting with good faith and professional integrity. At the system level, the aggregate output systematically excludes certain kinds of claims and privileges others. The ideology operates at the level of the system, not the individual. Individuals within the system cannot see the filter from inside it — which is precisely the structure Gödel described in formal terms.

This is also why [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Hume An Enquiry Concerning Human Understanding|Hume's account of belief formation through custom and habit]] is Chomsky's philosophical foundation: repeated exposure to a frame, without rational argument, produces conviction. The mechanism works at the aggregate level of social habit, not at the level of individual reasoning.

### Power Law — The Tail is the Level That Matters

[[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Power Law|Power law distributions]] are scale-free: they have no characteristic typical value. The mean is not just uninformative — it actively misleads. In a power-law world, the tail is not an anomaly to be explained away. It is the signal. The largest city is not an outlier; it is a consequence of the same mechanism that produced every other city size. Ignoring it produces systematically wrong predictions.

The levels-of-description problem here is statistical rather than ontological: if you only look at the mean, you are operating at the wrong level of description for the phenomenon you are trying to understand. The information that matters — the structure of the tail — is invisible from the level of summary statistics. Moving to the full distributional level reveals what the mean conceals.

This is a particular instance of Simpson's Paradox reasoning: the level of aggregation (mean vs. full distribution) determines what you see. A financial model that assumes normally distributed returns will encounter events that appear to be 25-sigma impossibilities. Under a power-law model, those same events are merely unlikely. The choice of level is not neutral — it determines whether the result is unthinkable or predictable.

---

## The Meta-Point: Making the Level Explicit

Each of these eight cases exhibits the same structural feature:

1. A level of description is chosen — whether it is the vocabulary of a formal system, the method of a statistical analysis, the social scale of an institution, or the summary statistic used to characterise data.
2. That level enables certain conclusions and produces certain regularities.
3. There is something real that the level cannot see — and that something is not randomly located. It is systematically above the current level, or in the structure of the system itself, or in the transition between levels.
4. The fix is not to abandon the level but to make it explicit, and to ask what higher or lower levels would reveal.

Hume's fix: acknowledge that induction is a habit, not a proof — and work empirically rather than seeking certainty.

Gödel's fix: to prove a system's consistency, you need a stronger system. Hilbert's dream of a self-certifying closed system is a structural impossibility.

Pearl's fix for Simpson's Paradox: make the causal model explicit before aggregating. The question "which level is the right level?" is answered by the causal structure of the problem, not by the data alone.

The emergence fix: do not try to derive the higher level from the lower. Study each level with its own vocabulary and its own methods. Ask what the transition between levels produces.

**This is a navigational tool, not a counsel of despair.** It does not mean that knowledge is impossible, that statistics are useless, or that formal systems should be abandoned. It means that knowing the blind spot is structural allows you to act on it deliberately. The question is not whether your level of description has limits — it always does. The question is whether you know what those limits are and can move between levels when the problem requires it.

---

## Connections

- [[MOC/Self-Formation|Self-Formation MOC]] — the Aggregation Problem is the structural backbone of the self-formation cluster: the question "what is the self?" is unanswerable without specifying the level of description; at the level of drives, no unified "I" exists; at the level of narrative, one does; neither level is more real
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Hume An Enquiry Concerning Human Understanding|Hume — An Enquiry Concerning Human Understanding]] — the founding epistemological case: induction cannot justify its own foundations from within
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — the formal mathematical proof that truth exceeds provability; no system can fully audit itself
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Simpson's Paradox|Simpson's Paradox]] — the statistical instantiation: the level of aggregation chosen determines the conclusion; resolving it requires an explicit causal model
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|What Is Emergence]] — the ontological version: the whole has properties not derivable from the parts; each level requires its own vocabulary
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Simple Rules Complex Behavior|Simple Rules, Complex Behavior]] — how micro-level rules produce macro-level structures that cannot be read back into the lower level
- [[02-Areas/Learning/Self-Study/Social-Science/2026-03-22 — The Dunbar Number|The Dunbar Number]] — the phase transition between social levels: what works below ~150 (reputation, personal trust) does not exist above it in the same form; institutions are a higher-level phenomenon
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Benford's Law|Benford's Law]] — aggregate statistical structure invisible at the level of individual data points; a diagnostic tool that uses the higher level to monitor the lower
- [[02-Areas/Learning/Self-Study/Social-Science/2026-03-21 — Chomsky on Systems of Power|Chomsky on Systems of Power]] — system-level ideology operating above the Dunbar threshold, invisible to participants reasoning at the individual level; Hume's belief formation as the psychological mechanism
- [[02-Areas/Learning/Self-Study/Statistics/2026-03-21 — Power Law|Power Law]] — the level of the mean conceals the structure of the tail; summary statistics operate at the wrong level of description for heavy-tailed phenomena
- [[02-Areas/Work/Security/2026-03-22 — NIST SP 800-171r2 CUI Security Requirements|NIST SP 800-171r2]] — the System Security Plan (3.12.4) is a Gödelian formal system: the organisation must produce a document that certifies its own security posture, yet no SSP can prove its own completeness from within — the auditor or third-party assessor is the necessary external meta-level; 3.14 monitoring is the applied instance of the aggregation insight: individual log events are noise, the meaningful signal only emerges at the aggregate distributional level
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Prion Information Paradox|The Prion Information Paradox]] — prion conformation as a molecular biology instance of the levels-of-description problem; the sequence level of description misses properties that only appear at the conformation level — the same structural move as every other case in this synthesis
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — Wittgenstein Beetle in a Box|Wittgenstein — Beetle in a Box]] — the canonical philosophy-of-language instance of the aggregation insight: the inaccessible private inner referent (what is in the box) is the level that drops out; meaning exists only at the public/functional level above it; Wittgenstein and Kant make structurally parallel moves toward the same conclusion
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — Nietzsche God Is Dead|Nietzsche — God Is Dead]] — the value-theory instance of the aggregation insight: the transcendent moral order (God) is a level of description imposed on the world and forgotten as imposed — the same structure as every other case in the synthesis; secular substitutes (nationalism, ideology) are the same move repeated
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-22 — Mycorrhizal Networks|Mycorrhizal Networks]] — a biological instance: the forest modelled at the organism level misses the dynamics entirely; the relevant unit of analysis (the fungal network) is emergent from interactions between individual organisms and invisible from the organism-level description
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Lindy Effect|The Lindy Effect]] — an applied corrective to the aggregation error of weighting old and new knowledge equally; survival-tested robustness is the relevant level of description, not recency; the Lindy Effect is what you see when you move to the right level for assessing non-perishable things
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Overview Effect|The Overview Effect]] — the Aggregation Problem made visceral and involuntary: the astronaut's shift in physical vantage point is the clearest empirical demonstration that the level of description determines what phenomena are available to cognition; borders exist at the language-game level and dissolve when the vantage point is removed
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — John Dewey — Philosopher|John Dewey]] — Dewey's anti-Cartesian naturalism targets the same artificial dualisms (mind/body, theory/practice, fact/value) that generate aggregation-style errors; his account of inquiry as moving between levels of description — from habitual practice to explicit reflection when breakdown occurs — is a practical version of the levels-of-description insight
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — Richard Rorty — Philosopher|Richard Rorty]] — Rorty's anti-foundationalism is precisely the aggregation insight applied to epistemology: there is no meta-level "mirror of nature" from which all vocabularies can be validated; the demand for such a meta-level is the philosophical error his entire career argues against
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — Thomas Kuhn — Philosopher of Science|Thomas Kuhn]] — Kuhn's paradigms are level-of-description phenomena: normal science operates within a level (the paradigm) that cannot audit its own foundations; the anomalies that trigger revolution are invisible at the level the paradigm provides; paradigm shifts are transitions between levels
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — Michel Foucault — Philosopher|Michel Foucault]] — Foucault's epistemes are the discourse-level analog: each historical episteme defines what can be seen and said; the conditions of knowledge are invisible from within the episteme, just as a formal system cannot prove its own consistency
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — Martin Heidegger — Philosopher|Martin Heidegger]] — the ready-to-hand/present-at-hand distinction is the experiential version of the aggregation insight: tools are transparent in use (invisible at the current level of engagement) and only become visible as objects when they break down; Heidegger shows the same structure Gödel proved formally
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Clathrus archeri Octopus Stinkhorn|Clathrus archeri]] — the insect cannot cross-check the olfactory signal against other channels; a biological instance of single-channel aggregation failure
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Chitin Walls Fungal Cell Structure|Chitin Walls — Fungal Cell Structure]] — distinguishing fungal from bacterial infection is an aggregation of imperfect signals (culture, gram stain, clinical context)
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Extracellular Digestion Absorptive Nutrition in Fungi|Extracellular Digestion]] — predicting ecosystem decomposition rates from individual enzyme kinetics is a textbook aggregation problem
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Differential Diagnosis Reasoning Under Uncertainty|Differential Diagnosis — Reasoning Under Uncertainty]] — DDx is the clinical instance of the aggregation problem: combining multiple imperfect signals to reach a defensible conclusion
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]] — Bayesian updating is the principled solution to the aggregation problem: it provides a mathematically coherent method for combining multiple imperfect evidence sources into a single posterior belief, making the weighting of evidence explicit rather than implicit
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-17 — The 20% of Bayesian You Need to Know|The 20% of Bayesian You Need to Know]] — the compressed five-idea reference; sequential updating (idea #5) is the operational procedure the aggregation problem demands: treat each posterior as the prior for the next piece of evidence rather than aggregating all evidence at once
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Heuristics — Fast Rules for Good-Enough Decisions|Heuristics]] — heuristics are low-computation aggregation strategies: instead of optimally weighting all evidence (Bayesian), use one cue (Take-the-best) or count cues (tallying). The question of when heuristics succeed vs. fail maps directly onto the question of when simplified aggregation is adequate and when it conceals a levels-of-description error
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition]] — metacognition is the ability to notice when your aggregation strategy is operating at the wrong level: to ask "am I combining evidence correctly, or am I anchoring on one signal and ignoring the rest?" The Dunning-Kruger effect is a failure of metacognitive access to one's own blind spots — which is precisely the aggregation insight applied inward
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Treatment of Hypothyroidism|Treatment of Hypothyroidism]] — treating to a TSH number vs. treating to symptoms; how do you weight a lab value against subjective patient report?
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-04 — Clinical Acronyms Internal Medicine Reference|Clinical Acronyms — Internal Medicine Reference]] — every multi-criteria scoring tool (qSOFA, CHADSVASC) is an aggregation problem: heterogeneous clinical signals collapsed into a single decision threshold
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Halteres Gyroscopic Stabilizers of Diptera|Halteres — Gyroscopic Stabilizers of Diptera]] — fly flight control aggregates signals from halteres, compound eyes, ocelli, and wing mechanoreceptors; biological multi-signal aggregation
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Ommatidia Units of the Compound Eye|Ommatidia — Units of the Compound Eye]] — compound eye as a literal aggregation problem; neural superposition as the brain's elegant aggregation solution
- [[02-Areas/Learning/Self-Study/Biology/2026-04-06 — The Square-Cube Law|The Square-Cube Law]] — a structural physical reason why micro-to-macro extrapolation fails: properties that are surface-dominated at small scale (diffusion, heat loss, sensing) become volume-dominated at large scale, changing qualitative system behavior; not just a failure of statistical aggregation but of geometric invariance assumptions
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — What Follows from the Aggregation Problem|What Follows from the Aggregation Problem?]] — the consequence note: draws out ontological pluralism (why reductionism fails in principle), limits of prediction (why Bayesian reasoning is the prior to the prior), the practical failure modes across security/medicine/policy, and the epistemic demands placed on any serious reasoner
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Holographic Principle|Holographic Principle]] — a precise physical version of the aggregation problem: the volume-level description of a region overcounts degrees of freedom; the boundary is the correct level of description; the bulk is an aggregation artifact; the information paradox was caused by operating at the wrong level
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Heisenberg Uncertainty Principle|Heisenberg Uncertainty Principle]] — uncertainty is a level-of-description phenomenon: the conjugate-variable tradeoff means no single description captures all physical properties simultaneously; position-space and momentum-space are complementary, not jointly complete — the same structural blind-spot that appears across every case in this synthesis
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — String Theory|String Theory]] — the landscape problem is an aggregation question at the deepest level: 10⁵⁰⁰ vacua represent 10⁵⁰⁰ distinct levels of description, and the question of which one is "ours" may not be well-posed without specifying additional selection criteria that themselves involve a higher-level description
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Primordial Black Holes|Primordial Black Holes]] — the PBH mass function is a levels-of-description problem at cosmological scale: the same primordial density field, smoothed at different scales, yields different PBH populations; the "dark matter fraction in PBHs" is not an observer-independent fact but a function of the aggregation scale applied to the early-universe density field; whether PBHs explain all dark matter, some, or none depends entirely on which mass window you aggregate over
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Baryogenesis|Baryogenesis]] — the baryon-to-photon ratio η ≈ 6×10⁻¹⁰ is the aggregation problem at cosmological scale: it is a single bulk statistic inferred from two independent observational windows (Big Bang Nucleosynthesis and the CMB) separated by 380,000 years and radically different physical conditions; the agreement between those two measurements is itself a non-trivial aggregation result; and the deeper question — "why this η rather than zero?" — pushes the aggregation problem to the Sakharov conditions themselves, which are physics' structural answer to why the chosen level of description (matter-dominated universe) exists at all
- [[MOC/Emergence|Emergence MOC]] — the broader cluster this synthesis draws from
- [[MOC/Learning|Learning MOC]]
- [[02-Areas/Learning/Self-Study/Philosophy/2026-05-16 — Connections — Benacerraf, Hume, and the Limits of Mathematical Knowledge|Connections — Benacerraf, Hume, and the Limits of Mathematical Knowledge]] — applies the Aggregation Problem's central thesis to the philosophy/mathematics boundary: Benacerraf's dilemma is the Aggregation Problem instantiated there — no meta-level exists from which semantic and epistemological adequacy are simultaneously visible
