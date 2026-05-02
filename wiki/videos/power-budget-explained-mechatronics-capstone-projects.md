---
type: video
title: "Power Budget Explained [Mechatronics Capstone Projects]"
video_id: "DKPFsVOTJpw"
url: "https://youtu.be/DKPFsVOTJpw"
published: 2022-11-20
duration: "12:18"
tags: [mechatronics, capstone, power-budget, electrical, design-method, scuttle]
ingested: 2026-05-02
---

## Overview

A walkthrough of the Excel power-budget template David built for [[entities/places/texas-am-lab|TAMU MXET]] capstone teams. The example data comes from the COVID-era capstone team that turned a [[entities/projects/scuttle-robot|Scuttle robot]] into a UV-light sanitizing machine. Each tab of the spreadsheet attacks a different decision: peak power, runtime, system power map, exclusions, and justifications.

## Key takeaways

- A power budget is not a deliverable for its own sake — it's the artifact you use to size a battery, pick wires, and choose a DC-DC converter without surprises at demo day.
- The spreadsheet starts broad (peak power demand of the whole machine) and narrows toward specific decisions (cable gauge, connector size, converter rating).
- Group devices into assemblies, then group assemblies by operating mode (e.g. "moving the arm 25% of the time") to get a realistic average power rather than a worst-case sum.
- The "system power map" tab catches the failure mode where the battery is fine overall but a downstream rail (e.g. the 24V boost converter) can't supply enough amps for the loads bonded to it.
- Cheap Amazon DC-DC converters are roughly 80% efficient; high-end converters can hit 90%. Plan power losses into the budget.
- Skipping a question on the template is fine — but you should be able to justify why it's not relevant rather than just leaving it blank.

## Techniques demonstrated

- [[concepts/invisible-power-undersupply]] — catching a downstream-rail current shortfall the headline battery spec hides
- [[concepts/discharge-profile]] — using nominal voltage and amp-hours to size a battery for a target runtime
- Duty-cycle estimation per actuator/sensor module
- Peak vs. average power separation for connector and wire sizing

## Tools used

- [[entities/tools/dc-dc-converter|DC-DC converter]] (boost, 24V output)
- [[entities/tools/multimeter|Multimeter]] (implied for verification)
- Excel spreadsheet (the template itself)

## Materials used

(none — this is a methodology/template walkthrough)

## Projects

- [[entities/projects/scuttle-robot|Scuttle robot]] — Spring 2022 capstone team's UV-sanitizer build, used as the worked example throughout the spreadsheet

## People mentioned

- [[entities/people/david-malawey|David Malawey]] (lab coordinator)

## Notable quotes / timestamps

- [3:25] "How will the above information impact your design decisions such as selecting a battery."
- [8:01] Conditional-formatting trick: yellow when margin is small, red when negative — flags the rail that can't deliver enough current.
- [8:42] "Cheap converters lose a lot... if you get an expensive one you could maybe get it 90% efficient but the Amazon types are closer to 80%."
- [11:42] The template's purpose is "to trim back your work overall and only deliver in your deliverables the information and calculations that really matter."

## Related videos

- [[videos/3-ways-to-test-power-draw-for-mechatronics-designs]] — sequel that shows how to *measure* the values this template asks for
- [[videos/embedded-computer-users-should-know-this-power-issue]] — Raspberry Pi 5V rail current limits
- [[videos/dual-power-supply-for-electronics-prototyping-full-tutorial]]
