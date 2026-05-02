---
type: video
title: "How much CPU does it take to generate PWM signals on Raspberry Pi?"
video_id: "P2Zvfztf68M"
url: "https://www.youtube.com/watch?v=P2Zvfztf68M"
published: 2021-04-09
duration: "5:57"
series: "[[series/scuttle-robot-build]]"
tags: [scuttle, raspberry-pi, pwm, motor-control, benchmarking, mechatronics]
ingested: 2026-05-02
---

## Overview

A small benchmark: David runs four software-PWM channels (the SCUTTLE setup — two motors, two channels each) on a Raspberry Pi 3B+ and watches `htop` to see how the CPU load scales with PWM frequency. At 150 Hz the load is trivial (under 4%); at 15 kHz it climbs to ~108% summed across cores. The video sets up the case for switching at least two channels over to hardware PWM via the pigpio daemon.

## Key takeaways

- Software PWM cost on a Pi 3B+ scales roughly linearly with frequency × number of channels.
- 150 Hz × 4 channels = under 4% total CPU; motors sound rough and don't reach spec torque.
- 1.5 kHz is the practical minimum for smooth, torque-faithful brushed-motor drive.
- 15 kHz × 4 channels saturates a core (~108% summed), and other parts of the program become noticeably less responsive.
- Pi 3B+ has four threads, so `htop` shows four bars and percentages can sum past 100.
- Next step: move two channels to hardware PWM (GPIO 12/13) via a daemon (pigpio).

## Techniques demonstrated

- [[concepts/pwm|PWM]] software vs. hardware tradeoffs
- [[concepts/benchmarking-design|Benchmarking design]] — quick-and-dirty CPU load profiling with `htop`

## Tools used

- [[entities/brands/raspberry-pi|Raspberry Pi]] (3B+)
- [[entities/tools/dual-h-bridge-motor-driver|Dual H-bridge motor driver]]
- [[entities/tools/dc-gearmotor|DC gearmotor]]
- [[entities/tools/htop|htop]] (Linux process viewer)

## Projects

- [[entities/projects/scuttle-robot|SCUTTLE Robot]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Notable quotes / timestamps

- [4:42] "At 15 kilohertz... you've consumed what totals to be 108 percent."
- [5:25] "Our next step is to use outputs 12 and 13 which correspond to actual hardware-based PWM cycles, and run a daemon and tap into the hardware capabilities."

## Related videos

- [[videos/how-to-connect-a-hobby-esc-speed-control-to-raspberry-pi-drive-a-12v-dc-motor-bi]]
- [[videos/fully-explained-build-test-setup-pwm-generator-dc-motor-driver-gearmotor]]
