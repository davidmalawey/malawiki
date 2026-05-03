---
type: video
title: "SCUTTLE Robot - using Matlab GUI v1.1"
video_id: "fwuoglO3J0k"
url: "https://www.youtube.com/watch?v=fwuoglO3J0k"
published: 2019-03-05
duration: "4:03"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, matlab, gui, telemetry, udp, beaglebone]
ingested: 2026-05-02
---

## Overview

David walks through downloading the SCUTTLE GUI v1.1 zip from GitHub, syncing the latest `UDP_MATLAB.py` script onto the [[entities/tools/beaglebone-blue|BeagleBone Blue]] via [[entities/tools/cloud9|Cloud9]], and launching the [[entities/tools/matlab|MATLAB]] runtime executable on a host PC. The GUI displays live telemetry — battery voltage, IMU pitch/roll, compass, wheel speeds — and exposes keyboard arrow-key driving as a manual override.

## Key takeaways

- Workflow is: pull script from GitHub, paste into Cloud9 over the existing `UDP_MATLAB.py`, save, run on the BeagleBone, then launch the GUI executable on the PC.
- The MATLAB runtime (v9.5) is a free dependency required to run the compiled GUI; the version requirement is documented in the readme.
- Only some fields are wired up in v1.1 — battery voltage from the barrel plug is reliable; pitch/roll come straight from the BeagleBone IMU; compass is only accurate if calibrated; wheel speeds remain stale from a previous control method.
- Arrow keys drive the robot live, and once compass and wheel-speed calibration are complete the GUI will draw an approximate trajectory map.

## Techniques demonstrated

- [[concepts/source-linked-gist|source-linked-gist]] — pulling the latest script from GitHub raw view.
- [[concepts/manual-override-coexistence|manual-override-coexistence]] — keyboard arrow keys drive the robot alongside live telemetry display.
- [[concepts/sensor-calibration|sensor-calibration]] — fields like compass and wheel speed only become trustworthy after calibration.
- [[concepts/working-placeholder-design|working-placeholder-design]] — un-wired fields are left at "100%" defaults so the GUI ships even before all telemetry is hooked up.

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/cloud9|Cloud9]]
- [[entities/tools/matlab|MATLAB]]
- [[entities/tools/matlab-runtime|MATLAB Runtime]] v9.5
- [[entities/tools/scuttle-gui|SCUTTLE GUI]] v1.1
- [[entities/tools/github|GitHub]]
- [[entities/tools/mpu9250|onboard IMU]] (BeagleBone Blue's built-in)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable timestamps

- 0:25 — Copy `UDP_MATLAB.py` from GitHub into Cloud9.
- 1:43 — Unzip and launch `scuttle GUI.exe`.
- 2:28 — Click "connect"; live fields populate.
- 3:15 — Drive with keyboard arrow keys.

## Related videos

- [[videos/scuttle-robot-secure-your-beaglebone-blue]]
- [[videos/scuttle-robot-setup-vscode-to-connect-to-pi-and-edit-software-cloud9-alternative]]
- [[videos/scuttle-robot-how-the-magnetometer-sensor-compass-works]]
- [[videos/scuttle-robot-intro-to-software-architecture]]
