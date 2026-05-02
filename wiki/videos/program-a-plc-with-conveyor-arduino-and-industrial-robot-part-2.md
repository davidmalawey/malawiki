---
type: video
title: "Program a PLC with Conveyor, Arduino and Industrial Robot (PART 2)"
video_id: "dOceaFaPiSM"
url: "https://www.youtube.com/watch?v=dOceaFaPiSM"
published: 2021-10-21
duration: "3:09"
series: "[[series/mxet-conveyor-demo]]"
tags: [plc, conveyor, relay, mxet, mechatronics]
ingested: 2026-05-02
---

## Overview

Short follow-up to Part 1 focused on how the PLC actually drives the conveyor: the P1AM 24 V digital output module energizes two relays in a 4-relay bracket, whose contacts are wired *in series* with the existing on/off and forward/reverse switches inside a modified Dorner conveyor controller. To run the demo, the manual switches stay closed; the PLC takes over by opening or closing the series-connected relay contacts.

## Key takeaways

- The Dorner conveyor controller's existing manual switches (on/off and direction) were left in place; the modification adds external relays in series so PLC control coexists with manual override.
- Relay 0 (black/white wires) and relay 1 (red/green wires) each control one of the two conveyor switches.
- "Forward" direction has to be discovered empirically — the controller doesn't label which direction the switch position corresponds to.
- A 24 V output from the PLC closes a normally-open relay; the relay's NO/NC pair handles the actual conveyor control circuit.

## Techniques demonstrated

- [[concepts/plc-relay-control|PLC relay control]] (in-series with existing manual switches)
- [[concepts/manual-override-coexistence|Manual override coexistence]]

## Tools used

- [[entities/tools/p1am-100|P1AM-100 PLC]]
- [[entities/tools/relay-module|4-relay module]]
- [[entities/tools/dorner-conveyor|Dorner conveyor]]

## Projects

- [[entities/projects/mxet-conveyor-demo|MXET Conveyor Demo]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot]] (Part 1)
