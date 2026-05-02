---
type: video
title: "Fully Explained Build: Test Setup, PWM Generator, DC Motor Driver, Gearmotor"
video_id: "iNG-G44Cd5s"
url: "https://www.youtube.com/watch?v=iNG-G44Cd5s"
published: 2025-07-29
duration: "41:03"
tags: [pwm, dc-motor, motor-driver, h-bridge, electronics, tutorial, open-lab]
ingested: 2026-05-02
---

## Overview

A 40-minute end-to-end tutorial: [[entities/people/david-malawey|David]] wires a [[entities/tools/pwm-signal-generator|D-Rock PWM signal generator]] to a [[entities/tools/dual-h-bridge-motor-driver|dual H-bridge motor driver]] and a 200 RPM [[entities/tools/dc-gearmotor|DC gearmotor]], using a [[entities/tools/magnet-base-test-rig|magnet-base test rig]] as the workbench. Along the way he covers soldering Dupont pins onto a PCB, "stealing" 5 V from a 12 V circuit, sampling motor noise, eliminating loose wires, and laying out a lab so a student can be 4× more productive. This is the canonical [[entities/projects/scuttle-robot|SCUTTLE]] / Open Lab speed-controllable DC primer.

## Key takeaways

- A speed-controllable DC system is three boxes: a [[concepts/pwm|PWM]] command signal generator, an H-bridge driver, and a [[concepts/dc-motor-fundamentals|DC motor]] (often with a gearbox).
- PWM frequency must be tuned to the motor: too low and you get audible noise and hot windings; too high and the driver loses efficiency. Servo PWM (~50 Hz, 1–2 ms pulse) is a different convention than motor-driver PWM.
- Dupont housings + soldered header pins are the cheap way to convert "incompatible terminals" into something repluggable on a breadboard.
- A 12 V system can power a 5 V microcontroller side via a small linear/buck regulator board — saves a second supply.
- Test-rig hygiene (magnet base, no loose wires, labeled terminals) is the difference between a demo that runs and a project you can return to next week.

## Techniques demonstrated

- Wiring a [[concepts/pwm|PWM signal generator]] to a [[concepts/h-bridge-trigger-module|dual H-bridge driver]].
- Soldering Dupont header pins onto a PCB to expose breakable terminals.
- Tapping 5 V from a 12 V supply via a $1 regulator board.
- Sampling and recording acoustic noise from a running gearmotor at varied PWM frequencies.
- [[concepts/5s-methodology|5S-style]] lab organization for a portable test setup.

## Tools used

- [[entities/tools/pwm-signal-generator|D-Rock PWM signal generator]]
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver (5 A, 2 ch)]]
- [[entities/tools/dc-gearmotor|DC gearmotor (200 RPM)]]
- [[entities/tools/magnet-base-test-rig|Magnet base]] (for the test rig)
- [[entities/tools/dupont-housings-kit|Dupont housings kit]]
- [[entities/tools/pinecil|Pinecil soldering iron kit]]

## Materials used

- Breadboard, jumper wires, solder, header pins.

## Projects

- An open-source PWM-driven DC motor test bench, intended to be replicable by [[entities/projects/scuttle-robot|SCUTTLE]] students and the [[entities/projects/scuttle-robotics-lab-nigeria|Nigeria lab]].

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/make-a-frankenstein-power-drill-treadmill-motor-controller-easy|Make a Frankenstein Power Drill Treadmill Motor Controller]] — same architecture, harvested from a power tool instead of bought as breakouts.
- [[videos/dual-power-supply-for-electronics-prototyping-full-tutorial|Dual Power Supply for Electronics Prototyping]] — the 12 V + 5 V power source this kind of test rig needs.
