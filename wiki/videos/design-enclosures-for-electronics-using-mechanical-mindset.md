---
type: video
title: "Design enclosures for electronics (using mechanical mindset)"
video_id: "i4oJTfp18eg"
url: "https://www.youtube.com/watch?v=i4oJTfp18eg"
published: 2024-09-11
duration: "36:58"
tags: [enclosure-design, mechanical-design, 3d-printing, prototyping, reference, senior-design]
ingested: 2026-05-02
---

## Overview

A reference-grade lecture pulled from David's 5–10 years mentoring senior design at [[entities/places/texas-am|Texas A&M]]. The audience is electronics engineers and prototypers who suddenly need to be mechanical engineers. He walks through benchmarking, choosing parts whose datasheets you trust, why circles are your friend, working with stock [[entities/materials/pvc|PVC pipe]] and [[entities/tools/project-box|project boxes]], waterproofing without overkill, and a rapid-fire set of 3D-printing rules of thumb.

## Key takeaways

- **Step 1 is benchmarking, not CAD.** Don't reinvent the wheel — find an existing enclosure (high-volume injection-molded preferred) whose layout solves 80% of your problem and copy its decisions.
- **Buy from distributors that ship CAD models.** [[entities/brands/mouser|Mouser]] is David's favorite — datasheets include dimensioned drawings with [[concepts/tolerances|tolerances]]. Use [[entities/brands/amazon|Amazon]] only after you've scouted the part on a real distributor.
- **Default to circles.** Standardize on 12 mm round panel-mount features (buttons, jacks, glands) so you can drill, not 3D-print, the panel cutouts and reuse them across projects. Circles also tolerate hand drilling far better than slots.
- **Stock [[entities/materials/pvc|PVC pipe]] = free body geometry.** Slicing a section of PVC gives you a perfectly round, waterproof tube; you only need to design the end caps. The wall thickness is consistent and the OD/ID are standardized.
- **[[concepts/water-resistance|Water is OK]]** — most consumer projects don't need IP68. Splash-resistant via [[concepts/o-ring-design|O-ring]] grooves on a circular face is achievable with hobbyist tools.
- **The clamping/compliance trick:** add little 3D-printed fingers or ribs that flex and squish an O-ring evenly when fasteners pull two halves together. Plastic compliance is your friend.
- **8 rules of thumb for 3D printing enclosures:**
  - Wall thickness: ~2.4 mm default
  - Draft angles: start at 2°
  - Fillets first in the feature tree (so they don't break later edits)
  - Print orientation matters for both strength and surface finish ([[concepts/print-direction|see print-direction concept]])
  - Use [[entities/tools/heat-set-insert|heat-set brass inserts]] for any fastener that will be removed more than once — self-tapping screws into plastic strip on cycle 3 or 4
  - M3 is the workhorse screw; standardize and stock
  - Account for [[concepts/plastic-compressibility|plastic compressibility]] when stacking fasteners
  - Print check-fit pieces before committing to the full enclosure
- **Project boxes** (off-the-shelf aluminum or plastic) look more elegant than 3D prints, give you guaranteed [[concepts/tolerances|tolerances]] on the cavity, and let you concentrate effort on the panels.

## Techniques demonstrated

- [[concepts/benchmarking-design|Benchmarking]] — search for a high-volume part that already solves the problem.
- [[concepts/parametric-design|Parametric design]] of waterproof end caps for stock PVC.
- O-ring groove design and clamping with compliant 3D-printed fingers.
- Feature-tree ordering in [[entities/brands/solidworks|SolidWorks]] (fillets early, small chamfers last).

## Tools / parts referenced

- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/project-box|project box]] (aluminum)
- [[entities/tools/heat-set-insert|heat-set brass inserts]]
- [[entities/tools/o-ring|O-rings]]
- [[entities/tools/waterproof-button|waterproof panel-mount button]] (~12 mm)

## Materials used

- [[entities/materials/pvc|PVC pipe]] (stock body)
- [[entities/materials/pla|PLA]] / [[entities/materials/abs|ABS]] (printed end caps)
- [[entities/materials/aluminum|Aluminum]] (project box)
- Rubber [[entities/tools/o-ring|O-rings]]

## Brands mentioned

- [[entities/brands/mouser|Mouser]] (preferred parametric search)
- [[entities/brands/amazon|Amazon]]
- [[entities/brands/solidworks|SolidWorks]]
- [[entities/brands/grabcad|GrabCAD]] (parametric models published)
- [[entities/brands/texas-am|Texas A&M]] (senior design context)

## Concepts referenced

- [[concepts/benchmarking-design|benchmarking]]
- [[concepts/parametric-design|parametric design]]
- [[concepts/borrowing-tolerances|borrowing tolerances]] (from PVC and project boxes)
- [[concepts/o-ring-design|O-ring sealing]]
- [[concepts/water-resistance|water resistance vs. waterproofing]]
- [[concepts/wall-thickness-rule|3D-printed wall-thickness rule of thumb]]
- [[concepts/print-direction|print direction]]
- [[concepts/plastic-compressibility|plastic compressibility]]
- [[concepts/tolerances|tolerances]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/these-two-genius-designers-are-building-our-future|These two genius designers]] — same parametric / borrowed-tolerances philosophy.
- [[videos/clean-up-cords-wires-in-projects|Clean up cords & wires]] — natural follow-on once the enclosure exists.
- [[videos/how-to-choose-an-adhesive|How to choose an adhesive]] — bonding end caps to PVC tubes.
