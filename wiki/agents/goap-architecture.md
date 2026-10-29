# GOAP Agent Architecture

> Sources: Giglos Wiki Source, 2026-10-29; Chat H "Wiki planning and agent design follow-up", 2026-10-29
> Raw: [Giglos Wiki Source § GOAP agent architecture](../../raw/giglos/2026-10-29-giglos-wiki-source.md#GOAP%20agent%20architecture); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md); [Chat H transcript](../../raw/chats/2026-10-29-chat-H.md); [Chat I transcript](../../raw/chats/2026-10-07-chat-I.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

The core bet ([C+], Claude's framing that Zach built on): [every agent runs the same GOAP code over its own state](#^core-bet), speech acts are ordinary planner actions, and text is only a renderer. [All agents share one architecture](#^identical); [status derives from several sources](#^status), weighed by [each observer's stake](#^stake). [Beliefs come from observation or trusted sources](#^beliefs), and memory is [sparse gist](#^gist) that is [hierarchical and consolidates upward](#^hier-memory) (chat H). Whether memory and the forward model are one store is open.

## Canon

- The core bet: every agent runs the same GOAP code over its own state, speech acts are ordinary planner actions, and text or audio is only a renderer that never feeds back into the simulation. [C+] (G, M2) (was [Z], retagged 2026-10-29 after transcript check) ^core-bet

### Foundations

- GOAP-based game AI with inter-agent blackboard sharing that enables emergent cooperative behavior. LGOAP adds long-horizon plan influence. [Z] (M2)
- Framed as a handwritten symbolic approximation of abstract goal-directed reasoning: emergent but interpretable. [Z] (M2)
- Was on hiatus; active again as of late October 2026. [Z] (M2)
- Decided against using Jev (his separate decision model over up to 255 labeled options) as a chooser inside GOAP; instead, everything runs on confidence values inside the GOAP system. [Z] (G)

### Identical agents and status

- Every agent is the same architecture; they differ only in skills, experience, status and so on. A general worldview-affirming goal applies to everyone. [Z] (G) ^identical
- Status derives from several sources: inherited position in the hierarchy (lineage), the beliefs and power of the agent's social circle, and recognition earned from respect-granting actions experienced by others. [Z] (G) ^status
- Position, power and consensus are mostly what elites like to think about to consider themselves high status (snobbery). How an observer weighs another's status depends on their own stake in the doctrine and their place in the hierarchy: aspirants (for example outer-middle workers in the inner ring trying to get in) take position, power and consensus for granted; low-stake agents rely on more nuanced recognition. [Z] (G) ^stake
- Stake comes from the agent's own goals; an aspirant's goals align with entering the inner ring because they believe it improves their core survival goals. [Z] (G)

Cross-link (rejected-ideas row 24, refined): the stake-weighting claim above and the [C+] [aspirant split](../society/resistance.md) refine the [Z] ["Middle-ringers are typically easier" claim](reflection-and-persuasion.md). All three stand.

### Beliefs and memory

- Everything an agent believes comes from real observation or a trusted source; that is how their "brain" works. [Z] (G) ^beliefs
- Memory is not an exact event log. It is sparse, storing what higher-order goal abstraction noticed (which goals were satisfied, what information toward goals was gained), so agents know notable things happened but not the detailed steps; gaps are filled by prediction and confabulation from priors. [Z] (G) ^gist
- Memory is hierarchical. The lower layers (action, procedural memory of what happened) hold immediate, precise memory. Over time memory propagates up and consolidates, so the precise detail fades into the higher, more abstract levels' interpretation, at whatever goal level and timescale. [Z] (H) (refines the sparse-gist claim above) ^hier-memory

## Unconfirmed

### Identical agents and status

- The "swap test" (exchange two agents' state and behavior should swap). [C] (G)
- Persistence and openness derived, not dialed. [C] (G)
- Generate populations from simulated histories. [C] (G)
- Status as a per-observer readout of four sources. [C] (G)
- Legitimacy as a protected doctrine node. [C] (G)
- Decay on recognition to avoid rich-get-richer loops. [C] (G)
- Level of detail for pairwise beliefs. [C] (G)
- Exposure changes stake only through evidence. [C] (G)
- Disillusioned aspirants as prime recruits. [C] (G)
- New insiders becoming most zealous. [C] (G)

### Beliefs and memory

- A belief record of content, source (observed, told by, inferred), timestamp and hop count. [C] (G) (Split 2026-10-29: the probability and precision fields moved to History.)
- Testimony degrades per hop. [C] (G)
- Trust as a belief enabling retroactive discounting. [C] (G)
- Episodes gated by prediction error or goal relevance. [C] (G)
- Reconstruction as a planner query tagged inferred. [C] (G)
- Retelling drift and storing each telling. [C] (G)
- Source tags fading faster than content as a doctrine mechanism. [C] (G)
- Consolidation of repeated episodes into general beliefs. [C] (G)
- Where memory consolidates into higher levels, each level's memory may double as that level's prior for prediction, making memory and forward model one hierarchy. [C] (H) Bears on the [one-store-or-two question](#^one-store); not resolved.

## Open questions

- Is the forward model the same store as consolidated memory, or separate? (last open thread) [OPEN] (G) ^one-store
- Does the lineage prior on status decay as recognition accumulates? [OPEN] (G)
- Do agents track the original source of testimony or only the immediate teller (echo chambers)? [OPEN] (G)

## History

- Earlier idea, now dropped: Jev picks which precondition to target each step so an agent can give up on a stuck branch. [X] (I) Replaced by: confidence-weighted GOAP action costs (rejected-ideas row 22, (G, M2)).
- Probability and precision as fields of the belief record (split from the belief-record line under Unconfirmed). [X] (G, H) (was [C], rejected 2026-10-29) See [rejected-ideas row 29](../meta/rejected-ideas.md).
- Exact event logs as memory [X] (G). Replaced by: sparse, goal-abstracted gist memory with confabulated gaps.

## See Also

- [Staged build plan](staged-build-plan.md)
- [Reflection and persuasion](reflection-and-persuasion.md)
- [Communication as action](communication-as-action.md)
- [Dialogue interpreter](dialogue-interpreter.md)
- [Jev](jev.md)
- [Player agent and dialogue](../game/player-agent-and-dialogue.md)
- [Resistance](../society/resistance.md)
- [Prior art](../project/prior-art.md)
