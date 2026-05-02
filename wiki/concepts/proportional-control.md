---
type: concept
aliases: ["P control", "Kp control"]
tags: []
source_count: 1
---

# Proportional control

## Definition

Control-effort term `u_p = Kp × error`, where error = target − measured. The simplest and most common closed-loop response. SCUTTLE example: Kp=0.04, error=8.3 → u_p ≈ 0.33 (33% PWM duty).

## Appears in

- [[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]]

## Related

- [[concepts/pid-control]]
- [[concepts/closed-loop-feedback]]
- [[concepts/control-oscillation]]
