# Weekly Synthesis: AI Agents Research Loop

## Objective

Once per week, synthesize the daily AI agents research findings into a higher-level trend report. The weekly synthesis should not duplicate the daily findings log; it should identify patterns, implications, unresolved questions, and recommended follow-up research.

## Inputs

Read these files before writing the weekly synthesis:

- `findings.md`
- `open-questions.md`
- `topic-queue.md`
- `state.json`
- recent files under `briefings/`
- entity notes under `entities/`
- `graph.sqlite` when useful for counts or relationship queries

## Output Location

Write the weekly synthesis to:

```text
briefings/weekly/YYYY-WW.md
```

Use ISO week numbering, for example:

```text
briefings/weekly/2026-W27.md
```

## Required Sections

Each weekly synthesis should include:

1. **Executive summary** — 3-6 bullets.
2. **Top developments** — the most important findings from the week.
3. **Emerging themes** — clusters across findings, entities, and open questions.
4. **State of the field** — what appears to be changing in AI agents.
5. **Implementation implications** — concrete lessons for building scheduled, long-running, or multi-agent systems.
6. **Open questions** — unresolved issues worth tracking.
7. **Recommended follow-ups** — specific next research actions.
8. **Index snapshot** — counts from `graph.sqlite` for entities, relationships, wikilinks, and findings.

## Rules

- Prefer synthesis over repetition.
- Preserve source links when discussing specific claims.
- Mark speculative conclusions as speculative.
- Do not promote inferred relationships to confirmed without strong evidence.
- If the week has too few findings, write a concise low-activity report instead of padding.
- After writing the weekly report, run `python3 scripts/build_research_index.py`.
- If this directory is a git repository, commit meaningful Markdown/state changes with a concise message.

## Suggested Commit Message

```text
research: add weekly AI agents synthesis for YYYY-WW
```
