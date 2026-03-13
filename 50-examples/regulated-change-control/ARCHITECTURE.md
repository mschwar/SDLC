# ARCHITECTURE.md

## System Overview

The repo contains a small Python package that evaluates a regulated change request and produces a control packet plus an append-only audit event.

## Components

- `change_control.models`: request, packet, and audit data structures
- `change_control.service`: deterministic control-planning logic
- `change_control.audit`: tamper-evident audit-log storage and verification
- `change_control.cli`: command-line interface for planning and recording
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/audit_smoke.py`: end-to-end audit sanity check
- `tests/`: behavior and audit-chain checks

## Data Flow

1. Read a change request from JSON.
2. Validate it into a `ChangeRequest`.
3. Build a `ControlPacket`.
4. Optionally record an `AuditEvent` in the local audit store.
5. Return JSON that humans or automation can consume.

## Boundaries and Contracts

- input contract: documented in `SCHEMA.md`
- output contract: a JSON-friendly control packet
- audit contract: tamper-evident chained events
- quality gate: `scripts/run_quality_checks.py`

## Operational Constraints

- standard library only
- no network dependency for local development
- repo is optimized for regulated workflows where separation of duties matters
- planning logic is advisory until enforced by the surrounding release process

## Failure Domains

- incomplete change requests
- policy drift between docs and rules
- missing rollback posture for production changes
- restricted data changes routed without the proper approvers
- audit log corruption or chain breaks
