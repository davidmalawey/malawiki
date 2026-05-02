---
type: video
title: "SCUTTLE Robot - Intro to Software Architecture"
video_id: "JY8tARr74Ic"
url: "https://www.youtube.com/watch?v=JY8tARr74Ic"
published: 2019-11-07
duration: "4:44"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, software-architecture, python, layered-design, lidar, troubleshooting]
ingested: 2026-05-02
---

## Overview

Introduction to the three-layer Python software architecture used by the [[entities/projects/scuttle-robot|SCUTTLE robot]]. David walks through a block diagram: yellow sensors and orange actuators feed into Level-1 device-driver scripts (one per sensor/actuator), which feed into Level-2 derivation/computation scripts, which feed into Level-3 decision-making programs that command the actuators.

## Key takeaways

- **Level 1 (green):** one Python file per sensor or actuator; talks directly to hardware, returns raw or near-raw data.
- **Level 2 (blue):** consumes one or more Level-1 outputs and computes domain meaning (e.g. `l2_obstacle.py` derives nearest-obstacle X/Y from `l1_lidar.py`).
- **Level 3:** decision-making — combines Level-2 signals into algorithms that issue commands or feedback.
- Purple labels on signal arrows specify what data is being passed; explicit naming keeps the mission semantics clear.
- A single Level-2 can output multiple derived values (nearest-obstacle coords, opening direction, etc.).
- Each level should have a commented-out test loop you can uncomment to run that module standalone for troubleshooting.
- Troubleshooting flows bottom-up: first verify hardware + L1 work in isolation, then verify the L1+L2 column, then add L3.
- Dependencies run vertically within a column; an L2 may import multiple L1s, and L1s import external libraries (USB lib, PyRPlidar driver) that don't appear on the architecture diagram.

## Techniques demonstrated

- [[concepts/layered-software-architecture]]
- [[concepts/standalone-testable-modules]]
- [[concepts/bottom-up-troubleshooting]]
- [[concepts/explicit-signal-labeling]]

## Tools used

- [[entities/tools/rplidar-a1|RPLIDAR A1]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- Python 3
- PyRPlidar driver library

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]] (Level-3 control example)
- Other [[series/scuttle-tutorials-2019]] tutorials.
