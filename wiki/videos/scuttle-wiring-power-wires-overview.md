---
type: video
title: "Scuttle Wiring - Power Wires Overview"
video_id: "E7_NHTZwens"
url: "https://www.youtube.com/watch?v=E7_NHTZwens"
published: 2019-01-29
duration: "2:18"
series: "[[series/scuttle-v1-build]]"
tags: [scuttle, wiring, power, anderson-powerpole, overview]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David Malawey]] gives a quick tour of the four power-wire pairs on [[entities/projects/scuttle-robot|SCUTTLE]] version 1: BeagleBone power, motor driver power, and the two motor output pairs. The video frames the wiring as a deliberate harness with [[entities/tools/anderson-connector|Anderson Powerpole]] connectors so subassemblies can be unplugged for testing.

## Key takeaways

- Four power wire pairs total: battery to BeagleBone, battery to motor drivers, and motor drivers to each motor.
- The BeagleBone barrel-connector cable is cut, stripped, and re-terminated with Anderson Powerpoles to interface with the battery harness.
- Component orientation matters - if you rotate brackets 180 degrees, you need to redo wire-length math.
- Motor driver receives 12 V directly from battery on the center contacts; right and left motor outputs go to the respective motors.
- Adding intermediate connectors on motor leads lets you isolate motors for bench testing.
- Tin stripped wire ends so they don't fray when inserted into screw terminals.

## Techniques demonstrated

- [[concepts/system-power-distribution|System power distribution]]
- [[concepts/cable-management|Cable management]]
- [[concepts/tinning-stranded-wire|Tinning stranded wire]]
- [[concepts/crimping|Crimping]]
- [[concepts/standardize-mounting-interfaces|Standardize mounting interfaces]]

## Tools used

- [[entities/tools/anderson-connector|Anderson Powerpole connector]]
- [[entities/tools/dc-gearmotor|12 V DC gearmotor]]
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/screw-terminal|Screw terminal]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-build-anderson-powerpole-12v-distributor]]
- [[videos/scuttle-robot-crimp-anderson-connectors-build-12v-splitter-harness]]
- [[videos/how-to-crimp-anderson-connectors]]
- [[videos/soldering-leads-on-12v-dc-motors-18awg-and-heat-shrink]]
