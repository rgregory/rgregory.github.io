---
type: note
date: 2026-04-04
tags: [nuclear-energy, energy-systems, grid, transmission, SMR, emergence, complexity, area/learning]
status: filed
filed-date: 2026-04-04
location: 02-Areas/Learning/Self-Study/Nuclear-Energy/
created: 2026-04-04
---

# Challenges of Power Transmission with Remote Generation

Remote generation — stranded wind, hydro, nuclear, SMRs — creates a set of layered problems that are as much about physics and economics as they are about energy supply. The core challenge: getting electrons from where power is generated to where it is consumed, efficiently and reliably, over long distances.

## Physics

- **Resistive losses** — P_loss = I²R. Every kilometer of conductor dissipates power as heat. Long-distance transmission from remote sites makes this severe.
- **Reactive power** — AC lines generate and consume reactive power. Long AC lines require compensation (capacitor banks, STATCOMs) at intervals to maintain voltage stability.
- **Skin effect** — at AC frequencies, current flows along the conductor surface, effectively reducing the usable conductor cross-section over long distances.

## Engineering Tradeoffs

- **HVAC vs. HVDC** — High-voltage AC is the default but degrades above ~600 km. High-voltage DC (HVDC) eliminates reactive losses and is better for long hauls, but requires expensive converter stations at each end. Breakeven is roughly 600–800 km overhead, ~50 km undersea.
- **Thermal vs. stability limits** — conductor thermal capacity and grid stability limits (voltage/angular stability) often constrain transmission below the physical capacity of the wire.

## Infrastructure and Economics

- **Right-of-way** — remote terrain means permitting battles, environmental review, and construction in difficult conditions.
- **Who pays** — generators far from load centers can't always recover transmission costs. Merchant transmission economics are brutal without a captive off-taker.
- **Stranded investment risk** — a line built for one large remote plant becomes stranded if the generator underperforms or retires.

## Relevance to SMRs and Remote Nuclear

SMRs are designed to sidestep some of this: deploy generation near the load rather than transmit from a central plant. But SMRs near remote loads still face:

- Local grid stability (islanded microgrids are technically hard)
- Load-following vs. baseload tradeoffs
- Stranded asset risk when local load disappears

## Key Insight

> Remote generation is a transmission problem wearing an energy problem's clothes.

## Connections

- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — NuScale Power and SMR Technology|NuScale Power and SMR Technology]] — SMR design philosophy directly responds to the remote generation / transmission problem described here
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — Alternatives to TRISO Pebble Fuel with Molten Fluoride Salt Coolant|Alternatives to TRISO Pebble Fuel]] — broader SMR landscape note; both describe the same competitive environment from different angles
- [[MOC/Nuclear-Energy|Nuclear Energy MOC]] — this note extends the cluster into grid and transmission territory
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Simple Rules Complex Behavior|Simple Rules Complex Behavior]] — Grid stability at the transmission level is a classic emergent behavior problem: local rules (each line's thermal limit, each generator's governor response) produce global behavior (cascading failures, frequency collapse) that is hard to predict from the parts alone. See also [[MOC/Emergence|Emergence MOC]].
- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Halteres Gyroscopic Stabilizers of Diptera|Halteres — Gyroscopic Stabilizers of Diptera]] — MEMS gyroscopes (the technological implementation of the haltere principle) enable stable drone flight used in remote infrastructure inspection including transmission lines
