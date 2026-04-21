# Start Planning

Use this when the repo exists but you need the agent to turn an idea, request, or rough direction into a concrete first milestone.

## Before You Start

Write down these five inputs:

- the product or feature you want to plan
- the user problem
- the outcome you want
- the main constraint
- the deadline, if there is one

## Copy-Paste Prompt

```text
You are my planning operator inside the current repo.
I am a non-technical founder and I want a practical plan, not a theory document.

Planning context:
- What we are planning: [FEATURE / PRODUCT / MILESTONE]
- User problem: [PROBLEM]
- Desired outcome: [OUTCOME]
- Main constraint: [CONSTRAINT]
- Deadline: [DATE OR "NONE"]

Task:
Read only the repo context needed to understand the current state, then create or refresh a founder-readable plan for the next milestone.

I need:
- one clear milestone
- success criteria
- the top risks
- the first 3 to 5 tasks in the order they should happen
- the next approval gate
- the smallest set of decisions you still need from me

Rules:
- Prefer one milestone over a giant roadmap.
- Keep the plan actionable and literal.
- Write the plan into the repo, not just the chat.
- Reuse existing docs when that is cleaner than making duplicates.
- If something important is missing, name the gap plainly.

When done, report:
1. the milestone
2. the first tasks
3. the next gate
4. all changed files
```

## Good Output

- You can see the next milestone in plain English.
- The first tasks are small enough to hand to an agent.
- The next approval point is explicit.
