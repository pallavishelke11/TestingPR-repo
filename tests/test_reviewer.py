from pr_review.reviewer import review_file, summarize


def test_python_function_requires_snake_case(tmp_path):
    path = tmp_path / "service.py"
    path.write_text("def getUserProfile():\n    return True\n", encoding="utf-8")
    findings = review_file(path)
    assert any(finding.category == "naming" and "snake_case" in finding.message for finding in findings)


def test_python_function_accepts_snake_case(tmp_path):
    path = tmp_path / "service.py"
    path.write_text("def get_user_profile():\n    return True\n", encoding="utf-8")
    findings = review_file(path)
    assert not any(finding.category == "naming" for finding in findings)


def test_javascript_identifier_requires_camel_case(tmp_path):
    path = tmp_path / "service.js"
    path.write_text("const user_profile = 1;\n", encoding="utf-8")
    findings = review_file(path)
    assert any("camelCase" in finding.message for finding in findings)


def test_detects_private_key(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("-----BEGIN PRIVATE KEY-----\n", encoding="utf-8")
    findings = review_file(path)
    assert any(finding.category == "security" and finding.severity == "error" for finding in findings)


def test_detects_generic_secret_assignment(tmp_path):
    path = tmp_path / "settings.py"
    path.write_text('api_key = "real-secret-value"\n', encoding="utf-8")
    findings = review_file(path)
    assert any(finding.category == "security" for finding in findings)


def test_console_log_is_flagged(tmp_path):
    path = tmp_path / "client.js"
    path.write_text("console.log('debug');\n", encoding="utf-8")
    findings = review_file(path)
    assert any(finding.category == "debugging" for finding in findings)


def test_summary_for_clean_review():
    assert "No automated issues found" in summarize([])
