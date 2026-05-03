---
type: video
title: "Solidworks Recognize Features Manually (Tutorial with Example)"
video_id: "hDwoCrm2pkU"
url: "https://www.youtube.com/watch?v=hDwoCrm2pkU"
published: 2020-10-17
duration: "8:16"
tags: [solidworks, cad, tutorial, scuttle, feature-recognition, step-files]
ingested: 2026-05-02
---

## Overview

David walks through SolidWorks' manual FeatureWorks "Recognize Features" workflow on an imported STEP/XB file, rebuilding a corner bracket part feature-by-feature so it behaves like a native SLDPRT instead of a dumb solid body. The exercise is part of preparing a new assembly for the open-source [[entities/projects/scuttle-robot|SCUTTLE robot]].

## Key takeaways

- After 5-10 years of SolidWorks use, David tried manual feature recognition for the first time and recommends it over rebuilding from scratch when an imported model misbehaves.
- Right-click the solid body, choose FeatureWorks, then Recognize Features before doing anything else so you don't interfere with the model.
- Walk through one feature type at a time: boss extrudes first, then cut extrudes for pockets and holes, then fillets last (he notes fillets ideally should have been done first).
- For complicated parts, manual recognition becomes tedious — every line segment may need clicking — so it's not always worthwhile.
- Group same-radius fillets into one feature for cleanliness; group cut extrudes that share a plane.
- Anchor the first sketch to the front plane so the rebuilt part is properly grounded.
- "Every day I do a little work and if I have five minutes of free time I try a new function" — incremental self-training while staying productive.

## Techniques demonstrated

- [[concepts/feature-tree-naming|feature tree naming]] (implicit through the rebuild ordering)
- [[concepts/parametric-design|parametric design]] (recovering parametric structure from a static import)
- [[concepts/cad-configurations|CAD configurations]] (related — saving the result as a new part with `corner-bracket-3030-dm`)

## Tools used

- [[entities/brands/solidworks|SolidWorks]] (2019-era, FeatureWorks)
- [[entities/tools/3030-extrusion|3030 extrusion]] (the part is a corner bracket for 3030 aluminum extrusion)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]] — the new assembly this part is feeding into

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- 0:03 "I've been using SolidWorks for five or ten years... but I never attempted to do this process of manually importing features."
- 1:09 right-click solid body → FeatureWorks → Recognize Features.
- 3:29 "I should have done the fillets first because that's usually what I do last."
- 6:57 "Every day I do a little work, and if I have five minutes of free time I try a new function. That's how I self-train — I try to train on the fly because I still have to be productive."

## Related videos

- [[tutorial-modeling-and-mindset-for-a-parametric-bracket-solidworks]]
- [[what-is-a-parametric-design-with-solidworks-example]]
- [[how-to-deboss-a-dynamic-revision-number-for-3d-prints-solidworks]]
