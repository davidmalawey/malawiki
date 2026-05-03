---
title: "Reduce the Dead Band from your DC Motors with this Function"
url: "https://www.youtube.com/watch?v=sii5VDNHI-o"
video_id: "sii5VDNHI-o"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2022-02-12
duration: "6:55"
duration_sec: 415
views: 293
likes: 5
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/sii5VDNHI-o/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 343
chapters_count: 0
has_description: true
has_comments: false
---

## Description

see more mobile robotics content at www.scuttlerobot.org/videos

## Transcript

[0:03] hi everybody david here i'm going to
[0:03] hi everybody david here i'm going to explain to here in this video a little
[0:05] explain to here in this video a little
[0:05] explain to here in this video a little bit about a function that takes place in
[0:07] bit about a function that takes place in
[0:07] bit about a function that takes place in the motors.pi the motor.pi uh software
[0:11] the motors.pi the motor.pi uh software
[0:11] the motors.pi the motor.pi uh software in the scuttle library where um it's
[0:14] in the scuttle library where um it's
[0:14] in the scuttle library where um it's called compress that's the name of the
[0:16] called compress that's the name of the
[0:16] called compress that's the name of the function and it takes place
[0:19] function and it takes place
[0:19] function and it takes place uh bef after a motor duty cycle
[0:23] uh bef after a motor duty cycle
[0:23] uh bef after a motor duty cycle desired desired duty cycle is generated
[0:26] desired desired duty cycle is generated
[0:26] desired desired duty cycle is generated um and before the value gets sent out
[0:30] um and before the value gets sent out
[0:30] um and before the value gets sent out over the pwm communication uh wires to
[0:34] over the pwm communication uh wires to
[0:34] over the pwm communication uh wires to the motor driver
[0:36] the motor driver
[0:36] the motor driver so it's in this and it's just before it
[0:38] so it's in this and it's just before it
[0:38] so it's in this and it's just before it reaches these black signals here and the
[0:41] reaches these black signals here and the
[0:41] reaches these black signals here and the way
[0:42] way
[0:42] way we've depicted it in our slides is that
[0:44] we've depicted it in our slides is that
[0:44] we've depicted it in our slides is that it's this purple box here we're calling
[0:46] it's this purple box here we're calling
[0:46] it's this purple box here we're calling it compress
[0:47] it compress
[0:47] it compress and you give it a duty cycle in and
[0:50] and you give it a duty cycle in and
[0:50] and you give it a duty cycle in and output the output is also a duty cycle
[0:53] output the output is also a duty cycle
[0:53] output the output is also a duty cycle that's been adjusted
[0:54] that's been adjusted
[0:54] that's been adjusted so why would you want to adjust your
[0:57] so why would you want to adjust your
[0:57] so why would you want to adjust your duty cycle in a way that
[1:00] duty cycle in a way that
[1:00] duty cycle in a way that the controller by the way doesn't even
[1:02] the controller by the way doesn't even
[1:02] the controller by the way doesn't even know it's happening and nor does the
[1:05] know it's happening and nor does the
[1:05] know it's happening and nor does the user if you're going without a control
[1:07] user if you're going without a control
[1:07] user if you're going without a control without a pid controller and you're just
[1:09] without a pid controller and you're just
[1:09] without a pid controller and you're just using the game pad generate a signal you
[1:12] using the game pad generate a signal you
[1:12] using the game pad generate a signal you can still modify it and here's why
[1:15] can still modify it and here's why
[1:15] can still modify it and here's why um what you're looking at now is a
[1:18] um what you're looking at now is a
[1:18] um what you're looking at now is a an experiment where each color is a
[1:21] an experiment where each color is a
[1:21] an experiment where each color is a different trial but basically
[1:23] different trial but basically
[1:23] different trial but basically let's say 1500 hertz uh the gray line we
[1:27] let's say 1500 hertz uh the gray line we
[1:27] let's say 1500 hertz uh the gray line we we've basically
[1:29] we've basically
[1:29] we've basically delivered to the motors a fully negative
[1:32] delivered to the motors a fully negative
[1:33] negative duty cycle and swept it
[1:36] negative duty cycle and swept it incrementally all the way to a 100
[1:38] incrementally all the way to a 100
[1:38] incrementally all the way to a 100 forward duty cycle and then we measured
[1:42] forward duty cycle and then we measured
[1:42] forward duty cycle and then we measured on the y-axis the wheel speed that's
[1:45] on the y-axis the wheel speed that's
[1:45] on the y-axis the wheel speed that's that's resulting and as you can observe
[1:48] that's resulting and as you can observe
[1:48] that's resulting and as you can observe in all different cases we are getting
[1:50] in all different cases we are getting
[1:50] in all different cases we are getting some
[1:51] some
[1:51] some some area here in the middle which i
[1:53] some area here in the middle which i
[1:53] some area here in the middle which i will call the dead band
[1:55] will call the dead band
[1:55] will call the dead band that the the voltage is not sufficient
[1:59] that the the voltage is not sufficient
[1:59] that the the voltage is not sufficient uh being sent to the dc motors to
[2:02] uh being sent to the dc motors to
[2:02] uh being sent to the dc motors to overcome the internal friction of the
[2:04] overcome the internal friction of the
[2:04] overcome the internal friction of the motor the gearbox
[2:06] motor the gearbox
[2:06] motor the gearbox and the pulleys uh all together as an
[2:09] and the pulleys uh all together as an
[2:09] and the pulleys uh all together as an assembly
[2:10] assembly
[2:10] assembly ultimately nothing moves
[2:12] ultimately nothing moves
[2:12] ultimately nothing moves so
[2:13] so
[2:13] so um what you can do is uh
[2:16] um what you can do is uh
[2:16] um what you can do is uh run a couple trials um or
[2:19] run a couple trials um or
[2:19] run a couple trials um or or even just play with it until you can
[2:21] or even just play with it until you can
[2:21] or even just play with it until you can notice where how your dc motor is
[2:24] notice where how your dc motor is
[2:24] notice where how your dc motor is behaving they're all a little different
[2:26] behaving they're all a little different
[2:26] behaving they're all a little different from one another and then you can use
[2:28] from one another and then you can use
[2:28] from one another and then you can use that information to adjust your
[2:31] that information to adjust your
[2:31] that information to adjust your compress function so
[2:34] compress function so
[2:34] compress function so what does the compress function do there
[2:36] what does the compress function do there
[2:36] what does the compress function do there are basically two variables that are
[2:38] are basically two variables that are
[2:38] are basically two variables that are input by the user one of them is a slope
[2:41] input by the user one of them is a slope
[2:41] input by the user one of them is a slope that's the initial slope here in the
[2:43] that's the initial slope here in the
[2:43] that's the initial slope here in the middle and one of them is the y
[2:45] middle and one of them is the y
[2:45] middle and one of them is the y inflection so let me explain first what
[2:48] inflection so let me explain first what
[2:48] inflection so let me explain first what the graph means
[2:50] the graph means
[2:50] the graph means along the x-axis with the blue numbers
[2:52] along the x-axis with the blue numbers
[2:52] along the x-axis with the blue numbers this is your input to the function it's
[2:54] this is your input to the function it's
[2:54] this is your input to the function it's your initial duty cycle
[2:57] your initial duty cycle
[2:57] your initial duty cycle before
[2:58] before
[2:58] before the the algebra is run and the purple is
[3:02] the the algebra is run and the purple is
[3:02] the the algebra is run and the purple is your output it's also a duty cycle and
[3:04] your output it's also a duty cycle and
[3:04] your output it's also a duty cycle and that's what will ultimately go to the
[3:06] that's what will ultimately go to the
[3:06] that's what will ultimately go to the motor driver if you engage the function
[3:09] motor driver if you engage the function
[3:09] motor driver if you engage the function and
[3:11] and
[3:11] and basically what we are calling here the
[3:12] basically what we are calling here the
[3:12] basically what we are calling here the critical point is the
[3:15] critical point is the
[3:15] critical point is the the x
[3:17] the x
[3:17] the x value that corresponds to your y value
[3:21] value that corresponds to your y value
[3:21] value that corresponds to your y value uh that you would declare the critical y
[3:24] uh that you would declare the critical y
[3:24] uh that you would declare the critical y the the what is my duty cycle where i
[3:26] the the what is my duty cycle where i
[3:26] the the what is my duty cycle where i will actually get movement and earlier
[3:29] will actually get movement and earlier
[3:29] will actually get movement and earlier we said
[3:30] we said
[3:30] we said zero point like 15
[3:32] zero point like 15
[3:32] zero point like 15 from the recent um
[3:35] from the recent um
[3:35] from the recent um the the previous excel
[3:36] the the previous excel
[3:36] the the previous excel sheet but i just want to
[3:39] sheet but i just want to
[3:39] sheet but i just want to keep this at 0.22
[3:41] keep this at 0.22
[3:41] keep this at 0.22 for
[3:42] for
[3:42] for for saving it
[3:43] for saving it
[3:43] for saving it um and
[3:45] um and
[3:45] um and then we take a slope and we say how much
[3:47] then we take a slope and we say how much
[3:47] then we take a slope and we say how much do you want to increase
[3:49] do you want to increase
[3:49] do you want to increase the um basically the multiplier on that
[3:53] the um basically the multiplier on that
[3:53] the um basically the multiplier on that range of your uh your outputs
[3:57] range of your uh your outputs
[3:57] range of your uh your outputs if you don't if you were not to use the
[3:59] if you don't if you were not to use the
[3:59] if you don't if you were not to use the function then it would look like a slope
[4:01] function then it would look like a slope
[4:01] function then it would look like a slope of one because every output maps
[4:03] of one because every output maps
[4:03] of one because every output maps directly to an identical number um
[4:07] directly to an identical number um
[4:07] directly to an identical number um and the critical point is 0.22 because
[4:11] and the critical point is 0.22 because
[4:11] and the critical point is 0.22 because that's where we say the wheels will
[4:13] that's where we say the wheels will
[4:13] that's where we say the wheels will start moving
[4:14] start moving
[4:14] start moving and we have 28
[4:16] and we have 28
[4:16] and we have 28 of all possible commands will result in
[4:20] of all possible commands will result in
[4:20] of all possible commands will result in no movement at all
[4:21] no movement at all
[4:22] no movement at all and so there's two problems one is
[4:24] and so there's two problems one is
[4:24] and so there's two problems one is um that's sort of a useless area and
[4:27] um that's sort of a useless area and
[4:27] um that's sort of a useless area and when you're in this area you might
[4:29] when you're in this area you might
[4:29] when you're in this area you might listen to the motors you'll hear some
[4:31] listen to the motors you'll hear some
[4:31] listen to the motors you'll hear some buzzing
[4:32] buzzing
[4:32] buzzing it's a little unpleasant and then you'll
[4:33] it's a little unpleasant and then you'll
[4:33] it's a little unpleasant and then you'll get some heat generated inside the motor
[4:35] get some heat generated inside the motor
[4:35] get some heat generated inside the motor and you'll be using up current in your
[4:37] and you'll be using up current in your
[4:38] and you'll be using up current in your battery to get no effective motion so
[4:40] battery to get no effective motion so
[4:40] battery to get no effective motion so it's somewhat of a waste now if we can
[4:43] it's somewhat of a waste now if we can
[4:43] it's somewhat of a waste now if we can compress that region that 28 percent by
[4:46] compress that region that 28 percent by
[4:46] compress that region that 28 percent by increasing this slope we escape from the
[4:49] increasing this slope we escape from the
[4:49] increasing this slope we escape from the dead band sooner so if this is three
[4:52] dead band sooner so if this is three
[4:52] dead band sooner so if this is three the critical point is smaller that means
[4:55] the critical point is smaller that means
[4:55] the critical point is smaller that means any inputs between 0 and
[4:57] any inputs between 0 and
[4:57] any inputs between 0 and 0.073 or
[5:00] 0.073 or
[5:00] 0.073 or 7.5 percent duty cycle will map to
[5:04] 7.5 percent duty cycle will map to
[5:04] 7.5 percent duty cycle will map to values that ultimately get you moving
[5:07] values that ultimately get you moving
[5:07] values that ultimately get you moving along
[5:08] along
[5:08] along so
[5:09] so
[5:09] so you could compress it a lot actually we
[5:12] you could compress it a lot actually we
[5:12] you could compress it a lot actually we thought about before making this
[5:13] thought about before making this
[5:13] thought about before making this function what if we just delete all
[5:15] function what if we just delete all
[5:15] function what if we just delete all those values anything below uh 15
[5:19] those values anything below uh 15
[5:19] those values anything below uh 15 duty we'll just um
[5:22] duty we'll just um
[5:22] duty we'll just um increase it to 15
[5:24] increase it to 15
[5:24] increase it to 15 but that can cause some major
[5:26] but that can cause some major
[5:26] but that can cause some major disturbances when you're doing
[5:28] disturbances when you're doing
[5:28] disturbances when you're doing transients so let's say you're going
[5:30] transients so let's say you're going
[5:30] transients so let's say you're going from a
[5:31] from a
[5:31] from a from a dead stop to begin driving
[5:34] from a dead stop to begin driving
[5:34] from a dead stop to begin driving and your
[5:35] and your
[5:35] and your controller is gradually ramping up well
[5:38] controller is gradually ramping up well
[5:38] controller is gradually ramping up well um
[5:39] um
[5:39] um if
[5:40] if
[5:40] if in this case then you could make this
[5:43] in this case then you could make this
[5:43] in this case then you could make this very steep or you could totally um jump
[5:47] very steep or you could totally um jump
[5:47] very steep or you could totally um jump straight to the very first duty cycle
[5:49] straight to the very first duty cycle
[5:49] straight to the very first duty cycle that
[5:50] that
[5:50] that that results in motion that's that's
[5:52] that results in motion that's that's
[5:52] that results in motion that's that's okay for the static condition but for
[5:55] okay for the static condition but for
[5:55] okay for the static condition but for the transient condition when you're
[5:56] the transient condition when you're
[5:56] the transient condition when you're trying to go from moving to
[5:59] trying to go from moving to
[5:59] trying to go from moving to moving in reverse
[6:01] moving in reverse
[6:01] moving in reverse you could very much throw off the
[6:03] you could very much throw off the
[6:03] you could very much throw off the controller by uh by totally eliminating
[6:06] controller by uh by totally eliminating
[6:06] controller by uh by totally eliminating these ranges why
[6:08] these ranges why
[6:08] these ranges why because it's very likely that although
[6:10] because it's very likely that although
[6:10] because it's very likely that although it's no motion here and no motion here
[6:13] it's no motion here and no motion here
[6:13] it's no motion here and no motion here there is a difference in torque and so
[6:15] there is a difference in torque and so
[6:15] there is a difference in torque and so that would impact your acceleration and
[6:18] that would impact your acceleration and
[6:18] that would impact your acceleration and deceleration while you're moving along
[6:21] deceleration while you're moving along
[6:21] deceleration while you're moving along uh and and your while your pid
[6:23] uh and and your while your pid
[6:23] uh and and your while your pid controller is stacking up more
[6:27] controller is stacking up more
[6:27] controller is stacking up more more voltage to uh reach your speed or
[6:29] more voltage to uh reach your speed or
[6:29] more voltage to uh reach your speed or reducing it
[6:31] reducing it
[6:31] reducing it and so forth
[6:32] and so forth
[6:32] and so forth so basically
[6:35] so basically
[6:35] so basically um we've uh
[6:37] um we've uh
[6:37] um we've uh introduced these two variables you can
[6:39] introduced these two variables you can
[6:39] introduced these two variables you can work with them you can play with it and
[6:41] work with them you can play with it and
[6:41] work with them you can play with it and then
[6:42] then
[6:42] then that's gonna that's gonna have an impact
[6:44] that's gonna that's gonna have an impact
[6:44] that's gonna that's gonna have an impact on your
[6:45] on your
[6:45] on your uh initial measurements so you should
[6:48] uh initial measurements so you should
[6:48] uh initial measurements so you should have a smaller range here in the end
[6:50] have a smaller range here in the end
[6:50] have a smaller range here in the end that has no motion

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
