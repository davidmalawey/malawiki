---
title: "How to connect a Hobby ESC (speed control) to raspberry Pi - drive a 12v DC motor bi-directionally"
url: "https://www.youtube.com/watch?v=zvbN1lPjd-I"
video_id: "zvbN1lPjd-I"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2021-02-09
duration: "5:36"
duration_sec: 336
views: 2334
likes: 15
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/zvbN1lPjd-I/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 258
chapters_count: 0
has_description: true
has_comments: false
---

## Description

This is a cheap off-the-shelf Electronic Speed Control rated at 320A (is it legitimate?) commonly used for RC cars.  In this video I made Python code that allows our raspberry pi (or beaglebone) to drive the motors and we use a gamepad for user inputs.

Example ESC around $15 at Amazon:
https://amzn.to/3aMgSot

Example ESC around $18 at Walmart: 
https://bit.ly/3a4cXUX

SCUTTLE Robot Project documentation: 
https://mxet.github.io/SCUTTLE

## Transcript

[0:03] okay i just want to quickly show
[0:03] okay i just want to quickly show uh the software i threw together to test
[0:05] uh the software i threw together to test
[0:05] uh the software i threw together to test this brushed
[0:07] this brushed
[0:07] this brushed dc motor driver that's pretty standard
[0:10] dc motor driver that's pretty standard
[0:10] dc motor driver that's pretty standard for
[0:11] for
[0:11] for the older and semi-recent
[0:14] the older and semi-recent
[0:14] the older and semi-recent remote control cars i'm using the game
[0:16] remote control cars i'm using the game
[0:16] remote control cars i'm using the game pad that we always use
[0:17] pad that we always use
[0:17] pad that we always use for scuttle and um you can see that i've
[0:21] for scuttle and um you can see that i've
[0:21] for scuttle and um you can see that i've got it hooked up it's got the little
[0:23] got it hooked up it's got the little
[0:23] got it hooked up it's got the little light that comes on there in the back
[0:26] light that comes on there in the back
[0:26] light that comes on there in the back and the pulse width is what determines
[0:29] and the pulse width is what determines
[0:29] and the pulse width is what determines the speed
[0:30] the speed
[0:30] the speed that i'm sending as a command but
[0:32] that i'm sending as a command but
[0:32] that i'm sending as a command but there's a few extra details to this
[0:34] there's a few extra details to this
[0:34] there's a few extra details to this kind of esc so i'm going to jump into
[0:37] kind of esc so i'm going to jump into
[0:37] kind of esc so i'm going to jump into the frame and show you the gamepad and
[0:39] the frame and show you the gamepad and
[0:39] the frame and show you the gamepad and then i'll come back to the code
[1:04] okay so now you know what my thumb is
[1:04] okay so now you know what my thumb is doing to send these commands
[1:06] doing to send these commands
[1:06] doing to send these commands and um the first column on the printout
[1:09] and um the first column on the printout
[1:09] and um the first column on the printout is the axis
[1:10] is the axis
[1:10] is the axis that's the the value that it's capturing
[1:12] that's the the value that it's capturing
[1:12] that's the the value that it's capturing from the gamepad itself
[1:15] from the gamepad itself
[1:15] from the gamepad itself it goes from one to
[1:19] it goes from one to
[1:19] it goes from one to negative one that's the limits that you
[1:21] negative one that's the limits that you
[1:21] negative one that's the limits that you can send to the gamepad
[1:23] can send to the gamepad
[1:23] can send to the gamepad but um it doesn't exactly get translated
[1:26] but um it doesn't exactly get translated
[1:26] but um it doesn't exactly get translated to
[1:27] to
[1:27] to the motor this motor controller is
[1:30] the motor this motor controller is
[1:30] the motor this motor controller is based on the hobby kind of standard
[1:32] based on the hobby kind of standard
[1:32] based on the hobby kind of standard where 50 hertz is the speed
[1:35] where 50 hertz is the speed
[1:35] where 50 hertz is the speed of the um the frequency of the signal
[1:38] of the um the frequency of the signal
[1:38] of the um the frequency of the signal that goes out
[1:39] that goes out
[1:40] that goes out and then the pulse width ranges from um
[1:44] and then the pulse width ranges from um
[1:44] and then the pulse width ranges from um one millisecond to two milliseconds and
[1:46] one millisecond to two milliseconds and
[1:46] one millisecond to two milliseconds and i'll pull up i'll just show a little
[1:49] i'll pull up i'll just show a little
[1:49] i'll pull up i'll just show a little reference on that
[1:51] reference on that
[1:51] reference on that from one of my favorite
[1:55] from one of my favorite
[1:55] from one of my favorite favorite websites ever let's see if we
[1:57] favorite websites ever let's see if we
[1:57] favorite websites ever let's see if we can get this here
[1:59] can get this here
[1:59] can get this here so this is from last minute engineers
[2:03] so this is from last minute engineers
[2:03] so this is from last minute engineers you you can visit this page and you can
[2:06] you you can visit this page and you can
[2:06] you you can visit this page and you can see
[2:07] see
[2:07] see the standard is one millisecond is the
[2:10] the standard is one millisecond is the
[2:10] the standard is one millisecond is the minimum
[2:10] minimum
[2:10] minimum and yes that's a servo two milliseconds
[2:13] and yes that's a servo two milliseconds
[2:13] and yes that's a servo two milliseconds is the maximum
[2:14] is the maximum
[2:14] is the maximum that's um that's for 180 degree servo
[2:17] that's um that's for 180 degree servo
[2:17] that's um that's for 180 degree servo but it's also the same signal pattern
[2:19] but it's also the same signal pattern
[2:19] but it's also the same signal pattern you send out
[2:20] you send out
[2:20] you send out for motors okay so when we're testing
[2:24] for motors okay so when we're testing
[2:24] for motors okay so when we're testing um what is the proper signal to get this
[2:27] um what is the proper signal to get this
[2:27] um what is the proper signal to get this motor driver to send the maximum and
[2:30] motor driver to send the maximum and
[2:30] motor driver to send the maximum and minimum
[2:31] minimum
[2:31] minimum voltages it's is shown here so i'm
[2:34] voltages it's is shown here so i'm
[2:34] voltages it's is shown here so i'm mapping
[2:36] mapping
[2:36] mapping my gamepad axis to some kind of
[2:39] my gamepad axis to some kind of
[2:39] my gamepad axis to some kind of pulse width which is
[2:42] pulse width which is
[2:42] pulse width which is here at the maximum i've got 11 percent
[2:46] here at the maximum i've got 11 percent
[2:46] here at the maximum i've got 11 percent of a 20 millisecond
[2:54] duty cycle 20 millisecond period gives
[2:54] duty cycle 20 millisecond period gives me close to a little bit more than two
[2:56] me close to a little bit more than two
[2:56] me close to a little bit more than two milliseconds
[2:57] milliseconds
[2:57] milliseconds because each one of these is calibrated
[2:59] because each one of these is calibrated
[2:59] because each one of these is calibrated a little differently
[3:00] a little differently
[3:00] a little differently then if i go on the negative side i
[3:03] then if i go on the negative side i
[3:03] then if i go on the negative side i found that
[3:11] point five one point five
[3:11] point five one point five four eight milliseconds doesn't sound
[3:13] four eight milliseconds doesn't sound
[3:13] four eight milliseconds doesn't sound any different than
[3:15] any different than
[3:15] any different than point five four you see
[3:22] so there's a there's a point at which
[3:22] so there's a there's a point at which the the control
[3:23] the the control
[3:23] the the control saturates and there's actually no more
[3:25] saturates and there's actually no more
[3:25] saturates and there's actually no more change
[3:26] change
[3:26] change and if you go way out of the range then
[3:28] and if you go way out of the range then
[3:28] and if you go way out of the range then it won't respond at all
[3:29] it won't respond at all
[3:29] it won't respond at all and then finally the last nuance that
[3:31] and then finally the last nuance that
[3:31] and then finally the last nuance that needs to be tested is
[3:33] needs to be tested is
[3:33] needs to be tested is when you find the middle point you'll
[3:35] when you find the middle point you'll
[3:35] when you find the middle point you'll find that you can't just
[3:37] find that you can't just
[3:37] find that you can't just switch from forward to reverse
[3:40] switch from forward to reverse
[3:40] switch from forward to reverse you can from reverse to forward but
[3:41] you can from reverse to forward but
[3:41] you can from reverse to forward but forward to reverse means watch i'll just
[3:44] forward to reverse means watch i'll just
[3:44] forward to reverse means watch i'll just i'll flip my axis right now see it
[3:47] i'll flip my axis right now see it
[3:47] i'll flip my axis right now see it doesn't listen it doesn't like it
[3:48] doesn't listen it doesn't like it
[3:48] doesn't listen it doesn't like it because
[3:49] because
[3:49] because first it needs to see that pulse width
[3:52] first it needs to see that pulse width
[3:52] first it needs to see that pulse width that corresponds to the neutral and i
[3:55] that corresponds to the neutral and i
[3:55] that corresponds to the neutral and i found right now that
[3:56] found right now that
[3:56] found right now that the neutral is about 1.3 milliseconds
[3:59] the neutral is about 1.3 milliseconds
[3:59] the neutral is about 1.3 milliseconds and it's about
[4:00] and it's about
[4:00] and it's about um point six point five percent
[4:04] um point six point five percent
[4:04] um point six point five percent sorry this this percent down here is not
[4:06] sorry this this percent down here is not
[4:06] sorry this this percent down here is not exactly percent it's fraction
[4:08] exactly percent it's fraction
[4:08] exactly percent it's fraction a fraction of one so then after i go
[4:11] a fraction of one so then after i go
[4:12] a fraction of one so then after i go to the near zero point and sudden that
[4:14] to the near zero point and sudden that
[4:14] to the near zero point and sudden that signal then i can go to reverse
[4:17] signal then i can go to reverse
[4:17] signal then i can go to reverse and it'll follow my commands so this is
[4:19] and it'll follow my commands so this is
[4:19] and it'll follow my commands so this is how you
[4:20] how you
[4:20] how you the easiest way to find your center
[4:22] the easiest way to find your center
[4:22] the easiest way to find your center point is just allow it to sweep
[4:24] point is just allow it to sweep
[4:24] point is just allow it to sweep to above and below this 20 milliseconds
[4:28] to above and below this 20 milliseconds
[4:28] to above and below this 20 milliseconds and 2 milliseconds sorry 1 and 2
[4:30] and 2 milliseconds sorry 1 and 2
[4:30] and 2 milliseconds sorry 1 and 2 milliseconds
[4:32] milliseconds
[4:32] milliseconds gradually sweep through it with some
[4:33] gradually sweep through it with some
[4:33] gradually sweep through it with some kind of analog control and then you will
[4:35] kind of analog control and then you will
[4:35] kind of analog control and then you will find
[4:36] find
[4:36] find what's the the midsection for your
[4:38] what's the the midsection for your
[4:38] what's the the midsection for your controller
[4:40] controller
[4:40] controller and this is an awesome value for this um
[4:42] and this is an awesome value for this um
[4:42] and this is an awesome value for this um this
[4:43] this
[4:43] this brushed dc motor controller because
[4:46] brushed dc motor controller because
[4:46] brushed dc motor controller because um it has uh
[4:50] um it has uh
[4:50] um it has uh it has up to 320 amps that's what it
[4:53] it has up to 320 amps that's what it
[4:53] it has up to 320 amps that's what it claims maybe i
[4:54] claims maybe i
[4:54] claims maybe i won't try to push it that hard but it
[4:56] won't try to push it that hard but it
[4:56] won't try to push it that hard but it can take almost double the voltage that
[4:58] can take almost double the voltage that
[4:58] can take almost double the voltage that we're using it can take
[5:01] we're using it can take
[5:01] we're using it can take a lot of current it can pass current to
[5:04] a lot of current it can pass current to
[5:04] a lot of current it can pass current to two motors simultaneously
[5:06] two motors simultaneously
[5:06] two motors simultaneously it's quite robust and the value is very
[5:09] it's quite robust and the value is very
[5:09] it's quite robust and the value is very good because it's only
[5:10] good because it's only
[5:10] good because it's only i mean this was less than 10 u.s dollars
[5:14] i mean this was less than 10 u.s dollars
[5:14] i mean this was less than 10 u.s dollars it was like
[5:15] it was like
[5:15] it was like closer to five us dollars um
[5:18] closer to five us dollars um
[5:18] closer to five us dollars um and and these are available in many
[5:21] and and these are available in many
[5:21] and and these are available in many different variations so it's a really
[5:22] different variations so it's a really
[5:22] different variations so it's a really good value
[5:23] good value
[5:24] good value if you want a more high performance
[5:25] if you want a more high performance
[5:25] if you want a more high performance motor driver
[5:27] motor driver
[5:27] motor driver than the the plane h bridge like l298n
[5:31] than the the plane h bridge like l298n
[5:31] than the the plane h bridge like l298n or the one we've got on scuttle

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
