---
type: video
title: "SCUTTLE Robot - Hardware List (Fasteners, Screws, Nuts, Washers)"
video_id: "7ktPjW8NAww"
url: "https://www.youtube.com/watch?v=7ktPjW8NAww"
published: 2020-11-23
duration: "3:15"
tags: [scuttle, hardware, fasteners, bom, screws, t-slot, heat-set-insert]
ingested: 2026-05-02
---

## Overview

A complete walkthrough of every fastener on the SCUTTLE v2.3 robot: David lays each screw size on the bench, names its quantity, and points to where it goes on the assembly. Treat this as the canonical fastener BOM for the design as of late 2020.

## Key takeaways

- M2 x 6mm self-tapping (qty 3): two hold each encoder PCB to the wheel bracket, one holds the CPU.
- M2.5 brass heat-set inserts (qty 10): four on each wheel bracket for the encoder, two on motor-driver brackets, two in the battery pack assembly.
- M2.5 x 6mm pan head (qty 4): two secure the motor driver to the bracket; two spares.
- M2.5 x 10mm countersunk (qty 8): two per motor-driver bracket; four in the battery assembly (two top, two bottom).
- M3 x 10mm countersunk (qty 6): three per motor (two motors).
- M6 x 10mm Phillips pan head with expanded head (qty 20): replaces a washer; secures parts to the aluminum extrusion rails (4 per location, 5 locations including casters).
- M6 T-slot drop-in nuts (qty 20): partner to each M6 — improvement over earlier hammer/sliding nuts because they don't require pre-planning the build order.
- M8 x 110mm machine screw (qty 2, axles): each with two flat washers, one lock washer, one nut. Functions as the wheel axle; one flat washer protects the bearing.

## Techniques demonstrated

- [[concepts/heat-set-insert-installation|heat-set insert installation]] (referenced via the M2.5 brass inserts)
- [[concepts/standardize-mounting-interfaces|standardize mounting interfaces]] (M6 + T-slot pattern across the chassis)
- [[concepts/locally-sourced-bom|locally-sourced BOM]]

## Tools used

- [[entities/tools/threaded-insert|threaded insert]] (M2.5 brass heat-set)
- [[entities/tools/t-slot-nut|T-slot nut]] (M6 drop-in)
- [[entities/tools/2020-extrusion|2020 extrusion]] / [[entities/tools/3030-extrusion|3030 extrusion]] (the aluminum rails)
- [[entities/tools/ball-bearings|ball bearings]] (protected by the M8 axle washers)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (v2.3)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:18 M2 x 6mm self-tapping
- 0:34 M2.5 heat-set inserts
- 1:02 M2.5 x 6mm pan head
- 1:16 M2.5 x 10mm countersunk
- 1:37 M3 x 10mm countersunk
- 1:47 M6 x 10mm pan head (broad head replaces washer)
- 2:15 M6 T-slot drop-in nuts (improvement over slide-in)
- 2:43 M8 x 110mm axle assembly with washers + lock washer + nut

## Related videos

- [[scuttle-robot-cad-revisions-watch-before-downloading-stl-files]]
- [[scuttle-robot-press-in-wheel-bearings-and-glue-pulleys]]
- [[scuttle-robot-v3-0-assembly-animated]]
- [[build-a-payload-robot-start-to-finish-scuttle-v2-4]]
- [[what-screws-to-use-in-your-3d-print]]
- [[tapping-threads-in-extrusion-for-beginners]]
