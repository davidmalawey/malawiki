---
type: video
title: "Program a PLC with Conveyor, Arduino and Industrial Robot"
video_id: "30GM4m-Lyec"
url: "https://www.youtube.com/watch?v=30GM4m-Lyec"
published: 2021-09-29
duration: "22:00"
series: "[[series/mxet-conveyor-demo]]"
tags: [plc, arduino, conveyor, mechatronics, mxet, sensors, teaching]
ingested: 2026-05-02
---

## Overview

A 22-minute walkthrough of the MXET 400 conveyor demo at Texas A&M — a teaching system that integrates a Productivity1000 PLC (P1AM-100), an ESP8266/NodeMCU running an Arduino sketch, a VL53 time-of-flight distance sensor, two UR3e industrial robots, and a Dorner conveyor. David covers system documentation, power distribution, CAD file sourcing from AutomationDirect / GrabCAD, programming the PLC in Productivity Blocks (which exports to Arduino-compatible C++), pin-vs-slot addressing on the P1AM, the Productivity-Blocks-to-Arduino one-way export, and the Arduino tab structure (`.h` files for sensor and buzzer functions) that polls the VL53 and signals the PLC over GPIO.

## Key takeaways

- The system fans 120 V wall power through an e-stop, then a power switch, then to a 24 V DIN-rail supply that powers the P1AM and a 24 V output module; the conveyor controller takes its own 120 V feed.
- DIN rail itself is grounded; the green/yellow terminal block bonds to it.
- Productivity Blocks exports to a `.ino` file but **does not re-import** — once you customize the C++, edits to the visual program will overwrite your file on verify/upload.
- "Pin" addresses in Productivity Blocks refer to the P1AM's left-side terminal block; "slot" addresses refer to right-side expansion modules.
- The ESP8266 (NodeMCU) reads a VL53 distance sensor over I2C, blares a buzzer when an object is near, and signals the PLC over a GPIO line (D4) — fully digital handoff, no I2C between ESP and PLC.
- Splitting helper code into `.h` tabs (`buzzerFunctions.h`, `vl53Functions.h`) lets you control include order, which matters when libraries collide.
- The main loop runs ~50 Hz, more than enough to catch a soda can passing the sensor at conveyor speed.
- VL53 returns 0 when out of range; treat 0 as "no reading" and skip it before threshold logic.

## Techniques demonstrated

- [[concepts/plc-programming|PLC programming]] with Productivity Blocks (graphical → C++)
- [[concepts/plc-relay-control|PLC relay control]] of a conveyor
- [[concepts/i2c-sensor-integration|I2C sensor integration]] (VL53 on NodeMCU)
- [[concepts/system-power-distribution|System power distribution]] for mixed-voltage industrial demos
- [[concepts/din-rail-wiring|DIN rail wiring]]
- [[concepts/sensor-actuator-controller-loop|Sensor-actuator-controller loop]]

## Tools used

- [[entities/tools/p1am-100|P1AM-100 PLC]] (Arduino-compatible Productivity1000 controller)
- [[entities/tools/productivity-blocks|Productivity Blocks]] (graphical PLC IDE)
- [[entities/tools/arduino-ide|Arduino IDE]]
- [[entities/brands/arduino|Arduino]]
- [[entities/tools/esp8266-nodemcu|ESP8266 NodeMCU]]
- [[entities/tools/vl53-distance-sensor|VL53 distance sensor]]
- [[entities/tools/buzzer|Buzzer]]
- [[entities/tools/dorner-conveyor|Dorner conveyor]]
- [[entities/tools/ur3e|UR3e industrial robot]]
- [[entities/tools/relay-module|4-relay module]]
- [[entities/tools/24v-power-supply|24 V power supply]]
- [[entities/tools/e-stop|E-stop]] (push-pull)
- [[entities/tools/din-rail|DIN rail]]
- [[entities/brands/automation-direct|Automation Direct]]
- [[entities/brands/grabcad|GrabCAD]]
- [[entities/brands/solidworks|SolidWorks]]

## Projects

- [[entities/projects/mxet-conveyor-demo|MXET Conveyor Demo]]

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Places

- [[entities/places/texas-am-lab|Texas A&M lab]]

## Related videos

- [[videos/program-a-plc-with-conveyor-arduino-and-industrial-robot-part-2]]
- [[videos/how-much-cpu-does-it-take-to-generate-pwm-signals-on-raspberry-pi]]
