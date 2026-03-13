# AGENTS.md

## Mission

This repo plans regulated software changes and records durable audit evidence for those plans.

## Canonical Notes

- `AGENTS.md`
- `ARCHITECTURE.md`
- `SCHEMA.md`
- `DECISIONS.md`
- `CONTROL_OBJECTIVES.md`
- `APPROVAL_MATRIX.md`
- `DATA_CLASSIFICATION.md`
- `SANDBOX_POLICY.md`
- `AUDIT_LOG_POLICY.md`
- `INCIDENT_RESPONSE.md`

## Working Rules

- Branch from `origin/main`
- One branch per task
- Use conventional commits
- Run `python scripts/run_quality_checks.py` before commit
- Update control docs when approval or evidence logic changes
- Keep changes scoped to one control objective or one implementation task

## Definition of Done

- Quality checks pass
- Tests cover the changed behavior
- Scope matches the task
- Control documentation changes land with behavior changes
- Review and release impact is stated in the PR

## Expected Commands

- `python scripts/run_quality_checks.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python -m change_control plan examples/low-risk-change.json --pretty`
- `python -m change_control record examples/high-risk-change.json --actor compliance-worker --action plan-generated`
- `python scripts/audit_smoke.py`

## Hooks

Activate hooks once per clone:

```bash
git config core.hooksPath .githooks
```
