# SCHEMA.md

## Change Request

Required fields:

- `system`: system or service name
- `objective`: short description of the change
- `branch`: branch name for the work
- `owner`: accountable owner or team
- `target_environment`: one of `dev`, `staging`, `prod`
- `change_type`: one of `code`, `schema`, `config`, `access`, `policy`
- `data_class`: one of `internal`, `confidential`, `restricted`
- `acceptance_criteria`: non-empty list of completion checks

Optional fields:

- `risk_level`: `low`, `medium`, or `high`
- `touches_sensitive_data`: boolean
- `changes_policy`: boolean
- `vendor_impact`: boolean
- `rollback_ready`: boolean
- `evidence`: list of evidence items already attached

## Control Packet

Returned fields:

- `system`
- `approvers`
- `required_controls`
- `sandbox_tier`
- `required_evidence`
- `retention_class`
- `blocking_issues`
- `summary`

## Audit Event

Recorded fields:

- `event_index`
- `recorded_at`
- `actor`
- `action`
- `system`
- `payload_hash`
- `previous_hash`
- `chain_hash`

## Validation Rules

- branch names must be slash-delimited and contain no spaces
- acceptance criteria must not be empty
- production requests must declare `rollback_ready`
- restricted data or policy changes must produce stronger approver and control sets
