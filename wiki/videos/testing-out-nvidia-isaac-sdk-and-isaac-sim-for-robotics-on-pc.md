---
type: video
title: "Testing Out NVIDIA Isaac SDK and Isaac Sim for Robotics (On PC)"
video_id: "vs_cMoXaxnQ"
url: "https://www.youtube.com/watch?v=vs_cMoXaxnQ"
published: 2020-12-03
duration: "8:08"
tags: [nvidia, isaac-sdk, isaac-sim, simulation, robotics, lidar, scuttle, ubuntu, rtx]
ingested: 2026-05-02
---

## Overview

Guided exploration of NVIDIA's Isaac SDK and Isaac Sim on a custom Ubuntu PC, run as a play session with a collaborator narrating. David and his partner load the manipulator-arm sample, the Carter warehouse demo, and then bridge a live SDK-to-sim connection so a simulated robot is driven by the same engine that would later run onboard SCUTTLE for higher-performance LIDAR and computer-vision tasks.

## Key takeaways

- Isaac Sim uses RTX real-time ray tracing — visuals are striking but textures stream in (early frames render white before the warehouse "colors in").
- WASD-style fly camera in Isaac Sim: right-click + WASD to orbit, Q down, E up; X-mode lets you click a block then drag XYZ to reposition obstacles.
- The first manipulator demo plans an alternate path around a moved obstacle, but a non-solidified block lets the arm "go straight through" it — a sim-fidelity gotcha.
- Bridging Isaac SDK to Isaac Sim: load a scene (Carter warehouse), turn on robot engines, start the physics engine (David forgot first try), then start the SDK programs to see the connection light up.
- Once connected, the simulated LIDAR streams a real-time scan of the simulated environment back to the SDK — same data path you'd get from a physical sensor onboard the robot.
- Computer is "working so hard" — the workload "deserves a raise" (see PC build link in description). Plan is to migrate proven SDK code from sim to onboard SCUTTLE.

## Techniques demonstrated

- [[concepts/sensor-actuator-controller-loop|sensor-actuator-controller loop]] (sim-driven version of the same loop)
- [[concepts/vision-driven-kinematics|vision-driven kinematics]]
- [[concepts/mobile-robot-as-mobile-sensor|mobile robot as mobile sensor]]
- [[concepts/pc-evolution-analogy-for-robotics|PC evolution analogy for robotics]]

## Tools used

- NVIDIA Isaac SDK (no entity page yet)
- NVIDIA Isaac Sim (no entity page yet)
- Ubuntu (no entity page yet)
- [[entities/tools/rplidar-a1|RPLidar A1]] (referenced as the kind of sensor target this work is preparing for)
- [[entities/projects/lunchbox-pc|lunchbox PC]] / a custom PC build (linked in description)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (target deployment platform)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- A second voice walks through the demo alongside David (unnamed in transcript — likely a SCUTTLE collaborator).

## Notable quotes / timestamps

- 0:40 "Really exciting is they are using the RTX real-time tracings."
- 2:47 "We didn't solidify the block, that's okay — I just want to see a number of functions."
- 5:35 "This computer is working so hard — yes, I think it deserves a raise. Promotion."
- 6:26 "This is a LIDAR from the real real scanning of the environment" (referring to the simulated LIDAR scan inside Isaac Sim).
- 7:46 "SDK works with the simulation, so actually you can do your robot to work with the Isaac SDK engine — so you can make the navigation real work in the real world."

## Related videos

- [[the-lunchbox-pc-building-a-pc-in-2025]]
- [[simple-3d-printed-bracket-for-mounting-rplidar-a1-lidar-on-robot]]
- [[think-simple-mobile-robot-mobile-sensor]]
- [[how-real-experts-change-the-world-using-robotics]]
- [[optimal-robot-ecosystem]]
