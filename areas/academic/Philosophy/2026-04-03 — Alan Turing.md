---
type: note
date: "2026-04-03"
tags: [philosophy, computation, ai, philosophy-of-mind, mathematics]
status: filed
filed-date: "2026-04-03"
created: "2026-04-03"
---

# Alan Turing

Alan Turing (1912–1954) is the figure who essentially defined what computation means — before a single programmable computer had been built. His contributions span mathematics, logic, computer science, and philosophy of mind, and they remain foundational to all four.

---

## The Turing Machine

In his 1936 paper *On Computable Numbers, with an Application to the Entscheidungsproblem*, Turing introduced what is now called the **Turing Machine**: an abstract mathematical device consisting of an infinite tape divided into cells, a read/write head that moves left or right, and a finite set of states and transition rules.

The machine reads a symbol on the tape, consults its current state, writes a new symbol (or the same one), moves the head, and transitions to a new state. That is all. Despite this simplicity, Turing showed that anything computable — in any formal sense — can be computed by such a machine. A **Universal Turing Machine** can simulate any other Turing Machine given a description of it on the tape. This is the abstract precursor of the general-purpose computer.

### Why It Matters

The Turing Machine makes **computability** precise. Before Turing, "this problem can be solved mechanically" was an informal idea. Turing gave it a rigorous definition: a function is computable if and only if a Turing Machine can compute it. This definition has proven robust — every other reasonable formalization of computation (lambda calculus, recursive functions, Post systems) turns out to compute exactly the same class of functions.

### The Halting Problem

Turing also proved that certain things are **not** computable. The most famous: there is no Turing Machine that can take an arbitrary program and input and decide, in finite time, whether that program will halt or run forever. This is the **Halting Problem**, and its undecidability is proven by a diagonal argument structurally identical to Cantor's proof that real numbers are uncountable and to Gödel's construction of unprovable sentences (see [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]]).

The undecidability of the Halting Problem is not a limitation of current technology — it is a permanent feature of computation itself. No improvement in hardware changes it.

---

## The Church-Turing Thesis

The **Church-Turing Thesis** states that any function that is effectively computable by a human following an algorithm can be computed by a Turing Machine. It is called a *thesis* rather than a *theorem* deliberately: it cannot be formally proved, because "effectively computable" (or "mechanically calculable") is an informal, intuitive notion. You cannot prove a formal system captures an informal concept — you can only argue it does.

Alonzo Church arrived at an equivalent result independently using lambda calculus; the thesis is named for both.

### What It Does NOT Say

The Church-Turing Thesis is frequently misread. It does not claim:
- That the human brain is a Turing Machine
- That every physical process is computational
- That intelligence reduces to computation
- That consciousness is a form of computation

It is a claim about the extension of a specific mathematical concept (computability), not a metaphysical thesis about minds or nature. Confusing the mathematical claim with the metaphysical one generates a great deal of philosophical noise.

---

## The Turing Test

In his 1950 paper *Computing Machinery and Intelligence*, Turing opens by asking: "Can machines think?" — and then immediately sets it aside as poorly formed, because "machine" and "think" are both too ambiguous to support a useful answer.

### The Imitation Game

Instead, he proposes what he calls the **Imitation Game**. The original formulation involves three players: a man (A), a woman (B), and an interrogator (C). The interrogator, isolated in another room, communicates by typewriter and tries to determine which is the man and which the woman. A tries to mislead; B tries to help. Turing then asks: what happens if a machine takes the role of A? If the machine can play the imitation game as well as a man can, then whatever question we were trying to answer with "can machines think?" has, at minimum, been answered in a practically significant way.

### What Turing Actually Claimed

The popular version of the Turing Test — "if a machine can fool a human into thinking it's human, then it's intelligent" — is a distortion. Turing's actual claim is considerably more careful:

1. The test sidesteps definitional arguments by replacing the philosophically contested concept of "thinking" with an observable behavioral criterion.
2. Turing explicitly acknowledges the test is not definitionally equivalent to intelligence — it is a **useful operational substitute** for a question that may otherwise be unanswerable.
3. He devotes much of the paper to anticipating and responding to objections, rather than asserting the test as a proof.

Turing was making a methodological point: if we cannot agree on what thinking *is*, we can at least agree on what thinking *looks like*, and test for that.

---

## Turing's Response to the Gödelian/Lucas-Type Objection

The objection Turing anticipated — and that J.R. Lucas (1961) and Roger Penrose later formalized — goes roughly: Gödel's theorems show that for any consistent formal system F, there is a sentence G(F) that F cannot prove but that we can see to be true. Since a computer is a formal system, any computer has such a blind spot. But humans can see past it. Therefore, human minds are not computers.

### The System/Observer Conflation

Turing's response, sketched in the 1950 paper, cuts to the root of the argument. The objection **conflates being inside a system with being an observer of that system**. A Turing Machine (or any formal system) cannot prove its own Gödelian sentence from within its own rules — that is exactly what Gödel shows. But this does not mean that no external observer can prove it.

When a human "sees" that G(F) is true, they are doing so from *outside* F — they are operating in a richer meta-system. But then ask: can that meta-system prove *its own* Gödelian sentence? No. Can a further human observer see that the meta-system's Gödelian sentence is true? Yes — from yet another level up. The process iterates.

The Lucas-Penrose argument assumes that human mathematical insight is a single consistent formal system from which we can both operate and observe our own Gödelian blind spots simultaneously. But this assumption does precisely what Gödel's theorem says cannot be done: it treats the observer and the system as identical. The moment you say "I can see that G(F) is true," you are not operating *as* F — you are reasoning from something stronger.

This does not vindicate computationalism — it deflates the Gödelian objection. Whether human minds are computational remains an open question; this particular argument does not settle it. For a fuller treatment of the Lucas-Penrose argument and its weaknesses, see [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — The Lucas-Penrose Argument|The Lucas-Penrose Argument]].

---

## Turing's Broader Significance

Turing defined computation before computers existed. The architecture of every modern machine — the stored-program computer, the separation of data and instructions, the universality of the general-purpose processor — is implicit in the Universal Turing Machine.

He also gave the first rigorous framework for thinking about what machines *cannot* do. The limits of computation (undecidability, non-computable functions) are permanent mathematical results, not engineering problems. This matters for philosophy of mind, for AI, and for the foundations of mathematics.

Turing's 1936 and 1950 papers together bookend what computation is and what it might mean for minds. The first shows computation's power and limits. The second asks whether those limits matter for intelligence — and carefully refuses to answer definitively.

### Personal Context

Turing's work was done under conditions of extreme institutional hostility. He was a central figure in the British codebreaking effort at Bletchley Park during WWII — his work on the Enigma cipher and the Bombe machine was decisive for the Allied war effort. After the war, he was prosecuted by the British government for homosexuality, subjected to chemical castration, and died in 1954 under circumstances officially ruled a suicide. He was 41. He was granted a royal pardon posthumously in 2013.

The personal story does not change the mathematics, but it is relevant context: much of the work on machine intelligence was produced by a man whom his own government refused to recognize as fully human.

---

## Connections

- [[03-Resources/Sources/2026-05-16 — Van Heijenoort — From Frege to Gödel|Van Heijenoort — From Frege to Gödel (1967)]] — the 1879–1931 foundational crisis whose resolution Turing inherits
- [[03-Resources/Sources/2026-05-16 — Smith — An Introduction to Gödel's Theorems|Smith — An Introduction to Gödel's Theorems (2020)]] — Turing/Gödel diagonalization parallel; Church-Turing-Gödel triumvirate
- [[03-Resources/Sources/2026-05-16 — Wang — A Logical Journey From Gödel to Philosophy|Wang — A Logical Journey From Gödel to Philosophy (1996)]] — Gödel's views on Turing's result; paired architects of computability limits
- [[02-Areas/Learning/Self-Study/Philosophy/2026-03-21 — Gödel's Incompleteness Theorems|Gödel's Incompleteness Theorems]] — Turing's Halting Problem proof is structurally parallel to Gödel's diagonal construction; the two results are deeply related and were proved independently within a year of each other
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — The Lucas-Penrose Argument|The Lucas-Penrose Argument]] — The primary philosophical challenge to computationalism built on Gödel; Turing's 1950 paper anticipates the core objection
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — Searle Chinese Room|Searle's Chinese Room]] — Searle's Chinese Room is the most influential attack on the Turing Test as a criterion for understanding — Searle argues that passing the test requires no understanding whatsoever
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-02 — Ant Colony Intelligence — Intentional or Functional|Ant Colony Intelligence — Intentional or Functional?]] — The question of whether distributed systems have genuine intentionality is continuous with the question the Turing Test displaces; both avoid defining intelligence and focus on functional criteria
- [[02-Areas/Learning/Self-Study/Social-Science/2026-03-21 — Chomsky on Systems of Power|Chomsky on Systems of Power]] — Chomsky's formal language hierarchy (regular, context-free, context-sensitive, recursively enumerable languages) is a direct extension of the Turing framework; context-sensitive and recursively enumerable languages correspond precisely to classes of Turing Machine computation; Chomsky and Turing are in continuous dialogue across linguistics and computation theory
