---
type: video
title: "SCUTTLE Robot - SICK Lidar Sensor Scans for Nearest Obstacle"
video_id: "pNLbpHtOGBA"
url: "https://www.youtube.com/watch?v=pNLbpHtOGBA"
published: 2019-11-10
duration: "1:15"
series: "[[series/scuttle-robot]]"
tags: [scuttle, lidar, sick, beaglebone-blue, sensor, nodered, mxet300]
ingested: 2026-05-02
---

## Overview

Demonstrates a [[entities/projects/scuttle-robot|SCUTTLE robot]] using a SICK TiM561 lidar with a [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] to scan for the nearest obstacle. The program down-samples the array, finds the closest vector, and pushes distance and angle to a NodeRed GUI in real time.

## Key takeaways

- Lidar samples a full 810-point array 15 times per second; software requests it ~10 Hz and grabs ~50 vectors.
- Closest vector in proximity is identified each loop and logged with distance and angle (theta).
- Theta sign convention: positive theta is to the left, negative to the right (axis inverted from camera image).
- Range is approximately plus/minus 135 degrees of useful scan.
- NodeRed GUI subscribes to the log stream for real-time display.

## Tools used

- SICK TiM561 lidar (sensor module on the chassis)
- [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] (host controller)
- NodeRed (GUI dashboard)

## Concepts demonstrated

- [[concepts/mobile-robot-as-mobile-sensor]]
- [[concepts/sensor-actuator-controller-loop]]

## Related videos

- [[videos/scuttle-robot-fasten-lidar-to-the-chassis]]
- [[videos/simple-3d-printed-bracket-for-mounting-rplidar-a1-lidar-on-robot]]
