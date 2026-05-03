---
type: video
title: "SCUTTLE Robot - setup vscode to connect to pi and edit software (cloud9 alternative)"
video_id: "HokkkHJgUOo"
url: "https://www.youtube.com/watch?v=HokkkHJgUOo"
published: 2020-09-09
duration: "4:13"
tags: [scuttle-robot, vscode, sftp, ssh, raspberry-pi, beaglebone, dev-environment]
ingested: 2026-05-02
---

## Overview

A short tutorial on installing [[entities/tools/vscode|VS Code]] with the SFTP extension as a dynamic editor for SCUTTLE Python files — a more comfortable alternative to PuTTY/MobaXterm with `nano`, and a reasonable substitute for [[entities/tools/cloud9|Cloud9]] (which ships by default on the BeagleBone but isn't on the Pi). Shoutout to Danielle for showing David the setup.

## Key takeaways

- VS Code's SFTP extension lets you browse and edit files live on the Pi/BeagleBone over SSH from your desktop.
- Configure with `Ctrl+Shift+P` -> `SFTP: config`; only the `host` and login fields need to match your robot.
- "Open SSH in terminal" gives you a working shell inside the VS Code workspace.
- `Edit in local` produces a local working copy; the unsaved-circle / saved-x indicators are your safety cue against editing two divergent copies of the same file.

## Techniques demonstrated

- SFTP-based remote editing
- VS Code workspace setup for embedded Linux

## Tools used

- [[entities/tools/vscode|VS Code]] (with SFTP extension)
- [[entities/tools/putty|PuTTY]] (compared against)
- [[entities/tools/mobaxterm|MobaXterm]] (compared against)
- [[entities/tools/cloud9|Cloud9]] (compared against)
- [[entities/tools/raspberry-pi|Raspberry Pi]]
- [[entities/tools/beaglebone-y-ai|BeagleBone]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]
- [[entities/people/danielle|Danielle]] (credited for the VS Code setup tip)

## Related videos

- [[videos/scuttle-robot-nodered-function-to-extract-each-gamepad-axis-display]]
