---
title: "How much CPU does it take to generate PWM signals on Raspberry Pi?"
url: "https://www.youtube.com/watch?v=P2Zvfztf68M"
video_id: "P2Zvfztf68M"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2021-04-09
duration: "5:57"
duration_sec: 357
views: 301
likes: 5
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/P2Zvfztf68M/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 288
chapters_count: 0
has_description: true
has_comments: false
---

## Description

Quick experiment to learn about the load that we put on the processor when we ask the Pi to generate PWM using software.  In our setup we use the SCUTTLE Robot which has 4 PWM signals generated to drive the two wheels.

About our Open Source Robot: https://www.scuttlerobot.org

## Transcript

[0:03] hi everybody today we're going to look
[0:03] hi everybody today we're going to look at
[0:03] at
[0:04] at um on the raspberry pi uh how much
[0:06] um on the raspberry pi uh how much
[0:06] um on the raspberry pi uh how much processing power does it take to output
[0:08] processing power does it take to output
[0:08] processing power does it take to output the pwm signals that we use to drive the
[0:11] the pwm signals that we use to drive the
[0:11] the pwm signals that we use to drive the motors
[0:12] motors
[0:12] motors on our mobile robot pardon the noise but
[0:15] on our mobile robot pardon the noise but
[0:15] on our mobile robot pardon the noise but i have a
[0:16] i have a
[0:16] i have a 3d printer running right now and it's
[0:17] 3d printer running right now and it's
[0:18] 3d printer running right now and it's going to make a little bit of noise in
[0:19] going to make a little bit of noise in
[0:19] going to make a little bit of noise in the background
[0:20] the background
[0:20] the background now here on our raspberry pi we have
[0:23] now here on our raspberry pi we have
[0:23] now here on our raspberry pi we have four channels uh that are occupied
[0:27] four channels uh that are occupied
[0:27] four channels uh that are occupied on the gpio pins that are currently
[0:29] on the gpio pins that are currently
[0:29] on the gpio pins that are currently using
[0:30] using
[0:30] using software-based pwm outputs to drive
[0:33] software-based pwm outputs to drive
[0:33] software-based pwm outputs to drive the signals going to the motor driver
[0:36] the signals going to the motor driver
[0:36] the signals going to the motor driver the motor driver basically
[0:38] the motor driver basically
[0:38] the motor driver basically interprets these signals in pairs with
[0:40] interprets these signals in pairs with
[0:40] interprets these signals in pairs with inputs one
[0:41] inputs one
[0:41] inputs one and two corresponding to outputs one and
[0:43] and two corresponding to outputs one and
[0:43] and two corresponding to outputs one and two that's not hooked up right now
[0:45] two that's not hooked up right now
[0:46] two that's not hooked up right now but what it'll do is give me something
[0:47] but what it'll do is give me something
[0:47] but what it'll do is give me something in between positive 12 volts to zero
[0:50] in between positive 12 volts to zero
[0:50] in between positive 12 volts to zero to negative 12 volts going out to my dc
[0:53] to negative 12 volts going out to my dc
[0:53] to negative 12 volts going out to my dc motor
[0:53] motor
[0:53] motor to drive it forwards or backwards well
[0:57] to drive it forwards or backwards well
[0:57] to drive it forwards or backwards well as it turns out these motors are
[1:00] as it turns out these motors are
[1:00] as it turns out these motors are uh running they run a lot better um
[1:03] uh running they run a lot better um
[1:03] uh running they run a lot better um with less noise and a more efficiency
[1:05] with less noise and a more efficiency
[1:05] with less noise and a more efficiency and you will reach the spec
[1:07] and you will reach the spec
[1:07] and you will reach the spec torque only when you output a decently
[1:10] torque only when you output a decently
[1:10] torque only when you output a decently high
[1:11] high
[1:11] high pwm frequency on these channels
[1:15] pwm frequency on these channels
[1:15] pwm frequency on these channels and so that means we're going to be
[1:16] and so that means we're going to be
[1:16] and so that means we're going to be asking the processor of the raspberry pi
[1:19] asking the processor of the raspberry pi
[1:19] asking the processor of the raspberry pi to to generate using software
[1:23] to to generate using software
[1:23] to to generate using software the rising and falling edges on these
[1:25] the rising and falling edges on these
[1:25] the rising and falling edges on these four outputs
[1:26] four outputs
[1:26] four outputs which means you have demand on your
[1:29] which means you have demand on your
[1:29] which means you have demand on your processor of
[1:31] processor of
[1:31] processor of four signals times
[1:35] four signals times
[1:35] four signals times whatever frequency it is that you're
[1:37] whatever frequency it is that you're
[1:37] whatever frequency it is that you're asking for so let's look at the software
[1:40] asking for so let's look at the software
[1:40] asking for so let's look at the software and and try to take a look at how much
[1:43] and and try to take a look at how much
[1:43] and and try to take a look at how much this will ask
[1:43] this will ask
[1:43] this will ask from our processor so here on my
[1:47] from our processor so here on my
[1:47] from our processor so here on my computer i connected with the terminal
[1:49] computer i connected with the terminal
[1:49] computer i connected with the terminal to my raspberry pi and i'm going to run
[1:52] to my raspberry pi and i'm going to run
[1:52] to my raspberry pi and i'm going to run a program called l1 motor dot pi
[1:57] a program called l1 motor dot pi
[1:57] a program called l1 motor dot pi let me open it up first using nano
[2:00] let me open it up first using nano
[2:00] let me open it up first using nano and we can see that i have
[2:03] and we can see that i have
[2:03] and we can see that i have four channels being output left and
[2:06] four channels being output left and
[2:06] four channels being output left and right times a and b
[2:07] right times a and b
[2:07] right times a and b and the frequency right now is 15 000.
[2:11] and the frequency right now is 15 000.
[2:11] and the frequency right now is 15 000. so the default frequency where we
[2:14] so the default frequency where we
[2:14] so the default frequency where we started with
[2:14] started with
[2:14] started with or something suggested by
[2:18] or something suggested by
[2:18] or something suggested by the an example program is fairly low at
[2:21] the an example program is fairly low at
[2:22] the an example program is fairly low at 150 and this is where we
[2:23] 150 and this is where we
[2:23] 150 and this is where we don't get the best performance out of
[2:25] don't get the best performance out of
[2:25] don't get the best performance out of the motor
[2:26] the motor
[2:26] the motor so i'll save this i'm going to exit now
[2:30] so i'll save this i'm going to exit now
[2:30] so i'll save this i'm going to exit now and i'll run it so python 301 motor
[2:34] and i'll run it so python 301 motor
[2:34] and i'll run it so python 301 motor and then i'll come back to my other
[2:36] and then i'll come back to my other
[2:36] and then i'll come back to my other terminal connected to the same computer
[2:39] terminal connected to the same computer
[2:39] terminal connected to the same computer and you can see if you type in h top you
[2:42] and you can see if you type in h top you
[2:42] and you can see if you type in h top you can check the processes that are running
[2:45] can check the processes that are running
[2:45] can check the processes that are running so we have four times this process the
[2:48] so we have four times this process the
[2:48] so we have four times this process the python 3
[2:49] python 3
[2:49] python 3 l1 motor dot pi and they bounce around
[2:52] l1 motor dot pi and they bounce around
[2:52] l1 motor dot pi and they bounce around in the sequence but essentially we have
[3:00] we have the cpu being consumed at
[3:00] we have the cpu being consumed at 2 3.3 percent 1.3
[3:04] 2 3.3 percent 1.3
[3:04] 2 3.3 percent 1.3 1.3 0.7 okay it's a changing number
[3:08] 1.3 0.7 okay it's a changing number
[3:08] 1.3 0.7 okay it's a changing number but i took a screenshot of this and then
[3:10] but i took a screenshot of this and then
[3:10] but i took a screenshot of this and then i varied
[3:11] i varied
[3:11] i varied uh the frequency of these um
[3:15] uh the frequency of these um
[3:15] uh the frequency of these um of the motor driving
[3:18] of the motor driving
[3:18] of the motor driving and then i took my screenshots
[3:21] and then i took my screenshots
[3:21] and then i took my screenshots at different frequencies to check i
[3:23] at different frequencies to check i
[3:23] at different frequencies to check i should note
[3:24] should note
[3:24] should note that we have four different bars
[3:27] that we have four different bars
[3:27] that we have four different bars corresponding to the processor so maybe
[3:29] corresponding to the processor so maybe
[3:29] corresponding to the processor so maybe there are four
[3:31] there are four
[3:31] there are four threads that can run on my version of
[3:33] threads that can run on my version of
[3:33] threads that can run on my version of the raspberry this one
[3:34] the raspberry this one
[3:34] the raspberry this one happens to be the the pi
[3:37] happens to be the the pi
[3:37] happens to be the the pi 3b plus so um for my results i
[3:41] 3b plus so um for my results i
[3:41] 3b plus so um for my results i added up the percentages by each of them
[3:44] added up the percentages by each of them
[3:44] added up the percentages by each of them and
[3:44] and
[3:44] and what i got was pretty interesting and
[3:48] what i got was pretty interesting and
[3:48] what i got was pretty interesting and keep in mind this is a a crude uh kind
[3:51] keep in mind this is a a crude uh kind
[3:51] keep in mind this is a a crude uh kind of
[3:51] of
[3:51] of experiment but it's just to get an idea
[3:54] experiment but it's just to get an idea
[3:54] experiment but it's just to get an idea at 150 hertz
[3:55] at 150 hertz
[3:55] at 150 hertz of four signals we were only using a
[3:58] of four signals we were only using a
[3:58] of four signals we were only using a total
[3:59] total
[3:59] total of less than four percent at 1 500 hertz
[4:02] of less than four percent at 1 500 hertz
[4:02] of less than four percent at 1 500 hertz which is
[4:03] which is
[4:04] which is kind of minimal in my experience to get
[4:07] kind of minimal in my experience to get
[4:07] kind of minimal in my experience to get the motors to start
[4:08] the motors to start
[4:08] the motors to start sounding smooth and when you grip them
[4:10] sounding smooth and when you grip them
[4:10] sounding smooth and when you grip them while you're giving them a
[4:12] while you're giving them a
[4:12] while you're giving them a 90 duty cycle you grip the motor and you
[4:15] 90 duty cycle you grip the motor and you
[4:15] 90 duty cycle you grip the motor and you can feel that it's giving you a nice
[4:16] can feel that it's giving you a nice
[4:16] can feel that it's giving you a nice torque
[4:17] torque
[4:17] torque not so much true at 150 hertz or 50
[4:20] not so much true at 150 hertz or 50
[4:20] not so much true at 150 hertz or 50 hertz
[4:21] hertz
[4:21] hertz um this is using 30 percent
[4:24] um this is using 30 percent
[4:24] um this is using 30 percent almost sorry 23 of uh
[4:28] almost sorry 23 of uh
[4:28] almost sorry 23 of uh of the processor um maybe that's
[4:30] of the processor um maybe that's
[4:30] of the processor um maybe that's actually 23
[4:32] actually 23
[4:32] actually 23 of 400 but still very significant
[4:35] of 400 but still very significant
[4:35] of 400 but still very significant and it i would potentially want to go up
[4:39] and it i would potentially want to go up
[4:39] and it i would potentially want to go up into the kilohertz
[4:40] into the kilohertz
[4:40] into the kilohertz region like 15 kilohertz in that case
[4:42] region like 15 kilohertz in that case
[4:42] region like 15 kilohertz in that case you've consumed
[4:44] you've consumed
[4:44] you've consumed what totals to be 108 percent
[4:47] what totals to be 108 percent
[4:48] what totals to be 108 percent this is what it looked like python 3's
[4:50] this is what it looked like python 3's
[4:50] this is what it looked like python 3's up here in the
[4:52] up here in the
[4:52] up here in the cpu 29 24
[4:55] cpu 29 24
[4:55] cpu 29 24 23 percent uh consumption
[4:58] 23 percent uh consumption
[4:58] 23 percent uh consumption so i i would
[5:01] so i i would
[5:01] so i i would be interested to learn uh more precisely
[5:05] be interested to learn uh more precisely
[5:05] be interested to learn uh more precisely what these numbers mean and what they
[5:07] what these numbers mean and what they
[5:07] what these numbers mean and what they correspond to
[5:08] correspond to
[5:08] correspond to but you can notice when you're running a
[5:10] but you can notice when you're running a
[5:10] but you can notice when you're running a program
[5:11] program
[5:11] program that um the
[5:15] that um the
[5:15] that um the the response of other parts of your
[5:18] the response of other parts of your
[5:18] the response of other parts of your program
[5:18] program
[5:18] program don't always go as fast when you're
[5:21] don't always go as fast when you're
[5:21] don't always go as fast when you're running
[5:21] running
[5:22] running the motors at a higher frequency and
[5:24] the motors at a higher frequency and
[5:24] the motors at a higher frequency and that's a pretty major drawback so
[5:26] that's a pretty major drawback so
[5:26] that's a pretty major drawback so our next step is to to take this
[5:34] to take this and use um outputs
[5:34] to take this and use um outputs 12 and 13 which correspond to actual
[5:38] 12 and 13 which correspond to actual
[5:38] 12 and 13 which correspond to actual hardware-based um pwm
[5:41] hardware-based um pwm
[5:41] hardware-based um pwm cycles and then we're gonna we're gonna
[5:45] cycles and then we're gonna we're gonna
[5:45] cycles and then we're gonna we're gonna run a daemon and tap into the hardware
[5:48] run a daemon and tap into the hardware
[5:48] run a daemon and tap into the hardware capabilities
[5:49] capabilities
[5:49] capabilities and at least convert two of our signals
[5:52] and at least convert two of our signals
[5:52] and at least convert two of our signals over to hardware
[5:53] over to hardware
[5:53] over to hardware and i'll publish a video when i can get
[5:56] and i'll publish a video when i can get
[5:56] and i'll publish a video when i can get to that

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
