# Product Backlog

## Completed MVP

- Changed-file review CLI
- Python snake_case and class PascalCase checks
- JavaScript/TypeScript camelCase checks
- Secret/private-key detection
- Debug and TODO findings
- Markdown review summary
- GitHub Actions workflow
- Unit tests

## Next priority

1. Support repository-specific rules loaded from `review-rules.json`
2. Review only added changed lines, not unchanged file content
3. Post inline PR comments on exact file lines
4. Avoid duplicate comments and update an existing bot comment
5. Add one clean/new-change summary per workflow run
6. Add GitHub branch-protection instructions and validation script
7. Add test fixtures for Python, JavaScript, TypeScript, and Terraform

## Later enhancements

- Java, C#, Go, and Terraform naming rules
- Complexity and duplicated-code analysis
- Dependency and license checks
- Test-coverage delta analysis
- Pull request size and risk score
- AI review with redaction and human approval
- Metrics dashboard
- Organization-level rule management
- Slack/Teams notifications

## Definition of Done

A backlog item is complete only when it has:

- Implemented code or configuration
- Passing focused tests
- Updated documentation
- Security review for sensitive behavior
- A demonstration example
- CI workflow validation
