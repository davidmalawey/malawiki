---
type: concept
aliases: ["datasheet gap", "spec vs reality"]
tags: [design-philosophy, qa]
source_count: 6
---

# Datasheet vs. real-world fit

## Definition

The PH1 / Dinkle terminal mismatch and the Molex KK pin geometry both demonstrate the same gap: datasheets describe nominal geometry, real-world parts have tolerance bands, and a design that assumes the nominal will fail at the band's edges. Spec to the band, not the centerline.

## Appears in

- [[videos/disassemble-molex-kk-close-up-connector]]
- [[videos/modify-a-screwdriver-for-electronics-mechatronics]]
- [[videos/scuttle-robot-unbox-solder-mount-encoder-pcb-to-bracket]]
- [[videos/flashforge-creator-pro2-setup-first-print-in-4k-resolution]]
- [[videos/scuttle-robot-assembling-wheels-and-belt]]
- [[videos/scuttle-robot-gluing-the-wheel-pulleys-version-1-0]]

## Related

- [[concepts/tolerances]]
- [[concepts/borrowing-tolerances]]
- [[concepts/calibrate-the-humans]]
