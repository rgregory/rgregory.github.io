---
type: note
title: Agent Architecture Patterns for Autonomous Systems
tags:
  - ai
  - agents
  - architecture
  - distributed-systems
  - design-patterns
status: active
created: 2026-04-19
---

# Agent Architecture Patterns for Autonomous Systems

Architectural patterns for building autonomous AI agents that can learn, persist knowledge, and operate independently. These patterns emerge from Voyager, ADAS, and distributed systems theory.

## Core Pattern: Agent-as-Process

An autonomous agent is a persistent process that:
1. **Observes** the environment (task requests, system state, feedback)
2. **Reasons** about what to do (using LLM or logic)
3. **Acts** on the environment (execute skills, create outputs)
4. **Learns** from outcomes (capture feedback, refine skills)
5. **Repeats** indefinitely (triggered by schedule, events, or human requests)

```
┌─────────────┐
│  Observe    │ ← Environment (vault, tasks, outcomes)
└──────┬──────┘
       ↓
┌─────────────┐
│  Reason     │ ← LLM or decision logic
└──────┬──────┘
       ↓
┌─────────────┐
│   Act       │ ← Execute skills, create effects
└──────┬──────┘
       ↓
┌─────────────┐
│   Learn     │ ← Capture outcomes, refine
└──────┬──────┘
       ↓
    [Repeat]
```

This loop is **Dewey's learning-by-doing** and **Voyager's iterative prompting** applied to general autonomous agents.

---

## Deployment Architecture: Single-Instance vs. Distributed

### Pattern A: Single-Instance Monolithic

**Structure**: All components (reasoning, skill execution, memory, coordination) run on one machine.

```
┌─────────────────────────────────┐
│    Single Machine (24GB RAM)    │
├─────────────────────────────────┤
│  Agent Core                     │
│  ├─ LLM Interface               │
│  ├─ Skill Executor              │
│  ├─ Memory System (SQLite)      │
│  └─ Feedback Loop               │
└─────────────────────────────────┘
```

**Advantages**:
- No network coordination complexity
- Faster decision loops (no RPC latency)
- Simpler debugging and monitoring
- Lower infrastructure cost
- Easier state management (single process)

**Disadvantages**:
- Single point of failure
- Bounded by single machine resources
- Can't scale beyond one instance
- Less resilient to crashes

**Best for**: Personal agents, prototyping, small-scale autonomous systems

**Example**: Personal productivity agent on Oracle Cloud ARM (this project)

---

### Pattern B: Distributed Multi-Agent

**Structure**: Multiple specialized agents coordinating via message passing.

```
┌──────────────┐
│ Coordinator  │ (task dispatcher)
└──────┬───────┘
       │
    ┌──┴──┬──────┬──────┐
    ↓     ↓      ↓      ↓
┌──────┐┌──────┐┌──────┐
│Worker│ │Worker│ │Worker│ (skill executors)
│  1   │ │  2   │ │  3   │
└──────┘ └──────┘ └──────┘
    ↓     ↓      ↓      ↓
    └──────┬──────┴──────┘
           ↓
    ┌─────────────┐
    │ Shared KB   │ (memory/skills)
    └─────────────┘
```

**Advantages**:
- Resilience: if one worker fails, others continue
- Scalability: add more workers for more capacity
- Task parallelization: multiple skills run concurrently
- Load distribution: balance work across machines
- Specialization: workers can be optimized for specific skill domains

**Disadvantages**:
- Coordination complexity: message passing, consensus, ordering
- Network latency: slower decision loops than monolithic
- Consistency challenges: distributed state management
- Operational complexity: monitoring, logging across machines

**Best for**: Large-scale systems, fault-tolerant production agents, multi-domain specialization

**Example**: Research synthesis (one agent queries vault, one agent executes searches, one analyzes results)

---

## Skill Library Design

Skills are the **atomic unit of agent behavior** — reusable, improvable, composable chunks of intelligence.

### Representation: Code as Knowledge

**Decision**: Represent skills as **executable Python functions** in a **Git repository**.

```python
# skills/email_summarizer.py
def summarize_emails(inbox_path: str, max_count: int = 5) -> str:
    """
    Summarize the most recent unread emails.
    
    This skill was discovered by the agent on 2026-04-19.
    Version: 3 (improved from v2 based on user feedback)
    
    Returns: Markdown summary of email subjects and key points
    """
    # Implementation...
```

**Why code?**
- **Interpretability**: Humans can read and understand what the skill does
- **Composability**: Skills can call other skills; build hierarchies
- **Testability**: Run skills in isolation, validate behavior
- **Evolvability**: Diffs show exactly how the skill improved
- **Versionability**: Git history = lineage of improvements (ADAS pattern)

**Alternative**: Store as prompts (simpler, less interpretable, harder to compose)

### Skill Library Organization

```
skills/
├── _manifest.json          # Index of all skills
├── core/
│   ├── read_vault.py       # Read notes from vault
│   ├── write_note.py       # Create/update vault notes
│   └── query_knowledge.py  # Search skill library
├── productivity/
│   ├── email_summarizer.py
│   ├── task_scheduler.py
│   └── note_organizer.py
├── research/
│   ├── literature_search.py
│   ├── synthesis_generator.py
│   └── insight_extractor.py
└── meta/
    ├── improve_skill.py    # Agent improves its own skills
    └── discover_skill.py   # Agent invents new skills
```

**Manifest** (`_manifest.json`):
```json
{
  "skills": {
    "email_summarizer": {
      "path": "productivity/email_summarizer.py",
      "version": 3,
      "created": "2026-04-19",
      "last_improved": "2026-04-22",
      "reliability": 0.87,
      "cost": {"api_calls": 1, "execution_time": "5s"},
      "dependencies": ["core/read_vault", "core/write_note"]
    }
  }
}
```

Manifest enables:
- Skill discovery (LLM queries manifest, selects by tags/cost/reliability)
- Composition (know which skills depend on which)
- Metrics tracking (cost, reliability, improvement over time)

---

## Feedback Loop: Environment → Learning

The **feedback loop is everything**. Without it, the agent doesn't improve.

### Loop Mechanics

```
1. OBSERVE
   Agent receives: task request, environment state
   Example: "Summarize my emails from today"

2. REASON
   Agent consults skill library: "Which skills apply?"
   Example: "Use email_summarizer skill"

3. ACT
   Agent executes skill, captures outcome
   Example: Skill runs, produces summary, logs execution time

4. FEEDBACK
   Outcome is evaluated against expected result
   Example: "User rated summary as 8/10; took longer than expected"

5. LEARN
   Agent captures lesson for future iterations
   Example: "email_summarizer needs optimization; marked for refinement"

6. REFINE (optional)
   If outcome was poor, agent improves the skill
   Example: LLM receives feedback + old code → generates improved version
```

### Feedback Types

**Quantitative**:
- Execution time (did it run fast?)
- Resource usage (CPU, memory, API calls)
- Success/failure signal (binary pass/fail)
- Reliability metrics (error rate across runs)

**Qualitative**:
- User rating (1-10 scale on output quality)
- Comparison to baseline (better/worse than previous version)
- Usefulness judgment (was the result actionable?)

**Implicit**:
- Repeated use (frequent = good skill)
- Composition patterns (which skills are called together?)
- Error traces (where did execution fail?)

### Closing the Loop: From Feedback to Improvement

```
Feedback captured
    ↓
Analyze: "Why did it perform poorly?"
    ↓
Generate hypothesis: "Skill is missing X constraint"
    ↓
Refine: Send (old_code, feedback) to LLM → improved code
    ↓
Test: Run improved skill on same task
    ↓
Compare: Better? Keep it. Worse? Revert.
    ↓
Commit: Git push with message "v4: improved email_summarizer"
```

This is **Voyager's iterative prompting** loop applied to any skill domain.

### Connection to Bayesian Belief Updating: The Reliability Filter as Kalman Gain

The feedback loop at the core of agent self-improvement is mechanically identical to **[[02-Areas/Learning/Self-Study/Statistics/2026-05-13 — Kalman Gain|Kalman Gain]]** filtering. The skill manifest's `reliability` metric is a dynamically-updated posterior belief about how trustworthy the skill is:

- **Prior**: Initial belief about skill quality (e.g., 0.80 for a newly discovered skill)
- **Likelihood**: Outcome of the last execution (0 = failure, 1 = success)
- **Posterior**: Updated reliability after incorporating the execution outcome
- **Feedback loop**: Each new execution is a new measurement; the Kalman gain determines how much the new outcome shifts the prior

In pseudocode:
```
reliability[t+1] = reliability[t] + K * (outcome[t] - reliability[t])
```

where `K` (the Kalman gain) is proportional to the uncertainty in the current reliability estimate. If the agent has run a skill 100 times and gotten consistent results, K is small (new evidence only slightly adjusts the estimate). If the skill has been run only once, K is large (new evidence shifts the estimate substantially).

This is the engineering instantiation of [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]]: the agent maintains a probabilistic belief about each skill's reliability and updates it sequentially as evidence arrives. Skill selection becomes **MSE-optimal weighting**: prefer skills with high (posterior) reliability, but occasionally test low-reliability skills to reduce uncertainty (explore-exploit tradeoff).

---

## Memory & Knowledge Base

The agent's **long-term memory** — persistent across time, queryable, improvable.

### Layers of Memory

**1. Skill Library** (working memory)
- Skills the agent has learned
- Fast retrieval (seconds)
- Updated frequently (as agent improves)

**2. Knowledge Base** (episodic memory)
- Vault notes: your research, thoughts, decisions
- Task history: what the agent did before
- Outcomes: results of past actions
- Storage: SQLite + vector embeddings

**3. Metadata & Metrics** (semantic memory)
- Skill reliability: how often does skill X work?
- Cost tracking: which skills are expensive (API calls)?
- Temporal patterns: when is task X usually needed?
- Relationship graphs: which notes connect to which?

### Querying the Knowledge Base

**Vector search** (semantic similarity):
```python
# Find relevant vault notes for a task
query = "email productivity tips"
results = kb.vector_search(query, top_k=5)
# Returns: notes about email management, productivity hacks, etc.
```

**Structured search** (SQL):
```python
# Find skills that match criteria
fast_skills = db.query(
  "SELECT * FROM skills WHERE execution_time < 5 AND reliability > 0.9"
)
# Returns: skills suitable for interactive use
```

**Temporal search** (time-based):
```python
# What did the agent do last week?
recent_actions = db.query(
  "SELECT * FROM action_log WHERE timestamp > NOW() - INTERVAL 7 days"
)
```

### Knowledge Inheritance Across Generations

When you "upgrade" the agent (v1 → v2):

```
Agent v1:
├─ Skill library (50 skills, refined over weeks)
├─ Knowledge base (vault notes, task history)
└─ Metrics (reliability, cost per skill)

↓ Upgrade process

Agent v2:
├─ Inherits: All v1 skills + KB + metrics
├─ New capability: Improved reasoning (new LLM model)
├─ Continues: Same vault, same task patterns
└─ Result: v2 starts optimized, not from scratch
```

This is **ADAS's knowledge inheritance** — agent lineages that improve cumulatively.

---

## Coordination Mechanisms

For multi-agent systems, how do agents coordinate without a central controller?

### Pattern 1: Publish-Subscribe (Event-Driven)

Agent A publishes task completion; Agent B subscribes to that event.

```
Agent A: "I finished email triage"
  ↓
Event Bus
  ↓
Agent B: "Got it, now I'll synthesize insights"
```

**Advantages**: Loose coupling, scales to many agents
**Disadvantages**: Event ordering complexity

### Pattern 2: Shared State (Database)

All agents read/write to shared knowledge base.

```
Agent A: Writes summary to vault
  ↓
Shared KB (SQLite)
  ↓
Agent B: Reads summary, builds on it
```

**Advantages**: Simple to implement, strong consistency possible
**Disadvantages**: Coordination bottleneck if many agents

### Pattern 3: Request-Reply (RPC)

Agent A asks Agent B for a specific service.

```
Agent A: "Summarize this text"
  ↓
Agent B: (processes)
  ↓
Response: "Here's the summary"
```

**Advantages**: Explicit ordering, clear responsibilities
**Disadvantages**: Coupling, latency

---

## Anti-Patterns to Avoid

1. **Skill Bloat**: Too many similar skills (merge them)
2. **No Feedback Loop**: Agent improves based on nothing (add logging)
3. **Silent Failures**: Skill fails but agent doesn't notice (add assertions)
4. **Unbounded Learning**: Agent keeps generating new skills without stopping (add cost thresholds)
5. **Stale Skills**: Old skills never get replaced (add deprecation tracking)
6. **No Isolation**: One bad skill crashes entire agent (sandbox skill execution)

---

## Related Vault Notes

- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Voyager — LLM-Powered Embodied Agent|Voyager]] — Concrete instantiation of this pattern in Minecraft
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — ADAS — Automated Design of Agentic Systems|ADAS]] — Meta-learning approach to improve agents themselves
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — LLM Strategy and Cost Analysis|LLM Strategy & Cost Analysis]] — Which reasoning engine powers the Reason step of this loop
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Personal AI Agent Architecture Design|Personal AI Agent Architecture Design]] — Applies these patterns to two concrete agent designs
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Safety Guardrails|Safety Guardrails]] — Constraints that govern the Act step; sandboxing and rollback operate at this layer
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Oracle Cloud ARM Setup Guide|Oracle Cloud ARM Setup Guide]] — Deployment substrate for the single-instance monolithic pattern
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — Simple Rules Complex Behavior|Simple Rules, Complex Behavior]] — How simple skills compose into complex agents; the same compositionality principle
- [[02-Areas/Learning/Self-Study/Emergence/2026-04-04 — Complex Adaptive Systems|Complex Adaptive Systems]] — The agent-as-process loop is a micro-CAS: observe/act/adapt with feedback; distributed multi-agent pattern is a literal multi-agent CAS
- [[02-Areas/Learning/Self-Study/Emergence/2026-03-21 — What Is Emergence|What Is Emergence]] — Skill composition produces emergent behavior: capabilities that no individual skill possesses appear at the agent level (weak emergence)
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-04 — John Dewey — Philosopher|John Dewey]] — Learning-by-doing: philosophical foundation for the observe-act-learn loop
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition]] — Agent self-monitoring in the Learn step is applied metacognition: the agent tracks whether its own skills are working and regulates accordingly
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Bayesian Reasoning — Updating Beliefs Under Uncertainty|Bayesian Reasoning]] — The feedback loop is Bayesian updating: skill reliability metrics are the posterior; each run is a new data point; the agent updates its "belief" about which skills work
