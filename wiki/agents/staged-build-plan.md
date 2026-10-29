# Staged Build Plan

> Sources: Giglos Wiki Source, 2026-10-29
> Raw: [Giglos Wiki Source § GOAP agent architecture](../../raw/giglos/2026-10-29-giglos-wiki-source.md#GOAP%20agent%20architecture); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

Zach's plan is to [start from a toy environment and add communication in stages](#^plan), starting from Boeda's paper. The [eight-stage ladder](#^stage0) is Claude's structure adopted as the working plan, so each stage is [C+]. The [stage 4/5 jump](#^ask-why) is Zach's framing.

## Canon

- Zach's plan: start from a toy environment (agents work jobs to earn and feed themselves; farmers feed themselves from surplus on top of export yield), scale up to the ring hierarchy and supply system, then add communication in stages from simple to full verbal, starting from Boeda's GOAP cooperation paper. [Z] (G) ^plan

### Ladder as revised in chat G (Claude's structure, adopted as the working plan)

- Stage 0, solo survival: one agent, hunger, farm or buy to eat. [C+] (G) ^stage0
- Stage 1, wages: employers post jobs to a shared board. [C+] (G)
- Stage 2, ring supply chain: outskirts surplus, middle hauls, core pays; cut a link and check starvation propagates correctly. [C+] (G)
- Stage 3, reactive cooperation: typed messages (request, offer, accept, refuse) per Boeda; goals accepted as given. [C+] (G)
- Stage 4, reflection: goal provenance plus a forward model, still no language. [C+] (G)
- Stage 5, modeling others: other agents' goals and predicted behavior (plan recognition). [C+] (G)
- Stage 6, verbal acts as interventions on beliefs and goal provenance. [C+] (G)
- Stage 7, text interpreter, then politics (council, veto bloc, rhetoric spread, shared threat labels). [C+] (G)
- Zach's framing of the jump at stages 4 and 5: agents gain prediction of future world states, so they can ask why they pursue a goal rather than accept it as given. [Z] (G) ^ask-why

## Unconfirmed

- Each stage is an ablation with numbers (throughput, starvation, recovery time). [C] (G)
- Headless runs need no renderer. [C] (G)
- First milestone is a farmer whose backward plan fails until a hauler accepts an offer. [C] (G)
- Message schemas at each stage are subsets of the final speech-act schema. [C] (G)

## Open questions

- Stage 2: per-agent beliefs from the start, or global truth until stage 4? [OPEN] (G)
- Stage 2: prices or quotas driving the supply chain? [OPEN] (G)

## See Also

- [GOAP architecture](goap-architecture.md)
- [Reflection and persuasion](reflection-and-persuasion.md)
- [Speech-act schema](speech-act-schema.md)
- [Prior art](../project/prior-art.md)
- [The city](../society/the-city.md)
