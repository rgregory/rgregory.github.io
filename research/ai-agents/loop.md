# Research Loop: AI Agents

## Objective

Track meaningful developments in AI agents, with emphasis on:

- autonomous coding agents
- long-running task execution
- scheduled / cron-driven agents
- agent memory and durable state
- multi-agent coordination
- tool-use evaluation
- local-first agent systems
- Markdown/SQLite/Obsidian-style agent knowledge bases

## Operating Principle

This Markdown file is the source of truth for the research loop. Hermes should execute this file on schedule, maintain the files it names, and avoid changing the cron job unless the schedule/delivery itself changes.

Canonical storage is Markdown. SQLite is a derived index rebuilt from Markdown.

## Directory Layout

```text
/Users/rgregory/.hermes/akira/research/ai-agents/
  loop.md                         # this canonical research-loop spec
  sources.md                      # curated sources and search queries
  topic-queue.md                  # user-requested topics and follow-up research threads
  state.json                      # last run state, seen URLs, content hashes
  findings.md                     # chronological findings log
  open-questions.md               # questions to revisit
  briefings/                      # dated summaries
  entities/                       # Obsidian-style entity notes
  scripts/build_research_index.py # rebuild graph.sqlite from Markdown
  graph.sqlite                    # derived query/reporting/search index
```

## Run Instructions

On each scheduled run:

1. Read `loop.md`, `sources.md`, `topic-queue.md`, `state.json`, `findings.md`, and `open-questions.md`.
2. Discover new developments using the stable sources and queries in `sources.md`.
3. Also process user-requested topics from `topic-queue.md`:
   - prioritize `## Active` first, then high-priority `## Pending` topics
   - include each topic's `queries` in discovery
   - keep topics in `pending` if there is not enough signal yet
   - move a topic to `active` when current-run work is underway
   - move a topic to `done` only when its `done_when` condition is satisfied
   - move a topic to `blocked` or `needs-review` when progress requires user input or a source/API failed repeatedly
4. Prefer primary sources over summaries.
5. Ignore duplicate or already-seen URLs from `state.json` and `findings.md`.
6. Rank candidate findings by:
   - topic priority from `topic-queue.md`
   - novelty
   - credibility
   - relevance
   - practical usefulness
   - whether the source contains implementation details or primary evidence
7. Append only meaningful new findings to `findings.md`.
8. Write a dated briefing to `briefings/YYYY-MM-DD.md`.
9. Update `state.json` with:
   - `last_run_utc`
   - `seen_urls`
   - `last_briefing`
   - `active_topics`
   - `completed_topics`
   - `blocked_topics`
   - `notes`
10. Update `topic-queue.md` statuses when work starts, completes, blocks, or needs review. Preserve completed topic history under `## Done`.
11. Update or create entity notes under `entities/` when a finding introduces an important project, organization, person, paper, benchmark, or concept.
12. Rebuild `graph.sqlite` by running:

```bash
python3 /Users/rgregory/.hermes/akira/research/ai-agents/scripts/build_research_index.py
```

13. If this directory is a git repository and meaningful Markdown/state files changed, commit the changes with a concise message such as:

```bash
git add loop.md sources.md topic-queue.md state.json findings.md open-questions.md briefings entities scripts .gitignore weekly-synthesis.md
git commit -m "research: update AI agents research loop"
```

Do not commit `graph.sqlite`; it is a derived artifact and is ignored by `.gitignore`.

14. Return a concise briefing with:
   - number of new findings
   - top findings
   - what changed since last run
   - open questions
   - paths updated

## Finding Format

Append findings to `findings.md` using this exact format:

```markdown
## YYYY-MM-DD — Title

Source: URL  
Type: paper | repo | blog | docs | release | discussion | video | dataset | benchmark  
Importance: high | medium | low  
Confidence: high | medium | low  
Entities: [[Entity One]], [[Entity Two]]  
Tags: #agents #memory #evals

### Summary

...

### Why it matters

...

### Evidence

- ...

### Follow-up questions

- ...
```

## Entity Note Format

Use one Markdown file per entity under `entities/`:

```markdown
---
id: entity_slug
name: Entity Name
type: Project | Organization | Person | Paper | Benchmark | Concept | Product
tags:
  - agents
review_status: confirmed | pending
aliases: []
---

# Entity Name

## Summary

...

## Relationships

- relationship:: created_by | [[Organization Name]] | confirmed
- relationship:: related_to | [[Other Entity]] | pending

## Sources

- URL
```

## Quality Bar

Do not include low-signal listicles, SEO pages, or repeated commentary unless they point to a primary source. If there is nothing important, write a short briefing saying no high-signal updates were found and still update `state.json`.

## Human Review

If uncertain, add review candidates to `open-questions.md` instead of promoting them to confirmed entity relationships.
