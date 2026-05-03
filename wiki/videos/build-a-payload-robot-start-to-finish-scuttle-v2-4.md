---
type: video
title: "Build a payload robot start to finish! - SCUTTLE v2.4"
video_id: "jQu5wtPSW_U"
url: "https://www.youtube.com/watch?v=jQu5wtPSW_U"
published: 2022-10-31
duration: "42:38"
series: "[[scuttle-robot]]"
tags: [scuttle, build-tutorial, assembly, mechatronics, encoders, motor-driver, i2c]
ingested: 2026-05-02
---

## Overview

A 42-minute uncut bench build of a SCUTTLE v2.4 robot from off-the-shelf parts and 3D prints. David walks through the full mechanical assembly — chassis extrusions, wheel brackets, axles, motors, drive rods, encoders, and the i2c board — narrating tolerances, screw choices, and right/left symmetry along the way. All CAD is open source at scuttlerobot.org. This is camera 1 of 2 (42 of 70 minutes); a second-camera version covers the rest.

## Key takeaways

- SCUTTLE uses two extrusion-nut styles: drop-in nuts on the corner aluminum brackets (M6) and slide-in nuts on the wheel brackets — the choice affects whether you assemble with the bracket on or off.
- Tighten in passes: snug everything to "stays steady" first, then torque only at the end so parts can find their resting position. Most fasteners on this robot are finger-force, not wrist-force.
- The robot is symmetric, not identical, between left and right — pay attention when populating the caster, motor, and encoder brackets so screws end up in mirrored holes rather than identical ones.
- Right-hand motor cable is longer than left because the motor driver lives on the driver's (left) side; mark motors L and R.
- Six total M3 countersunk screws on the build — they're the only larger-diameter "fine" screws in the kit, easy to identify by sight.
- Encoder magnet is a strong neodymium that will jump to anything steel; keep it bagged until you're ready to press it onto the motor pulley shelf.
- Pulleys press onto the motor D-shaft with finger force — if you need pectoral force, swap the pulley (it's out of tolerance).
- v2.4 uses 1/2-inch aluminum tube rods. The roadmap is to migrate to [[entities/tools/din-rail|DIN rail]] in the next version.
- The i2c board uses M2 self-tapping screws into plastic — only assemble/disassemble a few times before the hole wears out.

## Techniques demonstrated

- [[concepts/aluminum-extrusion-wiring|Aluminum extrusion]] T-slot assembly (drop-in vs. slide-in nuts)
- [[concepts/torque-evaluation-on-assembled-fastener|Torque evaluation on assembled fastener]] (finger-force vs. wrist-force)
- [[concepts/version-marking|Version marking]] (1.5R / 1.5L on bracket prints)
- [[concepts/symmetric-not-identical|Symmetric not identical]] design language
- [[concepts/press-fit|Press fit]] (motor pulley to D-shaft)
- [[concepts/modularity|Modularity]] (most subassemblies removable in one step)

## Tools used

- [[entities/tools/3030-extrusion|30x30 aluminum extrusion]]
- [[entities/tools/dc-gearmotor|DC gearmotor]]
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver]]
- [[entities/tools/ball-bearings|Ball bearings]] (wheel hubs)
- [[entities/tools/cordless-drill|Cordless drill / electric driver]] (USB-charged)
- Magnetic parts bin (small-screw containment)
- Phillips #1 / #0 screwdrivers, 1.5mm Allen key

## Materials used

- [[entities/materials/pla|PLA]] (printed brackets, spacers, encoder mounts)
- [[entities/materials/aluminum|Aluminum]] (extrusion + half-inch rods)
- Neodymium magnets (encoder)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (v2.4)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [17:22] Torque is divided into "finger force" or "hand wrist force" — never specified beyond that for a hobby kit.
- [25:13] Rod brackets are "identical rather than symmetric — that's to save the number of designs we issue and people have to keep track of."
- [35:13] "If you need to use your pectorals to push this together, then you need to swap that out" — pulley press-fit feel test.

## Related videos

- [[videos/build-a-deck-for-cargo-bins]]
- [[videos/loads-of-stuff-you-can-add-to-a-12v-robot]]
- [[videos/aluminum-extrusions-fundamentals]]
- [[videos/mechanical-design-tutorial-for-a-hub]]
