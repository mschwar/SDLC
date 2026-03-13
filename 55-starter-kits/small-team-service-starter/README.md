# Small Team Service Starter

A starter repo for a Python service owned by a small team.

Copy this kit when you want:

- release-aware service docs
- a local and CI quality loop
- an HTTP surface with a smoke test
- room for ownership and runtime controls

## Replace First

- rename `service_app/`
- rewrite the request schema and output contract
- update environments, SLOs, and risk register
- replace the sample fixtures with real cases

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m service_app plan examples/low-risk-request.json --pretty
python scripts/smoke_test.py
git config core.hooksPath .githooks
```
