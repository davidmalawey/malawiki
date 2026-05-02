---
type: video
title: "Design for Manufacturing: Polymer FDM [Part 1]"
video_id: "HYnm2MD0Nks"
url: "https://www.youtube.com/watch?v=HYnm2MD0Nks"
published: 2022-06-20
duration: "11:54"
tags: [3d-printing, fdm, dfm, design-rules, tolerances, slicer, overhangs]
ingested: 2026-05-02
---

## Overview

Part 1 of a Design for Manufacturing series focused on FDM/FFF polymer 3D printing. David lays out concrete rules-of-thumb a designer should bake into CAD before sending parts to a printer: avoid overhangs, respect minimum wall thickness and nozzle/path width, cap the maximum hole size, prefer debossed labels, and use three-point clearance bumps instead of relying on tight diameter tolerances.

## Key takeaways

- Gravity matters: design parts so the build direction never demands unsupported overhangs. Eliminating supports makes the part faster, cheaper, and printable on a low-cost in-house machine.
- Minimum wall thickness: 1.5–2.0 mm. With a typical 0.4mm nozzle and ~0.44mm path width, two perimeters give 0.88mm; thicker walls let the slicer fill between them, which is where strength comes from.
- Holes in vertical planes: ~3mm is fine, ~6mm starts to fail at the ceiling. Convert circles to teardrops to print large holes without supports.
- Labels: deboss (cut into the part) at ~0.5mm depth — about one extrusion-width — for cleanest look without weakening the wall.
- Tolerance reality: assume ±0.3mm dimensional accuracy. "Design for what we can readily achieve, not what we can achieve."
- For tight fits, replace a continuous mating diameter with three protruding bumps: maintains center, easy to file/sand the small contacts if oversize.
- Clearance-fit rule of thumb: 0.3mm under the mating ID gives reliable assembly across printers.

## Techniques demonstrated

- [[concepts/design-for-manufacturing|Design for manufacturing]] (FDM-specific)
- [[concepts/print-direction|Print direction]] / build-direction awareness
- [[concepts/tolerances|Tolerances]] (the 0.3mm rule of thumb)
- [[concepts/three-point-clamping|Three-point clamping]] (bumps instead of full mating diameter)
- [[concepts/teardrop-holes|Teardrop holes]] for support-free vertical openings

## Tools used

- [[entities/tools/3d-printer|3D printer]] (FDM, 0.4mm nozzle)
- Slicer software (PrusaSlicer/Cura class)
- [[entities/tools/calipers|Calipers]] (for measuring the mating part)

## Materials used

- [[entities/materials/pla|PLA]] (and FDM thermoplastics generally)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [9:46] "We're not designing for what we can achieve, we're designing for what we can readily achieve."
- [0:38] "The best way to make the part difficult or come out poorly is to have a design that requires this overhang."

## Related videos

- [[videos/what-screws-to-use-in-your-3d-print]] — Part 2: fasteners
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
