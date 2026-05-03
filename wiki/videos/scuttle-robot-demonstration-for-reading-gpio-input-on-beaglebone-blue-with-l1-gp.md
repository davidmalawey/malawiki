---
type: video
title: "SCUTTLE Robot - Demonstration for reading GPIO Input on Beaglebone Blue with L1_gpio.py"
video_id: "DJ4fFIYNFxI"
url: "https://www.youtube.com/watch?v=DJ4fFIYNFxI"
published: 2019-11-20
duration: "1:56"
series: "[[series/scuttle-robot]]"
tags: [scuttle, beaglebone-blue, gpio, input, breadboard, python, pull-down]
ingested: 2026-05-02
---

## Overview

Companion to the GPIO output demo. Shows reading GPIO input on the [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] using the updated `L1_gpio.py`, with a button-and-LED pull-down test circuit on a breadboard.

## Key takeaways

- The new `L1_gpio.py` simplifies pin naming (port/pin pairs like `cord 0, pin 1`) for faster prototyping.
- Demo circuit: 3.3 V supply on rail; pushbutton bridges row 4 to row 6, completing a path through an LED and resistor to ground; the yellow signal wire on `n1` is held low through the pull-down resistor until the button is pressed.
- Pressing the button drives `n1` to 3.3 V — the program reads `1`; releasing reads `0`.
- Pattern: same GP1 connector convenience as the output demo (LEDs mirror the pin state for visual debug).

## Tools and components

- [[entities/tools/beaglebone-y-ai|BeagleBone Blue]] (GPIO port 0)
- Pushbutton, LED, resistors, breadboard
- Python `L1_gpio.py`

## Concepts demonstrated

- [[concepts/sensor-actuator-controller-loop]]
- [[concepts/feature-tree-naming]]

## Related videos

- [[videos/scuttle-robot-control-gpio-outputs-on-the-beaglebone-blue-with-led-demo]]
- [[videos/scuttle-robot-multithreading-explained-with-demonstration-speed-control-text-to-]]
