# AGENTS

This file is the single onboarding document for this repository.

Read it first. Use the rest of `docs/` on demand for domain-specific policy, schema, product, and architecture detail. Historical workflow ceremony now lives under `docs/archive/`.

## Mission

Build and maintain a personal evidence system that:
1. preserves verified professional facts in a structured ledger,
2. generates CVs, resumes, bios, and application materials from those facts,
3. automatically discovers relevant job listings and prepares ready-to-submit application directories.

The user acts as "hands" — agents prepare everything, the user reviews and submits.

## Current State

As of 2026-03-10:

- **Build phase (Gates 1-22)**: Complete. Core infrastructure, ledger, products, and QA are operational.
- **Phase 4 (Gates 23-28)**: Completed. Product inventory, chronology repair, targeted evidence acquisition, private-sidecar boundary, agent access surface, and phase closeout are all landed.
- **Phase 5 (Pipeline)**: Completed. Employer registry, crawler, screening, application builder, manifests, integration test, and pipeline QA are operational.
- **Phase 6**: In progress. Gates 33-35 are complete; Gates 36-37 remain pending.
- **Workflow modernization**: Complete. `AGENTS.md` is the canonical onboarding and workflow contract; historical ceremony docs are archived for reference.
- **Ledger**: 43 verified entries across 13 types. 0 non-verified entries. 0 entries missing primary evidence.
- **Products**: 5 families across CV, resumes, bios, references, and application materials. 6 product briefs.
- **QA**: Repository quality checks are enforced by git hooks when hooks are activated.

## Fast Onboarding

For the quickest safe orientation after this file, read:

1. `docs/artifacts/2026-03-10-gate27-agent-profile.md`
2. `docs/artifacts/2026-03-10-gate27-retrieval-surface.md`
3. `docs/artifacts/2026-03-10-open-risk-register.md`

These are routing aids, not canonical fact stores. Use them to choose the right ledger, product, workflow, or sidecar surface quickly.

## Core Model

The working lifecycle is:

`raw artifact -> normalized text -> ledger entry -> rendered product`

For the pipeline extension:

`employer registry -> crawler -> LLM screening -> ingestion -> application directory -> user applies`

### Layer Roles

- `corpus/raw/` — Immutable originals. Do not edit.
- `corpus/normalized/` — Generated derived text. Replaceable.
- `entries/` and `indexes/` — Curated structured facts. The main reusable knowledge layer.
- `products/` — CVs, resumes, bios, applications generated from ledger and briefs.
- `pipeline/` — Automated job search infrastructure.

## Canonical Rules

1. **Entries are canonical, not documents.** The ledger entry is the system of record. Products are views.
2. **Raw artifacts are immutable.** Never edit `corpus/raw/` after ingestion.
3. **Normalized text is replaceable.** OCR and markdown conversions can be regenerated.
4. **Products are views, not sources.** A rendered resume must not become the only place a fact lives.
5. **Verified-first rendering.** Products default to `verification.state = verified` entries.
6. **JSONL for operational manifests.** Append-only, one record per line (D-0009).
7. **No fabrication.** Never invent resume content, cover-letter claims, or evidence not in the ledger.
8. **No auto-submission.** The pipeline prepares applications; the user submits.

## Allowed Direct Edits

Agents may directly edit:

- `docs/`
- `schema/`
- `catalog/`
- `templates/`
- `scripts/`
- `entries/`
- `indexes/`
- `pipeline/`
- product source files in `products/*/source/` or `products/*/briefs/`

Agents should not directly edit:

- `corpus/raw/`
- generated outputs in `corpus/normalized/`
- rendered deliverables in `products/*/rendered/` except to replace them intentionally

## Required Behavior

### When working from a scoped prompt

1. Stay inside the stated scope.
2. Branch from `origin/main`, not local `main`.
3. Use a separate worktree or clone if multiple PRs are active.
4. Compare cleanliness against `origin/main`.
5. Run the validation named in the task before reporting completion.
6. Disclose validation side effects on tracked files.
7. Do not broaden scope because an adjacent cleanup looks easy.
8. If the work exposes a durable workflow lesson, report it so standing docs can be updated.

### When adding new material

1. Put new unprocessed material in `inbox/`.
2. Preserve the original as a raw artifact.
3. Generate normalized text separately.
4. Create or update ledger entries only after evidence is identified.

### When creating or editing ledger entries

1. Every meaningful claim must cite evidence.
2. Use `schema/ledger-entry.schema.json`.
3. If evidence is weak, mark verification accordingly. Do not overstate certainty.
4. Prefer one entry per reusable fact object.

### When generating products

1. Start from a product brief or explicit task.
2. Pull from ledger entries, not legacy folders.
3. Respect visibility and redaction requirements from `docs/SECURITY.md`.
4. Keep product regeneration markdown-first (D-0028).

### When working on the pipeline

1. Follow `docs/PRD-AUTOSEARCH.md` as the specification.
2. Keep all pipeline state in `pipeline/`.
3. Use environment variables for API keys and credentials, never tracked files.
4. Log crawl runs, screening decisions, and build actions to JSONL manifests.
5. Respect `robots.txt` and configured rate limits.
6. If the crawler or screener fails, log the failure and continue.
7. Prefer dry-run or temp-root validation that does not mutate tracked runtime history.

### When deduping or migrating

1. Do not delete legacy material just because it looks duplicated.
2. Record dedupe decisions in manifests or decision docs.
3. Preserve provenance from old paths to new paths.

## Workflow

- PR-first rule: no direct agent work lands on `main`.
- One task maps to one branch and one PR by default.
- Always branch from `origin/main`.
- If parallel work is active, use separate `git worktree` directories or separate clones.
- Keep the diff scoped to the task; do not bundle unrelated cleanup.
- Treat the prompt as the scope contract.
- Validation must be run before handoff or PR creation.
- Review is findings-first; summaries do not replace diff review.
- Delivery is not complete until the PR is reviewed and merged.
- **Artifacts & Reflections**:
    - `docs/artifacts/` is the active working area for current phase artifacts, onboarding aids, and the risk register.
    - `docs/archive/artifacts/` is for completed historical artifacts.
    - Gate reflections are still required for formal closeout; keep them with the gate artifacts and archive them once the gate is complete.
- Historical ceremony docs live in `docs/archive/ceremony/` and archived task packets live in `docs/archive/handoffs/`.

## Delegation

Lead and worker roles are simple:
- The lead scopes, routes, reviews, and decides acceptance.
- Workers execute bounded tasks, validate them, and return proof.
- The user launches the agent and remains in control of final submission and git publication.

Intelligence levels:

| Level | Meaning | Typical work |
|---|---|---|
| `L1` | Mechanical | Path cleanup, boilerplate docs, deterministic regeneration, low-risk file moves |
| `L2` | Applied engineering | Scripts, refactors, validation wiring, schema-constrained transforms |
| `L3` | Judgment engineering | Prompt design, screening rubrics, ambiguous mapping decisions, nuanced review |
| `L4` | Strategic | Architecture, policy boundaries, sequencing, conflict resolution |

Model routing:

| Model | Best use | Avoid as primary owner when |
|---|---|---|
| `codex` | Repo-local implementation, refactors, validation, CLI-heavy work, code review | the task is mostly strategic synthesis or prompt-policy judgment |
| `claude` | High-judgment reasoning, prompt design, nuanced review, writing-sensitive tasks | the task is mostly mechanical repo surgery |
| `gemini` | Large-context synthesis, planning, comparison across docs | the task needs heavy local implementation iteration |
| `opencode:<model>` | Targeted use of a known OpenRouter model for a specific tradeoff | the model choice is vague or unjustified |
| `local:<model>` | Cheap drafting, classification, low-risk summarization | correctness is high-stakes or the task changes core schemas |

Non-negotiables:
- Branch from `origin/main`, not local `main`.
- Use worktrees for concurrent PRs.
- Compare cleanliness against `origin/main`.
- The worker does not self-approve.
- Durable workflow changes belong in docs, not only in chat.

## Pull Requests

- Default to a Draft PR first.
- The comparison base is always `origin/main`.
- Before claiming readiness, check:

```bash
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git log --oneline origin/main..HEAD
git diff --stat origin/main..HEAD
git status --short
```

Clean branch checklist:
- scope matches the task
- branch started from `origin/main`
- diff contains only in-scope files
- validation is complete
- validation side effects are disclosed
- no forbidden paths were edited
- PR body matches the actual diff

## Git Hooks

`.githooks/` contains `pre-commit`, `commit-msg`, `post-commit`, `pre-push`, and `post-merge`.

Activate the hooks with:

```bash
git config core.hooksPath .githooks
```

The `pre-commit` hook runs repository quality checks automatically. Once hooks are activated, agents do not need separate reminder rules to run the full QA suite before every commit.

## Expected Commands

```bash
# Rewrite the ledger index to match current entries
python scripts/check_ledger_index.py --write

# Lint product briefs
python scripts/lint_product_briefs.py

# Report entry gaps
python scripts/report_entry_gaps.py
```

## Definition of Done

A task is done when:

1. Deliverables exist in the correct paths.
2. The scoped validation has passed.
3. Git hooks pass on commit when hooks are activated.
4. Any required doc or manifest updates are included.
5. The PR is reviewed and merged.

## Session-End

Before ending a session:

1. Ensure no partially written files are left behind.
2. Summarize what changed, what remains, and any validation side effects.
3. Do not leave hidden assumptions unstated if they affect review.

## Safety Defaults

1. Default unknown material to `internal` visibility.
2. Treat recommendation letters, transcripts, contracts, and sensitive business documents as higher sensitivity.
3. Prefer under-sharing to over-sharing.
4. Do not store API keys, credentials, or PII in tracked files.

## Escalation Rules

Stop and ask for clarification only when:

- two canonical candidates conflict and a judgment call would be risky,
- a requested move or deletion would destroy provenance,
- the sensitivity of a document is unclear and publication risk is real,
- a schema or architectural change would invalidate earlier work.

Otherwise, make reasonable progress and file the decision.
