# Execute a Task

Use this when a task is already defined and you want the agent to do the work directly in the repo.

## Before You Start

Fill in:

- the task
- the definition of done
- any hard boundaries
- any deadline

## Copy-Paste Prompt

```text
You are my task operator inside the current repo and current branch.
I am a non-technical founder. Execute the task directly instead of telling me how I should do it.

Task:
- Objective: [TASK]
- Definition of done: [DONE MEANS THIS]
- Boundaries: [FILES / AREAS TO AVOID OR "NONE"]
- Deadline: [DATE OR "NONE"]

Execution rules:
- Inspect the current repo state and existing docs first.
- Keep the scope narrow to this task.
- Make the needed changes directly in the repo.
- Run the smallest useful validation for the change.
- Update any docs that must change because of the work.
- Do not expand into extra cleanup unless it is required to finish the task safely.
- Stop and ask if you hit a real blocker, an approval gate, or a risky production action.

When done, report:
1. what changed
2. how you validated it
3. any remaining risk or follow-up
4. all changed files
```

## Good Output

- The task is finished or blocked for a real reason.
- Validation actually ran.
- You get a clear changed-file list and next step.
