---
type: video
title: "SolidWorks 2019 - Create Configurations with Various Pattern Instances"
video_id: "EYYGwN8R4sQ"
url: "https://www.youtube.com/watch?v=EYYGwN8R4sQ"
published: 2020-11-21
duration: "4:06"
tags: [solidworks, cad, tutorial, configurations, global-variables, patterns]
ingested: 2026-05-02
---

## Overview

A focused SolidWorks 2019 tutorial showing how to drive pattern instance counts with a global variable, then use the configuration manager to swap pattern quantities per configuration. David's example is a plastic sleeve with a separate-body pin, where both the sleeve cuts and the pin pattern share a single `pins` variable, letting one part stand in for many subassembly variants.

## Key takeaways

- For large assemblies, replace many-part subassemblies with a single part that has patterned features driven by a global variable — fewer files, less complexity.
- Two-body parts: deselect "merge result" in the second feature so the pin lives as its own body inside the same part.
- Bind a pattern's instance count to a global variable by typing `=myVar` in the count field; SolidWorks will offer to create the variable.
- Both patterns referencing the same `pins` variable update together when you edit equations.
- Configuration manager: right-click the top row, "Add Configuration", then change `pins` per-configuration via "Manage Equations" — choose "this configuration" in the evaluation dropdown.
- You can change feature dimensions per-configuration too ("only this configuration"), but driving via equations is cleaner when several features depend on the same number.

## Techniques demonstrated

- [[concepts/cad-configurations|CAD configurations]]
- [[concepts/parametric-design|parametric design]]
- [[concepts/parts-library|parts library]] (one parametric part replacing many SKUs)
- [[concepts/feature-tree-naming|feature tree naming]]

## Tools used

- [[entities/brands/solidworks|SolidWorks]] (2019)

## Materials used

- plastic sleeve (generic — no entity page warranted)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:18 main body walkthrough — sleeve + pin, separate body via deselect-merge.
- 0:53 binding the pattern count to a global variable named `pins`.
- 2:09 manage equations changes both patterns simultaneously.
- 2:30 configuration manager — add "four pin configuration".
- 3:09 per-configuration equation override.

## Related videos

- [[solidworks-recognize-features-manually-tutorial-with-example]]
- [[tutorial-modeling-and-mindset-for-a-parametric-bracket-solidworks]]
- [[what-is-a-parametric-design-with-solidworks-example]]
- [[how-to-deboss-a-dynamic-revision-number-for-3d-prints-solidworks]]
