---
type: video
title: "SCUTTLE Robot - How Proportional Feedback Control is Implemented (kp)"
video_id: "yt89x3SFG8A"
url: "https://www.youtube.com/watch?v=yt89x3SFG8A"
published: 2019-10-03
duration: "7:36"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, control-systems, pid, proportional-control, kp, node-red]
ingested: 2026-05-02
---

## Overview

David demonstrates how proportional feedback control (the Kp term in a PID controller) is implemented on the [[entities/projects/scuttle-robot|SCUTTLE robot]]. He runs `L3_PID_lab.py`, pulls the Kp value live from a `kp.txt` file written by the [[entities/tools/node-red|Node-RED]] dashboard, and walks through the math: error = target - measured, control effort u_p = Kp × error, fed as PWM duty cycle to the motor driver.

## Key takeaways

- Closed-loop wheel-speed control needs three live inputs: Phi-dot targets (left/right), measured Phi-dots, and dt for the optional derivative term.
- Kp is read from `kp.txt` so it can be tuned in real time from the Node-RED dashboard without restarting the program.
- Error is defined as `target - current`. For Phi-dot target = 9.7 rad/s and current = 1.36 rad/s, error = 8.34.
- u_p = Kp × error → 0.04 × 8.3 ≈ 0.33, meaning a 33% PWM duty cycle to the motor driver.
- At only 33% of 12V, the motors barely overcome static friction — shows the need for higher Kp or integral term.
- Increasing Kp from 0.05 to 0.07 brings wheel speed up to ~3.5–4 rad/s but introduces oscillation as the controller overshoots and undershoots the target each sample.
- Encoder readings have their own error sources: rollover, sample rate, and resolution.

## Techniques demonstrated

- [[concepts/proportional-control]]
- [[concepts/pid-control]]
- [[concepts/runtime-tunable-parameters]]
- [[concepts/closed-loop-feedback]]
- [[concepts/control-oscillation]]
- [[concepts/pwm]]

## Tools used

- [[entities/tools/node-red|Node-RED]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver]]
- [[entities/tools/dc-gearmotor|DC gearmotor]]
- [[entities/tools/wheel-encoder]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes

- "Your error will be defined as the difference between the target value and the current value."
- "0.33 is going to be the full control effort... we call that u_P."
- "That's how you end up with the oscillations when you're just dealing with Kp."

## Related videos

- [[videos/reduce-the-dead-band-from-your-dc-motors-with-this-function]]
- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
- Other [[series/scuttle-tutorials-2019]] tutorials.
