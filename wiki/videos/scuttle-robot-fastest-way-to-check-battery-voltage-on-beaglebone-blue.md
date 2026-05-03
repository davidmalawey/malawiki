---
type: video
title: "SCUTTLE Robot - fastest way to check battery voltage on beaglebone Blue"
video_id: "yBV0TCLIw5Y"
url: "https://www.youtube.com/watch?v=yBV0TCLIw5Y"
published: 2019-02-20
duration: "1:51"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle-robot, beaglebone-blue, battery, ssh, tutorial]
ingested: 2026-05-02
---

## Overview

Quick how-to for checking pack voltage on a [[entities/tools/beaglebone-blue|BeagleBone Blue]] over SSH using the built-in `rc_battery_monitor` utility. Demonstrates Wi-Fi SSH login via [[entities/tools/putty|PuTTY]], tab-completion to discover the command, and the `sudo` requirement for the live battery feed.

## Key takeaways

- Connect over Wi-Fi and SSH in via [[entities/tools/putty|PuTTY]].
- Type `rc_` and tab-complete to find `rc_battery_monitor` — useful pattern for discovering BeagleBone's `rc_*` library tools.
- The command must run as root: prefix with `sudo`.
- The live readout reports both the onboard pack and the barrel-jack supply; for SCUTTLE, watch the `Jack` reading.
- Floor for the barrel jack: 9 V under load, 8 V at no-load — below that, stop drawing or risk over-discharge of the pack covered in the [[videos/dont-destroy-your-18650-cells-use-this-analogy-to-understand|18650 video]].
- Exit the live monitor with Ctrl-C.

## Techniques demonstrated

- [[concepts/ssh-tab-completion-discovery]]
- [[concepts/sudo-required-utility]]
- [[concepts/battery-protection-circuit]]
- [[concepts/live-telemetry-readout]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/putty|PuTTY]]
- [[entities/tools/rc-battery-monitor|rc_battery_monitor]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## Notable quotes / timestamps

- 0:00 Intro
- 0:22 Check battery voltage
- 0:45 Run RC battery monitor
- 1:13 Barrel Jack

## Related videos

- [[videos/dont-destroy-your-18650-cells-use-this-analogy-to-understand]]
- [[videos/scuttle-robot-check-boot-drive-space-in-debian-on-beaglebone-blue]]
- [[videos/scuttle-robot-control-gpio-outputs-on-the-beaglebone-blue-with-led-demo]]
