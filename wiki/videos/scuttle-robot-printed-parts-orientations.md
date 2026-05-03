---
type: video
title: "Scuttle Robot - Printed Parts & Orientations"
video_id: "PXD6mWnY9d0"
url: "https://www.youtube.com/watch?v=PXD6mWnY9d0"
published: 2019-01-16
duration: "10:57"
series: "[[scuttle-bench-build-kickoff]]"
tags: [scuttle, 3d-printing, abs, print-orientation, fdm, design-for-manufacturing]
ingested: 2026-05-02
---

## Overview

Walks through every 3D-printed part on the [[entities/projects/scuttle-robot|SCUTTLE]] robot (v2.2.1) and the intended print orientation for each. Goal: keep all overhangs above 45 degrees so most parts print in [[entities/materials/abs|ABS]] on a [[entities/tools/flashforge-creator-pro|Flashforge Creator Pro]]-class machine without supports.

## Key takeaways

- Most SCUTTLE plastic parts print support-free if you put the correct face down. Two parts (the [[entities/tools/scuttle-universal-bracket|universal bracket]] and the universal dovetail) require supports because critical t-slot tolerances trump no-support design.
- Test-printed in ABS at **0.3 mm layer thickness** as the coarsest acceptable setting. Finer is fine; coarser is not recommended.
- **Drivetrain spacers:** only one of the two spacers has a chamfer; the chamfer must be printed pointing up so the chamfered face mates the inner race of the wheel bearing.
- **Pulleys** print without supports despite a small overhang on the underside flange - the resulting roughness doesn't interfere with the [[entities/tools/htd5-belt|HTD5 belt]].
- **Encoder brackets** (left and right) are physically identical; you choose which two of the four mounting holes to use depending on which side of the robot the bracket goes on. This is a [[concepts/symmetric-not-identical|symmetric-not-identical]] design pattern.
- **Universal bracket:** supports are placed with ~1.5 mm spacing on the bottom edge to maintain the t-slot mating profile.

## Techniques demonstrated

- [[concepts/print-direction|Print direction]]
- [[concepts/design-for-3d-printing|Design for 3D printing]]
- [[concepts/symmetric-not-identical|Symmetric not identical]]
- [[concepts/45-degree-overhang-rule|45-degree overhang rule]]
- [[concepts/standardize-mounting-interfaces|Standardize mounting interfaces]] (universal dovetail)

## Tools used

- [[entities/tools/flashforge-creator-pro|Flashforge Creator Pro]]
- [[entities/tools/simplify-3d|Simplify3D]]
- [[entities/brands/solidworks|SolidWorks]] (for cross-section and CAD)

## Materials used

- [[entities/materials/abs|ABS]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## Parts catalogued

- Motor driver bracket
- Battery pack case and lid
- BeagleBoard PCB bracket and cover
- Ultrasonic sensor bracket
- Compass sensor bracket
- Camera bracket cup
- Right-hand and left-hand encoder brackets (identical part, different hole pairs)
- Universal bracket and rod-holding bracket
- Universal dovetail
- Drivetrain spacers (chamfered and unchamfered)
- Motor pulley and wheel pulley

## Related videos

- [[scuttle-robot-hardware-overview]]
- [[scuttle-robot-cad-revisions-watch-before-downloading-stl-files]]
- [[scuttle-robot-ready-designs-for-easy-3d-printable-attachments]]
