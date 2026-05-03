---
type: concept
aliases: ["compress function", "duty-cycle compression", "DC motor dead band trim"]
tags: [motor-control, pid]
source_count: 2
---

# Dead-band compensation

## Definition

A piecewise mapping applied between commanded duty cycle and PWM output that compresses (skips most of) the low-duty range where a [[entities/tools/dc-gearmotor|DC gearmotor]] produces no motion due to internal friction. Two parameters: an initial slope, and the critical y-inflection (the duty cycle at which motion actually begins). Used in SCUTTLE's `motor.pi`. Different from naive thresholding — preserves torque differentials needed by PID during transients.

## Appears in

- [[videos/reduce-the-dead-band-from-your-dc-motors-with-this-function]]
- [[videos/scuttle-robot-open-loop-vs-closed-loop-speed-control]]

## Related

- [[concepts/pwm]]
- [[concepts/dc-motor-fundamentals]]
- [[entities/projects/scuttle-robot]]
