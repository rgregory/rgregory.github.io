---
type: note
date: "2026-05-11"
tags: [health-systems, gene-editing, genomic-medicine, clinical-trials, self-study, area/learning]
status: filed
created: 2026-05-11
year: 2022
---

# Base Editing in Humans — First Clinical Trial (2022)

In 2022, the first human clinical trial using **base editing** was reported, treating a patient with **familial hypercholesterolemia (FH)** — a genetic condition causing dangerously elevated LDL cholesterol and early-onset cardiovascular disease.

The trial used a base editor to silence the **PCSK9** gene in liver cells in vivo, reducing LDL production at the source. Results published showed a single infusion achieving a **~60% reduction in LDL cholesterol** that was durable through the 6-month follow-up period.

---

## What Base Editing Is

Base editing is a CRISPR-derived technology that makes **single-letter changes to DNA** without cutting both strands of the double helix. A standard Cas9 cut creates a double-strand break (DSB); the cell's repair of a DSB is imprecise and can introduce unwanted insertions or deletions.

Base editors use a **nickase Cas9** (cuts only one strand) fused to a **deaminase enzyme**. The deaminase chemically converts one DNA base to another directly:
- **Adenine base editors (ABEs)**: convert A to G (A•T → G•C)
- **Cytosine base editors (CBEs)**: convert C to T (C•G → T•A)

This allows precise single-nucleotide changes — correcting a point mutation, or disabling a gene by introducing a premature stop codon — with a cleaner safety profile than standard CRISPR cutting.

---

## The Familial Hypercholesterolemia Trial

FH is caused by mutations in LDL receptor pathways; PCSK9 is a protein that degrades LDL receptors (fewer receptors = less LDL clearance = higher circulating LDL).

The trial approach:
- Delivered base editor via **lipid nanoparticles (LNPs)** — mRNA encoding the base editor + guide RNA, same delivery vehicle as mRNA COVID vaccines
- Targeted **hepatocytes (liver cells)** — naturally LNP-accumulating tissue
- Introduced a stop codon in PCSK9, permanently reducing its expression

The LNP delivery is significant: it means the editing machinery does not persist in the body; it acts once and degrades. This addresses a key safety concern about permanent gene therapy vectors (like AAV, which integrates into the genome).

---

## Positioning in the Editing Landscape

| Tool | Edit size | Mechanism | Clinical status (2024) |
|---|---|---|---|
| Base editor | 1 nucleotide | Deaminase, no DSB | Phase 1/2 trials |
| CRISPR-Cas9 (Casgevy) | Small indels / regulatory disruption | DSB + repair | FDA approved 2023 |
| Bridge recombinase (IS622) | Up to 1 Mb | Recombination | Pre-clinical |

---

## Connections

- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — CRISPR Gene Therapy Approved — Casgevy (2023)|Casgevy — CRISPR Gene Therapy Approved]] — the approved milestone that preceded and was enabled by the same ecosystem of gene editing tools
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)|Bridge Recombinases]] — the large-scale end of the editing precision spectrum
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-01 — How Does CRISPR Work|How Does CRISPR Work]] — Cas9 mechanism; base editors are a modification of the same platform
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Single-Cell Analysis Technology — Disease Detection and Biomarkers (2026)|Single-Cell Analysis Technology]] — base editing trials generate single-cell readouts to verify on-target editing rates and off-target profiles at cellular resolution
