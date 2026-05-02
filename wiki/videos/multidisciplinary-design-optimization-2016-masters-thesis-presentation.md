---
type: video
title: "Multidisciplinary Design Optimization - 2016 Masters Thesis Presentation"
video_id: "XbSdwpLa4j4"
url: "https://www.youtube.com/watch?v=XbSdwpLa4j4"
published: 2023-12-15
duration: "30:01"
tags: [thesis, mdo, cubesat, optimization, fea, dfm, texas-am, 2016, genetic-algorithm, sqp, pareto-front]
ingested: 2026-05-02
---

## Overview

David's 2016 master's thesis defense at [[entities/places/texas-am-lab|Texas A&M]], uploaded to YouTube in December 2023. The research applies [[concepts/multidisciplinary-optimization|Multidisciplinary Design Optimization (MDO)]] to a CubeSat (small standardized satellite), optimizing for cost effectiveness and mass simultaneously across coupled mechanical, power, and propulsion subsystems. The output is a manufacturable prototype design fed directly by the optimizer, with machining time reduced from a 10-hour benchmark quote to 2 hours 21 minutes for two panels. David flags in the description that the same MDO method applies directly to robots — an explicit through-line to his current open-source robotics work.

## Key takeaways

- Existing CubeSat MDO research (e.g. University of Michigan) optimizes operational performance — power capture, data transmission — and assumes cost is no object. David's contribution is making **cost effectiveness** the objective and power demand the constraint, plus designing a frame that takes the **full 119 mm envelope** instead of the conventional 100 mm.
- Two-stage optimizer: a genetic algorithm (heuristic) chooses the three discrete design variables, then sequential quadratic programming (SQP, gradient method) refines the three continuous variables (number of solar panels, number of batteries, structure rail width) — guaranteeing a local minimum where the gradient goes to zero.
- Six design variables, three constraints (power demand met by solar + batteries; structural bending stiffness ≥ benchmark; propellant sufficient for delta-V), and an N-squared diagram with one feedback loop (propulsion ↔ battery/power ↔ mass).
- A weighted sum objective function J* = λ·cost + (1-λ)·mass sweeps λ from 0 to 1 to generate the Pareto front. False Pareto points appear when the GA gets stuck in a non-ideal region the gradient can't escape.
- Sensitivity analysis: mass is most sensitive to **structure rail thickness** (logical — structure mass equals batteries + panels combined). Cost is most sensitive to **solar panels** (~$1500 vs. $10 batteries).
- 8% of failed CubeSat missions in the "first 100 CubeSats" study fail mechanically — so don't over-invest in extensive mechanical simulation; do enough.
- DFM applied to the ISIS benchmark panel: doubling minimum tool radius and halving raw stock thickness cut a 10-hour machining quote to 3 hours; building fixtures and a CNC code that cuts two panels at once cut total prototype time from 8 hours to 2 hours 21 minutes for a pair.
- FEA convergence study under 1000 G load — factor of safety stayed between 2.5 and 3.5 as mesh refined, considered acceptable but not "beautiful."
- Final prototype fit the official NanoRacks PPOD deployer check fixture on the first try.
- Modular "fixed panel" subsystem accepts an inert panel, a solar panel, or a deployable antenna — same mounting interface, multiple payload variants.

## Techniques demonstrated

- [[concepts/multidisciplinary-optimization|Multidisciplinary optimization]] — the central methodology
- [[concepts/pareto-front|Pareto front analysis]] (new concept page) for cost-vs-mass tradeoff
- [[concepts/genetic-algorithm-plus-gradient|Genetic algorithm plus gradient method]] (new concept page) — heuristic-then-gradient two-stage optimization
- [[concepts/sensitivity-analysis|Sensitivity analysis]] (new concept page) on design variables and parameters
- [[concepts/design-for-manufacturing|Design for manufacturing]] — minimum tool radius, raw stock thickness reduction, fixturing, multi-part CNC programs
- [[concepts/finite-element-analysis|Finite element analysis]] (new concept page) with mesh convergence study
- [[concepts/benchmarking-design|Benchmarking design]] — used the ISIS CubeSat panel as the structural and cost reference
- [[concepts/n-squared-diagram|N-squared diagram]] (new concept page) — module coupling/feedback visualization
- [[concepts/borrowing-tolerances|Borrowing tolerances]] — bending stiffness constraint borrowed from benchmark beam cross-section

## Tools used

- CNC machining center (panel prototypes)
- FEA software (mesh convergence, 1000 G static analysis)
- Genetic algorithm + sequential quadratic programming (MATLAB toolchain implied; software repo at github.com/dmalawey/mdo)
- CMM / calipers (tolerance verification on machined parts)
- NanoRacks PPOD deployer check fixture

## Materials used

- [[entities/materials/aluminum|Aluminum]] (default rail material)
- Steel (alternate rail material — higher modulus of elasticity allows shorter L for same bending stiffness)

## Projects

- 2016 CubeSat MDO thesis (new project page)
- Modular fixed-panel subsystem (carries inert / solar / antenna variants)

## People mentioned

- [[entities/people/david-malawey|David Malawey]] (presenter)
- [[entities/people/joseph-morgan|Dr. Morgan]] (committee member, brought a cookie in)
- ISIS (Innovative Solutions In Space) — benchmark CAD model source
- [[entities/brands/nanoracks|NanoRacks]] (new brand page) — provided check fixture and unattributed CubeSat CAD
- University of Michigan researchers (cited prior work)

## Notable quotes / timestamps

- 0:00 Gathering — informal pre-defense banter, lighting setup
- 4:30 Background — first 100 CubeSats study, 8% mechanical failure rate
- 7:40 Optimization Formula — six design variables, three constraints, dual objective
- 12:30 Heuristic + Gradient Methods — two-stage GA + SQP architecture
- 17:20 Mechanical Prototype — DFM cuts on the ISIS benchmark
- 22:50 Prototyping Time Reduction — 8 hours → 2:21 for two panels
- 24:00 Fitment into Launcher — passed NanoRacks PPOD check fixture
- 28:30 "They assumed that cost is no object. Every study I've seen assumed that cost is no object." — the core differentiator

## Related videos

- [[videos/borrow-a-tolerance-mindset-for-designers]]
- [[videos/how-to-design-the-best-in-the-world]]
- [[videos/optimal-robot-ecosystem]]
- [[videos/some-designs-fight-thermodynamics-some-designs-work-together]]
- [[videos/study-before-designing|highly-engineered-emt-conduit-parts-to-study-before-designing]]
