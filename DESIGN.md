# Technical Design

## Architecture

```text
GitHub Pull Request
        |
GitHub Actions workflow
        |
Reviewer CLI
        |
Changed-file detection
        |
Rule engine
        |
Markdown report
        |
GitHub PR comment + workflow status
```

## Components

### Rule engine

`reviewer.py` scans text files and returns structured findings. Each finding includes severity, category, file, line, and message.

### CLI

`cli.py` discovers changed files with `git diff`, runs the rule engine, prints Markdown, and optionally writes a report.

### GitHub workflow

`pr-review.yml` runs on pull-request events, generates the summary, posts it to the pull request, and fails for error-level security findings.

## Severity model

| Severity | Meaning | Policy |
|---|---|---|
| Error | Security or merge blocker | Fail workflow |
| Warning | Convention violation | Show clearly, warn by policy |
| Info | Improvement suggestion | Advisory |

## Naming rules

- Python functions and variables: `snake_case`
- Python classes: `PascalCase`
- JavaScript and TypeScript functions/variables: `camelCase`
- React components: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

## Future interface

The MVP is CLI and GitHub Actions first. A later dashboard can provide repository configuration, rule profiles, trend reports, and deployment metrics.

## Security design

- Never print or commit credentials
- Use GitHub-provided short-lived workflow token
- Grant minimum pull-request and content permissions
- Review external PRs carefully because repository secrets are not available to untrusted forks
- Store organization rules outside application code

## Failure behavior

- No changed files: return clean review
- Invalid file encoding: read with replacement encoding and continue
- Secret detected: return error finding
- Git diff failure: show command error and exit non-zero
- Reporting failure: workflow reports diagnostics instead of silently succeeding
