---
type: concept
aliases: ["pose integration", "dead reckoning"]
tags: []
source_count: 1
---

# Numerical integration of pose

## Definition

Accumulating local-frame velocity increments (after rotation into the global frame) into a running global (x, y, theta) at each control tick. The simplest dead-reckoning algorithm and the substrate of [[videos/navigationvectors-part1-global-position-increment|NavigationVectors part 1]].

## Appears in

- [[videos/navigationvectors-part1-global-position-increment]]

## Related

- [[concepts/rotation-matrix]]
- [[concepts/differential-drive-kinematics]]
