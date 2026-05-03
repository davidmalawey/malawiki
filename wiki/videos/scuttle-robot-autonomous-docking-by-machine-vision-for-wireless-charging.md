---
type: video
title: "SCUTTLE Robot - Autonomous Docking by machine vision for Wireless Charging"
video_id: "ffzLKSx1p6A"
url: "https://www.youtube.com/watch?v=ffzLKSx1p6A"
published: 2020-09-24
duration: "11:44"
tags: [scuttle, robotics, machine-vision, wireless-charging, iot, capstone, beaglebone]
ingested: 2026-05-02
---

## Overview

A Texas A&M ETID capstone team ("nextec", graduated fall 2019) demonstrates an autonomous wireless charging station for [[entities/projects/scuttle-robot|SCUTTLE]]. The robot uses machine vision to detect a colored beacon, drives itself onto the dock, and the station tracks robot identity via RFID, reporting status to the [[entities/brands/cayenne|Cayenne]] IoT dashboard.

## Key takeaways

- Both the docking station and the on-board module run [[entities/tools/beaglebone-blue|BeagleBone Blue]] microcontrollers; the station handles RFID, vision target, and three wireless charging pads, while the SCUTTLE module manages relays for the LiPo charging path.
- Closed-loop docking uses a "theta offset" — the angle between the robot's vision center and the colored target — to keep the bot facing the station as it approaches.
- The PCB is designed with two large copper planes so it can pass at least 6 A across three 2 A wireless pads.
- RFID tags identify individual robots and the station auto-registers unknown tags as new Cayenne widgets, demonstrating a [[concepts/parts-ecosystem-design|parts ecosystem]] approach to fleet management.
- The front panel snaps off to disable wireless charging, an example of [[concepts/manual-override-coexistence|manual override coexistence]].

## Techniques demonstrated

- [[concepts/vision-driven-kinematics|vision-driven kinematics]]
- [[concepts/sensor-actuator-controller-loop|sensor-actuator-controller loop]]
- [[concepts/manual-override-coexistence|manual override coexistence]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/rfid-reader|RFID reader]]
- [[entities/tools/wireless-charging-pad|wireless charging pad]]
- [[entities/tools/relay-module|relay module]]

## Materials used

- [[entities/materials/acrylic|acrylic]] (etched front panel)
- [[entities/materials/lipo-battery|LiPo battery]] (3-cell)

## Projects

- [[entities/projects/scuttle-wireless-dock|SCUTTLE wireless dock]]
- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]] (customer)
- [[entities/people/nextec-capstone-team|nextec capstone team]]

## Brands

- [[entities/brands/cayenne|Cayenne]]
- [[entities/brands/texas-am|Texas A&M]]

## Notable quotes / timestamps

- 0:24 Conceptual block diagram
- 2:37 Software flow diagram
- 8:35 Station PCB schematic
- 10:30 RFID scan demo

## Related videos

- [[videos/iot-using-mqtt-on-esp8266-set-your-client-id-or-autogenerate-credentials]]
- [[videos/scuttle-robot-how-much-power-does-it-use-about-7w]]
