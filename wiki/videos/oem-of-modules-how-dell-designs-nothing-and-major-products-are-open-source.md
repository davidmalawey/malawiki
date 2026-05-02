---
type: video
title: "OEM of Modules: How Dell designs 'nothing' and major products are open source"
video_id: "fM7covpd0O4"
url: "https://www.youtube.com/watch?v=fM7covpd0O4"
published: 2024-07-04
duration: "18:57"
tags: [open-source, modularity, scuttle, dell, business-model, mechatronics]
ingested: 2026-05-02
---

## Overview

A 19-minute essay arguing that any sufficiently complex product is already partially open source — wherever a module bolts to the main design, the interface must be a published standard. [[entities/people/david-malawey|David]] uses the [[entities/brands/toyota|Toyota]] Camry (tires, airbags, [[entities/tools/18650-cell|18650]] Panasonic cells) and Dell PCs (Intel CPUs, Western Digital drives) to show that a high-value OEM is mostly an integrator. [[entities/projects/scuttle-robot|SCUTTLE]] is positioned as the same business model applied to mobile robotics.

## Key takeaways

- Every high-value product is "main design" + "third-party modules." The points where modules attach are by definition open standards (a tire fits any wheel that meets the spec).
- A module like a [[entities/tools/18650-cell|18650]] Panasonic lithium cell carries hundreds of years of materials science and tens of thousands of engineering hours — a "captured value" the integrator gets cheaply.
- Dell makes nothing — no processors, no RAM, no GPUs, no power supplies, no cables. Dell's value is selecting, characterizing, and supporting a configuration tuned to a customer outcome.
- "Component-to-design ratio": maximize the value imported from commodity modules; minimize the proprietary engineering cost. Margin on top of a high-value component is still a viable business.
- Function MUST overlap with module purpose. A screw used as a position fiducial captures none of its materials value; a battery used to deliver electrical energy captures all of it.
- [[entities/projects/scuttle-robot|SCUTTLE]] follows the Dell pattern: minimal proprietary design, maximum imported value (Raspberry Pi, Panasonic cells, MakerBeam extrusion), swappable modules let the same chassis serve different customer outcomes.
- Investors don't object to Dell sharing component specs because Dell sells outcomes, not designs.

## Techniques demonstrated

- Mapping a product as "main design IP + module IP + open interfaces" to find leverage points.
- Choosing modules so their function overlaps the customer outcome (otherwise the imported value is wasted).
- [[concepts/leverage-incumbent-engineering|Leveraging incumbent engineering]] via commodity supply.

## Tools used

- [[entities/tools/18650-cell|18650 cell]] (Panasonic)
- [[entities/brands/raspberry-pi|Raspberry Pi]]
- Jetson Nano (mentioned as swappable alternative to Pi)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] (v2.4 referenced)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:00] Big Products have Modules
- [1:50] Standard = Open Source
- [4:27] Dell is an OEM of Modules
- [6:25] Dell is secretly "Open Source"
- [7:18] Components-to-Design Ratio
- [9:45] Value MUST overlap Function
- [14:25] Our Designs are Negligible
- [18:00] Accelerate Pace while Industry Forms
- [11:25] "What we do with SCUTTLE is — let's minimize the space where we're the developers of the design, let's maximize the space where we capture value from really nice components."

## Related videos

- [[videos/open-source-hardware-is-evolving]]
- [[videos/this-is-why-you-cant-find-a-robotics-job-in-the-usa]]
- [[videos/how-real-experts-change-the-world-using-robotics]]
- [[videos/how-hardware-enshitification-occurs-and-how-easily-we-can-beat-it]]
