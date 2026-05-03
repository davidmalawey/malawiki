---
type: video
title: "Disassemble Molex KK (close-up) Connector"
video_id: "-WWxuLCnSlM"
url: "https://www.youtube.com/watch?v=-WWxuLCnSlM"
published: 2024-02-24
duration: "5:13"
tags: [connectors, molex, dupont, soldering, mechatronics, hardware]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] films a close-up tutorial showing how to remove and reinstall the terminals of a [[entities/brands/molex|Molex]] KK connector — the small connector typically used for PC fans. He compares the KK terminal to the more ubiquitous [[entities/tools/dupont-connector|DuPont]] terminal, explains why they intermate, and notes the trade-offs between the two for current-carrying versus signal applications.

## Key takeaways

- Molex KK terminals are retained in the housing by a single small tab (almost a burr) that catches against the plastic; depressing it with a blade releases the terminal.
- Orientation is critical on reinsertion — the tab must face the correct way or the terminal will not be retained.
- Molex KK pins and DuPont 2.54 mm pins share enough pitch and gauge to mechanically intermate, but DuPont has less contact area.
- For full-current applications (e.g. fans drawing ~1 A) use the proper Molex KK; for signals or a single fan, DuPont substitution is fine.
- DuPont is worth knowing because millions of Arduino, Raspberry Pi, and PCB sensors use the 2.54 mm standard.

## Techniques demonstrated

- Terminal extraction from a polarized housing using a clamp and a fine blade.
- Re-tensioning a crushed retention tab so the terminal still locks after reinsertion.

## Tools used

- [[entities/tools/dupont-connector|DuPont connector]] (2.54 mm pitch)
- Helping-hands clamp
- [[entities/tools/utility-knife|Utility knife]] / fine blade

## Materials used

- 28 AWG stranded wire (typical fan-cable gauge)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:46] "I believe this is a Molex type KK and I can confirm the pitch and the size."
- [4:37] "The reason DuPont is even discussed in this video is millions, millions of these PCBs and Arduino devices and sensors that are off the shelf are using that standard."

## Related videos

- [[videos/clean-up-cords-wires-in-projects]]
- [[videos/more-about-usb-than-you-ever-wanted-to-know]]
