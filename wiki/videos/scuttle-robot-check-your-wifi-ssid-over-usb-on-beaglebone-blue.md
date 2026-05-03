---
type: video
title: "SCUTTLE Robot - check your wifi SSID over USB on Beaglebone Blue"
video_id: "C7K95wd_ezU"
url: "https://www.youtube.com/watch?v=C7K95wd_ezU"
published: 2019-07-19
duration: "2:03"
tags: [scuttle, beaglebone-blue, wifi, ssid, ssh, mxet]
ingested: 2026-05-02
---

## Overview

A short SCUTTLE setup tutorial for finding the SSID of the Wi-Fi access point that the [[entities/tools/beaglebone-blue|BeagleBone Blue]] broadcasts when first plugged in over USB. David SSHs into the board with [[entities/tools/mobaxterm|MobaXterm]], runs `journalctl | grep wl18` to surface the soft AP info, and shows that `ifconfig` is an easier-to-remember alternative — both reveal the four-character suffix that uniquely identifies the board's SSID.

## Key takeaways

- A fresh BeagleBone Blue broadcasts its own Wi-Fi access point by default; you need to know its SSID before you can connect a PC to it.
- `journalctl | grep wl18` filters the system journal for the wl18 Wi-Fi module's setup messages, exposing the SSID and MAC.
- `ifconfig` shows the same information under interface `softap0` — easier to recall.
- The last 4 characters of the MAC become the board-unique tail of the SSID.

## Techniques demonstrated

- [[concepts/journalctl-grep-debug|journalctl grep debug]]
- [[concepts/soft-ap-discovery|soft AP discovery]]
- [[concepts/ssh-over-usb|SSH over USB]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/mobaxterm|MobaXterm]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- [[videos/scuttle-robot-beaglebone-blue-setup-wpa-enterprise-wifi]]
- [[videos/scuttle-robot-check-boot-drive-space-in-debian-on-beaglebone-blue]]
- [[videos/scuttle-robot-control-gpio-outputs-on-the-beaglebone-blue-with-led-demo]]
