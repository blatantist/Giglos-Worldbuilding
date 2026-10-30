#!/usr/bin/env python3
"""Copy a Claude Code session transcript into a wiki raw source.

Mechanical copy only: no model touches the text. Keeps Zach's typed turns and
Claude's visible replies; drops tool calls, tool output, thinking, subagent
traffic and app-injected messages. Pasted blocks are marked as attachments.

Modes:
  live   Run by the Stop hook after every turn. Reads the hook's JSON on stdin
         and (re)writes raw/_live/<session_id>.md. Staging only, not immutable.
  final  Run at wrap-up. Writes raw/chats/YYYY-MM-DD-chat-<CODE>.md once and
         refuses to overwrite an existing file (raw/ is immutable).
  off    Stop capturing the current session (/nocapture). Deletes its live copy.
  on     Resume capturing the current session (/capture).
  status Print whether the current session is being captured.

"Current session" for off/on/status is the most recently active transcript in
this project, i.e. the one that just received the command.

Usage:
  capture_session.py live < hook.json
  capture_session.py final --session <id> --code J --title "Short title"
  capture_session.py off | on | status [--session <id>]
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS = Path.home() / ".claude" / "projects"
PASTE_RE = re.compile(r'<pasted_content id="([^"]+)">\n?(.*?)\n?</pasted_content id="\1">', re.S)
NOISE_RE = re.compile(r"<(system-reminder|command-[a-z-]+|local-command-[a-z-]+)>.*?</\1>", re.S)
ATTACH = "**[Attachment: pasted text]** (not Zach's own words; tag nothing from it as [Z])"


LIVE = ROOT / "raw" / "_live"
OFF = LIVE / ".off"


def project_dir():
    return PROJECTS / re.sub(r"[^A-Za-z0-9]", "-", str(ROOT))


def current_session():
    found = sorted(project_dir().glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not found:
        sys.exit("no session transcripts found for this project")
    return found[-1].stem


def transcript_path(session_id):
    hits = list(PROJECTS.glob(f"*/{session_id}.jsonl"))
    if len(hits) != 1:
        sys.exit(f"expected one transcript for {session_id}, found {len(hits)}")
    return hits[0]


def human_text(content):
    if not isinstance(content, str):
        return None
    text = NOISE_RE.sub("", content)

    def quote(m):
        body = "\n".join("> " + ln if ln else ">" for ln in m.group(2).splitlines())
        return f"\n{ATTACH}\n\n{body}\n"

    text = PASTE_RE.sub(quote, text).strip()
    return text or None


def read_turns(path):
    turns = []  # [role, timestamp, [texts]]
    for line in path.open(encoding="utf-8"):
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            continue
        if d.get("isSidechain") or d.get("isMeta"):
            continue
        msg = d.get("message") or {}
        if d.get("type") == "user" and msg.get("role") == "user":
            text = human_text(msg.get("content"))
            if text:
                turns.append(["Human (Zach)", d.get("timestamp", ""), [text]])
        elif d.get("type") == "assistant" and isinstance(msg.get("content"), list):
            texts = [b.get("text", "") for b in msg["content"] if b.get("type") == "text"]
            texts = [t.strip() for t in texts if t.strip()]
            if not texts:
                continue
            if turns and turns[-1][0] == "Assistant (Claude)":
                turns[-1][2].extend(texts)
            else:
                turns.append(["Assistant (Claude)", d.get("timestamp", ""), texts])
    return turns


def render(session_id, turns, code, title, src):
    first = turns[0][1] if turns else ""
    last = turns[-1][1] if turns else ""
    out = [
        "---",
        f"source_code: {code}",
        f'title: "{title}"',
        f"session_id: {session_id}",
        f"created_at: {first}",
        f"updated_at: {last}",
        f"derived_from: Claude Code session transcript {src.name} (verbatim text; tool calls, tool output and thinking omitted)",
        f"turns: {len(turns)}",
        "---",
        "",
        f"# Chat {code}: {title}",
        "",
    ]
    for i, (role, ts, texts) in enumerate(turns):
        out += [f"## Turn {i} - {role}", f"<!-- {ts} -->", "", "\n\n".join(texts), ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["live", "final", "off", "on", "status"])
    ap.add_argument("--session")
    ap.add_argument("--code")
    ap.add_argument("--title")
    a = ap.parse_args()

    if a.mode in ("off", "on", "status"):
        sid = a.session or current_session()
        marker = OFF / sid
        if a.mode == "off":
            OFF.mkdir(parents=True, exist_ok=True)
            marker.touch()
            (LIVE / f"{sid}.md").unlink(missing_ok=True)
        elif a.mode == "on":
            marker.unlink(missing_ok=True)
        print(f"session {sid}: capture {'off' if marker.exists() else 'on'}")
        return

    if a.mode == "live":
        hook = json.load(sys.stdin)
        sid = hook["session_id"]
        if (OFF / sid).exists():
            return
        src = Path(hook.get("transcript_path") or transcript_path(sid))
        dest = LIVE / f"{sid}.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(sid, read_turns(src), "LIVE", "live session", src), encoding="utf-8")
        return

    if not (a.session and a.code and a.title):
        sys.exit("final needs --session, --code and --title")
    if (OFF / a.session).exists():
        sys.exit(f"capture is off for {a.session}; run 'on' first if this session should be a source")
    src = transcript_path(a.session)
    turns = read_turns(src)
    if not turns:
        sys.exit("no turns found")
    date = turns[0][1][:10]
    dest = ROOT / "raw" / "chats" / f"{date}-chat-{a.code}.md"
    if dest.exists():
        sys.exit(f"{dest} exists; raw/ is immutable")
    dest.write_text(render(a.session, turns, a.code, a.title, src), encoding="utf-8")
    print(dest.relative_to(ROOT))


if __name__ == "__main__":
    main()
