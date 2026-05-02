---
title: "what GPT5 is doing to open robotics design - better than I imagined"
url: "https://www.youtube.com/watch?v=GBuXDm2Qahw"
video_id: "GBuXDm2Qahw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-08-11
duration: "15:59"
duration_sec: 959
views: 3953
likes: 192
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/GBuXDm2Qahw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 726
chapters_count: 0
has_description: true
has_comments: false
---

## Description

I'm posting this entirely unplanned video because there's good news!   Last month was very rough for me and today I'm seeing brand new possibilities unlocked.  My example comes from ChatGPT-5 but it's not about AI, really.  It's about making sacrifices for a long time that are paying off now.  More learners can have more access to more success with engineering and robotics.

This demonstration shows a BELT AND PULLEY SYSTEM that we use on SCUTTLE Robot for educating engineering students and hands-on designs.  With just one simple prompt, I could make an accurate visualized model of the belt system to give students control of the physical system design.

I certainly aware of crises facing our world.  It's hard to set aside those topics and they impact me directly.  But today is for focusing on the good, please! 

[ATTACHMENT COMING]
I'm planning to make available the code output from this belt & pulley simulation, if it's desired.  Please let me know in comments!

## Transcript

[0:03] Oh my gosh, you guys. This is like
[0:03] Oh my gosh, you guys. This is like dreams unfolding in real life. Okay, 5
[0:06] dreams unfolding in real life. Okay, 5
[0:06] dreams unfolding in real life. Okay, 5 years ago, I made a bet that we should
[0:08] years ago, I made a bet that we should
[0:08] years ago, I made a bet that we should engineer systems to teach students with
[0:10] engineer systems to teach students with
[0:10] engineer systems to teach students with robotics uh with real life usable
[0:13] robotics uh with real life usable
[0:13] robotics uh with real life usable robotic systems and then we should take
[0:15] robotic systems and then we should take
[0:15] robotic systems and then we should take like 10 times more effort than necessary
[0:19] like 10 times more effort than necessary
[0:19] like 10 times more effort than necessary to get a functional machine working. And
[0:22] to get a functional machine working. And
[0:22] to get a functional machine working. And all of that was for the sake of having
[0:25] all of that was for the sake of having
[0:25] all of that was for the sake of having parameters. I don't know if if you have
[0:27] parameters. I don't know if if you have
[0:27] parameters. I don't know if if you have a system and you have every single how
[0:30] a system and you have every single how
[0:30] a system and you have every single how many grams is this thing and how what's
[0:32] many grams is this thing and how what's
[0:32] many grams is this thing and how what's the plastic and what's the what's the
[0:34] the plastic and what's the what's the
[0:34] the plastic and what's the what's the exact geometry already stored and
[0:36] exact geometry already stored and
[0:36] exact geometry already stored and digitized then from there as technology
[0:38] digitized then from there as technology
[0:38] digitized then from there as technology unfolds we can extract and develop new
[0:41] unfolds we can extract and develop new
[0:41] unfolds we can extract and develop new simulations and new like better learning
[0:44] simulations and new like better learning
[0:44] simulations and new like better learning materials and graphics and explanations
[0:48] materials and graphics and explanations
[0:48] materials and graphics and explanations and videos based on the physical real
[0:50] and videos based on the physical real
[0:50] and videos based on the physical real stuff as long as it's characterized and
[0:53] stuff as long as it's characterized and
[0:53] stuff as long as it's characterized and we can do that um if we put the the
[0:57] we can do that um if we put the the
[0:57] we can do that um if we put the the front side effort on uh creating that
[1:00] front side effort on uh creating that
[1:00] front side effort on uh creating that system. So that that system was was and
[1:03] system. So that that system was was and
[1:03] system. So that that system was was and is the the Scoal robot where three
[1:07] is the the Scoal robot where three
[1:07] is the the Scoal robot where three iterations three major versions of this
[1:09] iterations three major versions of this
[1:09] iterations three major versions of this robot have been produced. I did most of
[1:12] robot have been produced. I did most of
[1:12] robot have been produced. I did most of the engineering for all of this
[1:13] the engineering for all of this
[1:13] the engineering for all of this mechanical stuff so that the electronics
[1:16] mechanical stuff so that the electronics
[1:16] mechanical stuff so that the electronics can be swapped and interchanged and
[1:18] can be swapped and interchanged and
[1:18] can be swapped and interchanged and enhanced and mechanically it's sturdy
[1:21] enhanced and mechanically it's sturdy
[1:21] enhanced and mechanically it's sturdy enough that we can build up on it and we
[1:23] enough that we can build up on it and we
[1:23] enough that we can build up on it and we can add things that will change the
[1:24] can add things that will change the
[1:24] can add things that will change the center of mass and change the speeds and
[1:26] center of mass and change the speeds and
[1:26] center of mass and change the speeds and uh make it give it brushless wheels and
[1:30] uh make it give it brushless wheels and
[1:30] uh make it give it brushless wheels and super speed or we can add different
[1:32] super speed or we can add different
[1:32] super speed or we can add different actuators. Just a quick example.
[1:35] actuators. Just a quick example.
[1:35] actuators. Just a quick example. So this is the exact same chassis.
[1:38] So this is the exact same chassis.
[1:38] So this is the exact same chassis. Everything's the same, but we've swapped
[1:40] Everything's the same, but we've swapped
[1:40] Everything's the same, but we've swapped the wheels out, which changes the gear
[1:41] the wheels out, which changes the gear
[1:42] the wheels out, which changes the gear ratio, changes how it drives, and
[1:43] ratio, changes how it drives, and
[1:43] ratio, changes how it drives, and changes the the clearance. So, if you
[1:45] changes the the clearance. So, if you
[1:45] changes the the clearance. So, if you want to do an outdoor delivery system,
[1:48] want to do an outdoor delivery system,
[1:48] want to do an outdoor delivery system, then it's literally just a few
[1:50] then it's literally just a few
[1:50] then it's literally just a few parameters swapped on the the design of
[1:53] parameters swapped on the the design of
[1:53] parameters swapped on the the design of this assembly, and then we uh load this
[1:56] this assembly, and then we uh load this
[1:56] this assembly, and then we uh load this wheel onto there. But the other
[1:58] wheel onto there. But the other
[1:58] wheel onto there. But the other constraint of the system is every single
[2:00] constraint of the system is every single
[2:00] constraint of the system is every single part has to be directly off the shelf
[2:02] part has to be directly off the shelf
[2:02] part has to be directly off the shelf from a super high volume, super well-
[2:04] from a super high volume, super well-
[2:04] from a super high volume, super well- characterized component. So there's a
[2:08] characterized component. So there's a
[2:08] characterized component. So there's a deterministic amount of mass and
[2:10] deterministic amount of mass and
[2:10] deterministic amount of mass and materials and uh and a super clear like
[2:14] materials and uh and a super clear like
[2:14] materials and uh and a super clear like behind each of these elements and behind
[2:16] behind each of these elements and behind
[2:16] behind each of these elements and behind the Panasonic batteries there's a heaps
[2:18] the Panasonic batteries there's a heaps
[2:18] the Panasonic batteries there's a heaps and heaps of data that defines what
[2:21] and heaps of data that defines what
[2:21] and heaps of data that defines what you're starting with so that when you
[2:23] you're starting with so that when you
[2:23] you're starting with so that when you modify it you can modify it with the
[2:25] modify it you can modify it with the
[2:25] modify it you can modify it with the help of well now we have AI for that.
[2:28] help of well now we have AI for that.
[2:28] help of well now we have AI for that. So, in a sense, this robot isn't about
[2:30] So, in a sense, this robot isn't about
[2:30] So, in a sense, this robot isn't about this robot. It's about the the first and
[2:33] this robot. It's about the the first and
[2:33] this robot. It's about the the first and only modular but fully ready and
[2:36] only modular but fully ready and
[2:36] only modular but fully ready and repeatable
[2:38] repeatable
[2:38] repeatable um robotic system that includes all the
[2:40] um robotic system that includes all the
[2:40] um robotic system that includes all the same elements that we include in all
[2:42] same elements that we include in all
[2:42] same elements that we include in all these other different kinds of systems.
[2:43] these other different kinds of systems.
[2:43] these other different kinds of systems. For instance, these kind of motors
[2:45] For instance, these kind of motors
[2:45] For instance, these kind of motors operate with our very common affordable
[2:49] operate with our very common affordable
[2:49] operate with our very common affordable uh off-the-shelf brushless motor
[2:51] uh off-the-shelf brushless motor
[2:52] uh off-the-shelf brushless motor drivers. And there's millions to select
[2:54] drivers. And there's millions to select
[2:54] drivers. And there's millions to select from. And then they these use a kind of
[2:56] from. And then they these use a kind of
[2:56] from. And then they these use a kind of signal that's uh a certain waveform that
[2:59] signal that's uh a certain waveform that
[2:59] signal that's uh a certain waveform that we get from the servo type drivers.
[3:02] we get from the servo type drivers.
[3:02] we get from the servo type drivers. These have been longstanding as a
[3:04] These have been longstanding as a
[3:04] These have been longstanding as a standard um in the hobby RC hobby space,
[3:08] standard um in the hobby RC hobby space,
[3:08] standard um in the hobby RC hobby space, airplanes, drones um and RC cars and so
[3:11] airplanes, drones um and RC cars and so
[3:11] airplanes, drones um and RC cars and so forth. And that's a different type of
[3:13] forth. And that's a different type of
[3:14] forth. And that's a different type of signal than the signal we send to our
[3:16] signal than the signal we send to our
[3:16] signal than the signal we send to our motor driver. But we want to be able to
[3:18] motor driver. But we want to be able to
[3:18] motor driver. But we want to be able to accommodate both of them. And so me as
[3:20] accommodate both of them. And so me as
[3:20] accommodate both of them. And so me as an instructor and as an engineer, I'm
[3:22] an instructor and as an engineer, I'm
[3:22] an instructor and as an engineer, I'm creating these modules to say, okay,
[3:24] creating these modules to say, okay,
[3:24] creating these modules to say, okay, here's here's the motor and driver and
[3:26] here's here's the motor and driver and
[3:26] here's here's the motor and driver and power for that as a system. And here's
[3:29] power for that as a system. And here's
[3:29] power for that as a system. And here's how you would isolate that as a a
[3:32] how you would isolate that as a a
[3:32] how you would isolate that as a a working module and then swap and and the
[3:36] working module and then swap and and the
[3:36] working module and then swap and and the possibilities are limitless. We want to
[3:38] possibilities are limitless. We want to
[3:38] possibilities are limitless. We want to be able to empower students and uh the
[3:42] be able to empower students and uh the
[3:42] be able to empower students and uh the most ready students to operate with this
[3:44] most ready students to operate with this
[3:44] most ready students to operate with this system are, you know, given our standard
[3:47] system are, you know, given our standard
[3:47] system are, you know, given our standard typical curriculums in colleges, the
[3:49] typical curriculums in colleges, the
[3:49] typical curriculums in colleges, the electronic students, the ones who
[3:50] electronic students, the ones who
[3:50] electronic students, the ones who already know how to program
[3:52] already know how to program
[3:52] already know how to program microcontrollers and hook up generally
[3:54] microcontrollers and hook up generally
[3:54] microcontrollers and hook up generally hook up power to things. And so behind
[3:58] hook up power to things. And so behind
[3:58] hook up power to things. And so behind the robot are lots and lots of tables
[4:00] the robot are lots and lots of tables
[4:00] the robot are lots and lots of tables that I built. uh every decision that I
[4:03] that I built. uh every decision that I
[4:03] that I built. uh every decision that I made on this robot, I also made a a
[4:06] made on this robot, I also made a a
[4:06] made on this robot, I also made a a reference material that explains, well,
[4:09] reference material that explains, well,
[4:09] reference material that explains, well, how did we make this decision? And then
[4:11] how did we make this decision? And then
[4:11] how did we make this decision? And then turn down the amount of mechanical
[4:13] turn down the amount of mechanical
[4:13] turn down the amount of mechanical knowledge that you would need to make
[4:16] knowledge that you would need to make
[4:16] knowledge that you would need to make modifications to the robot. um coming
[4:19] modifications to the robot. um coming
[4:19] modifications to the robot. um coming from here's an example of the pulleys
[4:21] from here's an example of the pulleys
[4:21] from here's an example of the pulleys that we used. They have a timing belt
[4:24] that we used. They have a timing belt
[4:24] that we used. They have a timing belt specification and if you change that
[4:26] specification and if you change that
[4:26] specification and if you change that here is a all these options of where we
[4:29] here is a all these options of where we
[4:29] here is a all these options of where we would go from there to adjust the gear
[4:31] would go from there to adjust the gear
[4:32] would go from there to adjust the gear ratios etc.
[4:34] ratios etc.
[4:34] ratios etc. Um the point of all this data was to
[4:37] Um the point of all this data was to
[4:37] Um the point of all this data was to pre-calculate the mechanical engineering
[4:40] pre-calculate the mechanical engineering
[4:40] pre-calculate the mechanical engineering aspects of this drivetrain for example
[4:43] aspects of this drivetrain for example
[4:43] aspects of this drivetrain for example and then to slim down the effort level
[4:46] and then to slim down the effort level
[4:46] and then to slim down the effort level and the learning requirements for let's
[4:48] and the learning requirements for let's
[4:48] and the learning requirements for let's say electronic students to make
[4:51] say electronic students to make
[4:51] say electronic students to make decisions and make changes and take
[4:53] decisions and make changes and take
[4:53] decisions and make changes and take control with the mechanical modules on
[4:57] control with the mechanical modules on
[4:57] control with the mechanical modules on the robot. And that's really
[4:59] the robot. And that's really
[4:59] the robot. And that's really challenging. And so, uh, on my end, like
[5:01] challenging. And so, uh, on my end, like
[5:01] challenging. And so, uh, on my end, like I've got multiple tables of, uh,
[5:05] I've got multiple tables of, uh,
[5:05] I've got multiple tables of, uh, computing this. For example, the the
[5:08] computing this. For example, the the
[5:08] computing this. For example, the the center distance will have to be changed
[5:10] center distance will have to be changed
[5:10] center distance will have to be changed if you swap parts between the motor
[5:13] if you swap parts between the motor
[5:13] if you swap parts between the motor driving on one side and the the wheel
[5:16] driving on one side and the the wheel
[5:16] driving on one side and the the wheel pulley on the other side. And we oh it
[5:21] pulley on the other side. And we oh it
[5:21] pulley on the other side. And we oh it it's um to make the decision once is a
[5:24] it's um to make the decision once is a
[5:24] it's um to make the decision once is a simple calculation for a mechanically ch
[5:27] simple calculation for a mechanically ch
[5:27] simple calculation for a mechanically ch trained person and it can be really
[5:29] trained person and it can be really
[5:29] trained person and it can be really difficult to try to um explain that to a
[5:32] difficult to try to um explain that to a
[5:32] difficult to try to um explain that to a person outside of mechanical engineering
[5:34] person outside of mechanical engineering
[5:34] person outside of mechanical engineering and the reason is we have our our
[5:37] and the reason is we have our our
[5:37] and the reason is we have our our theoretical calculations that include
[5:39] theoretical calculations that include
[5:39] theoretical calculations that include like a a pitch circumference of a given
[5:43] like a a pitch circumference of a given
[5:43] like a a pitch circumference of a given pulley but that's a that's in theory and
[5:46] pulley but that's a that's in theory and
[5:46] pulley but that's a that's in theory and that's in between somewhere or the the
[5:48] that's in between somewhere or the the
[5:48] that's in between somewhere or the the outside thickness of the belt and the
[5:50] outside thickness of the belt and the
[5:50] outside thickness of the belt and the inside engagement of each of the teeth,
[5:53] inside engagement of each of the teeth,
[5:53] inside engagement of each of the teeth, the the positive insertion towards that
[5:56] the the positive insertion towards that
[5:56] the the positive insertion towards that center. Anyway, forgetting all that now
[5:59] center. Anyway, forgetting all that now
[5:59] center. Anyway, forgetting all that now I have a student right now who is Okay,
[6:02] I have a student right now who is Okay,
[6:02] I have a student right now who is Okay, my my chat's open here and here's a
[6:04] my my chat's open here and here's a
[6:04] my my chat's open here and here's a photo. She has printed out a new variety
[6:06] photo. She has printed out a new variety
[6:06] photo. She has printed out a new variety of the the wheel pulley and purchased an
[6:10] of the the wheel pulley and purchased an
[6:10] of the the wheel pulley and purchased an off-the-shelf um motor pulley and a new
[6:14] off-the-shelf um motor pulley and a new
[6:14] off-the-shelf um motor pulley and a new the new belt that we actually have
[6:15] the new belt that we actually have
[6:15] the new belt that we actually have wanted for some time. The narrower,
[6:18] wanted for some time. The narrower,
[6:18] wanted for some time. The narrower, thinner, but still very very strong um
[6:21] thinner, but still very very strong um
[6:21] thinner, but still very very strong um uh GT2 shaped pulley, smaller, finer uh
[6:25] uh GT2 shaped pulley, smaller, finer uh
[6:25] uh GT2 shaped pulley, smaller, finer uh teeth. Okay, now she's needing to modify
[6:28] teeth. Okay, now she's needing to modify
[6:28] teeth. Okay, now she's needing to modify this uh drivetrain uh main 3D bracket
[6:32] this uh drivetrain uh main 3D bracket
[6:32] this uh drivetrain uh main 3D bracket and to I'm trying to help her out
[6:35] and to I'm trying to help her out
[6:35] and to I'm trying to help her out without doing that uh redesign myself
[6:38] without doing that uh redesign myself
[6:38] without doing that uh redesign myself because that's the proof that our
[6:40] because that's the proof that our
[6:40] because that's the proof that our original designs have been uh made
[6:43] original designs have been uh made
[6:43] original designs have been uh made sufficiently simple enough to to have
[6:46] sufficiently simple enough to to have
[6:46] sufficiently simple enough to to have students redesign these and then they're
[6:48] students redesign these and then they're
[6:48] students redesign these and then they're learning as they go instead of just
[6:50] learning as they go instead of just
[6:50] learning as they go instead of just stumbling and waiting to for something
[6:52] stumbling and waiting to for something
[6:52] stumbling and waiting to for something to exist to solve their problem. Um, and
[6:55] to exist to solve their problem. Um, and
[6:55] to exist to solve their problem. Um, and then all right, so I'm going through the
[6:57] then all right, so I'm going through the
[6:57] then all right, so I'm going through the math of what what I can show her to help
[6:59] math of what what I can show her to help
[6:59] math of what what I can show her to help her calculate and adjust this 3D model,
[7:01] her calculate and adjust this 3D model,
[7:01] her calculate and adjust this 3D model, but there's a lot involved. Now, chat
[7:04] but there's a lot involved. Now, chat
[7:04] but there's a lot involved. Now, chat GPT5,
[7:06] GPT5,
[7:06] GPT5, we've got a whole new situation here.
[7:09] we've got a whole new situation here.
[7:09] we've got a whole new situation here. And um, this is we're one prompt into
[7:13] And um, this is we're one prompt into
[7:13] And um, this is we're one prompt into this this morning. That's the reason I I
[7:15] this this morning. That's the reason I I
[7:15] this this morning. That's the reason I I turned on this video right now.
[7:18] turned on this video right now.
[7:18] turned on this video right now. Okay, you're looking at one prompt and
[7:20] Okay, you're looking at one prompt and
[7:20] Okay, you're looking at one prompt and about two and a half minutes of
[7:22] about two and a half minutes of
[7:22] about two and a half minutes of computation from the chat GPT site. I'm
[7:24] computation from the chat GPT site. I'm
[7:24] computation from the chat GPT site. I'm paying for the GPT pro. I don't know if
[7:26] paying for the GPT pro. I don't know if
[7:26] paying for the GPT pro. I don't know if you can do this with the free version,
[7:28] you can do this with the free version,
[7:28] you can do this with the free version, but this was this is the 1990 something
[7:31] but this was this is the 1990 something
[7:31] but this was this is the 1990 something per month uh subscription and for sure
[7:34] per month uh subscription and for sure
[7:34] per month uh subscription and for sure loads and loads of free competitors will
[7:37] loads and loads of free competitors will
[7:37] loads and loads of free competitors will be out there or already are out there
[7:38] be out there or already are out there
[7:38] be out there or already are out there and stuff. Okay, it is the prompt is
[7:41] and stuff. Okay, it is the prompt is
[7:41] and stuff. Okay, it is the prompt is make a visual simulation for a system of
[7:43] make a visual simulation for a system of
[7:43] make a visual simulation for a system of two pulleys in a drive belt driving the
[7:46] two pulleys in a drive belt driving the
[7:46] two pulleys in a drive belt driving the pulleys from input to output. The belt
[7:48] pulleys from input to output. The belt
[7:48] pulleys from input to output. The belt has GT2 timing belt geometry. Make user
[7:51] has GT2 timing belt geometry. Make user
[7:51] has GT2 timing belt geometry. Make user inputs for two pulley sizes which have 2
[7:53] inputs for two pulley sizes which have 2
[7:53] inputs for two pulley sizes which have 2 mm tooth pitch and the input accepts
[7:57] mm tooth pitch and the input accepts
[7:57] mm tooth pitch and the input accepts integers for the number of teeth between
[7:59] integers for the number of teeth between
[7:59] integers for the number of teeth between 16 and 60. Then make an output indicator
[8:02] 16 and 60. Then make an output indicator
[8:02] 16 and 60. Then make an output indicator for the minimum center distance and the
[8:04] for the minimum center distance and the
[8:04] for the minimum center distance and the corresponding belt length. Give the
[8:07] corresponding belt length. Give the
[8:07] corresponding belt length. Give the simulation a rotation of one rotation
[8:09] simulation a rotation of one rotation
[8:09] simulation a rotation of one rotation per uh second on the input shaft and let
[8:12] per uh second on the input shaft and let
[8:12] per uh second on the input shaft and let the output pulley turn at the rate
[8:14] the output pulley turn at the rate
[8:14] the output pulley turn at the rate defined by the gear ratio. Put
[8:16] defined by the gear ratio. Put
[8:16] defined by the gear ratio. Put everything in a standalone HTML file.
[8:19] everything in a standalone HTML file.
[8:19] everything in a standalone HTML file. So, first off, all this code is sitting
[8:21] So, first off, all this code is sitting
[8:21] So, first off, all this code is sitting inside of one HTML file that's human
[8:24] inside of one HTML file that's human
[8:24] inside of one HTML file that's human readable. And that's crazy cuz I've
[8:28] readable. And that's crazy cuz I've
[8:28] readable. And that's crazy cuz I've never done some. Look at they even have
[8:30] never done some. Look at they even have
[8:30] never done some. Look at they even have gradient colors in the background of
[8:31] gradient colors in the background of
[8:31] gradient colors in the background of this stuff. And this is all going to be
[8:34] this stuff. And this is all going to be
[8:34] this stuff. And this is all going to be continually open sourced. Everything's
[8:35] continually open sourced. Everything's
[8:36] continually open sourced. Everything's already out there on the internet
[8:37] already out there on the internet
[8:37] already out there on the internet almost. Um, okay. And so we can see the
[8:40] almost. Um, okay. And so we can see the
[8:40] almost. Um, okay. And so we can see the rotation of this driving pulley. They
[8:43] rotation of this driving pulley. They
[8:43] rotation of this driving pulley. They indicated the belt. Uh, looks like
[8:45] indicated the belt. Uh, looks like
[8:45] indicated the belt. Uh, looks like there'll have to be an adjustment there
[8:47] there'll have to be an adjustment there
[8:47] there'll have to be an adjustment there because it's the radius is inverted on
[8:51] because it's the radius is inverted on
[8:51] because it's the radius is inverted on this section. And we have this speed of
[8:54] this section. And we have this speed of
[8:54] this section. And we have this speed of rotation and a gear ratio to begin with.
[8:58] rotation and a gear ratio to begin with.
[8:58] rotation and a gear ratio to begin with. 20 uh teeth on the input and 40. And
[9:02] 20 uh teeth on the input and 40. And
[9:02] 20 uh teeth on the input and 40. And then let's see if they have a a speed
[9:04] then let's see if they have a a speed
[9:04] then let's see if they have a a speed output speed 0.5. So the input speed was
[9:08] output speed 0.5. So the input speed was
[9:08] output speed 0.5. So the input speed was one, output speed 0.5. That's correct.
[9:12] one, output speed 0.5. That's correct.
[9:12] one, output speed 0.5. That's correct. Um, if we make this only 30.
[9:16] Um, if we make this only 30.
[9:16] Um, if we make this only 30. Oops. Oh, that's so cool. So the gear
[9:20] Oops. Oh, that's so cool. So the gear
[9:20] Oops. Oh, that's so cool. So the gear ratio is 1:3 and so we get 1/3 as the
[9:23] ratio is 1:3 and so we get 1/3 as the
[9:24] ratio is 1:3 and so we get 1/3 as the output speed. And you can see this thing
[9:26] output speed. And you can see this thing
[9:26] output speed. And you can see this thing moving slower. It's to It should take 3
[9:29] moving slower. It's to It should take 3
[9:29] moving slower. It's to It should take 3 seconds to rotate. But I think both of
[9:31] seconds to rotate. But I think both of
[9:31] seconds to rotate. But I think both of these are uh sped up. Maybe they're sped
[9:34] these are uh sped up. Maybe they're sped
[9:34] these are uh sped up. Maybe they're sped up by pi because that's definitely going
[9:37] up by pi because that's definitely going
[9:37] up by pi because that's definitely going around more than once per second. Um but
[9:40] around more than once per second. Um but
[9:40] around more than once per second. Um but oh my goodness. And so you guys have to
[9:43] oh my goodness. And so you guys have to
[9:43] oh my goodness. And so you guys have to realize we've had a thousand student
[9:46] realize we've had a thousand student
[9:46] realize we've had a thousand student projects around the world so far based
[9:49] projects around the world so far based
[9:49] projects around the world so far based on this scuttle robot uh robotic system.
[9:52] on this scuttle robot uh robotic system.
[9:52] on this scuttle robot uh robotic system. But um each of them have these stumbling
[9:55] But um each of them have these stumbling
[9:55] But um each of them have these stumbling blocks that I can see while I'm being an
[9:57] blocks that I can see while I'm being an
[9:57] blocks that I can see while I'm being an assistant to the students and helping
[9:59] assistant to the students and helping
[9:59] assistant to the students and helping them work out a new design module. Uh I
[10:03] them work out a new design module. Uh I
[10:03] them work out a new design module. Uh I can see the barriers they bump into and
[10:05] can see the barriers they bump into and
[10:05] can see the barriers they bump into and half of them are more on the mechanical
[10:07] half of them are more on the mechanical
[10:07] half of them are more on the mechanical and configuration side and half of them
[10:10] and configuration side and half of them
[10:10] and configuration side and half of them are in the software side. And so from
[10:13] are in the software side. And so from
[10:13] are in the software side. And so from the time of high school, I studied HTML
[10:15] the time of high school, I studied HTML
[10:16] the time of high school, I studied HTML and used uh a little Java stuff with
[10:19] and used uh a little Java stuff with
[10:19] and used uh a little Java stuff with Flash uh and I did um C++ in uh
[10:24] Flash uh and I did um C++ in uh
[10:24] Flash uh and I did um C++ in uh undergrad and then I further studied
[10:27] undergrad and then I further studied
[10:27] undergrad and then I further studied Python uh in the the late 201s and and
[10:33] Python uh in the the late 201s and and
[10:33] Python uh in the the late 201s and and all this effort, it's really still hard
[10:35] all this effort, it's really still hard
[10:35] all this effort, it's really still hard for me to compile it in a in an
[10:38] for me to compile it in a in an
[10:38] for me to compile it in a in an approachable way the best demonstrations
[10:41] approachable way the best demonstrations
[10:41] approachable way the best demonstrations and quickly respond to when students
[10:43] and quickly respond to when students
[10:44] and quickly respond to when students make changes to the mechanical
[10:45] make changes to the mechanical
[10:45] make changes to the mechanical configuration. How can I create uh these
[10:49] configuration. How can I create uh these
[10:49] configuration. How can I create uh these um basically demonstrations that are
[10:52] um basically demonstrations that are
[10:52] um basically demonstrations that are working without errors from which the
[10:54] working without errors from which the
[10:54] working without errors from which the students can modify things and explore
[10:57] students can modify things and explore
[10:57] students can modify things and explore and uh go back to study instead of
[10:59] and uh go back to study instead of
[10:59] and uh go back to study instead of studying Linux which is just another
[11:01] studying Linux which is just another
[11:01] studying Linux which is just another thing that I had to to learn is some
[11:04] thing that I had to to learn is some
[11:04] thing that I had to to learn is some Linux command line stuff. I in all these
[11:08] Linux command line stuff. I in all these
[11:08] Linux command line stuff. I in all these years from like 2016, I withheld from
[11:11] years from like 2016, I withheld from
[11:11] years from like 2016, I withheld from going and deep dive studying into for
[11:14] going and deep dive studying into for
[11:14] going and deep dive studying into for instance ROSS robot operating system cuz
[11:16] instance ROSS robot operating system cuz
[11:16] instance ROSS robot operating system cuz people keep making new tools and new
[11:18] people keep making new tools and new
[11:18] people keep making new tools and new languages. Uh like
[11:21] languages. Uh like
[11:21] languages. Uh like you could just spend your life
[11:22] you could just spend your life
[11:22] you could just spend your life continually learning new software
[11:24] continually learning new software
[11:24] continually learning new software languages. But the essence the the
[11:27] languages. But the essence the the
[11:27] languages. But the essence the the crucial thing has always been do I know
[11:29] crucial thing has always been do I know
[11:29] crucial thing has always been do I know how to convert a um a real life problem
[11:32] how to convert a um a real life problem
[11:32] how to convert a um a real life problem statement into a mathematical problem
[11:35] statement into a mathematical problem
[11:35] statement into a mathematical problem and then embed encode that problem in
[11:38] and then embed encode that problem in
[11:38] and then embed encode that problem in from human language into a a machine
[11:42] from human language into a a machine
[11:42] from human language into a a machine usable
[11:44] usable
[11:44] usable discrete set of of written encoded
[11:48] discrete set of of written encoded
[11:48] discrete set of of written encoded problems and it's like I have this skill
[11:51] problems and it's like I have this skill
[11:51] problems and it's like I have this skill but continually I'm always feeling
[11:53] but continually I'm always feeling
[11:53] but continually I'm always feeling behind on how do
[11:55] behind on how do
[11:55] behind on how do I need to get better at this software
[11:57] I need to get better at this software
[11:57] I need to get better at this software and this software and this software. I
[11:59] and this software and this software. I
[11:59] and this software and this software. I put much more of my effort into the the
[12:02] put much more of my effort into the the
[12:02] put much more of my effort into the the communication, creating documentation,
[12:04] communication, creating documentation,
[12:04] communication, creating documentation, creating mechanical refinements that no
[12:07] creating mechanical refinements that no
[12:07] creating mechanical refinements that no one else could do, whereas a lot of
[12:09] one else could do, whereas a lot of
[12:09] one else could do, whereas a lot of other uh users and contributors could
[12:12] other uh users and contributors could
[12:12] other uh users and contributors could create new outcomes in the software. And
[12:15] create new outcomes in the software. And
[12:15] create new outcomes in the software. And so, uh, always we were always shy of the
[12:19] so, uh, always we were always shy of the
[12:19] so, uh, always we were always shy of the types of demonstrations that I wanted to
[12:21] types of demonstrations that I wanted to
[12:21] types of demonstrations that I wanted to be able to show and tell. Like, compared
[12:23] be able to show and tell. Like, compared
[12:23] be able to show and tell. Like, compared with another system, this system can do
[12:25] with another system, this system can do
[12:25] with another system, this system can do a lot more, but we just can't always
[12:27] a lot more, but we just can't always
[12:27] a lot more, but we just can't always show it. And this is just the doors are
[12:30] show it. And this is just the doors are
[12:30] show it. And this is just the doors are being blown open now. So anyone who's a
[12:35] being blown open now. So anyone who's a
[12:35] being blown open now. So anyone who's a mechanical engineer
[12:37] mechanical engineer
[12:37] mechanical engineer basically we can solve we can deliver
[12:39] basically we can solve we can deliver
[12:39] basically we can solve we can deliver now all the exactly the lessons you need
[12:42] now all the exactly the lessons you need
[12:42] now all the exactly the lessons you need to make a new result on a robot. Um, if
[12:46] to make a new result on a robot. Um, if
[12:46] to make a new result on a robot. Um, if you're an electronics engineer, you can
[12:48] you're an electronics engineer, you can
[12:48] you're an electronics engineer, you can get the information of the mechanical
[12:50] get the information of the mechanical
[12:50] get the information of the mechanical stuff or you can get your explanations
[12:51] stuff or you can get your explanations
[12:51] stuff or you can get your explanations now. And if you're a mechanical person
[12:54] now. And if you're a mechanical person
[12:54] now. And if you're a mechanical person or an electron uh electrical engineer,
[12:57] or an electron uh electrical engineer,
[12:57] or an electron uh electrical engineer, non- electronics so much, you can get
[12:59] non- electronics so much, you can get
[12:59] non- electronics so much, you can get your, you know, which um mathematical
[13:04] your, you know, which um mathematical
[13:04] your, you know, which um mathematical uh refinements need to be put embedded
[13:06] uh refinements need to be put embedded
[13:06] uh refinements need to be put embedded into the system. Now, we can translate
[13:08] into the system. Now, we can translate
[13:08] into the system. Now, we can translate that. We can use we can use a large
[13:11] that. We can use we can use a large
[13:11] that. We can use we can use a large language model to embed our our needed
[13:16] language model to embed our our needed
[13:16] language model to embed our our needed desired uh outputs into code have it
[13:20] desired uh outputs into code have it
[13:20] desired uh outputs into code have it running and this is just amazing. I
[13:23] running and this is just amazing. I
[13:23] running and this is just amazing. I can't
[13:25] can't
[13:25] can't I put a huge and I passed up so much
[13:29] I put a huge and I passed up so much
[13:29] I put a huge and I passed up so much potential money. I could probably be
[13:31] potential money. I could probably be
[13:31] potential money. I could probably be swimming in
[13:33] swimming in
[13:33] swimming in uh millions of dollars if I had always
[13:36] uh millions of dollars if I had always
[13:36] uh millions of dollars if I had always gone for the short-term uh output like,
[13:39] gone for the short-term uh output like,
[13:39] gone for the short-term uh output like, oh, let's showcase something really
[13:43] oh, let's showcase something really
[13:43] oh, let's showcase something really really cool. And and I spend two years
[13:45] really cool. And and I spend two years
[13:45] really cool. And and I spend two years just building one one design of one type
[13:49] just building one one design of one type
[13:49] just building one one design of one type for for one type of showcase to please
[13:52] for for one type of showcase to please
[13:52] for for one type of showcase to please one group of of investor types and
[13:55] one group of of investor types and
[13:55] one group of of investor types and instead of getting this out to the
[13:57] instead of getting this out to the
[13:57] instead of getting this out to the world. And so now we're we've got our
[13:59] world. And so now we're we've got our
[13:59] world. And so now we're we've got our our people in Asia that can take this
[14:01] our people in Asia that can take this
[14:01] our people in Asia that can take this and run with it. We've got people in
[14:03] and run with it. We've got people in
[14:03] and run with it. We've got people in Nigeria that can take this and run with
[14:04] Nigeria that can take this and run with
[14:04] Nigeria that can take this and run with it. And now all we have to do is uh
[14:07] it. And now all we have to do is uh
[14:08] it. And now all we have to do is uh enhance the the communication of the
[14:09] enhance the the communication of the
[14:10] enhance the the communication of the team. And I've got extra documents that
[14:12] team. And I've got extra documents that
[14:12] team. And I've got extra documents that have always been on my uh my desktop not
[14:15] have always been on my uh my desktop not
[14:15] have always been on my uh my desktop not quite complete. I feel like I'm very
[14:17] quite complete. I feel like I'm very
[14:17] quite complete. I feel like I'm very close to I can just blast some of that
[14:19] close to I can just blast some of that
[14:19] close to I can just blast some of that stuff out onto the internet, get it
[14:20] stuff out onto the internet, get it
[14:20] stuff out onto the internet, get it stuck in a repository and users, even
[14:23] stuck in a repository and users, even
[14:23] stuck in a repository and users, even though it's incomplete, the users can
[14:25] though it's incomplete, the users can
[14:25] though it's incomplete, the users can can use the large language models to
[14:28] can use the large language models to
[14:28] can use the large language models to interpret that stuff, benefit from it.
[14:30] interpret that stuff, benefit from it.
[14:30] interpret that stuff, benefit from it. The it's populating background
[14:32] The it's populating background
[14:32] The it's populating background information about different components
[14:35] information about different components
[14:35] information about different components and the behaviors of of electronics that
[14:37] and the behaviors of of electronics that
[14:37] and the behaviors of of electronics that that are relevant to the system. I I
[14:40] that are relevant to the system. I I
[14:40] that are relevant to the system. I I can't imagine what's going to happen
[14:42] can't imagine what's going to happen
[14:42] can't imagine what's going to happen next, but uh this is really good, you
[14:44] next, but uh this is really good, you
[14:44] next, but uh this is really good, you guys. I think uh if you're an engineer
[14:47] guys. I think uh if you're an engineer
[14:47] guys. I think uh if you're an engineer like me, maybe one thing to try is come
[14:49] like me, maybe one thing to try is come
[14:49] like me, maybe one thing to try is come back to a a problem statement that you
[14:51] back to a a problem statement that you
[14:51] back to a a problem statement that you had on a mechanical system that you
[14:55] had on a mechanical system that you
[14:55] had on a mechanical system that you wanted to work with. Or if you're an
[14:56] wanted to work with. Or if you're an
[14:56] wanted to work with. Or if you're an educator, what's something that you
[14:58] educator, what's something that you
[14:58] educator, what's something that you needed to explain, but you really need a
[15:00] needed to explain, but you really need a
[15:00] needed to explain, but you really need a graphic uh a graphical moving output to
[15:04] graphic uh a graphical moving output to
[15:04] graphic uh a graphical moving output to illustrate it? Here you go. That's
[15:06] illustrate it? Here you go. That's
[15:06] illustrate it? Here you go. That's that's one prompt that probably can be
[15:08] that's one prompt that probably can be
[15:08] that's one prompt that probably can be refined and I would love to hear. Um, so
[15:11] refined and I would love to hear. Um, so
[15:11] refined and I would love to hear. Um, so obviously you guys the the simulation
[15:13] obviously you guys the the simulation
[15:13] obviously you guys the the simulation that I made, I bet any mechanical
[15:15] that I made, I bet any mechanical
[15:15] that I made, I bet any mechanical engineer could see in their heads
[15:17] engineer could see in their heads
[15:17] engineer could see in their heads exactly what I was looking for when I
[15:19] exactly what I was looking for when I
[15:19] exactly what I was looking for when I made this prompt. Uh, I'd be happy to
[15:22] made this prompt. Uh, I'd be happy to
[15:22] made this prompt. Uh, I'd be happy to hear your other prompts, but um, yeah,
[15:25] hear your other prompts, but um, yeah,
[15:25] hear your other prompts, but um, yeah, information on how
[15:27] information on how
[15:27] information on how what I what I can explore from here to
[15:29] what I what I can explore from here to
[15:30] what I what I can explore from here to make this uh, to make this better and
[15:32] make this uh, to make this better and
[15:32] make this uh, to make this better and which part of this um, ought to be
[15:34] which part of this um, ought to be
[15:34] which part of this um, ought to be documented. I could clear I could
[15:36] documented. I could clear I could
[15:36] documented. I could clear I could certainly I could grab that HTML file
[15:38] certainly I could grab that HTML file
[15:38] certainly I could grab that HTML file and I can put that in a in a notepad
[15:41] and I can put that in a in a notepad
[15:41] and I can put that in a in a notepad document and publish this along with the
[15:43] document and publish this along with the
[15:43] document and publish this along with the video. I just I didn't even know what to
[15:45] video. I just I didn't even know what to
[15:45] video. I just I didn't even know what to do next cuz everything so many new
[15:48] do next cuz everything so many new
[15:48] do next cuz everything so many new things just became possible and and
[15:51] things just became possible and and
[15:51] things just became possible and and they're in our hands now. Thanks
[15:53] they're in our hands now. Thanks
[15:53] they're in our hands now. Thanks everyone. I hope that uh hope that's
[15:55] everyone. I hope that uh hope that's
[15:55] everyone. I hope that uh hope that's exciting for you guys as it is for me.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
