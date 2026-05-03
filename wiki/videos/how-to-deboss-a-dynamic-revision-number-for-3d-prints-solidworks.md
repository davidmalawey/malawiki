---
type: video
title: "How to DeBoss a Dynamic Revision Number for 3D Prints [Solidworks]"
video_id: "e63CJcZJ5TY"
url: "https://www.youtube.com/watch?v=e63CJcZJ5TY"
published: 2023-01-20
duration: "1:45"
tags: [solidworks, 3d-printing, revision-control, cad-tutorial, version-marking]
ingested: 2026-05-02
---

## Overview

A 1:45 [[entities/brands/solidworks|SolidWorks]] tutorial showing how to embed a live, property-linked revision number into a 3D-printed part as a debossed text feature. The text is a sketched cut-extrude that automatically updates whenever the file's Revision custom property changes — so reprinted parts always carry the right version.

## Key takeaways

- Use a sketch + cut-extrude tied to the file's Revision custom property (File > Properties > Custom > Revision) so the deboss text updates dynamically with the property.
- Recommended formatting: **DS ISO Bold** font, **6 mm** height, **0.5 mm** depth — least invasive depth that's still legible after printing.
- Place the text near the bottom of the part and oriented vertically (facing up during print) so you can verify mid-print that (a) the print started in the right direction and (b) you didn't load an outdated file.
- Workflow: open part, sketch on face, place text, click Link to Property, pick Revision, choose font/size, cut-extrude, then update the property and rebuild.

## Techniques demonstrated

- [[concepts/version-marking|Version marking]] — embedding revision metadata into the geometry itself.
- Property-driven text in CAD as a [[concepts/parametric-design|parametric]] feature.
- [[concepts/print-direction|Print direction]] reasoning — placing identifying features where they're visible early in the print.
- [[concepts/design-for-manufacturing|Design for manufacturing]] applied to FDM 3D printing.

## Tools used

- [[entities/brands/solidworks|SolidWorks]] CAD (sketch, cut-extrude, custom file properties)
- [[entities/tools/3d-printer|3D printer]] (target output)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:11] "we want it to print in that direction so we always place our revision number on facing vertical"
- [1:18] "0.5 mm — sort of the least invasive depth that you can still see the value pretty clearly"
- [1:34] "and it will automatically update the text"

## Related videos

- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge|How to design a 3D print (functional hinge example)]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part|How to design a functional printable open-source mechanical part]]
- [[videos/excessively-technical-video-about-a-vacuum-adapter|Excessively technical video about a vacuum adapter]] — also uses parametric SolidWorks features.
