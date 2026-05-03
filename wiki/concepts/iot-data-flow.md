---
type: concept
aliases: ["pub-sub data pipeline"]
tags: []
source_count: 5
---

# IoT data flow

## Definition

The pub/sub data pipeline pattern SCUTTLE uses for telemetry: producer writes to a flat file → [[entities/tools/node-red|Node-RED]] reads → [[concepts/mqtt|MQTT]] publish → broker → MQTT subscribe → Node-RED writes flat file → consumer reads. Decoupled, polyglot, debuggable at any seam.

## Appears in

- [[videos/scuttle-robot-nodered-read-csv-to-send-mqtt]]
- [[videos/scuttle-robot-nodered-receive-mqtt-message-save-to-csv]]
- [[videos/scuttle-robot-plot-gamepad-values-in-nodered-via-txt-file]]
- [[videos/scuttle-robot-iot-in-all-forms-esp-pc-mobile-phone-raspi-demo-with-buzzer]]
- [[videos/scuttle-robot-send-receive-mqtt-messages-display-with-nodered-on-beaglebone-blue]]

## Related

- [[concepts/mqtt]]
- [[concepts/file-as-ipc]]
- [[concepts/telemetry-via-flat-files]]
- [[concepts/m2m-iot-communication]]
