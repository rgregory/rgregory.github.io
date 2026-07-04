---
type: note
date: "2026-05-15"
tags: [physics, planck-units, natural-units, foundations, dimensional-analysis]
status: filed
location: "02-Areas/Learning/Self-Study/Physics"
---

# Planck Units

The Planck units are the universe's own measurement system — a complete set of base units derived exclusively from the fundamental constants of nature, requiring no reference to human artifacts, Earth's properties, or any particular civilization. As Planck wrote in 1899: "for all times and all civilizations, even extraterrestrial and non-human ones."

---

## 1. What Natural Units Are

Every unit system is a choice. The SI meter was originally one ten-millionth of the distance from equator to North Pole. The kilogram was a platinum-iridium cylinder in a vault in Sèvres. The second was 1/86,400 of a solar day. These are anthropocentric: defined by human-scale phenomena and, ultimately, arbitrary conventions.

A **natural unit system** dissolves this arbitrariness by setting fundamental physical constants equal to 1. The constants become the yardstick. This is not merely convenient — it reveals which quantities are genuinely fundamental and which are conversion factors between units humans chose to measure separately.

Different choices of constants = 1 yield different natural unit systems:

| System | Constants set to 1 | Primary use |
|---|---|---|
| Gaussian (CGS) | $c = 1$ | Classical electromagnetism |
| Heaviside-Lorentz | $c = \hbar = 1$ | Quantum field theory |
| Geometrized | $c = G = 1$ | General relativity |
| Stoney (1881) | $c = G = e = 1$ (uses elementary charge, not $\hbar$) | Pre-quantum natural units |
| **Planck** | $c = G = \hbar = k_B = 1$ | Quantum gravity, fundamental physics |

Stoney units (G. Johnstone Stoney, 1881) were the first proposal for natural units — predating Planck by nearly two decades — but used the elementary charge $e$ as the quantum of action. Planck's 1899 system is superior because $\hbar$ is the truly fundamental quantum of action; $e$ is a derived quantity that depends on the fine-structure constant $\alpha \approx 1/137$.

---

## 2. The Three Defining Constants

Setting $c = G = \hbar = 1$ uniquely determines all Planck units. Each constant carries a physical meaning:

**$\hbar$ — the quantum of action** (reduced Planck constant, $1.055 \times 10^{-34}$ J·s)
Action is energy × time. $\hbar$ sets the scale below which quantum discreteness dominates over classical continuity. It appears in Heisenberg's uncertainty principle ($\Delta x \Delta p \geq \hbar/2$), in the Schrödinger equation, in spin quantization. Setting $\hbar = 1$ means measuring action in "one quantum."

**$G$ — the gravitational coupling** ($6.674 \times 10^{-11}$ m³ kg⁻¹ s⁻²)
$G$ sets the strength of gravity. It is absurdly small — the weakest of all forces by ~40 orders of magnitude. Setting $G = 1$ means measuring mass in units where gravitational self-energy is comparable to rest-mass energy. The weakness of gravity is why the Planck mass ends up macroscopic (see §4).

**$c$ — the causal speed limit** ($2.998 \times 10^8$ m/s)
$c$ is not just the speed of light — it is the conversion factor between space and time, the maximum speed of causal influence, the bridge between mass and energy ($E = mc^2$). Setting $c = 1$ unifies space and time measurement: one light-second of distance equals one second of time.

These three constants span three independent dimensions (mass, length, time). Setting all three to 1 uniquely determines a unit of each — there is exactly one combination with the right dimensions for each base quantity.

---

## 3. The Five Base Planck Units

### 3.1 Planck Length

$$\ell_P = \sqrt{\frac{\hbar G}{c^3}} \approx 1.616 \times 10^{-35} \text{ m}$$

The spatial resolution limit of spacetime. Below this scale, the act of measurement — which requires a photon energetic enough to resolve the distance — creates a black hole that swallows the geometry being probed (the Compton–Schwarzschild argument). The concept of "distance" loses meaning. See [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Length|Planck Length]] for the full derivation.

Scale comparison: ~10⁻²⁰ times the diameter of a proton. The LHC resolves to ~10⁻¹⁹ m — still 16 orders of magnitude above the Planck length.

### 3.2 Planck Time

$$t_P = \sqrt{\frac{\hbar G}{c^5}} = \frac{\ell_P}{c} \approx 5.391 \times 10^{-44} \text{ s}$$

The temporal resolution limit. The time it takes light to cross one Planck length. Before $t_P$ after the Big Bang, the density and temperature of the universe exceed the Planck scale, and no current physical theory can describe what happened. The Planck time is therefore the earliest moment physics can say anything meaningful about the universe's history.

The entire observable history of the universe — from the Planck epoch to now (~13.8 billion years = $4.35 \times 10^{17}$ s) — spans about $10^{61}$ Planck times.

### 3.3 Planck Mass

$$m_P = \sqrt{\frac{\hbar c}{G}} \approx 2.176 \times 10^{-8} \text{ kg} \approx 22 \text{ μg}$$

The mass at which a particle's gravitational self-energy equals its quantum rest energy — equivalently, the mass of a particle whose Compton wavelength equals its Schwarzschild radius. Both become equal to $\ell_P$.

**Strikingly macroscopic.** 22 micrograms is about the mass of a flea egg, a grain of salt, or a small sand grain. This is visible to the naked eye. It is 10 orders of magnitude more massive than a proton. In particle physics terms: $m_P c^2 \approx 1.22 \times 10^{19}$ GeV — the Planck energy in mass units.

Why so large? Because gravity is extraordinarily weak. You need an enormous amount of mass before gravitational effects compete with quantum effects. The Planck mass is where they finally become equal — and that equality point happens to sit in the macroscopic world, not the subatomic one.

A black hole with mass $m_P$ has a Schwarzschild radius of exactly $\ell_P$ and a Hawking temperature of exactly $T_P/8\pi$.

### 3.4 Planck Energy

$$E_P = m_P c^2 = \sqrt{\frac{\hbar c^5}{G}} \approx 1.956 \times 10^9 \text{ J} \approx 1.22 \times 10^{19} \text{ GeV}$$

The energy of a photon whose wavelength equals the Planck length — or equivalently, the rest energy of the Planck mass. This is the energy scale at which quantum gravitational effects become order-1: where graviton exchange becomes as strong as any other force, where the known laws of particle physics break down.

For comparison: the LHC operates at ~13,000 GeV per collision. The Planck energy is $10^{15}$ times higher. No accelerator built from known materials on a planet of finite size could approach this energy. In absolute terms, $E_P \approx 2$ GJ — roughly the energy released by half a ton of TNT, but concentrated in a single quantum.

### 3.5 Planck Temperature

$$T_P = \frac{E_P}{k_B} = \sqrt{\frac{\hbar c^5}{G k_B^2}} \approx 1.417 \times 10^{32} \text{ K}$$

The temperature at which the thermal energy per particle ($k_B T$) equals the Planck energy. This is the temperature of the universe at $t = t_P$ — the Planck epoch. Above this temperature, thermal fluctuations are energetic enough to create quantum-gravitational effects in the background spacetime itself.

The hottest known events in the observable universe (quark-gluon plasma at the LHC: ~$5 \times 10^{12}$ K) are about 20 orders of magnitude below the Planck temperature. The early universe passed through $T_P$ in the first $t_P$ of its existence.

---

## 4. Derived Planck Units

Beyond the five base units, further Planck quantities arise naturally:

| Quantity | Formula | Value | Physical meaning |
|---|---|---|---|
| Planck area | $\ell_P^2$ | $2.612 \times 10^{-70}$ m² | The "pixel" of the holographic screen; minimum area eigenvalue in LQG |
| Planck volume | $\ell_P^3$ | $4.222 \times 10^{-105}$ m³ | Smallest meaningful volume |
| Planck density | $m_P / \ell_P^3$ | $\approx 5.155 \times 10^{96}$ kg/m³ | Maximum possible density — the density of a Planck-mass black hole |
| Planck force | $m_P c / t_P = c^4/G$ | $\approx 1.211 \times 10^{44}$ N | The force unit; appears in Einstein's field equations |
| Planck charge | $\sqrt{4\pi\epsilon_0 \hbar c}$ | $\approx 1.876 \times 10^{-18}$ C | $\approx 11.7$ elementary charges; note $q_P \neq e$ |
| Planck momentum | $m_P c$ | $\approx 6.525$ kg·m/s | Momentum of a photon with wavelength $\ell_P$ |

**Planck density** deserves emphasis: $\sim 5 \times 10^{96}$ kg/m³ is incomprehensibly large. The density of a proton is ~$10^{17}$ kg/m³; the Planck density exceeds it by 79 orders of magnitude. This is sometimes called the maximum possible density — though strictly, it is the density at which quantum gravity dominates.

**Planck force** has a clean form: $F_P = c^4/G \approx 1.21 \times 10^{44}$ N. It appears naturally in Einstein's field equations (the coefficient of the Einstein tensor in terms of the stress-energy tensor is $8\pi G/c^4 = 8\pi/F_P$). At Planck force, the curvature of spacetime becomes order-1.

---

## 5. The Planck Mass Puzzle and the Hierarchy Problem

The Planck mass being macroscopic (~22 μg) is a profound clue about the structure of physics. It points directly to one of the deepest unsolved problems in theoretical physics: **the hierarchy problem**.

The weak force is mediated by the W and Z bosons, which acquire their mass through the Higgs mechanism. The Higgs boson has a measured mass of ~125 GeV. The Planck mass is ~$1.22 \times 10^{19}$ GeV. The ratio:

$$\frac{m_{\text{Higgs}}}{m_P} \approx 10^{-17}$$

Why is the Higgs 17 orders of magnitude lighter than the Planck mass? In quantum field theory, particle masses receive "radiative corrections" — quantum contributions that are naturally of order the largest energy scale in the theory (the cutoff). If the cutoff is the Planck scale, then the Higgs mass should be of order $m_P$ — but it isn't. Something is canceling these corrections to 34 decimal places.

Proposed resolutions:
- **Supersymmetry (SUSY)**: introduces superpartners that cancel quantum corrections order by order. The LHC has found no superpartners; the minimal SUSY models are severely constrained.
- **Large extra dimensions**: if gravity propagates in extra spatial dimensions, the true Planck scale could be much lower (TeV scale), making the hierarchy apparent rather than real.
- **Little Higgs / Composite Higgs**: the Higgs is a pseudo-Goldstone boson from a higher-symmetry breaking; its mass is protected by the broken symmetry.
- **Anthropic selection**: in a multiverse with varying Planck/Higgs ratios, only universes with small ratios produce long-lived stars and therefore observers. This is considered unsatisfying by most physicists.
- **No solution yet**: the hierarchy problem remains open.

The Planck mass is macroscopic because gravity is weak. Why gravity is weak — why $G$ is so small — is the hierarchy problem reframed.

---

## 6. Planck Units in Theoretical Frameworks

### String Theory

The fundamental object in string theory is a one-dimensional vibrating string. The natural length scale is the **string length** $l_s$, related to the string tension $\alpha'$ by $l_s = \sqrt{\alpha'}$. The string length is related to the Planck length by:

$$l_s = g_s^{1/2} \ell_P$$

where $g_s$ is the string coupling constant. In the perturbative regime ($g_s \ll 1$), the string scale sits above the Planck scale. Spacetime geometry is emergent from string dynamics at or near $\ell_P$; the classical smooth manifold of GR is an approximation valid at scales $\gg \ell_P$.

### Loop Quantum Gravity (LQG)

LQG quantizes spacetime directly using connection variables. Quantum states of geometry are **spin network** states, and the area operator has a discrete spectrum. The minimum nonzero eigenvalue of the area operator is:

$$A_{\min} = 4\pi\gamma\sqrt{3}\,\ell_P^2$$

where $\gamma \approx 0.2375$ is the Immirzi parameter. The Planck area $\ell_P^2$ is therefore literally the pixel size of space — geometry is granular below this scale, not continuous. The Planck length is promoted from an energy-scale argument to an actual discrete eigenvalue of a quantum observable.

### Holographic Principle and AdS/CFT

The Bekenstein-Hawking entropy formula:

$$S_{BH} = \frac{k_B A}{4\ell_P^2}$$

expresses black hole entropy in Planck areas. Each Planck area on the horizon corresponds to roughly one bit of information. This underlies the holographic principle ('t Hooft, Susskind): the information content of a volume of space is bounded by its surface area measured in Planck units. The Planck area $\ell_P^2$ is the resolution of the holographic screen — the fundamental pixel of reality.

In Maldacena's AdS/CFT correspondence, this becomes concrete: a $d$-dimensional gravity theory is exactly equivalent to a $(d-1)$-dimensional conformal field theory on its boundary. The Planck scale in the bulk sets the UV cutoff of the boundary theory.

### Generalized Uncertainty Principle (GUP)

Combining Heisenberg uncertainty with the Compton-Schwarzschild argument yields a minimum position uncertainty:

$$\Delta x \geq \frac{\hbar}{2\Delta p} + \alpha \ell_P^2 \frac{\Delta p}{\hbar}$$

The second term grows with momentum — investing more energy to localize a particle eventually creates a black hole instead of improving resolution. The minimum uncertainty is $\Delta x_{\min} \sim \ell_P$, achieved at $\Delta p \sim m_P c$. This appears in multiple approaches to quantum gravity as a model-independent consequence.

---

## 7. Historical Context

| Year | Event |
|---|---|
| 1874 | G. Johnstone Stoney proposes the first natural unit system, using $c$, $G$, and $e$ (elementary charge). Predates quantum mechanics — $\hbar$ is unavailable. |
| 1899 | Max Planck introduces Planck units in a paper to the Prussian Academy, replacing $e$ with $\hbar$ (which he had just derived). Writes that these constants "necessarily retain their meaning for all times and for all civilizations, even extraterrestrial and non-human ones." |
| 1905 | Einstein's photoelectric effect paper — $\hbar$ is confirmed as the quantum of action. |
| 1915 | General relativity — $G$ and $c$ unified as geometric quantities. |
| 1920s | Quantum mechanics formalized — $\hbar$ becomes central to the entire theory. Planck's 1899 intuition is vindicated: $\hbar$ was always the right quantum. |
| 1955 | John Wheeler coins "quantum foam" — the Planck-scale structure of spacetime. |
| 1967 | Bryce DeWitt writes the Wheeler-DeWitt equation: $\hat{H}|\Psi\rangle = 0$, the first attempt at a quantum equation for the universe. Planck units are its natural language. |
| 1972 | Jacob Bekenstein proposes that black holes have entropy proportional to horizon area in Planck units. |
| 1974 | Hawking derives black hole radiation — the Planck temperature becomes physically real as the temperature of an evaporating black hole. |
| 1995–present | String theory, LQG, and AdS/CFT all place the Planck scale at the center of quantum gravity research. |

---

## 8. Philosophical Significance

Planck units are not a human construct imposed on nature — they are the units that nature itself selects. Every other unit system (SI, CGS, imperial) requires an external reference: a physical artifact, a property of Earth, a biological fact about human perception. Planck units require only the laws of physics.

This gives them a distinctive philosophical status: they are the candidates for what a truly objective description of the universe would use. An alien civilization, starting from quantum mechanics and general relativity, would derive the same Planck length, the same Planck time, the same Planck mass — even if they never knew about meters, kilograms, or seconds.

At the same time, the Planck scale marks the edge of current knowledge — the domain where both general relativity and quantum mechanics break down, where something genuinely new is needed. The Planck units are simultaneously the universe's bedrock measurement system and the signpost at the boundary of what we understand.

---

## Connections

- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Planck Length|Planck Length]] — the spatial unit; that note covers the Compton-Schwarzschild derivation, GUP, holographic principle, and LQG in detail; this note is the family overview going deeper than the table in §The Planck Units Family
- [[02-Areas/Learning/Self-Study/Physics/2026-04-24 — Black Holes|Black Holes]] — Bekenstein-Hawking entropy is measured in Planck areas ($S = k_B A / 4\ell_P^2$); a Planck-mass black hole has Schwarzschild radius $= \ell_P$ and Hawking temperature $= T_P / 8\pi$
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Baryogenesis|Baryogenesis]] — Planck temperature and Planck time mark the earliest epoch; GUT baryogenesis at ~$10^{16}$ GeV is two orders below the Planck energy; PBH baryogenesis via Hawking evaporation encodes Planck units directly in the evaporation temperature
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Heisenberg Uncertainty Principle|Heisenberg Uncertainty Principle]] — Planck units are where $\hbar = 1$; the GUP extends Heisenberg with a gravitational correction that produces $\Delta x_{\min} \sim \ell_P$; Heisenberg is the quantum floor, Planck is the quantum-gravitational floor
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — General Relativity|General Relativity]] — Planck units are where $G = 1$; GR breaks down at the Planck scale; Einstein's field equations use $c^4/G$ (the Planck force) as a natural coefficient
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Quantum Mechanics|Quantum Mechanics]] — Planck units are where $\hbar = 1$; QM formalism simplifies; path integrals, commutation relations, and the uncertainty principle all become dimensionally clean in Planck units
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — String Theory|String Theory]] — the string length $l_s = g_s^{1/2} \ell_P$ is given in Planck units; strings vibrate at the Planck scale; the Planck energy is the natural UV cutoff of string theory; see §6.1
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Loop Quantum Gravity|Loop Quantum Gravity]] — the minimum area eigenvalue in LQG is $4\pi\gamma\sqrt{3}\,\ell_P^2$ — literally the Planck area times the Barbero-Immirzi parameter; Planck units are LQG's native language; see §6.2
- [[02-Areas/Learning/Self-Study/Physics/2026-05-15 — Holographic Principle|Holographic Principle]] — the Bekenstein-Hawking entropy is measured in Planck areas ($S = k_B A / 4\ell_P^2$); each Planck area encodes one bit; the holographic screen is pixelated at the Planck scale; see §6.3
