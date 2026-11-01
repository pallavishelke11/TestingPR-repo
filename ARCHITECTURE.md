# Architecture

## System context

The system reviews source changes submitted through GitHub pull requests and returns findings without changing repository code.

```text
Developer
   |
   v
Pull Request --> GitHub Actions --> PR Reviewer CLI
                                     |
                                     v
                              Changed-file scanner
                                     |
                                     v
                               Rule engine
                                     |
                         +-----------+-----------+
                         |                       |
                         v                       v
                 Pull request comment      Workflow result
```

## Runtime components

| Component | Responsibility |
|---|---|
| GitHub Actions | Detect pull request events and execute the review |
| CLI | Read arguments and discover changed files |
| Reviewer engine | Apply naming, security, style, and maintenance rules |
| Markdown formatter | Convert findings into human-readable output |
| Unit tests | Verify rule behavior independently of GitHub |

## Data flow

1. A pull request is opened or updated.
2. GitHub checks out the pull request branch and complete history.
3. The CLI requests a diff between base and head commits.
4. The reviewer reads only changed source files.
5. Findings are grouped by severity and category.
6. Markdown is added to the job summary and pull request comment.
7. Error-level findings fail the review job.

## Security boundaries

- GitHub validates pull request and repository permissions.
- The workflow grants read access to repository contents.
- The workflow grants write access only to pull-request comments.
- Real secrets are not placed in the rule engine or test files.
- Fork pull requests do not receive access to organization secrets.

## Extensibility

Later components can include:

- A language analyzer abstraction for Python, JavaScript, TypeScript, Java, and Terraform
- A repository-specific rules configuration service
- Inline GitHub comment annotations
- AI-assisted semantic review with mandatory human confirmation
- Metrics collection for findings, false positives, and merge outcomes
- A dashboard for repository administrators

## Non-functional requirements

- Changed-file review must complete quickly for normal pull requests.
- Rule execution must be deterministic.
- Findings must include severity, category, file, and line.
- The tool must fail safe when the diff cannot be read.
- The automated reviewer must not approve or merge a pull request.
