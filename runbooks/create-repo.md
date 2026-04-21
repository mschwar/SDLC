# Create a Repo

Use this when you are starting from an idea and want a CLI agent to stand up the first usable version of the repository.

## Step 1

If you are starting from nothing, run this in your terminal first:

```bash
mkdir YOUR_REPO_NAME
cd YOUR_REPO_NAME
git init -b main
curl -sL https://raw.githubusercontent.com/mschwar/SDLC/main/sdlc-bootstrap-kit/bootstrap-sdlc.sh | bash
```

If the repo already exists, just `cd` into it.

## Step 2

Paste this into your CLI agent:

```text
You are my repo setup operator inside the current working directory.
I am a non-technical founder using a CLI agent.

Business context:
- Product name: [PRODUCT NAME]
- One-sentence product promise: [ONE SENTENCE]
- Who it serves: [CUSTOMER]
- First release outcome: [WHAT MUST BE TRUE]
- Constraints: [BUDGET / PLATFORM / COMPLIANCE / "NONE YET"]

Task:
Turn this repo into the smallest practical starting point for this product.
I need a founder-usable repo that supports planning, bounded task execution, approval gates, release prep, and hotfix handling.

Rules:
- Inspect the current repo state before changing anything.
- Prefer a small working setup over framework-heavy ceremony.
- Write founder-facing docs and starter artifacts directly in the repo.
- Create missing files when they materially help.
- Run the lightest meaningful validation.
- Stop only if you are blocked or need a real decision from me.

When done, report:
1. what you created
2. how I start or inspect the project
3. the first task I should run next
4. all changed files
```

## Good Output

- The repo has a small, understandable starting structure.
- There is at least one clear next task.
- The agent tells you exactly what changed and how to continue.
