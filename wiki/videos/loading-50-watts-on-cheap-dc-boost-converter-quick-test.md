---
type: video
title: "Loading 50 Watts on Cheap DC Boost Converter - Quick Test"
video_id: "Tf5gEjGLlgI"
url: "https://www.youtube.com/watch?v=Tf5gEjGLlgI"
published: 2022-11-02
duration: "4:08"
tags: [boost-converter, dc-dc, power, soldering-iron, bench-test, voltage-regulation]
ingested: 2026-05-02
---

## Overview

Quick bench test of a roughly $3 adjustable DC boost converter (rated 5A, three-for-$10). David feeds it from a stable 12V supply, dials the output up near 20V, and loads it with a soldering iron pulling ~47W to see whether the regulator holds voltage and how hot it gets.

## Key takeaways

- Cheap boost converter held ~20.2V at ~2.5A (47W) while heating to about 50C — never reaching peak temperature in the test window.
- Stepping back down to ~12.8V output, it pulled 18–20W and warmed to 44C — surprisingly steady for the price.
- The trim potentiometer is highly non-linear; many turns are needed to drop a few volts in some ranges.
- Verdict: fine for fans, LEDs, and other tolerant loads; not appropriate for sensitive instrumentation. Worth a higher-fidelity voltage/current sweep next.
- A 5A claim at 40V output is implausible at this price — the converter will saturate well before that.

## Techniques demonstrated

- [[concepts/instrument-resolution|Bench-instrument resolution]] (using inline USB-style power meter to read V/A/W)
- [[concepts/share-the-failure|Share the failure]] (publishing a quick "good enough" test before a polished one)

## Tools used

- [[entities/tools/dc-dc-converter|DC-DC boost converter]] (cheap adjustable, $3-class)
- [[entities/tools/soldering-iron|Soldering iron]] (~60W load)
- [[entities/tools/usb-power-meter|USB / inline power meter]]
- 12V bench power supply

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/loads-of-stuff-you-can-add-to-a-12v-robot]]
- [[videos/build-a-battery-adapter-to-power-the-whole-lab]]
- [[videos/build-a-diy-power-supply-a-tutorial-using-openbox]]
- [[videos/embedded-computer-users-should-know-this-power-issue]]
