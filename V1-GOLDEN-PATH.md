# V1 Golden Path

## Purpose

This document defines the first end-to-end workflow this repo must support as a product.

It exists to keep the scope narrow while the system moves from "framework and examples" to "founder-grade repo factory."

## V1 Product Promise

A non-technical founder can use CLI agents to create and run one practical kind of software repository end to end, with clear docs, bounded task execution, approval gates, release preparation, and hotfix handling.

## Primary User

- a non-technical founder working through an agent-capable CLI

## First Supported Repo Type

### Chosen Profile

- small-team Python service

### Why This Profile Comes First

This profile is the best v1 proving ground because it is still small enough to understand while covering the full lifecycle the product needs to govern:

- repo setup
- canonical docs
- milestone planning
- bounded task execution
- local validation
- approval gates
- release preparation
- rollback thinking
- hotfix handling

It is a better first target than:

- the solo starter, which is simpler but too thin for full release and gate behavior
- the regulated starter, which adds too much governance complexity too early
- the monorepo starter, which adds retrieval and coordination complexity before the single-repo path is stable

## Founder Inputs Required

The founder should only need to provide:

1. product name
2. one-sentence product promise
3. target user
4. first release outcome
5. notable constraints

Optional inputs:

- target deadline
- platform preference
- compliance requirements
- existing repo or greenfield

## Canonical V1 Workflow

### Step 1. Founder Describes The Product

The founder gives a short prompt with the product basics.

System outcome:

- classify the request as a small-team Python service
- confirm or propose the profile

### Step 2. System Creates The Repo Baseline

The system creates the first usable repository baseline from the chosen profile.

Required outputs:

- repo structure
- baseline docs
- working rules
- hooks and CI baseline
- founder-facing quickstart and runbooks

### Step 3. System Generates The First Milestone Plan

The system turns the founder's release goal into one concrete milestone.

Required outputs:

- milestone objective
- success criteria
- top risks
- first 3 to 5 tasks
- next approval gate

### Step 4. Founder Hands A Task To An Agent

The founder uses a copy-paste runbook to tell the agent to execute one bounded task.

Required behavior:

- inspect repo state first
- work directly in the repo
- update durable docs when needed
- run the lightest meaningful validation

### Step 5. System Assembles A Gate Packet

The system pauses at a meaningful decision point and creates a founder-readable gate packet.

Required outputs:

- what is complete
- what is not complete
- evidence
- main risks
- recommendation
- exact approval question

### Step 6. System Prepares A Release

When a milestone is ready, the system creates a release packet before anything ships.

Required outputs:

- included scope
- excluded scope
- existing validation
- missing validation
- rollout plan
- rollback plan
- release notes draft

### Step 7. System Supports Hotfixes

If something urgent breaks, the system switches to a narrow hotfix workflow without abandoning evidence and approval discipline.

Required outputs:

- severity estimate
- blast radius
- containment or rollback recommendation
- smallest viable fix
- targeted validation
- founder update

## Minimum Durable Artifacts For V1

The system should be able to generate or maintain these artifacts for the first supported repo type:

- `README.md`
- `AGENTS.md`
- `ARCHITECTURE.md`
- `SCHEMA.md`
- `DECISIONS.md`
- `ROADMAP.md`
- `RISK_REGISTER.md`
- `ENVIRONMENTS.md`
- `SLOS.md`
- founder-facing runbooks

## What Counts As Success

V1 is successful when a founder can do the following with minimal manual stitching:

1. create a repo from a short prompt
2. receive a working baseline for the chosen repo type
3. get a founder-readable first milestone plan
4. hand a task to an agent with a copy-paste runbook
5. receive a real gate packet before high-value decisions
6. prepare a release packet without ad hoc prompting
7. run a hotfix flow when needed

## Failure Modes To Guard Against

The v1 path fails if:

- the founder has to understand internal SDLC concepts to continue
- the agent explains what to do instead of operating in the repo
- the repo baseline is too generic to be useful
- gates exist in theory but do not produce decision-ready artifacts
- release prep does not include rollout and rollback thinking
- the doc library is broad but not actionable

## V1 Non-Goals

V1 does not try to solve:

- broad multi-language repo generation
- advanced multi-agent swarm orchestration
- autonomous production deployment without explicit approval
- highly regulated workflows as the default
- monorepo-first support
- a complete retrieval engine before the golden path is proven

## How This Connects To Phase 2

Phase 2 should build directly against this document.

The first generator and manifest should target the small-team Python service profile and produce the artifacts needed for this exact workflow, not a generalized framework engine.

## Immediate Next Build Implication

The next implementation task after this document is:

- define the canonical manifest schema for the small-team Python service profile
