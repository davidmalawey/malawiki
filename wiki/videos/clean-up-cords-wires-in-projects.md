---
type: video
title: "Clean up cords & wires in projects (for prototype or product level)"
video_id: "31hwwpmNlCo"
url: "https://www.youtube.com/watch?v=31hwwpmNlCo"
published: 2024-09-27
duration: "58:39"
tags: [cable-management, wiring, prototyping, electromechanical, reference]
ingested: 2026-05-02
---

## Overview

A long, comprehensive reference on how to manage wires and cables in electronic / electromechanical projects — the boring topic David couldn't find covered anywhere else on YouTube. Spans from quick prototype zip-tying to product-level [[concepts/din-rail-wiring|DIN rail wiring]] and ribbon-style [[entities/tools/dupont-connector|Dupont]] cabling. He shares his own parametric printable [[entities/tools/cable-clip|cable clip]] (on [[entities/brands/grabcad|GrabCAD]]) and a printable Raspberry Pi pin cover.

## Key takeaways

- **Spiral wrap** is the unsung hero — bundles a variable-diameter group of wires neatly, lets you split mid-run to add a branch, more forgiving than [[entities/tools/loom|loom tubing]].
- **[[entities/tools/zip-tie|Zip ties]] are legitimate** for production use, but stop and learn the technique: tension matters (under = floppy, over = damaged insulation), flush-cutting takes practice, and the cable mark left after release tells you whether you over-tensioned.
- **Mounting zip ties** (the kind with a paddle base + adhesive or screw hole) replace single-purpose hardware in a huge fraction of cases.
- **Cable cuff** (and similar reusable cinches) are between zip ties and [[entities/tools/velcro-strap|Velcro]] — temporary, reusable.
- **Adhesive-backed mounts (often [[entities/brands/3m|3M]] adhesive)** are reliable on clean surfaces; double-check the substrate's compatibility (ties back to [[videos/how-to-choose-an-adhesive|adhesive selection]]).
- **[[entities/tools/cable-tray|Cable tray]]** for the lab: dedicate a tray under the bench, run trunk wires there, drop branches up to specific stations.
- **[[concepts/aluminum-extrusion-wiring|Aluminum 20×20 / 2020 extrusion]]** is the de-facto skeleton for student/maker projects — its T-slot is a built-in cable channel and mount surface. Use the channel both as the structural frame and the wire-routing chase.
- **[[concepts/din-rail-wiring|DIN rail]]** is the upgrade once you have multiple actuators / power supplies. There is essentially one universal size; brands and components are deeply standardized. David recommends [[entities/brands/automation-direct|Automation Direct]].
- **[[entities/tools/grommet|Grommets]]** wherever wires pass through sheet metal or 3D-printed panels — protects insulation from chafe.
- **Shortening cables** is worth doing for permanent installs; long coiled excess is unreliable and ugly. Keep it longer for prototypes.
- **[[entities/tools/dupont-connector|Dupont]] ribbon cables (ribbon-style not individual jumpers)** are far better for any 5+ wire run. Consider this default purchase.
- **Pin cover** (David's printable design) protects exposed Raspberry Pi GPIO from shorts.

## Techniques demonstrated

- Spiral-wrapping a bundle and splitting mid-run.
- Zip-tie tension calibration; flush-cutting safely without gouging insulation.
- Routing wires through 2020 extrusion T-slots.
- S-bend trick: deliberately wave excess length flat on a surface and zip-tie it down.
- Mounting using 3D-printed bases that include integrated zip-tie pass-throughs.
- Tinning Dupont jumper tips for cleaner crimps / terminal block connections.
- Heat-shrink + grommet combinations for wires entering enclosures.

## Tools / hardware

- [[entities/tools/zip-tie|zip ties]] (regular and mounting style)
- [[entities/tools/spiral-wrap|spiral wrap]]
- [[entities/tools/loom|loom tubing]]
- [[entities/tools/velcro-strap|Velcro cable straps]]
- [[entities/tools/cable-cuff|cable cuff]] (reusable)
- [[entities/tools/cable-clip|cable clip]] (David's parametric printable design on GrabCAD)
- [[entities/tools/cable-tray|cable tray]]
- [[entities/tools/din-rail|DIN rail]]
- [[entities/tools/dupont-connector|Dupont connector / housing]]
- [[entities/tools/grommet|grommets]]
- [[entities/tools/heat-shrink|heat shrink]]
- 2020 [[concepts/aluminum-extrusion-wiring|aluminum extrusion]]
- [[entities/tools/3d-printer|3D printer]] (for clips, pin covers, mounts)
- [[entities/tools/raspberry-pi|Raspberry Pi]] (for pin cover demo)

## Materials used

- [[entities/materials/abs|ABS]] / [[entities/materials/pla|PLA]] (printed mounts, clips, pin cover)
- [[entities/materials/aluminum|Aluminum]] (extrusion, DIN rail)
- [[entities/materials/nylon|Nylon]] (zip ties)

## Brands mentioned

- [[entities/brands/3m|3M]] (adhesive on mounts)
- [[entities/brands/grabcad|GrabCAD]] (David's published designs)
- [[entities/brands/automation-direct|Automation Direct]] (DIN rail components)
- [[entities/brands/raspberry-pi|Raspberry Pi]]
- [[entities/brands/amazon|Amazon]] (cable supplies)

## Concepts referenced

- [[concepts/cable-management|cable management]]
- [[concepts/aluminum-extrusion-wiring|2020 / 2040 extrusion as wire chase]]
- [[concepts/din-rail-wiring|DIN rail wiring]]
- [[concepts/strain-relief|strain relief]]
- [[concepts/parametric-design|parametric design]] (his cable clip is parametric)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/design-enclosures-for-electronics-using-mechanical-mindset|Design enclosures for electronics]] — natural prerequisite (you need somewhere for the wires to terminate).
- [[videos/how-to-choose-an-adhesive|How to choose an adhesive]] — adhesive-backed mounts rely on the same substrate-matching logic.
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify|Insights in real-world battery energy]] — same audience: prototype-to-product makers using cordless power.
