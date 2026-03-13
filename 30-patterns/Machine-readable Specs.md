---
tags:
  - pattern
  - specs
type: pattern
status: active
updated: 2026-03-10
---

# Machine-readable Specs

> [!summary] Use
> Add machine-readable artifacts when prose is no longer enough to stabilize autonomous execution.

## Good Candidates

- JSON or YAML system specification objects
- OpenAPI or Protobuf contracts
- JSON Schema validation rules
- executable acceptance criteria
- state or sequence diagrams

## When To Use This Pattern

- multiple agents need stable boundaries
- the same ambiguity keeps causing defects
- parallel implementation depends on fixed interfaces

## Avoid

- replacing every human-readable note with a rigid schema too early
- generating contracts that nobody maintains

## Related Notes

- [[10-layers/Layer 1 - Architecture and Blueprints]]
- [[20-reference/Contract-Driven Development]]
- [[40-templates/Spec Template]]
