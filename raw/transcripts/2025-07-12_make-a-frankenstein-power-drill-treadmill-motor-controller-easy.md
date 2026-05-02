---
title: "Make a Frankenstein Power Drill Treadmill Motor Controller, Easy"
url: "https://www.youtube.com/watch?v=tt13GCgdD68"
video_id: "tt13GCgdD68"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-07-12
duration: "37:20"
duration_sec: 2240
views: 2021
likes: 81
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/tt13GCgdD68/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1550
chapters_count: 0
has_description: true
has_comments: false
---

## Description

What should I title this video? I’m open to your suggestions.

It’s for learning what’s inside the modern power tools with brushed DC motors, how they work, how the controller adjusts the power from the battery to the machine.

## Transcript

[0:04] This right here is an old power drill,
[0:04] This right here is an old power drill, but it's still modern technology. And
[0:07] but it's still modern technology. And
[0:07] but it's still modern technology. And we're going to take a look at all the
[0:09] we're going to take a look at all the
[0:09] we're going to take a look at all the pieces that live inside of it, like uh
[0:13] pieces that live inside of it, like uh
[0:13] pieces that live inside of it, like uh these gears, sun and ring gears, etc. Hi
[0:17] these gears, sun and ring gears, etc. Hi
[0:17] these gears, sun and ring gears, etc. Hi everybody. I'm David Malloway. I'm a
[0:19] everybody. I'm David Malloway. I'm a
[0:19] everybody. I'm David Malloway. I'm a robotics engineer. I'd like to use this
[0:21] robotics engineer. I'd like to use this
[0:21] robotics engineer. I'd like to use this video to give you guys a walkthrough of
[0:24] video to give you guys a walkthrough of
[0:24] video to give you guys a walkthrough of the elements that live inside um some of
[0:27] the elements that live inside um some of
[0:27] the elements that live inside um some of these power tools. Well, pretty much all
[0:30] these power tools. Well, pretty much all
[0:30] these power tools. Well, pretty much all of them. Um, get you familiar with some
[0:33] of them. Um, get you familiar with some
[0:33] of them. Um, get you familiar with some of the components and then understand
[0:35] of the components and then understand
[0:35] of the components and then understand what is the value of the individual
[0:37] what is the value of the individual
[0:37] what is the value of the individual component outside of uh when it lives
[0:40] component outside of uh when it lives
[0:40] component outside of uh when it lives inside of the machine because there's a
[0:42] inside of the machine because there's a
[0:42] inside of the machine because there's a few elements that you could actually
[0:45] few elements that you could actually
[0:45] few elements that you could actually retrieve them and reuse them in other
[0:47] retrieve them and reuse them in other
[0:47] retrieve them and reuse them in other ways. Or just knowing about the the
[0:50] ways. Or just knowing about the the
[0:50] ways. Or just knowing about the the components inside of a device can help
[0:52] components inside of a device can help
[0:52] components inside of a device can help you understand the value of a tool,
[0:54] you understand the value of a tool,
[0:54] you understand the value of a tool, whether it's on sale or whether it's a
[0:56] whether it's on sale or whether it's a
[0:56] whether it's on sale or whether it's a really nice brand or a cheaper brand. to
[0:59] really nice brand or a cheaper brand. to
[0:59] really nice brand or a cheaper brand. to just read the specifications and then
[1:01] just read the specifications and then
[1:01] just read the specifications and then you have a sense of how the value of
[1:03] you have a sense of how the value of
[1:03] you have a sense of how the value of that tool compares with another. Um, and
[1:06] that tool compares with another. Um, and
[1:06] that tool compares with another. Um, and then in the context of open lab, this
[1:08] then in the context of open lab, this
[1:08] then in the context of open lab, this open-source uh lab that I'm trying to
[1:11] open-source uh lab that I'm trying to
[1:11] open-source uh lab that I'm trying to document further and further so that we
[1:13] document further and further so that we
[1:13] document further and further so that we have a a template mechatronics
[1:17] have a a template mechatronics
[1:17] have a a template mechatronics prototyping lab space that lives online
[1:19] prototyping lab space that lives online
[1:19] prototyping lab space that lives online that people can retrieve best practices
[1:22] that people can retrieve best practices
[1:22] that people can retrieve best practices and exchange new ideas to uh fill out
[1:26] and exchange new ideas to uh fill out
[1:26] and exchange new ideas to uh fill out this new industry called mechatronics
[1:28] this new industry called mechatronics
[1:28] this new industry called mechatronics engineering. Um, these components are
[1:31] engineering. Um, these components are
[1:31] engineering. Um, these components are fairly central to that. So, it's worth
[1:33] fairly central to that. So, it's worth
[1:33] fairly central to that. So, it's worth talking through it.
[1:35] talking through it.
[1:35] talking through it. Okay, a friend of mine dropped off this
[1:38] Okay, a friend of mine dropped off this
[1:38] Okay, a friend of mine dropped off this uh broken power drill, but it's only
[1:41] uh broken power drill, but it's only
[1:41] uh broken power drill, but it's only broken in one way and there are several
[1:43] broken in one way and there are several
[1:43] broken in one way and there are several modules. So, I decided we'll uh tear it
[1:46] modules. So, I decided we'll uh tear it
[1:46] modules. So, I decided we'll uh tear it apart, look inside, share that with the
[1:48] apart, look inside, share that with the
[1:48] apart, look inside, share that with the audience um so that if you've never
[1:50] audience um so that if you've never
[1:50] audience um so that if you've never taken one apart, then you can know what
[1:52] taken one apart, then you can know what
[1:52] taken one apart, then you can know what lives inside of there. And it's only a
[1:55] lives inside of there. And it's only a
[1:55] lives inside of there. And it's only a few modules. So, the way that I see
[1:57] few modules. So, the way that I see
[1:58] few modules. So, the way that I see these devices is in terms of a set of
[2:00] these devices is in terms of a set of
[2:00] these devices is in terms of a set of modules, and each one can be a higher or
[2:03] modules, and each one can be a higher or
[2:03] modules, and each one can be a higher or lower quality. Um, but this is a a
[2:06] lower quality. Um, but this is a a
[2:06] lower quality. Um, but this is a a fairly standard size of a a well-made,
[2:10] fairly standard size of a a well-made,
[2:10] fairly standard size of a a well-made, uh, brushed motor, uh, brushed style,
[2:15] uh, brushed motor, uh, brushed style,
[2:15] uh, brushed motor, uh, brushed style, um, power driver. Some people call it a
[2:18] um, power driver. Some people call it a
[2:18] um, power driver. Some people call it a drill, but this is a drill driver. Um,
[2:21] drill, but this is a drill driver. Um,
[2:21] drill, but this is a drill driver. Um, so what lives inside of here is if you
[2:24] so what lives inside of here is if you
[2:24] so what lives inside of here is if you were to open it up, you'd find a drill
[2:26] were to open it up, you'd find a drill
[2:26] were to open it up, you'd find a drill in the back. You'd find a gear train
[2:29] in the back. You'd find a gear train
[2:29] in the back. You'd find a gear train here in the middle. And
[2:37] this gear train is obviously
[2:37] this gear train is obviously disassembled. As soon as I unscrewed
[2:39] disassembled. As soon as I unscrewed
[2:39] disassembled. As soon as I unscrewed this part, it starts falling apart. And
[2:41] this part, it starts falling apart. And
[2:41] this part, it starts falling apart. And that's that's not easy to reassemble.
[2:43] that's that's not easy to reassemble.
[2:43] that's that's not easy to reassemble. So, this is just, you know, for the
[2:45] So, this is just, you know, for the
[2:45] So, this is just, you know, for the visual aid. Um, you have one simple uh
[2:50] visual aid. Um, you have one simple uh
[2:50] visual aid. Um, you have one simple uh spurgeear that's steel and these are
[2:53] spurgeear that's steel and these are
[2:54] spurgeear that's steel and these are hardened steels. This is a really nice
[2:55] hardened steels. This is a really nice
[2:55] hardened steels. This is a really nice steel that all of these are made of. And
[2:57] steel that all of these are made of. And
[2:57] steel that all of these are made of. And that's standard. If you spend more than
[2:59] that's standard. If you spend more than
[2:59] that's standard. If you spend more than $50 on any on a drill device, then
[3:02] $50 on any on a drill device, then
[3:02] $50 on any on a drill device, then you're going to get something like that
[3:04] you're going to get something like that
[3:04] you're going to get something like that with the modern brands. Um, and then uh
[3:08] with the modern brands. Um, and then uh
[3:08] with the modern brands. Um, and then uh this outputs to the gear train and you
[3:11] this outputs to the gear train and you
[3:11] this outputs to the gear train and you can select two different uh two
[3:13] can select two different uh two
[3:13] can select two different uh two different gear ratios. So, it's you've
[3:15] different gear ratios. So, it's you've
[3:15] different gear ratios. So, it's you've got a a low and high speed. I think
[3:17] got a a low and high speed. I think
[3:17] got a a low and high speed. I think there will be a familiar button.
[3:20] there will be a familiar button.
[3:20] there will be a familiar button. Everyone has maybe seen this that works
[3:22] Everyone has maybe seen this that works
[3:22] Everyone has maybe seen this that works with those uh drills. Usually, the one
[3:25] with those uh drills. Usually, the one
[3:25] with those uh drills. Usually, the one that comes with a chuck
[3:28] that comes with a chuck
[3:28] that comes with a chuck uh will have a its own mechanical gear
[3:31] uh will have a its own mechanical gear
[3:31] uh will have a its own mechanical gear selector. Um one's low speed, high
[3:34] selector. Um one's low speed, high
[3:34] selector. Um one's low speed, high torque. Two is high speed and lower
[3:38] torque. Two is high speed and lower
[3:38] torque. Two is high speed and lower torque.
[3:39] torque.
[3:39] torque. um that doesn't do any this has no
[3:42] um that doesn't do any this has no
[3:42] um that doesn't do any this has no impact on the power being sent to the DC
[3:46] impact on the power being sent to the DC
[3:46] impact on the power being sent to the DC motor uh that goes out to the shaft um
[3:50] motor uh that goes out to the shaft um
[3:50] motor uh that goes out to the shaft um to the drivetrain if you will. That is a
[3:53] to the drivetrain if you will. That is a
[3:53] to the drivetrain if you will. That is a a pure mechanical um selector. It would
[3:57] a pure mechanical um selector. It would
[3:57] a pure mechanical um selector. It would change the gear ratio within this
[4:00] change the gear ratio within this
[4:00] change the gear ratio within this gearbox. Um okay. And then you have the
[4:05] gearbox. Um okay. And then you have the
[4:05] gearbox. Um okay. And then you have the trigger module that I've already ripped
[4:07] trigger module that I've already ripped
[4:07] trigger module that I've already ripped out. trigger module is here and that's
[4:11] out. trigger module is here and that's
[4:11] out. trigger module is here and that's the special component for today where uh
[4:15] the special component for today where uh
[4:15] the special component for today where uh this is essentially an Hbridgeidge and a
[4:18] this is essentially an Hbridgeidge and a
[4:18] this is essentially an Hbridgeidge and a little bit of extra circuitry. I'll come
[4:20] little bit of extra circuitry. I'll come
[4:20] little bit of extra circuitry. I'll come back to this. So, the trigger module
[4:23] back to this. So, the trigger module
[4:23] back to this. So, the trigger module lives in there. And the trigger module
[4:25] lives in there. And the trigger module
[4:25] lives in there. And the trigger module lives in between the battery at the base
[4:30] lives in between the battery at the base
[4:30] lives in between the battery at the base and the DC motor up here. And it is
[4:33] and the DC motor up here. And it is
[4:33] and the DC motor up here. And it is sending a lower, medium, or higher a
[4:37] sending a lower, medium, or higher a
[4:37] sending a lower, medium, or higher a selectable level of power up to this
[4:41] selectable level of power up to this
[4:41] selectable level of power up to this motor. And it does that in the form of
[4:44] motor. And it does that in the form of
[4:44] motor. And it does that in the form of voltage. You have an 18vt battery.
[4:48] voltage. You have an 18vt battery.
[4:48] voltage. You have an 18vt battery. There's a circuit here. Main point is
[4:52] There's a circuit here. Main point is
[4:52] There's a circuit here. Main point is that the tabs that reach into the
[4:55] that the tabs that reach into the
[4:55] that the tabs that reach into the battery when you plug a battery in, so
[4:57] battery when you plug a battery in, so
[4:58] battery when you plug a battery in, so you have access to your full 18 volts.
[5:00] you have access to your full 18 volts.
[5:00] you have access to your full 18 volts. Uh on a fully charged battery, maybe
[5:02] Uh on a fully charged battery, maybe
[5:02] Uh on a fully charged battery, maybe 20.5 volts and a lot of amps available,
[5:06] 20.5 volts and a lot of amps available,
[5:06] 20.5 volts and a lot of amps available, but zero amps are sent until you pull
[5:08] but zero amps are sent until you pull
[5:08] but zero amps are sent until you pull this trigger. And then it starts to
[5:11] this trigger. And then it starts to
[5:11] this trigger. And then it starts to raise the voltage that's reaching these
[5:13] raise the voltage that's reaching these
[5:13] raise the voltage that's reaching these two wires. Therefore, uh raising the
[5:17] two wires. Therefore, uh raising the
[5:17] two wires. Therefore, uh raising the voltage to the motor available to the
[5:19] voltage to the motor available to the
[5:19] voltage to the motor available to the motor. And since this has a essentially
[5:23] motor. And since this has a essentially
[5:23] motor. And since this has a essentially some nominal resistance, then more and
[5:25] some nominal resistance, then more and
[5:25] some nominal resistance, then more and more voltage is going to make this
[5:27] more voltage is going to make this
[5:27] more voltage is going to make this consume more and more current and
[5:30] consume more and more current and
[5:30] consume more and more current and produce more and more power uh in the
[5:33] produce more and more power uh in the
[5:33] produce more and more power uh in the form of rotation.
[5:35] form of rotation.
[5:35] form of rotation. Okay? And so it's really that's the same
[5:39] Okay? And so it's really that's the same
[5:39] Okay? And so it's really that's the same for any of the different brands.
[5:42] for any of the different brands.
[5:42] for any of the different brands. We can for example compare this one.
[5:46] We can for example compare this one.
[5:46] We can for example compare this one. It's going to be almost exactly the
[5:48] It's going to be almost exactly the
[5:48] It's going to be almost exactly the same. And so now what as you get
[5:52] same. And so now what as you get
[5:52] same. And so now what as you get familiar and you start to work with
[5:53] familiar and you start to work with
[5:54] familiar and you start to work with these, you can start to say, "Oh, well,
[5:57] these, you can start to say, "Oh, well,
[5:57] these, you can start to say, "Oh, well, I like this style of the clutch in here,
[6:00] I like this style of the clutch in here,
[6:00] I like this style of the clutch in here, or I like this um uh I want to have to
[6:05] or I like this um uh I want to have to
[6:05] or I like this um uh I want to have to see a brushless motor that reaches this
[6:07] see a brushless motor that reaches this
[6:07] see a brushless motor that reaches this many RPMs." you can start to have uh
[6:10] many RPMs." you can start to have uh
[6:10] many RPMs." you can start to have uh your preferences for each of the modules
[6:13] your preferences for each of the modules
[6:13] your preferences for each of the modules and that preference turns into then when
[6:16] and that preference turns into then when
[6:16] and that preference turns into then when you go shopping then you can get the
[6:18] you go shopping then you can get the
[6:18] you go shopping then you can get the value. If you have the most expensive
[6:21] value. If you have the most expensive
[6:21] value. If you have the most expensive fanciest tool but it doesn't match your
[6:23] fanciest tool but it doesn't match your
[6:23] fanciest tool but it doesn't match your preferences for the jobs you need to do
[6:25] preferences for the jobs you need to do
[6:25] preferences for the jobs you need to do then of course you're losing out on
[6:27] then of course you're losing out on
[6:27] then of course you're losing out on value. So uh the thing to note about
[6:29] value. So uh the thing to note about
[6:29] value. So uh the thing to note about this one you notice it's a little bit
[6:31] this one you notice it's a little bit
[6:31] this one you notice it's a little bit smaller and it's brushless. Uh, I
[6:34] smaller and it's brushless. Uh, I
[6:34] smaller and it's brushless. Uh, I believe I upgraded a few years back and
[6:38] believe I upgraded a few years back and
[6:38] believe I upgraded a few years back and that means at the same given motor size
[6:42] that means at the same given motor size
[6:42] that means at the same given motor size can usually crank out uh a higher power.
[6:47] can usually crank out uh a higher power.
[6:47] can usually crank out uh a higher power. Um, but higher power of course that also
[6:49] Um, but higher power of course that also
[6:49] Um, but higher power of course that also means you're draining the battery
[6:50] means you're draining the battery
[6:50] means you're draining the battery faster. So again uh your preferences.
[6:54] faster. So again uh your preferences.
[6:54] faster. So again uh your preferences. Also, the brushless maybe at times um I
[6:58] Also, the brushless maybe at times um I
[6:58] Also, the brushless maybe at times um I think at the very best it's capable of a
[7:01] think at the very best it's capable of a
[7:01] think at the very best it's capable of a higher efficiency than the DC motors.
[7:05] higher efficiency than the DC motors.
[7:05] higher efficiency than the DC motors. So, um running this at mid power or full
[7:09] So, um running this at mid power or full
[7:09] So, um running this at mid power or full power uh all the way through the life of
[7:11] power uh all the way through the life of
[7:11] power uh all the way through the life of the battery is going to live longer than
[7:15] the battery is going to live longer than
[7:15] the battery is going to live longer than the equivalent model that's using the
[7:17] the equivalent model that's using the
[7:17] the equivalent model that's using the brushed motor. And it may also have a
[7:20] brushed motor. And it may also have a
[7:20] brushed motor. And it may also have a higher peak torque. Um back to the
[7:24] higher peak torque. Um back to the
[7:24] higher peak torque. Um back to the anatomy
[7:26] anatomy
[7:26] anatomy regarding what was broken in this
[7:28] regarding what was broken in this
[7:28] regarding what was broken in this assembly in this machine. What was
[7:30] assembly in this machine. What was
[7:30] assembly in this machine. What was broken when it uh reached my hands was
[7:33] broken when it uh reached my hands was
[7:33] broken when it uh reached my hands was uh something in this base circuit that
[7:36] uh something in this base circuit that
[7:36] uh something in this base circuit that communicates or interacts with the the
[7:39] communicates or interacts with the the
[7:39] communicates or interacts with the the battery that you plug in. And so the
[7:42] battery that you plug in. And so the
[7:42] battery that you plug in. And so the issue was just water damage. It was left
[7:43] issue was just water damage. It was left
[7:43] issue was just water damage. It was left out in the rain or something like that.
[7:45] out in the rain or something like that.
[7:45] out in the rain or something like that. And if you encounter water damage uh for
[7:48] And if you encounter water damage uh for
[7:48] And if you encounter water damage uh for a tool, any tool like this stuff, then
[7:51] a tool, any tool like this stuff, then
[7:51] a tool, any tool like this stuff, then it is likely that um your your chuck
[7:55] it is likely that um your your chuck
[7:56] it is likely that um your your chuck assembly will survive, your gear train
[7:58] assembly will survive, your gear train
[7:58] assembly will survive, your gear train will survive. It's very likely that your
[8:00] will survive. It's very likely that your
[8:00] will survive. It's very likely that your motor will survive just fine. uh because
[8:03] motor will survive just fine. uh because
[8:03] motor will survive just fine. uh because these tend to uh expel water. Unless it
[8:06] these tend to uh expel water. Unless it
[8:06] these tend to uh expel water. Unless it was sitting and able to corrode and and
[8:09] was sitting and able to corrode and and
[8:09] was sitting and able to corrode and and have contacts kind of uh messed up, then
[8:14] have contacts kind of uh messed up, then
[8:14] have contacts kind of uh messed up, then these DC motors usually can survive. And
[8:17] these DC motors usually can survive. And
[8:17] these DC motors usually can survive. And u and then the the
[8:20] u and then the the
[8:20] u and then the the fragile, not fragile, the more
[8:22] fragile, not fragile, the more
[8:22] fragile, not fragile, the more susceptible components would be this guy
[8:26] susceptible components would be this guy
[8:26] susceptible components would be this guy and your uh trigger assembly. And so to
[8:30] and your uh trigger assembly. And so to
[8:30] and your uh trigger assembly. And so to test whether this is still working,
[8:32] test whether this is still working,
[8:32] test whether this is still working, first we just need to know what it what
[8:34] first we just need to know what it what
[8:34] first we just need to know what it what it does. Um if I want to test if this is
[8:38] it does. Um if I want to test if this is
[8:38] it does. Um if I want to test if this is still working, I have to uh offer power
[8:42] still working, I have to uh offer power
[8:42] still working, I have to uh offer power to it and have basically the whole um
[8:45] to it and have basically the whole um
[8:45] to it and have basically the whole um the whole drill assembly ready.
[8:48] the whole drill assembly ready.
[8:48] the whole drill assembly ready. And then uh how do I communicate that?
[8:54] And then uh how do I communicate that?
[8:54] And then uh how do I communicate that? Well,
[8:55] Well,
[8:55] Well, if if you look at it as a chain of
[8:58] if if you look at it as a chain of
[8:58] if if you look at it as a chain of elements, then you can start going from
[9:01] elements, then you can start going from
[9:01] elements, then you can start going from the bottom removing elements and if you
[9:03] the bottom removing elements and if you
[9:03] the bottom removing elements and if you can uh offer a signal or a power etc to
[9:07] can uh offer a signal or a power etc to
[9:07] can uh offer a signal or a power etc to the the chain after that and th that
[9:11] the the chain after that and th that
[9:11] the the chain after that and th that subsystem works or that set of modules
[9:14] subsystem works or that set of modules
[9:14] subsystem works or that set of modules works then you know that the problem
[9:16] works then you know that the problem
[9:16] works then you know that the problem lies before that point. So I yanked this
[9:21] lies before that point. So I yanked this
[9:21] lies before that point. So I yanked this out and then I hooked up power directly
[9:23] out and then I hooked up power directly
[9:23] out and then I hooked up power directly to this which really only has four
[9:26] to this which really only has four
[9:26] to this which really only has four important terminals.
[9:28] important terminals.
[9:28] important terminals. Um so
[9:31] Um so
[9:31] Um so uh the way that we know what this even
[9:34] uh the way that we know what this even
[9:34] uh the way that we know what this even does is a set of uh I guess clues. So
[9:38] does is a set of uh I guess clues. So
[9:38] does is a set of uh I guess clues. So you can see M1 and M2
[9:42] you can see M1 and M2
[9:42] you can see M1 and M2 those two terminals were were sent out
[9:45] those two terminals were were sent out
[9:45] those two terminals were were sent out to the the motor. So this is motor one,
[9:48] to the the motor. So this is motor one,
[9:48] to the the motor. So this is motor one, motor two, and you have a uh let's see
[9:53] motor two, and you have a uh let's see
[9:53] motor two, and you have a uh let's see uh
[9:55] uh
[9:55] uh battery plus and battery minus.
[10:00] battery plus and battery minus.
[10:00] battery plus and battery minus. And those I mean I think they were
[10:03] And those I mean I think they were
[10:03] And those I mean I think they were actually colored wires when it was
[10:05] actually colored wires when it was
[10:05] actually colored wires when it was connected in the machine. So the color
[10:07] connected in the machine. So the color
[10:07] connected in the machine. So the color helps, but also plus and minus helps.
[10:09] helps, but also plus and minus helps.
[10:09] helps, but also plus and minus helps. And so why do we have motors? Why is
[10:12] And so why do we have motors? Why is
[10:12] And so why do we have motors? Why is there not a positive and negative for
[10:14] there not a positive and negative for
[10:14] there not a positive and negative for the motor? That's because it is
[10:16] the motor? That's because it is
[10:16] the motor? That's because it is reversible. So when you're using the
[10:19] reversible. So when you're using the
[10:19] reversible. So when you're using the machine, then ab above the trigger,
[10:23] machine, then ab above the trigger,
[10:23] machine, then ab above the trigger, there's this button that can click and
[10:26] there's this button that can click and
[10:26] there's this button that can click and it moves the white uh the white lever.
[10:30] it moves the white uh the white lever.
[10:30] it moves the white uh the white lever. This would be off on most drills. This
[10:33] This would be off on most drills. This
[10:33] This would be off on most drills. This is for backwards
[10:35] is for backwards
[10:36] is for backwards and this is forwards or the opposite of
[10:38] and this is forwards or the opposite of
[10:38] and this is forwards or the opposite of that. But we do know that this is going
[10:40] that. But we do know that this is going
[10:40] that. But we do know that this is going to control the rever the direction of
[10:43] to control the rever the direction of
[10:43] to control the rever the direction of our motor output. Um, and therefore
[10:48] our motor output. Um, and therefore
[10:48] our motor output. Um, and therefore there shouldn't be a positive and
[10:49] there shouldn't be a positive and
[10:49] there shouldn't be a positive and negative for the motor because you can
[10:52] negative for the motor because you can
[10:52] negative for the motor because you can switch them. Um, there must be a
[10:54] switch them. Um, there must be a
[10:54] switch them. Um, there must be a function inside of here that digitally
[10:56] function inside of here that digitally
[10:56] function inside of here that digitally indicates uh that digitally uh
[11:00] indicates uh that digitally uh
[11:00] indicates uh that digitally uh electronically controls um the path of
[11:03] electronically controls um the path of
[11:04] electronically controls um the path of the current and the voltage. And so I
[11:07] the current and the voltage. And so I
[11:07] the current and the voltage. And so I haven't even broken this open because we
[11:09] haven't even broken this open because we
[11:09] haven't even broken this open because we got it working already and I don't want
[11:11] got it working already and I don't want
[11:11] got it working already and I don't want to tamper with it any further. Then we
[11:14] to tamper with it any further. Then we
[11:14] to tamper with it any further. Then we just had one more um smaller contact. By
[11:17] just had one more um smaller contact. By
[11:17] just had one more um smaller contact. By the way, the size of the tabs and the
[11:19] the way, the size of the tabs and the
[11:19] the way, the size of the tabs and the size of the solder and the wires gives
[11:21] size of the solder and the wires gives
[11:21] size of the solder and the wires gives gives you an idea of how much uh how
[11:23] gives you an idea of how much uh how
[11:24] gives you an idea of how much uh how much current is going through a
[11:26] much current is going through a
[11:26] much current is going through a terminal. And this one was smaller. This
[11:28] terminal. And this one was smaller. This
[11:28] terminal. And this one was smaller. This is the original wire and it says L. And
[11:31] is the original wire and it says L. And
[11:31] is the original wire and it says L. And so certainly this was um sent out to the
[11:34] so certainly this was um sent out to the
[11:34] so certainly this was um sent out to the light, the LED light, which a lot of
[11:36] light, the LED light, which a lot of
[11:36] light, the LED light, which a lot of these tools will have a light like in
[11:39] these tools will have a light like in
[11:39] these tools will have a light like in this case. There's one down here. A lot
[11:42] this case. There's one down here. A lot
[11:42] this case. There's one down here. A lot of the tools have a light. And that's
[11:43] of the tools have a light. And that's
[11:44] of the tools have a light. And that's nice. It lets you know, for instance,
[11:45] nice. It lets you know, for instance,
[11:45] nice. It lets you know, for instance, before you pull the trigger all the way,
[11:47] before you pull the trigger all the way,
[11:47] before you pull the trigger all the way, you pull it just a little bit and
[11:49] you pull it just a little bit and
[11:49] you pull it just a little bit and there's a sensor in here that says we
[11:50] there's a sensor in here that says we
[11:50] there's a sensor in here that says we have some amount of trigger pull. And
[11:53] have some amount of trigger pull. And
[11:53] have some amount of trigger pull. And then it'll turn on the light. Okay,
[11:55] then it'll turn on the light. Okay,
[11:55] then it'll turn on the light. Okay, that's information for the user. It's
[11:57] that's information for the user. It's
[11:57] that's information for the user. It's pretty pretty useful. Um, so I think I
[12:00] pretty pretty useful. Um, so I think I
[12:00] pretty pretty useful. Um, so I think I tested that and it was uh with 18 volts
[12:03] tested that and it was uh with 18 volts
[12:04] tested that and it was uh with 18 volts coming into the module, we only had like
[12:07] coming into the module, we only had like
[12:07] coming into the module, we only had like uh I think 8 volts going out here. Eight
[12:11] uh I think 8 volts going out here. Eight
[12:11] uh I think 8 volts going out here. Eight positive. You could measure this with a
[12:14] positive. You could measure this with a
[12:14] positive. You could measure this with a positive probe on a multimeter compared
[12:16] positive probe on a multimeter compared
[12:16] positive probe on a multimeter compared with that ground. Treat this as ground
[12:19] with that ground. Treat this as ground
[12:19] with that ground. Treat this as ground and you'll see a positive eight or six,
[12:22] and you'll see a positive eight or six,
[12:22] and you'll see a positive eight or six, something like that around here. And
[12:24] something like that around here. And
[12:24] something like that around here. And you'll notice if you power this up, you
[12:26] you'll notice if you power this up, you
[12:26] you'll notice if you power this up, you have nothing connected out there. Um,
[12:28] have nothing connected out there. Um,
[12:28] have nothing connected out there. Um, then you can get that to modulate by you
[12:31] then you can get that to modulate by you
[12:31] then you can get that to modulate by you can turn it off entirely. When that's
[12:33] can turn it off entirely. When that's
[12:33] can turn it off entirely. When that's off, you can't get it to light up. When
[12:36] off, you can't get it to light up. When
[12:36] off, you can't get it to light up. When it's forward or reverse, then that
[12:39] it's forward or reverse, then that
[12:39] it's forward or reverse, then that voltage turns on. And then you start to
[12:40] voltage turns on. And then you start to
[12:40] voltage turns on. And then you start to understand how the module itself works.
[12:44] understand how the module itself works.
[12:44] understand how the module itself works. Okay? So DC motors because we know this
[12:46] Okay? So DC motors because we know this
[12:46] Okay? So DC motors because we know this one is a DC motor. If it didn't say it
[12:49] one is a DC motor. If it didn't say it
[12:49] one is a DC motor. If it didn't say it on the on the specifications or in the
[12:52] on the on the specifications or in the
[12:52] on the on the specifications or in the manual then you can understand by if you
[12:55] manual then you can understand by if you
[12:55] manual then you can understand by if you can detect if you can find brushes
[12:58] can detect if you can find brushes
[12:58] can detect if you can find brushes and you can measure continuity. You
[13:00] and you can measure continuity. You
[13:00] and you can measure continuity. You could talk with chatt and then ask oh
[13:02] could talk with chatt and then ask oh
[13:02] could talk with chatt and then ask oh how can I probe this motor to discover
[13:04] how can I probe this motor to discover
[13:04] how can I probe this motor to discover whether it's DC or AC there. Um, that's
[13:07] whether it's DC or AC there. Um, that's
[13:07] whether it's DC or AC there. Um, that's a pretty short and quick uh test, but um
[13:12] a pretty short and quick uh test, but um
[13:12] a pretty short and quick uh test, but um I'm familiar at this stage just by
[13:14] I'm familiar at this stage just by
[13:14] I'm familiar at this stage just by looking at it. Um, and by the way,
[13:17] looking at it. Um, and by the way,
[13:17] looking at it. Um, and by the way, there's no gearbox inside of this motor
[13:19] there's no gearbox inside of this motor
[13:19] there's no gearbox inside of this motor housing. The I can map this whole
[13:23] housing. The I can map this whole
[13:23] housing. The I can map this whole machine over to our scuttle robot. So
[13:25] machine over to our scuttle robot. So
[13:26] machine over to our scuttle robot. So the motor plus the gearbox is equivalent
[13:29] the motor plus the gearbox is equivalent
[13:29] the motor plus the gearbox is equivalent to
[13:31] to
[13:31] to our DC motor and gearbox.
[13:41] So this um you could interchange these.
[13:41] So this um you could interchange these. You could use that motor uh controller
[13:45] You could use that motor uh controller
[13:45] You could use that motor uh controller to send varial variable current to this
[13:49] to send varial variable current to this
[13:49] to send varial variable current to this very motor. I could literally solder
[13:51] very motor. I could literally solder
[13:51] very motor. I could literally solder these two wires that come out of our
[13:54] these two wires that come out of our
[13:54] these two wires that come out of our motor here over to that and plug and and
[13:58] motor here over to that and plug and and
[13:58] motor here over to that and plug and and control my motor with that device. Or I
[14:02] control my motor with that device. Or I
[14:02] control my motor with that device. Or I could use my uh DC motor control module
[14:07] could use my uh DC motor control module
[14:08] could use my uh DC motor control module here, which is called a dual Hbridge,
[14:11] here, which is called a dual Hbridge,
[14:11] here, which is called a dual Hbridge, one one Hbridgeidge for one motor. It
[14:14] one one Hbridgeidge for one motor. It
[14:14] one one Hbridgeidge for one motor. It can send um current that has a variable
[14:17] can send um current that has a variable
[14:18] can send um current that has a variable amount just like I mentioned the the
[14:20] amount just like I mentioned the the
[14:20] amount just like I mentioned the the from a low voltage to a high voltage and
[14:23] from a low voltage to a high voltage and
[14:23] from a low voltage to a high voltage and it can also invert that current so that
[14:25] it can also invert that current so that
[14:25] it can also invert that current so that your motor is going backwards. Only
[14:27] your motor is going backwards. Only
[14:27] your motor is going backwards. Only difference between this and that module
[14:29] difference between this and that module
[14:29] difference between this and that module is that one is receiving its inputs from
[14:32] is that one is receiving its inputs from
[14:32] is that one is receiving its inputs from a sensor that's probably embedded on the
[14:34] a sensor that's probably embedded on the
[14:34] a sensor that's probably embedded on the circuit board and attached to that that
[14:36] circuit board and attached to that that
[14:36] circuit board and attached to that that lever that trigger lever. And ours is
[14:39] lever that trigger lever. And ours is
[14:39] lever that trigger lever. And ours is receiving its signal from these uh these
[14:43] receiving its signal from these uh these
[14:43] receiving its signal from these uh these signal wires. Two wires for each motor
[14:47] signal wires. Two wires for each motor
[14:47] signal wires. Two wires for each motor and one ground. So you could remove
[14:50] and one ground. So you could remove
[14:50] and one ground. So you could remove everything and you'd have these four
[14:52] everything and you'd have these four
[14:52] everything and you'd have these four terminals. two powering to go in to the
[14:57] terminals. two powering to go in to the
[14:57] terminals. two powering to go in to the power and go out to the motor. That's
[14:59] power and go out to the motor. That's
[14:59] power and go out to the motor. That's the So, we send it from the battery and
[15:03] the So, we send it from the battery and
[15:03] the So, we send it from the battery and spend it on this motor driver or if you
[15:06] spend it on this motor driver or if you
[15:06] spend it on this motor driver or if you isolate the motor driver as a system,
[15:09] isolate the motor driver as a system,
[15:09] isolate the motor driver as a system, you're sending it out to the motor and
[15:12] you're sending it out to the motor and
[15:12] you're sending it out to the motor and spending it at the motor. Um, and then
[15:16] spending it at the motor. Um, and then
[15:16] spending it at the motor. Um, and then yeah, so this is a DC gear motor. We
[15:19] yeah, so this is a DC gear motor. We
[15:19] yeah, so this is a DC gear motor. We call it a gear motor because in that
[15:21] call it a gear motor because in that
[15:21] call it a gear motor because in that gray larger diameter housing, it's
[15:24] gray larger diameter housing, it's
[15:24] gray larger diameter housing, it's reducing the speed of the DC motor. Most
[15:27] reducing the speed of the DC motor. Most
[15:27] reducing the speed of the DC motor. Most DC motors uh around this size range are
[15:30] DC motors uh around this size range are
[15:30] DC motors uh around this size range are going to spin up to maybe 10,000 RPMs or
[15:34] going to spin up to maybe 10,000 RPMs or
[15:34] going to spin up to maybe 10,000 RPMs or many, many RPMs, and it's more than you
[15:36] many, many RPMs, and it's more than you
[15:36] many, many RPMs, and it's more than you want. Uh it's a higher speed and a lower
[15:42] want. Uh it's a higher speed and a lower
[15:42] want. Uh it's a higher speed and a lower torque than you usually want for most
[15:45] torque than you usually want for most
[15:45] torque than you usually want for most common appliances, whether that's a
[15:47] common appliances, whether that's a
[15:47] common appliances, whether that's a blender or a drill or um the the tool
[15:50] blender or a drill or um the the tool
[15:50] blender or a drill or um the the tool that's doing work on the order of power
[15:53] that's doing work on the order of power
[15:53] that's doing work on the order of power as a human could do work. Uh filing or
[15:57] as a human could do work. Uh filing or
[15:57] as a human could do work. Uh filing or turning or twisting
[15:59] turning or twisting
[15:59] turning or twisting that um these motors to to achieve that
[16:02] that um these motors to to achieve that
[16:02] that um these motors to to achieve that amount of power, the speed is usually
[16:04] amount of power, the speed is usually
[16:04] amount of power, the speed is usually higher. And it's not common to find a
[16:06] higher. And it's not common to find a
[16:06] higher. And it's not common to find a motor that can do a slower RPM and a
[16:11] motor that can do a slower RPM and a
[16:11] motor that can do a slower RPM and a high torque.
[16:13] high torque.
[16:13] high torque. So we we start with a a motor that's
[16:16] So we we start with a a motor that's
[16:16] So we we start with a a motor that's spinning fast and we slow it down to
[16:18] spinning fast and we slow it down to
[16:18] spinning fast and we slow it down to increase its torque. And that's just
[16:20] increase its torque. And that's just
[16:20] increase its torque. And that's just common across many many appliances. Uh
[16:24] common across many many appliances. Uh
[16:24] common across many many appliances. Uh okay.
[16:26] okay.
[16:26] okay. Okay. Now I have these two rotating
[16:28] Okay. Now I have these two rotating
[16:28] Okay. Now I have these two rotating tools. Uh rotary tools or this one may
[16:32] tools. Uh rotary tools or this one may
[16:32] tools. Uh rotary tools or this one may be referred to as a cutout tool. um to
[16:34] be referred to as a cutout tool. um to
[16:34] be referred to as a cutout tool. um to compare them in terms of engineering
[16:36] compare them in terms of engineering
[16:36] compare them in terms of engineering value. This is what I see when I'm
[16:38] value. This is what I see when I'm
[16:38] value. This is what I see when I'm looking at these. Um both of them are
[16:41] looking at these. Um both of them are
[16:41] looking at these. Um both of them are capable of carrying these uh types of
[16:44] capable of carrying these uh types of
[16:44] capable of carrying these uh types of it's a 1/8 or 3 mm shaft shaft tools
[16:50] it's a 1/8 or 3 mm shaft shaft tools
[16:50] it's a 1/8 or 3 mm shaft shaft tools like these uh gorgeous little
[16:54] like these uh gorgeous little
[16:54] like these uh gorgeous little um carbide
[16:56] um carbide
[16:56] um carbide burr tools. like this is one of my
[16:59] burr tools. like this is one of my
[16:59] burr tools. like this is one of my favorite
[17:01] favorite
[17:01] favorite filing instruments or cutting
[17:03] filing instruments or cutting
[17:03] filing instruments or cutting instruments that can cut steel. And
[17:05] instruments that can cut steel. And
[17:05] instruments that can cut steel. And there's not a lot of other uh tools in
[17:07] there's not a lot of other uh tools in
[17:07] there's not a lot of other uh tools in the lab that can do um small filing uh
[17:12] the lab that can do um small filing uh
[17:12] the lab that can do um small filing uh carefully controlled cutting of uh hard
[17:15] carefully controlled cutting of uh hard
[17:15] carefully controlled cutting of uh hard materials like steel. And so then when I
[17:19] materials like steel. And so then when I
[17:19] materials like steel. And so then when I do a job like that, I have access to
[17:22] do a job like that, I have access to
[17:22] do a job like that, I have access to this Dremel which is um one value is
[17:26] this Dremel which is um one value is
[17:26] this Dremel which is um one value is that we can control the speed and a
[17:29] that we can control the speed and a
[17:29] that we can control the speed and a variable amount.
[17:31] variable amount.
[17:32] variable amount. What I think is that we have a a fixed
[17:34] What I think is that we have a a fixed
[17:34] What I think is that we have a a fixed what four volts 3.7 volts and we're uh
[17:39] what four volts 3.7 volts and we're uh
[17:39] what four volts 3.7 volts and we're uh there's a circuit board in here that
[17:42] there's a circuit board in here that
[17:42] there's a circuit board in here that basically listens to the switches coming
[17:45] basically listens to the switches coming
[17:45] basically listens to the switches coming in and we get five discrete
[17:49] in and we get five discrete
[17:49] in and we get five discrete power levels including zero. Okay. So
[17:52] power levels including zero. Okay. So
[17:52] power levels including zero. Okay. So now we have control over the the
[17:55] now we have control over the the
[17:55] now we have control over the the rotating velocity that's that is
[17:58] rotating velocity that's that is
[17:58] rotating velocity that's that is desirable for any time when I'm using
[18:00] desirable for any time when I'm using
[18:00] desirable for any time when I'm using this tool. I also would like to have the
[18:03] this tool. I also would like to have the
[18:03] this tool. I also would like to have the ability to control its speed. It very
[18:05] ability to control its speed. It very
[18:05] ability to control its speed. It very much makes an impact on heat buildup and
[18:08] much makes an impact on heat buildup and
[18:08] much makes an impact on heat buildup and the effectiveness overall different and
[18:11] the effectiveness overall different and
[18:11] the effectiveness overall different and these are not all designed uh to go at
[18:14] these are not all designed uh to go at
[18:14] these are not all designed uh to go at the same speed. And I want a very high
[18:16] the same speed. And I want a very high
[18:16] the same speed. And I want a very high speed on the on the burr tools on steel
[18:20] speed on the on the burr tools on steel
[18:20] speed on the on the burr tools on steel and maybe half of that. say if I want
[18:23] and maybe half of that. say if I want
[18:23] and maybe half of that. say if I want 25,000 RPMs on this on steel and I I may
[18:27] 25,000 RPMs on this on steel and I I may
[18:27] 25,000 RPMs on this on steel and I I may only want 10,000 RPMs when I'm uh
[18:30] only want 10,000 RPMs when I'm uh
[18:30] only want 10,000 RPMs when I'm uh shaping plastic and then maybe less than
[18:33] shaping plastic and then maybe less than
[18:33] shaping plastic and then maybe less than that when I'm just drilling a hole. So
[18:37] that when I'm just drilling a hole. So
[18:37] that when I'm just drilling a hole. So um that that is one of the uh its value
[18:41] um that that is one of the uh its value
[18:42] um that that is one of the uh its value in terms of engineering and and work but
[18:44] in terms of engineering and and work but
[18:44] in terms of engineering and and work but and it's also a cost in terms of the
[18:47] and it's also a cost in terms of the
[18:47] and it's also a cost in terms of the tool and so you have uh my most frequent
[18:52] tool and so you have uh my most frequent
[18:52] tool and so you have uh my most frequent uh complaint with this tool is that I'm
[18:55] uh complaint with this tool is that I'm
[18:55] uh complaint with this tool is that I'm wanting more torque. So, I'm cutting a
[18:57] wanting more torque. So, I'm cutting a
[18:57] wanting more torque. So, I'm cutting a hard material or I'm using one of the
[18:59] hard material or I'm using one of the
[18:59] hard material or I'm using one of the larger bits here, then it's taking more
[19:02] larger bits here, then it's taking more
[19:02] larger bits here, then it's taking more energy, more power to do the work. And I
[19:05] energy, more power to do the work. And I
[19:05] energy, more power to do the work. And I can run out of torque. When you're going
[19:07] can run out of torque. When you're going
[19:07] can run out of torque. When you're going at a high speed, if you press hard
[19:09] at a high speed, if you press hard
[19:09] at a high speed, if you press hard against the surface, then it's going to
[19:11] against the surface, then it's going to
[19:11] against the surface, then it's going to stall. Little red light will blink and
[19:13] stall. Little red light will blink and
[19:13] stall. Little red light will blink and it just stops. And I have to bring it
[19:15] it just stops. And I have to bring it
[19:15] it just stops. And I have to bring it all the way back down to zero and spool
[19:17] all the way back down to zero and spool
[19:17] all the way back down to zero and spool it up again. versus this uh larger
[19:23] it up again. versus this uh larger
[19:23] it up again. versus this uh larger uh well, it's a larger battery and it's
[19:24] uh well, it's a larger battery and it's
[19:24] uh well, it's a larger battery and it's a larger motor with a much bigger
[19:27] a larger motor with a much bigger
[19:27] a larger motor with a much bigger torque, but I can still achieve that
[19:29] torque, but I can still achieve that
[19:29] torque, but I can still achieve that same RPM. So, the value here is I'm
[19:33] same RPM. So, the value here is I'm
[19:33] same RPM. So, the value here is I'm going to use this for heavier jobs that
[19:36] going to use this for heavier jobs that
[19:36] going to use this for heavier jobs that are going to last longer without the
[19:37] are going to last longer without the
[19:37] are going to last longer without the battery dying or what I just simply
[19:39] battery dying or what I just simply
[19:40] battery dying or what I just simply cannot achieve the work that I want to
[19:41] cannot achieve the work that I want to
[19:41] cannot achieve the work that I want to do with this smaller torque. Um,
[19:45] do with this smaller torque. Um,
[19:45] do with this smaller torque. Um, however, this one is just an onoff tool.
[19:49] however, this one is just an onoff tool.
[19:49] however, this one is just an onoff tool. Um, you've got one switch and it's a
[19:53] Um, you've got one switch and it's a
[19:53] Um, you've got one switch and it's a brushed motor as well. So, it could this
[19:56] brushed motor as well. So, it could this
[19:56] brushed motor as well. So, it could this brushed motor could have a controller
[19:58] brushed motor could have a controller
[19:58] brushed motor could have a controller that has a variable speed available, but
[20:02] that has a variable speed available, but
[20:02] that has a variable speed available, but it doesn't that would cost more to make
[20:04] it doesn't that would cost more to make
[20:04] it doesn't that would cost more to make the tool and maybe the the price in the
[20:07] the tool and maybe the the price in the
[20:07] the tool and maybe the the price in the store would be higher. Um, and they do
[20:10] store would be higher. Um, and they do
[20:10] store would be higher. Um, and they do make variations of it's essentially the
[20:13] make variations of it's essentially the
[20:13] make variations of it's essentially the same thing when you look at I'll grab
[20:16] same thing when you look at I'll grab
[20:16] same thing when you look at I'll grab it.
[20:23] When you look at this tool, uh, I forget
[20:23] When you look at this tool, uh, I forget what they call it, but now this one has
[20:25] what they call it, but now this one has
[20:25] what they call it, but now this one has a trigger pull with a variable level of
[20:30] a trigger pull with a variable level of
[20:30] a trigger pull with a variable level of you can control the speed with your with
[20:32] you can control the speed with your with
[20:32] you can control the speed with your with your finger.
[20:34] your finger.
[20:34] your finger. And it has the same ingredients as this
[20:37] And it has the same ingredients as this
[20:37] And it has the same ingredients as this one, but more flexibility and speed. And
[20:41] one, but more flexibility and speed. And
[20:42] one, but more flexibility and speed. And that's what I wish that I had on this
[20:44] that's what I wish that I had on this
[20:44] that's what I wish that I had on this device. Uh, so we can achieve that if if
[20:48] device. Uh, so we can achieve that if if
[20:48] device. Uh, so we can achieve that if if you wanted to hook this up before um
[20:52] you wanted to hook this up before um
[20:52] you wanted to hook this up before um after the battery and before you go into
[20:54] after the battery and before you go into
[20:54] after the battery and before you go into the machine.
[20:56] the machine.
[20:56] the machine. Okay. So, we have this 3D printed module
[21:00] Okay. So, we have this 3D printed module
[21:00] Okay. So, we have this 3D printed module that uh that's a a dummy for a battery.
[21:03] that uh that's a a dummy for a battery.
[21:03] that uh that's a a dummy for a battery. It pretends to be a battery and it has
[21:05] It pretends to be a battery and it has
[21:05] It pretends to be a battery and it has these two terminals plugged in where the
[21:07] these two terminals plugged in where the
[21:07] these two terminals plugged in where the battery would be. And we have a um some
[21:10] battery would be. And we have a um some
[21:10] battery would be. And we have a um some chaos of wires, but all you need to know
[21:13] chaos of wires, but all you need to know
[21:13] chaos of wires, but all you need to know is the wires mapped back to this other
[21:17] is the wires mapped back to this other
[21:17] is the wires mapped back to this other battery. So, we have 18 volts. At most,
[21:19] battery. So, we have 18 volts. At most,
[21:19] battery. So, we have 18 volts. At most, we could send using this device, we'll
[21:22] we could send using this device, we'll
[21:22] we could send using this device, we'll send at most the full voltage of this
[21:25] send at most the full voltage of this
[21:25] send at most the full voltage of this battery to the machine. And the machine,
[21:28] battery to the machine. And the machine,
[21:28] battery to the machine. And the machine, that's what the machine is rated to
[21:30] that's what the machine is rated to
[21:30] that's what the machine is rated to handle anyway. So, we're not going to
[21:32] handle anyway. So, we're not going to
[21:32] handle anyway. So, we're not going to hurt anything. We're just going to send.
[21:33] hurt anything. We're just going to send.
[21:34] hurt anything. We're just going to send. We might hurt it if we go in reverse,
[21:35] We might hurt it if we go in reverse,
[21:35] We might hurt it if we go in reverse, which this doesn't have a reverse
[21:37] which this doesn't have a reverse
[21:37] which this doesn't have a reverse switch. So, we're going to keep it in
[21:39] switch. So, we're going to keep it in
[21:39] switch. So, we're going to keep it in one direction. Um hopefully I still had
[21:41] one direction. Um hopefully I still had
[21:41] one direction. Um hopefully I still had it in the same direction as before. H I
[21:44] it in the same direction as before. H I
[21:44] it in the same direction as before. H I forgot. Anyway, we have uh 18 volts
[21:48] forgot. Anyway, we have uh 18 volts
[21:48] forgot. Anyway, we have uh 18 volts coming here. I've powered this on. I've
[21:52] coming here. I've powered this on. I've
[21:52] coming here. I've powered this on. I've powered this one
[21:54] powered this one
[21:54] powered this one from the off to the on position. Now,
[21:57] from the off to the on position. Now,
[21:57] from the off to the on position. Now, normally this tool would be running full
[21:59] normally this tool would be running full
[21:59] normally this tool would be running full speed
[22:01] speed
[22:01] speed going for 28,000 RPM minus whatever the
[22:05] going for 28,000 RPM minus whatever the
[22:05] going for 28,000 RPM minus whatever the battery has been drained to. And
[22:07] battery has been drained to. And
[22:07] battery has been drained to. And instead, we're just going to get however
[22:08] instead, we're just going to get however
[22:08] instead, we're just going to get however much I pull the trigger.
[22:11] much I pull the trigger.
[22:11] much I pull the trigger. So, this is maybe the minimum. I'm
[22:14] So, this is maybe the minimum. I'm
[22:14] So, this is maybe the minimum. I'm telling I'm limiting that battery's
[22:16] telling I'm limiting that battery's
[22:16] telling I'm limiting that battery's voltage by the amount I'm asking for
[22:19] voltage by the amount I'm asking for
[22:19] voltage by the amount I'm asking for with the trigger pull. And then it goes
[22:22] with the trigger pull. And then it goes
[22:22] with the trigger pull. And then it goes straight to the motor in here. There's
[22:23] straight to the motor in here. There's
[22:24] straight to the motor in here. There's very little circuitry in this machine
[22:25] very little circuitry in this machine
[22:25] very little circuitry in this machine that controls it. So, we're able to do
[22:27] that controls it. So, we're able to do
[22:27] that controls it. So, we're able to do this and then we can go medium.
[22:40] So, I can listen to the pitch of that
[22:40] So, I can listen to the pitch of that motor turning when I go full uh full
[22:43] motor turning when I go full uh full
[22:43] motor turning when I go full uh full trigger pull. And that sounds just like
[22:46] trigger pull. And that sounds just like
[22:46] trigger pull. And that sounds just like it sounds when I have this battery
[22:48] it sounds when I have this battery
[22:48] it sounds when I have this battery hooked directly into the tool.
[22:51] hooked directly into the tool.
[22:52] hooked directly into the tool. Okay, just for funsies, we can also um
[22:55] Okay, just for funsies, we can also um
[22:55] Okay, just for funsies, we can also um operate this big treadmill motor with
[22:57] operate this big treadmill motor with
[22:57] operate this big treadmill motor with the same battery, 18 volts, and the same
[23:02] the same battery, 18 volts, and the same
[23:02] the same battery, 18 volts, and the same um power module. And then basically we
[23:06] um power module. And then basically we
[23:06] um power module. And then basically we have the 18 volts goes into the power
[23:08] have the 18 volts goes into the power
[23:08] have the 18 volts goes into the power module as before. And then the the two
[23:12] module as before. And then the the two
[23:12] module as before. And then the the two uh wires going out are going into this
[23:15] uh wires going out are going into this
[23:15] uh wires going out are going into this power distribution block. Um these are D
[23:18] power distribution block. Um these are D
[23:18] power distribution block. Um these are D terminals. Um they're easy to hook up
[23:21] terminals. Um they're easy to hook up
[23:21] terminals. Um they're easy to hook up and replace and swap and change. Um and
[23:24] and replace and swap and change. Um and
[23:24] and replace and swap and change. Um and then this the positive and negative jump
[23:28] then this the positive and negative jump
[23:28] then this the positive and negative jump onto the next cord. This is all 16 gauge
[23:31] onto the next cord. This is all 16 gauge
[23:31] onto the next cord. This is all 16 gauge wire. And then it goes into the base of
[23:33] wire. And then it goes into the base of
[23:33] wire. And then it goes into the base of this big motor. Uh ties in where the old
[23:37] this big motor. Uh ties in where the old
[23:37] this big motor. Uh ties in where the old circuit was tied in on the treadmill and
[23:40] circuit was tied in on the treadmill and
[23:40] circuit was tied in on the treadmill and it has a big heavy um mass, a flywheel
[23:45] it has a big heavy um mass, a flywheel
[23:45] it has a big heavy um mass, a flywheel if you will on this. And we can uh we
[23:49] if you will on this. And we can uh we
[23:49] if you will on this. And we can uh we can control that as well. So uh I'm
[23:51] can control that as well. So uh I'm
[23:51] can control that as well. So uh I'm going to leave it in the same direction
[23:53] going to leave it in the same direction
[23:53] going to leave it in the same direction as before. And then I'm going to press
[23:55] as before. And then I'm going to press
[23:55] as before. And then I'm going to press just a little bit on the terminal. I
[23:57] just a little bit on the terminal. I
[23:57] just a little bit on the terminal. I mean on the trigger.
[23:59] mean on the trigger.
[23:59] mean on the trigger. And you can see we get a slow rotation.
[24:03] And you can see we get a slow rotation.
[24:03] And you can see we get a slow rotation. This is a beautiful motor by the way.
[24:05] This is a beautiful motor by the way.
[24:05] This is a beautiful motor by the way. It's so it has such a nice linear
[24:08] It's so it has such a nice linear
[24:08] It's so it has such a nice linear response from a low speed to a high
[24:11] response from a low speed to a high
[24:11] response from a low speed to a high speed. And that's something that I
[24:13] speed. And that's something that I
[24:13] speed. And that's something that I expect when I take apart a a treadmill
[24:16] expect when I take apart a a treadmill
[24:16] expect when I take apart a a treadmill machine. I already know. Well, these
[24:17] machine. I already know. Well, these
[24:18] machine. I already know. Well, these these are um they have settings to go
[24:21] these are um they have settings to go
[24:21] these are um they have settings to go gradually from a low speed to a high
[24:23] gradually from a low speed to a high
[24:23] gradually from a low speed to a high speed. So that motor should be should be
[24:25] speed. So that motor should be should be
[24:25] speed. So that motor should be should be built such that it can accept a wide
[24:27] built such that it can accept a wide
[24:28] built such that it can accept a wide range of voltages if it's DC. And so we
[24:32] range of voltages if it's DC. And so we
[24:32] range of voltages if it's DC. And so we can go further. Oh no, that's full
[24:35] can go further. Oh no, that's full
[24:35] can go further. Oh no, that's full power. So this motor is rated to go up
[24:39] power. So this motor is rated to go up
[24:39] power. So this motor is rated to go up to 120 volts of DC, which is really high
[24:43] to 120 volts of DC, which is really high
[24:43] to 120 volts of DC, which is really high compared to most appliances. Um, and if
[24:46] compared to most appliances. Um, and if
[24:46] compared to most appliances. Um, and if I let off the trigger, it slows down.
[24:49] I let off the trigger, it slows down.
[24:49] I let off the trigger, it slows down. But then if I let all the way off, it
[24:51] But then if I let all the way off, it
[24:51] But then if I let all the way off, it kind of jerks, I think, because this has
[24:54] kind of jerks, I think, because this has
[24:54] kind of jerks, I think, because this has uh a braking function of some sort.
[24:57] uh a braking function of some sort.
[24:57] uh a braking function of some sort. Okay. And then we can also reverse this
[25:00] Okay. And then we can also reverse this
[25:00] Okay. And then we can also reverse this direction.
[25:02] direction.
[25:02] direction. And then hit it again. And we can go the
[25:05] And then hit it again. And we can go the
[25:05] And then hit it again. And we can go the other way.
[25:08] other way.
[25:08] other way. What I learned about this trigger module
[25:10] What I learned about this trigger module
[25:10] What I learned about this trigger module is that it uh it doesn't have uh a lot
[25:13] is that it uh it doesn't have uh a lot
[25:13] is that it uh it doesn't have uh a lot of gradation gradation. I don't know a
[25:17] of gradation gradation. I don't know a
[25:17] of gradation gradation. I don't know a lot of smooth steps between zero power
[25:21] lot of smooth steps between zero power
[25:21] lot of smooth steps between zero power and full power. There are at least three
[25:23] and full power. There are at least three
[25:23] and full power. There are at least three discrete settings that I can find. And I
[25:25] discrete settings that I can find. And I
[25:25] discrete settings that I can find. And I think there's a somewhat of a continuous
[25:27] think there's a somewhat of a continuous
[25:27] think there's a somewhat of a continuous range down near the lower the lower side
[25:31] range down near the lower the lower side
[25:31] range down near the lower the lower side of the trigger pull. So that's full. And
[25:33] of the trigger pull. So that's full. And
[25:33] of the trigger pull. So that's full. And if I release it quickly, I won't do this
[25:35] if I release it quickly, I won't do this
[25:35] if I release it quickly, I won't do this a lot, but just once you get that uh you
[25:39] a lot, but just once you get that uh you
[25:39] a lot, but just once you get that uh you can see the inertia jump and and pull
[25:41] can see the inertia jump and and pull
[25:41] can see the inertia jump and and pull this whole assembly back the other way.
[25:45] this whole assembly back the other way.
[25:45] this whole assembly back the other way. And we power off and we can simply take
[25:49] And we power off and we can simply take
[25:49] And we power off and we can simply take the screwdriver and remove these uh
[25:53] the screwdriver and remove these uh
[25:53] the screwdriver and remove these uh wires from the screw terminals. Okay,
[25:55] wires from the screw terminals. Okay,
[25:56] wires from the screw terminals. Okay, now I have those available and I don't
[25:58] now I have those available and I don't
[25:58] now I have those available and I don't want to turn this back on uh while those
[26:01] want to turn this back on uh while those
[26:01] want to turn this back on uh while those wires are exposed. These are simply
[26:04] wires are exposed. These are simply
[26:04] wires are exposed. These are simply fererals that I used in lots of projects
[26:06] fererals that I used in lots of projects
[26:06] fererals that I used in lots of projects and I think I've shown before. Um they
[26:09] and I think I've shown before. Um they
[26:09] and I think I've shown before. Um they are crimped on and that you just need to
[26:11] are crimped on and that you just need to
[26:11] are crimped on and that you just need to select the size that matches your wires.
[26:13] select the size that matches your wires.
[26:13] select the size that matches your wires. I use a lot of 18 gauge wire. That's
[26:16] I use a lot of 18 gauge wire. That's
[26:16] I use a lot of 18 gauge wire. That's this size. And then for a heavier
[26:20] this size. And then for a heavier
[26:20] this size. And then for a heavier machine like this, I'm using 16.
[26:23] machine like this, I'm using 16.
[26:23] machine like this, I'm using 16. Essentially, you can choose by just
[26:25] Essentially, you can choose by just
[26:25] Essentially, you can choose by just matching the size of the copper that
[26:27] matching the size of the copper that
[26:27] matching the size of the copper that you're finding in in the machine that
[26:29] you're finding in in the machine that
[26:29] you're finding in in the machine that you're dismantling. Okay. So, if you
[26:31] you're dismantling. Okay. So, if you
[26:31] you're dismantling. Okay. So, if you wanted to reproduce this project that I
[26:33] wanted to reproduce this project that I
[26:33] wanted to reproduce this project that I just did, I'll walk through in this
[26:35] just did, I'll walk through in this
[26:35] just did, I'll walk through in this section uh just the tools that are
[26:37] section uh just the tools that are
[26:37] section uh just the tools that are required because there aren't that many
[26:39] required because there aren't that many
[26:39] required because there aren't that many tools and there aren't that many
[26:40] tools and there aren't that many
[26:40] tools and there aren't that many supplies in order to do this and then
[26:43] supplies in order to do this and then
[26:43] supplies in order to do this and then maybe the audience will gain
[26:44] maybe the audience will gain
[26:44] maybe the audience will gain familiarity. This is the same equipment
[26:46] familiarity. This is the same equipment
[26:46] familiarity. This is the same equipment that we use for the robotics projects,
[26:48] that we use for the robotics projects,
[26:48] that we use for the robotics projects, same supplies that we use for many other
[26:51] same supplies that we use for many other
[26:51] same supplies that we use for many other pro projects. And this is why um they if
[26:55] pro projects. And this is why um they if
[26:55] pro projects. And this is why um they if this appears to be along your path of uh
[26:59] this appears to be along your path of uh
[26:59] this appears to be along your path of uh project space, then I then I would
[27:01] project space, then I then I would
[27:02] project space, then I then I would recommend uh everything you see here has
[27:04] recommend uh everything you see here has
[27:04] recommend uh everything you see here has been and tested, benchmarked, and
[27:06] been and tested, benchmarked, and
[27:06] been and tested, benchmarked, and compared with other similar options um
[27:10] compared with other similar options um
[27:10] compared with other similar options um over at least 5 years. Okay. To
[27:13] over at least 5 years. Okay. To
[27:13] over at least 5 years. Okay. To disassemble the plastic housing of this
[27:15] disassemble the plastic housing of this
[27:15] disassemble the plastic housing of this drill driver, all it took was a Phillips
[27:19] drill driver, all it took was a Phillips
[27:19] drill driver, all it took was a Phillips one screwdriver. And those were ordinary
[27:23] one screwdriver. And those were ordinary
[27:23] one screwdriver. And those were ordinary uh Phillips screws, but they're just a
[27:25] uh Phillips screws, but they're just a
[27:25] uh Phillips screws, but they're just a little bit deep set recessed into the
[27:27] little bit deep set recessed into the
[27:28] little bit deep set recessed into the plastic. And so this is a you want a
[27:30] plastic. And so this is a you want a
[27:30] plastic. And so this is a you want a narrow um a convenient narrow
[27:34] narrow um a convenient narrow
[27:34] narrow um a convenient narrow screwdriver for that that's at least got
[27:36] screwdriver for that that's at least got
[27:36] screwdriver for that that's at least got an inch of length to it. The the
[27:39] an inch of length to it. The the
[27:40] an inch of length to it. The the alternatives that we use all the time
[27:41] alternatives that we use all the time
[27:41] alternatives that we use all the time are this this type of um bit set based
[27:46] are this this type of um bit set based
[27:46] are this this type of um bit set based screwdrivers. They have all these
[27:49] screwdrivers. They have all these
[27:49] screwdrivers. They have all these collections of bits that come with them,
[27:51] collections of bits that come with them,
[27:51] collections of bits that come with them, but uh they're they're a maybe on
[27:53] but uh they're they're a maybe on
[27:53] but uh they're they're a maybe on whether they will reach or not. Um then
[27:57] whether they will reach or not. Um then
[27:57] whether they will reach or not. Um then to to cut wires free, then we're using a
[28:01] to to cut wires free, then we're using a
[28:01] to to cut wires free, then we're using a steel flush cutter that lives here on
[28:04] steel flush cutter that lives here on
[28:04] steel flush cutter that lives here on the benchtop. We almost don't even need
[28:05] the benchtop. We almost don't even need
[28:05] the benchtop. We almost don't even need to leave this benchtop in order to do
[28:07] to leave this benchtop in order to do
[28:07] to leave this benchtop in order to do the project. Um the flush cutters, this
[28:11] the project. Um the flush cutters, this
[28:11] the project. Um the flush cutters, this specific one, uh it's has a it's not a
[28:13] specific one, uh it's has a it's not a
[28:14] specific one, uh it's has a it's not a stamped steel. It's actually either
[28:15] stamped steel. It's actually either
[28:16] stamped steel. It's actually either forged or um or uh cast steel shape and
[28:22] forged or um or uh cast steel shape and
[28:22] forged or um or uh cast steel shape and then it's actually ground. So you have
[28:25] then it's actually ground. So you have
[28:25] then it's actually ground. So you have that very fine precision point. But you
[28:28] that very fine precision point. But you
[28:28] that very fine precision point. But you want to when you're cutting larger
[28:30] want to when you're cutting larger
[28:30] want to when you're cutting larger things like this diameter, then you want
[28:32] things like this diameter, then you want
[28:32] things like this diameter, then you want to grab all the way down uh so that
[28:35] to grab all the way down uh so that
[28:35] to grab all the way down uh so that you're not damaging the tip. That's your
[28:38] you're not damaging the tip. That's your
[28:38] you're not damaging the tip. That's your best odds. You you really won't damage
[28:40] best odds. You you really won't damage
[28:40] best odds. You you really won't damage cutting uh copper or tin with steel. you
[28:44] cutting uh copper or tin with steel. you
[28:44] cutting uh copper or tin with steel. you should be fine. Um, then moving the the
[28:48] should be fine. Um, then moving the the
[28:48] should be fine. Um, then moving the the solder, removing the solder from
[28:53] solder, removing the solder from
[28:53] solder, removing the solder from um, let's say on here
[28:57] um, let's say on here
[28:57] um, let's say on here on this trigger mechanism,
[29:01] on this trigger mechanism,
[29:01] on this trigger mechanism, we've got to heat up those solder points
[29:04] we've got to heat up those solder points
[29:04] we've got to heat up those solder points on the previous wires. And you just lift
[29:06] on the previous wires. And you just lift
[29:06] on the previous wires. And you just lift them off. It's that easy. And you need
[29:09] them off. It's that easy. And you need
[29:09] them off. It's that easy. And you need at least probably 40 watts on your
[29:11] at least probably 40 watts on your
[29:11] at least probably 40 watts on your soldering iron. And so, uh, the most
[29:15] soldering iron. And so, uh, the most
[29:15] soldering iron. And so, uh, the most soldering irons will do it, but I would
[29:17] soldering irons will do it, but I would
[29:17] soldering irons will do it, but I would say you're, if you have one of these,
[29:19] say you're, if you have one of these,
[29:19] say you're, if you have one of these, you know, $10 units or thing from the
[29:22] you know, $10 units or thing from the
[29:22] you know, $10 units or thing from the dollar store, it may or may not uh, be
[29:25] dollar store, it may or may not uh, be
[29:25] dollar store, it may or may not uh, be hot enough to really get you going. And
[29:28] hot enough to really get you going. And
[29:28] hot enough to really get you going. And then I cranked this up to a very high
[29:30] then I cranked this up to a very high
[29:30] then I cranked this up to a very high temperature because I believe those uh
[29:34] temperature because I believe those uh
[29:34] temperature because I believe those uh initial
[29:35] initial
[29:36] initial initial terminals with the solder that
[29:38] initial terminals with the solder that
[29:38] initial terminals with the solder that was on the circuit board from the
[29:40] was on the circuit board from the
[29:40] was on the circuit board from the factory it was uh lead free and there
[29:44] factory it was uh lead free and there
[29:44] factory it was uh lead free and there there are certain certifications. So
[29:46] there are certain certifications. So
[29:46] there are certain certifications. So most of the storebought circuits you'll
[29:49] most of the storebought circuits you'll
[29:49] most of the storebought circuits you'll you'll find with lead free solder it's a
[29:51] you'll find with lead free solder it's a
[29:51] you'll find with lead free solder it's a lot harder to work with and it has a
[29:52] lot harder to work with and it has a
[29:52] lot harder to work with and it has a higher melting point. So, I would add a
[29:56] higher melting point. So, I would add a
[29:56] higher melting point. So, I would add a little bit of this leaded solder. It's
[29:58] little bit of this leaded solder. It's
[29:58] little bit of this leaded solder. It's heavily leaded with I think 40%.
[30:02] heavily leaded with I think 40%.
[30:02] heavily leaded with I think 40%. Anyway, that's easy to to Google and
[30:04] Anyway, that's easy to to Google and
[30:04] Anyway, that's easy to to Google and learn more about the types. Um, but I
[30:06] learn more about the types. Um, but I
[30:06] learn more about the types. Um, but I added a little bit of my own solder that
[30:08] added a little bit of my own solder that
[30:08] added a little bit of my own solder that mixes with the solder that's on the
[30:11] mixes with the solder that's on the
[30:11] mixes with the solder that's on the board and it becomes easier for the
[30:13] board and it becomes easier for the
[30:13] board and it becomes easier for the whole little uh puddle, the whole joint
[30:16] whole little uh puddle, the whole joint
[30:16] whole little uh puddle, the whole joint to become liquid and then come free. I
[30:19] to become liquid and then come free. I
[30:19] to become liquid and then come free. I did end up using, you could get away
[30:21] did end up using, you could get away
[30:21] did end up using, you could get away without it, but I did end up using the
[30:24] without it, but I did end up using the
[30:24] without it, but I did end up using the solder sucker, which is simply a pump.
[30:27] solder sucker, which is simply a pump.
[30:27] solder sucker, which is simply a pump. It has this volume in the body that
[30:30] It has this volume in the body that
[30:30] It has this volume in the body that turns to a vacuum when you press this
[30:32] turns to a vacuum when you press this
[30:32] turns to a vacuum when you press this button. Then it's going to lift that
[30:34] button. Then it's going to lift that
[30:34] button. Then it's going to lift that liquid solder off of a joint uh once
[30:37] liquid solder off of a joint uh once
[30:38] liquid solder off of a joint uh once you've melted it and you have it uh
[30:41] you've melted it and you have it uh
[30:41] you've melted it and you have it uh nice and wet and melted. Then this, you
[30:45] nice and wet and melted. Then this, you
[30:45] nice and wet and melted. Then this, you reach this up to the tip and then you
[30:47] reach this up to the tip and then you
[30:47] reach this up to the tip and then you just press that button and it will suck
[30:50] just press that button and it will suck
[30:50] just press that button and it will suck up a big glob of the solder. Maybe half
[30:52] up a big glob of the solder. Maybe half
[30:52] up a big glob of the solder. Maybe half of it will be gone and the rest is easy
[30:54] of it will be gone and the rest is easy
[30:54] of it will be gone and the rest is easy to work with. Um, then
[30:58] to work with. Um, then
[30:58] to work with. Um, then I'm always using my favorite wires that
[31:01] I'm always using my favorite wires that
[31:01] I'm always using my favorite wires that are already paired. That reduces the
[31:03] are already paired. That reduces the
[31:03] are already paired. That reduces the messes that you work with uh the the
[31:06] messes that you work with uh the the
[31:06] messes that you work with uh the the craziness of the wires when you're
[31:07] craziness of the wires when you're
[31:07] craziness of the wires when you're prototyping things. This is um silicone
[31:11] prototyping things. This is um silicone
[31:11] prototyping things. This is um silicone and it has fine strands. So, in most
[31:13] and it has fine strands. So, in most
[31:14] and it has fine strands. So, in most projects, the fine strands makes it more
[31:15] projects, the fine strands makes it more
[31:15] projects, the fine strands makes it more flexible and more easy to work with. And
[31:18] flexible and more easy to work with. And
[31:18] flexible and more easy to work with. And instead of having frayed um messy tips,
[31:21] instead of having frayed um messy tips,
[31:21] instead of having frayed um messy tips, we add these fererals. And the fereral
[31:23] we add these fererals. And the fereral
[31:24] we add these fererals. And the fereral crimper looks like this. And it's right
[31:26] crimper looks like this. And it's right
[31:26] crimper looks like this. And it's right here at the station. Um
[31:29] here at the station. Um
[31:29] here at the station. Um you can get these tools for maybe $15,
[31:33] you can get these tools for maybe $15,
[31:33] you can get these tools for maybe $15, 20. And they have this uh these steel
[31:38] 20. And they have this uh these steel
[31:38] 20. And they have this uh these steel little plates that move in and crush the
[31:42] little plates that move in and crush the
[31:42] little plates that move in and crush the the tin
[31:44] the tin
[31:44] the tin alloy sleeve with these fererals that
[31:48] alloy sleeve with these fererals that
[31:48] alloy sleeve with these fererals that look like this. 16 gauges like this. You
[31:52] look like this. 16 gauges like this. You
[31:52] look like this. 16 gauges like this. You slip that onto the end of the wire and
[31:54] slip that onto the end of the wire and
[31:54] slip that onto the end of the wire and then you crimp it
[31:56] then you crimp it
[31:56] then you crimp it in order to send power to any of your
[32:00] in order to send power to any of your
[32:00] in order to send power to any of your tools. Now, people have created a lot of
[32:03] tools. Now, people have created a lot of
[32:03] tools. Now, people have created a lot of uh mod 3D models online where you can
[32:07] uh mod 3D models online where you can
[32:07] uh mod 3D models online where you can build your own terminal dummy. Uh but
[32:09] build your own terminal dummy. Uh but
[32:09] build your own terminal dummy. Uh but this one for the rigid tools, I have a
[32:11] this one for the rigid tools, I have a
[32:11] this one for the rigid tools, I have a lot of them listed on GrabCAD. So, all I
[32:15] lot of them listed on GrabCAD. So, all I
[32:15] lot of them listed on GrabCAD. So, all I did was place the wires into uh into the
[32:18] did was place the wires into uh into the
[32:18] did was place the wires into uh into the slots and I crimped on these spade
[32:21] slots and I crimped on these spade
[32:21] slots and I crimped on these spade terminals. These are not exactly ideal.
[32:24] terminals. These are not exactly ideal.
[32:24] terminals. These are not exactly ideal. you will have a slightly more limited
[32:27] you will have a slightly more limited
[32:27] you will have a slightly more limited current uh that you can send to the
[32:29] current uh that you can send to the
[32:29] current uh that you can send to the tool, but for short term and for
[32:31] tool, but for short term and for
[32:31] tool, but for short term and for testing, this is totally satisfactory.
[32:34] testing, this is totally satisfactory.
[32:34] testing, this is totally satisfactory. And these would just slide into the
[32:35] And these would just slide into the
[32:36] And these would just slide into the prongs that grab a hold of it
[32:39] prongs that grab a hold of it
[32:39] prongs that grab a hold of it um inside of this housing.
[32:42] um inside of this housing.
[32:42] um inside of this housing. Then we have these red and black
[32:44] Then we have these red and black
[32:44] Then we have these red and black Anderson terminals that we use on I use
[32:47] Anderson terminals that we use on I use
[32:47] Anderson terminals that we use on I use these whenever we're working with 10
[32:49] these whenever we're working with 10
[32:49] these whenever we're working with 10 amps or larger. Um, so these they have a
[32:54] amps or larger. Um, so these they have a
[32:54] amps or larger. Um, so these they have a a nice conductive terminal inside that
[32:57] a nice conductive terminal inside that
[32:57] a nice conductive terminal inside that gets crimped with a heavier crimpers.
[33:00] gets crimped with a heavier crimpers.
[33:00] gets crimped with a heavier crimpers. Uh, Anderson is one of the brand names,
[33:02] Uh, Anderson is one of the brand names,
[33:02] Uh, Anderson is one of the brand names, but now there are many. This device is
[33:05] but now there are many. This device is
[33:05] but now there are many. This device is available probably 15 or $20 as well and
[33:08] available probably 15 or $20 as well and
[33:08] available probably 15 or $20 as well and it should last a lifetime. Um, there are
[33:11] it should last a lifetime. Um, there are
[33:11] it should last a lifetime. Um, there are replaceable jaws. Um, and in any case,
[33:14] replaceable jaws. Um, and in any case,
[33:14] replaceable jaws. Um, and in any case, so there are 15, 30, and 45 amp styles
[33:18] so there are 15, 30, and 45 amp styles
[33:18] so there are 15, 30, and 45 amp styles of these going from small to large that
[33:21] of these going from small to large that
[33:21] of these going from small to large that crimp onto the wires. And then those uh
[33:24] crimp onto the wires. And then those uh
[33:24] crimp onto the wires. And then those uh crimped ends of the wire gets slid and
[33:27] crimped ends of the wire gets slid and
[33:27] crimped ends of the wire gets slid and snapped into the front of here. So that
[33:29] snapped into the front of here. So that
[33:29] snapped into the front of here. So that you can see the tips of the terminals
[33:31] you can see the tips of the terminals
[33:31] you can see the tips of the terminals there.
[33:33] there.
[33:34] there. And then so I treat these connections uh
[33:36] And then so I treat these connections uh
[33:36] And then so I treat these connections uh this is uh semi-permanent. This is more
[33:40] this is uh semi-permanent. This is more
[33:40] this is uh semi-permanent. This is more costly, probably uh a dollar or $150
[33:43] costly, probably uh a dollar or $150
[33:43] costly, probably uh a dollar or $150 worth of equipment on the end of this
[33:45] worth of equipment on the end of this
[33:45] worth of equipment on the end of this wire. And so that's what I build when
[33:47] wire. And so that's what I build when
[33:47] wire. And so that's what I build when I'm sure I want to keep it in this
[33:49] I'm sure I want to keep it in this
[33:50] I'm sure I want to keep it in this format. And before I'm sure, then I'm
[33:52] format. And before I'm sure, then I'm
[33:52] format. And before I'm sure, then I'm just using those fererals like you see
[33:55] just using those fererals like you see
[33:55] just using those fererals like you see here to get something quickly put
[33:57] here to get something quickly put
[33:57] here to get something quickly put together. And I can always snip these
[33:59] together. And I can always snip these
[33:59] together. And I can always snip these clean and add uh this later if I decide
[34:02] clean and add uh this later if I decide
[34:02] clean and add uh this later if I decide to keep it. And the last bit is um to
[34:07] to keep it. And the last bit is um to
[34:07] to keep it. And the last bit is um to temporarily or quickly get um wires
[34:11] temporarily or quickly get um wires
[34:11] temporarily or quickly get um wires bridged together. Black goes to black
[34:13] bridged together. Black goes to black
[34:13] bridged together. Black goes to black and you have continuity from left to
[34:15] and you have continuity from left to
[34:15] and you have continuity from left to right on each of these uh the the wires
[34:19] right on each of these uh the the wires
[34:19] right on each of these uh the the wires plug into a hole. And this is I think
[34:21] plug into a hole. And this is I think
[34:21] plug into a hole. And this is I think called a WGO. WGO is a brand WGO style
[34:24] called a WGO. WGO is a brand WGO style
[34:24] called a WGO. WGO is a brand WGO style uh terminals. So we just have a um
[34:27] uh terminals. So we just have a um
[34:27] uh terminals. So we just have a um container full of these on hand that
[34:30] container full of these on hand that
[34:30] container full of these on hand that these get used all the time during
[34:32] these get used all the time during
[34:32] these get used all the time during prototyping.
[34:34] prototyping.
[34:34] prototyping. So I think that's it. Um the the total
[34:37] So I think that's it. Um the the total
[34:37] So I think that's it. Um the the total tools are quite minimal. You can do a
[34:40] tools are quite minimal. You can do a
[34:40] tools are quite minimal. You can do a whole lot with just a few tools. And
[34:42] whole lot with just a few tools. And
[34:42] whole lot with just a few tools. And what I love about this project is that
[34:44] what I love about this project is that
[34:44] what I love about this project is that they um all the tools are also ones that
[34:47] they um all the tools are also ones that
[34:47] they um all the tools are also ones that serve many many other projects. There's
[34:49] serve many many other projects. There's
[34:49] serve many many other projects. There's nothing that was uh specially needed for
[34:52] nothing that was uh specially needed for
[34:52] nothing that was uh specially needed for this project. So um and also I apologize
[34:55] this project. So um and also I apologize
[34:56] this project. So um and also I apologize to Joshua. We have a team member Joshua
[34:58] to Joshua. We have a team member Joshua
[34:58] to Joshua. We have a team member Joshua who's a meatronics engineering recent
[35:01] who's a meatronics engineering recent
[35:01] who's a meatronics engineering recent graduate and he's working here in this
[35:03] graduate and he's working here in this
[35:03] graduate and he's working here in this lab. He is totally capable of doing the
[35:06] lab. He is totally capable of doing the
[35:06] lab. He is totally capable of doing the explanation for um the driver breakdown
[35:10] explanation for um the driver breakdown
[35:10] explanation for um the driver breakdown and its electronics. But, uh, yeah,
[35:13] and its electronics. But, uh, yeah,
[35:13] and its electronics. But, uh, yeah, we're we're working on I'm working on
[35:14] we're we're working on I'm working on
[35:14] we're we're working on I'm working on getting, uh, some camera time for them
[35:16] getting, uh, some camera time for them
[35:16] getting, uh, some camera time for them and and we're working out how to work
[35:19] and and we're working out how to work
[35:19] and and we're working out how to work the cameras and microphones and the
[35:21] the cameras and microphones and the
[35:21] the cameras and microphones and the space with multiple people here in the
[35:23] space with multiple people here in the
[35:24] space with multiple people here in the lab. So, I'm I'm looking forward to
[35:25] lab. So, I'm I'm looking forward to
[35:25] lab. So, I'm I'm looking forward to that. Um, and what else? Okay, very last
[35:30] that. Um, and what else? Okay, very last
[35:30] that. Um, and what else? Okay, very last thing. There was one uh question, a
[35:32] thing. There was one uh question, a
[35:32] thing. There was one uh question, a mystery that was solved for me in the
[35:34] mystery that was solved for me in the
[35:34] mystery that was solved for me in the course of dismantling this uh drill. And
[35:37] course of dismantling this uh drill. And
[35:37] course of dismantling this uh drill. And that is what kind of mechanism lives
[35:39] that is what kind of mechanism lives
[35:39] that is what kind of mechanism lives inside of here that allows the the
[35:41] inside of here that allows the the
[35:41] inside of here that allows the the slipping clutch where you'll hear a a
[35:44] slipping clutch where you'll hear a a
[35:44] slipping clutch where you'll hear a a clacker clanking sound like that. And
[35:48] clacker clanking sound like that. And
[35:48] clacker clanking sound like that. And you can use this, let the clutch slip
[35:52] you can use this, let the clutch slip
[35:52] you can use this, let the clutch slip and have that that cranking without
[35:55] and have that that cranking without
[35:55] and have that that cranking without damaging this over the life of the tool.
[35:57] damaging this over the life of the tool.
[35:57] damaging this over the life of the tool. And the way that looks is uh it takes
[36:01] And the way that looks is uh it takes
[36:01] And the way that looks is uh it takes place on this ring where there are uh
[36:06] place on this ring where there are uh
[36:06] place on this ring where there are uh little ball bearings that live in the
[36:08] little ball bearings that live in the
[36:08] little ball bearings that live in the groove and they jump over the humps on
[36:13] groove and they jump over the humps on
[36:13] groove and they jump over the humps on this ring. And so there's an interface
[36:15] this ring. And so there's an interface
[36:15] this ring. And so there's an interface inside the gearbox where this is able to
[36:18] inside the gearbox where this is able to
[36:18] inside the gearbox where this is able to slip with respect to the the forward set
[36:22] slip with respect to the the forward set
[36:22] slip with respect to the the forward set of gears by uh these balls just jumping
[36:28] of gears by uh these balls just jumping
[36:28] of gears by uh these balls just jumping over the humps. And I would expect, I
[36:31] over the humps. And I would expect, I
[36:31] over the humps. And I would expect, I didn't look super close, but um I would
[36:33] didn't look super close, but um I would
[36:34] didn't look super close, but um I would expect that when you adjust the torque
[36:36] expect that when you adjust the torque
[36:36] expect that when you adjust the torque on that clutch, you are probably simply
[36:40] on that clutch, you are probably simply
[36:40] on that clutch, you are probably simply adjusting the closeness or the spring
[36:43] adjusting the closeness or the spring
[36:44] adjusting the closeness or the spring pressure of one side of the assembly up
[36:47] pressure of one side of the assembly up
[36:47] pressure of one side of the assembly up against those balls on the other side of
[36:49] against those balls on the other side of
[36:50] against those balls on the other side of the assembly. And so a higher pressure
[36:52] the assembly. And so a higher pressure
[36:52] the assembly. And so a higher pressure means it's going to be a stronger torque
[36:53] means it's going to be a stronger torque
[36:53] means it's going to be a stronger torque before it slips.
[37:01] And you can hear that heavier
[37:01] And you can hear that heavier uh clanking. And over here it's a
[37:03] uh clanking. And over here it's a
[37:03] uh clanking. And over here it's a lighter clanking.
[37:05] lighter clanking.
[37:06] lighter clanking. So that's all folks. Have a great day.
[37:08] So that's all folks. Have a great day.
[37:08] So that's all folks. Have a great day. Hope you learned something. And uh feel
[37:10] Hope you learned something. And uh feel
[37:10] Hope you learned something. And uh feel free to add any comments if you've got
[37:12] free to add any comments if you've got
[37:12] free to add any comments if you've got information, if I missed something, um
[37:14] information, if I missed something, um
[37:14] information, if I missed something, um or if you have questions that would uh
[37:16] or if you have questions that would uh
[37:16] or if you have questions that would uh go along with this topic uh in a future
[37:18] go along with this topic uh in a future
[37:18] go along with this topic uh in a future video.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
