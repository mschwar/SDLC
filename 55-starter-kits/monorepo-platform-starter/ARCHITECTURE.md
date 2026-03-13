# ARCHITECTURE.md

## System Overview

Replace this with the smallest accurate description of your monorepo surfaces.

## Components

- `packages/contracts/contracts.models`: shared contract structures
- `services/api_service/api_service.service`: API logic
- `services/api_service/api_service.server`: HTTP and static serving
- `apps/web_portal/`: static frontend assets
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/e2e_smoke.py`: end-to-end sanity check
