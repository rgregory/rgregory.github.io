---
type: note
date: "2026-05-16"
tags: [biology, molecular-biology, enzymes, replication, transcription]
status: filed
created: 2026-05-16
---

# DNA and RNA Polymerase — The Molecular Copy Machines

Polymerases are the enzymes that synthesize nucleic acid polymers — DNA or RNA — from a template strand. They are among the most consequential molecules in biology: every cell division, every gene expression event, every hereditary transmission depends on a polymerase reading a template and producing a faithful copy. The entire edifice of the Central Dogma rests on their accuracy.

The word "polymerase" describes function: an enzyme that builds polymers. But behind that simple description is a suite of molecular machines operating with staggering speed, processivity, and — in the case of DNA polymerase — extraordinary fidelity.

---

## DNA Polymerase — Copying the Genome

### The Core Mechanism

DNA polymerase reads a template strand in the 3'→5' direction and synthesizes the new complementary strand in the 5'→3' direction. This directionality is not arbitrary — it is dictated by chemistry. The enzyme adds nucleotides only to the free 3'-hydroxyl group of the growing chain. Run it backwards and there is no free 3'-OH to extend; the chemistry simply does not work.

This constraint creates an immediate geometric problem.

### The Leading/Lagging Strand Problem

The two strands of a DNA double helix run antiparallel — one 5'→3', the other 3'→5'. The replication fork opens in one direction. That means one strand (the **leading strand**) runs 3'→5' relative to the fork's direction of travel, so DNA polymerase can synthesize it continuously, chasing the fork as it opens. The other strand (the **lagging strand**) runs 5'→3' relative to fork movement — the wrong direction for continuous synthesis.

The solution is discontinuous synthesis. On the lagging strand, polymerase repeatedly loops back, synthesizes short fragments (100–200 nucleotides in eukaryotes, ~1,000–2,000 in bacteria), then releases. These fragments are the **Okazaki fragments**, named for Reiji and Tsuneko Okazaki who discovered them in the 1960s. Once synthesized, Okazaki fragments are joined by DNA ligase into a continuous strand.

### The Primer Problem

DNA polymerase cannot initiate a new strand from scratch — it can only extend an existing strand with a free 3'-OH. This is a design constraint with major consequences. Every new DNA strand begins with an RNA primer, synthesized by **primase** (a specialized RNA polymerase). The primer provides the free 3'-OH that DNA pol needs to get started. Later, the RNA primer is removed and replaced with DNA. On the leading strand this happens once per replication; on the lagging strand, at every Okazaki fragment.

This requirement also explains **telomere erosion**: at the linear chromosome ends in eukaryotes, the lagging strand can never fully replicate its 5' end because once the terminal RNA primer is removed, there is no upstream 3'-OH from which to fill the gap. Telomeres — repetitive non-coding sequences at chromosome ends — serve as a sacrificial buffer. **Telomerase** (a reverse transcriptase with its own RNA template) counteracts this erosion in germline cells and stem cells.

### Proofreading — the 3'→5' Exonuclease

DNA polymerase is not just a synthesizing enzyme — it is also an editor. Most replicative polymerases carry a built-in **3'→5' exonuclease** activity: a second active site that can recognize a mismatched base at the 3' end of the growing chain, excise it, and allow the correct nucleotide to be inserted. This is proofreading in real time.

The mechanism: if an incorrect nucleotide is incorporated, the base pairing is weak. The 3' end of the chain slips into the exonuclease active site. The mismatch is removed. The 3' end returns to the polymerase active site and synthesis resumes. The whole operation takes milliseconds.

Without proofreading, the intrinsic error rate of DNA synthesis is approximately **1 in 10^5**. With proofreading, it drops to **1 in 10^7**. Mismatch repair systems downstream bring it to **1 in 10^9–10^10** — roughly one error per genome duplication, per cell division.

### Processivity and the Sliding Clamp

Speed matters. *E. coli* replicative polymerase (Pol III) synthesizes ~1,000 nucleotides per second. Human replicative polymerases (~100 nt/s) are slower but must copy a genome roughly 6,000 times larger. To avoid wasting time repeatedly re-binding the template, polymerases use a **sliding clamp**: a ring-shaped protein complex that encircles the double-stranded DNA and tethers the polymerase to the template like a ring on a rod. The clamp is loaded by a **clamp loader** (RFC in eukaryotes, the γ-complex in bacteria) in an ATP-dependent step. Once loaded, the polymerase can synthesize thousands of nucleotides without dissociating.

Processivity — the average number of nucleotides synthesized per binding event — jumps from a few dozen (without the clamp) to hundreds of thousands with it. The sliding clamp is one of evolution's most elegant solutions to an engineering problem.

---

## The Replication Fork — The Full Molecular Machine

Replication does not happen with polymerase alone. At each replication fork, a coordinated team of proteins operates in concert:

| Protein | Role |
|---|---|
| **Helicase** (DnaB in bacteria; MCM complex in eukaryotes) | Unwinds the double helix by breaking hydrogen bonds; moves 5'→3' on the lagging strand template |
| **Primase** | Synthesizes RNA primers (8–12 nt in bacteria; ~10 nt in eukaryotes) to give DNA pol its starting 3'-OH |
| **SSB proteins** (single-strand binding proteins) | Coat the separated single strands to prevent reannealing and protect from nucleases |
| **Topoisomerase** (Type I and II) | Relieves supercoiling ahead of the fork; positive supercoils accumulate as the helix unwinds, and topoisomerase cuts and rejoins strands to release torsional stress |
| **DNA Polymerase III** / **Pol δ, ε** | Synthesizes the new strands; proofreads in real time |
| **RNase H / Pol I (bacteria); FEN1 (eukaryotes)** | Removes RNA primers |
| **DNA Ligase** | Seals nicks between Okazaki fragments; uses ATP (eukaryotes) or NAD⁺ (bacteria) as cofactor |

In eukaryotes, the two leading-strand and lagging-strand polymerases (Pol ε and Pol δ respectively) are held at the fork by proliferating cell nuclear antigen (PCNA) — the eukaryotic sliding clamp — while cohesion is maintained with the parental template by a complex called the replisome. This entire machine operates at two replication forks simultaneously (forks move bidirectionally from each origin of replication), and in humans there are ~30,000–50,000 origins active in S-phase.

---

## RNA Polymerase — Reading the Genome

### The Core Difference

RNA polymerase (RNAP) transcribes DNA into RNA. It shares the same 5'→3' synthesis direction and template-reading logic as DNA pol, but differs in three critical ways:

1. **No primer needed.** RNAP can initiate synthesis *de novo* — it can lay down the first nucleotide without a pre-existing 3'-OH. This is possible because RNAP holds the first two nucleotides in place using a different active site geometry that stabilizes the initial base pair without the aid of a primer.

2. **No proofreading.** RNAP has no intrinsic exonuclease for real-time mismatch correction. (Some RNAPs have a slow backtracking mechanism that can correct errors, but it is orders of magnitude less effective than DNA pol proofreading.)

3. **Synthesizes RNA, not DNA.** It uses ribonucleoside triphosphates (ATP, GTP, CTP, UTP), and the product is RNA — single-stranded, using uracil instead of thymine, with 2'-OH groups that make it far more chemically reactive than DNA.

### Promoter Recognition — Bacteria

In bacteria, RNAP is a multi-subunit enzyme (core: α₂ββ'ω) that requires a **sigma factor** (σ) to recognize promoters and initiate transcription. The σ factor dissociates after initiation, leaving the core enzyme to elongate. Different sigma factors recognize different promoter sequences, allowing bacteria to rapidly reprogram transcription under stress:

- **σ⁷⁰** — housekeeping genes (most genes, optimal growth conditions); recognizes the –10 and –35 elements
- **σ³²** — heat shock response; upregulated when misfolded proteins accumulate
- **σ⁵⁴** — nitrogen starvation response
- **σ²⁸** — flagella and chemotaxis genes

One sigma factor change rewires thousands of genes. It is one of the most efficient regulatory switches in biology.

### Promoter Recognition — Eukaryotes

Eukaryotic transcription is far more elaborate. There are three main RNA polymerases:

- **RNA Pol I** — transcribes ribosomal RNA (rRNA); found in the nucleolus
- **RNA Pol II** — transcribes all protein-coding genes (mRNA) and most non-coding RNAs
- **RNA Pol III** — transcribes tRNA, 5S rRNA, and other small structural RNAs

Pol II (the most studied) cannot bind its promoter alone. It requires **General Transcription Factors (GTFs)**: TFIIA, TFIIB, TFIID (which contains the TATA-binding protein, TBP), TFIIE, TFIIF, and TFIIH — which together assemble a pre-initiation complex at the promoter. TFIIH carries a helicase that unwinds the DNA to form the transcription bubble, and a kinase that phosphorylates Pol II's C-terminal domain (CTD), triggering promoter escape and elongation.

This complexity enables exquisite regulatory control. Activators and repressors do not bind Pol II directly — they interact with the GTF assembly or with Mediator (a ~30-subunit coactivator complex) to tune the transcription rate of individual genes. Archaea, interestingly, use a streamlined version of this system: archaeal RNA polymerase closely resembles eukaryotic Pol II, and archaeal TBP and TFB are direct homologs of their eukaryotic counterparts. See [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Archaea — The Third Domain of Life|Archaea — The Third Domain of Life]].

### No Proofreading — Error Rate and Its Consequences

RNA polymerase makes approximately **1 error per 10^4–10^5 nucleotides**. This is five orders of magnitude less accurate than DNA polymerase. Why is this tolerable?

Because RNA is transient. A given mRNA molecule is transcribed hundreds or thousands of times from the same gene; a defective transcript may fail to produce a functional protein, but the next transcript likely will. The cell can afford occasional transcriptional errors because the population of transcripts provides redundancy. The gene — the DNA template — remains accurate.

This logic does not work for genomic replication: the genome is unique and must be passed on with near-perfect fidelity. DNA polymerase's proofreading exists because the stakes are irreversible. RNA polymerase's lack of proofreading is not sloppiness — it is a rational trade-off between fidelity and speed.

---

## Reverse Transcriptase — The Exception

The Central Dogma (DNA → RNA → protein) has a well-known exception: **reverse transcriptase** (RT), which synthesizes DNA from an RNA template. This "reverse" flow was discovered by David Baltimore and Howard Temin in 1970 (Nobel Prize, 1975) in retroviruses.

Reverse transcriptase is a single enzyme with three activities:
1. **RNA-dependent DNA polymerase** — synthesizes a DNA strand using RNA as template
2. **RNase H** — degrades the RNA strand of the RNA:DNA hybrid once the DNA copy is made
3. **DNA-dependent DNA polymerase** — synthesizes the second DNA strand to produce double-stranded DNA, which then integrates into the host genome

RT has no proofreading and an extremely high error rate (~1 per 10^4 bases) — one reason HIV evolves drug resistance so rapidly. The viral quasi-species is a cloud of mutants generated by error-prone reverse transcription.

**Telomerase** is a cellular reverse transcriptase: it carries its own RNA template (TERC in humans) and uses it to extend chromosome ends, counteracting the end-replication problem described above.

---

## Error Rates Compared

| Enzyme | Error Rate | Proofreading? | Why |
|---|---|---|---|
| DNA Pol III (bacteria) + mismatch repair | ~1 per 10^9–10^10 | Yes (3'→5' exo) | Genomic fidelity is irreversible |
| DNA Pol δ/ε (eukaryotes) + mismatch repair | ~1 per 10^9–10^10 | Yes | Same |
| RNA Pol II (eukaryotes) | ~1 per 10^4–10^5 | No | Transcripts are redundant and transient |
| Reverse transcriptase (HIV) | ~1 per 10^4 | No | Enables rapid viral evolution; selective advantage |
| Telomerase | Low (RNA template is fixed) | No | Template is built into the enzyme |

---

## Why This Matters

**The Central Dogma depends on polymerase fidelity.** Information flows from DNA to RNA to protein with coherence because the copy machines are accurate. Prions represent the one known case where this system can be circumvented — protein conformation propagating independently of nucleic acid templates, bypassing the polymerase-based fidelity chain entirely. See [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Prion Information Paradox|The Prion Information Paradox]] for the philosophical implications.

**Cancer is partly a polymerase failure.** DNA pol mutation rate increases when mismatch repair proteins are defective (Lynch syndrome: loss of MLH1, MSH2, MSH6, PMS2). Tumors accumulate hundreds to thousands of mutations per cell division instead of the normal ~1. Similarly, some cancer-associated polymerases (POLE, POLD1 — the proofreading subunits) carry inactivating mutations in the exonuclease domain, producing hypermutated tumors. The fidelity machinery is itself tumor-suppressive.

**Antiviral drugs target viral polymerases.** Because viral polymerases differ from host polymerases in structure and mechanism, they are excellent drug targets. **Remdesivir** (COVID-19, Ebola) is a nucleoside analog that incorporates into the nascent RNA chain during SARS-CoV-2 RNA-dependent RNA polymerase (RdRp) synthesis, causing chain termination. Nucleoside RT inhibitors (NRTIs) like zidovudine (AZT) work the same way against HIV reverse transcriptase. **Sofosbuvir** targets hepatitis C virus RdRp.

**CRISPR interacts with the polymerase world.** CRISPR-Cas9 creates a double-strand break; the break is repaired by the cell's own DNA repair machinery — which itself depends on polymerases (Pol β for base excision repair; Pol δ/ε during homology-directed repair). In HDR-based CRISPR gene correction, the donor template is copied by polymerase into the broken locus. See [[02-Areas/Learning/Self-Study/Biology/2026-05-11 — CRISPR Gene Therapy Approved 2023|CRISPR Gene Therapy Approved 2023]].

---

## Conceptual Note — Fidelity as Biology's Bet

Polymerase fidelity is not free. Proofreading slows synthesis (the polymerase must pause, translocate to the exonuclease site, excise, return) and consumes energy. Mismatch repair adds another layer of cost. The cell invests heavily in accuracy because heritable errors compound: a mutation in a somatic cell may kill it or make it cancerous; a mutation in a germline cell propagates to every cell of every offspring.

But RNA polymerase's intentional inaccuracy is equally interesting as a design principle. By not proofreading, RNAP trades fidelity for speed and flexibility. The transcriptome can respond rapidly to changing conditions precisely because it is disposable. What looks like a deficiency — no proofreading — is actually a feature of a system that treats its outputs as drafts rather than permanent records.

Evolution built two different copy machines for two different jobs, with exactly the right tradeoffs for each. The molecular logic is elegant in a way that rewards careful attention.

---

## Connections

- [[02-Areas/Learning/Self-Study/Biology/2026-04-04 — Archaea — The Third Domain of Life|Archaea — The Third Domain of Life]] — archaeal RNA Pol is a direct structural homolog of eukaryotic Pol II; archaeal TBP/TFB are the evolutionary precursors of the eukaryotic GTF system; the deep conservation of RNAP across Archaea and Eukarya is some of the strongest evidence for their common ancestor
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-22 — The Prion Information Paradox|The Prion Information Paradox]] — prions bypass the polymerase-based information-verification system entirely; DNA pol is the biological "fact-checker" enforcing sequence fidelity; the prion is the case where the grammar breaks down
- [[02-Areas/Learning/Self-Study/Biology/2026-05-11 — CRISPR Gene Therapy Approved 2023|CRISPR Gene Therapy Approved 2023]] — CRISPR creates breaks that are repaired using cellular polymerases; HDR gene correction is, at the mechanistic level, a polymerase-mediated process
- [[02-Areas/Learning/Self-Study/Health-Systems/2026-04-01 — Evidentiality Biology vs Linguistics|Evidentiality Biology vs Linguistics]] — DNA pol as a biological evidentiality system: proofreading is the mechanism by which the cell enforces epistemic standards on inherited sequence information
- [[02-Areas/Learning/Self-Study/Biology/2026-04-15 — Molecular Computation|Molecular Computation]] — polymerases can be repurposed as molecular computing components; DNA polymerase in strand displacement amplification is used in diagnostic molecular logic circuits
- [[02-Areas/Learning/Self-Study/Biology/2026-05-11 — Bridge Recombinases 2024|Bridge Recombinases 2024]] — next-generation programmable DNA writers; operate alongside (and sometimes in competition with) native replication machinery
- [[02-Areas/Learning/Self-Study/Biology/2026-05-16 — Connections — DNA Polymerase Proofreading, Goodhart's Law, and the Imperial Examination|Connections — DNA Polymerase Proofreading, Goodhart's Law, and the Imperial Examination]] — synthesis note: all three are fidelity-enforcement systems that face the same structural impossibility — any proxy for the underlying goal is gameable; proofreading is the one case where evolution solved it; the other two are the cases where it wasn't solved
