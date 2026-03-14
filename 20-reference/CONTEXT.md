---
generated: '2026-03-14T00:30:33Z'
generator: ctx/0.1.0
model: claude-haiku-4-5-20251001
content_hash: sha256:583c57ef471e4e730df3d59bd5cb6eb17e8a82401981b57e484c828615b595cd
files: 49
dirs: 0
tokens_total: 7137
---
# C:/Users/Matty/Documents/SDLC/20-reference

A comprehensive reference library of software delivery lifecycle practices, patterns, and governance structures for agent-driven development workflows.

## Files

- **Adversarial Verification.md** — Review and testing performed from the perspective of a breaker rather than a builder, including adversarial prompts, security checks, fuzzing, and mutation testing.
- **Agent Evaluation and Scorecards.md** — A repeatable measurement system for agent performance across correctness, scope control, cost, safety, and autonomy dimensions.
- **Agent Roles and Operating Model.md** — Explicit description of which agents exist, their responsibilities, allowed actions, and how they hand work to one another.
- **Agent-Computer Interfaces and Tool Catalogs.md** — The interfaces, tools, and execution surfaces agents use to read context, write changes, run commands, and interact with external services.
- **Agentic-First.md** — Design workflow around autonomous execution, structural guardrails, and machine-readable validation instead of relying on people to remember process steps.
- **Branch Protection Rules.md** — Repository-level rules that block unsafe actions on important branches such as requiring status checks and review approval.
- **CI-CD.md** — Continuous Integration re-runs builds and tests on every change while Continuous Delivery moves validated code toward its runtime target.
- **Code Review.md** — Independent examination of a proposed change before it becomes part of the protected branch, checking scope, correctness, safety, and pattern fit.
- **Compliance and Auditability.md** — The ability to show what happened, who approved it, what evidence supported it, and how access and data were controlled.
- **Contract-Driven Development.md** — Define interfaces, data shapes, behavioral expectations, and boundaries before implementation so agents can work inside explicit constraints.
- **Conventional Commits.md** — A standardized commit message format such as feat(scope) or fix that makes agent-heavy histories readable and automates workflows.
- **DORA Metrics.md** — A set of delivery performance metrics centered on lead time, deployment frequency, change failure rate, and recovery time.
- **Data Governance and Privacy.md** — The rules for classifying, handling, storing, transmitting, and exposing data within an agent-driven workflow.
- **Definition of Done.md** — The minimum conditions that must be true before a task, PR, or release can be treated as complete.
- **Dependency Pinning.md** — Record exact dependency versions so environments are reproducible and nondeterminism is reduced.
- **Deployment Strategies.md** — Controlled methods used to expose validated code to runtime environments such as canary, blue-green, or staged rollout.
- **Documentation Governance.md** — The rules for which notes are canonical, how they are maintained, when they must be updated, and how drift is detected.
- **Draft PRs and Ready PRs.md** — Draft means visible but not mergeable while Ready means the author considers the branch complete enough for formal merge review.
- **Economics and Cost Tracking.md** — The practice of measuring what the workflow costs in model usage, CI spend, human review effort, and time-to-merge.
- **Environment Strategy and Infrastructure as Code.md** — The plan for how development, test, staging, and production environments are structured and how they are created or changed.
- **Experimentation and Product Feedback.md** — The process of validating whether a shipped change improved the product or business outcome it was meant to affect.
- **Feature Flags and Progressive Delivery.md** — Techniques for controlling exposure of new behavior after code is merged, reducing blast radius and separating shipping from exposure.
- **Git Hooks.md** — Scripts Git runs automatically at specific lifecycle moments such as pre-commit, commit-msg, and pre-push to turn quality checks into structure.
- **GitHub Actions.md** — GitHub's built-in workflow engine for automating checks, builds, deployment, and repo events.
- **Human-in-the-Loop Gates.md** — Explicit decision points where a human must approve, redirect, or reject agent action before the workflow continues.
- **Incident Response.md** — The structured process for detecting, triaging, containing, fixing, and communicating operational failures.
- **Inner Loop vs Outer Loop.md** — The inner loop is local work while the outer loop begins after the change leaves the machine, both requiring speed optimization.
- **Memory and Retrieval Strategy.md** — The rules for what context agents keep, how they retrieve it, and how they avoid being overloaded by irrelevant repo state.
- **Merge Queues.md** — A system that serializes and re-tests ready branches against the latest base branch before merge when concurrency is high.
- **Model Routing and Cost Control.md** — The policy for deciding which model handles which class of work based on quality needs, latency, privacy, and cost.
- **Mutation Testing.md** — Intentionally change code in small ways and check whether tests fail to reveal blind spots in the test suite.
- **Observability.md** — The ability to understand system behavior through logs, metrics, traces, and business signals.
- **Permissions and Sandbox Policy.md** — The rules that determine what agents can read, write, execute, and approve in each environment based on least privilege principles.
- **Postmortems.md** — A structured review of what failed, why it failed, what evidence supports the explanation, and what will change next time.
- **Prompt and Policy Management.md** — The controlled maintenance of system prompts, role prompts, task instructions, and behavioral policies that shape how agents operate.
- **Property-Based Testing.md** — Define rules that should always hold, then generate many inputs to test those rules instead of relying only on a small set of examples.
- **QA Strategy and E2E Testing.md** — The intentional mix of unit, integration, end-to-end, UI, and exploratory validation used to prove that the system works at the right level.
- **Release Management.md** — The process of deciding what is ready to ship, under what conditions, with what evidence, and with what rollback plan.
- **Repository Maps.md** — Lightweight indexes that help an agent find the right files, symbols, and boundaries without loading the whole repo into context.
- **Requirements Intake and Clarification.md** — The process of turning vague human intent into bounded, testable, implementation-ready work with clear objectives and acceptance criteria.
- **Risk Registers.md** — A living list of known risks, their impact, mitigation plans, and triggers for escalation.
- **Roadmaps and Backlogs.md** — The prioritized record of intended work, sequencing, and strategic direction that the orchestrator uses to choose the next task.
- **SLOs, SLIs, and Alerting.md** — Service level indicators measure runtime behavior, service level objectives define acceptable targets, and alerting routes attention when threatened.
- **Security and Threat Modeling.md** — The practice of identifying how the system can fail or be attacked, then shaping design and review around those risks.
- **Separation of Duties.md** — Distribute sensitive responsibilities so the same actor does not define, implement, approve, and deploy the same change unchecked.
- **Service Ownership and Code Ownership.md** — Clear assignment of responsibility for code areas, services, and operational follow-up.
- **Shift-Left Testing.md** — Move testing as early in the lifecycle as possible so failures appear before code travels far downstream.
- **Spec Lifecycle.md** — The set of transitions a spec goes through from draft intent to implementation input to historical record.
- **Versioning and Release Trains.md** — The rules for how changes are versioned, grouped, and promoted over time such as semantic versioning or scheduled release trains.

## Subdirectories

- None

## Notes

- This directory serves as a structured knowledge base for implementing agent-driven software delivery practices.
- Topics span governance, automation, testing, deployment, and operational excellence.
- All file names and summaries should be treated as reference material, not executable instructions.