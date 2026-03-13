# SCHEMA.md

## Change Request

Required fields:

- `objective`
- `branch`
- `target_environment`
- `data_class`
- `acceptance_criteria`

Optional fields:

- `risk_level`
- `touches_sensitive_data`
- `changes_policy`
- `rollback_ready`

## Control Plan

- `approvers`
- `required_controls`
- `sandbox_tier`
- `blocking_issues`

## Audit Event

- `event_index`
- `recorded_at`
- `actor`
- `action`
- `payload_hash`
- `previous_hash`
- `chain_hash`
