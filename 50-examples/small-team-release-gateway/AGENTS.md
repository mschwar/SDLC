# AGENTS.md

## Mission

This repo determines how a small team should review, stage, and release changes to a deployed service.

## Canonical Notes

- `AGENTS.md`
- `ARCHITECTURE.md`
- `SCHEMA.md`
- `DECISIONS.md`
- `ENVIRONMENTS.md`
- `SLOS.md`
- `THREAT_MODEL.md`

## Working Rules

- Branch from `origin/main`
- One branch per task
- Use conventional commits
- Run `python scripts/run_quality_checks.py` before commit
- Update operating docs when release controls change
- Keep changes scoped to one operational objective

## Definition of Done

- Quality checks pass
- Tests cover the changed behavior
- Scope matches the task
- Documentation changes land with behavior changes
- Release and rollback impact is stated in the PR

## Expected Commands

- `python scripts/run_quality_checks.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python -m release_gateway plan examples/low-risk-request.json --pretty`
- `python scripts/smoke_test.py`

## Hooks

Activate hooks once per clone:

```bash
git config core.hooksPath .githooks
```
