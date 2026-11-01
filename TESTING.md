# Testing Strategy

## Unit tests

Unit tests validate individual rules without GitHub or AWS dependencies.

```powershell
python -m pytest -q
```

## Test cases

| Test | Expected result |
|---|---|
| Python `getUserProfile` | Warning with snake_case guidance |
| Python `get_user_profile` | No naming warning |
| JavaScript `user_profile` | Warning with camelCase guidance |
| Private key text | Security error |
| AWS-style secret assignment | Security error |
| `console.log` | Debugging warning |
| Clean file | No findings |

## CLI validation

Create two commits or branches, then run:

```powershell
python -m pr_review.cli --base origin/main --head HEAD --output pr-review.md
```

## GitHub integration validation

1. Push the project to GitHub.
2. Open pull request 1 with clean code.
3. Confirm no-error summary is posted.
4. Open pull request 2 with `console.log` or a fake secret.
5. Confirm warning/error placement and workflow behavior.
6. Add branch protection after false-positive review is complete.

## Security note

Never use real credentials in test files. Synthetic values should follow patterns that are clearly test data.
