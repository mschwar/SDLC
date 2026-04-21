# Handle a Hotfix

Use this when something important is broken now and you need a fast, safe response.

## Before You Start

Collect what you know:

- the symptom
- who is affected
- the environment
- when it started
- any logs, screenshots, or error text

## Copy-Paste Prompt

```text
You are my hotfix operator inside the current repo.
I am a non-technical founder and I need a safe, fast response.

Incident context:
- Symptom: [WHAT IS BROKEN]
- Impact: [WHO IS BLOCKED / REVENUE / TRUST / INTERNAL ONLY]
- Environment: [PRODUCTION / STAGING / OTHER]
- First known time: [TIME OR "UNKNOWN"]
- Evidence: [ERROR / LOG / SCREENSHOT / LINK / "NONE YET"]

Task:
Triage, contain, and fix this issue with the smallest safe change.

I need you to:
1. confirm severity
2. estimate blast radius
3. propose containment or rollback if that is safer than a rushed fix
4. reproduce the issue in the safest way available
5. implement the smallest viable fix
6. run targeted validation
7. prepare a short founder update and follow-up task list

Rules:
- Prefer safe containment over a risky broad change.
- Keep the scope tight to the incident.
- Record evidence and decisions in the repo.
- Stop and ask before any risky production action that needs approval.
- Be explicit about residual risk.

When done, report:
1. what happened
2. what you changed
3. how you validated the fix
4. what still needs watching
5. all changed files
```

## Optional Follow-Up

If the proposed hotfix plan looks right and it still needs to be released, paste this:

```text
Proceed with the approved hotfix release. Use the smallest safe rollout, update the repo with the release outcome, and report what shipped, residual risk, and the follow-up work that should happen after the incident is stable.
```
