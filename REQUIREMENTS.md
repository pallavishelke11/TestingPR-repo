# Requirements

## Functional requirements

| ID | Requirement |
|---|---|
| FR-01 | Trigger when a pull request is opened, synchronized, or reopened |
| FR-02 | Identify changed files between base and head commits |
| FR-03 | Check Python function and class naming |
| FR-04 | Check JavaScript and TypeScript identifier naming |
| FR-05 | Detect secret-like assignments and private keys |
| FR-06 | Detect debugging statements and TODO markers |
| FR-07 | Generate findings with severity, category, file, and line |
| FR-08 | Publish a Markdown summary |
| FR-09 | Add a comment to the pull request |
| FR-10 | Fail the workflow for configured error findings |
| FR-11 | Allow rule configuration for individual repositories |

## Non-functional requirements

| ID | Requirement |
|---|---|
| NFR-01 | Local review should start from one command |
| NFR-02 | Unit tests should be independent of GitHub and AWS |
| NFR-03 | The workflow should use least-privilege permissions |
| NFR-04 | The tool must not print or persist detected secret values |
| NFR-05 | Repeated scans should produce deterministic findings |
| NFR-06 | Review findings should not be treated as human approval |
| NFR-07 | The implementation should support additional language rules |

## Security requirements

- Repository secrets must never be included in source comments or summaries.
- Workflow tokens must use short-lived GitHub credentials.
- Error-level secret findings must block merge only where policy requires it.
- Production AI or external scanning services must not receive private source code without approval.

## Acceptance criteria

- Unit tests pass locally and in GitHub Actions.
- A pull request receives an automated review comment.
- Python and JavaScript naming examples produce findings.
- Private-key and secret-like assignments produce error findings.
- The workflow returns failure for configured security errors.
- Clean changes receive a no-findings summary.
