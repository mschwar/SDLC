# Agentic SDLC Blueprint

An end-to-end software development lifecycle designed for repositories where AI agents do the execution and humans provide direction, guardrails, and final decisions.

This document serves two purposes:

1. **Template.** Copy this into any new repo and adapt the specifics. The structure, hooks, and automation patterns are portable.
2. **Guide.** Every concept is explained from first principles. If you have never heard of a term, the explanation is here.

---

## Table of Contents

- [How to Read This Document](#how-to-read-this-document)
- [The Pipeline at a Glance](#the-pipeline-at-a-glance)
- [Layer 1: Architecture and Blueprints](#layer-1-architecture-and-blueprints)
- [Layer 2: Task Management](#layer-2-task-management)
- [Layer 3: The Inner Loop — Code, Test, Commit](#layer-3-the-inner-loop--code-test-commit)
- [Layer 4: Version Control](#layer-4-version-control)
- [Layer 5: Pull Requests](#layer-5-pull-requests)
- [Layer 6: Review, CI/CD, and Merge](#layer-6-review-cicd-and-merge)
- [Layer 7: Deployment and Feedback](#layer-7-deployment-and-feedback)
- [Concept Reference](#concept-reference)
- [The Hook Chain](#the-hook-chain)
- [Minimum Viable Toolchain](#minimum-viable-toolchain)
- [Metrics That Matter](#metrics-that-matter)
- [Adapting This Blueprint](#adapting-this-blueprint)
- [Optional Advanced Extensions](#optional-advanced-extensions)
- [Further Reading](#further-reading)

---

## How to Read This Document

Each layer follows the same structure:

- **What happens here.** The activity in plain English.
- **Who does it.** Human, agent, or automated system.
- **How it is enforced.** The structural guardrail that makes skipping impossible.
- **What can go wrong.** The failure mode this layer prevents.

Concepts that may be unfamiliar are explained in the [Concept Reference](#concept-reference) section at the end. When you see a term in **bold** for the first time, its full explanation is there.

---

## The Pipeline at a Glance

```
Human turns the key (launches orchestrator)
    |
    v
Orchestrator reads repo state, picks tasks, prints launch instructions
    |
    v
Human pastes instructions into N terminal tabs (launches worker agents)
    |
    v
Worker writes code on a branch
    |
    v
git commit
    |--- pre-commit hook: quality checks (BLOCKS on failure)
    |--- commit-msg hook: validates message format
    |--- post-commit hook: pushes branch, opens draft PR
    v
Draft PR exists on GitHub
    |
    v
GitHub Actions CI runs quality checks on the PR
    |
    v
Review agent picks up the PR
    |--- reads diff
    |--- checks scope and quality
    |--- fixes issues (pushes fix commits)
    |--- CI re-runs on fixes
    v
All clear: review agent approves and merges
    |
    v
post-merge hook fires (dependency sync check)
    |
    v
main is updated, orchestrator picks next task
```

The human touches the keyboard three times: launch orchestrator, paste worker commands, approve merges (or delegate that too).

---

## Layer 1: Architecture and Blueprints

**What happens here.** The repository's structure, schemas, and design decisions are defined. This is the foundation that every other layer builds on.

**Who does it.** The human or lead agent. Architecture is a judgment-heavy activity (L4 in the intelligence-level framework) and should not be delegated without strong review.

**How it is enforced.** Living documents that agents read before every task:

| Document | Purpose |
|----------|---------|
| `AGENTS.md` | Single onboarding file. How to work in this repo. |
| `ARCHITECTURE.md` | System structure, layer roles, data flow. |
| `SCHEMA.md` | Data formats and validation rules. |
| `DECISIONS.md` | Architectural decisions and their rationale. |

**What can go wrong.** Without explicit architecture docs, each agent invents its own conventions. Over 10 tasks, you get 10 different patterns. The documents are the constitution; the agents are the government.

**Principle:** Keep exactly one onboarding document (`AGENTS.md`) that points to everything else. An agent that reads one file should know how to work in the repo. If it needs to read 18 files before starting, the onboarding surface is too large.

When the repo grows beyond a small codebase, add **contract-driven** artifacts alongside the prose docs. Good candidates are OpenAPI specs, JSON Schema or Protobuf contracts, Mermaid sequence diagrams, and structured acceptance criteria. The prose explains intent; the contracts make boundaries machine-checkable.

Do not start with machine-readable everything. Start with the four core docs above. Add machine-readable specs only where ambiguity or cross-team coordination keeps causing defects.

**Failure mode to watch:** as autonomy increases, the main risk is not only inconsistency. It is context loss and cascading hallucination. One bad schema or interface decision at the architecture layer can propagate through coding, testing, and deployment. Explicit contracts and narrow permissions reduce the blast radius.

---

## Layer 2: Task Management

**What happens here.** Work is identified, prioritized, and assigned.

**Who does it.** The orchestrator (lead agent) reads the current state — the roadmap, the risk register, and the codebase — and decides what to work on next.

**How it is enforced.** The roadmap IS the backlog. No separate ticket system, no handoff templates, no ceremony. The orchestrator gives each worker a short prompt:

```
"Read AGENTS.md. [Objective in 1-3 sentences]. Branch: [name]."
```

The worker reads the repo, understands the context, and executes. Agents do not need 130-line instruction documents because they can read the entire repo in seconds.

**What can go wrong.** Without clear scope, agents silently broaden tasks. The orchestrator's prompt must include an objective AND a branch name. The branch name anchors the scope — everything on that branch should serve that objective.

**Anti-pattern:** Writing detailed handoff documents that duplicate information already in the codebase. If the agent needs to know the schema, it reads `SCHEMA.md`. You do not copy the schema into the handoff.

When the repo outgrows a single context window, add repository maps rather than longer prompts. Symbol indexes, `ctags`, language-server navigation, and curated file lists let the orchestrator route only the relevant parts of the repo to each worker.

For larger programs, a clarifier or PM agent can sit ahead of the orchestrator and turn raw intent into PRDs, acceptance criteria, epics, or user stories. For a small repo, this is optional overhead. The roadmap can remain the backlog.

---

## Layer 3: The Inner Loop — Code, Test, Commit

> The **inner loop** is the fast, local cycle that a developer repeats minute by minute: write code, run checks, fix, repeat. Optimizing it makes individual work faster.

**What happens here.** The worker agent writes code, runs local checks, and commits.

**Who does it.** The worker agent. Autonomously.

**How it is enforced.** **Git hooks** — automatic scripts that Git runs at specific moments. The agent does not need to remember to run quality checks. The hooks make it structurally impossible to commit without passing them.

### The commit sequence

```
Agent runs: git commit -m "feat(pipeline): add validation"
    |
    |-- 1. pre-commit hook fires
    |      Runs: python scripts/run_quality_checks.py
    |      Result: PASS → continue / FAIL → commit blocked
    |
    |-- 2. commit-msg hook fires
    |      Checks: does the message follow conventional commit format?
    |      Result: PASS → continue / FAIL → commit blocked
    |
    |-- 3. Commit is recorded
    |
    |-- 4. post-commit hook fires
    |      Runs: git push -u origin <branch>
    |      Runs: gh pr create --draft --fill (if no PR exists)
    |      Result: branch pushed, draft PR opened
```

**What can go wrong.** Without hooks, quality checks are advisory. Agents skip them when they are in a hurry or when their instructions do not mention them. Hooks remove the choice.

### Shift-left testing

> **Shift-left** means moving testing as early as possible. A bug caught during coding costs one hour to fix. The same bug caught in production costs 100x more.

The pre-commit hook is the ultimate shift-left: testing happens BEFORE the code is even recorded in version control. Nothing untested ever enters the history.

### An agent-native TDD loop

For repos with meaningful validation logic, use an explicit Red → Green → Blue loop:

1. **Red:** write or generate the test first; watch it fail.
2. **Green:** write the smallest code change that makes the test pass.
3. **Blue:** refactor, simplify, lint, and re-run the suite.

Agents are particularly strong at this loop because they can execute it quickly and repeatedly. If the stack allows it, prefer AST- or LSP-aware editing over blind text manipulation. Structured edits reduce bracket, indentation, and symbol-resolution mistakes.

### Self-healing local execution

The inner loop gets stronger when compiler errors, test failures, and runtime traces are fed directly back into the worker's context. The agent should not only "write code." It should write, run, read the failure, patch, and retry until the local checks pass.

---

## Layer 4: Version Control

**What happens here.** Code changes are organized into branches, commits are structured, and history is maintained.

**Who does it.** The worker agent. The conventions are defined in `AGENTS.md`; the agent follows them.

**How it is enforced.**

| Convention | Enforcement |
|------------|-------------|
| Branch from `origin/main` | Stated in `AGENTS.md`. Verified during review. |
| One branch per task | Orchestrator assigns branch names in the prompt. |
| **Conventional commits** | `commit-msg` hook validates format. |
| Parallel work uses worktrees | Stated in `AGENTS.md`. Prevents cross-contamination. |

### Conventional commits

Every commit message follows this format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `perf`.

Examples:
```
feat(pipeline): add employer registry validation
fix(qa): correct false positive in language checker
docs: archive completed-phase roadmaps
chore: add pre-commit quality hook
```

**Why this matters.** When agents produce dozens of commits per session, structured messages let the human scan history efficiently. They also enable automated changelog generation and version bumping.

**What can go wrong.** Without the `commit-msg` hook, agents write messages like "update files" or "fix stuff." These are useless for review and make rollbacks dangerous because you cannot tell what a commit changed from its message alone.

---

## Layer 5: Pull Requests

**What happens here.** Completed work is proposed for merging into `main`.

**Who does it.** The `post-commit` hook creates draft PRs automatically. The worker agent does not need to think about PR creation — it is a side effect of committing.

**How it is enforced.**

```bash
# .githooks/post-commit (simplified)
branch=$(git branch --show-current)
if [ "$branch" != "main" ]; then
    git push -u origin "$branch"
    if no PR exists for this branch; then
        gh pr create --draft --fill
    fi
fi
```

### Draft vs. ready

- **Draft PR**: "Here is my work in progress. Track it, but do not merge it."
- **Ready PR**: "This is done. Review and merge."

In this workflow, all PRs start as drafts. They become ready when the review agent approves them.

**What can go wrong.** Without automatic PR creation, agents finish their work but forget to open a PR. The code sits on a branch that nobody knows about. Auto-PR-on-commit makes every piece of work immediately visible.

---

## Layer 6: Review, CI/CD, and Merge

This is the most complex layer. Three systems work together:

### 6a. Continuous Integration (CI)

> **CI** means that every time code is pushed, an automated server builds it and runs the full test suite. If anything breaks, the team knows within minutes.

**What happens here.** GitHub Actions runs the same quality checks that the local hooks run, but in a clean environment on GitHub's servers.

**Who does it.** Automated. Triggered by the push event from the `post-commit` hook.

**How it is enforced.** A workflow file defines the pipeline:

```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements.txt
      - run: python scripts/run_quality_checks.py
```

**Why run the same checks twice (local hooks AND CI)?** Because hooks can be bypassed (`--no-verify`) and different machines may have different environments. CI is the belt; hooks are the suspenders. Together they catch everything.

**Optional extension:** when CI fails on a routine issue, a repair agent can reproduce the failure in a sandbox, patch the branch, and open a fix commit or PR automatically. Keep that agent separate from the original worker so failure review remains independent.

### 6b. Code Review

> **Code review** is the checkpoint where proposed changes are examined before merging. Automated review catches mechanical issues; human review catches logic and intent problems.

**What happens here.** A review agent picks up draft PRs, reads the diff, checks quality, and either:
- **Approves and merges** if everything is clean, or
- **Pushes fix commits** to the PR branch if issues are found, then re-reviews after CI passes on the fixes.

**Who does it.** The review agent (launched by the human, running on a loop or triggered by PR events).

**The review agent's checklist:**

1. Does the diff match the stated objective (branch name)?
2. Do quality checks pass on this branch?
3. Are there scope creep changes (files outside the task's domain)?
4. Are there security concerns (credentials, injection vectors)?
5. Is the code consistent with existing patterns?

**What can go wrong.** Without review, agents merge their own work. This is the agentic equivalent of a student grading their own exam. The review agent is a separate agent from the worker — separation of concerns.

When possible, make review adversarial. Use a different model, prompt, or role from the worker and explicitly ask it to look for auth bypasses, unsafe assumptions, edge cases, and hidden scope creep. The goal is not politeness; the goal is to break weak code before production does.

For UI changes, require evidence in the PR: test output, screenshots, or Playwright traces. For service changes, require contract diffs and integration-test evidence. The PR should carry proof, not just claims.

### 6c. Merge

**What happens here.** Approved PRs are merged into `main`.

**Who does it.** The review agent (after approval) or the human.

**How it is enforced.** **Branch protection rules** on GitHub:

| Rule | Purpose |
|------|---------|
| Require status checks to pass | CI must be green before merge |
| Require review approval | At least one approval (from review agent or human) |
| Prevent force-push to main | History is immutable |
| Require branches to be up to date | No stale merges |

After merge, the `post-merge` hook fires:

```bash
# .githooks/post-merge
# Check if requirements.txt changed in the merge
if git diff HEAD@{1} --name-only | grep -q "requirements.txt"; then
    echo "WARNING: requirements.txt changed. Run: pip install -r requirements.txt"
fi
```

### Merge queues (when to add one)

> A **merge queue** batches approved PRs and tests them in sequence against the latest code before merging, so `main` never breaks.

For a single-developer agentic workflow, a merge queue is unnecessary overhead. Add one only when you regularly have 3+ PRs merging into the same branch in the same hour and see conflicts.

---

## Layer 7: Deployment and Feedback

**What happens here.** Merged code reaches its destination and its impact is measured.

**Who does it.** Depends on the project.

### For repos with a deployment target (web apps, APIs, services)

The CD pipeline automatically deploys merged code to staging, runs integration tests, and promotes to production if they pass. This layer adds:

- Staging environments
- Integration and smoke tests
- Canary or blue-green deployments
- Rollback automation
- Production monitoring and alerting

At higher maturity, add a dedicated deployer or SRE agent with narrow permissions. Production access should default to read-only. Let the agent inspect telemetry, reproduce incidents in staging or sandboxes, and submit hotfix PRs. Reserve direct production writes for tightly scoped actions with explicit approval thresholds.

### For repos without a deployment target (this repo)

"Deployment" is `main` being in a good state. The human pulls `main` and the system is ready. This layer simplifies to:

- `main` is always green (enforced by CI + branch protection)
- The human runs `git pull` when they want the latest state
- Quality checks pass on `main` at all times

### Feedback loop

Regardless of deployment target, this layer closes the loop:

```
Merged code → Observe outcomes → Update roadmap → Pick next task
```

The orchestrator reads the updated `main`, the risk register, and the roadmap, then decides what to work on next. The cycle repeats.

The observation step should eventually include logs, traces, infrastructure metrics, and business metrics, not just "did CI pass." A mature loop can auto-create fix tasks from telemetry, route them back to workers, and even permit safe self-healing actions such as rollback, restart, scale, or config correction under policy.

---

## Concept Reference

Detailed explanations for every technical term used in this blueprint. Read any entry independently.

---

### Git Hooks

> Automatic scripts that Git runs at specific moments in your workflow — before a commit, after a push, and so on.

Git hooks are small programs that live inside your repository and fire automatically when certain Git events happen. You do not run them manually; Git runs them for you at exactly the right moment. They are your repo's immune system — intercepting bad changes before they take root.

Without hooks, every quality check depends on someone remembering to run it. Agents operating at speed do not remember.

**Analogy.** Airport security checkpoints. You do not choose to go through the metal detector; it is built into the path between the ticket counter and the gate.

| Hook | When | Purpose |
|------|------|---------|
| `pre-commit` | Before commit is recorded | Lint, format, validate. Block bad commits. |
| `commit-msg` | After message is written, before commit finalizes | Validate message format. Reject bad messages. |
| `post-commit` | After commit is recorded | Push, open PR, update indexes. Cannot block. |
| `pre-push` | Before push to remote | Run heavy checks. Block bad pushes. |
| `post-merge` | After merge completes | Reinstall deps, rebuild caches. |

**Setup.** Store hooks in `.githooks/` (version-controlled) and configure Git to use them:

```bash
git config core.hooksPath .githooks
```

---

### Conventional Commits

> A standardized format for commit messages so that both humans and machines can understand what changed and why.

Format: `<type>(<scope>): <description>`

Types: `feat` (new feature), `fix` (bug fix), `docs` (documentation), `chore` (maintenance), `refactor` (restructure without behavior change), `test`, `style`, `perf`.

**Analogy.** A library where every book's spine follows a standard — `[Genre] Title - Author` — instead of handwritten "stuff." The standardized library is navigable.

---

### CI/CD

> An automated system that builds, tests, and (optionally) ships your code every time someone makes a change.

**Continuous Integration (CI):** Every push triggers an automated build and test run. If anything breaks, you know within minutes.

**Continuous Deployment (CD):** If all tests pass, code is automatically deployed without manual intervention.

**Analogy.** CI is a restaurant kitchen that inspects every plate before it leaves the pass. CD is the conveyor belt that delivers the inspected plate to the customer's table without a waiter carrying it.

---

### GitHub Actions

> GitHub's built-in automation engine. You write YAML files in `.github/workflows/` that define what happens when events occur (push, PR opened, schedule).

Each workflow has jobs. Each job has steps. Steps run commands or invoke pre-built actions from the community. Configuration lives in the repo alongside the code it governs.

**Analogy.** A factory's programmable automation system. You write recipes ("when a box arrives on conveyor A, scan it, weigh it, route it to shelf B") and the factory follows them 24/7.

---

### Draft PRs vs. Ready PRs

> A draft PR says "work in progress, do not merge." A ready PR says "this is done, review it."

In agentic workflows, all PRs start as drafts (created automatically by the `post-commit` hook). The review agent promotes them to ready after approval. This prevents half-finished work from being merged.

**Analogy.** A draft PR is a painting on an easel with "WORK IN PROGRESS" on it. A ready PR is the painting moved to the gallery wall with a price tag.

---

### Code Review

> Having someone (or something) examine code changes before they become permanent.

**Automated review:** Tools scan for anti-patterns, security issues, style violations. Catches mechanical problems.

**Human/agent review:** Reads the diff for logic, architecture, intent. Catches design problems.

Use both. Automated review catches what humans miss through fatigue. Human review catches what tools cannot understand.

**Analogy.** A spell-checker (automated) catches typos. An editor (human) checks whether the argument holds together. You need both.

---

### Branch Protection Rules

> Repository-level settings that prevent certain actions on important branches.

Common rules: require CI to pass before merge, require review approval, prevent force-pushes to `main`, require branches to be up-to-date.

**Why this matters for agents.** Without branch protection, an agent could merge its own work without review. Branch protection makes self-approval structurally impossible.

**Analogy.** A bank vault requiring two keys turned simultaneously. Even if someone has the code ready and tests passing, they still need a second person's approval.

---

### Shift-Left Testing

> Moving testing as early as possible in the development process.

If development flows left to right (idea → code → test → deploy), "shift left" means pulling testing toward the beginning. Pre-commit hooks are the ultimate shift-left: testing happens before code enters version control.

**Analogy.** Proofreading each paragraph as you write versus writing the entire essay and discovering on the last page that your thesis was wrong.

---

### DORA Metrics

> Four measurements (from Google's DevOps Research and Assessment) that predict engineering team performance.

| Metric | Measures | Elite Benchmark |
|--------|----------|-----------------|
| Lead Time for Changes | Commit to production | < 1 day |
| Deployment Frequency | How often you deploy | Multiple times/day |
| Change Failure Rate | % of deployments causing failures | < 5% |
| Failed Deployment Recovery Time | Time to restore service | < 1 hour |

**Analogy.** The four vital signs a doctor checks: heart rate, blood pressure, temperature, respiratory rate. No single number tells the story, but together they show health.

For solo agentic work, the relevant adaptations are:
- **Quality check pass rate** (change failure rate equivalent)
- **PR cycle time** (lead time equivalent)
- **Rework rate** (commits that fix a previous commit's mistake)

---

### Merge Queues

> An automated system that tests approved PRs in sequence against the latest code before merging.

Solves the "passes individually, breaks together" problem when multiple PRs merge simultaneously. Not needed for single-developer workflows. Add when you regularly have 3+ concurrent PRs targeting the same branch.

**Analogy.** A traffic light with a green arrow at a highway on-ramp. Each car is checked for speed and spacing before merging into traffic.

---

### Property-Based Testing

> Instead of testing specific examples you thought of, define rules that should always be true and let the framework generate thousands of random inputs.

Example-based: `assert add(2, 3) == 5` — tests one case.
Property-based: "for any two positive integers, their sum exceeds either input" — tests thousands of cases.

**Analogy.** A driving test with three specific turns (example-based) versus "drive anywhere in the city for an hour" (property-based). The second discovers whether you can handle anything.

Python tool: `hypothesis`.

---

### Mutation Testing

> Deliberately inject bugs into your code and check whether your tests catch them.

Creates "mutants" (copies of code with small changes: `+` becomes `-`, `>` becomes `>=`, lines deleted). Runs tests against each mutant. If tests still pass, the mutant "survived" — your tests have a blind spot.

**Analogy.** Museum security. Code coverage tells you "sensors exist in every room." Mutation testing is someone actually trying to steal a painting to see if the alarm goes off.

Python tool: `mutmut`.

---

### Dependency Pinning

> Recording exact version numbers of every external library so builds are identical everywhere.

`pyyaml==6.0.1` (pinned) vs. `pyyaml>=6.0` (unpinned). Pinned builds are reproducible. Unpinned builds can break when a library author pushes a bad update.

**Analogy.** A recipe that says "227g of King Arthur all-purpose flour, lot #4521" vs. "some flour." The first produces identical results every time.

---

### Inner Loop vs. Outer Loop

> The inner loop is the fast local cycle (code → test → fix). The outer loop is everything after code leaves your machine (CI → review → merge → deploy).

Optimizing the inner loop makes individuals faster. Optimizing the outer loop makes the whole system faster. You need both.

**Analogy.** A writer drafting at their desk (inner loop) vs. editorial review, fact-checking, printing, and distribution (outer loop). The writer's speed matters, but a slow printing press still delays the book.

---

### Agentic-First

> Designing your entire development process around the assumption that AI agents do most of the execution, with humans providing direction and guardrails.

This means:
- Tasks are bounded, explicit objectives (not vague tickets)
- Validation is automated and machine-readable (not "eyeball it")
- Guardrails are structural (hooks, branch protection) not behavioral ("please remember to...")
- Handoffs have clear inputs and outputs
- Agents do not review their own work

**Analogy.** A highway designed for cars (lane markings, guard rails, on-ramps) vs. a carriage road that cars happen to drive on. The highway has structural safety; the carriage road relies on the driver being careful.

---

### Contract-Driven Development

> Define the boundaries first, then let agents implement inside them.

Contracts are the typed edges of the system: API schemas, data formats, state transitions, acceptance criteria, and infrastructure expectations. Loose boundaries invite hallucination. Tight boundaries make parallel work safe.

**Analogy.** A machine shop where every part has a tolerance spec. If every part is "roughly the right size," assembly fails.

---

### Repository Maps

> Lightweight indexes that help an agent find the right files, symbols, and boundaries without loading the whole repo into context.

Examples include `ctags`, language-server symbol graphs, ownership maps, and curated file manifests. Repository maps are a scaling tool. They preserve short prompts while improving retrieval quality.

**Analogy.** A city map that gets you to the correct neighborhood before you start checking individual addresses.

---

### Adversarial Verification

> Review and testing performed from the perspective of a breaker, not a builder.

Instead of asking "does this look fine?", ask "how would I make this fail?" This can include security-focused prompts, edge-case generation, mutation testing, fuzzing, and using a different model family for review than the one that wrote the code.

**Analogy.** Crash-testing a car into a wall before selling it.

---

### Observability

> The ability to understand what the system is doing from its outputs: logs, metrics, traces, and business signals.

Observability is what turns deployment from a one-way action into a feedback loop. If agents are expected to diagnose incidents or prioritize fixes, they need machine-readable telemetry instead of screenshots of dashboards.

**Analogy.** A cockpit with instruments, not just a windshield.

---

## The Hook Chain

Complete implementation of all git hooks for an agentic workflow.

### .githooks/pre-commit

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== Pre-commit: running quality checks ==="
python scripts/run_quality_checks.py
echo "=== Pre-commit: PASSED ==="
```

### .githooks/commit-msg

```bash
#!/usr/bin/env bash
set -euo pipefail

MSG_FILE="$1"
MSG=$(head -1 "$MSG_FILE")

# Conventional commit pattern: type(scope): description  OR  type: description
PATTERN='^(feat|fix|docs|chore|refactor|test|style|perf|ci|build|revert)(\(.+\))?: .+'

if ! echo "$MSG" | grep -qE "$PATTERN"; then
    echo "ERROR: Commit message does not follow conventional commit format."
    echo "Expected: <type>(<scope>): <description>"
    echo "Types: feat, fix, docs, chore, refactor, test, style, perf, ci, build, revert"
    echo "Got: $MSG"
    exit 1
fi

echo "=== Commit-msg: format OK ==="
```

### .githooks/post-commit

```bash
#!/usr/bin/env bash

BRANCH=$(git branch --show-current)

# Only auto-push and create PRs for non-main branches
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    exit 0
fi

echo "=== Post-commit: pushing branch ==="
git push -u origin "$BRANCH" 2>/dev/null || {
    echo "WARNING: push failed (no remote, or network issue). Push manually."
    exit 0
}

# Create draft PR if one does not exist
EXISTING=$(gh pr list --head "$BRANCH" --state open --json number -q '.[0].number' 2>/dev/null)
if [ -z "$EXISTING" ]; then
    echo "=== Post-commit: creating draft PR ==="
    gh pr create --draft --fill 2>/dev/null || {
        echo "WARNING: PR creation failed. Create manually."
        exit 0
    }
else
    echo "=== Post-commit: PR #$EXISTING already exists ==="
fi
```

### .githooks/pre-push

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "=== Pre-push: running full quality suite ==="
python scripts/run_quality_checks.py
echo "=== Pre-push: PASSED ==="
```

### .githooks/post-merge

```bash
#!/usr/bin/env bash

# Alert if requirements.txt changed in the merge
if git diff HEAD@{1} --name-only 2>/dev/null | grep -q "requirements.txt"; then
    echo ""
    echo "========================================"
    echo "  requirements.txt changed in this merge"
    echo "  Run: pip install -r requirements.txt"
    echo "========================================"
    echo ""
fi
```

### Activation

One command, once per clone:

```bash
git config core.hooksPath .githooks
```

Add this to `AGENTS.md` so every agent that clones the repo activates hooks automatically.

---

## Minimum Viable Toolchain

What to install, in priority order. Each row is independently valuable.

### Install now (30 minutes)

| Tool | What it does | Effort |
|------|-------------|--------|
| `.githooks/` directory with all 5 hooks | Automates quality, format, push, PR creation | Create 5 files |
| `requirements.txt` | Pins dependencies for reproducibility | Create 1 file |
| `git config core.hooksPath .githooks` | Activates hooks | 1 command |

### Install next (1 hour)

| Tool | What it does | Effort |
|------|-------------|--------|
| `.github/workflows/ci.yml` | Remote quality checks on every push/PR | 15 lines of YAML |
| Branch protection on `main` | Requires CI + review before merge | GitHub settings page |
| Lean `AGENTS.md` | Single onboarding doc, absorb workflow/delegation/PR docs | Edit 1 file |

### Install later (when pain demands it)

| Tool | What it does | When |
|------|-------------|------|
| `anthropics/claude-code-action` | Automated PR review via GitHub Actions | When review volume exceeds manual capacity |
| `hypothesis` | Property-based testing | When validation logic grows complex |
| `mutmut` | Mutation testing | When test suite exists and you want to verify its quality |
| `playwright` | Browser automation and UI evidence capture | When UI flows matter |
| `trivy` / `checkov` | Security and infrastructure scanning | When the repo touches cloud, containers, or IaC |
| GitHub merge queue | Serialized conflict-free merging | When 3+ PRs merge per hour regularly |

### Explicitly skip

| Tool | Why |
|------|-----|
| Husky, lefthook, simple-git-hooks | Node.js dependencies in a Python repo. Use native `.githooks/`. |
| Docker-based CI (Jenkins, Drone) | No deployment target. GitHub Actions is sufficient. |
| DORA dashboards | Premature for repo scale. `git log` gives you the data. |
| Complex ticket systems | Agents read the codebase. The roadmap is the backlog. |

---

## Metrics That Matter

### Track now (zero tooling, free from git)

| Metric | How to measure | What it tells you |
|--------|---------------|-------------------|
| Quality check pass rate | Pre-commit hook exit codes | Are agents producing valid work? |
| Commits per session | `git log --oneline --since="today"` | Volume indicator |
| Rework rate | Commits that fix a previous commit on the same branch | Agent accuracy |

### Track when you have CI

| Metric | How to measure | What it tells you |
|--------|---------------|-------------------|
| CI pass rate | GitHub Actions run history | Defect escape from local hooks |
| PR cycle time | Time from PR open to merge | Workflow friction |
| PR throughput | PRs merged per week | Velocity |

### Track when you have orchestration

| Metric | How to measure | What it tells you |
|--------|---------------|-------------------|
| Autonomous solve rate | % of tasks completed without human rescue | True agent reliability |
| Human touch-points per task | Spec approvals, review interventions, deploy approvals | Where autonomy still breaks down |
| Cost per merged change | Model spend + CI/runtime cost by PR or task | Whether more autonomy is economically worth it |

### The key insight

Research shows AI agents increase PR volume by ~98% but do not automatically improve delivery quality. More PRs do not mean better outcomes. Quality checks are more important than velocity metrics. Optimize for pass rate first, throughput second.

---

## Adapting This Blueprint

### For a new repo

1. Copy `.githooks/` directory and `requirements.txt` pattern.
2. Write an `AGENTS.md` with: mission, directory structure, canonical rules, expected commands, definition of done.
3. Add `.github/workflows/ci.yml`.
4. Set branch protection on `main`.
5. Start working. Add complexity only when pain demands it.

### For a repo with a deployment target

Add to Layer 7:
- Staging environment and integration tests
- CD pipeline (deploy on merge to `main`)
- Health checks and rollback automation
- Production monitoring

### For a team (multiple humans)

Add:
- CODEOWNERS file for automatic review assignment
- Merge queue (to prevent "passes alone, breaks together")
- Stricter branch protection (require 2 approvals)
- PR templates (`.github/PULL_REQUEST_TEMPLATE.md`)

### For a monorepo

Add:
- Path-based CI triggers (only run tests for changed packages)
- Scoped conventional commits (`feat(auth):`, `fix(api):`)
- Per-package `requirements.txt` or equivalent

### For a higher-autonomy setup

Add:
- Explicit human gates for spec approval, architecture review, and deployment authorization
- Separate worker, reviewer, tester or security, and SRE roles
- Sandboxed execution environments for run-fail-fix loops
- Read-only production access by default for SRE or deployer agents
- Structured telemetry so agents can diagnose failures without a human dashboard

---

## Optional Advanced Extensions

Everything above is enough for a practical agentic repo. The patterns below are useful when the repo grows, the team grows, or the autonomy level rises.

### Machine-readable specs

If prose docs stop being enough, add machine-readable artifacts next to them:

- System Specification Object (JSON or YAML) for intent, constraints, and acceptance criteria
- OpenAPI, JSON Schema, or Protobuf contracts for interfaces
- Mermaid diagrams for sequence or state transitions
- Gherkin-style acceptance tests when behavior needs explicit executable wording

These artifacts are extensions to the blueprint, not replacements for a clear `AGENTS.md`.

### Swarm orchestration

For simple repos, one orchestrator plus one worker plus one reviewer is enough. For higher throughput, split responsibilities into specialized roles such as clarifier or PM, architect, coder swarm, tester, reviewer, integrator, deployer, SRE, and governance.

Stateful orchestration frameworks such as LangGraph, CrewAI, AutoGen, or Temporal become useful only when you need durable workflows, retries, routing, or many concurrent agents. Historical exemplars such as MetaGPT and ChatDev are useful as patterns, not as mandatory stack choices.

### Optional tooling examples

| Category | Examples | Use when |
|----------|----------|----------|
| Sandboxed execution | E2B, Daytona, Codespaces | Agents need safe run-fail-fix loops |
| Repo-facing coding surfaces | OpenHands, Copilot Agent mode, SWE-agent, Aider, Cursor Composer | You want more automation than a chat window provides |
| Living-spec systems | GitHub Spec Kit, Intent | Specs must stay synchronized with implementation |
| Observability backends | Prometheus, Datadog, Azure Monitor | Agents need machine-readable telemetry |
| Security and IaC scanning | Trivy, Checkov | The repo touches cloud or deployment infrastructure |
| Model routing | Frontier models plus local models via Ollama | Cost, latency, or privacy pressure justifies a mixed-model stack |
| Governance infrastructure | Centralized MCP broker, prompt library, policy engine | Many agents need shared tools and policy guardrails |

### Advanced failure modes

As the system becomes more autonomous, watch for:

- Context degradation: agents forget important repo details when prompts become too large
- Cascading hallucination: one bad architectural assumption propagates through the whole pipeline
- Permission blast radius: agents with broad cloud or data access can do real damage quickly

The fixes are boring and structural: smaller tasks, stronger contracts, better retrieval, stricter permissions, and explicit review gates.

---

## Further Reading

### Specifications

- [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [DORA Metrics Guide](https://dora.dev/guides/dora-metrics/)
- [Git Hooks Documentation](https://git-scm.com/docs/githooks)

### Foundational Texts

- [The Twelve-Factor App](https://12factor.net/) — methodology for building modern applications
- [GitHub Flow](https://docs.github.com/en/get-started/using-git/github-flow) — lightweight branching model

### Agentic Engineering

- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices) — Anthropic's guide to agentic coding
- [Agentic Coding Handbook: TDD Workflow](https://tweag.github.io/agentic-coding-handbook/WORKFLOW_TDD/) — test-driven development with agents
- [Guardrails for Agentic Coding](https://jvaneyck.wordpress.com/2026/02/22/guardrails-for-agentic-coding-how-to-move-up-the-ladder-without-lowering-your-bar/) — structural safety patterns

### Testing

- [Hypothesis (Property-Based Testing for Python)](https://hypothesis.readthedocs.io/)
- [mutmut (Mutation Testing for Python)](https://mutmut.readthedocs.io/)

### CI/CD

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Branch Protection Rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-a-branch-protection-rule)
