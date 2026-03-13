# AUDIT_LOG_POLICY.md

## Audit Rules

- every recorded event must include actor, action, time, and hashed payload
- events are append-only
- each event references the previous event hash
- chain verification must pass in local quality checks

## Retention

- internal changes: 1 year
- confidential changes: 3 years
- restricted changes: 7 years

## Review Expectations

- audit breaks are treated as blocking issues
- replayable examples must exist for representative risky changes
