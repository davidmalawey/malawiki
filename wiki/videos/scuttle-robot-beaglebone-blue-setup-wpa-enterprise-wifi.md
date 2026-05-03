---
type: video
title: "SCUTTLE Robot - Beaglebone Blue setup WPA enterprise WiFi"
video_id: "5l-xO3AWcM8"
url: "https://www.youtube.com/watch?v=5l-xO3AWcM8"
published: 2019-08-26
duration: "4:13"
tags: [scuttle, beaglebone-blue, wifi, wpa-enterprise, mxet, debian, cloud9]
ingested: 2026-05-02
---

## Overview

Setup instructions for connecting a [[entities/tools/beaglebone-blue|BeagleBone Blue]] to a WPA Enterprise Wi-Fi network (specifically the Texas A&M `tamulink-wpa` AP, which requires both a username and password). David grabs `setup_wpa_enterprise.py` from the SCUTTLE GitHub, pastes it into a local text file, then connects PC-to-Beagle by Wi-Fi (default password `BeagleBone`), opens the [[entities/tools/cloud9|Cloud9]] IDE at `192.168.1.x:3000`, recreates the Python file in the home directory, and runs it with sudo to enter credentials. After a reboot the Beagle auto-connects to the enterprise network. Supports MXET 300 Lab 1, Fall 2019.

## Key takeaways

- Enterprise APs require both a username and a password, unlike home WPA-PSK networks — a dedicated setup script (`setup_wpa_enterprise.py`) handles writing the right Debian config.
- Bootstrap the Beagle by connecting through its own Wi-Fi AP first, using `192.168.1.x:3000` to reach the Cloud9 IDE in a browser.
- The script masks the password input but not the username — useful detail when recording or sharing screen.
- After running once, the Beagle saves a config file and auto-reconnects on subsequent boots.

## Techniques demonstrated

- [[concepts/wpa-enterprise-setup|WPA Enterprise setup]]
- [[concepts/soft-ap-discovery|soft AP discovery]]
- [[concepts/cloud9-ide-workflow|Cloud9 IDE workflow]]
- [[concepts/raw-github-paste|raw GitHub paste]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/cloud9|Cloud9]]
- [[entities/tools/notepad-plus-plus|Notepad++]]
- [[entities/tools/github|GitHub]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Places

- [[entities/places/texas-am|Texas A&M]]

## Related videos

- [[videos/scuttle-robot-check-your-wifi-ssid-over-usb-on-beaglebone-blue]]
- [[videos/scuttle-robot-check-boot-drive-space-in-debian-on-beaglebone-blue]]
- [[videos/scuttle-robot-setup-vscode-to-connect-to-pi-and-edit-software-cloud9-alternative]]
