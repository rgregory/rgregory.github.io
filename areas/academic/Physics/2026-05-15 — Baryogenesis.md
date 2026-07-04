---
type: note
date: "2026-05-15"
tags: [physics, cosmology, particle-physics, symmetry]
status: filed
location: "02-Areas/Learning/Self-Study/Physics"
---

# Baryogenesis

## The Problem

The universe is made almost entirely of matter. This is a problem.

The Big Bang should have produced equal amounts of matter and antimatter. When matter meets antimatter, the two annihilate into photons. If the initial conditions were perfectly symmetric, every baryon should have been annihilated by its antibaryon partner, leaving a universe containing only radiation — no atoms, no stars, no observers.

Instead, one baryon per roughly one billion photon-antibaryon annihilations survived. This is the **baryon asymmetry**, quantified as the baryon-to-photon ratio:

$$\eta = \frac{n_B - n_{\bar{B}}}{n_\gamma} \approx 6 \times 10^{-10}$$

This number is measured with high precision from two independent sources — Big Bang Nucleosynthesis (the primordial abundance of helium, deuterium, and lithium) and the CMB power spectrum — and they agree. That agreement is itself strong evidence that the standard cosmological model is correct at the epoch of nucleosynthesis.

The tiny asymmetry $\eta \approx 6 \times 10^{-10}$ is why anything exists at all. The puzzle is how it got there.

## Sakharov Conditions (1967)

In 1967, Andrei Sakharov identified three necessary conditions that any mechanism for generating the baryon asymmetry must satisfy. They are known as the **Sakharov conditions**:

1. **Baryon number violation** — some physical process must produce more baryons than antibaryons. If baryon number (the count of baryons minus antibaryons) is strictly conserved, no asymmetry can be generated from symmetric initial conditions. At least one process must violate this conservation law.

2. **C and CP violation** — charge conjugation (C) and the combined charge-parity (CP) symmetry must be broken. If C were exact, every baryon-number-violating process would have a CP mirror image that produces antimatter at the same rate; the two contributions would cancel. CP violation ensures that matter-creating reactions proceed at a different rate than antimatter-creating ones, allowing a net asymmetry to accumulate. The Standard Model contains CP violation (in the CKM matrix for quarks, and potentially in the PMNS matrix for neutrinos), but the observed amount appears insufficient by orders of magnitude.

3. **Departure from thermal equilibrium** — in thermal equilibrium, every forward reaction is perfectly balanced by its reverse (the condition of detailed balance). Any asymmetry produced by a forward reaction would immediately be washed out by the reverse reaction. The universe must pass through a non-equilibrium phase — a period where some process is proceeding faster than its inverse — for a net asymmetry to accumulate and survive. The expanding universe provides this generically, but the expansion must happen fast enough relative to the relevant interaction rates.

All three conditions must be simultaneously satisfied. The Standard Model satisfies all three in principle — but not sufficiently.

## Major Mechanisms

Several proposals exist for how baryogenesis actually happened. None is confirmed.

### Electroweak Baryogenesis (EWBG)

The electroweak phase transition occurred roughly $10^{-12}$ seconds after the Big Bang, when the universe cooled through $\sim 100$ GeV and the Higgs field acquired its vacuum expectation value, breaking electroweak symmetry and giving the W and Z bosons their masses.

The key players are **sphalerons** — topological field configurations of the electroweak gauge fields that can convert leptons into baryons and vice versa, violating baryon number by 3 units at a time. Sphaleron processes are unsuppressed at temperatures above the electroweak scale and suppressed exponentially below it.

The scenario: during a first-order phase transition, bubbles of the broken phase nucleate and expand. At the bubble walls, departure from thermal equilibrium is strong. CP-violating interactions at the wall bias the sphaleron rate, producing a net baryon asymmetry inside the bubbles. Once the bubble interior is in the broken phase, sphalerons are suppressed and the asymmetry is preserved.

The problem: the Standard Model gives a **crossover**, not a first-order phase transition, for the Higgs mass of 125 GeV. The departure from equilibrium at a crossover is too small. Additionally, the CP violation from the CKM matrix is insufficient. EWBG requires new physics — an extended Higgs sector, supersymmetry, or other BSM additions — to strengthen the transition and add CP violation. It is theoretically elegant and experimentally testable: a strong first-order EWBG transition would produce a stochastic gravitational wave background detectable by LISA (launch ~2034), and may leave signatures at the FCC.

### GUT Baryogenesis

Grand Unified Theories (GUTs) — which embed the Standard Model gauge group $SU(3) \times SU(2) \times U(1)$ into a larger group such as $SU(5)$ or $SO(10)$ — naturally contain heavy gauge bosons (X and Y bosons) whose masses sit at the GUT scale, $\sim 10^{16}$ GeV. These bosons violate baryon number directly; their decay into quarks and leptons can proceed at different rates for particles and antiparticles (if CP is violated), satisfying all three Sakharov conditions.

This was historically the first baryogenesis mechanism proposed (Yoshimura 1978, Weinberg 1979), and it is conceptually the most straightforward. The universe was at the GUT temperature $\sim 10^{16}$ GeV at roughly $10^{-36}$ seconds, and X/Y boson production and decay would have generated an asymmetry.

The problem: if inflation occurred after the GUT scale — as most inflationary models require — it dilutes any pre-existing asymmetry exponentially. Reheating after inflation would need to reach the GUT scale to regenerate the asymmetry, but high reheating temperatures create a gravitino overproduction problem in supersymmetric theories. GUT baryogenesis remains viable in specific models but is not the leading candidate.

### Leptogenesis

Leptogenesis, proposed by Fukugita and Yanagida (1986), generates a **lepton asymmetry** first, then converts it into a baryon asymmetry via sphalerons.

The mechanism requires heavy right-handed Majorana neutrinos, which are a natural prediction of the seesaw mechanism — the leading theoretical explanation for why ordinary neutrinos have such small masses. These heavy neutrinos, with masses well above the electroweak scale ($\sim 10^{10}$–$10^{15}$ GeV), decay in the early universe. If their decay is CP-asymmetric (which it can be, given complex Yukawa couplings), it produces a net lepton asymmetry. Sphalerons, which violate both baryon number and lepton number but preserve $B - L$, convert part of this lepton asymmetry into a baryon asymmetry at the electroweak scale.

Leptogenesis is currently the leading theoretical candidate for several reasons:
- It connects baryogenesis to the well-motivated seesaw mechanism and neutrino mass physics
- It does not require a first-order phase transition
- It operates at energy scales consistent with most inflationary models

The drawback is testability: the relevant heavy neutrino masses are far above any foreseeable collider energy. Low-scale leptogenesis variants exist that bring the scale closer to reach, but the parameter space is constrained. The observation of CP violation in neutrino oscillations (ongoing at experiments like NOvA and T2K, and future DUNE) would be consistent with but not proof of leptogenesis.

### Affleck-Dine Mechanism

In supersymmetric theories, there exist flat directions in the scalar field potential — directions along which the potential is exactly zero in the supersymmetric limit. These flat directions carry baryon or lepton number. During inflation, these scalar fields (called Affleck-Dine fields) can acquire large vacuum expectation values (VEVs). After inflation ends, the field evolves away from the flat direction and eventually decays into baryons.

Because the field VEV can be very large — comparable to the inflationary Hubble scale — the Affleck-Dine mechanism can produce baryon asymmetries orders of magnitude larger than other mechanisms. It is particularly relevant in scenarios where PBH formation requires a large initial density perturbation that also produces a large baryon asymmetry locally.

### PBH Baryogenesis

Primordial black holes evaporating via Hawking radiation in the early universe satisfy all three Sakharov conditions simultaneously:

1. **Baryon number violation**: if PBHs emit GUT-scale particles near the end of their evaporation (when the Hawking temperature $T_H = \hbar c^3 / 8\pi G M k_B$ climbs to GUT energies as the mass $M$ drops), these particles can decay with baryon-number-violating interactions.
2. **CP violation**: as above, the same GUT-scale decay processes violate CP.
3. **Departure from thermal equilibrium**: Hawking evaporation is inherently a non-equilibrium process — the black hole is shrinking irreversibly, and the radiation it emits is not in equilibrium with the surrounding plasma.

This mechanism, developed in detail by Baumann and collaborators, links the baryon asymmetry directly to the PBH mass spectrum from the early universe. It is attractive because it requires no new physics beyond what PBHs already need to exist — it is a prediction of combining general relativity, quantum field theory, and GUT-scale physics.

## Current Status

No baryogenesis mechanism is confirmed. The field is defined by an uncomfortable fact: the Standard Model satisfies all three Sakharov conditions, but the CP violation from the CKM matrix is too small by roughly ten orders of magnitude to explain the observed $\eta$. New physics is required.

The experimental situation:

- **CP violation in neutrino oscillations** — experiments like NOvA, T2K, and future DUNE are measuring the CP-violating phase $\delta_{CP}$ in the PMNS matrix. A large CP-violating phase would be consistent with leptogenesis but cannot confirm it.
- **Gravitational waves** — LISA and next-generation detectors could detect the stochastic gravitational wave background from a first-order electroweak phase transition, which would strongly support EWBG.
- **Collider searches** — the FCC (proposed successor to the LHC) could probe extended Higgs sectors relevant to EWBG and look for signs of new CP-violating physics.
- **PBH searches** — if PBHs are confirmed (via microlensing, gravitational waves, or Hawking radiation detection), PBH baryogenesis becomes a live candidate.

The baryon asymmetry is one of the great unsolved problems in physics. Unlike dark matter or dark energy, it is not a matter of detecting something new — it is a matter of explaining why something old (matter) exists at all.

## Philosophical Note

Baryogenesis is an existence problem. Without it, the universe contains only radiation. Every atom, every star, every mind is the consequence of a symmetry violation — $\eta \approx 6 \times 10^{-10}$, a one-in-a-billion excess of matter over antimatter — that occurred in the first fraction of a second after the Big Bang.

The Sakharov conditions are physics' answer to "why is there something rather than nothing?" — though they only push the question back to why those conditions were met, what broke the symmetry, and whether the asymmetry was inevitable or contingent. The Standard Model says CP violation is possible; it does not say how much is required or why the universe chose $\eta \approx 6 \times 10^{-10}$ rather than zero.

## Connections

- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Primordial Black Holes|Primordial Black Holes]] — PBH evaporation via Hawking radiation satisfies all three Sakharov conditions; as a PBH loses mass its Hawking temperature rises, eventually reaching GUT energies where baryon-number-violating decays occur; the non-equilibrium character of irreversible evaporation provides condition 3 for free; baryogenesis via PBH evaporation is a prediction of combining GR, QFT, and GUT-scale physics without additional assumptions
- [[02-Areas/Learning/Self-Study/Physics/2026-04-24 — Black Holes|Black Holes]] — Hawking radiation is central to PBH baryogenesis; the temperature formula $T_H = \hbar c^3 / 8\pi G M k_B$ is what connects black hole mass to GUT-scale emission; black hole thermodynamics (entropy, temperature, evaporation) is the physical basis for condition 3 in PBH baryogenesis
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Length|Planck Length]] — GUT baryogenesis operates at $\sim 10^{16}$ GeV and $\sim 10^{-36}$ s, close to the Planck epoch ($10^{19}$ GeV, $\sim 5 \times 10^{-44}$ s); the Planck scale is the energy at which all forces unify and quantum gravity dominates; baryogenesis mechanisms set upper bounds on how close to the Planck epoch the relevant physics must occur
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|What Is Emergence]] — the baryon asymmetry is the ultimate emergence story: a $10^{-9}$ fluctuation in the first second produces all matter in the observable universe; macroscopic structure — galaxies, stars, chemistry, life — emerges from a microscopic symmetry breaking that left behind one baryon per billion photons; the universe's entire material content is an emergent residue of a quantum asymmetry
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem]] — the baryon-to-photon ratio $\eta$ is a bulk statistic that hides the microphysics; its value is inferred from two independent observational windows (BBN and CMB) at very different scales and epochs; the agreement between these two $\eta$ measurements is itself a non-trivial aggregation result — the same number emerges from averaging over processes separated by 380,000 years and very different physical conditions
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — Nietzsche God Is Dead|Nietzsche — "God Is Dead"]] — both address the question theology once owned: "why is there something rather than nothing?" Nietzsche relocates value-creation from transcendent grounding to contingent human act; baryogenesis relocates the existence of matter from creation ex nihilo to a contingent symmetry breaking ($\eta \approx 6 \times 10^{-10}$ rather than zero); both push the question back one level without dissolving it — the Sakharov conditions specify the structure of the answer but not why those conditions were met, just as Nietzsche's Übermensch specifies the structure of value-creation without guaranteeing any particular values

See also: [[MOC/Physics]]
