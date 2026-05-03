---
type: concept
aliases: [borrow a tolerance, borrowed precision]
tags: [design-philosophy, assemblies, tolerances]
source_count: 13
---

# Borrowing tolerances

## Definition

Instead of manufacturing precision yourself (expensive), find an already-mass-produced part whose tolerances are tight — for reasons that have nothing to do with your project — and design around *its* precision. The classic example is the [[entities/tools/ball-bearings|ball bearing]]: 3 cents each, precision no hobbyist machining can match, and it will self-center in a loose 3D-printed ring.

## How David uses it

In [[videos/borrow-a-tolerance-mindset-for-designers]]:

- **Balls** centering a hub — [[entities/tools/ball-bearings|ball bearings]] handle nominal contact, team effort, distributed tolerancing, and force distribution.
- **Paper clip wire** for a flange spring — manufacturers care about diameter and flatness for their own reasons; you get the tolerance for free.
- **[[entities/materials/spring-steel|Spring steel]]** for deterministic elastic behavior that 3D-printed ABS can't deliver.
- **[[entities/materials/hdpe|HDPE]] tubing** from water-system supply chains for cheap, tough, low-friction sliding surfaces.
- **A golf tee** as a repeatable positioning reference when you don't need the absolute dimension.
- **[[entities/tools/calipers|Calipers]]** used once on one ball, so subsequent balls can be compared relatively without absolute re-measurement.

The idea shows up implicitly elsewhere:

- [[videos/label-supplies-to-multiply-results]] — manufacturer labels, copyright dates, and compatibility manuals carry data they didn't mean to share. You "borrow" their information in the same way you borrow tolerances.

## Variations

- **Borrowed toughness** — use HDPE / urethane where impact resistance matters, rather than printing a thick-walled part in a brittle material.
- **Borrowed smoothness** — same HDPE as a sliding surface where 3D-print surface finish is unreliable.
- **Borrowed data** — [[concepts/free-data|free data]] from labels and manuals that companies have already paid to generate.

## Related

- [[concepts/plastic-compressibility]]
- [[concepts/screw-as-spring]]
- [[concepts/parametric-design]]

## Appears in

- [[videos/borrow-a-tolerance-mindset-for-designers]]
- [[videos/label-supplies-to-multiply-results]]
- [[videos/these-two-genius-designers-are-building-our-future]]
- [[videos/design-enclosures-for-electronics-using-mechanical-mindset]]
- [[videos/how-to-drill-a-hole-in-metal-plastic-wood-and-laminate]]
- [[videos/build-a-diy-power-supply-a-tutorial-using-openbox]]
- [[videos/excessively-technical-video-about-a-vacuum-adapter]]
- [[videos/we-discovered-a-shape-and-its-not-a-big-deal]]
- [[videos/how-to-design-a-3d-print-with-example-funtional-hinge]]
- [[videos/mechanical-design-tutorial-for-a-hub]]
- [[videos/highly-engineered-emt-conduit-parts-to-study-before-designing]]
- [[videos/scuttle-robot-prep-your-axle-hole-wear-a-helmet]]
- [[videos/scuttle-robot-assembling-wheels-and-belt]]
