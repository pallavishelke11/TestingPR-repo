import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    file: str
    line: int
    message: str

    def as_dict(self):
        return asdict(self)


SECRET_PATTERNS = {
    "AWS access key": r"AKIA[0-9A-Z]{16}",
    "Private key": r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "Generic API secret assignment": r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*[\"'][^\"']{8,}[\"']",
}


def _python_name_finding(name: str, file: str, line: int) -> Finding | None:
    if name.isupper() or re.fullmatch(r"_[a-z][a-z0-9_]*", name):
        return None
    if not re.fullmatch(r"[a-z][a-z0-9_]*", name):
        return Finding("warning", "naming", file, line, f"Python name '{name}' should use snake_case")
    return None


def _javascript_name_finding(name: str, file: str, line: int) -> Finding | None:
    if name.isupper() or name.startswith(("_", "$")):
        return None
    if not re.fullmatch(r"[a-zA-Z_$][a-zA-Z0-9_$]*", name):
        return Finding("warning", "naming", file, line, f"JavaScript name '{name}' is invalid")
    if "_" in name:
        return Finding("warning", "naming", file, line, f"JavaScript identifier '{name}' should use camelCase, not underscores")
    return None


def review_file(path: str | Path, content: str | None = None) -> list[Finding]:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8", errors="replace") if content is None else content
    lines = text.splitlines()
    findings: list[Finding] = []
    suffix = file_path.suffix.lower()

    if len(lines) > 500:
        findings.append(Finding("info", "maintainability", str(path), 1, f"File has {len(lines)} lines; consider splitting it into smaller modules"))

    for line_number, line in enumerate(lines, start=1):
        if len(line.rstrip("\n\r")) > 120:
            findings.append(Finding("info", "style", str(path), line_number, "Line exceeds 120 characters"))

        for category, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, line):
                findings.append(Finding("error", "security", str(path), line_number, f"Possible {category} detected; move it to a secret store"))

        if "console.log(" in line:
            findings.append(Finding("warning", "debugging", str(path), line_number, "Remove console.log before merging"))
        if re.search(r"\bprint\s*\(", line) and suffix == ".py":
            findings.append(Finding("info", "debugging", str(path), line_number, "Verify this print is intentional; use logging in production"))
        if "TODO" in line or "FIXME" in line:
            findings.append(Finding("info", "maintenance", str(path), line_number, "Unresolved TODO/FIXME marker"))

        if suffix == ".py":
            match = re.match(r"\s*(?:async\s+)?def\s+([A-Za-z_][A-Za-z0-9_]*)", line)
            if match:
                finding = _python_name_finding(match.group(1), str(path), line_number)
                if finding:
                    findings.append(finding)
            match = re.match(r"\s*class\s+([A-Za-z_][A-Za-z0-9_]*)", line)
            if match and not re.fullmatch(r"(?:[A-Z][a-z0-9]*)+", match.group(1)):
                findings.append(Finding("warning", "naming", str(path), line_number, f"Python class '{match.group(1)}' should use PascalCase"))

        if suffix in {".js", ".jsx", ".ts", ".tsx"}:
            match = re.search(r"\b(?:function|const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)", line)
            if match:
                finding = _javascript_name_finding(match.group(1), str(path), line_number)
                if finding:
                    findings.append(finding)

    return findings


def review_files(paths: Iterable[str | Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        if Path(path).is_file():
            findings.extend(review_file(path))
    return findings


def summarize(findings: Iterable[Finding]) -> str:
    findings = list(findings)
    counts = {severity: sum(1 for finding in findings if finding.severity == severity) for severity in ("error", "warning", "info")}
    lines = [
        "## Automated PR Review",
        "",
        f"**Errors:** {counts['error']}  |  **Warnings:** {counts['warning']}  |  **Suggestions:** {counts['info']}",
        "",
    ]
    if not findings:
        lines.append("No automated issues found. 👍")
        return "\n".join(lines)

    for finding in findings:
        icon = {"error": "🔴", "warning": "🟡", "info": "🔵"}[finding.severity]
        lines.append(f"- {icon} `{finding.file}:{finding.line}` **{finding.category}** — {finding.message}")
    lines.extend(["", "This review is advisory and should be checked by a human reviewer."])
    return "\n".join(lines)
