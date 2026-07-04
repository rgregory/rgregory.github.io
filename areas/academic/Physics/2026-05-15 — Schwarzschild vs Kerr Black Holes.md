---
type: note
date: "2026-05-15"
tags: [physics, black-holes, general-relativity, cosmology]
status: filed
location: "02-Areas/Learning/Self-Study/Physics"
---

# Schwarzschild vs Kerr Black Holes

All black holes are defined by at most three numbers — mass, charge, and angular momentum — a result known as the **no-hair theorem**. The Schwarzschild and Kerr solutions are the two most physically important members of this family, differing on exactly one parameter: rotation.

## Schwarzschild Black Hole (1916)

Karl Schwarzschild derived the first exact solution to Einstein's field equations in 1915–1916 — while serving as an artillery officer on the Russian front. He sent the paper to Einstein from the trenches. He died of illness at the front months later.

**Defining properties:**
- Non-rotating, uncharged
- Spherically symmetric
- Single parameter: mass $M$

**Schwarzschild radius** (event horizon):
$$r_s = \frac{2GM}{c^2}$$

Everything within $r_s$ is causally disconnected from the outside universe. At the center sits a **point singularity** — a single mathematical point of infinite density where the curvature of spacetime diverges. General relativity breaks down here.

**No frame-dragging.** Spacetime outside a Schwarzschild black hole is static — there is no preferred direction, no rotation. An infalling observer experiences purely radial forces.

The Schwarzschild solution is the idealized, textbook case: perfectly clean, perfectly symmetric, analytically tractable.

## Kerr Black Hole (1963)

Roy Kerr found the rotating solution in 1963, nearly half a century after Schwarzschild. This was considered one of the most significant results in general relativity — the delay reflects how much harder the rotating case is.

**Defining properties:**
- Rotating, uncharged
- Axially symmetric (not spherically symmetric)
- Two parameters: mass $M$ + angular momentum $J$

The spin parameter is:
$$a = \frac{J}{Mc}$$

with maximum value $a = M$ (in geometrized units). When $a = 0$, the Kerr metric reduces exactly to the Schwarzschild metric.

### Two Horizons

Unlike Schwarzschild, the Kerr solution has **two distinct horizons**:

1. **Outer event horizon** — the point of no return, analogous to the Schwarzschild horizon
2. **Inner Cauchy horizon** — an inner boundary where the predictive power of general relativity fails. Inside the Cauchy horizon, the laws of physics as currently formulated cannot determine the future from the past. Determinism breaks down structurally, not just in practice.

### Ring Singularity

The Schwarzschild point singularity becomes a **ring singularity** in the Kerr solution — a one-dimensional ring in the equatorial plane. The geometry near this ring is pathological: closed timelike curves (paths through spacetime that loop back to their own past) are mathematically possible in the vicinity, though whether they are physically realizable remains an open question.

### Ergosphere

Outside the outer event horizon, the Kerr metric produces an **ergosphere** — a region where spacetime is dragged so violently by the black hole's rotation that no physical object can remain stationary relative to distant observers. Within the ergosphere, all objects are forced to co-rotate with the black hole; the only choice is how fast.

The ergosphere is bounded by the **static limit**, which lies outside the event horizon at the equator and touches it at the poles.

### Penrose Process

Because the ergosphere lies outside the event horizon, it is accessible. A particle entering the ergosphere can, in principle, split: one fragment falls into the black hole with negative energy (as measured from infinity), and the other escapes carrying more energy than the original particle had. Net result: rotational energy is extracted from the black hole. The black hole slows down slightly.

This is the **Penrose process** — a mechanism for mining rotational energy from a spinning black hole. In astrophysics, the relativistic jets from active galactic nuclei are believed to be powered by a magnetized analog of this process (the Blandford-Znajek mechanism).

### Frame-Dragging (Lense-Thirring Effect)

A rotating mass drags the surrounding spacetime along with it — like a spinning ball bearing turning honey. This **frame-dragging** (Lense-Thirring effect) is a consequence of Einstein's equations: mass-energy in motion generates not just gravitational attraction but a rotational distortion of spacetime geometry itself. The effect is weak for ordinary masses (confirmed for Earth's rotation by Gravity Probe B in 2011) and extreme near a Kerr black hole.

## The Four Solutions — Complete Family

| Solution | Rotation | Charge | Parameters |
|---|---|---|---|
| Schwarzschild (1916) | No | No | $M$ |
| Reissner-Nordström (1916–18) | No | Yes | $M, Q$ |
| Kerr (1963) | Yes | No | $M, J$ |
| Kerr-Newman (1965) | Yes | Yes | $M, J, Q$ |

The no-hair theorem says this table is complete: no other classical parameters characterize a stationary black hole. All the complexity of the collapsing star — its composition, shape, history — is erased. Only mass, charge, and spin survive.

In practice, astrophysical black holes are expected to be nearly uncharged (charge is quickly neutralized by surrounding plasma). The physically relevant solutions are Schwarzschild and Kerr.

## Why Kerr Is the Physically Relevant One

Every astrophysical black hole is expected to rotate, for a simple reason: **conservation of angular momentum**. Stars rotate; when a star collapses, its angular momentum is conserved and compressed into a much smaller object. Even a slowly rotating progenitor star produces a rapidly spinning black hole.

The spin parameter $a$ ranges from $0$ (Schwarzschild) to $M$ (extremal Kerr — maximum spin). An extremal Kerr black hole is a theoretical limit: reaching $a = M$ exactly would require infinite energy addition, so real black holes approach but do not reach it.

Schwarzschild is the pedagogically useful idealization. Kerr is the universe.

## Observational Evidence

The Event Horizon Telescope image of M87* (2019) shows an asymmetric brightness ring — the southern limb is brighter than the northern. This is consistent with **relativistic beaming**: matter in the accretion disk on the approaching side is Doppler-boosted, as expected for a system where frame-dragging organizes the flow around a spinning Kerr black hole. The data are consistent with a significant spin parameter, though precise measurement requires longer baselines.

## Connections

- [[02-Areas/Learning/Self-Study/Physics/2026-04-24 — Black Holes|Black Holes]] — the parent overview note; Schwarzschild and Kerr are the two fundamental exact solutions to Einstein's field equations and define the structure of all astrophysical black holes
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Primordial Black Holes|Primordial Black Holes]] — PBHs formed in the early universe could be either Schwarzschild or Kerr depending on the angular momentum of the collapsing density fluctuation; the geometry of this note describes the internal structure and horizon topology that PBHs would instantiate; evaporating PBHs probe the singularity structure (Schwarzschild point vs. Kerr ring) at Planck-scale energies; the mass gap events (GW190521) that PBHs explain involve black holes whose properties are fully described by the Kerr metric
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Length|Planck Length]] — a Planck-mass black hole has a Schwarzschild radius equal to the Planck length ($r_s = 2GM_P/c^2 = \ell_P$); at the Planck scale, the Schwarzschild/Kerr distinction dissolves because angular momentum is quantized and approaches zero in natural units — the classical smooth distinction between rotating and non-rotating geometries breaks down where spacetime itself becomes discrete
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — the Cauchy horizon inside a Kerr black hole is a physical analog of formal undecidability: it is a boundary beyond which the laws of physics as formulated cannot predict future states from past states; determinism fails not from ignorance but from structural incompleteness of the theory at that boundary, mirroring how Gödel's theorems identify true statements no consistent formal system can prove
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — The Lucas-Penrose Argument|The Lucas-Penrose Argument]] — Penrose's Orch-OR hypothesis invokes quantum state reduction at the Planck scale as the physical seat of non-computable cognition; the Kerr geometry is directly relevant: Penrose discovered the Penrose process (energy extraction from the ergosphere) and the Penrose diagrams that map the causal structure of spacetime around spinning black holes; the same physicist who proved the singularity theorems for Kerr black holes proposed that Planck-scale spacetime geometry implements non-algorithmic cognition
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|What Is Emergence]] — frame-dragging is an emergent geometric effect: a rotating mass-energy distribution generates new spacetime structure (the ergosphere, the Cauchy horizon) that has no analog in the static Schwarzschild case; the geometry that emerges from rotation is qualitatively different from, not merely a modification of, the non-rotating geometry

See also: [[MOC/Physics]]
