---
type: video
title: "SCUTTLE Robot - Servo Arm Design V1 Overview (using PVC, 3D prints, and low cost parts)"
video_id: "Tq0Sddyiaes"
url: "https://www.youtube.com/watch?v=Tq0Sddyiaes"
published: 2019-10-26
duration: "9:45"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, servo, robot-arm, 3d-printing, pvc, cad, grabcad]
ingested: 2026-05-02
---

## Overview

CAD walkthrough of a low-cost two-joint servo arm for the [[entities/projects/scuttle-robot|SCUTTLE robot]] — built from hobby servos, [[entities/materials/pvc|PVC pipe]], 3D-printed brackets, skateboard 608 ball bearings, and a hockey-puck counterweight. STL files live on GitHub at MXET/SCUTTLE; the CAD model is published on [[entities/brands/grabcad|GrabCAD]] as `servoArm-v1.1`.

## Key takeaways

- Base bracket bolts to a [[entities/tools/3030-extrusion|30x30 mm aluminum extrusion]] with four M-screws; even two bolts are enough to start testing.
- Tower is 1.5" CPVC (gray); cap is a 3D-printed part glued on with PVC cement or super glue.
- Green servo bracket has intentional sidewall slop to absorb hobby-servo dimensional variance.
- 608 skateboard ball bearing snaps into the green bracket via three compression nubs on the inner race; the same bearing is reused on the SCUTTLE drive wheels.
- Purple part snaps onto the bearing's outer race; centering is done by hand once the servo is at its zero-degree position.
- The same green/blue/purple parts repeat at the second joint — flipped upside-down — for design commonality.
- Joint-to-joint distance is 150 mm by default for clean kinematics math.
- Counterweight bracket holds a standard 172 g hockey puck; you can stack 1-4 pucks for heavier payloads.
- Range of motion slightly exceeds 180°, matching most hobby servos.
- Servo cable routes through a channel in the bracket and down the inside of the PVC tube to keep it clear of the joint sweep.

## Techniques demonstrated

- [[concepts/design-commonization]]
- [[concepts/snap-fit-bearing-mount]]
- [[concepts/counterweight-design]]
- [[concepts/cable-routing-through-structure]]
- [[concepts/print-direction]]
- [[concepts/design-for-3d-printing]]

## Tools used

- [[entities/tools/3030-extrusion|30x30 mm aluminum extrusion]]
- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/hobby-servo]]
- [[entities/tools/ball-bearings|608 skateboard bearing]]
- [[entities/tools/servo-horn]]

## Materials used

- [[entities/materials/pvc|CPVC 1.5" pipe]]
- [[entities/materials/pvc|PVC 3/4" pipe]]
- [[entities/materials/pla|3D-print plastic (PLA)]]
- [[entities/materials/pvc-cement|PVC glue]]
- [[entities/materials/super-glue|super glue]]
- Hockey puck (172 g, standard)

## Projects

- [[entities/projects/scuttle-servo-arm-v1]]
- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-press-in-wheel-bearings-and-glue-pulleys]]
- Other [[series/scuttle-tutorials-2019]] tutorials.
