---
title: "SCUTTLE Robot - Plot Gamepad values in Nodered via txt file"
url: "https://www.youtube.com/watch?v=EQzNhDv-AKI"
video_id: "EQzNhDv-AKI"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-06
duration: "6:35"
duration_sec: 395
views: 344
likes: 6
category: "Education"
keywords: ["beaglebone", "nodered", "open source robot", "educational robotics", "gui", "telemetry", "csv", "logging", "SCUTTLE", "mobileRobot", "mobile robot"]
thumbnail_url: "https://i.ytimg.com/vi/EQzNhDv-AKI/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 302
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://MXET.github.io/SCUTTLE

Next step: get both values from one file: https://youtu.be/hzgSystU4yI

Nodered flow for this project: https://gist.github.com/dmalawey/e52e4492d373fda80928d054d87c0f9d

How to get a variable value from one gamepad axis, save it into a text file (temporary file) and retrieve it in NodeRed for plotting.  Choose your frequency of writing file and updating the chart.   Choose the location of the generated txt file.  Use lower level programs: gamepad.py and log.py

## Transcript

[0:03] hello this video is to show the
[0:03] hello this video is to show the minimum number of steps to capture the
[0:05] minimum number of steps to capture the
[0:05] minimum number of steps to capture the gamepad information
[0:07] gamepad information
[0:07] gamepad information on your linux machine grab that
[0:10] on your linux machine grab that
[0:10] on your linux machine grab that in node-red and start graphing it so
[0:14] in node-red and start graphing it so
[0:14] in node-red and start graphing it so let's look at the node-red space
[0:17] let's look at the node-red space
[0:17] let's look at the node-red space it all starts with the timestamp because
[0:19] it all starts with the timestamp because
[0:19] it all starts with the timestamp because you're injecting
[0:20] you're injecting
[0:20] you're injecting a call to request something is done
[0:24] a call to request something is done
[0:24] a call to request something is done every 0.25 seconds you have to choose
[0:26] every 0.25 seconds you have to choose
[0:26] every 0.25 seconds you have to choose the interval
[0:28] the interval
[0:28] the interval and it doesn't matter if this box is
[0:31] and it doesn't matter if this box is
[0:31] and it doesn't matter if this box is checked but basically
[0:32] checked but basically
[0:32] checked but basically you want it to be fairly rapid so i did
[0:34] you want it to be fairly rapid so i did
[0:34] you want it to be fairly rapid so i did every 0.25 seconds
[0:36] every 0.25 seconds
[0:36] every 0.25 seconds and i don't mess with this stuff these
[0:37] and i don't mess with this stuff these
[0:37] and i don't mess with this stuff these are defaults
[0:39] are defaults
[0:39] are defaults done now we're going to read a file
[0:43] done now we're going to read a file
[0:43] done now we're going to read a file there's a folder um at a pretty high
[0:46] there's a folder um at a pretty high
[0:46] there's a folder um at a pretty high level directory called tmp
[0:48] level directory called tmp
[0:48] level directory called tmp that's designed for temporary files that
[0:51] that's designed for temporary files that
[0:51] that's designed for temporary files that are produced during running we're going
[0:54] are produced during running we're going
[0:54] are produced during running we're going to create
[0:55] to create
[0:55] to create ufile.txt for
[0:58] ufile.txt for
[0:58] ufile.txt for unique file you'll see why
[1:01] unique file you'll see why
[1:01] unique file you'll see why it's just a single file with a single
[1:04] it's just a single file with a single
[1:04] it's just a single file with a single value in it
[1:05] value in it
[1:05] value in it that's an integer in our case or it may
[1:07] that's an integer in our case or it may
[1:07] that's an integer in our case or it may be a float
[1:09] be a float
[1:09] be a float doesn't really matter as long as it's
[1:11] doesn't really matter as long as it's
[1:11] doesn't really matter as long as it's only the number
[1:12] only the number
[1:12] only the number now that's been created and this slash
[1:15] now that's been created and this slash
[1:15] now that's been created and this slash here is important
[1:20] next we're going to grab that value and
[1:20] next we're going to grab that value and it's going to go out to
[1:22] it's going to go out to
[1:22] it's going to go out to two different places right now we have
[1:24] two different places right now we have
[1:24] two different places right now we have this chart
[1:25] this chart
[1:25] this chart we have this graph gauge
[1:29] we have this graph gauge
[1:29] we have this graph gauge so the gauge is configured like this
[1:32] so the gauge is configured like this
[1:32] so the gauge is configured like this default location the gauge is the type
[1:35] default location the gauge is the type
[1:36] default location the gauge is the type the name tells us what's it reading
[1:38] the name tells us what's it reading
[1:38] the name tells us what's it reading units or percent but this is
[1:40] units or percent but this is
[1:40] units or percent but this is this doesn't change the output it just
[1:42] this doesn't change the output it just
[1:42] this doesn't change the output it just changes what it's
[1:43] changes what it's
[1:43] changes what it's called um and then i set the the range
[1:47] called um and then i set the the range
[1:47] called um and then i set the the range from minus 100 to 100 because we're
[1:49] from minus 100 to 100 because we're
[1:49] from minus 100 to 100 because we're going to
[1:50] going to
[1:50] going to take this
[1:53] take this
[1:53] take this axis and we're going to capture it and
[1:55] axis and we're going to capture it and
[1:55] axis and we're going to capture it and it goes between 0
[1:56] it goes between 0
[1:56] it goes between 0 -1 and 1 we'll scale it up
[2:00] -1 and 1 we'll scale it up
[2:00] -1 and 1 we'll scale it up okay that's all now
[2:04] okay that's all now
[2:04] okay that's all now for the chart it's basically the same
[2:06] for the chart it's basically the same
[2:06] for the chart it's basically the same kind of thing with a different output
[2:08] kind of thing with a different output
[2:08] kind of thing with a different output we name it no that's not right we're
[2:10] we name it no that's not right we're
[2:10] we name it no that's not right we're going to say gamepad
[2:12] going to say gamepad
[2:12] going to say gamepad axis zero chart
[2:15] axis zero chart
[2:16] axis zero chart leave it as line chart you choose how
[2:18] leave it as line chart you choose how
[2:18] leave it as line chart you choose how many points you want to
[2:19] many points you want to
[2:19] many points you want to collect and you choose the axes
[2:23] collect and you choose the axes
[2:23] collect and you choose the axes bounds
[2:29] that this is the name that shows up just
[2:29] that this is the name that shows up just in your
[2:30] in your
[2:30] in your dashboard here no in your
[2:37] this screen i'm forgetting the name
[2:37] this screen i'm forgetting the name right now
[2:38] right now
[2:38] right now so we deploy and then you want to see it
[2:41] so we deploy and then you want to see it
[2:41] so we deploy and then you want to see it so you can um
[2:51] where's my where's my tab you click here
[2:51] where's my where's my tab you click here you click on this little button and then
[2:54] you click on this little button and then
[2:54] you click on this little button and then this is the button that brings you the
[2:56] this is the button that brings you the
[2:56] this is the button that brings you the dashboard so if it's closed
[2:59] dashboard so if it's closed
[2:59] dashboard so if it's closed open the dashboard okay now i've got
[3:01] open the dashboard okay now i've got
[3:01] open the dashboard okay now i've got values
[3:02] values
[3:02] values and they're not changing by the way
[3:03] and they're not changing by the way
[3:03] and they're not changing by the way we're getting a whole bunch of zeros
[3:06] we're getting a whole bunch of zeros
[3:06] we're getting a whole bunch of zeros so how do we produce those values um
[3:09] so how do we produce those values um
[3:09] so how do we produce those values um i want to come over here to um
[3:13] i want to come over here to um
[3:13] i want to come over here to um my uh my shell and
[3:16] my uh my shell and
[3:16] my uh my shell and i'm gonna um i don't need to go to the
[3:20] i'm gonna um i don't need to go to the
[3:20] i'm gonna um i don't need to go to the tmp directory that's gonna be
[3:22] tmp directory that's gonna be
[3:22] tmp directory that's gonna be produced automatically so um
[3:26] produced automatically so um
[3:26] produced automatically so um let's see we're in the folder called pi
[3:29] let's see we're in the folder called pi
[3:29] let's see we're in the folder called pi scuttle
[3:30] scuttle
[3:30] scuttle uh if you go up one directory you'll see
[3:32] uh if you go up one directory you'll see
[3:32] uh if you go up one directory you'll see this is kind of our home
[3:34] this is kind of our home
[3:34] this is kind of our home and um pi scuttle is our folder where we
[3:37] and um pi scuttle is our folder where we
[3:37] and um pi scuttle is our folder where we want to
[3:38] want to
[3:38] want to work so cd pi scuttle
[3:42] work so cd pi scuttle
[3:42] work so cd pi scuttle all right and then um the program that
[3:45] all right and then um the program that
[3:45] all right and then um the program that we use
[3:45] we use
[3:46] we use today is called l3 chart and show you
[3:49] today is called l3 chart and show you
[3:49] today is called l3 chart and show you what we've put inside of it um nano
[3:54] what we've put inside of it um nano
[3:54] what we've put inside of it um nano l3 tab gets you the chart and i'm maybe
[3:58] l3 tab gets you the chart and i'm maybe
[3:58] l3 tab gets you the chart and i'm maybe playing with the naming convention i
[3:59] playing with the naming convention i
[3:59] playing with the naming convention i left out the underscore
[4:01] left out the underscore
[4:01] left out the underscore all right we import time this is a
[4:04] all right we import time this is a
[4:04] all right we import time this is a common library
[4:11] and we import two other lower level
[4:11] and we import two other lower level function um programs python programs
[4:14] function um programs python programs
[4:14] function um programs python programs gamepad and log we'll go through those
[4:17] gamepad and log we'll go through those
[4:18] gamepad and log we'll go through those in another video
[4:20] in another video
[4:20] in another video and we're grabbing a function from each
[4:22] and we're grabbing a function from each
[4:22] and we're grabbing a function from each of those
[4:23] of those
[4:23] of those from gamepad we're grabbing get gp
[4:26] from gamepad we're grabbing get gp
[4:26] from gamepad we're grabbing get gp that collects all of the values from all
[4:29] that collects all of the values from all
[4:29] that collects all of the values from all the buttons in one go
[4:31] the buttons in one go
[4:31] the buttons in one go and it stores it to gp data access 0 and
[4:34] and it stores it to gp data access 0 and
[4:34] and it stores it to gp data access 0 and axis 1
[4:35] axis 1
[4:35] axis 1 are extracting this axis
[4:38] are extracting this axis
[4:38] are extracting this axis up and down in this axis left and right
[4:41] up and down in this axis left and right
[4:41] up and down in this axis left and right some of these buttons are binary but
[4:43] some of these buttons are binary but
[4:43] some of these buttons are binary but this one actually has a floating point
[4:45] this one actually has a floating point
[4:45] this one actually has a floating point so we have two pieces of data we're only
[4:47] so we have two pieces of data we're only
[4:47] so we have two pieces of data we're only going to use one
[4:49] going to use one
[4:49] going to use one now the log function we're doing
[4:52] now the log function we're doing
[4:52] now the log function we're doing log dot tmp file and then we need to
[4:55] log dot tmp file and then we need to
[4:55] log dot tmp file and then we need to give it two arguments the first argument
[4:57] give it two arguments the first argument
[4:57] give it two arguments the first argument is the value produced by my
[5:00] is the value produced by my
[5:00] is the value produced by my my right and left axis and the second
[5:03] my right and left axis and the second
[5:03] my right and left axis and the second one
[5:03] one
[5:04] one is um the name of the file that's going
[5:06] is um the name of the file that's going
[5:06] is um the name of the file that's going to be
[5:07] to be
[5:07] to be created if it's not already there called
[5:10] created if it's not already there called
[5:10] created if it's not already there called ufile.txt so it's going to overwrite
[5:13] ufile.txt so it's going to overwrite
[5:13] ufile.txt so it's going to overwrite this one constantly
[5:15] this one constantly
[5:15] this one constantly next we just put a small sleep in there
[5:18] next we just put a small sleep in there
[5:18] next we just put a small sleep in there at
[5:18] at
[5:18] at 0.25 seconds so same frequency we're
[5:22] 0.25 seconds so same frequency we're
[5:22] 0.25 seconds so same frequency we're plotting
[5:23] plotting
[5:23] plotting control x closes it and then we can
[5:26] control x closes it and then we can
[5:26] control x closes it and then we can actually
[5:26] actually
[5:26] actually just run it um
[5:29] just run it um
[5:29] just run it um python let's try without sudo python3
[5:33] python let's try without sudo python3
[5:33] python let's try without sudo python3 l3 tab enter
[5:39] l3 tab enter
[5:39] l3 tab enter permission9 okay let's try this again
[5:41] permission9 okay let's try this again
[5:42] permission9 okay let's try this again with sudo
[5:49] all right the no protocol specified is
[5:49] all right the no protocol specified is not an error that's going to stop us so
[5:52] not an error that's going to stop us so
[5:52] not an error that's going to stop us so now that file is getting overwritten
[5:54] now that file is getting overwritten
[5:54] now that file is getting overwritten i won't show you but i promise it is and
[5:57] i won't show you but i promise it is and
[5:58] i won't show you but i promise it is and as long as um these but these lights are
[6:00] as long as um these but these lights are
[6:00] as long as um these but these lights are indicating i'm connected so now
[6:02] indicating i'm connected so now
[6:02] indicating i'm connected so now now i'm just plotting this one single
[6:04] now i'm just plotting this one single
[6:04] now i'm just plotting this one single axis
[6:06] axis
[6:06] axis and if i go to the right now
[6:09] and if i go to the right now
[6:09] and if i go to the right now everything's reversed i'm not sure
[6:10] everything's reversed i'm not sure
[6:10] everything's reversed i'm not sure what's going on but
[6:11] what's going on but
[6:11] what's going on but one direction gives me the negative
[6:13] one direction gives me the negative
[6:13] one direction gives me the negative values max it out
[6:15] values max it out
[6:15] values max it out you get minus 100 the other direction
[6:17] you get minus 100 the other direction
[6:17] you get minus 100 the other direction gives you the
[6:19] gives you the
[6:19] gives you the positive values max it out you get
[6:22] positive values max it out you get
[6:22] positive values max it out you get positive 100
[6:24] positive 100
[6:24] positive 100 and now you can start plotting away
[6:27] and now you can start plotting away
[6:27] and now you can start plotting away and in the next steps we would add more
[6:30] and in the next steps we would add more
[6:30] and in the next steps we would add more data to this file
[6:31] data to this file
[6:31] data to this file and and plot several things at once

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
