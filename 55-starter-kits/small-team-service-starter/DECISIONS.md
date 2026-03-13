# DECISIONS.md

## Durable Decisions

### D-001: Service And Release Logic Stay Deterministic

The same request should produce the same release plan.

### D-002: Production Changes Need Rollback Posture

Prod requests without rollback readiness are incomplete.
