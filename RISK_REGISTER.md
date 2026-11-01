# Risk Register

| Risk | Impact | Likelihood | Rating | Control / Owner |
|---|---|---|---|---|
| False positive secret findings | Developers lose trust | Medium | Medium | Review patterns, allowlists, and report evidence |
| Naming rules conflict with repository style | Widespread warnings | Medium | Medium | Repository-specific configuration |
| Workflow permissions are over-broad | Repository compromise impact | Low | High | Minimum GitHub permissions and peer review |
| External PR exposes workflow token | Confidential action access | Low | High | Do not grant secrets to fork workflows |
| Regex-only review misses complex bugs | Missed code defect | High | High | Label automation advisory and require human review |
| Large PR slows runner | Poor developer experience | Medium | Medium | Analyze changed files and later changed lines only |
| AI integration sends source externally | Data privacy breach | Medium | High | Require architectural/security approval and redaction |
| Users bypass required check | Security rule bypass | Low | High | Branch rulesets and protected workflow names |
| Report comments repeat on every commit | PR noise | Medium | Medium | Update existing bot comment or add comment throttling |

## High-risk controls

- Human approval remains mandatory.
- Secret review findings must not include detected secret values.
- Workflow changes require code-owner review.
- Organization repositories require merge protection.
