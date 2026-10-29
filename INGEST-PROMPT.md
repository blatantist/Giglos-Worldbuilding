# First ingest prompt

Start a **fresh** Claude Code session in this folder and paste:

---

Use the karpathy-llm-wiki skill and follow CLAUDE.md exactly. It overrides the skill where they differ.

Ingest `Giglos Wiki Source.md` into the wiki. Do it in two steps:

**Step 1: plan only. Write nothing under `wiki/` yet.**
Copy the source verbatim into `raw/giglos/` (no cleanup of the body), then show me:
- the topic directories and page list, with `Kind` (stub/draft/stable) for each
- which source sections feed each page
- the stub pages (use the source's "Stub pages" list) and the seeds for `wiki/meta/tensions.md` and `wiki/meta/rejected-ideas.md`
- anything in the source you'd have to guess a tag for

**Step 2: after I approve the plan,** build the wiki. Keep every claim on its own line with its tag and chat codes; never merge claims with different tags; never promote a [C]; flag tensions and do not resolve them. Then report claim counts by tag per page, and run the lint script.

Do not update `wiki/index.md` or `wiki/log.md` until I approve the result.

---

Then open this folder as a vault in Obsidian (Open folder as vault). Wiki pages are plain markdown with relative links.
