---
type: video
title: "Scuttle Battery Pack - assembly & wire lengths"
video_id: "JS_9AhtAyLg"
url: "https://www.youtube.com/watch?v=JS_9AhtAyLg"
published: 2019-01-29
duration: "3:43"
series: "[[scuttle-bench-build-kickoff]]"
tags: [scuttle, battery-pack, 18awg, 18650, wire-routing, build]
ingested: 2026-05-02
---

## Overview

Specifies wire lengths and routing for the SCUTTLE v1.0 [[entities/tools/18650-cell|3-cell 18650]] battery pack. Each conductor is 18 AWG (0.75 mm^2). David also explains the clearance constraints: solder bumps must sit at the lowest point in the case so wires don't lift the assembly out of the lid plane.

## Key takeaways

- **Series-link wires** between cells: 85 mm each (includes strip length).
- **Positive battery lead to switch:** 145 mm (includes strip + crimp allowance).
- **Red lead from switch:** 70 mm.
- **Negative/ground lead:** 80 mm.
- **Crimp jumpers** between terminals: 50 mm before stripping.
- The lowest point of any solder joint must be the bottom of the soldered area - **don't cross wires under the cells** or the pack rises above the case lid plane.
- The case dovetail features slide into grooves; assemble with one corner hooked first, then slide the dovetail in, then close the lid against the brass [[entities/tools/threaded-insert|threaded inserts]].

## Techniques demonstrated

- [[concepts/wire-length-specification|Wire length specification]]
- [[concepts/cable-management|Cable management]]
- [[concepts/strain-relief|Strain relief]]
- [[concepts/wire-gauge-selection|Wire gauge selection]]

## Tools used

- [[entities/tools/wire-cutters|Wire cutters]]
- [[entities/tools/wire-strippers|Wire strippers]]
- [[entities/tools/soldering-iron|Soldering iron]]
- [[entities/tools/threaded-insert|Threaded insert]]
- [[entities/tools/18650-cell|18650 cell]]

## Materials used

- [[entities/materials/18awg-wire|18 AWG wire (0.75 mm^2)]]
- [[entities/materials/abs|ABS]] (battery case)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (battery pack v1.0)

## Related videos

- [[scuttle-robot-battery-pack-soldering-the-bottom-side]]
- [[scuttle-battery-pack-crimping-insulated-terminals]]
- [[scuttle-battery-pack-heat-set-inserts]]
