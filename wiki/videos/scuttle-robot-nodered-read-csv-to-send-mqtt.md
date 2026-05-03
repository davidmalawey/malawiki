---
type: video
title: "SCUTTLE Robot - nodered read csv to send mqtt"
video_id: "6eDT6jU8MtU"
url: "https://www.youtube.com/watch?v=6eDT6jU8MtU"
published: 2020-09-03
duration: "5:57"
tags: [scuttle, nodered, mqtt, csv, iot, raspberry-pi]
ingested: 2026-05-02
---

## Overview

Tutorial on building a [[entities/tools/nodered|Node-RED]] flow that reads a tab-separated CSV file from disk and publishes its contents as an [[concepts/mqtt-pub-sub|MQTT]] message to the public HiveMQ broker, then verifies the message arrives on a phone via the MQTTool app. David creates the source file on a [[entities/tools/raspberry-pi|Raspberry Pi]] with `touch` and `nano`, configures the Node-RED `file in` and `csv` nodes (separator = tab, header row contains column names, one message per row), and exports the finished flow to a public gist.

## Key takeaways

- Create the data file at `/home/pi/scuttle/data2.csv` with two columns and tab-separated values.
- Node-RED flow: timestamp inject -> file in -> csv parser -> mqtt out + debug.
- In the csv node, set separator to tab, "skip 0 lines", "first row contains column names", "one message per row".
- MQTT topic: `scuttle/pi/gp` (gp = gamepad) on the public HiveMQ broker.
- On the phone, the MQTTool app subscribes to the topic and confirms the published payload.
- Export the flow with "Export -> Current flow -> Copy to clipboard" and store it in a public gist for sharing.

## Techniques demonstrated

- Node-RED flow design (file in -> csv -> mqtt out)
- [[concepts/mqtt-pub-sub|MQTT publish/subscribe]] over a public broker (HiveMQ)
- CSV parsing with column-name headers and tab separators
- [[concepts/open-source-knowledge|Open-source knowledge]] — sharing flows as public gists
- [[concepts/iot-data-flow|IoT data flow]] — telemetry from a Linux SBC to a phone

## Tools used

- [[entities/tools/nodered|Node-RED]]
- [[entities/tools/raspberry-pi|Raspberry Pi]] (Linux shell, nano)
- MQTTool (iOS/Android MQTT client app)
- HiveMQ public broker
- GitHub Gist

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## Notable quotes / timestamps

- 0:04 "Create a CSV file for parameters that will update on the SCUTTLE robot."
- 2:17 "The first row contains column names."
- 4:39 "There we go — I get one message with both pieces of information."
- 5:11 "Save this in a gist — I'm calling it flow-mqtt-csv."

## Related videos

- [[videos/scuttle-robot-nodered-receive-mqtt-message-save-to-csv]]
- [[videos/scuttle-robot-plot-gamepad-values-in-nodered-via-txt-file]]
- [[videos/scuttle-robot-soldering-breadboards-for-i2c-bus]]
