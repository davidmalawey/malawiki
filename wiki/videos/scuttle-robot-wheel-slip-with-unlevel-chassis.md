---
type: video
title: "Scuttle Robot - Wheel Slip with unlevel chassis"
video_id: "JfYrRua7tiw"
url: "https://www.youtube.com/watch?v=JfYrRua7tiw"
published: 2019-02-12
duration: "0:23"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle-robot, wheel-slip, chassis, kinematics, test]
ingested: 2026-05-02
---

## Overview

A short demonstration showing that a non-level [[entities/projects/scuttle-robot|SCUTTLE]] chassis biases wheel slip toward one side under straight-line drive commands. Levelling the chassis evens the load and reduces overall slipping.

## Key takeaways

- With pure forward/backward commands and no turning input, an unlevel chassis still produces asymmetric wheel behavior.
- A non-level chassis tends to let one wheel slip predominantly and requires less torque to enter a slip condition.
- Levelling the chassis evens out slip across both wheels and reduces overall slipping.

## Techniques demonstrated

- [[concepts/wheel-slip-diagnosis]]
- [[concepts/chassis-leveling]]
- [[concepts/leveraging-physical-testing]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## Related videos

- [[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]]
- [[videos/navigationvectors-part1-global-position-increment]]
