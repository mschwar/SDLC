---
tags:
  - examples
  - python
  - monorepo
  - web-app
type: example
status: active
updated: 2026-03-10
---

# Monorepo Delivery Portal Example

> [!summary] Use
> This is a fully worked example repo for the monorepo variant: one repository, multiple surfaces, shared contracts, and path-aware ownership boundaries.

## Example Repo

- [[50-examples/monorepo-delivery-portal/README]]

## What It Demonstrates

- Layer 1: repo constitution plus explicit package, service, and app boundaries
- Layer 2: repository maps and ownership maps that reduce cross-package confusion
- Layer 3: local quality checks across shared contracts, backend code, and static frontend assets
- Layer 6 and 7: deployment-aware API service plus UI-facing smoke coverage

## Recommended Reading Path

1. [[50-examples/monorepo-delivery-portal/README]]
2. [[50-examples/monorepo-delivery-portal/REPO_MAP]]
3. [[50-examples/monorepo-delivery-portal/OWNERSHIP_MAP]]
4. [[50-examples/monorepo-delivery-portal/ARCHITECTURE]]
5. [[50-examples/monorepo-delivery-portal/scripts/run_quality_checks.py]]
6. [[50-examples/monorepo-delivery-portal/scripts/e2e_smoke.py]]

## Related Notes

- [[35-variants/Monorepo Variant]]
- [[35-variants/Deployed Product Variant]]
- [[20-reference/Repository Maps]]
- [[20-reference/QA Strategy and E2E Testing]]
- [[20-reference/Environment Strategy and Infrastructure as Code]]
