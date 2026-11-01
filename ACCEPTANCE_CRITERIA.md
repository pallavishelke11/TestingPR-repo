# Acceptance Criteria

## MVP acceptance

- Given a pull request, when it is opened or synchronized, then the review workflow runs.
- Given a changed Python function named `getUserProfile`, then the review reports snake_case guidance.
- Given a changed JavaScript variable named `user_profile`, then the review reports camelCase guidance.
- Given private-key or secret-like text, then the review returns an error severity finding.
- Given a clean changed file, then the review reports no automated issues.
- Given findings, then the summary identifies severity, category, file, and line.
- Given a security error, then the workflow fails when `--fail-on-error` is enabled.
- Given completed review, then the workflow posts a Markdown comment to the pull request.

## Evidence required

- Unit test command output
- Example review output
- GitHub Actions workflow run link
- Pull request comment screenshot or exported Markdown
- Branch-protection verification
