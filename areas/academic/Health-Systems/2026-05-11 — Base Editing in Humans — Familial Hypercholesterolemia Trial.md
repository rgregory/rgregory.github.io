---
type: note
date: "2026-05-11"
tags: [health-systems, genetics, gene-editing, base-editing, self-study, area/learning]
status: filed
created: 2026-05-11
source: "https://www.fbae.org/blog/crispr-clinical-trials-2026/"
---

# Base Editing in Humans — Familial Hypercholesterolemia Trial (2022)

In 2022, **Verve Therapeutics** dosed the first human participant in a base editing trial targeting **familial hypercholesterolemia (FH)** — an inherited disorder that causes severely elevated LDL cholesterol and early-onset cardiovascular disease. This was the first in-human use of base editing technology.

---

## What Base Editing Is

Base editing is a next-generation gene editing approach developed in the David Liu lab at the Broad Institute (~2016). It uses a modified CRISPR-Cas9 system that has been disabled from making double-strand breaks. Instead, the catalytically impaired Cas9 (nickase) is fused to a **deaminase enzyme** that chemically converts one DNA base to another without cutting:

- **Adenine base editors (ABEs)**: convert A → G (A•T base pair to G•C)
- **Cytosine base editors (CBEs)**: convert C → T (C•G base pair to T•A)

The guide RNA still directs the system to the target location. The deaminase then makes a precise, single-letter chemical change at a defined position within the editing window. No double-strand break, no template DNA required, no HDR pathway needed.

This is important because double-strand breaks — the mechanism underlying conventional CRISPR-Cas9 — carry risk of chromosomal rearrangements and large deletions. Base editing largely avoids this.

---

## The Target: PCSK9

The FH trial targets the **PCSK9 gene** in liver cells. PCSK9 encodes a protein that degrades LDL receptors on hepatocytes. More PCSK9 = fewer LDL receptors = higher circulating LDL cholesterol. Gain-of-function mutations cause FH; loss-of-function mutations are protective against heart disease (naturally occurring in some populations).

Verve's approach: deliver base editors via **lipid nanoparticles (LNPs)** directly to the liver (the primary site of PCSK9 expression), introduce a specific point mutation that functionally inactivates PCSK9, and thereby permanently reduce LDL cholesterol — a one-time intervention replacing lifelong statin therapy.

---

## Trial Results (Phase 1b, HEART-1)

- Initial cohort showed **LDL cholesterol reductions of 39–55%** in the highest dose groups
- Effect appears durable — based on the mechanism, it should be permanent (somatic cells edited, not germline)
- One serious adverse event (cardiac) in a patient with severe pre-existing disease; causality assessment was complex
- The trial demonstrated that in vivo base editing via LNPs in humans is feasible, safe at tested doses, and produces clinically meaningful effects

---

## Why This Matters

**In vivo delivery** is the key advance over Casgevy. Casgevy requires extracting cells, editing them ex vivo, conditioning the patient with chemotherapy, and reinfusing. The FH trial delivers the editor directly into the body via an LNP injection — a vastly simpler administration pathway. If in vivo editing proves broadly applicable, it changes the cost and accessibility equation for gene therapy dramatically.

**Cardiovascular disease** is the leading cause of mortality globally. A one-time therapy that permanently lowers LDL could prevent millions of heart attacks and strokes, especially in FH patients for whom statins are insufficient.

**Platform validation**: The trial establishes the LNP + base editor platform. The same delivery mechanism and editing chemistry could be re-aimed at other liver-expressed genes (ANGPTL3, TTR for transthyretin amyloidosis, etc.).

---

## Status in 2026

- Phase 2 enrollment ongoing
- Competing programs from Beam Therapeutics, Prime Medicine using related base editing and prime editing platforms
- Regulatory agencies are developing frameworks for heritable versus somatic base editing; the liver-targeted LNP approach is firmly somatic, which avoids germline ethics concerns
- LNP delivery to tissues beyond the liver (CNS, muscle) remains a frontier challenge

---

## Connections

- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-01 — How Does CRISPR Work|How Does CRISPR Work]] — conventional CRISPR mechanism from which base editing departs; understanding the double-strand break pathway explains why avoiding it is valuable
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Casgevy — First FDA-Approved CRISPR Therapy|Casgevy]] — ex vivo CRISPR approach; base editing's in vivo LNP delivery is the next step in accessibility
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Bridge Recombinases — IS622 Mechanism|Bridge Recombinases]] — complementary large-scale editing tool; base editing, CRISPR, and bridge recombinases now cover nucleotide, gene, and chromosomal scales respectively
- [[02-Areas/Learning/Self-Study/Statistics/2026-04-03 — P-Values and Statistical Significance|P-Values and Statistical Significance]] — Phase 1b trial interpretation requires careful attention to sample sizes, effect confidence intervals, and the distinction between statistical and clinical significance
