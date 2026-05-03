---
type: video
title: "Refuel butane torches (a deep dive to solve all the issues)"
video_id: "kxGagkzpKZg"
url: "https://www.youtube.com/watch?v=kxGagkzpKZg"
published: 2024-10-11
duration: "12:50"
tags: [thermodynamics, butane, psychrometrics, supercritical-fluid, pneumatics, refilling]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] applies thermodynamics fundamentals to the everyday frustration of refilling butane torch lighters. He frames refilling as a [[concepts/psychrometrics|psychrometrics]] problem — figuring out at what pressures and temperatures the butane is liquid versus gas — and uses that lens to explain why refills sometimes succeed, sometimes do nothing, and sometimes need two cycles. The same physics, he notes, transfers directly to propane, pneumatics, and eventually to more efficient robotics.

## Key takeaways

- Butane in the canister exists as a [[concepts/supercritical-fluid|supercritical fluid]] — both liquid and gas at the same time, around 2 bar (~30 PSI).
- Liquid must be available at the nozzle of the source canister when refilling, so orientation (upside-down) matters.
- Both donor and receiver are at the same equilibrium pressure, so you must release a little gas from the lighter first to create the pressure delta that drives flow.
- Expansion cools the receiver; warming it back up with your hands restores pressure and lets you do round two.
- Sealing only needs to beat ~30 PSI — barely a pound of force — so a generally-sealed nozzle is enough, even if a tiny hiss escapes.

## Techniques demonstrated

- [[concepts/psychrometrics|Psychrometrics]] reasoning applied to a closed two-phase system.
- Using a syringe with water as an analog for the supercritical butane state.
- Hand-warming a depleted canister between refill cycles to re-pressurize.

## Tools used

- Butane torch lighters (multiple form factors)
- Butane refill canisters
- Syringe (used as a teaching analog for liquid + vapor coexistence)

## Materials used

- Butane (the working fluid)

## Notable quotes / timestamps

- 0:39 — TL;DR: turn both items upside down, press, expect a small hiss, expect to do it twice.
- 2:38 — "step one this is a psychrometrics problem."
- 9:01 — Why a hand-warmed canister flows again: warming raises pressure relative to the cooled receiver.

## Related videos

- [[videos/build-a-diy-power-supply-a-tutorial-using-openbox|Build a DIY power supply (a tutorial using openBox)]] — same channel pattern of teaching one ubiquitous device to ground much bigger concepts.
