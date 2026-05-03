---
type: video
title: "SCUTTLE Robot - How the Magnetometer Sensor (compass) works"
video_id: "o6_OJ3TO8rM"
url: "https://www.youtube.com/watch?v=o6_OJ3TO8rM"
published: 2020-07-28
duration: "7:56"
tags: [scuttle, sensor, magnetometer, imu, calibration, robotics]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] explains how the magnetometer compass on the [[entities/projects/scuttle-robot|SCUTTLE]] robot works and why it has to be calibrated per-robot. The compass is a three-axis magnetometer embedded inside the BeagleBone Blue's MPU9250 9-axis IMU; encoders give relative orientation but only the magnetometer can fix scuttle's heading to global north. Each axis maxes out (+1) pointing at magnetic north and minimums (-1) pointing south, but raw values are not normalized at the factory — calibration discovers the per-axis min/max by spinning the robot in place, then rescales and centers the readings to [-1, 1]. With calibrated x and y, `arctan2(y, x)` gives an unambiguous heading across all four quadrants.

## Key takeaways

- The compass is a 3-axis magnetometer; only x and y are needed for heading on a flat surface, z matters only when the robot tilts.
- IMUs are bundles: a magnetometer + accelerometer + gyro. SCUTTLE uses the MPU9250 on the [[entities/tools/beaglebone-y-ai|BeagleBone]] Blue.
- Encoders give relative motion; the magnetometer is what anchors that motion to a global frame (e.g. the building or earth's north).
- Calibration must be done with the sensor mounted on the robot — surrounding ferrous metal and magnets shift the readings.
- Calibration procedure: spin the robot in a full circle to discover per-axis min/max, then rescale to a span of 2 and subtract 1 to center on zero.
- A single axis is ambiguous (east and west both read zero on x). `arctan2(y, x)` resolves the quadrant correctly using the sign pair.
- Theta is defined as scuttle's x-vector minus the global x-vector; positive theta means scuttle has turned left of north.

## Techniques demonstrated

- Per-device sensor calibration (min/max sweep, rescale, center).
- Quadrant-correct heading recovery via `arctan2`.
- Sensor fusion concept: relative (encoders) vs absolute (compass) orientation.

## Tools used

- [[entities/tools/beaglebone-y-ai|BeagleBone]] Blue — host board with the on-board MPU9250 IMU.
- MPU9250 9-axis IMU (magnetometer + accelerometer + gyro).
- `mpu.py` — script run on the BeagleBone to read and test the magnetometer.

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE]] — the robot using this compass for global heading.

## People mentioned

- [[entities/people/david-malawey|David Malawey]].

## Notable quotes / timestamps

- 1:27 — Calibration.
- 2:15 — How does the magnetometer behave.
- 4:55 — Determining the absolute orientation.
- 7:26 — Choosing the quadrant (arctan2).

## Related videos

- [[videos/navigationvectors-part1-global-position-increment|NavigationVectors part 1]] and [[videos/navigationvectors-part2-curve-criteria|part 2]] — consume this heading to drive in a global frame.
