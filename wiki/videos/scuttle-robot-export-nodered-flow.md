---
type: video
title: "SCUTTLE Robot - Export NodeRed flow"
video_id: "mzOOg71oGzs"
url: "https://www.youtube.com/watch?v=mzOOg71oGzs"
published: 2019-09-25
duration: "4:40"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, node-red, telemetry, export, github-gist]
ingested: 2026-05-02
---

## Overview

Walkthrough of exporting a [[entities/tools/node-red|Node-RED]] flow that visualizes SCUTTLE telemetry (X-dot and theta-dot from the kinematics module) so it can be shared or reimported. David demonstrates the full path: Python program writes telemetry to text files, Node-RED reads those files and updates a dashboard, then the flow is exported via clipboard and stashed as a [[entities/tools/github-gist|GitHub Gist]] linked from the Python source as a comment.

## Key takeaways

- The kinematics module returns a C-array with X-dot (linear) and theta-dot (angular) wheel-derived speeds.
- Python `log_unique_file` function emits `.txt` files that Node-RED tails for live dashboard updates.
- File-path prefix in `log.py` must match the path Node-RED reads from.
- Spinning only the right wheel forward should produce positive X-dot AND positive theta-dot — a quick sanity check on kinematics signs.
- Export flow: top-right menu → Export → Clipboard → Formatted, paste into a public Gist, link the Gist URL as a comment in the Python source for reproducibility.
- Import flow: Import → Clipboard → paste raw text → New Flow.

## Techniques demonstrated

- [[concepts/node-red-flow-export-import]]
- [[concepts/telemetry-via-flat-files]]
- [[concepts/kinematics-sign-check]]
- [[concepts/source-linked-gist]]

## Tools used

- [[entities/tools/node-red|Node-RED]]
- [[entities/tools/github-gist|GitHub Gist]]
- [[entities/tools/beaglebone-blue|BeagleBone Blue]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-export-flow-from-node-red-import]] (next-day re-recording)
- Other [[series/scuttle-tutorials-2019]] tutorials.
