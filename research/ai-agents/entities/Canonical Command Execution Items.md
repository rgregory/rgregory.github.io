---
id: canonical_command_execution_items
name: Canonical Command Execution Items
type: Concept
tags:
  - agents
  - tool-use
  - observability
review_status: confirmed
aliases:
  - TurnItem::CommandExecution
---

# Canonical Command Execution Items

## Summary

Canonical Command Execution Items are structured lifecycle records for shell command execution in OpenAI Codex, intended to provide one consistent command execution representation across app-server, compatibility events, replay, and completion bookkeeping.

## Relationships

- relationship:: implemented_in | [[OpenAI Codex]] | confirmed
- relationship:: related_to | [[Tool-Use Governance]] | confirmed

## Sources

- https://github.com/openai/codex/commit/cca16a10878202cb2f6e9666b6b4330329ea7e65
