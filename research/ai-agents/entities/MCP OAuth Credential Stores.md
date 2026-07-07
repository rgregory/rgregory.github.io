---
id: mcp_oauth_credential_stores
name: MCP OAuth Credential Stores
type: Concept
tags:
  - agents
  - mcp
  - security
  - state
review_status: confirmed
aliases: []
---

# MCP OAuth Credential Stores

## Summary

MCP OAuth Credential Stores are durable File, Secrets, or Direct keyring stores used by OpenAI Codex to hold MCP server OAuth credentials. Shared aggregate File/Secrets maps require serialization to avoid lost updates under concurrent sessions or background agents.

## Relationships

- relationship:: implemented_in | [[OpenAI Codex]] | confirmed
- relationship:: related_to | [[Tool-Use Governance]] | confirmed

## Sources

- https://github.com/openai/codex/commit/6cf42cf16516ab3a125d853561ae3b8c77d6c13e
