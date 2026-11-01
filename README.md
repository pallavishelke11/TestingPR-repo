# Automated Pull Request Review

This project automatically reviews pull requests and reports naming, security, debugging, maintenance, and style issues.

## What the MVP checks

- Python function names use `snake_case`
- Python classes use `PascalCase`
- JavaScript and TypeScript identifiers use `camelCase`
- AWS keys, private keys, and secret assignments do not appear in changed code
- `console.log`, print debugging, TODO markers, and very long lines are flagged
- Files longer than 500 lines receive a maintainability suggestion

## Recommended review policy

- Security errors block merge
- Naming warnings block merge only if the team enables strict naming rules
- Human reviewers still approve the final change
- Automated feedback does not replace testing or architectural review

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m pr_review.cli --base origin/main --head HEAD --fail-on-error --output pr-review.md
```

## GitHub setup

1. Push the project to a GitHub repository.
2. Open a pull request.
3. GitHub Actions runs `.github/workflows/pr-review.yml`.
4. The workflow posts the review summary on the pull request.
5. Review errors can be configured to block merge through a branch ruleset.

## Project documents

- `PLANNING.md` — scope, milestones, assumptions, and risks
- `REQUIREMENTS.md` — functional, non-functional, security, and acceptance requirements
- `ARCHITECTURE.md` — components, data flow, boundaries, and extensibility
- `DESIGN.md` — detailed rule and workflow design
- `DEVOPS.md` — CI/CD and GitHub branch protection
- `TESTING.md` — test strategy and manual validation
- `SECURITY.md` — secrets, permissions, and reporting process
- `RISK_REGISTER.md` — project risks and controls
- `PRODUCT_BACKLOG.md` — delivered scope and future enhancements
- `ACCEPTANCE_CRITERIA.md` — observable acceptance scenarios
- `RUNBOOK.md` — local operations and troubleshooting
- `CONTRIBUTING.md` — development and rule contribution process
- `CHANGELOG.md` — release history and known limitations
