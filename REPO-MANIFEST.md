# Repo Manifest

## Purpose

The repo manifest is the machine-readable contract used to generate a repository baseline from a founder's intent.

For v1, it exists to keep the generator deterministic and scoped to one supported repo type instead of trying to infer everything from freeform prompts at runtime.

## V1 Rule

The manifest describes the repository that should be created.

It does not describe:

- milestone tasks
- implementation backlog
- dynamic gate outcomes
- release-by-release decisions

Those belong to planning, orchestration, and evidence systems built on top of the manifest.

## Canonical Files

- schema: [repo-manifest.schema.json](repo-manifest.schema.json)
- first example profile: [profiles/small-team-python-service.manifest.json](profiles/small-team-python-service.manifest.json)
- first supported workflow: [V1-GOLDEN-PATH.md](V1-GOLDEN-PATH.md)

## What The Manifest Must Answer

The manifest must tell the system:

1. which repo profile is being created
2. what the repo is called
3. what product or service it supports
4. what code shape should exist
5. which canonical docs must be generated
6. which quality commands and checks are part of the baseline
7. which environments the repo assumes
8. which review roles, gates, and release strategies the baseline needs

## Top-Level Sections

### `schema_version`

The manifest format version.

### `profile`

The chosen repo profile and the starter-kit lineage it comes from.

### `repository`

Core repository identity and default branch settings.

### `product`

The founder-facing product or service description.

### `service`

The technical service shape for the generated repo, including package/module naming and interface type.

### `docs`

The canonical docs and founder-facing surfaces the generated repo must contain.

### `quality`

The local checks, smoke tests, and CI baseline expected for the repo.

### `environments`

The environments the repo is expected to support and the approval posture for each.

### `controls`

The baseline review roles, supported gates, and release strategies for the repo type.

### `constraints`

Optional constraints that shape generation, such as data posture, deployment posture, or compliance expectations.

## Design Rules

1. Keep the manifest declarative.
2. Keep the first schema narrow and explicit.
3. Prefer fields that directly drive generated files or repo structure.
4. Do not bury policy logic in prose if it needs to be consumed by code.
5. Do not expand the schema for repo types that are out of v1 scope.

## V1 Success Criteria

The manifest layer is successful when:

- a founder prompt can be normalized into this format
- the manifest is enough to generate the first usable repo baseline
- the generated repo aligns with the small-team Python service golden path
- the manifest can be validated without human interpretation

## Immediate Next Build Step

Now that the schema exists, the next implementation step is to add manifest loading and generator scaffolding that can render the v1 repo baseline from this contract.
