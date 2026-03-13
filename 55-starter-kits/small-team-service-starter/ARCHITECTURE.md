# ARCHITECTURE.md

## System Overview

Replace this with the smallest accurate description of your service.

## Components

- `service_app.models`: request and response structures
- `service_app.service`: release or workflow logic
- `service_app.server`: HTTP interface
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/smoke_test.py`: end-to-end sanity check
