---
type: video
title: "How to Crimp Ferrules (and what goes wrong)"
video_id: "LtvPOjP6O40"
url: "https://www.youtube.com/watch?v=LtvPOjP6O40"
published: 2023-01-13
duration: "3:28"
tags: [ferrules, crimping-series, mechatronics, screw-terminals, wire-prep, aggie-engineering]
ingested: 2026-05-02
---

## Overview

A practical tutorial on using a self-adjusting hex/square ferrule crimper (Iwiss / "perceiva" HSC 86-6A, the "iron sphincter") to prepare stranded wire for [[entities/tools/din-rail|DIN rail]] and screw terminals. David walks through wire-gauge selection (18 AWG as the workhorse), strip length, crimp action, the tug test, and trimming ferrules that are too long.

## Key takeaways

- Ferrules beat tinning: more repeatable, more secure in screw terminals, and they avoid solder creep that can fatigue under vibration.
- Wire gauge matters — 18 AWG (red ferrule) is the sweet spot for most mechatronics power delivery; 16 AWG is often too fat for off-the-shelf screw terminals; 22 AWG is signal-territory only.
- Strip ~10 mm, slightly more than the exposed metal length of the terminal, twist the strands, feed the ferrule vertically, then crimp. Double-crimp to compress missed regions.
- Always do a tug test — both after the crimp and after tightening the screw terminal.
- If the ferrule sticks out of the terminal, trim one notch off with [[entities/tools/flush-cutters|flush cutters]] (or a rounder cutter to keep the ferrule shape).
- Sizing trick when you don't know the gauge: find the ferrule that fits, then step down one size at a time until the conductor no longer fits — that's your size.
- Use the right screwdriver (P0 or P1 Phillips for typical screw terminals) so you don't strip the head.

## Techniques demonstrated

- Ferrule crimping with a self-adjusting hex crimper.
- Tug test as a [[concepts/torque-evaluation-on-assembled-fastener|simple in-situ verification]].
- Step-down sizing method to identify the correct ferrule for an unknown gauge.
- Trimming over-long ferrules to leave no exposed conductor in screw terminals (safety practice).
- [[concepts/strain-relief|Strain relief]] via proper crimp + screw clamp.

## Tools used

- Iwiss / "perceiva" HSC 86-6A self-adjusting ferrule crimper ("iron sphincter")
- [[entities/tools/flush-cutters|Flush cutters]] (for trimming)
- P0 / P1 Phillips screwdriver
- Wire strippers
- Screw terminal blocks, [[entities/tools/din-rail|DIN rail terminals]]

## Materials used

- 18 AWG, 16 AWG, 22 AWG stranded [[entities/materials/copper|copper]] wire
- Color-coded ferrules (red 18 AWG, etc.)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:26] "this crimper has a fascinating closing action"
- [3:17] "once you've mastered using the iron sphincter you can get away with a whole lot less soldering"

## Related videos

- [[videos/how-not-to-use-flush-cutters|How NOT to use Flush Cutters]] — direct prerequisite from the day before; flush cutters return here as the trim tool.
- [[videos/strip-round-cables-without-damaging-insulation|Strip round cables without damaging insulation]] — earlier step in the wire-prep workflow.
- [[videos/clean-up-cords-wires-in-projects|Clean up cords and wires in projects]]
- [[videos/build-a-diy-power-supply-a-tutorial-using-openbox|Build a DIY power supply using OpenBox]] — heavy use of screw terminals.
