---
type: video
title: "Exoskeleton Design & Control of Fastener Torque"
video_id: "khiMEj0_Yjo"
url: "https://www.youtube.com/watch?v=khiMEj0_Yjo"
published: 2026-02-13
duration: "23:21"
tags: [exoskeleton, robotics, controls, harmonic-drive, torque-wrench, fastener, texas-am, scuttle, lab-tour]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] visits Dr. Reza Langari's lab at [[entities/places/texas-am-lab|Texas A&M]] and meets two PhD students — [[entities/people/ibraheem|Ibraheem]] and [[entities/people/precious|Precious]] — who are developing an [[entities/projects/assist-as-needed-exoskeleton|assist-as-needed rehabilitation exoskeleton]]. After a tour of the rig (joint-level torque sensors, [[concepts/bio-signal-meter|bio-signal meters]] for muscle EMG, and a [[entities/tools/harmonic-drive|harmonic-drive]] gearbox close-up), David shifts to a how-to second half: how to use a [[entities/tools/torque-wrench|torque wrench]] and a [[entities/tools/handheld-torque-screwdriver|handheld torque screwdriver]] to evaluate the existing torque on a fastener in an already-assembled assembly.

## Key takeaways

- An "assist-as-needed" exoskeleton supplies the residual torque the patient can't produce themselves; bio-signal meters (EMG) plus joint torque sensors close the control loop.
- Every joint needs its own torque sensor; you confirm patient effort by the *lack* of patient-produced torque combined with the muscle signal.
- [[entities/tools/harmonic-drive|Harmonic-drive]] gearboxes give very high reduction with low backlash — appropriate for compliant exoskeleton joints.
- To evaluate torque on an installed fastener: slowly increase torque on a calibrated wrench until the fastener just begins to move; that breakaway value is a lower-bound estimate of the original torque (slightly under, because static friction was already overcome).
- A handheld torque screwdriver (slip-clutch style) is the right tool for small-screw-spec checks; a beam or click torque wrench covers larger fasteners.
- The [[entities/projects/scuttle-robot|SCUTTLE]] connection: Precious previously worked on Scuttle Lab Nigeria in Aeri.

## Techniques demonstrated

- [[concepts/torque-evaluation-on-assembled-fastener|Torque evaluation on an already-assembled fastener]] (breakaway method)
- [[concepts/screw-as-spring|Screw as spring]] — review of why fastener torque equals stored preload
- Use of a slip-clutch [[entities/tools/handheld-torque-screwdriver|torque screwdriver]] for small-screw specs

## Tools used

- [[entities/tools/torque-wrench|Torque wrench]]
- [[entities/tools/handheld-torque-screwdriver|Handheld torque screwdriver]]
- [[entities/tools/harmonic-drive|Harmonic drive]] (gearbox)
- [[entities/tools/emg-sensor|EMG / bio-signal meter]]

## Projects

- [[entities/projects/assist-as-needed-exoskeleton|Assist-as-needed rehabilitation exoskeleton]] (Langari lab, Texas A&M)
- [[entities/projects/scuttle-robot|SCUTTLE]] — referenced via Scuttle Lab Nigeria

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- [[entities/people/reza-langari|Dr. Reza Langari]] — David's former adviser, exoskeleton lab PI
- [[entities/people/ibraheem|Ibraheem]] — mechanical engineering PhD student, controls
- [[entities/people/precious|Precious]] — mechanical engineering PhD student from Nigeria, controls; previously worked on Scuttle Lab Nigeria

## Places mentioned

- [[entities/places/texas-am-lab|Texas A&M lab]] (Dr. Langari's lab)
- [[entities/places/aeri-nigeria|Aeri, Nigeria]] (Scuttle Lab Nigeria site)

## Related videos

- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]] — earlier discussion of [[concepts/screw-as-spring|screw as spring]] and fastener load.
