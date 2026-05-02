---
type: video
title: "How to Design the Best in the World"
video_id: "gjGNDaH15Ik"
url: "https://www.youtube.com/watch?v=gjGNDaH15Ik"
published: 2025-06-21
duration: "23:33"
tags: [design-method, open-source, benchmarking, cad, parametric, scuttle]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] outlines a method for producing genuinely best-in-the-world 3D-printable designs as a hobbyist designer. The argument: closed-box products can never be globally verified, so open-source publication on platforms like [[entities/brands/grabcad|GrabCAD]] and Printables is the only path to a provable best-in-the-world result. He walks through three worked examples — a hex-bit rack, a printable bearing, and a spray-can cap — to show the loop of benchmarking, iterating, and inviting expert feedback.

## Key takeaways

- A best-in-the-world claim requires (a) a defined user (you), (b) measurable benchmarks against the alternatives, and (c) a published artifact discoverable by people more expert than you.
- The design must remain editable: keep the native [[entities/brands/solidworks|CAD]] file (not just an STL) so a smarter contributor can revise it.
- Use [[concepts/parametric-design|parametric design]] so dimensions like inner diameter can be retuned by other users for adjacent use cases.
- Credit the prior author when you fork — preserve the chain of provenance so future improvers can trace it back.
- Free, open designs raise the bar for paid competitors: when Linux competed with Microsoft, Microsoft had to give the OS away. The same dynamic applies to a $20 USB-on-power-tool dongle versus an open one.
- This is the same operating principle behind [[entities/projects/scuttle-robot|SCUTTLE Robotics]] — every belt, pulley, and decision rationale is published so external experts can suggest improvements.

## Techniques demonstrated

- Benchmarking against existing parts on the qualities the user cares about.
- Forking a [[entities/brands/grabcad|GrabCAD]] design, saving an unmodified copy, then editing.
- Versioning published designs with revision numbers and feature folders.
- [[concepts/parametric-design|Parametric design]] to expose key dimensions to downstream users.

## Tools used

- [[entities/brands/grabcad|GrabCAD]], Printables, Thingiverse (publication targets)
- [[entities/brands/solidworks|SolidWorks]] (native CAD)
- [[entities/tools/3d-printer|3D printer]]

## Projects

- The hex-bit holder rack that mounts to existing [[entities/materials/d-rail|D-rail]] systems.
- A printable bearing forked from another GrabCAD user (Daniel) and reparameterized for various tube diameters including PVC.
- A spray-can / lubricant-bottle cap that fits 12+ different bottle types — published free on GrabCAD.
- [[entities/projects/scuttle-robot|SCUTTLE Robotics]] referenced as a full-system example of this design philosophy.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- Daniel — original designer of the printable bearing David forked.
- Linus Torvalds — invoked as the prototypical open-source committer.

## Related videos

- [[videos/what-gpt5-is-doing-to-open-robotics-design-better-than-i-imagined|what GPT5 is doing to open robotics design]] — shows what becomes possible once parametric designs are characterized digitally.
