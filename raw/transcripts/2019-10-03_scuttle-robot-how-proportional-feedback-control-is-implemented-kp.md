---
title: "SCUTTLE Robot - How Proportional Feedback Control is Implemented (kp)"
url: "https://www.youtube.com/watch?v=yt89x3SFG8A"
video_id: "yt89x3SFG8A"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-10-03
duration: "7:36"
duration_sec: 456
views: 156
likes: 5
category: "Education"
keywords: ["yt:cc=on control systems"]
thumbnail_url: "https://i.ytimg.com/vi/yt89x3SFG8A/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 312
chapters_count: 0
has_description: true
has_comments: false
---

## Description

a demonstration and walkthrough of the calculation of kp and the control effort based on a kp (proportional) control value, and how it drives the wheels in our robot.

## Transcript

[0:02] this short video will demonstrate
[0:02] this short video will demonstrate proportional control on the scuttle
[0:05] proportional control on the scuttle
[0:05] proportional control on the scuttle robot so first of all we're running a
[0:10] robot so first of all we're running a
[0:10] robot so first of all we're running a program called
[0:11] program called
[0:11] program called well L three PID lab and we're calling a
[0:16] well L three PID lab and we're calling a
[0:16] well L three PID lab and we're calling a loop that is asking to drive in the
[0:19] loop that is asking to drive in the
[0:19] loop that is asking to drive in the closed-loop feedback control method to
[0:23] closed-loop feedback control method to
[0:23] closed-loop feedback control method to reach a certain Phi dot targets for left
[0:25] reach a certain Phi dot targets for left
[0:25] reach a certain Phi dot targets for left and right wheel speeds and it feeds in
[0:29] and right wheel speeds and it feeds in
[0:29] and right wheel speeds and it feeds in the current five dots that are being
[0:30] the current five dots that are being
[0:30] the current five dots that are being measured in real-time and it feeds in
[0:33] measured in real-time and it feeds in
[0:33] measured in real-time and it feeds in the the Delta in time from the previous
[0:36] the the Delta in time from the previous
[0:36] the the Delta in time from the previous sample to the current sample so that
[0:38] sample to the current sample so that
[0:38] sample to the current sample so that derivative control can be implemented if
[0:42] derivative control can be implemented if
[0:42] derivative control can be implemented if necessary but right now we're just
[0:43] necessary but right now we're just
[0:43] necessary but right now we're just dealing with proportional so what else I
[0:48] dealing with proportional so what else I
[0:48] dealing with proportional so what else I have implemented is that we're pulling
[0:50] have implemented is that we're pulling
[0:50] have implemented is that we're pulling the KP value which is going to be the
[0:53] the KP value which is going to be the
[0:53] the KP value which is going to be the proportional control constant we're
[0:55] proportional control constant we're
[0:55] proportional control constant we're pulling that from a file that we're
[0:57] pulling that from a file that we're
[0:57] pulling that from a file that we're setting in real time where 0.04 is our
[1:02] setting in real time where 0.04 is our
[1:02] setting in real time where 0.04 is our nominal it's kind of our starting point
[1:04] nominal it's kind of our starting point
[1:04] nominal it's kind of our starting point but after we get sampling we're going to
[1:07] but after we get sampling we're going to
[1:07] but after we get sampling we're going to pull the value from KP txt and that is
[1:13] pull the value from KP txt and that is
[1:13] pull the value from KP txt and that is over here and I won't open it up so I
[1:17] over here and I won't open it up so I
[1:17] over here and I won't open it up so I don't break anything but it's basically
[1:19] don't break anything but it's basically
[1:19] don't break anything but it's basically going to come from the node-red
[1:20] going to come from the node-red
[1:20] going to come from the node-red dashboard I have three tabs the
[1:24] dashboard I have three tabs the
[1:24] dashboard I have three tabs the kinematics tab right now is measuring
[1:26] kinematics tab right now is measuring
[1:26] kinematics tab right now is measuring the Phi dot left and Phi dot right wheel
[1:28] the Phi dot left and Phi dot right wheel
[1:28] the Phi dot left and Phi dot right wheel speeds in radians per second and right
[1:31] speeds in radians per second and right
[1:31] speeds in radians per second and right now they're going almost as slow as they
[1:33] now they're going almost as slow as they
[1:33] now they're going almost as slow as they can go before they stop about 1.5
[1:37] can go before they stop about 1.5
[1:37] can go before they stop about 1.5 radians per second and obviously they're
[1:40] radians per second and obviously they're
[1:40] radians per second and obviously they're oscillating this is not the Phi dot this
[1:43] oscillating this is not the Phi dot this
[1:43] oscillating this is not the Phi dot this is actual encoder reading so disregard
[1:45] is actual encoder reading so disregard
[1:45] is actual encoder reading so disregard disregard the encoder readings for right
[1:47] disregard the encoder readings for right
[1:47] disregard the encoder readings for right now so let's go to our code in here
[1:51] now so let's go to our code in here
[1:51] now so let's go to our code in here we've set our Phi dot targets to be
[1:55] we've set our Phi dot targets to be
[1:55] we've set our Phi dot targets to be we're feeding the Phi dot targets left
[1:58] we're feeding the Phi dot targets left
[1:58] we're feeding the Phi dot targets left and right that's in the speed control
[2:01] and right that's in the speed control
[2:01] and right that's in the speed control and in our level three function or level
[2:05] and in our level three function or level
[2:05] and in our level three function or level three program we are choosing our
[2:07] three program we are choosing our
[2:07] three program we are choosing our targets so right now it's nine point
[2:09] targets so right now it's nine point
[2:09] targets so right now it's nine point seven radians per second
[2:12] seven radians per second
[2:12] seven radians per second for both left and right wheels and
[2:14] for both left and right wheels and
[2:14] for both left and right wheels and clearly based on our dashboard we're not
[2:17] clearly based on our dashboard we're not
[2:17] clearly based on our dashboard we're not getting nine point seven radians per
[2:19] getting nine point seven radians per
[2:19] getting nine point seven radians per second so let's show how this is being
[2:22] second so let's show how this is being
[2:22] second so let's show how this is being implemented first of all the control is
[2:26] implemented first of all the control is
[2:26] implemented first of all the control is the is just driving the KP value right
[2:30] the is just driving the KP value right
[2:30] the is just driving the KP value right now it's set to 0.04 we can increase it
[2:33] now it's set to 0.04 we can increase it
[2:33] now it's set to 0.04 we can increase it to 0.05 and you will observe a small
[2:38] to 0.05 and you will observe a small
[2:38] to 0.05 and you will observe a small increase in these wheel speeds even
[2:40] increase in these wheel speeds even
[2:40] increase in these wheel speeds even though we didn't change the targets and
[2:42] though we didn't change the targets and
[2:42] though we didn't change the targets and here's how that's calculated this is
[2:46] here's how that's calculated this is
[2:46] here's how that's calculated this is just using an example of wheel speeds
[2:49] just using an example of wheel speeds
[2:49] just using an example of wheel speeds that have been logged to a log file
[2:51] that have been logged to a log file
[2:51] that have been logged to a log file these are sample numbers that are
[2:53] these are sample numbers that are
[2:53] these are sample numbers that are separated by I think less than a tenth
[2:56] separated by I think less than a tenth
[2:56] separated by I think less than a tenth of a second the speed that we were
[2:59] of a second the speed that we were
[2:59] of a second the speed that we were achieving understand that the speed also
[3:03] achieving understand that the speed also
[3:03] achieving understand that the speed also has its own error based on the encoder
[3:05] has its own error based on the encoder
[3:05] has its own error based on the encoder the encoder roll over and the encoder
[3:08] the encoder roll over and the encoder
[3:08] the encoder roll over and the encoder sampling rate and the encoder resolution
[3:10] sampling rate and the encoder resolution
[3:10] sampling rate and the encoder resolution and then we have our target so for any
[3:13] and then we have our target so for any
[3:13] and then we have our target so for any control system your error will be
[3:16] control system your error will be
[3:16] control system your error will be defined as the difference between the
[3:19] defined as the difference between the
[3:19] defined as the difference between the target value and the current value so in
[3:22] target value and the current value so in
[3:22] target value and the current value so in our case this error is calculated by
[3:25] our case this error is calculated by
[3:25] our case this error is calculated by nine point seven minus one point three
[3:27] nine point seven minus one point three
[3:27] nine point seven minus one point three six so in a previous iteration where our
[3:30] six so in a previous iteration where our
[3:30] six so in a previous iteration where our target was constant and our speed was
[3:33] target was constant and our speed was
[3:33] target was constant and our speed was far lower than nine point seven that
[3:36] far lower than nine point seven that
[3:36] far lower than nine point seven that gives us an error of eight point three
[3:38] gives us an error of eight point three
[3:38] gives us an error of eight point three so how does the KP value get implemented
[3:41] so how does the KP value get implemented
[3:41] so how does the KP value get implemented well what the KP value does is it says
[3:44] well what the KP value does is it says
[3:44] well what the KP value does is it says we're going to proportionally control
[3:46] we're going to proportionally control
[3:46] we're going to proportionally control our driver or our actuator in this case
[3:49] our driver or our actuator in this case
[3:49] our driver or our actuator in this case it's a PWM output on our motor drivers
[3:52] it's a PWM output on our motor drivers
[3:52] it's a PWM output on our motor drivers we're going to proportionately control
[3:54] we're going to proportionately control
[3:54] we're going to proportionately control that by point zero four times whatever
[3:57] that by point zero four times whatever
[3:57] that by point zero four times whatever error we've discovered so in this case
[4:00] error we've discovered so in this case
[4:00] error we've discovered so in this case if our KP is 0.04 and our error is eight
[4:04] if our KP is 0.04 and our error is eight
[4:04] if our KP is 0.04 and our error is eight point three understand that in the very
[4:07] point three understand that in the very
[4:07] point three understand that in the very first sample our error is going to be
[4:09] first sample our error is going to be
[4:09] first sample our error is going to be the entire target because the speed is
[4:12] the entire target because the speed is
[4:12] the entire target because the speed is zero but if we have a some nominal error
[4:15] zero but if we have a some nominal error
[4:15] zero but if we have a some nominal error around seven or eight we're going to
[4:17] around seven or eight we're going to
[4:17] around seven or eight we're going to multiply that by our KP and then we're
[4:19] multiply that by our KP and then we're
[4:19] multiply that by our KP and then we're going to feed that value to the motor
[4:22] going to feed that value to the motor
[4:22] going to feed that value to the motor driver so 0.33 is
[4:25] driver so 0.33 is
[4:25] driver so 0.33 is going to be the full control effort in
[4:27] going to be the full control effort in
[4:27] going to be the full control effort in this case we call that u P or u sub P
[4:30] this case we call that u P or u sub P
[4:30] this case we call that u P or u sub P and u sub P is going to be 0.33 and that
[4:35] and u sub P is going to be 0.33 and that
[4:35] and u sub P is going to be 0.33 and that will also equal u total since we're not
[4:39] will also equal u total since we're not
[4:39] will also equal u total since we're not using integral or derivative control
[4:42] using integral or derivative control
[4:42] using integral or derivative control then this 0.33 will mean that
[4:45] then this 0.33 will mean that
[4:45] then this 0.33 will mean that thirty-three out of a hundred
[4:48] thirty-three out of a hundred
[4:48] thirty-three out of a hundred basically 33 percent of the time our
[4:51] basically 33 percent of the time our
[4:51] basically 33 percent of the time our signal to the motor driver will be high
[4:54] signal to the motor driver will be high
[4:54] signal to the motor driver will be high and the remainder of the time the signal
[4:56] and the remainder of the time the signal
[4:56] and the remainder of the time the signal will be low so when we have twelve volts
[4:59] will be low so when we have twelve volts
[4:59] will be low so when we have twelve volts coming into our motor driver and only
[5:02] coming into our motor driver and only
[5:02] coming into our motor driver and only 0.33 out of one times that twelve volts
[5:06] 0.33 out of one times that twelve volts
[5:06] 0.33 out of one times that twelve volts is going to be passed to the motors in
[5:08] is going to be passed to the motors in
[5:08] is going to be passed to the motors in the result we have a speed that's far
[5:12] the result we have a speed that's far
[5:12] the result we have a speed that's far less than the maximum speed just so that
[5:15] less than the maximum speed just so that
[5:15] less than the maximum speed just so that you know our our typical maximum speed
[5:19] you know our our typical maximum speed
[5:19] you know our our typical maximum speed when the the vehicles on the ground and
[5:22] when the the vehicles on the ground and
[5:22] when the the vehicles on the ground and unloaded the maximum speed typically is
[5:25] unloaded the maximum speed typically is
[5:25] unloaded the maximum speed typically is nine point seven so if you gave a duty
[5:27] nine point seven so if you gave a duty
[5:27] nine point seven so if you gave a duty cycle of 100% to the motors with twelve
[5:31] cycle of 100% to the motors with twelve
[5:31] cycle of 100% to the motors with twelve volts on the ground you would achieve
[5:32] volts on the ground you would achieve
[5:32] volts on the ground you would achieve somewhere around nine point seven
[5:34] somewhere around nine point seven
[5:34] somewhere around nine point seven radians per second on left and right
[5:36] radians per second on left and right
[5:36] radians per second on left and right wheels in this case we're only giving
[5:39] wheels in this case we're only giving
[5:39] wheels in this case we're only giving about a third of the voltage and it's
[5:41] about a third of the voltage and it's
[5:41] about a third of the voltage and it's just barely enough to actually drive
[5:44] just barely enough to actually drive
[5:44] just barely enough to actually drive those wheels from a standstill since the
[5:47] those wheels from a standstill since the
[5:47] those wheels from a standstill since the motor Specht at 12 volts it's not very
[5:51] motor Specht at 12 volts it's not very
[5:51] motor Specht at 12 volts it's not very typical to ask that motor to even move
[5:53] typical to ask that motor to even move
[5:53] typical to ask that motor to even move at all under load when you're only
[5:56] at all under load when you're only
[5:56] at all under load when you're only giving it less than half of the voltage
[5:58] giving it less than half of the voltage
[5:58] giving it less than half of the voltage so we come over here and we can increase
[6:02] so we come over here and we can increase
[6:02] so we come over here and we can increase our KP right now it's 0.05 we can
[6:05] our KP right now it's 0.05 we can
[6:05] our KP right now it's 0.05 we can increase that to let's say point O seven
[6:07] increase that to let's say point O seven
[6:08] increase that to let's say point O seven and audibly you can't hear on the
[6:10] and audibly you can't hear on the
[6:10] and audibly you can't hear on the microphone but I can hear my wheels have
[6:13] microphone but I can hear my wheels have
[6:13] microphone but I can hear my wheels have increased in their speed and right now
[6:15] increased in their speed and right now
[6:15] increased in their speed and right now we're achieving about 3.5 to 4 radians
[6:20] we're achieving about 3.5 to 4 radians
[6:20] we're achieving about 3.5 to 4 radians per second so that means when the new
[6:23] per second so that means when the new
[6:23] per second so that means when the new value is calculated for the control
[6:26] value is calculated for the control
[6:26] value is calculated for the control signal it's actually not going to give
[6:29] signal it's actually not going to give
[6:29] signal it's actually not going to give you point O 4 or it's not going to give
[6:32] you point O 4 or it's not going to give
[6:32] you point O 4 or it's not going to give you point o 7 times the original error
[6:36] you point o 7 times the original error
[6:36] you point o 7 times the original error it's going to give you point of
[6:39] it's going to give you point of
[6:39] it's going to give you point of seven this is what you'd get
[6:43] seven this is what you'd get
[6:43] seven this is what you'd get instantaneously you'd get 58 percent
[6:46] instantaneously you'd get 58 percent
[6:46] instantaneously you'd get 58 percent duty cycle but since our new speed is
[6:49] duty cycle but since our new speed is
[6:49] duty cycle but since our new speed is actually somewhere around 4.5 radians
[6:52] actually somewhere around 4.5 radians
[6:52] actually somewhere around 4.5 radians per second we're still back down to a
[6:55] per second we're still back down to a
[6:55] per second we're still back down to a little bit lower KP and then we're going
[6:57] little bit lower KP and then we're going
[6:58] little bit lower KP and then we're going to have these oscillations where the the
[7:01] to have these oscillations where the the
[7:01] to have these oscillations where the the motors swing up up and down and the
[7:03] motors swing up up and down and the
[7:03] motors swing up up and down and the further they once they the control
[7:06] further they once they the control
[7:06] further they once they the control signal increases then they're closer to
[7:09] signal increases then they're closer to
[7:09] signal increases then they're closer to the target the following sample will
[7:11] the target the following sample will
[7:11] the target the following sample will decrease the control signal and when the
[7:13] decrease the control signal and when the
[7:13] decrease the control signal and when the control signal is decreased then the
[7:16] control signal is decreased then the
[7:16] control signal is decreased then the wheel speed is going to fall down again
[7:17] wheel speed is going to fall down again
[7:17] wheel speed is going to fall down again and we're going to give a higher one and
[7:20] and we're going to give a higher one and
[7:20] and we're going to give a higher one and that's how you end up with the
[7:21] that's how you end up with the
[7:22] that's how you end up with the oscillations when you're just dealing
[7:24] oscillations when you're just dealing
[7:24] oscillations when you're just dealing with KP so hopefully this gives you a
[7:27] with KP so hopefully this gives you a
[7:27] with KP so hopefully this gives you a starting point to understand KP in your
[7:30] starting point to understand KP in your
[7:30] starting point to understand KP in your control system

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
