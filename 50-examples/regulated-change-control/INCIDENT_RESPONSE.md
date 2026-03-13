# INCIDENT_RESPONSE.md

## Incident

### Summary

Use this path when audit evidence is missing, a restricted-data change is misrouted, or a production control fails.

### Severity

- Sev 1: restricted-data exposure or broken production control
- Sev 2: audit-chain corruption without known exposure
- Sev 3: documentation or evidence gap without active risk

### Detection

- quality-check failure
- audit verification failure
- review escalation

### Containment

- stop release
- preserve current audit store
- open incident record

### Mitigation

- restore approved controls
- regenerate or recover evidence where possible
- escalate to compliance if data handling is in doubt

### Recovery

- verify chain integrity
- rerun quality checks
- re-approve the change if required

### Follow-up

- update controls, docs, and tests
- record a postmortem
