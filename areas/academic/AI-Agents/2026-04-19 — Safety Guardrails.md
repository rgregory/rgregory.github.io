---
type: note
title: Safety Guardrails for Autonomous Agents
tags:
  - safety
  - agents
  - security
  - constraints
  - approval-workflows
status: active
created: 2026-04-19
---

# Safety Guardrails for Autonomous Agents

Constraints, approval workflows, and rollback mechanisms to ensure agents operate safely and maintain human control.

---

## Core Principle

**Least Privilege + Human in the Loop**: Agents have minimal capabilities by default. Only explicitly whitelisted actions are allowed. High-risk actions require human approval before execution.

---

## Action Whitelist

### Tier 1: Automatic (No Approval Needed)

Agents can execute these actions without human review:

**Read Operations** ✅
- Read any vault note (all folders)
- Read task log (SQLite)
- Read agent-log.md
- List files in directories
- Parse YAML frontmatter
- Search vault (full-text, vector similarity)

**Write to Inbox** ✅
- Create notes in `00-Inbox/`
- This is the **staging area** — you review before filing

**Local Compute** ✅
- Execute skills (Python code in `skills/` folder)
- Call local LLM inference (llama.cpp)
- Run SQLite queries
- Calculate metrics
- Generate text

**Safe File I/O** ✅
- Create text files (`.md`, `.txt`, `.json`)
- Append to logs
- Create directories under `agent_data/`

**Git Operations** ✅
- `git add` and `git commit` (with agent attribution)
- `git pull` (read-only from remote)
- View `git log`, `git diff`

---

### Tier 2: Approval Required (Agent Proposes, You Review)

Agents request permission for these actions; you approve before execution:

**Sending Communications** 🔒
- Send email
- Post to Slack
- Send calendar invitation
- Publishing to external service

**Paid API Calls** 💰
- Call Claude API (for skill improvement)
- Call OpenAI API
- Call any paid external service

**Modifying Permanent Vault Files** 🗂️
- Edit notes outside `00-Inbox/`
- Modify `Meta/`, `02-Areas/`, `01-Projects/`
- Rename or move files
- Update MOCs

**Discovering New Skills** 🧠
- Agent generates novel skill code (never run before)
- You review code before first execution
- Subsequent iterations of same skill are auto-approved (if previous version passed)

**Vault Metadata Changes** 📋
- Modify frontmatter (tags, type, status)
- Change naming conventions
- Restructure folders

---

### Tier 3: Explicitly Forbidden (Always Blocked)

Agents **cannot** do these, ever:

**Delete Operations** ❌
- Delete files, folders, or notes
- Empty trash
- Purge history
- Clear database

**Dangerous System Commands** ❌
- `rm -rf` or any destructive shell commands
- `sudo` commands
- Modify system files (`/etc/`, `/usr/`)
- Kill processes
- Change permissions

**Credential / Secret Handling** ❌
- Access `.env` files
- Read SSH keys, API keys, passwords
- Store credentials in vault notes
- Log sensitive data

**Network / External** ❌
- Make unapproved network requests
- Download files from untrusted sources
- Curl external URLs (unless whitelisted)
- Modify DNS, firewall rules

**Vault Integrity** ❌
- Bypass whitelist checks
- Escape sandbox execution
- Modify agent code or whitelist itself
- Override approval workflows

---

## Approval Workflow

### How It Works

1. **Agent detects** an action that requires approval
2. **Agent generates** proposal and logs to `Meta/pending-approvals.json`
3. **You review** via `check pending approvals` command
4. **You approve/reject** with one-line decision
5. **Agent executes** only if approved

### Example: Sending Email

```json
{
  "id": "approval:send-email:productivity:1",
  "timestamp": "2026-04-19T09:00:00Z",
  "agent": "productivity",
  "action": "send_email",
  "status": "pending",
  "payload": {
    "to": "colleague@example.com",
    "subject": "Your task update",
    "body": "Here's what I completed this week..."
  },
  "expires_in_seconds": 3600,
  "priority": "normal"
}
```

You review:
```bash
# In vault or via chat command
cat Meta/pending-approvals.json | jq '.[] | select(.status == "pending")'

# Approve
echo '{"approval_id": "approval:send-email:productivity:1", "decision": "approve"}' > /tmp/approve.json

# Or reject
echo '{"approval_id": "approval:send-email:productivity:1", "decision": "reject", "reason": "Change recipient to manager instead"}' > /tmp/approve.json
```

Agent polls approvals file every minute. If approved, it executes. If rejected, it logs the decision and stops.

### Timeout

Approvals expire after 1 hour if not reviewed. Agent logs: "Approval expired; not executed."

---

## Skill Versioning & Rollback

### Versioning

Each skill is stored with a version number:

```
skills/
├── email_summarizer.py (latest)
├── email_summarizer.v1.py
├── email_summarizer.v2.py
└── email_summarizer.v3.py
```

Git tracks the full history:

```bash
git log --oneline skills/email_summarizer.py

# Output:
# abc1234 v3: email_summarizer — improved header detection
# def5678 v2: email_summarizer — fix unicode rendering
# ghi9012 v1: email_summarizer — initial skill
```

### Rollback Trigger

**Automatic**: If a skill fails 3 times in a row, agent reverts to previous version:

```json
{
  "skill": "email_summarizer.py",
  "version": 3,
  "status": "failed",
  "error": "UnicodeDecodeError: utf-8",
  "failures_in_row": 3,
  "action": "ROLLBACK_TO_V2"
}
```

**Manual**: You can request a rollback at any time:

```bash
# Agent rollback command (in chat or vault note)
# Revert email_summarizer to v2
rollback skill:email_summarizer to:v2
```

Agent checks git history, reverts file, commits with message: "rollback: email_summarizer v3 → v2 (manual request)".

### Diff Before Improve

When agent improves a skill, it shows you the diff:

```bash
git diff skills/email_summarizer.py

# Output:
# - return summary[:500]
# + return summary[:1000]  # Handle longer emails
#
# + # Fix: properly handle forwarded threads
```

You can approve or ask agent to revise before committing.

---

## Execution Sandboxing

### Skill Execution Environment

Skills run in an isolated environment with:

- **No network access** (unless whitelisted)
- **No file system access** outside `agent_data/`
- **Timeout**: 30 seconds max per skill (prevent hangs)
- **Memory limit**: 512MB (prevent runaway memory use)
- **CPU limit**: 1 core (prevent hogging)

### Whitelist for External Access

Only specific skills can access specific resources:

```json
{
  "skill": "email_summarizer.py",
  "allowed_apis": ["gmail_read_only"],
  "allowed_dirs": ["vault/", "agent_data/"],
  "timeout_sec": 30,
  "memory_limit_mb": 512
}
```

---

## Audit & Transparency

### Agent Action Log

Every action is logged to `Meta/agent-log.md`:

```markdown
## 2026-04-19

### 09:00 — Productivity Agent: Daily Digest
- Status: Success
- Duration: 12 sec
- Emails processed: 23
- Tasks extracted: 5
- Output: 00-Inbox/agent_daily_digest_2026-04-19.md
- Approval status: N/A (auto-approved)

### 14:30 — Research Agent: Synthesis Generation
- Status: Pending Approval
- Action: Send email draft to colleague
- Approval required: YES
- Pending since: 14:30:00
- Expires: 15:30:00
```

### Skill Metrics Log

`Meta/agent-metrics.json` tracks skill performance:

```json
{
  "email_summarizer": {
    "v3": {
      "runs": 15,
      "successes": 14,
      "failures": 1,
      "reliability": 0.93,
      "avg_duration_sec": 8.2,
      "last_improved": "2026-04-18",
      "improvement_delta": "better error handling for unicode"
    }
  }
}
```

---

## Incident Response

### Detect a Problem

Agent misbehaves:

Example: Skill deletes a file (even though it shouldn't be possible)

### Response Steps

1. **Stop agent immediately**:
   ```bash
   systemctl stop agent
   # Or kill the process
   pkill -f agent.main
   ```

2. **Identify root cause**:
   - Check `Meta/agent-log.md` for the action
   - Check git history: `git log --oneline` to see what changed
   - Check skill code: `git show <commit>` to see the exact change

3. **Assess damage**:
   - Which files were affected?
   - Can they be recovered from git history?
   - `git checkout HEAD~1 -- filename` to restore

4. **Rollback**:
   ```bash
   git revert <commit>  # Undo the problematic change
   git push
   ```

5. **Fix root cause**:
   - Update whitelist (if agent shouldn't have had access)
   - Fix the skill code (if logic error)
   - Add a guard condition (if edge case not handled)

6. **Test fix**:
   - Run skill manually: `python3 -c "from agent.skills import email_summarizer; print(email_summarizer.run(...))"`
   - Verify it works as expected

7. **Restart agent**:
   ```bash
   systemctl start agent
   ```

8. **Document**:
   - Create incident note in vault
   - Record timeline, root cause, fix
   - Update safety rules if needed

---

## Testing Approval Workflows

### Dry-Run Mode

Before deploying agents live, test in **dry-run mode**:

```python
# In agent config
DRY_RUN = True  # Agent proposes actions but doesn't execute
```

All agent actions are logged as "would do" rather than "did do". You review and confirm the behavior is correct before switching to live mode.

### Staged Rollout

1. **Week 1**: Email triage agent (lowest-risk, read-only)
2. **Week 2**: Task extraction agent (writes to Inbox, no side effects)
3. **Week 3**: Weekly synthesis (writes to Inbox)
4. **Week 4**: Add research agent (read + writes to Inbox)
5. **Week 5**: Enable skill auto-improvement (requires approval for each version)

---

## Principle-Based Safety

### The Three Principles

**1. Transparency**: Every action logged; you can audit at any time

**2. Control**: You can stop agent, review decisions, rollback changes

**3. Least Privilege**: Agent starts with minimal capabilities; request more as needed

### When in Doubt

If uncertain whether an action is safe:

- **Reject the approval** and ask agent to revise
- **Rollback** the skill version
- **Disable the agent** and investigate
- **Update the whitelist** to restrict further

The burden of proof is on the agent. You get final say.

---

## Related Notes

- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Personal AI Agent Architecture Design|Personal AI Agent Architecture Design]] — Agent design and use cases; the whitelist tiers map directly onto the approval workflows in that design
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Agent Architecture Patterns|Agent Architecture Patterns]] — The anti-patterns section there (silent failures, unbounded learning) is what these guardrails prevent; sandboxing maps to skill execution isolation
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Oracle Cloud ARM Setup Guide|Oracle Cloud ARM Setup Guide]] — The Git-sync strategy (Step 8) is the mechanism that makes rollback and audit logging possible
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — LLM Strategy and Cost Analysis|LLM Strategy & Cost Analysis]] — Paid API calls are a Tier 2 action requiring approval; cost discipline here enforces the hybrid budget model
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-14 — First-Person Epistemology — Can Inner Experience Produce Knowledge|First-Person Epistemology]] — Trust and verification in autonomous systems; the agent cannot report on its own inner states with authority — audit logs substitute for introspection
- [[02-Areas/Learning/Self-Study/Philosophy/2026-04-03 — Searle Chinese Room|Searle's Chinese Room]] — The intentionality gap is a direct argument for why least-privilege constraints are necessary: an agent executing correct-looking actions has no semantic understanding of what it is doing; the whitelist substitutes for judgment
- [[02-Areas/Learning/Self-Study/Emergence/2026-04-04 — Complex Adaptive Systems|Complex Adaptive Systems]] — The approval workflow is a deliberately designed control layer on top of an adaptive CAS; Hayek's knowledge problem cuts both ways — decentralized agents can produce bad emergent outcomes too, not just good ones
- [[02-Areas/Learning/Self-Study/Cognitive-Science/2026-04-06 — Metacognition Thinking About Thinking|Metacognition]] — The skill metrics log (reliability, error traces, improvement delta) is a metacognitive record: the agent monitoring its own performance across time, which is the prerequisite for regulation
- [[03-Resources/Technical/Containers/OCI-Runtimes/Podman/Podman vs Docker|Podman vs Docker]] — Podman rootless is the OS-layer implementation of the same least-privilege principle: user namespace UID mapping contains any breakout to the invoking user's privilege level, mirroring the agent whitelist that constrains what any given skill can touch; the tiered architecture (rootless by default, rootful only when explicitly needed) maps structurally to the Tier 1/Tier 2/Tier 3 action model here
- [[03-Resources/Technical/Containers/Apple-Containers/Apple Containers Fundamentals|Apple Containers Fundamentals]] — Apple's entitlement model is the platform-native version of this whitelist architecture: capabilities must be declared at build time, silently denied if absent, no runtime escalation; this is capability-based access control implemented at OS layer rather than application layer
- [[03-Resources/Technical/Containers/BSD-Containerization/FreeBSD/FreeBSD Jails|FreeBSD Jails]] — the Jail model is structurally isomorphic to the Tier 1/2/3 whitelist architecture here: both define a bounded execution environment where operations outside the declared perimeter are unconditionally rejected; the "confined root" insight (UID 0 inside a jail cannot affect the host) maps exactly to Tier 3 prohibitions that cannot be overridden even by a skill claiming elevated intent; Jails predate Linux containers by a decade and were built for the same shared-hosting multi-tenant security problem that agent sandboxing addresses
- [[03-Resources/Technical/Containers/BSD-Containerization/OpenBSD/OpenBSD Pledge and Unveil|OpenBSD Pledge and Unveil]] — pledge/unveil is the closest OS-level analog to this note's whitelist architecture: both are subtractive (define what is permitted; everything else is denied), both are declared at initialization before the untrusted operational phase, and both enforce unconditional termination on violation rather than graceful degradation; the progressive narrowing pattern in pledge (calling pledge() multiple times to tighten the promise set as startup phases complete) maps directly to the staged-rollout model in Section "Staged Rollout" here
- [[03-Resources/Technical/Containers/BSD-Containerization/NetBSD/NetBSD Rump Kernels|NetBSD Rump Kernels]] — rump kernels push the least-privilege principle to the kernel-component level: an application linked against only the rump subsystems it needs cannot be affected by kernel vulnerabilities in any other subsystem; this is the deepest technical implementation of Tier 3 isolation — not just "no delete operations" but "no kernel attack surface beyond what this process structurally requires"
