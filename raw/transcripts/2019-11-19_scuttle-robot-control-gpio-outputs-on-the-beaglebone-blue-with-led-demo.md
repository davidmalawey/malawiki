---
title: "SCUTTLE Robot - Control GPIO Outputs on the BeagleBone Blue with LED Demo"
url: "https://www.youtube.com/watch?v=rYfygKmDT4Q"
video_id: "rYfygKmDT4Q"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-11-19
duration: "2:27"
duration_sec: 147
views: 686
likes: 2
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/rYfygKmDT4Q/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 86
chapters_count: 0
has_description: true
has_comments: false
---

## Description

How to connect a general purpose output to the beagle with Scuttle Robot, and L1_gpio.py

## Transcript

[0:02] if you're controlling output pins it's
[0:03] if you're controlling output pins it's smart to start with the gp1 connector
[0:06] smart to start with the gp1 connector
[0:06] smart to start with the gp1 connector here which is the leftmost on the board
[0:09] here which is the leftmost on the board
[0:09] here which is the leftmost on the board and the reason I'm choosing this one to
[0:11] and the reason I'm choosing this one to
[0:11] and the reason I'm choosing this one to start with is because these two outputs
[0:13] start with is because these two outputs
[0:13] start with is because these two outputs also correspond to the green and red
[0:16] also correspond to the green and red
[0:16] also correspond to the green and red LEDs so it gives you extra feedback
[0:18] LEDs so it gives you extra feedback
[0:18] LEDs so it gives you extra feedback about the condition of the pin by
[0:21] about the condition of the pin by
[0:21] about the condition of the pin by default on the board and it's referring
[0:23] default on the board and it's referring
[0:23] default on the board and it's referring to green and red as these LEDs that are
[0:26] to green and red as these LEDs that are
[0:26] to green and red as these LEDs that are close to what they call the user LEDs 1
[0:30] close to what they call the user LEDs 1
[0:30] close to what they call the user LEDs 1 2 3 0 1 2 3 so what I have right now is
[0:34] 2 3 0 1 2 3 so what I have right now is
[0:34] 2 3 0 1 2 3 so what I have right now is a program running that's turning on the
[0:37] a program running that's turning on the
[0:37] a program running that's turning on the green LED for I think 3 seconds and off
[0:40] green LED for I think 3 seconds and off
[0:40] green LED for I think 3 seconds and off for 2 seconds and then the 6 pin jst
[0:44] for 2 seconds and then the 6 pin jst
[0:44] for 2 seconds and then the 6 pin jst connector has the leftmost wire in my
[0:49] connector has the leftmost wire in my
[0:49] connector has the leftmost wire in my case is the green one is on the same
[0:53] case is the green one is on the same
[0:53] case is the green one is on the same court as the green LED and the red is
[0:57] court as the green LED and the red is
[0:57] court as the green LED and the red is actually the next one which does not
[0:58] actually the next one which does not
[0:58] actually the next one which does not have a wire connected my my ground a
[1:02] have a wire connected my my ground a
[1:02] have a wire connected my my ground a ground wire right here is connected to a
[1:06] ground wire right here is connected to a
[1:06] ground wire right here is connected to a circuit and then this is my accessory so
[1:09] circuit and then this is my accessory so
[1:09] circuit and then this is my accessory so this could be a relay or some other
[1:13] this could be a relay or some other
[1:13] this could be a relay or some other device that's activated by logic level
[1:15] device that's activated by logic level
[1:15] device that's activated by logic level high and low where my ground is going to
[1:18] high and low where my ground is going to
[1:18] high and low where my ground is going to the ground of the breadboard and then my
[1:22] the ground of the breadboard and then my
[1:22] the ground of the breadboard and then my my high voltage 3 point 3 or 0 is in the
[1:27] my high voltage 3 point 3 or 0 is in the
[1:27] my high voltage 3 point 3 or 0 is in the first row which goes to the positive pin
[1:30] first row which goes to the positive pin
[1:30] first row which goes to the positive pin of this LED then the negative pin of the
[1:34] of this LED then the negative pin of the
[1:34] of this LED then the negative pin of the LED travels through the 1k ohm resistor
[1:39] LED travels through the 1k ohm resistor
[1:39] LED travels through the 1k ohm resistor and then back to the ground and then you
[1:42] and then back to the ground and then you
[1:42] and then back to the ground and then you can see that these two green lights are
[1:45] can see that these two green lights are
[1:45] can see that these two green lights are being synchronized
[1:52] so this is nice if you're connecting a
[1:52] so this is nice if you're connecting a new actuator for the first time you can
[1:54] new actuator for the first time you can
[1:54] new actuator for the first time you can get the feedback if you use these two
[1:56] get the feedback if you use these two
[1:56] get the feedback if you use these two channels and then on the software the
[2:01] channels and then on the software the
[2:01] channels and then on the software the level one folder the level one file
[2:04] level one folder the level one file
[2:04] level one folder the level one file that's controlling this is called GPIO
[2:08] that's controlling this is called GPIO
[2:08] that's controlling this is called GPIO PI and we're gonna come out with a an
[2:11] PI and we're gonna come out with a an
[2:11] PI and we're gonna come out with a an updated version of this very soon but it
[2:14] updated version of this very soon but it
[2:14] updated version of this very soon but it will still look very similar the loop
[2:18] will still look very similar the loop
[2:18] will still look very similar the loop just has initialized the pin and then
[2:22] just has initialized the pin and then
[2:22] just has initialized the pin and then drive it high and drive it low in the
[2:25] drive it high and drive it low in the
[2:25] drive it high and drive it low in the sequence

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
