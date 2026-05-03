---
type: video
title: "SCUTTLE Robot - how much power does it use? About 7w."
video_id: "Y3Fg8WhpVKE"
url: "https://www.youtube.com/watch?v=Y3Fg8WhpVKE"
published: 2020-09-30
duration: "4:58"
tags: [scuttle, power-budget, battery, 18650, raspberry-pi, measurement]
ingested: 2026-05-02
---

## Overview

David measures real power consumption of [[entities/projects/scuttle-robot|SCUTTLE]] across idle, driving, and accessory-on conditions, then back-calculates expected runtime from a 3-cell [[entities/tools/18650-cell|18650]] pack. Driving with [[entities/tools/raspberry-pi|Raspberry Pi]] and Bluetooth lands around 7.5 W; idle is 3.2 W. Pack capacity is roughly 31 Wh, yielding ~4 h driving or ~10 h idle.

## Key takeaways

- 3.2 W idle (with Bluetooth controller talking), 7.5 W driving, 12.5 W with accessory lights — measured with a [[entities/tools/usb-power-meter|USB power meter]] on the [[entities/tools/raspberry-pi|Raspberry Pi]].
- A single Panasonic 18650 cell test from 2006 (1 A constant discharge from 4.13 V to 2.8 V cutoff) yielded 3.02 Ah, ~10.5 Wh per cell — three cells give ~31 Wh pack.
- Conservative practice: stop discharging well before 2.8 V to avoid the steep voltage drop-off zone.
- Adding LIDAR (4 W on this rig) is a major fraction of the power budget — sensor choices matter.
- BeagleBone draws similar power to Raspberry Pi here, "something below 7.5 W" while driving.

## Techniques demonstrated

- [[concepts/power-budget-method|power budget method]]
- [[concepts/discharge-profile|discharge profile]]
- [[concepts/delta-power-measurement|delta power measurement]]
- [[concepts/instrument-resolution|instrument resolution]]

## Tools used

- [[entities/tools/18650-cell|18650 cell]]
- [[entities/tools/usb-power-meter|USB power meter]]
- [[entities/tools/raspberry-pi|Raspberry Pi]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]

## Materials used

- [[entities/materials/lipo-battery|LiPo battery]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Brands

- [[entities/brands/panasonic|Panasonic]]
- [[entities/brands/raspberry-pi|Raspberry Pi]]

## Related videos

- [[videos/scuttle-robot-autonomous-docking-by-machine-vision-for-wireless-charging]]
- [[videos/can-we-power-scuttle-robot-100-using-22-worth-of-solar-panels]]
- [[videos/3-ways-to-test-power-draw-for-mechatronics-designs]]
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify]]
