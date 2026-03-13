---
tags:
  - variant
  - deployment
type: variant
status: active
updated: 2026-03-10
---

# Deployed Product Variant

> [!summary] Fit
> Use this when merges trigger runtime behavior in staging, production, or both.

## Additions

- rollout policy
- rollback policy
- environment-specific checks
- incident response and postmortems
- production telemetry and alerting

## Risks

- treating CI as the only feedback loop
- agents with broad production permissions
- shipping changes without runtime evidence

## Related Notes

- [[10-layers/Layer 7 - Deployment and Feedback]]
- [[20-reference/Incident Response]]
- [[20-reference/Postmortems]]
- [[20-reference/Observability]]
