---
type: video
title: "Scuttle Robot - Modifying the Wheel Pulley in Solidworks"
video_id: "8o-XcZ3_teM"
url: "https://www.youtube.com/watch?v=8o-XcZ3_teM"
published: 2019-02-05
duration: "6:15"
series: "[[series/scuttle-v1-build]]"
tags: [scuttle, solidworks, wheel-pulley, parametric, customization, grabcad]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] walks through customizing the [[entities/tools/wheel-pulley|SCUTTLE wheel pulley]] in [[entities/brands/solidworks|SolidWorks]] for a non-standard skateboard wheel. He downloads the part from [[entities/brands/grabcad|GrabCAD]], uses Convert Entities to project a face into a sketch, builds an angled triangular cut constrained by a centerline-to-point relation, then circular-patterns the cut to all three arms. The walkthrough is a representative example of using parametric SolidWorks to adapt a published part to local hardware.

## Key takeaways

- Pulley is downloaded from [[entities/brands/github|GitHub]] (CAD/SolidWorks designs/wheel pulley v1) and opened in SolidWorks - skip Feature Recognition for this edit.
- Goal: narrow each arm to fit between the spokes of a non-standard skateboard wheel.
- Workflow: right-click face -> Sketch -> Ctrl+8 to view normal -> Convert Entities to project the boundary line.
- Build a centerline from corner to corner, then constrain a sketch point to the intersection of the two trim lines so left and right are trimmed equally.
- Use Make Equal between the two trim lines as the symmetry constraint - all sketch entities turn black (fully defined) when correct.
- Smart Dimension is intentionally exited (Escape) so the equality constraint is added cleanly.
- Trim the middle line so the sketch closes into two triangle regions.
- Extrude Cut from the sketch plane to the opposite surface, with both contours selected.
- Circular Pattern around a cylindrical wall (auto-detected as axis), 360 degrees, 3 instances - applies the cut to all three arms in one feature.
- Save as solid (e.g., v1.2) then export STL. STL is archived geometry - keep the solid file as the source of truth.
- Imprinting [[concepts/version-marking|version numbers]] on the part is the safer way to keep track of which print is which.

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]]
- [[concepts/cad-configurations|CAD configurations]]
- [[concepts/constraint-driven-sketching|Constraint-driven sketching]]
- [[concepts/convert-entities|Convert entities (project geometry into sketch)]]
- [[concepts/circular-pattern|Circular pattern]]
- [[concepts/version-marking|Version marking]]
- [[concepts/feature-tree-naming|Feature tree naming]]
- [[concepts/print-direction|Print direction]]
- [[concepts/manual-feature-recognition|Manual feature recognition]]

## Tools used

- [[entities/brands/solidworks|SolidWorks]]
- [[entities/tools/wheel-pulley|Wheel pulley (v1)]]
- [[entities/tools/3d-printer|3D printer]]

## Materials used

- [[entities/materials/abs|ABS]]

## Brands

- [[entities/brands/grabcad|GrabCAD]]
- [[entities/brands/github|GitHub]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-gluing-the-wheel-pulleys-version-1-0]]
- [[videos/scuttle-robot-assembling-wheels-and-belt]]
- [[videos/solidworks-2019-create-configurations-with-various-pattern-instances]]
- [[videos/solidworks-recognize-features-manually-tutorial-with-example]]
- [[videos/how-to-deboss-a-dynamic-revision-number-for-3d-prints-solidworks]]
- [[videos/scuttle-robot-cad-revisions-watch-before-downloading-stl-files]]
- [[videos/what-is-a-parametric-design-with-solidworks-example]]
