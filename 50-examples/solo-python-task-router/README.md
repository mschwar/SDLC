# Solo Python Task Router

A minimal example repository that validates work specs and recommends the workflow controls they require.

This repo exists to demonstrate the vault in executable form:

- canonical docs
- local quality checks
- git hooks
- CI
- tests
- PR evidence structure

## Domain

The project accepts a task spec in JSON and returns a routing decision:

- which review roles should be involved
- which gates are required
- which release strategy should be used
- what evidence should be attached to the PR

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m task_router examples/low-risk-task.json --pretty
python -m task_router examples/high-risk-task.json --pretty
git config core.hooksPath .githooks
```

## Structure

- `AGENTS.md`: onboarding and working rules
- `ARCHITECTURE.md`: code and workflow structure
- `SCHEMA.md`: task spec contract
- `DECISIONS.md`: durable repo decisions
- `task_router/`: application code
- `tests/`: unit tests
- `scripts/run_quality_checks.py`: blocking local validation
- `.githooks/`: local automation
- `.github/workflows/ci.yml`: remote validation

## Example Inputs

- `examples/low-risk-task.json`
- `examples/high-risk-task.json`

## Definition of Done

A change is done when:

- `python scripts/run_quality_checks.py` passes
- scope matches the objective
- docs are updated if behavior changed
- PR evidence is attached when relevant
