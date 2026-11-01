# Contributing

## Development setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e .
python -m pytest -q
```

## Adding a rule

1. Add a focused unit test that fails first.
2. Implement the rule in `src/pr_review/reviewer.py`.
3. Return a structured finding with file and line data.
4. Update `config/review-rules.json` if the rule is configurable.
5. Add documentation and a demonstration example.
6. Run the complete test suite.

## Review expectations

- No real credentials in tests, fixtures, or logs
- No external source transfer without review
- Avoid regex rules with unclear false-positive behavior
- Keep GitHub permissions at the minimum required level
- Human review remains the final approval authority
