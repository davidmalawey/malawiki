---
type: video
title: "pneumatic air battery"
video_id: "AszFG81e_ro"
url: "https://www.youtube.com/watch?v=AszFG81e_ro"
published: 2023-11-25
duration: "11:29"
tags: [pneumatics, air-battery, fire-extinguisher, brad-nailer, scuttle, diy, npt-thread]
ingested: 2026-05-02
---

## Overview

David walks through how to convert a cheap fire-extinguisher bottle into a portable pneumatic "air battery" capable of driving a brad nailer or stapler — the reservoir holds enough charge to drive an inch-and-a-quarter brad through solid oak and fire five units before refilling. He covers the fittings, threads, and modifications needed, and frames the result as a future actuator option for the [[entities/projects/scuttle-robot|SCUTTLE]] robotics ecosystem, since pneumatics can do many things electric motors cannot.

## Key takeaways

- A small fire-extinguisher bottle is cheaper than buying its individual gauge or Schrader valve separately, and the components are very high quality — bottle is steel, threads aluminum, valve solid brass.
- Tools work on small-volume high-pressure flow (brad nailer, stapler) — not on high-flow tools like impact guns. Fill to ~120 PSI from any gas-station tire pump, up to ~180 PSI with a portable pump.
- Pressure adjustment on the tool itself controls how deep the fastener drives — start high, dial back.
- The bottle's front nozzle uses M12x1.5 (uncommon in pneumatic catalogs); David tapped it instead with 1/4" NPT to mate to standard fittings.
- Schrader valve = same valve as a bicycle/car tire — universally available and cheap in 4-packs.
- Aluminum is soft enough to tap easily; clear debris before sealing or it will end up in the bottle.
- Safety bound: as long as everything from bottle to nozzle is metal (no soldered/glued plastic in the pressure path), the system is safe within fire-extinguisher pressure ratings (rated ~195 PSI, won't burst until 400+ PSI).

## Techniques demonstrated

- [[concepts/pneumatic-fitting-conversion|Pneumatic fitting conversion]] (new concept page) — repurposing fire extinguisher hardware for compressed-air tooling
- Tapping aluminum with NPT thread
- PTFE tape sealing on tapered NPT
- Heating sealant resin with a torch (creme brulee torch suffices) to break the gauge bond
- [[concepts/locally-sourced-bom|Locally sourced BOM]] — Missouri Quik Trip free-air observation
- [[concepts/leverage-incumbent-engineering|Leverage incumbent engineering]] — fire-extinguisher manufacturers already over-engineered the pressure vessel

## Tools used

- Brad nailer (rigid, depth-adjustable)
- Pneumatic stapler (~$25 cast aluminum/iron)
- Push-to-connect pneumatic fittings (4 mm × 6 mm tubing kit, ~$13 on Amazon)
- 1/4" NPT to push-connect adapters
- Industrial quick-connect coupler (male/female pair)
- 1/8" NPT brass tee with three outlets
- Schrader valve (brass, off-the-shelf)
- Pressure gauge
- 11 mm wrench (for the gauge)
- NPT 1/4" tap
- Creme brulee torch / hot air gun
- Portable car tire pump
- [[entities/tools/ptfe-teflon|PTFE]] tape

## Materials used

- Fire-extinguisher bottle (~$15 Kidde, steel body, aluminum threads, rubber O-ring)
- Aluminum (front nozzle, tapped)
- Brass (fittings, Schrader valve, tee)
- Solid oak (test target)
- 1.25" brads, staples
- [[entities/materials/rubber|Rubber]] (O-ring)
- [[entities/materials/ptfe-teflon|PTFE tape]]

## Projects

- Pneumatic air battery (new project page)
- Future integration with [[entities/projects/scuttle-robot|SCUTTLE]] for pneumatic actuators

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 2:53 "It's rated full from a regular $15 Kidde fire extinguisher at like 195 PSI… 400 PSI won't break the bottle."
- 6:36 "All the components in these fire extinguishers are very well made, very high quality, and the system is cheap."
- 8:48 "If you're in Missouri where the gas stations are awesome — Quik Trip has free air for tires, so you go and you fill up your bottle at the gas station."

## Related videos

- [[videos/refuel-butane-torches-a-deep-dive-to-solve-all-the-issues]]
- [[videos/a-multidisciplinary-engineering-lab-tour-all-types-of-actuators]]
