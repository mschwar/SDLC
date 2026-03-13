# Small Team Release Gateway

A standard-library Python service that accepts a release request and returns the controls required to ship it safely.

This example demonstrates the vault in a more operational setting than the solo repo:

- canonical repo docs
- ownership and risk artifacts
- local quality checks
- git hooks
- CI
- tests
- an HTTP endpoint
- release-aware decision logic

## Domain

The project accepts a release request in JSON and returns a release plan:

- which reviewers must approve
- which gates block deployment
- which rollout strategy applies
- which environments are allowed
- which evidence is required before merge or release

## Quick Start

```bash
python scripts/run_quality_checks.py
python -m release_gateway plan examples/low-risk-request.json --pretty
python -m release_gateway plan examples/high-risk-request.json --pretty
python scripts/smoke_test.py
git config core.hooksPath .githooks
```

## Structure

- `AGENTS.md`: onboarding and working rules
- `ARCHITECTURE.md`: system and operational structure
- `SCHEMA.md`: request and response contracts
- `DECISIONS.md`: durable repo decisions
- `ROADMAP.md`: current delivery plan
- `RISK_REGISTER.md`: explicit operating risks
- `ENVIRONMENTS.md`: release environment policy
- `SLOS.md`: service-level targets and alerts
- `THREAT_MODEL.md`: primary trust boundaries and abuse cases
- `CODEOWNERS`: review ownership
- `release_gateway/`: application code
- `tests/`: unit and HTTP behavior checks
- `scripts/`: quality and smoke validation
- `.githooks/`: local automation
- `.github/workflows/ci.yml`: remote validation

## Example Inputs

- `examples/low-risk-request.json`
- `examples/high-risk-request.json`

## Definition of Done

A change is done when:

- `python scripts/run_quality_checks.py` passes
- the relevant example inputs still validate
- risk and operational docs are updated when controls change
- the PR includes evidence for tests, rollout, and rollback
