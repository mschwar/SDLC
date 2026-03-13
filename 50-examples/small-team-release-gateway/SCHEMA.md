# SCHEMA.md

## Release Request

Required fields:

- `service`: service name
- `objective`: short description of the change
- `branch`: branch name for the work
- `owner`: primary team or service owner
- `environment`: target environment, one of `dev`, `staging`, `prod`
- `change_type`: one of `docs`, `feature`, `bugfix`, `schema`, `infrastructure`
- `acceptance_criteria`: non-empty list of completion checks

Optional fields:

- `risk_level`: `low`, `medium`, or `high`
- `customer_visible`: boolean
- `touches_auth`: boolean
- `touches_schema`: boolean
- `requires_migration`: boolean
- `rollback_ready`: boolean
- `needs_data_review`: boolean
- `evidence`: list of evidence items already attached

## Release Plan

Returned fields:

- `service`
- `review_roles`
- `required_gates`
- `allowed_environments`
- `rollout_strategy`
- `required_evidence`
- `blocking_issues`
- `summary`

## Validation Rules

- branch names must be slash-delimited and contain no spaces
- acceptance criteria must not be empty
- production requests must declare `rollback_ready`
- risky schema or auth changes must carry matching gates in the output plan
