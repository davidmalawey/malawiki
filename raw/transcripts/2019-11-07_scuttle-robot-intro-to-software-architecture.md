---
title: "SCUTTLE Robot - Intro to Software Architecture"
url: "https://www.youtube.com/watch?v=JY8tARr74Ic"
video_id: "JY8tARr74Ic"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-11-07
duration: "4:44"
duration_sec: 284
views: 1259
likes: 7
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/JY8tARr74Ic/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 170
chapters_count: 4
has_description: true
has_comments: false
---

## Description

explanation of level 1 files, level 2 files, how data flows and how testing can be done to validate modules.

## Chapters

- 0:00 Intro
- 1:06 Labeling
- 2:02 Troubleshooting
- 3:37 Dependencies

## Transcript

[0:04] this slide explains the basics of how
[0:04] this slide explains the basics of how software is created for the scuttle
[0:06] software is created for the scuttle
[0:06] software is created for the scuttle architecture the yellow items down at
[0:10] architecture the yellow items down at
[0:10] architecture the yellow items down at the bottom indicate sensors the orange
[0:12] the bottom indicate sensors the orange
[0:12] the bottom indicate sensors the orange items indicate actuators and then the
[0:16] items indicate actuators and then the
[0:16] items indicate actuators and then the green items on the level one
[0:18] green items on the level one
[0:18] green items on the level one they are Python files that communicate
[0:22] they are Python files that communicate
[0:22] they are Python files that communicate with one sensor and receive data or they
[0:25] with one sensor and receive data or they
[0:25] with one sensor and receive data or they communicate to one actuator and they
[0:28] communicate to one actuator and they
[0:28] communicate to one actuator and they output data really the output commands
[0:31] output data really the output commands
[0:31] output data really the output commands for that actuator to function the level
[0:34] for that actuator to function the level
[0:34] for that actuator to function the level two blocks in blue are performing the
[0:38] two blocks in blue are performing the
[0:38] two blocks in blue are performing the receiving of data from a level one and
[0:40] receiving of data from a level one and
[0:40] receiving of data from a level one and some computation or deriving some
[0:43] some computation or deriving some
[0:43] some computation or deriving some meaning for the mission that your robot
[0:46] meaning for the mission that your robot
[0:46] meaning for the mission that your robot is on and then the level three is doing
[0:50] is on and then the level three is doing
[0:50] is on and then the level three is doing some decision-making where you compare
[0:52] some decision-making where you compare
[0:52] some decision-making where you compare different pieces of information and you
[0:55] different pieces of information and you
[0:55] different pieces of information and you create algorithms that that ultimately
[0:59] create algorithms that that ultimately
[0:59] create algorithms that that ultimately give commands to the actuators or
[1:03] give commands to the actuators or
[1:03] give commands to the actuators or feedback to the user the purple text
[1:08] feedback to the user the purple text
[1:08] feedback to the user the purple text along each signal is to indicate what
[1:11] along each signal is to indicate what
[1:11] along each signal is to indicate what information is being passed from one
[1:15] information is being passed from one
[1:15] information is being passed from one block to another it's important to note
[1:18] block to another it's important to note
[1:18] block to another it's important to note that l2 obstacle pie may be sending more
[1:25] that l2 obstacle pie may be sending more
[1:25] that l2 obstacle pie may be sending more than just this single piece of data
[1:27] than just this single piece of data
[1:27] than just this single piece of data nearest obstacle but basically you could
[1:33] nearest obstacle but basically you could
[1:33] nearest obstacle but basically you could have a function that describes nearest
[1:36] have a function that describes nearest
[1:36] have a function that describes nearest obstacle and this would be an X and a
[1:38] obstacle and this would be an X and a
[1:38] obstacle and this would be an X and a y-coordinate it's best to be specific
[1:41] y-coordinate it's best to be specific
[1:41] y-coordinate it's best to be specific about labeling your signals so that
[1:45] about labeling your signals so that
[1:45] about labeling your signals so that you're clear on what your mission is
[1:46] you're clear on what your mission is
[1:46] you're clear on what your mission is actually doing and I could have an
[1:50] actually doing and I could have an
[1:50] actually doing and I could have an alternative function that tells me
[1:52] alternative function that tells me
[1:52] alternative function that tells me what's the direction of the opening in
[1:56] what's the direction of the opening in
[1:56] what's the direction of the opening in the room that's been derived from the
[2:00] the room that's been derived from the
[2:00] the room that's been derived from the lidar so if we want to do
[2:03] lidar so if we want to do
[2:03] lidar so if we want to do troubleshooting then you can start from
[2:05] troubleshooting then you can start from
[2:05] troubleshooting then you can start from the bottom and move up let's say we want
[2:09] the bottom and move up let's say we want
[2:09] the bottom and move up let's say we want to know can we detect an obstacle and
[2:12] to know can we detect an obstacle and
[2:12] to know can we detect an obstacle and drive around it
[2:14] drive around it
[2:14] drive around it and we want to begin troubleshooting so
[2:18] and we want to begin troubleshooting so
[2:18] and we want to begin troubleshooting so first you want to validate that these
[2:20] first you want to validate that these
[2:20] first you want to validate that these two boxes are working fine
[2:22] two boxes are working fine
[2:22] two boxes are working fine this means your hardware is connected
[2:24] this means your hardware is connected
[2:24] this means your hardware is connected properly it's communicating with your
[2:27] properly it's communicating with your
[2:27] properly it's communicating with your robot and this l1 lidar dot pi is able
[2:31] robot and this l1 lidar dot pi is able
[2:31] robot and this l1 lidar dot pi is able to receive the data the raw data from
[2:34] to receive the data the raw data from
[2:34] to receive the data the raw data from the sensor and these level ones should
[2:36] the sensor and these level ones should
[2:36] the sensor and these level ones should have a loop that you can uncomment and
[2:38] have a loop that you can uncomment and
[2:39] have a loop that you can uncomment and execute the the program by itself and in
[2:42] execute the the program by itself and in
[2:42] execute the the program by itself and in a standalone manner you can just run
[2:44] a standalone manner you can just run
[2:44] a standalone manner you can just run these two items and validate that your
[2:48] these two items and validate that your
[2:48] these two items and validate that your that your subsystem is working then you
[2:52] that your subsystem is working then you
[2:52] that your subsystem is working then you would comment your loop that executes
[2:55] would comment your loop that executes
[2:55] would comment your loop that executes infinitely in this program and then you
[2:58] infinitely in this program and then you
[2:58] infinitely in this program and then you can test this whole column and you can
[3:02] can test this whole column and you can
[3:02] can test this whole column and you can say am I getting my arrays of distances
[3:06] say am I getting my arrays of distances
[3:06] say am I getting my arrays of distances and angles and then am i taking the
[3:08] and angles and then am i taking the
[3:08] and angles and then am i taking the subset of arrays and figuring out which
[3:11] subset of arrays and figuring out which
[3:11] subset of arrays and figuring out which one is the nearest obstacle and can I
[3:14] one is the nearest obstacle and can I
[3:14] one is the nearest obstacle and can I output this information and so when you
[3:17] output this information and so when you
[3:17] output this information and so when you make a level two it should also have a
[3:19] make a level two it should also have a
[3:19] make a level two it should also have a loop that outputs its important relevant
[3:22] loop that outputs its important relevant
[3:22] loop that outputs its important relevant information if the level two has five
[3:25] information if the level two has five
[3:25] information if the level two has five different functions then maybe while
[3:27] different functions then maybe while
[3:27] different functions then maybe while you're troubleshooting you're going to
[3:28] you're troubleshooting you're going to
[3:28] you're troubleshooting you're going to just execute one of those functions in
[3:31] just execute one of those functions in
[3:31] just execute one of those functions in the loop in the testing the testing loop
[3:34] the loop in the testing the testing loop
[3:34] the loop in the testing the testing loop for this software it's important to note
[3:38] for this software it's important to note
[3:38] for this software it's important to note that these these columns indicate some
[3:43] that these these columns indicate some
[3:43] that these these columns indicate some dependencies it says well level two
[3:46] dependencies it says well level two
[3:46] dependencies it says well level two obstacle pi will obviously need to
[3:51] obstacle pi will obviously need to
[3:51] obstacle pi will obviously need to import the l1 lidar dot pi but on
[3:54] import the l1 lidar dot pi but on
[3:54] import the l1 lidar dot pi but on occasion you might design a level two
[3:57] occasion you might design a level two
[3:57] occasion you might design a level two that's that's dependent on multiple
[3:59] that's that's dependent on multiple
[3:59] that's that's dependent on multiple level ones and alternatively the level
[4:05] level ones and alternatively the level
[4:05] level ones and alternatively the level ones and the level twos may be importing
[4:08] ones and the level twos may be importing
[4:08] ones and the level twos may be importing information from other libraries so the
[4:11] information from other libraries so the
[4:11] information from other libraries so the l1 lidar PI is going to import the USB
[4:17] l1 lidar PI is going to import the USB
[4:17] l1 lidar PI is going to import the USB library for python and it's also
[4:20] library for python and it's also
[4:20] library for python and it's also importing a library called PI SiC Tim
[4:22] importing a library called PI SiC Tim
[4:22] importing a library called PI SiC Tim which is kind of like a driver for the
[4:25] which is kind of like a driver for the
[4:25] which is kind of like a driver for the lidar device so the X
[4:27] lidar device so the X
[4:27] lidar device so the X libraries are not indicated in this
[4:29] libraries are not indicated in this
[4:29] libraries are not indicated in this diagram

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
