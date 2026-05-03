---
type: video
title: "Scuttle Robot - Soldering Breadboards For I2C Bus"
video_id: "zGzvy32n1eo"
url: "https://www.youtube.com/watch?v=zGzvy32n1eo"
published: 2021-02-20
duration: "3:19"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, soldering, i2c, breadboard, technique]
ingested: 2026-05-02
---

## Overview

Short close-up tutorial on soldering header pins onto a small custom breadboard / PCB used as an I2C bus distribution board for SCUTTLE. David shares a "no helping hands" trick for tacking plastic header bodies, then walks through bridging power/ground rows to give every device a common power-ground-clock-signal interface.

## Key takeaways

- If you don't have helping hands, tack the plastic of a header in place first, wait ~10 s for it to grip the PCB, then solder.
- Approach the joint from the side away from already-soldered pins so the iron's heat doesn't reflow neighbors.
- Liquid that looks like a short between pins is usually just flux; verify with a continuity check after the fact.
- Bridging adjacent solder pads is easier when the pads are slightly cooler — too hot and the solder is too fluid to span the gap.

## Techniques demonstrated

- [[concepts/soldering-header-pins|Soldering header pins]]
- [[concepts/solder-bridging|Solder bridging]] (intentional, for power/ground rails)
- Continuity check for short-detection

## Tools used

- [[entities/tools/soldering-iron|Soldering iron]]
- [[entities/tools/multimeter|Multimeter]] (for continuity)
- [[entities/tools/breadboard-pcb|Breadboard / perfboard PCB]]
- [[entities/tools/header-pins|Header pins]]

## Materials used

- Solder (with flux core)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## Related videos

- [[videos/hack-a-soldering-iron-with-a-mechanical-engineer]]
- [[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot]]
