---
type: video
title: "NavigationVectors part1: global position increment"
video_id: "7k-5QmsfEpU"
url: "https://www.youtube.com/watch?v=7k-5QmsfEpU"
published: 2020-06-26
duration: "14:15"
tags: [scuttle, navigation, kinematics, software, robotics]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] walks through the global-position increment math used in the new [[entities/projects/scuttle-robot|SCUTTLE]] driving software. The robot moves in two-part waypoint segments — a constant-radius curve followed by a straight — and on every wheel-encoder tick the code computes a small translation in scuttle's local frame, rotates it into the global frame using a rotation matrix built from the average of the previous and updated heading, and accumulates that into the global XY position. Companion to [[videos/navigationvectors-part2-curve-criteria|part 2]].

## Key takeaways

- Every waypoint resolves into two phases: curve at constant radius, then drive straight. No point turns.
- For each tiny increment (~1-5 mm), local displacement is treated as a straight line `[dx, 0]` in the robot's frame, ignoring the small arc.
- The rotation angle used in the rotation matrix is `previous_heading + d_theta/2` — the average of headings before and after the step, not the new heading itself.
- Global position update: `global_position += R(theta_avg) @ [dx, 0]`.
- Heading is updated as a separate step after the position increment.
- Code is in a public gist linked from the video description (with known errors).

## Techniques demonstrated

- Numerical integration of differential-drive kinematics from wheel encoder increments.
- Use of a 2D rotation matrix to transform body-frame displacements into the world frame.
- Approximation that small arc segments can be treated as straight-line translations.

## Tools used

- Tablet sketching for live whiteboarding of the math.

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE]] — this is part of its driving software.

## People mentioned

- [[entities/people/david-malawey|David Malawey]] — author of the code and explanation.

## Notable quotes / timestamps

- 0:00 — sketch setup, two-part curve+straight waypoint behavior.
- 7:40 — Rotation Matrix chapter.
- 10:10 — Global Vector chapter.
- 12:38 — Updating the Heading chapter.

## Related videos

- [[videos/navigationvectors-part2-curve-criteria|NavigationVectors part 2: Curve Criteria]] — paired companion video on when to stop curving.
- [[videos/scuttle-robot-how-the-magnetometer-sensor-compass-works|SCUTTLE Robot - How the Magnetometer Sensor (compass) works]] — provides the absolute heading the global frame is referenced to.
