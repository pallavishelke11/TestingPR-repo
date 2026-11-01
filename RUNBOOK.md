# Operations Runbook

## Locally run a review

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
python -m pr_review.cli --base origin/main --head HEAD --fail-on-error
```

## Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| `origin/main` not found | Remote reference was not fetched | Run `git fetch origin` |
| Workflow does not start | Trigger or workflow syntax is incorrect | Verify the Actions workflow and pull-request event |
| No PR comment appears | Permission is missing | Enable `pull-requests: write` |
| Secret finding is false positive | Test fixture or allowed pattern matched | Add precise allowlist logic and regression test |
| Workflow fails on clean code | Error-level finding exists | Inspect the generated summary and finding line |
| CLI cannot import package | Editable package installation is missing | Run `python -m pip install -e .` |

## Updating a rule

1. Add an input fixture.
2. Add an expected unit test.
3. Update the rule implementation.
4. Run local tests.
5. Open a pull request.
6. Review automated findings and human feedback.

## Rollback

If a rule creates excessive false positives:

1. Disable branch protection enforcement if required to recover development.
2. Adjust or disable the rule.
3. Add a regression test.
4. Create a new pull request.
5. Re-enable enforcement after validation.
