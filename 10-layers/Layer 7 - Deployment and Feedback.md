---
tags:
  - sdlc
  - layer
  - deployment
  - feedback
layer: 7
type: layer
status: active
updated: 2026-03-10
---

# Layer 7 - Deployment and Feedback

> [!summary] Outcome
> Get verified code to its destination, observe what happens, and route what you learn back into planning.

## What Happens Here

- deploy or promote code when the repo has a runtime target
- keep `main` green when the repo is documentation or source-only
- observe outcomes through telemetry
- turn observations into follow-up work

## Deployment Targets

For deployed systems:

- staging, smoke tests, rollout policy, rollback policy
- production telemetry and alerting
- tightly scoped deployer or SRE permissions

For non-deployed repos:

- `main` is the release artifact
- the feedback loop still matters

## Feedback Loop

```text
Merged code -> Observe outcomes -> Update roadmap -> Pick next task
```

At higher maturity, the observation layer should include logs, traces, metrics, and business signals. A safe self-healing loop may create fix tasks automatically or permit bounded rollback, restart, scale, or config corrections under policy.

## Failure Modes

- no telemetry beyond CI status
- agents cannot diagnose production behavior without a human dashboard
- production permissions are too broad for autonomous actors

## Related Notes

- [[20-reference/Observability]]
- [[30-patterns/Higher-Autonomy Setup]]
- [[30-patterns/Advanced Failure Modes]]
