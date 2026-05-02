---
type: video
title: "SCUTTLE Robot - Ready Designs for Easy 3D Printable Attachments"
video_id: "JH5nNZ1AVIs"
url: "https://www.youtube.com/watch?v=JH5nNZ1AVIs"
published: 2019-11-15
duration: "5:40"
series: "[[series/scuttle-robot]]"
tags: [scuttle, 3d-printing, brackets, servo, parametric, modularity]
ingested: 2026-05-02
---

## Overview

Tour of six pre-designed 3D printable brackets that recombine into custom servo joints, camera pivots, and end-effector mounts for the [[entities/projects/scuttle-robot|SCUTTLE robot]]. Hobby servos are used because they are cheap, off-the-shelf, and the [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] can drive up to 8 of them directly.

## Key takeaways

- Servo Hub Assembly: a U-bracket holds a hobby servo with four screws; a round servo horn (M2 coarse screws) couples to a printed output bracket; a skateboard bearing on the back supports moments on the output.
- Cord routing voids are built into the brackets so servo wires can pass through cleanly.
- A "friction pivot" can be sliced (boss-extrude rectangle, then split) and bonded with super glue or PVC glue to combine with other brackets.
- Camera pivot variant flexes around a USB camera, with a 90 degree twist option for two-axis rotation.
- Six base components recombine for ultrasonic, IR temp sensors, or any custom payload — add a flat boss with screw holes when in doubt.
- PVC adapter variant couples the bracket to a PVC pipe to extend reach.

## Tools and components

- Hobby servos (off-the-shelf, ~8 max on BeagleBone Blue)
- Servo horn + M2 coarse screws
- Skateboard bearing (off-the-shelf)
- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/beaglebone-y-ai|BeagleBone Blue]]

## Materials used

- [[entities/materials/abs|ABS]] / [[entities/materials/pla|PLA]] (printable brackets)
- [[entities/materials/super-glue|Super glue]] or [[entities/materials/pvc-cement|PVC cement]] (sliced-part bonding)
- [[entities/materials/pvc|PVC]] pipe (extension adapter)

## Concepts demonstrated

- [[concepts/modularity]]
- [[concepts/parametric-design]]
- [[concepts/design-for-3d-printing]]
- [[concepts/parts-ecosystem-design]]
- [[concepts/standardize-mounting-interfaces]]

## Related videos

- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
