---
type: video
title: "I Applied Toyota Root Cause Analysis to the Sticky Lids - Here's My Solution"
video_id: "IvZXdxWh7dg"
url: "https://www.youtube.com/watch?v=IvZXdxWh7dg"
published: 2025-10-03
duration: "20:18"
tags: [root-cause-analysis, toyota, open-source-hardware, parametric-design, pdca, 3d-printing]
ingested: 2026-05-02
---

## Overview

David applies Toyota Business Practice root-cause analysis to a household nuisance — paint, glue, and chemical jars whose lids stick shut and ruin the contents. He traces the problem to a feedback loop where insufficient initial tightening allows fluid to harden in the threads, which then prevents future sealing. His countermeasure is a 3D-printable hex-shaped grip that lets users hand-tighten lids hard enough to seal, paired with a behavior change. The video doubles as a tutorial on how to publish open-source hardware so it delivers value to every audience tier (no printer, has printer, has CAD skills, has engineering skills, has a small business).

## Key takeaways

- Counterintuitive root cause: tighter sealing on the way in produces *looser* removal months later, because hardened residue is what jams the threads.
- A countermeasure used only one direction (loosening) reinforces the failure mode in the other direction (sealing).
- 22, 35, and 45 mm cap diameters cover a surprising fraction of common lab/paint/glue jars — one parametric model spawns three variants.
- Open-source hardware delivers stacked value: STL for printers, STEP for CAD users, source-of-truth Solid Works file for engineers, problem narrative for everyone.
- Embedding version numbers directly in the printed STL preserves provenance after the file is shared away from its host page.
- Free open hardware doesn't kill private competitors — it raises the floor and forces them to outperform "free + 30 cents of plastic."

## Techniques demonstrated

- [[concepts/root-cause-analysis|root-cause analysis]] (Toyota Business Practice)
- [[concepts/pdca|plan-do-check-act (PDCA)]]
- [[concepts/parametric-design|parametric design]] with configuration tables
- [[concepts/open-source-hardware-publishing|open-source hardware publishing]] — packaging STL + STEP + parametric source + narrative
- [[concepts/version-marking|version marking]] embedded in STL geometry

## Tools used

- [[entities/tools/3d-printer|3D printer]]
- [[entities/brands/solidworks|SolidWorks]] (configuration tables for variants)
- Off-the-shelf strap wrench / oil filter wrench (the tool the grip replaces for tightening)

## Projects

- [[entities/projects/grip-22|Grip-22]] — open-source hex grip published on [[entities/brands/grabcad|GrabCAD]]
- [[entities/projects/openlab-project|OpenLab Project]] (qr.net/openlabproject)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 6:54 "If I close it tighter when I'm sealing, it is looser when I'm loosening. Not intuitive."
- 19:55 "I don't want to live in a country where we go to the moon twice and we still have to deal with these small problems that could have been solved a long time ago."

## Related videos

- (Other open-source design and SCUTTLE-related videos)
