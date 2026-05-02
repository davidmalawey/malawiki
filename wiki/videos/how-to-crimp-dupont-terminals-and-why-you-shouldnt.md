---
type: video
title: "How to crimp Dupont Terminals, and why you SHOULDNT"
video_id: "mdD9NaCWuJ8"
url: "https://youtu.be/mdD9NaCWuJ8"
published: 2023-01-11
duration: "5:09"
series: "[[series/crimping-tutorials]]"
tags: [crimping, dupont, tutorial, connectors, mxet, anti-pattern]
ingested: 2026-05-02
---

## Overview

The companion crimp tutorial — and a sustained argument against actually doing it. David walks through the mechanics of crimping a 28 AWG ribbon wire onto a 2.54 mm Dupont female terminal, but the entire framing is "for the love of God, do you really need this?" Off-the-shelf jumper extensions, Futaba-style servo leads, and 22 AWG single-cord wire all give you the same connection without the crimp step. When you must crimp, the female terminal goes on the wire, never the male — wires sling around and male pins waiting to short out are a bench fire waiting to happen.

## Key takeaways

- 2.54 mm pitch, 28 AWG ribbon is the canonical Dupont scenario. Looks intimidating, isn't.
- **First question: do you actually need to crimp?** Pre-crimped jumper extensions and Futaba-style servo leads use the *same* crimp and ship in many lengths.
- For breadboard/quick-and-dirty work, 22 AWG single-cord wire plugs straight into Dupont sockets and gives the same contact.
- **Female on the wire, male on the board** — always. The board can be fastened down; the wires sling around. A male pin on a flapping wire is a short waiting to happen and will fry components.
- Crimp mechanics: 3-4 mm strip, hang the wings on the front shelf of the crimper, pull toward you until it hangs up, click-click. Long wings bite the insulation, short wings bite the copper.
- **Never** put a single contact in an individual housing — there's no mechanical integrity. Always use a multi-contact housing matched to the contact count you need.
- Common failure: wings get hung up on the back of the housing during insertion. Fix: pointy object lifts the housing tab so the wings can pass.
- Cheap "28 AWG" wire is often closer to 30 AWG. If the crimp won't grip, squeeze the wings tighter top-to-bottom *before* re-inserting.
- Housing arrow indicates ground side. Two clicks on insertion = full seat. Tug test.
- Use the front-most die on the crimper; the others are for different crimps.

## Techniques demonstrated

- Female-on-wire / male-on-board safety convention
- Wing-on-shelf crimp orientation
- Two-stage crimp ("click click")
- Housing extraction with a pointy lift tool
- Wing pre-squeeze for under-spec wire
- Multi-contact housing rule (never single)

## Tools used

- Dupont crimper (front-most die)
- Wire stripper (28 AWG and 22 AWG positions)
- Pointy object / awl (for housing extraction)
- [[entities/tools/dupont-connector|Dupont terminals]] (female crimp, male board pins)
- Futaba-style servo extension leads (the off-the-shelf alternative)
- Pre-crimped jumper kits

## Materials used

- 28 AWG ribbon wire
- 22 AWG single-cord hookup wire (recommended substitute)
- [[entities/materials/copper|Copper]]

## Projects

(none — tool tutorial)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:53] "Before you use this tool you should be asking yourself, for the love of God, do I really need this?"
- [1:53] "Your board is the element that you have control of. The wires are the part that sling around. If you have male ends on your wires, you are just waiting for an opportunity to accidentally fry your components."
- [3:04] "What — no, never do that. Grab a housing with the number of contacts that you need, not individual housings."

## Related videos

- [[videos/how-to-crimp-anderson-connectors]] — the previous, less skeptical entry in the crimping series
- [[videos/3-ways-to-test-power-draw-for-mechatronics-designs]]
- [[videos/clean-up-cords-wires-in-projects]]
