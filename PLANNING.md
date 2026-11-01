# Project Planning

## Goal

Build an automated pull request review assistant that gives fast, consistent feedback before human review.

## Problem

Manual review often misses repeated naming, secret, debugging, and style problems. Review feedback can also vary between reviewers.

## MVP scope

### In scope

- GitHub pull request trigger
- Changed-file discovery
- Python naming conventions
- JavaScript and TypeScript naming conventions
- Secret and private-key detection
- Debug statement detection
- Line and file size suggestions
- Pull request summary comment
- GitHub Actions failure for security errors
- Automated unit tests

### Out of scope for MVP

- AI-generated semantic code review
- Automatic fixing of source code
- Pull request approval decisions
- Cross-file architectural analysis
- Multi-provider support

## Proposed milestones

1. Build rule engine with unit tests
2. Build command-line interface
3. Add GitHub Actions workflow
4. Add pull request summary comments
5. Add configurable rule profiles
6. Add inline comments and line-level findings
7. Add metrics and reviewer dashboard

## Example business rules

| Rule | Python | JavaScript/TypeScript |
|---|---|---|
| Function | snake_case | camelCase |
| Class/Component | PascalCase | PascalCase |
| Variable | snake_case | camelCase |
| Constant | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE |

## Success criteria

- Unit tests pass
- Every pull request receives a summary
- Secrets trigger errors
- Bad Python and JavaScript naming conventions are identified
- No tokens or AWS credentials are committed
- The workflow runs on pull request changes

## Risks and controls

| Risk | Mitigation |
|---|---|
| False positive secret detection | Use allowlists and human confirmation |
| Naming rule disagreement | Make rules configurable per repository |
| Workflow permissions too broad | Use read contents and write pull-request permissions |
| Large-code review performance | Review only changed files and later changed lines |
| Automated review replacing human judgment | Present automation as advisory evidence |
