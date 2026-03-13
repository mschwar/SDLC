# SCHEMA.md

## Task Spec

Input JSON shape:

```json
{
  "objective": "string",
  "branch": "string",
  "acceptance_criteria": ["string"],
  "risk_level": "low | medium | high",
  "touches_schema": false,
  "touches_auth": false,
  "needs_production_access": false,
  "requires_ui_validation": false,
  "tags": ["string"]
}
```

## Rules

- `objective` must be non-empty
- `branch` must be non-empty and contain no spaces
- `acceptance_criteria` must contain at least one non-empty entry
- `risk_level` must be `low`, `medium`, or `high`
- optional flags default to `false`

## Workflow Decision Output

```json
{
  "review_roles": ["reviewer"],
  "required_gates": [],
  "local_checks": ["python scripts/run_quality_checks.py"],
  "release_strategy": "merge-to-main",
  "notes": ["string"]
}
```
