# Giglos Wiki: Schema

Personal worldbuilding + game-design wiki: the Giglian species (biology, ecology, psychology,
society, law, religion, conlang in progress), a planned RPG set in that world, and a GOAP
multi-agent NPC architecture. The wiki organizes my thinking.

**Never write game code or implementation.** Design discussion and prose only.

This file extends the `karpathy-llm-wiki` skill (`.agents/skills/karpathy-llm-wiki/SKILL.md`).
Where this file and the skill disagree, **this file wins**. The overrides are listed explicitly below.

## Layout

- `raw/<topic>/` Immutable sources. Never edit, rename, or delete after capture.
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

## Ingest (supervised, overrides the skill's flow)

1. Fetch: copy the source into `raw/<topic>/YYYY-MM-DD-slug.md` with the skill's metadata header. **Do not clean or rewrite the body**: keep it byte-for-byte, including escaped tags and chat codes.
2. Triage per the skill, then **stop and show me a plan**: pages to create or change (with `Kind`), which source sections feed each, and expected tensions. Wait for my OK before writing anything under `wiki/`.
3. After approval, write the pages. One source at a time.
4. Report back: per page, claim counts by tag; any [UNTAGGED], tag conflicts, new tensions, and [X] collisions. Do not proceed past those without my answer.
5. Update `wiki/index.md` and `wiki/log.md` only after I approve the result.
6. No background capture, no automatic ingest, no hooks.
7. Grounding: numbers, dates, and quotes must appear verbatim in the linked raw file (skill's source-fidelity rule).

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
