---
title: "SCUTTLE Robot - nodered function to extract each gamepad axis & display"
url: "https://www.youtube.com/watch?v=hzgSystU4yI"
video_id: "hzgSystU4yI"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-09
duration: "7:20"
duration_sec: 440
views: 998
likes: 9
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/hzgSystU4yI/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 342
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://MXET.github.io/SCUTTLE

Copy & Paste Nodered Flow: https://gist.github.com/dmalawey/8b63adaa9bb83daff7ff58b150c3c423

Use NodeRED function to extract two data values from the 2 axes of the gamepad.  Display the two readings in Gauge indicators on the dashboard.

## Transcript

[0:03] hi everybody in the previous video i
[0:03] hi everybody in the previous video i made
[0:03] made
[0:03] made an instructions for sending sensor data
[0:06] an instructions for sending sensor data
[0:06] an instructions for sending sensor data into csv
[0:07] into csv
[0:07] into csv coming in from the gamepad here and
[0:10] coming in from the gamepad here and
[0:10] coming in from the gamepad here and going ultimately to
[0:11] going ultimately to
[0:11] going ultimately to node-red and the way we did that was
[0:14] node-red and the way we did that was
[0:14] node-red and the way we did that was putting it into a text file
[0:16] putting it into a text file
[0:16] putting it into a text file the the file extension was txt but
[0:19] the the file extension was txt but
[0:19] the the file extension was txt but truly was a comma separated values file
[0:22] truly was a comma separated values file
[0:22] truly was a comma separated values file because it would just had
[0:23] because it would just had
[0:23] because it would just had values and commas and a space
[0:27] values and commas and a space
[0:27] values and commas and a space we'll get to that so this video i want
[0:29] we'll get to that so this video i want
[0:30] we'll get to that so this video i want to show you how to format the
[0:31] to show you how to format the
[0:31] to show you how to format the same file to give two values to node-red
[0:35] same file to give two values to node-red
[0:35] same file to give two values to node-red and how to make the gauges for each of
[0:37] and how to make the gauges for each of
[0:37] and how to make the gauges for each of the axes that you want to plot
[0:39] the axes that you want to plot
[0:39] the axes that you want to plot and how to collect one value from the
[0:41] and how to collect one value from the
[0:41] and how to collect one value from the pair of axes
[0:43] pair of axes
[0:43] pair of axes how to correct the gamepad settings
[0:46] how to correct the gamepad settings
[0:46] how to correct the gamepad settings actually you don't need to correct it
[0:47] actually you don't need to correct it
[0:47] actually you don't need to correct it i'm just showing you that the correct
[0:49] i'm just showing you that the correct
[0:49] i'm just showing you that the correct setting
[0:49] setting
[0:49] setting is this one it has the
[0:52] is this one it has the
[0:52] is this one it has the the blue leds on the left half are
[0:56] the blue leds on the left half are
[0:56] the blue leds on the left half are lit and that's indicating what setting
[0:58] lit and that's indicating what setting
[0:58] lit and that's indicating what setting it's in
[0:59] it's in
[0:59] it's in then finally how to verify axes
[1:02] then finally how to verify axes
[1:02] then finally how to verify axes inversion that means we're going to just
[1:04] inversion that means we're going to just
[1:04] inversion that means we're going to just check our values at the end of
[1:07] check our values at the end of
[1:07] check our values at the end of showing them in our gauges
[1:10] showing them in our gauges
[1:10] showing them in our gauges the file you're looking at here is l3
[1:13] the file you're looking at here is l3
[1:13] the file you're looking at here is l3 chart.pi
[1:14] chart.pi
[1:14] chart.pi and it was previously used but i've
[1:16] and it was previously used but i've
[1:16] and it was previously used but i've modified it a little bit
[1:18] modified it a little bit
[1:18] modified it a little bit just consider that you don't have this
[1:20] just consider that you don't have this
[1:20] just consider that you don't have this file and it's unique
[1:22] file and it's unique
[1:22] file and it's unique so the only notable thing about this
[1:25] so the only notable thing about this
[1:25] so the only notable thing about this file that i want to talk about right now
[1:27] file that i want to talk about right now
[1:27] file that i want to talk about right now is that we we put a comma in between our
[1:29] is that we we put a comma in between our
[1:29] is that we we put a comma in between our two values
[1:30] two values
[1:30] two values that are stored as strings and we've
[1:32] that are stored as strings and we've
[1:32] that are stored as strings and we've removed the space
[1:34] removed the space
[1:34] removed the space the space caused me trouble later on
[1:36] the space caused me trouble later on
[1:36] the space caused me trouble later on when i'm grabbing it in node-red
[1:39] when i'm grabbing it in node-red
[1:39] when i'm grabbing it in node-red and then when you finally print the
[1:42] and then when you finally print the
[1:42] and then when you finally print the values
[1:43] values
[1:43] values they look like this so if i run the l3
[1:45] they look like this so if i run the l3
[1:46] they look like this so if i run the l3 program
[1:47] program
[1:47] program i'm using sudo python 3 l3 chart enter
[1:52] i'm using sudo python 3 l3 chart enter
[1:52] i'm using sudo python 3 l3 chart enter and now it's starting to grab these
[1:53] and now it's starting to grab these
[1:53] and now it's starting to grab these values and i'll and i'll show what it
[1:55] values and i'll and i'll show what it
[1:55] values and i'll and i'll show what it looks like
[1:56] looks like
[1:56] looks like um this is left
[2:00] um this is left
[2:00] um this is left direction this is the right direction
[2:05] direction this is the right direction
[2:05] direction this is the right direction this is down and this is
[2:08] this is down and this is
[2:08] this is down and this is up i thought i saw no positive here's a
[2:12] up i thought i saw no positive here's a
[2:12] up i thought i saw no positive here's a positive
[2:12] positive
[2:12] positive here's the negative okay it'll be easier
[2:15] here's the negative okay it'll be easier
[2:15] here's the negative okay it'll be easier to see it on the gauges
[2:21] over here in node-red i have first
[2:21] over here in node-red i have first removed the timestamp and i just want to
[2:24] removed the timestamp and i just want to
[2:24] removed the timestamp and i just want to show you
[2:24] show you
[2:24] show you that i'm doing this and i've replaced it
[2:27] that i'm doing this and i've replaced it
[2:27] that i'm doing this and i've replaced it with this cool function called
[2:28] with this cool function called
[2:28] with this cool function called watch and what it does is it watches
[2:31] watch and what it does is it watches
[2:31] watch and what it does is it watches this file and it only
[2:33] this file and it only
[2:33] this file and it only injects a trigger whenever there's a
[2:35] injects a trigger whenever there's a
[2:35] injects a trigger whenever there's a change in this file so that's neat that
[2:37] change in this file so that's neat that
[2:37] change in this file so that's neat that means
[2:38] means
[2:38] means node-red is basically going to match the
[2:40] node-red is basically going to match the
[2:40] node-red is basically going to match the frequency
[2:41] frequency
[2:41] frequency of my python program over here
[2:44] of my python program over here
[2:44] of my python program over here automatically
[2:45] automatically
[2:45] automatically now it goes to the the ufo file.txt
[2:50] now it goes to the the ufo file.txt
[2:50] now it goes to the the ufo file.txt and it reads it okay this hasn't changed
[2:52] and it reads it okay this hasn't changed
[2:52] and it reads it okay this hasn't changed from the last one
[2:54] from the last one
[2:54] from the last one and then the values are parsed
[2:57] and then the values are parsed
[2:57] and then the values are parsed by treating it as a csv file so
[3:00] by treating it as a csv file so
[3:00] by treating it as a csv file so if i remove this then it's just telling
[3:03] if i remove this then it's just telling
[3:03] if i remove this then it's just telling you that
[3:03] you that
[3:04] you that we're naming the columns explicitly here
[3:07] we're naming the columns explicitly here
[3:07] we're naming the columns explicitly here in the node but we're not passing the
[3:09] in the node but we're not passing the
[3:09] in the node but we're not passing the column names
[3:11] column names
[3:11] column names okay that hasn't changed and then the
[3:14] okay that hasn't changed and then the
[3:14] okay that hasn't changed and then the function
[3:14] function
[3:14] function that i've added is the new piece that
[3:17] that i've added is the new piece that
[3:17] that i've added is the new piece that that we change or
[3:18] that we change or
[3:18] that we change or and that needs to be reviewed right now
[3:20] and that needs to be reviewed right now
[3:20] and that needs to be reviewed right now in this video
[3:26] let's open up grab tdot which is the
[3:26] let's open up grab tdot which is the function that
[3:27] function that
[3:27] function that that takes the values both stored in csv
[3:31] that takes the values both stored in csv
[3:31] that takes the values both stored in csv and grabs just one of them so i can get
[3:33] and grabs just one of them so i can get
[3:34] and grabs just one of them so i can get my theta dot
[3:34] my theta dot
[3:34] my theta dot command so this has some residual
[3:38] command so this has some residual
[3:38] command so this has some residual comments
[3:39] comments
[3:39] comments but the only lines that we're using is
[3:42] but the only lines that we're using is
[3:42] but the only lines that we're using is message.payload equals
[3:45] message.payload equals
[3:45] message.payload equals message.payload with um this syntax here
[3:48] message.payload with um this syntax here
[3:48] message.payload with um this syntax here that reaches in
[3:49] that reaches in
[3:49] that reaches in and grabs the the gamepad theta dot
[3:53] and grabs the the gamepad theta dot
[3:53] and grabs the the gamepad theta dot parameter from the object
[3:57] parameter from the object
[3:57] parameter from the object and there's another way to do that
[3:59] and there's another way to do that
[3:59] and there's another way to do that that's slightly simpler i'll show you in
[4:01] that's slightly simpler i'll show you in
[4:01] that's slightly simpler i'll show you in the next one so we return the message
[4:03] the next one so we return the message
[4:03] the next one so we return the message that
[4:03] that
[4:03] that that used to have two values and now it
[4:05] that used to have two values and now it
[4:05] that used to have two values and now it just has one value the t
[4:07] just has one value the t
[4:07] just has one value the t dot okay then the grab
[4:10] dot okay then the grab
[4:10] dot okay then the grab x dot is very similar it's a cleaner
[4:13] x dot is very similar it's a cleaner
[4:13] x dot is very similar it's a cleaner looking
[4:13] looking
[4:14] looking though and what we do is we take the
[4:15] though and what we do is we take the
[4:15] though and what we do is we take the message.payload and we reassign it to b
[4:22] message.payload.gpx.
[4:22] message.payload.gpx. so this part of the payload is the
[4:26] so this part of the payload is the
[4:26] so this part of the payload is the parameter
[4:27] parameter
[4:27] parameter within the object um that we're gonna
[4:30] within the object um that we're gonna
[4:30] within the object um that we're gonna we're gonna take that parameter and sign
[4:31] we're gonna take that parameter and sign
[4:31] we're gonna take that parameter and sign it back to the payload move it one level
[4:33] it back to the payload move it one level
[4:33] it back to the payload move it one level up basically
[4:35] up basically
[4:35] up basically and we return that and both of these
[4:37] and we return that and both of these
[4:37] and we return that and both of these functions do the exact same thing
[4:39] functions do the exact same thing
[4:39] functions do the exact same thing but today i learned there's two ways to
[4:41] but today i learned there's two ways to
[4:41] but today i learned there's two ways to do it i'm going to deploy this now
[4:45] do it i'm going to deploy this now
[4:45] do it i'm going to deploy this now and then i'm going to manually overwrite
[4:48] and then i'm going to manually overwrite
[4:48] and then i'm going to manually overwrite the txt file because i want to see if it
[4:50] the txt file because i want to see if it
[4:50] the txt file because i want to see if it grabs my change so
[4:53] grabs my change so
[4:53] grabs my change so cd tmp slash tmp
[4:58] cd tmp slash tmp
[4:58] cd tmp slash tmp and i want to do uh cat no no
[5:01] and i want to do uh cat no no
[5:01] and i want to do uh cat no no nano u file
[5:05] nano u file
[5:05] nano u file and i'm going to change this to minus
[5:08] and i'm going to change this to minus
[5:08] and i'm going to change this to minus 0.1
[5:17] and then ctrl x to exit y enter
[5:17] and then ctrl x to exit y enter okay permission denied oh i need to
[5:21] okay permission denied oh i need to
[5:21] okay permission denied oh i need to have sudo into this in the temporary
[5:24] have sudo into this in the temporary
[5:24] have sudo into this in the temporary folder you have to be
[5:25] folder you have to be
[5:25] folder you have to be the super user so sudo
[5:28] the super user so sudo
[5:28] the super user so sudo this then i can change this to
[5:32] this then i can change this to
[5:32] this then i can change this to say minus 0.5 and click
[5:35] say minus 0.5 and click
[5:35] say minus 0.5 and click type control x y enter
[5:38] type control x y enter
[5:38] type control x y enter and then what i expected to see was
[5:41] and then what i expected to see was
[5:41] and then what i expected to see was maybe this
[5:43] maybe this
[5:43] maybe this would be running and capture a change
[5:47] would be running and capture a change
[5:47] would be running and capture a change oh this is disabled
[5:50] oh this is disabled
[5:50] oh this is disabled well i'll keep that in the video so we
[5:52] well i'll keep that in the video so we
[5:52] well i'll keep that in the video so we can learn the lesson
[5:54] can learn the lesson
[5:54] can learn the lesson deploy now let's change it again
[6:06] 0.6 control x y enter
[6:06] 0.6 control x y enter and boom we get all these debug
[6:08] and boom we get all these debug
[6:08] and boom we get all these debug informations
[6:09] informations
[6:09] informations so debug 1 is shown here
[6:12] so debug 1 is shown here
[6:12] so debug 1 is shown here it sees just the exactly the string that
[6:15] it sees just the exactly the string that
[6:15] it sees just the exactly the string that it read
[6:17] it read
[6:17] it read debug 2 has converted it into
[6:20] debug 2 has converted it into
[6:20] debug 2 has converted it into um an array because that's what this is
[6:22] um an array because that's what this is
[6:22] um an array because that's what this is supposed to do
[6:24] supposed to do
[6:24] supposed to do debug three um i don't i can't say much
[6:27] debug three um i don't i can't say much
[6:27] debug three um i don't i can't say much about this but obviously it's changed
[6:29] about this but obviously it's changed
[6:29] about this but obviously it's changed again
[6:30] again
[6:30] again and debug four looks a lot like debug
[6:32] and debug four looks a lot like debug
[6:32] and debug four looks a lot like debug three so let's dive
[6:34] three so let's dive
[6:34] three so let's dive into the actual um
[6:37] into the actual um
[6:37] into the actual um dashboard
[6:44] okay now i'm going to run l3 chart
[6:44] okay now i'm going to run l3 chart and then we're going to look at the
[6:46] and then we're going to look at the
[6:46] and then we're going to look at the values on the actual graph
[6:53] so when we come over to the gamepad and
[6:53] so when we come over to the gamepad and we look at the axes we have the
[6:55] we look at the axes we have the
[6:55] we look at the axes we have the the left and right where left turn is
[6:58] the left and right where left turn is
[6:58] the left and right where left turn is actually the positive
[6:59] actually the positive
[6:59] actually the positive theta dot request from the gamepad this
[7:02] theta dot request from the gamepad this
[7:02] theta dot request from the gamepad this is according to the scuttle coordinate
[7:04] is according to the scuttle coordinate
[7:04] is according to the scuttle coordinate system and then the right turn gives us
[7:06] system and then the right turn gives us
[7:06] system and then the right turn gives us the negative value
[7:08] the negative value
[7:08] the negative value and the x is one for the x dot
[7:11] and the x is one for the x dot
[7:11] and the x is one for the x dot forward motion the forward gives us a
[7:14] forward motion the forward gives us a
[7:14] forward motion the forward gives us a positive and the down
[7:15] positive and the down
[7:15] positive and the down gives us a negative

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
