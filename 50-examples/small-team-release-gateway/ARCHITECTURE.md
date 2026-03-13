# ARCHITECTURE.md

## System Overview

The repo contains a small Python service that evaluates release requests and returns the controls required to ship them.

## Components

- `release_gateway.models`: request and response data structures
- `release_gateway.service`: release-planning logic
- `release_gateway.cli`: file-based interface for local and agent use
- `release_gateway.server`: HTTP interface for team or pipeline integration
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/smoke_test.py`: end-to-end HTTP sanity check
- `tests/`: unit and protocol behavior checks

## Data Flow

1. Read a release request from JSON or an HTTP POST body.
2. Validate it into a `ReleaseRequest`.
3. Build a `ReleasePlan`.
4. Return JSON that a human, CI job, or orchestrator can consume.

## Boundaries and Contracts

- Input contract: documented in `SCHEMA.md`
- Output contract: a JSON-friendly release plan
- Local quality gate: `scripts/run_quality_checks.py`
- Runtime interface: `POST /plan`

## Operational Constraints

- standard library only
- no network dependency for local development
- repo is optimized for a small team with independent review, staging, and release approval
- release decisions are advisory until enforced by surrounding process or automation

## Failure Domains

- invalid or incomplete release requests
- under-specified rollback plans
- missing ownership for risky changes
- drift between documented environments and release logic
- HTTP contract regressions that break pipeline integrations
