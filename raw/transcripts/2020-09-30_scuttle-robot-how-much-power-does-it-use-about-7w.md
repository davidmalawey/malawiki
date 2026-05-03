---
title: "SCUTTLE Robot - how much power does it use? About 7w."
url: "https://www.youtube.com/watch?v=Y3Fg8WhpVKE"
video_id: "Y3Fg8WhpVKE"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-30
duration: "4:58"
duration_sec: 298
views: 171
likes: 4
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/Y3Fg8WhpVKE/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 191
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://mxet.github.com/SCUTTLE

I run a quick test for idle and driving of the robot and check the current and wattage consumption.  Then I show some hand calculations about the maximum drive time for the robot.  

It’s reasonable to expect 6 hours of mixed driving + idling.  If you add more features such as lidar (ours uses 4w) this will have a large impact.  This test uses raspberry pi but it's similar with Beaglebone.

## Transcript

[0:05] 3.2
[0:05] 3.2 watts with the bluetooth controller
[0:07] watts with the bluetooth controller
[0:08] watts with the bluetooth controller talking
[0:17] driving was like on
[0:17] driving was like on 12 watts
[0:29] lights off full speed
[0:29] lights off full speed 7.5 watts
[0:34] and driving
[0:34] and driving [Music]
[0:44] let's try uh
[0:44] let's try uh real life
[0:57] [Music]
[0:57] [Music] so this is the battery that we normally
[1:00] so this is the battery that we normally
[1:00] so this is the battery that we normally use i happen to have
[1:01] use i happen to have
[1:01] use i happen to have a similar one from lg on the robot right
[1:05] a similar one from lg on the robot right
[1:05] a similar one from lg on the robot right now but most people
[1:06] now but most people
[1:06] now but most people using scuttles just have this one and
[1:11] using scuttles just have this one and
[1:11] using scuttles just have this one and i compiled the basic information from
[1:13] i compiled the basic information from
[1:14] i compiled the basic information from our driving
[1:15] our driving
[1:15] our driving with bluetooth but idle we're at 3.2
[1:18] with bluetooth but idle we're at 3.2
[1:18] with bluetooth but idle we're at 3.2 watts this is watts
[1:25] driving with the wheels off the ground
[1:25] driving with the wheels off the ground 7.5
[1:26] 7.5
[1:26] 7.5 when we went on to the ground uh it was
[1:29] when we went on to the ground uh it was
[1:29] when we went on to the ground uh it was still 7.5
[1:31] still 7.5
[1:31] still 7.5 but i think the the velocity is just a
[1:33] but i think the the velocity is just a
[1:33] but i think the the velocity is just a little slower
[1:35] little slower
[1:35] little slower and this is when i was driving in
[1:37] and this is when i was driving in
[1:37] and this is when i was driving in reverse because
[1:38] reverse because
[1:38] reverse because the lights are off during that time and
[1:41] the lights are off during that time and
[1:41] the lights are off during that time and the lights are not a normal feature i
[1:43] the lights are not a normal feature i
[1:43] the lights are not a normal feature i just added those on so i measured those
[1:45] just added those on so i measured those
[1:45] just added those on so i measured those also
[1:46] also
[1:46] also driving on the ground with the accessory
[1:48] driving on the ground with the accessory
[1:48] driving on the ground with the accessory lights on
[1:49] lights on
[1:49] lights on 12.5 watts this is all using
[1:53] 12.5 watts this is all using
[1:53] 12.5 watts this is all using the raspberry pi um i
[1:56] the raspberry pi um i
[1:56] the raspberry pi um i i've measured in the past with the
[1:58] i've measured in the past with the
[1:58] i've measured in the past with the beaglebone and it's a similar
[2:01] beaglebone and it's a similar
[2:01] beaglebone and it's a similar power level something below 7.5
[2:05] power level something below 7.5
[2:05] power level something below 7.5 while driving so very
[2:09] while driving so very
[2:09] while driving so very very power efficient this is just
[2:12] very power efficient this is just
[2:12] very power efficient this is just a graph of the same information and then
[2:14] a graph of the same information and then
[2:14] a graph of the same information and then here's some more
[2:15] here's some more
[2:15] here's some more analysis um i have a
[2:19] analysis um i have a
[2:19] analysis um i have a chart from 2006 that i made when i
[2:21] chart from 2006 that i made when i
[2:21] chart from 2006 that i made when i tested one individual panasonic cell
[2:24] tested one individual panasonic cell
[2:24] tested one individual panasonic cell and i re-ran this several times with
[2:26] and i re-ran this several times with
[2:26] and i re-ran this several times with different conditions but basically i
[2:28] different conditions but basically i
[2:28] different conditions but basically i discharged it at a constant rate of one
[2:30] discharged it at a constant rate of one
[2:30] discharged it at a constant rate of one amp
[2:31] amp
[2:31] amp and this is not
[2:34] and this is not
[2:34] and this is not relevant information this is relevant
[2:37] relevant information this is relevant
[2:37] relevant information this is relevant relevant and this is relevant
[2:40] relevant and this is relevant
[2:40] relevant and this is relevant the the starting voltage is actually up
[2:42] the the starting voltage is actually up
[2:42] the the starting voltage is actually up here it says
[2:44] here it says
[2:44] here it says started at
[2:50] 4.13 volts ending at 2.8
[2:50] 4.13 volts ending at 2.8 that that actually was the cutoff for
[2:52] that that actually was the cutoff for
[2:52] that that actually was the cutoff for the test
[2:54] the test
[2:54] the test and um the total tested capacity was
[2:57] and um the total tested capacity was
[2:58] and um the total tested capacity was 3.02 amps
[2:59] 3.02 amps
[3:00] 3.02 amps this just shows this is description so
[3:02] this just shows this is description so
[3:02] this just shows this is description so that's not
[3:03] that's not
[3:03] that's not physically controlling the test
[3:06] physically controlling the test
[3:06] physically controlling the test discharge rate one amp that's actually
[3:08] discharge rate one amp that's actually
[3:08] discharge rate one amp that's actually controlling the test
[3:10] controlling the test
[3:10] controlling the test and you can see it looks like this so if
[3:12] and you can see it looks like this so if
[3:12] and you can see it looks like this so if you want to stay very
[3:13] you want to stay very
[3:13] you want to stay very uh conservative actually you you stop it
[3:16] uh conservative actually you you stop it
[3:16] uh conservative actually you you stop it earlier than 2.8
[3:18] earlier than 2.8
[3:18] earlier than 2.8 volts because that's when
[3:21] volts because that's when
[3:21] volts because that's when you get this drop off and there's no
[3:24] you get this drop off and there's no
[3:24] you get this drop off and there's no need to go near there if you don't need
[3:25] need to go near there if you don't need
[3:26] need to go near there if you don't need to if you don't have to
[3:27] to if you don't have to
[3:28] to if you don't have to um okay so now let's open up excel again
[3:33] um okay so now let's open up excel again
[3:33] um okay so now let's open up excel again voltage 1 is 4.1 voltage 2 is 2.8
[3:38] voltage 1 is 4.1 voltage 2 is 2.8
[3:38] voltage 1 is 4.1 voltage 2 is 2.8 and the average is 3.4 so the area under
[3:41] and the average is 3.4 so the area under
[3:41] and the average is 3.4 so the area under the curve would be the
[3:42] the curve would be the
[3:42] the curve would be the amp hours times the average
[3:45] amp hours times the average
[3:46] amp hours times the average voltage that gives us the watt hours
[3:49] voltage that gives us the watt hours
[3:49] voltage that gives us the watt hours capacity okay so 10.5
[3:52] capacity okay so 10.5
[3:52] capacity okay so 10.5 and that agrees with an article i just
[3:55] and that agrees with an article i just
[3:55] and that agrees with an article i just read
[3:56] read
[3:56] read about modern 18650 cells
[3:59] about modern 18650 cells
[3:59] about modern 18650 cells even though this test was wet back in
[4:02] even though this test was wet back in
[4:04] yeah crazy um
[4:07] yeah crazy um and we have three cells in our pack
[4:11] and we have three cells in our pack
[4:11] and we have three cells in our pack so the capacity of the pack is 31 watt
[4:13] so the capacity of the pack is 31 watt
[4:13] so the capacity of the pack is 31 watt hours
[4:15] hours
[4:15] hours and if we're using the regular driving
[4:19] and if we're using the regular driving
[4:20] and if we're using the regular driving it's 7.5 watts
[4:23] it's 7.5 watts
[4:23] it's 7.5 watts consumed across 31 watt hours gives us
[4:26] consumed across 31 watt hours gives us
[4:26] consumed across 31 watt hours gives us 4.2 hours
[4:27] 4.2 hours
[4:27] 4.2 hours if this was if you're actually idling
[4:29] if this was if you're actually idling
[4:29] if this was if you're actually idling and you're just mostly testing
[4:32] and you're just mostly testing
[4:32] and you're just mostly testing doing software and other things then
[4:35] doing software and other things then
[4:35] doing software and other things then this would actually be 3.2
[4:43] and you can run for 10 hours and
[4:43] and you can run for 10 hours and and once again that's the concern if you
[4:46] and once again that's the concern if you
[4:46] and once again that's the concern if you want to be conservative
[4:47] want to be conservative
[4:47] want to be conservative you want to turn off your machine early
[4:50] you want to turn off your machine early
[4:50] you want to turn off your machine early and start to recharge it but
[4:54] and start to recharge it but
[4:54] and start to recharge it but that's really nice it gives some
[4:56] that's really nice it gives some
[4:56] that's really nice it gives some flexibility

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
