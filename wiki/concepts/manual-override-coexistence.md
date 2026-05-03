---
type: concept
aliases: ["series-relay override"]
tags: [plc, safety, control]
source_count: 3
---

# Manual override coexistence

## Definition

Design pattern: keep an existing manual switch in place, but wire a relay in series with it. The system runs only when both are closed, so the PLC gains override authority without removing manual control.

## Appears in

- [[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot-part-2]]
- [[videos/scuttle-robot-nextec-team-tests-computer-vision-docking]]
- [[videos/scuttle-robot-using-matlab-gui-v1-1]]

## Related

- [[concepts/plc-relay-control]]
- [[entities/tools/relay-module]]
