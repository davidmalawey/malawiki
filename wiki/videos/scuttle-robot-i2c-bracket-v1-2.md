---
type: video
title: "Scuttle Robot - i2c bracket v1.2"
video_id: "_ZNiIEPJr7c"
url: "https://www.youtube.com/watch?v=_ZNiIEPJr7c"
published: 2019-02-26
duration: "1:03"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle-robot, i2c, bracket, 3d-printing, abs, mounting]
ingested: 2026-05-02
---

## Overview

Walkthrough of the v1.2 [[entities/tools/i2c-bracket|I2C bracket]] for [[entities/projects/scuttle-robot|SCUTTLE]] — a 3D-printed [[entities/materials/abs|ABS]] mount that holds the I2C PCB to the chassis aluminum rods, with a clearance shelf for through-hole pins and an orientation rule that places the headers near the rest of the electronics so cables can reach the encoders and the [[entities/tools/beaglebone-blue|BeagleBone]].

## Key takeaways

- v1.2 is 3D-printed in [[entities/materials/abs|ABS]] and uses two coarse M2 screws for fastening the PCB.
- A small shelf is designed in to give clearance for the through-hole pin tips on the underside of the PCB.
- A clip feature on the bracket grips the chassis aluminum rods directly — no extra fasteners for chassis attachment.
- Orient the PCB so the pin headers face inward toward the other electronics; this makes the encoder cables and the I2C run to the BeagleBone reach without strain — barely, "once you have the cap on."
- This is part of the broader [[concepts/snap-fit-bearing-mount|snap-fit mounting]] / [[concepts/standardize-mounting-interfaces|standardized mounting interface]] pattern across SCUTTLE.

## Techniques demonstrated

- [[concepts/clip-onto-extrusion-mounting]]
- [[concepts/pin-clearance-shelf]]
- [[concepts/connector-orientation-for-cable-reach]]
- [[concepts/version-marking]]
- [[concepts/standardize-mounting-interfaces]]
- [[concepts/cable-routing-through-structure]]

## Tools used

- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/i2c-bracket|I2C bracket]]
- [[entities/tools/i2c-bus-board|I2C bus board]]
- [[entities/tools/wheel-encoder|wheel encoder]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/m2-screw|M2 coarse screw]]

## Materials used

- [[entities/materials/abs|ABS]]
- [[entities/materials/aluminum|aluminum]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## Related videos

- [[videos/scuttle-robot-soldering-the-i2c-bus-board]]
- [[videos/scuttle-robot-cut-i2c-circuit-board]]
- [[videos/scuttle-robot-upgrade-i2c-bracket-for-new-pcb-retrofit-by-gluing]]
- [[videos/scuttle-robot-unbox-solder-mount-encoder-pcb-to-bracket]]
