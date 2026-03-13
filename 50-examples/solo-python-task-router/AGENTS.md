# AGENTS.md

## Mission

This repo validates task specifications and recommends workflow controls for a small agent-first development flow.

## Canonical Notes

- `AGENTS.md`
- `ARCHITECTURE.md`
- `SCHEMA.md`
- `DECISIONS.md`

## Working Rules

- Branch from `origin/main`
- One branch per task
- Use conventional commits
- Run `python scripts/run_quality_checks.py` before commit
- Keep changes scoped to the stated objective

## Definition of Done

- Quality checks pass
- Tests cover the changed behavior
- Scope matches the task
- Documentation changes land with behavior changes

## Expected Commands

- `python scripts/run_quality_checks.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python -m task_router examples/low-risk-task.json --pretty`

## Hooks

Activate hooks once per clone:

```bash
git config core.hooksPath .githooks
```
