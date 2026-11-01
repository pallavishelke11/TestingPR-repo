import argparse
import subprocess
import sys
from pathlib import Path

from .reviewer import review_files, summarize


def changed_files(base: str, head: str) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    return [Path(item.strip()) for item in result.stdout.splitlines() if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Automated pull request review")
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--fail-on-error", action="store_true")
    parser.add_argument("--output", help="Write the review summary to a Markdown file")
    args = parser.parse_args()

    paths = changed_files(args.base, args.head)
    findings = review_files(paths)
    summary = summarize(findings)

    print(summary)
    if args.output:
        Path(args.output).write_text(summary + "\n", encoding="utf-8")

    has_error = any(finding.severity == "error" for finding in findings)
    return 1 if args.fail_on_error and has_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
