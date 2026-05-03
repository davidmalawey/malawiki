---
title: "SCUTTLE Robot - setup vscode to connect to pi and edit software (cloud9 alternative)"
url: "https://www.youtube.com/watch?v=HokkkHJgUOo"
video_id: "HokkkHJgUOo"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-09
duration: "4:13"
duration_sec: 253
views: 77
likes: 4
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/HokkkHJgUOo/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 208
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: mxet.github.io/SCUTTLE

This video is a summary of why you may want vs code connected to your SCUTTLE, why it helps, how to configure the SFTP connection, and introduction to browsing directories and editing python programs.

Copy and Paste my Configuration File:
https://gist.github.com/dmalawey/46173ac9faf84975c8b31054ea98800d

## Transcript

[0:03] if you are using putty like this one
[0:03] if you are using putty like this one or um mobax term like this over here to
[0:07] or um mobax term like this over here to
[0:07] or um mobax term like this over here to connect to your robot
[0:08] connect to your robot
[0:08] connect to your robot and start programming python files
[0:11] and start programming python files
[0:11] and start programming python files it can be pretty inconvenient because
[0:13] it can be pretty inconvenient because
[0:13] it can be pretty inconvenient because the nano text editor
[0:15] the nano text editor
[0:15] the nano text editor is just not very dynamic so
[0:18] is just not very dynamic so
[0:18] is just not very dynamic so one really nice tool is called vs code
[0:21] one really nice tool is called vs code
[0:21] one really nice tool is called vs code visual studio code and shout out to
[0:24] visual studio code and shout out to
[0:24] visual studio code and shout out to danielle for showing me how to set this
[0:26] danielle for showing me how to set this
[0:26] danielle for showing me how to set this up in the first place
[0:28] up in the first place
[0:28] up in the first place you just need to go to the web find the
[0:30] you just need to go to the web find the
[0:30] you just need to go to the web find the download and
[0:31] download and
[0:31] download and get uh get the download according to
[0:33] get uh get the download according to
[0:33] get uh get the download according to your machine
[0:36] your machine
[0:36] your machine initially i didn't like to use this
[0:38] initially i didn't like to use this
[0:38] initially i didn't like to use this because you know as a mechanical
[0:39] because you know as a mechanical
[0:39] because you know as a mechanical engineer i'm thinking
[0:40] engineer i'm thinking
[0:40] engineer i'm thinking why do i need three or four softwares
[0:43] why do i need three or four softwares
[0:43] why do i need three or four softwares just to edit python files
[0:45] just to edit python files
[0:45] just to edit python files but after you spend some time
[0:47] but after you spend some time
[0:47] but after you spend some time programming you can benefit from the
[0:49] programming you can benefit from the
[0:49] programming you can benefit from the efficiency
[0:50] efficiency
[0:50] efficiency of a dynamic editor
[0:53] of a dynamic editor
[0:53] of a dynamic editor also i should note this isn't so
[0:55] also i should note this isn't so
[0:55] also i should note this isn't so important if you're
[0:56] important if you're
[0:56] important if you're already running cloud 9 which is
[0:58] already running cloud 9 which is
[0:58] already running cloud 9 which is installed on the beaglebone
[1:00] installed on the beaglebone
[1:00] installed on the beaglebone by default out of the box so vs code can
[1:04] by default out of the box so vs code can
[1:04] by default out of the box so vs code can remotely
[1:05] remotely
[1:05] remotely edit your python files live on your
[1:08] edit your python files live on your
[1:08] edit your python files live on your robot
[1:09] robot
[1:09] robot but first you have to set up the
[1:10] but first you have to set up the
[1:10] but first you have to set up the extensions so you can see
[1:12] extensions so you can see
[1:12] extensions so you can see on my install i have two extensions and
[1:15] on my install i have two extensions and
[1:15] on my install i have two extensions and the one we want to look at
[1:16] the one we want to look at
[1:16] the one we want to look at is this sftp the information for sftp
[1:21] is this sftp the information for sftp
[1:21] is this sftp the information for sftp can be found here on this web page and
[1:25] can be found here on this web page and
[1:25] can be found here on this web page and basically it's a step through a few
[1:28] basically it's a step through a few
[1:28] basically it's a step through a few clicks to install it and then you need
[1:31] clicks to install it and then you need
[1:31] clicks to install it and then you need to configure it to connect to your
[1:33] to configure it to connect to your
[1:33] to configure it to connect to your machine your robot so a configuration
[1:37] machine your robot so a configuration
[1:37] machine your robot so a configuration file is going to get added
[1:38] file is going to get added
[1:38] file is going to get added and i will show you how to do that now
[1:42] and i will show you how to do that now
[1:42] and i will show you how to do that now if i close this window then you're
[1:44] if i close this window then you're
[1:44] if i close this window then you're basically home
[1:45] basically home
[1:45] basically home and you can type control shift p and
[1:48] and you can type control shift p and
[1:48] and you can type control shift p and type in sftp
[1:52] type in sftp
[1:52] type in sftp colon config grab this option
[1:55] colon config grab this option
[1:55] colon config grab this option and it's going to open up a file that's
[1:57] and it's going to open up a file that's
[1:57] and it's going to open up a file that's basically configuring
[1:58] basically configuring
[1:58] basically configuring your vs codes connection over ssh
[2:02] your vs codes connection over ssh
[2:02] your vs codes connection over ssh so you name the connection however you
[2:04] so you name the connection however you
[2:04] so you name the connection however you want to you make the host
[2:06] want to you make the host
[2:06] want to you make the host line agree with the ip address of your
[2:10] line agree with the ip address of your
[2:10] line agree with the ip address of your machine
[2:11] machine
[2:11] machine your scuttle and you can leave these
[2:14] your scuttle and you can leave these
[2:14] your scuttle and you can leave these components
[2:15] components
[2:15] components these components must agree with your
[2:17] these components must agree with your
[2:17] these components must agree with your login for your
[2:18] login for your
[2:18] login for your raspberry pi or linux machine and then
[2:21] raspberry pi or linux machine and then
[2:22] raspberry pi or linux machine and then you can leave these components as they
[2:24] you can leave these components as they
[2:24] you can leave these components as they are and then control
[2:26] are and then control
[2:26] are and then control s to save and close that
[2:31] s to save and close that
[2:31] s to save and close that at this time if i open up my sftp menu
[2:34] at this time if i open up my sftp menu
[2:34] at this time if i open up my sftp menu and right click
[2:35] and right click
[2:35] and right click and hit control um open ssh in terminal
[2:39] and hit control um open ssh in terminal
[2:39] and hit control um open ssh in terminal then enter my password you are now
[2:43] then enter my password you are now
[2:43] then enter my password you are now involved in an ssh session with your
[2:47] involved in an ssh session with your
[2:47] involved in an ssh session with your robot inside the vs workspace
[2:52] robot inside the vs workspace
[2:52] robot inside the vs workspace see and you can see your your files and
[2:54] see and you can see your your files and
[2:54] see and you can see your your files and do all your ssh stuff
[2:58] do all your ssh stuff
[2:58] do all your ssh stuff the next thing is you can drop this down
[3:02] the next thing is you can drop this down
[3:02] the next thing is you can drop this down and discover all your files if you want
[3:05] and discover all your files if you want
[3:05] and discover all your files if you want to
[3:05] to
[3:05] to start manipulating file we can go to a
[3:08] start manipulating file we can go to a
[3:08] start manipulating file we can go to a familiar one
[3:10] familiar one
[3:10] familiar one pi scuttle and l3
[3:14] pi scuttle and l3
[3:14] pi scuttle and l3 chart.pi if you double click it then you
[3:17] chart.pi if you double click it then you
[3:17] chart.pi if you double click it then you can
[3:17] can
[3:18] can view everything in here but you can't
[3:19] view everything in here but you can't
[3:19] view everything in here but you can't start editing so you cannot edit in read
[3:21] start editing so you cannot edit in read
[3:21] start editing so you cannot edit in read only editor
[3:23] only editor
[3:23] only editor so what you can do is close this
[3:26] so what you can do is close this
[3:26] so what you can do is close this and right click edit in local that's
[3:29] and right click edit in local that's
[3:29] and right click edit in local that's going to produce a copy
[3:30] going to produce a copy
[3:30] going to produce a copy of the file here on your local machine
[3:33] of the file here on your local machine
[3:33] of the file here on your local machine instead of on your robot and let's say
[3:37] instead of on your robot and let's say
[3:37] instead of on your robot and let's say we want to
[3:38] we want to
[3:38] we want to comment all this out it's very
[3:39] comment all this out it's very
[3:39] comment all this out it's very convenient control
[3:41] convenient control
[3:41] convenient control slash now i've commented the while loop
[3:45] slash now i've commented the while loop
[3:45] slash now i've commented the while loop ctrl s to save close that
[3:48] ctrl s to save close that
[3:48] ctrl s to save close that and if you open it up again then you see
[3:50] and if you open it up again then you see
[3:50] and if you open it up again then you see your changes reflected
[3:57] the last thing to mention is just to be
[3:57] the last thing to mention is just to be careful since
[3:57] careful since
[3:58] careful since you do work with two different copies
[4:00] you do work with two different copies
[4:00] you do work with two different copies now
[4:01] now
[4:01] now when you have this tool and pay
[4:03] when you have this tool and pay
[4:03] when you have this tool and pay attention to little details like this
[4:05] attention to little details like this
[4:05] attention to little details like this circle here tells me i haven't saved it
[4:07] circle here tells me i haven't saved it
[4:07] circle here tells me i haven't saved it yet
[4:07] yet
[4:07] yet ctrl s changes it to an x and all those
[4:10] ctrl s changes it to an x and all those
[4:10] ctrl s changes it to an x and all those little clues
[4:11] little clues
[4:11] little clues help uh keep you safe

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
