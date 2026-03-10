# Append-Only Scratchpad

This scratchpad records material found in archived dump docs that is not currently represented in `agentic-sdlc-blueprint.md`.

Entries are appended in processing order. `agentic-sdlc-blueprint.md` remains the canonical working document.

## 2026-03-10 - Processed `dump-Gemini3.1-SDLC.md`

- Control-loop framing: the dump describes agentic SDLC in OODA/ReAct terms rather than only as a repo workflow.
- Agent-computer interfaces: headless browsers, terminals, Git, and LSPs are treated as first-class agent capabilities.
- Sandboxed execution environments: E2B and Daytona are named as safe run/fail/fix sandboxes.
- Repository retrieval pattern: ctags-style repo maps and selective retrieval are preferred over loading entire repositories into context.
- Planning artifact detail: PM agents generate PRDs, acceptance criteria, epics, and user stories, with optional sync to Linear or Jira.
- Named multi-agent exemplars: MetaGPT and ChatDev are cited as early virtual-company patterns.
- Architecture outputs not present in the blueprint: OpenAPI or Swagger contracts, database schemas, and Mermaid sequence diagrams.
- Architecture governance detail: architect agents can enforce SOPs and design patterns downstream.
- Implementation exemplars: Devin, OpenHands, SWE-agent, Cursor Composer, and Aider are named as concrete agentic coding or workspace tools.
- Testing detail absent from the blueprint: VLM-driven Playwright sessions for visual verification of rendered UIs.
- CI remediation loop: a DevOps agent can watch failed CI runs, patch the failure in a sandbox, and open a fix PR automatically.
- Failure modes not currently called out in the blueprint: context degradation or "lost in the middle", cascading hallucinations across agent stages, and the security risk of broad cloud or database permissions.

## 2026-03-10 - Processed `dump-Gemini3.1.md`

- Machine-readable-everything principle: replace free-form tickets and prose-heavy docs with JSON, YAML, or state-machine contracts where possible.
- Contract-driven development: define strict input and output boundaries before implementation to reduce hallucination and scope drift.
- AST-over-text preference: agents should edit via AST- or LSP-aware interfaces rather than raw text when the stack allows it.
- System Specification Object (SSO): a formal requirements artifact with acceptance criteria mapped to BDD or Gherkin.
- Architect-first testing: generate end-to-end and integration tests from the spec before implementation, then treat those tests as the source of truth.
- Architecture bias for agent reliability: micro-modules, strong decoupling, and strict typing; Rust, Go, and TypeScript are named as good fits.
- Orchestrator implementations: LangGraph, Temporal, and AutoGen are explicitly suggested for stateful multi-agent flows.
- Self-healing implementation loop detail: LSP-fed compiler or runtime errors are returned directly into the agent context for repair.
- Change-application detail: unified diff or AST-based application is recommended to reduce formatting and bracket errors.
- Parallel contract execution: frontend and backend agents can work concurrently when API contracts are fixed first.
- Adversarial verification detail: a security agent is prompted to behave as a malicious actor and attempt auth bypass, leak, or exception paths.
- Visual QA detail: VLM agents validate rendered UI states against Figma design tokens converted to JSON.
- DevOps specifics absent from the blueprint: infrastructure-as-code generation from performance or capacity requirements, conflict-resolution agents for merges, and verbose structured JSON logs intended for machine consumption.
- Operations detail: Datadog or Prometheus polling, sandboxed hotfix generation, auto-rollback, and a read-only-production or write-staging boundary for SRE agents.
- HITL gate model: explicit human approval gates for intent, architecture, and deployment.

## 2026-03-10 - Processed `dump-Grok4.2.md`

- Spec-driven development emphasis: living, bidirectional specs are treated as the central constitution for all agents.
- Swarm-level operating assumptions: small atomic tasks, persistent repo memory, explicit self-reflection loops, and heavy native tool use across git, terminal, browser, CI, and observability systems.
- Traceability requirement: every agent logs reasoning, decisions, and evidence for later audit.
- Governance additions: model routing for cost control, escalation thresholds, and a dedicated governance or security role spanning the whole lifecycle.
- Metrics not present in the blueprint: autonomous solve rate, cost per feature, and human touch-point counts.
- Expanded role taxonomy: Integrator or CI Agent, Deployer Agent, SRE or Observability Agent, and Governance or Security Agent are called out as separate roles.
- Spec approval nuance: low-risk work can be auto-approved while high-risk work still requires a human gate.
- Implementation loop detail absent from the blueprint: explicit Red, Green, Blue agent TDD plus a self-critique or reflection pass.
- PR content detail: spec links, test evidence, and Playwright screenshots are treated as standard PR payload.
- Review mechanics: adversarial multi-model review, conventional line comments or suggestions, risk scoring, and threshold-based auto-merge.
- Release mechanics: blue-green or canary rollout, smoke tests, and governance-based production-readiness scoring.
- Observability scope: business metrics and user behavior are included alongside logs, traces, and infrastructure telemetry.
- Self-healing nuance: scale, restart, or config-tweak actions can be automated under approval thresholds.
- Meta-layer concept: measure agent performance, replace weak agents, and evolve prompts or tools from production outcomes.
- Additional ecosystem or tooling references: CrewAI, GitHub Copilot Agent mode, GitHub Spec Kit, Intent, Azure Monitor, Trivy, Checkov, centralized MCP brokers, and mixed frontier or local model routing.

## 2026-03-10 - Processed `dump-toolchain.md`

- Local-model note absent from the blueprint: the toolchain can mix local GPU-hosted models via Ollama with frontier and alternative code models.
- Repo or agent tooling note: GitHub plus Copilot Agent mode, OpenHands, or custom SWE-agent derivatives are named as repo-facing execution surfaces.
- Spec tooling note: GitHub Spec Kit and Intent are named as concrete living-spec systems.
- Security tooling note: Trivy and Checkov are named alongside agent-generated tests and property-based testing.
- Observability tooling note: Azure Monitor or Prometheus plus AIOps agents.
- Governance tooling note: centralized MCP broker plus a standardized prompt library.
