---
tags:
  - examples
  - python
  - small-team
  - deployed-product
type: example
status: active
updated: 2026-03-10
---

# Small Team Release Gateway Example

> [!summary] Use
> This is a fully worked example repo for a small team that owns a deployed service.
> It extends the solo example with ownership, runtime controls, release gates, HTTP integration, and operational documents.

## Example Repo

- [[50-examples/small-team-release-gateway/README]]

## What It Demonstrates

- Layer 1: repo constitution plus service-level operating documents
- Layer 3: local quality enforcement and smoke validation
- Layer 5 and 6: stronger PR evidence, ownership, and independent review controls
- Layer 7: deployment-aware release planning, environment strategy, and SLO-driven operations

## Recommended Reading Path

1. [[50-examples/small-team-release-gateway/README]]
2. [[50-examples/small-team-release-gateway/AGENTS]]
3. [[50-examples/small-team-release-gateway/ARCHITECTURE]]
4. [[50-examples/small-team-release-gateway/scripts/run_quality_checks.py]]
5. [[50-examples/small-team-release-gateway/scripts/smoke_test.py]]
6. [[50-examples/small-team-release-gateway/.github/workflows/ci.yml]]

## Related Notes

- [[35-variants/Small Team Variant]]
- [[35-variants/Deployed Product Variant]]
- [[20-reference/Release Management]]
- [[20-reference/Service Ownership and Code Ownership]]
- [[20-reference/SLOs, SLIs, and Alerting]]
