---
type: video
title: "SCUTTLE Robot CAD Revisions - Watch Before Downloading STL Files"
video_id: "Dn0qTvfdMcU"
url: "https://www.youtube.com/watch?v=Dn0qTvfdMcU"
published: 2020-11-23
duration: "5:36"
tags: [scuttle, cad, version-control, stl, grabcad, github, revisioning]
ingested: 2026-05-02
---

## Overview

A versioning explainer for the open-source [[entities/projects/scuttle-robot|SCUTTLE robot]]. David lays out the rules he uses for the major-vs-minor revision numbers across whole-robot assemblies, individual 3D-printed parts, off-the-shelf parts, and subassemblies, plus where each format (SLDPRT, SLDASM, STEP, STL) lives between [[entities/brands/grabcad|GrabCAD]] and GitHub.

## Key takeaways

- Major change of the robot assembly = the integer changes (v1 → v2). Construction has changed significantly; offered as a SolidWorks assembly plus a STEP assembly on GrabCAD. The STEP version is preferred for browser navigation and cross-CAD compatibility.
- Minor change = decimal increments (2.1 → 2.2 → 2.3). Several small modeling improvements bundled together; design function unchanged. Latest version 2.2 / 2.3 at time of recording.
- Major part change (3D-printed): integer bump on the STL, released on GitHub. Old shape is incompatible with the new — you don't have to upgrade unless you want the performance gain.
- Minor part change: decimal bump, compatible with previous; released on GitHub and the old file is overwritten/deleted (history preserves the old version). Example shown: a flat region became curved to improve springiness on the battery pack clip.
- Off-the-shelf parts: no special version scheme. Updates (e.g. swapping a generic vendor model for a measured custom one) are batched until the next minor SCUTTLE assembly release.
- Major subassemblies (e.g. a new camera bracket): may get a new part number; if standalone, lives as its own GrabCAD assembly with link as accessory; if standardized, gets folded into the next minor scuttle release with BOM and software updates.

## Techniques demonstrated

- [[concepts/version-marking|version marking]]
- [[concepts/open-source-hardware-publishing|open-source hardware publishing]]
- [[concepts/documented-design-as-leverage|documented design as leverage]]
- [[concepts/parts-ecosystem-design|parts ecosystem design]]
- [[concepts/standards-as-open-source|standards as open source]]

## Tools used

- [[entities/brands/solidworks|SolidWorks]] (SLDPRT, SLDASM)
- [[entities/brands/grabcad|GrabCAD]] (assembly hosting)
- GitHub (STL hosting — no entity page needed yet)
- STEP / STL file formats

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:00 major assembly changes explained.
- 2:26 minor changes explained.
- 3:31 off-the-shelf parts handling.
- 4:24 subassembly changes (camera bracket as the example).

## Related videos

- [[scuttle-robot-v3-0-assembly-animated]]
- [[build-a-payload-robot-start-to-finish-scuttle-v2-4]]
- [[scuttle-robot-hardware-list-fasteners-screws-nuts-washers]]
- [[how-to-deboss-a-dynamic-revision-number-for-3d-prints-solidworks]]
- [[open-source-hardware-is-evolving]]
