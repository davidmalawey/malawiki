---
title: "SCUTTLE Robot - Send & Receive MQTT messages, display with NodeRed, on Beaglebone Blue"
url: "https://www.youtube.com/watch?v=qmSQHYQaYrs"
video_id: "qmSQHYQaYrs"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-07-24
duration: "6:34"
duration_sec: 394
views: 189
likes: 0
category: "Entertainment"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/qmSQHYQaYrs/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 202
chapters_count: 0
has_description: false
has_comments: false
---

## Transcript

[0:04] let's look at how to pass MQTT
[0:04] let's look at how to pass MQTT information from the scuttle robot out
[0:07] information from the scuttle robot out
[0:07] information from the scuttle robot out to the web to be received on another
[0:10] to the web to be received on another
[0:10] to the web to be received on another edge device or another client as we
[0:13] edge device or another client as we
[0:13] edge device or another client as we would say in the mqtt world so the
[0:16] would say in the mqtt world so the
[0:16] would say in the mqtt world so the speeds published here on screen are
[0:21] speeds published here on screen are
[0:21] speeds published here on screen are directly coming from the scuttle robot
[0:25] directly coming from the scuttle robot
[0:25] directly coming from the scuttle robot that's the left and the white right
[0:26] that's the left and the white right
[0:26] that's the left and the white right wheel speeds being controlled by my
[0:28] wheel speeds being controlled by my
[0:28] wheel speeds being controlled by my joystick on my controller and what I
[0:32] joystick on my controller and what I
[0:32] joystick on my controller and what I have on my node-red
[0:33] have on my node-red
[0:33] have on my node-red dashboard is every 0.2 seconds or so a a
[0:41] dashboard is every 0.2 seconds or so a a
[0:41] dashboard is every 0.2 seconds or so a a file is read that's indicating my left
[0:44] file is read that's indicating my left
[0:44] file is read that's indicating my left and right wheel speed left here right
[0:47] and right wheel speed left here right
[0:47] and right wheel speed left here right here and those go to these gauges as
[0:50] here and those go to these gauges as
[0:50] here and those go to these gauges as well as a chart the way the dashboard
[0:52] well as a chart the way the dashboard
[0:52] well as a chart the way the dashboard looks is like this i press forward and
[0:56] looks is like this i press forward and
[0:56] looks is like this i press forward and you can see I have a positive velocity
[0:58] you can see I have a positive velocity
[0:58] you can see I have a positive velocity on left and right like go backwards and
[1:01] on left and right like go backwards and
[1:01] on left and right like go backwards and it goes negative but this information is
[1:06] it goes negative but this information is
[1:06] it goes negative but this information is not going to the World Wide Web it's
[1:08] not going to the World Wide Web it's
[1:08] not going to the World Wide Web it's still local just being transmitted by
[1:10] still local just being transmitted by
[1:10] still local just being transmitted by Wi-Fi from device to from the beagle
[1:14] Wi-Fi from device to from the beagle
[1:14] Wi-Fi from device to from the beagle device to my computer so now I want to
[1:17] device to my computer so now I want to
[1:17] device to my computer so now I want to send things to and from the web the item
[1:23] send things to and from the web the item
[1:23] send things to and from the web the item that you can inject is sorry the item
[1:28] that you can inject is sorry the item
[1:28] that you can inject is sorry the item you can add to your screen is an MQTT
[1:33] you can add to your screen is an MQTT
[1:34] you can add to your screen is an MQTT item and so if I have an input or an
[1:38] item and so if I have an input or an
[1:38] item and so if I have an input or an output here's how they function this is
[1:42] output here's how they function this is
[1:42] output here's how they function this is an output I have information coming from
[1:44] an output I have information coming from
[1:44] an output I have information coming from my robot and it's going out to the web I
[1:47] my robot and it's going out to the web I
[1:47] my robot and it's going out to the web I choose the I've MQ server that I just
[1:50] choose the I've MQ server that I just
[1:50] choose the I've MQ server that I just set up using this the only information
[1:53] set up using this the only information
[1:53] set up using this the only information that you need is Broker dot hi of fmq
[1:56] that you need is Broker dot hi of fmq
[1:56] that you need is Broker dot hi of fmq comm and port 1883 this information is
[2:01] comm and port 1883 this information is
[2:01] comm and port 1883 this information is going to match the information on my
[2:05] going to match the information on my
[2:05] going to match the information on my of my broker so the topic needs to be
[2:10] of my broker so the topic needs to be
[2:10] of my broker so the topic needs to be defined this is important test topic is
[2:12] defined this is important test topic is
[2:12] defined this is important test topic is a topic DM as a sub topic and to is yet
[2:17] a topic DM as a sub topic and to is yet
[2:17] a topic DM as a sub topic and to is yet another subtopic and the quality of
[2:19] another subtopic and the quality of
[2:19] another subtopic and the quality of service is set to two you can learn more
[2:22] service is set to two you can learn more
[2:22] service is set to two you can learn more about quality of service elsewhere it's
[2:25] about quality of service elsewhere it's
[2:25] about quality of service elsewhere it's pretty important
[2:27] pretty important
[2:27] pretty important okay so then over here I have a
[2:32] okay so then over here I have a
[2:32] okay so then over here I have a WebSocket client that can connect to the
[2:36] WebSocket client that can connect to the
[2:36] WebSocket client that can connect to the hive m QT v mq free mqtt broker we're
[2:42] hive m QT v mq free mqtt broker we're
[2:42] hive m QT v mq free mqtt broker we're connecting via port 8000 in this case
[2:44] connecting via port 8000 in this case
[2:44] connecting via port 8000 in this case all these are defaults i click connect
[2:47] all these are defaults i click connect
[2:47] all these are defaults i click connect and i should be able to publish and
[2:49] and i should be able to publish and
[2:49] and i should be able to publish and subscribe on a topic i think my topic is
[2:54] subscribe on a topic i think my topic is
[2:54] subscribe on a topic i think my topic is DM /to to receive updates from my wheels
[3:01] DM /to to receive updates from my wheels
[3:01] DM /to to receive updates from my wheels of my robot so and i'm not going to
[3:04] of my robot so and i'm not going to
[3:04] of my robot so and i'm not going to publish though i'll actually subscribe
[3:05] publish though i'll actually subscribe
[3:05] publish though i'll actually subscribe so test topic / DM / - okay so now i
[3:14] so test topic / DM / - okay so now i
[3:14] so test topic / DM / - okay so now i have zeros here i'm gonna go forward on
[3:16] have zeros here i'm gonna go forward on
[3:16] have zeros here i'm gonna go forward on the robot and I'm starting to get these
[3:18] the robot and I'm starting to get these
[3:18] the robot and I'm starting to get these positive values that should match the
[3:21] positive values that should match the
[3:21] positive values that should match the values coming from the robot I'm gonna
[3:24] values coming from the robot I'm gonna
[3:24] values coming from the robot I'm gonna drive negative reverse okay so that's
[3:29] drive negative reverse okay so that's
[3:29] drive negative reverse okay so that's how I can send data to the web and
[3:31] how I can send data to the web and
[3:31] how I can send data to the web and receive it on another device such as a
[3:33] receive it on another device such as a
[3:33] receive it on another device such as a cell phone next item is to publish a
[3:37] cell phone next item is to publish a
[3:37] cell phone next item is to publish a message and I'm going to publish a six
[3:39] message and I'm going to publish a six
[3:39] message and I'm going to publish a six on channel three and if I subscribe
[3:47] on channel three and if I subscribe
[3:47] on channel three and if I subscribe actually to DM / hashtag this is going
[3:51] actually to DM / hashtag this is going
[3:51] actually to DM / hashtag this is going to subscribe to all sub topics under
[3:54] to subscribe to all sub topics under
[3:54] to subscribe to all sub topics under this topic and subtopic that's that's
[4:00] this topic and subtopic that's that's
[4:00] this topic and subtopic that's that's the wild card the hashtag subscribe
[4:04] the wild card the hashtag subscribe
[4:04] the wild card the hashtag subscribe so now if I publish publish publish I
[4:06] so now if I publish publish publish I
[4:06] so now if I publish publish publish I got some sixes and you can see it in the
[4:09] got some sixes and you can see it in the
[4:09] got some sixes and you can see it in the feet now I go to my dashboard and I have
[4:13] feet now I go to my dashboard and I have
[4:13] feet now I go to my dashboard and I have an input that it's on the same server
[4:17] an input that it's on the same server
[4:17] an input that it's on the same server but in this case I have written my topic
[4:20] but in this case I have written my topic
[4:20] but in this case I have written my topic to be DM slash 3 and now
[4:35] any information being published on this
[4:35] any information being published on this topic on the hive mqt 5mq broker will be
[4:40] topic on the hive mqt 5mq broker will be
[4:40] topic on the hive mqt 5mq broker will be passed to a gauge on my node red
[4:43] passed to a gauge on my node red
[4:43] passed to a gauge on my node red dashboard okay so since I had input six
[4:46] dashboard okay so since I had input six
[4:46] dashboard okay so since I had input six it's currently sitting at six if I bring
[4:49] it's currently sitting at six if I bring
[4:49] it's currently sitting at six if I bring this over here
[4:50] this over here
[4:50] this over here and I know it says I'm disconnected
[4:54] and I know it says I'm disconnected
[4:54] and I know it says I'm disconnected connect again I'll publish sure thirteen
[5:00] connect again I'll publish sure thirteen
[5:00] connect again I'll publish sure thirteen and here you can see it's updating this
[5:03] and here you can see it's updating this
[5:03] and here you can see it's updating this information is coming directly from my
[5:06] information is coming directly from my
[5:06] information is coming directly from my my Beagle hardware so you know that the
[5:10] my Beagle hardware so you know that the
[5:10] my Beagle hardware so you know that the that the robot has received the data if
[5:12] that the robot has received the data if
[5:12] that the robot has received the data if this is updating another way we can
[5:15] this is updating another way we can
[5:15] this is updating another way we can verify that we received the data is we
[5:18] verify that we received the data is we
[5:18] verify that we received the data is we create a new cell shell session
[5:29] and we want to go home we're already
[5:30] and we want to go home we're already home um we need a CD basics and the file
[5:37] home um we need a CD basics and the file
[5:37] home um we need a CD basics and the file that we're writing to is where is it
[5:42] that we're writing to is where is it
[5:42] that we're writing to is where is it mqtt data.txt so I'm going to cat
[5:47] mqtt data.txt so I'm going to cat
[5:47] mqtt data.txt so I'm going to cat I'm QT D data dot txt and you can see a
[5:51] I'm QT D data dot txt and you can see a
[5:51] I'm QT D data dot txt and you can see a whole bunch of sixes that I published
[5:54] whole bunch of sixes that I published
[5:54] whole bunch of sixes that I published earlier and the 13 I'm going to publish
[5:56] earlier and the 13 I'm going to publish
[5:56] earlier and the 13 I'm going to publish another one I'll go out to the dashboard
[6:14] right here and I'll do 14 publish okay
[6:14] right here and I'll do 14 publish okay shows up here on my dashboard and then
[6:17] shows up here on my dashboard and then
[6:18] shows up here on my dashboard and then issues also show up here if I do the cat
[6:20] issues also show up here if I do the cat
[6:20] issues also show up here if I do the cat again now I have a 14 so this is how you
[6:23] again now I have a 14 so this is how you
[6:23] again now I have a 14 so this is how you can essentially control your robot if
[6:25] can essentially control your robot if
[6:25] can essentially control your robot if your robot grabs the information from
[6:28] your robot grabs the information from
[6:28] your robot grabs the information from this file and then performs an action
[6:30] this file and then performs an action
[6:30] this file and then performs an action based on that

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
