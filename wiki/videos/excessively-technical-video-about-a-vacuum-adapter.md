---
type: video
title: "Excessively technical video about a vacuum adapter"
video_id: "wWQ2x0hBkBY"
url: "https://www.youtube.com/watch?v=wWQ2x0hBkBY"
published: 2025-03-18
duration: "31:14"
tags: [vacuum, dust-collection, parametric-design, 3d-printing, shop-tools, airflow, open-source]
ingested: 2026-05-02
---

## Overview

A self-described chaotic edit about David's parametric vacuum-adapter design. The thread underneath is that vacuums are an under-served corner of the automation/robotics stack — moving air takes the most energy of any shop task, vacuum tube interfaces are wildly non-standard, and a 3D-printed parametric adapter can replace dozens of single-purpose adapters big brands sell. The video doubles as a pitch for parametric design as a 1000x utility multiplier over fixed designs.

## Key takeaways

- Vacuum/airflow tools take the most energy of any shop or robotic process — so getting their interfaces right matters disproportionately.
- Vacuum hose connectors look standardized but aren't. Common nominal sizes (e.g., 35 mm) hide ~1 mm taper differences across brands; David measured both ID and OD on multiple brands.
- A single 3D-printed parametric adapter can fit a surprising range of brand connectors at once — design directionality matters.
- Parametric design (vs. fixed design) gives 1000x more utility because users can re-export geometry per use case rather than reorder physical SKUs.
- This is a design that "should exist" — if it becomes popular, it could cost big vacuum brands money in adapter sales.
- All design files live on Open Lab (qr.net/openlabproject).

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] applied to a 3D-printed mechanical interface — varying ID, OD, length, taper, and directionality from a single source model.
- Measuring real-world parts with [[entities/tools/calipers|calipers]] across multiple brands to discover hidden tolerance variation.
- [[concepts/borrowing-tolerances|Borrowing tolerances]] — using one brand's measurements to set parametric defaults that fit many.

## Tools used

- [[entities/tools/3d-printer|3D printer]] (fabricates the adapter)
- [[entities/tools/calipers|Calipers]] (measure connector ID/OD)
- [[entities/tools/shop-vacuum|Shop vacuum]] — multiple brands (Rigid portable battery vacuum referenced explicitly)
- [[entities/tools/circular-saw|Circular saw]] / [[entities/tools/miter-saw|miter saw]] / oscillating tool — example tools that benefit from a vacuum tap

## Materials used

- [[entities/materials/pla|PLA]] / [[entities/materials/abs|ABS]] (typical 3D-print stocks)

## Projects

- [[entities/projects/parametric-vacuum-adapter|Parametric Vacuum Adapter]] — the design centerpiece of the video.
- [[entities/projects/open-lab-project|Open Lab Project]] — qr.net/openlabproject; hosts the design files.

## Brands mentioned

- [[entities/brands/ridgid|Ridgid]] (portable battery vacuum)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related concepts

- [[concepts/parametric-design|Parametric design]]
- [[concepts/borrowing-tolerances|Borrowing tolerances]]
- [[concepts/vacuum-interface-standards|Vacuum interface (non-)standards]] — the hidden mismatch across brands at "the same" nominal size.

## Notable timestamps

- 6:00 Minimizing energy by design
- 10:50 Vac connector geometry
- 13:30 Measuring, common sizes
- 18:00 Directionality
- 20:00 Surprise! they all fit
- 25:50 Parametric design PURPOSE
