# SDLC Product Roadmap

## Product Goal

Turn this repository into an operator-grade system that lets a non-technical founder use CLI agents to create, govern, and run a software repository end to end with minimal manual stitching.

Core promise:

- start from intent, not repo mechanics
- generate the repo, docs, gates, plans, and agent instructions
- run a bounded SDLC and TDD workflow through agents
- keep documentation callable as a live runtime resource
- preserve human approval only at clearly defined high-risk gates

## Primary User

- non-technical founder operating through an agent-capable CLI

## North Star Use Case

1. founder describes the business and the software they want
2. system selects a repo profile
3. system creates the repository skeleton
4. system generates canonical docs and policies
5. system creates the initial roadmap, gates, and plans
6. system gives the founder copy-paste runbooks to hand to agents
7. agents execute the work through a governed TDD loop
8. the system records evidence, reviews, approvals, and closeout artifacts
9. the founder can query the documentation library at any time for guidance

## Product Contract

The system is successful when a founder can do the following without understanding software delivery internals:

1. create a repo from a short prompt
2. choose or confirm a repo type
3. generate all baseline docs and working rules
4. generate an actionable roadmap and task plan
5. generate risk-based gates and approval requirements
6. hand copy-paste runbooks to agents for execution
7. run a TDD-style implementation workflow
8. run review, release, and hotfix workflows
9. query the doc library for exact next-step guidance
10. inspect durable evidence of what happened and why

## Current State

What already exists:

- a strong blueprint and reference vault
- useful templates and playbooks
- starter kits and worked examples
- bootstrap scripts for basic guardrails
- example decision engines for workflow, release, and control logic

What is missing:

- one opinionated entrypoint
- founder-grade runbooks
- a machine-readable repo manifest
- a shared policy engine
- a real orchestration runtime
- live retrieval over the documentation system
- end-to-end proof that the full workflow works headlessly

## Guiding Decisions

1. Optimize for operator clarity before architectural elegance.
2. Prefer one golden path before supporting many variants.
3. Promote working code from examples into shared core modules.
4. Treat documentation as an active runtime dependency, not passive prose.
5. Add autonomy only when evidence, testing, and approvals are structurally enforced.

## Workstreams

### 1. Operator UX

Make the system understandable and usable by a founder who is not a developer.

Deliverables:

- workflow-first README
- founder quickstart
- copy-paste runbooks for create, plan, execute, gate, release, and hotfix
- one obvious entrypoint for every major task

### 2. Repo Factory

Create repositories from a small set of structured inputs instead of manual copying.

Deliverables:

- machine-readable repo manifest
- generator that renders docs, structure, prompts, and configs
- starter profiles for solo, small-team service, regulated, and monorepo cases

### 3. Shared SDLC Engine

Unify planning, gates, evidence, review roles, and release controls into shared code.

Deliverables:

- intake model
- planning engine
- gate policy engine
- release policy engine
- evidence requirements model

### 4. Orchestration Runtime

Run the lifecycle as a stateful workflow instead of disconnected prompts.

Deliverables:

- workflow state model
- orchestration commands
- task decomposition and assignment model
- gate closeout and approval handling
- durable status outputs

### 5. Retrieval and Memory

Make the documentation library callable during execution.

Deliverables:

- docs index
- topic and phase lookup
- repo-shape and risk-aware retrieval
- query command for agents and operators

### 6. Proof and Governance

Prove the system works and remains trustworthy.

Deliverables:

- end-to-end acceptance tests
- golden-path demo scenario
- evidence ledger
- process drift checks between docs, prompts, and implementation

## Phased Plan

### Phase 0. Product Definition And Golden Path

Goal:
Define the exact operator journey and narrow the first supported path.

Deliverables:

- written product contract
- canonical founder journey
- supported repo profile for v1
- success metrics and failure modes
- initial architecture decision record for the product direction

Exit criteria:

- one-sentence promise is stable
- one founder workflow is defined from start to finish
- repo scope is explicitly narrowed for v1

### Phase 1. Founder Entry Surface

Goal:
Replace framework-first navigation with workflow-first onboarding.

Deliverables:

- rewrite `README.md` around operator workflows
- add `FOUNDER-QUICKSTART.md`
- add `RUNBOOKS.md` index
- add copy-paste runbooks for:
  - create a repo
  - start planning
  - execute a task
  - close a gate
  - prepare a release
  - handle a hotfix

Exit criteria:

- a non-technical user can identify the next command or runbook in under two minutes
- every major workflow has a copy-pasteable operator artifact

### Phase 2. Canonical Repo Manifest And Generator

Goal:
Move from manual template copying to structured generation.

Deliverables:

- `repo.manifest.json` or equivalent canonical schema
- profile definitions for supported repo types
- generator that renders:
  - docs
  - prompts
  - CI
  - hooks
  - baseline repo structure
  - roadmap and risk artifacts
- template variable system for `40-templates/`

Exit criteria:

- one command can create a usable repo from a prompt plus manifest
- generated outputs are deterministic and testable

### Phase 3. Shared Planning And Gate Engine

Goal:
Promote the policy logic hidden in examples into product code.

Deliverables:

- shared Python package for:
  - intake normalization
  - task planning
  - gate generation
  - review-role assignment
  - evidence requirements
  - release control selection
- migration of current example logic into reusable modules
- test coverage for low-, medium-, and high-risk scenarios

Exit criteria:

- examples consume shared engine code instead of duplicating logic
- identical inputs always produce identical plans and gates

### Phase 4. Orchestrator Runtime

Goal:
Turn outputs into a controllable workflow engine.

Deliverables:

- state machine for:
  - intake
  - planning
  - task execution
  - TDD loop
  - review
  - gate handling
  - release
  - closeout
- CLI commands such as:
  - `sdlc create`
  - `sdlc intake`
  - `sdlc plan`
  - `sdlc run`
  - `sdlc gate`
  - `sdlc release`
  - `sdlc docs query`
- status and artifact outputs for human review

Exit criteria:

- one operator can drive the lifecycle through commands and runbooks instead of ad hoc prompting
- state transitions are explicit and inspectable

### Phase 5. Documentation Retrieval Layer

Goal:
Make the vault operationally useful during execution.

Deliverables:

- structured index over:
  - title
  - path
  - tags
  - repo variant
  - lifecycle phase
  - risk class
- query command that returns the most relevant runbook, template, or reference
- retrieval rules that prefer the smallest relevant context

Exit criteria:

- agents can fetch exact guidance for the current step without loading broad sections of the vault
- founder questions can be answered from the local doc system directly

### Phase 6. Evidence Ledger And Drift Control

Goal:
Make execution auditable and keep docs aligned with reality.

Deliverables:

- append-only evidence ledger for:
  - plan generation
  - gate decisions
  - local checks
  - CI results
  - approvals
  - release outcomes
  - gate closeout artifacts
- drift checks between:
  - prompts
  - playbooks
  - templates
  - generated repo outputs
  - implementation behavior

Exit criteria:

- every workflow step leaves a durable artifact
- process changes cannot silently diverge from docs

### Phase 7. End-To-End Proof

Goal:
Use the repo to create and operate a repo from start to finish.

Deliverables:

- self-hosted demo flow where this repo creates a new repo from the library
- automated end-to-end acceptance test for the v1 golden path
- operator demo transcript
- failure report template for any broken phase

Exit criteria:

- the system can create a repo, generate docs, generate plans and gates, run a TDD workflow, and produce release-ready artifacts with minimal manual intervention

## The 15 Priorities Incorporated

### Improve Existing Assets

1. convert playbooks into copy-paste operator runbooks
2. convert templates into generators
3. promote example logic into shared core code
4. create a retrieval surface over the vault
5. replace multiple entrypoints with one opinionated entrypoint

### Leadership Actions

6. optimize for the non-technical founder use case
7. design one golden path first
8. rewrite the top-level UX around workflows, not concepts
9. separate core engine, generated outputs, reference library, and examples
10. add hard proof with a full headless acceptance path

### Next-Level Capabilities

11. build a real `sdlc` CLI
12. define a machine-readable repo manifest
13. implement a stateful orchestrator runtime
14. add retrieval-backed runbook execution
15. add an evidence ledger for governance and traceability

## Immediate Execution Order

### Wave 1

- define the v1 product contract
- choose the first supported repo type
- rewrite README around the founder journey
- create founder quickstart and runbook index

### Wave 2

- define the manifest schema
- build generator scaffolding
- convert one starter kit into generated output

### Wave 3

- extract shared planning and gate logic from examples
- add tests around shared policy behavior

### Wave 4

- implement core CLI commands
- add workflow state handling
- generate durable status artifacts

### Wave 5

- build docs indexing and query
- add evidence ledger
- run the end-to-end self-bootstrap test

## Success Metrics

- founder time from idea to created repo
- founder time from task request to agent-ready runbook
- percent of workflows executable without custom prompting
- percent of workflows leaving complete evidence artifacts
- end-to-end golden path pass rate
- drift incidents between docs and behavior

## Major Risks

1. overbuilding before the golden path is proven
2. preserving too many variants too early
3. keeping logic duplicated between docs, examples, and product code
4. producing generic runbooks that still require technical judgment
5. treating retrieval as search only instead of action-oriented guidance

## What We Are Not Doing First

- broad multi-language support
- generalized swarm orchestration before the single orchestrator path is stable
- autonomous production changes without explicit approvals
- multiple overlapping repo creation interfaces
- speculative advanced patterns that do not improve the founder golden path

## Next Milestone

Deliver a v1 founder journey where a user can:

1. run one creation command
2. receive a generated repo and core docs
3. use copy-paste runbooks to plan and execute the first feature
4. enforce gates and collect evidence
5. query the doc library for the next step at any point
