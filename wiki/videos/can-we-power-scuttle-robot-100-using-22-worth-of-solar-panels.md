---
type: video
title: "Can we power SCUTTLE robot 100% using $22 worth of solar panels?"
video_id: "iXn-_rjCiiU"
url: "https://www.youtube.com/watch?v=iXn-_rjCiiU"
published: 2020-10-17
duration: "7:38"
tags: [scuttle, solar, power, off-grid, malaysia, battery, mppt]
ingested: 2026-05-02
---

## Overview

David tests a $11 Cytron 10 W solar panel directly into [[entities/projects/scuttle-robot|SCUTTLE]]'s [[entities/tools/18650-cell|18650]] battery pack. Open-circuit voltage hits ~21 V, but loaded into the 10.4 V pack he gets ~5 W per panel under cloudy Malaysian midday sun. Two panels in parallel comfortably cover SCUTTLE's 7 W driving budget — a fully solar-powered robot for ~$22.

## Key takeaways

- Solar panel rated 10 W at 22 V; loaded onto a 10.4 V LiPo pack, real output dropped to 3.9–5.1 W due to voltage mismatch (no MPPT in this naive setup).
- Open circuit reading: 21.7 V; under load: 10.43 V — confirms the panel wants to operate at higher voltage to deliver rated power.
- SCUTTLE's measured 7 W driving budget (from the prior power test) means two panels in parallel give ~10 W — enough margin for sustained driving when sun is high.
- Doubling power requires more panels, not just changing voltage — but a buck/MPPT converter could likely recover the unused panel power.
- David is reckless-on-purpose with the bare battery protection circuit — flags the missing details for follow-up.

## Techniques demonstrated

- [[concepts/solar-charging|solar charging]]
- [[concepts/power-budget-method|power budget method]]
- [[concepts/instrument-resolution|instrument resolution]]
- [[concepts/datasheet-vs-real-world-fit|datasheet vs real-world fit]]

## Tools used

- [[entities/tools/solar-panel|solar panel]] (Cytron 10 W)
- [[entities/tools/multimeter|multimeter]]
- [[entities/tools/usb-power-meter|USB power meter]]
- [[entities/tools/18650-cell|18650 cell]]
- [[entities/tools/raspberry-pi|Raspberry Pi]]

## Materials used

- [[entities/materials/lipo-battery|LiPo battery]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]
- [[entities/projects/scuttle-solar|SCUTTLE solar]]
- [[entities/projects/scuttle-asia-malaysia|SCUTTLE Asia Malaysia]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Brands

- [[entities/brands/cytron|Cytron]]

## Places

- [[entities/places/malaysia|Malaysia]]

## Related videos

- [[videos/scuttle-robot-how-much-power-does-it-use-about-7w]]
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify]]
- [[videos/loading-50-watts-on-cheap-dc-boost-converter-quick-test]]
- [[videos/3-ways-to-test-power-draw-for-mechatronics-designs]]
