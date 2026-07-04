---
type: note
date: 2026-04-04
tags: [nuclear-energy, TRISO, fuel-fabrication, advanced-reactors, materials-science]
status: active
created: 2026-04-04T00:00:00
---

# TRISO Particle Fabrication Process

## How TRISO Particles Are Made

TRISO fabrication is a precision coating process, done layer by layer in a **fluidized bed chemical vapor deposition (CVD)** reactor.

### Step 1 — Kernel Fabrication

- Uranium oxycarbide (UCO) or UO₂ is formed into microspheres ~0.5–1 mm diameter
- Wet chemistry process: uranium nitrate solution converted via sol-gel or precipitation into gel spheres, dried and sintered at ~1400°C to densify

### Step 2 — Fluidized Bed CVD Coating

The kernel is suspended in upward gas flow inside a vertical tube furnace. Coating gases introduced sequentially:

| Layer | Gas Precursor | Temp | Result |
|-------|--------------|------|--------|
| Porous carbon buffer | Acetylene (C₂H₂) + propylene | ~1300°C | Low-density carbon ~100 μm — absorbs fission recoil, accommodates swelling |
| Inner PyC (IPyC) | Propylene or acetylene | ~1300°C | Dense isotropic pyrolytic carbon ~40 μm |
| SiC | Methyltrichlorosilane (CH₃SiCl₃) + H₂ | ~1500°C | Silicon carbide ~35 μm — primary fission product barrier |
| Outer PyC (OPyC) | Same as IPyC | ~1300°C | Dense isotropic carbon ~40 μm — protects SiC |

Particles tumble in gas flow, ensuring uniform coating on all sides.

### Step 3 — Inspection and Quality Control

- Coating thickness, density, sphericity, and defect rate characterized per batch
- X-ray, ceramography (polished cross-section microscopy), pressure testing
- Defect rates must be extremely low — cracked SiC = potential fission product release

### Step 4 — Pebble Fabrication (pebble-bed designs)

- ~15,000 TRISO particles mixed into graphite matrix (graphite powder + resin binder)
- Pressed into ~6 cm sphere under high pressure
- Outer ~5 mm pure graphite (no fuel — reflector + handling layer)
- Sintered/carbonized to cure binder and densify matrix

## Why It's Hard to Make

- SiC deposition at 1500°C with chlorosilane gases requires precise atmosphere control
- Coating uniformity across thousands of particles per batch is critical
- Very few facilities worldwide can produce commercial-scale TRISO fuel: Oak Ridge, BWX Technologies (U.S.); INET (China)

## Connections
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — TRISO Pebble Fuel and Molten Fluoride Salt Coolant|TRISO Pebble Fuel and Molten Fluoride Salt Coolant]] — end use of these particles in pebble-bed FHR designs
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — Alternatives to TRISO Pebble Fuel with Molten Fluoride Salt Coolant|Alternatives to TRISO Pebble Fuel]] — the fabrication constraints described here (SiC deposition, very few qualified facilities globally) are part of why some alternatives are attractive: prismatic block fuel uses the same TRISO particles, but fuel-in-salt eliminates the fabrication challenge entirely
- [[02-Areas/Learning/Self-Study/Nuclear-Energy/2026-04-04 — NuScale Power and SMR Technology|NuScale Power and SMR Technology]] — SMR landscape context; X-energy and Kairos use TRISO-based fuel
- [[02-Areas/Learning/Self-Study/Technical/2026-05-17 — M-DISC — Archival Optical Storage|M-DISC — Archival Optical Storage]] — another inorganic ceramic medium designed for extreme permanence; both rely on physically stable inorganic matrices (SiC / pyrolytic carbon vs. rock-like mineral compound) verified via accelerated stress tests rather than direct multi-century observation; both are write-once or irreversible by design
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Aggregation Problem|The Aggregation Problem — Levels of Description]] — the quality control problem in TRISO fabrication is a precise engineering instance of the levels-of-description blind spot: acceptable defect rates are specified at the batch level (cracked SiC layers per 10,000 particles), but fuel performance and fission product release are properties of the assembled pebble containing ~15,000 particles, which is then one of hundreds of thousands in the reactor core; the failure mode (one defective SiC layer triggers release in that particle) is invisible at the individual-particle inspection level and only becomes a safety-relevant signal at the aggregate-core level; managing this requires deliberately reasoning across levels, exactly the navigational move the Aggregation Problem note describes
