---
title: "NavigationVectors part2:   Curve Criteria"
url: "https://www.youtube.com/watch?v=bU78G0S6LGw"
video_id: "bU78G0S6LGw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-06-26
duration: "16:08"
duration_sec: 968
views: 27
likes: 1
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/bU78G0S6LGw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 310
chapters_count: 0
has_description: true
has_comments: false
---

## Description

Video for collaborating as we develop software for SCUTTLE driving.
SCUTTLE project: mxet.github.io/SCUTTLE

This part explains how it's decided to curve or drive straight towards the destination. (no version number because the previous version was not released.)

Associated code, with some errors:
https://gist.github.com/dmalawey/b6355be2f011440a68d15098c4fc6225

## Transcript

[0:03] you're gonna continue where I left off
[0:03] you're gonna continue where I left off the last video was basically saying
[0:08] the last video was basically saying
[0:08] the last video was basically saying let's try to talk how do we calculate
[0:14] let's try to talk how do we calculate
[0:14] let's try to talk how do we calculate the advancement
[0:20] the advancement
[0:20] the advancement [Music]
[0:35] [Music]
[0:35] [Music] increments
[0:37] increments
[0:37] increments the wheels that was basically answered
[0:47] the wheels that was basically answered
[0:47] the wheels that was basically answered in part one now part two is more about
[0:52] in part one now part two is more about
[0:52] in part one now part two is more about the behavior target
[1:12] and I want to answer how do we decide if
[1:12] and I want to answer how do we decide if we should curve or remain straight and
[1:21] we should curve or remain straight and
[1:21] we should curve or remain straight and the goals for the robot are that we
[1:24] the goals for the robot are that we
[1:24] the goals for the robot are that we don't want to create another PID
[1:27] don't want to create another PID
[1:27] don't want to create another PID controller where we're changing our
[1:30] controller where we're changing our
[1:30] controller where we're changing our curving rate and we're oscillating or
[1:34] curving rate and we're oscillating or
[1:35] curving rate and we're oscillating or having multiple modes of approaching a
[1:38] having multiple modes of approaching a
[1:39] having multiple modes of approaching a target we really want to keep it simple
[1:42] target we really want to keep it simple
[1:42] target we really want to keep it simple make in this case we have two parts of
[1:46] make in this case we have two parts of
[1:46] make in this case we have two parts of behavior options curve followed by
[1:55] behavior options curve followed by
[1:55] behavior options curve followed by straight and this video should just
[2:00] straight and this video should just
[2:00] straight and this video should just describe how do we decide when to
[2:03] describe how do we decide when to
[2:03] describe how do we decide when to transition from curving to going
[2:05] transition from curving to going
[2:05] transition from curving to going straight so let's jump in with some
[2:11] straight so let's jump in with some
[2:11] straight so let's jump in with some sketches
[2:25] fumbling with the tablet here okay we
[2:25] fumbling with the tablet here okay we look up here we said that there's a
[2:28] look up here we said that there's a
[2:28] look up here we said that there's a target and code this is called the point
[2:42] super non-descriptive but it's nice
[2:42] super non-descriptive but it's nice because we really only want to deal with
[2:44] because we really only want to deal with
[2:44] because we really only want to deal with one point per call of the function and
[2:48] one point per call of the function and
[2:48] one point per call of the function and then we're letting the the criteria of
[2:53] then we're letting the the criteria of
[2:53] then we're letting the the criteria of the code decide how to drive the wheels
[2:55] the code decide how to drive the wheels
[2:55] the code decide how to drive the wheels and then the PID controller to handle or
[2:57] and then the PID controller to handle or
[2:57] and then the PID controller to handle or the wheels do so there's point and it's
[3:01] the wheels do so there's point and it's
[3:01] the wheels do so there's point and it's gonna be lowercase actually for this
[3:10] [Music]
[3:10] [Music] and first off light gray and paste
[3:23] and first off light gray and paste
[3:23] and first off light gray and paste I accidentally change the screen to
[3:25] I accidentally change the screen to
[3:25] I accidentally change the screen to white I don't want to lose my lines
[3:26] white I don't want to lose my lines
[3:26] white I don't want to lose my lines completely so um we can't just go
[3:30] completely so um we can't just go
[3:30] completely so um we can't just go straight like this because we're not
[3:32] straight like this because we're not
[3:32] straight like this because we're not allowing any point turns so that can't
[3:38] allowing any point turns so that can't
[3:38] allowing any point turns so that can't happen and and secondly if we measure
[3:44] happen and and secondly if we measure
[3:44] happen and and secondly if we measure the distance from this point to this
[3:47] the distance from this point to this
[3:47] the distance from this point to this point
[3:53] and we use that as the criteria like we
[3:53] and we use that as the criteria like we used to that one no longer be valid
[3:55] used to that one no longer be valid
[3:55] used to that one no longer be valid because it's increased by this curve or
[3:59] because it's increased by this curve or
[3:59] because it's increased by this curve or if you only use this segment obviously
[4:02] if you only use this segment obviously
[4:02] if you only use this segment obviously it's decreased by that curve so the new
[4:08] it's decreased by that curve so the new
[4:08] it's decreased by that curve so the new behavior and this version of the
[4:10] behavior and this version of the
[4:10] behavior and this version of the software is calculating the vector every
[4:14] software is calculating the vector every
[4:14] software is calculating the vector every single time the wheels have an increment
[4:17] single time the wheels have an increment
[4:17] single time the wheels have an increment that I erase all that stuff let's let's
[4:21] that I erase all that stuff let's let's
[4:21] that I erase all that stuff let's let's draw it out I'm gonna draw up scuttle
[4:26] draw it out I'm gonna draw up scuttle
[4:26] draw it out I'm gonna draw up scuttle actually as if it was in somewhere in
[4:31] actually as if it was in somewhere in
[4:31] actually as if it was in somewhere in the middle of this curve and it's almost
[4:35] the middle of this curve and it's almost
[4:35] the middle of this curve and it's almost ready to finish the curve
[4:54] okay so here's our point and this is the
[4:54] okay so here's our point and this is the distance accomplished in the previous
[4:58] distance accomplished in the previous
[4:58] distance accomplished in the previous segment and we know also with that
[5:04] segment and we know also with that
[5:04] segment and we know also with that actually occurred
[5:06] actually occurred
[5:06] actually occurred okay and picking changing color
[5:25] yeah and then let's make that purple
[5:25] yeah and then let's make that purple okay so true is purple blue as estimated
[5:30] okay so true is purple blue as estimated
[5:30] okay so true is purple blue as estimated and let's continue with the blue because
[5:32] and let's continue with the blue because
[5:32] and let's continue with the blue because that's what we're actually doing with
[5:34] that's what we're actually doing with
[5:34] that's what we're actually doing with four calculations now my new heading is
[5:38] four calculations now my new heading is
[5:38] four calculations now my new heading is aligned with the purple one
[5:51] we don't have exactly a Greek letter
[5:51] we don't have exactly a Greek letter assigned for this we call it heading
[5:54] assigned for this we call it heading
[5:54] assigned for this we call it heading because this is the global X here this
[6:03] because this is the global X here this
[6:03] because this is the global X here this vector and this is our heading after
[6:09] vector and this is our heading after
[6:09] vector and this is our heading after updating
[6:21] so and then let's draw slightly far away
[6:21] so and then let's draw slightly far away target and that will be in green so yeah
[6:33] target and that will be in green so yeah
[6:33] target and that will be in green so yeah you know every time we advance from
[6:39] you know every time we advance from
[6:39] you know every time we advance from point to point then we're going to
[6:40] point to point then we're going to
[6:40] point to point then we're going to calculate a new vector from our measured
[6:47] calculate a new vector from our measured
[6:47] calculate a new vector from our measured point
[6:57] from our global position to the
[6:57] from our global position to the destination so this is point and this is
[7:14] and I think we refer to it also it
[7:14] and I think we refer to it also it locally has a global vector okay and so
[7:23] locally has a global vector okay and so
[7:23] locally has a global vector okay and so we have two vectors to compare the
[7:26] we have two vectors to compare the
[7:26] we have two vectors to compare the global vector in the heading and that's
[7:32] global vector in the heading and that's
[7:32] global vector in the heading and that's how we generate our criteria for
[7:35] how we generate our criteria for
[7:35] how we generate our criteria for finishing our curve basically the
[7:41] finishing our curve basically the
[7:41] finishing our curve basically the criteria says we measure the gap here
[7:48] criteria says we measure the gap here
[7:48] criteria says we measure the gap here and that's called yeah
[8:03] and for sketch purposes I'm gonna call
[8:03] and for sketch purposes I'm gonna call it theta gap
[8:13] and then we have another one called the
[8:13] and then we have another one called the span which is allowable
[8:35] and deviation between our heading and
[8:35] and deviation between our heading and required heading to drive exactly over
[8:39] required heading to drive exactly over
[8:39] required heading to drive exactly over the point and this can never be zero
[8:42] the point and this can never be zero
[8:42] the point and this can never be zero because your your heading is a true
[8:47] because your your heading is a true
[8:47] because your your heading is a true measurement that eventually comes from
[8:49] measurement that eventually comes from
[8:49] measurement that eventually comes from the wheels and you will never produce a
[8:53] the wheels and you will never produce a
[8:53] the wheels and you will never produce a heading that's exactly the same angle as
[8:55] heading that's exactly the same angle as
[8:55] heading that's exactly the same angle as the global vector so so we're creating
[9:00] the global vector so so we're creating
[9:00] the global vector so so we're creating the span which is user-defined
[9:16] and this this means that the programmer
[9:16] and this this means that the programmer can decide what their kind of allowable
[9:20] can decide what their kind of allowable
[9:20] can decide what their kind of allowable tolerance is and you when you make a
[9:23] tolerance is and you when you make a
[9:23] tolerance is and you when you make a vigorous fan of course you're saying I
[9:24] vigorous fan of course you're saying I
[9:24] vigorous fan of course you're saying I don't need to drive exactly to the point
[9:26] don't need to drive exactly to the point
[9:26] don't need to drive exactly to the point I just need to be close did you make a
[9:28] I just need to be close did you make a
[9:28] I just need to be close did you make a smaller span you're saying don't finish
[9:31] smaller span you're saying don't finish
[9:31] smaller span you're saying don't finish curving until you're right on or very
[9:34] curving until you're right on or very
[9:34] curving until you're right on or very close to the global vector however
[9:38] close to the global vector however
[9:38] close to the global vector however you're gonna eventually if you continue
[9:42] you're gonna eventually if you continue
[9:42] you're gonna eventually if you continue making span smaller then you're going to
[9:47] making span smaller then you're going to
[9:47] making span smaller then you're going to run into a situation where you overshoot
[9:49] run into a situation where you overshoot
[9:49] run into a situation where you overshoot the global vector every single time you
[9:51] the global vector every single time you
[9:51] the global vector every single time you try to approach it and so if you make it
[9:55] try to approach it and so if you make it
[9:55] try to approach it and so if you make it smaller
[10:17] to prevent you from overshooting new
[10:17] to prevent you from overshooting new targets and you should also note that
[10:20] targets and you should also note that
[10:20] targets and you should also note that the closer you are from the blue point
[10:24] the closer you are from the blue point
[10:24] the closer you are from the blue point to the green point the more rapidly you
[10:28] to the green point the more rapidly you
[10:28] to the green point the more rapidly you will be curbing your heading away from
[10:31] will be curbing your heading away from
[10:31] will be curbing your heading away from where you need to display imagine if you
[10:38] where you need to display imagine if you
[10:38] where you need to display imagine if you were
[10:54] you're very close then a small deviation
[10:54] you're very close then a small deviation will make you miss the vector versus
[10:58] will make you miss the vector versus
[10:58] will make you miss the vector versus that same angle
[11:20] maybe there's just not so much in fact
[11:20] maybe there's just not so much in fact depending how plus you are I won't make
[11:22] depending how plus you are I won't make
[11:22] depending how plus you are I won't make any claims about that until I kind of
[11:24] any claims about that until I kind of
[11:24] any claims about that until I kind of run through it on my own but you do need
[11:29] run through it on my own but you do need
[11:29] run through it on my own but you do need to go slower if you want to decrease
[11:31] to go slower if you want to decrease
[11:31] to go slower if you want to decrease your span no theta cap basically gets
[11:36] your span no theta cap basically gets
[11:36] your span no theta cap basically gets compared we say if datak out it's
[11:47] compared we say if datak out it's
[11:47] compared we say if datak out it's smaller than span then we need to well
[11:58] smaller than span then we need to well
[11:58] smaller than span then we need to well then we're okay to go drive straight
[12:19] then we need to continue turning to
[12:19] then we need to continue turning to curving
[12:30] and I keep saying curve because in
[12:30] and I keep saying curve because in previous discussions we said that the
[12:32] previous discussions we said that the
[12:32] previous discussions we said that the curving the act of turning at our
[12:36] curving the act of turning at our
[12:36] curving the act of turning at our specify various other colors
[12:38] specify various other colors
[12:38] specify various other colors I'm not curved will not describe a point
[12:43] I'm not curved will not describe a point
[12:43] I'm not curved will not describe a point time and then the other case is if you
[12:50] time and then the other case is if you
[12:50] time and then the other case is if you have a negative span so theta gap can be
[12:56] have a negative span so theta gap can be
[12:56] have a negative span so theta gap can be negative because we're just doing
[13:00] negative because we're just doing
[13:00] negative because we're just doing subtraction here the heading the global
[13:05] subtraction here the heading the global
[13:05] subtraction here the heading the global vector minus the heading so if it's
[13:07] vector minus the heading so if it's
[13:07] vector minus the heading so if it's negative you need to turn in the other
[13:08] negative you need to turn in the other
[13:08] negative you need to turn in the other direction and so we're going to say
[13:13] direction and so we're going to say
[13:13] direction and so we're going to say reverse curve or rather continue reverse
[13:18] reverse curve or rather continue reverse
[13:18] reverse curve or rather continue reverse curve and the way we do that is I made a
[13:23] curve and the way we do that is I made a
[13:23] curve and the way we do that is I made a variable called flip and when flip is
[13:30] variable called flip and when flip is
[13:30] variable called flip and when flip is positive
[13:54] that's negative and if it's zero or if
[13:54] that's negative and if it's zero or if it's close enough to our target then you
[13:58] it's close enough to our target then you
[13:58] it's close enough to our target then you don't go
[14:06] and that's nice because later in the
[14:06] and that's nice because later in the code we say that there's a curb speed
[14:16] initially I think it's called the curve
[14:16] initially I think it's called the curve rate where you know when we're driving
[14:19] rate where you know when we're driving
[14:19] rate where you know when we're driving and tuning we checked what what rate is
[14:23] and tuning we checked what what rate is
[14:23] and tuning we checked what what rate is a nice approachable an acceptable rate
[14:27] a nice approachable an acceptable rate
[14:27] a nice approachable an acceptable rate of curving our theta of our robot you
[14:32] of curving our theta of our robot you
[14:32] of curving our theta of our robot you know physically when you all start
[14:34] know physically when you all start
[14:34] know physically when you all start driving we have to say well how fast can
[14:38] driving we have to say well how fast can
[14:38] driving we have to say well how fast can we go on a circle without saturating our
[14:42] we go on a circle without saturating our
[14:42] we go on a circle without saturating our controller or sliding the wheels or just
[14:45] controller or sliding the wheels or just
[14:45] controller or sliding the wheels or just overshooting everything and the curve
[14:48] overshooting everything and the curve
[14:48] overshooting everything and the curve speed gets multiplied by flip
[15:06] to get us the command that gets put into
[15:06] to get us the command that gets put into things called settler
[15:19] and that's a chassis speed which text
[15:19] and that's a chassis speed which text desired convey to time we say well we
[15:26] desired convey to time we say well we
[15:26] desired convey to time we say well we literally just put this whole equation
[15:36] but essentially that's the desired
[15:36] but essentially that's the desired paradigm this all gets packaged up and
[15:40] paradigm this all gets packaged up and
[15:40] paradigm this all gets packaged up and it goes to the PID controllers
[15:45] it goes to the PID controllers
[15:45] it goes to the PID controllers individual individual wheel controllers
[15:49] individual individual wheel controllers
[15:49] individual individual wheel controllers to get you and of course it goes through
[15:53] to get you and of course it goes through
[15:53] to get you and of course it goes through the kinematics to get there

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
