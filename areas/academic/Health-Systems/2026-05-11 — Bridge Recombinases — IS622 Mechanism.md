---
type: note
date: "2026-05-11"
tags: [health-systems, genetics, gene-editing, self-study, area/learning]
status: filed
created: 2026-05-11
source: "https://www.quantamagazine.org/videos/2024-biggest-breakthroughs-in-biology/"
---

# Bridge Recombinases — IS622 and Large-Scale Genome Editing (2024)

In 2024, researchers characterizing the **IS622 transposon system** identified a new class of genome-editing enzymes called **bridge recombinases**. Unlike CRISPR-Cas9, which makes targeted cuts at individual nucleotide sequences, bridge recombinases can insert, delete, or invert segments of DNA up to **1 million base pairs** in length — entire genes plus their regulatory regions.

---

## The Mechanism

Bridge recombinases are recombination enzymes encoded by insertion sequences (IS elements) — mobile genetic elements that bacteria have used for billions of years to rearrange their own genomes. The IS622 element was one of the first studied in detail.

The key distinguishing feature is **bridging**: the enzyme binds to two specific DNA sites simultaneously and brings them into physical proximity, catalyzing recombination between them. This allows:

- **Large-scale inversions** — flipping a megabase-scale segment end-for-end
- **Deletions** — excising an entire gene cluster including its promoters and enhancers
- **Insertions** — landing a new sequence at a precise genomic location at scale

The size range — up to 1 Mb — is what separates this from Cas9-based editing. CRISPR-Cas9 works efficiently at the scale of individual nucleotides to a few hundred base pairs. Bridge recombinases operate at the chromosomal architecture level.

---

## Why Regulatory Regions Matter

Most disease-causing genetic variation does not sit inside protein-coding genes — it sits in the non-coding regulatory regions that control when and how much a gene is expressed. Enhancers, silencers, promoters, and insulators can be kilobases to megabases away from the genes they regulate.

CRISPR-Cas9's precision targeting is excellent for correcting point mutations within genes. But for diseases driven by regulatory dysfunction — many cancers, complex polygenic disorders, developmental syndromes — the ability to move, invert, or delete entire regulatory domains is a different kind of tool. Bridge recombinases offer exactly that.

---

## Research Status (2024–2026)

- Initial characterization published 2024; the IS622 system is one of several bridge recombinases under investigation
- Programmability — the ability to target arbitrary sequences — is still being developed; native bridge recombinases have fixed site preferences, unlike guide-RNA-directed Cas9
- The field is actively engineering chimeric systems that combine the large-scale recombination capability with programmable targeting
- Applications being explored: chromosomal rearrangement correction (translocations in cancer), full-gene replacement therapies, and synthetic biology at the chromosomal scale

---

## Connections

- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Casgevy — First FDA-Approved CRISPR Therapy|Casgevy — First CRISPR Therapy]] — the current clinical gold standard; bridge recombinases address the complementary problem space (regulatory regions, large-scale architecture) that CRISPR cannot efficiently reach
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-01 — How Does CRISPR Work|How Does CRISPR Work]] — foundational CRISPR mechanism for comparison; the PAM requirement and cut-site logic contrast with bridge recombinase site preferences
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-05-11 — Base Editing in Humans — Familial Hypercholesterolemia Trial|Base Editing in Humans]] — another 2022/2024 precision editing approach operating at the single-base level; the three tools (Cas9, base editors, bridge recombinases) cover complementary scales of genomic intervention
- [[02-Areas/Learning/Self-Study/Biology/2026-04-15 — Molecular Computation|Molecular Computation]] — IS elements as ancient molecular machines; bridge recombinases as a case where evolution's toolkit is being repurposed for bioengineering
