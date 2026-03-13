# ARCHITECTURE.md

## System Overview

The repo contains a static portal app, a Python API service, and a shared contracts package. The service exposes work-item data and summary metrics; the app consumes those endpoints.

## Components

- `packages/shared_contracts/shared_contracts.models`: shared work-item and summary structures
- `services/delivery_api/delivery_api.service`: load and summarize work items
- `services/delivery_api/delivery_api.server`: API and static-file server
- `apps/ops_portal/`: HTML, CSS, and JavaScript client
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/e2e_smoke.py`: end-to-end HTTP and static-surface sanity check
- `tests/`: contract, service, and HTTP behavior checks

## Data Flow

1. Load work items from `examples/work-items.json`.
2. Validate them through the shared contract package.
3. Build summary metrics in the API service.
4. Serve JSON endpoints and static assets.
5. Fetch and render dashboard data in the portal app.

## Boundaries and Contracts

- shared contract: documented in `SCHEMA.md`
- app boundary: `apps/ops_portal/`
- service boundary: `services/delivery_api/`
- package boundary: `packages/shared_contracts/`
- quality gate: `scripts/run_quality_checks.py`

## Operational Constraints

- standard library only
- no network dependency for local development
- monorepo tasks should stay path-scoped whenever possible
- cross-surface changes must keep contract, service, and UI behavior aligned

## Failure Domains

- contract drift between service and frontend
- accidental cross-path edits
- summary logic changes without UI updates
- static assets served incorrectly after API changes
