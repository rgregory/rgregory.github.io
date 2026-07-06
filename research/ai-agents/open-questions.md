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
