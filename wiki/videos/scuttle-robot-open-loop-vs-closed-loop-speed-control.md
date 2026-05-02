---
type: video
title: "SCUTTLE Robot - open loop vs closed loop speed control"
video_id: "uYnGog1Pc_8"
url: "https://www.youtube.com/watch?v=uYnGog1Pc_8"
published: 2019-08-09
duration: "1:16"
tags: [scuttle, control-systems, pid, open-loop, closed-loop, mxet]
ingested: 2026-05-02
---

## Overview

A short demo contrasting two driving modes on SCUTTLE: open-loop (gamepad trigger directly maps to PWM voltage) and closed-loop (joystick axes set target wheel speeds, two PID controllers act on each wheel). Open-loop responds instantly with no oscillations but cannot guarantee a target speed, and small throttle inputs may not move the vehicle at all. Closed-loop achieves the target but, with the loop poorly tuned, exhibits oscillation and integral wind-up (the robot keeps creeping after release).

## Key takeaways

- Open-loop control is simple and stable, but doesn't account for load — small voltages may produce zero motion below the dead band.
- Closed-loop PID hits a target speed but requires tuning, and untuned gains visibly produce oscillation and wind-up.
- Joystick axes for the closed-loop mode are interpreted as `x_dot` (forward/backward) and `theta_dot` (yaw rate), with kinematics fully described in the SCUTTLE Kinematics Guide.
- Integral wind-up shows up as the robot continuing to drive briefly after the input is released.

## Techniques demonstrated

- [[concepts/open-loop-control|open-loop control]]
- [[concepts/closed-loop-feedback|closed-loop feedback]]
- [[concepts/pid-control|PID control]]
- [[concepts/integral-windup|integral wind-up]]
- [[concepts/dead-band-compensation|dead-band compensation]]
- [[concepts/control-oscillation|control oscillation]]
- [[concepts/differential-drive-kinematics|differential drive kinematics]]
- [[concepts/pwm|PWM]]

## Tools used

- [[entities/tools/gamepad|gamepad]]
- [[entities/tools/dc-gearmotor|DC gearmotor]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]]
- [[videos/reduce-the-dead-band-from-your-dc-motors-with-this-function]]
- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
- [[videos/navigationvectors-part1-global-position-increment]]
