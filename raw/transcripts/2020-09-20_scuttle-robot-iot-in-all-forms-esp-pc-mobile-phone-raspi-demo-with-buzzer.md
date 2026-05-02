---
title: "SCUTTLE Robot - IoT in ALL FORMS!  ESP / PC / Mobile Phone / RasPi / demo with BUZZER"
url: "https://www.youtube.com/watch?v=Vr_CxYMBWKY"
video_id: "Vr_CxYMBWKY"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-20
duration: "23:30"
duration_sec: 1410
views: 285
likes: 8
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/Vr_CxYMBWKY/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 964
chapters_count: 6
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://mxet.github.io/SCUTTLE

EVERYTHING is talking together on IoT:
[ Arduino ] - [ Raspberry Pi ] - [ Computer ] - [ Cell Phone ] - [ Beaglebone ]

Software:
[ C++ ] [ Python 3 ] [ Nodered ] [ Debian Linux ]

This video throws all the pieces together for the first time.  We show how to program an Arduino Microcontroller to receive MQTT messages from SCUTTLE - M2M style. Connect a buzzer to the Arduino and the Arduino stands alone on battery power to demonstrate RX of data based on the robot's motion.  The Robot creates a message in Python and sends it out using NodeRED. Lastly, we show again that we can send the same data from a Cell phone instead of from the robot.

## Chapters

- 0:00 <Untitled Chapter 1>
- 3:43 Mobile Phone Demos
- 7:35 Install the Node Red
- 15:24 Arduino
- 19:29 Gamepad Demo
- 23:03 Demo Mqtt from the Cell Phone to the Esp Device

## Transcript

[0:03] all right today's demo
[0:03] all right today's demo is the one that ties it all together
[0:07] is the one that ties it all together
[0:07] is the one that ties it all together and let me show you how so you have the
[0:10] and let me show you how so you have the
[0:10] and let me show you how so you have the the scuttle robot here
[0:25] and he's getting controlled today by
[0:25] and he's getting controlled today by the gamepad the xbox style gamepad
[0:31] the gamepad the xbox style gamepad
[0:31] the gamepad the xbox style gamepad all right and the connection here is
[0:35] all right and the connection here is
[0:35] all right and the connection here is with bluetooth let's get a little bigger
[0:45] okay and then scuttle is making
[0:45] okay and then scuttle is making connection
[0:45] connection
[0:45] connection over to the cloud
[0:49] over to the cloud
[0:49] over to the cloud via mqtt
[0:57] mqtt is the protocol
[0:57] mqtt is the protocol by which messages are going to get sent
[0:59] by which messages are going to get sent
[0:59] by which messages are going to get sent with a topic
[1:02] with a topic
[1:02] with a topic and a payload
[1:08] those two pieces of information are the
[1:08] those two pieces of information are the critical parts of the message
[1:10] critical parts of the message
[1:10] critical parts of the message and this is happening with uh an action
[1:13] and this is happening with uh an action
[1:13] and this is happening with uh an action called
[1:14] called
[1:14] called publishing okay
[1:17] publishing okay
[1:17] publishing okay and this is not publishing the only the
[1:20] and this is not publishing the only the
[1:20] and this is not publishing the only the pink one
[1:21] pink one
[1:21] pink one all right and then secondly we've also
[1:24] all right and then secondly we've also
[1:24] all right and then secondly we've also showed you on another occasion how
[1:27] showed you on another occasion how
[1:27] showed you on another occasion how you can have the esp device which is an
[1:31] you can have the esp device which is an
[1:31] you can have the esp device which is an arduino programmed gadget
[1:40] in this case it's at uh i have this cool
[1:40] in this case it's at uh i have this cool one that
[1:41] one that
[1:41] one that that supports an 18650 battery
[1:44] that supports an 18650 battery
[1:44] that supports an 18650 battery so that means it's a standalone device
[1:47] so that means it's a standalone device
[1:47] so that means it's a standalone device that's what they call it a
[1:52] that's what they call it a
[1:52] that's what they call it a called a wemo something
[1:58] that's if it's if it's branded and this
[1:58] that's if it's if it's branded and this is a
[1:59] is a
[1:59] is a super affordable nine dollars on amazon
[2:03] super affordable nine dollars on amazon
[2:03] super affordable nine dollars on amazon gadget and it's communicating over wi-fi
[2:06] gadget and it's communicating over wi-fi
[2:06] gadget and it's communicating over wi-fi so you have this action going on here
[2:09] so you have this action going on here
[2:10] so you have this action going on here today it's listening so
[2:13] today it's listening so
[2:13] today it's listening so we're not publishing instead we are
[2:15] we're not publishing instead we are
[2:15] we're not publishing instead we are subscribing
[2:21] and this arrow's going this way
[2:21] and this arrow's going this way not that one okay
[2:25] not that one okay
[2:25] not that one okay to the cloud using the same
[2:29] to the cloud using the same
[2:29] to the cloud using the same topic that's how you receive the payload
[2:32] topic that's how you receive the payload
[2:32] topic that's how you receive the payload okay and i've already shown in addition
[2:34] okay and i've already shown in addition
[2:34] okay and i've already shown in addition to that
[2:36] to that
[2:36] to that also how your pc
[2:52] um this can also perform the
[2:52] um this can also perform the publishing and subscribing and we've
[2:55] publishing and subscribing and we've
[2:55] publishing and subscribing and we've tested it
[2:56] tested it
[2:56] tested it in other videos and briefly today we're
[2:58] in other videos and briefly today we're
[2:58] in other videos and briefly today we're going to do this
[2:59] going to do this
[2:59] going to do this publishing to make sure verify the
[3:02] publishing to make sure verify the
[3:02] publishing to make sure verify the communication
[3:04] communication
[3:04] communication is received by the other devices
[3:08] is received by the other devices
[3:08] is received by the other devices okay but we also sub
[3:11] okay but we also sub
[3:12] okay but we also sub and the reason is
[3:26] this is just so convenient to do in the
[3:26] this is just so convenient to do in the web browser
[3:27] web browser
[3:27] web browser so we do the sub and we listen on the
[3:30] so we do the sub and we listen on the
[3:30] so we do the sub and we listen on the same topic that we
[3:32] same topic that we
[3:32] same topic that we publish and then that all works okay
[3:35] publish and then that all works okay
[3:35] publish and then that all works okay and then today's hardware
[3:38] and then today's hardware
[3:38] and then today's hardware before i get to that let's let's finish
[3:41] before i get to that let's let's finish
[3:41] before i get to that let's let's finish this off
[3:42] this off
[3:42] this off we also have the mobile phone demos
[3:45] we also have the mobile phone demos
[3:45] we also have the mobile phone demos and there's a couple of them so far
[3:47] and there's a couple of them so far
[3:47] and there's a couple of them so far there will be lots more
[3:48] there will be lots more
[3:48] there will be lots more because mobile phones are useful
[4:06] for mqtt such as mq
[4:06] for mqtt such as mq oops t
[4:09] oops t
[4:09] oops t tool that's just
[4:13] tool that's just
[4:13] tool that's just one of many
[4:20] and we do the same thing we
[4:20] and we do the same thing we publish to send commands and we
[4:22] publish to send commands and we
[4:22] publish to send commands and we subscribe
[4:24] subscribe
[4:24] subscribe um and then well how do we know that
[4:26] um and then well how do we know that
[4:26] um and then well how do we know that this little device here
[4:28] this little device here
[4:28] this little device here the esp device is getting the right
[4:32] the esp device is getting the right
[4:32] the esp device is getting the right information
[4:33] information
[4:33] information well that's what today is all about a
[4:35] well that's what today is all about a
[4:35] well that's what today is all about a cheap little
[4:37] cheap little
[4:37] cheap little simple two-wire speaker
[4:40] simple two-wire speaker
[4:40] simple two-wire speaker so let's stick with yellow
[4:44] so let's stick with yellow
[4:44] so let's stick with yellow and what does it do
[4:49] it's not even a speaker it's it's a
[4:49] it's not even a speaker it's it's a buzzer
[4:56] so this is transmitting whatever is
[4:56] so this is transmitting whatever is uh showing up here is also going here
[4:59] uh showing up here is also going here
[4:59] uh showing up here is also going here and then we we get a buzzing sound today
[5:02] and then we we get a buzzing sound today
[5:02] and then we we get a buzzing sound today and um and then that means without any
[5:05] and um and then that means without any
[5:05] and um and then that means without any um
[5:07] um
[5:07] um any interface such as the serial port
[5:10] any interface such as the serial port
[5:10] any interface such as the serial port without any wires without any displays
[5:13] without any wires without any displays
[5:13] without any wires without any displays you know that this little guy is talking
[5:15] you know that this little guy is talking
[5:15] you know that this little guy is talking and listening
[5:16] and listening
[5:16] and listening and um and it's all stand alone because
[5:19] and um and it's all stand alone because
[5:20] and um and it's all stand alone because it's on this
[5:20] it's on this
[5:20] it's on this this battery this 18650
[5:25] this battery this 18650
[5:25] this battery this 18650 so i think that's fantastic and the
[5:28] so i think that's fantastic and the
[5:28] so i think that's fantastic and the price is unbeatable this is
[5:30] price is unbeatable this is
[5:30] price is unbeatable this is ten five years ago this would have been
[5:32] ten five years ago this would have been
[5:32] ten five years ago this would have been unheard of
[5:34] unheard of
[5:34] unheard of and it was it was unheard of
[5:37] and it was it was unheard of
[5:37] and it was it was unheard of and what's the last parts of this oh the
[5:39] and what's the last parts of this oh the
[5:39] and what's the last parts of this oh the last part is
[5:41] last part is
[5:41] last part is how
[5:48] well that color is intense let's dial it
[5:48] well that color is intense let's dial it back
[6:04] how are we doing this publishing and
[6:04] how are we doing this publishing and subscribing here
[6:07] subscribing here
[6:07] subscribing here one
[6:14] what's the organization for this okay
[6:14] what's the organization for this okay this is through
[6:17] this is through
[6:17] this is through a web gui
[6:34] okay and then on the scuttle side
[6:34] okay and then on the scuttle side we say how
[6:42] and and that's in reference to this
[6:42] and and that's in reference to this thing here
[6:43] thing here
[6:43] thing here how are we publishing through scuttle on
[6:46] how are we publishing through scuttle on
[6:46] how are we publishing through scuttle on a wonderful thing called node-red
[6:54] which is a tool of course we could
[6:54] which is a tool of course we could install a library in python and just go
[6:56] install a library in python and just go
[6:56] install a library in python and just go straight from a python
[7:00] straight from a python
[7:00] straight from a python script to communicating and publishing
[7:03] script to communicating and publishing
[7:03] script to communicating and publishing but node-red is awesome because it can
[7:07] but node-red is awesome because it can
[7:07] but node-red is awesome because it can stand alone
[7:12] when you're not running any other
[7:12] when you're not running any other software on your
[7:14] software on your
[7:14] software on your linux machine you can just have the node
[7:17] linux machine you can just have the node
[7:17] linux machine you can just have the node red
[7:17] red
[7:17] red start up in the background and go
[7:19] start up in the background and go
[7:19] start up in the background and go automatically listening or
[7:21] automatically listening or
[7:21] automatically listening or or communicating on these channels about
[7:23] or communicating on these channels about
[7:23] or communicating on these channels about stuff like your battery
[7:25] stuff like your battery
[7:25] stuff like your battery okay runs in the background
[7:30] okay runs in the background
[7:30] okay runs in the background and then what else you've got
[7:33] and then what else you've got
[7:33] and then what else you've got how when you install the node red
[7:43] oh this is the beautiful part
[7:43] oh this is the beautiful part it is so versatile that it can do
[7:48] it is so versatile that it can do
[7:48] it is so versatile that it can do it can be installed on windows
[7:56] but through python it can be installed
[7:56] but through python it can be installed on linux
[8:11] but it's it's a fairly universal tool
[8:11] but it's it's a fairly universal tool and it's fairly lightweight because i've
[8:13] and it's fairly lightweight because i've
[8:13] and it's fairly lightweight because i've run it on both the pi and the beagle and
[8:16] run it on both the pi and the beagle and
[8:16] run it on both the pi and the beagle and other machines very smoothly and and i'm
[8:19] other machines very smoothly and and i'm
[8:19] other machines very smoothly and and i'm just
[8:20] just
[8:20] just so impressed because it looks nice
[8:26] so impressed because it looks nice
[8:26] so impressed because it looks nice you don't have to take my word for it
[8:29] you don't have to take my word for it
[8:29] you don't have to take my word for it this is
[8:30] this is
[8:30] this is i mean it's in it's in several of our
[8:31] i mean it's in it's in several of our
[8:32] i mean it's in it's in several of our demos okay
[8:33] demos okay
[8:33] demos okay and then the last part is what's going
[8:36] and then the last part is what's going
[8:36] and then the last part is what's going on
[8:38] on
[8:38] on here
[8:41] here
[8:41] here what's my computer
[8:53] that is
[8:54] that is it can be a beagle beaglebone blue
[9:00] which we have used tried and tested a
[9:00] which we have used tried and tested a lot
[9:02] lot
[9:02] lot it can be a raspberry pi
[9:05] it can be a raspberry pi
[9:05] it can be a raspberry pi or it can be a
[9:09] or it can be a
[9:10] or it can be a jetson nano honestly it can be any
[9:11] jetson nano honestly it can be any
[9:12] jetson nano honestly it can be any embedded computer but
[9:17] this is one that sounds really exciting
[9:17] this is one that sounds really exciting to start up soon
[9:19] to start up soon
[9:19] to start up soon because people are writing pretty
[9:21] because people are writing pretty
[9:21] because people are writing pretty advanced scripts
[9:23] advanced scripts
[9:23] advanced scripts that will work on node-red and do really
[9:26] that will work on node-red and do really
[9:26] that will work on node-red and do really nice stuff like
[9:28] nice stuff like
[9:28] nice stuff like [Music]
[9:29] [Music]
[9:29] [Music] interpreting information from photos and
[9:31] interpreting information from photos and
[9:31] interpreting information from photos and doing
[9:32] doing
[9:32] doing algorithms that that text to speech type
[9:35] algorithms that that text to speech type
[9:35] algorithms that that text to speech type of stuff and speech attacks and writing
[9:37] of stuff and speech attacks and writing
[9:37] of stuff and speech attacks and writing files and saving them in the background
[9:39] files and saving them in the background
[9:39] files and saving them in the background so here we are oops
[9:42] so here we are oops
[9:42] so here we are oops that's my other my other revisions up
[9:44] that's my other my other revisions up
[9:44] that's my other my other revisions up here okay so
[9:45] here okay so
[9:45] here okay so here we are today connecting so many of
[9:49] here we are today connecting so many of
[9:49] here we are today connecting so many of these pieces
[9:50] these pieces
[9:50] these pieces and just watch and learn
[9:58] okay so this here is a super simple
[9:58] okay so this here is a super simple diagram
[9:59] diagram
[9:59] diagram showing the buzzer is connected there's
[10:01] showing the buzzer is connected there's
[10:01] showing the buzzer is connected there's a button connected too but we're not
[10:02] a button connected too but we're not
[10:02] a button connected too but we're not using that for this video
[10:04] using that for this video
[10:04] using that for this video and up in the corner you can see the
[10:06] and up in the corner you can see the
[10:06] and up in the corner you can see the actual device on my very crummy webcam
[10:09] actual device on my very crummy webcam
[10:09] actual device on my very crummy webcam okay there's a button on the left four
[10:12] okay there's a button on the left four
[10:12] okay there's a button on the left four pins are connected
[10:13] pins are connected
[10:13] pins are connected and the little buzzer okay so
[10:17] and the little buzzer okay so
[10:17] and the little buzzer okay so we grab the web browser
[10:24] and i'll show you where it is so we just
[10:24] and i'll show you where it is so we just have
[10:24] have
[10:24] have this thing here it's a hive mq and my
[10:28] this thing here it's a hive mq and my
[10:28] this thing here it's a hive mq and my topic
[10:28] topic
[10:28] topic is this and the message is let's just
[10:32] is this and the message is let's just
[10:32] is this and the message is let's just test out one we're requesting
[10:36] test out one we're requesting
[10:36] test out one we're requesting a we're requesting a
[10:39] a we're requesting a
[10:39] a we're requesting a certain sound between one and nine which
[10:41] certain sound between one and nine which
[10:42] certain sound between one and nine which is in a library i'll show you next
[10:43] is in a library i'll show you next
[10:43] is in a library i'll show you next okay so let me just hold the buzzer next
[10:46] okay so let me just hold the buzzer next
[10:46] okay so let me just hold the buzzer next to the microphone here and i'm going to
[10:47] to the microphone here and i'm going to
[10:48] to the microphone here and i'm going to do
[10:48] do
[10:48] do two publish
[10:52] two publish
[10:52] two publish need to make sure that i'm subscribed
[10:54] need to make sure that i'm subscribed
[10:54] need to make sure that i'm subscribed here so
[10:56] here so
[10:56] here so used to be buzz code now we're on buzz
[10:57] used to be buzz code now we're on buzz
[10:58] used to be buzz code now we're on buzz we're going to subscribe to our own
[11:00] we're going to subscribe to our own
[11:00] we're going to subscribe to our own three and go
[11:04] three and go
[11:04] three and go and we can see that we received it and
[11:06] and we can see that we received it and
[11:06] and we can see that we received it and you can hear audibly
[11:07] you can hear audibly
[11:08] you can hear audibly that the little wemos device
[11:11] that the little wemos device
[11:11] that the little wemos device also received it this thing just does
[11:14] also received it this thing just does
[11:14] also received it this thing just does not want to show itself and
[11:17] not want to show itself and
[11:17] not want to show itself and it's terrible okay
[11:20] it's terrible okay
[11:20] it's terrible okay next let's check out the node-red code
[11:23] next let's check out the node-red code
[11:23] next let's check out the node-red code that's being installed on
[11:28] that's being installed on
[11:28] that's being installed on this is this is on the raspberry pi
[11:32] this is this is on the raspberry pi
[11:32] this is this is on the raspberry pi or beagle if you're using a beagle okay
[11:34] or beagle if you're using a beagle okay
[11:34] or beagle if you're using a beagle okay so you navigate to node red
[11:36] so you navigate to node red
[11:36] so you navigate to node red and then you can see everything up here
[11:39] and then you can see everything up here
[11:39] and then you can see everything up here is from my
[11:40] is from my
[11:40] is from my previous video so that's all explained
[11:43] previous video so that's all explained
[11:43] previous video so that's all explained another time
[11:44] another time
[11:44] another time all you had to add now is
[11:48] all you had to add now is
[11:48] all you had to add now is a watch node that's checking this file
[11:51] a watch node that's checking this file
[11:51] a watch node that's checking this file tmp slash
[11:52] tmp slash
[11:52] tmp slash buzz code with a camel case with a
[11:55] buzz code with a camel case with a
[11:55] buzz code with a camel case with a capital c for the second word okay
[11:58] capital c for the second word okay
[11:58] capital c for the second word okay and our text file has a camel case
[12:01] and our text file has a camel case
[12:01] and our text file has a camel case then uh read the flag so
[12:04] then uh read the flag so
[12:04] then uh read the flag so when this first part changes if there's
[12:07] when this first part changes if there's
[12:07] when this first part changes if there's a detected change in that text file then
[12:09] a detected change in that text file then
[12:09] a detected change in that text file then we're going
[12:09] we're going
[12:10] we're going to read the same the very same file
[12:13] to read the same the very same file
[12:13] to read the same the very same file okay and then we're going to send out
[12:17] okay and then we're going to send out
[12:17] okay and then we're going to send out a message on the hive mq broker
[12:20] a message on the hive mq broker
[12:20] a message on the hive mq broker which is already configured on this
[12:22] which is already configured on this
[12:22] which is already configured on this topic
[12:24] topic
[12:24] topic and the payload is going to be simply
[12:27] and the payload is going to be simply
[12:27] and the payload is going to be simply whatever's inside of this file the
[12:29] whatever's inside of this file the
[12:29] whatever's inside of this file the output is this string
[12:31] output is this string
[12:31] output is this string so next we show you where in the code
[12:35] so next we show you where in the code
[12:35] so next we show you where in the code are we producing this information that's
[12:39] are we producing this information that's
[12:39] are we producing this information that's on the in the text file okay so this is
[12:41] on the in the text file okay so this is
[12:41] on the in the text file okay so this is another
[12:42] another
[12:42] another recycled piece of code that um
[12:50] i will just highlight the important part
[12:50] i will just highlight the important part and the rest is
[12:51] and the rest is
[12:51] and the rest is in existing demonstration from previous
[12:54] in existing demonstration from previous
[12:54] in existing demonstration from previous video we
[12:55] video we
[12:55] video we i have two videos talking about csv
[12:57] i have two videos talking about csv
[12:58] i have two videos talking about csv files
[12:58] files
[12:58] files extracting values and and sending out
[13:00] extracting values and and sending out
[13:00] extracting values and and sending out mqtt
[13:02] mqtt
[13:02] mqtt so this is the main piece we can delete
[13:06] so this is the main piece we can delete
[13:06] so this is the main piece we can delete that
[13:07] that
[13:07] that stuff control
[13:10] stuff control
[13:10] stuff control plus let's get this bigger let's
[13:14] plus let's get this bigger let's
[13:14] plus let's get this bigger let's pop this tab out of the way okay so and
[13:17] pop this tab out of the way okay so and
[13:17] pop this tab out of the way okay so and you can see it's running because it's
[13:19] you can see it's running because it's
[13:19] you can see it's running because it's printing out the five dot targets
[13:21] printing out the five dot targets
[13:21] printing out the five dot targets okay so this block of code is of
[13:23] okay so this block of code is of
[13:23] okay so this block of code is of interest today we say
[13:25] interest today we say
[13:25] interest today we say if the axis one which is the forward
[13:28] if the axis one which is the forward
[13:28] if the axis one which is the forward joystick movement on the gamepad is not
[13:32] joystick movement on the gamepad is not
[13:32] joystick movement on the gamepad is not zero that means maybe it changed to one
[13:35] zero that means maybe it changed to one
[13:35] zero that means maybe it changed to one we say if our existing flag isn't
[13:38] we say if our existing flag isn't
[13:38] we say if our existing flag isn't already high that means this is
[13:40] already high that means this is
[13:40] already high that means this is being changed right now if it's um
[13:44] being changed right now if it's um
[13:44] being changed right now if it's um okay so then that statement's true we're
[13:47] okay so then that statement's true we're
[13:47] okay so then that statement's true we're going to raise the flag high
[13:49] going to raise the flag high
[13:49] going to raise the flag high and we're going to send out a message
[13:51] and we're going to send out a message
[13:51] and we're going to send out a message with a value
[13:52] with a value
[13:52] with a value 1 on this function called buzz message
[13:55] 1 on this function called buzz message
[13:55] 1 on this function called buzz message okay the lf is not necessary i'm i'm a
[13:58] okay the lf is not necessary i'm i'm a
[13:58] okay the lf is not necessary i'm i'm a novice at python so
[14:00] novice at python so
[14:00] novice at python so i tried some things that didn't work
[14:02] i tried some things that didn't work
[14:02] i tried some things that didn't work next um
[14:05] next um
[14:05] next um if the axis one is zero
[14:08] if the axis one is zero
[14:08] if the axis one is zero and we're checking if it has changed
[14:11] and we're checking if it has changed
[14:12] and we're checking if it has changed to zero we checked that it wasn't
[14:14] to zero we checked that it wasn't
[14:14] to zero we checked that it wasn't already zero
[14:15] already zero
[14:15] already zero we toggled the flag to zero and then we
[14:17] we toggled the flag to zero and then we
[14:17] we toggled the flag to zero and then we generate this
[14:18] generate this
[14:18] generate this stop request and the only difference
[14:20] stop request and the only difference
[14:20] stop request and the only difference between a start and stop request
[14:22] between a start and stop request
[14:22] between a start and stop request is what kind of music we're gonna play
[14:25] is what kind of music we're gonna play
[14:25] is what kind of music we're gonna play okay and then let me show you buzz
[14:27] okay and then let me show you buzz
[14:27] okay and then let me show you buzz message
[14:28] message
[14:28] message it's here we're importing
[14:32] it's here we're importing
[14:32] it's here we're importing our log level 2 file
[14:35] our log level 2 file
[14:35] our log level 2 file so l2 log which is part of the scuttle
[14:37] so l2 log which is part of the scuttle
[14:37] so l2 log which is part of the scuttle architecture
[14:39] architecture
[14:39] architecture and we're going to log a temporary file
[14:42] and we're going to log a temporary file
[14:42] and we're going to log a temporary file using
[14:43] using
[14:43] using the argument message code and
[14:46] the argument message code and
[14:46] the argument message code and into the file named buzzcode.txt
[14:49] into the file named buzzcode.txt
[14:49] into the file named buzzcode.txt with the camel case so this is the file
[14:51] with the camel case so this is the file
[14:51] with the camel case so this is the file node reddit's reading
[14:53] node reddit's reading
[14:53] node reddit's reading all right the only other piece that you
[14:56] all right the only other piece that you
[14:56] all right the only other piece that you need to know
[14:57] need to know
[14:57] need to know to to repeat my work is to have this
[15:00] to to repeat my work is to have this
[15:00] to to repeat my work is to have this a1 flag declared i declared it before
[15:03] a1 flag declared i declared it before
[15:03] a1 flag declared i declared it before the loop so that
[15:05] the loop so that
[15:05] the loop so that it's not getting declared and taking up
[15:08] it's not getting declared and taking up
[15:08] it's not getting declared and taking up processing
[15:09] processing
[15:09] processing to to re-declare it every time and it
[15:12] to to re-declare it every time and it
[15:12] to to re-declare it every time and it started out as false when you
[15:13] started out as false when you
[15:13] started out as false when you when you call it false then it's stored
[15:16] when you call it false then it's stored
[15:16] when you call it false then it's stored in python as
[15:17] in python as
[15:17] in python as a boolean kind of
[15:20] a boolean kind of
[15:20] a boolean kind of variable
[15:27] next up we have arduino so how did we
[15:27] next up we have arduino so how did we program the wemos device
[15:28] program the wemos device
[15:28] program the wemos device or esp device to
[15:32] or esp device to
[15:32] or esp device to do the handling of the oh my goodness no
[15:35] do the handling of the oh my goodness no
[15:35] do the handling of the oh my goodness no no simple receiver this was an example i
[15:38] no simple receiver this was an example i
[15:38] no simple receiver this was an example i started from
[15:40] started from
[15:40] started from don't have time to explain how i produce
[15:42] don't have time to explain how i produce
[15:42] don't have time to explain how i produce the code i'm just going to show you as
[15:43] the code i'm just going to show you as
[15:44] the code i'm just going to show you as an intro
[15:44] an intro
[15:44] an intro so mqtt buzz um the important part
[15:48] so mqtt buzz um the important part
[15:48] so mqtt buzz um the important part is that you can't see my wifi password
[15:51] is that you can't see my wifi password
[15:51] is that you can't see my wifi password um
[15:52] um
[15:52] um and here we are
[15:56] and here we are
[15:56] and here we are section for interval not so important
[15:58] section for interval not so important
[15:58] section for interval not so important okay this is the section this is the
[16:00] okay this is the section this is the
[16:00] okay this is the section this is the part of the loop that runs
[16:02] part of the loop that runs
[16:02] part of the loop that runs constantly and all it does is
[16:05] constantly and all it does is
[16:05] constantly and all it does is it's pulling the mqtt
[16:08] it's pulling the mqtt
[16:08] it's pulling the mqtt it's pulling any channels that we're
[16:10] it's pulling any channels that we're
[16:10] it's pulling any channels that we're subscribed to
[16:11] subscribed to
[16:11] subscribed to i i won't have time to explain this code
[16:14] i i won't have time to explain this code
[16:14] i i won't have time to explain this code in this but
[16:15] in this but
[16:15] in this but but then it it assigns
[16:19] but then it it assigns
[16:19] but then it it assigns the integer payload which is what was
[16:21] the integer payload which is what was
[16:21] the integer payload which is what was the payload in the mqtt message
[16:24] the payload in the mqtt message
[16:24] the payload in the mqtt message that i'm subscribed to which is i'm only
[16:26] that i'm subscribed to which is i'm only
[16:26] that i'm subscribed to which is i'm only subscribed to one channel
[16:28] subscribed to one channel
[16:28] subscribed to one channel it assigns that to something called my
[16:30] it assigns that to something called my
[16:30] it assigns that to something called my sound which was
[16:31] sound which was
[16:31] sound which was declared and as a an integer
[16:35] declared and as a an integer
[16:35] declared and as a an integer also and then it says
[16:38] also and then it says
[16:38] also and then it says if my sound has something in it which is
[16:41] if my sound has something in it which is
[16:41] if my sound has something in it which is non-zero
[16:42] non-zero
[16:42] non-zero then i'm gonna do this routine where i i
[16:45] then i'm gonna do this routine where i i
[16:45] then i'm gonna do this routine where i i print it out on the serial which you're
[16:46] print it out on the serial which you're
[16:46] print it out on the serial which you're not gonna get because
[16:48] not gonna get because
[16:48] not gonna get because we're only connected over wi-fi we're
[16:49] we're only connected over wi-fi we're
[16:49] we're only connected over wi-fi we're not doing any
[16:51] not doing any
[16:51] not doing any talking to the computer directly we
[16:53] talking to the computer directly we
[16:53] talking to the computer directly we perform a buzz
[16:54] perform a buzz
[16:54] perform a buzz chirp using that value and then we
[16:57] chirp using that value and then we
[16:57] chirp using that value and then we reassign the value to zero
[16:59] reassign the value to zero
[16:59] reassign the value to zero and if we go to buzz tab it's all based
[17:02] and if we go to buzz tab it's all based
[17:02] and if we go to buzz tab it's all based on the
[17:03] on the
[17:03] on the cute buzzersounds.h and
[17:06] cute buzzersounds.h and
[17:06] cute buzzersounds.h and um and and you could be doing a fart but
[17:09] um and and you could be doing a fart but
[17:09] um and and you could be doing a fart but instead
[17:09] instead
[17:09] instead we're doing uh what did i say
[17:13] we're doing uh what did i say
[17:13] we're doing uh what did i say on this case
[17:19] when we start driving we're gonna send a
[17:19] when we start driving we're gonna send a one
[17:20] one
[17:20] one when we finish driving we're send to six
[17:22] when we finish driving we're send to six
[17:22] when we finish driving we're send to six based on my research
[17:23] based on my research
[17:24] based on my research these are the most appropriate sounds
[17:25] these are the most appropriate sounds
[17:25] these are the most appropriate sounds for starting and stopping and driving
[17:27] for starting and stopping and driving
[17:27] for starting and stopping and driving so one is gonna be this and six is gonna
[17:31] so one is gonna be this and six is gonna
[17:31] so one is gonna be this and six is gonna be
[17:31] be
[17:31] be two three four five this happy
[17:34] two three four five this happy
[17:34] two three four five this happy it's happy when it finishes driving so
[17:37] it's happy when it finishes driving so
[17:38] it's happy when it finishes driving so um this is also a poorly made
[17:41] um this is also a poorly made
[17:41] um this is also a poorly made kind of c programming you can do this
[17:43] kind of c programming you can do this
[17:43] kind of c programming you can do this better with a case statement i
[17:45] better with a case statement i
[17:45] better with a case statement i understand that
[17:46] understand that
[17:46] understand that but this is all proof of concept so
[17:49] but this is all proof of concept so
[17:49] but this is all proof of concept so ascii is the form of lookup table where
[17:53] ascii is the form of lookup table where
[17:53] ascii is the form of lookup table where when i send an integer 1 it's read in as
[17:55] when i send an integer 1 it's read in as
[17:55] when i send an integer 1 it's read in as a character and then i have to re-assign
[17:57] a character and then i have to re-assign
[17:57] a character and then i have to re-assign that to be an integer
[17:59] that to be an integer
[17:59] that to be an integer okay it's becoming a 49. google ascii
[18:03] okay it's becoming a 49. google ascii
[18:03] okay it's becoming a 49. google ascii characters if you don't understand how
[18:05] characters if you don't understand how
[18:05] characters if you don't understand how that works okay
[18:07] that works okay
[18:07] that works okay and um so there it is we upload it we do
[18:10] and um so there it is we upload it we do
[18:10] and um so there it is we upload it we do tools um board and um
[18:14] tools um board and um
[18:14] tools um board and um probably several options will work but
[18:16] probably several options will work but
[18:16] probably several options will work but right now i'm dealing with the
[18:18] right now i'm dealing with the
[18:18] right now i'm dealing with the um lowland we know wemos d1r2 oh my
[18:22] um lowland we know wemos d1r2 oh my
[18:22] um lowland we know wemos d1r2 oh my goodness a mouthful
[18:23] goodness a mouthful
[18:24] goodness a mouthful okay and the only difference i found
[18:25] okay and the only difference i found
[18:26] okay and the only difference i found that that makes right now
[18:27] that that makes right now
[18:27] that that makes right now aside from generic sb is
[18:31] aside from generic sb is
[18:31] aside from generic sb is um we import it
[18:34] um we import it
[18:34] um we import it and what do we do the difference that it
[18:37] and what do we do the difference that it
[18:37] and what do we do the difference that it makes
[18:38] makes
[18:38] makes is the pin assignment
[18:43] is the pin assignment
[18:43] is the pin assignment buzz tab okay d4
[18:47] buzz tab okay d4
[18:47] buzz tab okay d4 has a meaning and d3 has a meaning when
[18:50] has a meaning and d3 has a meaning when
[18:50] has a meaning and d3 has a meaning when you're using that that board selection
[18:53] you're using that that board selection
[18:54] you're using that that board selection all it means is instead of just giving
[18:56] all it means is instead of just giving
[18:56] all it means is instead of just giving an integer that corresponds to the
[18:57] an integer that corresponds to the
[18:57] an integer that corresponds to the actual
[18:58] actual
[18:58] actual microcontroller's pin which is quite
[19:01] microcontroller's pin which is quite
[19:01] microcontroller's pin which is quite confusing
[19:02] confusing
[19:02] confusing i can show you right now
[19:08] right here if you look up the the data
[19:08] right here if you look up the the data sheet on this device
[19:11] sheet on this device
[19:11] sheet on this device which you don't want to have to do
[19:13] which you don't want to have to do
[19:13] which you don't want to have to do unless
[19:14] unless
[19:14] unless you need to then you're going to find
[19:16] you need to then you're going to find
[19:16] you need to then you're going to find out that the pin numberings do not
[19:18] out that the pin numberings do not
[19:18] out that the pin numberings do not match this silk screen anyway
[19:21] match this silk screen anyway
[19:21] match this silk screen anyway that's all trouble for me not trouble
[19:23] that's all trouble for me not trouble
[19:23] that's all trouble for me not trouble for you you just copy
[19:24] for you you just copy
[19:24] for you you just copy and then um let's try it out
[19:28] and then um let's try it out
[19:28] and then um let's try it out okay so i'm running the gamepad demo
[19:32] okay so i'm running the gamepad demo
[19:32] okay so i'm running the gamepad demo in this mode i drive forward and
[19:34] in this mode i drive forward and
[19:34] in this mode i drive forward and backwards
[19:36] backwards
[19:36] backwards okay and and i can turn this is just an
[19:39] okay and and i can turn this is just an
[19:39] okay and and i can turn this is just an exact copy of the previous demo
[19:41] exact copy of the previous demo
[19:41] exact copy of the previous demo um there's no there's no control
[19:44] um there's no there's no control
[19:44] um there's no there's no control on border here except for interpreting
[19:46] on border here except for interpreting
[19:46] on border here except for interpreting these two axes
[19:47] these two axes
[19:47] these two axes and then here we are activated
[19:51] and then here we are activated
[19:51] and then here we are activated the the wemos device and what it's going
[19:54] the the wemos device and what it's going
[19:54] the the wemos device and what it's going to do is when i
[19:55] to do is when i
[19:55] to do is when i start driving forward or actually when i
[19:58] start driving forward or actually when i
[19:58] start driving forward or actually when i start
[19:58] start
[19:58] start doing any x direction movement which is
[20:01] doing any x direction movement which is
[20:01] doing any x direction movement which is forward or backwards
[20:03] forward or backwards
[20:03] forward or backwards then this is going to detect a change on
[20:06] then this is going to detect a change on
[20:06] then this is going to detect a change on the raspberry pi
[20:07] the raspberry pi
[20:07] the raspberry pi in the python program and it's going to
[20:09] in the python program and it's going to
[20:09] in the python program and it's going to send the mqtt message
[20:11] send the mqtt message
[20:11] send the mqtt message and then when i stop driving it'll
[20:14] and then when i stop driving it'll
[20:14] and then when i stop driving it'll detect the flag has changed again
[20:16] detect the flag has changed again
[20:16] detect the flag has changed again and it'll send a different message so
[20:19] and it'll send a different message so
[20:19] and it'll send a different message so here we go
[20:21] here we go
[20:21] here we go [Music]
[20:23] [Music]
[20:23] [Music] it's hard to hear the first the startup
[20:25] it's hard to hear the first the startup
[20:25] it's hard to hear the first the startup one because uh
[20:27] one because uh
[20:27] one because uh the sound of the motors but here we go
[20:45] it's just lightning fast so
[20:46] it's just lightning fast so here you have a system that responds so
[20:48] here you have a system that responds so
[20:48] here you have a system that responds so fast
[20:49] fast
[20:49] fast that you could almost treat it as part
[20:52] that you could almost treat it as part
[20:52] that you could almost treat it as part of
[20:52] of
[20:52] of the robot and you can mount this on the
[20:55] the robot and you can mount this on the
[20:55] the robot and you can mount this on the robot and you could have controlling a
[20:56] robot and you could have controlling a
[20:56] robot and you could have controlling a speaker or lights or anything that that
[20:58] speaker or lights or anything that that
[20:58] speaker or lights or anything that that that you want to offload
[21:00] that you want to offload
[21:00] that you want to offload processing power especially for micro
[21:03] processing power especially for micro
[21:03] processing power especially for micro controller level speeds
[21:04] controller level speeds
[21:04] controller level speeds instead of micro processor
[21:08] instead of micro processor
[21:08] instead of micro processor micro computer level speeds right and
[21:12] micro computer level speeds right and
[21:12] micro computer level speeds right and and if you have a team with multiple
[21:14] and if you have a team with multiple
[21:14] and if you have a team with multiple people then you can have some team
[21:16] people then you can have some team
[21:16] people then you can have some team members
[21:17] members
[21:17] members working on part of your technology
[21:19] working on part of your technology
[21:19] working on part of your technology completely independent
[21:21] completely independent
[21:21] completely independent of the other part of your technology
[21:24] of the other part of your technology
[21:24] of the other part of your technology you can have your software written
[21:25] you can have your software written
[21:26] you can have your software written separately you can have testing done
[21:27] separately you can have testing done
[21:27] separately you can have testing done separately which is really important
[21:29] separately which is really important
[21:29] separately which is really important because
[21:29] because
[21:30] because this stuff is honestly getting pretty
[21:31] this stuff is honestly getting pretty
[21:31] this stuff is honestly getting pretty complicated
[21:33] complicated
[21:33] complicated but but now you have a way to expand
[21:35] but but now you have a way to expand
[21:35] but but now you have a way to expand look at how fast this is
[21:42] that data is going to singapore and back
[21:42] that data is going to singapore and back uh in my case uh but in your case
[21:46] uh in my case uh but in your case
[21:46] uh in my case uh but in your case it's probably going at least several
[21:48] it's probably going at least several
[21:48] it's probably going at least several hundred miles
[21:49] hundred miles
[21:49] hundred miles to the nearest cloud server for uh all
[21:52] to the nearest cloud server for uh all
[21:52] to the nearest cloud server for uh all the passages along mqtt
[21:54] the passages along mqtt
[21:54] the passages along mqtt and back instantaneously and well not
[21:58] and back instantaneously and well not
[21:58] and back instantaneously and well not instantaneously you
[21:59] instantaneously you
[21:59] instantaneously you you can see it
[22:05] there's no editing tricks here so
[22:05] there's no editing tricks here so so now um you have everything but 100
[22:08] so now um you have everything but 100
[22:08] so now um you have everything but 100 reliability right because
[22:11] reliability right because
[22:11] reliability right because independently this can lose connection
[22:13] independently this can lose connection
[22:13] independently this can lose connection to the wi-fi this can lose connection to
[22:15] to the wi-fi this can lose connection to
[22:15] to the wi-fi this can lose connection to the wi-fi
[22:15] the wi-fi
[22:15] the wi-fi but there are many tasks that that that
[22:19] but there are many tasks that that that
[22:19] but there are many tasks that that that loss of connection can be acceptable
[22:21] loss of connection can be acceptable
[22:21] loss of connection can be acceptable temporarily you can detect it
[22:23] temporarily you can detect it
[22:23] temporarily you can detect it you can have your robot program to
[22:26] you can have your robot program to
[22:26] you can have your robot program to complain about it
[22:27] complain about it
[22:27] complain about it and we're just opening so many doors
[22:30] and we're just opening so many doors
[22:30] and we're just opening so many doors here and in my next test i really want
[22:32] here and in my next test i really want
[22:32] here and in my next test i really want to find out how long can i make this
[22:33] to find out how long can i make this
[22:33] to find out how long can i make this battery last
[22:34] battery last
[22:34] battery last can i make it sleep and can i have
[22:36] can i make it sleep and can i have
[22:36] can i make it sleep and can i have scuttle distributing devices
[22:39] scuttle distributing devices
[22:39] scuttle distributing devices that are like sensors or other modules
[22:41] that are like sensors or other modules
[22:41] that are like sensors or other modules around a facility and then
[22:43] around a facility and then
[22:43] around a facility and then come back and collect them and have the
[22:47] come back and collect them and have the
[22:47] come back and collect them and have the devices telling scuttle when they need
[22:49] devices telling scuttle when they need
[22:49] devices telling scuttle when they need to be collected because their battery is
[22:51] to be collected because their battery is
[22:51] to be collected because their battery is low or
[22:52] low or
[22:52] low or when there's a condition where scuttle
[22:55] when there's a condition where scuttle
[22:55] when there's a condition where scuttle needs to come
[22:55] needs to come
[22:55] needs to come take an action so there you go hope you
[22:59] take an action so there you go hope you
[22:59] take an action so there you go hope you learned something
[23:06] here's a quick demo mqtt from the cell
[23:06] here's a quick demo mqtt from the cell phone
[23:07] phone
[23:07] phone to the esp device okay we're choosing
[23:10] to the esp device okay we're choosing
[23:10] to the esp device okay we're choosing message eight
[23:11] message eight
[23:11] message eight hit publish boom it received it let's
[23:14] hit publish boom it received it let's
[23:14] hit publish boom it received it let's change
[23:15] change
[23:15] change to a different sound um let's try
[23:18] to a different sound um let's try
[23:18] to a different sound um let's try number five okay publish
[23:23] number five okay publish
[23:23] number five okay publish seven publish

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
