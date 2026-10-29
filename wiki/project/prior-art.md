# Prior Art and Reading List

> Sources: Giglos Wiki Source, 2026-10-29; Chat H "Wiki planning and agent design follow-up", 2026-10-29
> Raw: [Giglos Wiki Source § Prior art and reading list](../../raw/giglos/2026-10-29-giglos-wiki-source.md#Prior%20art%20and%20reading%20list); [Chat A transcript](../../raw/chats/2026-09-23-chat-A.md); [Chat B transcript](../../raw/chats/2026-10-05-chat-B.md); [Chat C transcript](../../raw/chats/2026-10-12-chat-C.md); [Chat D transcript](../../raw/chats/2026-10-19-chat-D.md); [Chat F transcript](../../raw/chats/2026-10-25-chat-F.md); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md); [Chat H transcript](../../raw/chats/2026-10-29-chat-H.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

[Boeda's GOAP cooperation paper](#^boeda) is Zach's chosen starting point for the agent work. Everything under Unconfirmed was surfaced by Claude as context and has not been evaluated by Zach.

## Canon

### Agent AI and dialogue

- [Boeda, "Multi-Agent Cooperation in Games with GOAP" (Square Enix, AIIDE 2021)](https://cdn.aaai.org/ojs/18909/18909-52-22675-1-2-20211004.pdf): per-agent backward GOAP; failed plans insert cooperation actions on any-agent conditions; RequestCooperation messaging. Relevance: basis for stage 3; its limits (blind discovery, refusal only by busyness or liking, bare goal requests) are what Zach's design extends. Status: chosen by Zach. [Z] (G) ^boeda
- Talk of the Town / Bad News (Ryan, Mateas et al.): agents with imperfect memory and gossip; grammar-based dialogue realization. Zach read the realization paper and found it "pretty basic". Status: read. [Z] (G)
- [Ryan et al. 2016b, "A lightweight videogame dialogue manager"](https://dl.digra.org/index.php/dl/article/view/798): dialogue management. Status: read. [Z] (H)
- Ryan et al. 2016b assessment: interesting take, but the dialogue manager relies too heavily on authored dialogue realizing the state. [Z] (H)
- Cicero (Meta, Diplomacy): strategic planner plus language model realizer. Zach likes its ideas. Status: noted. [Z] (F)

### Worldbuilding, biology, society (Zach's references)

- Michael Levin's bioelectricity research (planaria, Xenopus, eyes on tadpole tails): core inspiration for growth control. Zach's source. [Z] (A)
- Glaggleland meme: visual inspiration. Zach's source. [Z] (A)
- Disco Elysium: skills as voices, Thought Cabinet, dialogue lock-in. Zach playing as research. [Z] (B)
- Fallout: New Vegas: multiple faction endgame routes. Zach's reference. [Z] (C)
- Adventure Time (Jake), Steven Universe (gem fusion), Rick and Morty (split episodes): growth look, fusion as marriage, personality splitting. Zach's references. [Z] (A, C)
- Ayn Rand ("who is John Galt?"): middle-ring ideology. Zach's reference. [Z] (C)
- Tolkien's method: conlang plus history plus narrative. Zach's model. [Z] (F)

## Unconfirmed

### Agent AI and dialogue (suggested by Claude)

- Orkin, F.E.A.R. squad AI: shared blackboard GOAP squads; classic GOAP coordination. [C] (G)
- BDI agents: belief-desire-intention architectures; goal commitment. [C] (G)
- Epistemic / theory-of-mind planning: planning over others' beliefs; stage 5. [C] (G)
- Comme il Faut / Prom Week, Versu: social acts with preconditions; menu-based input; "buttons first" baseline. [C] (F, G)
- Facade: free text mapped to discourse acts by rules; misparse risks. [C] (C, F)
- Generative Agents (Park et al.): LLM agents with memory and reflection; contrast case. [C] (G)
- Rational Speech Act models: pragmatic listeners; intended-act inference. [C] (G)
- Allen and Perrault; Cohen and Levesque: speech acts as plan operators; theory behind the act schema. [C] (F)
- FIPA ACL; ISO 24617-2: agent message and dialogue act taxonomies; ready-made act vocabularies. [C] (F)
- TrindiKit, GoDiS: Information State Update dialogue managers; structured dialogue state. [C] (F)
- Inform 7 / TADS: parser IF grounded in scope; entities-in-scope parsing. [C] (F)
- Grammatical Framework, OpenCCG, Prolog DCGs: bidirectional grammars; shared parse and generate. [C] (F)
- Reiter and Dale; SimpleNLG: classic NLG pipeline; realizer. [C] (F)
- SentencePiece, fastText: subword tokenizers and n-gram embeddings; no-LLM token scheme. [C] (F)

### Worldbuilding, biology, society (Claude's references)

- Spinoza, capabilities approach, privation theory: joy ethics. [C] (D)
- Parfit fission; U and non-U, Simmel, Bourdieu: identity doctrines; prestige cycles. [C] (F)
- von Thunen, Hamilton's rule, Anderson's imagined communities: city and cohesion. [C] (A)
- Sharp, Chenoweth and Stephan, Granovetter, Snow and Benford, Tsebelis: revolution, rhetoric, veto points. [C] (F)
- Rosenfelder's Language Construction Kit; Peterson, The Art of Language Invention: conlang craft. [C] (F)

## Open questions

- Ryan et al. 2015b, "Toward characters who observe, tell, misremember, and lie": belief and memory handling; most relevant to source-tracked beliefs and gist memory; Claude offered to pull it next. Status: to read. [OPEN] (G)

## History

- Talk of the Town realization paper as the key reference [X] (G). Replaced by: Zach found it basic; belief and memory papers suggested instead.
- Note: the source listed Ryan et al. 2016b as "Zach reportedly reading independently", status Reading (G), untagged. Zach updated it in chat H (see Canon).

## See Also

- [GOAP architecture](../agents/goap-architecture.md)
- [Staged build plan](../agents/staged-build-plan.md)
- [Dialogue interpreter](../agents/dialogue-interpreter.md)
- [Project overview](overview.md)
