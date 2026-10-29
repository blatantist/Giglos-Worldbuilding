# Communication as Action

> Sources: Giglos Wiki Source, 2026-10-29
> Raw: [Giglos Wiki Source § GOAP agent architecture](../../raw/giglos/2026-10-29-giglos-wiki-source.md#GOAP%20agent%20architecture); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

[The verbal text system is mostly a renderer](#^renderer); text is rendered only near the player. [Rendering is keyed to the player's vicinity](#^vicinity) because TTS prosody carries belief signals. [Talking is just an action](#^action), with no separate conversation state.

## Canon

- The verbal text system is mostly a renderer for the expressive GOAP state. Background agents communicate without rendered text; text is rendered only for agents in range of the player. [Z] (G) ^renderer
- Rendering is keyed to the player's vicinity, not only the conversation partner, because a TTS system will take a prosody signal from the agent's beliefs and parameters so the player can infer beliefs; any extra signal added for that must also be visible to non-text agents. [Z] (G) ^vicinity
- Talking is just an action with no separate conversation state. An agent goes up to another, sends a signal to get attention, and the other, being in range, independently perceives and responds. [Z] (G) ^action

## Unconfirmed

- Communication level of detail (near: full text; mid: acts without realizer; far: batched exchanges). [C] (G)
- Rendering is a pure function and a seed-replay test checks rendering on and off give identical state. [C] (G)
- A small paralinguistic vector on every act (confidence, certainty, valence, arousal, stance, focus) computed for all agents. [C] (G)
- Leakage of true state with masking as a costly action. [C] (G)
- Noisy, range-limited perception. [C] (G)
- Addressee inferred with a "was that for me" confidence. [C] (G)
- Recent-dialogue context kept in each agent's own beliefs. [C] (G)
- Turn-taking from action durations. [C] (G)
- Guarding against courtesy loops. [C] (G)

## Open questions

- Is masking in the first version, or is leakage involuntary at first? [OPEN] (G)
- Addressee as an explicit act slot, or inferred from gaze and position? [OPEN] (G)
- Retroactive overhearing of recent act logs, or forward-only rendering? [OPEN] (G)

## See Also

- [GOAP architecture](goap-architecture.md)
- [Dialogue interpreter](dialogue-interpreter.md)
- [Reflection and persuasion](reflection-and-persuasion.md)
- [Player agent and dialogue](../game/player-agent-and-dialogue.md)
