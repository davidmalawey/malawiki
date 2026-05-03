---
type: video
title: "SprayMaster 3D Printable Open Design"
video_id: "verF-mPjaHg"
url: "https://www.youtube.com/watch?v=verF-mPjaHg"
published: 2023-02-23
duration: "1:43"
tags: [scuttle, spraymaster, 3d-printing, open-source-hardware, addon, robotics]
ingested: 2026-05-02
---

## Overview

A 1:43 product demo for **SprayMaster**, a sub-$25, 3D-printable open-design accessory for [[entities/projects/scuttle-robot|SCUTTLE robot]] that holds and triggers an aerosol can. David rapid-fires use cases (paint, waterproofing, lubricant, spray adhesive, cleaner, graffiti remover) then shows the integration: mount via [[entities/tools/2020-extrusion|extrusion]], add a $1 laser pointer for aim, and a $1 relay tied to a [[entities/brands/raspberry-pi|Raspberry Pi]] GPIO for software-driven actuation off a 12 V actuator.

## Key takeaways

- SprayMaster is an open, DIY add-on — total parts cost under $25 — published to Hackster (hackster.io/dmalawey/spraymaster-6212d0).
- A cheap laser pointer attached to the spray nozzle is a powerful aiming aid: spray direction becomes visible before triggering.
- Mechatronics stack: SCUTTLE chassis -> extrusion mount -> SprayMaster bracket -> 12 V linear actuator -> $1 relay -> 3 GPIO pins on Raspberry Pi.
- One robot platform + a spray can = autonomous painting, waterproofing, sanitizing, lubrication, adhesive application, residue removal, and graffiti stripping.
- Wiring uses screw terminals on the relay; the actuator's positive 12 V leg is what gets switched.

## Techniques demonstrated

- [[concepts/standardize-mounting-interfaces|Standardized mounting interface]] — extrusion slot lets the same add-on dock onto any SCUTTLE.
- [[concepts/open-source-hardware-publishing|Open-source hardware publishing]] (Hackster + downloadable prints).
- Relay control of an inductive actuator from a Pi (low-side switching of 12 V positive lead).
- [[concepts/locally-sourced-bom|Locally sourced BOM]] thinking — $1 laser, $1 relay.

## Tools used

- [[entities/tools/3d-printer|3D printer]] (printable bracket and trigger parts)
- [[entities/tools/2020-extrusion|2020 aluminum extrusion]] (SCUTTLE rail)
- [[entities/brands/raspberry-pi|Raspberry Pi]]
- $1 relay module
- Linear actuator (12 V)
- Cheap laser pointer (aim aid)
- Aerosol can (mounted payload)

## Materials used

- [[entities/materials/pla|PLA]] / printable plastic (printed parts)

## Projects

- **SprayMaster** — the open SCUTTLE add-on demoed here (new project — propose entity page).
- [[entities/projects/scuttle-robot|SCUTTLE robot]] — host platform.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:44] "we can use this one dollar laser to attach to the spray master — and suddenly you can see exactly where you're gonna spray"

## Related videos

- [[videos/payload-deck-demo-on-scuttle-robot|Payload Deck Demo on SCUTTLE Robot]] — sibling SCUTTLE add-on from the same window.
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part|How to design a functional printable open-source mechanical part]]
- [[videos/make-a-frankenstein-power-drill-treadmill-motor-controller-easy|Make a Frankenstein power drill / treadmill motor controller]]
