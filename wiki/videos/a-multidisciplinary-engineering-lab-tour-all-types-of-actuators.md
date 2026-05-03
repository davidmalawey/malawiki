---
type: video
title: "A Multidisciplinary Engineering Lab Tour - all types of actuators"
video_id: "23hqRMnvwW4"
url: "https://www.youtube.com/watch?v=23hqRMnvwW4"
published: 2025-03-14
duration: "1:14:33"
tags: [lab-tour, actuators, motors, pumps, valves, batteries, heating, cooling, reference]
ingested: 2026-05-02
---

## Overview

David's first full lab tour, organized as a taxonomy of actuators rather than by station or project. Over 70+ minutes he walks through every category of motion, fluid, force, energy storage, and heat-handling actuator the multidisciplinary engineering lab supports — the same lab that hosts Scuttle development. Companion PDF outline lives on the openLab GitHub.

## Key takeaways

- The lab is a space for putting any type of actuator into a functional device. Everything in the lab is, in a sense, an actuator.
- Linear, rotating, and oscillating motion are the three motion families. Air flow, liquid flow, and pressure are the three fluid families. Storing energy and moving heat round out the taxonomy.
- Stepper motors require dedicated drivers (a "silent stepper driver" example is shown installed in a Creator Pro 3D printer); brushless DC fans surprisingly only need power and ground (the third wire is a tach signal).
- Lithium-ion (~3.6 V nominal) and LiPo (Lithium Polymer, ~3.7 V nominal) are nearly interchangeable in casual usage; LiPo is a modified Li-ion. 18650 cells are the lab's central format. LiFePO4 is a separate chemistry.
- Pneumatic and hydraulic actuators (a hydraulic press piston is shown), solenoid valves, needle valves, and pressure vessels (including a fire extinguisher) are all surveyed.
- Fans, water pumps, bilge pumps, aquarium pumps, and air bubblers are walked through as examples of liquid- and air-flow actuators.
- Heat-moving (heat sinks, copper coils, radiator fans) vs. heat-generating (water heaters, hot air guns, infrared bulbs) actuators are kept conceptually distinct.

## Techniques demonstrated

- Categorizing every device in a multidisciplinary lab by actuator type rather than by application.
- Reading a fan's wires (red/black for power, third for tach) as an example of [[concepts/borrowing-tolerances|reading datasheets and standards]] across brands.

## Tools used

- Stepper motors and stepper drivers (silent stepper drivers in a FlashForge Creator Pro)
- AC motors, brushless DC motors, [[entities/tools/computer-fan|computer fans]]
- Linear actuators, lock actuators, vibrators, oscillating tools, ultrasonic actuators
- Air pumps, centrifugal fans, radiator fans, water pumps, bilge pumps, aquarium pumps, air bubbler pumps, piston pumps
- Pressure vessels, fire extinguishers, solenoid valves, needle valves, hydraulic pistons, screw vices
- Heat sinks, copper coils, water heaters, hot air guns, infrared bulbs
- Motor drivers, [[entities/tools/h-bridge|H-bridges]]

## Materials used

- [[entities/materials/copper|Copper]] (coils, heat-transfer)
- LiPo / Lithium-ion / LiFePO4 battery chemistries
- 18650 cell format

## Projects

- [[entities/projects/scuttle-robot|Scuttle]] — the lab is the same lab Scuttle is developed in.
- [[entities/projects/open-lab-project|Open Lab Project]] — qr.net/openlabproject; companion PDF on actuators lives in the openLab GitHub repo.

## People mentioned

- [[entities/people/david-malawey|David Malawey]]

## Related concepts

- [[concepts/actuator-taxonomy|Actuator taxonomy]] — motion / fluid / pressure / force / energy / heat as the lab's organizing axes.
- [[concepts/battery-chemistry-tradeoffs|Battery chemistry tradeoffs]] — Li-ion vs. LiPo vs. LiFePO4.
- [[concepts/loop-vs-routine|Loop vs. routine]] — referenced when distinguishing functional actuators from accessories.

## Notable timestamps

- 0:00 Overview - actuators
- 2:00 Linear motion
- 7:20 Rotating motion
- 17:30 Oscillating motion
- 23:00 Air flow
- 28:50 Liquid flow
- 35:15 Generate pressure
- 38:30 Store pressure
- 40:30 Control pressure
- 45:00 Direct force
- 52:30 Store energy
- 57:30 Electrochemical energy
- 1:01:03 Move heat
- 1:09:30 Generate heat
