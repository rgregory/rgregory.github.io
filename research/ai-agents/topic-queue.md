# Topic Queue

User-requested topics and follow-up research threads for the AI agents research loop.

## How to Add a Topic

Add a topic under `## Pending` using this format:

```markdown
### Topic title

- id: topic_slug
- priority: high | medium | low
- added: YYYY-MM-DD
- status: pending
- requested_by: Roger
- notes: what to focus on
- queries:
  - search query one
  - search query two
- done_when: concrete completion condition
```

## Lifecycle

```text
pending -> active -> done
              |
              -> blocked
              -> needs-review
```

## Pending

## Active

### Agent memory systems

- id: agent_memory_systems
- priority: high
- added: 2026-07-03
- status: active
- requested_by: Roger
- notes: Focus on durable memory, episodic memory, retrieval, personal knowledge graphs, and how agent systems persist useful context across runs. 2026-07-04 update: added ContextSniper as one high-signal primary source. 2026-07-06 update: added Governed Evolving Memory / MemState as a second high-signal memory source; continue looking for at least one more implementation-oriented source before marking done.
- queries:
  - "AI agent memory systems" durable episodic retrieval
  - "agent memory" knowledge graph SQLite Markdown
  - "long term memory" autonomous agents evaluation
- done_when: At least three high-signal primary sources are summarized, with implementation implications and open questions.

### Coding agent evaluation benchmarks

- id: coding_agent_evals
- priority: medium
- added: 2026-07-03
- status: active
- requested_by: Roger
- notes: Compare SWE-bench, terminal/tool-use benchmarks, background-agent reliability, and evals for long-running coding agents. 2026-07-04 update: added Distributed Attacks in Persistent-State AI Control and PACE as high-signal sources. 2026-07-06 update: added Infinite Agentic Loops and AgentFlow as static-analysis/governance sources; continue toward a comparison briefing before marking done.
- queries:
  - "coding agent benchmark" SWE-bench terminal-bench
  - "tool use evaluation" coding agents benchmark
  - "autonomous coding agent" evaluation reliability
- done_when: Produce a comparison of benchmark scope, limitations, and relevance to scheduled/background agents.

## Blocked

## Needs Review

## Done
