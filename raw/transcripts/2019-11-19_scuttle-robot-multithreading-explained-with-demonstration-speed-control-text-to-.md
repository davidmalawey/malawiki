---
title: "SCUTTLE Robot - Multithreading Explained with Demonstration (Speed control & text-to-speech)"
url: "https://www.youtube.com/watch?v=DY7C0zPWRa8"
video_id: "DY7C0zPWRa8"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-11-19
duration: "6:39"
duration_sec: 399
views: 156
likes: 1
category: "Education"
keywords: ["yt:cc=on", "multithreading", "robotics", "python", "mxet300", "tamu", "demo"]
thumbnail_url: "https://i.ytimg.com/vi/DY7C0zPWRa8/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 250
chapters_count: 0
has_description: true
has_comments: false
---

## Description

Explanation of how and why to execute multithreading on the SCUTTLE robot using the Beaglebone Blue, Debian Linux, and the Scuttle software architecture. 

The software files used for this example are found on the project's github.

Level 3 driving: https://raw.githubusercontent.com/MXET/SCUTTLE/master/software/python/addons/L3_driveGP.py

Level 3 Speaking:
https://raw.githubusercontent.com/MXET/SCUTTLE/master/software/python/addons/L3_tellHeading.py

Level 4 Multithreading:
https://raw.githubusercontent.com/MXET/SCUTTLE/master/software/python/addons/L4_multithread.py

## Transcript

[0:02] let's quickly go over how you can use
[0:02] let's quickly go over how you can use multi-threading on your scuttle robot to
[0:05] multi-threading on your scuttle robot to
[0:05] multi-threading on your scuttle robot to improve the performance of execution of
[0:07] improve the performance of execution of
[0:07] improve the performance of execution of different tasks so we'll start with an
[0:11] different tasks so we'll start with an
[0:11] different tasks so we'll start with an example I want to execute two main
[0:13] example I want to execute two main
[0:13] example I want to execute two main programs each of which has a level 3
[0:16] programs each of which has a level 3
[0:16] programs each of which has a level 3 software to run on the left hand here I
[0:18] software to run on the left hand here I
[0:18] software to run on the left hand here I want to collect commands from the
[0:20] want to collect commands from the
[0:20] want to collect commands from the gamepad and perform closed loop speed
[0:23] gamepad and perform closed loop speed
[0:23] gamepad and perform closed loop speed control this program needs to execute at
[0:25] control this program needs to execute at
[0:25] control this program needs to execute at least five times per second in order to
[0:27] least five times per second in order to
[0:27] least five times per second in order to have smooth driving performance on the
[0:30] have smooth driving performance on the
[0:30] have smooth driving performance on the second program I want to have my robot
[0:33] second program I want to have my robot
[0:33] second program I want to have my robot evaluate its current heading and speak
[0:35] evaluate its current heading and speak
[0:35] evaluate its current heading and speak out loud to tell the heading to the user
[0:37] out loud to tell the heading to the user
[0:37] out loud to tell the heading to the user via voice to text so basically I have
[0:41] via voice to text so basically I have
[0:41] via voice to text so basically I have the encoders telling me the movement of
[0:44] the encoders telling me the movement of
[0:44] the encoders telling me the movement of my wheels I have the gamepad information
[0:47] my wheels I have the gamepad information
[0:47] my wheels I have the gamepad information captured on this column and passing
[0:50] captured on this column and passing
[0:50] captured on this column and passing commands to the level three and then the
[0:53] commands to the level three and then the
[0:53] commands to the level three and then the information gets crunched and spent to
[0:55] information gets crunched and spent to
[0:55] information gets crunched and spent to the speed control to give the target
[0:57] the speed control to give the target
[0:57] the speed control to give the target wheel speeds which eventually meet reach
[1:02] wheel speeds which eventually meet reach
[1:02] wheel speeds which eventually meet reach the motors on the second program I have
[1:05] the motors on the second program I have
[1:05] the motors on the second program I have the MPU sensor that's onboard the
[1:07] the MPU sensor that's onboard the
[1:07] the MPU sensor that's onboard the BeagleBone that's getting its values
[1:10] BeagleBone that's getting its values
[1:10] BeagleBone that's getting its values sampled from the compass driver in the
[1:14] sampled from the compass driver in the
[1:14] sampled from the compass driver in the RC py library the level 2 program called
[1:17] RC py library the level 2 program called
[1:17] RC py library the level 2 program called l2 heading is computing the heading of
[1:20] l2 heading is computing the heading of
[1:20] l2 heading is computing the heading of the robot from the compass values and
[1:24] the robot from the compass values and
[1:24] the robot from the compass values and then the information is getting
[1:27] then the information is getting
[1:27] then the information is getting converted into a couple of strings and
[1:29] converted into a couple of strings and
[1:29] converted into a couple of strings and the level 1 text-to-speech DUP PI
[1:32] the level 1 text-to-speech DUP PI
[1:32] the level 1 text-to-speech DUP PI program is going to pass to the audio
[1:34] program is going to pass to the audio
[1:34] program is going to pass to the audio driver and to the speaker onboard the
[1:36] driver and to the speaker onboard the
[1:36] driver and to the speaker onboard the scuttle the the heading so it can be
[1:40] scuttle the the heading so it can be
[1:40] scuttle the the heading so it can be spoken out loud so I only need to have
[1:44] spoken out loud so I only need to have
[1:44] spoken out loud so I only need to have the heading declared once every 3
[1:46] the heading declared once every 3
[1:46] the heading declared once every 3 seconds in other examples I may want to
[1:49] seconds in other examples I may want to
[1:49] seconds in other examples I may want to have messages declared through the
[1:51] have messages declared through the
[1:51] have messages declared through the speaker such as obstacle discovered
[1:53] speaker such as obstacle discovered
[1:53] speaker such as obstacle discovered which can occur due to specific specific
[1:56] which can occur due to specific specific
[1:56] which can occur due to specific specific events rather than on a space fixed
[2:00] events rather than on a space fixed
[2:00] events rather than on a space fixed timing regardless of the timing of the
[2:03] timing regardless of the timing of the
[2:03] timing regardless of the timing of the speaking loop it takes about 1.5 seconds
[2:06] speaking loop it takes about 1.5 seconds
[2:06] speaking loop it takes about 1.5 seconds to say the words out loud if the
[2:08] to say the words out loud if the
[2:08] to say the words out loud if the speaking event is added inside of the
[2:10] speaking event is added inside of the
[2:10] speaking event is added inside of the driving loop over here
[2:13] driving loop over here
[2:13] driving loop over here it will cause a big gap in the speed
[2:15] it will cause a big gap in the speed
[2:15] it will cause a big gap in the speed control executions and it will cause an
[2:17] control executions and it will cause an
[2:17] control executions and it will cause an interruption of the motors receiving an
[2:19] interruption of the motors receiving an
[2:19] interruption of the motors receiving an updated power level in this case
[2:22] updated power level in this case
[2:22] updated power level in this case multi-threading can be used so that both
[2:24] multi-threading can be used so that both
[2:24] multi-threading can be used so that both these tasks can be executed in parallel
[2:27] these tasks can be executed in parallel
[2:27] these tasks can be executed in parallel the ARM processor can handle rapid
[2:29] the ARM processor can handle rapid
[2:29] the ARM processor can handle rapid executions of all functions and the
[2:32] executions of all functions and the
[2:32] executions of all functions and the potential delays are simply due to the
[2:34] potential delays are simply due to the
[2:34] potential delays are simply due to the time it takes to execute speaking if you
[2:37] time it takes to execute speaking if you
[2:37] time it takes to execute speaking if you have delays due to heavy processing
[2:39] have delays due to heavy processing
[2:39] have delays due to heavy processing requirements multi-threading will not
[2:41] requirements multi-threading will not
[2:41] requirements multi-threading will not solve your problem multi-threading is
[2:43] solve your problem multi-threading is
[2:43] solve your problem multi-threading is not a magic tool here's how I have set
[2:49] not a magic tool here's how I have set
[2:49] not a magic tool here's how I have set up the level 3 tell heading dot PI
[2:52] up the level 3 tell heading dot PI
[2:52] up the level 3 tell heading dot PI program and the level 3 Drive GP program
[2:56] program and the level 3 Drive GP program
[2:56] program and the level 3 Drive GP program this one is for driving by the gamepad
[2:58] this one is for driving by the gamepad
[2:58] this one is for driving by the gamepad and actually for the video that's coming
[3:01] and actually for the video that's coming
[3:01] and actually for the video that's coming up I've actually taken out the Phi dot
[3:05] up I've actually taken out the Phi dot
[3:05] up I've actually taken out the Phi dot targets that are requested from the
[3:08] targets that are requested from the
[3:08] targets that are requested from the gamepad and replace them with simple
[3:10] gamepad and replace them with simple
[3:10] gamepad and replace them with simple constants so my robot will drive in a
[3:12] constants so my robot will drive in a
[3:12] constants so my robot will drive in a circle all the information the importing
[3:16] circle all the information the importing
[3:16] circle all the information the importing takes place and then the variables which
[3:19] takes place and then the variables which
[3:19] takes place and then the variables which are initialized outside of the main loop
[3:22] are initialized outside of the main loop
[3:22] are initialized outside of the main loop are actually re copied into a program
[3:26] are actually re copied into a program
[3:26] are actually re copied into a program called into a function called go and
[3:29] called into a function called go and
[3:29] called into a function called go and then the purpose of the go function is
[3:34] then the purpose of the go function is
[3:34] then the purpose of the go function is to wrap up all of the declarations and
[3:38] to wrap up all of the declarations and
[3:38] to wrap up all of the declarations and functions that I would normally have in
[3:41] functions that I would normally have in
[3:41] functions that I would normally have in the loop of the level 3 and you can see
[3:44] the loop of the level 3 and you can see
[3:44] the loop of the level 3 and you can see down here the while loop for the level 3
[3:47] down here the while loop for the level 3
[3:47] down here the while loop for the level 3 has been commented out and basically all
[3:49] has been commented out and basically all
[3:49] has been commented out and basically all this information is put into a function
[3:51] this information is put into a function
[3:51] this information is put into a function called go in level 3 tell heading dot pi
[3:55] called go in level 3 tell heading dot pi
[3:55] called go in level 3 tell heading dot pi I have the same situation a switch case
[3:59] I have the same situation a switch case
[3:59] I have the same situation a switch case is what's generating the north west east
[4:02] is what's generating the north west east
[4:02] is what's generating the north west east south strings that are going to get
[4:05] south strings that are going to get
[4:05] south strings that are going to get passed to the audio and then the
[4:07] passed to the audio and then the
[4:07] passed to the audio and then the function called go is going to do the
[4:11] function called go is going to do the
[4:11] function called go is going to do the the Declaration of the heading via voice
[4:15] the Declaration of the heading via voice
[4:15] the Declaration of the heading via voice and then it's going to sleep for 3
[4:17] and then it's going to sleep for 3
[4:17] and then it's going to sleep for 3 seconds so that there's a delay and it's
[4:20] seconds so that there's a delay and it's
[4:20] seconds so that there's a delay and it's not continuously talking in the level 4
[4:24] not continuously talking in the level 4
[4:24] not continuously talking in the level 4 we basically just import both
[4:26] we basically just import both
[4:26] we basically just import both threes and we asked them to join the
[4:29] threes and we asked them to join the
[4:29] threes and we asked them to join the threading what happens is the importing
[4:32] threading what happens is the importing
[4:32] threading what happens is the importing is here in lines 8 &amp; 9 then I define a
[4:35] is here in lines 8 &amp; 9 then I define a
[4:35] is here in lines 8 &amp; 9 then I define a loop speak where I'm simply I'm not
[4:40] loop speak where I'm simply I'm not
[4:40] loop speak where I'm simply I'm not actually even going to loop in this
[4:41] actually even going to loop in this
[4:41] actually even going to loop in this instance I'm just going to call that
[4:44] instance I'm just going to call that
[4:44] instance I'm just going to call that function once and it has an infinite
[4:46] function once and it has an infinite
[4:46] function once and it has an infinite while loop inside of it the same thing
[4:48] while loop inside of it the same thing
[4:48] while loop inside of it the same thing is happening with the loop drive so I
[4:50] is happening with the loop drive so I
[4:50] is happening with the loop drive so I have Drive go now in the main function
[4:54] have Drive go now in the main function
[4:54] have Drive go now in the main function of my level 4 I'm going to tell you that
[4:58] of my level 4 I'm going to tell you that
[4:58] of my level 4 I'm going to tell you that I'm starting the main function I'm going
[4:59] I'm starting the main function I'm going
[4:59] I'm starting the main function I'm going to create an object for the threads I'm
[5:02] to create an object for the threads I'm
[5:02] to create an object for the threads I'm going to make my first thread object and
[5:06] going to make my first thread object and
[5:06] going to make my first thread object and inside that object will be a target
[5:09] inside that object will be a target
[5:09] inside that object will be a target equals loop speak so the speaking will
[5:11] equals loop speak so the speaking will
[5:11] equals loop speak so the speaking will be added to this so then I'm going to
[5:14] be added to this so then I'm going to
[5:14] be added to this so then I'm going to append this object to the threads object
[5:17] append this object to the threads object
[5:17] append this object to the threads object and then I'll start this thread and
[5:21] and then I'll start this thread and
[5:21] and then I'll start this thread and we're going to print out to the to the
[5:24] we're going to print out to the to the
[5:24] we're going to print out to the to the screen that we thought started the first
[5:26] screen that we thought started the first
[5:26] screen that we thought started the first thread the same the same few options are
[5:32] thread the same the same few options are
[5:32] thread the same the same few options are being executed for thread 2 which is
[5:35] being executed for thread 2 which is
[5:35] being executed for thread 2 which is going to handle the driving and then
[5:37] going to handle the driving and then
[5:37] going to handle the driving and then thread 2 is being asked to start and
[5:39] thread 2 is being asked to start and
[5:39] thread 2 is being asked to start and then finally lines 36 and 37 refer to
[5:44] then finally lines 36 and 37 refer to
[5:44] then finally lines 36 and 37 refer to the details you should read up on it's
[5:48] the details you should read up on it's
[5:48] the details you should read up on it's most important if you need to wait for
[5:50] most important if you need to wait for
[5:50] most important if you need to wait for one thread to complete some certain
[5:53] one thread to complete some certain
[5:53] one thread to complete some certain actions before you finish your program
[5:55] actions before you finish your program
[5:55] actions before you finish your program or before you finish operating another
[6:02] or before you finish operating another
[6:02] or before you finish operating another thread
[6:04] thread
[6:04] thread [Music]

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
