---
type: note
title: Personal AI Agent Architecture Design
tags:
  - ai
  - agents
  - personal-automation
  - productivity
  - research
  - architecture
status: active
created: 2026-04-19
---

# Personal AI Agent Architecture Design

Concrete agent designs for your two primary use cases: personal productivity automation and research assistance. These agents run on Oracle Cloud's always-free ARM instance (24GB RAM) and coordinate via shared knowledge base.

---

## Overview: Two-Agent System

**Productivity Agent** — handles daily task automation (email, calendar, notes)  
**Research Agent** — learns your research interests and generates synthesis

Both agents:
- Share a single SQLite knowledge base (your vault + task history)
- Read/write to your vault via Git sync
- Execute safely with action whitelisting
- Improve their own skills iteratively (Voyager pattern)
- Inherit learnings across agent generations (ADAS pattern)

---

## Agent 1: Productivity Agent

### Purpose

Automate routine personal knowledge work: email triage, task scheduling, note synthesis, daily summaries.

### Core Responsibilities

1. **Email Triage** (daily, 9 AM)
   - Query inbox for new emails
   - Classify by domain (work, personal, urgent, FYI)
   - Summarize threads
   - Log summary to vault note
   - Goal: "What do I need to know from email today?"

2. **Task Extraction** (triggered by note creation)
   - Parse vault for incomplete tasks
   - Extract from email (action items from meetings)
   - Query calendar for upcoming deadlines
   - Consolidate into daily task list
   - Goal: "What should I do today?"

3. **Note Synthesis** (weekly, Friday 5 PM)
   - Summarize week's activity: vault edits, tasks completed, research progress
   - Extract key decisions and learnings
   - Identify patterns (what consumed most time? what was most valuable?)
   - Write synthesis note to vault for your review
   - Goal: "What happened this week and what should I do differently?"

4. **Daily Digest** (daily, 8 AM)
   - Compile: Today's schedule, inbox summary, task list, weather, quotes/inspiration
   - Write to Daily Note in vault
   - Optional: Send as email or Slack message
   - Goal: "Start the day informed"

### Skills Library

Executable Python code stored in Git repo, versioned by iteration:

```
skills/
├── core/
│   ├── read_vault.py          # Query vault notes, parse YAML frontmatter
│   ├── write_note.py          # Create/update vault notes atomically
│   ├── search_vault.py        # Full-text + vector search over notes
│   └── list_tasks.py          # Extract tasks from task log
├── productivity/
│   ├── email_summarizer.py    # (v1, v2, v3...) summarize threads
│   ├── task_extractor.py      # (v1, v2...) parse action items
│   ├── calendar_reader.py     # List today's events, extract deadlines
│   ├── weekly_synthesis.py    # Generate week summary
│   └── daily_digest.py        # Compile morning briefing
└── meta/
    ├── evaluate_skill.py      # Rate skill performance (speed, quality)
    └── improve_skill.py       # Agent refines its own code via Claude
```

### Feedback Loop

Each execution produces structured feedback:

```json
{
  "task_id": "productivity:daily_digest:2026-04-19",
  "skill": "daily_digest.py",
  "version": 2,
  "execution_time_sec": 12,
  "status": "success",
  "output_quality": 8,  // 1-10 user rating or auto-score
  "user_feedback": "Clear and actionable, but too long",
  "issues": ["exceeds 500-word limit"],
  "suggested_improvement": "Summarize task list; cut weather"
}
```

Agent uses feedback to improve: sends (old_code, feedback) to Claude → revised code → test on same input → compare.

### Inbox & Interactions

**Triggers**:
- Scheduled (9 AM email triage, 8 AM digest, Friday synthesis)
- User request: "What should I work on today?"
- External: Email arrives → optionally trigger triage immediately
- Vault change: New note created → extract tasks

**Outputs**:
- Vault notes (daily digest, weekly synthesis, task list)
- Optional: email draft, Slack message, calendar updates
- Logs: skill execution records stored in vault for analysis

---

## Input Processing Capabilities

Both agents can ingest and process external content:

### Webpage Processing
- Fetch & parse HTML content from URLs
- Convert to markdown with metadata extraction
- Example: Agent reads published article, extracts key points, synthesizes into research note

### Image OCR
- Extract text from images (PNG, JPG, GIF)
- Example: Agent processes screenshot, extracts code/text, files to appropriate vault location

### PDF Text Extraction
- Full text extraction from PDF documents
- Metadata capture (title, author, publish date)
- Example: Agent reads research paper PDF, extracts abstract and key findings, cites in synthesis note

### Unified Input Handler
- Detects content type (webpage vs. PDF vs. image)
- Routes to appropriate processor
- Returns unified text output
- Cost tracking: webpage fetch (~tokens), PDF extract (~0 local), OCR (~0 local, fast)

### Integration with Feedback Loop
1. User provides URL or file: "Process this article about emergence"
2. Agent fetches/extracts text via input processor
3. Agent routes content to relevant skill (synthesis, extraction, analysis)
4. Output saved to vault with citation
5. Feedback cycle: Agent learns which processing methods work well

---

## Agent 2: Research Agent

### Purpose

Learn your research interests from vault patterns. Generate insights, identify gaps, refine investigation strategy.

### Core Responsibilities

1. **Vault Pattern Analysis** (weekly)
   - Read all your research notes (Philosophy, AI, Emergence, etc.)
   - Build semantic map: which topics interconnect?
   - Identify which notes are "hubs" (frequently referenced)
   - Detect weak connections (notes that seem related but aren't linked)
   - Goal: "What does the vault reveal about your thinking?"

2. **Gap Detection** (monthly)
   - Analyze "Learning Queue" — topics you want to explore
   - Cross-reference against existing vault content
   - Identify: "You're interested in X, but haven't explored Y (related concept)"
   - Propose new research directions
   - Goal: "What should you study next?"

3. **Synthesis Generation** (on demand)
   - User: "Connect Emergence and AI Agents" → agent reads both clusters
   - Finds common concepts (adaptation, feedback loops, self-organization)
   - Generates synthesis note with cross-links
   - Reads back to you: "Here's how these domains relate"
   - Goal: "Generate unexpected connections"

4. **Research Assistant** (ongoing)
   - User: "I'm reading about X" → agent queries related vault notes
   - Prepares context: "You've studied X before, here's what you found"
   - Suggests follow-up questions based on past work
   - Goal: "Deepen the learning process"

### Skills Library

```
skills/
├── core/
│   ├── read_vault.py
│   ├── vector_search.py       # Semantic search over note embeddings
│   ├── graph_analysis.py      # Topic network analysis
│   └── moc_reader.py          # Parse MOC structure
├── research/
│   ├── topic_mapper.py        # (v1, v2...) identify topic clusters
│   ├── gap_detector.py        # Find unexplored areas
│   ├── synthesis_writer.py    # Generate cross-domain synthesis
│   ├── context_retriever.py   # Find relevant past notes
│   └── question_generator.py  # Suggest research questions
└── meta/
    ├── strategy_analyzer.py   # "How is your research evolving?"
    └── improve_synthesis.py   # Refine synthesis quality based on feedback
```

### Feedback Loop

User rates synthesis notes:
```json
{
  "task_id": "research:synthesis:emergence-ai:2026-04-19",
  "skill": "synthesis_writer.py",
  "version": 3,
  "quality_rating": 7,  // 1-10 from you
  "feedback": "Good connections, but missed Searle. Add philosophical grounding.",
  "suggested_improvement": "Include philosophy notes in cross-reference"
}
```

Agent iterates: "I should check Philosophy folder for relevant thinkers when doing AI synthesis."

---

## Coordination: How Agents Work Together

### Shared Knowledge Base

Both agents read/write to:
- **Vault notes** (your research, decisions, context)
- **Task log** (SQLite: task ID, status, owner-agent, completed-date)
- **Skill metrics** (per-agent: which skills work well, which need iteration)
- **Daily notes** (one note per day: inbox summary, digest, tasks, synthesis)

### Message Passing (Agent → Agent)

Simple event log in SQLite:

```sql
CREATE TABLE agent_log (
  timestamp TEXT,
  agent TEXT,
  event TEXT,
  payload JSON,
  next_agent TEXT  -- which agent should pick this up?
);
```

Example:
1. Productivity Agent finishes email triage, logs: `event="inbox_processed", next_agent="task_extractor"`
2. Task Extractor wakes up, reads the log, pulls inbox summary
3. Task Extractor generates task list, logs: `event="tasks_extracted", next_agent="none"` (task list is for you)

### Avoiding Conflicts

- **Separate skill domains**: Productivity Agent owns email/tasks; Research Agent owns vault analysis
- **Non-overlapping schedules**: Productivity runs morning/evening; Research runs weekly/on-demand
- **Single writer to critical files**: Only one agent modifies a note at a time (SQLite transaction)
- **Approval for vault changes**: Both agents write to Inbox; Architect (human-supervised) files notes to permanent locations

---

## Integration with Your Vault

### Vault Locations

Agent-managed notes:

```
vault/
├── 00-Inbox/
│   ├── agent_daily_digest_2026-04-19.md     (Productivity)
│   ├── agent_weekly_synthesis_2026-04-19.md (Productivity)
│   └── agent_research_gaps_2026-04-19.md    (Research)
├── 07-Daily/
│   ├── 2026-04-19.md          (Productivity Agent writes: digest + tasks)
├── 02-Areas/Learning/
│   └── 2026-04-19 — Agent Synthesis — Emergence & AI.md  (Research Agent)
└── Meta/
    ├── agent-log.md           (Agent execution history)
    ├── agent-metrics.md       (Skill performance over time)
    └── skills-manifest.json   (Inventory of learned skills)
```

### Vault Sync

Agent runs on Oracle ARM instance; vault on your machine:

```
Option 1: Git sync (recommended)
  Oracle instance clones your vault repo
  Agent commits changes via git
  You pull changes; see agent's work as commits
  
Option 2: Bidirectional sync
  Agent instance syncs via rsync/Syncthing
  Faster than git; more state to manage
  
Option 3: Read-only on agent
  Agent reads vault; writes to separate "agent output" dir
  You review agent's output, manually integrate if good
```

For transparency and auditability, **Option 1 (Git sync)** is recommended.

---

## Safety Guardrails

### Action Whitelist

Agents can safely:
- ✅ Read any vault note
- ✅ Write to 00-Inbox/ (for you to review before filing)
- ✅ Read email / calendar
- ✅ Create drafts (not send)
- ✅ Execute local Python skills
- ✅ Query SQLite knowledge base
- ✅ Commit to git (with clear agent-attribution messages)

Agents **cannot**:
- ❌ Delete files
- ❌ Execute shell commands (except git, safe file I/O)
- ❌ Access credentials / secrets
- ❌ Send email without approval
- ❌ Modify permanent vault notes (only Inbox or meta files)
- ❌ Call external APIs (unless whitelisted)

### Approval Workflows

**Automatic execution**: Daily digest, email triage, task extraction (low-risk)

**Human review before execution**: 
- Sending emails
- Modifying permanent vault files
- Calling paid APIs (Claude for skill improvement)
- Agent discovering "new" skill (proposes code, you review)

**Rollback mechanisms**:
- Agent commits include a "rollback ID" (git tag)
- If a skill causes problems, revert to prior version instantly
- Skill metrics track reliability; low-confidence skills get extra review

---

## Implementation Approach

### Phase 1: Productivity Agent MVP (Week 1-3)

1. **Week 1**: Core infrastructure
   - Vault Git sync
   - SQLite knowledge base setup
   - read_vault.py, write_note.py, list_tasks.py

2. **Week 2**: First skill (email triage)
   - email_summarizer.py (v1: basic summary)
   - Manual feedback loop
   - Agent improves to v2

3. **Week 3**: Extend to daily digest
   - daily_digest.py (v1)
   - task_extractor.py (v1)
   - Test for a week; refine

### Phase 2: Research Agent (Week 4-5)

1. Vector embeddings for vault notes
2. topic_mapper.py (analyze your research interests)
3. synthesis_writer.py (generate cross-domain insights)

### Phase 3: Integration & Hardening (Week 6+)

- Both agents running; test for 1-2 weeks
- Refine approval workflows
- Optimize performance

---

## Success Metrics

**Productivity Agent**:
- Email digest created daily (100% on-time rate)
- Task extraction catches 90%+ of action items
- Weekly synthesis rated 7+/10 quality
- Average skill improvement trajectory (v1 → v2 → v3 shows measurable gains)

**Research Agent**:
- Gap detection identifies 3-5 new research opportunities/month
- Synthesis notes make unexpected connections (you rate as surprising/useful)
- Vault pattern analysis reveals your topic clusters accurately

**Overall**:
- Agents run reliably for 4+ weeks without human intervention
- Skills evolve visibly (git history shows improvement trajectory)
- No unwanted actions taken (whitelist enforcement works)

---

## Related Notes

- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Agent Architecture Patterns|Agent Architecture Patterns]] — Deployment patterns, skill design, feedback mechanics
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — LLM Strategy and Cost Analysis|LLM Strategy & Cost Analysis]] — Which LLM to use; cost trade-offs; hybrid routing logic implemented here
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Oracle Cloud ARM Setup Guide|Oracle Cloud ARM Setup Guide]] — Provisioning the always-free ARM instance this system runs on
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Safety Guardrails|Safety Guardrails]] — Full specification of the action whitelist, approval workflows, and rollback logic referenced in the Safety section above
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Voyager — LLM-Powered Embodied Agent|Voyager]] — Reference model for skill library + iterative prompting
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — ADAS — Automated Design of Agentic Systems|ADAS]] — Reference model for agent self-improvement and knowledge inheritance across generations
- [[02-Areas/Learning/Self-Study/Emergence/2026-04-04 — Complex Adaptive Systems|Complex Adaptive Systems]] — The two-agent system is a minimal CAS: agents with local skill rules, shared environment (vault), and emergent knowledge synthesis; coordination via shared KB mirrors how CAS agents coordinate via local signals
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]] — The Research Agent's gap detection and synthesis generation are operational Bayesian reasoning: prior = existing vault knowledge; new notes = evidence; posterior = updated research strategy
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition]] — Agent self-improvement via structured feedback (skill quality ratings, improvement proposals) is applied metacognition at the system level: monitoring + regulation, but for a software agent rather than a human mind
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — John Dewey — Philosopher|John Dewey — Pragmatism and Learning-by-Doing]] — The Personal AI Agent architecture instantiates Dewey's pragmatist epistemology: agents learn through organism-environment transaction, where "organism" is the agent and "environment" is the vault + feedback loop; skills improve through iterative problem-solving (Dewey's inquiry) rather than passive knowledge transfer; the agent's self-improvement via feedback and skill refinement is computational embodiment of Dewey's learning-by-doing thesis
