---
title: "SCUTTLE Robot - nodered read csv to send mqtt"
url: "https://www.youtube.com/watch?v=6eDT6jU8MtU"
video_id: "6eDT6jU8MtU"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-03
duration: "5:57"
duration_sec: 357
views: 1339
likes: 17
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/6eDT6jU8MtU/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 212
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://mxet.github.io/SCUTTLE/

This tutorial creates a new csv file manually (thru command line), adds a single line of data, creates a nodered flow to read the .csv file, parse the file into an MQTT message, and send out the message.  On my mobile phone I subscribe to the mqtt topic, receive the message and verify the contents!

keywords: cell phone, MQTTool, publish, subscribe, IoT

Nodered flow is shared here: https://gist.github.com/dmalawey/48a23761f58d5c1ca681ecd32faf5bd8

## Transcript

[0:04] in this video i want to review how to
[0:04] in this video i want to review how to create a csv file for parameters that
[0:06] create a csv file for parameters that
[0:06] create a csv file for parameters that will update on the scuttle robot
[0:08] will update on the scuttle robot
[0:08] will update on the scuttle robot and access the csv data in order to
[0:11] and access the csv data in order to
[0:11] and access the csv data in order to create
[0:12] create
[0:12] create mqtt messages on ned red
[0:16] mqtt messages on ned red
[0:16] mqtt messages on ned red so we're gonna start our session here
[0:20] so we're gonna start our session here
[0:20] so we're gonna start our session here and i'm gonna go to um i'm in my home
[0:23] and i'm gonna go to um i'm in my home
[0:23] and i'm gonna go to um i'm in my home directory now i'm gonna go to
[0:25] directory now i'm gonna go to
[0:25] directory now i'm gonna go to uh pi
[0:29] uh pi
[0:29] uh pi scuttle and right here i have data.csv
[0:34] scuttle and right here i have data.csv
[0:34] scuttle and right here i have data.csv i'm going to create a new one so
[0:35] i'm going to create a new one so
[0:35] i'm going to create a new one so touch data2.csv
[0:45] and enter and nano data
[0:45] and enter and nano data two dot csv now i can edit it
[0:48] two dot csv now i can edit it
[0:48] two dot csv now i can edit it i'm gonna do field one here
[0:51] i'm gonna do field one here
[0:51] i'm gonna do field one here tab over field two here
[0:55] tab over field two here
[0:55] tab over field two here enter and i'll put a random value so 5.5
[0:58] enter and i'll put a random value so 5.5
[0:58] enter and i'll put a random value so 5.5 here tab over 5.6
[1:01] here tab over 5.6
[1:02] here tab over 5.6 here and i will save it control
[1:06] here and i will save it control
[1:06] here and i will save it control x y for save enter
[1:10] x y for save enter
[1:10] x y for save enter now i will go over to
[1:13] now i will go over to
[1:13] now i will go over to uh well let's just make sure that it's
[1:15] uh well let's just make sure that it's
[1:15] uh well let's just make sure that it's there
[1:16] there
[1:16] there ls okay so data2 dot csv is there
[1:21] ls okay so data2 dot csv is there
[1:21] ls okay so data2 dot csv is there now in the node-red you'll create a
[1:24] now in the node-red you'll create a
[1:24] now in the node-red you'll create a new flow or add to your existing flow
[1:28] new flow or add to your existing flow
[1:28] new flow or add to your existing flow make a time stamp that's comes from
[1:31] make a time stamp that's comes from
[1:31] make a time stamp that's comes from the inject it automatically defaults to
[1:34] the inject it automatically defaults to
[1:34] the inject it automatically defaults to time stamp
[1:36] time stamp
[1:36] time stamp then you're gonna access a file so
[1:40] then you're gonna access a file so
[1:40] then you're gonna access a file so this comes from the file
[1:43] this comes from the file
[1:43] this comes from the file not the writing but the reading and we
[1:46] not the writing but the reading and we
[1:46] not the writing but the reading and we double click it
[1:47] double click it
[1:47] double click it and all you have to modify is home pi
[1:56] pi scuttle data 2 dot csv
[1:56] pi scuttle data 2 dot csv you'll have to create write this whole
[1:58] you'll have to create write this whole
[1:58] you'll have to create write this whole field
[2:00] field
[2:00] field then we're going to
[2:04] then we're going to
[2:04] then we're going to change this to tab and that's the only
[2:07] change this to tab and that's the only
[2:07] change this to tab and that's the only thing you need to modify
[2:10] thing you need to modify
[2:10] thing you need to modify no be below this line you need to also
[2:14] no be below this line you need to also
[2:14] no be below this line you need to also skip zero lines indicate that the first
[2:17] skip zero lines indicate that the first
[2:17] skip zero lines indicate that the first row contains
[2:18] row contains
[2:18] row contains column names and um
[2:22] column names and um
[2:22] column names and um i think this was already checked i'll
[2:24] i think this was already checked i'll
[2:24] i think this was already checked i'll leave it alone
[2:25] leave it alone
[2:25] leave it alone one message per row done
[2:29] one message per row done
[2:29] one message per row done now message.payload
[2:37] this is um unmodified all i did was
[2:37] this is um unmodified all i did was basically
[2:38] basically
[2:38] basically uh this is the the debug um
[2:43] uh this is the the debug um
[2:43] uh this is the the debug um item and i connect it to the output of
[2:46] item and i connect it to the output of
[2:46] item and i connect it to the output of the csv
[2:47] the csv
[2:47] the csv just so i could read it but i won't be
[2:49] just so i could read it but i won't be
[2:49] just so i could read it but i won't be using that now this is just for reading
[2:51] using that now this is just for reading
[2:51] using that now this is just for reading in between
[2:53] in between
[2:53] in between and ultimately i'll read it on my
[2:55] and ultimately i'll read it on my
[2:55] and ultimately i'll read it on my another device that's
[2:57] another device that's
[2:57] another device that's watching this um
[3:00] watching this um
[3:00] watching this um this topic on the hive mq server so
[3:03] this topic on the hive mq server so
[3:04] this topic on the hive mq server so my topic is scuttle slash pi gp for
[3:07] my topic is scuttle slash pi gp for
[3:07] my topic is scuttle slash pi gp for gamepad
[3:09] gamepad
[3:09] gamepad i'll call it gp i'll just leave it as gp
[3:13] i'll call it gp i'll just leave it as gp
[3:13] i'll call it gp i'll just leave it as gp and um not gp2
[3:16] and um not gp2
[3:16] and um not gp2 since i have a new file and click done
[3:20] since i have a new file and click done
[3:20] since i have a new file and click done and these blue bubbles need to be
[3:22] and these blue bubbles need to be
[3:22] and these blue bubbles need to be cleared because it shows there's changes
[3:24] cleared because it shows there's changes
[3:24] cleared because it shows there's changes so i hit
[3:25] so i hit
[3:25] so i hit deploy okay and then
[3:28] deploy okay and then
[3:28] deploy okay and then if i watch this one
[3:32] if i watch this one
[3:32] if i watch this one and i click here it will inject one
[3:35] and i click here it will inject one
[3:35] and i click here it will inject one so it shows message.payload
[3:38] so it shows message.payload
[3:38] so it shows message.payload and it has field one with this value
[3:40] and it has field one with this value
[3:40] and it has field one with this value field two with this value that means it
[3:42] field two with this value that means it
[3:42] field two with this value that means it successfully read
[3:44] successfully read
[3:44] successfully read the csv file that i wrote here and
[3:47] the csv file that i wrote here and
[3:48] the csv file that i wrote here and next i want to see if i can view it on
[3:51] next i want to see if i can view it on
[3:51] next i want to see if i can view it on my phone
[3:58] okay i opened up the mqt tool
[3:58] okay i opened up the mqt tool app and i add the the host port and
[4:01] app and i add the the host port and
[4:01] app and i add the the host port and client id
[4:02] client id
[4:02] client id actually this client id is automatically
[4:04] actually this client id is automatically
[4:04] actually this client id is automatically generated
[4:05] generated
[4:05] generated i just click connect it says it's
[4:09] i just click connect it says it's
[4:09] i just click connect it says it's connected
[4:10] connected
[4:10] connected then i go to subscribe and i enter the
[4:14] then i go to subscribe and i enter the
[4:14] then i go to subscribe and i enter the topic i want to subscribe with is
[4:16] topic i want to subscribe with is
[4:16] topic i want to subscribe with is gp 2
[4:19] gp 2
[4:20] gp 2 done and quality of service 2
[4:23] done and quality of service 2
[4:23] done and quality of service 2 is most reliable for testing for
[4:26] is most reliable for testing for
[4:26] is most reliable for testing for starting
[4:27] starting
[4:27] starting hit subscribe it says i am subscribed
[4:30] hit subscribe it says i am subscribed
[4:30] hit subscribe it says i am subscribed now i'm going to hit
[4:31] now i'm going to hit
[4:31] now i'm going to hit inject again on my
[4:35] inject again on my
[4:35] inject again on my node red and there we go i get
[4:39] node red and there we go i get
[4:39] node red and there we go i get one message with both pieces of
[4:42] one message with both pieces of
[4:42] one message with both pieces of information
[4:43] information
[4:44] information looks good
[4:50] now i'm going to see if i can export
[4:50] now i'm going to see if i can export this
[4:56] flow
[4:56] flow flows
[5:09] current flow copy to clipboard
[5:09] current flow copy to clipboard now i'll just save this in a gist i'm
[5:11] now i'll just save this in a gist i'm
[5:11] now i'll just save this in a gist i'm calling it flow mqtt
[5:13] calling it flow mqtt
[5:13] calling it flow mqtt csv
[5:24] whoa it's all on one line soft wrap here
[5:24] whoa it's all on one line soft wrap here we are
[5:26] we are
[5:26] we are and let's call this one it's the first
[5:29] and let's call this one it's the first
[5:29] and let's call this one it's the first one
[5:35] another red flow for
[5:35] another red flow for retrieving csv info
[5:38] retrieving csv info
[5:38] retrieving csv info and sending mqtt
[5:41] and sending mqtt
[5:41] and sending mqtt message
[5:53] create public just create
[5:53] create public just create okay i'll put this one in the video

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
