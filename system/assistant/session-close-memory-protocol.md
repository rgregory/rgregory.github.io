---
type: system-note
id: system_session_close_memory_protocol
aliases:
  - Session Close Memory Protocol
  - End-of-Session Durable Memory
area: assistant
status: active
review_status: confirmed
tags:
  - hermes
  - memory
  - obsidian
  - protocol
relationships:
  - type: implements
    target: Long-Term Memory
    status: confirmed
  - type: indexed_by
    target: Assistant Memory Index
    status: confirmed
  - type: related_to
    target: Vault Graph Index
    status: confirmed
---

# Session Close Memory Protocol

At the end of every meaningful Hermes session, make memory durable in the Akira vault.

## Rule

Before wrapping a session, preserve durable outcomes in Markdown, not just chat history or compact Hermes memory.

## What to Save

Save only durable, reusable information:

- decisions and rationale
- new research topics or conclusions
- new entities and relationships
- workflow changes
- durable project/vault status
- links to created plans, scripts, cron jobs, or notes
- open questions that should survive the session

Do **not** store temporary progress noise, transient command output, one-off errors already fixed, secrets, credentials, or data that will be stale within a week.

## Procedure

1. Identify what from the session is durable.
2. Write or update the appropriate Markdown note in the vault.
3. Add YAML frontmatter relationships when the item should enter the graph.
4. Rebuild the derived SQLite graph:

```bash
python3 scripts/build_graph_index.py --vault /Users/rgregory/.hermes/akira
```

5. Validate Markdown↔SQLite sync:

```bash
python3 /Users/rgregory/.hermes/scripts/akira_validate_graph_sync.py
```

6. Commit Markdown/source changes in the local Git repo.
7. Keep Hermes built-in memory compact: pointers, preferences, and stable conventions only.

## Related

- [[long-term-memory]]
- [[assistant-memory-index]]
- [[vault-graph-index]]
- [[import-review]]
