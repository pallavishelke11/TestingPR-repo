# Security Policy

## Supported scope

This MVP scans source text locally during GitHub Actions execution. It does not send source or findings to an external model or service.

## Reporting vulnerabilities

For a vulnerability in this project, report it privately to the repository security contact. Do not create a public issue containing secrets, exploit details, or private source code.

## Secret handling

- Synthetic values must be used in tests and examples.
- Test patterns must never contain real keys or credentials.
- Workflow summaries must describe the finding without echoing secret values.
- Organization, repository, and environment secrets remain in GitHub's secret store.
- Forked pull requests must not receive privileged repository secrets.

## Workflow permissions

Use only:

```yaml
permissions:
  contents: read
  pull-requests: write
```

## Required safeguards before organization rollout

1. Add code-owner review for workflow changes.
2. Add branch protection for the review workflow and main branch.
3. Add organization-level secret scanning.
4. Add rule and allowlist validation.
5. Add audit logging for configuration changes.
6. Verify that external contributors cannot enable privileged workflow conditions.
