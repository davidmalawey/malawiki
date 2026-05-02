---
type: video
title: "SCUTTLE Robot - nodered function to extract each gamepad axis & display"
video_id: "hzgSystU4yI"
url: "https://www.youtube.com/watch?v=hzgSystU4yI"
published: 2020-09-09
duration: "7:20"
tags: [scuttle-robot, node-red, gamepad, csv, dashboard]
ingested: 2026-05-02
---

## Overview

David walks through how to format a CSV-style text file written by his Python gamepad reader so that [[concepts/node-red|Node-RED]] can extract two separate axis values (theta-dot for turn, x-dot for forward motion) and display them on dashboard gauges. He demonstrates two equivalent JavaScript approaches inside Node-RED function nodes, plus the `watch` node as a change-driven trigger that auto-syncs Node-RED's frequency to the upstream Python program.

## Key takeaways

- Drop the trailing space when writing CSV from Python — it breaks parsing in Node-RED downstream.
- The `watch` node injects a trigger only on file change, so Node-RED inherits the producer's update rate for free.
- Two function syntaxes both work: `msg.payload = msg.payload["gamepad.thetadot"]` (bracket reach-in) and `msg.payload = msg.payload.gpx` (dot reassignment, cleaner).
- Editing files inside `/tmp` requires `sudo` because of the super-user permissions on that folder.
- Verify axis polarity (left turn = positive theta-dot, forward = positive x-dot) by physically driving the gauges before trusting them.

## Techniques demonstrated

- [[concepts/node-red|Node-RED dashboard wiring]]
- CSV column extraction inside Node-RED function nodes
- File-watch event-driven flows

## Tools used

- [[entities/tools/gamepad|gamepad]] (Xbox-style)
- [[entities/tools/raspberry-pi|Raspberry Pi]] running the Python loop
- Node-RED dashboard (browser)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- Companion video on writing the CSV from gamepad input (referenced as the previous upload)
- [[videos/scuttle-robot-setup-vscode-to-connect-to-pi-and-edit-software-cloud9-alternative]]
