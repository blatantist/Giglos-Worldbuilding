# Reflection, Belief and Persuasion

> Sources: Giglos Wiki Source, 2026-10-29; Chat H "Wiki planning and agent design follow-up", 2026-10-29
> Raw: [Giglos Wiki Source § GOAP agent architecture](../../raw/giglos/2026-10-29-giglos-wiki-source.md#GOAP%20agent%20architecture); [Chat G transcript](../../raw/chats/2026-10-27-chat-G.md); [Chat H transcript](../../raw/chats/2026-10-29-chat-H.md)
> Updated: 2026-10-29
> Kind: draft

## Overview

[Beliefs and doctrine govern what an agent is willing to question](#^doctrine). A [reaction depends on content and delivery](#^reaction). [All choices are GOAP actions with confidence-weighted costs](#^confidence). Belief is [not strongly probabilistic](#^not-prob) but [anchored by evidence](#^anchored) (chat H), and [patience is derived, not stored](#^patience).

## Canon

### Reflection, doctrine and reactions

- Beliefs and doctrine sit on top of goal reasoning and govern what an agent is willing to question. Inner-ring dogma is pervasive, so convincing them peacefully needs a stealth path; failing makes them angry and label you a terrorist. Middle-ringers are typically easier because the dogma is less pervasive. [Z] (G) ^doctrine

Cross-link (rejected-ideas row 24, refined): this claim stands, refined by the [Z] [stake-weighting claim](goap-architecture.md) and the [C+] [aspirant split](../society/resistance.md). The "angry" outcome here is refined by the disgust line that follows.

- A reaction depends on content (threat to doctrine) and delivery (respectful vs contemptuous). Respectful disagreement may produce a rebuttal or ending the interaction; contempt produces anger. Disgust is also possible, not only anger. (Zach's example: a respectful atheist vs a mocking one talking to a devout Christian.) [Z] (G) ^reaction

### Confidence instead of a chooser

- All choices (reactions, persuasion, clarification) are GOAP actions with confidence-weighted costs. [Z] (G) ^confidence

### Belief model (chat H)

- Belief is not strongly probabilistic. Randomness enters only in choosing among similarly confident plans, goals or actions. [Z] (H) ^not-prob
- Belief is anchored by evidence. Where the source has been forgotten it can be blind faith, which is more manipulable. [Z] (H) ^anchored
- Goals are weighed by the beliefs around their conditions and outcomes, and by the reasons for pursuing them. [Z] (H)
- Gaining a new belief requires good evidence or reason, or compatibility with existing beliefs. [Z] (H)
- Something that goes against an agent's beliefs can only be convinced by avoiding the conflicting subject and relying on other beliefs, false impressions and so on: social engineering, the way cults indoctrinate. [Z] (H)

### Recruitment and persuasion loop

- The player recruits by explaining a goal; the agent asks for clarification, justification or sources in a back-and-forth until convinced. [Z] (G)
- Patience is not a stored value. It derives from confidence, trust, alignment with beliefs and similar, so an elite becomes more patient when you weave their politics into the conversation. [Z] (G) ^patience

## Unconfirmed

### Reflection and doctrine

- Goal provenance chains ("haul grain" serves "earn coin" serves "stop being hungry"). [C] (G)
- Prediction error triggers reconsideration. [C] (G)
- Rigidity of a belief derived from how many goals hang off it, not from ring. [C] (G) ^rigidity
- Stealth persuasion targets dependent goals so error accumulates around the protected node. [C] (G)
- Anger adds a neutralize goal and a threat label, disgust adds exclusion and isolation, both cascading through shared blackboards. [C] (G)
- A stance modifier on every act. [C] (G)
- Commitment with trigger-based reconsideration. [C] (G)
- Belief resistance may be a readout of support: how much evidence it has, and how many other beliefs and goals depend on it. [C] (H) Links to the [rigidity line](#^rigidity).

### Confidence

- Plan confidence as the product of step confidences. [C] (G)
- Information-gathering actions are chosen when they raise downstream confidence enough. [C] (G)
- Failed attempts lower confidence so stuck branches are abandoned. [C] (G)
- Start with three coarse levels. [C] (G)

### Recruitment and persuasion

- Adoption confidence has components (understanding, feasibility, value, truth, trust) and each question type targets the weakest one, which also tells the player what is blocking. [C] (G)
- Repetition has diminishing returns. [C] (G)
- An unanswerable source question becomes an emergent quest. [C] (G)
- Patience as the computed value of continuing. [C] (G)
- Flattery inferred as instrumental backfires. [C] (G)

## Open questions

- Does rigidity harden when challenged? [OPEN] (G)
- Is stance a free knob or derived from state? [OPEN] (G)
- Recruits adopt the player's goal as their own, or as a "help the player" subgoal? [OPEN] (G)
- Can agents verify claims themselves (asynchronous persuasion)? [OPEN] (G)
- How is a belief's resistance to change determined in the evidence-anchored model? [OPEN] (H)

## History

- Keep two numbers per belief, probability and precision (doctrine is high on both; hardening under attack is a precision increase). [X] (G, H) (was [C], rejected 2026-10-29) Replaced by: the evidence-anchored belief model above.
- The chat summary records probability and precision as settled, but Zach never explicitly confirmed it. [X] (G, H) (was [C+], rejected 2026-10-29) Replaced by: the evidence-anchored belief model above.
- Anger as the single failure reaction [X] (G). Replaced by: content threat plus delivery stance; disgust possible.
- Patience as a stored trait [X] (G). Replaced by: derived from confidence, trust and belief alignment.

## See Also

- [GOAP architecture](goap-architecture.md)
- [Communication as action](communication-as-action.md)
- [Staged build plan](staged-build-plan.md)
- [Resistance](../society/resistance.md)
- [Player agent and dialogue](../game/player-agent-and-dialogue.md)
- [Identity doctrines](../society/identity-doctrines.md)
