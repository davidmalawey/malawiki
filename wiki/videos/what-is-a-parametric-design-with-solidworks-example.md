---
type: video
title: "What is a Parametric Design? (with SOLIDWORKS example)"
video_id: "ISbHy9DpyU8"
url: "https://www.youtube.com/watch?v=ISbHy9DpyU8"
published: 2023-11-21
duration: "17:25"
tags: [parametric-design, solidworks, cad, open-source, multidisciplinary, design-for-manufacturing]
ingested: 2026-05-02
---

## Overview

David's foundational explainer on parametric design. Starting from a real-world ball-mount ball joint (the same design sold by two unrelated brands at different sizes), he defines the three-step path — characterize > digital > parametric — and demos it inside SOLIDWORKS using global variables, configurations, equations, and constraint-driven sketches. The closing argument: making physical hardware parametric does for mechanical engineering what software did in the 90s — value compounds because designs can be duplicated, modified, and stacked across collaborators.

## Key takeaways

- A **design** becomes **digital** by characterizing material and dimensions, and becomes **parametric** by exposing global variables that can be changed without breaking the model.
- Two visibly different products can share the same parametric design (1/4-20 thread, ball-and-socket geometry) — only a few parameters (length, ball diameter) actually vary.
- Three steps: (1) characterize the design, (2) make it digital, (3) make it parametric.
- In SOLIDWORKS, the equals/sigma symbol on a dimension means it links to a global variable — that's the entry point to a parametric model.
- Use **configurations** to bake multiple sizes (32 mm vs 42 mm ball-arm; 9 mm vs 12 mm ball) into a single file; assemblies can carry their own configurations that swap part configurations together.
- Big tip: drive sketches with **constraints** (equal, centered, vertical) instead of numeric dimensions wherever possible — fewer hard numbers means a model that survives parameter changes.
- Open-source + parametric = compounding value. Each engineer's work stacks instead of being re-derived.
- Parametric mechanical hardware enables AI to vary designs the same way software is varied today.

## Techniques demonstrated

- [[concepts/parametric-design|Parametric design]] — characterize, digitize, parametrize.
- [[concepts/feature-tree-naming|Feature-tree naming]] / SOLIDWORKS feature-tree management.
- Global variables, equations, and configurations in SOLIDWORKS.
- Constraint-driven sketching (equal, centered, vertical) over hard-dimensioning.
- Assembly-level configurations that propagate to part configurations.
- [[concepts/design-for-manufacturing|Design for manufacturing]].
- [[concepts/standardize-mounting-interfaces|Standardize mounting interfaces]] — the 1/4-20 camera thread as a universal interface.
- [[concepts/open-source-hardware-publishing|Open-source hardware publishing]] as compounding leverage.
- [[concepts/documented-design-as-leverage|Documented design as leverage]].

## Tools used

- [[entities/brands/solidworks|SOLIDWORKS]] (Texas A&M Student Edition)
- [[entities/brands/grabcad|GrabCAD]] — host for the published ball-mount file (`grabcad.com/library/ball-mount-v1-1`)
- Ball-mount / ball-joint hardware (two different sizes, different brands)
- Reference to laser-cut [[entities/materials/acrylic|acrylic]] prototypes

## Materials used

- [[entities/materials/aluminum|Aluminum]] — cast main body
- Stainless steel — ball element
- [[entities/materials/acrylic|Acrylic]] — referenced for laser-cut prototypes

## Projects

- Ball-mount v1.1 (published on GrabCAD) — the working example throughout.

## People mentioned

- [[entities/people/david-malawey|David Malawey]] — narrator and designer of the reverse-engineered ball-mount file.
- [[entities/brands/texas-am|Texas A&M]] — provider of the SOLIDWORKS Student Edition.

## Notable quotes / timestamps

- 0:00 Intro
- 1:15 Commonized features
- 1:34 Thread for cameras
- 3:35 Define parametric intention
- 6:40 Three Steps to Parametric
- 8:00 Example: SOLIDWORKS
- 10:10 Part Parameters
- 11:20 Part Configurations
- 12:08 SOLIDWORKS Sketch
- 13:05 Assembly Configurations
- 14:50 Historical Impacts
- 7:41 "You cannot have a parametric design until you first have a digital design and first have a characterized design."
- 12:44 "The less you have described everything with numbers directly, the more your whole model will be ready to cooperate with itself."
- 15:01 "Duplicating a design was free and instantaneous, almost — this is the essence of a digital design."
- 17:03 "The value that each engineer adds into it can get stacked up and up and up."

## Related videos

- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/how-to-design-the-best-in-the-world]]
- [[videos/excessively-technical-video-about-a-vacuum-adapter]]
- [[videos/how-hardware-enshitification-occurs-and-how-easily-we-can-beat-it]]
- [[videos/what-gpt5-is-doing-to-open-robotics-design-better-than-i-imagined]]
- [[videos/3d-printed-bearing-with-nylon-balls]]
