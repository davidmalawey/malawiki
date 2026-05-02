---
title: "SCUTTLE Robot - Choosing MQTT topics for mobile robot, IoT Guide (preliminary)"
url: "https://www.youtube.com/watch?v=Ty5oz7wUEcw"
video_id: "Ty5oz7wUEcw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-22
duration: "5:06"
duration_sec: 306
views: 209
likes: 6
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/Ty5oz7wUEcw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 270
chapters_count: 5
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://mxet.github.com/SCUTTLE

This video comes with the first-draft of our SCUTTLE Ecosystem IoT guide.  If all of our robots speak on similar channels, we can share data, perform machine to machine (M2M) communication, and make wild new results!  

MQTT broker: broker.mqttdashboard.com
Port: 1883
Topic example: scuttle/fleet/onboard/battery/602/voltage
Payload example: 11.6

Learn more by downloading our guide from the SCUTTLE webpage.

## Chapters

- 0:00 Intro
- 0:47 MQTT topic structure
- 4:12 MQTT ecosystem
- 4:28 Mobile app
- 4:42 Outro

## Transcript

[0:02] okay everybody this is just a
[0:02] okay everybody this is just a preliminary
[0:03] preliminary
[0:03] preliminary uh release of a video i want to
[0:06] uh release of a video i want to
[0:06] uh release of a video i want to introduce the idea of the
[0:08] introduce the idea of the
[0:08] introduce the idea of the scuttle iot environment or ecosystem
[0:12] scuttle iot environment or ecosystem
[0:12] scuttle iot environment or ecosystem and this is going to be honed and
[0:14] and this is going to be honed and
[0:14] and this is going to be honed and updated later but
[0:15] updated later but
[0:15] updated later but for the time being i just want to get
[0:17] for the time being i just want to get
[0:17] for the time being i just want to get the idea out there what topics we would
[0:19] the idea out there what topics we would
[0:19] the idea out there what topics we would like to use
[0:20] like to use
[0:20] like to use because that way when the student teams
[0:23] because that way when the student teams
[0:23] because that way when the student teams start creating
[0:24] start creating
[0:24] start creating projects right away and testing
[0:28] projects right away and testing
[0:28] projects right away and testing that we can all be playing in the same
[0:30] that we can all be playing in the same
[0:30] that we can all be playing in the same arena
[0:32] arena
[0:32] arena i won't read through this slide but
[0:35] i won't read through this slide but
[0:35] i won't read through this slide but the main benefit is that if we all use
[0:38] the main benefit is that if we all use
[0:38] the main benefit is that if we all use the same broker the same topics then we
[0:40] the same broker the same topics then we
[0:40] the same broker the same topics then we can begin to
[0:41] can begin to
[0:41] can begin to borrow each other's data see the status
[0:44] borrow each other's data see the status
[0:44] borrow each other's data see the status of various robots
[0:45] of various robots
[0:45] of various robots and and benefit from that so
[0:49] and and benefit from that so
[0:49] and and benefit from that so main point here is that the broker we're
[0:52] main point here is that the broker we're
[0:52] main point here is that the broker we're starting with
[0:53] starting with
[0:53] starting with is the hive mq public broker it's free
[0:55] is the hive mq public broker it's free
[0:56] is the hive mq public broker it's free and
[0:56] and
[0:56] and it's just a server that stays online
[0:59] it's just a server that stays online
[0:59] it's just a server that stays online 24 hours and it'll it'll retrieve and
[1:02] 24 hours and it'll it'll retrieve and
[1:02] 24 hours and it'll it'll retrieve and pass
[1:03] pass
[1:03] pass your mqtt messages wherever you ask that
[1:07] your mqtt messages wherever you ask that
[1:07] your mqtt messages wherever you ask that ask them to go example topic and payload
[1:10] ask them to go example topic and payload
[1:10] ask them to go example topic and payload is shown here
[1:11] is shown here
[1:11] is shown here but let's jump forward to the main part
[1:14] but let's jump forward to the main part
[1:14] but let's jump forward to the main part this is the topic structure okay so each
[1:18] this is the topic structure okay so each
[1:18] this is the topic structure okay so each each bar from left to right each
[1:21] each bar from left to right each
[1:21] each bar from left to right each box from left to right is going to be
[1:22] box from left to right is going to be
[1:22] box from left to right is going to be separated with a slash
[1:24] separated with a slash
[1:24] separated with a slash and so basically your topic for
[1:27] and so basically your topic for
[1:27] and so basically your topic for something like
[1:28] something like
[1:28] something like um the ambient pressure might be
[1:31] um the ambient pressure might be
[1:31] um the ambient pressure might be scuttle slash fleet slash
[1:35] scuttle slash fleet slash
[1:35] scuttle slash fleet slash onboard slash ambient
[1:38] onboard slash ambient
[1:38] onboard slash ambient slash um the
[1:41] slash um the
[1:41] slash um the number of your machine that you decided
[1:44] number of your machine that you decided
[1:44] number of your machine that you decided on
[1:45] on
[1:45] on slash pressure and then you'll have the
[1:48] slash pressure and then you'll have the
[1:48] slash pressure and then you'll have the payload
[1:48] payload
[1:48] payload which is whatever value you're
[1:52] which is whatever value you're
[1:52] which is whatever value you're sending i recommend that you just send a
[1:54] sending i recommend that you just send a
[1:54] sending i recommend that you just send a float or
[1:55] float or
[1:55] float or integer and no extra characters
[1:58] integer and no extra characters
[1:58] integer and no extra characters describing the units and so forth if you
[2:00] describing the units and so forth if you
[2:00] describing the units and so forth if you do units you should do it on a separate
[2:02] do units you should do it on a separate
[2:02] do units you should do it on a separate topic
[2:03] topic
[2:03] topic okay and this is not a comprehensive
[2:06] okay and this is not a comprehensive
[2:06] okay and this is not a comprehensive list but this is giving the
[2:08] list but this is giving the
[2:08] list but this is giving the starting point for how we can create
[2:11] starting point for how we can create
[2:12] starting point for how we can create a nice structure for topics that we can
[2:14] a nice structure for topics that we can
[2:14] a nice structure for topics that we can retrieve from one another
[2:16] retrieve from one another
[2:16] retrieve from one another there's a quite a bit of strategy that
[2:18] there's a quite a bit of strategy that
[2:18] there's a quite a bit of strategy that goes on between
[2:20] goes on between
[2:20] goes on between why we chose one two three four five six
[2:23] why we chose one two three four five six
[2:23] why we chose one two three four five six levels
[2:24] levels
[2:24] levels and um and a lot of that is to do has to
[2:27] and um and a lot of that is to do has to
[2:27] and um and a lot of that is to do has to do with
[2:28] do with
[2:28] do with the way that you can subscribe to
[2:30] the way that you can subscribe to
[2:30] the way that you can subscribe to multiple topics at the same time
[2:32] multiple topics at the same time
[2:32] multiple topics at the same time so uh if you have questions just throw
[2:35] so uh if you have questions just throw
[2:35] so uh if you have questions just throw them down at the bottom of this video
[2:36] them down at the bottom of this video
[2:36] them down at the bottom of this video and i will use those questions to
[2:39] and i will use those questions to
[2:39] and i will use those questions to produce
[2:39] produce
[2:39] produce the more thorough video and i can
[2:42] the more thorough video and i can
[2:42] the more thorough video and i can explain
[2:43] explain
[2:43] explain how all of us synchronizing on these
[2:45] how all of us synchronizing on these
[2:45] how all of us synchronizing on these channels will help us
[2:47] channels will help us
[2:47] channels will help us and then second major note for this is
[2:50] and then second major note for this is
[2:50] and then second major note for this is that
[2:51] that
[2:51] that the scuttle infrastructure is
[2:54] the scuttle infrastructure is
[2:54] the scuttle infrastructure is for all the subtopics for devices that
[2:58] for all the subtopics for devices that
[2:58] for all the subtopics for devices that are not
[2:58] are not
[2:58] are not scuttle robots but they are maybe
[3:01] scuttle robots but they are maybe
[3:01] scuttle robots but they are maybe sensors that are in the room that are
[3:03] sensors that are in the room that are
[3:04] sensors that are in the room that are helping with the
[3:05] helping with the
[3:05] helping with the the location or their sensors on the
[3:08] the location or their sensors on the
[3:08] the location or their sensors on the payload
[3:09] payload
[3:09] payload way station that's taking the mass of
[3:11] way station that's taking the mass of
[3:11] way station that's taking the mass of the scuttle and sending the data
[3:13] the scuttle and sending the data
[3:13] the scuttle and sending the data back to the scuttle and things like that
[3:17] back to the scuttle and things like that
[3:17] back to the scuttle and things like that so this is this is uh other sensors and
[3:20] so this is this is uh other sensors and
[3:20] so this is this is uh other sensors and machines that you might want to get
[3:21] machines that you might want to get
[3:21] machines that you might want to get online
[3:22] online
[3:22] online to have communicating in the scuttle
[3:23] to have communicating in the scuttle
[3:24] to have communicating in the scuttle environment
[3:24] environment
[3:24] environment [Music]
[3:26] [Music]
[3:26] [Music] and then the next subdivision is whether
[3:28] and then the next subdivision is whether
[3:28] and then the next subdivision is whether the
[3:29] the
[3:29] the the its data coming from the unit
[3:33] the its data coming from the unit
[3:33] the its data coming from the unit this is for the robot fleet is it data
[3:36] this is for the robot fleet is it data
[3:36] this is for the robot fleet is it data that's on board your
[3:37] that's on board your
[3:37] that's on board your robot or is it information that's kind
[3:40] robot or is it information that's kind
[3:40] robot or is it information that's kind of static
[3:41] of static
[3:41] of static regarding your robot and this one is
[3:43] regarding your robot and this one is
[3:43] regarding your robot and this one is less necessary it will come into play
[3:45] less necessary it will come into play
[3:45] less necessary it will come into play later when we want to
[3:47] later when we want to
[3:47] later when we want to have a server collecting a lot of data
[3:50] have a server collecting a lot of data
[3:50] have a server collecting a lot of data about a lot of robots
[3:51] about a lot of robots
[3:51] about a lot of robots and um and disseminating that
[3:54] and um and disseminating that
[3:54] and um and disseminating that information
[3:54] information
[3:54] information in a new structure okay and
[3:58] in a new structure okay and
[3:58] in a new structure okay and and all the stuff is optional but if you
[4:00] and all the stuff is optional but if you
[4:00] and all the stuff is optional but if you if you start to use this then you're
[4:02] if you start to use this then you're
[4:02] if you start to use this then you're going to see
[4:02] going to see
[4:02] going to see your friend's data and you're going to
[4:04] your friend's data and you're going to
[4:04] your friend's data and you're going to be able to learn uh from other people's
[4:06] be able to learn uh from other people's
[4:06] be able to learn uh from other people's messages
[4:07] messages
[4:07] messages and and have a lot of fun uh
[4:11] and and have a lot of fun uh
[4:11] and and have a lot of fun uh data to play with this is the
[4:14] data to play with this is the
[4:14] data to play with this is the scuttle ecosystem that's that's a slide
[4:17] scuttle ecosystem that's that's a slide
[4:17] scuttle ecosystem that's that's a slide in progress
[4:18] in progress
[4:18] in progress uh showing an idea
[4:21] uh showing an idea
[4:21] uh showing an idea of many different units that are going
[4:23] of many different units that are going
[4:24] of many different units that are going to be speaking in the same ecosystem
[4:26] to be speaking in the same ecosystem
[4:26] to be speaking in the same ecosystem all across the world and this is uh
[4:30] all across the world and this is uh
[4:30] all across the world and this is uh snapshots that are also shown in a
[4:32] snapshots that are also shown in a
[4:32] snapshots that are also shown in a couple of my videos of
[4:34] couple of my videos of
[4:34] couple of my videos of how to quickly grab this app on the
[4:37] how to quickly grab this app on the
[4:37] how to quickly grab this app on the iphone i think it's also on android
[4:40] iphone i think it's also on android
[4:40] iphone i think it's also on android and um
[4:43] and um
[4:43] and um and i think further slides are still yet
[4:46] and i think further slides are still yet
[4:46] and i think further slides are still yet to be
[4:47] to be
[4:47] to be uh developed here and best practices
[4:51] uh developed here and best practices
[4:51] uh developed here and best practices you can you can read that if you choose
[4:52] you can you can read that if you choose
[4:52] you can you can read that if you choose this is found on the
[4:54] this is found on the
[4:54] this is found on the on the scuttle github in the same place
[4:57] on the scuttle github in the same place
[4:57] on the scuttle github in the same place as the other the other scuttle guides
[5:01] as the other the other scuttle guides
[5:01] as the other the other scuttle guides thank you

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
