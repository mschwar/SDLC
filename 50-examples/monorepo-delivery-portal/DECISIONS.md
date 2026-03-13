# DECISIONS.md

## Durable Decisions

### D-001: Shared Contracts Live In Their Own Package

The app and service both depend on a single contract package so schema drift is harder to hide.

### D-002: The Service Serves Static Assets For Local Integration

The example serves the portal app directly from the API process to keep local setup simple while still demonstrating app/service boundaries.

### D-003: Monorepo Boundaries Must Be Explicit

Repo map and ownership map are required artifacts because monorepo confusion is often a retrieval and scoping problem before it becomes a code problem.

### D-004: Standard Library Only

The example uses only the Python standard library so it can run anywhere the vault is cloned.
