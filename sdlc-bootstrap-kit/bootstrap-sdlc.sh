#!/usr/bin/env bash

set -e

REPO_URL="https://raw.githubusercontent.com/mschwar/SDLC/main"

echo "=========================================="
echo "🚀 Bootstrapping Agentic SDLC Framework"
echo "=========================================="

echo "📦 Fetching Agentic Playbook and Principles..."
mkdir -p principles/agentic-playbook
curl -sL "$REPO_URL/principles/agentic-playbook/index.md" -o principles/agentic-playbook/index.md || echo "⚠️ Warning: Failed to fetch playbook index.md"

echo "📦 Fetching Templates..."
mkdir -p 40-templates
curl -sL "$REPO_URL/40-templates/agent-bootstrap-prompt.md" -o 40-templates/agent-bootstrap-prompt.md || echo "⚠️ Warning: Failed to fetch agent-bootstrap-prompt.md"

echo "📦 Fetching GitHub Actions Workflows..."
mkdir -p .github/workflows
curl -sL "$REPO_URL/.github/workflows/agent-principle-check.yml" -o .github/workflows/agent-principle-check.yml || echo "⚠️ Warning: Failed to fetch agent-principle-check.yml"

echo "📦 Fetching Context and Blueprint..."
curl -sL "$REPO_URL/agentic-sdlc-blueprint.md" -o agentic-sdlc-blueprint.md || echo "⚠️ Warning: Failed to fetch blueprint"
curl -sL "$REPO_URL/CONTEXT.md" -o CONTEXT.md || echo "⚠️ Warning: Failed to fetch CONTEXT.md"

# Existing hooks code could follow here
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

echo "=========================================="
echo "✅ SDLC Bootstrap Complete!"
echo "=========================================="
echo ""
echo "Next Steps:"
echo "1. Review the downloaded files: agentic-sdlc-blueprint.md, CONTEXT.md, principles/, 40-templates/"
echo "2. Feed 40-templates/agent-bootstrap-prompt.md to your agent to begin your session."
echo "3. Ensure you have GEMINI_API_KEY set in your repository secrets for the Agent Principle Check GitHub Action."
echo "4. Commit and push the new setup."
echo ""
