#!/usr/bin/env python3
"""PreToolUse guard for Marathon GC (adapts the idea behind "Claude Code
Safety Net" and "Agent Guard" from awesome-claude-code).

Blocks (exit 2):
  - destructive shell commands (rm -rf on /, ~ or .., git push --force,
    git reset --hard, git clean -fdx, disk formatting)
  - git commit / push while staged files contain EIN-like, US phone-like or
    street-address-like strings (this repo is public)

Reads the hook JSON from stdin. Anything it does not recognise is allowed.
"""
import json
import re
import subprocess
import sys

DESTRUCTIVE = [
    (r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\s+(/|~|\.\.|\*|\$HOME)(\s|$)", "rm -rf on a root, home or parent path"),
    (r"\bgit\s+push\b.*(--force(?![-\w])|\s-f(?![-\w]))", "git push --force (use --force-with-lease, and only on your own branch)"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard discards work"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f[a-zA-Z]*d", "git clean -fd deletes untracked files"),
    (r"\b(mkfs|format)\b(\.\w+)?\s", "disk formatting"),
    (r"\bdd\s+.*of=/dev/", "dd onto a device"),
]

SECRETS = [
    (re.compile(r"\b\d{2}-\d{7}\b"), "EIN-like number"),
    (re.compile(r"\(?\b\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}\b"), "phone number"),
    (re.compile(r"\b\d{1,5}\s+[A-Z][a-z]+\s+(Ave|Avenue|St|Street|Rd|Road|Dr|Drive|Ln|Lane)\b"), "street address"),
]
ALLOW_MARKER = "marathon-guard: allow"


def block(reason: str) -> None:
    print(f"Blocked by marathon_guard: {reason}", file=sys.stderr)
    sys.exit(2)


def staged_text() -> str:
    try:
        return subprocess.run(
            ["git", "diff", "--cached", "-U0", "--no-color"],
            capture_output=True, text=True, timeout=15,
        ).stdout
    except Exception:
        return ""


def scan_for_private(diff: str) -> list[str]:
    hits = []
    for line in diff.splitlines():
        if not line.startswith("+") or line.startswith("+++") or ALLOW_MARKER in line:
            continue
        for pattern, label in SECRETS:
            if pattern.search(line):
                hits.append(f"{label}: {line[1:].strip()[:80]}")
    return hits


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except Exception:
        return
    if event.get("tool_name") != "Bash":
        return
    command = (event.get("tool_input") or {}).get("command", "")
    for pattern, reason in DESTRUCTIVE:
        if re.search(pattern, command):
            block(reason)
    if re.search(r"\bgit\s+(commit|push)\b", command):
        hits = scan_for_private(staged_text())
        if hits:
            block("this repo is public and the staged changes look private:\n  "
                  + "\n  ".join(hits[:10])
                  + f"\nRemove them (keep them in Marathon Brain), or add '{ALLOW_MARKER}' on a line that is a false positive.")


if __name__ == "__main__":
    main()
