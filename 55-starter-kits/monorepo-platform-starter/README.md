# Monorepo Platform Starter

A starter repo for a monorepo with shared contracts, an API service, and a small static frontend.

Copy this kit when you want:

- explicit `apps/`, `services/`, and `packages/` boundaries
- a shared schema package
- path-aware ownership and repo maps
- fast local smoke coverage across multiple surfaces

## Replace First

- rename the app, service, and contracts packages
- rewrite `REPO_MAP.md` and `OWNERSHIP_MAP.md`
- replace the sample schema and fixtures
- update the static app to match your domain

## Quick Start

```bash
python scripts/run_quality_checks.py
python scripts/dev_server.py
python scripts/e2e_smoke.py
git config core.hooksPath .githooks
```
