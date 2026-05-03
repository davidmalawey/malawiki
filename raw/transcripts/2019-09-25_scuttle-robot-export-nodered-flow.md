---
title: "SCUTTLE Robot - Export NodeRed flow"
url: "https://www.youtube.com/watch?v=mzOOg71oGzs"
video_id: "mzOOg71oGzs"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-09-25
duration: "4:40"
duration_sec: 280
views: 197
likes: 2
category: "Entertainment"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/mzOOg71oGzs/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 142
chapters_count: 4
has_description: true
has_comments: false
---

## Description

export your Node Red GUI to be imported later or shared.

## Chapters

- 0:00 Intro
- 1:05 Create flow
- 1:34 Test flow
- 2:37 Export flow

## Transcript

[0:03] in this video we are going to show you
[0:03] in this video we are going to show you how to export your no dread flow for the
[0:07] how to export your no dread flow for the
[0:07] how to export your no dread flow for the sake of lab 4 so I created a level 3
[0:12] sake of lab 4 so I created a level 3
[0:12] sake of lab 4 so I created a level 3 program called run PI I'm importing my
[0:16] program called run PI I'm importing my
[0:16] program called run PI I'm importing my kinematics to get access to the get
[0:18] kinematics to get access to the get
[0:18] kinematics to get access to the get motion function and this function is
[0:21] motion function and this function is
[0:21] motion function and this function is going to return to us the the C array
[0:24] going to return to us the the C array
[0:24] going to return to us the the C array which has the X dot value and the theta
[0:28] which has the X dot value and the theta
[0:28] which has the X dot value and the theta dot value your lab 4 is also going to
[0:30] dot value your lab 4 is also going to
[0:30] dot value your lab 4 is also going to ask for your five dot left and find out
[0:33] ask for your five dot left and find out
[0:33] ask for your five dot left and find out right corresponding to the wheel speeds
[0:36] right corresponding to the wheel speeds
[0:36] right corresponding to the wheel speeds on your robot so this this program will
[0:41] on your robot so this this program will
[0:41] on your robot so this this program will run when I go right now I'm already
[0:45] run when I go right now I'm already
[0:45] run when I go right now I'm already running it so the way to start it up is
[0:47] running it so the way to start it up is
[0:47] running it so the way to start it up is python 3 L 3 run PI enter it needs to be
[0:52] python 3 L 3 run PI enter it needs to be
[0:52] python 3 L 3 run PI enter it needs to be in the same directory as my level 1 and
[0:55] in the same directory as my level 1 and
[0:55] in the same directory as my level 1 and level 2 s and you're going to see that
[0:57] level 2 s and you're going to see that
[0:57] level 2 s and you're going to see that these dot txt files have been created
[1:01] these dot txt files have been created
[1:01] these dot txt files have been created automatically by this function log
[1:04] automatically by this function log
[1:04] automatically by this function log unique file so you're going to go into
[1:07] unique file so you're going to go into
[1:07] unique file so you're going to go into node read and you're going to create
[1:08] node read and you're going to create
[1:08] node read and you're going to create your flow this flow is very simple
[1:11] your flow this flow is very simple
[1:11] your flow this flow is very simple there's a time stamp injected at the
[1:13] there's a time stamp injected at the
[1:13] there's a time stamp injected at the interval we have the X dot file to
[1:16] interval we have the X dot file to
[1:16] interval we have the X dot file to access where this file path needs to
[1:19] access where this file path needs to
[1:19] access where this file path needs to meet match the path the prefix which is
[1:23] meet match the path the prefix which is
[1:23] meet match the path the prefix which is in your log PI program and the suffix or
[1:27] in your log PI program and the suffix or
[1:27] in your log PI program and the suffix or the the actual file name which is
[1:29] the the actual file name which is
[1:29] the the actual file name which is located in your level 3 program when you
[1:32] located in your level 3 program when you
[1:32] located in your level 3 program when you call the function okay so when we deploy
[1:36] call the function okay so when we deploy
[1:36] call the function okay so when we deploy this this one's already been deployed
[1:38] this this one's already been deployed
[1:38] this this one's already been deployed you come over to the dashboard and
[1:40] you come over to the dashboard and
[1:40] you come over to the dashboard and you're gonna see theta dot and you're
[1:43] you're gonna see theta dot and you're
[1:43] you're gonna see theta dot and you're gonna see X done and this should be in
[1:45] gonna see X done and this should be in
[1:45] gonna see X done and this should be in meters per second this should be in
[1:47] meters per second this should be in
[1:47] meters per second this should be in radians per second and then I'm gonna
[1:50] radians per second and then I'm gonna
[1:50] radians per second and then I'm gonna spin the the right hand wheel forward
[1:53] spin the the right hand wheel forward
[1:53] spin the the right hand wheel forward and you should see a a left turn on the
[1:58] and you should see a a left turn on the
[1:58] and you should see a a left turn on the theta dot which is a positive here we go
[2:14] that's a few movements by my hand
[2:14] that's a few movements by my hand turning it and you saw that the X dot
[2:16] turning it and you saw that the X dot
[2:16] turning it and you saw that the X dot went positive and the theta dot went
[2:19] went positive and the theta dot went
[2:19] went positive and the theta dot went positive so that's that verifies that my
[2:24] positive so that's that verifies that my
[2:24] positive so that's that verifies that my software is working because when my
[2:25] software is working because when my
[2:25] software is working because when my right hand wheel moves forward and my
[2:28] right hand wheel moves forward and my
[2:28] right hand wheel moves forward and my left hand wheel does nothing my chassis
[2:30] left hand wheel does nothing my chassis
[2:30] left hand wheel does nothing my chassis will move in the positive direction and
[2:32] will move in the positive direction and
[2:32] will move in the positive direction and my theta dot will be rotating in the
[2:35] my theta dot will be rotating in the
[2:35] my theta dot will be rotating in the positive direction in order to export
[2:38] positive direction in order to export
[2:38] positive direction in order to export this flow we're going to do the sorry
[2:43] this flow we're going to do the sorry
[2:43] this flow we're going to do the sorry top right menu
[2:44] top right menu
[2:44] top right menu we're gonna go to export clipboard okay
[2:48] we're gonna go to export clipboard okay
[2:48] we're gonna go to export clipboard okay and it's nice if you select formatted
[2:51] and it's nice if you select formatted
[2:51] and it's nice if you select formatted and it looks like it's exported to
[2:54] and it looks like it's exported to
[2:54] and it looks like it's exported to clipboard as of now you can create a
[2:57] clipboard as of now you can create a
[2:57] clipboard as of now you can create a gist where you just github.com I'm going
[3:03] gist where you just github.com I'm going
[3:03] gist where you just github.com I'm going to put it in here my node red lab 4 ok
[3:13] to put it in here my node red lab 4 ok
[3:13] to put it in here my node red lab 4 ok I'm going to create public gist and now
[3:20] I'm going to create public gist and now
[3:20] I'm going to create public gist and now in my github I have this this address
[3:27] in my github I have this this address
[3:27] in my github I have this this address which leads me to the entire node red
[3:29] which leads me to the entire node red
[3:29] which leads me to the entire node red flow ok and I can place that inside my
[3:36] flow ok and I can place that inside my
[3:36] flow ok and I can place that inside my code for convenience and compactness
[3:40] code for convenience and compactness
[3:40] code for convenience and compactness find the node red flow here
[3:51] and we're gonna make this into a comment
[3:51] and we're gonna make this into a comment as well
[3:51] as well
[3:51] as well so now wherever this file is stored
[3:55] so now wherever this file is stored
[3:55] so now wherever this file is stored l-3 run up high you also have access to
[3:58] l-3 run up high you also have access to
[3:58] l-3 run up high you also have access to the flow which is going to make this
[4:01] the flow which is going to make this
[4:01] the flow which is going to make this this correspond to this program and you
[4:06] this correspond to this program and you
[4:06] this correspond to this program and you come in here and you can do import
[4:20] clipboard we can take this raw select
[4:20] clipboard we can take this raw select all copy paste new flow and it may just
[4:27] all copy paste new flow and it may just
[4:27] all copy paste new flow and it may just look the exact same once I'm done okay
[4:29] look the exact same once I'm done okay
[4:29] look the exact same once I'm done okay so essentially it has copied the flow so
[4:33] so essentially it has copied the flow so
[4:33] so essentially it has copied the flow so that's how you do it

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
