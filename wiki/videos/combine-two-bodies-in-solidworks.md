---
type: video
title: "Combine Two Bodies in Solidworks"
video_id: "F7rsOU_ex5Y"
url: "https://www.youtube.com/watch?v=F7rsOU_ex5Y"
published: 2019-06-20
duration: "5:26"
tags: [solidworks, cad, multibody, 3d-printing, laminar-flow]
ingested: 2026-05-02
---

## Overview

A SolidWorks tutorial showing how to use the Combine feature (subtract mode) so that one part conforms exactly to the mating surface of another. David designs an inlet diffuser whose underside matches the contour of the laminar flow orifice that sits below it, splitting one ideal monolithic part into two 3D-printable bodies that can be glued together. The tutorial supports the [[videos/3d-printed-laminar-flow-nozzle-construction|laminar flow nozzle build]].

## Key takeaways

- For a 3D-printable assembly, sometimes the right move is to split a single conceptual part into two pieces, each with its preferred print orientation, then glue them.
- The Combine feature with the Subtract option lets you carve one body to match the geometry of another instead of measuring and re-modeling the mating surface.
- For Combine to recognize separate bodies, the source revolve/extrude must have the "Merge result" option deselected — otherwise SolidWorks fuses everything into a single body.
- Leave a small intentional gap between mated 3D-printed surfaces to absorb dimensional deviations and to make room for the glue layer.

## Techniques demonstrated

- [[concepts/multibody-modeling|multibody modeling]]
- [[concepts/merge-result-toggle|merge-result toggle]]
- [[concepts/borrowing-tolerances|borrowing tolerances]] (the diffuser borrows the orifice's surface geometry)
- [[concepts/design-for-3d-printing|design for 3D printing]]
- [[concepts/print-direction|print direction]]
- [[concepts/working-placeholder-design|working placeholder design]] (the small offset gap eyeballed for glue + tolerance stack)

## Tools used

- [[entities/tools/solidworks|SolidWorks]]

## Projects

- [[entities/projects/laminar-flow-nozzle|laminar flow nozzle]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [3:13] "merge result says I'm going to create this revolved feature and I'm going to take whatever volume that it occupies and have that volume merged with the existing features in the part — well we need to have it not merged so that they can still be separate bodies."
- [4:55] On leaving a glue gap: "I just eyeballed it… the top surface here is a little bit higher than it would be if I had mated these two components."

## Related videos

- [[videos/3d-printed-laminar-flow-nozzle-construction]]
- [[videos/solidworks-2019-create-configurations-with-various-pattern-instances]]
- [[videos/solidworks-recognize-features-manually-tutorial-with-example]]
