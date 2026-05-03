---
type: video
title: "What screws to use in your 3D Print"
video_id: "LMyhFwJscI0"
url: "https://www.youtube.com/watch?v=LMyhFwJscI0"
published: 2022-11-18
duration: "12:04"
tags: [3d-printing, fasteners, dfm, screws, heat-set-insert, mcmaster-carr, cad]
ingested: 2026-05-02
---

## Overview

Part 2 of the FDM Design for Manufacturing series, focused entirely on choosing fasteners. David covers four common screw archetypes (machine vs. self-tapping, flat-head vs. countersunk), shows how to size their holes in CAD, and walks through using McMaster-Carr to find canonical dimensions and download STEP files. He closes with three default screws that cover almost every hobby-print situation.

## Key takeaways

- Four screw axes to think about: thread type (machine vs. self-tapping/coarse) and head type (flat/pan vs. countersunk).
- Machine screws are for assemblies you'll open repeatedly; pair them with a nut, wing nut, or [[entities/tools/threaded-insert|heat-set insert]]. Self-tapping screws engage plastic directly and are for one-or-few assemblies.
- Heat-set inserts (brass) install with a soldering iron, melt the plastic locally, and give plastic parts machine-screw-quality threads forever.
- Hole-size rules of thumb on FDM: design 0.3mm clearance per side beyond what the screw/insert spec calls for. For a McMaster insert with a 3.57mm drill spec, model a 4.0mm hole and the printer will land near 3.4mm — a good fit.
- McMaster-Carr is the canonical reference: filter by metric size (M2.5 is David's favorite), pick zinc-plated steel over stainless to save cost, and download the STEP file. Lower CAD render quality on threaded parts so they don't bog down the assembly.
- Three-screw default kit that "gets you very far": M2.5 flat-head (for PCBs), M2.5 countersunk (for plastic-to-plastic mating), and M2 self-tapping (for snap-together plastic and PCB).
- For PCB clamping, use flat-head — a countersunk head puts radial stress on a via and can crack the board. Adafruit boards reliably accommodate M2.5; cheap Amazon clones often won't fit even an M2 without drilling out.

## Techniques demonstrated

- [[concepts/design-for-manufacturing|Design for manufacturing]] (fastener-aware CAD)
- [[concepts/screw-as-spring|Screw as spring]] (head choice for PCB clamping)
- [[concepts/parametric-design|Parametric design]] (driving hole diameter from a McMaster spec)
- [[concepts/heat-set-insert-installation|Heat-set insert installation]] with a soldering iron
- [[concepts/parts-library|Parts library]] (McMaster STEP files dropped into CAD)

## Tools used

- [[entities/tools/threaded-insert|Heat-set threaded insert]]
- [[entities/tools/soldering-iron|Soldering iron]] (insert installation)
- [[entities/tools/calipers|Calipers]]
- [[entities/tools/3d-printer|3D printer]] (FDM)
- [[entities/tools/multimeter|Multimeter]] (referenced for case-screw example)
- CAD with parametric sketches (Fusion 360 / SolidWorks class)
- McMaster-Carr web catalog (reference)

## Materials used

- [[entities/materials/pla|PLA]] / FDM thermoplastics
- Brass heat-set inserts
- Zinc-plated steel screws (M2, M2.5)

## Projects

- (general DFM tutorial — no single project)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- Adafruit (referenced as a reputable sensor vendor with usable mounting holes)

## Notable quotes / timestamps

- [11:21] "You can basically get away with using just these three types of screws — the M2.5 flat-head, the M2.5 countersunk, and the self-tapping M2."
- [3:53] "Sometimes it's worthwhile to purchase your sensors from a reputable vendor like Adafruit even if it costs an extra ten dollars instead of the knockoffs."

## Related videos

- [[videos/design-for-manufacturing-polymer-fdm-part-1]] — Part 1: geometry rules
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/exoskeleton-design-control-of-fastener-torque]]
- [[videos/expanded-pvc-for-engineering-designs-the-easiest-panel-in-fabrication]]
