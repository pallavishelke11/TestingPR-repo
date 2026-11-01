# DevOps and CI/CD

## Pipeline

The pull-request pipeline performs:

1. Checkout pull request code with full history
2. Set up Python 3.12
3. Install pytest dependencies
4. Identify changed files
5. Run automated review
6. Publish Markdown summary
7. Comment on the pull request
8. Fail only for configured security findings

## Required GitHub permissions

```yaml
permissions:
  contents: read
  pull-requests: write
```

## Branch protection recommendations

1. Require the `review` job to succeed.
2. Require at least one human approval.
3. Block direct pushes to `main`.
4. Require pull request branches to be current before merge.
5. Enable dismiss stale approvals after new commits.

## Secret handling

- Do not add repository secrets unless a future API integration requires them.
- Use `${{ github.token }}` for pull-request comments.
- Token permissions are scoped by the workflow declaration.
- Do not print environment variables in logs.

## Rollout plan

1. Run in advisory mode on one repository.
2. Review false positives for two weeks.
3. Move security errors to required checks.
4. Add repository-specific naming profiles.
5. Expand supported languages.
