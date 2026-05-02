---
type: video
title: "Reduce the Dead Band from your DC Motors with this Function"
video_id: "sii5VDNHI-o"
url: "https://www.youtube.com/watch?v=sii5VDNHI-o"
published: 2022-02-12
duration: "6:55"
series: "[[scuttle-robot]]"
tags: [scuttle, dc-motor, pwm, controls, dead-band, software, calibration]
ingested: 2026-05-02
---

## Overview

David walks through the `compress` function inside SCUTTLE's `motor.pi` software — a small mapping that sits between the controller's commanded duty cycle and the PWM output sent to the motor driver. Its purpose is to compress out the "dead band," that range of low duty-cycle commands where the motor receives current but produces no motion because the voltage can't overcome internal friction in the motor, gearbox, and pulleys.

## Key takeaways

- DC gearmotors have a dead band: roughly 28% of the commanded range produces buzzing, heat, and current draw but no wheel motion.
- The `compress` function takes two user-set parameters — an initial slope and a critical y-inflection (the duty cycle at which motion actually starts, e.g. 0.22).
- Increasing the slope shrinks the dead band so small inputs map quickly into the moving region (e.g. inputs above 0.073 or 7.5% can produce motion).
- Don't compress all the way to zero dead band: jumping straight to a motion-producing duty cycle hides torque differences across the dead-band range and disturbs PID transients during accelerate/decelerate or direction reversal.
- Each motor is slightly different — run a sweep, observe wheel speed vs. duty cycle, then tune `compress` per motor.

## Techniques demonstrated

- [[concepts/pwm|PWM]] generation and trim for DC motors
- [[concepts/dc-motor-fundamentals|DC motor fundamentals]] (dead band, internal friction)
- [[concepts/dead-band-compensation|Dead-band compensation]] via piecewise mapping
- [[concepts/sensor-actuator-controller-loop|Sensor-actuator-controller loop]] tuning

## Tools used

- [[entities/tools/dual-h-bridge-motor-driver|H-bridge motor driver]]
- [[entities/tools/dc-gearmotor|DC gearmotor]]
- [[entities/tools/pwm-signal-generator|PWM signal generator]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [1:51] "some area here in the middle which I will call the dead band" — voltage insufficient to overcome internal friction.
- [4:43] If you compress too aggressively (jump straight to motion) you "throw off the controller" during transients.

## Related videos

- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
- [[videos/make-a-frankenstein-power-drill-treadmill-motor-controller-easy]]
