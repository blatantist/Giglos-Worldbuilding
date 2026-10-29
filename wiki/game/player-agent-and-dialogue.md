# Player Agent and Dialogue

> Sources: Giglos Wiki Source, 2026-10-29
> Raw: [Giglos Wiki Source § Game design: progression, dialogue, player agent](../../raw/giglos/2026-10-29-giglos-wiki-source.md#Game%20design%3A%20progression%2C%20dialogue%2C%20player%20agent); [Chat C transcript](../../raw/chats/2026-10-12-chat-C.md); [Chat F transcript](../../raw/chats/2026-10-25-chat-F.md); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

[The player is an actor under the same GOAP conditions as NPCs](#^same-conditions), [a full GOAP agent that cannot act on its own](#^shadow), scored against what the human does. NPCs [build a model of the player](#^model), though how much of the player's blackboard they see is tension T4. Zach wants [persuasion through actual talk](#^persuasion). The LLM dialogue tier is tension T5.

## Canon

### Player as a GOAP agent

- The player is an actor under the same GOAP conditions as NPCs, but the human does not see the blackboard; they just play. [Z] (C) ^same-conditions
- The player's blackboard is hidden only from the human. NPCs can see it, so they interact with the player as a GOAP agent and speak in a way that feels intelligent, as if they see and remember. [Z] (C)

> **Status: Disputed**
> T4: vs NPCs building a model of you from observation (below); Claude argued for scoped access to avoid omniscience. Recorded in [tensions](../meta/tensions.md), unresolved.

- NPC-to-NPC blackboard cooperation stays visible in the world, as in Boeda's multi-agent GOAP paper. [Z] (C)
- NPCs experience things about the player, remember what you tell them, and build a model of you (predicting your goals). They do the same about each other; this is the general mechanism for cooperation. [Z] (C) ^model

> **Status: Disputed**
> T4: vs NPCs being able to see the player's blackboard (above). Recorded in [tensions](../meta/tensions.md), unresolved.

- Plan to make the hidden layer a theory-of-mind style layer. [Z] (M1) (was (C, M1); no chat-C turn says this, re-cited 2026-10-29)
- The player agent is a full GOAP agent that cannot act on its own. Its expected goals (the general NPC goal substrate plus the quest tree made into goals) and its preferred action can be scored against what the human actually does. [Z] (C) ^shadow

### NPC dialogue output

- Each character's dialogue is informed semi-procedurally by GOAP state. Low end: a non-neural interpreter of the state and blackboard that procedurally generates dialogue. High end: an LLM fed state, character background and a few candidate ideal dialogue-tree scripts. [Z] (C)

> **Status: Disputed**
> T5: vs "no actual LLM" for the interpreter in chat F ([dialogue interpreter](../agents/dialogue-interpreter.md)). Recorded in [tensions](../meta/tensions.md), unresolved.

- Later interpreter discussion leans away from LLMs (see [dialogue interpreter](../agents/dialogue-interpreter.md)). [Z] (F)

### Persuasion as play

- Zach wants a game where you actually talk to people to convince them to join, instead of a script assigning followers, with procedural input matching procedural output. [Z] (C) ^persuasion
- Recruiting: the player explains a goal, and the agent asks for clarification, justification or sources in a back-and-forth until convinced. [Z] (G)

## Unconfirmed

- NPCs should read a modeled view of the player except inside trust or lineage groups (no omniscience). [C] (C)
- Plan recognition by scoring actions against each goal's plan. [C] (C)
- Surprise as a signal. [C] (C)
- An "exploring" bucket to avoid over-reading noise. [C] (C)
- Keep models per NPC to avoid railroading. [C] (C)
- Show locked options with reasons. [C] (C)
- Keep memory flags coarse. [C] (C)
- NPCs voice what they believe about you plus a journal for legibility. [C] (C)
- An LLM tier may talk but never decide. [C] (C)
- Hand-author plot-critical beats. [C] (C)
- Prototype with a menu of acts first; if persuasion is not fun with buttons, typing will not fix it. [C] (C)

## Open questions

- Is the shadow agent a hidden director shaping pacing, or only an analysis tool? [OPEN] (C)
- Can the player lie, and do false claims plant false models? [OPEN] (C)
- Does trust accumulate across encounters? [OPEN] (C)

## See Also

- [Progression and skill points](progression-and-skill-points.md)
- [GOAP architecture](../agents/goap-architecture.md)
- [Reflection and persuasion](../agents/reflection-and-persuasion.md)
- [Dialogue interpreter](../agents/dialogue-interpreter.md)
- [Communication as action](../agents/communication-as-action.md)
