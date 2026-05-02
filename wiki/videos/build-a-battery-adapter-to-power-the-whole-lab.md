---
type: video
title: "Build a Battery Adapter to Power the Whole Lab"
video_id: "lcV9Wvxn6qk"
url: "https://www.youtube.com/watch?v=lcV9Wvxn6qk"
published: 2025-11-15
duration: "30:51"
tags: [battery, usb-c-pd, dc-power, open-source, 3d-printing, build, electronics]
ingested: 2026-05-02
---

## Overview

David designs and builds an open-source battery adapter for power-tool batteries (specifically Rigid 18 V) that outperforms the $89 Rigid commercial unit at ~$20 — higher USB-C PD wattage (65 W vs. 45 W), DC output, lower idle draw (1 W vs. 2.2 W), updatable connectors, and parametric for any battery brand. The build uses an off-the-shelf North American electrical "handy box," 3D-printed Terminal V2 (a two-body part — Body A holds Molex connectors into the battery, Body B routes the wires), and a knock-off GaN USB-C PD adapter. He closes with an extended message to Elon Musk about the original promise of Tesla — higher performance, lower cost, longer lifespan — and how the company never delivered the cost-down.

## Key takeaways

- USB-C PD at 45+ W (up to 21 V) is now the bottleneck for portable lab tools — soldering irons, jigsaws, routers all benefit.
- The Rigid commercial unit wastes ~2.2 W idle; the open-source build idles below 1 W (twice the standby battery life).
- Inverters lose ~20% reliably; prefer DC-out for any tool that accepts it, especially when stepping *down* from 18 V.
- Off-the-shelf electrical handy boxes ($2.50) provide a rigid metal mounting surface that beats 3D-printed enclosures for adding features.
- Open-source two-body design lets users print just Body A for direct battery access, or both halves for the full adapter.
- Parametric connector sleeves let you swap Anderson Powerpole for any other connector by changing one rectangular extrude cut.
- "When Rigid improves their battery, they're enhancing my design" — leveraging massive corporate engineering effort by composing your design on top of theirs.
- Gallium nitride USB-C PD adapters now hit ~95% efficiency; David recommends an Akeer-brand 65W unit ($10).

## Techniques demonstrated

- [[concepts/standardized-handybox|standardized handy box]] as a universal mounting/enclosure platform
- [[concepts/parametric-connector-sleeve|parametric connector sleeve]] — one extrude-cut variable controls connector compatibility
- [[concepts/leverage-incumbent-engineering|leveraging incumbent engineering]] — design on top of mass-produced parts
- [[concepts/tap-imperial-to-metric|retap imperial 8-32 to metric M4]] for better clamping
- M2.5 screws as pins (no threads needed) when there's no pull-out load

## Tools used

- [[entities/tools/3d-printer|3D printer]] (FDM, no supports per David's design rules)
- [[entities/tools/soldering-iron-pinecil|Pinecil USB-C PD soldering iron]]
- [[entities/tools/usb-power-meter|USB power meter]] (in-line, ~0.1 W resolution)
- [[entities/tools/handy-box|North American handy box]] (electrical outlet box, ~$2.50)
- [[entities/tools/molex-44262|Molex 44262 series connectors]]
- [[entities/tools/anderson-powerpole|Anderson Powerpole]] connectors

## Materials used

- [[entities/materials/abs|ABS]] / [[entities/materials/pla|PLA]] (3D-printed terminal body)
- [[entities/materials/heat-shrink|heat shrink tubing]]
- 14 AWG and 18 AWG wire

## Projects

- [[entities/projects/terminal-v2|Terminal V2]] — open-source battery terminal adapter on [[entities/brands/grabcad|GrabCAD]]
- [[entities/projects/openbox-project|OpenBox Project]] — handybox-based design family
- [[entities/projects/openlab-project|OpenLab Project]]

## Brands / products mentioned

- [[entities/brands/rigid|Rigid]] (Emerson Electric, ~$75B market cap) — class-leading 18 V power-tool batteries
- [[entities/brands/reiko|Reiko]] — handy-box manufacturer
- [[entities/brands/akeer|Akeer]] — knock-off 65 W GaN USB-C PD adapter
- [[entities/brands/tesla|Tesla]] / [[entities/people/elon-musk|Elon Musk]] (closing message)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- [[entities/people/elon-musk|Elon Musk]]

## Notable quotes / timestamps

- 25:35 "They work for me now, because this is my creation, and when they improve this battery makes the next generation of this, then they will be enhancing my design."
- 28:23 "If this thing had the mileage and the cost and the performance that was going to last longer than a Toyota, then I would be working for you today."

## Related videos

- [[videos/10-years-of-engineering-labs|10 Years of Engineering Labs]]
- [[videos/expanded-pvc-for-engineering-designs-the-easiest-panel-in-fabrication|Expanded PVC for Engineering Designs]]
