---
type: video
title: "Insights in REAL-WORLD battery energy that YOU can verify."
video_id: "G2JmWiyUJ3s"
url: "https://www.youtube.com/watch?v=G2JmWiyUJ3s"
published: 2024-07-31
duration: "32:39"
tags: [batteries, lithium-ion, power-tools, instrumentation, characterization]
ingested: 2026-05-02
---

## Overview

A deep, hands-on tour of what is actually happening inside cordless power-tool batteries — the kind of insight engineering students don't get in the classroom. [[entities/people/david-malawey|David]] measures voltage, current, and watt-hours under varying loads, characterizes a battery's [[concepts/discharge-profile|discharge profile]], examines the [[concepts/battery-protection-circuit|battery protection circuit]]'s cutoff behavior, demonstrates [[concepts/solar-charging|solar charging]] via DC, and produces a load map / tool power chart for several cordless tools.

## Key takeaways

- Voltage and amp-hour ratings are "informative but not honest." A 4 Ah, 20 V battery does not deliver 80 Wh — voltage sags under load, and energy delivered depends heavily on draw rate.
- The "20 V" on a [[entities/brands/dewalt|DeWalt]] battery is the no-load open-circuit voltage. Under any real load it sits closer to 18 V or below. [[entities/brands/ridgid|Ridgid]] is more honest in David's testing.
- Inside the pack: several [[entities/tools/18650-cell|18650 cells]] (typically Panasonic or Sanyo), 3S/4S/5S series stacks, plus a [[concepts/battery-protection-circuit|protection circuit]] that monitors balance, temperature, current, and undervoltage, and shuts the pack to 0 V when limits are exceeded.
- Two paths to cutoff: (a) high state of charge but a huge load drops voltage past the threshold, or (b) low state of charge plus a small draw. The tool itself doesn't decide — the pack does.
- A battery can be characterized by sweeping load currents at multiple states of charge to build a [[concepts/load-map|load map]]. Once that map exists, you can infer the load drawn by an actuator just by watching voltage sag — "magic measurement without current."
- DC-to-DC charging from a [[entities/tools/solar-panel|solar panel]] beats AC-to-DC-to-AC-to-DC when the source is small (avoids two conversion losses). A $25 / 10 W panel from [[entities/brands/amazon|Amazon]] feeds the charging port with usable wattage.
- Tool no-load power numbers David captured: vacuum (highest), reciprocating saw ~200 W, blower ~370 W with max-output battery, grinder 142 W, impact driver ~60 W full-trigger.

## Techniques demonstrated

- [[concepts/discharge-profile|Discharge profile]] measurement using a constant-current load (CBA tester).
- Acoustic RPM estimation using the Sonic and Decibel X apps (frequency → RPM, accounting for "things that wobble four times per rotation").
- Load map characterization at 100/75/50/25% SOC.
- Voltage-only state-of-charge inference once a battery is characterized.
- Powering a 12 V automotive radiator fan from an 18 V tool battery — robust auto parts tolerate it well.

## Tools used

- [[entities/tools/usb-power-meter|watt meter]] (also for tool / charger draw)
- CBA discharge tester
- DeWalt and Ridgid power tool batteries (2 Ah, 4 Ah, max-output)
- Vacuum, impact driver, reciprocating saw, blower, grinder
- 10 W solar panel (Amazon)

## Materials used

- [[entities/tools/18650-cell|18650 lithium-ion cells]]

## Brands mentioned

- [[entities/brands/dewalt|DeWalt]], [[entities/brands/ridgid|Ridgid]]
- [[entities/brands/amazon|Amazon]]
- Panasonic, Sanyo (cell suppliers)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [10:31] "If you buy a 4 amp-hour battery and they're saying we're 20 volts, so we're claiming 80 Wh — that's a big fat lie."
- [29:48] (Once a battery is characterized) "We can apply a load, observe the voltage… and this is absolute magic, my friends."

## Related videos

- [[videos/hack-a-soldering-iron-with-a-mechanical-engineer|Hack a soldering iron]] — same instrument-driven approach using a watt meter to read power.
- [[videos/design-enclosures-for-electronics-using-mechanical-mindset|Design enclosures for electronics]]
