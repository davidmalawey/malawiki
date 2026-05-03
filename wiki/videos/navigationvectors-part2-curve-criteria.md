---
type: video
title: "NavigationVectors part2: Curve Criteria"
video_id: "bU78G0S6LGw"
url: "https://www.youtube.com/watch?v=bU78G0S6LGw"
published: 2020-06-26
duration: "16:08"
tags: [scuttle, navigation, control, software, robotics]
ingested: 2026-05-02
---

## Overview

Companion to [[videos/navigationvectors-part1-global-position-increment|part 1]]. [[entities/people/david-malawey|David]] explains how the [[entities/projects/scuttle-robot|SCUTTLE]] driving algorithm decides whether to curve or drive straight toward the target. On every wheel increment, the code recomputes a "global vector" from the current measured position to the target point and compares its angle to the robot's current heading; the difference is `theta_gap`. A user-defined `span` sets the angular tolerance — if `theta_gap` is inside the span, drive straight; otherwise keep curving. A `flip` variable picks the sign of the curve, and curve speed is `curve_rate * flip`.

## Key takeaways

- Goal: avoid a PID-on-curvature controller; keep behavior simple with two modes (curve, then straight) and one threshold.
- The curve-vs-straight decision is recomputed every wheel increment, not once per waypoint.
- `theta_gap = angle(global_vector) - heading`. Positive means turn one way, negative the other (handled via `flip`).
- `span` is user-tunable: too large and you drive sloppily past the point; too small and you oscillate, especially near the target where small position errors map to large angular errors.
- Closer to the target, the same lateral error produces a larger angular deviation, so practically you also need to slow down to use a smaller span.
- The curve command flowing out is `curve_speed = curve_rate * flip`, packaged into a chassis-speed command and handed to the per-wheel PID controllers via the kinematics.

## Techniques demonstrated

- Threshold-based switching between curve and straight phases instead of continuous curvature control.
- Sign management with a `flip` variable to pick turn direction.
- Reasoning about how span tolerance interacts with proximity and speed to avoid overshoot.

## Tools used

- Tablet sketching for the heading/global-vector geometry.

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE]] — driving software.

## People mentioned

- [[entities/people/david-malawey|David Malawey]].

## Related videos

- [[videos/navigationvectors-part1-global-position-increment|NavigationVectors part 1: global position increment]] — provides the position and heading state this part consumes.
- [[videos/scuttle-robot-how-the-magnetometer-sensor-compass-works|SCUTTLE Robot - How the Magnetometer Sensor (compass) works]] — the heading source.
