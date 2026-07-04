---
type: note
date: "2026-07-02"
tags: [note, computer-science, operating-systems, plan-9, microkernels, formal-verification, distributed-systems]
status: filed
created: "2026-07-02"
filed-date: "2026-07-02"
location: "02-Areas/Learning/Self-Study/Technical/"
---

# Plan 9, Alternative OS Philosophies, and Formal Verification

## Plan 9's Core Philosophy

Plan 9 from Bell Labs (Pike, Thompson, Ritchie et al.) took Unix's half-finished ideas and pushed them all the way through.

**"Everything is a file" — actually enforced.** Unix said this but broke it constantly (sockets weren't files, ioctls were special-cased). Plan 9 made every resource — processes, network connections, graphics, even remote machines — a plain file accessed with `open`/`read`/`write`/`close`. No separate APIs per subsystem.

**One protocol for everything: 9P.** All file access, local or remote, goes over a single simple protocol. There's no architectural distinction between talking to a local disk and talking to a remote server — both just look like mounted file trees. This made distributed computing fall naturally out of the filesystem model instead of being bolted on via RPC or NFS.

**Private per-process namespaces.** Instead of one global filesystem tree, each process (or group) builds its own view of the world by mounting/binding different trees. This yields sandboxing, resource virtualization, and location transparency almost for free — and is a direct ancestor of Linux namespaces / container isolation.

**Machines as roles, not monoliths.** The design assumed CPU servers, file servers, and thin terminals, composed over the network via namespaces rather than one heavyweight workstation per user.

**UTF-8.** Invented by Rob Pike and Ken Thompson specifically for Plan 9, so Unicode text handling would be a first-class design assumption rather than a retrofit.

**The unifying idea:** Unix treated "everything is a file" as a UI convenience. Plan 9 treated it as a systems architecture — one abstraction, one protocol, composed via namespaces — for building distributed, resource-agnostic computing. Never got mass adoption, but union mounts, `/proc`-style interfaces, container namespaces, and UTF-8 all trace back to it.

---

## Other OSes Worth Knowing (Same "What If We Didn't Accept the Default" Spirit)

| OS | Core idea |
|---|---|
| **TempleOS** (Terry Davis) | Single-address-space, 8086-mode OS with its own language (HolyC) blurring compiler/shell — kernel functions callable interactively like a REPL. No memory protection, because the whole system was one trusted address space. |
| **Smalltalk / Xerox Alto OS (Squeak)** | The OS is just live objects sending messages, inspectable and editable at runtime. No real line between "OS," "IDE," and "running program." Ancestor of live-coding IDE features. |
| **Urbit** | Personal server modeled as a single deterministic, event-sourced VM (Nock/Hoon) with a global identity/addressing system instead of processes-and-files. Extreme functional-purity approach to "what is a computer." |
| **seL4** | Formally verified microkernel — mathematically proven correct down to the binary against its spec. |
| **Genera (Symbolics Lisp Machines)** | Entire stack, kernel included, written in Lisp; kernel functions redefinable live from a REPL. |
| **Barrelfish (multikernel OS)** | Treats a multicore machine like a distributed system internally — each core runs its own kernel instance, cores communicate via message passing instead of shared memory + locks. |
| **Redox OS** | Modern Rust rewrite of the Plan 9 idea: "everything is a URL" instead of "everything is a file," using Rust ownership for OS-level memory safety. |

---

## Formally Verified Operating Systems

Full-system verification is still too expensive for anything Linux/Windows-scale, so the field has converged on: **verify a small trusted core (microkernel/hypervisor), treat everything else as untrusted userspace.**

- **seL4** — the landmark: proven correct end-to-end against its formal spec.
- **CertiKOS** (Yale FLINT group) — verified concurrent OS kernel; proves correctness *across* abstraction layers (hardware → multicore-safe kernel). Originally framed as a certified hypervisor for secure cloud computing (isolating guest VMs from each other *and* from the cloud provider's own management software).
- **CompCert** — not an OS, but the load-bearing piece underneath: a formally verified C compiler proving semantic preservation from source to assembly.
- **Ironclad / IronFleet** (Microsoft Research) — verified low-level services and, in IronFleet's case, verified *distributed* protocols (consensus, replication) in Dafny.
- **Verve** (Microsoft Research) — OS built from verified low-level typed assembly + C#, full type-safety without a separate hypervisor.
- **HACMS (DARPA)** — used seL4 + verified compilers/drivers to build a drone that survived a red-team hacking exercise.
- **Komodo** and similar Iris-based work — verify small TEE/enclave monitors (SGX/TrustZone equivalents).

### CertiKOS Commercial Uses

CertiKOS itself never shipped as a deployed commercial OS — it remains a Yale research project (mCertiKOS, mC2 concurrent kernel), demonstrating that formal verification scales to a real concurrent kernel with shared-memory concurrency (~6,500 lines of C/x86 assembly, proven in Coq).

Two commercial threads grew out of the same lineage:

1. **CertiK** — a Web3/blockchain security company founded by Yale and Columbia professors connected to the CertiKOS research. It commercializes formal-verification techniques for smart contract auditing (DeepSEA compiler, CertiK Virtual Machine) rather than deploying CertiKOS as an OS.
2. **CompCert** — the verified compiler CertiKOS depends on has its own commercial license, sold with professional support by **AbsInt**; the research/non-commercial version is free.

So: CertiKOS-the-kernel is research-only, but its verification methodology seeded a real commercial security company (CertiK) and rides on a compiler (CompCert) that's itself commercially licensed.

---

## Connections

- [[MOC/Technical]] — systems and infrastructure
- [[03-Resources/Technical/Containers/BSD-Containerization/_index|BSD Containerization]] — Plan 9's per-process namespaces are a direct conceptual ancestor of FreeBSD Jails / Linux namespaces / container isolation
- [[03-Resources/Technical/Containers/_index|Containers]] — namespace-based isolation as a throughline from Plan 9 to modern container runtimes
