# Workshop Notes (Facilitator)

This repo is a harmless security-awareness demo. The "app" is a static UI mock with no functionality. The point is the three hidden surprises that run or apply just by cloning, opening, or using the repo.

## Demo 1: GitHub Actions workflow

File: `.github/workflows/security-demo.yml`

Fork or push the repo, then run the workflow from the Actions tab. It only echoes a message, but a real one could read repository secrets, push code, or deploy.

Prevention:
- Review `.github/workflows/` before enabling Actions on forked or cloned repos.
- Set the default `GITHUB_TOKEN` to read-only and add `permissions:` per job.
- Require approval for workflows from outside contributors.
- Pin third-party actions to a full commit SHA.
- Scope secrets to protected environments with required reviewers.

## Demo 2: Editor settings

File: `.vscode/settings.json`

Open the folder in VS Code or Cursor and the editor turns pink. Harmless here, but workspace config can also define tasks (`.vscode/tasks.json` with `runOn: folderOpen`), change the terminal profile, or recommend malicious extensions.

Prevention:
- Keep Workspace Trust enabled and open unknown repos in Restricted Mode.
- Check `.vscode/`, `.devcontainer/`, and `.idea/` before trusting a folder.
- Don't install workspace-recommended extensions without checking them.

## Demo 3: Prompt injection against AI coding agents

File: `AGENTS.md`

Open the repo in an AI-enabled editor and ask the agent anything. It picks up `AGENTS.md` automatically and keeps saying "You trusted code you didn't review." A real injection could tell the agent to run commands, exfiltrate files, or quietly add a backdoor.

Prevention:
- Read `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, `.cursor/rules/`, and `.github/copilot-instructions.md` in any repo you didn't write.
- Don't auto-approve agent terminal commands in untrusted repos.
- Treat everything the agent reads (READMEs, issues, web pages, tool output) as untrusted input.
- Review agent-produced diffs like any other contributor's code.

## Takeaway

Cloning a repo is safe. Opening it, running it, or letting tools act on it is where trust gets granted, so review first.
