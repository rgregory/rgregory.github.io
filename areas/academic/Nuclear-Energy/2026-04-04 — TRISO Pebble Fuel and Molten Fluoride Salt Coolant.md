---
type: note
date: 2026-04-04
tags: [nuclear-engineering, advanced-reactors, TRISO, molten-salt, PB-FHR, learning]
status: active
created: 2026-04-04
---

# TRISO Pebble Fuel and Molten Fluoride Salt Coolant

A reactor concept combining two distinct technologies from advanced nuclear design: TRISO coated particle fuel in pebble form, and a molten fluoride salt coolant.

---

## TRISO Fuel

**TRISO** (Tri-structural ISOtropic) is a coated particle fuel:

- A kernel of uranium oxycarbide (UCO) or UO₂ (~0.5–1 mm diameter)
- Surrounded by 4 layers:
  1. **Porous carbon buffer** — absorbs fission recoil
  2. **Inner pyrolytic carbon (IPyC)** — structural, retains fission gases
  3. **Silicon carbide (SiC)** — primary pressure vessel, retains fission products up to ~1600°C
  4. **Outer pyrolytic carbon (OPyC)** — protects SiC during fabrication

**Pebble form**: Thousands of TRISO particles embedded in a graphite matrix, formed into ~6 cm diameter spheres. The graphite also serves as moderator.

Key property: **inherent fission product retention** — the multilayer coating keeps cesium, strontium, and other radionuclides contained even if cooling is lost.

---

## Molten Fluoride Salt Coolant

Fluoride salts (e.g., **FLiBe** = lithium fluoride + beryllium fluoride, or FLiNaK) used as coolant:

| Property | Value |
|---|---|
| Operating temp | ~600–700°C |
| Boiling point | >1400°C |
| Heat capacity | High (similar to water) |
| Neutron moderation | Low (mostly transparent) |

Key advantages:
- **High thermal margin** — liquid at atmospheric pressure, no pressurization needed
- **Chemically stable** at high temperatures
- **Low vapor pressure** — no risk of steam explosion
- Excellent heat transfer

---

## The Combined Concept — PB-FHR

**Pebble Bed Fluoride-salt-cooled High-temperature Reactor (PB-FHR)**:

- Pebbles flow slowly through the reactor core (online refueling — no shutdown needed)
- Salt flows around the pebbles, extracting heat
- Graphite moderates neutrons; salt carries heat to a power cycle

Key institutions: UC Berkeley, Kairos Power (commercial), SINAP (China — TMSR project)

---

## Why This Combination Is Interesting

| Challenge | Solution |
|---|---|
| Core meltdown | TRISO retains fuel even at >1600°C — passive safety |
| High-pressure coolant failure | Salt operates near atmospheric pressure — no blowdown |
| Coolant loss accident | High boiling point means salt stays liquid; gravity drains to freeze-plug |
| Fuel handling | Pebbles flow continuously — no refueling shutdown |
| Proliferation | Highly dilute fuel, difficult to divert |

---

## Open Challenges

- **Tritium production** from FLiBe (Li-6 + neutron → T + He-4) — tritium must be captured before it permeates heat exchangers
- **Beryllium toxicity** in FLiBe — handling and maintenance hazards
- **Salt chemistry control** — redox potential must be tightly managed to prevent corrosion
- **Pebble-salt interaction** — buoyancy (pebbles float in salt), flow dynamics, and wear
- **Licensing** — no established regulatory framework for salt-cooled reactors in most countries

---

## Current Status

- **Kairos Power (KP-FHR)** — closest to deployment; received NRC construction permit for Hermes demo reactor (Tennessee, ~35 MWth) — first advanced non-LWR to receive such a permit in the US
- **China TMSR-LF1** — experimental fluoride salt reactor, operational since ~2021, though fuel-in-salt (dissolved), not pebble-bed

---

## Connections

- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — TRISO Particle Fabrication Process|TRISO Particle Fabrication Process]] — how the multilayer particles described here are actually manufactured
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — Alternatives to TRISO Pebble Fuel with Molten Fluoride Salt Coolant|Alternatives to TRISO Pebble Fuel]] — what happens when you substitute the fuel form, the coolant, or both
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — NuScale Power and SMR Technology|NuScale Power and SMR Technology]] — SMR landscape context; NuScale (iPWR) and Kairos (FHR) represent opposite ends of the design conservatism spectrum
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Emergence — The Whole Is More Than Its Parts|Emergence — The Whole Is More Than Its Parts]] — TRISO's passive safety is a textbook case of weak emergence: the multilayer coating (buffer carbon, IPyC, SiC, OPyC) produces a fission-product-retention property at 1600°C that exists in none of the individual layers alone; the whole safety claim only makes sense at the level of the assembled system, not at the level of any single coating layer; the PB-FHR then adds a second layer of emergence — a freeze-plug drainage system whose safety property arises from the combination of TRISO retention and salt physics, again not reducible to either component alone
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Lindy Effect|The Lindy Effect]] — the HTGR variant (helium-cooled TRISO, as in China's HTR-PM) has been tested since the 1960s and is now operational; the FLiBe salt-cooled version is newer and less selection-tested; the decision matrix in the Alternatives note implicitly encodes Lindy logic — "maturity" is the survival-selection signal
- [[02-Areas/Learning/Self-Study/Geology/2026-05-17 — Phonolite Lava Lakes and Mount Erebus|Phonolite Lava Lakes and Mount Erebus]] — cross-domain parallel: both TRISO and phonolite involve inorganic materials (SiC/PyC layers; alkali-feldspar/nepheline assemblages) maintaining structural integrity at extreme temperatures (~1600°C TRISO design limit; ~1000°C lava lake surface); the SiC pressure-vessel layer in TRISO and the anorthoclase phenocrysts in Erebus bombs are both inorganic mineral-phase systems studied for behavior under prolonged extreme heat
- No existing nuclear engineering / physics area in the vault — see Architect message below
