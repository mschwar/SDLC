---
tags:
  - pattern
  - orchestration
type: pattern
status: active
updated: 2026-03-10
---

# Swarm Orchestration

> [!summary] Use
> Split responsibility across specialized agents when one orchestrator-worker-reviewer loop is no longer enough.

## Typical Roles

- clarifier or PM
- architect
- coder swarm
- tester
- reviewer
- integrator
- deployer
- SRE
- governance

## When To Use This Pattern

- many tasks can run independently
- work requires durable routing or retries
- review, testing, and deployment need separate policy boundaries

## Risks

- role explosion
- orchestration overhead
- hidden coupling between agents

## Related Notes

- [[10-layers/Layer 2 - Task Management]]
- [[10-layers/Layer 6 - Review, CI-CD, and Merge]]
- [[30-patterns/Higher-Autonomy Setup]]
