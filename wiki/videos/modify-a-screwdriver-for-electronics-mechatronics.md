---
type: video
title: "modify a screwdriver for electronics, mechatronics"
video_id: "Tv_4055fiXU"
url: "https://www.youtube.com/watch?v=Tv_4055fiXU"
published: 2024-06-26
duration: "4:07"
tags: [screwdriver, philips, mechatronics, din-rail, fasteners, tooling]
ingested: 2026-05-02
---

## Overview

[[entities/people/david-malawey|David]] explains why a Phillips driver size mismatch on small DIN-rail terminals can leave electrical connections under-torqued (and thus dangerous), and shows the fix: take a Phillips zero, file down its tip to roughly a Phillips one cross-section, and you get a driver whose shank fits the terminal hole while the tip carries one-size's worth of torque.

## Key takeaways

- Phillips sizes (PH0, PH1, PH2, PH3) are designed to match the size of screw they drive — and small Phillips heads on big screws are deliberate, intended to slip before over-torquing.
- Dinkle [[entities/tools/din-rail|DIN-rail]] terminal data sheets specify Phillips 1, but the typical PH1 shank from most suppliers is too fat to enter the access hole — a documented data-sheet mismatch.
- The fix: file down a PH0 tip until it cross-sections like a PH1. The shank stays slim enough to enter the terminal cavity, but the tip carries PH1 torque.
- Wrong size (using stock PH0) either strips the driver or — worse — limits your tightening torque so a 240 V terminal can vibrate loose later.
- [[entities/brands/dewalt|DeWalt]] PH1 has a particularly girthy shank that can be confused with a PH2 once dirty or scratched.
- Flat-head drivers are sized in millimeters of head width.

## Techniques demonstrated

- Filing a Phillips zero into a hybrid PH0-shank / PH1-tip driver.
- Reading screw-driver size hints to anticipate the designer's intended torque (small head = intentional torque limiter).
- [[concepts/torque-evaluation-on-assembled-fastener|Torque evaluation on assembled fastener]] — recognizing under-torque hazards on terminals.

## Tools used

- Phillips screwdrivers (PH0, PH1, PH2, PH3)
- File (for tip modification)
- Dinkle DIN-rail terminal block (the problem case)

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [1:45] "I learned a very difficult lesson about Phillips 1 and Phillips Z[ero]."
- [2:43] "When you use the wrong size... you'll limit the torque... and then your terminals can be loose, and then you can just have 240 volts or something like that just floating around."
- [3:42] "When they put a very small Phillips size on there, it's because they want to limit how much torque you can apply before this thing slips out."

## Related videos

- [[videos/exoskeleton-design-control-of-fastener-torque]]
- [[videos/hack-a-soldering-iron-with-a-mechanical-engineer]]
- [[videos/tapping-threads-in-extrusion-for-beginners]]
