# THREAT_MODEL.md

## Trust Boundaries

- local developer machines
- CI runner
- HTTP clients that submit release requests

## Primary Abuse Cases

- malformed JSON causes server failure
- unowned high-risk change is routed without review
- production release is suggested without rollback readiness
- auth or schema changes bypass stronger gates

## Controls

- strict input validation
- deterministic planning logic
- ownership as a required field
- blocking issues in the response for unsafe requests
