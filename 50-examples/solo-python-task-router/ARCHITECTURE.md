# ARCHITECTURE.md

## System Overview

The repo contains a small Python package that accepts a task spec and returns a workflow decision.

## Components

- `task_router.models`: input and output data structures
- `task_router.service`: decision logic
- `task_router.cli`: command-line interface
- `scripts/run_quality_checks.py`: local structural validation
- `tests/`: behavior checks

## Data Flow

1. Read task spec JSON from disk.
2. Validate it into a `TaskSpec`.
3. Build a `WorkflowDecision`.
4. Print JSON for human or agent consumption.

## Boundaries and Contracts

- Input contract: documented in `SCHEMA.md`
- Output contract: a JSON-friendly workflow decision
- Quality gate: `scripts/run_quality_checks.py`

## Operational Constraints

- standard library only
- no network dependency for local development
- repo is optimized for a solo workflow with independent review as a policy, not an automation service

## Failure Domains

- invalid task specs
- weak branch naming
- missing acceptance criteria
- under-specified workflow controls for high-risk work
