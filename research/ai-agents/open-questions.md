# Open Questions

Use this file for uncertain claims, review candidates, and follow-up research threads.

## Review Queue

- 2026-07-03: Investigate whether Claude Code Manual-by-default permissions require a separate unattended-agent policy profile for cron/scheduled use.
- 2026-07-03: Check whether CrewAI's flow stream-frame protocol is documented as a stable interface or only an internal alpha implementation detail.
- 2026-07-04: Determine what policy language best separates safe unattended multi-agent delegation from interactive, user-approved delegation in OpenAI Codex-style configurable delegation policies.
- 2026-07-04: Check which coding-agent benchmarks can be adapted to evaluate cross-run or multi-PR attacks like Iterative VibeCoding.
- 2026-07-04: Evaluate whether PACE-style proxy benchmark sets detect regressions in long-running/background-agent reliability, not just static agentic capability.
- 2026-07-04: Check whether ContextSniper is available as code or only described in the arXiv paper, and whether its evidence-selection approach can be reused outside program repair.
- 2026-07-04: Verify whether CrewAI repository-backed agent references work in fully local/offline runs or depend on CrewAI Plus APIs.
- 2026-07-04: Decide whether provider-specific strictness failures, such as duplicate tool-call ID rejection, should be tracked as a separate tool-use reliability category.
- 2026-07-06: Check whether IAL-style static checks can be adapted into a scheduled-agent preflight lint for loop limits, tool budgets, and external side-effect guards.
- 2026-07-06: Identify which watched agent frameworks can export Agent Dependency Graph-like metadata directly rather than requiring source reconstruction.
- 2026-07-06: Design a Markdown-first representation for memory revision and forgetting that preserves auditability while supporting Governed Evolving Memory-style state evolution.
- 2026-07-06: Determine whether scheduled LangGraph agents should verify first-checkpoint persistence after state initialization.
- 2026-07-06: Explore whether execution-scoped attribution can generalize from Codex network access to file writes, process trees, browser actions, and MCP/tool calls.
- 2026-07-07: Decide whether advisory workflow-size settings are enough for unattended cron use, or whether scheduled agents should require enforced caps on spawned agents, tool calls, and cost.
- 2026-07-07: Explore whether canonical command items should become the common join point for network attribution, file-write attribution, sandbox policy decisions, and replayable agent transcripts.
- 2026-07-07: Check whether scheduled-agent harnesses should include explicit concurrency tests for shared memory, credential, and tool-state stores before enabling multiple background workers.
- 2026-07-07: Design how Markdown-first agent memories should distinguish lossy compaction summaries from confirmed durable facts and auditable source records.
- 2026-07-07: Decide whether all gateway connectors should enforce self-contained plain-text fallbacks for approval prompts before enabling high-impact unattended actions.
- 2026-07-08: Decide which Claude Code background-agent failure classes should become regression checks for scheduled coding-agent workflows.
- 2026-07-08: Explore whether Hermes session-owned event drains should be generalized for all async tool results, notifications, and approval replies.
- 2026-07-08: Define policy/audit boundaries for Codex-style remote plugins enabled by default and MCP tool search as the default discovery path.
- 2026-07-08: Evaluate whether extension-owned turn-item schemas belong in an agent bill of materials for durable transcript validation after plugin upgrades.
- 2026-07-08: Prototype whether scheduled research loops can store AgentTether-like Transition Units and repair guidance in Markdown/SQLite.
- 2026-07-08: Adapt SWE-Together’s corrective-feedback-turn metric for asynchronous background agents where human feedback is delayed.
- 2026-07-08: Test whether CXI-style action manifests can be represented as YAML frontmatter or SQLite rows in Markdown-first agent audit logs.
