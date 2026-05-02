---
type: video
title: "SCUTTLE Robot - nodered receive mqtt message & save to csv"
video_id: "4_rlm2HexTI"
url: "https://www.youtube.com/watch?v=4_rlm2HexTI"
published: 2020-09-04
duration: "5:36"
tags: [scuttle, nodered, mqtt, csv, iot, raspberry-pi]
ingested: 2026-05-02
---

## Overview

Companion to the previous [[entities/tools/nodered|Node-RED]] tutorial, but in the receive direction: David's phone publishes a comma-separated MQTT payload to `scuttle/pi/cmd` on the HiveMQ broker, the [[entities/tools/raspberry-pi|Raspberry Pi]]'s Node-RED flow subscribes to that topic, parses the payload through a csv node configured with named columns ("field a, field b"), and writes the result to `/home/pi/scuttle/data3.csv`. He demonstrates the round-trip: phone publishes "2.5,2.6", the file appears on disk, and `cat` shows the values bound to their column names.

## Key takeaways

- Flow: mqtt in -> debug -> csv parser -> debug + file out.
- Configure the csv node with column names ("field a, field b"); separator = comma (a phone keyboard can't easily type a tab).
- File-out node creates the directory and file if missing, appends a newline per payload, and uses default UTF-8 encoding.
- Topic split mirrors the previous video: `scuttle/pi/cmd` for commands flowing in, `scuttle/pi/gp` for gamepad data flowing out.
- The output `cat data3.csv` shows JSON-shaped key/value pairs because the csv node bound the incoming string to the named columns.
- Shared the flow as a public gist for reuse.

## Techniques demonstrated

- Node-RED flow design (mqtt in -> csv -> file out)
- [[concepts/mqtt-pub-sub|MQTT publish/subscribe]] in the inbound direction
- CSV parsing of an inbound string into named fields
- [[concepts/iot-data-flow|IoT data flow]] from phone to robot
- [[concepts/open-source-knowledge|Open-source knowledge]] — flow shared as a public gist

## Tools used

- [[entities/tools/nodered|Node-RED]]
- [[entities/tools/raspberry-pi|Raspberry Pi]] (or [[entities/tools/beaglebone-y-ai|BeagleBone]])
- MQTTool app (iOS/Android)
- HiveMQ public broker
- GitHub Gist

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## Notable quotes / timestamps

- 0:46 "My cell phone is going to send commands wirelessly and my robot is going to receive the commands."
- 1:21 "Comma works better because on my cell phone I don't know how to add a tab."
- 4:32 "Boom, now we have data3.csv."
- 5:22 "Has the same information but it's conditioned as we expected."

## Related videos

- [[videos/scuttle-robot-nodered-read-csv-to-send-mqtt]]
- [[videos/scuttle-robot-plot-gamepad-values-in-nodered-via-txt-file]]
- [[videos/scuttle-robot-soldering-breadboards-for-i2c-bus]]
