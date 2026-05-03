---
type: concept
aliases: ["text-file telemetry"]
tags: []
source_count: 4
---

# Telemetry via flat files

## Definition

A Python program writes named `.txt`/`.csv` files at sample rate; [[entities/tools/node-red|Node-RED]] tails those files to drive a live dashboard. Decouples the runtime program from the UI without IPC plumbing — also enables the [[concepts/runtime-tunable-parameters|runtime-tunable-parameters]] pattern in reverse.

## Appears in

- [[videos/scuttle-robot-export-nodered-flow]]
- [[videos/scuttle-robot-plot-gamepad-values-in-nodered-via-txt-file]]
- [[videos/scuttle-robot-nodered-read-csv-to-send-mqtt]]
- [[videos/scuttle-robot-send-receive-mqtt-messages-display-with-nodered-on-beaglebone-blue]]

## Related

- [[concepts/file-as-ipc]]
- [[concepts/iot-data-flow]]
