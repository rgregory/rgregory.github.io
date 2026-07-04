---
type: note
date: "2026-05-11"
tags: [health-systems, gene-editing, genomic-medicine, molecular-biology, self-study, area/learning]
status: filed
created: 2026-05-11
year: 2024
---

# Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)

Research published in 2024 described a new class of genome editing tools called **bridge recombinases**, with IS622 as the lead example. Unlike CRISPR, which cuts DNA at a single point and relies on cellular repair, bridge recombinases can **insert, excise, or invert large DNA segments** — up to one million base pairs — with programmable precision.

---

## What Bridge Recombinases Do

Standard CRISPR-Cas9 makes a double-strand break and then depends on the cell's repair machinery to incorporate changes. This limits the size of insertions (typically a few hundred to a few thousand base pairs before efficiency drops sharply) and creates risks from the break itself (off-target cuts, chromosome rearrangements).

Bridge recombinases work differently:

- They recognize **attachment sites** (short sequences called attB and attP) on two DNA molecules
- They catalyze **recombination directly** — physically bridging the two DNA molecules and exchanging segments without requiring a cut-and-repair cycle
- IS622 was characterized as programmable: its target specificity can be redirected by changing a **short RNA guide** (analogous to CRISPR's guide RNA but with different recombination logic)

The result: insertions of **entire genes plus their regulatory regions** (promoters, enhancers, insulators) in a single operation. Previous CRISPR approaches could rarely deliver a full gene with its control architecture intact.

---

## Why Scale Matters

Most genetic diseases are not caused by a single base-pair mutation. Many involve:
- Structural variants (large deletions, duplications, inversions)
- Loss of a gene's regulatory landscape (not just the coding sequence)
- Polygenic architectures requiring multiple simultaneous edits

CRISPR is poorly suited to all three. Bridge recombinases directly address the **large-scale editing gap**: the space between single-nucleotide edits (base editors) and full chromosome engineering (not yet clinically feasible).

---

## Current Status (2024)

- IS622 characterized in vitro and in cell lines; not yet in clinical trials
- Demonstrated successful insertion of ~1 Mb segments in human cells
- Programmability (retargeting via guide sequence changes) validated across multiple loci
- Off-target profile appears favorable compared to nuclease-based approaches, but head-to-head clinical data is not yet available

---

## Connections

- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — CRISPR Gene Therapy Approved — Casgevy (2023)|Casgevy — CRISPR Gene Therapy Approved]] — Casgevy works at small scale (disabling a regulatory element); bridge recombinases represent the next tier of editing ambition
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Base Editing in Humans — First Clinical Trial (2022)|Base Editing in Humans]] — base editors operate at the single-nucleotide scale; the three tools (base editing / CRISPR / bridge recombinases) form a precision spectrum from smallest to largest edit
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-01 — How Does CRISPR Work|How Does CRISPR Work]] — foundational CRISPR mechanism for contrast
- [[02-Areas/Learning/Self-Study/Biology/2026-04-15 — Molecular Computation|Molecular Computation]] — bridge recombinases are programmable molecular machines; their RNA-directed specificity is a form of molecular computation analogous to CRISPR
