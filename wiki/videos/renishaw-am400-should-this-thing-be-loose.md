---
type: video
title: "Renishaw AM400 - Should this thing be loose?"
video_id: "VBk1gkTI7PY"
url: "https://www.youtube.com/watch?v=VBk1gkTI7PY"
published: 2019-03-18
duration: "1:41"
tags: [metal-am, renishaw, am400, troubleshooting, oxygen-sensor, argon, root-cause]
ingested: 2026-05-02
---

## Overview

David inspects an internal assembly inside the [[entities/tools/renishaw-am400|Renishaw AM400]] metal additive manufacturing machine that appears looser than expected after he replaced the [[entities/tools/oxygen-sensor|oxygen sensor]]. He hypothesizes that air ingress at this loose joint explains a stubborn high-oxygen reading and the "argon bubble" that Renishaw technicians had previously instructed him to purge — a symptom he had reported over a year earlier while struggling to complete the inert cycle without burning excessive argon.

## Key takeaways

- The internal assembly should articulate, but not flop loosely — observed motion suggests two unspecified fasteners ("two minutes" — likely transcript artifact for "nuts" or "screws") have backed off.
- Recent maintenance was limited to swapping the oxygen sensor, an operation that should not have transferred any force capable of loosening this joint.
- A loose joint at this location is consistent with air ingress, which would explain (a) elevated oxygen reading on this sensor specifically and (b) the persistent argon bubble Renishaw asked him to purge by opening a valve and re-purging post-vacuum.
- This is a recurring problem — David flagged the slow inert-cycle / high argon consumption to Renishaw a year prior, and the loose-joint observation may finally be the root cause.

## Techniques demonstrated

- [[concepts/root-cause-analysis|root-cause-analysis]] — connecting an observed mechanical anomaly (loose assembly) to a long-standing symptom (high oxygen reading, persistent argon bubble, slow inert cycle).
- [[concepts/symptom-watch|symptom-watch]] — keeping a long-running log of unresolved process anomalies until evidence aligns to a cause.
- [[concepts/expert-dialogue-gap|expert-dialogue-gap]] — the OEM technicians prescribed a workaround (purge the bubble) without diagnosing the underlying mechanical issue; the operator's hands-on inspection surfaces what the remote support workflow missed.
- [[concepts/connecting-the-dots-backward|connecting-the-dots-backward]] — a year-old complaint suddenly aligns with new physical evidence.

## Tools used

- [[entities/tools/renishaw-am400|Renishaw AM400]]
- [[entities/tools/oxygen-sensor|oxygen sensor]]
- argon purge valve (machine-internal)
- vacuum system (machine-internal)

## Materials used

- [[entities/materials/argon|argon]] (inert atmosphere gas)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- Renishaw technicians (unnamed support team)

## Brands mentioned

- [[entities/brands/renishaw|Renishaw]]

## Places

- [[entities/places/texas-am-lab|Texas A&M lab]] (implied — David's then-current workspace housing the AM400)

## Notable timestamps

- 0:09 — Demonstrates the unexpected motion of the internal assembly.
- 0:30 — Hypothesizes air ingress at the loose joint as the source of the high oxygen reading.
- 1:00 — Recounts Renishaw's prescribed purge workaround.
- 1:24 — Notes he raised this exact symptom to Renishaw over a year ago.

## Related videos

- [[videos/multidisciplinary-design-optimization-2016-masters-thesis-presentation]]
- [[videos/a-multidisciplinary-engineering-lab-tour-all-types-of-actuators]]
