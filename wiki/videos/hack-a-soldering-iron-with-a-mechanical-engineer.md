---
type: video
title: "Hack a Soldering Iron with a mechanical engineer"
video_id: "-eF5kLdLvU0"
url: "https://www.youtube.com/watch?v=-eF5kLdLvU0"
published: 2024-08-12
duration: "11:04"
tags: [soldering, heat-transfer, thermodynamics, mechatronics, hack]
ingested: 2026-05-02
---

## Overview

A side-project born while prepping the adhesives video: David turns a basic, no-thermostat [[entities/tools/soldering-iron|soldering iron]] into a temperature-controllable plastic-melting / thread-setting tool by exploiting steady-state 1-D heat conduction along its 1/4" tip shank. He frames it as the most teachable example of a notoriously dense ME course (heat transfer / thermodynamics) — no math required.

## Key takeaways

- An iron with a fixed 42 W heater plus a sliding 1/4" tip = a tunable temperature source. Slide the rod in for hotter tip, out for cooler tip — the temperature gradient along the rod does the work.
- This is a classic 1-D, single-mode (passive convection) heat transfer problem in disguise. Long rods approach ambient at the tip; shorter rods stay closer to source temperature.
- You don't need to know the actual tip temperature to control it — you only need to be able to raise or lower it relative to your task (melting plastic, not melting solder).
- [[entities/materials/silicone|Silicone]] sleeving along the shank acts as insulation, trapping more heat in the active zone and either raising the tip temperature or letting you reach the same temperature at lower wattage.
- [[entities/tools/threaded-insert|Threaded inserts / heat-set inserts]] for plastic, [[entities/tools/rivnut|rivnuts]], and wood-burning kits all use the same hardware — different tips on the same heat source.
- A drilled hole + thermocouple in the tip would close the control loop; an aquarium pump + heatproof silicone tube can pipe controlled airflow through a hollow tip for hot-air work.

## Techniques demonstrated

- [[concepts/steady-state-heat-conduction|Steady-state 1-D heat conduction]] reasoning to control tip temperature without instrumentation.
- Conservation of energy as area-equivalence on the temperature-vs-position graph (energy not lost to convection in a removed segment shows up as higher tip temperature).
- Using a [[entities/tools/usb-power-meter|watt meter]] on the iron's mains to verify reduced power draw when insulated.
- Soldering brass to aluminum to fix a heat-exchanger tip; switching to a rivnut when soldering proved too finicky.

## Tools used

- [[entities/tools/soldering-iron|soldering iron]] with 1/4" interchangeable shank (42 W, no thermostat)
- Pipe cutter (for brass and copper)
- Chamfer tool
- [[entities/tools/usb-power-meter|watt meter]]
- [[entities/tools/rivnut|rivnut]] / threaded rivet tool
- CPU heat sinks (repurposed as melting tips)

## Materials used

- Brass (tip body, threaded inserts)
- [[entities/materials/aluminum|Aluminum]] (heat-exchanger sleeve, rivnut option)
- [[entities/materials/copper|Copper]] (alternative tip)
- [[entities/materials/silicone|Silicone]] (insulating sleeve, heatproof tube)
- Solder (for joining brass to aluminum)
- Plastic substrates (target for ridging / threading)

## Concepts referenced

- [[concepts/steady-state-heat-conduction|steady-state heat conduction]]
- [[concepts/passive-convection|passive convection]]
- Surface preparation by melting (vs. sanding) for adhesion — bridges into the [[videos/how-to-choose-an-adhesive|adhesives video]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/how-to-choose-an-adhesive|How to choose an adhesive]] — this hack was prep for surface-prep experiments shown there.
- [[videos/insights-in-real-world-battery-energy-that-you-can-verify|Insights in real-world battery energy]]
