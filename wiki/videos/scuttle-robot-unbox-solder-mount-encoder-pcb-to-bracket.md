---
type: video
title: "SCUTTLE Robot - Unbox, solder, mount encoder pcb to bracket"
video_id: "EmvBnSHmWR0"
url: "https://www.youtube.com/watch?v=EmvBnSHmWR0"
published: 2020-09-01
duration: "5:30"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, encoder, soldering, pcb, magnetic-sensor, version-marking]
ingested: 2026-05-02
---

## Overview

Full encoder-PCB workflow for a [[entities/projects/scuttle-robot|SCUTTLE]] wheel: unbox a brand-new magnetic encoder board, solder eight gold-plated male header pins, bridge the two extra pins required only on the left-hand encoder, then fasten the board to the printed encoder bracket with M2 plastite screws. David also explains how the diametric magnet is sensed and the sub-millimeter air gap required for proper readings, and reminds viewers to check their bracket version number before following older instructions.

## Key takeaways

- Set the iron to 360 C and use solder paste — gold-plated header pins are preferred.
- The left-hand encoder needs an extra solder bridge between two specific pins.
- Mount the PCB with M2 x 6 mm course-thread screws designed for plastic; tighten by feel, not by power driver — the screws can snap and the printed holes can be imperfect.
- The encoder reads a diametric magnet (north/south poles across the diameter of the disc) glued to the wheel shaft.
- Magnet-to-sensor air gap is sub-1 mm; check the datasheet.
- Document and check the part [[concepts/version-marking|version number]] (this bracket is v2.4) — older videos show separate left/right brackets that have since been consolidated into one design.

## Techniques demonstrated

- [[concepts/soldering-header-pins|Soldering header pins]] with paste and an iron
- [[concepts/solder-bridging|Solder bridging]] for left-hand encoder configuration
- [[concepts/heat-set-insert-installation|Driving plastite screws into 3D-printed holes]] without stripping
- [[concepts/version-marking|Version marking]] of mechanical parts
- [[concepts/symmetric-not-identical|Symmetric not identical]] — single bracket design serving both sides via mirrored mounting
- [[concepts/datasheet-vs-real-world-fit|Datasheet vs. real-world fit]] for magnet gap

## Tools used

- [[entities/tools/soldering-iron|Soldering iron]] (set to 360 C)
- Solder paste, solder
- Male header pins (gold-plated)
- M2 x 6 mm plastite screws
- Rubber soldering mat

## Materials used

- [[entities/materials/pla|PLA]] / 3D-printed encoder bracket
- Diametric magnet
- Encoder PCB

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]] — encoder bracket v2.4

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:38 "Iron temperature 360."
- 1:56 "One extra step for the left-hand encoder — we need to bridge these two pins."
- 4:27 "This is the diametric magnet — that means according to the diameter you get the north and south poles."
- 5:11 "It's important to note this is version 2.4."

## Related videos

- [[videos/scuttle-robot-press-in-wheel-bearings-and-glue-pulleys]]
- [[videos/scuttle-robot-insert-the-bearings-in-new-wheels]]
- [[videos/scuttle-robot-soldering-breadboards-for-i2c-bus]]
- [[videos/build-a-payload-robot-start-to-finish-scuttle-v2-4]]
