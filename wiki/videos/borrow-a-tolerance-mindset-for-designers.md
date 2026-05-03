---
type: video
title: "Borrow a Tolerance: Mindset for Designers"
video_id: "pN-rh6UwR_A"
url: "https://www.youtube.com/watch?v=pN-rh6UwR_A"
published: 2024-08-15
duration: "32:09"
views: 112764
likes: 4868
tags: [design, tolerances, 3d-printing, assemblies, mindset]
ingested: 2026-04-24
---

# Borrow a Tolerance: Mindset for Designers

## Overview

A 32-minute design-philosophy video arguing that 3D-printed and hobbyist parts don't need to match machined precision — they just need to *borrow* precision from cheaper parts that are already manufactured tightly (ball bearings, spring steel, paper-clip wire, HDPE tubing, even a golf tee). David frames this as a gap in mechanical-engineering curricula: "six years of schooling still did not cover how to build assemblies," and Toyota's real-world assembly work is where he learned it.

## Key takeaways

- **[[concepts/borrowing-tolerances|Borrow a tolerance]]** — a [[entities/tools/ball-bearings|ball bearing]] costs ~3¢ and is manufactured to precision no hobbyist machining operation can match. Drop a few into a sloppy 3D-printed ring and the balls re-center the assembly for you.
- **Surface finish is unreliable on FDM prints; alignment is reliable.** A 3D printer will give you perpendicularity for free, but a press-fit hole diameter needs a drill pass (David uses an 8.03 mm bit for an 8 mm nominal hole, allowing for plastic compression).
- **Five ways balls help an assembly:** nominal contact, team effort, distributed tolerancing, force distribution (spreads F over A, drops pressure P₂ below P₁), and selective material properties (glass for electrical insulation, nylon for low friction, steel for rigidity).
- **Borrow a spring from [[entities/materials/spring-steel|spring steel]], not from plastic.** Plastic spring features are not deterministic — same filament spool produces different spring rates, and cycling + temperature re-shape them. Spring steel is temperature-stable across any range a human can tolerate.
- **Borrow toughness and smoothness from [[entities/materials/hdpe|HDPE]]** (water-system tubing, cheap, tough) and [[entities/materials/urethane|urethane]] (pneumatic hoses, very tough) instead of trying to print those properties.
- **Toughness is a real engineering metric** — it's about impact/impulse loads, not just an adjective.

## Techniques demonstrated

- [[concepts/borrowing-tolerances|Borrowing tolerances]] from off-the-shelf precision parts (ball bearings, paper clips, golf tees, calipers as a reference measurement)
- Drilling a press-fit hole in 3D-printed PLA/ABS with a slightly oversized bit to account for [[concepts/plastic-compressibility|plastic compressibility]]
- [[concepts/print-direction|Print orientation]] to put loaded holes perpendicular to print lines
- [[concepts/screw-as-spring|Screw as a spring]] — the clamping region between head and nut elongates under preload; no elongation length = no preload range
- Parametric CAD so the same hinge design can be re-dimensioned for different loads/geometries without redesign

## Tools used

- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/ball-bearings|Ball bearings]] (precision-manufactured, ~3¢ each)
- [[entities/tools/calipers|Calipers]]
- Drill + side-o drill bit (8.03 mm)
- [[entities/tools/collet|Collet]] / 3-jaw chuck (contrasted for precision)

## Materials discussed

- [[entities/materials/pla|PLA]] · [[entities/materials/abs|ABS]] · PETG — common print materials with varying toughness
- [[entities/materials/hdpe|HDPE]] — tough, smooth, low static friction coefficient
- [[entities/materials/nylon|Nylon]] — low friction, non-abrasive
- [[entities/materials/urethane|Urethane]] — very tough, pneumatic hoses
- [[entities/materials/spring-steel|Spring steel]] — deterministic elastic behavior across temperature
- [[entities/materials/aluminum|Aluminum]] (cast, non-precision, requires machining a datum)
- Cast iron (references a compressor block)

## Projects referenced

- [[entities/projects/scuttle-robot|SCUTTLE robot]] — David's open-source robot platform; the wheel bracket is the only part that requires post-processing (the 8.03 mm drilled hole). Designs on [[entities/brands/grabcad|GrabCAD]].
- In-progress three-jaw-chuck-inspired centering mechanism, to be open-sourced.

## Notable quotes / timestamps

- `[0:30]` "This is a little bit hard for me to organize because it's not something that I've learned in a curriculum or in a book. Believe it or not, six years of schooling in mechanical engineering did not cover how to build assemblies."
- `[28:55]` The golf-tee demonstration: you don't trust the tee's absolute dimensions, but you trust its repeatability to re-measure one ball against another.

## Related videos

- [[videos/aluminum-extrusions-fundamentals|Aluminum Extrusions Fundamentals]] — the same [[concepts/screw-as-spring|screw-as-spring]] concept is used to explain why set screws are inferior to machine screws.
- [[videos/label-supplies-to-multiply-results|Label supplies]] — also leans on "borrowing" (the marketing-label copyright date, the manual's compatibility list) as free data sources.
