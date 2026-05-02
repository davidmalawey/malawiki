---
type: video
title: "Make a Frankenstein Power Drill Treadmill Motor Controller, Easy"
video_id: "tt13GCgdD68"
url: "https://www.youtube.com/watch?v=tt13GCgdD68"
published: 2025-07-12
duration: "37:20"
tags: [power-tools, dc-motor, h-bridge, teardown, mechatronics, open-lab]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] tears down a broken cordless drill to expose its modular components — battery interface, [[concepts/h-bridge-trigger-module|H-bridge trigger module]], brushed [[concepts/dc-motor-fundamentals|DC motor]], planetary gearbox with sun and ring gears, and chuck — and explains how each piece works. He then "Frankensteins" the drill's trigger module onto a salvaged treadmill motor, demonstrating that the same H-bridge / battery / brushed-DC architecture scales from an 18 V hand tool to a much larger flywheel-loaded machine. The video doubles as a [[entities/projects/scuttle-robot|SCUTTLE]]-adjacent open-lab teaching artifact.

## Key takeaways

- Modern cordless drills are a small set of swappable modules: battery, trigger/H-bridge controller, motor, gearbox, clutch, chuck. Knowing the modules helps you compare brands by the parts that matter to you.
- The trigger module is essentially an [[concepts/h-bridge-trigger-module|H-bridge]] with extra circuitry — it sits between battery and motor and meters voltage to the brushed DC motor.
- A two-position mechanical gear selector changes ratios in the planetary gearbox; it has no effect on the electrical power delivery.
- Brushless variants spin faster and last longer than brushed equivalents but the system architecture is the same.
- The drill's trigger module can drive a treadmill motor on the same 18 V battery — same physics, different scale of mass and inertia.
- The drill's [[concepts/h-bridge-trigger-module|trigger module]] maps cleanly onto a [[entities/projects/scuttle-robot|SCUTTLE]] motor + driver pair, useful for student intuition.

## Techniques demonstrated

- Teardown and module-by-module identification of a power drill.
- Bench-testing a salvaged [[concepts/h-bridge-trigger-module|H-bridge trigger module]] outside its host tool.
- Driving a [[entities/tools/treadmill-motor|treadmill motor]] from an 18 V cordless drill battery via the drill's own controller.

## Tools used

- [[entities/tools/cordless-drill|Cordless drill]] (donor unit)
- [[entities/tools/treadmill-motor|Treadmill motor]] (Frankenstein load)
- [[entities/tools/cordless-drill-battery|18 V cordless drill battery]]

## Materials used

- Hardened steel planetary gears (sun and ring), spur gear, and clutch components from inside the drill.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor|Fully Explained Build: Test Setup, PWM Generator, DC Motor Driver, Gearmotor]] — the lab-grade equivalent: same H-bridge + brushed DC system, but built from breakout boards instead of harvested.
