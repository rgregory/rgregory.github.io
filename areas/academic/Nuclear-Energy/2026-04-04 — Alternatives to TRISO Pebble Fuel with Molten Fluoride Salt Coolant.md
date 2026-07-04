---
type: note
date: 2026-04-04
tags: [nuclear-energy, reactor-design, fuel-types, coolant, SMR, msr, htgr, TRISO]
status: filed
created: 2026-04-04
---

# Alternatives to TRISO Pebble Fuel with Molten Fluoride Salt Coolant

The alternatives break down by which component you're substituting — the fuel form, the coolant, or both.

---

## Alternative Fuel Forms (keeping salt coolant)

### 1. Prismatic Block Fuel (TRISO in graphite blocks)
- Same TRISO particles, but embedded in hexagonal graphite blocks instead of pebbles
- Blocks are stationary — no online refueling; reactor shuts down to swap fuel
- Used in: X-energy Xe-100, General Atomics GT-MHR
- Tradeoff: more predictable neutronics vs. loss of continuous refueling

### 2. Fuel-in-Salt (Dissolved Fuel)
- Uranium dissolved directly into the fluoride salt as UF₄ — no solid fuel form at all
- The salt IS the fuel AND the coolant
- Used in: Molten Salt Reactor Experiment (ORNL, 1960s), TerraPower MCFR, China TMSR-LF1
- Tradeoff: eliminates fuel fabrication complexity, but online salt chemistry challenges and tritium/fission product management in coolant itself

### 3. Plate/Pin Fuel with Salt Coolant
- Conventional metal-clad fuel pins or plates bathed in fluoride salt
- Similar to existing LWR fuel geometry, adapted for high-temperature salt
- Explored by Elysium Industries (molten chloride design)
- Tradeoff: familiar fabrication, but clad integrity at high temp is a challenge

---

## Alternative Coolants (keeping TRISO pebble fuel)

### 1. Helium Gas Cooling (HTGR)
- The most mature alternative — TRISO pebbles cooled by high-pressure helium gas
- Used in: HTR-PM (China, operational), PBMR (South Africa, cancelled)
- Tradeoff: excellent chemical inertness, high outlet temps (~750°C+); no tritium problem; no corrosion; but requires high-pressure vessel

### 2. Liquid Salt — Different Composition
- Instead of FLiBe, use:
  - **FLiNaK** (lithium + sodium + potassium fluoride) — no beryllium toxicity, easier handling, but less favorable neutronics
  - **KF-ZrF₄** — lower melting point (~390°C), no Be, no Li-6 tritium issue
  - **Chloride salts** (NaCl-UCl₃) — better for fast spectrum reactors; used in TerraPower MCFR
- Tradeoff: each salt has different corrosion, tritium, and activation profiles

### 3. Molten Lead or Lead-Bismuth Eutectic (LBE)
- Heavy liquid metal coolant, fast-spectrum reactor
- TRISO not typically used here (fast reactors prefer metallic or nitride fuels)
- Used in: Westinghouse LFR, BREST-OD-300 (Russia)
- Tradeoff: very high boiling point, but lead is heavy and corrosive to structural steel

### 4. Liquid Sodium
- Fast spectrum, sodium-cooled
- Natural pairing is metallic or oxide fuel pins, not TRISO
- Used in: TerraPower Natrium, GE PRISM
- Tradeoff: high heat transfer, well-understood; but sodium fires on air/water contact

---

## Completely Different Reactor Concepts

| Concept | Fuel | Coolant | Developer | Status |
|---------|------|---------|-----------|--------|
| BWRX-300 | UO₂ pins | Light water | GE Hitachi | Construction committed (Canada) |
| Natrium | Metallic U-Zr | Liquid sodium | TerraPower | Under construction (Wyoming) |
| MCFR | UF₄ in salt | Chloride salt | TerraPower | Design phase |
| ARC-100 | Metallic fuel | Sodium | ARC Clean Energy | Design phase |
| eVinci | UO₂ pins | Heat pipes | Westinghouse | Prototype testing |
| LFR-AS-200 | Nitride pins | Liquid lead | Newcleo | Design phase |

---

## Summary Decision Matrix

| Option | Passive Safety | Online Refueling | High Temp Output | Maturity |
|--------|---------------|-----------------|-----------------|---------|
| TRISO pebble + FLiBe (PB-FHR) | Yes | Yes | Yes | Medium |
| TRISO pebble + He (HTGR) | Yes | Yes | Yes (higher) | High |
| Fuel-in-salt (MSR) | Yes | Yes | Yes | Low–Medium |
| Metallic fuel + sodium | Yes | No | Medium | Medium |
| UO₂ pins + water (SMR) | Medium | No | No | High |

---

## Connections
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — TRISO Pebble Fuel and Molten Fluoride Salt Coolant|TRISO Pebble Fuel and Molten Fluoride Salt Coolant]] — the baseline design this note takes as its starting point
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — TRISO Particle Fabrication Process|TRISO Particle Fabrication Process]] — understanding why some alternatives (e.g., fuel-in-salt) are attractive requires understanding the fabrication constraints of TRISO itself
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — NuScale Power and SMR Technology|NuScale Power and SMR Technology]] — the SMR comparison table there and the decision matrix here together map the full competitive landscape; NuScale (UO₂ pins + light water) occupies the "high maturity, no passive safety at scale" cell
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Lindy Effect|The Lindy Effect]] — the Summary Decision Matrix here is implicitly a Lindy table: HTGR (TRISO pebble + helium) is rated "High" maturity because it has survived the most selection pressure; fuel-in-salt and the PB-FHR are rated "Low–Medium" because they have passed fewer real tests; the matrix encodes survival-selection logic even though it doesn't name it as such; Lindy would predict you should weight maturity more heavily than the matrix suggests when comparing options for early deployment
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Emergence — The Whole Is More Than Its Parts|Emergence — The Whole Is More Than Its Parts]] — the "Completely Different Reactor Concepts" table is a reminder that reactor safety is a system-level property: sodium's excellent heat transfer and metallic fuel's known behavior combine to produce a passive safety characteristic that neither component alone would suggest; each reactor type in the table is a different recipe for achieving the same emergent system property (walk-away safety) through different micro-level rules
