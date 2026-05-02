---
type: video
title: "Economics of Mechanical Designs (Part 2)"
video_id: "qSascGA3_lM"
url: "https://youtu.be/qSascGA3_lM"
published: 2022-12-02
duration: "6:54"
series: "[[series/economics-of-mechanical-design]]"
tags: [design-economics, 3d-printing, commodity-parts, modularity, open-source-hardware, essay]
ingested: 2026-05-02
---

## Overview

The solution half of David's two-part essay. Stop trying to *re-engineer* fine tolerances — *borrow* them from off-the-shelf commodities (brass threaded inserts, spring steel, ball bearings, HDPE tube, steel screws) and use 3D-printed parts only where you genuinely need custom geometry. The mindset extends from borrowing a single property (roundness, modulus, airtightness) to borrowing whole electromechanical assemblies. The end-state: hardware design that mirrors software economics — modular, copyable, parametric, evolving rapidly across the world.

## Key takeaways

- Three regimes — prototype (high price, fine tolerance), commodity (low price, fine tolerance), 3D print (low price, looser tolerance). The 3D print's job is to *connect* commodity parts, not replace them.
- Each commodity supplies one engineered property to your design: brass inserts give thread tolerance, spring steel gives modulus + diameter accuracy, ball bearings give roundness, HDPE gives chemical resistance + roundness, steel screws give strength.
- You can scale this up to borrowing an *entire* electromechanical assembly (motor + drive + software) and using a 3D print only for the mechanical interface to your extrusions.
- "Don't re-engineer a whole system. Borrow the performance of off-the-shelf parts, borrow their fine tolerances, borrow their low cost — only design the unique elements."
- Hardware can now mirror 20 years of software economics because vendors ship parametric CAD models with their parts, making the design side itself feel like software.
- "Digital manufacturing" is broader than 3D printing — it includes all processes that go straight from digital design to a part without analog engineering overhead. Worth a separate video.
- Recap: update the design mindset, transfer fine tolerances to commodities, eliminate manufacturing engineering overhead from custom designs, commoditize custom design itself, save trillions.

## Techniques demonstrated

- [[concepts/borrowing-tolerances]] — the central thesis
- [[concepts/leverage-incumbent-engineering]]
- [[concepts/modularity]]
- [[concepts/parametric-design]]
- [[concepts/open-source-hardware-publishing]]
- [[concepts/parts-ecosystem-design]] — designing into an existing ecosystem of commodity hardware

## Tools used

- [[entities/tools/3d-printer|3D printer]]
- [[entities/tools/threaded-insert|Brass threaded inserts]]
- [[entities/tools/ball-bearings|Steel ball bearings]]
- Spring-steel "fingers" (collet style)
- Steel screws
- Aluminum cast/machined camera-mount components (borrowed assembly)

## Materials used

- [[entities/materials/spring-steel|Spring steel]]
- [[entities/materials/hdpe|HDPE]]
- [[entities/materials/aluminum|Aluminum]] (cast/machined)
- Brass

## Projects

(none — methodology synthesis with worked examples)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [0:45] "Borrowing performance" — the chapter that names the technique.
- [3:33] "Don't reinvent the wheel."
- [4:09] "We can begin to make hardware the way software has been for the last 20 years."
- [4:50] "Digital manufacturing... is more than just 3D printing."
- [5:22] "These components that we buy now are beginning to come with their own CAD models, often parametric."
- [6:51] "Then we save trillions."

## Related videos

- [[videos/economics-of-mechanical-design-part-1]] — the problem statement
- [[videos/how-to-design-a-functional-printable-open-source-mechanical-part]] — practical demonstration of borrowing a 608 bearing's tolerances inside a printed sleeve
- [[videos/borrow-a-tolerance-mindset-for-designers]]
- [[videos/highly-engineered-emt-conduit-parts-to-study-before-designing]]
