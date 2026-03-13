#!/usr/bin/env bash

set -e

echo "=========================================="
echo "🚀 Bootstrapping SDLC Guardrails & Hooks"
echo "=========================================="

# 1. Check for package.json
if [ ! -f "package.json" ]; then
  echo "📦 No package.json found. Initializing..."
  npm init -y
fi

# 2. Install Dependencies
echo "📦 Installing Husky and Commitlint..."
npm install --save-dev husky @commitlint/cli @commitlint/config-conventional

# 3. Setup Husky
echo "🪝 Initializing Husky..."
npx husky init

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 4. Create Git Hooks
echo "🛡️ Creating pre-commit, pre-push, and commit-msg hooks..."

cat << 'EOF' > .husky/pre-commit
#!/usr/bin/env sh

branch="$(git rev-parse --abbrev-ref HEAD)"

if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  echo "🚨 ERROR: Direct commits to the 'main' or 'master' branch are forbidden."
  echo "Please create a feature branch, commit your changes there, and open a Pull Request."
  echo "Example: git checkout -b feature/my-new-feature"
  exit 1
fi
EOF

cat << 'EOF' > .husky/pre-push
#!/usr/bin/env sh

branch="$(git rev-parse --abbrev-ref HEAD)"

if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  echo "🚨 ERROR: Direct pushes to the 'main' or 'master' branch are forbidden."
  echo "All changes must go through a Pull Request."
  exit 1
fi
EOF

cat << 'EOF' > .husky/commit-msg
#!/usr/bin/env sh

npx --no -- commitlint --edit "$1"
EOF

chmod +x .husky/pre-commit .husky/pre-push .husky/commit-msg

# 5. Copy Configuration & Templates
echo "📄 Copying config files and templates..."
cp "$SCRIPT_DIR/templates/commitlint.config.mjs" ./commitlint.config.mjs
cp "$SCRIPT_DIR/templates/GATE_CLOSEOUT.md" ./GATE_CLOSEOUT.md

mkdir -p .github/workflows
cp "$SCRIPT_DIR/templates/pr-checks.yml" .github/workflows/pr-checks.yml

echo "=========================================="
echo "✅ SDLC Bootstrap Complete!"
echo "=========================================="
echo ""
echo "Next Steps for the Repository Owner / Agent:"
echo "1. Append the contents of '$SCRIPT_DIR/templates/AGENTS-SDLC-SECTION.md' to this repository's AGENTS.md (or equivalent instruction file)."
echo "2. Add GATE_CLOSEOUT.md to the project scaffolding docs list in RUNBOOK.md."
echo "3. Run 'git add .' and commit the new hooks and configuration files."
echo ""
