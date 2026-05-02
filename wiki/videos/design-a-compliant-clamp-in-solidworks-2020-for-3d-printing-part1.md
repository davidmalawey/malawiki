---
type: video
title: "Design a compliant clamp in Solidworks 2020 for 3D Printing (part1)"
video_id: "VyrneksJNfw"
url: "https://www.youtube.com/watch?v=VyrneksJNfw"
published: 2020-10-16
duration: "19:57"
tags: [solidworks, cad, 3d-printing, compliance, clamp, scuttle, conveyor, tutorial]
ingested: 2026-05-02
---

## Overview

David walks through the SolidWorks 2020 design process for a single-piece compliant clamp that grips a 3030 aluminum extrusion on the [[entities/projects/scuttle-conveyor|SCUTTLE conveyor]]. He thinks out loud about printability, fastener commonization, wall thickness minimums, stress relief fillets, heat-set insert seating, and the iteration plan: print, test, then refine.

## Key takeaways

- A monolithic compliant clamp replaces a typical multi-part T-slot clamping kit — the web is designed to bend and curl under screw tension instead of having a separate moving piece.
- Standardize on M6 hardware across the assembly so only one screw size needs to be stocked — example of [[concepts/parts-ecosystem-design|parts ecosystem design]].
- Wall thicknesses: 3.5 mm minimum for structural [[entities/materials/abs|ABS]] walls, 1.5 mm minimum for shoulders, 2.5 mm for the compliant outer web.
- Counter-bore screw heads to keep them flush — preserves room to add features later and keeps overall envelope minimal.
- Fillets on outside corners save material and improve printer adhesion; inside fillets help relieve stress concentration even when loads are well below limits.
- Heat-set insert seating is gravity-friendly here — screw tension wants to push the insert deeper, opposite of the typical pull-out failure mode.
- Design strategy: nail the first sketch's primary dimensions, then physically print and iterate — don't try to simulate every interaction.
- 6 mm holes are near the upper printable limit without supports; 3 mm always works.

## Techniques demonstrated

- [[concepts/compliance-clamping|compliance clamping]]
- [[concepts/design-for-3d-printing|design for 3D printing]]
- [[concepts/parametric-design|parametric design]]
- [[concepts/feature-tree-naming|feature tree naming]]
- [[concepts/constraint-driven-sketching|constraint-driven sketching]]
- [[concepts/heat-set-insert-installation|heat-set insert installation]]
- [[concepts/working-placeholder-design|working placeholder design]]
- [[concepts/parts-ecosystem-design|parts ecosystem design]]

## Tools used

- [[entities/brands/solidworks|SolidWorks 2020]]
- [[entities/tools/threaded-insert|threaded insert]] (M6 brass, 9 mm OD)
- [[entities/tools/3d-printer|3D printer]]

## Materials used

- [[entities/materials/abs|ABS]]
- [[entities/materials/aluminum|aluminum]] (3030 extrusion)
- [[entities/materials/nylon|nylon]] (existing slide pad)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- [[entities/projects/scuttle-conveyor|SCUTTLE conveyor]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Brands

- [[entities/brands/solidworks|SolidWorks]]

## Notable quotes / timestamps

- 1:14 Design overview
- 4:00 Sketch dimensions
- 10:25 Assembly check

## Related videos

- [[videos/flashforge-creator-pro2-setup-first-print-in-4k-resolution]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
- [[videos/tutorial-modeling-and-mindset-for-a-parametric-bracket-solidworks]]
- [[videos/what-is-a-parametric-design-with-solidworks-example]]
- [[videos/what-screws-to-use-in-your-3d-print]]
