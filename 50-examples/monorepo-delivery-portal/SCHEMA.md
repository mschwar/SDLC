# SCHEMA.md

## Work Item

Required fields:

- `id`
- `title`
- `owner`
- `area`
- `status`: one of `queued`, `in-review`, `blocked`, `ready`
- `risk_level`: one of `low`, `medium`, `high`

Optional fields:

- `has_runbook`: boolean
- `needs_migration`: boolean
- `deployment_target`: one of `none`, `staging`, `prod`

## Summary Payload

Returned fields:

- `total_items`
- `status_counts`
- `high_risk_count`
- `blocked_items`
- `runbook_gaps`

## Validation Rules

- `id`, `title`, `owner`, and `area` must be non-empty strings
- status and risk level must be from the allowed sets
- blocked items should surface in `blocked_items`
- high-risk items missing a runbook should surface in `runbook_gaps`
