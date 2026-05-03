---
title: "NavigationVectors part1:  global position increment"
url: "https://www.youtube.com/watch?v=7k-5QmsfEpU"
video_id: "7k-5QmsfEpU"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-06-26
duration: "14:15"
duration_sec: 855
views: 53
likes: 2
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/7k-5QmsfEpU/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 274
chapters_count: 4
has_description: true
has_comments: false
---

## Description

Video for collaborating as we develop software for SCUTTLE driving.

This part explains how the global position is incremented in the latest revision. (no version number because the previous version was not released.)

Associated code, with some errors:
https://gist.github.com/dmalawey/b6355be2f011440a68d15098c4fc6225

## Chapters

- 0:00 <Untitled Chapter 1>
- 7:40 Rotation Matrix
- 10:10 Global Vector
- 12:38 Updating the Heading

## Transcript

[0:04] okay let's dive in and just see where
[0:04] okay let's dive in and just see where this goes
[0:05] this goes
[0:05] this goes no planning for this video let's get the
[0:10] no planning for this video let's get the
[0:10] no planning for this video let's get the pen out pens working okay so your
[0:17] pen out pens working okay so your
[0:17] pen out pens working okay so your coordinates well the X&amp;Y robot always
[0:22] coordinates well the X&amp;Y robot always
[0:22] coordinates well the X&amp;Y robot always starts at zero facing in this direction
[0:26] starts at zero facing in this direction
[0:26] starts at zero facing in this direction for the time being and then we give a
[0:32] for the time being and then we give a
[0:32] for the time being and then we give a desired coordinate point we're gonna
[0:35] desired coordinate point we're gonna
[0:35] desired coordinate point we're gonna call this point five point five the new
[0:41] call this point five point five the new
[0:41] call this point five point five the new driving method should create a behavior
[0:45] driving method should create a behavior
[0:45] driving method should create a behavior where we curve we don't do any point
[0:51] where we curve we don't do any point
[0:51] where we curve we don't do any point turns and then we drive forward so every
[1:00] turns and then we drive forward so every
[1:00] turns and then we drive forward so every Waypoint has two sections the curve of a
[1:06] Waypoint has two sections the curve of a
[1:06] Waypoint has two sections the curve of a constant radius may be in the code it's
[1:13] constant radius may be in the code it's
[1:13] constant radius may be in the code it's a lowercase R and then a distance of
[1:19] a lowercase R and then a distance of
[1:19] a lowercase R and then a distance of straight driving in but we're in both
[1:23] straight driving in but we're in both
[1:23] straight driving in but we're in both segments curving and driving we're
[1:26] segments curving and driving we're
[1:26] segments curving and driving we're measuring the change in theta the change
[1:32] measuring the change in theta the change
[1:32] measuring the change in theta the change in the heading of the robot where theta
[1:36] in the heading of the robot where theta
[1:36] in the heading of the robot where theta is not the heading but theta describes
[1:39] is not the heading but theta describes
[1:39] is not the heading but theta describes them the movement basically it's the
[1:42] them the movement basically it's the
[1:42] them the movement basically it's the heading of scuttle in his frame and
[1:46] heading of scuttle in his frame and
[1:46] heading of scuttle in his frame and we're checking DX and for a distance of
[1:52] we're checking DX and for a distance of
[1:52] we're checking DX and for a distance of 500 millimeters and 500 millimeters
[1:56] 500 millimeters and 500 millimeters
[1:56] 500 millimeters and 500 millimeters maybe we'll be driving
[1:59] maybe we'll be driving
[1:59] maybe we'll be driving and performing 100 or 200 segments
[2:05] and performing 100 or 200 segments
[2:05] and performing 100 or 200 segments that's that's just how fast we're going
[2:08] that's that's just how fast we're going
[2:08] that's that's just how fast we're going and how fast we're sampling so this will
[2:13] and how fast we're sampling so this will
[2:13] and how fast we're sampling so this will be something like one millimeter to five
[2:20] be something like one millimeter to five
[2:20] be something like one millimeter to five millimeters I'm not quite sure but
[2:23] millimeters I'm not quite sure but
[2:23] millimeters I'm not quite sure but that's the basic scale now let's look at
[2:30] that's the basic scale now let's look at
[2:30] that's the basic scale now let's look at the curve section and the criteria for
[2:33] the curve section and the criteria for
[2:33] the curve section and the criteria for everything
[2:34] everything
[2:34] everything our very first point all started in
[2:37] our very first point all started in
[2:37] our very first point all started in orange and our very first motion will
[2:43] orange and our very first motion will
[2:43] orange and our very first motion will have some curving in some advancement so
[2:48] have some curving in some advancement so
[2:48] have some curving in some advancement so deep orange this is zoomed in a lot okay
[2:54] deep orange this is zoomed in a lot okay
[2:54] deep orange this is zoomed in a lot okay this is going to be let's just say
[2:58] this is going to be let's just say
[2:58] this is going to be let's just say that's four millimeters arc length
[3:11] and and we have to do two things after
[3:11] and and we have to do two things after this update heading and update the dis
[3:24] this update heading and update the dis
[3:24] this update heading and update the dis the X&amp;Y
[3:26] the X&amp;Y
[3:26] the X&amp;Y global positions so the translation of
[3:30] global positions so the translation of
[3:30] global positions so the translation of the robot because these are so small and
[3:35] the robot because these are so small and
[3:35] the robot because these are so small and this might be the maximum but often this
[3:42] this might be the maximum but often this
[3:42] this might be the maximum but often this might only be half a millimeter I'm not
[3:44] might only be half a millimeter I'm not
[3:44] might only be half a millimeter I'm not sure but because this distance is so
[3:46] sure but because this distance is so
[3:46] sure but because this distance is so small we're not going to consider the
[3:48] small we're not going to consider the
[3:48] small we're not going to consider the fact that it's an art we're going to
[3:49] fact that it's an art we're going to
[3:49] fact that it's an art we're going to consider that it's a straight line for
[3:52] consider that it's a straight line for
[3:52] consider that it's a straight line for the keeping them the math low-intensity
[3:57] the keeping them the math low-intensity
[3:57] the keeping them the math low-intensity it's already fairly intense because of
[3:59] it's already fairly intense because of
[3:59] it's already fairly intense because of the other kinematics being done but but
[4:01] the other kinematics being done but but
[4:01] the other kinematics being done but but here's what's happening um this is the
[4:05] here's what's happening um this is the
[4:05] here's what's happening um this is the heading in the initial heading in yellow
[4:16] and I'm gonna call this we'll call it
[4:16] and I'm gonna call this we'll call it theta initial and then I'm gonna make a
[4:22] theta initial and then I'm gonna make a
[4:22] theta initial and then I'm gonna make a red one okay and this is Theta
[4:42] and so if you compare those two we get
[4:42] and so if you compare those two we get this use again
[4:53] maybe it's a little bit stronger than
[4:53] maybe it's a little bit stronger than that
[4:59] okay so d-theta
[5:00] okay so d-theta he's right there and in this case theta
[5:03] he's right there and in this case theta
[5:03] he's right there and in this case theta I was zero maybe we don't need to use
[5:06] I was zero maybe we don't need to use
[5:06] I was zero maybe we don't need to use that but in order to calculate this this
[5:12] that but in order to calculate this this
[5:13] that but in order to calculate this this X movement I'm here to here blue equals
[5:19] X movement I'm here to here blue equals
[5:19] X movement I'm here to here blue equals the translation we'll come back to it
[5:28] the translation we'll come back to it
[5:28] the translation we'll come back to it but to calculate our translation we have
[5:31] but to calculate our translation we have
[5:31] but to calculate our translation we have to choose how we want to calculate it
[5:35] to choose how we want to calculate it
[5:35] to choose how we want to calculate it without using an arc because the arts
[5:37] without using an arc because the arts
[5:37] without using an arc because the arts math is more intensive so what we're
[5:42] math is more intensive so what we're
[5:42] math is more intensive so what we're gonna do is show a purple we wouldn't
[5:51] gonna do is show a purple we wouldn't
[5:51] gonna do is show a purple we wouldn't use this angle and pretend that instead
[5:55] use this angle and pretend that instead
[5:55] use this angle and pretend that instead of starting out at the yellow area and
[5:58] of starting out at the yellow area and
[5:58] of starting out at the yellow area and ending up at the red area that actually
[6:01] ending up at the red area that actually
[6:01] ending up at the red area that actually the whole time we just drove in the
[6:03] the whole time we just drove in the
[6:03] the whole time we just drove in the purple direction and so this would be in
[6:10] purple direction and so this would be in
[6:10] purple direction and so this would be in the code this is called I don't think we
[6:14] the code this is called I don't think we
[6:14] the code this is called I don't think we even named the variable we just start
[6:16] even named the variable we just start
[6:16] even named the variable we just start using it we put it in in the short part
[6:21] using it we put it in in the short part
[6:21] using it we put it in in the short part of the code it's used enough to create a
[6:23] of the code it's used enough to create a
[6:23] of the code it's used enough to create a rotation matrix so I'm sorry but this is
[6:28] rotation matrix so I'm sorry but this is
[6:28] rotation matrix so I'm sorry but this is theta for the function and that equals D
[6:38] theta for the function and that equals D
[6:38] theta for the function and that equals D theta over two and in the rotation
[6:42] theta over two and in the rotation
[6:42] theta over two and in the rotation matrix this needs to be added to the
[6:49] matrix this needs to be added to the
[6:49] matrix this needs to be added to the data over to must be added to the
[6:52] data over to must be added to the
[6:52] data over to must be added to the previous heading
[6:55] previous heading
[6:55] previous heading which is actually called self dot
[6:58] which is actually called self dot
[6:58] which is actually called self dot heading I don't know how to denote this
[7:02] heading I don't know how to denote this
[7:02] heading I don't know how to denote this but the soaked up heading has not been
[7:05] but the soaked up heading has not been
[7:05] but the soaked up heading has not been updated when we perform this calculation
[7:14] updated when we perform this calculation
[7:14] updated when we perform this calculation so this is data thunk encode it's just
[7:24] so this is data thunk encode it's just
[7:24] so this is data thunk encode it's just called theta but it's it's local to one
[7:27] called theta but it's it's local to one
[7:27] called theta but it's it's local to one function and and it's never called again
[7:30] function and and it's never called again
[7:30] function and and it's never called again so you won't know that that data is
[7:32] so you won't know that that data is
[7:32] so you won't know that that data is special unless you just read the code
[7:36] special unless you just read the code
[7:36] special unless you just read the code but it's okay because it's not used
[7:38] but it's okay because it's not used
[7:38] but it's okay because it's not used anywhere else and then that's put into a
[7:41] anywhere else and then that's put into a
[7:41] anywhere else and then that's put into a rotation matrix that's a capital R
[8:04] which is something like this is a
[8:04] which is something like this is a standard 2d rotation matrix I don't want
[8:07] standard 2d rotation matrix I don't want
[8:07] standard 2d rotation matrix I don't want to get my signs round so it's just an
[8:11] to get my signs round so it's just an
[8:11] to get my signs round so it's just an array of cosines and sines and then we
[8:13] array of cosines and sines and then we
[8:13] array of cosines and sines and then we perform the rotation matrix where we
[8:16] perform the rotation matrix where we
[8:16] perform the rotation matrix where we take the the displacement we believe
[8:21] take the the displacement we believe
[8:21] take the the displacement we believe took place was so when your robot
[8:38] the displacement so when you're driving
[8:38] the displacement so when you're driving and we're calculating using kinematics
[8:42] and we're calculating using kinematics
[8:42] and we're calculating using kinematics the X advancement there is never any why
[8:56] why translation it's always in the ice
[8:56] why translation it's always in the ice so you have a vector that looks like
[8:59] so you have a vector that looks like
[8:59] so you have a vector that looks like this DX and 0 and that is the that's
[9:14] this DX and 0 and that is the that's
[9:14] this DX and 0 and that is the that's called we call it in the code
[9:37] okay because that's the displacement in
[9:37] okay because that's the displacement in the local coordinate plan and then we
[9:44] the local coordinate plan and then we
[9:44] the local coordinate plan and then we multiply R times the local vector
[10:50] come up here that means every time we
[10:50] come up here that means every time we drive a tiny amount such as one
[10:53] drive a tiny amount such as one
[10:53] drive a tiny amount such as one millimeter or four millimeters the
[10:56] millimeter or four millimeters the
[10:56] millimeter or four millimeters the global vector that's added to the
[11:02] global vector that's added to the
[11:02] global vector that's added to the existing position because between these
[11:05] existing position because between these
[11:05] existing position because between these two blue lines is that value so the
[11:09] two blue lines is that value so the
[11:09] two blue lines is that value so the global vector that's a product of these
[11:12] global vector that's a product of these
[11:12] global vector that's a product of these and of course it's so one by two shaped
[11:19] and of course it's so one by two shaped
[11:19] and of course it's so one by two shaped like this now you should have in mind
[11:30] like this now you should have in mind
[11:30] like this now you should have in mind and I get up the scale so somewhere in
[11:37] and I get up the scale so somewhere in
[11:38] and I get up the scale so somewhere in the XY coordinate system you have your
[11:42] the XY coordinate system you have your
[11:42] the XY coordinate system you have your actual position of the robot and that
[11:46] actual position of the robot and that
[11:47] actual position of the robot and that means this purple vector is actually
[11:51] means this purple vector is actually
[11:51] means this purple vector is actually quite large
[12:00] and when we add this global vector to
[12:00] and when we add this global vector to the global position it's basically
[12:02] the global position it's basically
[12:02] the global position it's basically saying okay can I perform this small
[12:08] saying okay can I perform this small
[12:08] saying okay can I perform this small deviation so in the end every single
[12:23] deviation so in the end every single
[12:23] deviation so in the end every single translation is treated as a straight
[12:25] translation is treated as a straight
[12:25] translation is treated as a straight line and the angle that we're using for
[12:30] line and the angle that we're using for
[12:30] line and the angle that we're using for that is an average between the angle of
[12:34] that is an average between the angle of
[12:34] that is an average between the angle of our headings before and after in the
[12:36] our headings before and after in the
[12:36] our headings before and after in the movement and then finally updating the
[12:39] movement and then finally updating the
[12:39] movement and then finally updating the heading is extremely easy because we
[12:41] heading is extremely easy because we
[12:41] heading is extremely easy because we just take basically the heading was the
[12:50] just take basically the heading was the
[12:50] just take basically the heading was the heading plots
[13:28] which we should know gets fed by wheels
[13:28] which we should know gets fed by wheels you have excuse me there's no dots here
[13:39] you have excuse me there's no dots here
[13:39] you have excuse me there's no dots here for this for this set of variables it's
[13:44] for this for this set of variables it's
[13:44] for this for this set of variables it's just the five increment and you could
[13:48] just the five increment and you could
[13:48] just the five increment and you could say then when we do it you could just
[13:51] say then when we do it you could just
[13:51] say then when we do it you could just say that's a delta all right that's all
[13:57] say that's a delta all right that's all
[13:57] say that's a delta all right that's all for this video

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
