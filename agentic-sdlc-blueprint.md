---
aliases:
  - Agentic SDLC
  - SDLC Blueprint
tags:
  - sdlc
  - agentic-engineering
  - software-process
type: blueprint
status: active
created: 2026-03-10
updated: 2026-03-10
---

# Agentic SDLC Blueprint

> [!summary] Canonical Overview
> This note is the high-level map of the vault.
> Use it to understand the full workflow, then move into the linked layer, reference, pattern, and template notes for implementation detail.

## Agentic Principles Playbook (Mandatory)

This framework is governed by the [Agentic Principles Playbook](principles/agentic-playbook/index.md). This playbook is non-negotiable for every workflow. Every agent must load, internalize, and obey these principles before taking any action.

## Start Here

- Vault map: [[00-index/Agentic SDLC Vault]]
- Layer map: [[00-index/Layers]]
- Reference map: [[00-index/Reference]]
- Pattern map: [[00-index/Patterns]]
- Variant map: [[00-index/Variants]]
- Playbook map: [[00-index/Playbooks]]
- Template map: [[00-index/Templates]]
- Starter kit map: [[00-index/Starter Kits]]
- Example map: [[00-index/Examples]]
- Full historical monolith: [[archive/agentic-sdlc-blueprint-monolith-2026-03-10]]

## Core Thesis

An agent-first SDLC is not "developers, but faster."
It is a workflow redesigned around these assumptions:

- agents do most execution
- humans set intent, boundaries, and escalation rules
- quality is enforced structurally, not socially
- verification must be machine-readable
- agents do not approve their own work

## The End-to-End Pipeline

```text
Intent -> Architecture -> Task Routing -> Code/Test/Commit -> PR -> CI/Review -> Merge -> Deploy/Observe -> Next Task
```

## The Seven Layers

| Layer | Purpose | Note |
|------|---------|------|
| 1 | define the repo constitution | [[10-layers/Layer 1 - Architecture and Blueprints]] |
| 2 | turn intent into bounded work | [[10-layers/Layer 2 - Task Management]] |
| 3 | make the local execution loop fast and reliable | [[10-layers/Layer 3 - The Inner Loop - Code, Test, Commit]] |
| 4 | preserve scoped and readable history | [[10-layers/Layer 4 - Version Control]] |
| 5 | surface work early through draft PRs | [[10-layers/Layer 5 - Pull Requests]] |
| 6 | verify independently and merge safely | [[10-layers/Layer 6 - Review, CI-CD, and Merge]] |
| 7 | deploy, observe, and learn | [[10-layers/Layer 7 - Deployment and Feedback]] |

## Golden Path

1. Define the repo rules and architecture boundaries.
2. Let the orchestrator assign a short, scoped task with a branch.
3. Run a blocking local quality loop before commit.
4. Auto-push and open a draft PR for visibility.
5. Re-run checks in CI.
6. Review independently, ideally adversarially.
7. Merge only behind branch protection.
8. Observe the result and turn what you learn into the next task.

## Minimum Viable Implementation

> [!check] Baseline Repo Setup
> - copy [[40-templates/AGENTS Template]]
> - add [[40-templates/Quality Checks Template]]
> - add [[40-templates/CI Workflow Template]]
> - require evidence with [[40-templates/PR Template]]
> - define done with [[40-templates/Definition of Done Checklist]]
> - enable branch protection
>
> For a copyable repo skeleton instead of assembling fragments by hand, start with [[00-index/Starter Kits]].

## What Scales This System

Three things make the blueprint scale without collapsing into prompt chaos:

- stronger contracts: [[20-reference/Contract-Driven Development]]
- better retrieval: [[20-reference/Repository Maps]]
- better telemetry: [[20-reference/Observability]]

## Optional Advanced Patterns

Add these only when the core path is already trustworthy:

- machine-readable spec systems: [[30-patterns/Machine-readable Specs]]
- specialized multi-agent orchestration: [[30-patterns/Swarm Orchestration]]
- higher-autonomy operational controls: [[30-patterns/Higher-Autonomy Setup]]
- structural risk management: [[30-patterns/Advanced Failure Modes]]
- workflow anti-pattern guardrails: [[30-patterns/Workflow Anti-Patterns]]
- drift detection and recovery: [[30-patterns/Documentation Drift and Process Erosion]]

## Variants

Use the smallest variant that matches the repo you actually have:

- [[35-variants/Solo Repo Variant]]
- [[35-variants/Small Team Variant]]
- [[35-variants/Monorepo Variant]]
- [[35-variants/Deployed Product Variant]]
- [[35-variants/Regulated Environment Variant]]

## Control Planes Beyond The Core Flow

These notes cover the parts of an end-to-end SDLC that sit around the seven layers rather than inside a single layer:

- planning and prioritization: [[20-reference/Roadmaps and Backlogs]] and [[20-reference/Risk Registers]]
- intake and clarification: [[20-reference/Requirements Intake and Clarification]]
- spec governance: [[20-reference/Spec Lifecycle]]
- agent operating model: [[20-reference/Agent Roles and Operating Model]]
- agent tool surfaces: [[20-reference/Agent-Computer Interfaces and Tool Catalogs]]
- prompt and policy control: [[20-reference/Prompt and Policy Management]]
- memory and retrieval: [[20-reference/Memory and Retrieval Strategy]]
- model selection and cost: [[20-reference/Model Routing and Cost Control]]
- human decision gates: [[20-reference/Human-in-the-Loop Gates]]
- separation of duties: [[20-reference/Separation of Duties]]
- permissions and sandboxing: [[20-reference/Permissions and Sandbox Policy]]
- data governance and privacy: [[20-reference/Data Governance and Privacy]]
- security and threat modeling: [[20-reference/Security and Threat Modeling]]
- compliance and auditability: [[20-reference/Compliance and Auditability]]
- documentation maintenance: [[20-reference/Documentation Governance]]
- release control: [[20-reference/Release Management]] and [[20-reference/Deployment Strategies]]
- versioning and rollout control: [[20-reference/Versioning and Release Trains]] and [[20-reference/Feature Flags and Progressive Delivery]]
- environments and infrastructure: [[20-reference/Environment Strategy and Infrastructure as Code]]
- ownership and reliability targets: [[20-reference/Service Ownership and Code Ownership]] and [[20-reference/SLOs, SLIs, and Alerting]]
- QA and product feedback: [[20-reference/QA Strategy and E2E Testing]] and [[20-reference/Experimentation and Product Feedback]]
- incidents and learning: [[20-reference/Incident Response]] and [[20-reference/Postmortems]]
- evaluation and economics: [[20-reference/Agent Evaluation and Scorecards]] and [[20-reference/Economics and Cost Tracking]]

## Metrics That Matter

Start simple:

- local check pass rate
- rework rate
- PR cycle time

Add more only when the system is mature enough to justify them:

- autonomous solve rate
- human touch-points per task
- cost per merged change

See also: [[20-reference/DORA Metrics]]

## Recommended Reading Paths

### If You Want The Operational Workflow

1. [[10-layers/Layer 1 - Architecture and Blueprints]]
2. [[10-layers/Layer 2 - Task Management]]
3. [[10-layers/Layer 3 - The Inner Loop - Code, Test, Commit]]
4. [[10-layers/Layer 6 - Review, CI-CD, and Merge]]
5. [[10-layers/Layer 7 - Deployment and Feedback]]

### If You Want To Implement It In A Repo

1. [[00-index/Templates]]
2. [[00-index/Starter Kits]]
3. [[55-starter-kits/Solo Python Starter Kit]]
4. [[55-starter-kits/Small Team Service Starter Kit]]
5. [[55-starter-kits/Regulated Change Control Starter Kit]]
6. [[55-starter-kits/Monorepo Platform Starter Kit]]

### If You Want A Concrete Worked Example

1. [[00-index/Examples]]
2. [[50-examples/Solo Python Task Router Example]]
3. [[50-examples/Small Team Release Gateway Example]]
4. [[50-examples/Regulated Change Control Example]]
5. [[50-examples/Monorepo Delivery Portal Example]]
6. [[50-examples/solo-python-task-router/README]]
7. [[50-examples/small-team-release-gateway/README]]
8. [[50-examples/regulated-change-control/README]]
9. [[50-examples/monorepo-delivery-portal/README]]
10. [[50-examples/monorepo-delivery-portal/scripts/run_quality_checks.py]]

### If You Want Operational Runbooks

1. [[00-index/Playbooks]]
2. [[45-playbooks/Greenfield Repo Setup Playbook]]
3. [[45-playbooks/Feature Delivery Playbook]]
4. [[45-playbooks/Release Playbook]]
5. [[45-playbooks/Hotfix Playbook]]
6. [[45-playbooks/Architecture and Process Change Playbook]]

### If You Want To Scale Autonomy

1. [[20-reference/Contract-Driven Development]]
2. [[20-reference/Repository Maps]]
3. [[20-reference/Observability]]
4. [[30-patterns/Higher-Autonomy Setup]]
5. [[30-patterns/Advanced Failure Modes]]

## Design Rules

> [!important] Keep The Core Boring
> The default path should be simple enough for one repo, one human operator, one worker, and one reviewer.
> Add swarms, machine-readable specs, deployment automation, and self-healing only when the simpler structure is already reliable.

## Related Notes

- [[00-index/Agentic SDLC Vault]]
- [[00-index/Layers]]
- [[00-index/Reference]]
- [[00-index/Patterns]]
- [[00-index/Variants]]
- [[00-index/Playbooks]]
- [[00-index/Templates]]
- [[00-index/Examples]]
- [[50-examples/Example Implementation Roadmap]]
