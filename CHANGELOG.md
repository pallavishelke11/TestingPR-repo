# Changelog

## Unreleased

### Added

- Pull request review rule engine
- Python, JavaScript, and TypeScript naming checks
- Secret and private-key detection
- Markdown review summaries
- GitHub Actions pull request workflow
- Unit tests and example files
- Planning, design, DevOps, requirements, security, risk, and testing documents

### Changed

- Automated findings use error, warning, and information severity.
- Security errors are intended to be merge blockers when enabled by branch policy.

### Known limitations

- Regex-based checks may create false positives.
- Inline line comments are not yet posted.
- Repository-specific rules are not yet loaded by the CLI.
- Language support is currently limited.
- AI semantic review is intentionally not included in the MVP.
