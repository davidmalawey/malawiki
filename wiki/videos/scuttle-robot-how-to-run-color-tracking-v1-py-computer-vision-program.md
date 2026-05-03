---
type: video
title: "SCUTTLE Robot - How to run color_tracking_v1.py computer vision program"
video_id: "PZ6i2W_9lJE"
url: "https://www.youtube.com/watch?v=PZ6i2W_9lJE"
published: 2019-03-08
duration: "4:08"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, computer-vision, color-tracking, opencv, python, beaglebone]
ingested: 2026-05-02
---

## Overview

David demonstrates running `color_tracking_v1.py` on the [[entities/projects/scuttle-robot|SCUTTLE robot]]. The program is pulled from GitHub raw view, pasted into [[entities/tools/cloud9|Cloud9]] on the [[entities/tools/beaglebone-blue|BeagleBone Blue]], saved, and executed from the terminal. With a [[entities/tools/usb-webcam|USB webcam]] attached, the script counts pixels matching a calibrated color range (basketball orange) and emits "too-far / too-close / left / right / turning" decisions based on the apparent radius and centroid X-coordinate.

## Key takeaways

- The "raw" button on GitHub is the canonical copy source — Ctrl-A, Ctrl-C, paste into a new Cloud9 file with the matching name so everyone is on the same page.
- Loading OpenCV (cv.py) libraries on first run takes noticeable time; one "corrupt JPEG data" warning per frame is normal startup noise from the USB camera, not a failure.
- The program uses pixel count to estimate distance: more pixels of the target color → smaller perceived range, fewer pixels → too far. Center-pixel X-coordinate drives left/right turning.
- Lighting must match the calibration environment — the demo's "too-close" condition was hard to trigger because the room lighting differed from where calibration was done.

## Techniques demonstrated

- [[concepts/apparent-size-ranging|apparent-size-ranging]] — pixel count from a colored target maps to distance.
- [[concepts/vision-driven-kinematics|vision-driven-kinematics]] — centroid X-coordinate and pixel-count drive the turning and approach decisions.
- [[concepts/sensor-calibration|sensor-calibration]] — color thresholds depend on the calibration scene's lighting.
- [[concepts/threshold-switching-control|threshold-switching-control]] — discrete states (too-far, too-close, turning-left, turning-right) emerge from threshold comparisons rather than continuous control.
- [[concepts/source-linked-gist|source-linked-gist]] — script is canonical-source-linked from GitHub raw view.

## Tools used

- [[entities/tools/beaglebone-blue|BeagleBone Blue]]
- [[entities/tools/cloud9|Cloud9]]
- [[entities/tools/usb-webcam|USB webcam]]
- [[entities/tools/opencv|OpenCV]]
- [[entities/tools/github|GitHub]]
- [[entities/tools/python|Python]]
- [[entities/tools/color-tracking-v1|color_tracking_v1.py]]

## Materials used

- basketball (used as orange-color test target)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable timestamps

- 0:21 — Grab `color_tracking_v1.py` from GitHub raw.
- 1:36 — "Corrupt JPEG data" startup warning is harmless.
- 2:15 — Pixel-count-vs-radius distance estimation explained.
- 3:24 — Centroid X drives left/right turning logic.

## Related videos

- [[videos/scuttle-robot-nextec-team-tests-computer-vision-docking]]
- [[videos/scuttle-robot-autonomous-docking-by-machine-vision-for-wireless-charging]]
- [[videos/scuttle-robot-using-matlab-gui-v1-1]]
- [[videos/scuttle-robot-intro-to-software-architecture]]
