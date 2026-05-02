---
type: video
title: "A&M University's Lab Burned Down and Here's What I Learned"
video_id: "1-9dbWSUl7w"
url: "https://www.youtube.com/watch?v=1-9dbWSUl7w"
published: 2025-11-20
duration: "26:31"
tags: [3d-printing, safety, root-cause-analysis, fire, maintenance, commentary, texas-am]
ingested: 2026-05-02
---

## Overview

In November 2018 a fire destroyed the prototyping labs in Texas A&M's Kane mechanical engineering building, attributed via rumor to a 3D printer. After seven years of asking and getting nowhere, David — who runs the same Creator Pro printers in a different department — publishes his own root-cause analysis. He shows corrosion building up on the heated-bed power connector, the pin that carries high current at 24 V; once contact resistance climbs, the joint heats further, accelerating corrosion until it can ignite. The university's countermeasure (don't sit printers on wood) treats printers as inherently fire-breathing rather than fixing the connector. The video doubles as a meditation on institutional culture: closed, fearful information-hoarding raises costs, reduces capability, and prevents shared learning.

## Key takeaways

- Heated-bed power connectors corrode over years — high current, occasional thermal cycling, ambient humidity. Replace at first sign of dullness.
- Symptom to watch for: preheat takes much longer than expected and the bed indicator LED is intermittent — that's voltage failing across a corroded contact.
- The original spec connector is "minimal" — undersized for sustained high-current duty; resoldering with a larger connector is the engineering fix.
- Without root-cause analysis, the only countermeasures available are buying things (better printers, fire-rated tables, more insurance, fewer labs). Money replaces engineering.
- Texas A&M post-fire: fewer 3D-printing spaces, more expensive printers, more staff hours per printer, less student access — exactly the wrong direction.
- "Fearless on every front" is Texas A&M's stated value — David invokes it as the basis for finally going public after seven years of internal silence.
- Three-step printer safety: (1) stop and investigate any behavior change, (2) have a contingency plan even with countermeasures in place, (3) keep manuals accessible (David uses QR codes on machines).
- Communication trumps everything — share humble failures because that's when other people actually help.

## Techniques demonstrated

- [[concepts/root-cause-analysis|root-cause analysis]] (Toyota-style, applied to a fire)
- [[concepts/connector-corrosion-cycle|connector corrosion cycle]] — resistance + heat + humidity compounding
- [[concepts/symptom-watch|symptom watching]] — slow preheat as an electrical failure signal
- [[concepts/qr-code-manuals|QR-code manuals]] — making maintenance reference frictionless
- [[concepts/share-the-failure|share the failure]] — transparent failure communication beats institutional silence

## Tools used

- [[entities/tools/3d-printer|3D printer]] — specifically [[entities/tools/flashforge-creator-pro|FlashForge Creator Pro]] (the printer brand involved in the fire and still in David's lab)
- [[entities/tools/fire-blanket|fire blanket]] (recommended contingency)

## Places mentioned

- [[entities/places/texas-am|Texas A&M]] — Kane Building (mechanical engineering); Engineering Technology and Industrial Distribution
- [[entities/places/kane-building|Kane Building]] — site of the November 2018 fire

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 15:45 "Without the root cause, you need to assume that your 3D printer is a fire-breathing machine and spend however much it costs to overcome that problem."
- 16:55 "If you're a student or a prospective student, when you go to tour a college campus... ask: 'has there been any failure in the technical environment here?' If they say no, that's a lie."
- 25:02 "Fearless on every front... I cannot factor fear into my situation of trying to do the best thing."

## Related videos

- [[videos/i-applied-toyota-root-cause-analysis-to-the-sticky-lids-heres-my-solution|I Applied Toyota Root Cause Analysis to the Sticky Lids]]
- [[videos/10-years-of-engineering-labs|10 Years of Engineering Labs]]
