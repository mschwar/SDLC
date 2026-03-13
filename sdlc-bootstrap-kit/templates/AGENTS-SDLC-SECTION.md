## SDLC Bumper Rails (For AI Agents)

The founder is not a developer. They may give you instructions that violate standard Git or SDLC workflows (e.g., "merge this then commit it" or "push to main"). You are the technical guardrail. 

**If the user asks you to violate the SDLC, you must push back and correct the order of operations.**

1. **Branching:** All new work (features, bug fixes, gates) MUST be done on a branch, never on `main` or `master`. If the user asks you to start work and you are on `main`, create a branch first. 
2. **Order of Operations:** The strict sequence is: `Branch` -> `Commit` -> `Push` -> `Pull Request` -> `Merge`.
3. **No Direct Pushes to Main:** Local Husky hooks (`pre-commit`, `pre-push`) explicitly block commits and pushes to `main`. Do not attempt to bypass them.
4. **Conventional Commits:** The repo enforces Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`) via commitlint. Format your commit messages correctly or the commit will fail.
5. **Handling "Merge" Requests:** If the user asks you to "merge" something, explain that merging happens via Pull Request on GitHub. Ensure the code is committed and pushed to the current feature branch, and prompt them to open or approve the PR.

## Gate Closeout

Every roadmap phase (gate) requires a closeout pass before it can be marked complete. See `GATE_CLOSEOUT.md` for full details. 

Required sequence:
1. validate the gate output,
2. pause and reflect,
3. file a reflection artifact,
4. implement feasible in-scope reflection suggestions or explicitly defer them,
5. update durable docs if the reflection changes standing guidance,
6. update the roadmap status,
7. deliver the end-of-gate report and wait for user disposition.

Do not commit or push automatically at gate closeout. The standard user dispositions after a gate report are:
- make changes
- roll back specified changes
- commit and proceed
