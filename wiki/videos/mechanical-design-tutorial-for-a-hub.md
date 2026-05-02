---
type: video
title: "Mechanical Design Tutorial for a Hub"
video_id: "QnAuQ8QLtgs"
url: "https://www.youtube.com/watch?v=QnAuQ8QLtgs"
published: 2025-09-17
duration: "20:58"
tags: [mechanical-design, cad, parametric-design, 3d-printing, tutorial, hub, bearing]
ingested: 2026-05-02
---

## Overview

David walks through designing "Hub Zero," a 3D-printed bearing hub, by reframing mechanical design as a finite list of discrete questions, each answered by a benchmark, a standard, or a measurement of mating parts. The tutorial deliberately strips out experience-based intuition so that learners from electronics or software backgrounds can produce sturdy mechanical parts. He arrives at a part nearly identical to the freehand "Hub One" he produced in 15 minutes — evidence that the questioning method captures what experienced designers do implicitly.

## Key takeaways

- Mechanical design can be decomposed into ~9 discrete questions, ~10 numeric values, and 3 sources of solutions (benchmarks, standards, mating parts).
- For each design feature, map every numeric choice back to its origin so the model carries design intent.
- Symmetry around a rotation axis drives geometry choices — bolt circles over Cartesian patterns when the function is rotation.
- 4 mm flange thickness comes from benchmarking similar plastic ABS parts under load; standard range is 4–6 mm.
- For 3D-printed bearing pockets, 1 mm diametral clearance avoids interference; three contact pads at ~5 mm width provide adjustable clamping force linearly tied to pad width.
- When mating to a less-controlled stamped-steel part, use a smaller screw (M5 vs. M6) so the tighter-toleranced part dictates assembly geometry.
- Name sketches and features in CAD as you would comment code — design intent must survive 5 years of memory loss.

## Techniques demonstrated

- [[concepts/borrowing-tolerances|borrowing tolerances]] from mating parts and reference benchmarks
- [[concepts/parametric-design|parametric design]] — single-variable changes propagate through the model
- [[concepts/benchmarking-design|benchmarking design]] — extracting dimensions from reliable existing parts
- [[concepts/design-by-questions|design by questions]] — converting design steps into discrete answerable questions
- [[concepts/three-point-clamping|three-point clamping]] for round stock retention
- Chamfering edges on FDM prints for free aesthetic and easier bed release

## Tools used

- [[entities/brands/solidworks|SolidWorks]] (CAD with sketches, revolves, extrude cuts, patterns)
- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/ball-bearings|ball bearings]] (22 mm OD, 8 mm ID, 8 mm height)
- [[entities/tools/calipers|calipers]]

## Materials used

- [[entities/materials/abs|ABS]] or similar plastic (3D-printed hub body)

## Projects

- [[entities/projects/hub-zero|Hub Zero]] — open-source bearing hub published on [[entities/brands/grabcad|GrabCAD]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- (Earlier hub-related and SCUTTLE robot videos in the channel)
