---
type: video
title: "SCUTTLE robot hardware overview"
video_id: "wpSIqTLZpCg"
url: "https://www.youtube.com/watch?v=wpSIqTLZpCg"
published: 2019-01-17
duration: "9:36"
series: "[[scuttle-bench-build-kickoff]]"
tags: [scuttle, hardware, fasteners, screws, m6, m2-5, m3, hex-keys, t-slot-nut]
ingested: 2026-05-02
---

## Overview

Hardware tour of every screw, nut, washer, tab, and hex key on SCUTTLE v1.0. David lays out each fastener in turn, points to where it goes on the robot, and explains the measurement convention (countersunk: from top of head; pan-head: from bottom of head).

## Key takeaways

- **M2.5 x 10 mm countersunk** screws hold the battery case and the encoder bracket cover.
- **M2.5 x 12 mm pan-head** screws are long enough to pass through the BeagleBoard, the spacer, and into the plastic standoff designed into the bracket.
- **M2.5 x 6 mm pan-head** screws fasten the BeagleBoard lid and the motor driver. The driver is held by **two screws into M2.5 brass [[entities/tools/threaded-insert|heat-set inserts]]** with 3.4 mm depth.
- **M2 coarse-thread plastic-tapping screws** mount the encoder PCB (two per encoder, on the catty-corner pair) and the ultrasonic sensor.
- **M6 t-slot tabs (M6 nut tabs)** drop into the [[entities/tools/2020-extrusion|2020 extrusion]] grooves. Two black-style tabs come from the kit; alternative profile aluminum tabs from Amazon kits also fit but extend further outward and won't fit every location.
- **M6 x 10 mm bolts** for thin hardware (90-degree brackets, caster plates); **M6 x 14 mm bolts** for the thick acrylic/aluminum plate. Length is chosen so threads don't bottom out in the extrusion's inner wall.
- **M6 flat washers** spread the bolt force on the acrylic plate (newer versions are aluminum).
- **M3 countersunk Phillips screws** (3 per motor) flush-mount the gearmotor to the plate.
- **M8 axle bolt** runs through two skateboard-wheel [[entities/tools/ball-bearings|ball bearings]] separated by a steel spacer that prevents the bearings from being compressed against each other.
- **Hex-key color code:** blue = 2.5 mm (set screws), green = 4 mm (all M6 hardware), and a 6 mm hex fits the M8 axle bolt.

## Techniques demonstrated

- [[concepts/screw-measurement-conventions|Screw measurement conventions]] (countersunk vs pan-head)
- [[concepts/heat-set-insert-installation|Heat-set insert installation]]
- [[concepts/symmetric-not-identical|Symmetric not identical]]
- [[concepts/poka-yoke|Poka-yoke]] (color-coded hex keys)
- [[concepts/parts-library|Parts library]]

## Tools used

- [[entities/tools/scuttle-hardware-kit|SCUTTLE hardware kit]]
- [[entities/tools/hex-key-set|Hex-key set]] (2.5 mm, 4 mm, 6 mm)
- [[entities/tools/ratcheting-driver|Ratcheting hex driver]]
- [[entities/tools/threaded-insert|Threaded insert (M2.5)]]
- [[entities/tools/ball-bearings|Ball bearings]]
- [[entities/tools/2020-extrusion|2020 extrusion]]

## Materials used

- [[entities/materials/abs|ABS]]
- [[entities/materials/acrylic|Acrylic]]
- [[entities/materials/aluminum|Aluminum]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (v1.0)

## Related videos

- [[scuttle-robot-printed-parts-orientations]]
- [[scuttle-robot-hardware-list-fasteners-screws-nuts-washers]]
- [[scuttle-battery-pack-heat-set-inserts]]
