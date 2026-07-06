---
id: concept_agent_dependency_graph
name: Agent Dependency Graph
type: Concept
tags:
  - agents
  - static-analysis
  - governance
review_status: confirmed
aliases:
  - ADG
---

# Agent Dependency Graph

## Summary

An Agent Dependency Graph is a framework-agnostic representation of agent programs with typed nodes for agents, prompts, models, tools/capabilities, memory states, and control policies, plus typed dependency, control-flow, and data-flow edges.

## Relationships

- relationship:: generated_by | [[AgentFlow]] | confirmed
- relationship:: supports | [[Agent Bill of Materials]] | confirmed

## Sources

- http://arxiv.org/abs/2607.01640v1
