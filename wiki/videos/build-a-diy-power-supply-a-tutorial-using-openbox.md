---
type: video
title: "Build a DIY power supply (a tutorial using openBox)"
video_id: "VLrEtrU10ow"
url: "https://www.youtube.com/watch?v=VLrEtrU10ow"
published: 2024-10-20
duration: "21:33"
tags: [diy, power-supply, openbox, robotics, anderson-connectors, parametric-design, scuttle]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] walks through a benchtop DIY power supply built from a metal handy-box, a 12V car-style socket, [[entities/tools/anderson-connector|Anderson Powerpole]] connectors, and a printed parametric adapter — one of many modules in the [[entities/projects/openbox|OpenBox]] design cluster used in the [[entities/projects/scuttle-robot|SCUTTLE]] lab. The pitch: borrow voltage from a power-tool battery (or solar panel, or LiFePO4), expose it via a ubiquitous car adapter that already accepts USB-PD, USB-A, and a hundred truck-driver gadgets, and avoid the trap of designing custom buck/boost circuitry for every student prototype.

## Key takeaways

- Tap M4 metric threads into electrical handy-box knockouts so the box integrates with David's broader metric design system.
- A printed parametric bushing with a split allows friction-fit insertion into out-of-round knockouts.
- Anderson Powerpole orientation: "read and red on the right" — letter A reads, red contact on the right side of the housing.
- Anderson recommends a pin (not a screw) to keep dovetails aligned; a same-diameter M2.5 screw works as a substitute without splitting the plastic.
- A car-socket adapter is far cheaper and more efficient than a wall adapter at the same wattage because it's DC-direct and made for a competitive trucker market.
- Direct DC sourcing accepts up to ~24V — works equally with 18V tool batteries, 18V solar panels, or LiFePO4 packs without any conversion circuitry.
- For student/researcher projects, swap "design two batteries + boost converters + buck converters" for "one hefty common battery + this $12 car adapter that already has USB-PD."
- Reverse-polarity protection diodes are the only circuitry needed when running off a solar panel.

## Techniques demonstrated

- Tapping M4 threads into thin sheet steel knockouts ([[concepts/borrowing-tolerances|borrowing tolerances]] from existing metric system).
- [[concepts/parametric-design|Parametric design]] in [[entities/brands/solidworks|SolidWorks]] — suppress/show features to generate variants of one bushing.
- Plastic-deforming (slightly squeezing) loose Spade Terminals for re-tightening.
- Designing a flush cover variant rather than using the off-the-shelf flange version.
- Publishing parametric models on [[entities/brands/grabcad|GrabCAD]] (search "OpenBox" / "handy box").

## Tools used

- M4 tap and matching drill
- [[entities/tools/anderson-connector|Anderson Powerpole connector]] (with included spring pin)
- [[entities/tools/spade-terminal|Spade Terminals]]
- [[entities/tools/3d-printer|3D printer]] (for adapter, bushing, cover)
- M2.5 pan-head stainless screws
- E600 silicone adhesive (referenced from his adhesives video)

## Materials used

- 12V/24V cigarette-lighter style socket and matching plug (Amazon)
- [[entities/materials/pla|PLA]] / printed plastic for adapter and bushing
- Painted steel handy-box (interior unpainted to retain ground continuity)
- Replaceable inline fuse
- Lithium-ion power-tool battery (Ridgid, chosen for lifetime warranty)
- [[entities/materials/lifepo4|LiFePO4]] battery (alternative source)
- Solar panel (~18V, fits within 24V envelope)

## Projects

- [[entities/projects/openbox|OpenBox]] — David's GitHub-published cluster of handy-box-based modules (this is one).
- [[entities/projects/scuttle-robot|SCUTTLE]] robotics lab — where these supplies are used for testing electronics.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Brands mentioned

- [[entities/brands/amazon|Amazon]] — source for the socket
- [[entities/brands/anderson-powerworks|Anderson Powerworks]] — connector standard
- [[entities/brands/ridgid|Ridgid]] — power-tool battery (lifetime warranty)
- [[entities/brands/solidworks|SolidWorks]] — parametric CAD
- [[entities/brands/grabcad|GrabCAD]] — model hosting

## Notable quotes / timestamps

- 4:18 — "read and red on the right" — Anderson polarity mnemonic.
- 11:50 — Why car adapters are cheaper and more efficient than wall adapters.
- 19:30 — "BIG BIG PICTURE": one common battery + car adapter beats custom regulators for prototypes.

## Related videos

- [[videos/how-to-drill-a-hole-in-metal-plastic-wood-and-laminate|How to Drill a Hole in Metal, Plastic, Wood, and Laminate]] — companion reference for the drilling and tapping shown here.
