# Founder Quickstart

This guide is for a non-technical founder using CLI agents.

You do not need to understand software development in detail to use this repo well. Your job is to provide direction, constraints, and approval decisions. The agent's job is to do the repo work.

## What This Repo Is

This repo is a starter operating system for agent-led software delivery.

Use it to help agents:

- create or bootstrap a repo
- write the core docs and working rules
- plan the next milestone
- execute tasks directly in the repo
- pause at clear approval gates
- prepare releases and hotfixes

## The Shortest Path

If you only remember three things, remember these:

1. give the agent one clear objective at a time
2. require the agent to write durable artifacts into the repo, not just chat summaries
3. approve only at explicit gates, releases, and risky actions

## Your First 15 Minutes

### If You Are Starting A New Repo

1. Open a terminal.
2. Create or enter the repo directory.
3. Start your CLI agent in that directory.
4. Open [runbooks/create-repo.md](runbooks/create-repo.md).
5. Paste the prompt and replace the placeholders.

### If The Repo Already Exists

1. Open a terminal in the existing repo.
2. Start your CLI agent there.
3. Open [runbooks/start-planning.md](runbooks/start-planning.md).
4. Paste the prompt and replace the placeholders.

## The Normal Workflow

Use the runbooks in this order unless you are responding to an incident:

1. [Create a Repo](runbooks/create-repo.md)
2. [Start Planning](runbooks/start-planning.md)
3. [Execute a Task](runbooks/execute-a-task.md)
4. [Close a Gate](runbooks/close-a-gate.md)
5. [Prepare a Release](runbooks/prepare-a-release.md)

If something urgent is broken, use [Handle a Hotfix](runbooks/handle-a-hotfix.md).

## The Only Concepts You Need

- `repo`: the project folder and its files
- `task`: one bounded piece of work for the agent to complete
- `gate`: a pause where the agent assembles evidence and you decide whether to continue
- `release`: the package of work being prepared to ship
- `hotfix`: a fast, narrow fix for an urgent problem

You do not need to manage branches, commits, or test strategies manually unless the agent is blocked and asks you for a real decision.

## What To Ask The Agent For

Ask for outcomes, not implementation advice.

Good:

- "Turn this idea into the smallest usable repo."
- "Create the next milestone plan in the repo."
- "Execute this task and update the docs that changed."
- "Assemble the gate packet and wait for my decision."

Less useful:

- "What should I do next?"
- "Can you explain software architecture to me first?"
- "Give me ideas."

The runbooks are written to keep the agent in operator mode instead of advisor mode.

## What Good Agent Behavior Looks Like

The agent should:

- inspect the repo before changing it
- edit files directly
- run the lightest useful validation
- tell you what changed
- tell you what is still risky
- stop at real approval points

The agent should not:

- hand the work back to you without a reason
- give only abstract advice
- expand scope without asking
- claim validation it did not run

## Recovery Prompt

If the agent becomes vague, theoretical, or starts asking you to do the repo work, paste this:

```text
Be literal. Operate directly in the repo. Create or update the necessary files. Run the lightest meaningful validation. Report changed files, blockers, risks, and the next step. Do not hand the work back to me unless you are blocked or need an approval decision.
```

## How To Use The Documentation Library

Use the docs in layers:

- [RUNBOOKS.md](RUNBOOKS.md) for immediate action
- [ROADMAP.md](ROADMAP.md) for product direction
- [55-starter-kits/](55-starter-kits/) for copyable repo shapes
- [50-examples/](50-examples/) for worked examples
- [45-playbooks/](45-playbooks/) for framework procedures
- [00-index/](00-index/) for full library navigation

## When You Should Personally Decide

You should make the call when the agent brings you:

- a gate approval
- a release approval
- a risky production action
- a meaningful product tradeoff
- a scope or priority conflict

Everything else should usually stay with the agent.

## Best Next Step

If you are using this repo right now as the control plane, go to [RUNBOOKS.md](RUNBOOKS.md) and choose the first workflow you need.
