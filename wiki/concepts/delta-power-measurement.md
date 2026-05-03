---
type: concept
aliases: ["sensor power delta", "subtractive current measurement"]
tags: [power, measurement]
source_count: 2
---

# Delta power measurement

## Definition

Measure a sensor's real-world consumption by reading the host's total current with the sensor idle, then again with the sensor active, and taking the difference. Avoids the data-sheet trap of trusting a 3.3 V rating when the wall-side draw is what actually matters.

## Appears in

- [[videos/3-ways-to-test-power-draw-for-mechatronics-designs]]
- [[videos/scuttle-robot-how-much-power-does-it-use-about-7w]]

## Related

- [[concepts/instrument-resolution]]
- [[concepts/power-budget-method]]
- [[concepts/datasheet-vs-real-world-fit]]
