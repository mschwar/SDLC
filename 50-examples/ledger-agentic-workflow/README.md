# Ledger

A personal evidence system that preserves verified professional facts and generates CVs, resumes, bios, and application materials on demand. An automated job-search pipeline discovers relevant listings and prepares ready-to-submit application directories.

## Quick Start

```bash
# Activate repo hooks
git config core.hooksPath .githooks

# Add a target employer (Phase 5A foundation)
python scripts/add_employer.py --name "Broad Institute" --url "https://broadinstitute.wd1.myworkdayjobs.com"

# Crawl enabled employer portals (Phase 5A foundation)
python pipeline/crawler/crawl_portals.py --dry-run
```

## Onboarding

New agents should read these files in order:

1. `AGENTS.md` — canonical onboarding, workflow, delegation, PR, and edit rules
2. `docs/ARCHITECTURE.md` — layer model, directory roles, data flow
3. `docs/SCHEMA.md` — data models for entries, artifacts, briefs, provenance
4. `docs/PRD-AUTOSEARCH.md` — automated job search pipeline specification
5. `ROADMAP.md` — phased plan with exit criteria
6. `BACKLOG.md` — prioritized implementation tasks
7. `RUNBOOK.md` — operating and recovery reference

For fast orientation after `AGENTS.md`, use:

- `docs/artifacts/2026-03-10-gate27-agent-profile.md`
- `docs/artifacts/2026-03-10-gate27-retrieval-surface.md`
- `docs/artifacts/2026-03-10-open-risk-register.md`

## Canonical Layers

| Layer | Path | Role |
|---|---|---|
| Ledger entries | `entries/` | One structured fact per file — the system of record |
| Indexes | `indexes/` | Derived rollups over entries |
| Products | `products/` | Rendered CVs, resumes, bios, applications |
| Pipeline | `pipeline/` | Automated job search and application prep (Phase 5) |
| Corpus | `corpus/raw/`, `corpus/normalized/` | Preserved originals and derived text |
| Scripts | `scripts/` | Validation, reporting, ingestion automation |
| Docs | `docs/` | Operating docs, roadmaps, decisions, gate artifacts |

Live contact records, outreach status, and credential-assembly notes do not belong in the tracked repo. Keep that mutable workflow state in a sibling private sidecar workspace named `ledger-sidecar/`, or point `LEDGER_SIDECAR_ROOT` at an equivalent location outside the repo. Secrets such as API keys and passwords stay in environment variables rather than in repo files or sidecar notes.

## Operating Docs

| Doc | Purpose |
|---|---|
| `docs/ARCHITECTURE.md` | Layer model and directory roles |
| `docs/SCHEMA.md` | Data models and field definitions |
| `docs/PRODUCTS.md` | Product families and rendering policy |
| `docs/NAMING.md` | Naming and path conventions |
| `docs/INGESTION.md` | Evidence ingestion workflow |
| `docs/PROVENANCE.md` | Provenance and verification rules |
| `docs/SECURITY.md` | Privacy and sensitivity policy |
| `docs/DECISIONS.md` | 30 architectural decisions |
| `AGENTS.md` | Canonical workflow, delegation, PR, hook, and edit contract |
| `docs/PRD-AUTOSEARCH.md` | Automated pipeline PRD |
| `docs/archive/ceremony/` | Archived workflow and gate-ceremony history |

## Workflow

Use the repo as a prompt-driven, PR-first system:

1. Scope one bounded task per branch.
2. Branch from `origin/main`.
3. Use a separate worktree for parallel work.
4. Have the worker follow `AGENTS.md` and the task prompt.
5. Return branch proof plus validation evidence.
6. Review the diff against `origin/main` before merge.
7. Archive historical task packets under `docs/archive/handoffs/` when they matter.

## Current State

- **43** verified ledger entries across 13 types
- **6** product briefs across 3 role families
- **5** product families: CV, resume (3 variants), bio (3 lengths), references, applications
- **21** validation/automation scripts
- **Phases 1-5** completed; **Phase 6** in progress (Gates 33-35 complete, Gates 36-37 pending)
- All QA checks passing
