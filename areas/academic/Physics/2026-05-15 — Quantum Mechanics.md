---
type: note
date: "2026-05-15"
tags: [physics, quantum-mechanics, foundations]
status: filed
location: "02-Areas/Learning/Self-Study/Physics"
---

# Quantum Mechanics

Quantum mechanics (QM) is the fundamental physical theory describing nature at the scale of atoms and subatomic particles. It replaces classical mechanics in the regime where energy and angular momentum are exchanged in discrete packets — quanta — and where the act of measurement irrevocably disturbs the system being measured. It is, by any measure, the most accurately tested theory in the history of science.

---

## Historical Development

### 1900 — Planck's Quantization

Max Planck resolved the "ultraviolet catastrophe" — the classical prediction that a hot body should radiate infinite energy at high frequencies — by proposing that electromagnetic radiation is emitted not continuously but in discrete packets, each with energy:

$$E = h\nu$$

where $h$ is Planck's constant ($6.626 \times 10^{-34}$ J·s) and $\nu$ is frequency. Planck himself considered this a mathematical trick, not a physical reality. He was wrong.

### 1905 — Einstein and the Photoelectric Effect

Einstein extended Planck's idea: if radiation is quantized at emission, it must be quantized in transit too. Light consists of discrete particles — photons — each carrying energy $E = h\nu$. This explained why shining light on a metal releases electrons only above a threshold frequency (independent of intensity), contradicting classical wave theory. Einstein received the Nobel Prize for this in 1921, not for relativity.

### 1913 — Bohr Model

Niels Bohr proposed that electrons orbit the nucleus only at discrete radii corresponding to quantized angular momentum ($L = n\hbar$, where $n$ is an integer and $\hbar = h/2\pi$). When an electron drops from a higher orbit to a lower one, it emits a photon whose energy equals the difference. The model correctly predicted the hydrogen spectrum but had no theoretical justification for why orbits were quantized.

### 1924 — de Broglie's Hypothesis

Louis de Broglie proposed that if light (a wave) can behave as a particle (photon), matter (a particle) should also behave as a wave. The de Broglie wavelength of a particle with momentum $p$ is:

$$\lambda = \frac{h}{p}$$

This explained Bohr's quantization: stable electron orbits are those where an integer number of de Broglie wavelengths fit around the circumference — a standing wave condition. Confirmed experimentally by electron diffraction (Davisson-Germer, 1927).

### 1925 — Heisenberg's Matrix Mechanics

Werner Heisenberg, working with Max Born and Pascual Jordan, developed the first complete formulation of quantum mechanics. Physical observables (position, momentum, energy) are represented as matrices, not numbers. The key insight: the order of measurement matters — position and momentum matrices do not commute:

$$[x, p] = xp - px = i\hbar$$

This non-commutativity is the mathematical origin of the uncertainty principle.

### 1926 — Schrödinger's Wave Equation

Erwin Schrödinger developed an equivalent but physically intuitive formulation: the quantum state is a wave function $\psi(\mathbf{x}, t)$ satisfying:

$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$

where $\hat{H}$ is the Hamiltonian operator (total energy). The time-independent version:

$$\hat{H}\psi = E\psi$$

is an eigenvalue equation: the allowed energies $E$ are its eigenvalues. Heisenberg and Schrödinger were shown by Dirac to be equivalent representations of the same underlying structure.

### 1926 — Born Rule

Max Born proposed what the wave function *means*: $|\psi(\mathbf{x})|^2$ is a probability density — the probability of finding the particle at position $\mathbf{x}$ upon measurement. This interpretation was not obvious and remains philosophically contested. Schrödinger himself rejected it; he thought his equation described a literal wave, not a probability amplitude.

### 1928 — Dirac Equation

Paul Dirac combined quantum mechanics with special relativity, producing an equation for the electron that:
1. Naturally incorporated electron spin (no longer an ad hoc assumption)
2. Predicted the existence of antimatter (the positron), confirmed in 1932
3. Required four-component "spinors" rather than scalar wave functions

$$\left(i\gamma^\mu \partial_\mu - \frac{mc}{\hbar}\right)\psi = 0$$

The Dirac equation marks the beginning of quantum field theory.

---

## Core Formalism

### State Vectors in Hilbert Space

In quantum mechanics, the complete description of a system at a moment in time is a **state vector** $|\psi\rangle$ (Dirac's "ket" notation) in an abstract complex vector space called a Hilbert space. The Hilbert space for a spin-1/2 particle is 2-dimensional; for a particle in 3D space it is infinite-dimensional.

The dual vector $\langle\psi|$ ("bra") allows inner products: $\langle\phi|\psi\rangle$ is a complex number representing the "overlap" between two states. The probability of measuring state $|\phi\rangle$ given the system is in state $|\psi\rangle$ is $|\langle\phi|\psi\rangle|^2$.

### Observables as Hermitian Operators

Physical quantities — position, momentum, energy, spin — are represented by **Hermitian operators** $\hat{A}$ (operators equal to their conjugate transpose: $\hat{A} = \hat{A}^\dagger$). Hermitian operators have:
- Real eigenvalues (physical measurements are real numbers)
- Orthogonal eigenvectors (distinct measurement outcomes are mutually exclusive)
- Eigenvectors that form a complete basis (every state can be decomposed into measurement outcomes)

### The Eigenvalue Problem

Measuring observable $\hat{A}$ on state $|\psi\rangle$ always yields one of the eigenvalues $a_n$, where $\hat{A}|a_n\rangle = a_n|a_n\rangle$. After measurement, the system is in the eigenstate $|a_n\rangle$ corresponding to the result obtained. This irreversible "collapse" is the measurement problem.

### Superposition Principle

Any linear combination of valid quantum states is also a valid quantum state:

$$|\psi\rangle = \sum_n c_n |a_n\rangle$$

where the complex coefficients $c_n$ are **probability amplitudes**. The probability of obtaining eigenvalue $a_n$ is $|c_n|^2$. Superposition is not ambiguity or ignorance — the system genuinely has no definite value of the observable until measured.

### Born Rule (formal statement)

If $|\psi\rangle = \sum_n c_n |a_n\rangle$ and you measure $\hat{A}$, the probability of outcome $a_n$ is:

$$P(a_n) = |\langle a_n | \psi \rangle|^2 = |c_n|^2$$

The probabilities sum to 1: $\sum_n |c_n|^2 = 1$ (normalization).

---

## Key Principles

### Quantization of Energy and Angular Momentum

Energy is quantized in bound systems (atoms, quantum dots, quantum wells). The hydrogen atom has discrete energy levels $E_n = -13.6 \text{ eV}/n^2$. Angular momentum is quantized: $L = \sqrt{l(l+1)}\hbar$ for orbital angular momentum with integer $l$, and $S = \sqrt{s(s+1)}\hbar$ for spin with half-integer $s$.

### Wave-Particle Duality

Quantum objects are neither classical waves nor classical particles. They exhibit wave behavior (interference, diffraction, superposition) when not measured, and particle behavior (discrete detection events) when measured. The double-slit experiment makes this explicit: a single electron fired at a double slit produces an interference pattern on the detector screen — but if you measure which slit it went through, the interference vanishes.

### Heisenberg Uncertainty Principle

For any two non-commuting observables $\hat{A}$ and $\hat{B}$:

$$\Delta A \cdot \Delta B \geq \frac{1}{2}|\langle[\hat{A}, \hat{B}]\rangle|$$

The most important cases:

- **Position-momentum**: $\Delta x \cdot \Delta p \geq \hbar/2$
- **Energy-time**: $\Delta E \cdot \Delta t \geq \hbar/2$

These are not measurement artifacts or technological limitations. They reflect the fact that position and momentum are Fourier conjugates: a state with definite position is a superposition of all momenta; a state with definite momentum is spread over all positions. The uncertainty is intrinsic to what it means to have a quantum state.

The energy-time relation explains the finite linewidth of atomic transitions (a state with finite lifetime $\Delta t$ has energy uncertainty $\Delta E$) and permits "virtual particles" in quantum field theory (energy can fluctuate by $\Delta E$ for a time $\Delta t \sim \hbar/\Delta E$).

### Pauli Exclusion Principle

No two identical fermions (half-integer spin particles: electrons, protons, neutrons, quarks) can occupy the same quantum state simultaneously. This follows from the antisymmetry requirement on fermionic wave functions: swapping two identical fermions introduces a minus sign, so if they're in the same state the wave function must be zero. The Pauli principle explains the stability of matter, the structure of the periodic table, and neutron star stability against gravitational collapse.

Bosons (integer spin: photons, gluons, Higgs, helium-4) have symmetric wave functions and can occupy the same state — which is why lasers work (stimulated emission fills one photon state) and why Bose-Einstein condensates form.

### Spin

Spin is an intrinsic angular momentum with no classical analog. An electron has spin-1/2: measured along any axis, it yields exactly $+\hbar/2$ or $-\hbar/2$. Spin is not the electron spinning on its axis — that model leads to surface speeds exceeding $c$. It is a purely quantum mechanical degree of freedom, described by 2-component spinors and the SU(2) symmetry group. Spin-1/2 particles require a 720° rotation to return to their original quantum state (a 360° rotation produces a sign flip). This has been confirmed experimentally with neutron interferometers.

---

## The Measurement Problem

The Schrödinger equation is linear and deterministic: given $|\psi(0)\rangle$, it predicts $|\psi(t)\rangle$ exactly. But measurement appears to produce a definite, random outcome with only probabilistic prediction. How do we reconcile a deterministic, reversible evolution (Schrödinger) with an apparently irreversible, non-deterministic collapse?

This is the measurement problem — arguably the deepest unresolved question in the foundations of physics.

### Copenhagen Interpretation (Bohr, Heisenberg)

The wave function is not a description of reality but a tool for calculating probabilities. There is a sharp divide between the quantum system and the classical measuring apparatus. When measurement occurs, the wave function "collapses" to an eigenstate — but this collapse is not a physical process; it is an update of the observer's knowledge. Questions about what the system was doing before measurement are meaningless. Copenhagen refuses to answer "what is really happening" — it only says what measurements will yield.

This is operationally effective but philosophically unsatisfying: where exactly is the quantum-classical cut? Why does observation have special status?

### Many-Worlds Interpretation (Everett, 1957)

Hugh Everett proposed that there is no collapse. The Schrödinger equation always applies — to the system, the apparatus, and the observer. Measurement entangles all three, and what we interpret as "collapse" is actually the universe branching into a superposition of worlds, one for each outcome. Every quantum outcome occurs; we find ourselves on one branch.

Many-Worlds is mathematically elegant (no additional postulates beyond the Schrödinger equation) but faces the "preferred basis problem" (why do worlds branch along measurement eigenstates, not some other basis?) and the probability problem (how do we derive the Born rule, $P = |\psi|^2$, from a theory that says all outcomes occur?).

### Decoherence

Decoherence is not an interpretation — it is a physical process. Real quantum systems are never perfectly isolated; they interact with their environment (air molecules, photons, electromagnetic fields). These interactions entangle the system with billions of environmental degrees of freedom. The interference terms between superposition branches become unmeasurably small, exponentially fast, on timescales from $10^{-23}$ s (a large molecule in air) to millions of years (an isolated atom in space). The apparent randomness and definiteness of measurement outcomes is, in this picture, a consequence of environmental entanglement.

Decoherence explains why we don't see macroscopic superpositions and why the appearance of collapse is sharp. But it does not fully solve the measurement problem: it explains why we *can't see* the interference between branches, not why we *find ourselves on one branch*.

### Wigner's Friend

Eugene Wigner proposed a thought experiment: Wigner's friend is in a lab, measuring a quantum system. From inside, the friend sees a definite outcome. From outside (Wigner's perspective), before learning the result, the system + friend + detector are all in superposition. The question: does consciousness collapse the wave function? Recent extended versions ("Wigner's friend extended") lead to contradictions in standard quantum mechanics, suggesting that not all agents can simultaneously apply the Born rule consistently — a hint that quantum mechanics may need modification at the level of observers.

### Quantum Zeno Effect

Continuous observation prevents quantum evolution. If a system is measured so frequently that it has no time to evolve away from its initial state, it is "frozen." The Zeno effect has been confirmed experimentally with unstable atomic states. It highlights that measurement in quantum mechanics is an active intervention, not a passive recording.

---

## Entanglement

Two particles are entangled when their quantum states cannot be described independently — the joint state cannot be written as a product $|\psi_A\rangle \otimes |\psi_B\rangle$.

Example: two electrons in a singlet state:

$$|\Psi^-\rangle = \frac{1}{\sqrt{2}}\left(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle\right)$$

If you measure electron A as spin-up along any axis, electron B will instantly be spin-down along that axis, regardless of the spatial separation.

### EPR Paradox (1935)

Einstein, Podolsky, and Rosen argued that quantum mechanics must be incomplete. If measuring A instantaneously determines B's state, then either: (a) there is non-local "spooky action at a distance" violating relativity, or (b) the particles had definite correlated values all along, encoded in "hidden variables" that QM doesn't describe. EPR favored (b).

### Bell's Theorem (1964)

John Bell derived inequalities that any local hidden variable theory must satisfy. Quantum mechanics predicts violations of these inequalities. The CHSH inequality, for example, bounds correlations between measurements on entangled pairs: local hidden variables require $|S| \leq 2$; quantum mechanics predicts $|S| \leq 2\sqrt{2} \approx 2.83$.

### Bell Inequality Violations

Alain Aspect's experiments (1982) confirmed that the Bell inequality is violated — ruling out local hidden variable theories. Loophole-free Bell tests (Hensen et al. 2015, multiple groups 2015) closed the detection loophole and locality loophole simultaneously. Nature is non-local in the sense that entangled correlations cannot be explained by pre-existing classical correlations or any local mechanism.

### No-Signaling

Despite the non-locality, entanglement cannot be used to send information faster than light. Measuring A does change the state of B instantly, but the outcome of the A measurement is random — the B observer learns nothing about whether A was measured until informed by a classical channel. No-signaling is a theorem of quantum mechanics: the reduced density matrix of B is unaffected by operations performed on A.

---

## Schrödinger's Cat

Schrödinger designed this thought experiment (1935) to show that the Copenhagen interpretation leads to absurdity at macroscopic scales. A cat is in a sealed box with a quantum device (a radioactive atom) that may or may not trigger a lethal mechanism. Before the box is opened, quantum mechanics (naively applied) describes the cat as being in a superposition of alive and dead states. When does collapse occur? At the detector? At the cat? At the observer's eye?

The cat illustrates why the quantum-classical boundary is problematic. The resolution in modern physics is **decoherence**: the cat's quantum state entangles with ~$10^{23}$ environmental degrees of freedom in microseconds — effectively collapsing the superposition before any human observes. The interference terms between "alive" and "dead" branches are suppressed by factors of $e^{-N}$ where $N$ is enormous. The cat is not literally in superposition in any observable sense; the branching is real (in Many-Worlds) or the off-diagonal terms are negligibly small (in decoherence). Either way, we open the box and find a classical world.

---

## Path Integral Formulation (Feynman)

Richard Feynman (1948) developed a third, equivalent formulation of quantum mechanics. The probability amplitude for a particle to travel from point A to point B is the sum over all possible paths connecting them, each weighted by $e^{iS/\hbar}$ where $S$ is the classical action along that path:

$$\langle B | A \rangle = \int \mathcal{D}[x(t)] \, e^{iS[x(t)]/\hbar}$$

The integral $\int \mathcal{D}[x(t)]$ is over all paths — including wildly non-classical trajectories. In the classical limit ($\hbar \to 0$), the phases oscillate wildly and cancel everywhere except near the path of stationary action (Fermat's principle, Hamilton's principle) — the classical trajectory. Quantum mechanics adds corrections from neighboring paths.

The path integral formulation is the natural framework for quantum field theory and has been essential in particle physics. It makes the connection to classical mechanics transparent: the classical path is the one that dominates when action $S \gg \hbar$.

---

## QM and Classical Mechanics

### Correspondence Principle (Bohr)

In the limit of large quantum numbers (large $n$), quantum mechanics must reproduce classical mechanics. This was a guiding constraint for early quantum theory: the frequency of radiation from an electron transitioning between adjacent high orbits approaches the classical orbital frequency.

### Ehrenfest's Theorem

The expectation values of position and momentum in quantum mechanics obey classical equations of motion:

$$\frac{d\langle x \rangle}{dt} = \frac{\langle p \rangle}{m}, \qquad \frac{d\langle p \rangle}{dt} = -\left\langle \frac{\partial V}{\partial x} \right\rangle$$

These are Newton's laws applied to expectation values. For a sharply peaked wave packet in a slowly varying potential, $\langle x \rangle$ follows the classical trajectory. Quantum corrections become important when the wave packet spreads or the potential varies significantly over the packet width.

### Classical Limit ($\hbar \to 0$)

As $\hbar \to 0$, the de Broglie wavelength $\lambda = h/p \to 0$, and wave behavior becomes negligible. Superpositions decohere instantaneously. The path integral is dominated by the classical path. Quantum discreteness (energy level spacing $\propto \hbar$) vanishes. The classical world is the limit of quantum mechanics, not a separate domain.

---

## What QM Does NOT Explain

### Gravity

Quantum mechanics and general relativity are mutually incompatible at their current formulations. Quantum field theory on curved spacetime (as in Hawking radiation calculations) treats spacetime as fixed — it does not quantize gravity. A full quantum theory of gravity — describing what happens at the Planck length ($10^{-35}$ m), inside black hole singularities, or at the Big Bang — does not yet exist. String theory and loop quantum gravity are candidate frameworks; neither has experimental confirmation.

### The Measurement Problem

Despite decades of work, no consensus exists on which interpretation of QM is correct. Copenhagen, Many-Worlds, Bohmian mechanics, objective collapse theories (GRW), relational QM, and QBism each handle the measurement problem differently — and they have different empirical consequences in exotic scenarios (Wigner's friend extended tests). This is not merely philosophical: the correct interpretation of QM determines what questions can be asked, and what the answer to "what really happened before measurement" could mean.

---

## Connections

- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Length|Planck Length]] — Planck's quantization of radiation (1900) was the birth of QM; the Planck length ($\ell_P \approx 1.616 \times 10^{-35}$ m) is where QM meets gravity and where current QM breaks down — it is the scale at which a quantum theory of gravity is required
- [[02-Areas/Learning/Self-Study/Physics/2026-04-24 — Black Holes|Black Holes]] — Hawking radiation is a quantum effect in curved spacetime: a black hole's gravitational field separates virtual particle pairs, allowing one to escape; the Bekenstein-Hawking entropy formula ($S = k_B A / 4\ell_P^2$) encodes QM in the thermodynamics of spacetime
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — both reveal fundamental limits of formal systems: Gödel on provability within axiomatic systems, QM on simultaneous measurability of conjugate observables; the measurement problem has a Gödelian flavor — a quantum system cannot fully represent its own measurement process from within
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — The Lucas-Penrose Argument|The Lucas-Penrose Argument]] — Penrose argues consciousness exploits quantum gravity (Orchestrated Objective Reduction, Orch-OR): quantum superpositions in microtubules collapse via gravitational self-energy at the Planck scale; QM is the framework he claims is insufficient and must be extended with gravitational state reduction
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|What Is Emergence]] — the classical world emerges from the quantum substrate via decoherence; smooth, deterministic macroscopic behavior is an emergent property of systems coupled to environments with enormous numbers of degrees of freedom; classicality is not fundamental — it is a high-entropy limit
- [[02-Areas/Learning/Self-Study/Philosophy/Nagel — What Is It Like to Be a Bat?|Nagel — What Is It Like to Be a Bat?]] — the measurement problem raises the question of whether observation requires consciousness (Wigner's interpretation); even physicists who reject this view must explain why the observer has special status; Nagel's hard problem and the measurement problem both locate an explanatory gap at the intersection of the physical and the experiential
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — General Relativity|General Relativity]] — QM and GR are mutually incompatible at their current formulations; QM cannot incorporate dynamical spacetime and GR has no consistent quantum extension; reconciling them is the central open problem in theoretical physics
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Heisenberg Uncertainty Principle|Heisenberg Uncertainty Principle]] — a core principle of QM: the non-commutativity of position and momentum operators is the mathematical source of the uncertainty relations; the uncertainty principle is not separate from QM but embedded in its formalism
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — String Theory|String Theory]] — one of the two leading candidate frameworks for a quantum theory of gravity; derives GR as a low-energy limit; the graviton is a closed string mode; the worldsheet is a 2D quantum field theory built on QM
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Loop Quantum Gravity|Loop Quantum Gravity]] — the other leading candidate; applies standard QM quantization directly to the gravitational field; spin networks are quantum states of spatial geometry in the same Hilbert-space sense as QM states
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Holographic Principle|Holographic Principle]] — the unitarity of QM (information conservation) is what the black hole information paradox puts at stake; the holographic principle vindicates unitarity by showing information is preserved on boundaries; the boundary theory in AdS/CFT is a quantum field theory built on QM
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Units|Planck Units]] — Planck units are where $\hbar = 1$; the natural language of QM at its deepest level; all QM commutation relations, path integrals, and uncertainty bounds simplify to dimensionally clean forms in Planck units
