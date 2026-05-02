---
type: concept
aliases: ["vision-not-encoders"]
tags: [robotics, sensing, control]
source_count: 5
---

# Vision-driven kinematics

## Definition

Measure the end effector and target only via vision; skip joint encoders entirely. Removes a large source of additive error (each joint encoder's tolerance compounds along the kinematic chain) and matches how humans coordinate movement.

## Appears in

- [[videos/human-inspired-bio-inspired-ideas-missing-in-modern-robots]]
- [[videos/scuttle-robot-nextec-team-tests-computer-vision-docking]]
- [[videos/scuttle-robot-autonomous-docking-by-machine-vision-for-wireless-charging]]
- [[videos/testing-out-nvidia-isaac-sdk-and-isaac-sim-for-robotics-on-pc]]
- [[videos/scuttle-robot-how-to-run-color-tracking-v1-py-computer-vision-program]]

## Related

- [[concepts/bio-inspired-dynamics]]
- [[concepts/sensor-actuator-controller-loop]]
