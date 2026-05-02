---
type: concept
aliases: ["L1/L2/L3 layers", "SCUTTLE layered architecture"]
tags: []
source_count: 2
---

# Layered software architecture

## Definition

SCUTTLE's L1/L2/L3 split. L1 = device drivers (one Python module per sensor/actuator). L2 = derivation (kinematics, fusion, threshold logic). L3 = decision-making (which behavior to execute, when). Each layer only depends on the layer below.

## Appears in

- [[videos/scuttle-robot-intro-to-software-architecture]]
- [[videos/introduction-to-quantam-import-parts-set-up-a-build]]

## Related

- [[concepts/sensor-actuator-controller-loop]]
- [[concepts/standalone-testable-modules]]
- [[concepts/bottom-up-troubleshooting]]
