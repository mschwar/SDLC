# Solo Python Starter

A small starter repo for a solo or tightly scoped agent workflow.

Copy this kit when you want:

- a simple Python package
- blocking local quality checks
- CI parity
- draft-PR-friendly repo structure

## Replace First

- rename `app/`
- rewrite `SCHEMA.md` for your real input contract
- replace `examples/sample-input.json`
- update repo mission and done criteria

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m app examples/sample-input.json --pretty
git config core.hooksPath .githooks
```
