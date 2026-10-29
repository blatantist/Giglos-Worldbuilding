# Giglos Wiki Source

Oct 29, 2026 · @Zach Bernard

## About this source

This is raw source material for a Claude Code wiki agent (Karpathy-style LLM wiki), compiled from all seven chats in the Giglos Worldbuilding project plus Zach's saved memory notes. It is not the wiki itself. Every claim is tagged by who said it, so the agent can separate canon from suggestion and turn open items into page stubs.

### Provenance tags

| Tag | Meaning | How the wiki should treat it |
| --- | --- | --- |
| \[Z\] | Zach stated or decided it | Canon (working canon, can still change) |
| \[Z?\] | Zach said it tentatively ("not final", "throwing at the wall", "idk") | Tentative canon, flag as such |
| \[C\] | Claude proposed it; Zach did not confirm | Unconfirmed proposal, never state as canon |
| \[C+\] | Claude proposed it; Zach built on it or reacted positively without explicitly adopting | Likely canon, flag for confirmation |
| \[X\] | Rejected or superseded | History only; see Rejected section |
| \[OPEN\] | Unresolved question | Page stub or open-question block |

Source codes in brackets after a claim, such as (C), point to the chat below. Memory files (M) are Zach's saved notes and agree with the chats unless noted.

### Source chats (chronological)

| Code | Chat title | Last updated | Main topics |
| --- | --- | --- | --- |
| A | [Giglian lore and biology](https://claude.ai/chat/e6a1a937-b287-4116-8f34-796415cbe856) | 2026-10-11 (begun late Sept) | Origin notes, bioelectric growth, organs, mitosis psyche split, city seeding, greedy mitosis law, ungrowing |
| B | [Giglians game concept](https://claude.ai/chat/5f8b3130-7066-4ddc-97e7-66015b2e5a76) | 2026-10-11 | Plot premise, protagonist, purge by mitose, routes, skill-point economy, Disco Elysium |
| C | [Giglos speciation ecology](https://claude.ai/chat/2bd0ad1d-8a5a-451d-9ccb-f7d722536045) | 2026-10-15 | Speciation, fungi, humidity, tools, medicine, courts, religion, monks, re-education, clean splits, food scarcity, Founder, fusion, skill transplant, player shadow agent, speech-act dialogue |
| D | [Giglian moral philosophy and joy](https://claude.ai/chat/e9fb6d3e-d1aa-4cad-9738-aea2bed358f3) | 2026-10-20 | Joy, giggling, holding pressure, depression, genome vocabulary, frame and foam, split planes, degenerate mitosis, dissolution, forensics, forced splitting, exile |
| E | [Circular city layout design](https://claude.ai/chat/549b5876-b638-4212-a188-bfaffcdf583b) | 2026-10-22 | Ring layout, resource flow, entrance ladder, infiltration, four paths, half choice, species name, phonology |
| F | [GOAP dialogue text interpreters](https://claude.ai/chat/f7e5c80e-ef93-4d2e-956c-89756b7805a7) | 2026-10-26 | Interpreter survey, subword tokens, hierarchical interpreter, English-only game, conlang method, private experience, identity doctrines, doctrine spread, rhetoric and labeling, council path |
| G | [GOAP agent system design](https://claude.ai/chat/accdad1c-0120-4a13-a21c-ec12384d4033) | 2026-10-27 | Full agent architecture, staged toy society, Boeda paper, reflection, doctrine rigidity, two-axis reactions, confidence costs, communication as action, prosody vector, recruitment loop, identical agents, status, belief provenance, gist memory, prior art |

Memory notes: M1 = project lore notes, M2 = project GOAP notes, M3 and M4 = older account-level copies of the same (M3 holds the original pasted lore notes). Jev is a separate Zach project referenced here but documented outside this project.

## Project overview and status

Giglos is Zach's alien-species worldbuilding project that has grown into a planned narrative RPG, with a GOAP agent simulation as its technical core. Three strands run together and feed each other:

1. **Worldbuilding (lore):** the Giglians, a slime-like, mitosis-reproducing species, their biology, ecology, psychology, society and a stratified city-state ruled by "the Founder". \[Z\] (A, C, D, E)
2. **Game design:** an RPG about a cast-off half of the Founder lineage toppling the regime, with multiple endgame routes like Fallout: New Vegas, but explicitly not a Bethesda-style RPG. \[Z\] (B, C, E)
3. **Agent AI:** GOAP agents with blackboard sharing, belief modeling, persuasion and verbal acts, where language is only a renderer over the simulation. Currently the active build focus. \[Z\] (F, G, M2)

### Long-term deliverables named by Zach

- A codex or artbook of Giglos, plus designs for the planet's other species and flora. \[Z\] (A, M3)
- A full Giglian conlang developed alongside history and narrative, Tolkien-style. \[Z\] (F)
- The game itself. \[Z\] (B, C)

### Status as of late Oct 2026

- GOAP agent work was on hiatus and is active again; the next step is a staged toy society environment building up to verbal communication. \[Z\] (G, M2)
- Species name is a placeholder pending phonology. \[Z\] (E)
- Zach was playing Disco Elysium as research ("homework"). \[Z\] (B)
- Last open thread: whether agent memory and the forward model are one store or two, and whether to read Ryan et al. 2015b next. \[OPEN\] (G)

### Design temperament (how Zach works on this)

- Prefers scientifically grounded mechanisms that do explanatory work over arbitrary rules. \[Z\] (A, C)
- Corrects Claude often; many Claude extrapolations were walked back (see Rejected section). The wiki agent should weight \[Z\] lines far above \[C\] lines. (all)
- Keeps systems deliberately decoupled, for example the skill-point economy is separate from the undecided dialogue and skill-check system. \[Z\] (B)
- Notes the setting is an unintentionally cartoonish take on human positivity, with implicit commentary on class hierarchy and mental health. \[Z\] (D)

## Naming, terminology, setting basics

- **"Giglian" is a placeholder.** Calling them Giglians is like calling humans "earthicans". The real endonym will be derived once the phonology exists. \[Z\] (E)
- **Origin of the concept:** inspired by glaggles, the smiley creatures of the "Glaggleland" internet meme. \[Z\] (A, M3) The glaggle look (round head, no arms, tall black eyes, big smile) is what a smiley looks like, and Zach uses it as the Giglian base form or head, not as a costume. \[Z\] (A)
- **Where they live:** original notes say Giglians are "from the third moon of giglos". \[Z\] (A, M3) The name Giglos is also used for the government and the setting as a whole. \[Z\] (A) Whether Giglos is the planet, the moon, or the city-state is not pinned down. \[OPEN\]
- **Moon habitability:** Claude noted a moon needs enough gravity or magnetic shielding to hold a thick wet atmosphere, and suggested a Titan-like body with tidal heating. \[C\] (C) Not answered. \[OPEN\]
- **Glaggleland echo:** the death-spiral or euthanasia rollercoaster joke (Giglians ride lethal rides for fun because they have no bloodflow to be hurt by G-forces) is part of Zach's original notes. \[Z\] (A, M3)

### Terms Zach has fixed

| Term | Meaning | Note |
| --- | --- | --- |
| Mitosis / split | Neutral word for a Giglian dividing into two | "Birth" is NOT neutral; only the death-and-birth camp calls it birth \[Z\] (F) |
| Farmland | Fungal crop land | Use instead of "beds", which Zach rejected \[Z\] (C) |
| Giggle | English label for a Giglian vocalization type, positive valence when involuntary | Not a human giggle; speech is controlled giggling \[Z\] (F) |
| Holding pressure | Cultural metaphor for maintaining healthy baseline mood and form | Only loosely literal \[Z\] (D) |
| Leaky | Folk description of depression, being unable to hold pressure | \[Z\] (D) |
| The Founder | Whichever living descendant is fewest splits from the original city founder | The original no longer exists \[Z\] (C) |
| Greedy / unbalanced mitosis | A deliberately unequal split | Central moral and legal controversy \[Z\] (A, B) |
| Clean split | A controlled split where the splitter chooses what each half keeps | Elite-trained skill \[Z\] (C) |
| Degenerate mitosis | Involuntary splitting from chronic deflation | \[Z\] (D) |
| Dissolution / collapse | Uncontrolled cascading mitosis down to goop | Always uncontrolled mitosis \[Z\] (D) |
| Purge by mitose | State practice of splitting dissent into a disposable half | Coined by Claude, adopted enthusiastically by Zach \[C+\] (B) |
| Waste half | The cast-off remainder of a skill harvest | \[Z\] (C) |

Terms Claude coined that Zach has not adopted (use only as labeled proposals): split registry, memory laundering, career lottery, partial adult, leasehold of experience, window (of experience), shadow agent. \[C\] (C, D, F)

## Ecology and deep-time evolution

Zach's goal here is to work out how speciation feasibly happens among asexual Giglian-like organisms, in order to build the wider ecology of Giglos. \[Z\] (C)

### Decided

- **Species boundary = mergeability.** Tissue fusion compatibility between lineages defines a species. Zach likes this because it ties back to his old mycelium-healing idea. \[Z\] (C)
- **Dominant flora are alien mushrooms and fungi.** \[Z\] (C)
- **Deep-time lineage of mobile "fungi":** free-floating bacteria-like cells, slime-mold-like organisms, proto-plants, many lineages rising and falling over billions of years, larger multicellular slime or fungus-like swimmers and sedentary filter feeders, then plants and animals on land. Order not fixed. \[Z\] (C)
- **Very humid atmosphere** is accepted as implied by the ecology. \[Z\] (C)
- **Genome as vocabulary:** each species' genome fixes which organs and cell types it can grow (a bird analog grows bird eyes and wings; a Giglian grows a Giglian eye, arm and hand). Within that catalog the individual chooses arrangement and count. A bird analog could learn a more hand-shaped wing but stays bounded by its biology. \[Z\] (D)
- **Heredity of learned skill** is real for them because they physically inherit the substrate holding experience; Zach agreed this looks Lamarckian but is true given their function. \[Z\] (C)

### Claude proposals, unconfirmed

- Speciation via niche ecotypes (plasticity is costly, so low-energy niches favor slow or sessile cousins), mergeability via allorecognition genes, and "culture before genome" via the Baldwin effect. \[C\] (C)
- Somatic mosaic mutations split unevenly at mitosis, so genetic and psychic divergence share one mechanism. \[C\] (C)
- Life on Giglos organized along walled vs wall-less and aggregate vs syncytial axes; walled lineages become the sessile mushroom flora, wall-less lineages stay mobile and evolve an internal cartilage lattice. \[C\] (C)
- Ancestry story: aggregators evolve allorecognition to police cheaters; walled fungal flora colonize land first and build humid soil; wall-less giants arrive late into moist understory. \[C\] (C)
- Ball resting form as a water-saving minimum-surface shape; dry zones as speciation barriers; cooling is hard in saturated air; fog favors big dark eyes, sound and electroreception; combustion is hard, so tech leans hydraulic, steam and bio-battery. \[C\] (C)
- Fungi as Giglians' shared lineage (as Earth fungi are closer to animals), baroque fungal sexual systems contrasting Giglian asexuality, a Cordyceps-like growth-hijacking parasite. \[C\] (C)
- Fused-lineage chimeras, hybridization by absorption, forced incompatible fusion as an attack (necrotic scar). \[C\] (C)

### Open

- Are there fixed-body ambulating animals (limbs, shells, bones), or does every mobile creature share some plasticity? \[OPEN\] (C)
- The planet's other species and flora, including the bird-like analog Zach mentioned. Stub. \[OPEN\] (A, D)
- How the city's surrounding open desert squares with a humid world (rain shadow, water diverted inward, something else). \[OPEN\] (E)

## Giglian biology

Giglians are distributed, slime-mold-like organisms whose cells share one genome and whose growth is consciously steered by bioelectric signals, inspired by Michael Levin's bioelectricity research. \[Z\] (A)

### Body plan and tissue

- A mix between a giant unicellular organism and a mycelial network; "slime people" with a cartilage-like skeleton. \[Z\] (A)
- No concept of gender. \[Z\] (A)
- Hybrid body: cartilaginous structural ("frame") tissue plus foamy tissue that acts roughly as muscle. Giglians do not really have muscles. \[Z\] (D)
- Cells have no normal cell wall. \[Z\] (D)
- Neural substrate is distributed in nerve-like cells throughout the body. \[Z\] (A)
- Skill ("muscle memory") lives in localized neural substrate in the tissue; a pianist's arm holds substrate trained for playing. \[Z\] (D)
- No veins or bloodflow, which makes them G-force resistant. \[Z\] (A) Zach later allowed that some nutrient and oxidizer carrier must circulate: tissue grows out slime-mold-like and widens, ends shaped by bioelectric signals, with nutrients sent along that growth. "Tendril" was only a visual analogy; the microscale mechanism is left open. \[Z\] (A)
- Not senescent. They can die (attack, bleeding out, starvation, dissolution), but never of old age. \[Z\] (C)

### Growth and shape

- Cells with identical genome can be induced to grow different parts by electrical signal; Giglians control those signals consciously, fictionally sped up so they can grow arms at will. \[Z\] (A)
- Growth control is a trained skill, like fine motor skill. With no childhood, it is inherited from whichever ancestor in the split lineage learned it (walking, squishing through gaps, stretching an arm to a shelf). \[Z\] (A)
- Different control specializations (growth, density or rheology shifting, etc.) are like human skills (singing, running, lifting) that each person takes interest in and practices. \[Z\] (A)
- Deformation conserves mass. A well-trained Giglian can aerate (whip cytoplasm into foam) to increase volume at constant mass; "aeration, not inflation". \[Z\] (A)
- Limb growth looks smooth and bulk-flowing, like Jake from Adventure Time but toned down, not spindly or webby. \[Z\] (C)
- The frame is grown like arms are: a hip-like or thorax-like area can be shaped by attention; whether a species can grow a "pelvis" at all is genetic. The genome is the plan, intentional changes are possible (the bird analog's hand-shaped wings). \[Z\] (D)
- Frog-eyes-on-butt precedent: a Giglian could grow an arm on its back. \[Z\] (D)
- Homeostatic growth runs subconsciously for the whole body; changing shape is intentional. \[Z\] (D)

### Base form and appearance

- Head: round ball, big mouth resting in a smile, black vertically elongated eyes (tall ellipses), no visible sclera. \[Z\] (A)
- The glaggle look is the base or resting form: what the body relaxes to when no growth effort is held, or specifically what the head looks like. \[Z\] (A)
- Likely a somewhat humanoid base form that can be changed beyond. \[Z\] (D)
- The base is not fixed for the species; it follows the previous life before the split. \[Z\] (A)

### Wounds and healing

- They can stop bleeding by holding a wound closed or pinching it. \[Z\] (A)
- Passive healing exists; attending to a wound speeds it. \[Z\] (C)
- Webbing is kept only as a wound-healing mode (replacing his earlier whole-body mycelium idea). \[Z\] (C)
- Zach was unsure how "ungrowing" a developed part (hand, eye) would work, and floated cutting the part off (perhaps blocking nerves and shutting off flow) and regrowing. \[Z?\] (A) Claude described salamander blastema regrowth and dedifferentiation, and noted cut nerves block regeneration in newts. \[C\] (A)

### Organs (largely open)

Zach's required list: focused eyes, directional hearing, energy intake (digestive, photosynthetic, other), oxygen intake, chemical filtering, waste exit, and audible communication. \[Z\] (A)

Claude proposals, none confirmed \[C\] (A): diffuse skin light-sensing plus grown focused eyes; pinna-like growths or a lateral-line pressure sense for hearing; a single-opening gastrovascular gut; tracheal or cutaneous respiration; distributed flame-cell filtering; a grown resonance chamber for voice; clotting as reflexive sol-gel switching; whip-crack technique for strong punches.

The phonology work (beak, fused tongue, no nose) partly settles the mouth; see Language.

## Mitosis, fusion, dissolution and death

One mechanism (relaxing and re-holding "pressure") underlies reproduction, depression and death; the only differences are control and fuel. \[Z\] (D)

### Mitosis

- Requires eating a lot first (they keep growing, like alligators) so both halves have enough mass, then willing the split by intense concentration. \[Z\] (A)
- Mechanism: relax the pressure and coalesce back toward a blob, which mixes the substrate a bit as it redistributes, then two bodies condense out. \[Z\] (D)
- Normal mitosis feels like a controlled, meditative dissociation. \[Z\] (D)
- Psyche splits unevenly: most is shared, but specific memories, skills and personality aspects may end up in one half and be lost in the other, like the Rick and Morty split-personality episodes. Not a hivemind, more like clones. \[Z\] (A)
- Later refinement: a split keeps about half the memories and loses about half the learned skill, so a post-split Giglian is not an infant. \[Z\] (C) Note: the earliest notes said both halves get "the same memories"; the refined version supersedes it. \[X\] (A)
- Giglians always know which memories are pre-split; those still feel like their own. \[Z\] (F)
- Memory survives only a limited number of splits; after enough, it dilutes so most cannot personally remember an era. \[Z\] (C)
- Splits need not be bilateral: a split can give one half both arms and the other both legs. \[Z\] (D)
- Clean (controlled) splits are a learned skill that mostly only elites get trained in. \[Z\] (C) See Re-education and clean splitting.
- Family history is based on the setting of the split; Giglians far from home slowly diverge from the groupthink. \[Z\] (A)
- Culture has a norm for what age or year to mitose, like when to have a baby. \[Z\] (C)
- Claude proposals: memory half-life counted in splits rather than years; splitting as mandatory "insurance" before dangerous jobs; relearning after a split is faster than first learning (savings effect). \[C\] (C)

### Fusion (merging)

- Zach likes fusion because it (1) allows gene mixing, (2) can be an analog of marriage, like gem fusion in Steven Universe, and (3) lets him introduce inbreeding into the inner circle. \[Z\] (C)
- Compatibility for fusion is the species boundary. \[Z\] (C)
- Fusion is the basis of elite skill transplant (see State repression). \[Z\] (C)
- Claude proposals: fuse-then-split as a parasexual gene shuffle that also fights mutation buildup (Muller's ratchet); messy "divorce"; monks syncing memory by ritual fusion; practicing clean splits by splitting then fusing back; failed fusion leaving a necrotic scar. \[C\] (C)

### Involuntary splitting and dissolution

- Chronic deflation (depression) lessens the ability to stay incorporated; letting go enough causes an involuntary split, "degenerate mitosis". Zach flagged this would change a lot about how the underclass works. \[Z\] (D)
- Chronic case: random splitting continues until cohesion is lost and the Giglian dies, once pieces lack faculties, mass and fuel. It looks like early embryonic cell division in reverse: smaller and smaller weakened husks that cannot support their own weight, shrivel and dry out into roughly a chunky powder. \[Z\] (D)
- Wall-less cells in the cascade burst under their own weight from lack of nutrient and support. \[Z\] (D)
- Dissolution is always uncontrolled mitosis down to goop, never a separate process. \[Z\] (D)
- Collapse sequence: intentional modifications drop, then the base form, leaving a ballish blob with a strained smiley face (baseline expression is a smile, they are far below baseline). The ball looks like the normal head but blobbier and larger, since it holds the whole body's mass. Worse still, form is lost and they split to death. \[Z\] (D)
- Starvation alone can also cause the collapse to a ball. \[Z\] (D)
- Personal collapse through depression is akin to suicide; forced collapse is akin to extreme shock causing a fatal stroke. \[Z\] (D)
- Suicide (self-inflicted death) is a separate class from depressive degenerate mitosis, and weighs more than for humans because it ends descendants' experience too. \[Z\] (F)
- Forensics: chronic collapse leaves more homogeneous goop than forced collapse (like blood-splatter analysis). \[Z\] (D)
- Claude proposals: the body resorbs into the head on the way down; whether feeding revives a ball distinguishes starvation from pressure failure; dried remains feed the fungi; acute goop keeps lumps of frame and trained tissue; fuel state of cells as a second forensic reading. \[C\] (D)

### Open

- Is an early cascade reversible if the stressor stops, or is there a point of no return? \[OPEN\] (D)
- Do halves of an involuntary split inherit the low baseline (spiral) or get brief relief? \[OPEN\] (D)
- Does a long-held body form become the new default set point? \[OPEN\] (D)
- When the collapsed ball scales up, do facial features stretch or stay small? \[OPEN\] (D)
- At what size is a severed piece a person rather than inert tissue? \[OPEN\] (A)

## Mind, mood, joy and moral philosophy

Giglian ethics centers on a tenet translated as "joy", a healthy outward-growing baseline rather than pleasure, and their language has no independent concept of negative emotion. \[Z\] (D)

### Joy and valence

- "Joy" is not necessarily pleasure; it is closer to a healthy baseline where the individual or collective (depending on social hierarchy) can succeed. \[Z\] (D)
- The word for joy is etymologically muddled like English "happy": pleasure, increased power, needs and wants being met are mixed together, and people argue over what it really means. \[Z\] (D)
- No real concept of negative emotion. Negatives are described relative to the positive. \[Z\] (D)
- Metaphor axis is out and in: positive is outward growth, negative is the outcome of no growth (decay, inward). \[Z\] (D)
- Sadness, misery and depression feel like sinking into yourself, which literally inhibits attention-driven growth. Deep depression means dissolving back into a blob of more neutral cells from lack of effort. Hence joy is physical excellence. \[Z\] (D)
- Claude supplied philosophical references Zach asked for: eudaimonism, the capabilities approach (Sen, Nussbaum), Spinoza's Ethics (joy as increase in power, sadness only relational), Augustine's privation theory. Reference only. \[C\] (D)

### Holding pressure

- A healthy Giglian's default is a steady, slightly positive baseline held as "holding pressure". Going below it is not normal and not believed to be intentional; it is an affliction of stagnation, a loss of holding pressure leading to collapse. \[Z\] (D)
- Some people manage or afford a better baseline through joyous efforts. \[Z\] (D)
- Depression is conceptualized as being unable to hold pressure, sometimes described as "leaky". \[Z\] (D)
- The pressure language is a metaphor, only loosely literal through foam-inflation growth. Depression has a social side, but giggling cannot simply cheer someone up; real causes (loss, mental illness) still need treating, as with humans. \[Z\] (D)

### Giggling and speech

- Giggling is a general social signal of joyous experience, not human laughter's trust and bonding role. Trust is explicit through shared memory and experience, and hierarchy is stronger because you can know what someone would do. \[Z\] (D)
- Speech is a controlled extension of giggling; good speech is thought of as controlled laughter. \[Z\] (D)
- There is no negative-valence giggle, so Giglians struggle to conceptualize or speak about negative valence. \[Z\] (D)
- "Giggle" is only the English label for the vocalization type; see Language. \[Z\] (F)

### Claude proposals, unconfirmed

- Rival schools of joy (expansion, fulfillment, release, social). \[C\] (D)
- Competing folk theories of leakiness: a hole to seal, a weak pump to build, or an environment that drains. \[C\] (D)
- Two vocabularies: state words from the joy domain, cause words borrowed from wounds and medicine (grief as being "wounded"). \[C\] (D)
- A Giglian toxic positivity ("giggle more", "hold up") that fails the grieving. \[C\] (D)
- Fluent pleasant speech can mask low pressure; elites with clean-split control mask best, so "everyone sounds fine" is a warning sign. \[C\] (D)
- A tonic, constant low giggle signal for baseline. \[C\] (D)
- Parallel to computational psychiatry: holding pressure as precision of priors. \[C\] (D)

### Open

- Does grief have its own named place in the moral framework? \[OPEN\] (D)
- Is recovery from leakiness mostly solitary or mostly social? \[OPEN\] (D)
- Should players read the social commentary directly, or mostly feel it through systems? \[OPEN\] (D)

## Identity metaphysics and splitting doctrines

Whether a split continues one experience or ends one and starts two is deliberately unresolvable in-world, so rival doctrines ("camps") hold each view. \[Z\] (F)

### Decided

- Private experience exists but gets less cultural focus, because it begins and ends at mitosis. Conscious experience is like a license you hold until you mitose; then it is split. \[Z\] (F)
- Zach has not decided whether experience continues through mitosis (it just splits) or the original effectively dies and two are born. This sets the existential weight of mitosis. It cannot be verified from inside, and different philosophies can hold either view. \[Z\] (F)
- Giglians always know which memories are pre-split. They feel like their own, but depending on philosophy one can rationalize that they were not actually experienced by oneself. \[Z\] (F)
- Neutral usage is "split" or "mitosis". "Birth" counts only within the death-and-birth camp. \[Z\] (F)
- Doctrine about splitting is not taught in secular post-mitosis re-education. It seeps in through life: a convincing person, a missionary, and so on. It may or may not be inherited at a split. \[Z\] (F)
- Splitting doctrines mostly arose in the city, not from the Founder, who was focused on bureaucracy and progression. The Founder thinks doctrine and religion are silly and tries to contain them without banning them. \[Z\] (F)
- Doctrines trickle outward and sometimes back up and down across classes over long timescales, like posh-England fashion cycles. That drift is lore and history only, not simulated in the game. \[Z\] (F)

### Claude proposals, unconfirmed

- Framing references: Parfit's fission cases; U and non-U usage (Ross, Mitford), Simmel's trickle-down, Bourdieu's distinction, enregisterment. \[C\] (F)
- Evidential grammar marks pre-split vs current-window memory; which marker a speaker uses for old memories reveals their camp. \[C\] (F)
- Each camp has its own word for a split (continuity camp: "branching"-like; death-and-birth camp: mourning-and-arrival vocabulary); the neutral word is a dry founder-era administrative coinage; choosing it signals agnosticism or caution. \[C\] (F)
- The Founder's containment means registering doctrines and keeping them out of courts; the regime's scarcity ideology is itself an unlabeled doctrine. \[C\] (F)
- Missionaries cluster around re-education centers because freshly split Giglians are most receptive. \[C\] (F)
- Since descendants exist only if a split happens, "dying unsplit" may be the real taboo. \[C\] (F)
- Elites drift toward the flat procedural register, so the top sounds most bureaucratic. \[C\] (F)

### Open

- What are the camps called, and how many are there? Stub. \[OPEN\]
- Does missionary success depend on the target's state (grieving, newly split, in power), or only on the argument? \[OPEN\] (F)
- Is the neutral term plainly physical or ceremonial? \[OPEN\] (F)
- Do the outskirts produce their own doctrines? \[OPEN\] (F)
- Which parts of a life are most valued: experiences, built skills, or what is passed on? \[OPEN\] (F)

## The city: founding, layout, economy, food

The city is a near-Texas-sized ring city seeded by one founder's repeated mitosis, where raw goods flow inward and value, food and rights concentrate at the center. \[Z\] (A, E)

### Founding and cohesion

- A city can be seeded by one city planner who mitoses repeatedly to build and staff it. The resulting near-identical psyches act as a low-greed, high-cooperation collective (not a literal hivemind), relying on the plan's effectiveness and the lack of greed among copies of "me". \[Z\] (A)
- A Giglian who leaves, mitoses for several generations outside, and returns may no longer agree with the city. \[Z\] (A)
- Many divergent generations still coexist because the city compels and incentivizes participation: do your part in your (literally your) city and everyone benefits, "like authoritarian luxury communism". \[Z\] (A)
- Government is built around overcomplicated public works and entertainment. Bureaucracy is efficient because Giglians have similar opinions. Not a utopia: slums exist and are covered up or classified by the "benevolent" authoritarian state. \[Z\] (A, M3)
- Cities cannot extend infinitely, so there are well-maintained cores, sketchier outskirts, and unincorporated land or other cities beyond. \[Z\] (A)
- Getting deeper into the city is a low-key psychic-purity matter: outskirts residents are often there because a greedy mitosis put the good parts in the other half. \[Z\] (A)

### Layout

- Circular, with concentric rings. \[Z\] (E)
- **Center (elite):** sprawls edge to edge; skyscraper offices at its edge, then expensive apartments, high-rise condos, penthouses. Roughly the size of a small state. \[Z\] (E)
- **Middle ring:** bumps up against the center, feeding off it while trying to get in; smaller but still large office buildings, then suburbs and small businesses. \[Z\] (E)
- **No man's land:** a tapering buffer between middle and outer rings. \[Z\] (E)
- **Outer ring:** mainly farming, livestock, mining and drilling, with some material-processing factories on its inner edge, then barracks, slums and markets, ending in open desert. \[Z\] (E)
- Whole city a bit smaller than Texas. \[Z\] (E)
- Claude estimated a radius near 250 miles and a 60 to 100 mile center radius, making a core-to-desert trip multi-day. \[C\] (E)

### Resource flow

- Manufacturing sits in the outer-middle zone. High-speed rail or maglev ships raw resources from the outer ring to a middle-ring checkpoint, where they are distributed for manufacturing, then shipped to the center and redistributed outward. \[Z\] (E)
- Few middle-manufactured goods reach the outer ring; goods both made and produced by the middle travel farther out. Center luxuries mostly stay in the center unless you have connections. \[Z\] (E)
- The middle ring manages but does not own. The center keeps watch through people well aligned with it, under promise of favorable marks on the center entrance evaluation. \[Z\] (E)
- People near the entrance have jobs that take them into the center on business, and eventually earn enough trust to be promoted into more rights within. \[Z\] (E)

### Food and ideology

- Food scarcity is a mix: real scarcity caused by artificial means on the outskirts, and controlled distribution in the middle rings. \[Z\] (C)
- The over-developed center cannot support its own demand, which is the resistance's natural lever. \[Z\] (C)
- The inner city believes itself a post-scarcity utopia: stay in line and you get protection, like a company town or mob protection. It willingly ignores the outskirts until it forgets. \[Z\] (C)
- Middle-ring loyalty is not purely religious; it is a Randian corporate "utopia" myth, in the spirit of "who is John Galt?". \[Z\] (C) Clarified: not a rhetorical shrug, but a mythological Founder spoken of as still in power, while in reality mitosis slowly degrades the original ambition and memory. \[Z\] (C)

### Claude proposals, unconfirmed

- Urban theory framing: von Thunen rings and the monocentric city; kin selection (Hamilton's rule); Anderson's imagined communities. \[C\] (A)
- Radial freight lines as resistance chokepoints; the no man's land as checkpoints, customs and quarantine infrastructure; fast prestige lines inward, slow freight outward. \[C\] (E)
- The entrance evaluation as a tournament that fragments the middle ring; tiered rights (day passes, clearance, limited residency, citizenship), each a hostage; couriers as both informants and resistance eyes; stalled low-tier middle-ringers as best recruits. \[C\] (E)
- Humidity and climate control as a class good; spore-load quarantine as a surveillance pretext. \[C\] (C)
- State seed monopoly over cultivars, manufactured blights, calorie licensing cross-checked against registered splits; fast spoilage keeps the core just-in-time. \[C\] (C)

### Open

- Where farmland water comes from, given the open-desert edge. \[OPEN\] (E)
- What the center entrance evaluation actually tests (skill, loyalty, genetic compatibility). \[OPEN\] (E)
- How the center verifies identity at the border (papers, memory, tissue). \[OPEN\] (E)
- Does the middle ring know the outskirts are starved deliberately? Does the state keep real reserves? \[OPEN\] (C)
- Inter-city politics: other cities seeded from other founders. Stub. \[OPEN\] (A)

## Government, the Founder, elites

The state is a city-state-corporation run as a direct line of control from the Founder, a title held by whichever living descendant is fewest splits from the original. \[Z\] (B, C)

### The Founder

- The original founder no longer exists; "the Founder" is whichever descendant is fewest splits from the original. \[Z\] (C)
- The chain of command follows split distance: the founder mitosed, the subordinate half mitosed further, and so on, so rank tracks how many iterations you are from the original. \[Z\] (B)
- The Founder is spoken of as a mythological figure still in power. In reality mitosis slowly degrades the original ambition and memory. \[Z\] (C)
- The current ruler holds most of the original's memory thanks to careful splitting, but splits strip learned ability and training needed to run the state. If unrest or infighting (caused by the protagonist) reveals the ruler has no real skill left, only the founder's record of experience and ideas, then as new ideas gain popularity in the inner circle the Founder could be labeled a fraud or a puppet. \[Z\] (C)
- Skill restoration: fuse the ruler with a sacrificial, highly skilled member of the inner circle, then mitose again and split off the rest of that person as waste. \[Z\] (C) Donor rules are under State repression.
- The founding era was laser-focused on bureaucracy and progression; the Founder treats religion and doctrine as silly and contains it without banning it. \[Z\] (F)
- Founding origin (not final): a settling party arrived, and the founder betrayed and slaughtered them at an opportune time so they could be the sole seed of the civilization. \[Z?\] (C)

### Elites and knowledge

- Everyone in power is the "purest", because the state is a direct line to the founder. \[Z\] (C)
- Elites know clean splitting because the founder had to mitose to plan the city and learned it well. Knowledge is graded: leaders get the memory and skill as backup, workers are not given it. \[Z\] (C)
- Leaders likely know what the main pain medicine does (tobacco-industry style) but keep plausible deniability, since they rarely had to work for their position and can claim no memory of its effects beyond covered-up recreational-use scandals. Only a token few loyal climbers from below know firsthand. \[Z\] (C)
- Fusion within the inner circle brings inbreeding. \[Z\] (C)

### Governance structure

- Removing the Founder runs through a council vote, not a democratic election. \[Z\] (F)
- Ousting the top levels, up to the Founder seat, requires replacing enough of the rest of government to veto or impeach them. \[Z\] (F)

### Claude proposals, unconfirmed

- "Memory laundering": a leader splits before a dirty decision and casts off the half that knows. \[C\] (C)
- Authorship (remembering intent) vs competence (running the state) as two separate kinds of legitimacy; "puppet" (useful figurehead) vs "fraud" (discarded) as different accusations. \[C\] (C)
- Someone else must perform the ruler's splits, so they may be curating what "the Founder remembers". \[C\] (C)
- The regime has a skill clock: each purge spends the ruler's own skill; collateral lines may hold more of the original than the official ruler. \[C\] (C)
- Ruler copies as stand-ins and succession backup; the ruler's split history classified. \[C\] (C)
- After many harvests the ruler becomes a composite of everyone consumed; inbreeding shows as growth-control failure (a Habsburg-jaw analog). \[C\] (C)
- Veto player theory (Tsebelis) as framing; recordkeepers who certify lineage as a hidden veto point. \[C\] (F)

### Open

- Who performs the ruler's splits, and does the ruler know they might be edited? \[OPEN\] (C)
- Does the regime know its skill is running out? \[OPEN\] (C)
- How is the council seated (lineage, appointment, co-option), and can members be recalled? \[OPEN\] (F)
- Is the impeachment threshold a seat count, or specific offices (records, courts, council) agreeing? \[OPEN\] (F)
- The original founder's motive in detail. \[OPEN\] (B, C)

## Law, courts, evidence

Giglian law presumes an unequal split was intentional, rebuttable only by rarely provable duress, and its courts lean heavily on testimony. \[Z\] (A, C)

### Greedy mitosis law

- Greedy (unequal) mitosis is a hot political debate, shaped like the pro-life debate but framed as "it's unethical to create a half that has no chance at success". \[Z\] (A)
- Mitosing is a conscious decision, so an unequal split is presumed intentional unless the Giglian proves it was induced under stress or duress. \[Z\] (A)
- Proving coercion is about as possible as proving a child was conceived by rape: rare, but sometimes possible through circumstance and corroboration. \[Z\] (A)
- A case pits the greedy half against the discarded half. \[Z\] (A) If coercion is proven, neither half is culpable; liability falls on the coercer (another individual, an employer, or the state). \[Z\] (A)

### Testimony and history

- Courts generally trust testimony more than humans do. A culprit who has mitosed into 8 by trial means 8 witnesses. \[Z\] (C)
- Courts were surely corrupt earlier in Giglian history, like pre-19th-century Earth, and this is taught in history class as the rise and fall of nations. \[Z\] (C)

### Claude proposals, unconfirmed

- Legal framing: wrongful-life claims; mens rea with a duress excuse (strict liability with an excuse clause). \[C\] (A)
- The two halves share all pre-split memory, so trials are about interpretation and motivated reasoning, not hidden facts. \[C\] (A)
- Siblings who split after an event count as one source; corrupt courts counted them as many (show trials); disagreement between siblings is the forensic signal; "independent witness" defined by lineage distance. \[C\] (C)
- A split registry (timestamp and lineage of every mitosis) as the post-corruption reform and the first great bureaucracy; whoever edits it can hide purges. \[C\] (C)
- Untrained workers cannot aim a split, so presuming intent punishes them for bad luck; a reform movement could argue this. \[C\] (C)
- Intoxicated mitosis, chemical coercion to force an uneven split, and drug traces in a cast-off half as evidence of duress. \[C\] (C)
- Killings valued by how much unshared experience died; liability attached to the whole branch to stop culprits splitting to dilute punishment. \[C\] (C)
- Forensic goop reading as a contested, state-controlled discipline. \[C\] (D)

### Open

- If coercion is not proven, is the greedy half liable by default, or does the case go nowhere? \[OPEN\] (A)
- Does a descendant owe for a crime they remember committing? \[OPEN\] (C)
- Is a killing priced by lost memory, or by the sanctity of the body? \[OPEN\] (C)
- Is the skill-rich half obligated to support the skill-poor one? \[OPEN\] (C)
- Is forensics a recordkeeper specialty or a state role? \[OPEN\] (D)

## Medicine, drugs, early technology

Giglian medicine is mostly topical herbalism, constrained by one rule: anything that dulls sensation also dulls the attention the patient needs to heal. \[Z\] (C)

### Tools and early technology

- Giglian tool use diverges from human: besides early-tool analogs, they make clothing, ointments and similar to survive other climates. \[Z\] (C)
- Claude proposals: moisture tech first (hydrogel wraps, damp fungal mats); ointments as the key invention (sealants, hygroscopic coatings, antifungals); braces and scaffolds to hold a shape without paying attention for it; fungal farming as the founding technology (fungal leather, chitin, glues); ointment supply as a state control lever over who can leave the humid core. \[C\] (C)

### Healing practice

- Lots of herbal medicine around skin issues. \[Z\] (C)
- Scar removal: cut out small shallow wedges, hold them closed, repeat until all scar tissue is gone. Cuts stay shallow so an ordinary patient can will the wound closed without being distracted. \[Z\] (C)
- Passive healing exists, attending to the wound speeds it. \[Z\] (C)
- No anesthesia, not even local, because it dulls the ability to attend to growth. General pain-numbing salves still exist, weak or local enough not to inhibit movement. \[Z\] (C)

### The main medicine (opioid analog)

- Numbs pain without much affecting attention or sensation, like a drug where you can technically still ambulate but shouldn't drive. \[Z\] (C)
- Blue-collar workers get addicted after overexertion injuries (like hurting your back lifting on the job). Zach called this "beautiful". \[Z\] (C)
- Leaders know its effects, tobacco-industry style, with plausible deniability (see Government). \[Z\] (C)

### Claude proposals, unconfirmed

- Ailments: dry rot from desiccation, spore infections, slime-layer loss, "mis-growth" as the cancer analog, numb zones, failed-fusion scars, split scars. \[C\] (C)
- Pharmacopeia of ion-channel drugs: growth locks, growth primers, hygroscopic balms, antifungals; a recreational "shape-drunk" compound. \[C\] (C)
- Pain is the targeting map for attended healing, which is why local anesthesia cannot work. \[C\] (C)
- Healers as coaches; dosing by lineage skill as well as body size. \[C\] (C)
- Graded impairment: willing a mitosis is the first ability lost under heavy sedation. Tolerance from the network turning sensitivity up; withdrawal as involuntary rippling and uncontrolled growth. \[C\] (C)
- Held-form strain (bracing as living scaffolds) as the typical injury; employer as pusher; splitting to dump a hooked half fails because dependency splits unevenly too. \[C\] (C)

### Open

- Is herbalism a respected craft or a tolerated gray market in the core? \[OPEN\] (C)
- Is the main medicine state-controlled or a free folk remedy? \[OPEN\] (C)
- Do the first tools come from the body (secreted materials) or the flora? \[OPEN\] (C)
- Do split scars carry their own cultural meaning? \[OPEN\] (C)
- Do lineages differ in passive healing speed, or only in attended skill? \[OPEN\] (C)

## Religion, monks, recordkeepers, history, education

Because memory dilutes with each split, Giglian society depends on long-lived memory holders (monks and recordkeepers), history classes, and re-education after every split. \[Z\] (C)

### Religion

- Religion is likely tied to record and family-history keeping, as churches kept family histories and printing began as religious. It also fills explanatory gaps before the scientific method. \[Z\] (C)
- Doctrines on what splitting means are a city phenomenon (see Identity and doctrine). \[Z\] (F)
- Claude proposals: the central theological gaps are identity after a split, death, "the Forgetting" of lost eras, and the founder; slow-splitting monastic orders as clergy and living libraries; greedy mitosis as sin and the cast-off half as a "lost soul"; fusion with a lost half as sacrament; the dead feeding the fungal farmland as a literal cycle; heresy detectable by divergence from an orthodox lineage. \[C\] (C)

### Monks

- Monks live simple lives for centuries in solitude, holding historical knowledge. Several live in each cloister, but they get no visitors. \[Z\] (C)
- In the game, the player meets a solitary recordkeeper monk who remembers the time before the city. \[Z\] (C)
- Claude proposals: stillness keeps metabolism low so a cloister feeds many; no visitors protects the archive from spores and state-edited memories; monks drift from current culture; several monks may be halves of one person; monks share memory by ritual fusion; the order may refuse to take sides. \[C\] (C)

### Recordkeepers

- Civilizations also have recordkeepers who live longer than most. \[Z\] (C)
- There is likely a cultural norm for what year or age you should mitose, like when to have a baby. \[Z\] (C)
- Claude proposals: recordkeepers split on a fixed schedule with halves posted to different offices; the longest-lived clerk is a prime bribery or assassination target; "split too late" hoards unshared experience, "split too early" leaves both halves short. \[C\] (C)

### History education

- A history class is needed because memory survives only so many splits; after enough, most cannot remember an era. It teaches the earlier corrupt courts as the rise and fall of nations. \[Z\] (C)

### Re-education and higher learning

- A post-mitosis Giglian is not an infant: they keep half the memories but lose half the learned skill, so there is baseline re-education plus higher learning beyond it. \[Z\] (C)
- A split can cost someone their livelihood: a good pianist and good tailor might keep the piano (a hobby) but lose the sewing muscle memory, and so their income. \[Z\] (C)
- Doctrine is not part of secular re-education. \[Z\] (F)
- Claude proposals: relearning is faster than first learning; education runs alongside refeeding; siblings are the best teachers; the intake assessment doubles as evidence of a greedy split; re-education is also an indoctrination window; people keep a second marketable skill as insurance; split clauses in employment contracts; lineage "skill-banking". \[C\] (C)

### Clean splitting

- Cleaner, controlled splits are possible but need training that mostly only elites get. \[Z\] (C)
- Elites learned it because the founder had to mitose to plan the city; leaders are given the skill as backup, workers are not. \[Z\] (C)
- It is a learned skill, so dissidents can learn it too, for example the protagonist on the full-mitosis path. \[Z\] (C)
- Mechanism (from the split mechanics): selectively holding some tissue rigid while the rest relaxes. \[C+\] (D)
- Claude proposals: practice requires real splits and fusing back, which needs a compatible partner, lots of food, time and safety; one's own halves are the ideal practice partners; the state's defenses are cost (food rationing) and surveillance rather than secrecy; trained dissidents can resist forced splitting. \[C\] (C, D)

### Open

- One state-fused faith, or several competing? \[OPEN\] (C)
- Is the monastic order allied with the state, or an old schism? \[OPEN\] (C)
- Is the customary split age one norm, or by trade and lineage? \[OPEN\] (C)
- Is baseline re-education state-run and mandatory, or left to family and lineage? \[OPEN\] (C)
- Does the state ration clean-split training openly, or deny it exists? \[OPEN\] (C)

## State repression

The regime controls dissent mainly through forced splitting: dissent is cut out and destroyed when small, and exiled or imprisoned when it amounts to a whole person. \[Z\] (B, D)

### Purge by mitose and forced splitting

- The state quietly uses coerced mitosis to extract dissent into a disposable half, so the outskirts are full of cast-off halves. Claude coined "purge by mitose"; Zach adopted it with enthusiasm. \[C+\] (B)
- Since involuntary splitting comes from letting go, the upper class can force subjects to split a certain way through controlled torture or trauma. \[Z\] (D)
- Forced splitting is a secret but common way of controlling dissent: forcibly split off just the piece or pieces holding dissent, then kill or incinerate that part. \[Z\] (D)
- Subjects with too much dissent to destroy, because the dissenting piece constitutes a mitosed person, are exiled to the outskirts or to a prison or camp, probably in the outskirts. \[Z\] (D)

### Forced collapse as torture

- Forcing stress-based dissolution is one of the most brutal tortures. It is not done just to kill (a blender is cheaper); it is done behind closed doors to split someone, or worse, until each part confesses. \[Z\] (D)
- Because the goop is forensically traceable, no ordinary murderer would try it; only the worst of the worst at the top would do it to their enemies. \[Z\] (D)

### Skill harvesting

- The ruler restores lost skill by fusing with a sacrificial skilled donor and splitting off the rest of the donor as waste. \[Z\] (C)
- Donors must come from the city center, never the outskirts: inner-city Giglians share the ruler's ideology and are trained where the ruler needs it, while an outskirts Giglian carries the experience and truth of the predatory system, which would destabilize the faith. \[Z\] (C)
- Waste halves from harvests are handled by a mixture of exile and political imprisonment. \[Z\] (C)

### Economic control

- Manufactured food scarcity on the outskirts and controlled distribution in the middle rings (see The city). \[Z\] (C)

### Claude proposals, unconfirmed

- Interrogators can steer forced splits; each fragment is a witness holding a different slice; several fragments "corroborate" a forced confession in a testimony-trusting court. \[C\] (D)
- Forced splitting framed as "treatment" for a failing baseline; survivors return calm with an unexplained memory hole, which reads as cured joy. \[C\] (D)
- Defenses: holding key substrate rigid under duress, or deliberately splitting first and stashing the dissent-holding piece in a resistance safe house to fuse back later. \[C\] (D)
- Records as a counter-check: a person whose memory contradicts the written record is a flagged purge survivor. \[C\] (D)
- Exiles are halves of loyal citizens still in the city, so separation prevents re-fusion. \[C\] (D)
- Camps hold inmates near the collapse threshold; prisons control food and humidity because walls cannot hold a squishing, splitting body; exiles are memory-washed by a further split. \[C\] (C, D)
- Waste halves of true-believer donors are ideal resistance messengers to the middle ring. \[C\] (C)
- Overshot interrogations leave lumpy goop that loyalists homogenize; a "too chronic" death becomes a tell. \[C\] (D)

### Open

- Does a purged survivor sense that something is missing? \[OPEN\] (D)
- Can exiles ever fuse back with their loyal half? \[OPEN\] (D)
- Is the prison one hidden site or scattered cells in the middle ring? \[OPEN\] (C)
- Is the pain medicine used in interrogation? \[OPEN\] (D)

## Resistance and routes to power

There are two broad ways to topple the regime: revolution (outer ring plus middle ring seize the supply lines) or the much harder peaceful route of persuading enough of the inner government to veto or impeach the Founder. \[Z\] (C, F)

### Revolution

- The natural weakness is the over-developed center, which cannot feed itself. \[Z\] (C)
- Not a flat farming boycott: farmers could still feed themselves, but it would starve the middle rings. Instead the resistance must organize and convince the middle rings to join, then together commandeer shipments and serve only themselves. \[Z\] (C)
- This is treacherous because many are ingrained in the propaganda of the mythical, godlike Founder and see the resistance as terrorism. \[Z\] (C)
- Sequence: build a movement out of the outer ring, convince the middle ring, add their support and control of the supply lines, then bring the inner ring to its knees. Considerably easier than the peaceful route. \[Z\] (F)
- Unrest or infighting caused by the protagonist can expose that the ruler has no skill left, letting the inner circle brand the Founder a fraud or puppet. \[Z\] (C)

### Peaceful route

- Social engineering through a council vote, not a democratic election. \[Z\] (F)
- Ousting the top requires replacing enough of the government to veto or impeach. \[Z\] (F)
- The inner ring needs a "stealth" approach to be convinced peacefully. Failed persuasion makes inner-ring agents angry (or disgusted) and they label the persuader a terrorist. \[Z\] (G)

### Rhetoric and labeling

- Revolutionary rhetoric spreads naturally inward until the upper class catches on and scorns it as terrorism. \[Z\] (F)
- The terrorism labeling is emergent from agents, not a hard rule, so the peaceful path stays possible. \[Z\] (F)

### Infiltration

- Infiltrating the center is required on every path. The recruitment path likely has more middle-ring support (from convincing them to join), which gives easier access. \[Z\] (E)

### Claude proposals, unconfirmed

- Ledgers of real yields vs quotas, held by middle-ring clerks, as the most persuasive evidence; the monks' archive as counter-history. \[C\] (C)
- Operational security by split timing: cells split before receiving sensitive details, since siblings share memory. \[C\] (C)
- The state's best counter is a staged blight timed to the first seized shipment. \[C\] (C)
- Flip the Randian frame: the outskirts farmers are the real producers and the core the looters. \[C\] (C)
- The middle ring splits into aspirants (high stake, loyal) and the unaspiring (swing group); disillusioned aspirants are the best recruits. \[C+\] (G)
- Supply squeezes can open persuasion options, so the two routes can be mixed, but violence raises threat labels that close inner-ring doors. \[C\] (F)
- Real-world framing: Gene Sharp's pillars of support, Chenoweth and Stephan on nonviolent campaigns, Granovetter threshold models, Snow and Benford framing theory. \[C\] (F)

### Open

- Should supply lines be a simulated resource flow, or an abstract per-ring pressure value? \[OPEN\] (F)
- Where does the resistance get food reserves to survive a squeeze (wild unincorporated farmland, smuggling)? \[OPEN\] (C)

## Language, phonology, conlang

Zach wants a full Giglian conlang, derived from their anatomy and grown alongside history and narrative Tolkien-style; it is a worldbuilding tool, while the game itself ships in English. \[Z\] (E, F)

### Scope and method

- Game input and output text is English (or the player's language, a later localization issue). Giglian is for Zach's worldbuilding: deriving names, places and culture. \[Z\] (F)
- A full conlang, not just morphemes, so idioms, syntax quirks, vocabulary and verbiage are well defined. English game text translates it directly, with Giglian loanwords for Giglian-specific actions and concepts humans lack words for. \[Z\] (F)
- Building the conlang is a main source of fun for Zach. \[Z\] (F)
- Method: language, worldbuilding and narrative developed together and piggybacking, so culture shapes how language spreads and changes and vice versa; the full narrative is written so the world breathes rather than sitting as ideas. \[Z\] (F)
- A full conlang is necessary for a culture with almost nothing in common with humans besides social order, so the Giglians do not read as "space Germany". Pointy-eared-human elves could do without one. \[Z\] (F)
- The species endonym waits until the phonology is done. \[Z\] (E)

### Physiology for phonology

- Phonology comes from physiology; the goal is something humans can still roughly pronounce. \[Z\] (E)
- No teeth. Probably a cartilaginous beak as part of the lips: mouth corners more flexible, center and behind stiffer so they can bite. Whether they need a hard surface depends on how they eat, still undecided. \[Z?\] (E)
- The human-tongue equivalent is completely fused to the floor of the mouth, so the mouth is a variable-length tube opened and closed by a fleshy tongue-like pad. \[Z\] (E)
- No nose. \[Z\] (E)
- Speech sounds like a human talking with the tongue held back in the throat; dental-fricative-like sounds are made with the middle of the tongue against the palate. \[Z\] (E)
- Zach tested this himself and can speak pretty well with those restrictions while holding nose and velum closed, so the inventory is richer than Claude first predicted. \[Z\] (E)
- Speech is controlled giggling, and "giggle" is only the English name for that vocalization type. \[Z\] (D, F)

### Claude proposals, unconfirmed

- Phonetic predictions: no nasal contrast; most tongue-tip consonants collapse into pad-against-palate places plus labial, pharyngeal and glottal sounds; vowel quality from tube shape and lip rounding; contrast shifted to length, pitch and phonation; variable tube length as a global formant knob for prosody; giggle pulses as syllable nuclei; beak taps as click-like consonants. Caveats: Zach still has a mobile tongue body, and perception (what listeners can distinguish) limits phonemes more than production; record and compare spectrograms. \[C\] (E)
- Grammar features that pay off: evidentiality marking pre-split vs current memory (ties to blackboard source tags), "window"-based tense, pronouns for "the one I was" and "the one who split from me", graded giggle intensity as mood or register. \[C\] (F)
- A per-lexeme policy table: plain translation, calque ("hold your pressure"), or loanword. \[C\] (F)
- Idioms drawn from Giglian biology (pressure, holding, growth) instead of hearts, blood and eyes; test alienness through insults, oaths and endearments. \[C\] (F)
- References: Tolkien's Appendix F translation convention; Dwarf Fortress compositional names with English glosses; Heaven's Vault and Chants of Sennaar; Rosenfelder's Language Construction Kit; Peterson's The Art of Language Invention; sound-change appliers; Tolkien's languages-first account and the Thingol ban on Quenya as narrative reshaping language; short written scenes as vocabulary probes. \[C\] (F)

### Open (stubs)

- Phoneme inventory, phonotactics, romanization. \[OPEN\]
- Can the pad bulge independently at several points (palatal vs velar contrast), and can it seal against the palate or does it flutter? \[OPEN\] (E)
- Start from the sound system or from needed grammatical categories? \[OPEN\] (F)
- The proto-language and the first event or migration that splits it. \[OPEN\] (F)
- Are evidential markers obligatory? \[OPEN\] (F)
- Endonym for the species and names for places. \[OPEN\] (E)

## Game design: premise, protagonist, paths

The game is an RPG where a cast-off half of the Founder lineage works to topple the regime by one of four paths, with endgame routes inspired by Fallout: New Vegas but not built like a Bethesda RPG. \[Z\] (B, C, E)

### Premise and protagonist

- Working plot: over the city's history the head of the city-state-corporation kept a chain of command by split distance. The one remaining closest to the first split holds the most lived experience of the world before, and so still carries some "humanity", deemed a weakness. They mitose the "good" and "bad" parts apart, producing one perfect fascist leader and one "weak" half that wants change (escape from groupthink, civil liberty). The weak half is cast aside and becomes the protagonist. \[Z\] (B)
- The motive for that split was not worked out; Zach liked purge by mitose (the state's own tool turned inward) as the precedent. \[C+\] (B)
- The protagonist is the most capable dissenter because they are half of a full founder-level person, not the marginal waste of dissenters further down the chain. \[Z\] (B)
- Reconcile: later lore says the original founder no longer exists and the Founder is a diluted lineage tip with memory but little skill, so the protagonist is half of that diluted ruler. \[Z\] (C) The wiki should note this as a refinement of the original premise, not a contradiction to resolve silently.
- Player agency over where the plot goes (revolution or otherwise). \[Z\] (B)
- The goal of toppling the regime is like Fallout: New Vegas, but not a Bethesda-type RPG. \[Z\] (C)

### The four main paths

| Path | Bodies come from | Notes |
| --- | --- | --- |
| Solo recruitment | Recruits only; never mitose | \[Z\] (E) |
| Mitosis + recruitment | Balanced mitosis plus recruiting | \[Z\] (E) |
| Balanced mitosis | Own halves only, no recruitment | \[Z\] (E) |
| Unbalanced mitosis | Make yourself powerful with an army of peons | The "evil" route; may involve recruitment, likely through fear \[Z\] (E) |

This four-path set supersedes the earlier spectrum of recruit-only, self-mitose-only and a neutral middle. \[X\] (B, C)

### Rules attached to the paths

- Infiltrating the center is required on every path; recruitment gives easier access via middle-ring support. \[Z\] (E)
- On every path, at each mitosis the player chooses which half to continue as; the other half becomes an ordinary GOAP NPC. There is no swapping between halves (no psychic link in lore, and swapping would act as teleporting, break up the game, and buff the neutral path over solo recruitment). \[Z\] (E)
- Skill-tree flavor by path: neutral builds mix some mitosis with using others for numbers; full recruitment or solo play gives more offensive skills; full mitosis gives abilities specific to splitting and regenerating well. \[Z\] (C)
- Clean splitting can be learned by the protagonist on the full-mitosis path. \[Z\] (C)
- Two macro routes to victory: revolution vs peaceful council takeover (see Resistance). \[Z\] (F)
- A solitary monk recordkeeper who remembers the pre-city era is a planned encounter. \[Z\] (C)

### Claude proposals, unconfirmed

- Possible endings: merge the cast-offs; reintegrate with the leader's half; become the next leader; dismantle the city. \[C\] (B)
- The unbalanced path mirrors the founder; success there means becoming the next Founder, subject to the same decay. \[C\] (E)
- The abandoned half can return as ally, rival, or regime captive who testifies against you. \[C\] (E)
- Choosing a half under a clean split (informed partition) vs a dirty split (partly random gamble). \[C\] (E)
- The monk as the founder's own first discarded conscience rather than a party survivor. \[C\] (C)
- Design risks: legibility of many rules without a codex; keeping cheerful art direction so the horror lands. \[C\] (D)

### Open

- Does the leader's half know the protagonist survived (cast aside vs hunted)? \[OPEN\] (B)
- Where does the player start: loyal inside the middle rings, or already on the margins? What are the first ten minutes? \[OPEN\] (D)
- Endings list. Stub. \[OPEN\]
- Does the unbalanced army come from your own fragments, or from Giglians pressed into service by fear? \[OPEN\] (E)
- Is the half choice made before the split (designed partition) or after (pick between two determined halves)? \[OPEN\] (E)
- Is the monk a witness to the founding massacre, or a cast-off piece of the founder? \[OPEN\] (C)

## Game design: progression, dialogue, player agent

Memory gates what the player can say, skills govern what the body can do, and the player is a full GOAP agent that NPCs model like any other. \[Z\] (C)

### Two-axis character model

- Dialogue options are gated by what you have experienced and remembered this playthrough, not by skills affecting speech checks. \[Z\] (C)
- Skills govern growth abilities (movement and similar) on a skill tree. \[Z\] (C)
- Earlier, Zach liked Disco Elysium-style traits that lock which dialogue options are available later instead of a Fallout SPECIAL sheet, and pictured mitosis "locking in" traits by splitting away what you learned. \[Z\] (B) The memory-gating rule above is the later, more specific form. \[Z\] (C)
- Memory is medium-grained. \[Z\] (C)

### Skill-point economy for mitosis (from chat B)

Zach kept this deliberately separable from whatever dialogue, skill-check and leveling systems come later; he did not specify where points come from. \[Z\] (B)

- A non-mitosing run just levels normally with skill points. \[Z\] (B)
- Mitosing halves the point values; with an upgrade or difficulty option, each half gets 60% of the unsplit total (10 points becomes 6 per half). \[Z\] (B)
- No half may get more than half the points unless the player specs into the mitosis route to unlock unbalanced mitosis. \[Z\] (B)
- With the 20% bonus and the unbalanced perk: all 10 points may go to one half, then the 20% bonus is split evenly on top (1 point each from 10, 2 each from 20). \[Z\] (B)
- Unspent points saved until a split can be distributed freely (evenly, without the perk). \[Z\] (B)
- Already-assigned points split per skill while keeping totals even, for example int 5, str 3, agi 8 becomes A: 2, 1, 5 and B: 3, 2, 3. Unequal totals need the perk. \[Z\] (B)
- Unbalanced splitting is learned the way the body learns it: repeatedly attempting uneven splits across generations raises how unevenly you can assign, up to splitting off everything except the 10% each half gets free. \[Z\] (B)
- The further you spec into uneven mitosis, the less charitable the extra becomes, until max-level uneven mitosis outright loses total power. Speccing into clean splits instead is rewarded at higher levels with more than 20% extra. \[Z?\] (B)
- Non-mitosis might get more points per level, or might instead need a nerf, since it never pays the split cost and can hoard points. \[Z?\] (B)
- Example of starting state: the protagonist is the discarded portion that was open to outside opinion and change, so is weak at fascist-style leadership, though not necessarily good at any leadership style. \[Z\] (B)
- Claude notes: depth beats breadth for single-actor checks; total power grows by 1.2 to the n per split with the bonus; price greedy splits through world consequences (persistent discarded halves) rather than point nerfs; cap bodies with the food cost. \[C\] (B)

### Player as a GOAP agent

- The player is an actor under the same GOAP conditions as NPCs, but the human does not see the blackboard; they just play. \[Z\] (C)
- The player's blackboard is hidden only from the human. NPCs can see it, so they interact with the player as a GOAP agent and speak in a way that feels intelligent, as if they see and remember. \[Z\] (C)
- NPC-to-NPC blackboard cooperation stays visible in the world, as in Boeda's multi-agent GOAP paper. \[Z\] (C)
- NPCs experience things about the player, remember what you tell them, and build a model of you (predicting your goals). They do the same about each other; this is the general mechanism for cooperation. \[Z\] (C)
- Plan to make the hidden layer a theory-of-mind style layer. \[Z\] (M1)
- The player agent is a full GOAP agent that cannot act on its own. Its expected goals (the general NPC goal substrate plus the quest tree made into goals) and its preferred action can be scored against what the human actually does. \[Z\] (C)
- Claude proposals: NPCs should read a modeled view of the player except inside trust or lineage groups (no omniscience); plan recognition by scoring actions against each goal's plan; surprise as a signal; an "exploring" bucket to avoid over-reading noise; keep models per NPC to avoid railroading. \[C\] (C)

### NPC dialogue output

- Each character's dialogue is informed semi-procedurally by GOAP state. Low end: a non-neural interpreter of the state and blackboard that procedurally generates dialogue. High end: an LLM fed state, character background and a few candidate ideal dialogue-tree scripts. \[Z\] (C) Later interpreter discussion leans away from LLMs (see Interpreter section). \[Z\] (F)
- Claude proposals: show locked options with reasons; keep memory flags coarse; NPCs voice what they believe about you plus a journal for legibility; an LLM tier may talk but never decide; hand-author plot-critical beats. \[C\] (C)

### Persuasion as play

- Zach wants a game where you actually talk to people to convince them to join, instead of a script assigning followers, with procedural input matching procedural output. \[Z\] (C)
- Recruiting: the player explains a goal, and the agent asks for clarification, justification or sources in a back-and-forth until convinced. \[Z\] (G)
- Claude proposal: prototype with a menu of acts first; if persuasion is not fun with buttons, typing will not fix it. \[C\] (C)

### Open

- Is the shadow agent a hidden director shaping pacing, or only an analysis tool? \[OPEN\] (C)
- Can the player lie, and do false claims plant false models? \[OPEN\] (C)
- Does trust accumulate across encounters? \[OPEN\] (C)
- Is the 20% bonus free points or a scaling of assigned points, and can a half exceed the unsplit value in a skill? \[OPEN\] (B)
- Actual skill list and tree. Stub. \[OPEN\]

## GOAP agent architecture

The core bet: every agent runs the same GOAP code over its own state, speech acts are ordinary planner actions, and text or audio is only a renderer that never feeds back into the simulation. \[Z\] (G, M2)

### Foundations

- GOAP-based game AI with inter-agent blackboard sharing that enables emergent cooperative behavior. LGOAP adds long-horizon plan influence. \[Z\] (M2)
- Framed as a handwritten symbolic approximation of abstract goal-directed reasoning: emergent but interpretable. \[Z\] (M2)
- Was on hiatus; active again as of late October 2026. \[Z\] (M2)
- Decided against using Jev (his separate decision model over up to 255 labeled options) as a chooser inside GOAP; instead, everything runs on confidence values inside the GOAP system. \[Z\] (G) Earlier idea, now dropped: Jev picks which precondition to target each step so an agent can give up on a stuck branch. \[X\] (M4)

### Staged build plan

Zach's plan: start from a toy environment (agents work jobs to earn and feed themselves; farmers feed themselves from surplus on top of export yield), scale up to the ring hierarchy and supply system, then add communication in stages from simple to full verbal, starting from Boeda's GOAP cooperation paper. \[Z\] (G)

Ladder as revised in chat G (Claude's structure, adopted as the working plan; \[C+\]):

1. **Stage 0, solo survival:** one agent, hunger, farm or buy to eat.
2. **Stage 1, wages:** employers post jobs to a shared board.
3. **Stage 2, ring supply chain:** outskirts surplus, middle hauls, core pays; cut a link and check starvation propagates correctly.
4. **Stage 3, reactive cooperation:** typed messages (request, offer, accept, refuse) per Boeda; goals accepted as given.
5. **Stage 4, reflection:** goal provenance plus a forward model, still no language.
6. **Stage 5, modeling others:** other agents' goals and predicted behavior (plan recognition).
7. **Stage 6, verbal acts** as interventions on beliefs and goal provenance.
8. **Stage 7, text interpreter, then politics** (council, veto bloc, rhetoric spread, shared threat labels).

- Zach's framing of the jump at stages 4 and 5: agents gain prediction of future world states, so they can ask why they pursue a goal rather than accept it as given. \[Z\] (G)
- Claude proposals: each stage is an ablation with numbers (throughput, starvation, recovery time); headless runs need no renderer; first milestone is a farmer whose backward plan fails until a hauler accepts an offer; message schemas at each stage are subsets of the final speech-act schema. \[C\] (G)

### Reflection, doctrine and reactions

- Beliefs and doctrine sit on top of goal reasoning and govern what an agent is willing to question. Inner-ring dogma is pervasive, so convincing them peacefully needs a stealth path; failing makes them angry and label you a terrorist. Middle-ringers are typically easier because the dogma is less pervasive. \[Z\] (G)
- A reaction depends on content (threat to doctrine) and delivery (respectful vs contemptuous). Respectful disagreement may produce a rebuttal or ending the interaction; contempt produces anger. Disgust is also possible, not only anger. \[Z\] (G) (Zach's example: a respectful atheist vs a mocking one talking to a devout Christian.)
- Claude proposals: goal provenance chains ("haul grain" serves "earn coin" serves "stop being hungry"); prediction error triggers reconsideration; rigidity of a belief derived from how many goals hang off it, not from ring; stealth persuasion targets dependent goals so error accumulates around the protected node; anger adds a neutralize goal and a threat label, disgust adds exclusion and isolation, both cascading through shared blackboards; a stance modifier on every act; commitment with trigger-based reconsideration. \[C\] (G)

### Confidence instead of a chooser

- All choices (reactions, persuasion, clarification) are GOAP actions with confidence-weighted costs. \[Z\] (G)
- Claude proposals: keep two numbers per belief, probability and precision (doctrine is high on both; hardening under attack is a precision increase); plan confidence as the product of step confidences; information-gathering actions are chosen when they raise downstream confidence enough; failed attempts lower confidence so stuck branches are abandoned; start with three coarse levels. \[C\] (G) The chat summary records probability and precision as settled, but Zach never explicitly confirmed it. \[C+\] (G)

### Communication as action

- The verbal text system is mostly a renderer for the expressive GOAP state. Background agents communicate without rendered text; text is rendered only for agents in range of the player. \[Z\] (G)
- Rendering is keyed to the player's vicinity, not only the conversation partner, because a TTS system will take a prosody signal from the agent's beliefs and parameters so the player can infer beliefs; any extra signal added for that must also be visible to non-text agents. \[Z\] (G)
- Talking is just an action with no separate conversation state. An agent goes up to another, sends a signal to get attention, and the other, being in range, independently perceives and responds. \[Z\] (G)
- Claude proposals: communication level of detail (near: full text; mid: acts without realizer; far: batched exchanges); rendering is a pure function and a seed-replay test checks rendering on and off give identical state; a small paralinguistic vector on every act (confidence, certainty, valence, arousal, stance, focus) computed for all agents; leakage of true state with masking as a costly action; noisy, range-limited perception; addressee inferred with a "was that for me" confidence; recent-dialogue context kept in each agent's own beliefs; turn-taking from action durations; guarding against courtesy loops. \[C\] (G)

### Recruitment and persuasion loop

- The player recruits by explaining a goal; the agent asks for clarification, justification or sources in a back-and-forth until convinced. \[Z\] (G)
- Patience is not a stored value. It derives from confidence, trust, alignment with beliefs and similar, so an elite becomes more patient when you weave their politics into the conversation. \[Z\] (G)
- Claude proposals: adoption confidence has components (understanding, feasibility, value, truth, trust) and each question type targets the weakest one, which also tells the player what is blocking; repetition has diminishing returns; an unanswerable source question becomes an emergent quest; patience as the computed value of continuing; flattery inferred as instrumental backfires. \[C\] (G)

### Identical agents and status

- Every agent is the same architecture; they differ only in skills, experience, status and so on. A general worldview-affirming goal applies to everyone. \[Z\] (G)
- Status derives from several sources: inherited position in the hierarchy (lineage), the beliefs and power of the agent's social circle, and recognition earned from respect-granting actions experienced by others. \[Z\] (G)
- Position, power and consensus are mostly what elites like to think about to consider themselves high status (snobbery). How an observer weighs another's status depends on their own stake in the doctrine and their place in the hierarchy: aspirants (for example outer-middle workers in the inner ring trying to get in) take position, power and consensus for granted; low-stake agents rely on more nuanced recognition. \[Z\] (G)
- Stake comes from the agent's own goals; an aspirant's goals align with entering the inner ring because they believe it improves their core survival goals. \[Z\] (G)
- Claude proposals: the "swap test" (exchange two agents' state and behavior should swap); persistence and openness derived, not dialed; generate populations from simulated histories; status as a per-observer readout of four sources; legitimacy as a protected doctrine node; decay on recognition to avoid rich-get-richer loops; level of detail for pairwise beliefs; exposure changes stake only through evidence; disillusioned aspirants as prime recruits; new insiders becoming most zealous. \[C\] (G)

### Beliefs and memory

- Everything an agent believes comes from real observation or a trusted source; that is how their "brain" works. \[Z\] (G)
- Memory is not an exact event log. It is sparse, storing what higher-order goal abstraction noticed (which goals were satisfied, what information toward goals was gained), so agents know notable things happened but not the detailed steps; gaps are filled by prediction and confabulation from priors. \[Z\] (G)
- Claude proposals: a belief record of content, probability, precision, source (observed, told by, inferred), timestamp and hop count; testimony degrades per hop; trust as a belief enabling retroactive discounting; episodes gated by prediction error or goal relevance; reconstruction as a planner query tagged inferred; retelling drift and storing each telling; source tags fading faster than content as a doctrine mechanism; consolidation of repeated episodes into general beliefs. \[C\] (G)

### Open

- Is the forward model the same store as consolidated memory, or separate? (last open thread) \[OPEN\] (G)
- Stage 2: per-agent beliefs from the start, or global truth until stage 4? Prices or quotas driving the supply chain? \[OPEN\] (G)
- Does rigidity harden when challenged? Is stance a free knob or derived from state? \[OPEN\] (G)
- Is masking in the first version, or is leakage involuntary at first? \[OPEN\] (G)
- Addressee as an explicit act slot, or inferred from gaze and position? \[OPEN\] (G)
- Retroactive overhearing of recent act logs, or forward-only rendering? \[OPEN\] (G)
- Recruits adopt the player's goal as their own, or as a "help the player" subgoal? \[OPEN\] (G)
- Can agents verify claims themselves (asynchronous persuasion)? \[OPEN\] (G)
- Does the lineage prior on status decay as recognition accumulates? \[OPEN\] (G)
- Do agents track the original source of testimony or only the immediate teller (echo chambers)? \[OPEN\] (G)

## Dialogue interpreter and realizer

The interpreter turns player text into GOAP-compatible speech acts and the realizer turns acts back into text; Zach's direction is tentative ("throwing shit at the wall") but leans toward symbolic speech acts with a subword token scheme and no LLM. \[Z?\] (F)

### Zach's stated direction

- Wondering whether players could convince people with real text input, via a manual text interpreter (worried it could be clunky or restrictive) or a neural interpreter that turns text into GOAP-compatible communication. \[Z\] (C)
- Likes speech acts as planning operators with structured state and an abstract syntax, plus ideas from Cicero. \[Z?\] (F)
- Wants an LLM-style subword token scheme so foreign or coined words fit as subtoken clusters, but no actual LLM. \[Z?\] (F)
- Interested in a hierarchical interpreter that goes from raw text to implicit meaning in a way one pass cannot. \[Z?\] (F)
- The game is English only; Giglian is never an NLP target. \[Z\] (F)
- Jev was once floated as the speech-act picker; the later decision to run choices on GOAP confidence values instead makes its role here doubtful. \[X\] (C, G)

### Claude's proposed design, unconfirmed

1. Define the act schema first: about 15 acts (inform, ask, request, promise, threaten, appeal, and similar) with typed slots (agent, belief, goal, item), restricted to in-scope entities. \[C\] (F)
2. Robust input: fastText-style character n-grams for typos and coined names, plus an entity linker matching spans against in-scope names and aliases. \[C\] (F)
3. Hierarchical layers: surface tokens and entities, then literal content (slot frame), then literal act, then intended act. The last step uses the NPC's plan recognition, the same module as threat labeling, which mirrors predictive coding (literal parses up, goal expectations down). Return ranked candidates; ask for clarification when confidence is low. \[C\] (F, G)
4. Test whether layers 1 to 3 in one classifier handle most input before building the top-down layer. \[C\] (F)
5. Realization from templates or a Grammatical Framework-style grammar so parse and generate share one abstract syntax; round-trip tests (realize, parse, compare). \[C\] (F)
6. The abstract syntax can be Giglian-native semantics, with English as one concrete syntax and other languages added later for localization; each doctrine camp's word for a split is a different linearization chosen by the speaker's beliefs. \[C\] (F)
7. A realizer request is (act, slots, paralinguistic vector); text hedges come from the same confidence value as TTS prosody so they never disagree. \[C\] (G)
8. From Talk of the Town's grammar: act metadata on grammar symbols, middle-out expansion from mid-level symbols, preconditions gated on speaker state, runtime variables that read beliefs, story sampling as the dev loop. Do not adopt its obligation-based dialogue manager. \[C\] (G)
9. The model, if any, translates and never decides; NPC paraphrase ("so you're promising me food?") lets players correct misparses. \[C\] (C)

### Open

- Shared grammar for parsing and generation, or templates out with a learned input? \[OPEN\] (F)
- How much indirect speech do players produce vs direct asks? \[OPEN\] (F)
- Exact act inventory. Stub. \[OPEN\]
- Is the high-end LLM realizer from chat C still on the table given the no-LLM interpreter preference? \[OPEN\] (C, F)

## Prior art and reading list

Boeda's GOAP cooperation paper is Zach's chosen starting point; everything else was surfaced by Claude as context and has not been evaluated by Zach unless noted.

### Agent AI and dialogue

| Work | What it is | Relevance | Status |
| --- | --- | --- | --- |
| [Boeda, "Multi-Agent Cooperation in Games with GOAP" (Square Enix, AIIDE 2021)](https://cdn.aaai.org/ojs/18909/18909-52-22675-1-2-20211004.pdf) | Per-agent backward GOAP; failed plans insert cooperation actions on any-agent conditions; RequestCooperation messaging | Basis for stage 3; its limits (blind discovery, refusal only by busyness or liking, bare goal requests) are what Zach's design extends | Chosen by Zach \[Z\] (G) |
| Talk of the Town / Bad News (Ryan, Mateas et al.) | Agents with imperfect memory and gossip; grammar-based dialogue realization | Zach read the realization paper and found it "pretty basic" \[Z\] (G) | Read |
| Ryan et al. 2015b, "Toward characters who observe, tell, misremember, and lie" | Belief and memory handling | Most relevant to source-tracked beliefs and gist memory; Claude offered to pull it next | To read \[OPEN\] (G) |
| Ryan et al. 2016b, "A lightweight videogame dialogue manager" | Dialogue management | Zach reportedly reading independently | Reading (G) |
| Orkin, F.E.A.R. squad AI | Shared blackboard GOAP squads | Classic GOAP coordination | Suggested \[C\] (G) |
| BDI agents | Belief-desire-intention architectures | Goal commitment | Suggested \[C\] (G) |
| Epistemic / theory-of-mind planning | Planning over others' beliefs | Stage 5 | Suggested \[C\] (G) |
| Comme il Faut / Prom Week, Versu | Social acts with preconditions; menu-based input | "Buttons first" baseline | Suggested \[C\] (F, G) |
| Facade | Free text mapped to discourse acts by rules | Misparse risks | Suggested \[C\] (C, F) |
| Generative Agents (Park et al.) | LLM agents with memory and reflection | Contrast case | Suggested \[C\] (G) |
| Cicero (Meta, Diplomacy) | Strategic planner plus language model realizer | Zach likes its ideas \[Z\] (F) | Noted |
| Rational Speech Act models | Pragmatic listeners | Intended-act inference | Suggested \[C\] (G) |
| Allen and Perrault; Cohen and Levesque | Speech acts as plan operators | Theory behind the act schema | Suggested \[C\] (F) |
| FIPA ACL; ISO 24617-2 | Agent message and dialogue act taxonomies | Ready-made act vocabularies | Suggested \[C\] (F) |
| TrindiKit, GoDiS | Information State Update dialogue managers | Structured dialogue state | Suggested \[C\] (F) |
| Inform 7 / TADS | Parser IF grounded in scope | Entities-in-scope parsing | Suggested \[C\] (F) |
| Grammatical Framework, OpenCCG, Prolog DCGs | Bidirectional grammars | Shared parse and generate | Suggested \[C\] (F) |
| Reiter and Dale; SimpleNLG | Classic NLG pipeline | Realizer | Suggested \[C\] (F) |
| SentencePiece, fastText | Subword tokenizers and n-gram embeddings | No-LLM token scheme | Suggested \[C\] (F) |

### Worldbuilding, biology, society

| Work or idea | Relevance | Status |
| --- | --- | --- |
| Michael Levin's bioelectricity research (planaria, Xenopus, eyes on tadpole tails) | Core inspiration for growth control | Zach's source \[Z\] (A) |
| Glaggleland meme | Visual inspiration | Zach's source \[Z\] (A) |
| Disco Elysium | Skills as voices, Thought Cabinet, dialogue lock-in | Zach playing as research \[Z\] (B) |
| Fallout: New Vegas | Multiple faction endgame routes | Zach's reference \[Z\] (C) |
| Adventure Time (Jake), Steven Universe (gem fusion), Rick and Morty (split episodes) | Growth look, fusion as marriage, personality splitting | Zach's references \[Z\] (A, C) |
| Ayn Rand ("who is John Galt?") | Middle-ring ideology | Zach's reference \[Z\] (C) |
| Tolkien's method | Conlang plus history plus narrative | Zach's model \[Z\] (F) |
| Spinoza, capabilities approach, privation theory | Joy ethics | Claude references \[C\] (D) |
| Parfit fission; U and non-U, Simmel, Bourdieu | Identity doctrines; prestige cycles | Claude references \[C\] (F) |
| von Thunen, Hamilton's rule, Anderson's imagined communities | City and cohesion | Claude references \[C\] (A) |
| Sharp, Chenoweth and Stephan, Granovetter, Snow and Benford, Tsebelis | Revolution, rhetoric, veto points | Claude references \[C\] (F) |
| Rosenfelder's Language Construction Kit; Peterson, The Art of Language Invention | Conlang craft | Claude references \[C\] (F) |

## Rejected or superseded ideas

These should appear in the wiki only as history or "not this" notes, so the agent never reintroduces them as canon.

| Rejected or superseded | Replaced by | Source |
| --- | --- | --- |
| Whole body made of mycelium-like webbing | Smooth, Jake-like bulk-flow growth; webbing only for wound healing | (C) |
| Both mitosis halves get identical memories | Uneven psyche split; about half the memories and half the learned skill | (A, C) |
| Fungal "beds" | "Farmland" | (C) |
| A rhetorical "Who is the Founder?" shrug | A mythological Founder spoken of as still in power | (C) |
| Flat farming boycott | Convince the middle rings, then commandeer shipments together | (C) |
| Outskirts skill donors (or engineered consent) | Donors only from ideologically entrenched center residents | (C) |
| Three routes (recruit, self-mitose, neutral) | Four paths (solo recruitment, mitosis plus recruitment, balanced mitosis, unbalanced mitosis) | (B, C, E) |
| Swapping control between mitosed halves, RTS-style, with a 2 to the n control budget | Choose one half to continue as; the other becomes an ordinary NPC | (E) |
| Skills drive speech checks | Memory gates dialogue; skills govern growth and movement | (C) |
| A suppressed or negative-valence giggle as a distress signal | No negative giggle exists | (D) |
| Decay as the default state | A held, slightly positive homeostatic baseline | (D) |
| Giggling as a shared pressure reservoir that cheers others up | Pressure is a metaphor; real causes need treatment | (D) |
| Forced and chronic collapse leaving different kinds of remains | Dissolution is always uncontrolled mitosis; goop homogeneity differs | (D) |
| Starving cells shrivel (or simply burst like animal cells) | Wall-less cells in a frame-and-foam hybrid; husks burst under their own weight, then dry to chunky powder | (D) |
| Deliberate self-relaxation as a distinct death type | That is just ordinary mitosis; suicide is a separate self-inflicted class | (D, F) |
| Default bilateral split plane | Splits in any direction via relaxing pressure | (D) |
| Giggle intensity as the game's native NLP output | The game is English; Giglian is worldbuilding only | (F) |
| "Birth" as the neutral term for a split | "Split" or "mitosis"; birth is doctrinal | (F) |
| No private thoughts in Giglian culture | Private experience exists, held like a license until the split | (F) |
| Simulating doctrine fashion drift in game | Lore only; only rhetoric spread is simulated | (F) |
| A democratic election as the peaceful target | A council vote; veto or impeachment by replacing office-holders | (F) |
| Jev as GOAP precondition chooser or reaction chooser | Confidence-weighted GOAP action costs | (G, M2) |
| Anger as the single failure reaction | Content threat plus delivery stance; disgust possible | (G) |
| "Middle ring is easier to convince" as one rule | Weighting depends on each agent's stake; aspirants vs low-stake | (G) |
| Patience as a stored trait | Derived from confidence, trust and belief alignment | (G) |
| Exact event logs as memory | Sparse, goal-abstracted gist memory with confabulated gaps | (G) |
| Talk of the Town realization paper as the key reference | Zach found it basic; belief and memory papers suggested instead | (G) |

## Open questions and page stubs

Per-topic open questions are listed at the end of each section above; this section collects areas Zach has barely touched, which should become stub pages, and tensions the wiki must flag rather than resolve.

### Stub pages (little or no material yet)

| Topic | What exists | What is missing |
| --- | --- | --- |
| Giglos as a world | "Third moon of Giglos", very humid, open desert at the city edge | Planet vs moon vs city naming, astronomy, geography, climate, water cycle |
| Other species and flora | Mushrooms dominant; a bird-like analog with genome-bounded growth | Any concrete species, food web, wild fauna |
| Giglian organs | Zach's required list; mouth anatomy from phonology | Decisions on eyes, hearing, digestion, respiration, filtering, waste |
| Conlang | Method and physiology | Phonemes, grammar, lexicon, writing system, romanization |
| Species endonym and place names | Placeholder only | Everything |
| History and timeline | Settling party betrayal (not final), corrupt-court era, rise and fall of nations | Dated events, eras, founding details |
| Other cities and unincorporated lands | Exist beyond the outskirts; seeded by other founders | Any specific city or region |
| Doctrine camps | Continuity vs death-and-birth views | Names, institutions, rites |
| Monastic order and recordkeepers | Roles and lifestyle | Named orders, locations, the game's monk character |
| Public works and entertainment | Overcomplicated projects, death-spiral rollercoasters | Specific works, spectacle culture |
| Center entrance evaluation | Trust ladder via business travel | What it tests, tiers |
| Characters | Protagonist, ruler, monk, council members as roles | Names, personalities, arcs |
| Endings | Revolution and peaceful council routes; four paths | Ending list and conditions |
| Combat | "Offensive skills" on solo and recruitment builds; fighting as an option | Any combat design |
| Skill tree | Growth and movement skills; split-specific skills on the mitosis path | Actual skills |
| Speech-act schema | About 15 acts proposed by Claude | Final act inventory and slots |
| Codex and artbook | A stated goal | Visual style guide, cross-section drawings |
| Technology level | Skyscrapers, maglev, factories, drilling | Power sources, materials, how records are kept in humid air |
| Jev | Decision model over up to 255 labeled options, documented elsewhere | Its current input format (asked, unanswered in chat C) |

### Tensions to flag, not resolve

1. **Premise vs later Founder lore:** the original plot has the closest-to-first-split founder splitting into fascist and weak halves; later lore says the original no longer exists and the Founder is a diluted tip. (B vs C)
2. **Circulation:** "no veins or bloodflow" vs some nutrient and oxidizer carrier moving along grown channels. (A)
3. **Memory at a split:** "same memories" in the first notes vs "half the memories" later. (A vs C)
4. **NPC access to the player:** NPCs "can see" the player's blackboard vs NPCs building a model of you from observation; Claude argued for scoped access to avoid omniscience. (C)
5. **LLMs:** a high-end LLM dialogue tier in chat C vs "I don't want to use an LLM" for the interpreter in chat F. (C vs F)
6. **Humid world vs open desert** at the city's outer edge. (C vs E)
7. **Base form:** the glaggle ball (no arms) vs a somewhat humanoid base; Zach treats the ball as the fully relaxed or collapsed state and the glaggle face as the head. (A, D)
8. **Dialogue lock-in:** Disco Elysium-style trait lock-in and the mitosis skill-point economy (B) vs memory-gated dialogue with skills for growth only (C).

## Glossary

Quick definitions for entity linking; the tag shows whether the term is Zach's or Claude's.

| Term | Definition | Origin |
| --- | --- | --- |
| Aeration | Whipping cytoplasm into foam to gain volume at constant mass | \[Z\] |
| Aspirant | Middle-ring agent whose goals route through entering the inner ring | \[Z\] concept, \[C\] label |
| Blackboard | Per-agent and shared GOAP state; mirrors lineage memory sharing | \[Z\] |
| Boeda paper | Multi-Agent Cooperation in Games with GOAP, AIIDE 2021 | \[Z\] |
| Clean split | Controlled mitosis choosing what each half keeps; elite-trained | \[Z\] |
| Degenerate mitosis | Involuntary split from chronic deflation | \[Z\] |
| Dissolution / collapse | Uncontrolled cascading mitosis ending in goop and powder | \[Z\] |
| Doctrine | Beliefs about what splitting means; also what agents will not question | \[Z\] |
| Founding-plot split | The founding-plot split into a perfect fascist leader and a "weak" protagonist half | \[Z\] concept, \[C\] label |
| Forced splitting | Torture-induced splitting to extract confessions or purge dissent | \[Z\] |
| Frame and foam | Cartilaginous structural tissue and foamy muscle-like tissue | \[Z\] |
| Fusion | Merging two compatible Giglians; gene mixing, marriage analog | \[Z\] |
| Giggle | English label for the Giglian vocalization; speech is controlled giggling | \[Z\] |
| Glaggle | Meme smiley that inspired the Giglian head and base form | \[Z\] |
| GOAP / LGOAP | Goal-oriented action planning; LGOAP adds long-horizon plan influence | \[Z\] |
| Greedy mitosis | Deliberately unequal split; presumed intentional in law | \[Z\] |
| Holding pressure | Maintained healthy baseline; cultural metaphor | \[Z\] |
| Jev | Zach's separate decision model over up to 255 labeled options | \[Z\] |
| Joy | Core moral tenet; outward-growing healthy baseline | \[Z\] |
| Leaky | Folk description of depression | \[Z\] |
| Middle ring | Managers of logistics; manage but do not own | \[Z\] |
| Paralinguistic vector | Per-act confidence, valence, stance, focus feeding TTS and listeners | \[C\] |
| Purge by mitose | State extraction of dissent into a disposable half | \[C+\] |
| Shadow agent | The player's GOAP agent that never acts, scored against the human | \[Z\] concept, \[C\] label |
| Skill transplant / harvest | Ruler fuses with a skilled donor then splits off the waste half | \[Z\] |
| Split registry | Proposed record of every mitosis | \[C\] |
| Stealth path | Persuading the inner ring without triggering threat labels | \[Z\] |
| Swap test | Exchange two agents' state and check behavior swaps | \[C\] |
| The Founder | Living descendant fewest splits from the original founder | \[Z\] |
| Waste half | Cast-off remainder of a skill harvest | \[Z\] |
