---
type: video
title: "Introduction to QuantAM - import parts & set up a build"
video_id: "kjLAztgDgHw"
url: "https://www.youtube.com/watch?v=kjLAztgDgHw"
published: 2019-06-12
duration: "4:21"
tags: [metal-am, quantam, renishaw, build-prep, slicing, supports]
ingested: 2026-05-02
---

## Overview

David walks through [[entities/tools/quantam|QuantAM]], the Renishaw build-prep software, demonstrating the orientation, support, layout, material, and review stages required to set up a metal-AM build for the [[entities/tools/renishaw-am400|Renishaw AM400]]. He imports a part, applies a Z-offset, generates medium supports, instances the part across the build plate, assigns a stainless-steel stripe-pattern material profile, and reviews the per-layer scan paths and estimated 7h37m build time.

## Key takeaways

- The gray box represents the build plate; the workflow stages (orientation → support → layout → material → review) are followed in sequence.
- Orientation stage: select downward surface, apply Z-offset (2mm shown) so the part floats above the plate to make room for supports.
- Support stage: pick a profile (medium supports demoed), use auto-highlight to mark regions needing support, then auto-generate.
- Layout stage: instance parts via dialog or by drag-arrow; hold Shift to box-select multiples, Alt-drag to relocate, then re-instance for grids.
- Material stage: stainless-steel stripe-pattern profile assigns scan parameters per part — up-skin power 160 W, hatch power 200 W, point distance 60 microns, exposure time 80 microseconds.
- Review stage: purple = up-skin, red = border, yellow = interior hatching; layers rotate hatch direction; "show scan points" reveals every laser exposure (slow to render).
- Final summary: build time (~7h37m, fairly accurate), build height, layer count, part volume, and support volume; cost estimate is unreliable.

## Techniques demonstrated

- [[concepts/digital-manufacturing|digital-manufacturing]] — slicing and parameter assignment in the metal-AM build-prep workflow.
- [[concepts/parametric-design|parametric-design]] — instancing identical parts via a tool dialog or drag-arrow.
- [[concepts/print-direction|print-direction]] — orientation stage chooses the downward surface and Z-offset.
- [[concepts/speeds-and-feeds|speeds-and-feeds]] — laser power, point distance, and exposure time form the metal-AM analog of cutting speeds/feeds.
- [[concepts/layered-software-architecture|layered-software-architecture]] — stage-based UI (orientation, support, layout, material, review) walks the operator through the dependencies.

## Tools used

- [[entities/tools/quantam|QuantAM]] (Renishaw build-prep software)
- [[entities/tools/renishaw-am400|Renishaw AM400]] (target machine)

## Materials used

- [[entities/materials/stainless-steel|stainless steel]] (stripe-pattern material profile)

## Brands mentioned

- [[entities/brands/renishaw|Renishaw]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable timestamps

- 0:55 — The Layout stage.
- 2:18 — Up-skin power 160 W; hatch power 200 W; 60-micron point distance; 80-microsecond exposure.
- 2:45 — Review stage: purple/red/yellow scan-line color coding.
- 3:28 — Show Scan Points view (per-exposure points).
- 3:53 — Build time and summary statistics.

## Related videos

- [[videos/renishaw-am400-should-this-thing-be-loose]]
- [[videos/multidisciplinary-design-optimization-2016-masters-thesis-presentation]]
