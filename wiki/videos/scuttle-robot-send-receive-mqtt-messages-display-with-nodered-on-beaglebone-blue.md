---
type: video
title: "SCUTTLE Robot - Send & Receive MQTT messages, display with NodeRed, on Beaglebone Blue"
video_id: "qmSQHYQaYrs"
url: "https://www.youtube.com/watch?v=qmSQHYQaYrs"
published: 2019-07-24
duration: "6:34"
tags: [scuttle, mqtt, node-red, beaglebone-blue, hivemq, iot]
ingested: 2026-05-02
---

## Overview

David walks through bidirectional MQTT messaging between the SCUTTLE robot's [[entities/tools/beaglebone-blue|BeagleBone Blue]] and a remote Node-RED dashboard via the public HiveMQ broker. Wheel speeds (driven by the gamepad) are read every ~0.2s from a flat file and pushed out as MQTT publishes; commands sent back from a WebSocket client land in another flat file the robot can poll. The video demonstrates topic hierarchies, the `#` wildcard subscribe, and using `cat mqtt_data.txt` to verify reception.

## Key takeaways

- Free public brokers like HiveMQ (`broker.hivemq.com:1883` for MQTT, `:8000` for WebSockets) are good enough for early IoT prototyping.
- Topic hierarchies (`testtopic/dm/2`) plus the `#` wildcard let one subscriber catch everything under a parent topic.
- Telemetry and commands can be exchanged by reading and writing flat text files — Node-RED reads files at a 0.2s cadence to update gauges, and the robot's main loop reads incoming command files.
- Quality of service level matters and is set per published item (David uses QoS 2 here).

## Techniques demonstrated

- [[concepts/mqtt|MQTT]]
- [[concepts/m2m-iot-communication|M2M IoT communication]]
- [[concepts/iot-data-flow|IoT data flow]]
- [[concepts/mqtt-topic-wildcards|MQTT topic wildcards]]
- [[concepts/mqtt-quality-of-service|MQTT quality of service]]
- [[concepts/telemetry-via-flat-files|telemetry via flat files]]
- [[concepts/file-as-ipc|file as IPC]]
- [[concepts/node-red-dashboard|Node-RED dashboard]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/node-red|Node-RED]]
- [[entities/tools/hivemq|HiveMQ]]
- [[entities/tools/gamepad|gamepad]]
- [[entities/tools/mqtt-websocket-client|MQTT WebSocket client]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- [[entities/projects/scuttle-iot-ecosystem|SCUTTLE IoT ecosystem]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-choosing-mqtt-topics-for-mobile-robot-iot-guide-preliminary]]
- [[videos/scuttle-robot-export-flow-from-node-red-import]]
- [[videos/scuttle-robot-export-nodered-flow]]
- [[videos/scuttle-robot-iot-in-all-forms-esp-pc-mobile-phone-raspi-demo-with-buzzer]]
- [[videos/iot-using-mqtt-on-esp8266-set-your-client-id-or-autogenerate-credentials]]
- [[videos/scuttle-robot-nodered-read-csv-to-send-mqtt]]
- [[videos/scuttle-robot-nodered-receive-mqtt-message-save-to-csv]]
