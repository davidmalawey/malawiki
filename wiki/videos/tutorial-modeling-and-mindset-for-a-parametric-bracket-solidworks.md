---
type: video
title: "Tutorial: modeling and mindset for a parametric bracket (SOLIDWORKS)"
video_id: "OkRfWXU7b-k"
url: "https://www.youtube.com/watch?v=OkRfWXU7b-k"
published: 2024-06-08
duration: "6:48"
tags: [solidworks, parametric-design, 3d-printing, brackets, tutorial, cad]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] designs and prints a [[entities/tools/din-rail|DIN-rail]] mount for his [[entities/tools/multimeter|multimeter]] in [[entities/brands/solidworks|SolidWorks]], using compliance (the elastic deflection of plastic) to grip the device. The real lesson is mindset: treat CAD as software — make every design parametric, expose only the few variables a downstream user needs to change, and you turn one model into a reusable family of brackets.

## Key takeaways

- Engineering must be redone "from the ground up" — only software is fully digital, fully [[concepts/parametric-design|parametric]], fully shareable. CAD should be treated the same way.
- A stamped-steel bracket costs ~$10K in tooling; an injection-molded plastic one ~$5K. A parametric 3D print delivers a customized result for ~$0 marginal cost when volume is low.
- The clamp uses compliance — two arms deflect ~2 mm to grip the multimeter, holding it via spring force.
- Two configurations of the same SolidWorks model (one for the multimeter, one for a servo controller) come from changing two variables — width and thickness.
- Designing parametrically means putting your expertise into the fixed elements (the 2 mm flex target) and exposing only the dimensions a non-mechanical engineer needs to change.
- The hinge is a piece of 1/4" OD HDPE irrigation tubing — a deliberately commodity, locally sourceable part.

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] in SolidWorks with multiple configurations driven by sketch variables.
- [[concepts/plastic-compressibility|Plastic compressibility]] / compliance for fastener-free clamping.
- Borrowing a commodity material ([[entities/materials/hdpe|HDPE]] irrigation tubing) as a structural part.

## Tools used

- [[entities/brands/solidworks|SolidWorks]]
- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/multimeter|Multimeter]] (the held device)
- [[entities/tools/din-rail|DIN rail]]

## Materials used

- [[entities/materials/hdpe|HDPE]] (1/4" OD tubing as hinge pin)
- Polyurethane tubing (alternative)
- 3D-print plastic for the bracket body

## Projects

- Multimeter DIN-rail bracket (parametric)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:03] "We have to redo engineering from the ground up... the only part that we can keep is software — it's the only part that's 100% digital, fully parametric, fully modular."
- [3:09] "If you realize that CAD is software, then why would you make your software without variables and turn everything to constants?"
- [4:42] "We want to put our expertise into the fixed elements... and then a non-mechanical engineer can figure it out from there."

## Related videos

- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
- [[videos/excessively-technical-video-about-a-vacuum-adapter]]
- [[videos/design-enclosures-for-electronics-using-mechanical-mindset]]
