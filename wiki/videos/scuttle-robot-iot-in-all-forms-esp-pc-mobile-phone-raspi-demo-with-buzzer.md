---
type: video
title: "SCUTTLE Robot - IoT in ALL FORMS!  ESP / PC / Mobile Phone / RasPi / demo with BUZZER"
video_id: "Vr_CxYMBWKY"
url: "https://www.youtube.com/watch?v=Vr_CxYMBWKY"
published: 2020-09-20
duration: "23:30"
tags: [iot, mqtt, scuttle-robot, esp8266, wemos, arduino, node-red, buzzer, m2m]
ingested: 2026-05-02
---

## Overview

The "tie it all together" IoT demo: gamepad -> SCUTTLE (Pi/BeagleBone) -> [[concepts/mqtt|MQTT]] over the public HiveMQ broker -> standalone WeMos/ESP device on a single 18650 battery -> buzzer chirps when motion starts/stops. David shows the full publish/subscribe loop across Python, [[concepts/node-red|Node-RED]], an Arduino-programmed ESP, a PC web client, and a mobile phone — all five device types speaking the same MQTT topic.

## Chapters

- 0:00 Intro
- 3:43 Mobile phone demos
- 7:35 Install Node-RED
- 15:24 Arduino
- 19:29 Gamepad demo
- 23:03 Demo MQTT from cell phone to ESP

## Key takeaways

- MQTT cleanly decouples robot from peripheral devices: the buzzer ESP needs no wires, no serial, just Wi-Fi and a battery.
- Node-RED is universal-enough to run on Pi, BeagleBone, Jetson Nano, Windows, and Linux — and can start at boot to publish in the background.
- A `watch` node + `tmp/buzzCode.txt` flag pattern lets Python signal Node-RED without tight coupling: Python writes the file, Node-RED detects the change and publishes MQTT.
- The Arduino sketch on the WeMos D1 R2 reads the integer payload via ASCII (so a "1" arrives as character 49 — keep that in mind).
- Round-trip latency from Texas to a Singapore broker and back is fast enough that the buzzer feels like part of the robot.
- Distributed M2M architecture lets team members work on independent modules in parallel — software, sensors, payload modules — and tolerate temporary connection loss gracefully.

## Techniques demonstrated

- [[concepts/mqtt|MQTT publish/subscribe]] across heterogeneous devices
- [[concepts/node-red|Node-RED]] file-watch -> MQTT publish flow
- Boolean flag-based event detection in Python (rising/falling edge on joystick)
- Arduino + ESP8266 sketch programming with board-specific pin mappings (D3/D4 vs raw GPIO)
- Standalone-battery embedded IoT node (WeMos + 18650)

## Tools used

- [[entities/tools/raspberry-pi|Raspberry Pi]]
- [[entities/tools/beaglebone-y-ai|BeagleBone Blue]]
- [[entities/tools/jetson-nano|Jetson Nano]] (mentioned as alternative)
- [[entities/tools/esp8266-nodemcu|ESP8266 / WeMos D1 R2]]
- [[entities/tools/18650-cell|18650 cell]]
- [[entities/tools/buzzer|Piezo buzzer]]
- [[entities/tools/gamepad|Xbox-style gamepad]]
- [[entities/tools/arduino-ide|Arduino IDE]]

## Materials/Software

- Python 3, C++, Node-RED, Debian Linux, MQTT (HiveMQ public broker)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- SCUTTLE IoT ecosystem demo

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-choosing-mqtt-topics-for-mobile-robot-iot-guide-preliminary]]
- [[videos/scuttle-robot-nodered-function-to-extract-each-gamepad-axis-display]]
