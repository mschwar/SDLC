# Close a Gate

Use this when you want the agent to assemble a decision packet before you approve, hold, or reject the next stage of work.

## Step 1

Paste this into your CLI agent:

```text
You are my gate-closure operator inside the current repo.
I am a non-technical founder and I need a decision packet I can trust.

Gate context:
- Gate name: [GATE NAME]
- Decision requested: [APPROVE WHAT]
- Scope under review: [FEATURE / PHASE / RELEASE]
- Evidence to inspect: [DOCS / PR / TESTS / DEMO / "CURRENT REPO STATE"]

Task:
Review the current state and assemble a founder-readable gate packet.

I need:
- the purpose of this gate
- what is complete
- what is not complete
- the strongest evidence that matters
- the main risks if I approve now
- options: approve, hold, or reject
- your recommendation and why
- the exact next step for each option

Rules:
- Use real repo evidence or say it is missing.
- Be concrete, not diplomatic.
- If the repo needs a gate closeout note, create or update it.
- After you assemble the packet, stop and wait for my decision.

When done, report:
1. your recommendation
2. the approval question in one sentence
3. all changed files
```

## Step 2

After you review the packet, paste one of these:

Approve:

```text
Approve this gate. Record the decision in the repo, update the next-state docs, and begin the next recommended step. Report changed files when done.
```

Hold:

```text
Hold this gate. Record the blockers in the repo, turn them into the next tasks, and stop. Report changed files when done.
```

Reject:

```text
Reject this gate. Record why it was rejected, what must change before retry, and stop. Report changed files when done.
```
