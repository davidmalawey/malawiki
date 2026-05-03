---
type: video
title: "SCUTTLE Robot - Plot Gamepad values in Nodered via txt file"
video_id: "EQzNhDv-AKI"
url: "https://www.youtube.com/watch?v=EQzNhDv-AKI"
published: 2020-09-06
duration: "6:35"
tags: [scuttle, nodered, gamepad, telemetry, dashboard, python, raspberry-pi]
ingested: 2026-05-02
---

## Overview

Telemetry tutorial that bridges a USB gamepad axis into a [[entities/tools/nodered|Node-RED]] dashboard via a temporary text file. A small Python script (`l3chart.py`) imports the SCUTTLE-internal `gamepad.py` and `log.py` modules, polls axis values every 0.25 s with `getGP()`, and writes the chosen axis to `/tmp/ufile.txt` using `log.tmpFile()`. Node-RED reads that file at the same cadence, scales it from -1..1 to -100..100, and feeds both a gauge and a line chart on the dashboard.

## Key takeaways

- `/tmp` is the proper place for transient telemetry files on Linux — files vanish on reboot.
- Match the write cadence (0.25 s in Python) to the read/inject cadence (0.25 s in Node-RED) so the chart updates smoothly.
- Node-RED pipeline: timestamp inject -> file in -> [function/scale] -> gauge + line chart.
- Gamepad axes are floats in -1..1; scale up to -100..100 for a readable gauge.
- Some gamepad buttons are binary, but joystick axes are floating-point.
- Two lower-level Python modules do the heavy lifting: `gamepad.py` (provides `getGP`) and `log.py` (provides `tmpFile`).
- "No protocol specified" warning under sudo is benign and doesn't stop execution.

## Techniques demonstrated

- [[concepts/iot-data-flow|IoT / telemetry data flow]] via a shared file
- File-as-IPC between a Python loop and Node-RED
- Range-mapping floats -1..1 -> -100..100 for visualization
- Using `/tmp` for ephemeral data
- Live dashboarding with Node-RED gauges and line charts

## Tools used

- [[entities/tools/nodered|Node-RED]] (gauge, chart, file-in nodes)
- [[entities/tools/raspberry-pi|Raspberry Pi]] / [[entities/tools/beaglebone-y-ai|BeagleBone]]
- USB gamepad
- Python 3 (`l3chart.py`, `gamepad.py`, `log.py`)
- GitHub Gist

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## Notable quotes / timestamps

- 0:43 "There's a folder at a pretty high level called tmp — that's designed for temporary files that are produced during running."
- 4:23 "From gamepad we're grabbing getGP — that collects all of the values from all the buttons in one go."
- 5:18 "Same frequency we're plotting."
- 6:13 "One direction gives me the negative values; max it out you get minus 100."

## Related videos

- [[videos/scuttle-robot-nodered-read-csv-to-send-mqtt]]
- [[videos/scuttle-robot-nodered-receive-mqtt-message-save-to-csv]]
- [[videos/build-a-payload-robot-start-to-finish-scuttle-v2-4]]
