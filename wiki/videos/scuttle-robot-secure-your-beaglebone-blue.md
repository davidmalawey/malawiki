---
type: video
title: "Scuttle Robot - secure your beaglebone blue"
video_id: "X2x7R6xTDok"
url: "https://www.youtube.com/watch?v=X2x7R6xTDok"
published: 2019-02-26
duration: "1:38"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, beaglebone, fastening, assembly, mechatronics]
ingested: 2026-05-02
---

## Overview

David shows a quick fastening trick for mounting the [[entities/tools/beaglebone-blue|BeagleBone Blue]] to its 3D-printed case using silver screws and a homemade compressible orange sleeve spacer. The sleeve takes up unused thread length, prevents the screw from slipping off the board during install, and provides a touch of springiness so the board is not held rigidly.

## Key takeaways

- Cut the orange sleeve to roughly half the screw length to act as a custom spacer that absorbs unused threads.
- Pre-thread the sleeve onto the screw so it stays put when handling — the small bit of compression engages the plastic without overconstraining the board.
- Listen for a "tapping" sound while seating the screw — it indicates a remaining gap between board and case; tighten until the sound disappears.
- Never perform this install with the BeagleBoard powered on — a dropped screw can short contacts.

## Techniques demonstrated

- [[concepts/screw-as-spring|screw-as-spring]] — using a compressible sleeve so the fastener clamps without rigidly constraining the PCB.
- [[concepts/clip-before-power-rule|clip-before-power-rule]] — never assemble or fasten on a live board.
- [[concepts/symptom-watch|symptom-watch]] — listening for the tapping sound as a gap indicator.

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/sleeve|orange sleeve]] (used as compressible spacer)
- screws (silver self-tapping)
- scissors / [[entities/tools/flush-cutters|clippers]]

## Materials used

- 3D-printed plastic BeagleBone case
- orange rubber/silicone sleeve material

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-control-gpio-outputs-on-the-beaglebone-blue-with-led-demo]]
- [[videos/scuttle-robot-check-boot-drive-space-in-debian-on-beaglebone-blue]]
- [[videos/scuttle-robot-demonstration-for-reading-gpio-input-on-beaglebone-blue-with-l1-gp]]
