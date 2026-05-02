---
type: entity
kind: tool
aliases: ["rotary encoder", "wheel-speed encoder"]
first_seen: "[[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]]"
tags: [sensor, robotics, scuttle]
source_count: 5
---

# Wheel encoder

Rotary encoder providing the live phi-dot wheel-speed signal used by SCUTTLE's closed-loop control. David flags rollover, sample rate, and resolution as encoder error sources. SCUTTLE's encoder PCB uses a magnetic sensor reading a [[entities/materials/diametric-magnet|diametric magnet]] glued to the wheel hub.

## Appears in

- [[videos/scuttle-robot-how-proportional-feedback-control-is-implemented-kp]]
- [[videos/scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-]]
- [[videos/scuttle-robot-nextec-team-tests-computer-vision-docking]]
- [[videos/scuttle-robot-unbox-solder-mount-encoder-pcb-to-bracket]]
- [[videos/scuttle-robot-soldering-the-i2c-bus-board]]

## Related

- [[concepts/closed-loop-feedback]]
- [[concepts/proportional-control]]
