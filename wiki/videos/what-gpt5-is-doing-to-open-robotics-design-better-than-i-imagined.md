---
type: video
title: "what GPT5 is doing to open robotics design - better than I imagined"
video_id: "GBuXDm2Qahw"
url: "https://www.youtube.com/watch?v=GBuXDm2Qahw"
published: 2025-08-11
duration: "15:59"
tags: [ai, gpt-5, simulation, scuttle, belt-and-pulley, parametric, payoff]
ingested: 2026-05-02
---

## Overview

An unplanned reaction video. [[entities/people/david-malawey|David]] gives [[entities/brands/chatgpt|ChatGPT-5]] one prompt — "make a visual simulation for a system of two pulleys and a belt, defined by the gear ratio, in a single standalone HTML file" — and gets back a working interactive simulation in about two and a half minutes. The point isn't AI per se: it's the payoff for five years of carefully [[concepts/parametric-design|parametrizing]] [[entities/projects/scuttle-robot|SCUTTLE]] so every dimension was already characterized when AI tools matured enough to consume them.

## Key takeaways

- The bet five years ago — invest 10× more effort than necessary to fully digitize and parametrize a real working robot — paid off the moment LLMs got good enough to generate accurate simulations from natural-language prompts.
- One prompt produced a single self-contained HTML file (human-readable code) simulating a two-pulley belt drive with adjustable gear ratio.
- This unlocks a new path for engineering education: students can manipulate the simulation to understand pulley pitch, GT2 tooth geometry, and belt engagement without first learning the math.
- It also changes who can modify [[entities/projects/scuttle-robot|SCUTTLE]]: a student can swap to a smaller GT2 pulley + belt and use AI to update the 3D bracket, instead of waiting for a mechanical engineer to redo the calculation.
- The big lesson: open-source designs that include not just CAD but the *decision rationale* behind each choice (why this belt, why this pulley) are the ones AI can productively iterate on.

## Techniques demonstrated

- Prompting an LLM to produce a standalone HTML simulation of a mechanical system.
- Using AI to translate parametric CAD into student-manipulable interactive learning materials.

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]] — three major hardware iterations, every dimension parametrized.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/how-to-design-the-best-in-the-world|How to Design the Best in the World]] — the parametric/open-source discipline that made this AI workflow possible.
