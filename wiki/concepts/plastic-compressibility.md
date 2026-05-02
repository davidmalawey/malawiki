---
type: concept
aliases: [plastic compression, elastic compliance]
tags: [3d-printing, tolerances, drilling]
source_count: 3
---

# Plastic compressibility

## Definition

3D-printed plastic is compliant — it compresses slightly under a drill bit and springs back, so the finished hole is narrower than the bit's nominal diameter.

## How David uses it

In [[videos/borrow-a-tolerance-mindset-for-designers]], David drills the [[entities/projects/scuttle-robot|SCUTTLE]] wheel-bracket hole using an **8.03 mm bit for an 8 mm nominal hole** — the 0.03 mm oversize accounts for the plastic stretching, then compressing back after the bit passes. This is the only post-processing operation the SCUTTLE design requires, and it's documented as intentional rather than fudged.

## Related

- [[concepts/print-direction]]
- [[concepts/borrowing-tolerances]]
- [[entities/tools/3d-printer]]

## Appears in

- [[videos/borrow-a-tolerance-mindset-for-designers]]
- [[videos/design-enclosures-for-electronics-using-mechanical-mindset]]
- [[videos/mechanical-design-tutorial-for-a-hub]]