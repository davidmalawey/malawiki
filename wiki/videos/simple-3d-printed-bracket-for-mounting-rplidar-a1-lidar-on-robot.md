---
type: video
title: "Simple 3D Printed Bracket for Mounting RPLIDAR A1 Lidar on Robot"
video_id: "vRt7o7RDvvk"
url: "https://www.youtube.com/watch?v=vRt7o7RDvvk"
published: 2021-12-02
duration: "3:00"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, lidar, 3d-printing, bracket, extrusion]
ingested: 2026-05-02
---

## Overview

David shares v1 of his 3D-printed bracket for the Slamtec RPLIDAR A1 mounted on SCUTTLE's [[entities/tools/3030-extrusion|30x30 aluminum extrusion]]. The bracket holds the LIDAR with four M2.5x6 screws, supports two mount-styles (a quick "twist dovetail" and a more secure M6 T-slot mount), and is published on GrabCAD for anyone using 30 mm extrusion-based robots.

## Key takeaways

- LIDAR is held by four M2.5 x 6 mm screws; same screw size used elsewhere on SCUTTLE so it shares the parts kit.
- Two mount options: a twist-dovetail (quick and dirty) and slide-in T-slot M6 nuts (more secure).
- A small alignment feature on the underside helps the bracket sit flat on the extrusion when bolted; for the dovetail mount, that feature must be trimmed off with a knife to clear the slot.
- The dovetail's "snap" gives roughly +/- 1 degree of yaw alignment without the trimming step.
- Designed for SCUTTLE but portable — works on any 30 mm aluminum-extrusion robot frame.
- CAD published on GrabCAD: "slamtec-rplidar-with-bracket-for-3030-extrusion".

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] — bracket reuses screws already in robot's BOM
- [[concepts/standardize-mounting-interfaces|Standardize mounting interfaces]] (30 mm extrusion as common rail)
- [[concepts/print-direction|Print direction]] / support material trimming
- [[concepts/open-source-hardware-publishing|Open source hardware publishing]] (GrabCAD release)

## Tools used

- [[entities/tools/rplidar-a1|RPLIDAR A1]]
- [[entities/tools/3030-extrusion|30x30 aluminum extrusion]]
- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/utility-knife|Utility knife]]
- [[entities/tools/t-slot-nut|T-slot nut]]
- [[entities/tools/twist-dovetail-bracket|Twist dovetail bracket]]
- [[entities/brands/grabcad|GrabCAD]]
- [[entities/brands/slamtec|Slamtec]]

## Materials used

- [[entities/materials/pla|PLA]] (typical SCUTTLE print material)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]
- [[entities/projects/rplidar-bracket|RPLIDAR Bracket]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/aluminum-extrusions-fundamentals]]
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
