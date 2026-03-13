---
tags:
  - sdlc
  - layer
  - architecture
layer: 1
type: layer
status: active
updated: 2026-03-10
---

# Layer 1 - Architecture and Blueprints

> [!summary] Outcome
> Define the repo constitution before autonomous work begins.
> This layer gives agents a stable structure, shared language, and hard boundaries.

## What Happens Here

- Define the system structure and operating constraints
- Document architecture, data formats, decisions, and onboarding rules
- Introduce machine-checkable contracts when the repo becomes too ambiguous for prose alone

## Core Artifacts

| Artifact | Purpose |
|----------|---------|
| `AGENTS.md` | single onboarding note for human and agent execution |
| `ARCHITECTURE.md` | system structure, boundaries, and data flow |
| `SCHEMA.md` | canonical data contracts and validation rules |
| `DECISIONS.md` | durable rationale for architectural choices |

## Guardrails

- Keep one canonical onboarding note
- Prefer explicit boundaries over implied conventions
- Add contracts only when ambiguity becomes expensive
- Keep permissions narrow at architecture boundaries

## Failure Modes

- Every agent invents a different local convention
- One bad interface decision propagates through the whole pipeline
- The repo becomes too implicit for reliable autonomous execution

## Upgrade Path

When prose stops being enough, add:

- OpenAPI, JSON Schema, or Protobuf contracts
- Mermaid sequence or state diagrams
- structured acceptance criteria
- explicit permission boundaries for deployer or SRE agents

## Related Notes

- [[20-reference/Contract-Driven Development]]
- [[20-reference/Repository Maps]]
- [[30-patterns/Machine-readable Specs]]
- [[40-templates/AGENTS Template]]
- [[40-templates/Architecture Template]]
- [[40-templates/Decision Log Template]]
