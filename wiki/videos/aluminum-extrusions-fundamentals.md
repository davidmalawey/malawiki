---
type: video
title: "Aluminum Extrusions Fundamentals"
video_id: "cLrIE6ltErE"
url: "https://www.youtube.com/watch?v=cLrIE6ltErE"
published: 2025-09-03
duration: "34:20"
views: 191235
likes: 6160
tags: [aluminum-extrusion, fasteners, frame-design, solidworks, prototyping]
ingested: 2026-04-24
---

# Aluminum Extrusions Fundamentals

## Overview

A 34-minute reference on T-slot aluminum extrusions (2020 and 3030 profiles) — nut types, cutting technique, corner brackets, fastener selection, frame geometry, failure modes, and accessories. David ends with a Solid Works weldments tutorial that generates a cut list from a 3D sketch without making a full multi-part assembly. Storage racks in his shop are 3030 from [[entities/brands/automation-direct|Automation Direct]]; 2020 is cheaper on [[entities/brands/amazon|Amazon]].

## Key takeaways

- **Rub [[entities/materials/paraffin-wax|paraffin wax]] on a wood-blade miter saw before cutting aluminum.** Grocery-store paraffin (a few bucks) prevents aluminum from smearing onto the teeth and gives near-factory cut quality. Same trick works on magnesium. A [[entities/brands/crayola|Crayola]] crayon would probably work too.
- **The slide-in nut is the daily driver;** drop-in solves the after-assembly problem; ball-spring is the premium option that holds its vertical position. Stamped nuts are usually inch-spec — skip them.
- **Use M5 for 2020, M6 for 3030** as fastener defaults. The end-hole for longitudinal fastening isn't threaded — tap it yourself (M6 for 2020's end hole, M8 for 3030's).
- **Set screws are worse than machine screws** because [[concepts/screw-as-spring|they can't elongate]] — no spring region means they go from loose to fully-tight in one turn, and they gouge the extrusion.
- **The most common mistake**: a screw too long for a thinner clamped section drives into the groove floor, so everything looks tight but the workpiece is loose. Keep 10 mm and 12 mm Phillips-head fasteners on hand; use thick washers to lift the bolt head when stuck with a long bolt.
- **Don't over-engineer horizontals** — a length of [[entities/materials/d-rail|steel d-rail]] across two vertical extrusion frames is cheaper, easier to cut, and gives you adjustment play that two matched 3030 rails won't.
- **Wheels off the shelf are disappointing.** Use David's 3D-printable bracket on [[entities/brands/grabcad|GrabCAD]] to adapt cheap rollerblade wheels instead.

## Techniques demonstrated

- Cutting extrusion with [[entities/materials/paraffin-wax|paraffin wax]] + wood blade (miter or circular saw).
- Tapping the end hole of an extrusion for a longitudinal M6 or M8 fastener.
- Fastener-strength recipe: large screw + large head area + matched drive + snug-before-preload (no gaps).
- Cantilever joint analysis: support the tension side (top), compression side is along for the ride.
- Miter-joint planning that reuses the offcut from one 45° as the other face — no triangular waste.
- Solid Works weldments workflow for generating a cut list from a 3D sketch without a multi-part assembly.

## Tools used

- [[entities/tools/miter-saw|Miter saw]] / [[entities/tools/circular-saw|circular saw]] with wood blade
- [[entities/materials/paraffin-wax|Paraffin wax]] (grocery-store grade)
- Drill + tap (M6, M8)
- Torque wrench (60 inch-lb reference)
- [[entities/tools/sharpie|Sharpie]] on silver; pencil on black
- Acetone for mark removal
- Hand file (for trimming bracket tabs)
- Hand-lever cutting machine for d-rail

## Materials / components discussed

- [[entities/materials/aluminum|Aluminum]] 2020 and 3030 T-slot extrusion (anodized gray standard, black available)
- Nut types: slide-in, drop-in, ball-spring, stamped
- Corner brackets (exterior cast-aluminum, interior hidden)
- Three-way connectors (less strong due to set screws)
- [[entities/materials/d-rail|Steel d-rail]] (for cheap horizontal connectors)
- End caps (mostly not worth it — use hot glue to retain)
- LED strips, rubber-strip sealing, cork sheet

## Projects referenced

- Storage racks (3030 shelves)
- Test rig chassis with two vertical frames tied by horizontal d-rails
- [[entities/projects/scuttle-robot|SCUTTLE]]-lineage bracket designs on [[entities/brands/grabcad|GrabCAD]], including the rollerblade-wheel adapter and parametric hinge

## Brands / platforms

[[entities/brands/automation-direct|Automation Direct]] (David's 3030 supplier of choice) · [[entities/brands/amazon|Amazon]] (2020, common) · [[entities/brands/solidworks|Solid Works]] (weldments workflow) · [[entities/brands/grabcad|GrabCAD]] (open-source brackets) · [[entities/brands/home-depot|Home Depot]] / [[entities/brands/lowes|Lowe's]] (steel handy boxes, $2-3, USA-made) · [[entities/brands/crayola|Crayola]] · Discord (David's community link).

## Notable quotes / timestamps

- `[4:51]` "I bet this is nearly the same formulation as any low-cost simple wax… a Crayola crayon even would do the job."
- `[12:57]` "When you use this set screw, there is no place for it to elongate, and it is simply in compression, making it go from loose to fully tight very quickly" — contrasting with a real machine screw's spring region.
- `[21:00]` "This here is the most common mistake I see people encounter using these extrusions" — bolt bottoming out in the slot.

## Related videos

- [[videos/borrow-a-tolerance-mindset-for-designers|Borrow a Tolerance]] — [[concepts/screw-as-spring|screw-as-spring]] is set up there and referenced here. Same Scuttle / GrabCAD design-sharing ethos.
- [[videos/more-than-you-ever-wanted-to-know-about-tape|Tape reference]] — aluminum foil tape is covered in detail there; this video covers aluminum as structural stock.
