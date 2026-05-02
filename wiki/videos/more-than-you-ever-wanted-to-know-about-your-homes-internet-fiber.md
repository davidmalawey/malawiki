---
type: video
title: "More than you ever wanted to know about your home's internet fiber"
video_id: "vaBI-zFmS2k"
url: "https://www.youtube.com/watch?v=vaBI-zFmS2k"
published: 2024-08-24
duration: "1:07:16"
tags: [fiber-optic, networking, splicing, telecom, interview, field-tour]
ingested: 2026-05-02
---

## Overview

A long-form, on-site interview / field tour. David films [[entities/people/peter-fiber-tech|Peter]] — a residential [[concepts/fiber-optic-installation|fiber-optic installation]] technician — as he explains the physical layer of home internet, dissects the cables, and performs a live [[concepts/fusion-splicing|fusion splice]] on a glass fiber. David asks the dumb-but-smart questions that tie the explanation back to electronics-engineer mental models (attenuation, signal loss, [[concepts/laser-light|laser light]] transmission).

## Key takeaways

- Residential fiber drop cables include a glass fiber core, [[entities/materials/kevlar|Kevlar]] aramid strength members, and a UV-rated jacket. The Kevlar carries tension; the glass would shear without it.
- "Rock fiber" (toned, direct-burial) and aerial fiber are different external builds for the same internal optical element.
- Fiber from the utility pole splits into a [[entities/tools/junction-box|junction box]] / [[entities/tools/optical-network-terminal|ONT (optical network terminal)]] at the home, then to the modem. Connectors can be terminated in the field, or — preferred — the line is [[concepts/fusion-splicing|fusion-spliced]] for lower attenuation.
- [[concepts/fusion-splicing|Fusion splicing]] workflow: strip the jacket → strip the buffer → wipe the bare fiber → score and break with a precision [[entities/tools/fiber-cleaver|fiber cleaver]] → load both ends in the [[entities/tools/fusion-splicer|arc-welder splicer]] → machine aligns the cores via camera and arcs them together → tension-test → slide a steel-reinforced heat-shrink sleeve over the joint and heat to lock it.
- Light loss is measured as [[concepts/optical-attenuation|attenuation]] (in dB, negative). Damage to the outer jacket alone is usually fine — the glass core is what carries signal.
- An [[entities/tools/otdr|OTDR]] (optical time-domain reflectometer) shoots a [[concepts/laser-light|laser]] down the line from one end and uses reflections to localize loss events — distance and severity from a single endpoint.
- City-side terminals aggregate dozens of customer fibers into trunk lines via patch panels and additional splices. The same physics scales from house drop to backbone.
- Safety: never look directly into a live fiber — the laser is invisible at telecom wavelengths and will damage your retina.

## Techniques demonstrated (live)

- Stripping a fiber drop cable down to bare glass.
- Cleaving glass with a precision fiber cleaver to get a perpendicular endface.
- Loading the splicer; watching the machine align cores and arc-weld them.
- Tension-testing the fresh splice before heat-shrinking.
- Sliding the steel-reinforced heat-shrink sleeve and curing it in the splicer's heater.
- Reading an [[entities/tools/otdr|OTDR]] trace to find attenuation events along the line.

## Tools used

- [[entities/tools/fiber-cleaver|fiber cleaver]]
- [[entities/tools/fusion-splicer|fusion splicer (arc welder)]]
- [[entities/tools/otdr|OTDR / optical time-domain reflectometer]]
- Strippers for jacket and buffer
- [[entities/tools/optical-network-terminal|ONT]] / junction enclosures

## Materials used

- Glass [[entities/materials/optical-fiber|optical fiber]] (core + cladding)
- [[entities/materials/kevlar|Kevlar / aramid]] strength members
- UV-rated outer jacket
- Steel-reinforced heat-shrink splice sleeve

## Concepts referenced

- [[concepts/fiber-optic-installation|fiber-optic installation]]
- [[concepts/fusion-splicing|fusion splicing]]
- [[concepts/optical-attenuation|optical attenuation]]
- [[concepts/laser-light|laser light transmission]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- [[entities/people/peter-fiber-tech|Peter]] (residential fiber technician)

## Related videos

- [[videos/clean-up-cords-wires-in-projects|Clean up cords & wires]] — general cable / wire management, contrast with telecom-grade workmanship.
