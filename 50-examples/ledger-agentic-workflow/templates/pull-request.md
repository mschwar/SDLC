# Pull Request

Title: `<title>`
Status: `draft | ready-for-review`
Branch: `<branch-name>`
Base: `origin/main`
Handoff: `<docs/handoffs/active/... or none>`
Related issue: `<issue or none>`

## Summary

<One short paragraph describing what this PR does.>

## Changes

- <change area>
- <change area>

## Validation

- `<command>` — <result>
- `<command>` — <result>

## Branch Proof

- `git rev-parse HEAD`
- `git rev-parse origin/main`
- `git log --oneline origin/main..HEAD`
- `git diff --stat origin/main..HEAD`
- `git status --short`

## Validation Side Effects

- `none` or list any tracked files touched by validation

## Reviewer Focus

- <logic, risk, or behavior to inspect carefully>

## Risks / Notes

- <risk, assumption, or note>

## Deferred Follow-Ups

- `none` or list any intentionally deferred follow-up work

## Checklist

- [ ] Scope matches the handoff
- [ ] Branch started from `origin/main`
- [ ] Only allowed files are included
- [ ] Validation was run
- [ ] Validation side effects are disclosed
- [ ] No unrelated files were bundled
- [ ] PR body matches the final diff
