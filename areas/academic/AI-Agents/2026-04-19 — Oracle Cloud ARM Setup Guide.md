---
type: note
title: Oracle Cloud ARM Setup Guide
tags:
  - infrastructure
  - oracle-cloud
  - arm
  - devops
  - llm
  - deployment
status: active
created: 2026-04-19
---

# Oracle Cloud ARM Setup Guide

Practical guide to provisioning and configuring Oracle Cloud's always-free ARM instance for running autonomous agents with local LLM inference.

---

## Prerequisites

- **Oracle Cloud Account** (free tier)
- **SSH key pair** (generate locally or let Oracle create one)
- **Docker** installed locally (for local testing)
- **Git** installed locally
- **~15 minutes** for instance creation

---

## Step 1: Provision Always-Free ARM Instance

### In Oracle Cloud Console

1. **Navigate**: Compute → Instances
2. **Click**: "Create Instance"
3. **Configure**:
   - **Name**: `agent-brain` (or your choice)
   - **Image**: Oracle Linux 9 (ARM-compatible; free tier eligible)
   - **Shape**: Ampere A1 Compute
     * CPU: 4 cores (OCPU) ← default free tier
     * RAM: 24GB ← always-free tier limit
     * Network bandwidth: 40 Gbps (shared)
   - **Virtual Cloud Network**: Create new or use default
   - **Subnet**: Public (allows SSH from internet)
   - **SSH Key**: Upload your public key or let Oracle generate one
   - **Availability Domain**: Any (doesn't matter for free tier)

4. **Click**: Create

   Instance creation takes ~2-3 minutes. You'll see status: "PROVISIONING" → "RUNNING".

5. **Copy**: The instance's **Public IP Address** (e.g., `150.202.10.42`)

### Verify SSH Access

```bash
ssh -i ~/.ssh/oracle_key ubuntu@150.202.10.42
# If Oracle-generated key:
ssh -i ~/path/to/downloaded/key.key opc@150.202.10.42
```

You should see the Oracle Linux 9 prompt. Exit with `exit`.

---

## Step 2: Initial Setup on Instance

Log in to the instance:

```bash
ssh -i ~/.ssh/oracle_key opc@<YOUR_IP>
```

### Update System

```bash
sudo yum update -y
sudo yum install -y git curl wget python3.11 python3.11-pip
```

### Create Working Directory

```bash
mkdir -p ~/agent-brain
cd ~/agent-brain
```

### Clone Your Vault

Your vault is the knowledge base. Clone it into the instance:

```bash
git clone https://github.com/yourusername/your-vault.git vault
cd vault
```

(Or use SSH key if the repo is private:)

```bash
git clone git@github.com:yourusername/your-vault.git vault
```

---

## Step 3: Install Local LLM (Llama.cpp)

Two options: **llama.cpp** (faster, recommended) or **Ollama** (easier UI, slower).

### Option A: llama.cpp (Recommended)

**Install from source** (compiles with ARM optimizations):

```bash
cd ~/agent-brain
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# Build with ARM SIMD optimizations
make -j4 LLAMA_ARM_NEON=1
```

This takes ~3-5 minutes. When done, you'll have `./main` binary.

**Download model** (Llama 2 7B quantized, 4-bit):

```bash
cd ~/agent-brain/llama.cpp

# Download a quantized model (~3.5GB)
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_K_M.gguf

# Verify download
ls -lh llama-2-7b-chat.ggmlv3.q4_K_M.gguf
```

**Test inference**:

```bash
./main -m llama-2-7b-chat.ggmlv3.q4_K_M.gguf \
  -n 128 \
  -p "Explain AI agents in one sentence:"
```

You should see text generation at ~10-15 tokens/sec. Let it finish (Ctrl+C after a few sentences).

### Option B: Ollama (Easier, Slightly Slower)

**Install Ollama**:

```bash
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve &
```

Wait for "Listening on...". Then in another terminal:

```bash
ollama pull llama2
```

This downloads the model (~3.5GB). Test:

```bash
ollama run llama2 "Explain AI agents in one sentence"
```

---

## Step 4: Set Up Agent Python Environment

### Install Python dependencies

```bash
cd ~/agent-brain
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install \
  sqlite3-python \
  fastapi uvicorn \
  aiohttp aiofiles \
  pyyaml \
  sentence-transformers \
  openai \
  gitpython \
  apscheduler
```

This takes ~5-10 minutes (sentence-transformers is large).

### Create Agent Core Structure

```bash
mkdir -p agent/{core,skills,memory}
touch agent/__init__.py
touch agent/core/{llm.py,vault.py,executor.py}
touch agent/skills/__init__.py
touch agent/memory/__init__.py
```

---

## Step 5: Configure LLM Interface

### Create `agent/core/llm.py`

```python
import json
import subprocess
import asyncio

class LocalLLM:
    """Interface to llama.cpp or Ollama"""
    
    def __init__(self, model_path=None, use_ollama=False):
        self.use_ollama = use_ollama
        self.model_path = model_path
    
    async def generate(self, prompt: str, max_tokens: int = 500) -> str:
        if self.use_ollama:
            return await self._generate_ollama(prompt, max_tokens)
        else:
            return await self._generate_llama_cpp(prompt, max_tokens)
    
    async def _generate_llama_cpp(self, prompt: str, max_tokens: int) -> str:
        """Call llama.cpp main binary"""
        cmd = [
            "./main",
            "-m", self.model_path,
            "-n", str(max_tokens),
            "-p", prompt,
            "-t", "4",  # 4 threads
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return result.stdout
    
    async def _generate_ollama(self, prompt: str, max_tokens: int) -> str:
        """Call Ollama API"""
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama2", "prompt": prompt, "stream": False}
            ) as resp:
                data = await resp.json()
                return data["response"]
```

### Create `agent/core/vault.py`

```python
import os
import json
from pathlib import Path

class VaultInterface:
    """Read/write vault notes"""
    
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.inbox_path = self.vault_path / "00-Inbox"
    
    def read_note(self, path: str) -> str:
        """Read a note file"""
        full_path = self.vault_path / path
        if full_path.exists():
            return full_path.read_text()
        return None
    
    def write_note(self, path: str, content: str) -> bool:
        """Write a note to Inbox for review"""
        target_path = self.inbox_path / path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content)
        return True
    
    def list_notes(self, folder: str) -> list:
        """List all .md files in a folder"""
        folder_path = self.vault_path / folder
        if not folder_path.exists():
            return []
        return [f.name for f in folder_path.glob("*.md")]
```

---

## Step 6: Set Up APScheduler (Task Scheduling)

Agent tasks run on a schedule. Create `agent/scheduler.py`:

```python
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio

scheduler = AsyncIOScheduler()

# Daily digest at 8 AM
scheduler.add_job(
    daily_digest_task,
    CronTrigger(hour=8, minute=0),
    id="daily_digest"
)

# Email triage at 9 AM
scheduler.add_job(
    email_triage_task,
    CronTrigger(hour=9, minute=0),
    id="email_triage"
)

# Weekly synthesis on Friday at 5 PM
scheduler.add_job(
    weekly_synthesis_task,
    CronTrigger(day_of_week=4, hour=17, minute=0),
    id="weekly_synthesis"
)

async def run_scheduler():
    scheduler.start()
    try:
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
```

---

## Step 7: Network & Remote Access

### SSH Tunnel (Recommended for Security)

To access agent API from your local machine:

```bash
# On your local machine
ssh -N -L 8000:localhost:8000 opc@<YOUR_IP>
```

Then locally:

```bash
curl http://localhost:8000/health
```

### Open Firewall (If Direct Access Needed)

On the Oracle instance:

```bash
sudo firewall-cmd --permanent --add-port=8000/tcp
sudo firewall-cmd --reload
```

Then access from anywhere:

```bash
curl http://<YOUR_IP>:8000/health
```

**Warning**: Leaving ports open exposes the API. Use SSH tunnel in production.

---

## Step 8: Vault Sync Strategy

### Option 1: Git (Recommended)

Agent commits its changes to git. You pull periodically.

```bash
cd ~/agent-brain/vault
git config user.email "agent@local"
git config user.name "Agent"

# Agent commits after each task
git add .
git commit -m "feat: daily digest 2026-04-19"
git push origin main
```

On your local machine:

```bash
cd /path/to/vault
git pull  # See agent's work as commits
```

### Option 2: Syncthing (Bidirectional Sync)

Install Syncthing on instance and your machine; keep vault folders in sync.

```bash
# On instance
curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
sudo apt update && sudo apt install syncthing

syncthing  # Starts UI on localhost:8384
```

Then add folders in both Syncthing instances to keep them in sync.

### Option 3: Read-Only on Agent

Agent reads vault (cloned via git), writes outputs to separate directory. You review and integrate manually.

```bash
~/agent-brain/
├── vault/               (read-only clone of your vault)
├── agent_output/       (where agent writes synthesis, drafts)
└── agent/              (agent code)
```

**Option 1 (Git)** is recommended for transparency and auditability.

---

## Step 9: Storage Considerations

### Current Disk Usage

Oracle's free tier includes **50GB** block storage (sufficient):

```bash
# Check usage
df -h /

# Monitor vault size
du -sh ~/agent-brain/vault
```

As your vault grows (unlikely to exceed 5GB for years), you'll be fine.

### Backup Strategy

The vault is in git, so version control is your backup. Additionally:

```bash
# Weekly snapshot to object storage (free tier includes 20GB)
sudo yum install -y awscli

# Create S3 bucket (Oracle or AWS)
# Set up cron job to push vault weekly
```

---

## Step 10: Monitoring & Logs

### Agent Logs

Structured JSON logs to vault:

```
Meta/
├── agent-log.md          (Human-readable execution history)
├── agent-metrics.json    (Skill performance metrics)
└── agent-errors.log     (Error traces)
```

### System Monitoring

```bash
# Monitor instance health
vmstat 1 5   # CPU, memory, I/O
top          # Process list

# Monitor LLM process
ps aux | grep llama
```

---

## Step 11: Starting the Agent

### Create `start_agent.sh`

```bash
#!/bin/bash

cd ~/agent-brain

# Activate venv
source venv/bin/activate

# Start llama.cpp in background (if not Ollama)
cd llama.cpp
./main -m llama-2-7b-chat.ggmlv3.q4_K_M.gguf --port 8001 &
cd ..

# Start agent scheduler
python3 -m agent.main &

echo "Agent started. PID: $!"
```

```bash
chmod +x start_agent.sh
./start_agent.sh
```

### Run as Service (Optional)

Create `/etc/systemd/system/agent.service`:

```ini
[Unit]
Description=Agent Brain Service
After=network.target

[Service]
Type=simple
User=opc
WorkingDirectory=/home/opc/agent-brain
ExecStart=/home/opc/agent-brain/start_agent.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable agent
sudo systemctl start agent
sudo systemctl status agent
```

---

## Troubleshooting

### LLM Inference Slow (< 5 tokens/sec)

- **Check CPU**: `top` should show llama.cpp using ~300% CPU (3 cores)
- **If low CPU**: Increase threads in llama.cpp (`-t 4`)
- **If still slow**: Model may be too large; try 7B-q4 instead of larger quantization

### Agent can't read vault

- **Check path**: `ls -la ~/agent-brain/vault/` should list vault files
- **Check permissions**: `ls -la ~/agent-brain/vault/00-Inbox/` should be readable
- **Test read**: `python3 -c "import pathlib; print(list(pathlib.Path('vault').glob('*.md')))"`

### Out of memory

- **Check**: `free -h` should show ~20GB free
- **Kill unneeded processes**: `killall -9 java` (if any)
- **Reduce model size**: Use 4-bit quantization instead of 8-bit

### Git push fails

- **Check SSH key**: `ssh -T git@github.com` should authenticate
- **Configure git**: `git config --global user.email "agent@local"`
- **Check branch**: `git branch -a` to see remote branches

---

## Cost & Sustainability

**Total monthly cost**: **$0**

- Instance: free-tier always-free
- Storage: included in free-tier
- Bandwidth: included in free-tier
- Your electricity: negligible (ARM uses ~5W idle)

Instance can run 24/7 indefinitely on free tier.

---

## Related Notes

- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Personal AI Agent Architecture Design|Personal AI Agent Architecture Design]] — Agent design for your use cases; this guide provisions the substrate that design runs on
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — LLM Strategy and Cost Analysis|LLM Strategy & Cost Analysis]] — Why local LLM is cost-sustainable; the ARM benchmarks in that note map directly to this hardware
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Agent Architecture Patterns|Agent Architecture Patterns]] — This guide implements the Single-Instance Monolithic pattern (Pattern A) with vault sync enabling optional distributed coordination
- [[02-Areas/Learning/Self-Study/AI-Agents/2026-04-19 — Safety Guardrails|Safety Guardrails]] — The execution sandboxing, audit logs, and rollback procedures in that note depend on the Git-sync strategy set up here (Step 8)
- [[03-Resources/Technical/Containers/OCI-Runtimes/Docker/Docker Image Optimization|Docker Image Optimization]] — Docker is listed as a prerequisite for this guide (Step 1); the multi-stage build and distroless hardening patterns in that note are the correct approach for containerizing the llama.cpp and Ollama inference services deployed here
- [[03-Resources/Technical/Containers/OCI-Runtimes/Podman/Podman vs Docker|Podman vs Docker]] — for a multi-workload Oracle Cloud ARM instance, Podman rootless is the hardened alternative to Docker: it eliminates the docker group root-equivalence risk while maintaining full OCI compatibility with the same llama.cpp and Ollama container images
