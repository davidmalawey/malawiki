---
type: concept
aliases: [print orientation, layer direction]
tags: [3d-printing, fdm, design-for-manufacture]
source_count: 14
---

# Print direction

## Definition

The orientation of a part on the printer's build plate determines the direction of layer lines. Because FDM parts are weaker along the layer-separation axis, part orientation is a first-order design decision, not a printing preference.

## How David uses it

In [[videos/borrow-a-tolerance-mindset-for-designers]], David points out that loaded press-fit holes must be perpendicular to print lines. A shaft going through a hole whose axis parallels the print lines will split the part along the layers under side load; a shaft whose axis is perpendicular to the layers spreads contact over many layers and resists splitting.

This is cited as a baked-in design feature of [[entities/projects/scuttle-robot|SCUTTLE]] parts — "every single part of design for 3D printing such as the consideration for the print direction while we're achieving strength etc."

## Related

- [[entities/tools/3d-printer]]
- [[concepts/plastic-compressibility]]
- [[concepts/borrowing-tolerances]]

## Appears in

- [[videos/borrow-a-tolerance-mindset-for-designers]]
- [[videos/design-enclosures-for-electronics-using-mechanical-mindset]]
- [[videos/excessively-technical-video-about-a-vacuum-adapter]]
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/i-applied-toyota-root-cause-analysis-to-the-sticky-lids-heres-my-solution]]
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]]
- [[videos/scuttle-robot-servo-arm-design-v1-overview-using-pvc-3d-prints-and-low-cost-part]]
- [[videos/introduction-to-quantam-import-parts-set-up-a-build]]
- [[videos/scuttle-robot-modifying-the-wheel-pulley-in-solidworks]]
- [[videos/scuttle-robot-printed-parts-orientations]]
