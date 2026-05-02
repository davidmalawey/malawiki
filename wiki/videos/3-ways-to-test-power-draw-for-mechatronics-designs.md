---
type: video
title: "3 Ways to test Power Draw for mechatronics designs"
video_id: "s4Syzco1ziM"
url: "https://youtu.be/s4Syzco1ziM"
published: 2022-12-14
duration: "9:54"
tags: [mechatronics, capstone, power-measurement, instrumentation, battery-testing, scuttle]
ingested: 2026-05-02
---

## Overview

Companion to the [[videos/power-budget-explained-mechatronics-capstone-projects|power-budget walkthrough]]. David runs through three power-measurement instruments available in the [[entities/places/texas-am-lab|MXET lab]] and shows when to reach for each: USB/USB-C inline meters for sensors and microcontroller-class loads, an Anderson-Powerwerx-style DC meter for higher-wattage devices like pumps and motors, and the West Mountain Radio Computerized Battery Analyzer (CBA) for long-form battery discharge curves and charge-monitoring tests.

## Key takeaways

- USB inline meter: cheapest, perfect for measuring a Raspberry Pi-class load with sensors plugged in. Take a delta — read with the MCU idling, then read again with the sensor active — to back out the sensor's real consumption rather than trusting the data sheet's 3.3V number.
- The conversion from 5V down to 3.3V on the host board is lossy, so measuring at the wall is more honest than calculating from the rail spec.
- DC meter (Powerwerx-branded or knock-off): rated to 150A, takes Anderson connectors directly. Always attach alligator clips *before* plugging power in to avoid short circuits.
- A 12V wall adapter rarely outputs exactly 12V. Measuring no-load vs. loaded voltage on the meter shows the actual sag and tells you whether your supply is decent quality.
- CBA V5: USB to PC, free software. Two test modes — discharge (cutoff voltage + target amps, runs until cutoff and reports total Ah/Wh) and charge monitor (logs voltage only, with a separate ammeter in series).
- Selection rule: CBA for accurate energy-over-time logs; Powerwerx for 1-150W devices; USB meter for everything else and DIY harnesses (a USB-PD trigger board or breakout makes any 5V load measurable).
- Crimping compatible terminals everywhere on your bench reduces hairball wiring and lets you swap testers in seconds.

## Techniques demonstrated

- [[concepts/instrument-resolution]] — picking the meter whose range matches the device
- [[concepts/discharge-profile]] — CBA discharge test for true Ah/Wh
- Delta-power measurement (idle vs. active reading) for sensor characterization
- Charge-monitor test setup (parallel voltage probe + series ammeter)

## Tools used

- [[entities/tools/usb-power-meter|USB power meter]] (basic + 1mA-resolution model)
- [[entities/tools/usb-pd-trigger-board|USB-PD trigger / breakout board]]
- Powerwerx (or off-brand) DC power meter, up to 150A
- Computerized Battery Analyzer (CBA V5, West Mountain Radio)
- [[entities/tools/anderson-connector|Anderson connectors]]
- Alligator clips
- 12V peristaltic pump (load example)
- Infrared temperature sensor (sensor example)
- [[entities/tools/multimeter|Multimeter]] (implied)

## Materials used

(none specific)

## Projects

(none — instrumentation tutorial)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:02] "These three kinds of power meters can pretty much cover any of the mechatronics projects you want to build."
- [3:33] "Always attach these alligator clips before we plug in our connector — so that we don't have a chance of the clips contacting something and short-circuiting."
- [4:48] "The wattage of the device depends on the voltage and the wattage will vary from the data sheet."
- [9:09] "By crimping the compatible terminals on your electronics, you might save a lot of hairballs of wires on your desk."

## Related videos

- [[videos/power-budget-explained-mechatronics-capstone-projects]] — the planning side; this video is the measurement side
- [[videos/how-to-crimp-anderson-connectors]] — the crimp workflow that lets you connect to the Powerwerx meter
- [[videos/embedded-computer-users-should-know-this-power-issue]]
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify]]
- [[videos/build-a-diy-power-supply-a-tutorial-using-openbox]]
