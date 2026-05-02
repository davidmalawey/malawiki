---
type: video
title: "SCUTTLE Robot - Control GPIO Outputs on the BeagleBone Blue with LED Demo"
video_id: "rYfygKmDT4Q"
url: "https://www.youtube.com/watch?v=rYfygKmDT4Q"
published: 2019-11-19
duration: "2:27"
series: "[[series/scuttle-robot]]"
tags: [scuttle, beaglebone-blue, gpio, led, breadboard, python, mxet300]
ingested: 2026-05-02
---

## Overview

Demonstrates how to drive a GPIO output pin on the [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] using SCUTTLE's `L1_gpio.py`. The GP1 connector is recommended for first prototyping because its two outputs mirror the on-board green and red user LEDs.

## Key takeaways

- GP1 (leftmost connector) outputs are tied to the board's green/red user LEDs — free visual feedback while debugging.
- Pin sequence on the 6-pin JST: leftmost wire = green LED line, next = red LED line.
- Demo wiring: 3.3 V from the GPIO pin into an LED, through a 1 kohm resistor, to ground on a breadboard.
- The level-1 file controlling output is `gpio.py`; loop initializes the pin then drives high/low on a timed sequence.
- Useful pattern: when bringing up a new actuator, wire it to GP1 so the on-board LEDs visually confirm pin state.

## Tools and components

- [[entities/tools/beaglebone-y-ai|BeagleBone Blue]]
- LED, 1 kohm resistor, breadboard, 6-pin JST cable
- Python (`L1_gpio.py`)

## Concepts demonstrated

- [[concepts/sensor-actuator-controller-loop]]
- [[concepts/loop-vs-routine]]
- [[concepts/graceful-degradation]]

## Related videos

- [[videos/scuttle-robot-demonstration-for-reading-gpio-input-on-beaglebone-blue-with-l1-gp]]
- [[videos/scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-]]
