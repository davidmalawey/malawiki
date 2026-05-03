---
type: video
title: "SCUTTLE Robot - Choosing MQTT topics for mobile robot, IoT Guide (preliminary)"
video_id: "Ty5oz7wUEcw"
url: "https://www.youtube.com/watch?v=Ty5oz7wUEcw"
published: 2020-09-22
duration: "5:06"
tags: [mqtt, iot, scuttle-robot, topic-design, ecosystem, hivemq]
ingested: 2026-05-02
---

## Overview

A preliminary release of the SCUTTLE IoT guide proposing a shared [[concepts/mqtt|MQTT]] topic structure so every team can publish to the same broker (HiveMQ public, port 1883) and benefit from each other's data. David lays out a six-level topic taxonomy (e.g. `scuttle/fleet/onboard/battery/602/voltage`) and a payload convention (raw float/int, units on a separate topic).

## Chapters

- 0:00 Intro
- 0:47 MQTT topic structure
- 4:12 MQTT ecosystem
- 4:28 Mobile app
- 4:42 Outro

## Key takeaways

- Shared brokers + shared topics = shared data. If everyone uses the same convention, you can subscribe to other teams' robots and learn from their telemetry.
- Topic skeleton: `scuttle / fleet|infrastructure / onboard|static / <category> / <unit#> / <metric>` — six levels chosen for wildcard subscription flexibility.
- Payload should be a bare float or integer; emit units on a separate topic, not embedded in the value string.
- `scuttle/infrastructure/...` is reserved for off-robot devices (room sensors, payload way-stations) that participate in the same ecosystem.
- HiveMQ's free public broker is the starting point; everything is overridable later.

## Techniques demonstrated

- [[concepts/mqtt|MQTT topic taxonomy design]]
- Standardization-as-open-source for hobbyist robot fleets
- Payload separation of value from units

## Tools used

- HiveMQ public MQTT broker (`broker.mqttdashboard.com:1883`)
- Mobile MQTT app (iPhone / Android)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- SCUTTLE IoT ecosystem guide (in progress)

## Concepts

- [[concepts/mqtt|MQTT]]
- [[concepts/standards-as-open-source|Standards as open source]]
- [[concepts/parts-ecosystem-design|Ecosystem design]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-iot-in-all-forms-esp-pc-mobile-phone-raspi-demo-with-buzzer]]
