---
type: video
title: "More about USB than you ever wanted to know"
video_id: "9c9-YUSbgYs"
url: "https://www.youtube.com/watch?v=9c9-YUSbgYs"
published: 2024-07-25
duration: "57:46"
views: 281880
likes: 6239
tags: [electronics, usb, power, mechatronics, teaching]
ingested: 2026-04-24
---

# More about USB than you ever wanted to know

## Overview

A 58-minute teardown and teaching pass on USB — cables, adapters, power budgets, and the debugging pitfalls that catch students. David slices cables open on camera to show what separates a good 4-wire cable from a charging-only 2-wire cable, then walks through voltage-vs-current adapter testing, shared-bus limitations, and when (and when not) to use Quick Charge. PD / USB-C is deferred to a future video.

## Key takeaways

- **Cables with only two terminals are power-only.** If you need data — photos, serial, MCU comms — you need all four wires. Shielding and a [[concepts/ferrite-noise-suppression|ferrite core]] matter only for the data pair.
- **Cheap "ferrite cores" are sometimes just rubber.** Test with a magnet — real ferrite is magnetic.
- **USB is a shared bus.** Every port on one motherboard controller shares one data pair and one 5V rail. Charging a phone while streaming from a USB mic on the same bus often causes the disconnect errors students can't explain.
- **Don't draw power from the Arduino 5V pin for LED strips or actuators.** Dupont header contacts are low-pressure signal connectors; the on-board regulator isn't sized for amps. This is the single most common student-project failure mode David sees.
- **[[concepts/quick-charge|Quick Charge]] (QC) negotiates 9V over the data pins.** That makes it dangerous on a shared splitter — if one device requests 9V, every 5V device on that bus could receive 9V. Avoid QC outside of dedicated single-port charging.

## Techniques demonstrated

- Slicing a cable to inspect gauge, shielding, and ground continuity between housings.
- Testing a 5V adapter's regulation curve by pulling loads from 0A up to its rated limit and past the cliff.
- Using a ~$5 [[entities/tools/usb-power-meter|USB power meter]] to measure mAh consumed over time (integral of current) instead of instantaneous amps — necessary for variable-load devices.
- Sanity-check math: `V₁·I₁ = V₂·I₂`. When boosting 3V → 5V at 1A out, you need 1.67A in, plus ~20% for losses.
- [[concepts/instrument-resolution|Choosing instrument range]] — a kilowatt-hour meter is wrong by 10-20% reading USB-level power; use an instrument rated close to what you're measuring.

## Tools used

- [[entities/tools/usb-power-meter|USB power meter]] ($5-10, 0-20V range)
- USB breakout boards (packs of 5)
- Controllable current tester
- Cigarette-lighter 12V → USB adapter (as an over-specced protected supply)
- Boost regulator modules (3V → 5V)

## Hardware shown

- [[entities/brands/texas-instruments|Texas Instruments]] Launchpad (ships with a known-good micro USB cable)
- [[entities/brands/arduino|Arduino]] (5V pin, signal-level regulator)
- [[entities/brands/raspberry-pi|Raspberry Pi]] 3 (dual USB bus)
- Dremel charger (1A, well-labeled output)
- [[entities/brands/cooler-master|Cooler Master]] PSU (15A on 5V rail)
- 12V wall-warts with tunable potentiometer
- QC-era LG phone charger (9V boost)
- Wireless Qi charger (2-wire cable only charges at 5V; 4-wire cable triggers QC negotiation to 9V → 20W)

## Materials and concepts

- 4-wire USB anatomy: red (+5V, 22 AWG), black (GND, 22 AWG), green/white (D+/D-, 28 AWG)
- [[entities/materials/copper|Copper]] conductors, gold vs tin-plated terminals
- [[entities/materials/vinyl|Vinyl]] cable sheathing, cotton strength strands, foil shielding
- Lithium polymer cells (nominal 3.7V) and 18650 cells
- [[concepts/ferrite-noise-suppression|Ferrite core noise suppression]]

## Notable quotes / timestamps

- `[5:25]` "If the customer has a problem then we have a problem" — David quoting the principle he picked up at [[entities/brands/toyota|Toyota]] about why Apple polices its own cable quality.
- `[33:16]` "The most common error I see in student projects is that they're drawing power from an Arduino 5V pin" — then blaming Wi-Fi for the resulting power fluctuation.

## Related videos

- [[videos/borrow-a-tolerance-mindset-for-designers|Borrow a Tolerance]] — shares the "student Capstone mistakes" frame and the Toyota reference.
- [[videos/label-supplies-to-multiply-results|Label supplies to multiply results]] — the "write the measured result on a label" idea applies directly to characterizing adapters like this.

## Open threads

- PD / USB-C video promised but not yet ingested. Check for a follow-up once more transcripts land.
