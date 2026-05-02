---
type: video
title: "SCUTTLE Robot - Check boot drive space in Debian on Beaglebone Blue"
video_id: "SzzNJBzTZss"
url: "https://www.youtube.com/watch?v=SzzNJBzTZss"
published: 2019-09-04
duration: "3:01"
series: "[[series/scuttle-tutorials-2019]]"
tags: [scuttle, beaglebone-blue, debian, linux, tutorial]
ingested: 2026-05-02
---

## Overview

A short reference clip showing how to inspect boot drive partitions and free space on the [[entities/tools/beaglebone-blue|BeagleBone Blue]] Debian image used for the [[entities/projects/scuttle-robot|SCUTTLE robot]]. David walks through `fdisk -l` output to identify which partition is booted and `df -h /` to see used vs. available space.

## Key takeaways

- After running the SCUTTLE self-installer part 1, the SD card partition is grown from ~3.6 GB to 14.5 GB.
- `fdisk -l` lists all partitions; the partition marked with a `*` is the active boot device.
- The internal eMMC on the BeagleBone shows up as a separate block device (~3.6 GB usable).
- Advertised storage capacity is always slightly less than usable in the OS.
- `df -h /` shows percentage used of root filesystem; flash drives or additional partitions also appear here.

## Techniques demonstrated

- [[concepts/linux-partition-inspection]]
- [[concepts/sd-card-partition-expansion]]

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/sd-card]]

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related videos

- Other early-2019 SCUTTLE tutorials in the [[series/scuttle-tutorials-2019]] series.
