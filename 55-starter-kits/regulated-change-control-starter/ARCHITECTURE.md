# ARCHITECTURE.md

## System Overview

Replace this with the smallest accurate description of your regulated workflow.

## Components

- `control_app.models`: request, plan, and audit structures
- `control_app.service`: control-planning logic
- `control_app.audit`: append-only audit storage and verification
- `scripts/run_quality_checks.py`: blocking local validation
- `scripts/audit_smoke.py`: end-to-end audit sanity check
