# Founder Runbooks

These runbooks are for a non-technical founder working with CLI agents. Each one gives you a literal sequence and a copy-paste prompt so the agent can do the work in the repo instead of handing the work back to you.

If you are new to this repo, read [FOUNDER-QUICKSTART.md](FOUNDER-QUICKSTART.md) first.

## Before You Start

1. Open a terminal in the repo you want to work on.
2. Start your CLI agent in that repo.
3. Paste the full prompt from the runbook, then replace the bracketed placeholders.
4. Prefer one active objective at a time.
5. At gates, releases, and hotfixes, require evidence and an explicit recommendation before approving the next step.

If an agent becomes abstract or starts explaining instead of operating, paste this:

```text
Be literal. Work directly in the repo. Create or update the needed files. Run the lightest useful validation. Report changed files, blockers, and the next step. Do not hand the work back to me unless you are blocked or need an approval decision.
```

## Golden Path

1. [Create a Repo](runbooks/create-repo.md)
2. [Start Planning](runbooks/start-planning.md)
3. [Execute a Task](runbooks/execute-a-task.md)
4. [Close a Gate](runbooks/close-a-gate.md)
5. [Prepare a Release](runbooks/prepare-a-release.md)
6. [Handle a Hotfix](runbooks/handle-a-hotfix.md)

## What Good Looks Like

- The agent edits the repo directly.
- The agent writes durable artifacts in the repo instead of giving you a chat-only summary.
- The agent reports what it changed, what it validated, what is still risky, and what should happen next.
- You make decisions at clear approval points instead of managing every implementation detail.
