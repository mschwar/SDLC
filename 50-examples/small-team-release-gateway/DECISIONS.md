# DECISIONS.md

## Durable Decisions

### D-001: Standard Library Only

The example uses only the Python standard library so it can run anywhere the vault is cloned.

### D-002: JSON As The Interface Contract

Both CLI and HTTP paths use the same JSON contract so local and automated flows stay aligned.

### D-003: Release Plans Are Deterministic

The service is rule-based, not probabilistic. The same request must always produce the same plan.

### D-004: Production Changes Need Explicit Rollback Readiness

Any request targeting production must state whether rollback is ready because release advice without rollback posture is incomplete.

### D-005: Operational Docs Are Part Of The Product Surface

`ENVIRONMENTS.md`, `SLOS.md`, `RISK_REGISTER.md`, and `THREAT_MODEL.md` are treated as first-class artifacts, not optional documentation.
