---
description: Stop capturing this session as a wiki source (deletes its live transcript copy)
allowed-tools: Bash(python3 scripts/capture_session.py:*)
---

Run `python3 scripts/capture_session.py off` and report the result in one line.

For the rest of this session: do not dispatch the wiki drafting subagent, and do not finalize or ingest this session at wrap-up. If a draft branch or worktree already exists for this session, tell Zach and ask whether to delete it; do not delete it on your own.
