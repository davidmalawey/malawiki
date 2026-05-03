---
type: video
title: "Dual Power Supply for Electronics Prototyping [FULL TUTORIAL]"
video_id: "Zrt5EQ3SnGU"
url: "https://www.youtube.com/watch?v=Zrt5EQ3SnGU"
published: 2025-08-29
duration: "16:49"
tags: [usb-pd, power-supply, electronics, tutorial, open-lab, prototyping]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] builds a compact 12 V + 5 V dual-rail benchtop power supply from a [[entities/tools/usb-pd-trigger-board|USB-PD trigger board]], a $1 5 V regulator board, and a cork-board base — all powered from any USB-C PD wall adapter. The design solves a real problem from his [[entities/places/texas-am-lab|Texas A&M lab]]: students were running out of bench space because every project needed a separate benchtop supply for the microcontroller and the actuator. Output: 30 W at 12 V plus 5 W at 5 V, simultaneously available, off a single USB-C cable.

## Key takeaways

- USB-PD trigger boards are now cheap enough to be the right answer for "I need 12 V at the bench" in a teaching lab — no more bench-monster supplies.
- Tap the trigger board's vias to solder a 5 V regulator directly onto its 12 V output, merging two boards into one unit.
- A cork-board base + hot glue is the right amount of structure for a $5 prototype power supply — rigid enough, easy to MOD/rework, no enclosure design required.
- The resulting supply gives "exactly what you need" for typical mechatronics: a microcontroller rail (5 V) and an actuator rail (12 V).
- "Is it professional grade? No. It's better, because it's more accessible & less investment." — explicit re-framing of accessibility as a design quality.
- A [[entities/tools/usb-power-meter|USB power meter]] confirms actual draw before students plug in expensive boards.

## Techniques demonstrated

- Identifying and soldering to PCB vias to expose 12 V and ground from a [[entities/tools/usb-pd-trigger-board|PD trigger board]].
- Stacking and merging two breakout boards into one unit.
- Cork-board + hot-glue prototype housing as a deliberately MOD-friendly enclosure.
- Verifying voltage and current with a [[entities/tools/usb-power-meter|USB power meter]] before powering downstream electronics.

## Tools used

- [[entities/tools/usb-pd-trigger-board|USB-PD trigger board]]
- 5 V regulator board (~$1 generic, formerly labeled "HK…")
- [[entities/tools/usb-power-meter|USB power meter]]
- Soldering iron, hot glue gun

## Materials used

- Cork board (base)
- Hot glue
- USB-C PD wall adapter and cable

## Projects

- Open-lab benchtop supply, documented at qr.net/openlabproject as part of the Open Lab tooling David is curating for [[entities/projects/scuttle-robot|SCUTTLE]] / [[entities/projects/scuttle-robotics-lab-nigeria|Nigeria lab]] use.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor|Fully Explained Build: Test Setup, PWM Generator, DC Motor Driver, Gearmotor]] — uses the kind of 12 V + 5 V rails this supply provides.
