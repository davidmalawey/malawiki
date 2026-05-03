---
title: "SCUTTLE Robot - nodered receive mqtt message & save to csv"
url: "https://www.youtube.com/watch?v=4_rlm2HexTI"
video_id: "4_rlm2HexTI"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-04
duration: "5:36"
duration_sec: 336
views: 1532
likes: 8
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/4_rlm2HexTI/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 252
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://mxet.github.io/SCUTTLE/

Nodered Flow: https://gist.github.com/dmalawey/b99dd0c593c0ae296d8d9f65f1cd80c5

Demonstration including: make a nodered flow, send an mqtt message from a mobile phone app, capture two datapoints in one message, parse it as CSV values, create the .csv file on the raspberry pi (or beagle), and save the data from the mqtt message in the file.

## Transcript

[0:03] okay in this video i will try to
[0:03] okay in this video i will try to receive an mqtt message from my cell
[0:06] receive an mqtt message from my cell
[0:06] receive an mqtt message from my cell phone
[0:07] phone
[0:07] phone and then i'm going to listen to it here
[0:08] and then i'm going to listen to it here
[0:08] and then i'm going to listen to it here in node-red
[0:10] in node-red
[0:10] in node-red display what i get then i'm going to try
[0:12] display what i get then i'm going to try
[0:12] display what i get then i'm going to try to parse it
[0:13] to parse it
[0:13] to parse it by csv values and then i'm going to try
[0:15] by csv values and then i'm going to try
[0:15] by csv values and then i'm going to try to
[0:16] to
[0:16] to save that on a csv sheet in my
[0:20] save that on a csv sheet in my
[0:20] save that on a csv sheet in my on my linux device in this case it's my
[0:23] on my linux device in this case it's my
[0:23] on my linux device in this case it's my pi
[0:24] pi
[0:24] pi and i'll also do the debug to see what
[0:26] and i'll also do the debug to see what
[0:26] and i'll also do the debug to see what comes out of this
[0:27] comes out of this
[0:27] comes out of this csv parser
[0:31] csv parser
[0:31] csv parser let's start here it's an mqtt receive
[0:34] let's start here it's an mqtt receive
[0:34] let's start here it's an mqtt receive node
[0:35] node
[0:35] node i've set it up for the hive mq channel
[0:39] i've set it up for the hive mq channel
[0:39] i've set it up for the hive mq channel and i'm creating a new topic called
[0:41] and i'm creating a new topic called
[0:41] and i'm creating a new topic called scuttle slash pi
[0:43] scuttle slash pi
[0:43] scuttle slash pi cmd for command and i'm going to pretend
[0:46] cmd for command and i'm going to pretend
[0:46] cmd for command and i'm going to pretend that
[0:46] that
[0:46] that my cell phone is going to send commands
[0:49] my cell phone is going to send commands
[0:49] my cell phone is going to send commands wirelessly and my robot is going to
[0:51] wirelessly and my robot is going to
[0:52] wirelessly and my robot is going to receive the commands
[1:01] now in the csv node um
[1:01] now in the csv node um the column names must be entered so
[1:04] the column names must be entered so
[1:04] the column names must be entered so uh this is how it starts uh just asking
[1:07] uh this is how it starts uh just asking
[1:07] uh this is how it starts uh just asking you to put comma separated column names
[1:09] you to put comma separated column names
[1:09] you to put comma separated column names so i
[1:09] so i
[1:10] so i entered field a field b and then
[1:12] entered field a field b and then
[1:12] entered field a field b and then separator is comma
[1:14] separator is comma
[1:14] separator is comma this is for the actual string that
[1:16] this is for the actual string that
[1:16] this is for the actual string that you're going to receive
[1:17] you're going to receive
[1:17] you're going to receive in the mqtt message this could be a tab
[1:20] in the mqtt message this could be a tab
[1:20] in the mqtt message this could be a tab but
[1:21] but
[1:21] but comma works better because on my cell
[1:22] comma works better because on my cell
[1:22] comma works better because on my cell phone don't know how to add a tab
[1:26] phone don't know how to add a tab
[1:26] phone don't know how to add a tab now the other options mostly are default
[1:30] now the other options mostly are default
[1:30] now the other options mostly are default skip zero lines first row is not going
[1:33] skip zero lines first row is not going
[1:33] skip zero lines first row is not going to contain column names because i want
[1:35] to contain column names because i want
[1:35] to contain column names because i want to send a simple message
[1:36] to send a simple message
[1:36] to send a simple message on the cell phone and parse numerical
[1:39] on the cell phone and parse numerical
[1:39] on the cell phone and parse numerical values that was default checked
[1:41] values that was default checked
[1:41] values that was default checked and it worked fine for me so i left it
[1:43] and it worked fine for me so i left it
[1:43] and it worked fine for me so i left it the new line
[1:45] the new line
[1:45] the new line um is linux so i'm assuming
[1:49] um is linux so i'm assuming
[1:49] um is linux so i'm assuming i can type this new line into my mqtt
[1:51] i can type this new line into my mqtt
[1:51] i can type this new line into my mqtt message
[1:52] message
[1:52] message haven't tested it yet i'm trying
[1:54] haven't tested it yet i'm trying
[1:54] haven't tested it yet i'm trying starting simple
[1:56] starting simple
[1:56] starting simple okay then what is this i'm going to
[1:59] okay then what is this i'm going to
[1:59] okay then what is this i'm going to create a file
[2:00] create a file
[2:00] create a file or write to a file it's going to create
[2:03] or write to a file it's going to create
[2:03] or write to a file it's going to create the directory
[2:04] the directory
[2:04] the directory and i assume the file if it doesn't
[2:06] and i assume the file if it doesn't
[2:06] and i assume the file if it doesn't exist and add a new line to each payload
[2:10] exist and add a new line to each payload
[2:10] exist and add a new line to each payload um should try both ways on this one
[2:14] um should try both ways on this one
[2:14] um should try both ways on this one and i'm going to overwrite the file so
[2:16] and i'm going to overwrite the file so
[2:16] and i'm going to overwrite the file so yeah i probably won't see the effects of
[2:18] yeah i probably won't see the effects of
[2:18] yeah i probably won't see the effects of this
[2:19] this
[2:19] this then the encoding uh
[2:22] then the encoding uh
[2:22] then the encoding uh default probably will work i just
[2:25] default probably will work i just
[2:25] default probably will work i just successfully used
[2:26] successfully used
[2:26] successfully used utf-8 but let's try default done
[2:30] utf-8 but let's try default done
[2:30] utf-8 but let's try default done now um i'll deploy
[2:35] now um i'll deploy
[2:35] now um i'll deploy okay first i'm over here i'm connecting
[2:38] okay first i'm over here i'm connecting
[2:38] okay first i'm over here i'm connecting to
[2:38] to
[2:38] to my raspberry pi or beaglebone
[2:42] my raspberry pi or beaglebone
[2:42] my raspberry pi or beaglebone and i will go to let's see where i am i
[2:45] and i will go to let's see where i am i
[2:45] and i will go to let's see where i am i want to enter
[2:45] want to enter
[2:45] want to enter the cd pi scuttle
[2:49] the cd pi scuttle
[2:49] the cd pi scuttle folder and then i went to um
[2:52] folder and then i went to um
[2:52] folder and then i went to um i have data3 dot csv i want to delete it
[2:55] i have data3 dot csv i want to delete it
[2:55] i have data3 dot csv i want to delete it to make sure that it's created
[2:57] to make sure that it's created
[2:57] to make sure that it's created new so rm data3.csv
[3:02] new so rm data3.csv
[3:02] new so rm data3.csv ls all right so that's gone now let's go
[3:05] ls all right so that's gone now let's go
[3:05] ls all right so that's gone now let's go to the cell phone
[3:12] okay my application is mqt tool
[3:12] okay my application is mqt tool it's very simple i enter the host the
[3:14] it's very simple i enter the host the
[3:14] it's very simple i enter the host the port as default
[3:16] port as default
[3:16] port as default the client id is default and
[3:19] the client id is default and
[3:19] the client id is default and you start like this you click connect
[3:21] you start like this you click connect
[3:22] you start like this you click connect and then it says connected
[3:23] and then it says connected
[3:23] and then it says connected click done on the to get rid of the
[3:25] click done on the to get rid of the
[3:25] click done on the to get rid of the keyboard
[3:26] keyboard
[3:26] keyboard go to publish and now i'm going to be
[3:29] go to publish and now i'm going to be
[3:29] go to publish and now i'm going to be sending a message
[3:30] sending a message
[3:30] sending a message from my cell phone so my topic is
[3:33] from my cell phone so my topic is
[3:33] from my cell phone so my topic is scuttle
[3:33] scuttle
[3:33] scuttle slash pi cmd
[3:37] slash pi cmd
[3:37] slash pi cmd here and um i'm going to do a new
[3:39] here and um i'm going to do a new
[3:40] here and um i'm going to do a new message
[3:40] message
[3:40] message where the first value is 2.5
[3:45] where the first value is 2.5
[3:45] where the first value is 2.5 and i'll do a comma and then a space and
[3:48] and i'll do a comma and then a space and
[3:48] and i'll do a comma and then a space and 2.6 i worked with a space let's try
[3:51] 2.6 i worked with a space let's try
[3:51] 2.6 i worked with a space let's try without a space
[3:54] without a space
[3:54] without a space 2.6 so this should be two
[3:56] 2.6 so this should be two
[3:56] 2.6 so this should be two values and done and
[4:01] values and done and
[4:01] values and done and publish publish succeeded now let's
[4:04] publish publish succeeded now let's
[4:04] publish publish succeeded now let's uh go to subscribe to see yep right here
[4:08] uh go to subscribe to see yep right here
[4:08] uh go to subscribe to see yep right here um no
[4:16] i don't have it yet subscribe
[4:16] i don't have it yet subscribe let's publish again just to make sure
[4:19] let's publish again just to make sure
[4:19] let's publish again just to make sure publish succeeded
[4:20] publish succeeded
[4:20] publish succeeded subscribe got it 2.5 2.6
[4:25] subscribe got it 2.5 2.6
[4:25] subscribe got it 2.5 2.6 now let's go back to the computer
[4:28] now let's go back to the computer
[4:28] now let's go back to the computer okay here we are i'm going to ls again
[4:32] okay here we are i'm going to ls again
[4:32] okay here we are i'm going to ls again and boom now we have data3.csv
[4:36] and boom now we have data3.csv
[4:36] and boom now we have data3.csv and i'm going to do cat data3.csv
[4:42] and i'm going to do cat data3.csv
[4:42] and i'm going to do cat data3.csv and this is what i get um it's a string
[4:45] and this is what i get um it's a string
[4:46] and this is what i get um it's a string that's actually formatted maybe that's
[4:48] that's actually formatted maybe that's
[4:48] that's actually formatted maybe that's json gonna learn that next
[4:50] json gonna learn that next
[4:50] json gonna learn that next um indicating field a and field b
[4:53] um indicating field a and field b
[4:54] um indicating field a and field b with the corresponding 2.5 and 2.6
[4:57] with the corresponding 2.5 and 2.6
[4:57] with the corresponding 2.5 and 2.6 um just a reminder that where those
[5:00] um just a reminder that where those
[5:00] um just a reminder that where those field
[5:01] field
[5:01] field names came from was right here
[5:04] names came from was right here
[5:04] names came from was right here we named them field a and field b
[5:07] we named them field a and field b
[5:08] we named them field a and field b on the last part i just want to show
[5:09] on the last part i just want to show
[5:10] on the last part i just want to show that my debug
[5:11] that my debug
[5:11] that my debug 2 has indicated it received
[5:14] 2 has indicated it received
[5:14] 2 has indicated it received this exact string 2.5 comma 2.6
[5:18] this exact string 2.5 comma 2.6
[5:18] this exact string 2.5 comma 2.6 and my debug 3 which is after the csv
[5:21] and my debug 3 which is after the csv
[5:21] and my debug 3 which is after the csv parser
[5:22] parser
[5:22] parser is has the same information but it's
[5:25] is has the same information but it's
[5:25] is has the same information but it's conditioned
[5:26] conditioned
[5:26] conditioned as we expected
[5:32] and since i sent it twice they came in
[5:32] and since i sent it twice they came in twice
[5:34] twice
[5:34] twice that's all

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
