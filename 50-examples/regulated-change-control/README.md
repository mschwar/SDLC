# Regulated Change Control

A standard-library Python project that accepts a change request and returns the approvals, controls, evidence, and audit posture required to move the change safely through a regulated workflow.

This example demonstrates the vault in a higher-control setting:

- canonical repo docs
- approval and separation-of-duties artifacts
- sandbox and data-classification policy
- append-only audit evidence
- local quality checks
- git hooks
- CI
- tests

## Domain

The project accepts a change request in JSON and returns a control packet:

- which approvers are required
- which controls must be satisfied
- which sandbox tier applies
- which evidence must exist before release
- which issues block the change

It can also record a tamper-evident audit event for that packet.

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m change_control plan examples/low-risk-change.json --pretty
python -m change_control plan examples/high-risk-change.json --pretty
python -m change_control record examples/high-risk-change.json --actor compliance-worker --action plan-generated
python scripts/audit_smoke.py
git config core.hooksPath .githooks
```

## Structure

- `AGENTS.md`: onboarding and working rules
- `ARCHITECTURE.md`: system and control structure
- `SCHEMA.md`: request, packet, and audit contracts
- `DECISIONS.md`: durable repo decisions
- `CONTROL_OBJECTIVES.md`: the controls this repo is trying to satisfy
- `APPROVAL_MATRIX.md`: who must approve what
- `DATA_CLASSIFICATION.md`: data classes and allowed handling
- `SANDBOX_POLICY.md`: execution permissions and escalation rules
- `AUDIT_LOG_POLICY.md`: audit chain and retention rules
- `INCIDENT_RESPONSE.md`: failure and breach response path
- `CODEOWNERS`: ownership and review boundaries
- `change_control/`: application code
- `tests/`: service and audit behavior checks
- `scripts/`: quality and audit smoke validation
- `audit/`: local audit database location
- `.githooks/`: local automation
- `.github/workflows/ci.yml`: remote validation

## Example Inputs

- `examples/low-risk-change.json`
- `examples/high-risk-change.json`

## Definition of Done

A change is done when:

- `python scripts/run_quality_checks.py` passes
- audit-chain validation passes
- policy docs are updated if controls changed
- the PR includes evidence, approval impact, and rollback posture
