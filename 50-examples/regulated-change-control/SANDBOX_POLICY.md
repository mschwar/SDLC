# SANDBOX_POLICY.md

## Read Permissions

- source repo
- local fixtures
- local audit database

## Write Permissions

- repo workspace
- local audit store under `audit/`
- temporary local test artifacts

## External Network Policy

- disabled by default for local development
- explicit human approval required for external transmission

## Approval Thresholds

- production-affecting changes require human approval
- restricted-data changes require privacy and compliance review
- irreversible actions require explicit escalation

## Forbidden Actions

- sending restricted data to unapproved external tools
- modifying audit records in place
- bypassing approval requirements by reclassifying data without doc changes

## Escalation Path

- worker -> reviewer -> service-owner -> compliance-officer
