---
type: video
title: "How to connect a Hobby ESC (speed control) to raspberry Pi - drive a 12v DC motor bi-directionally"
video_id: "zvbN1lPjd-I"
url: "https://www.youtube.com/watch?v=zvbN1lPjd-I"
published: 2021-02-09
duration: "5:36"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, raspberry-pi, motor-control, pwm, esc, mechatronics]
ingested: 2026-05-02
---

## Overview

David walks through using a cheap RC-car-grade brushed DC ESC (rated 320 A, ~$5-10) driven by a Raspberry Pi over the standard hobby servo PWM signal (50 Hz, 1-2 ms pulse width). He shows how a gamepad axis maps to pulse width, how to find the neutral point, and the quirk that the controller refuses to switch directly forward-to-reverse without first passing through neutral.

## Key takeaways

- Hobby ESCs use the same 50 Hz / 1-2 ms PWM convention as standard 180-degree servos.
- 1.0 ms = full reverse, 1.5 ms (approx.) = neutral, 2.0 ms = full forward — but each unit calibrates slightly differently and saturates outside its range.
- Forward-to-reverse transitions require touching neutral first; reverse-to-forward is more permissive.
- Sweep an analog control through the range to discover the controller's actual neutral point.
- Off-the-shelf RC ESCs are a high-value alternative to bare H-bridges like the L298N when you need more current capacity.

## Techniques demonstrated

- [[concepts/pwm|PWM]] generation for hobby servo / ESC signaling
- Mapping a gamepad axis to a pulse-width range
- Finding controller saturation and neutral by sweep

## Tools used

- [[entities/brands/raspberry-pi|Raspberry Pi]]
- [[entities/tools/hobby-esc|Hobby ESC]] (320 A brushed DC controller)
- [[entities/tools/gamepad|Gamepad]] (USB)
- [[entities/tools/h-bridge|H-bridge]] (referenced as alternative — L298N)
- [[entities/tools/dc-gearmotor|DC gearmotor]] (12 V brushed)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [1:30] "This motor controller is based on the hobby kind of standard where 50 hertz is the speed of the frequency of the signal that goes out, and then the pulse width ranges from one millisecond to two milliseconds."
- [3:36] On forward-to-reverse: "First it needs to see that pulse width that corresponds to the neutral."

## Related videos

- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
- [[videos/how-much-cpu-does-it-take-to-generate-pwm-signals-on-raspberry-pi]]
