---
type: concept
aliases: []
tags: []
source_count: 1
---

# Rotation matrix

## Definition

2x2 matrix that rotates a local-frame velocity vector into the global frame using the current heading angle theta. Core technique in the [[videos/navigationvectors-part1-global-position-increment|NavigationVectors]] code: at each tick, transform the local position increment, then add to the running global pose.

## Appears in

- [[videos/navigationvectors-part1-global-position-increment]]

## Related

- [[concepts/numerical-integration-of-pose]]
- [[concepts/differential-drive-kinematics]]
