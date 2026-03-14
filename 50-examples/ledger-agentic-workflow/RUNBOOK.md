# Runbook

How to operate, validate, extend, and recover this repository.

## Prerequisites

- Python 3.11+
- Git
- For pipeline (Phase 5): `httpx` or `requests`, `beautifulsoup4`, `anthropic` SDK

Install pipeline dependencies:
```bash
pip install httpx beautifulsoup4 anthropic pyyaml
```

## Running Validation

### Full QA suite

```bash
python scripts/run_quality_checks.py
```

This runs all standing checks:
- `check_ledger_index.py` — ledger/index consistency
- `lint_product_briefs.py` — brief structure validation
- `check_render_consistency.py` — source/rendered coverage
- `check_verified_render_inputs.py` — verified-first policy enforcement
- `check_product_language.py` — product quality checks
- `check_application_inventory.py` — application packet audit
- `report_entry_gaps.py` — non-verified entries, missing evidence, broken brief references

Run this before every commit and at every gate closeout.

## Private Sidecar Boundary

Use a sibling private workspace named `ledger-sidecar/` for live reference, outreach, and credential operations. Resolve it with `LEDGER_SIDECAR_ROOT` when set; otherwise treat it as a sibling of the canonical repo root rather than a child of the current checkout or `.worktrees/` directory.

Use the helper below when you need a safe path check or a bootstrap plan:

```bash
python scripts/sidecar_helper.py resolve
python scripts/sidecar_helper.py bootstrap --dry-run
python scripts/sidecar_helper.py validate --root /safe/scratch/ledger-sidecar
```

The helper fails closed if the resolved sidecar path is inside the tracked repo.

Keep in the tracked repo:
- reusable evidence-backed facts
- reference-lane guidance and application instructions
- rendered products that omit live contact and outreach state

Keep in the private sidecar:
- referee names, emails, phone numbers, and relationship notes
- outreach logs, follow-up dates, and response state
- private credential-packet assembly notes and interview logistics

Keep out of files entirely:
- API keys
- auth tokens
- passwords or secret reset links

## Fast Agent Orientation

When an agent needs the quickest safe path into the repo, read in this order:

1. `AGENTS.md`
2. `docs/artifacts/2026-03-10-gate27-agent-profile.md`
3. `docs/artifacts/2026-03-10-gate27-retrieval-surface.md`
4. `docs/artifacts/2026-03-10-open-risk-register.md`

Then branch by task:

- claim or evidence question -> `indexes/seed-ledger-index.json`, then `entries/`
- product or application work -> `products/` plus `docs/archive/artifacts/2026-03-10-gate23-application-workflow-memo.md`
- reference operations -> `products/references/` plus Gate 26 sidecar guidance
- dump mining request -> `docs/archive/artifacts/2026-03-10-gate27-dump-gem-target-map.md` before touching any archive cluster

## Delegating to Another Agent

Use this when the lead agent wants to assign bounded work to another model.

1. Read `AGENTS.md`, especially the `Workflow`, `Delegation`, and `Pull Requests` sections.
2. Choose the worker model and intelligence level using `AGENTS.md`.
3. Write a scoped launch prompt that names:
   - objective
   - base ref
   - branch name
   - allowed and blocked paths
   - validation commands
   - expected side effects
4. Launch the worker with that prompt.
5. For concurrent PRs, use separate worktrees or separate clones.
6. When the worker reports completion, review the diff against `origin/main`.

Required branch-proof commands for a worker completion report:

```bash
git rev-parse HEAD
git rev-parse origin/main
git log --oneline origin/main..HEAD
git diff --stat origin/main..HEAD
git status --short
```

Rule:
- workers execute
- the lead reviews and decides acceptance
- only the lead closes the handoff
- PR cleanliness is judged against `origin/main`
- validation should avoid dirtying tracked runtime logs unless explicitly in scope

### Launch Prompt Templates

Use these prompt shapes when launching or resuming worker tasks.

Fresh launch:

```text
Take ownership of `chore/<scope>`.
Read `AGENTS.md`.
Branch from `origin/main`, stay inside scope, run the required validation, and return the completion report with branch proof.
```

Resume an existing branch:

```text
Take ownership of `<branch-name>`.
Read `AGENTS.md`.
Continue from the current branch state, stay in scope, run the required validation, and return updated branch proof.
```

Fix review findings only:

```text
Take ownership of `<branch-name>`.
Fix the review findings only, do not broaden scope, rerun the handoff validation, and return updated branch proof.
```

Launch a closeout task after implementation is merged:

```text
Take ownership of `<branch-name>`.
Read `AGENTS.md` and `docs/archive/ceremony/GATE-CLOSEOUT.md`.
Base the work on current `origin/main`, follow the archived closeout protocol if needed, run validation, and return the completion report with branch proof.
```

Rule of thumb:
- use a scoped branch prompt for a clean start
- use `Take ownership of <branch>` only when work already exists on that branch and should continue there

### Lead Prompt Templates

Use these prompt shapes when you want the lead to scope work, draft handoffs, or design gates.

Scope the next wave:

```text
Act as lead. Inspect the current repo state, scope the next wave of work, and recommend the launch order.
```

Scope without file edits:

```text
Act as lead, but do not change files. Inspect the current repo state and recommend the next wave of work.
```

Draft worker prompt packets:

```text
Act as lead. Scope the next wave and write the worker launch prompts.
```

Draft a specific worker prompt:

```text
Act as lead. Write a worker launch prompt for <task>, including scope, allowed paths, validation, and reviewer focus.
```

Design a new gate:

```text
Act as lead. Propose the next gate for <topic>, with deliverables, exit criteria, closeout expectations, and suggested worker slices.
```

Update roadmap plus launch packet:

```text
Act as lead. Update the roadmap for the next phase or gate, then prepare the handoff packets needed to start it.
```

Queue cleanup:

```text
Act as lead. Reconcile the roadmap, active handoffs, and merged work. Then clean up the handoff queue and tell me what is still live.
```

## Reviewing A Returned Worker PR

Use this after a worker reports completion.

1. `git fetch origin`
2. inspect the branch proof the worker reported
3. verify `git log --oneline origin/main..HEAD`
4. verify `git diff --stat origin/main..HEAD`
5. read the PR body or packet and compare it to the actual diff
6. rerun the required validation for the risk level
7. decide accept, request correction, or reclaim the task

Review is findings-first. Do not accept a worker summary without checking the branch contents.

## Lead Review Loop

Use this exact loop after a worker finishes a handoff:

1. Get the worker's completion report and branch proof.
2. Have the lead or a fresh reviewer agent review the branch against `origin/main` and the handoff file.
3. Do not use the original worker as the approver of its own work.
4. After review, choose exactly one of:
   - `accept`: merge the branch, push `main`, then archive any durable task packet under `docs/archive/handoffs/` if one exists
   - `request correction`: send findings back to the worker on the same branch, have it fix only those findings, rerun validation, and report back for another review pass
   - `reclaim or split`: stop the current loop, take the work back, or issue a narrower follow-up handoff
5. Only after the accepted branch is merged should you launch or merge the next dependent handoff.

Useful prompt shapes:

```text
Review `branch-name` against `origin/main` and the scoped prompt. Findings first.
```

```text
Take ownership of `branch-name`, fix the review findings only, rerun the handoff validation, and return updated branch proof.
```

```text
Merge `branch-name` into `main`, push `main`, then archive any durable task packet under `docs/archive/handoffs/`.
```

### Dependent Handoffs

For dependent slices, accept and merge the upstream handoff before treating the downstream handoff as ready.

Example:
- review and merge `h5`
- then review `h6` against the now-current `origin/main`
- then launch `h7` only after `h6` is merged

If a downstream branch finished early, hold it, rebase or re-check it against the accepted upstream result, then review it.

## Closeout Notes

Use the lightest closeout that preserves the learning:

- routine PR: PR body plus review is enough
- workflow/process lesson: use `templates/success-friction-update.md` or update standing docs directly
- roadmap gate: follow `docs/archive/ceremony/GATE-CLOSEOUT.md`

### Individual checks

```bash
# Rewrite ledger index to match current entries
python scripts/check_ledger_index.py --write

# Lint briefs only
python scripts/lint_product_briefs.py

# Report gaps only
python scripts/report_entry_gaps.py
```

## Adding a Ledger Entry

1. Choose the entry type from `catalog/entry-types.yaml`.
2. Copy the template from `templates/ledger-entry.md`.
3. Fill in fields following `schema/ledger-entry.schema.json`.
4. Save to `entries/<entry_type>/<entry_id>.json`.
5. Update the index: `python scripts/check_ledger_index.py --write`.
6. Run QA: `python scripts/run_quality_checks.py`.

Entry ID pattern: `<entry_type>_<org_or_scope>_<slug>_<start_date_or_year>`

## Adding a Product Brief

1. Copy an existing brief from `products/applications/briefs/` as a template.
2. Update `brief_id`, `product_type`, `variant`, `audience`, `goal`, `tone`, `selection`.
3. Save to `products/applications/briefs/<brief_id>.json`.
4. Run: `python scripts/lint_product_briefs.py`.

## Rendering Products

Products are currently markdown-first and manually authored/edited (D-0028). The workflow is:

1. Start from a product brief or explicit task.
2. Pull content from verified ledger entries.
3. Write the source file in `products/<type>/source/`.
4. Write the rendered output in `products/<type>/rendered/`.
5. Run QA to verify consistency.

## Pipeline Operations (Phase 5A Foundation)

### Adding an employer

```bash
python scripts/add_employer.py \
  --name "Broad Institute" \
  --url "https://broadinstitute.wd1.myworkdayjobs.com" \
  --sector biotech \
  --portal-type workday \
  --search-terms "applied scientist,program manager,data scientist"
```

### Listing employers

```bash
python scripts/add_employer.py --list
```

### Running the crawler

```bash
python pipeline/crawler/crawl_portals.py --dry-run
```

Raw crawler hits are staged under `pipeline/crawler/staged-hits/` and are ignored by git.

### Running the screener

```bash
python pipeline/screening/screen_hits.py
```

### Pipeline integration test

```bash
python scripts/test_pipeline_e2e.py
```

This test exercises the Phase 5 pipeline end to end without mutating tracked runtime state:
- serves a synthetic local employer portal for the crawler
- runs the crawler in side-effect-safe temp space
- stages a synthetic hit and screens it with `--mock`
- processes the resulting ingestion file through the builder/watcher path
- verifies the generated application directory contains the required files
- confirms the ingestion file is cleaned up and tracked pipeline manifests/logs are unchanged

Use this when changing pipeline wiring, ingestion contracts, or application-directory generation behavior.

### Starting the ingestion watcher

```bash
python scripts/watch_ingestion.py
```

This polls `pipeline/ingestion/` and triggers application directory builds.

### Checking application status

Look at `pipeline/manifests/job-applications.jsonl` or check individual directories:
```bash
cat pipeline/jobs/*/status.json
```

### Applying for a job

1. Check `pipeline/notifications.md` or console output for new applications.
2. Open the application directory.
3. Read `application-instructions.md` — this is the playbook.
4. Review and personalize `resume.md` and `cover-letter.md`.
5. Open the application URL.
6. Submit.
7. Update `status.json`: `{ "state": "applied", "applied_date": "2026-03-09" }`.

Referee names, contact details, and outreach status for the live application should be maintained in the private sidecar rather than in the tracked job directory.

## Common Failure Modes

### QA checks fail after ledger changes

**Symptom**: `run_quality_checks.py` reports index drift or missing entries.
**Fix**: Run `python scripts/check_ledger_index.py --write` to resync the index, then rerun QA.

### Brief references nonexistent entry

**Symptom**: `lint_product_briefs.py` reports missing entry IDs.
**Fix**: Either create the missing entry or remove the reference from the brief.

### Verified-first check fails

**Symptom**: `check_verified_render_inputs.py` reports unverified entries in briefs/sources.
**Fix**: Either verify the entry (upgrade `verification.state`) or remove it from the brief/source.

### Crawler returns zero hits

**Symptom**: `crawl-runs.jsonl` shows a run with 0 hits for a previously active employer.
**Fix**: Check if the employer's portal URL changed. Update the registry. Check if `robots.txt` is blocking. Consider switching `scrape_strategy`.

### Crawler is blocked by robots.txt

**Symptom**: `crawl-runs.jsonl` shows employer status `blocked` with reason `robots.txt disallowed crawl`.
**Fix**: Do not work around the block in the current html-search flow. Leave the employer disabled, switch to a different approved portal URL if one exists, or defer that employer until a different allowed strategy is implemented.

### Screening rejects everything

**Symptom**: `screen-runs.jsonl` shows all `reject` verdicts.
**Fix**: Review `screen-config.yaml` thresholds. The `auto_pass_relevance` threshold may be too high, or `disqualifiers` may be too broad.

### Validation dirties tracked runtime logs

**Symptom**: A dry-run or structural test leaves diffs in tracked JSONL runtime logs such as crawler or screening run logs.
**Fix**: Prefer side-effect-safe dry-run modes, temp output paths, or explicit scratch outputs. If a tracked log must change for validation, say so in the handoff and in the completion report.

### Ingestion file not processed

**Symptom**: JSON file sits in `pipeline/ingestion/` without being picked up.
**Fix**: Check that `watch_ingestion.py` is running. Check the file matches the hot-folder JSON contract. Check `pipeline/manifests/pipeline-runs.jsonl` for error logs.

### Builder fails to match role family

**Symptom**: Application directory created with `status.json` showing `needs-review`.
**Fix**: The listing didn't match any existing product brief role family. Either create a new brief for this role type or manually assign the closest match.

## What to Update When

| Change | Update |
|---|---|
| New entry type | `catalog/entry-types.yaml`, `docs/SCHEMA.md` |
| New schema | `schema/`, `docs/SCHEMA.md` |
| New product family | `products/`, `docs/PRODUCTS.md`, `docs/ARCHITECTURE.md` |
| New script | `scripts/`, `scripts/README.md`, `RUNBOOK.md` |
| New delegation or workflow rule | `AGENTS.md`, `README.md`, `RUNBOOK.md` |
| Architectural decision | `docs/DECISIONS.md` |
| New gate completed | `ROADMAP.md`, relevant phase roadmap in `docs/`, reflection artifact |
| Pipeline config change | Relevant YAML in `pipeline/`, `RUNBOOK.md` if it changes operations |
| New employer | `pipeline/employers/employer-registry.jsonl` via helper script |

## Session-End Checklist

Before ending a work session:

- [ ] Run `python scripts/run_quality_checks.py` — all checks pass.
- [ ] No partially written or orphaned files left behind.
- [ ] If a gate was completed, consult `docs/archive/ceremony/GATE-CLOSEOUT.md` if historical closeout detail is needed.
- [ ] If the work exposed a durable workflow lesson, update standing docs or file a short closeout note.
- [ ] Summarize: what was done, what changed, what remains.
- [ ] Do not commit or push without user approval.

## Environment Variables (Phase 5)

When the pipeline is implemented, these will be needed:

```bash
# Required for LLM screening
ANTHROPIC_API_KEY=sk-ant-...

# Optional: custom user agent for crawler
LEDGER_CRAWLER_USER_AGENT="LedgerJobCrawler/1.0"
```

Never store these in tracked files. Use `.env` (which is in `.gitignore`) or system environment variables.
