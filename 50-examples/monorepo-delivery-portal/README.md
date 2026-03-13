# Monorepo Delivery Portal

A standard-library monorepo that serves a small delivery dashboard from a Python API and a static portal app, with shared contracts across both surfaces.

This example demonstrates the vault in a multi-surface repository:

- canonical repo docs
- repo and ownership maps
- shared contract package
- API service
- static frontend app
- local quality checks
- git hooks
- CI
- tests

## Domain

The repo presents delivery work items to a dashboard:

- the shared contract defines the work-item and summary schema
- the API service loads work items and exposes JSON endpoints
- the portal app renders the summary and item list from the API

## Quick Start

```bash
python scripts/run_quality_checks.py
python scripts/dev_server.py
python scripts/e2e_smoke.py
git config core.hooksPath .githooks
```

## Structure

- `AGENTS.md`: onboarding and working rules
- `ARCHITECTURE.md`: system and boundary structure
- `SCHEMA.md`: shared contract for work items and summary payloads
- `DECISIONS.md`: durable repo decisions
- `REPO_MAP.md`: package and path map
- `OWNERSHIP_MAP.md`: path ownership boundaries
- `ENVIRONMENTS.md`: local, staging, and production policy
- `QA_STRATEGY.md`: unit, HTTP, and static-surface coverage
- `apps/ops_portal/`: static frontend assets
- `services/delivery_api/`: API service package
- `packages/shared_contracts/`: shared schema package
- `tests/`: contract, service, and HTTP checks
- `scripts/`: quality, dev-server, and smoke scripts
- `.githooks/`: local automation
- `.github/workflows/ci.yml`: remote validation

## Example Inputs

- `examples/work-items.json`

## Definition of Done

A change is done when:

- `python scripts/run_quality_checks.py` passes
- shared contract changes update both service and UI touchpoints
- repo map and ownership docs stay accurate when boundaries move
- the PR states which surface areas were changed
