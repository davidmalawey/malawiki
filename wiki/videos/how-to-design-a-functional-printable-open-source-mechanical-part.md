---
type: video
title: "How to design a functional, printable, open source mechanical part"
video_id: "CvhiSP_6ESQ"
url: "https://www.youtube.com/watch?v=CvhiSP_6ESQ"
published: 2025-12-09
duration: "37:09"
tags: [design-process, parametric-design, 3d-printing, grabcad, sleeve, bearing, openbox, openlab]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] walks through his full mechanical-engineering design process for a 3D-printable [[entities/tools/sleeve|sleeve]] — the part that retains a shaft (and optionally a [[entities/tools/ball-bearings|bearing]]) through a thin steel wall of a [[entities/tools/handy-box|handy box]]. He motivates the part by pointing at three off-the-shelf devices (lamps, an articulating lamp arm, a fan) where designers solved the same "thin steel wall + pin" joint, then walks through design questions, research questions, load testing, parametric variants, and how the questions get embedded back into the file naming (sleeve, sleeve-BR, sleeve-BR-inch).

## Key takeaways

- A functional design starts by asking *why* — what real-world joint or function does this part solve? Find three existing examples before drawing.
- Define the design questions explicitly: How is the part retained? How does it transfer load? Where does it bottom out? Then answer each with a feature (chamfer, shoulder, press fit).
- A [[concepts/parametric-design|parametric design]] should encode answers to the questions; variants (bushing, bearing, inch-bearing) become derived files in a [[concepts/parts-library|parts library]].
- Press-fit a [[entities/tools/ball-bearings|608 bearing]] into the sleeve so the bearing carries the radial load; keep the sleeve geometry common across the family.
- Watch for the bending moment when the bearing isn't centered over the steel wall — the wall isn't the load path, the sleeve shoulder is.
- Print at default settings (e.g. 0.3 mm layer, 30% infill) to keep the design honestly reproducible by anyone who downloads the file.
- Publish on [[entities/brands/grabcad|GrabCAD]] so other people can branch and contribute back.

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] with derived part files
- [[concepts/press-fit|Press fit]] of bearing into printed sleeve
- [[concepts/design-questions|Design-questions framework]] — list the questions a part must answer, then add features that answer each one
- [[concepts/parts-library|Parts library / family of variants]]
- [[concepts/print-direction|Print direction]] considerations and chamfer-as-overhang-elimination

## Tools used

- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/sleeve|Sleeve]] (his own design)
- [[entities/tools/ball-bearings|608 ball bearing]]
- [[entities/tools/solidworks|SolidWorks]]

## Materials used

- [[entities/materials/abs|ABS]]

## Projects

- [[entities/projects/openbox-project|OpenBox Project]]
- [[entities/projects/openlab-project|OpenLab Project]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/highly-engineered-emt-conduit-parts-to-study-before-designing]] — the prerequisite "study existing parts" episode.
- [[videos/innovations-underway-friction-welded-pvc-unistrut-slide-mechanism-structural-ste]] — more parametric/printable parts in the same library.
