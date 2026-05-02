---
title: "Fully Explained Build: Test Setup, PWM Generator, DC Motor Driver, Gearmotor"
url: "https://www.youtube.com/watch?v=iNG-G44Cd5s"
video_id: "iNG-G44Cd5s"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-07-29
duration: "41:03"
duration_sec: 2463
views: 3381
likes: 128
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/iNG-G44Cd5s/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1438
chapters_count: 0
has_description: true
has_comments: false
---

## Description

I take the simple PWM generator device and wire it up to test it out with a dual h-bridge and DC motor. These components are at the heart of every speed-controllable DC system.  Get familiar so you can design any machine you want.  I’m breaking it down into tiny steps so nobody gets left behind. 

For this build, I’ll add parts lists soon and Amazon links.  Everything is open source, always.

I hope one learner arrives here, makes a breakthrough and asks every question he has in the comments, so I can continue improving these videos.

David M

[Good Parts]
PWM Generator  https://amzn.to/4lQTbyH
Motor Driver 5A 2ch https://amzn.to/3IOHsSA
Gearmotor 200RPM https://amzn.to/3IOHsSA
Magnet Base https://amzn.to/3U47xzl
Dupont Housings kit https://amzn.to/4mfdYLT
Pinecil Iron kit https://amzn.to/3IIYiCn

## Transcript

[0:02] Hi everybody, I'm David and if you stay
[0:02] Hi everybody, I'm David and if you stay exactly where you are for the next 40
[0:03] exactly where you are for the next 40
[0:03] exactly where you are for the next 40 minutes, you're going to learn the
[0:04] minutes, you're going to learn the
[0:04] minutes, you're going to learn the following stuff with a demonstration.
[0:07] following stuff with a demonstration.
[0:07] following stuff with a demonstration. Build a test rig for electronics. Hook
[0:09] Build a test rig for electronics. Hook
[0:09] Build a test rig for electronics. Hook up a DC motor driver. Generate a PWM
[0:12] up a DC motor driver. Generate a PWM
[0:12] up a DC motor driver. Generate a PWM signal. Connect incompatible terminals
[0:14] signal. Connect incompatible terminals
[0:14] signal. Connect incompatible terminals and electronics. Solder Dupont pins on a
[0:17] and electronics. Solder Dupont pins on a
[0:17] and electronics. Solder Dupont pins on a PCB. Steal 5 volts from a 12vt circuit.
[0:20] PCB. Steal 5 volts from a 12vt circuit.
[0:20] PCB. Steal 5 volts from a 12vt circuit. Design a custom dent bracket. Sample and
[0:23] Design a custom dent bracket. Sample and
[0:23] Design a custom dent bracket. Sample and record noise from a motor. Eliminate
[0:26] record noise from a motor. Eliminate
[0:26] record noise from a motor. Eliminate loose wires from a project. check the
[0:29] loose wires from a project. check the
[0:29] loose wires from a project. check the function of a PWM signal generator and
[0:31] function of a PWM signal generator and
[0:31] function of a PWM signal generator and organize a laboratory for four times
[0:34] organize a laboratory for four times
[0:34] organize a laboratory for four times more productivity in a given project
[0:36] more productivity in a given project
[0:36] more productivity in a given project such as this.
[0:38] such as this.
[0:38] such as this. And it's all going to be delivered by a
[0:41] And it's all going to be delivered by a
[0:41] And it's all going to be delivered by a gentleman who is this close to being the
[0:43] gentleman who is this close to being the
[0:43] gentleman who is this close to being the first person in the history of our
[0:45] first person in the history of our
[0:45] first person in the history of our planet to release a full complete worked
[0:48] planet to release a full complete worked
[0:48] planet to release a full complete worked out bachelor's degree in mechanical
[0:50] out bachelor's degree in mechanical
[0:50] out bachelor's degree in mechanical engineering, which is kind of the
[0:51] engineering, which is kind of the
[0:51] engineering, which is kind of the foundation of everything around you. Um,
[0:54] foundation of everything around you. Um,
[0:54] foundation of everything around you. Um, and so if he's a little bit tired and it
[0:56] and so if he's a little bit tired and it
[0:56] and so if he's a little bit tired and it goes kind of slow, just keep in mind
[0:58] goes kind of slow, just keep in mind
[0:58] goes kind of slow, just keep in mind you're learning all of this stuff in 40
[1:00] you're learning all of this stuff in 40
[1:00] you're learning all of this stuff in 40 minutes, it's probably worth it. And
[1:02] minutes, it's probably worth it. And
[1:02] minutes, it's probably worth it. And then I'll walk you through it and it'll
[1:04] then I'll walk you through it and it'll
[1:04] then I'll walk you through it and it'll include a number of best practices that
[1:07] include a number of best practices that
[1:07] include a number of best practices that I think are not often considered. They
[1:10] I think are not often considered. They
[1:10] I think are not often considered. They overcome a dozen little problems that
[1:13] overcome a dozen little problems that
[1:13] overcome a dozen little problems that uh, riddle our students or DIY
[1:16] uh, riddle our students or DIY
[1:16] uh, riddle our students or DIY electronics projects. And so those are
[1:18] electronics projects. And so those are
[1:18] electronics projects. And so those are the
[1:20] the
[1:20] the uh standalone little advice that that
[1:23] uh standalone little advice that that
[1:23] uh standalone little advice that that just show up better if we do it in a
[1:25] just show up better if we do it in a
[1:25] just show up better if we do it in a project. So here we go. Today I'm
[1:28] project. So here we go. Today I'm
[1:28] project. So here we go. Today I'm working with this new device which is
[1:31] working with this new device which is
[1:31] working with this new device which is really built around just one chip to do
[1:33] really built around just one chip to do
[1:33] really built around just one chip to do one thing that we need and that is to
[1:35] one thing that we need and that is to
[1:35] one thing that we need and that is to generate a PWM signal but we also want
[1:39] generate a PWM signal but we also want
[1:39] generate a PWM signal but we also want to have control over the frequency of
[1:41] to have control over the frequency of
[1:41] to have control over the frequency of that signal. Um different frequencies
[1:43] that signal. Um different frequencies
[1:43] that signal. Um different frequencies could drive different kinds of motors or
[1:46] could drive different kinds of motors or
[1:46] could drive different kinds of motors or devices. um servos operate at what is it
[1:51] devices. um servos operate at what is it
[1:51] devices. um servos operate at what is it a frequency for two millisecond cycles.
[1:55] a frequency for two millisecond cycles.
[1:55] a frequency for two millisecond cycles. This one we can go higher than that
[1:57] This one we can go higher than that
[1:57] This one we can go higher than that 1,000 htz or 2,000 htz as we drive a
[2:00] 1,000 htz or 2,000 htz as we drive a
[2:00] 1,000 htz or 2,000 htz as we drive a motor a DC motor with different um
[2:05] motor a DC motor with different um
[2:05] motor a DC motor with different um frequencies
[2:06] frequencies
[2:06] frequencies then we'll discover it performs
[2:09] then we'll discover it performs
[2:09] then we'll discover it performs differently and these motors depending
[2:12] differently and these motors depending
[2:12] differently and these motors depending on the size will behave more clean
[2:14] on the size will behave more clean
[2:14] on the size will behave more clean deliver more torque generate less noise
[2:17] deliver more torque generate less noise
[2:17] deliver more torque generate less noise with a frequency that's tuned for the
[2:20] with a frequency that's tuned for the
[2:20] with a frequency that's tuned for the power we're trying to output and the
[2:21] power we're trying to output and the
[2:22] power we're trying to output and the size of the the assembly. So, if we want
[2:24] size of the the assembly. So, if we want
[2:24] size of the the assembly. So, if we want to run a lot of tests on this motor
[2:26] to run a lot of tests on this motor
[2:26] to run a lot of tests on this motor because that's in our robot, we want a
[2:28] because that's in our robot, we want a
[2:28] because that's in our robot, we want a standalone subsystem of the the whole
[2:32] standalone subsystem of the the whole
[2:32] standalone subsystem of the the whole scuttle robot. This is what we would do
[2:35] scuttle robot. This is what we would do
[2:35] scuttle robot. This is what we would do at Toyota. Like, we would grab
[2:38] at Toyota. Like, we would grab
[2:38] at Toyota. Like, we would grab the engine out of the car and set that
[2:42] the engine out of the car and set that
[2:42] the engine out of the car and set that on its own test bench and kind of build
[2:44] on its own test bench and kind of build
[2:44] on its own test bench and kind of build a room around it, instrument the parts
[2:46] a room around it, instrument the parts
[2:46] a room around it, instrument the parts we need to, and then we can look very
[2:47] we need to, and then we can look very
[2:47] we need to, and then we can look very close, isolate features, and take
[2:50] close, isolate features, and take
[2:50] close, isolate features, and take measurements.
[2:52] measurements.
[2:52] measurements. Okay. What is this device? Its brand is
[2:55] Okay. What is this device? Its brand is
[2:55] Okay. What is this device? Its brand is DRock. It's a frequency generator. I'm
[2:59] DRock. It's a frequency generator. I'm
[2:59] DRock. It's a frequency generator. I'm not sure that it's a meter as well. It
[3:02] not sure that it's a meter as well. It
[3:02] not sure that it's a meter as well. It operates from 3.3 volts to 30 volts DC.
[3:06] operates from 3.3 volts to 30 volts DC.
[3:06] operates from 3.3 volts to 30 volts DC. It takes that amplitude on the inputs
[3:09] It takes that amplitude on the inputs
[3:09] It takes that amplitude on the inputs and it also can generate the outputs
[3:11] and it also can generate the outputs
[3:11] and it also can generate the outputs with that equal amplitude to what you've
[3:15] with that equal amplitude to what you've
[3:15] with that equal amplitude to what you've sent in to the volts minus and plus that
[3:19] sent in to the volts minus and plus that
[3:19] sent in to the volts minus and plus that would equal the ground and the positive
[3:21] would equal the ground and the positive
[3:21] would equal the ground and the positive of your DC supply voltage. PWM it
[3:25] of your DC supply voltage. PWM it
[3:26] of your DC supply voltage. PWM it they've integrated ground and PWM as the
[3:29] they've integrated ground and PWM as the
[3:29] they've integrated ground and PWM as the second two terminals which tells me the
[3:32] second two terminals which tells me the
[3:32] second two terminals which tells me the pulse up and down signal will be on the
[3:36] pulse up and down signal will be on the
[3:36] pulse up and down signal will be on the fourth pin with respect to this always
[3:40] fourth pin with respect to this always
[3:40] fourth pin with respect to this always zero signal on the ground pin. Um, so we
[3:47] zero signal on the ground pin. Um, so we
[3:47] zero signal on the ground pin. Um, so we can essentially I expect we it's
[3:50] can essentially I expect we it's
[3:50] can essentially I expect we it's possible to have these the same volt
[3:52] possible to have these the same volt
[3:52] possible to have these the same volt minus and ground. Those ones can both be
[3:56] minus and ground. Those ones can both be
[3:56] minus and ground. Those ones can both be at the 0 volts level. Um, the first step
[4:00] at the 0 volts level. Um, the first step
[4:00] at the 0 volts level. Um, the first step was to build the cable because we want
[4:03] was to build the cable because we want
[4:03] was to build the cable because we want to connect it to our motor driver board.
[4:06] to connect it to our motor driver board.
[4:06] to connect it to our motor driver board. What do we need a signal generator for?
[4:10] What do we need a signal generator for?
[4:10] What do we need a signal generator for? This one is going to be the
[4:12] This one is going to be the
[4:12] This one is going to be the communicator, the command module that
[4:15] communicator, the command module that
[4:15] communicator, the command module that tells this motor driver board what to
[4:19] tells this motor driver board what to
[4:19] tells this motor driver board what to do. So, the motor driver has its power
[4:22] do. So, the motor driver has its power
[4:22] do. So, the motor driver has its power terminals or they take power in and send
[4:24] terminals or they take power in and send
[4:24] terminals or they take power in and send the power out on two different motors.
[4:27] the power out on two different motors.
[4:27] the power out on two different motors. We're just going to look at one motor
[4:28] We're just going to look at one motor
[4:28] We're just going to look at one motor right now. Um, and we are going to have
[4:32] right now. Um, and we are going to have
[4:32] right now. Um, and we are going to have signals coming in to the board. On the
[4:36] signals coming in to the board. On the
[4:36] signals coming in to the board. On the scuttle robot, we're commanding four
[4:38] scuttle robot, we're commanding four
[4:38] scuttle robot, we're commanding four signals that control two motors forwards
[4:40] signals that control two motors forwards
[4:40] signals that control two motors forwards and backwards. And we're just going to
[4:42] and backwards. And we're just going to
[4:42] and backwards. And we're just going to focus on one. So, if I take this out,
[4:47] focus on one. So, if I take this out,
[4:47] focus on one. So, if I take this out, you have the labels.
[4:50] you have the labels.
[4:50] you have the labels. Can we get a focus?
[4:53] Can we get a focus?
[4:53] Can we get a focus? Ground input 1 2 3 4 and 5 volts. So,
[4:59] Ground input 1 2 3 4 and 5 volts. So,
[4:59] Ground input 1 2 3 4 and 5 volts. So, this driver board was kind enough to
[5:02] this driver board was kind enough to
[5:02] this driver board was kind enough to offer us a 5volt output. uh given any
[5:07] offer us a 5volt output. uh given any
[5:07] offer us a 5volt output. uh given any acceptable voltage on the VCC pin. So
[5:10] acceptable voltage on the VCC pin. So
[5:10] acceptable voltage on the VCC pin. So this one red wire powers up the entire
[5:13] this one red wire powers up the entire
[5:13] this one red wire powers up the entire system this board and we can use this
[5:16] system this board and we can use this
[5:16] system this board and we can use this board to offer power out of the five
[5:19] board to offer power out of the five
[5:19] board to offer power out of the five plus pin out to an accessory. So, we're
[5:23] plus pin out to an accessory. So, we're
[5:23] plus pin out to an accessory. So, we're going to even though this is command
[5:26] going to even though this is command
[5:26] going to even though this is command controlled by the D-Rock
[5:29] controlled by the D-Rock
[5:29] controlled by the D-Rock device in my setup, the D-Rock will
[5:32] device in my setup, the D-Rock will
[5:32] device in my setup, the D-Rock will receive its power from the motor driver.
[5:35] receive its power from the motor driver.
[5:35] receive its power from the motor driver. At least that's what I hope. So, we have
[5:38] At least that's what I hope. So, we have
[5:38] At least that's what I hope. So, we have a test setup that is a signal, a motor
[5:43] a test setup that is a signal, a motor
[5:43] a test setup that is a signal, a motor driver, power coming into motor driver,
[5:45] driver, power coming into motor driver,
[5:45] driver, power coming into motor driver, and motor. That should give us control
[5:48] and motor. That should give us control
[5:48] and motor. That should give us control to make lots of variables adjust and
[5:51] to make lots of variables adjust and
[5:51] to make lots of variables adjust and measure performance. uh such as the
[5:53] measure performance. uh such as the
[5:53] measure performance. uh such as the speed of the motor. Um so
[5:57] speed of the motor. Um so
[5:57] speed of the motor. Um so right when we begin to start hooking
[5:59] right when we begin to start hooking
[5:59] right when we begin to start hooking things up is when my project differs
[6:01] things up is when my project differs
[6:01] things up is when my project differs from a lot of the student projects that
[6:03] from a lot of the student projects that
[6:03] from a lot of the student projects that are equivalent. Uh I grabbed a spare
[6:07] are equivalent. Uh I grabbed a spare
[6:08] are equivalent. Uh I grabbed a spare motor driver out of our supplies bin and
[6:11] motor driver out of our supplies bin and
[6:12] motor driver out of our supplies bin and this is instead of taking a working unit
[6:15] this is instead of taking a working unit
[6:16] this is instead of taking a working unit off of my robot. see that ultimately
[6:18] off of my robot. see that ultimately
[6:18] off of my robot. see that ultimately this is all for the the robot design
[6:21] this is all for the the robot design
[6:21] this is all for the the robot design robot calibration and then what we do is
[6:24] robot calibration and then what we do is
[6:24] robot calibration and then what we do is we print out we produce a bracket so
[6:27] we print out we produce a bracket so
[6:27] we print out we produce a bracket so that this can get held down the typical
[6:30] that this can get held down the typical
[6:30] that this can get held down the typical student project oh pretty much
[6:32] student project oh pretty much
[6:32] student project oh pretty much everybody's project that I see this will
[6:35] everybody's project that I see this will
[6:35] everybody's project that I see this will have this board sitting flat on a table
[6:39] have this board sitting flat on a table
[6:39] have this board sitting flat on a table and moving about we want to get it fixed
[6:41] and moving about we want to get it fixed
[6:41] and moving about we want to get it fixed that takes u all the potential moving
[6:45] that takes u all the potential moving
[6:46] that takes u all the potential moving and toggling of the wires and potential
[6:50] and toggling of the wires and potential
[6:50] and toggling of the wires and potential short circuits between dropping if I
[6:52] short circuits between dropping if I
[6:52] short circuits between dropping if I drop a metallic part onto my system. We
[6:56] drop a metallic part onto my system. We
[6:56] drop a metallic part onto my system. We want that avoided. We're going to get
[6:57] want that avoided. We're going to get
[6:57] want that avoided. We're going to get this off the table and we can hang it up
[7:00] this off the table and we can hang it up
[7:00] this off the table and we can hang it up on any different drail like this guy.
[7:04] on any different drail like this guy.
[7:04] on any different drail like this guy. Um, so lucky me, I already have a
[7:09] Um, so lucky me, I already have a
[7:09] Um, so lucky me, I already have a bracket designed for that. But here's
[7:12] bracket designed for that. But here's
[7:12] bracket designed for that. But here's where you can get a resource. Um, this
[7:16] where you can get a resource. Um, this
[7:16] where you can get a resource. Um, this motor driver bracket is a 3D model. It's
[7:19] motor driver bracket is a 3D model. It's
[7:19] motor driver bracket is a 3D model. It's just as it's more accessible than the
[7:21] just as it's more accessible than the
[7:21] just as it's more accessible than the other parts. You can download the model,
[7:23] other parts. You can download the model,
[7:23] other parts. You can download the model, you can print the file, and then this
[7:25] you can print the file, and then this
[7:25] you can print the file, and then this thing may not fit your uh your circuit
[7:29] thing may not fit your uh your circuit
[7:29] thing may not fit your uh your circuit board, but these four holes are the only
[7:32] board, but these four holes are the only
[7:32] board, but these four holes are the only feature that that depend on the my board
[7:37] feature that that depend on the my board
[7:37] feature that that depend on the my board that I'm testing. So, we measure these
[7:39] that I'm testing. So, we measure these
[7:40] that I'm testing. So, we measure these holes. We adjust as needed. We adjust
[7:42] holes. We adjust as needed. We adjust
[7:42] holes. We adjust as needed. We adjust these humps and the holes with them. And
[7:45] these humps and the holes with them. And
[7:45] these humps and the holes with them. And then we drive these screws through.
[7:47] then we drive these screws through.
[7:47] then we drive these screws through. Using the same bracket and the same
[7:49] Using the same bracket and the same
[7:49] Using the same bracket and the same screws, you can mount up almost any
[7:51] screws, you can mount up almost any
[7:51] screws, you can mount up almost any circuit board that you can buy out of
[7:54] circuit board that you can buy out of
[7:54] circuit board that you can buy out of the electronic source. Um, that's a
[7:57] the electronic source. Um, that's a
[7:57] the electronic source. Um, that's a parameter. The width between these and
[7:59] parameter. The width between these and
[7:59] parameter. The width between these and the height between these. You move that
[8:01] the height between these. You move that
[8:01] the height between these. You move that parameter, it updates the model. You
[8:03] parameter, it updates the model. You
[8:03] parameter, it updates the model. You print it out. Now, there's no more
[8:06] print it out. Now, there's no more
[8:06] print it out. Now, there's no more trying to figure out. This isn't about
[8:08] trying to figure out. This isn't about
[8:08] trying to figure out. This isn't about designing a bracket anymore. It's about
[8:10] designing a bracket anymore. It's about
[8:10] designing a bracket anymore. It's about just using it. Um, then we have the the
[8:14] just using it. Um, then we have the the
[8:14] just using it. Um, then we have the the power coming in. Not sure where I'm
[8:17] power coming in. Not sure where I'm
[8:17] power coming in. Not sure where I'm going to get my power in my test rig so
[8:19] going to get my power in my test rig so
[8:19] going to get my power in my test rig so far, but I use a plane wire that's 18
[8:22] far, but I use a plane wire that's 18
[8:22] far, but I use a plane wire that's 18 gauge. And I grabbed one of that already
[8:25] gauge. And I grabbed one of that already
[8:25] gauge. And I grabbed one of that already has uh from previous testing. It was
[8:28] has uh from previous testing. It was
[8:28] has uh from previous testing. It was useful to build this um the simple
[8:30] useful to build this um the simple
[8:30] useful to build this um the simple voltmeter into it. So, as soon as I'm
[8:33] voltmeter into it. So, as soon as I'm
[8:33] voltmeter into it. So, as soon as I'm powered up, I can see the voltage and
[8:35] powered up, I can see the voltage and
[8:35] powered up, I can see the voltage and I'm aware if that's deviating, if
[8:37] I'm aware if that's deviating, if
[8:37] I'm aware if that's deviating, if there's any issues, if there's um if I
[8:40] there's any issues, if there's um if I
[8:40] there's any issues, if there's um if I haven't plugged it in. Um, we start to
[8:44] haven't plugged it in. Um, we start to
[8:44] haven't plugged it in. Um, we start to build in the troubleshooting into the
[8:46] build in the troubleshooting into the
[8:46] build in the troubleshooting into the testing.
[8:48] testing.
[8:48] testing. Um, okay. To make these two talk, um, we
[8:52] Um, okay. To make these two talk, um, we
[8:52] Um, okay. To make these two talk, um, we have these are female Dupont DuPont pins
[8:56] have these are female Dupont DuPont pins
[8:56] have these are female Dupont DuPont pins soldered into the board. These Oh, let's
[8:59] soldered into the board. These Oh, let's
[9:00] soldered into the board. These Oh, let's look closer.
[9:06] These are common for loads of
[9:06] These are common for loads of electronics. And if all of our
[9:09] electronics. And if all of our
[9:09] electronics. And if all of our electronics had these pins, then we
[9:11] electronics had these pins, then we
[9:11] electronics had these pins, then we could safely just keep a stack of these
[9:15] could safely just keep a stack of these
[9:15] could safely just keep a stack of these wires,
[9:17] wires,
[9:17] wires, um, tear off the number of wires we need
[9:20] um, tear off the number of wires we need
[9:20] um, tear off the number of wires we need for our test and then have female on one
[9:24] for our test and then have female on one
[9:24] for our test and then have female on one side, female on the other side.
[9:27] side, female on the other side.
[9:27] side, female on the other side. What I did was I took a ribbon like this
[9:30] What I did was I took a ribbon like this
[9:30] What I did was I took a ribbon like this and I split it and I grabbed how many
[9:33] and I split it and I grabbed how many
[9:33] and I split it and I grabbed how many signals do I need? I need ground.
[9:37] signals do I need? I need ground.
[9:37] signals do I need? I need ground. Uh that's the reference with which the
[9:40] Uh that's the reference with which the
[9:40] Uh that's the reference with which the if I send an input signal, it's only
[9:42] if I send an input signal, it's only
[9:42] if I send an input signal, it's only measured with respect to ground. 0 volts
[9:45] measured with respect to ground. 0 volts
[9:45] measured with respect to ground. 0 volts here and some PWM here on input one. Um,
[9:49] here and some PWM here on input one. Um,
[9:49] here and some PWM here on input one. Um, I need one and two to take control of
[9:53] I need one and two to take control of
[9:53] I need one and two to take control of those so that I can deliver a full PWM
[9:56] those so that I can deliver a full PWM
[9:56] those so that I can deliver a full PWM pair. And I need this 5 volts. So,
[10:01] pair. And I need this 5 volts. So,
[10:01] pair. And I need this 5 volts. So, all I did, and I have a separate video
[10:03] all I did, and I have a separate video
[10:03] all I did, and I have a separate video for this, is that I take the individual
[10:07] for this, is that I take the individual
[10:07] for this, is that I take the individual housings off. I grab the number of wires
[10:10] housings off. I grab the number of wires
[10:10] housings off. I grab the number of wires that I need and then I set those into
[10:14] that I need and then I set those into
[10:14] that I need and then I set those into uh a six pin housing that has far far
[10:18] uh a six pin housing that has far far
[10:18] uh a six pin housing that has far far far more mechanical robustness.
[10:21] far more mechanical robustness.
[10:21] far more mechanical robustness. Um, and I configure those and I plug
[10:24] Um, and I configure those and I plug
[10:24] Um, and I configure those and I plug them in to the locations where my pins
[10:27] them in to the locations where my pins
[10:27] them in to the locations where my pins are going to go. So that looks like
[10:29] are going to go. So that looks like
[10:29] are going to go. So that looks like this.
[10:32] this.
[10:32] this. I have all this stuff to choose from,
[10:34] I have all this stuff to choose from,
[10:34] I have all this stuff to choose from, but this is absolutely maybe I have more
[10:36] but this is absolutely maybe I have more
[10:36] but this is absolutely maybe I have more stuff than you, but this is the most
[10:38] stuff than you, but this is the most
[10:38] stuff than you, but this is the most common stuff there is. Um, three pin
[10:41] common stuff there is. Um, three pin
[10:41] common stuff there is. Um, three pin housing. You could take any larger
[10:43] housing. You could take any larger
[10:43] housing. You could take any larger number and actually file it down, cut
[10:47] number and actually file it down, cut
[10:47] number and actually file it down, cut it, and then sand it smooth. And you're
[10:49] it, and then sand it smooth. And you're
[10:49] it, and then sand it smooth. And you're going to have your three pin housing. On
[10:51] going to have your three pin housing. On
[10:51] going to have your three pin housing. On one side, uh there is an arrow. That's
[10:55] one side, uh there is an arrow. That's
[10:55] one side, uh there is an arrow. That's going to indicate for us, we keep our
[10:58] going to indicate for us, we keep our
[10:58] going to indicate for us, we keep our ground in uh the position with the arrow
[11:01] ground in uh the position with the arrow
[11:01] ground in uh the position with the arrow as often as possible. So things just
[11:03] as often as possible. So things just
[11:03] as often as possible. So things just taking the form of a standard
[11:05] taking the form of a standard
[11:05] taking the form of a standard um there's a three pin. These come in
[11:09] um there's a three pin. These come in
[11:09] um there's a three pin. These come in kits, by the way, like $6 for a kit that
[11:11] kits, by the way, like $6 for a kit that
[11:11] kits, by the way, like $6 for a kit that has lots of different housings.
[11:14] has lots of different housings.
[11:14] has lots of different housings. There's the six pin six position. And
[11:17] There's the six pin six position. And
[11:18] There's the six pin six position. And they don't all need to be occupied. So
[11:19] they don't all need to be occupied. So
[11:19] they don't all need to be occupied. So we take
[11:23] we take
[11:23] we take we're reordering these. So brown is
[11:26] we're reordering these. So brown is
[11:26] we're reordering these. So brown is going to be our ground
[11:29] going to be our ground
[11:29] going to be our ground and that has our arrow.
[11:36] Orange and yellow, those are our
[11:36] Orange and yellow, those are our signals. And this is an active decision
[11:39] signals. And this is an active decision
[11:39] signals. And this is an active decision because orange and yellow are signal
[11:41] because orange and yellow are signal
[11:41] because orange and yellow are signal colors on the robot in the first place.
[11:44] colors on the robot in the first place.
[11:44] colors on the robot in the first place. Red is our 5 volts power. So, uh, orange
[11:49] Red is our 5 volts power. So, uh, orange
[11:49] Red is our 5 volts power. So, uh, orange and yellow are passing information this
[11:52] and yellow are passing information this
[11:52] and yellow are passing information this way, and brown and red are sending power
[11:55] way, and brown and red are sending power
[11:55] way, and brown and red are sending power this way. And we come over here. Oh,
[11:58] this way. And we come over here. Oh,
[11:58] this way. And we come over here. Oh, you're not supposed to see that yet.
[12:01] you're not supposed to see that yet.
[12:01] you're not supposed to see that yet. Um,
[12:03] Um,
[12:03] Um, what we might find when the students do
[12:07] what we might find when the students do
[12:07] what we might find when the students do their projects
[12:09] their projects
[12:09] their projects is, all right, they need to get it
[12:11] is, all right, they need to get it
[12:11] is, all right, they need to get it plugged in here. So, you might uh if you
[12:15] plugged in here. So, you might uh if you
[12:15] plugged in here. So, you might uh if you only have females,
[12:17] only have females,
[12:17] only have females, then you've got to produce a male end
[12:21] then you've got to produce a male end
[12:21] then you've got to produce a male end that's going to go into the screw
[12:23] that's going to go into the screw
[12:23] that's going to go into the screw terminal here. Um, but these wires are
[12:26] terminal here. Um, but these wires are
[12:26] terminal here. Um, but these wires are very fine gauge and you already start to
[12:28] very fine gauge and you already start to
[12:28] very fine gauge and you already start to have uh less robustness trying to get
[12:31] have uh less robustness trying to get
[12:31] have uh less robustness trying to get them into this this terminal. So,
[12:36] them into this this terminal. So,
[12:36] them into this this terminal. So, um okay, the first thought is to snip
[12:39] um okay, the first thought is to snip
[12:39] um okay, the first thought is to snip these free. uh strip a bit off of the
[12:42] these free. uh strip a bit off of the
[12:42] these free. uh strip a bit off of the wire and then tin it with solder. Now
[12:45] wire and then tin it with solder. Now
[12:45] wire and then tin it with solder. Now you have a rigid stick end and you can
[12:48] you have a rigid stick end and you can
[12:48] you have a rigid stick end and you can go in here. Um but I don't want to have
[12:52] go in here. Um but I don't want to have
[12:52] go in here. Um but I don't want to have my wires free and floating. I want to be
[12:54] my wires free and floating. I want to be
[12:54] my wires free and floating. I want to be able to unplug and change my mind on the
[12:57] able to unplug and change my mind on the
[12:57] able to unplug and change my mind on the setup. So, I've got
[13:11] um a choice of using these. Um these are
[13:11] um a choice of using these. Um these are usually intended to solder into a PCB
[13:13] usually intended to solder into a PCB
[13:14] usually intended to solder into a PCB with the mail end sticking up for
[13:16] with the mail end sticking up for
[13:16] with the mail end sticking up for plugging. I can snap these the size that
[13:20] plugging. I can snap these the size that
[13:20] plugging. I can snap these the size that I want. And this is the time to use
[13:24] I want. And this is the time to use
[13:24] I want. And this is the time to use the
[13:25] the
[13:26] the very fine precise um
[13:30] very fine precise um
[13:30] very fine precise um snips uh what what are we calling these
[13:33] snips uh what what are we calling these
[13:33] snips uh what what are we calling these um flush cutters because they can cut
[13:36] um flush cutters because they can cut
[13:36] um flush cutters because they can cut flush here on that surface. This is my
[13:38] flush here on that surface. This is my
[13:38] flush here on that surface. This is my favorite model and it's listed on open
[13:40] favorite model and it's listed on open
[13:40] favorite model and it's listed on open lab uh open lab project. So you can grab
[13:45] lab uh open lab project. So you can grab
[13:45] lab uh open lab project. So you can grab in between, count the number that you
[13:47] in between, count the number that you
[13:48] in between, count the number that you need on a connection and simply clip it.
[13:51] need on a connection and simply clip it.
[13:51] need on a connection and simply clip it. And then you still have fully operable
[13:54] And then you still have fully operable
[13:54] And then you still have fully operable pins, all of them.
[13:57] pins, all of them.
[13:57] pins, all of them. In this case, I want to have these pins
[14:03] In this case, I want to have these pins
[14:03] In this case, I want to have these pins uh rigid and together as a pair. I don't
[14:07] uh rigid and together as a pair. I don't
[14:07] uh rigid and together as a pair. I don't need three. I just need two. And I need
[14:08] need three. I just need two. And I need
[14:08] need three. I just need two. And I need the spacing to fit nicely and plug in
[14:11] the spacing to fit nicely and plug in
[14:11] the spacing to fit nicely and plug in here. So what I can do is can remove
[14:16] here. So what I can do is can remove
[14:16] here. So what I can do is can remove this
[14:17] this
[14:17] this middle segment that's interfering
[14:30] You can sometimes just grip it with your
[14:30] You can sometimes just grip it with your fingers. Okay. So now I have a book to
[14:33] fingers. Okay. So now I have a book to
[14:33] fingers. Okay. So now I have a book to connector. Um then I test is this long
[14:37] connector. Um then I test is this long
[14:38] connector. Um then I test is this long enough? So if I plug these ends, these
[14:41] enough? So if I plug these ends, these
[14:41] enough? So if I plug these ends, these are the proper length to fit into
[14:44] are the proper length to fit into
[14:44] are the proper length to fit into the female terminal space and grip. We
[14:48] the female terminal space and grip. We
[14:48] the female terminal space and grip. We need them to grip. So that's a little
[14:50] need them to grip. So that's a little
[14:50] need them to grip. So that's a little tug test. All right. And then is the
[14:53] tug test. All right. And then is the
[14:54] tug test. All right. And then is the short end long enough to hold inside of
[14:57] short end long enough to hold inside of
[14:57] short end long enough to hold inside of here? And so I tested that out all by
[14:59] here? And so I tested that out all by
[14:59] here? And so I tested that out all by itself. I found that if I
[15:04] itself. I found that if I
[15:04] itself. I found that if I trim down just a little bit on this
[15:06] trim down just a little bit on this
[15:06] trim down just a little bit on this midsection,
[15:08] midsection,
[15:08] midsection, that's
[15:10] that's
[15:10] that's going to no longer interfere with my the
[15:14] going to no longer interfere with my the
[15:14] going to no longer interfere with my the plastic zone here. Can we focus?
[15:24] Oh, that was the wrong button.
[15:24] Oh, that was the wrong button. That will no longer interfere with this
[15:26] That will no longer interfere with this
[15:26] That will no longer interfere with this plastic zone here and give me an extra
[15:28] plastic zone here and give me an extra
[15:28] plastic zone here and give me an extra millimeter. And we have a surefire
[15:30] millimeter. And we have a surefire
[15:30] millimeter. And we have a surefire clamping into this terminal.
[15:33] clamping into this terminal.
[15:33] clamping into this terminal. Other thing is
[15:35] Other thing is
[15:35] Other thing is um just to start working with this right
[15:38] um just to start working with this right
[15:38] um just to start working with this right away, we have this flat uh screwdriver,
[15:42] away, we have this flat uh screwdriver,
[15:42] away, we have this flat uh screwdriver, but it's actually narrower than almost
[15:45] but it's actually narrower than almost
[15:45] but it's actually narrower than almost any average flathead that you will just
[15:48] any average flathead that you will just
[15:48] any average flathead that you will just go buy uh from the store. And so we have
[15:51] go buy uh from the store. And so we have
[15:51] go buy uh from the store. And so we have the the size of this. This is ready.
[15:55] the the size of this. This is ready.
[15:55] the the size of this. This is ready. This is used so frequently that it gets
[15:57] This is used so frequently that it gets
[15:57] This is used so frequently that it gets stored
[16:00] stored
[16:00] stored up here in these locations.
[16:02] up here in these locations.
[16:02] up here in these locations. The Phillips one, Phillips Zero, and
[16:04] The Phillips one, Phillips Zero, and
[16:04] The Phillips one, Phillips Zero, and flat. Phillips zero and flat will fit
[16:06] flat. Phillips zero and flat will fit
[16:06] flat. Phillips zero and flat will fit into any of these uh housings that are
[16:11] into any of these uh housings that are
[16:11] into any of these uh housings that are recessed and then they're going to grip
[16:13] recessed and then they're going to grip
[16:13] recessed and then they're going to grip around your screwdriver. It's very often
[16:15] around your screwdriver. It's very often
[16:15] around your screwdriver. It's very often I see students uh reaching into there
[16:18] I see students uh reaching into there
[16:18] I see students uh reaching into there and they can't actually feel if their
[16:20] and they can't actually feel if their
[16:20] and they can't actually feel if their screw is engaging, the screwdriver is
[16:23] screw is engaging, the screwdriver is
[16:23] screw is engaging, the screwdriver is engaging because it it actually is just
[16:26] engaging because it it actually is just
[16:26] engaging because it it actually is just uh catching friction around the housing.
[16:29] uh catching friction around the housing.
[16:29] uh catching friction around the housing. So, we eliminate that. We use the right
[16:31] So, we eliminate that. We use the right
[16:31] So, we eliminate that. We use the right tool and you can grind down a tool if
[16:33] tool and you can grind down a tool if
[16:34] tool and you can grind down a tool if you don't already have one to make it
[16:35] you don't already have one to make it
[16:35] you don't already have one to make it nice and slim.
[16:38] nice and slim.
[16:38] nice and slim. Okay. So, we have our uh
[16:43] Okay. So, we have our uh
[16:44] Okay. So, we have our uh Okay, I found a way to make this more
[16:45] Okay, I found a way to make this more
[16:45] Okay, I found a way to make this more elegant uh just now. If we use the bent
[16:49] elegant uh just now. If we use the bent
[16:49] elegant uh just now. If we use the bent pens, these are a longer length of metal
[16:52] pens, these are a longer length of metal
[16:52] pens, these are a longer length of metal in total, but in any case, we can add
[16:56] in total, but in any case, we can add
[16:56] in total, but in any case, we can add this into a breadboard.
[16:59] this into a breadboard.
[16:59] this into a breadboard. And if we line it up, you will find
[17:02] And if we line it up, you will find
[17:02] And if we line it up, you will find three of the pins line up precisely on
[17:06] three of the pins line up precisely on
[17:06] three of the pins line up precisely on the interfering plastic. And the other
[17:09] the interfering plastic. And the other
[17:09] the interfering plastic. And the other four pins line up directly into those
[17:11] four pins line up directly into those
[17:11] four pins line up directly into those holes. So, I'm going to build my own
[17:14] holes. So, I'm going to build my own
[17:14] holes. So, I'm going to build my own adapter because that can live together
[17:16] adapter because that can live together
[17:16] adapter because that can live together with this thing. I don't ever need to
[17:17] with this thing. I don't ever need to
[17:17] with this thing. I don't ever need to build it again. And I can choose which
[17:20] build it again. And I can choose which
[17:20] build it again. And I can choose which kind of uh wires I want to plug into
[17:22] kind of uh wires I want to plug into
[17:22] kind of uh wires I want to plug into this board.
[17:25] this board.
[17:25] this board. I can take every other pin and
[17:30] I can take every other pin and
[17:30] I can take every other pin and cause it to exit
[17:37] so that we're left with four,
[17:37] so that we're left with four, but we still keep the
[17:40] but we still keep the
[17:40] but we still keep the nice accurate spacing.
[17:49] I'm squeezing on the bottom of the tip
[17:49] I'm squeezing on the bottom of the tip and the top of that plastic housing.
[18:07] Don't forget, you can do whatever you
[18:07] Don't forget, you can do whatever you want to make a working test that's more
[18:14] want to make a working test that's more
[18:14] want to make a working test that's more reliable than
[18:17] reliable than
[18:17] reliable than uh something that's just whipped
[18:18] uh something that's just whipped
[18:18] uh something that's just whipped together.
[18:20] together.
[18:20] together. We can't go that way. We can go this
[18:22] We can't go that way. We can go this
[18:22] We can't go that way. We can go this way.
[18:24] way.
[18:24] way. Okay. And then I'll check that these can
[18:27] Okay. And then I'll check that these can
[18:27] Okay. And then I'll check that these can fit in and secure with the clearances
[18:30] fit in and secure with the clearances
[18:30] fit in and secure with the clearances that I have left.
[18:32] that I have left.
[18:32] that I have left. Thanks to my fancy vice here that has
[18:36] Thanks to my fancy vice here that has
[18:36] Thanks to my fancy vice here that has rotating, I can hold this in a position
[18:38] rotating, I can hold this in a position
[18:38] rotating, I can hold this in a position that give me an accurate cut. And I'll
[18:41] that give me an accurate cut. And I'll
[18:41] that give me an accurate cut. And I'll cut along the H zone,
[18:45] cut along the H zone,
[18:45] cut along the H zone, the H row.
[18:47] the H row.
[18:47] the H row. And we're going to see if we can make
[18:49] And we're going to see if we can make
[18:49] And we're going to see if we can make this
[18:51] this
[18:51] this more pretty than it is ugly.
[19:12] Okay,
[19:12] Okay, starts out not so pretty. We'll we'll
[19:14] starts out not so pretty. We'll we'll
[19:14] starts out not so pretty. We'll we'll sand this by hand. Now, just imagine if
[19:18] sand this by hand. Now, just imagine if
[19:18] sand this by hand. Now, just imagine if I was in a lab that didn't already have
[19:19] I was in a lab that didn't already have
[19:19] I was in a lab that didn't already have these materials ready to go. This could
[19:23] these materials ready to go. This could
[19:23] these materials ready to go. This could escalate to
[19:25] escalate to
[19:25] escalate to 10 times
[19:27] 10 times
[19:27] 10 times take the whole day just to make this.
[19:30] take the whole day just to make this.
[19:30] take the whole day just to make this. Instead, it'll only take me 15 minutes
[19:32] Instead, it'll only take me 15 minutes
[19:32] Instead, it'll only take me 15 minutes and an extra 15 minutes to record the
[19:35] and an extra 15 minutes to record the
[19:35] and an extra 15 minutes to record the video.
[19:50] Okay. So, we have that true and
[19:50] Okay. So, we have that true and straight.
[19:51] straight.
[19:51] straight. And then we're going to solder our first
[19:53] And then we're going to solder our first
[19:53] And then we're going to solder our first bits or decide where the next set of
[19:55] bits or decide where the next set of
[19:55] bits or decide where the next set of pins will go. Okay. So, I need these
[19:59] pins will go. Okay. So, I need these
[19:59] pins will go. Okay. So, I need these pins to enter here.
[20:02] pins to enter here.
[20:02] pins to enter here. And I want it to go uh deep and secure.
[20:06] And I want it to go uh deep and secure.
[20:06] And I want it to go uh deep and secure. So, I'm going to take off a little bit
[20:07] So, I'm going to take off a little bit
[20:07] So, I'm going to take off a little bit of this green zone so that it can drop
[20:11] of this green zone so that it can drop
[20:11] of this green zone so that it can drop down closer.
[20:16] Three.
[20:16] Three. Four. Five.
[20:19] Four. Five.
[20:19] Four. Five. Six. Turn it around to keep the pressure
[20:22] Six. Turn it around to keep the pressure
[20:22] Six. Turn it around to keep the pressure balanced. 7. 8. 9. 10.
[20:40] We've got 80 grit paper here if you're
[20:40] We've got 80 grit paper here if you're wanting to know.
[20:43] wanting to know.
[20:43] wanting to know. But I think that's Yeah, it's labeled. I
[20:44] But I think that's Yeah, it's labeled. I
[20:44] But I think that's Yeah, it's labeled. I don't know if it's in the camera shot.
[20:54] Okay. It's a lot closer to
[20:54] Okay. It's a lot closer to uh giving me the clearance. This bottom
[20:58] uh giving me the clearance. This bottom
[20:58] uh giving me the clearance. This bottom edge was the same as the right this top
[21:00] edge was the same as the right this top
[21:00] edge was the same as the right this top right side edge previously. Um and now I
[21:05] right side edge previously. Um and now I
[21:05] right side edge previously. Um and now I want to wash all this fiberglass dust
[21:06] want to wash all this fiberglass dust
[21:06] want to wash all this fiberglass dust off my hands. And I'm going to vacuum
[21:08] off my hands. And I'm going to vacuum
[21:08] off my hands. And I'm going to vacuum that up because this this doesn't
[21:10] that up because this this doesn't
[21:10] that up because this this doesn't degrade when um when you're sanding
[21:14] degrade when um when you're sanding
[21:14] degrade when um when you're sanding something simple like this that's not
[21:16] something simple like this that's not
[21:16] something simple like this that's not full of muck. You can simply
[21:19] full of muck. You can simply
[21:19] full of muck. You can simply vacuum that out and recondition it with
[21:20] vacuum that out and recondition it with
[21:20] vacuum that out and recondition it with rubber if necessary and that lasts
[21:22] rubber if necessary and that lasts
[21:22] rubber if necessary and that lasts forever.
[21:56] [Applause]
[21:56] [Applause] You'll notice I just inadvertently built
[21:59] You'll notice I just inadvertently built
[21:59] You'll notice I just inadvertently built four stations for this whole process.
[22:01] four stations for this whole process.
[22:01] four stations for this whole process. This was the place where I'm measuring
[22:02] This was the place where I'm measuring
[22:02] This was the place where I'm measuring the electronics.
[22:05] the electronics.
[22:05] the electronics. And then I came over here and I do my
[22:07] And then I came over here and I do my
[22:07] And then I came over here and I do my cutting. I don't have to borrow tools
[22:10] cutting. I don't have to borrow tools
[22:10] cutting. I don't have to borrow tools from that side. The tools for cutting
[22:13] from that side. The tools for cutting
[22:13] from that side. The tools for cutting live here. Cool. Tools for clamping,
[22:16] live here. Cool. Tools for clamping,
[22:16] live here. Cool. Tools for clamping, etc. Some of the stuff needs to still be
[22:19] etc. Some of the stuff needs to still be
[22:19] etc. Some of the stuff needs to still be put away.
[22:20] put away.
[22:20] put away. All these live right there.
[22:28] The vacuum is available to clean up
[22:28] The vacuum is available to clean up where I am there. And this vacuum will
[22:30] where I am there. And this vacuum will
[22:30] where I am there. And this vacuum will also reach over since I needed more
[22:33] also reach over since I needed more
[22:33] also reach over since I needed more space yet to set down my my sanding
[22:36] space yet to set down my my sanding
[22:36] space yet to set down my my sanding block that's just made of a ceramic uh
[22:40] block that's just made of a ceramic uh
[22:40] block that's just made of a ceramic uh $2 ceramic tile from the hardware store.
[22:43] $2 ceramic tile from the hardware store.
[22:43] $2 ceramic tile from the hardware store. And then this was borrowed over from I
[22:47] And then this was borrowed over from I
[22:47] And then this was borrowed over from I don't know vacuum/ cutting bench and it
[22:50] don't know vacuum/ cutting bench and it
[22:50] don't know vacuum/ cutting bench and it goes back in there my parts
[22:53] goes back in there my parts
[22:54] goes back in there my parts and bring them back to stage one.
[22:58] and bring them back to stage one.
[22:58] and bring them back to stage one. So the message for academicians in this
[23:00] So the message for academicians in this
[23:00] So the message for academicians in this situation is to do a nice job of the
[23:05] situation is to do a nice job of the
[23:05] situation is to do a nice job of the very first steps of the electronics
[23:07] very first steps of the electronics
[23:08] very first steps of the electronics projects took four different stations
[23:10] projects took four different stations
[23:10] projects took four different stations for me and most of my students will just
[23:12] for me and most of my students will just
[23:12] for me and most of my students will just wind up with one station. As soon as
[23:15] wind up with one station. As soon as
[23:15] wind up with one station. As soon as they leave their their main desk where
[23:17] they leave their their main desk where
[23:17] they leave their their main desk where everything's piling up, then they're
[23:20] everything's piling up, then they're
[23:20] everything's piling up, then they're interfering with other teams and
[23:22] interfering with other teams and
[23:22] interfering with other teams and crossing paths and and trying to borrow
[23:24] crossing paths and and trying to borrow
[23:24] crossing paths and and trying to borrow tools. We need to create these stations.
[23:26] tools. We need to create these stations.
[23:26] tools. We need to create these stations. Um, we need to enhance the amount of
[23:29] Um, we need to enhance the amount of
[23:29] Um, we need to enhance the amount of space available
[23:31] space available
[23:31] space available because in this case even four students
[23:33] because in this case even four students
[23:33] because in this case even four students could be working at the same time. One
[23:35] could be working at the same time. One
[23:35] could be working at the same time. One here, one here, one here, one over
[23:39] here, one here, one here, one over
[23:39] here, one here, one here, one over there.
[23:41] there.
[23:41] there. Okay, now it's time to get ready to
[23:43] Okay, now it's time to get ready to
[23:43] Okay, now it's time to get ready to solder. And I can discard the scraps
[23:46] solder. And I can discard the scraps
[23:46] solder. And I can discard the scraps here.
[23:48] here.
[23:48] here. Um,
[23:55] P 0 flat.
[23:55] P 0 flat. This comes up here.
[23:58] This comes up here.
[23:58] This comes up here. This one can get unattached for now.
[24:07] So before all of this, I just did a
[24:07] So before all of this, I just did a general power on for my new D-Rock
[24:11] general power on for my new D-Rock
[24:11] general power on for my new D-Rock device just to make sure it does power
[24:14] device just to make sure it does power
[24:14] device just to make sure it does power on. It does function a little bit with
[24:17] on. It does function a little bit with
[24:17] on. It does function a little bit with the scrolling values using the knob. So,
[24:21] the scrolling values using the knob. So,
[24:21] the scrolling values using the knob. So, we wouldn't invest this time until
[24:23] we wouldn't invest this time until
[24:23] we wouldn't invest this time until there's a very very initial idea
[24:27] there's a very very initial idea
[24:27] there's a very very initial idea that our
[24:29] that our
[24:29] that our powering up plan is going to work.
[24:32] powering up plan is going to work.
[24:32] powering up plan is going to work. And the activity we've put into the
[24:35] And the activity we've put into the
[24:35] And the activity we've put into the video so far are just based on the how
[24:38] video so far are just based on the how
[24:38] video so far are just based on the how we're going to configure
[24:41] we're going to configure
[24:41] we're going to configure our wiring.
[24:44] our wiring.
[24:44] our wiring. Um, let's see.
[24:56] I want to grab
[24:56] I want to grab a spare container
[25:00] a spare container
[25:00] a spare container and that's where I'll drop in my parts
[25:03] and that's where I'll drop in my parts
[25:03] and that's where I'll drop in my parts not yet used for the project.
[25:35] Blue wires and brown wire get put away
[25:35] Blue wires and brown wire get put away because those are not being used.
[25:48] needle nose goes there.
[25:48] needle nose goes there. All right. This is my cable that I will
[25:51] All right. This is my cable that I will
[25:51] All right. This is my cable that I will use. This is the housing that's no
[25:53] use. This is the housing that's no
[25:53] use. This is the housing that's no longer needed. This is single pin that
[25:55] longer needed. This is single pin that
[25:55] longer needed. This is single pin that was snipped out and a piece of
[25:59] was snipped out and a piece of
[25:59] was snipped out and a piece of metal that was clung to my magnetic
[26:02] metal that was clung to my magnetic
[26:02] metal that was clung to my magnetic motor.
[26:04] motor.
[26:04] motor. Okay. Motor sits up. So, there's a tack
[26:09] Okay. Motor sits up. So, there's a tack
[26:09] Okay. Motor sits up. So, there's a tack that's convenient for a temporary
[26:12] that's convenient for a temporary
[26:12] that's convenient for a temporary holding. This is simply sticky tack
[26:16] holding. This is simply sticky tack
[26:16] holding. This is simply sticky tack that's been around for many years
[26:19] that's been around for many years
[26:19] that's been around for many years for classroom
[26:21] for classroom
[26:22] for classroom activities. And I'm going to set this
[26:24] activities. And I'm going to set this
[26:24] activities. And I'm going to set this here. Here, let's make sure our camera
[26:27] here. Here, let's make sure our camera
[26:27] here. Here, let's make sure our camera is showing what we need to show.
[26:36] I'm setting the two sets of terminals on
[26:36] I'm setting the two sets of terminals on the board
[26:38] the board
[26:38] the board and getting them
[26:42] and getting them
[26:42] and getting them to hold in place with the sticky tack.
[26:45] to hold in place with the sticky tack.
[26:46] to hold in place with the sticky tack. And that will let me solder. It sure
[26:48] And that will let me solder. It sure
[26:48] And that will let me solder. It sure doesn't help that I have a band-aid on
[26:50] doesn't help that I have a band-aid on
[26:50] doesn't help that I have a band-aid on my thumb.
[26:52] my thumb.
[26:52] my thumb. Make them aligned.
[26:57] And then I'm going to flip it upside
[26:57] And then I'm going to flip it upside down. It can rest right here.
[27:01] down. It can rest right here.
[27:01] down. It can rest right here. Okay. Today we're using this soldering
[27:04] Okay. Today we're using this soldering
[27:04] Okay. Today we're using this soldering iron called pine sill. It's already
[27:06] iron called pine sill. It's already
[27:06] iron called pine sill. It's already powered on and this button is going to
[27:08] powered on and this button is going to
[27:08] powered on and this button is going to let us heat it up. We see that's heating
[27:12] let us heat it up. We see that's heating
[27:12] let us heat it up. We see that's heating up. 70 watts are going into it. And um
[27:18] up. 70 watts are going into it. And um
[27:18] up. 70 watts are going into it. And um usually it's not super necessary, but we
[27:20] usually it's not super necessary, but we
[27:20] usually it's not super necessary, but we can add some flux to the surfaces where
[27:23] can add some flux to the surfaces where
[27:23] can add some flux to the surfaces where we want the solder to stick.
[27:27] we want the solder to stick.
[27:27] we want the solder to stick. And we can grab our flux cord solder
[27:31] And we can grab our flux cord solder
[27:31] And we can grab our flux cord solder that's about 2 mm diameter.
[27:34] that's about 2 mm diameter.
[27:34] that's about 2 mm diameter. And safety glasses belong on the face.
[27:55] Now, this is two stages for the way that
[27:55] Now, this is two stages for the way that I do this soldering.
[28:04] First stage is just to do one terminal,
[28:04] First stage is just to do one terminal, heat up the joint, and feed in some
[28:06] heat up the joint, and feed in some
[28:06] heat up the joint, and feed in some solder
[28:09] solder
[28:09] solder until the solder sits down and wets the
[28:11] until the solder sits down and wets the
[28:12] until the solder sits down and wets the surface of both
[28:15] surface of both
[28:15] surface of both pin and the board. Oh, it's moving
[28:17] pin and the board. Oh, it's moving
[28:17] pin and the board. Oh, it's moving around.
[28:19] around.
[28:20] around. The first one is a little more
[28:21] The first one is a little more
[28:21] The first one is a little more precarious than the rest. So, I'm now
[28:24] precarious than the rest. So, I'm now
[28:24] precarious than the rest. So, I'm now that's cooled down and we can remove the
[28:26] that's cooled down and we can remove the
[28:26] that's cooled down and we can remove the sticky tack and we can verify. Oh,
[28:28] sticky tack and we can verify. Oh,
[28:28] sticky tack and we can verify. Oh, that's a little bit gooey. Verify that
[28:31] that's a little bit gooey. Verify that
[28:31] that's a little bit gooey. Verify that the positions are nice and we don't need
[28:33] the positions are nice and we don't need
[28:33] the positions are nice and we don't need to bend something and adjust it.
[28:40] And they are. I can further trim the
[28:40] And they are. I can further trim the board later if I want to.
[28:43] board later if I want to.
[28:43] board later if I want to. Um, so now I want to hold that
[28:47] Um, so now I want to hold that
[28:47] Um, so now I want to hold that using a clamp.
[28:50] using a clamp.
[28:50] using a clamp. Uh, where's my clamp? Oh, here.
[29:00] Upside down is the best orientation. And
[29:00] Upside down is the best orientation. And then everything else on the orientation
[29:02] then everything else on the orientation
[29:02] then everything else on the orientation is up to
[29:04] is up to
[29:04] is up to what works best for my hands and my
[29:07] what works best for my hands and my
[29:07] what works best for my hands and my eyes.
[29:09] eyes.
[29:09] eyes. Um, let's check the frame.
[29:27] Too much zoom. No, that's better.
[29:27] Too much zoom. No, that's better. Okay,
[29:29] Okay,
[29:29] Okay, we're going to solder these four first.
[29:38] We're working at 350 degrees, but this
[29:38] We're working at 350 degrees, but this would probably run
[29:41] would probably run
[29:41] would probably run cooler. That would be fine.
[29:45] cooler. That would be fine.
[29:45] cooler. That would be fine. And we want ventilation. So, I turn on
[29:47] And we want ventilation. So, I turn on
[29:47] And we want ventilation. So, I turn on the ventilation.
[29:50] the ventilation.
[29:50] the ventilation. First row is only four pins, but the
[29:52] First row is only four pins, but the
[29:52] First row is only four pins, but the second row I'll do all uh seven pins.
[29:58] second row I'll do all uh seven pins.
[29:58] second row I'll do all uh seven pins. Then the pins are available if I want to
[30:12] It's pretty hard to get the lighting
[30:12] It's pretty hard to get the lighting clean. Oh, come on.
[30:20] Um, then I'm going to bridge these
[30:20] Um, then I'm going to bridge these terminals
[30:23] terminals
[30:23] terminals uh directly
[30:25] uh directly
[30:25] uh directly front to back.
[30:28] front to back.
[30:28] front to back. And this is a process that takes a
[30:31] And this is a process that takes a
[30:31] And this is a process that takes a little practice. So I just did that in
[30:33] little practice. So I just did that in
[30:33] little practice. So I just did that in like a second, but if you take four or
[30:36] like a second, but if you take four or
[30:36] like a second, but if you take four or five, six seconds, you're going to start
[30:37] five, six seconds, you're going to start
[30:37] five, six seconds, you're going to start heating things up. You need to stop, let
[30:40] heating things up. You need to stop, let
[30:40] heating things up. You need to stop, let it cool down, and start over so that the
[30:42] it cool down, and start over so that the
[30:42] it cool down, and start over so that the plastic
[30:43] plastic
[30:43] plastic connector
[30:45] connector
[30:45] connector modules don't uh don't melt.
[30:49] modules don't uh don't melt.
[30:49] modules don't uh don't melt. You'll see that I bridged one that I
[30:51] You'll see that I bridged one that I
[30:51] You'll see that I bridged one that I didn't intend to bridge.
[31:02] I'm cleaning my iron. Oh, this is I
[31:02] I'm cleaning my iron. Oh, this is I still don't quite have a wonderful
[31:04] still don't quite have a wonderful
[31:04] still don't quite have a wonderful filming setup for this to have my my
[31:07] filming setup for this to have my my
[31:07] filming setup for this to have my my hands where I want them, etc.
[31:20] All right, I'm bridging all kinds of
[31:20] All right, I'm bridging all kinds of stuff. I promise I'm better at this when
[31:22] stuff. I promise I'm better at this when
[31:22] stuff. I promise I'm better at this when I'm not filming. Okay. So, we just need
[31:24] I'm not filming. Okay. So, we just need
[31:24] I'm not filming. Okay. So, we just need to remove one area. I'll use the solder
[31:27] to remove one area. I'll use the solder
[31:28] to remove one area. I'll use the solder sucker.
[31:36] So, actually, I changed my mind. Um, I
[31:36] So, actually, I changed my mind. Um, I like that I've already bridged these L
[31:39] like that I've already bridged these L
[31:39] like that I've already bridged these L shapes because now I have one, two pins
[31:43] shapes because now I have one, two pins
[31:43] shapes because now I have one, two pins for each terminal except for this one,
[31:45] for each terminal except for this one,
[31:45] for each terminal except for this one, uh, available for testing or probing.
[31:48] uh, available for testing or probing.
[31:48] uh, available for testing or probing. I'll show you what I mean. PWM is the
[31:51] I'll show you what I mean. PWM is the
[31:51] I'll show you what I mean. PWM is the final pin. And now it's also going to be
[31:53] final pin. And now it's also going to be
[31:53] final pin. And now it's also going to be expressed on this pin uh next to it. And
[31:59] expressed on this pin uh next to it. And
[31:59] expressed on this pin uh next to it. And I'm gonna take my previously jerryrigged
[32:02] I'm gonna take my previously jerryrigged
[32:02] I'm gonna take my previously jerryrigged assembly out. Now I've got ground space
[32:06] assembly out. Now I've got ground space
[32:06] assembly out. Now I've got ground space power.
[32:08] power.
[32:08] power. And that belongs
[32:10] And that belongs
[32:10] And that belongs um
[32:13] um
[32:13] um V minus for ground
[32:16] V minus for ground
[32:16] V minus for ground and V+.
[32:18] and V+.
[32:18] and V+. Oh boy, there's a little snag on my
[32:21] Oh boy, there's a little snag on my
[32:21] Oh boy, there's a little snag on my housing.
[32:24] housing.
[32:24] housing. I don't like that.
[32:34] That doesn't usually happen.
[32:34] That doesn't usually happen. Okay, in any case,
[32:41] they're plugged in.
[32:41] they're plugged in. We have
[32:43] We have
[32:43] We have red at 5 volts and brown at ground.
[32:48] red at 5 volts and brown at ground.
[32:48] red at 5 volts and brown at ground. that are going to power up this board. I
[32:50] that are going to power up this board. I
[32:50] that are going to power up this board. I could begin just right here and I can
[32:53] could begin just right here and I can
[32:53] could begin just right here and I can test out if things will work. So
[32:58] test out if things will work. So
[32:58] test out if things will work. So um
[33:00] um
[33:00] um we have 5 volts down at the end.
[33:04] we have 5 volts down at the end.
[33:04] we have 5 volts down at the end. So this housing
[33:08] So this housing
[33:08] So this housing fits neatly on the whole set of pins.
[33:10] fits neatly on the whole set of pins.
[33:10] fits neatly on the whole set of pins. And then I'm going to get my power
[33:13] And then I'm going to get my power
[33:13] And then I'm going to get my power supply to activate to send voltage to my
[33:17] supply to activate to send voltage to my
[33:17] supply to activate to send voltage to my motor driver. I pulled out a piece of
[33:19] motor driver. I pulled out a piece of
[33:19] motor driver. I pulled out a piece of drail. I snapped my motor driver bracket
[33:23] drail. I snapped my motor driver bracket
[33:23] drail. I snapped my motor driver bracket onto here. And then I'm going to put I
[33:27] onto here. And then I'm going to put I
[33:27] onto here. And then I'm going to put I want my
[33:28] want my
[33:28] want my PWM generator to be on the left hand.
[33:33] PWM generator to be on the left hand.
[33:33] PWM generator to be on the left hand. So, what we'll do is grab this generic
[33:36] So, what we'll do is grab this generic
[33:36] So, what we'll do is grab this generic bracket
[33:38] bracket
[33:38] bracket and fasten that on. And then I'm going
[33:40] and fasten that on. And then I'm going
[33:40] and fasten that on. And then I'm going to just simply double stick tape that at
[33:43] to just simply double stick tape that at
[33:43] to just simply double stick tape that at least
[33:44] least
[33:44] least so we can have our starting test set up
[33:48] so we can have our starting test set up
[33:48] so we can have our starting test set up that doesn't move around. Um,
[33:53] that doesn't move around. Um,
[33:53] that doesn't move around. Um, okay. I've got this acrylic tape. It's a
[33:56] okay. I've got this acrylic tape. It's a
[33:56] okay. I've got this acrylic tape. It's a little around 2 mm thick. And then I put
[34:00] little around 2 mm thick. And then I put
[34:00] little around 2 mm thick. And then I put two strips here on the top side so that
[34:02] two strips here on the top side so that
[34:02] two strips here on the top side so that we don't impede the motion when we want
[34:04] we don't impede the motion when we want
[34:04] we don't impede the motion when we want to clamp on and off. Peel off that
[34:07] to clamp on and off. Peel off that
[34:07] to clamp on and off. Peel off that thing. And also before you peel off the
[34:10] thing. And also before you peel off the
[34:10] thing. And also before you peel off the the protective film, you want to make
[34:13] the protective film, you want to make
[34:13] the protective film, you want to make sure you've
[34:15] sure you've
[34:15] sure you've uh pushed it down eliminate air pockets
[34:18] uh pushed it down eliminate air pockets
[34:18] uh pushed it down eliminate air pockets and enhance the bond between the tape
[34:22] and enhance the bond between the tape
[34:22] and enhance the bond between the tape and my bracket.
[34:25] and my bracket.
[34:25] and my bracket. Try to get access. my oh fingernails are
[34:28] Try to get access. my oh fingernails are
[34:28] Try to get access. my oh fingernails are clipped and it's hard to get. All right,
[34:30] clipped and it's hard to get. All right,
[34:30] clipped and it's hard to get. All right, so those are ready and I want to just So
[34:33] so those are ready and I want to just So
[34:33] so those are ready and I want to just So here's the thing. I want a tape that has
[34:35] here's the thing. I want a tape that has
[34:35] here's the thing. I want a tape that has a thickness rather than a generic
[34:36] a thickness rather than a generic
[34:36] a thickness rather than a generic double-sided tape because when you uh
[34:40] double-sided tape because when you uh
[34:40] double-sided tape because when you uh contact this, it can curve whether it's
[34:43] contact this, it can curve whether it's
[34:43] contact this, it can curve whether it's pushing or pulling or whether it's
[34:45] pushing or pulling or whether it's
[34:45] pushing or pulling or whether it's relaxed, there can easily form a gap
[34:48] relaxed, there can easily form a gap
[34:48] relaxed, there can easily form a gap between this surface which is not
[34:51] between this surface which is not
[34:51] between this surface which is not perfectly flat and the next surface
[34:53] perfectly flat and the next surface
[34:53] perfectly flat and the next surface where you want to bond it. The 2
[34:56] where you want to bond it. The 2
[34:56] where you want to bond it. The 2 millimeter thickness lets me bond this
[34:59] millimeter thickness lets me bond this
[34:59] millimeter thickness lets me bond this in a way that it grabs hold even uh it
[35:03] in a way that it grabs hold even uh it
[35:03] in a way that it grabs hold even uh it conforms to whatever curve I've got on
[35:07] conforms to whatever curve I've got on
[35:07] conforms to whatever curve I've got on the back of this meter. And then that
[35:09] the back of this meter. And then that
[35:09] the back of this meter. And then that tape is still definitely removable.
[35:11] tape is still definitely removable.
[35:12] tape is still definitely removable. That's pretty simple. All right. So
[35:16] That's pretty simple. All right. So
[35:16] That's pretty simple. All right. So we have a cable that's going to come
[35:19] we have a cable that's going to come
[35:19] we have a cable that's going to come over towards V minus as the first pin
[35:23] over towards V minus as the first pin
[35:23] over towards V minus as the first pin towards the right hand and I go brown
[35:27] towards the right hand and I go brown
[35:27] towards the right hand and I go brown connects to that and then V+ voltage
[35:30] connects to that and then V+ voltage
[35:30] connects to that and then V+ voltage input a red. Okay. And my signals if I
[35:35] input a red. Okay. And my signals if I
[35:35] input a red. Okay. And my signals if I plug it in wrong I can reverse it later.
[35:38] plug it in wrong I can reverse it later.
[35:38] plug it in wrong I can reverse it later. No harm.
[35:47] Okay, signal is plugged in.
[35:47] Okay, signal is plugged in. Uh, and if one of our, so when
[35:50] Uh, and if one of our, so when
[35:50] Uh, and if one of our, so when pulsewidth sends a high value, it will
[35:55] pulsewidth sends a high value, it will
[35:55] pulsewidth sends a high value, it will only be on one of these two pins. And we
[35:57] only be on one of these two pins. And we
[35:57] only be on one of these two pins. And we want I want that to be on input two.
[36:01] want I want that to be on input two.
[36:01] want I want that to be on input two. So that's yellow. And that gives our our
[36:04] So that's yellow. And that gives our our
[36:04] So that's yellow. And that gives our our second input here on the sensor. Now, I
[36:08] second input here on the sensor. Now, I
[36:08] second input here on the sensor. Now, I could use any DC power supply to plug in
[36:11] could use any DC power supply to plug in
[36:11] could use any DC power supply to plug in here. But you can see I've switched the
[36:13] here. But you can see I've switched the
[36:13] here. But you can see I've switched the cable because this cable has my um my
[36:17] cable because this cable has my um my
[36:17] cable because this cable has my um my Anderson connector for the scuttle
[36:19] Anderson connector for the scuttle
[36:19] Anderson connector for the scuttle battery. And that gives me the
[36:21] battery. And that gives me the
[36:21] battery. And that gives me the portability that I'm wishing for. And
[36:23] portability that I'm wishing for. And
[36:23] portability that I'm wishing for. And this is the same voltage we run
[36:25] this is the same voltage we run
[36:25] this is the same voltage we run ordinarily on the scuttle robot with
[36:27] ordinarily on the scuttle robot with
[36:27] ordinarily on the scuttle robot with this motor driver. If I power on the
[36:30] this motor driver. If I power on the
[36:30] this motor driver. If I power on the battery, we power on the motor driver.
[36:32] battery, we power on the motor driver.
[36:32] battery, we power on the motor driver. and our 5 volts apparently is going out
[36:35] and our 5 volts apparently is going out
[36:35] and our 5 volts apparently is going out to our uh frequency generator PWM
[36:39] to our uh frequency generator PWM
[36:39] to our uh frequency generator PWM generator. Um
[36:42] generator. Um
[36:42] generator. Um it looks like it recalled the value from
[36:45] it looks like it recalled the value from
[36:45] it looks like it recalled the value from when I played with it earlier. If I
[36:48] when I played with it earlier. If I
[36:48] when I played with it earlier. If I start to press these buttons, I'm still
[36:50] start to press these buttons, I'm still
[36:50] start to press these buttons, I'm still learning how this device works. So
[36:52] learning how this device works. So
[36:52] learning how this device works. So there's my percentage.
[36:54] there's my percentage.
[36:54] there's my percentage. We're working at 2.7
[36:58] We're working at 2.7
[36:58] We're working at 2.7 kilhertz,
[36:59] kilhertz,
[36:59] kilhertz, which is
[37:02] which is
[37:02] which is usually a a nice healthy range for one
[37:04] usually a a nice healthy range for one
[37:04] usually a a nice healthy range for one of these DC motors. So, let's hook up a
[37:07] of these DC motors. So, let's hook up a
[37:07] of these DC motors. So, let's hook up a motor. Okay, we have a test setup ready.
[37:10] motor. Okay, we have a test setup ready.
[37:10] motor. Okay, we have a test setup ready. And I brought over the other micro
[37:13] And I brought over the other micro
[37:14] And I brought over the other micro the other microphone. I have a solution
[37:16] the other microphone. I have a solution
[37:16] the other microphone. I have a solution for that as well. Um, I tell students
[37:19] for that as well. Um, I tell students
[37:19] for that as well. Um, I tell students that they shouldn't have motors just
[37:22] that they shouldn't have motors just
[37:22] that they shouldn't have motors just wobbling around on tables. So, this is a
[37:25] wobbling around on tables. So, this is a
[37:25] wobbling around on tables. So, this is a magnet slot that I can turn off and on,
[37:28] magnet slot that I can turn off and on,
[37:28] magnet slot that I can turn off and on, and it'll hold that motor steady.
[37:32] and it'll hold that motor steady.
[37:32] and it'll hold that motor steady. It'll also clamp my my magnetic uh
[37:35] It'll also clamp my my magnetic uh
[37:35] It'll also clamp my my magnetic uh microphone. So, we're going to power on
[37:39] microphone. So, we're going to power on
[37:39] microphone. So, we're going to power on and get it to start moving right away.
[37:42] and get it to start moving right away.
[37:42] and get it to start moving right away. And I have uh reduced the frequency down
[37:46] And I have uh reduced the frequency down
[37:46] And I have uh reduced the frequency down to 800.
[37:48] to 800.
[37:48] to 800. And I think that the selector is still
[37:52] And I think that the selector is still
[37:52] And I think that the selector is still Oh, it's on the percent. So, we're going
[37:54] Oh, it's on the percent. So, we're going
[37:54] Oh, it's on the percent. So, we're going to keep 30%.
[37:56] to keep 30%.
[37:56] to keep 30%. And I'll try to change the frequency at
[37:59] And I'll try to change the frequency at
[37:59] And I'll try to change the frequency at some low frequency that you can hear a
[38:02] some low frequency that you can hear a
[38:02] some low frequency that you can hear a much much different um sound. And
[38:07] much much different um sound. And
[38:07] much much different um sound. And actually now we've we've reduced the
[38:09] actually now we've we've reduced the
[38:09] actually now we've we've reduced the speed
[38:10] speed
[38:10] speed of this the RPM of this shaft.
[38:18] Um we may have reduced effectively the
[38:18] Um we may have reduced effectively the voltage going through these wires and to
[38:22] voltage going through these wires and to
[38:22] voltage going through these wires and to my motor simply because uh the transient
[38:25] my motor simply because uh the transient
[38:25] my motor simply because uh the transient effects of these coils this whole motor
[38:28] effects of these coils this whole motor
[38:28] effects of these coils this whole motor al together capacitance etc. um with
[38:32] al together capacitance etc. um with
[38:32] al together capacitance etc. um with fluctuating voltage we can actually lose
[38:35] fluctuating voltage we can actually lose
[38:35] fluctuating voltage we can actually lose the the effective voltage. So
[38:43] let's go to
[38:43] let's go to um back to the frequency and raise it
[38:46] um back to the frequency and raise it
[38:46] um back to the frequency and raise it up.
[38:53] You should hear I mean if the speed is
[38:53] You should hear I mean if the speed is climbing it should eventually level off.
[39:01] Now you're hearing a high pitch sound,
[39:01] Now you're hearing a high pitch sound, but that's not reflective of the motor's
[39:03] but that's not reflective of the motor's
[39:04] but that's not reflective of the motor's rotation itself.
[39:05] rotation itself.
[39:06] rotation itself. You're hearing that wind uh that's wind
[39:08] You're hearing that wind uh that's wind
[39:08] You're hearing that wind uh that's wind that's probably
[39:15] tiny oscillations
[39:15] tiny oscillations at 2 kHz
[39:17] at 2 kHz
[39:17] at 2 kHz that take place inside this housing due
[39:20] that take place inside this housing due
[39:20] that take place inside this housing due to the electromagnetic field moving. Oh,
[39:23] to the electromagnetic field moving. Oh,
[39:23] to the electromagnetic field moving. Oh, darn it.
[39:25] darn it.
[39:25] darn it. So, it looks like this goes to sleep
[39:27] So, it looks like this goes to sleep
[39:27] So, it looks like this goes to sleep after I stop pressing the buttons and
[39:29] after I stop pressing the buttons and
[39:29] after I stop pressing the buttons and then it moves the selector down to
[39:32] then it moves the selector down to
[39:32] then it moves the selector down to percentage, the duty percentage.
[39:37] percentage, the duty percentage.
[39:37] percentage, the duty percentage. So, we get a high pitch one climbing. I
[39:38] So, we get a high pitch one climbing. I
[39:38] So, we get a high pitch one climbing. I wonder if you can hear this on the
[39:40] wonder if you can hear this on the
[39:40] wonder if you can hear this on the microphone. I'll have to check it.
[39:50] The human hearing is supposed to stop
[39:50] The human hearing is supposed to stop around 20 kHz or something. Oh, come on.
[39:59] You can see this the speed isn't
[39:59] You can see this the speed isn't increasing but the sound is
[40:04] increasing but the sound is
[40:04] increasing but the sound is in pitch. There we go. Now it's
[40:06] in pitch. There we go. Now it's
[40:06] in pitch. There we go. Now it's completely quiet and this has slowed
[40:09] completely quiet and this has slowed
[40:09] completely quiet and this has slowed down. No, that's just the Yeah, that's
[40:14] down. No, that's just the Yeah, that's
[40:14] down. No, that's just the Yeah, that's interesting. 22 kHz and everything
[40:19] interesting. 22 kHz and everything
[40:19] interesting. 22 kHz and everything is quiet. Oh, and slow moving.
[40:22] is quiet. Oh, and slow moving.
[40:22] is quiet. Oh, and slow moving. Huh.
[40:23] Huh.
[40:24] Huh. So, this motor is going to have a lot
[40:25] So, this motor is going to have a lot
[40:25] So, this motor is going to have a lot different behavior.
[40:35] Come on.
[40:35] Come on. Let's wait for that to
[40:42] Well, it's a clean, smooth sound. I do
[40:42] Well, it's a clean, smooth sound. I do appreciate the sound we get at 20 kHz.
[40:46] appreciate the sound we get at 20 kHz.
[40:46] appreciate the sound we get at 20 kHz. And I bet the waveform on these wires,
[40:48] And I bet the waveform on these wires,
[40:48] And I bet the waveform on these wires, the output of this is almost pure DC at
[40:51] the output of this is almost pure DC at
[40:52] the output of this is almost pure DC at this stage.
[40:59] There you go.
[40:59] There you go. Shut it off.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
