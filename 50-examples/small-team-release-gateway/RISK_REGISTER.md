# RISK_REGISTER.md

## Active Risks

| ID | Risk | Impact | Mitigation |
|----|------|--------|------------|
| R-001 | release rules drift from documented process | medium | keep docs in the required files list and test representative requests |
| R-002 | production changes are accepted without rollback posture | high | block production requests when `rollback_ready` is false |
| R-003 | HTTP contract changes break automation | medium | keep HTTP tests and smoke test in the quality loop |
| R-004 | ownership is unclear on high-risk work | high | require `owner` and CODEOWNERS review |
