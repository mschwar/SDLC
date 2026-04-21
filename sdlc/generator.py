from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from .manifest import RepoManifest

ROOT = Path(__file__).resolve().parent.parent
_STARTER_PACKAGE_NAME = "service_app"


class GeneratorError(ValueError):
    """Raised when repo generation cannot proceed."""


@dataclass(frozen=True)
class GenerationResult:
    output_dir: Path
    starter_kit: Path
    manifest_path: Path
    written_files: tuple[str, ...]


def generate_repo(manifest: RepoManifest, output_dir: str | Path, *, force: bool = False) -> GenerationResult:
    target = Path(output_dir).expanduser().resolve()
    starter_kit = (ROOT / manifest.profile.starter_kit).resolve()
    if not starter_kit.exists():
        raise GeneratorError(f"Starter kit not found: {starter_kit}")

    if target.exists():
        if any(target.iterdir()) and not force:
            raise GeneratorError(f"Output directory is not empty: {target}")
    else:
        target.mkdir(parents=True)

    shutil.copytree(starter_kit, target, dirs_exist_ok=True)

    if manifest.service.package_name != _STARTER_PACKAGE_NAME:
        _rename_package_dir(target, manifest.service.package_name)

    _replace_text(target, _STARTER_PACKAGE_NAME, manifest.service.package_name)
    written_files = list(_write_generated_files(target, manifest))
    manifest_path = target / "repo.manifest.json"
    manifest_path.write_text(json.dumps(manifest.to_dict(), indent=2) + "\n", encoding="utf-8")
    written_files.append(str(manifest_path.relative_to(target)))

    return GenerationResult(
        output_dir=target,
        starter_kit=starter_kit,
        manifest_path=manifest_path,
        written_files=tuple(sorted(set(written_files))),
    )


def _rename_package_dir(target: Path, package_name: str) -> None:
    original = target / _STARTER_PACKAGE_NAME
    renamed = target / package_name
    if not original.exists():
        raise GeneratorError(f"Starter package directory not found: {original}")
    if renamed.exists():
        raise GeneratorError(f"Target package directory already exists: {renamed}")
    original.rename(renamed)


def _replace_text(target: Path, old: str, new: str) -> None:
    if old == new:
        return
    for path in sorted(target.rglob("*")):
        if not path.is_file():
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if old not in content:
            continue
        path.write_text(content.replace(old, new), encoding="utf-8")


def _write_generated_files(target: Path, manifest: RepoManifest) -> tuple[str, ...]:
    written: list[str] = []
    docs = {
        "README.md": _render_readme(manifest),
        "AGENTS.md": _render_agents(manifest),
        "ARCHITECTURE.md": _render_architecture(manifest),
        "SCHEMA.md": _render_schema(manifest),
        "DECISIONS.md": _render_decisions(manifest),
        "ROADMAP.md": _render_roadmap(manifest),
        "ENVIRONMENTS.md": _render_environments(manifest),
        "SLOS.md": _render_slos(manifest),
        "RISK_REGISTER.md": _render_risk_register(manifest),
    }
    for name, content in docs.items():
        path = target / name
        path.write_text(content, encoding="utf-8")
        written.append(name)

    founder_surfaces = set(manifest.docs.founder_surfaces)
    if "FOUNDER-QUICKSTART.md" in founder_surfaces:
        path = target / "FOUNDER-QUICKSTART.md"
        path.write_text(_render_founder_quickstart(manifest), encoding="utf-8")
        written.append(path.name)
    if "RUNBOOKS.md" in founder_surfaces:
        written.extend(_write_runbooks(target, manifest))

    written.extend(_write_example_payloads(target, manifest))
    return tuple(written)


def _write_runbooks(target: Path, manifest: RepoManifest) -> tuple[str, ...]:
    written: list[str] = []
    runbooks_dir = target / "runbooks"
    runbooks_dir.mkdir(exist_ok=True)
    files = {
        target / "RUNBOOKS.md": _render_runbooks_index(manifest),
        runbooks_dir / "start-planning.md": _render_start_planning_runbook(manifest),
        runbooks_dir / "execute-a-task.md": _render_execute_task_runbook(manifest),
        runbooks_dir / "close-a-gate.md": _render_close_gate_runbook(manifest),
        runbooks_dir / "prepare-a-release.md": _render_release_runbook(manifest),
        runbooks_dir / "handle-a-hotfix.md": _render_hotfix_runbook(manifest),
    }
    for path, content in files.items():
        path.write_text(content, encoding="utf-8")
        written.append(str(path.relative_to(target)))
    return tuple(written)


def _write_example_payloads(target: Path, manifest: RepoManifest) -> tuple[str, ...]:
    examples_dir = target / "examples"
    examples_dir.mkdir(exist_ok=True)
    low_risk = {
        "objective": f"Ship the first low-risk improvement for {manifest.product.name}",
        "branch": f"feat/{manifest.repository.slug}-first-improvement",
        "environment": "dev",
        "acceptance_criteria": [
            "The contract reflects the intended service behavior",
            "Tests cover the intended path",
        ],
        "risk_level": "low",
        "customer_visible": False,
        "rollback_ready": False,
    }
    high_risk = {
        "objective": f"Prepare the first production-facing release for {manifest.product.name}",
        "branch": f"release/{manifest.repository.slug}-production-readiness",
        "environment": "prod",
        "acceptance_criteria": [
            "Release plan is explicit",
            "Rollback posture is documented",
            "Required approvals are identified",
        ],
        "risk_level": "high",
        "customer_visible": True,
        "rollback_ready": True,
    }
    payloads = {
        examples_dir / "low-risk-request.json": low_risk,
        examples_dir / "high-risk-request.json": high_risk,
    }
    written: list[str] = []
    for path, payload in payloads.items():
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        written.append(str(path.relative_to(target)))
    return tuple(written)


def _render_readme(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # {manifest.product.name}

        {manifest.product.promise}

        This repository was generated from the Agentic SDLC v1 repo manifest for the small-team Python service profile.

        ## Product

        - Target user: {manifest.product.target_user}
        - First release outcome: {manifest.product.first_release_outcome}
        - Service runtime: {manifest.service.runtime}
        - Interface: {manifest.service.interface}

        ## Quick Start

        ```bash
        python scripts/run_quality_checks.py
        python -m {manifest.service.package_name} plan examples/low-risk-request.json --pretty
        python scripts/smoke_test.py
        git config core.hooksPath .githooks
        ```

        ## Canonical Docs

        - `AGENTS.md`
        - `ARCHITECTURE.md`
        - `SCHEMA.md`
        - `DECISIONS.md`
        - `ROADMAP.md`
        - `ENVIRONMENTS.md`
        - `SLOS.md`
        - `RISK_REGISTER.md`

        ## Founder Surfaces

        - `FOUNDER-QUICKSTART.md`
        - `RUNBOOKS.md`

        ## Notes

        - This is a generated baseline. Replace placeholder targets, thresholds, and ownership details before shipping real changes.
        - The generated `repo.manifest.json` is the source-of-truth contract this baseline came from.
        """
    )


def _render_agents(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # AGENTS.md

        ## Mission

        Support {manifest.product.name}: {manifest.product.promise}

        ## Canonical Notes

        - `AGENTS.md`
        - `ARCHITECTURE.md`
        - `SCHEMA.md`
        - `DECISIONS.md`
        - `ROADMAP.md`
        - `ENVIRONMENTS.md`
        - `SLOS.md`
        - `RISK_REGISTER.md`

        ## Working Rules

        - branch from `origin/main`
        - one branch per task
        - use conventional commits
        - run `python scripts/run_quality_checks.py` before commit
        - update operating docs when release behavior changes
        - stop at approval gates for risky production actions
        """
    )


def _render_architecture(manifest: RepoManifest) -> str:
    package = manifest.service.package_name
    return dedent(
        f"""\
        # ARCHITECTURE.md

        ## System Overview

        {manifest.product.name} is a small-team Python service designed to {manifest.product.promise.lower()}.

        ## Components

        - `{package}.models`: request and response structures
        - `{package}.service`: planning and release logic
        - `{package}.server`: HTTP interface
        - `scripts/run_quality_checks.py`: blocking local validation
        - `scripts/smoke_test.py`: end-to-end sanity check

        ## Boundaries and Contracts

        - The service accepts JSON requests and returns deterministic planning or release outputs.
        - Repo behavior is governed by `SCHEMA.md`, `DECISIONS.md`, and `ENVIRONMENTS.md`.
        - Production-facing changes require explicit approval and rollback posture.

        ## Operational Constraints

        - Runtime: {manifest.service.runtime}
        - Interface: {manifest.service.interface}
        - Deployment posture: {manifest.constraints.deployment_posture or "founder-approved"}

        ## Open Questions

        - replace placeholder request and response contracts with domain-specific fields
        - replace example fixtures with real cases
        - tune service-level targets and risk posture for production use
        """
    )


def _render_schema(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # SCHEMA.md

        This generated baseline starts with a planning-style request contract for {manifest.product.name}.

        ## Request

        Required fields:

        - `objective`
        - `branch`
        - `environment`
        - `acceptance_criteria`

        Optional fields:

        - `risk_level`
        - `customer_visible`
        - `rollback_ready`

        ## Response

        - `review_roles`
        - `required_gates`
        - `release_strategy`
        - `blocking_issues`

        ## Replace Next

        Replace this generic contract with the real request and response shape for {manifest.product.first_release_outcome.lower()}.
        """
    )


def _render_decisions(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # DECISIONS.md

        ## Generated Baseline Decisions

        ### Deterministic Service Output
        - Status: accepted
        - Context: Planning and release logic should be testable and reproducible.
        - Decision: The same request should produce the same service output unless the contract changes.
        - Consequences: Contract changes must update docs, examples, and tests together.

        ### Explicit Production Approval
        - Status: accepted
        - Context: {manifest.product.name} may influence production-facing releases.
        - Decision: Risky production changes require explicit approval and rollback posture.
        - Consequences: The service should block or clearly flag production requests that are not rollback-ready.

        ### Founder-Readable Control Plane
        - Status: accepted
        - Context: This repo is intended to remain operable by a non-technical founder using agents.
        - Decision: Canonical docs and founder runbooks are part of the product surface, not optional extras.
        - Consequences: Workflow changes must update both operating docs and the generated guidance.
        """
    )


def _render_roadmap(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # ROADMAP.md

        ## Current Priorities

        - replace the starter contract with the real service contract
        - replace sample fixtures with domain-specific inputs
        - prove the first release outcome: {manifest.product.first_release_outcome}
        - validate release and rollback posture in staging

        ## Near-Term Milestones

        - baseline repo customized for {manifest.product.name}
        - first end-to-end planning path validated
        - release packet ready for founder review

        ## Risks and Constraints

        - generated defaults still need real domain thresholds
        - production behavior should remain approval-gated
        - docs and service logic must stay aligned as the contract evolves

        ## Deferred Work

        - deeper automation beyond the first service path
        - broader repo profiles

        ## Recently Completed

        - repo generated from `repo.manifest.json`
        """
    )


def _render_environments(manifest: RepoManifest) -> str:
    lines = ["# ENVIRONMENTS.md", "", "## Environment Policy", ""]
    for environment in manifest.environments:
        lines.extend(
            [
                f"### {environment.name.title()}",
                "",
                f"- purpose: {environment.purpose}",
                f"- approval required: {'yes' if environment.approval_required else 'no'}",
                f"- rollback required: {'yes' if environment.rollback_required else 'no'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def _render_slos(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # SLOS.md

        ## Targets

        - availability target for {manifest.product.name}
        - latency target for the primary {manifest.service.interface} workflow
        - correctness target for representative request fixtures

        ## Replace Next

        Replace these placeholders with real service-level targets before production use.
        """
    )


def _render_risk_register(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # RISK_REGISTER.md

        | ID | Risk | Impact | Mitigation |
        |----|------|--------|------------|
        | R-001 | service contract drifts from real workflow | medium | keep docs, examples, and tests aligned |
        | R-002 | production changes ship without rollback posture | high | block or flag prod when rollback is not ready |
        | R-003 | founder-facing guidance drifts from repo reality | medium | update runbooks and canonical docs when workflow changes |
        | R-004 | generated defaults remain in place too long | medium | replace placeholders during the first milestone for {manifest.product.name} |
        """
    )


def _render_founder_quickstart(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Founder Quickstart

        This repo was generated for {manifest.product.name}.

        You are expected to operate it through CLI agents, not by manually stitching together development workflow details.

        ## Product Snapshot

        - Promise: {manifest.product.promise}
        - Target user: {manifest.product.target_user}
        - First release outcome: {manifest.product.first_release_outcome}

        ## Shortest Path

        1. open this repo in your terminal
        2. start your CLI agent here
        3. read `RUNBOOKS.md`
        4. use `runbooks/start-planning.md` to define the first milestone
        5. use `runbooks/execute-a-task.md` for the next bounded task

        ## What You Should Personally Decide

        - gate approvals
        - release approvals
        - scope or priority changes
        - risky production actions
        """
    )


def _render_runbooks_index(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Founder Runbooks

        These runbooks are for operating {manifest.product.name} through CLI agents.

        ## Golden Path

        1. [Start Planning](runbooks/start-planning.md)
        2. [Execute a Task](runbooks/execute-a-task.md)
        3. [Close a Gate](runbooks/close-a-gate.md)
        4. [Prepare a Release](runbooks/prepare-a-release.md)
        5. [Handle a Hotfix](runbooks/handle-a-hotfix.md)

        ## Recovery Prompt

        ```text
        Be literal. Operate directly in the repo. Create or update the necessary files. Run the lightest meaningful validation. Report changed files, blockers, risks, and the next step. Do not hand the work back to me unless you are blocked or need an approval decision.
        ```
        """
    )


def _render_start_planning_runbook(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Start Planning

        ## Copy-Paste Prompt

        ```text
        You are my planning operator inside the current repo.
        I am a non-technical founder.

        Repo context:
        - Product: {manifest.product.name}
        - Promise: {manifest.product.promise}
        - First release outcome: {manifest.product.first_release_outcome}

        Task:
        Read only the repo context needed to understand the current state, then create or refresh the next founder-readable milestone plan in the repo.

        I need:
        - one clear milestone
        - success criteria
        - top risks
        - the first 3 to 5 tasks
        - the next approval gate

        Rules:
        - keep the milestone narrow
        - write the plan into the repo, not just the chat
        - reuse existing docs when cleaner than creating duplicates
        ```
        """
    )


def _render_execute_task_runbook(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Execute a Task

        ## Copy-Paste Prompt

        ```text
        You are my task operator inside the current repo and current branch.
        I am a non-technical founder. Execute the task directly instead of giving me implementation advice.

        Task:
        - Objective: [TASK]
        - Definition of done: [DONE MEANS THIS]
        - Boundaries: [FILES OR AREAS TO AVOID OR "NONE"]

        Repo context:
        - Product: {manifest.product.name}
        - Service package: {manifest.service.package_name}

        Rules:
        - inspect the current repo state first
        - keep scope narrow
        - run the smallest useful validation
        - update docs if behavior changed
        - stop only for a real blocker or approval gate
        ```
        """
    )


def _render_close_gate_runbook(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Close a Gate

        ## Copy-Paste Prompt

        ```text
        You are my gate-closure operator inside the current repo.
        I am a non-technical founder and I need a decision packet I can trust.

        Gate context:
        - Gate name: [GATE NAME]
        - Scope under review: [FEATURE / PHASE / RELEASE]
        - Evidence to inspect: [DOCS / TESTS / DEMO / CURRENT REPO STATE]

        Task:
        Assemble a founder-readable gate packet for {manifest.product.name}.

        I need:
        - what is complete
        - what is not complete
        - strongest evidence
        - main risks
        - your recommendation
        - the exact approval question

        Rules:
        - use real repo evidence or say it is missing
        - be concrete
        - stop after assembling the packet and wait for my decision
        ```
        """
    )


def _render_release_runbook(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Prepare a Release

        ## Copy-Paste Prompt

        ```text
        You are my release-prep operator inside the current repo.
        I am a non-technical founder. Prepare this release for approval without deploying it yet.

        Release context:
        - Release name or version: [VERSION]
        - Scope: [WHAT IS INCLUDED]
        - Target environment: [STAGING / PROD]

        Task:
        Prepare a founder-readable release packet for {manifest.product.name}.

        I need:
        - included scope
        - excluded scope
        - existing validation
        - missing validation
        - rollout plan
        - rollback plan
        - release notes draft
        - the exact approval question

        Rules:
        - verify from the repo instead of guessing
        - write release artifacts into the repo
        - do not deploy until I explicitly approve it
        ```
        """
    )


def _render_hotfix_runbook(manifest: RepoManifest) -> str:
    return dedent(
        f"""\
        # Handle a Hotfix

        ## Copy-Paste Prompt

        ```text
        You are my hotfix operator inside the current repo.
        I am a non-technical founder and I need a safe, fast response.

        Incident context:
        - Symptom: [WHAT IS BROKEN]
        - Impact: [WHO IS AFFECTED]
        - Environment: [PROD / STAGING / OTHER]
        - Evidence: [ERROR / LOG / SCREENSHOT / NONE YET]

        Task:
        Triage, contain, and fix this issue with the smallest safe change for {manifest.product.name}.

        I need:
        - severity estimate
        - blast radius
        - containment or rollback recommendation
        - smallest viable fix
        - targeted validation
        - founder update

        Rules:
        - prefer safe containment over broad risky changes
        - keep scope tight to the incident
        - stop before risky production actions that need approval
        ```
        """
    )
