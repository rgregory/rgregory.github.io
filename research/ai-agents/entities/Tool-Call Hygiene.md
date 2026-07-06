---
id: concept_tool_call_hygiene
name: Tool-Call Hygiene
type: Concept
tags:
  - agents
  - tool-use
  - reliability
review_status: confirmed
aliases:
  - tool call transcript hygiene
---

# Tool-Call Hygiene

## Summary

Practices and runtime repairs that keep tool-call transcripts valid for provider APIs, including deduplicating tool-call IDs and removing malformed historical messages.

## Relationships

- relationship:: related_to | [[Hermes Agent]] | confirmed
- relationship:: related_to | [[Agent Evaluation]] | pending

## Sources

- https://github.com/NousResearch/hermes-agent/commit/dba585c1794e0c5dc4409c6c60996046e2005063
