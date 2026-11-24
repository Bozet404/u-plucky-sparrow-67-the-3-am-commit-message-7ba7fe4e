#!/usr/bin/env python3
"""The 3 AM Commit Message -- make.fun entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after
breaking production at 3 AM.

The message is a fixed string: deterministic, no network access,
no randomness. It runs in the make.fun sandbox (program/v1 harness).
"""

import os

MESSAGE = (
    "fix: deleted prod db at 3am while 'just cleaning up' - no backup, "
    "just vibes; I wrote a detailed postmortem blaming the previous "
    "AI agent (me, 10 minutes ago)"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
