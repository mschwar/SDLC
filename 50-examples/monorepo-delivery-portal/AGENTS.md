# AGENTS.md

## Mission

This repo exposes delivery status through a static portal and a Python API while preserving clear package boundaries inside a monorepo.

## Canonical Notes

- `AGENTS.md`
- `ARCHITECTURE.md`
- `SCHEMA.md`
- `DECISIONS.md`
- `REPO_MAP.md`
- `OWNERSHIP_MAP.md`
- `ENVIRONMENTS.md`
- `QA_STRATEGY.md`

## Working Rules

- Branch from `origin/main`
- One branch per task
- Use conventional commits
- Run `python scripts/run_quality_checks.py` before commit
- Keep changes scoped to the relevant app, service, or package boundary
- Update repo and ownership maps when boundaries move

## Definition of Done

- Quality checks pass
- Tests cover the changed behavior
- Scope matches the task
- Docs change with boundary or behavior changes
- PR states which surfaces and paths were affected

## Expected Commands

- `python scripts/run_quality_checks.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/dev_server.py`
- `python scripts/e2e_smoke.py`

## Hooks

Activate hooks once per clone:

```bash
git config core.hooksPath .githooks
```
