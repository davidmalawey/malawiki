---
type: video
title: "Loads of stuff you can add to a 12v robot!"
video_id: "Mcer39NBsuc"
url: "https://www.youtube.com/watch?v=Mcer39NBsuc"
published: 2022-11-17
duration: "6:54"
series: "[[scuttle-robot]]"
tags: [scuttle, 12v, accessories, payload, peripherals, automotive, brainstorm]
ingested: 2026-05-02
---

## Overview

A whirlwind tour of off-the-shelf 12V devices David plugs straight into a SCUTTLE battery (~3-6A, ~40W) to demonstrate the design space a 12V mobile platform unlocks. Pumps, monitors, audio drivers, relays, voice assistants, sensors, solar panels, and even a printer all light up from the same source.

## Key takeaways

- A 12V SCUTTLE battery is roughly equivalent to an automotive accessory bus — anything that runs on a car (lighting, pumps, monitors) generally runs on SCUTTLE within the ~40W budget.
- Demonstrated loads: truck-style waterproof LED, USB-PD car-style outlet, vacuum/air pump, submerged water pump, 7-inch HDMI monitor (~5W), 10W audio driver + speaker, peristaltic dosing pump, Scuttle motor driver (+12 to -12V via PWM), 8-channel relay board, Echo Dot, voltage-monitor module, USB charge passthrough, and a 24V printer/scanner via boost converter.
- "Steer clear of the water on the table" — David notes the safety humor while running pumps near live electronics.
- Boost the 12V to 24V or 30V with a cheap converter to drive higher-voltage gear; respect the power budget (V*A).
- Sticking the SCUTTLE encoder magnet on the back of a peristaltic pump turns it into a metered dosing actuator.
- Solar charging: three 5V panels in series gives ~15V in bright sun, ~10V in dim — relies on the battery's BMS to soak it up safely.
- Action: walk an auto-parts store; many actuators run under 50W at 12V.

## Techniques demonstrated

- [[concepts/leverage-incumbent-engineering|Leverage incumbent engineering]] (auto parts ecosystem)
- [[concepts/parts-ecosystem-design|Parts ecosystem design]]
- [[concepts/usb-pd-vs-5v-power|USB-PD vs. 5V power]]
- [[concepts/solar-charging|Solar charging]]
- Encoder-magnet-as-dosing-counter trick

## Tools used

- [[entities/tools/dc-dc-converter|DC-DC boost converter]]
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver]] (Scuttle standard)
- Relay board (8-channel, ~$8)
- Peristaltic pump (12V)
- Vacuum pump, air pump, submerged water pump (all 12V)
- 7-inch HDMI monitor (12V)
- Audio driver / amplifier (12V, 10W)
- USB-PD trigger / car outlet
- [[entities/tools/solar-panel|Solar panel]] (5V each)
- [[entities/tools/usb-pd-trigger-board|USB-PD trigger board]]
- Battery voltage display module
- Echo Dot (Alexa)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- Alexa / Amazon Echo (referenced as a 12V-compatible accessory)

## Notable quotes / timestamps

- [0:08] "After you realize what you can do with 12 volts, the ideas are endless."
- [6:38] "Go to the auto parts store, just cruise the aisles — there's loads of actuators that run on 12 volts and they're all under 50 watts. It's time to explore. Put things on wheels."

## Related videos

- [[videos/loading-50-watts-on-cheap-dc-boost-converter-quick-test]]
- [[videos/build-a-payload-robot-start-to-finish-scuttle-v2-4]]
- [[videos/build-a-battery-adapter-to-power-the-whole-lab]]
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify]]
