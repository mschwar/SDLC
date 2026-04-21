# Prepare a Release

Use this when work is nearly ready and you want the agent to prepare a release packet before anything is deployed.

## Before You Start

Fill in:

- the release name or version
- what should be included
- the target environment
- the target date

## Copy-Paste Prompt

```text
You are my release-prep operator inside the current repo.
I am a non-technical founder. Prepare this release for approval without deploying anything yet.

Release context:
- Release name or version: [VERSION]
- Scope: [WHAT IS INCLUDED]
- Target environment: [STAGING / PRODUCTION / OTHER]
- Target date: [DATE OR "AS SOON AS READY"]

Task:
Prepare the release packet and any repo artifacts needed for a release decision.

I need:
- what is included
- what is excluded
- validation that already exists
- any validation still missing
- known issues or release risks
- rollout plan
- rollback plan
- release notes draft
- the exact approval question I should answer

Rules:
- Verify from the repo and current branch instead of guessing.
- Write release artifacts into the repo, not just the chat.
- Do not deploy unless I explicitly approve it later.
- If a release should be blocked, say so plainly.

When done, report:
1. release readiness status
2. the approval question
3. the main release risk
4. all changed files
```

## Optional Follow-Up

If you decide to ship after reviewing the packet, paste this:

```text
The release is approved. Execute the release plan now, update the repo with the outcome, and report exactly what shipped, what was validated during release, and what needs monitoring next.
```
