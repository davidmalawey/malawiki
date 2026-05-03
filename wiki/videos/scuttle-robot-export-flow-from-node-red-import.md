---
type: video
title: "SCUTTLE Robot - Export Flow from Node Red & Import"
video_id: "YV61BkHeDLQ"
url: "https://www.youtube.com/watch?v=YV61BkHeDLQ"
published: 2019-09-26
duration: "2:20"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, node-red, telemetry, export, github-gist, beaglebone-blue]
ingested: 2026-05-02
---

## Overview

A tighter re-cut of the previous day's [[videos/scuttle-robot-export-nodered-flow|Node-RED export tutorial]]. David shows the minimum steps to export a [[entities/tools/node-red|Node-RED]] dashboard flow to clipboard, paste into a [[entities/tools/github-gist|GitHub Gist]], link that Gist as a comment in the corresponding Python telemetry file, and reimport the flow on a new tab.

## Key takeaways

- Naming the flow (e.g. `export flow`) is optional but helps when you have many.
- Export → Clipboard → All Flows or Current Flow, with Formatted on for readable JSON.
- Save the Gist URL as a comment in `telemetry.py` so anyone running that Python program can find the matching dashboard.
- When importing, paste the raw Gist text into Import → Clipboard → New Flow so it doesn't overwrite the active flow.

## Techniques demonstrated

- [[concepts/node-red-flow-export-import]]
- [[concepts/source-linked-gist]]

## Tools used

- [[entities/tools/node-red|Node-RED]]
- [[entities/tools/github-gist|GitHub Gist]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-export-nodered-flow]] (the original from one day earlier)
- Other [[series/scuttle-tutorials-2019]] tutorials.
