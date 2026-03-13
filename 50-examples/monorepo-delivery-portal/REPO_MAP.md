# REPO_MAP.md

## Root Paths

- `apps/ops_portal/`: static portal app
- `services/delivery_api/`: backend service
- `packages/shared_contracts/`: shared schema package
- `scripts/`: repo-level automation
- `tests/`: repo-level checks
- `examples/`: fixture data

## Change Routing Rules

- UI-only work should stay in `apps/ops_portal/`
- API-only work should stay in `services/delivery_api/`
- schema changes start in `packages/shared_contracts/` and then propagate outward
- cross-surface changes must update all touched paths in one scoped task
