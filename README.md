# Agentic SDLC

This repository is being shaped into an operator-grade system for one primary use case:

- a non-technical founder uses CLI agents to create and run a software repo end to end

The long-term goal is simple:

- start from intent
- generate the repo, docs, gates, plans, and agent instructions
- run a governed SDLC and TDD workflow through agents
- keep the documentation library callable during execution

## Start Here If You Are The Founder

If you are not a developer and you want to use agents from the CLI, start here:

1. Read [FOUNDER-QUICKSTART.md](FOUNDER-QUICKSTART.md)
2. Use [RUNBOOKS.md](RUNBOOKS.md) to choose the exact workflow you need
3. Read [V1-GOLDEN-PATH.md](V1-GOLDEN-PATH.md) to see the first supported end-to-end workflow
4. Use [ROADMAP.md](ROADMAP.md) if you want to understand what the product is becoming

## What This Repo Gives You Today

Today this repo already includes the core building blocks:

- a blueprint for an agent-first SDLC in [agentic-sdlc-blueprint.md](agentic-sdlc-blueprint.md)
- a documentation vault with layers, references, patterns, templates, and playbooks
- starter kits in `55-starter-kits/`
- worked examples in `50-examples/`
- bootstrap scripts in `sdlc-bootstrap-kit/`
- a minimal CLI in [sdlc-cli.py](sdlc-cli.py)
- a roadmap for turning this into a full repo factory in [ROADMAP.md](ROADMAP.md)
- a concrete v1 workflow target in [V1-GOLDEN-PATH.md](V1-GOLDEN-PATH.md)
- a durable v1 scope record in [DECISIONS.md](DECISIONS.md)

What it does not fully provide yet:

- a single end-to-end command surface
- a shared planning and gate engine
- a stateful orchestrator runtime
- retrieval-backed docs queries
- a fully proven headless golden path

## Current Product Direction

This repo is moving from "framework and examples" toward "founder-grade repo factory."

The delivery plan is:

1. create founder-facing onboarding and copy-paste runbooks
2. define a canonical repo manifest and generator
3. promote planning and gate logic from examples into shared core code
4. build a real `sdlc` command surface
5. add runtime retrieval and durable evidence tracking
6. prove the full workflow end to end by using this repo to create a repo

## Recommended Navigation

Use the smallest surface that matches your need:

- `FOUNDER-QUICKSTART.md`: the shortest path if you are operating agents directly
- `RUNBOOKS.md`: copy-paste procedures for create, plan, execute, gate, release, and hotfix
- `V1-GOLDEN-PATH.md`: the exact first workflow this product is being built to support
- `55-starter-kits/`: ready-to-copy repo skeletons
- `50-examples/`: runnable examples of the framework in practice
- `40-templates/`: note and process templates
- `45-playbooks/`: framework playbooks and reference procedures
- `00-index/`: full vault navigation

## If You Are An Agent

Every agent working in this repo should start from the framework rules before doing work:

1. read [principles/agentic-playbook/index.md](principles/agentic-playbook/index.md)
2. load [40-templates/agent-bootstrap-prompt.md](40-templates/agent-bootstrap-prompt.md)
3. use [AGENT-GUIDE.md](AGENT-GUIDE.md), [CONTEXT.md](CONTEXT.md), and the canonical docs before acting

## Core Repository Surfaces

- [agentic-sdlc-blueprint.md](agentic-sdlc-blueprint.md): canonical operating model
- [ROADMAP.md](ROADMAP.md): product transformation plan
- [V1-GOLDEN-PATH.md](V1-GOLDEN-PATH.md): first supported founder workflow
- [DECISIONS.md](DECISIONS.md): durable product and scope decisions
- [00-index/Agentic SDLC Vault.md](00-index/Agentic%20SDLC%20Vault.md): vault map
- [sdlc-bootstrap-kit/README.md](sdlc-bootstrap-kit/README.md): bootstrap harness
- [CONTRIBUTING.md](CONTRIBUTING.md): contribution guidance
