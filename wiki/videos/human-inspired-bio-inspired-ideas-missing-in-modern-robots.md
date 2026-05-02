---
type: video
title: "Human-inspired / Bio-inspired Ideas MISSING in Modern Robots"
video_id: "5sXRnYCKep4"
url: "https://www.youtube.com/watch?v=5sXRnYCKep4"
published: 2023-06-16
duration: "12:15"
tags: [robotics, biomechanics, dynamics, ai, parametric-design, openarm]
ingested: 2026-05-02
---

## Overview

An unrehearsed thought-dump from David proposing six human-motion principles that modern robot arms ignore — and why AI plus parametric CAD make this the moment to fix it. He pitches an open-source, hackable robot arm and gestures at sketches (counterbalanced SCARA, slip-ring designs) he plans to refine. The framing is foundational for [[entities/projects/openarm|OpenArm]] and the broader open-robotics thesis.

## Key takeaways

- **Move small masses before large.** Finger before wrist before elbow before shoulder before torso. Robots invert this and pay for it with high-torque base motors.
- **Counterbalance instead of inducing reaction forces at the base.** Reaching with the right arm, the human retracts the left shoulder rather than driving torque through the feet.
- **Maintain center of gravity to generate high accelerations.** Flick a finger, the arm's CG barely shifts.
- **Pre-load reaction forces only when high force is anticipated.** A martial-arts jab loads through feet and torso; idle reaching does not.
- **Conserve angular momentum across joints** by counter-rotating segments instead of overpowering them.
- **Skip rigidity and fine joint measurement at the base.** Computer vision + AI can reduce the robot to "measure the finger and the flower" — kinematics from the wrist forward, not from the toenail up.
- All of this only becomes practical if the robot is published as a [[concepts/parametric-design|parametric design]] so others can iterate.

## Techniques demonstrated

- [[concepts/dynamics-vs-static-motion|Dynamics-vs-static motion]] thinking — biomechanics as a lens on actuator selection.
- [[concepts/parametric-design|Parametric design]] for slip-rings and SCARA variants.
- [[concepts/sensor-actuator-controller-loop|Sensor-actuator-controller loop]] redesigned around vision instead of joint encoders.
- Model-predictive control localized to the end-effector frame.
- Counterbalanced SCARA configuration to hold position without continuous motor torque.

## Tools used

- Pencil-and-paper engineering sketches (to be scanned and posted).
- Conceptual references to [[entities/tools/ball-bearings|ball bearings]] and 3D-printed slip rings.

## Materials used

None physically demonstrated; this is a whiteboard/discussion video.

## Projects

- [[entities/projects/openarm|OpenArm]] — the hackable, open-source robot arm David is proposing here.
- Counterbalanced SCARA concept — sketched, not yet built.
- Custom parametric slip-ring concept — referenced as a 10-year-old idea finally feasible with 3D printing.

## People mentioned

- [[entities/people/david-malawey|David Malawey]] — narrator; references his 2011 ME bachelor's at [[entities/brands/texas-am|Texas A&M]].
- Newton — invoked to point out that infants learn motion without computing dynamics.

## Notable quotes / timestamps

- 0:00 "Robots fail to implement human dynamics."
- 1:25 "We never move a large mass if we can move a small mass."
- 5:33 "We DON'T require rigidity or fine measurement."
- 6:14 "If I can measure the finger and the flower, nothing else needs to be measured."
- 10:13 "Nobody taught you how to throw a baseball by using math — first you learned through feel."
- 11:22 "All of these sketches are trying to orient us towards something that is a parametric design."

## Related videos

- [[videos/what-is-a-robot-engineer-explains]]
- [[videos/this-is-why-you-cant-find-a-robotics-job-in-the-usa]]
- [[videos/how-real-experts-change-the-world-using-robotics]]
- [[videos/what-gpt5-is-doing-to-open-robotics-design-better-than-i-imagined]]
- [[videos/a-multidisciplinary-engineering-lab-tour-all-types-of-actuators]]
