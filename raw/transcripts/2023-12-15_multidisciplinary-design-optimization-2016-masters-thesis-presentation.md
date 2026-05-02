---
title: "Multidisciplinary Design Optimization - 2016 Masters Thesis Presentation"
url: "https://www.youtube.com/watch?v=XbSdwpLa4j4"
video_id: "XbSdwpLa4j4"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2023-12-15
duration: "30:01"
duration_sec: 1801
views: 514
likes: 8
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/XbSdwpLa4j4/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1426
chapters_count: 16
has_description: true
has_comments: false
---

## Description

My 2016 thesis defense for master of science in mechanical engineering.  

Download Thesis Content Here: https://qr.net/openmeproject
► see masters ► thesis 
Software Repository here: https://github.com/dmalawey/mdo

My research project involved Multidisciplinary Design Optimization (MDO) focused on a design of a cubesat (small satellite).

As I post this video today (december 2023) I am very pleased because this concept can be directly applied to any engineering design, such as robots.  For highly integrated systems, it is nearly impossible to reach an optimal design of modules without a special strategy, because the interactions of each module cause trade-offs inevitably.  A bigger engine makes a heavier car. 

Using MDO gives the design team a special power to adjust their design's parameters to reach a system that best performs for their intended requirements.  Furthermore, the design can be adjusted for unlimited variations that suit new applications.  

Since it is hard to explain MDO to new folks, I wanted to post this as an example which answers the questions: 
1) what is MDO?
2) why is it useful?
3) how can we use MDO in a project for enhanced results?

Chapters:
0:00 Gathering
4:30 Background
6:22 Objectives
7:40 Optimization Formula
10:40 Design Diagram
12:30 Heuristic + Gradient Methods
14:00 Sensitivity Analysis
15:10 Pareto Front
17:20 Mechanical Prototype
19:10 Beams - Gradient method
20:40 FEA (static, dynamic)
22:50 Prototyping Time Reduction
24:00 Fitment into Launcher
25:50 Conclusions
26:30 Future Work
28:30 Questions & Elaborating

## Chapters

- 0:00 Gathering
- 4:30 Background
- 6:22 Objectives
- 7:40 Optimization Formula
- 10:40 Design Diagram
- 12:30 Heuristic + Gradient Methods
- 14:00 Sensitivity Analysis
- 15:10 Pareto Front
- 17:20 Mechanical Prototype
- 19:10 Beams - Gradient method
- 20:40 FEA (static, dynamic)
- 22:50 Prototyping Time Reduction
- 24:00 Fitment into Launcher
- 25:50 Conclusions
- 26:30 Future Work
- 28:30 Questions & Elaborating

## Transcript

[0:02] All right,
[0:02] All right, we are spending money
[0:06] we are spending money
[0:06] we are spending money on the workshop.
[0:08] on the workshop.
[0:08] on the workshop. So you can get me
[0:10] So you can get me
[0:10] So you can get me so sit where you can read size 16 font.
[0:14] so sit where you can read size 16 font.
[0:14] so sit where you can read size 16 font. Yeah, let me turn the light off.
[0:21] I almost was able to go to 18. You will
[0:21] I almost was able to go to 18. You will manage with this or
[0:23] manage with this or
[0:23] manage with this or if the lights off then too much. Let me
[0:25] if the lights off then too much. Let me
[0:25] if the lights off then too much. Let me go to the white slide. You tell me if
[0:26] go to the white slide. You tell me if
[0:26] go to the white slide. You tell me if it's if it's clear enough for you guys.
[0:30] it's if it's clear enough for you guys.
[0:30] it's if it's clear enough for you guys. Well I mean with the light on it
[0:33] Well I mean with the light on it
[0:33] Well I mean with the light on it actually with the light off wait a
[0:34] actually with the light off wait a
[0:34] actually with the light off wait a minute. Wait a minute. There's a secret
[0:36] minute. Wait a minute. There's a secret
[0:36] minute. Wait a minute. There's a secret set of lights here
[0:50] I would not divulge that secret for
[0:50] I would not divulge that secret for anybody else.
[1:03] So
[1:03] So if you
[1:04] if you
[1:04] if you had a chance to get your water and
[1:06] had a chance to get your water and
[1:06] had a chance to get your water and whatnot
[1:07] whatnot
[1:07] whatnot started as soon as Dr. Morgan's
[1:09] started as soon as Dr. Morgan's
[1:09] started as soon as Dr. Morgan's all set. Got his cookie.
[1:16] Okay, good afternoon. Thanks everybody
[1:16] Okay, good afternoon. Thanks everybody for being here and I'll get started
[1:19] for being here and I'll get started
[1:19] for being here and I'll get started right away talking about the mechanical
[1:20] right away talking about the mechanical
[1:20] right away talking about the mechanical design and optimization of a
[1:22] design and optimization of a
[1:22] design and optimization of a standardized CubeSat for my thesis
[1:24] standardized CubeSat for my thesis
[1:24] standardized CubeSat for my thesis defense.
[1:27] defense.
[1:27] defense. So
[1:28] So
[1:28] So let's outline what I'd like to talk
[1:29] let's outline what I'd like to talk
[1:29] let's outline what I'd like to talk about right now and I'll start with
[1:31] about right now and I'll start with
[1:31] about right now and I'll start with background and research objectives. I'll
[1:33] background and research objectives. I'll
[1:33] background and research objectives. I'll go to the multi-disciplinary
[1:35] go to the multi-disciplinary
[1:35] go to the multi-disciplinary optimization problem that I created and
[1:38] optimization problem that I created and
[1:38] optimization problem that I created and sensitivity analysis on a Pareto front.
[1:41] sensitivity analysis on a Pareto front.
[1:41] sensitivity analysis on a Pareto front. I'll go into the mechanical design and
[1:43] I'll go into the mechanical design and
[1:43] I'll go into the mechanical design and the prototyping process
[1:45] the prototyping process
[1:45] the prototyping process covering the design for
[1:46] covering the design for
[1:46] covering the design for manufacturability, finite element
[1:48] manufacturability, finite element
[1:48] manufacturability, finite element analysis
[1:49] analysis
[1:49] analysis and then move on to results, lessons and
[1:51] and then move on to results, lessons and
[1:51] and then move on to results, lessons and suggestions for future work
[1:54] suggestions for future work
[1:54] suggestions for future work including the machining results,
[1:56] including the machining results,
[1:56] including the machining results, the MDO results and my overall
[1:58] the MDO results and my overall
[1:59] the MDO results and my overall contributions. And then we'll have some
[2:01] contributions. And then we'll have some
[2:01] contributions. And then we'll have some time for questions and extras if you
[2:03] time for questions and extras if you
[2:03] time for questions and extras if you like to explore that.
[2:06] like to explore that.
[2:06] like to explore that. So I provided this table here just so we
[2:08] So I provided this table here just so we
[2:08] So I provided this table here just so we can
[2:10] can
[2:10] can cover some of the terms that are
[2:12] cover some of the terms that are
[2:12] cover some of the terms that are abbreviated in the slides. Power,
[2:15] abbreviated in the slides. Power,
[2:15] abbreviated in the slides. Power, batteries, solar panels are all
[2:16] batteries, solar panels are all
[2:16] batteries, solar panels are all abbreviated. X of N refers to design
[2:19] abbreviated. X of N refers to design
[2:19] abbreviated. X of N refers to design variables where X is the design vector
[2:22] variables where X is the design vector
[2:22] variables where X is the design vector and X star is the optimal design.
[2:26] and X star is the optimal design.
[2:26] and X star is the optimal design. P sub N refers to parameters that are
[2:28] P sub N refers to parameters that are
[2:28] P sub N refers to parameters that are put into the MDO problem. And G of X and
[2:31] put into the MDO problem. And G of X and
[2:31] put into the MDO problem. And G of X and P, J of X and P are the constraint
[2:33] P, J of X and P are the constraint
[2:33] P, J of X and P are the constraint function and objective functions
[2:36] function and objective functions
[2:36] function and objective functions and they're functions of the design
[2:37] and they're functions of the design
[2:37] and they're functions of the design variables and the parameters.
[2:40] variables and the parameters.
[2:40] variables and the parameters. A little background on MDO for CubeSats
[2:44] A little background on MDO for CubeSats
[2:44] A little background on MDO for CubeSats CubeSats specifically.
[2:46] CubeSats specifically.
[2:46] CubeSats specifically. There's a small number of papers you can
[2:48] There's a small number of papers you can
[2:48] There's a small number of papers you can actually find on this combination of
[2:50] actually find on this combination of
[2:50] actually find on this combination of topics.
[2:51] topics.
[2:51] topics. They include and rather extensive study
[2:54] They include and rather extensive study
[2:54] They include and rather extensive study by University of Michigan folks on
[2:57] by University of Michigan folks on
[2:57] by University of Michigan folks on maximizing the power generated and the
[2:59] maximizing the power generated and the
[2:59] maximizing the power generated and the data transmitted to Earth by a 3U
[3:01] data transmitted to Earth by a 3U
[3:01] data transmitted to Earth by a 3U CubeSat and they're taking an existing
[3:04] CubeSat and they're taking an existing
[3:04] CubeSat and they're taking an existing satellite design and and optimizing the
[3:06] satellite design and and optimizing the
[3:06] satellite design and and optimizing the configuration to achieve those goals.
[3:09] configuration to achieve those goals.
[3:09] configuration to achieve those goals. And for an uncertainty based MDO there's
[3:12] And for an uncertainty based MDO there's
[3:12] And for an uncertainty based MDO there's one that is maximizing capability for a
[3:15] one that is maximizing capability for a
[3:15] one that is maximizing capability for a lunar mission specifically and once
[3:17] lunar mission specifically and once
[3:17] lunar mission specifically and once again it's using an existing
[3:20] again it's using an existing
[3:20] again it's using an existing payload and the propulsion system is
[3:22] payload and the propulsion system is
[3:22] payload and the propulsion system is already decided on for this
[3:24] already decided on for this
[3:24] already decided on for this optimization.
[3:26] optimization.
[3:26] optimization. There's one covering the feasibility of
[3:29] There's one covering the feasibility of
[3:29] There's one covering the feasibility of a novel thruster design
[3:31] a novel thruster design
[3:31] a novel thruster design and it's optimizing
[3:33] and it's optimizing
[3:33] and it's optimizing efficiency of delta V maneuvers and
[3:36] efficiency of delta V maneuvers and
[3:36] efficiency of delta V maneuvers and actually changing the trajectory of a
[3:38] actually changing the trajectory of a
[3:38] actually changing the trajectory of a satellite
[3:40] satellite
[3:40] satellite to alter its orbit and things like that.
[3:43] to alter its orbit and things like that.
[3:43] to alter its orbit and things like that. And then my study is going into
[3:46] And then my study is going into
[3:46] And then my study is going into optimizing cost effectiveness of the
[3:47] optimizing cost effectiveness of the
[3:47] optimizing cost effectiveness of the satellite and
[3:49] satellite and
[3:49] satellite and relieving
[3:52] relieving
[3:52] relieving open variability for different types of
[3:54] open variability for different types of
[3:54] open variability for different types of missions not going off of one type of
[3:57] missions not going off of one type of
[3:57] missions not going off of one type of design existing. Also
[4:00] design existing. Also
[4:01] design existing. Also I'd like to note that I wanted to take a
[4:03] I'd like to note that I wanted to take a
[4:03] I'd like to note that I wanted to take a systems approach instead of just
[4:05] systems approach instead of just
[4:05] systems approach instead of just covering mechanical simulations because
[4:10] covering mechanical simulations because
[4:10] covering mechanical simulations because this this figure kind of sums up what I
[4:11] this this figure kind of sums up what I
[4:11] this this figure kind of sums up what I found when I was reading background.
[4:14] found when I was reading background.
[4:14] found when I was reading background. It comes from a study called the first
[4:16] It comes from a study called the first
[4:16] It comes from a study called the first 100 CubeSats and it's showing that 8% of
[4:20] 100 CubeSats and it's showing that 8% of
[4:20] 100 CubeSats and it's showing that 8% of the failed CubeSat missions are due to
[4:22] the failed CubeSat missions are due to
[4:22] the failed CubeSat missions are due to mechanical failure. So I don't want to
[4:24] mechanical failure. So I don't want to
[4:24] mechanical failure. So I don't want to dwell too much on
[4:26] dwell too much on
[4:26] dwell too much on extensive mechanical simulations.
[4:30] extensive mechanical simulations.
[4:30] extensive mechanical simulations. Okay, background on CubeSat prototypes.
[4:34] Okay, background on CubeSat prototypes.
[4:34] Okay, background on CubeSat prototypes. First I'd like to cover what's shown in
[4:36] First I'd like to cover what's shown in
[4:36] First I'd like to cover what's shown in figure one here
[4:37] figure one here
[4:37] figure one here and it's that we have an envelope of 119
[4:40] and it's that we have an envelope of 119
[4:40] and it's that we have an envelope of 119 mm of width and most existing satellites
[4:44] mm of width and most existing satellites
[4:44] mm of width and most existing satellites do not take this full envelope. They're
[4:46] do not take this full envelope. They're
[4:46] do not take this full envelope. They're only limiting themselves to 100 mm. So I
[4:48] only limiting themselves to 100 mm. So I
[4:48] only limiting themselves to 100 mm. So I wanted to be able to take advantage of
[4:50] wanted to be able to take advantage of
[4:50] wanted to be able to take advantage of that.
[4:51] that.
[4:51] that. Then we have different styles that I
[4:52] Then we have different styles that I
[4:52] Then we have different styles that I came across. Image two comes from
[4:55] came across. Image two comes from
[4:55] came across. Image two comes from cubesatkit.com and this is a flight
[4:57] cubesatkit.com and this is a flight
[4:58] cubesatkit.com and this is a flight proven unit and it's made from sheet
[5:00] proven unit and it's made from sheet
[5:00] proven unit and it's made from sheet metal
[5:01] metal
[5:01] metal which is something I want to stay away
[5:03] which is something I want to stay away
[5:03] which is something I want to stay away from because of the
[5:05] from because of the
[5:05] from because of the large investment cost to make a one-off
[5:08] large investment cost to make a one-off
[5:08] large investment cost to make a one-off prototype using sheet metal and meet
[5:10] prototype using sheet metal and meet
[5:10] prototype using sheet metal and meet tolerances.
[5:12] tolerances.
[5:12] tolerances. This would be rather expensive.
[5:15] This would be rather expensive.
[5:15] This would be rather expensive. We have a prototype from ISIS
[5:18] We have a prototype from ISIS
[5:18] We have a prototype from ISIS and I downloaded this CAD model and it
[5:20] and I downloaded this CAD model and it
[5:20] and I downloaded this CAD model and it turned out to be one of my favorite
[5:21] turned out to be one of my favorite
[5:21] turned out to be one of my favorite benchmarks but it does have some
[5:23] benchmarks but it does have some
[5:23] benchmarks but it does have some intricate machining which ends it to
[5:26] intricate machining which ends it to
[5:26] intricate machining which ends it to causes it to be rather expensive.
[5:28] causes it to be rather expensive.
[5:29] causes it to be rather expensive. Figure five shows that this this CAD
[5:32] Figure five shows that this this CAD
[5:32] Figure five shows that this this CAD model was shared with me by Nanoracks
[5:34] model was shared with me by Nanoracks
[5:34] model was shared with me by Nanoracks with an unknown designer and it does
[5:36] with an unknown designer and it does
[5:36] with an unknown designer and it does take up the full envelope available but
[5:39] take up the full envelope available but
[5:39] take up the full envelope available but it's not accounting for manufacturing
[5:40] it's not accounting for manufacturing
[5:40] it's not accounting for manufacturing whatsoever once you once you open up the
[5:42] whatsoever once you once you open up the
[5:42] whatsoever once you once you open up the CAD design and find the the radii and
[5:45] CAD design and find the the radii and
[5:45] CAD design and find the the radii and whatnot.
[5:46] whatnot.
[5:46] whatnot. So what what happens?
[5:50] So what what happens?
[5:50] So what what happens? When you said it doesn't account for
[5:53] When you said it doesn't account for
[5:53] When you said it doesn't account for so this model as shown could not be
[5:57] so this model as shown could not be
[5:57] so this model as shown could not be manufactured
[6:00] manufactured
[6:00] manufactured at all because
[6:02] at all because
[6:02] at all because if you extruded it or if you
[6:04] if you extruded it or if you
[6:04] if you extruded it or if you cut it or some combination you couldn't
[6:06] cut it or some combination you couldn't
[6:06] cut it or some combination you couldn't achieve all the all of the corners shown
[6:09] achieve all the all of the corners shown
[6:09] achieve all the all of the corners shown in here
[6:10] in here
[6:10] in here internally and
[6:11] internally and
[6:12] internally and some features you could find a way to do
[6:13] some features you could find a way to do
[6:13] some features you could find a way to do it but
[6:15] it but
[6:15] it but overall it's not a good design.
[6:23] So
[6:23] So the objectives of my research are to
[6:25] the objectives of my research are to
[6:25] the objectives of my research are to maximize mission effectiveness and
[6:27] maximize mission effectiveness and
[6:27] maximize mission effectiveness and minimize the mass of the critical
[6:29] minimize the mass of the critical
[6:29] minimize the mass of the critical functions. So I'm treating the CubeSat
[6:31] functions. So I'm treating the CubeSat
[6:31] functions. So I'm treating the CubeSat like a vehicle
[6:32] like a vehicle
[6:32] like a vehicle pickup truck that needs to carry a
[6:34] pickup truck that needs to carry a
[6:34] pickup truck that needs to carry a payload and I want to minimize the mass
[6:37] payload and I want to minimize the mass
[6:37] payload and I want to minimize the mass the resources taken by those critical
[6:39] the resources taken by those critical
[6:39] the resources taken by those critical functions leaving the most remaining
[6:41] functions leaving the most remaining
[6:41] functions leaving the most remaining resources for the payload so it can do
[6:43] resources for the payload so it can do
[6:43] resources for the payload so it can do its job.
[6:44] its job.
[6:45] its job. I want to optimize for cost
[6:46] I want to optimize for cost
[6:46] I want to optimize for cost effectiveness so include commercial
[6:48] effectiveness so include commercial
[6:48] effectiveness so include commercial off-the-shelf components where we have
[6:51] off-the-shelf components where we have
[6:51] off-the-shelf components where we have known information on the data sheets and
[6:54] known information on the data sheets and
[6:54] known information on the data sheets and known costs and as much of that
[6:56] known costs and as much of that
[6:56] known costs and as much of that information as possible.
[6:58] information as possible.
[6:58] information as possible. Maintain flexibility to re-optimize for
[7:00] Maintain flexibility to re-optimize for
[7:00] Maintain flexibility to re-optimize for different missions
[7:03] different missions
[7:03] different missions and take advantage of continuously
[7:04] and take advantage of continuously
[7:04] and take advantage of continuously growing data that's available.
[7:07] growing data that's available.
[7:07] growing data that's available. So here in this image I have a 2U
[7:12] So here in this image I have a 2U
[7:12] So here in this image I have a 2U configuration of my design and the
[7:15] configuration of my design and the
[7:15] configuration of my design and the optimizer is able to design if we allow
[7:19] optimizer is able to design if we allow
[7:19] optimizer is able to design if we allow it
[7:20] it
[7:20] it a larger satellite with this
[7:22] a larger satellite with this
[7:22] a larger satellite with this configuration
[7:23] configuration
[7:23] configuration and I want to make a prototype that's
[7:26] and I want to make a prototype that's
[7:26] and I want to make a prototype that's fed by the optimizer and is designed for
[7:28] fed by the optimizer and is designed for
[7:28] fed by the optimizer and is designed for manufacturability. So
[7:31] manufacturability. So
[7:31] manufacturability. So the output of my research is something
[7:33] the output of my research is something
[7:33] the output of my research is something that does not need to be need to be
[7:35] that does not need to be need to be
[7:35] that does not need to be need to be redesigned in order to actually be made.
[7:43] So I'll cover the multi-disciplinary
[7:43] So I'll cover the multi-disciplinary optimization but I think most of you
[7:44] optimization but I think most of you
[7:44] optimization but I think most of you have seen it once or twice already.
[7:47] have seen it once or twice already.
[7:47] have seen it once or twice already. I have a design vector including six
[7:49] I have a design vector including six
[7:49] I have a design vector including six design variables three of which are
[7:51] design variables three of which are
[7:51] design variables three of which are considered fully discrete and three of
[7:54] considered fully discrete and three of
[7:54] considered fully discrete and three of which are considered
[7:56] which are considered
[7:56] which are considered for my purpose they're allowed to be
[7:58] for my purpose they're allowed to be
[7:58] for my purpose they're allowed to be continuous.
[8:00] continuous.
[8:00] continuous. And the objective function is to
[8:02] And the objective function is to
[8:02] And the objective function is to minimize the mass
[8:03] minimize the mass
[8:03] minimize the mass and then secondarily an objective
[8:05] and then secondarily an objective
[8:05] and then secondarily an objective function of minimizing cost is
[8:07] function of minimizing cost is
[8:07] function of minimizing cost is introduced
[8:09] introduced
[8:09] introduced to gather a trade-off.
[8:11] to gather a trade-off.
[8:11] to gather a trade-off. Then there are three major constraints.
[8:13] Then there are three major constraints.
[8:13] Then there are three major constraints. The first one is power must be met power
[8:16] The first one is power must be met power
[8:16] The first one is power must be met power demand must be met by the solar panels
[8:17] demand must be met by the solar panels
[8:17] demand must be met by the solar panels and the batteries in combination. The
[8:19] and the batteries in combination. The
[8:20] and the batteries in combination. The structure bending stiffness must meet
[8:22] structure bending stiffness must meet
[8:22] structure bending stiffness must meet must be sufficient and that's based off
[8:25] must be sufficient and that's based off
[8:25] must be sufficient and that's based off of a benchmark and the propellant is
[8:27] of a benchmark and the propellant is
[8:27] of a benchmark and the propellant is sufficient to achieve the delta V we
[8:29] sufficient to achieve the delta V we
[8:29] sufficient to achieve the delta V we need which
[8:32] need which
[8:32] need which we're not going to actually change our
[8:33] we're not going to actually change our
[8:34] we're not going to actually change our trajectory. We're using delta V as a
[8:35] trajectory. We're using delta V as a
[8:35] trajectory. We're using delta V as a measure of attitude control force.
[8:39] measure of attitude control force.
[8:40] measure of attitude control force. So an example of the constraint is this
[8:42] So an example of the constraint is this
[8:42] So an example of the constraint is this power constraint shown in this equation
[8:45] power constraint shown in this equation
[8:45] power constraint shown in this equation which is basically saying we're summing
[8:47] which is basically saying we're summing
[8:47] which is basically saying we're summing up all the currents of all the
[8:49] up all the currents of all the
[8:49] up all the currents of all the components that are drawing power
[8:51] components that are drawing power
[8:52] components that are drawing power finding their power, their duty cycle
[8:53] finding their power, their duty cycle
[8:53] finding their power, their duty cycle and multiplying that by the length of
[8:55] and multiplying that by the length of
[8:55] and multiplying that by the length of the mission in days.
[8:57] the mission in days.
[8:57] the mission in days. And then we're saying that that needs to
[8:59] And then we're saying that that needs to
[8:59] And then we're saying that that needs to be less than or equal to
[9:01] be less than or equal to
[9:01] be less than or equal to the power that's generated by our our
[9:04] the power that's generated by our our
[9:04] the power that's generated by our our power sources.
[9:05] power sources.
[9:06] power sources. So if you compare your design
[9:07] So if you compare your design
[9:07] So if you compare your design objectives, right? And constraints with
[9:11] objectives, right? And constraints with
[9:11] objectives, right? And constraints with the prior work that you mentioned
[9:14] the prior work that you mentioned
[9:14] the prior work that you mentioned work at the University of Michigan,
[9:15] work at the University of Michigan,
[9:15] work at the University of Michigan, right?
[9:17] right?
[9:17] right? Do you compare with what their
[9:18] Do you compare with what their
[9:18] Do you compare with what their objectives were versus what you were
[9:21] objectives were versus what you were
[9:21] objectives were versus what you were using as objectives?
[9:23] using as objectives?
[9:23] using as objectives? Yeah, so they're they're strongly
[9:26] Yeah, so they're they're strongly
[9:27] Yeah, so they're they're strongly oriented towards
[9:29] oriented towards
[9:29] oriented towards capturing the most sun
[9:31] capturing the most sun
[9:31] capturing the most sun using their solar panels and so their
[9:35] using their solar panels and so their
[9:35] using their solar panels and so their objective was maximize the power,
[9:38] objective was maximize the power,
[9:38] objective was maximize the power, maximize the um
[9:42] maximize the um
[9:42] maximize the um the transmitted data
[9:44] the transmitted data
[9:44] the transmitted data and so they're dealing with
[9:46] and so they're dealing with
[9:46] and so they're dealing with timing
[9:47] timing
[9:48] timing and
[9:49] and
[9:49] and and they also take the impacts of their
[9:52] and they also take the impacts of their
[9:52] and they also take the impacts of their angles of their solar panel
[9:54] angles of their solar panel
[9:54] angles of their solar panel configuration that impacts their flight
[9:56] configuration that impacts their flight
[9:57] configuration that impacts their flight as well.
[9:58] as well.
[9:58] as well. So, their
[10:00] So, their
[10:00] So, their objective is maximizing this stuff. My
[10:02] objective is maximizing this stuff. My
[10:02] objective is maximizing this stuff. My objective is to minimize cost, but my
[10:05] objective is to minimize cost, but my
[10:05] objective is to minimize cost, but my constraint is to meet the power demand.
[10:08] constraint is to meet the power demand.
[10:08] constraint is to meet the power demand. So, their their objective is kind of
[10:11] So, their their objective is kind of
[10:11] So, their their objective is kind of like my constraint.
[10:19] Um and I pulled power demand uh
[10:19] Um and I pulled power demand uh examples from other CubeSat Whenever I
[10:21] examples from other CubeSat Whenever I
[10:21] examples from other CubeSat Whenever I found out well, how much power is taken
[10:23] found out well, how much power is taken
[10:23] found out well, how much power is taken by a attitude determination system, then
[10:26] by a attitude determination system, then
[10:26] by a attitude determination system, then that's what I used as my estimated power
[10:28] that's what I used as my estimated power
[10:28] that's what I used as my estimated power demand. Um and those kind of things.
[10:37] So, this is my N-squared diagram.
[10:37] So, this is my N-squared diagram. It's showing the flow of all the modules
[10:39] It's showing the flow of all the modules
[10:39] It's showing the flow of all the modules that are computing the objective
[10:40] that are computing the objective
[10:41] that are computing the objective function. We start with an
[10:43] function. We start with an
[10:43] function. We start with an uh the design vector.
[10:44] uh the design vector.
[10:44] uh the design vector. And then it feeds information about um
[10:47] And then it feeds information about um
[10:47] And then it feeds information about um the design uh
[10:49] the design uh
[10:49] the design uh the design variables and the parameters
[10:53] the design variables and the parameters
[10:53] the design variables and the parameters into all other modules. And it's been
[10:55] into all other modules. And it's been
[10:55] into all other modules. And it's been adjusted to make minimal feedback loops,
[10:58] adjusted to make minimal feedback loops,
[10:58] adjusted to make minimal feedback loops, but there's one feedback loop, and
[11:00] but there's one feedback loop, and
[11:00] but there's one feedback loop, and that's where
[11:01] that's where
[11:01] that's where the propulsion module takes the chosen
[11:03] the propulsion module takes the chosen
[11:03] the propulsion module takes the chosen thruster and decides how much power is
[11:05] thruster and decides how much power is
[11:05] thruster and decides how much power is going to be take used by that thruster.
[11:09] going to be take used by that thruster.
[11:09] going to be take used by that thruster. Um
[11:09] Um
[11:09] Um and then it feeds that into the battery
[11:11] and then it feeds that into the battery
[11:11] and then it feeds that into the battery and power module,
[11:13] and power module,
[11:13] and power module, which is um going to accommodate the
[11:16] which is um going to accommodate the
[11:16] which is um going to accommodate the uh solar panels and batteries to meet
[11:18] uh solar panels and batteries to meet
[11:18] uh solar panels and batteries to meet that. And then finally, you have a mass
[11:21] that. And then finally, you have a mass
[11:21] that. And then finally, you have a mass of all that equipment, and that mass
[11:23] of all that equipment, and that mass
[11:23] of all that equipment, and that mass gets updated and goes back to propulsion
[11:25] gets updated and goes back to propulsion
[11:25] gets updated and goes back to propulsion so that our delta V can be met. Um and
[11:27] so that our delta V can be met. Um and
[11:27] so that our delta V can be met. Um and the propulsion might adjust the amount
[11:30] the propulsion might adjust the amount
[11:30] the propulsion might adjust the amount of um
[11:31] of um
[11:31] of um propellant to still achieve the delta V
[11:34] propellant to still achieve the delta V
[11:34] propellant to still achieve the delta V with a new mass of satellite.
[11:36] with a new mass of satellite.
[11:36] with a new mass of satellite. And after after mass is calculated, then
[11:39] And after after mass is calculated, then
[11:39] And after after mass is calculated, then uh the cost is somewhat decoupled, and
[11:41] uh the cost is somewhat decoupled, and
[11:41] uh the cost is somewhat decoupled, and it's all um calculated at the end.
[11:48] So,
[11:48] So, for my optimization approach, I created
[11:52] for my optimization approach, I created
[11:52] for my optimization approach, I created a two-stage approach. And that means uh
[11:55] a two-stage approach. And that means uh
[11:55] a two-stage approach. And that means uh I'm using the genetic algorithm, which
[11:57] I'm using the genetic algorithm, which
[11:57] I'm using the genetic algorithm, which is a heuristic method, to calculate the
[11:59] is a heuristic method, to calculate the
[11:59] is a heuristic method, to calculate the first three variables. Now, actually, it
[12:02] first three variables. Now, actually, it
[12:02] first three variables. Now, actually, it calculates all six variables, and it's
[12:03] calculates all six variables, and it's
[12:04] calculates all six variables, and it's just doing its best to minimize uh the
[12:06] just doing its best to minimize uh the
[12:06] just doing its best to minimize uh the objective function.
[12:07] objective function.
[12:07] objective function. And then we take the result of the GA,
[12:10] And then we take the result of the GA,
[12:10] And then we take the result of the GA, and then we feed the first three
[12:12] and then we feed the first three
[12:12] and then we feed the first three variables, which are discrete, into the
[12:15] variables, which are discrete, into the
[12:15] variables, which are discrete, into the gradient function.
[12:16] gradient function.
[12:16] gradient function. And we uh treat those as fixed
[12:19] And we uh treat those as fixed
[12:19] And we uh treat those as fixed parameters. And then we allow the SQP to
[12:22] parameters. And then we allow the SQP to
[12:22] parameters. And then we allow the SQP to do work and maximize the efficiency of
[12:24] do work and maximize the efficiency of
[12:24] do work and maximize the efficiency of the last three variables, which are
[12:27] the last three variables, which are
[12:27] the last three variables, which are number of solar panels, number of
[12:28] number of solar panels, number of
[12:28] number of solar panels, number of batteries, and um structure rail width,
[12:31] batteries, and um structure rail width,
[12:31] batteries, and um structure rail width, treating those as continuous. Um and
[12:34] treating those as continuous. Um and
[12:34] treating those as continuous. Um and this can guarantee that we have a local
[12:37] this can guarantee that we have a local
[12:37] this can guarantee that we have a local um minimum because the gradient is going
[12:39] um minimum because the gradient is going
[12:40] um minimum because the gradient is going to be zero.
[12:41] to be zero.
[12:41] to be zero. So, in this example, the GA was able to
[12:45] So, in this example, the GA was able to
[12:45] So, in this example, the GA was able to form a design at 902 g, and then SQP was
[12:48] form a design at 902 g, and then SQP was
[12:48] form a design at 902 g, and then SQP was able to form a uh to reduce that to 886.
[12:53] able to form a uh to reduce that to 886.
[12:53] able to form a uh to reduce that to 886. And the overall process is fairly
[12:55] And the overall process is fairly
[12:55] And the overall process is fairly repeatable um at least
[12:57] repeatable um at least
[12:57] repeatable um at least one out of every two times that I run
[12:59] one out of every two times that I run
[12:59] one out of every two times that I run using the same uh parameters, it will
[13:02] using the same uh parameters, it will
[13:02] using the same uh parameters, it will give the same result.
[13:03] give the same result.
[13:03] give the same result. And oftentimes, you'll know if it if it
[13:06] And oftentimes, you'll know if it if it
[13:06] And oftentimes, you'll know if it if it got stuck and made a bad decision based
[13:08] got stuck and made a bad decision based
[13:08] got stuck and made a bad decision based on the genetic algorithm uh
[13:10] on the genetic algorithm uh
[13:10] on the genetic algorithm uh just
[13:11] just
[13:11] just ending up with a result that's at least
[13:13] ending up with a result that's at least
[13:13] ending up with a result that's at least 10% or 20% higher.
[13:17] 10% or 20% higher.
[13:17] 10% or 20% higher. Um this is describing our function of
[13:21] Um this is describing our function of
[13:21] Um this is describing our function of minimizing the objective function
[13:24] minimizing the objective function
[13:24] minimizing the objective function uh such that the constraints are less
[13:26] uh such that the constraints are less
[13:26] uh such that the constraints are less than or equal to zero, and the design
[13:28] than or equal to zero, and the design
[13:28] than or equal to zero, and the design variables fall in between the lower
[13:30] variables fall in between the lower
[13:30] variables fall in between the lower bounds and upper bounds.
[13:33] bounds and upper bounds.
[13:33] bounds and upper bounds. So, after finding an optimal design
[13:35] So, after finding an optimal design
[13:35] So, after finding an optimal design point, I need to check the sensitivity
[13:38] point, I need to check the sensitivity
[13:38] point, I need to check the sensitivity of the objective function to those
[13:40] of the objective function to those
[13:40] of the objective function to those variables. So,
[13:43] variables. So,
[13:43] variables. So, we look at mass sensitivity, and we find
[13:45] we look at mass sensitivity, and we find
[13:45] we look at mass sensitivity, and we find that uh out of the continuous variables,
[13:48] that uh out of the continuous variables,
[13:48] that uh out of the continuous variables, the mass is most sensitive to the
[13:50] the mass is most sensitive to the
[13:50] the mass is most sensitive to the structure rail uh the structure rail
[13:52] structure rail uh the structure rail
[13:52] structure rail uh the structure rail thickness. And to do a logic check here,
[13:55] thickness. And to do a logic check here,
[13:55] thickness. And to do a logic check here, we look at the overall CubeSat mass. We
[13:58] we look at the overall CubeSat mass. We
[13:58] we look at the overall CubeSat mass. We find that the um structure is taking up
[14:01] find that the um structure is taking up
[14:01] find that the um structure is taking up a mass that is equal to both the
[14:04] a mass that is equal to both the
[14:04] a mass that is equal to both the batteries and the panels combined, and
[14:07] batteries and the panels combined, and
[14:07] batteries and the panels combined, and so it should have a greater impact.
[14:09] so it should have a greater impact.
[14:09] so it should have a greater impact. And then when we look at cost
[14:10] And then when we look at cost
[14:11] And then when we look at cost sensitivity,
[14:12] sensitivity,
[14:12] sensitivity, we find that um the solar panels have
[14:15] we find that um the solar panels have
[14:15] we find that um the solar panels have the greatest impact.
[14:16] the greatest impact.
[14:16] the greatest impact. And once again, checking our overall um
[14:19] And once again, checking our overall um
[14:19] And once again, checking our overall um our overall cost comes
[14:22] our overall cost comes
[14:22] our overall cost comes majorly from the solar panels,
[14:24] majorly from the solar panels,
[14:24] majorly from the solar panels, and
[14:25] and
[14:25] and the cost of the solar panel is about
[14:27] the cost of the solar panel is about
[14:27] the cost of the solar panel is about $1,500
[14:28] $1,500
[14:28] $1,500 in this scenario.
[14:30] in this scenario.
[14:30] in this scenario. And the cost of the battery is only set
[14:32] And the cost of the battery is only set
[14:32] And the cost of the battery is only set to be $10.
[14:34] to be $10.
[14:34] to be $10. So, we should expect to see a greater
[14:37] So, we should expect to see a greater
[14:37] So, we should expect to see a greater impact from solar panels.
[14:39] impact from solar panels.
[14:39] impact from solar panels. Um
[14:40] Um
[14:40] Um I I also did a parameter sensitivity
[14:43] I I also did a parameter sensitivity
[14:43] I I also did a parameter sensitivity study where I adjusted parameters of the
[14:45] study where I adjusted parameters of the
[14:45] study where I adjusted parameters of the mission, such as the duration or the
[14:46] mission, such as the duration or the
[14:46] mission, such as the duration or the power that's able to be generated by one
[14:48] power that's able to be generated by one
[14:48] power that's able to be generated by one solar panel. Um and I can I can share
[14:52] solar panel. Um and I can I can share
[14:52] solar panel. Um and I can I can share that at the end if you'd like to to know
[14:54] that at the end if you'd like to to know
[14:54] that at the end if you'd like to to know that.
[14:58] So, uh
[14:58] So, uh we want to develop a Pareto front that
[15:00] we want to develop a Pareto front that
[15:00] we want to develop a Pareto front that shows us options for designs that have
[15:02] shows us options for designs that have
[15:02] shows us options for designs that have varying cost and varying mass, but all
[15:05] varying cost and varying mass, but all
[15:05] varying cost and varying mass, but all of which are optimal. And the Pareto
[15:07] of which are optimal. And the Pareto
[15:07] of which are optimal. And the Pareto front that I was able to generate from
[15:09] front that I was able to generate from
[15:09] front that I was able to generate from this two-stage system
[15:11] this two-stage system
[15:11] this two-stage system um is okay, but could be improved. Um
[15:16] um is okay, but could be improved. Um
[15:16] um is okay, but could be improved. Um The new objective function in order to
[15:19] The new objective function in order to
[15:19] The new objective function in order to create this front is right here. J star
[15:22] create this front is right here. J star
[15:22] create this front is right here. J star is a combination is a weighted sum of
[15:24] is a combination is a weighted sum of
[15:24] is a combination is a weighted sum of the cost and the mass, um taking lambda
[15:27] the cost and the mass, um taking lambda
[15:27] the cost and the mass, um taking lambda as lambda increments from zero to one
[15:31] as lambda increments from zero to one
[15:31] as lambda increments from zero to one and n number of iterations.
[15:33] and n number of iterations.
[15:33] and n number of iterations. And um we basically have
[15:36] And um we basically have
[15:36] And um we basically have um
[15:37] um
[15:37] um the results converge to these
[15:40] the results converge to these
[15:40] the results converge to these uh these data points give or take a few
[15:43] uh these data points give or take a few
[15:44] uh these data points give or take a few data points each each time that I
[15:46] data points each each time that I
[15:46] data points each each time that I that I run it. And you'll find that
[15:49] that I run it. And you'll find that
[15:49] that I run it. And you'll find that there may be uh a false Pareto point
[15:52] there may be uh a false Pareto point
[15:52] there may be uh a false Pareto point like this one here,
[15:53] like this one here,
[15:53] like this one here, um where it got stuck because the the
[15:57] um where it got stuck because the the
[15:57] um where it got stuck because the the heuristic optimizer chose a design that
[15:59] heuristic optimizer chose a design that
[15:59] heuristic optimizer chose a design that just wasn't in the right ballpark, and
[16:02] just wasn't in the right ballpark, and
[16:02] just wasn't in the right ballpark, and then the the gradient-based function
[16:04] then the the gradient-based function
[16:04] then the the gradient-based function still minimized locally, but it couldn't
[16:06] still minimized locally, but it couldn't
[16:06] still minimized locally, but it couldn't jump to the to the correct spot.
[16:09] jump to the to the correct spot.
[16:09] jump to the to the correct spot. So, what I did in this picture is try to
[16:12] So, what I did in this picture is try to
[16:12] So, what I did in this picture is try to capture um going from right to left,
[16:16] capture um going from right to left,
[16:16] capture um going from right to left, what is the major design change that was
[16:18] what is the major design change that was
[16:18] what is the major design change that was chosen, uh what major uh variable was
[16:22] chosen, uh what major uh variable was
[16:22] chosen, uh what major uh variable was changed that impacted it and caused it
[16:24] changed that impacted it and caused it
[16:24] changed that impacted it and caused it to move upwards. And so, that's what
[16:27] to move upwards. And so, that's what
[16:28] to move upwards. And so, that's what these comments are here.
[16:30] these comments are here.
[16:30] these comments are here. Um
[16:31] Um
[16:31] Um It is hard to capture all that
[16:33] It is hard to capture all that
[16:33] It is hard to capture all that information in in one graph, so I so I
[16:35] information in in one graph, so I so I
[16:35] information in in one graph, so I so I summarized it a lot. For example, um
[16:38] summarized it a lot. For example, um
[16:39] summarized it a lot. For example, um this point here is where the batteries
[16:41] this point here is where the batteries
[16:41] this point here is where the batteries had been moved from the lower bound to
[16:44] had been moved from the lower bound to
[16:44] had been moved from the lower bound to the upper bound. It means all of these
[16:47] the upper bound. It means all of these
[16:47] the upper bound. It means all of these designs had batteries at the lower
[16:48] designs had batteries at the lower
[16:48] designs had batteries at the lower bound.
[16:50] bound.
[16:50] bound. And then it finally decided that the
[16:52] And then it finally decided that the
[16:52] And then it finally decided that the tradeoff is worth it so that we take on
[16:54] tradeoff is worth it so that we take on
[16:54] tradeoff is worth it so that we take on a lot more mass of take using more
[16:56] a lot more mass of take using more
[16:56] a lot more mass of take using more batteries, um but reduce the cost of
[16:59] batteries, um but reduce the cost of
[16:59] batteries, um but reduce the cost of using the solar panels.
[17:07] So, next was um mechanical design and
[17:07] So, next was um mechanical design and prototyping. I began this process with
[17:09] prototyping. I began this process with
[17:09] prototyping. I began this process with the benchmark cuz I love benchmarks. And
[17:12] the benchmark cuz I love benchmarks. And
[17:12] the benchmark cuz I love benchmarks. And um I took this uh ISIS panel here,
[17:15] um I took this uh ISIS panel here,
[17:15] um I took this uh ISIS panel here, and the first thing I did was send it
[17:17] and the first thing I did was send it
[17:17] and the first thing I did was send it out for a machining quote to find out
[17:19] out for a machining quote to find out
[17:19] out for a machining quote to find out how long would this take to machine.
[17:21] how long would this take to machine.
[17:21] how long would this take to machine. Um
[17:22] Um
[17:22] Um and that came out to be 10 hours. And my
[17:25] and that came out to be 10 hours. And my
[17:25] and that came out to be 10 hours. And my goal here was to reduce the cost,
[17:27] goal here was to reduce the cost,
[17:27] goal here was to reduce the cost, maintain the function, and make a design
[17:29] maintain the function, and make a design
[17:29] maintain the function, and make a design that's fed by the optimizer. I'll talk
[17:31] that's fed by the optimizer. I'll talk
[17:31] that's fed by the optimizer. I'll talk about the third bullet point next, but
[17:33] about the third bullet point next, but
[17:34] about the third bullet point next, but in order to reduce the cost, um I was
[17:36] in order to reduce the cost, um I was
[17:36] in order to reduce the cost, um I was raising the minimum tool radius required
[17:38] raising the minimum tool radius required
[17:38] raising the minimum tool radius required to cut the panel. So, these very fine
[17:42] to cut the panel. So, these very fine
[17:42] to cut the panel. So, these very fine radii in here,
[17:43] radii in here,
[17:43] radii in here, um I eliminated those, increased the
[17:45] um I eliminated those, increased the
[17:46] um I eliminated those, increased the tool diameter by double. And then you
[17:49] tool diameter by double. And then you
[17:49] tool diameter by double. And then you can cut faster, and you can also have
[17:51] can cut faster, and you can also have
[17:51] can cut faster, and you can also have reduced tool wear when you're machining
[17:53] reduced tool wear when you're machining
[17:53] reduced tool wear when you're machining the parts. And then secondly,
[17:57] the parts. And then secondly,
[17:57] the parts. And then secondly, I reduced the thickness of the raw stock
[17:59] I reduced the thickness of the raw stock
[17:59] I reduced the thickness of the raw stock needed to make the part. So, if you're
[18:02] needed to make the part. So, if you're
[18:02] needed to make the part. So, if you're just considering making this part and
[18:03] just considering making this part and
[18:03] just considering making this part and starting with a raw material or a raw
[18:05] starting with a raw material or a raw
[18:05] starting with a raw material or a raw plate, um I reduced these bosses so that
[18:09] plate, um I reduced these bosses so that
[18:09] plate, um I reduced these bosses so that your thickness is reduced by
[18:11] your thickness is reduced by
[18:11] your thickness is reduced by 50% at least, and um
[18:14] 50% at least, and um
[18:14] 50% at least, and um and then those bosses carried some
[18:16] and then those bosses carried some
[18:16] and then those bosses carried some functionality that had to be replaced.
[18:17] functionality that had to be replaced.
[18:17] functionality that had to be replaced. For this, uh it was for mating to the
[18:20] For this, uh it was for mating to the
[18:20] For this, uh it was for mating to the other components, and I had to add in uh
[18:23] other components, and I had to add in uh
[18:23] other components, and I had to add in uh holes in order for my part to still be
[18:26] holes in order for my part to still be
[18:26] holes in order for my part to still be functional.
[18:27] functional.
[18:27] functional. So,
[18:28] So,
[18:28] So, um when I got a quote for this part, it
[18:30] um when I got a quote for this part, it
[18:30] um when I got a quote for this part, it was reduced all the way to 3 hours, and
[18:33] was reduced all the way to 3 hours, and
[18:33] was reduced all the way to 3 hours, and it didn't include the holes. So, in
[18:35] it didn't include the holes. So, in
[18:35] it didn't include the holes. So, in order to add those holes, it would be
[18:36] order to add those holes, it would be
[18:36] order to add those holes, it would be conservative to say that that new quote
[18:39] conservative to say that that new quote
[18:39] conservative to say that that new quote would be increased to 4 hours.
[18:47] So, uh this slide's talking about how is
[18:47] So, uh this slide's talking about how is it that the design takes results from
[18:49] it that the design takes results from
[18:49] it that the design takes results from the optimizer? Well, the optimizer
[18:51] the optimizer? Well, the optimizer
[18:51] the optimizer? Well, the optimizer considers the whole frame to be consist
[18:53] considers the whole frame to be consist
[18:53] considers the whole frame to be consist consisted of um
[18:55] consisted of um
[18:55] consisted of um one cross-section
[18:57] one cross-section
[18:57] one cross-section uh beam. So, all these external rails
[19:01] uh beam. So, all these external rails
[19:01] uh beam. So, all these external rails are considered to be of uh
[19:04] are considered to be of uh
[19:04] are considered to be of uh the same cross-section
[19:07] the same cross-section
[19:07] the same cross-section shown here.
[19:08] shown here.
[19:08] shown here. And um
[19:10] And um
[19:10] And um and the constraint is that the bending
[19:12] and the constraint is that the bending
[19:12] and the constraint is that the bending stiffness of my beam must be equal to or
[19:15] stiffness of my beam must be equal to or
[19:15] stiffness of my beam must be equal to or stronger than the bending stiffness of
[19:17] stronger than the bending stiffness of
[19:17] stronger than the bending stiffness of the benchmark. So, the benchmark has
[19:20] the benchmark. So, the benchmark has
[19:20] the benchmark. So, the benchmark has it's made of two different um angles. It
[19:23] it's made of two different um angles. It
[19:23] it's made of two different um angles. It has these cross-sections, and
[19:26] has these cross-sections, and
[19:27] has these cross-sections, and the third image is my cross-section
[19:29] the third image is my cross-section
[19:29] the third image is my cross-section that's has a greater um area moment of
[19:33] that's has a greater um area moment of
[19:33] that's has a greater um area moment of inertia than both of those.
[19:35] inertia than both of those.
[19:36] inertia than both of those. And those area moments of inertia are
[19:38] And those area moments of inertia are
[19:38] And those area moments of inertia are shown here. So, in
[19:41] shown here. So, in
[19:41] shown here. So, in the A axis, that's the principal axis
[19:44] the A axis, that's the principal axis
[19:44] the A axis, that's the principal axis bending axis of greatest strength, and A
[19:47] bending axis of greatest strength, and A
[19:47] bending axis of greatest strength, and A prime is 90° of that to that, and it's
[19:50] prime is 90° of that to that, and it's
[19:50] prime is 90° of that to that, and it's the lowest strength, and so this uh
[19:54] the lowest strength, and so this uh
[19:54] the lowest strength, and so this uh baseline for the constraint is greater
[19:57] baseline for the constraint is greater
[19:57] baseline for the constraint is greater than both of these. And then
[20:00] than both of these. And then
[20:00] than both of these. And then since the bending stiffness comes from
[20:03] since the bending stiffness comes from
[20:03] since the bending stiffness comes from the area moment of inertia and the
[20:05] the area moment of inertia and the
[20:05] the area moment of inertia and the modulus of elasticity, if the optimizer
[20:08] modulus of elasticity, if the optimizer
[20:08] modulus of elasticity, if the optimizer chooses steel instead of aluminum, then
[20:11] chooses steel instead of aluminum, then
[20:11] chooses steel instead of aluminum, then it's allowed to reduce L if it wants to
[20:15] it's allowed to reduce L if it wants to
[20:15] it's allowed to reduce L if it wants to to save weight.
[20:16] to save weight.
[20:16] to save weight. And it would still maintain that
[20:17] And it would still maintain that
[20:17] And it would still maintain that constraint. And then the area of moment
[20:19] constraint. And then the area of moment
[20:19] constraint. And then the area of moment of moment of inertia
[20:21] of moment of inertia
[20:21] of moment of inertia for
[20:22] for
[20:23] for section A is shown here.
[20:30] So,
[20:30] So, the next
[20:31] the next
[20:32] the next The next step was to take my model of a
[20:34] The next step was to take my model of a
[20:34] The next step was to take my model of a 1U and subject it to some finite element
[20:37] 1U and subject it to some finite element
[20:37] 1U and subject it to some finite element analysis.
[20:38] analysis.
[20:38] analysis. The analysis that I did here in this
[20:40] The analysis that I did here in this
[20:40] The analysis that I did here in this slide is to
[20:43] slide is to
[20:43] slide is to do 1,000 Gs of gravity
[20:46] do 1,000 Gs of gravity
[20:46] do 1,000 Gs of gravity downwards.
[20:47] downwards.
[20:47] downwards. And image two is showing how it would
[20:50] And image two is showing how it would
[20:50] And image two is showing how it would deform in an exaggerated manner under
[20:52] deform in an exaggerated manner under
[20:52] deform in an exaggerated manner under 1,000 Gs. And image three is showing the
[20:56] 1,000 Gs. And image three is showing the
[20:56] 1,000 Gs. And image three is showing the regions of the material that have a
[20:59] regions of the material that have a
[20:59] regions of the material that have a factor of safety less than 15.
[21:01] factor of safety less than 15.
[21:01] factor of safety less than 15. When that factor of safety for iso
[21:03] When that factor of safety for iso
[21:03] When that factor of safety for iso clipping is set to three, then you don't
[21:07] clipping is set to three, then you don't
[21:07] clipping is set to three, then you don't see any red regions.
[21:09] see any red regions.
[21:09] see any red regions. So, then I took the analysis that I did,
[21:12] So, then I took the analysis that I did,
[21:12] So, then I took the analysis that I did, and I wanted to do a convergence study.
[21:14] and I wanted to do a convergence study.
[21:14] and I wanted to do a convergence study. So, I started with a coarse mesh
[21:17] So, I started with a coarse mesh
[21:17] So, I started with a coarse mesh such as the one in figure four.
[21:20] such as the one in figure four.
[21:20] such as the one in figure four. And then I gradually refined that mesh
[21:22] And then I gradually refined that mesh
[21:22] And then I gradually refined that mesh to a finer and finer mesh and reran the
[21:24] to a finer and finer mesh and reran the
[21:24] to a finer and finer mesh and reran the study iteratively. And then I was
[21:27] study iteratively. And then I was
[21:27] study iteratively. And then I was checking each time what is the minimum
[21:29] checking each time what is the minimum
[21:29] checking each time what is the minimum factor of safety for all regions of the
[21:31] factor of safety for all regions of the
[21:31] factor of safety for all regions of the material. So, I want to see that the
[21:35] material. So, I want to see that the
[21:35] material. So, I want to see that the result converges, and it's not as nice
[21:38] result converges, and it's not as nice
[21:38] result converges, and it's not as nice as I wanted. The The convergence
[21:40] as I wanted. The The convergence
[21:40] as I wanted. The The convergence actually goes from right to left when
[21:41] actually goes from right to left when
[21:41] actually goes from right to left when you get finer.
[21:43] you get finer.
[21:43] you get finer. So, it's not as beautiful as I would
[21:45] So, it's not as beautiful as I would
[21:45] So, it's not as beautiful as I would want. And if I want to fully trust the
[21:47] want. And if I want to fully trust the
[21:47] want. And if I want to fully trust the FEA, then I would consult with somebody
[21:50] FEA, then I would consult with somebody
[21:50] FEA, then I would consult with somebody that's more experienced to say, "Is this
[21:52] that's more experienced to say, "Is this
[21:52] that's more experienced to say, "Is this a behavior that's good enough?" But in
[21:56] a behavior that's good enough?" But in
[21:56] a behavior that's good enough?" But in general, we're staying between 2.5 and
[21:59] general, we're staying between 2.5 and
[21:59] general, we're staying between 2.5 and 3.5 factor of safety. So, it's not
[22:02] 3.5 factor of safety. So, it's not
[22:02] 3.5 factor of safety. So, it's not extreme jumps. And so, I'm happy to see
[22:04] extreme jumps. And so, I'm happy to see
[22:04] extreme jumps. And so, I'm happy to see that.
[22:06] that.
[22:06] that. Um
[22:08] Um
[22:08] Um if I could confirm that the FEA is
[22:12] if I could confirm that the FEA is
[22:12] if I could confirm that the FEA is trustworthy and sufficient to say that
[22:14] trustworthy and sufficient to say that
[22:14] trustworthy and sufficient to say that the design is strong enough, then we
[22:17] the design is strong enough, then we
[22:17] the design is strong enough, then we could move away from the
[22:19] could move away from the
[22:19] could move away from the We could create designs that are less
[22:21] We could create designs that are less
[22:21] We could create designs that are less similar to the benchmark in geometry
[22:25] similar to the benchmark in geometry
[22:25] similar to the benchmark in geometry and just use the FEA to stand by rather
[22:28] and just use the FEA to stand by rather
[22:28] and just use the FEA to stand by rather than
[22:30] than
[22:30] than staying similar to the benchmark to
[22:32] staying similar to the benchmark to
[22:32] staying similar to the benchmark to claim that we're safe.
[22:40] So, as I continued with prototyping,
[22:40] So, as I continued with prototyping, the goals were to meet the tolerances,
[22:42] the goals were to meet the tolerances,
[22:42] the goals were to meet the tolerances, improve the speed, and find any
[22:45] improve the speed, and find any
[22:45] improve the speed, and find any weaknesses in the process that would
[22:47] weaknesses in the process that would
[22:47] weaknesses in the process that would cause it not to be manufacturable by the
[22:50] cause it not to be manufacturable by the
[22:50] cause it not to be manufacturable by the method I expect. So,
[22:53] method I expect. So,
[22:53] method I expect. So, starting with the eight hours from the
[22:55] starting with the eight hours from the
[22:55] starting with the eight hours from the quote, this is hours to
[22:59] quote, this is hours to
[22:59] quote, this is hours to build two panels.
[23:01] build two panels.
[23:01] build two panels. We start with eight hours, and then my
[23:04] We start with eight hours, and then my
[23:04] We start with eight hours, and then my first trial on building two panels
[23:07] first trial on building two panels
[23:07] first trial on building two panels yielded about six hours to build them.
[23:11] yielded about six hours to build them.
[23:11] yielded about six hours to build them. And then what I did was
[23:12] And then what I did was
[23:13] And then what I did was time
[23:14] time
[23:14] time cutting measures such as building a
[23:16] cutting measures such as building a
[23:16] cutting measures such as building a fixture
[23:18] fixture
[23:18] fixture that improves the that takes away time
[23:20] that improves the that takes away time
[23:20] that improves the that takes away time for lining things up and uh
[23:23] for lining things up and uh
[23:24] for lining things up and uh building a CNC code that's cutting two
[23:26] building a CNC code that's cutting two
[23:26] building a CNC code that's cutting two panels at once instead of just one panel
[23:28] panels at once instead of just one panel
[23:28] panels at once instead of just one panel at once. And I was able to reduce the
[23:29] at once. And I was able to reduce the
[23:29] at once. And I was able to reduce the time all the way from to two hours and
[23:32] time all the way from to two hours and
[23:32] time all the way from to two hours and 21 minutes.
[23:40] So, the final check for the prototype is
[23:40] So, the final check for the prototype is to meet tolerances and fit it where it's
[23:42] to meet tolerances and fit it where it's
[23:42] to meet tolerances and fit it where it's supposed to fit. So, image one is
[23:45] supposed to fit. So, image one is
[23:45] supposed to fit. So, image one is showing the CubeSat fitting into the
[23:49] showing the CubeSat fitting into the
[23:49] showing the CubeSat fitting into the PPOD deployer check fixture. So, the
[23:52] PPOD deployer check fixture. So, the
[23:52] PPOD deployer check fixture. So, the deployer comes from NanoRacks, and
[23:54] deployer comes from NanoRacks, and
[23:54] deployer comes from NanoRacks, and they're the official company that's
[23:55] they're the official company that's
[23:56] they're the official company that's delivering these to space. And so, if it
[23:57] delivering these to space. And so, if it
[23:58] delivering these to space. And so, if it fits in their check fixture, it's a go.
[24:00] fits in their check fixture, it's a go.
[24:00] fits in their check fixture, it's a go. And it did in fact fit in the check
[24:02] And it did in fact fit in the check
[24:02] And it did in fact fit in the check fixture. And also, I was measuring each
[24:05] fixture. And also, I was measuring each
[24:05] fixture. And also, I was measuring each part that came off of my CNC um
[24:09] part that came off of my CNC um
[24:09] part that came off of my CNC um to find out if it's meeting the
[24:10] to find out if it's meeting the
[24:10] to find out if it's meeting the tolerances that I just decided. And so,
[24:13] tolerances that I just decided. And so,
[24:13] tolerances that I just decided. And so, we're not 100% meeting the tolerances,
[24:15] we're not 100% meeting the tolerances,
[24:15] we're not 100% meeting the tolerances, but you have to keep in mind that I'm
[24:17] but you have to keep in mind that I'm
[24:17] but you have to keep in mind that I'm I'm changing the process each time to
[24:19] I'm changing the process each time to
[24:19] I'm changing the process each time to speed it up. So, the best tolerance here
[24:23] speed it up. So, the best tolerance here
[24:23] speed it up. So, the best tolerance here would likely be a repeatable tolerance
[24:26] would likely be a repeatable tolerance
[24:26] would likely be a repeatable tolerance once the the process is set in stone.
[24:30] once the the process is set in stone.
[24:30] once the the process is set in stone. And
[24:31] And
[24:31] And my solid red line refers to a tolerance
[24:35] my solid red line refers to a tolerance
[24:35] my solid red line refers to a tolerance if exceeded could cause interference
[24:37] if exceeded could cause interference
[24:37] if exceeded could cause interference between two mating parts. And my dash
[24:40] between two mating parts. And my dash
[24:40] between two mating parts. And my dash line here is a tolerance that would not
[24:42] line here is a tolerance that would not
[24:42] line here is a tolerance that would not cause any interference if it's violated,
[24:45] cause any interference if it's violated,
[24:45] cause any interference if it's violated, but it's
[24:47] but it's
[24:47] but it's not serving the design purpose so well.
[24:51] not serving the design purpose so well.
[24:51] not serving the design purpose so well. Um
[24:52] Um
[24:52] Um then finally, I designed and built a
[24:55] then finally, I designed and built a
[24:55] then finally, I designed and built a modular component called the fixed
[24:56] modular component called the fixed
[24:56] modular component called the fixed panel.
[24:57] panel.
[24:57] panel. And you could see that the fixed panel
[24:59] And you could see that the fixed panel
[24:59] And you could see that the fixed panel can simply be
[25:01] can simply be
[25:01] can simply be an inert panel
[25:02] an inert panel
[25:02] an inert panel or it can carry a solar panel, or it can
[25:05] or it can carry a solar panel, or it can
[25:05] or it can carry a solar panel, or it can carry a deployable antenna that I also
[25:08] carry a deployable antenna that I also
[25:08] carry a deployable antenna that I also designed, but I did not prototype.
[25:18] So, for conclusions,
[25:18] So, for conclusions, what I've drawn from the research is
[25:19] what I've drawn from the research is
[25:19] what I've drawn from the research is that a heuristic method is capable of
[25:22] that a heuristic method is capable of
[25:22] that a heuristic method is capable of optimizing a CubeSat and is enhanced by
[25:25] optimizing a CubeSat and is enhanced by
[25:25] optimizing a CubeSat and is enhanced by gradient-based functions to to do work
[25:28] gradient-based functions to to do work
[25:28] gradient-based functions to to do work on the continuous variables. I found
[25:31] on the continuous variables. I found
[25:31] on the continuous variables. I found that more commercial off-the-shelf
[25:33] that more commercial off-the-shelf
[25:33] that more commercial off-the-shelf subsystem data would be required to make
[25:36] subsystem data would be required to make
[25:36] subsystem data would be required to make a design that's fully truly usable. And
[25:41] a design that's fully truly usable. And
[25:41] a design that's fully truly usable. And that the manufacturing costs can be
[25:43] that the manufacturing costs can be
[25:43] that the manufacturing costs can be lowered by at least 50% from some
[25:46] lowered by at least 50% from some
[25:46] lowered by at least 50% from some existing designs. I don't have a
[25:48] existing designs. I don't have a
[25:48] existing designs. I don't have a guarantee that I benchmarked the lowest
[25:50] guarantee that I benchmarked the lowest
[25:50] guarantee that I benchmarked the lowest cost design, but I benchmarked a
[25:52] cost design, but I benchmarked a
[25:52] cost design, but I benchmarked a functional design and was able to reduce
[25:54] functional design and was able to reduce
[25:54] functional design and was able to reduce the time
[25:56] the time
[25:56] the time to build it.
[25:57] to build it.
[25:58] to build it. And this is based off of a a
[26:00] And this is based off of a a
[26:00] And this is based off of a a piece-by-piece evaluation. Where not
[26:02] piece-by-piece evaluation. Where not
[26:02] piece-by-piece evaluation. Where not 100% of the pieces are evaluated. Um
[26:06] 100% of the pieces are evaluated. Um
[26:06] 100% of the pieces are evaluated. Um So,
[26:07] So,
[26:07] So, this is what I have in recommendations
[26:09] this is what I have in recommendations
[26:09] this is what I have in recommendations for future work. One is to validate the
[26:12] for future work. One is to validate the
[26:12] for future work. One is to validate the X star design with a full prototype.
[26:14] X star design with a full prototype.
[26:14] X star design with a full prototype. This means building the model with all
[26:16] This means building the model with all
[26:16] This means building the model with all the subsystems,
[26:18] the subsystems,
[26:18] the subsystems, checking the power draw, and checking
[26:19] checking the power draw, and checking
[26:19] checking the power draw, and checking the propellant required. And And then
[26:23] the propellant required. And And then
[26:23] the propellant required. And And then going back to our numbers inside the
[26:24] going back to our numbers inside the
[26:24] going back to our numbers inside the model and updating them if they need to
[26:26] model and updating them if they need to
[26:26] model and updating them if they need to be changed to be fully representative of
[26:29] be changed to be fully representative of
[26:29] be changed to be fully representative of the truth. Then the model would be fully
[26:32] the truth. Then the model would be fully
[26:32] the truth. Then the model would be fully useful.
[26:33] useful.
[26:33] useful. So,
[26:34] So,
[26:34] So, then adding heuristic data to the Pareto
[26:37] then adding heuristic data to the Pareto
[26:37] then adding heuristic data to the Pareto front would give us a more full Pareto
[26:39] front would give us a more full Pareto
[26:39] front would give us a more full Pareto front, more options, and possibly
[26:43] front, more options, and possibly
[26:43] front, more options, and possibly better options. So, if for example, I
[26:47] better options. So, if for example, I
[26:47] better options. So, if for example, I added
[26:48] added
[26:48] added magnetorquers,
[26:49] magnetorquers,
[26:49] magnetorquers, which is a magnetic device for um
[26:52] which is a magnetic device for um
[26:52] which is a magnetic device for um for attitude control,
[26:54] for attitude control,
[26:54] for attitude control, then the optimizer might choose that all
[26:57] then the optimizer might choose that all
[26:57] then the optimizer might choose that all together instead of all propellant and
[26:59] together instead of all propellant and
[26:59] together instead of all propellant and and eliminate those needs for the
[27:01] and eliminate those needs for the
[27:01] and eliminate those needs for the propellant and the tanks.
[27:02] propellant and the tanks.
[27:03] propellant and the tanks. Um
[27:04] Um
[27:04] Um so, this would be useful. Adding
[27:07] so, this would be useful. Adding
[27:07] so, this would be useful. Adding multiple time scales to the optimization
[27:09] multiple time scales to the optimization
[27:09] multiple time scales to the optimization would make it more
[27:11] would make it more
[27:11] would make it more representative of the truth as well. Um
[27:14] representative of the truth as well. Um
[27:14] representative of the truth as well. Um because I have a constraint that says
[27:17] because I have a constraint that says
[27:17] because I have a constraint that says over the whole course of the mission,
[27:18] over the whole course of the mission,
[27:18] over the whole course of the mission, the power demand is met, but what about
[27:20] the power demand is met, but what about
[27:20] the power demand is met, but what about during that half an hour in the shade
[27:23] during that half an hour in the shade
[27:23] during that half an hour in the shade where it's not getting any power from
[27:24] where it's not getting any power from
[27:24] where it's not getting any power from the solar panels?
[27:26] the solar panels?
[27:26] the solar panels? Well, in my model, I made a minimum
[27:28] Well, in my model, I made a minimum
[27:28] Well, in my model, I made a minimum number of batteries for that reason, but
[27:30] number of batteries for that reason, but
[27:30] number of batteries for that reason, but it's not a
[27:31] it's not a
[27:32] it's not a It could be improved by adding multiple
[27:34] It could be improved by adding multiple
[27:34] It could be improved by adding multiple time scales.
[27:35] time scales.
[27:35] time scales. So, adding any details that impact
[27:38] So, adding any details that impact
[27:38] So, adding any details that impact performance in general, anything that I
[27:40] performance in general, anything that I
[27:40] performance in general, anything that I didn't account for that that is standard
[27:42] didn't account for that that is standard
[27:42] didn't account for that that is standard in CubeSat such as heating requirements.
[27:46] in CubeSat such as heating requirements.
[27:46] in CubeSat such as heating requirements. Some satellites have heaters that
[27:49] Some satellites have heaters that
[27:49] Some satellites have heaters that protect some elements from uh
[27:52] protect some elements from uh
[27:52] protect some elements from uh failing to operate. So, maybe the
[27:54] failing to operate. So, maybe the
[27:54] failing to operate. So, maybe the thruster, maybe one out of my three
[27:56] thruster, maybe one out of my three
[27:56] thruster, maybe one out of my three thrusters
[27:57] thrusters
[27:57] thrusters can operate in in too cold, and then you
[28:00] can operate in in too cold, and then you
[28:00] can operate in in too cold, and then you would need an extra power draw. So, that
[28:02] would need an extra power draw. So, that
[28:02] would need an extra power draw. So, that kind of relevant data needs to be added.
[28:04] kind of relevant data needs to be added.
[28:04] kind of relevant data needs to be added. And then
[28:06] And then
[28:06] And then a fancy thing to do would be write a CNC
[28:08] a fancy thing to do would be write a CNC
[28:08] a fancy thing to do would be write a CNC generating code. So,
[28:11] generating code. So,
[28:11] generating code. So, the optimizer would actually use the CAD
[28:14] the optimizer would actually use the CAD
[28:14] the optimizer would actually use the CAD design and be able to manipulate the CAD
[28:16] design and be able to manipulate the CAD
[28:16] design and be able to manipulate the CAD design and then
[28:18] design and then
[28:18] design and then output a CNC code that tells you how
[28:20] output a CNC code that tells you how
[28:20] output a CNC code that tells you how long does it take to manufacture and how
[28:22] long does it take to manufacture and how
[28:22] long does it take to manufacture and how much material is removed. Then
[28:26] much material is removed. Then
[28:26] much material is removed. Then then we could really
[28:28] then we could really
[28:28] then we could really fully integrate the machining with with
[28:31] fully integrate the machining with with
[28:31] fully integrate the machining with with the optimizer.
[28:33] the optimizer.
[28:33] the optimizer. So,
[28:35] So,
[28:35] So, I have references to sites, and I have
[28:39] I have references to sites, and I have
[28:39] I have references to sites, and I have time for questions and these topics that
[28:42] time for questions and these topics that
[28:42] time for questions and these topics that I kind of mentioned, but didn't fully
[28:44] I kind of mentioned, but didn't fully
[28:44] I kind of mentioned, but didn't fully elaborate on. So,
[28:47] elaborate on. So,
[28:47] elaborate on. So, Now now's the time for questions.
[28:54] Oh, and that's my reminder to give a
[28:54] Oh, and that's my reminder to give a handout so you can go through
[28:57] handout so you can go through
[28:57] handout so you can go through other slides if you wanted to. So, going
[29:00] other slides if you wanted to. So, going
[29:00] other slides if you wanted to. So, going back to that comparison with the
[29:02] back to that comparison with the
[29:02] back to that comparison with the the other studies that have been done to
[29:04] the other studies that have been done to
[29:04] the other studies that have been done to say that the mission of
[29:06] say that the mission of
[29:06] say that the mission of Sorry.
[29:07] Sorry.
[29:07] Sorry. So, they
[29:10] So, they
[29:10] So, they focused more on
[29:12] focused more on
[29:12] focused more on on optimizing the
[29:15] on optimizing the
[29:15] on optimizing the operational
[29:21] parameters like power delivery and
[29:21] parameters like power delivery and and
[29:23] and
[29:23] and data transmission rate, those sorts of
[29:25] data transmission rate, those sorts of
[29:25] data transmission rate, those sorts of things. And
[29:27] things. And
[29:27] things. And you focused more on
[29:33] not
[29:33] not the operational aspects, but more like
[29:35] the operational aspects, but more like
[29:35] the operational aspects, but more like the capital cost aspects of it, right?
[29:37] the capital cost aspects of it, right?
[29:37] the capital cost aspects of it, right? Basically, what is the mass and right?
[29:40] Basically, what is the mass and right?
[29:40] Basically, what is the mass and right? What is the cost to build this and so
[29:44] What is the cost to build this and so
[29:44] What is the cost to build this and so forth, right?
[29:45] forth, right?
[29:45] forth, right? So, it's kind of like
[29:47] So, it's kind of like
[29:47] So, it's kind of like the perspective is very different,
[29:49] the perspective is very different,
[29:49] the perspective is very different, right? Absolutely. The perspective is
[29:51] right? Absolutely. The perspective is
[29:51] right? Absolutely. The perspective is different. So, they assumed that
[29:54] different. So, they assumed that
[29:54] different. So, they assumed that cost is no object and Every study I've
[29:57] cost is no object and Every study I've
[29:57] cost is no object and Every study I've seen assumed that cost is no object.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
