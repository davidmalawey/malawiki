---
type: video
title: "Don't destroy your 18650 cells! Use this Analogy to understand."
video_id: "fC4sgXplA3k"
url: "https://www.youtube.com/watch?v=fC4sgXplA3k"
published: 2019-02-13
duration: "6:14"
series: "[[series/scuttle-robot-build]]"
tags: [18650, battery, lithium-ion, safety, analogy, scuttle-robot]
ingested: 2026-05-02
---

## Overview

David walks through proper handling of [[entities/tools/18650-cell|18650]] [[entities/materials/lipo-battery|lithium-ion]] cells used in [[entities/projects/scuttle-robot|SCUTTLE]]: charge/discharge voltage windows, the C-rate concept, why series packs need balanced charging, and the "cups of water" analogy for why one weak cell ruins a series string. He also shows a heat-gun rescue for partially peeled wrappers and warns this only mitigates damage rather than restoring cells.

## Key takeaways

- [[entities/brands/panasonic|Panasonic]] cells are 3.7 V nominal, 4.2 V max, and must not drop below 2.8 V — go outside that window and you cause permanent damage.
- The chargers used auto-shut off at the upper limit; the application (the robot) is what must enforce the lower cutoff.
- A round plastic tab inserted between cell and metal contact prevents the wrapper from snagging during removal.
- A [[entities/tools/heat-gun|heat gun]] can clean up a partially peeled wrapper but won't restore lost capacity.
- C-rate is amps to discharge a full battery in one hour and depends on capacity, so it's a useful chemistry-comparison metric (lithium-ion safely sustains higher C than lead acid).
- In a series pack, cells are like cups of water — once one empties the rest are forced past their floor and damage compounds; the same logic applies in reverse for charging if internal resistance differs.
- Current safe practice: remove cells and charge them individually in a controller-equipped charger.

## Techniques demonstrated

- [[concepts/battery-protection-circuit]]
- [[concepts/discharge-profile]]
- [[concepts/c-rate]]
- [[concepts/series-cell-balancing]]
- [[concepts/cups-of-water-cell-analogy]]
- [[concepts/individual-cell-charging]]
- [[concepts/wrapper-rescue-with-heat-gun]]
- [[concepts/battery-chemistry-tradeoffs]]

## Tools used

- [[entities/tools/18650-cell|18650 cell]]
- [[entities/tools/18650-charger|18650 charger]]
- [[entities/tools/heat-gun|heat gun]]
- [[entities/tools/cba-power-meter|CBA power meter]] (implied — discharge curve graph)
- [[entities/tools/cell-removal-tool|plastic cell removal tab]]

## Materials used

- [[entities/materials/lipo-battery|lithium-ion]]

## Brands

- [[entities/brands/panasonic|Panasonic]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## Notable quotes / timestamps

- [0:38] "If the battery goes above 4.2 or below 2.8 you will end up with permanent damage."
- [5:14] "Battery cells are like these little cups full of water."
- [6:09] "Each one is valuable so please take care of them."

## Related videos

- [[videos/scuttle-robot-fastest-way-to-check-battery-voltage-on-beaglebone-blue]]
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify]]
- [[videos/build-a-battery-adapter-to-power-the-whole-lab]]
