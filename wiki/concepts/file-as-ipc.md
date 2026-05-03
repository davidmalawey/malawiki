---
type: concept
aliases: []
tags: []
source_count: 2
---

# File as IPC

## Definition

Using a flat file (e.g. `/tmp/ufile.txt`) as the inter-process communication channel between a Python loop and [[entities/tools/node-red|Node-RED]]. Avoids socket / message-bus plumbing — the OS already serializes writes for you. Works because both sides are slow relative to file I/O.

## Appears in

- [[videos/scuttle-robot-plot-gamepad-values-in-nodered-via-txt-file]]
- [[videos/scuttle-robot-send-receive-mqtt-messages-display-with-nodered-on-beaglebone-blue]]

## Related

- [[concepts/telemetry-via-flat-files]]
- [[concepts/runtime-tunable-parameters]]
- [[concepts/iot-data-flow]]
