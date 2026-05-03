---
type: video
title: "Scuttle Robot - Nextec team tests computer vision docking"
video_id: "fRIDlLEdGno"
url: "https://www.youtube.com/watch?v=fRIDlLEdGno"
published: 2019-11-26
duration: "2:15"
series: "[[series/scuttle-robot]]"
tags: [scuttle, computer-vision, docking, webcam, encoders, autonomy, nextec]
ingested: 2026-05-02
---

## Overview

The Nextec team demos an early autonomous docking sequence on the [[entities/projects/scuttle-robot|SCUTTLE robot]] — a precursor to wireless docking and charging. Holding the gamepad B button hands control to a vision routine that finds the dock, triangulates the approach, and corrects course on its way in.

## Key takeaways

- Manual control: triggers for forward/back, shoulder buttons for left/right turn; press-and-hold B to initiate autonomous docking.
- Docking sequence: rotate to find the station via webcam, then triangulate based on apparent object size to estimate range.
- Distance estimation combines two signals — apparent dock size from the webcam (known dimension to scale lookup) and motor encoder counts for traveled distance.
- Self-correction loop visible during the approach (small jitter is partly attributed to a person holding the chassis).
- After a simulated charge, the robot backs off the dock and resumes its prior task.

## Tools and components

- [[entities/projects/scuttle-robot|SCUTTLE robot]] base
- USB webcam (vision sensor)
- Wheel encoders (odometry)
- Gamepad (manual override)
- Charging station / dock target

## Concepts demonstrated

- [[concepts/vision-driven-kinematics]]
- [[concepts/sensor-actuator-controller-loop]]
- [[concepts/manual-override-coexistence]]
- [[concepts/mobile-robot-as-mobile-sensor]]

## Related videos

- [[videos/scuttle-robot-sick-lidar-sensor-scans-for-nearest-obstacle]]
- [[videos/scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-]]
