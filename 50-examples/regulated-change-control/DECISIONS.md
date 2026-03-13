# DECISIONS.md

## Durable Decisions

### D-001: Standard Library Only

The example uses only the Python standard library so it can run anywhere the vault is cloned.

### D-002: Deterministic Control Planning

The same request must always produce the same control packet.

### D-003: Tamper-Evident Audit Trail

Audit events are hash-chained so local verification can detect breaks or edits.

### D-004: Policy Docs Are Part Of The Product Surface

`CONTROL_OBJECTIVES.md`, `APPROVAL_MATRIX.md`, `DATA_CLASSIFICATION.md`, `SANDBOX_POLICY.md`, and `AUDIT_LOG_POLICY.md` are required artifacts, not optional notes.

### D-005: Production Changes Need Explicit Rollback Posture

A regulated production change without rollback readiness is incomplete and must be blocked.
