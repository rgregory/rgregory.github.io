---
id: concept_passive_capability_roots
name: Passive Capability Roots
type: Concept
tags:
  - agents
  - tool-use
  - reliability
  - state
review_status: confirmed
aliases:
  - passive selected-root snapshot
---

# Passive Capability Roots

## Summary

Pattern from OpenAI Codex where read-only skill/capability catalog requests inspect only currently ready executor environments and fail fast instead of starting, reconnecting, or waiting on executors.

## Relationships

- relationship:: related_to | [[OpenAI Codex]] | confirmed
- relationship:: related_to | [[Tool-Use Governance]] | pending

## Sources

- https://github.com/openai/codex/commit/13ba8058f294723c47dba5c47ca58cf090f04781
