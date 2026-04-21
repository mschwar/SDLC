from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
_PACKAGE_RE = re.compile(r"^[a-z_][a-z0-9_]*$")


class ManifestError(ValueError):
    """Raised when a repo manifest is malformed or unsupported."""


def _require_mapping(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ManifestError(f"{name} must be a JSON object.")
    return value


def _require_string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ManifestError(f"{name} must be a non-empty string.")
    return value


def _require_bool(value: Any, name: str) -> bool:
    if not isinstance(value, bool):
        raise ManifestError(f"{name} must be a boolean.")
    return value


def _require_string_list(value: Any, name: str) -> tuple[str, ...]:
    if not isinstance(value, list) or not value:
        raise ManifestError(f"{name} must be a non-empty list.")
    items: list[str] = []
    for index, item in enumerate(value):
        items.append(_require_string(item, f"{name}[{index}]"))
    return tuple(items)


@dataclass(frozen=True)
class Profile:
    id: str
    name: str
    starter_kit: str
    operating_model: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Profile":
        return cls(
            id=_require_string(raw.get("id"), "profile.id"),
            name=_require_string(raw.get("name"), "profile.name"),
            starter_kit=_require_string(raw.get("starter_kit"), "profile.starter_kit"),
            operating_model=_require_string(raw.get("operating_model"), "profile.operating_model"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "starter_kit": self.starter_kit,
            "operating_model": self.operating_model,
        }


@dataclass(frozen=True)
class Repository:
    name: str
    slug: str
    visibility: str
    default_branch: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Repository":
        slug = _require_string(raw.get("slug"), "repository.slug")
        if not _SLUG_RE.fullmatch(slug):
            raise ManifestError("repository.slug must contain only lowercase letters, numbers, and hyphens.")
        default_branch = _require_string(raw.get("default_branch"), "repository.default_branch")
        if default_branch != "main":
            raise ManifestError("Only main is supported as the default branch in v1.")
        visibility = _require_string(raw.get("visibility"), "repository.visibility")
        if visibility not in {"private", "public"}:
            raise ManifestError("repository.visibility must be private or public.")
        return cls(
            name=_require_string(raw.get("name"), "repository.name"),
            slug=slug,
            visibility=visibility,
            default_branch=default_branch,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "slug": self.slug,
            "visibility": self.visibility,
            "default_branch": self.default_branch,
        }


@dataclass(frozen=True)
class Product:
    name: str
    promise: str
    target_user: str
    first_release_outcome: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Product":
        return cls(
            name=_require_string(raw.get("name"), "product.name"),
            promise=_require_string(raw.get("promise"), "product.promise"),
            target_user=_require_string(raw.get("target_user"), "product.target_user"),
            first_release_outcome=_require_string(raw.get("first_release_outcome"), "product.first_release_outcome"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "promise": self.promise,
            "target_user": self.target_user,
            "first_release_outcome": self.first_release_outcome,
        }


@dataclass(frozen=True)
class Service:
    package_name: str
    module_name: str
    entrypoint: str
    language: str
    runtime: str
    interface: str

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Service":
        package_name = _require_string(raw.get("package_name"), "service.package_name")
        if not _PACKAGE_RE.fullmatch(package_name):
            raise ManifestError("service.package_name must be a valid Python package name.")
        module_name = _require_string(raw.get("module_name"), "service.module_name")
        if not _PACKAGE_RE.fullmatch(module_name):
            raise ManifestError("service.module_name must be a valid Python module name.")
        language = _require_string(raw.get("language"), "service.language")
        interface = _require_string(raw.get("interface"), "service.interface")
        if language != "python":
            raise ManifestError("Only python services are supported in v1.")
        if interface != "http":
            raise ManifestError("Only http interfaces are supported in v1.")
        if module_name != package_name:
            raise ManifestError("service.module_name must match service.package_name in v1.")
        return cls(
            package_name=package_name,
            module_name=module_name,
            entrypoint=_require_string(raw.get("entrypoint"), "service.entrypoint"),
            language=language,
            runtime=_require_string(raw.get("runtime"), "service.runtime"),
            interface=interface,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "package_name": self.package_name,
            "module_name": self.module_name,
            "entrypoint": self.entrypoint,
            "language": self.language,
            "runtime": self.runtime,
            "interface": self.interface,
        }


@dataclass(frozen=True)
class Docs:
    canonical_files: tuple[str, ...]
    founder_surfaces: tuple[str, ...]

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Docs":
        return cls(
            canonical_files=_require_string_list(raw.get("canonical_files"), "docs.canonical_files"),
            founder_surfaces=_require_string_list(raw.get("founder_surfaces"), "docs.founder_surfaces"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "canonical_files": list(self.canonical_files),
            "founder_surfaces": list(self.founder_surfaces),
        }


@dataclass(frozen=True)
class Quality:
    local_checks: tuple[str, ...]
    smoke_test_command: str
    ci_workflow: str
    uses_git_hooks: bool

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Quality":
        return cls(
            local_checks=_require_string_list(raw.get("local_checks"), "quality.local_checks"),
            smoke_test_command=_require_string(raw.get("smoke_test_command"), "quality.smoke_test_command"),
            ci_workflow=_require_string(raw.get("ci_workflow"), "quality.ci_workflow"),
            uses_git_hooks=_require_bool(raw.get("uses_git_hooks"), "quality.uses_git_hooks"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "local_checks": list(self.local_checks),
            "smoke_test_command": self.smoke_test_command,
            "ci_workflow": self.ci_workflow,
            "uses_git_hooks": self.uses_git_hooks,
        }


@dataclass(frozen=True)
class Environment:
    name: str
    purpose: str
    approval_required: bool
    rollback_required: bool

    @classmethod
    def from_dict(cls, raw: dict[str, Any], index: int) -> "Environment":
        name = _require_string(raw.get("name"), f"environments[{index}].name")
        if name not in {"local", "staging", "prod"}:
            raise ManifestError(f"Unsupported environment name: {name}")
        return cls(
            name=name,
            purpose=_require_string(raw.get("purpose"), f"environments[{index}].purpose"),
            approval_required=_require_bool(raw.get("approval_required"), f"environments[{index}].approval_required"),
            rollback_required=_require_bool(raw.get("rollback_required"), f"environments[{index}].rollback_required"),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "purpose": self.purpose,
            "approval_required": self.approval_required,
            "rollback_required": self.rollback_required,
        }


@dataclass(frozen=True)
class Controls:
    review_roles: tuple[str, ...]
    supported_gates: tuple[str, ...]
    release_strategies: tuple[str, ...]

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Controls":
        release_strategies = _require_string_list(raw.get("release_strategies"), "controls.release_strategies")
        for strategy in release_strategies:
            if strategy not in {"direct", "staged-rollout", "canary"}:
                raise ManifestError(f"Unsupported release strategy: {strategy}")
        return cls(
            review_roles=_require_string_list(raw.get("review_roles"), "controls.review_roles"),
            supported_gates=_require_string_list(raw.get("supported_gates"), "controls.supported_gates"),
            release_strategies=release_strategies,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "review_roles": list(self.review_roles),
            "supported_gates": list(self.supported_gates),
            "release_strategies": list(self.release_strategies),
        }


@dataclass(frozen=True)
class Constraints:
    data_class: str | None
    compliance_posture: str | None
    deployment_posture: str | None

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "Constraints":
        if raw is None:
            return cls(data_class=None, compliance_posture=None, deployment_posture=None)
        data_class = raw.get("data_class")
        if data_class is not None:
            data_class = _require_string(data_class, "constraints.data_class")
        compliance_posture = raw.get("compliance_posture")
        if compliance_posture is not None:
            compliance_posture = _require_string(compliance_posture, "constraints.compliance_posture")
        deployment_posture = raw.get("deployment_posture")
        if deployment_posture is not None:
            deployment_posture = _require_string(deployment_posture, "constraints.deployment_posture")
        return cls(
            data_class=data_class,
            compliance_posture=compliance_posture,
            deployment_posture=deployment_posture,
        )

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        if self.data_class is not None:
            payload["data_class"] = self.data_class
        if self.compliance_posture is not None:
            payload["compliance_posture"] = self.compliance_posture
        if self.deployment_posture is not None:
            payload["deployment_posture"] = self.deployment_posture
        return payload


@dataclass(frozen=True)
class RepoManifest:
    schema_version: str
    profile: Profile
    repository: Repository
    product: Product
    service: Service
    docs: Docs
    quality: Quality
    environments: tuple[Environment, ...]
    controls: Controls
    constraints: Constraints

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "RepoManifest":
        schema_version = _require_string(raw.get("schema_version"), "schema_version")
        if schema_version != "1.0":
            raise ManifestError("Only manifest schema version 1.0 is supported.")

        profile = Profile.from_dict(_require_mapping(raw.get("profile"), "profile"))
        if profile.operating_model != "small-team-service":
            raise ManifestError("Only the small-team-service operating model is supported in v1.")

        environments_raw = raw.get("environments")
        if not isinstance(environments_raw, list) or not environments_raw:
            raise ManifestError("environments must be a non-empty list.")
        environments = tuple(Environment.from_dict(_require_mapping(item, f"environments[{index}]"), index) for index, item in enumerate(environments_raw))

        return cls(
            schema_version=schema_version,
            profile=profile,
            repository=Repository.from_dict(_require_mapping(raw.get("repository"), "repository")),
            product=Product.from_dict(_require_mapping(raw.get("product"), "product")),
            service=Service.from_dict(_require_mapping(raw.get("service"), "service")),
            docs=Docs.from_dict(_require_mapping(raw.get("docs"), "docs")),
            quality=Quality.from_dict(_require_mapping(raw.get("quality"), "quality")),
            environments=environments,
            controls=Controls.from_dict(_require_mapping(raw.get("controls"), "controls")),
            constraints=Constraints.from_dict(raw.get("constraints")),
        )

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "schema_version": self.schema_version,
            "profile": self.profile.to_dict(),
            "repository": self.repository.to_dict(),
            "product": self.product.to_dict(),
            "service": self.service.to_dict(),
            "docs": self.docs.to_dict(),
            "quality": self.quality.to_dict(),
            "environments": [item.to_dict() for item in self.environments],
            "controls": self.controls.to_dict(),
        }
        constraints = self.constraints.to_dict()
        if constraints:
            payload["constraints"] = constraints
        return payload


def load_manifest(path: str | Path) -> RepoManifest:
    manifest_path = Path(path)
    try:
        raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"Manifest not found: {manifest_path}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"Manifest is not valid JSON: {manifest_path}") from exc

    if not isinstance(raw, dict):
        raise ManifestError("Manifest root must be a JSON object.")
    return RepoManifest.from_dict(raw)
