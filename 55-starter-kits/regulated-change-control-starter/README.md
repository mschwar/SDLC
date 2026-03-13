# Regulated Change Control Starter

A starter repo for regulated workflows with approval boundaries, audit evidence, and explicit data-handling rules.

Copy this kit when you want:

- control docs to be first-class artifacts
- deterministic planning logic
- a local audit trail with chain verification
- stronger human approval boundaries

## Replace First

- rename `control_app/`
- rewrite control objectives and approval matrix
- align data classes and retention rules with real obligations
- replace the sample fixtures and audit wording

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m control_app plan examples/high-risk-change.json --pretty
python -m control_app record examples/high-risk-change.json --actor reviewer --action plan-generated
git config core.hooksPath .githooks
```
