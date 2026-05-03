---
type: video
title: "Embedded Computer users Should Know this Power Issue"
video_id: "EF9fIMgCdZw"
url: "https://www.youtube.com/watch?v=EF9fIMgCdZw"
published: 2025-03-20
duration: "14:43"
tags: [embedded, power, usb-c, sbc, raspberry-pi, beaglebone, robotics, mobile-power]
ingested: 2026-05-02
---

## Overview

David describes an invisible power problem affecting modern AI-capable single-board computers (SBCs): they expose USB-C ports but stay on the legacy 5 V rail, requiring 3+ A through a connector most adapters can only deliver 2 A on. The video is partly a question to the BeagleBone team — what's your recommended portable power solution? — and partly a call for the open-source robotics community to converge on best practices instead of reinventing custom power circuits per project.

## Key takeaways

- Latest BeagleBone and Raspberry Pi boards use USB-C for power but do NOT negotiate USB-PD higher voltages — they stay at 5 V.
- 15 W at 5 V means 3 A through the USB-C cable (vs. 1 A at 15 V); this triples conductor current and stresses the connector.
- The historical USB ecosystem maxed out at 5 V / 2 A. Millions of legacy adapters meet 5 V / 2 A but not 5 V / 3 A.
- Failure mode is invisible: the board boots and runs, but performance is throttled and weird symptoms (Wi-Fi disconnects, motor glitches) appear deep in the software stack.
- DC step-down converters (e.g., 12 V → 5 V at 3 A) are harder to find at quality than AC adapters; sketchy brands often misreport specs.
- Computer scientists and software developers are the largest user base of SBCs, but rarely have the electrical-evaluation expertise (e.g., a [[entities/tools/usb-power-meter|USB power meter]]) to catch the issue.
- For mobile/cordless robotics work the problem multiplies; David asks the community for known-good 5 V 3 A portable power banks and DC-DC modules.
- A [[entities/brands/canakit|Canakit]] Raspberry Pi 5 V 3.5 A adapter is shown as a positive reference (thick cable, full data-sheet labeling).

## Techniques demonstrated

- Reasoning about power = voltage × current and what that does to conductor stress at a connector.
- Diagnosing "invisible" undersupply: connectivity flakes and throttled compute as symptoms.
- Specifying power adapters by datasheet rather than label.

## Tools used

- [[entities/tools/usb-power-meter|USB power meter]]
- [[entities/tools/raspberry-pi|Raspberry Pi]] (versions 3, 4 shown)
- [[entities/tools/beaglebone-y-ai|BeagleBone Y-AI]] (the new AI-capable SBC being integrated into Scuttle)
- [[entities/tools/dc-dc-converter|DC-DC step-down converter]]
- USB-C cables, AC power adapters, portable power banks

## Brands mentioned

- [[entities/brands/raspberry-pi|Raspberry Pi]] — official 5.1 V 3.5 A adapter cited as a positive reference.
- [[entities/brands/beaglebone|BeagleBone]] (beaglebone.org) — open-source hardware org; David is integrating Y-AI into Scuttle.
- [[entities/brands/canakit|Canakit]] — Raspberry Pi kit reseller with quality power adapters.
- [[entities/brands/texas-instruments|Texas Instruments]] — TI Edge AI board used in a Scuttle variant; same power-portability struggle.
- Distributors: Mouser, Digi-Key, Element 14 / Newark / Avnet.

## Projects

- [[entities/projects/scuttle-robot|Scuttle]] — the BeagleBone Y-AI integration is the immediate driver for resolving this.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related concepts

- [[concepts/usb-pd-vs-5v-power|USB-PD vs. 5 V legacy power]]
- [[concepts/invisible-power-undersupply|Invisible power undersupply]] — boots fine, fails downstream.
- [[concepts/instrument-resolution|Instrument resolution]] — having a USB power meter is what makes this visible.

## Notable timestamps

- 1:10 BeagleBone Y-AI, Pi 5
- 5:00 Portable energy
- 6:15 Invisible problem
- 7:00 DC converter issues
- 9:30 Corded scenario
- 10:30 Cordless scenario

## Related videos

- [[videos/a-multidisciplinary-engineering-lab-tour-all-types-of-actuators|A Multidisciplinary Engineering Lab Tour]] — same lab, same power-bench equipment.
