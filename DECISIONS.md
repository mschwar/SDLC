# DECISIONS.md

## 2026-04-20 - Primary User Is The Non-Technical Founder
- Status: accepted
- Context:
  This repo started as a framework, vault, bootstrap kit, and example library. That made it useful as reference material, but too indirect for the product use case now driving the work.
- Decision:
  Treat the non-technical founder using CLI agents as the primary user for v1 product decisions.
- Consequences:
  Founder clarity now outranks framework completeness. Entry surfaces, runbooks, prompts, and generated artifacts should assume the user is directing agents, not writing code or designing SDLC process by hand.
- Revisit Trigger:
  Revisit if the product proves strong for the founder use case and there is evidence that a second operator persona needs a meaningfully different surface.

## 2026-04-20 - First Supported Repo Type Is A Small-Team Python Service
- Status: accepted
- Context:
  The repo currently contains several starter shapes: solo Python, small-team service, regulated change control, and monorepo platform. Supporting all of them equally would force premature abstraction.
- Decision:
  Use the small-team Python service as the first supported repo profile for the productized path.
- Consequences:
  The first generator, manifest, runbooks, and end-to-end proof should optimize for a single-service Python repository with enough operational surface to exercise planning, gates, release prep, rollback thinking, and hotfix handling.
- Revisit Trigger:
  Revisit after the small-team service golden path is proven end to end with acceptance coverage and real operator use.

## 2026-04-20 - V1 Ships One Golden Path Before Generalization
- Status: accepted
- Context:
  The repo already has broad framework coverage. The main risk now is building a general system without proving a concrete path that a founder can actually use.
- Decision:
  Build and prove one founder-readable golden path before expanding into a generalized repo factory.
- Consequences:
  New work should reduce ambiguity, increase determinism, and directly support the v1 flow documented in `V1-GOLDEN-PATH.md`. General abstractions should be avoided unless they immediately serve that path.
- Revisit Trigger:
  Revisit once the v1 flow can reliably create a repo, generate baseline docs, produce a first milestone plan, support task execution, assemble a gate packet, and prepare a release packet.

## 2026-04-20 - Documentation Is A Runtime Dependency, Not Just Reference Material
- Status: accepted
- Context:
  The repo's strongest asset is the documentation library, but today it behaves more like a passive vault than an operational control plane.
- Decision:
  Treat the documentation system as a runtime dependency that agents and founders should be able to query during execution.
- Consequences:
  Runbooks, canonical notes, and generated docs need to be concise, durable, and retrieval-friendly. Future CLI and retrieval work should prefer targeted, action-oriented outputs over broad explanatory dumps.
- Revisit Trigger:
  Revisit if a different retrieval model proves more reliable than doc-centric execution guidance.

## 2026-04-20 - V1 Non-Goals Must Stay Explicit
- Status: accepted
- Context:
  This repo contains enough reference material to tempt early expansion into regulated defaults, monorepos, multi-language support, and advanced orchestration before the base path is stable.
- Decision:
  Keep the following out of v1 scope by default: multi-language repo generation, monorepo-first support, regulated-first workflows, autonomous production deployment without approval, and advanced swarm orchestration.
- Consequences:
  Roadmap and implementation choices should bias toward a stable, founder-usable baseline instead of feature breadth. Any work outside the first golden path requires explicit justification.
- Revisit Trigger:
  Revisit after the first supported repo type has been proven with a passing end-to-end self-bootstrap flow.
