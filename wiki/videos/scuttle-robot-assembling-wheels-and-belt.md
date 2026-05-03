---
type: video
title: "Scuttle Robot - assembling wheels and belt"
video_id: "BN1E99_LWlo"
url: "https://www.youtube.com/watch?v=BN1E99_LWlo"
published: 2019-02-07
duration: "3:17"
series: "[[series/scuttle-v1-build]]"
tags: [scuttle, wheel-assembly, htd5-belt, axle-bolt, alignment]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] demonstrates the easiest sequence to install a [[entities/projects/scuttle-robot|SCUTTLE]] wheel + [[entities/tools/htd5-belt|belt]] assembly onto the v1 machined-aluminum chassis. The trick is to thread the axle bolt through one plate just enough to catch the assembly, hang the belt on the motor pulley first, slip the wheel pulley in next, then gently advance the bolt across to the second plate. Misalignment between plates is diagnosed by feel during the second-plate pass.

## Key takeaways

- Chassis context: this is the older [[entities/materials/aluminum|machined aluminum]] plate version; the newer [[entities/projects/scuttle-robot|v2.2.1]] uses 3D-printed wheel assemblies.
- Wheel sub-assembly: bearing - spacer (chamfer facing in) - bearing on a single bolt. Once threaded, never fully remove the bolt again.
- Hang the [[entities/tools/htd5-belt|belt]] on the motor pulley first to avoid fighting tension.
- Push the assembly close to the motor pulley so the belt has slack, expose the bolt's first thread on the rear pulley side, then insert into plate 1.
- If the bolt fights plate 2, that means plates are misaligned - loosen the plate-to-plate bolts and swing the plate until the axle clears.
- A [[entities/tools/lock-washer|split lock washer]] goes under the nut. Hand-tight is enough; no real wrench or ratchet needed.
- Removal is the reverse: loosen by hand, slide the bolt back just enough to catch the wheel, then slide the assembly toward the motor pulley so the belt unloads.
- The reason for sliding rather than flexing: bending the wheel along the axis to free the belt can crack the plastic pulley off the wheel.

## Techniques demonstrated

- [[concepts/three-point-clamping|Three-point clamping]]
- [[concepts/borrowing-tolerances|Borrowing tolerances]]
- [[concepts/symptom-watch|Symptom watch]] (binding on plate 2 -> diagnose plate misalignment)
- [[concepts/datasheet-vs-real-world-fit|Datasheet vs real-world fit]]
- [[concepts/assembly-sequencing|Assembly sequencing]]
- [[concepts/torque-evaluation-on-assembled-fastener|Torque evaluation on assembled fastener]]

## Tools used

- [[entities/tools/htd5-belt|HTD5 belt]]
- [[entities/tools/wheel-pulley|Wheel pulley]]
- [[entities/tools/ball-bearings|Ball bearings]]
- [[entities/tools/lock-washer|Lock washer (split)]]
- [[entities/tools/axle-bolt|Axle bolt]]

## Materials used

- [[entities/materials/aluminum|Aluminum (chassis plates)]]
- [[entities/materials/abs|ABS (printed pulleys)]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-gluing-the-wheel-pulleys-version-1-0]]
- [[videos/scuttle-robot-modifying-the-wheel-pulley-in-solidworks]]
- [[videos/scuttle-robot-press-in-wheel-bearings-and-glue-pulleys]]
- [[videos/scuttle-robot-insert-the-bearings-in-new-wheels]]
- [[videos/scuttle-robot-hardware-list-fasteners-screws-nuts-washers]]
- [[videos/build-a-payload-robot-start-to-finish-scuttle-v2-4]]
