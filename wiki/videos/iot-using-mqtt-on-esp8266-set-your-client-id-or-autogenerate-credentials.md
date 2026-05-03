---
type: video
title: "IoT using MQTT on ESP8266 - set your client ID or autogenerate credentials"
video_id: "CTDlxl7dhgs"
url: "https://www.youtube.com/watch?v=CTDlxl7dhgs"
published: 2020-10-11
duration: "7:25"
tags: [iot, mqtt, esp8266, arduino, scuttle, debugging, root-cause]
ingested: 2026-05-02
---

## Overview

David debugs an MQTT "error 2 / identifier rejected" on an [[entities/tools/esp8266-nodemcu|ESP8266]] and documents the fix: explicitly set a client ID instead of relying on the [[entities/tools/arduino-mqtt-client-library|ArduinoMqttClient]] library's `millis()` autogeneration. He also explains username/password fields, recommends a starting example sketch, and standardizes a `scuttle-esp6011` naming convention for the SCUTTLE IoT ecosystem.

## Key takeaways

- MQTT broker error code 2 means "identifier rejected" — the broker received a malformed or duplicate client ID.
- The ArduinoMqttClient library normally autogenerates a client ID from `millis()`, which is usually unique enough but can fail in edge cases.
- Username and password are optional in MQTT but useful once you start passing safety- or privacy-sensitive control data.
- Recommended starting sketch: `ArduinoMqttClient` library → `WiFiEchoCallback` example, since it tests both publish and subscribe paths.
- Standardized convention: `scuttle-espNNNN` IDs (`6011`, `6012`, ...) — avoid dots and spaces in IDs.
- Side note: David spotted a positive RSSI value, which is unphysical for received signal strength and flagged for follow-up.

## Techniques demonstrated

- [[concepts/root-cause-analysis|root cause analysis]]
- [[concepts/m2m-iot-communication|machine-to-machine IoT communication]]
- [[concepts/share-the-failure|share the failure]]
- [[concepts/version-marking|version marking]]

## Tools used

- [[entities/tools/esp8266-nodemcu|ESP8266 NodeMCU]]
- [[entities/tools/arduino-ide|Arduino IDE]]
- [[entities/tools/arduino-mqtt-client-library|ArduinoMqttClient library]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- [[entities/projects/scuttle-iot-guide|SCUTTLE IoT guide]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Brands

- [[entities/brands/arduino|Arduino]]
- [[entities/brands/grabcad|GrabCAD]]

## Notable quotes / timestamps

- 0:19 The problem (error code 2)
- 5:26 Conclusion
- 6:37 Example sketch recommendation

## Related videos

- [[videos/should-we-make-an-iot-racetrack-for-scuttle-bots-on-bots]]
- [[videos/scuttle-robot-autonomous-docking-by-machine-vision-for-wireless-charging]]
