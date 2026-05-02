---
type: video
title: "How to Design a 3D Print - (with example, functional Hinge)"
video_id: "ZOMu9AFOdCk"
url: "https://www.youtube.com/watch?v=ZOMu9AFOdCk"
published: 2025-06-08
duration: "41:00"
tags: [3d-printing, cad, solidworks, parametric, hinge, design-for-manufacturing, scuttle]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] walks through the design intent of a printable, parametric, multi-variant hinge used across [[entities/projects/scuttle-robot|SCUTTLE Robotics]] parts. He covers naming conventions, body identification, tolerancing the in-print hinge gap, parametric constraints, nozzle phenomena, methods to increase friction, even strength, the function of chamfers, debossing version markings, and CAD file properties for professional sharing. Treats the hinge as a worked example of "100 individual decisions" inside a single printed part.

## Key takeaways

- Standardize directional naming (purple = fixed body, green = pivot body) before features cascade — prevents ambiguity when revisiting CAD years later.
- Default print tolerance: 0.3 mm clearance between mating parts. For free-spinning pivots, increase the gap; for friction hinges, keep clearance minimal and crack the printed-as-one-piece part to separate.
- Print orientation matters: a hinge printed as one part with a thin gap relies on the slicer dropping that gap, then mechanical separation.
- [[concepts/parametric-design|Parametric modeling]] starts with naming variables early — let the height variable propagate so doubling the part doesn't require re-CADing features.
- Three hinge variants share parametric DNA: hinge-v3 (beefy single-pin), hinge-v2 (flush panel pair, 10 kg with two hinges), and hinge-double (lightweight articulation with two pins).
- Debossing the version number into the part itself makes physical iteration debuggable — you can identify a part you printed two years ago.
- File-properties metadata (keywords, description) lets you find the file later and shares like a professional asset.

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] using named constraints.
- [[concepts/borrowing-tolerances|Borrowing tolerances]] (referenced; previous video extends the concept).
- [[concepts/print-direction|Print direction]] for in-place hinge printing.
- [[concepts/feature-tree-naming|Feature tree naming]] — disciplined CAD naming for collaboration and future revisions.
- [[concepts/version-debossing|Version debossing]] — embedding revision number in the printed geometry.
- Body coloring as a solid-body identifier in [[entities/brands/solidworks|SolidWorks]].
- Chamfer placement to manage strength evenness and assembly clearance.

## Tools used

- [[entities/brands/solidworks|SolidWorks]] (parametric CAD)
- [[entities/tools/3d-printer|3D printer]]
- [[entities/brands/grabcad|GrabCAD]] (model hosting — fan_joint-1)

## Materials used

- [[entities/materials/pla|PLA]] / [[entities/materials/abs|ABS]] (typical print materials)

## Projects

- [[entities/projects/scuttle-hinge|SCUTTLE parametric hinge]] — multi-variant printable hinge family.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:00 why this video
- 3:54 naming files & features
- 6:20 tolerancing gaps (0.3 mm default clearance)
- 8:00 parametric using constraints
- 17:12 printing nozzle phenomena
- 19:50 increase hinge friction
- 23:00 evenness in strength
- 24:45 function of chamfers
- 25:50 debossing of version
- 28:40 file properties — more professional

## Related videos

- [[videos/we-discovered-a-shape-and-its-not-a-big-deal|We discovered a shape]] — earlier "borrow tolerances" piece referenced.
- [[videos/strategies-for-lab-workspace-design-of-lab-and-methods|strategies for lab workspace]]
