---
type: video
title: "SCUTTLE Robot - Build Motor Driver Signal Wires JST-ZH Macro View for Beagle"
video_id: "n-MyRkjyKvs"
url: "https://www.youtube.com/watch?v=n-MyRkjyKvs"
published: 2020-09-12
duration: "5:24"
tags: [scuttle-robot, jst-zh, dupont-connector, motor-driver, beaglebone, wiring, pwm]
ingested: 2026-05-02
---

## Overview

David builds the SCUTTLE motor driver signal harness: 2-pin [[entities/tools/jst-zh-connector|JST-ZH]] connectors mate to the BeagleBone's PWM outputs on one end and a 4-pin [[entities/tools/dupont-connector|Dupont]] header lands on the H-bridge motor driver on the other end. The video is mostly a macro-shot deep dive on connector reassembly, [[concepts/tug-test|tug-tests]], and the why-behind ground-pin marking conventions.

## Key takeaways

- JST-ZH contacts dissect the same way as Dupont: hook the little burr on the tab to release.
- After reassembly, plastically deform the tab a hair before reinsertion if the [[concepts/tug-test|tug test]] fails — you can't bend it once it's seated.
- Strip just enough wire to crimp; with short JST-ZH leads, fold rather than cut excess to keep maximum conductor length.
- Add a 5th plastic-only "ground marker" pin to the 4-pin Dupont housing so you never flip the connector or land a wire on the always-hot 5V rail.
- A Sharpie dot on the housing acts as a redundant ground indicator when the silkscreen arrow is hidden.

## Techniques demonstrated

- [[concepts/crimping|Crimping]] short-lead signal wires
- [[concepts/tug-test|Tug-test verification]]
- [[concepts/cable-management|Bending and tucking signal harnesses]] to survive vibration
- [[concepts/clip-before-power-rule|Power-isolate before plugging]] (lights-off check)

## Tools used

- [[entities/tools/jst-zh-connector|JST-ZH connector]]
- [[entities/tools/dupont-connector|Dupont connector]]
- [[entities/tools/dupont-crimper|Dupont crimper]]
- [[entities/tools/universal-cable-stripper|Wire stripper]]
- [[entities/tools/beaglebone-y-ai|BeagleBone]]
- [[entities/tools/dual-h-bridge-motor-driver|H-bridge motor driver]]
- [[entities/tools/sharpie|Sharpie]] (ground marker)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- Earlier Dupont connector close-up videos (referenced)
- [[videos/how-to-crimp-dupont-terminals-and-why-you-shouldnt]]
