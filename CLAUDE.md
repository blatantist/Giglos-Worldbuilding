# Giglos Wiki: Schema

Personal worldbuilding + game-design wiki: the Giglian species (biology, ecology, psychology,
society, law, religion, conlang in progress), a planned RPG set in that world, and a GOAP
multi-agent NPC architecture. The wiki organizes my thinking.

**Never write game code or implementation.** Design discussion and prose only.
(Wiki tooling such as `scripts/capture_session.py` is not game code.)

This file extends the `karpathy-llm-wiki` skill (`.agents/skills/karpathy-llm-wiki/SKILL.md`).
Where this file and the skill disagree, **this file wins**. The overrides are listed explicitly below.

## Layout

- `raw/<topic>/` Immutable sources. Never edit, rename, or delete after capture.
- `raw/chats/YYYY-MM-DD-chat-<CODE>.md` Chat transcripts, the primary sources. Compiled docs in `raw/giglos/` are derived from them.
- `raw/_live/<session_id>.md` Live staging copy of the current Claude Code session, rewritten after every turn by the Stop hook. Not a source, not immutable, gitignored.
- `scripts/capture_session.py` Mechanical transcript copier (`live` for the hook, `final` at wrap-up).
- `wiki/meta/sources.md` Chat codes (A, B, … I, then J, K, …) with title, date and transcript link.
- `wiki/<topic>/<page>.md` LLM-maintained pages. One topic level only, kebab-case names.
- `wiki/index.md` Catalog (skill format). Summary column also states counts, e.g. `3 [OPEN], 2 [Z?], 1 [C]`.
- `wiki/log.md` Append-only (skill format).
- `wiki/meta/tensions.md` Registry of contradictions (see Contradictions).
- `wiki/meta/rejected-ideas.md` Registry of [X] items (see Rejected ideas).
- `Giglos Wiki Source.md` in the project root is the original file. Ingest copies it into `raw/`; leave the original alone.

## Provenance tags (never alter, never invent)

| Tag | Meaning | Status |
|---|---|---|
| [Z] | my decision | Canon (working canon) |
| [Z?] | my tentative idea | Tentative canon, always flagged |
| [C] | Claude suggestion I never confirmed | **NOT canon.** Never stated as fact |
| [C+] | Claude suggestion I built on | Likely canon, flagged for my confirmation |
| [X] | rejected or superseded | History only |
| [OPEN] | unresolved question | Open question |

Raw files write tags escaped (`\[Z\]`). Wiki pages write them plain (`[Z]`).
Chat codes like `(C)`, `(A, D)`, `(M)` that follow a claim in the source are source anchors. Keep them.

## Claim format

- One atomic claim per line: `- <claim> [TAG] (<chat codes>)`
- Every claim line carries exactly one tag and the source's chat codes.
- Copy the tag from the source verbatim. If a source line has no tag, write `[UNTAGGED]` and ask me. Never guess.
- Keep the source's wording close. Do not generalize, polish, or "distill" a claim into something stronger or broader.
- **Never merge, blend, or summarize claims with different tags into one line or sentence.**
  A [C] line stays its own line even if a [Z] line says something similar.
- Prose in Overview sections may only describe [Z] and [C+] claims, and must link to the claim line.
  Anything resting on [Z?], [C], or [OPEN] must say so inline.
- Only I change a tag. When I say "promote X to [Z]", change the tag, append `(was [C], promoted YYYY-MM-DD)`, log it.
- A new claim must never cite a [C] line as its basis without that dependency stated in the claim.

## Tagging from transcripts

Transcripts carry no tags, so tags are inferred from who said what. Every inferred tag must be checkable against a turn.

- [Z]: Zach states or decides it in a Human turn. [Z?] when he hedges ("idk", "maybe", "not final", "throwing at the wall").
- [C]: Claude proposes it in an Assistant turn and Zach does not take it up.
- [C+]: Claude proposes it and Zach builds on it or reacts positively ("I like that", "yea") without clearly adopting it. Agreement alone is [C+], not [Z].
- [X]: Zach rejects or replaces an earlier idea, his or Claude's. Record what replaced it.
- [OPEN]: a question either side raises that stays unanswered by the end of the session.
- Attachment blocks (pasted text, files) are never Zach's words. Tag nothing from them as [Z].
- Chat codes for claims from a transcript are its code; the verification report also cites turns (e.g. `J14`).
- A one-sentence summary written by Claude is not a claim. Do not tag it [Z] because it summarizes Zach.

## Page format

Skill header, plus one line:

```
# Title
> Sources: <source name, date>
> Raw: [<source>](../../raw/<topic>/<file>.md)
> Updated: YYYY-MM-DD
> Kind: stub | draft | stable
```

Body sections, in this order, omitting empty ones (except on stubs):
`Overview` · `Canon` ([Z], [C+]) · `Tentative` ([Z?]) · `Unconfirmed` ([C]) · `Open questions` ([OPEN]) · `History` ([X]) · `See Also`.
A claim goes in the section matching its tag.

Skill override: the template says "distill, do not copy verbatim". Ignore that for claim lines (see Claim format).

## Stubs

- Thin topics get a page with `Kind: stub` even if almost empty: planet, other species and flora, conlang phonology, characters, endings, and every topic the source lists under "Stub pages".
- A stub holds its [OPEN] questions and links to the pages that touch it. Its Raw field points at the source section it came from.
- Lint never reports a stub as a problem. Never pad a stub with invented content.

## Contradictions

- Detect and record. **Never resolve, reconcile, or edit either claim.**
- Mark both claims with the skill's `> **Status: Disputed**` block and cross-link the pages.
- Add an entry to `wiki/meta/tensions.md`: both claims quoted with tags and chat codes, pages involved, `status: unresolved`.
- Seed `tensions.md` at first ingest from the source's "Tensions to flag, not resolve" section (e.g. original plot premise vs later Founder lore).
- Only I mark a tension resolved, and I say how.

## Rejected ideas

- [X] claims are never deleted or rewritten. Keep them in the page's `History` section with the reason and what superseded them, and list them in `wiki/meta/rejected-ideas.md`.
- Seed `rejected-ideas.md` from the source's "Rejected or superseded ideas" section.
- Before writing any new claim, check `rejected-ideas.md`. If it matches an [X] item, flag it to me instead of adding it.
- Use the skill's `Status: Outdated (date)` block only where a claim was superseded after being written into the wiki, never to hide history.

## Session ingest (Claude Code sessions in this folder; overrides the skill's flow)

Discussing the project here feeds the wiki automatically. `main` only changes at wrap-up, after verification.

**Capture.** The Stop hook runs `scripts/capture_session.py live` after every turn and rewrites `raw/_live/<session_id>.md`. Never hand-edit or paraphrase a transcript.
`/nocapture` turns capture off for the current session and deletes its live copy; while off, no drafting and no wrap-up ingest. `/capture` turns it back on (the live copy is rebuilt from the whole session, including turns sent while off).

**Draft (during the session).**
- The main agent dispatches a background drafting subagent whenever the discussion settles or shifts something: a decision, a correction, a surprising idea, a new open question. Its own judgment; not every turn.
- On the first dispatch, assign the next free chat code (after the last one in `wiki/meta/sources.md`) and create branch `session/YYYY-MM-DD-<CODE>` in a git worktree at `../giglos-draft-<CODE>`. All drafting happens there; never on `main`.
- The drafter reads the live transcript and writes claims on the branch, following every rule in this file (claim format, tags from transcripts, sections, tensions, rejected-ideas check, grounding against the live file).
- Drafts may be wrong. When a later turn corrects an earlier claim, revise the draft; if Zach rejected the idea, it goes to History as [X].
- The drafter keeps `PROPOSAL.md` at the worktree root: changed pages, and every doubtful item with its turn reference (inferred tags it is unsure of, new tensions, [X] collisions, stubs that could grow).
- The main agent keeps discussing and does not write under `wiki/` itself.

**Wrap-up (when Zach says "wrap up" or `/wrap`).**
1. Finalize: `scripts/capture_session.py final --session <id> --code <CODE> --title "<title>"` writes `raw/chats/YYYY-MM-DD-chat-<CODE>.md` (immutable from then on). Point the branch's Raw fields at it.
2. Verify every claim the session added or changed against the final transcript: a [Z] needs a Human turn that says it; a [C] or [C+] needs an Assistant turn. Run lint.
3. Ask Zach about every doubtful item and every verification mismatch, in one batch, with turn references and proposed answers. Apply his answers.
4. Publish: add the code to `wiki/meta/sources.md`, update `wiki/index.md` and `wiki/log.md`, commit, fast-forward `main`, remove the worktree.
5. If nothing worth a wiki change came up, still finalize the transcript and log `ingest | no material: <raw path>`.

## External ingest (sources not from a Claude Code session here: claude.ai exports, notes, papers)

1. Fetch: copy the source into `raw/<topic>/YYYY-MM-DD-slug.md` with the skill's metadata header. **Do not clean or rewrite the body**: keep it byte-for-byte, including escaped tags and chat codes.
2. Triage per the skill, then **stop and show me a plan**: pages to create or change (with `Kind`), which source sections feed each, and expected tensions. Wait for my OK before writing anything under `wiki/`.
3. After approval, write the pages. One source at a time.
4. Report back: per page, claim counts by tag; any [UNTAGGED], tag conflicts, new tensions, and [X] collisions. Do not proceed past those without my answer.
5. Update `wiki/index.md` and `wiki/log.md` only after I approve the result.

**Both flows.** Grounding: numbers, dates, and quotes must appear verbatim in the linked raw file (skill's source-fidelity rule). Never promote a [C] on your own.

## Lint (report only, overrides the skill's auto-fix)

Run `python3 .agents/skills/karpathy-llm-wiki/scripts/check_evidence.py .` for the mechanical check.

Report, never fix:
- untagged claims; a tag differing from the source's; a [C] used as the basis of a canon claim; [X] ideas reintroduced
- contradictions not yet in `tensions.md`; stubs that now have enough material to grow
- orphan pages, broken links, missing cross-references, index drift, unreferenced raw files

Auto-fix is limited to adding missing rows to `wiki/index.md`. Fixing links, deleting See Also entries, or touching any claim or tag requires my say-so.
Lint logs per the skill.

## Query

Cite pages and quote tags. State when an answer rests on [C], [Z?], or [OPEN] items.
Never present a [C] as established. Do not write files unless I ask.

## Search

Index-first, then grep. No vector search or extra tooling until I say recall has degraded.
