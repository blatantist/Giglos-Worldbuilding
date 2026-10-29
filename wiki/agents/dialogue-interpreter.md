# Dialogue Interpreter and Realizer

> Sources: Giglos Wiki Source, 2026-10-29; Chat H "Wiki planning and agent design follow-up", 2026-10-29
> Raw: [Giglos Wiki Source § Dialogue interpreter and realizer](../../raw/giglos/2026-10-29-giglos-wiki-source.md#Dialogue%20interpreter%20and%20realizer); [Chat C transcript](../../raw/chats/2026-10-12-chat-C.md); [Chat F transcript](../../raw/chats/2026-10-25-chat-F.md); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md); [Chat H transcript](../../raw/chats/2026-10-29-chat-H.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

The interpreter turns player text into GOAP-compatible speech acts; the realizer turns acts back into text. Zach's direction here is tentative [Z?]: symbolic speech acts with a subword token scheme and no LLM (see T5). [The game is English only](#^english). From chat H: [dialogue planning is hierarchical](#^hier-dialogue) so the realizer is close to a direct translation, and [vocabulary is the realizer's job](#^vocab) while doctrine lives in the plans above it.

## Canon

- Wondering whether players could convince people with real text input, via a manual text interpreter (worried it could be clunky or restrictive) or a neural interpreter that turns text into GOAP-compatible communication. [Z] (C)
- The game is English only; Giglian is never an NLP target. [Z] (F) ^english

### Hierarchical dialogue planning (chat H)

- Dialogue planning is hierarchical, like everything else including memory. The agent plans higher-level, nuanced, more syntactic dialogue state, so the realizer is close to a direct translation. [Z] (H) ^hier-dialogue
- Actual vocabulary is handled by the realizer. Doctrine and the like are inherent to the plans in the layers above, and are reflected in wording through the agent's communicative system. [Z] (H) ^vocab
- Example: an agent can speak directly about a doctrinal subject to someone who shares the belief, or speak about doctrine through a lens that doesn't raise suspicion in a non-follower. The choice comes from the agent's prediction of what the other agent is planning, and from the goal of the conversation (keeping the upper hand, not getting caught, or whatever it is). [Z] (H)

## Tentative

- The interpreter turns player text into GOAP-compatible speech acts and the realizer turns acts back into text; Zach's direction is tentative ("throwing shit at the wall") but leans toward symbolic speech acts with a subword token scheme and no LLM. [Z?] (F)
- Likes speech acts as planning operators with structured state and an abstract syntax, plus ideas from Cicero. [Z?] (F)
- Wants an LLM-style subword token scheme so foreign or coined words fit as subtoken clusters, but no actual LLM. [Z?] (F)

> **Status: Disputed**
> T5: vs the high-end LLM dialogue tier in chat C ([player agent and dialogue](../game/player-agent-and-dialogue.md)). Recorded in [tensions](../meta/tensions.md), unresolved.

- Interested in a hierarchical interpreter that goes from raw text to implicit meaning in a way one pass cannot. [Z?] (F)

## Unconfirmed

### Claude's proposed design

1. Define the act schema first: about 15 acts (inform, ask, request, promise, threaten, appeal, and similar) with typed slots (agent, belief, goal, item), restricted to in-scope entities. [C] (F)
2. Robust input: fastText-style character n-grams for typos and coined names, plus an entity linker matching spans against in-scope names and aliases. [C] (F)
3. Hierarchical layers: surface tokens and entities, then literal content (slot frame), then literal act, then intended act. The last step uses the NPC's plan recognition, the same module as threat labeling, which mirrors predictive coding (literal parses up, goal expectations down). Return ranked candidates; ask for clarification when confidence is low. [C] (F, G)
4. Test whether layers 1 to 3 in one classifier handle most input before building the top-down layer. [C] (F)
5. Realization from templates or a Grammatical Framework-style grammar so parse and generate share one abstract syntax; round-trip tests (realize, parse, compare). [C] (F)
6. The abstract syntax can be Giglian-native semantics, with English as one concrete syntax and other languages added later for localization; each doctrine camp's word for a split is a different linearization chosen by the speaker's beliefs. [C] (F)
7. A realizer request is (act, slots, paralinguistic vector); text hedges come from the same confidence value as TTS prosody so they never disagree. [C] (G)
8. From Talk of the Town's grammar: act metadata on grammar symbols, middle-out expansion from mid-level symbols, preconditions gated on speaker state, runtime variables that read beliefs, story sampling as the dev loop. Do not adopt its obligation-based dialogue manager. [C] (G)
9. The model, if any, translates and never decides; NPC paraphrase ("so you're promising me food?") lets players correct misparses. [C] (C)

### From chat H

- The realizer's input is content plus framing plus the paralinguistic vector. The planner chooses framing; the realizer only picks words that honor it. [C] (H)
- A speaker's default vocabulary is their own doctrine's, so holding a neutral lens costs effort. Tired, angry or careless agents slip, which makes vocabulary a tell. [C] (H)

## Open questions

- Shared grammar for parsing and generation, or templates out with a learned input? [OPEN] (F)
- How much indirect speech do players produce vs direct asks? [OPEN] (F)
- Is the high-end LLM realizer from chat C still on the table given the no-LLM interpreter preference? [OPEN] (C, F)
- Is the lexicon global, or per agent (learned, inherited unevenly at splits)? [OPEN] (H)
- Exact act inventory: see [speech-act schema](speech-act-schema.md).

## History

- Jev was once floated as the speech-act picker; the later decision to run choices on GOAP confidence values instead makes its role here doubtful. [X] (C, G) Replaced by: confidence-weighted GOAP action costs.
- Giggle intensity as the game's native NLP output [X] (F). Replaced by: the game is English; Giglian is worldbuilding only.

## See Also

- [Speech-act schema](speech-act-schema.md)
- [Communication as action](communication-as-action.md)
- [Player agent and dialogue](../game/player-agent-and-dialogue.md)
- [Jev](jev.md)
- [Conlang](../language/conlang.md)
- [Identity doctrines](../society/identity-doctrines.md)
- [Prior art](../project/prior-art.md)
