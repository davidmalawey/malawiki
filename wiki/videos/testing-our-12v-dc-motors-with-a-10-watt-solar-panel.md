---
type: video
title: "Testing Our 12V DC Motors with a 10 Watt Solar Panel"
video_id: "KB7mwN5sUbw"
url: "https://www.youtube.com/watch?v=KB7mwN5sUbw"
published: 2020-11-15
duration: "1:37"
tags: [solar, scuttle, dc-motor, power-budget, field-test]
ingested: 2026-05-02
---

## Overview

A short outdoor field test: David runs a 12V DC motor directly off a $11 "10 watt" solar panel and measures voltage and wattage under no-load and loaded conditions. The goal is to evaluate whether solar can sustain [[entities/projects/scuttle-robot|SCUTTLE]], which only draws about 7 watts to drive around — meaning two such panels could keep it running indefinitely.

## Key takeaways

- No-load motor sees ~21V from the panel; under partial cloud cover that drops to ~19V at 6W with a load.
- The panel charges the SCUTTLE battery pack at 12.4V / 4.7W when the pack is mostly full — the regulator caps further intake.
- A half-charged pack would accept more than 4.5W; charge acceptance scales with state-of-charge.
- Two $11 panels would provide enough headroom to run SCUTTLE perpetually (panel cost vs. SCUTTLE's ~7W consumption).

## Techniques demonstrated

- [[concepts/solar-charging|solar charging]]
- [[concepts/power-budget-method|power budget method]]
- [[concepts/discharge-profile|discharge profile]] (charge-acceptance side of the same curve)
- [[concepts/dc-motor-fundamentals|DC motor fundamentals]]

## Tools used

- [[entities/tools/solar-panel|solar panel]] (~10W rated, ~$11)
- [[entities/tools/dc-gearmotor|DC gearmotor]] (12V SCUTTLE motor)
- [[entities/tools/multimeter|multimeter]] / inline wattmeter

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:35 "Three watts so we need more motors — I can put a load on this."
- 1:14 "12.4 and 4.7 watts. Probably the regulator is not going to let it accept much more voltage."
- 1:25 "Man, I can feel the sun just searing me — this is really nice."

## Related videos

- [[loading-50-watts-on-cheap-dc-boost-converter-quick-test]]
- [[insights-in-real-world-battery-energy-that-you-can-verify]]
- [[3-ways-to-test-power-draw-for-mechatronics-designs]]
- [[fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
