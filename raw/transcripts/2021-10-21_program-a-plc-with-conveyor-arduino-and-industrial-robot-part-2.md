---
title: "Program a PLC with Conveyor, Arduino and Industrial Robot (PART 2)"
url: "https://www.youtube.com/watch?v=dOceaFaPiSM"
video_id: "dOceaFaPiSM"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2021-10-21
duration: "3:09"
duration_sec: 189
views: 420
likes: 5
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/dOceaFaPiSM/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 154
chapters_count: 0
has_description: true
has_comments: false
---

## Description

This is Part 2 from the previous video, linked below.  This video shows how the PLC controls the Relays, which are interlinked in the Conveyor Control Module circuitry.  So, the PLC relay module can activate the conveyor in forward, stop, and reverse.

Part 1► https://youtu.be/30GM4m-Lyec
Part 2 ► https://youtu.be/dOceaFaPiSM
Demonstration ► https://youtu.be/ZBGswS26Dy4

## Transcript

[0:03] now let's talk about how does the plc
[0:03] now let's talk about how does the plc control the direction and movement of
[0:06] control the direction and movement of
[0:06] control the direction and movement of the conveyor
[0:07] the conveyor
[0:07] the conveyor so we start with the plc's program
[0:10] so we start with the plc's program
[0:10] so we start with the plc's program that's uploaded
[0:11] that's uploaded
[0:11] that's uploaded and when it makes a decision to do so it
[0:14] and when it makes a decision to do so it
[0:14] and when it makes a decision to do so it will command the output module and slot
[0:17] will command the output module and slot
[0:17] will command the output module and slot slot 1 which is a 24 volt digital output
[0:21] slot 1 which is a 24 volt digital output
[0:21] slot 1 which is a 24 volt digital output module
[0:22] module
[0:22] module to
[0:23] to
[0:23] to activate a pin and send 24 volts out to
[0:26] activate a pin and send 24 volts out to
[0:26] activate a pin and send 24 volts out to a relay
[0:28] a relay
[0:28] a relay bracket so uh this bracket contains four
[0:31] bracket so uh this bracket contains four
[0:31] bracket so uh this bracket contains four relays and we're using
[0:33] relays and we're using
[0:33] relays and we're using a couple of them to control the conveyor
[0:35] a couple of them to control the conveyor
[0:35] a couple of them to control the conveyor the way it looks like is
[0:37] the way it looks like is
[0:37] the way it looks like is um
[0:38] um
[0:38] um on the on the full system they come the
[0:41] on the on the full system they come the
[0:41] on the on the full system they come the cables come out of here and they're
[0:42] cables come out of here and they're
[0:42] cables come out of here and they're controlling these two relays where a
[0:45] controlling these two relays where a
[0:45] controlling these two relays where a high 24 volt signal activates the relay
[0:48] high 24 volt signal activates the relay
[0:48] high 24 volt signal activates the relay and if it's normally open it will close
[0:51] and if it's normally open it will close
[0:51] and if it's normally open it will close the contacts that are normally closed
[0:52] the contacts that are normally closed
[0:52] the contacts that are normally closed will open
[0:59] inside the conveyor
[0:59] inside the conveyor the conveyor module that we've opened up
[1:01] the conveyor module that we've opened up
[1:01] the conveyor module that we've opened up and added to
[1:03] and added to
[1:03] and added to you have a circuit that looks like this
[1:06] you have a circuit that looks like this
[1:06] you have a circuit that looks like this this is the conveyor controller that
[1:08] this is the conveyor controller that
[1:08] this is the conveyor controller that came
[1:09] came
[1:09] came in the the gray box here by dorner
[1:12] in the the gray box here by dorner
[1:12] in the the gray box here by dorner and
[1:13] and
[1:13] and and has been modified and we have one
[1:15] and has been modified and we have one
[1:15] and has been modified and we have one cable coming out of it so the cable is
[1:18] cable coming out of it so the cable is
[1:18] cable coming out of it so the cable is doing uh what's going on in this image
[1:21] doing uh what's going on in this image
[1:21] doing uh what's going on in this image there's an on off switch that's manual
[1:24] there's an on off switch that's manual
[1:24] there's an on off switch that's manual for activating
[1:26] for activating
[1:26] for activating the conveyor it's
[1:28] the conveyor it's
[1:28] the conveyor it's if it's already set at some designated
[1:30] if it's already set at some designated
[1:30] if it's already set at some designated speed then uh closing the on switch will
[1:33] speed then uh closing the on switch will
[1:33] speed then uh closing the on switch will make it move that speed instead of zero
[1:36] make it move that speed instead of zero
[1:36] make it move that speed instead of zero and there's a light inside of the switch
[1:38] and there's a light inside of the switch
[1:38] and there's a light inside of the switch to indicate its status
[1:41] to indicate its status
[1:41] to indicate its status then secondly there's another switch
[1:43] then secondly there's another switch
[1:43] then secondly there's another switch that's going to control the forward or
[1:45] that's going to control the forward or
[1:45] that's going to control the forward or reverse function of that stepper motor
[1:49] reverse function of that stepper motor
[1:49] reverse function of that stepper motor the when we close this switch it tells
[1:51] the when we close this switch it tells
[1:51] the when we close this switch it tells the onboard controller which direction
[1:53] the onboard controller which direction
[1:53] the onboard controller which direction it's going to go when we when we have
[1:56] it's going to go when we when we have
[1:56] it's going to go when we when we have the the switch open it's going forward
[1:59] the the switch open it's going forward
[1:59] the the switch open it's going forward and uh forward you have to test by
[2:01] and uh forward you have to test by
[2:01] and uh forward you have to test by looking which direction that means
[2:03] looking which direction that means
[2:03] looking which direction that means because obviously there's not a distinct
[2:06] because obviously there's not a distinct
[2:06] because obviously there's not a distinct forward indicated
[2:08] forward indicated
[2:08] forward indicated then um out coming from this box we have
[2:11] then um out coming from this box we have
[2:11] then um out coming from this box we have a gray cable that gives us the access to
[2:13] a gray cable that gives us the access to
[2:14] a gray cable that gives us the access to these four terminals and we've put
[2:15] these four terminals and we've put
[2:15] these four terminals and we've put switches in series with the existing
[2:19] switches in series with the existing
[2:19] switches in series with the existing switches of the controller and these
[2:21] switches of the controller and these
[2:21] switches of the controller and these switches are being controlled by the plc
[2:24] switches are being controlled by the plc
[2:24] switches are being controlled by the plc by being
[2:26] by being
[2:26] by being attached to the relays
[2:28] attached to the relays
[2:28] attached to the relays so we normally we close both of these
[2:31] so we normally we close both of these
[2:31] so we normally we close both of these switch to switches to run the system to
[2:35] switch to switches to run the system to
[2:35] switch to switches to run the system to run the demo and then we take control by
[2:37] run the demo and then we take control by
[2:37] run the demo and then we take control by opening or closing the the contacts on
[2:39] opening or closing the the contacts on
[2:39] opening or closing the the contacts on the relays so relay zero has black and
[2:43] the relays so relay zero has black and
[2:43] the relays so relay zero has black and white wires relay one has red and green
[2:46] white wires relay one has red and green
[2:46] white wires relay one has red and green wires and they control these two
[2:48] wires and they control these two
[2:48] wires and they control these two switches
[2:49] switches
[2:49] switches so
[2:50] so
[2:50] so when you come over to
[2:53] when you come over to
[2:53] when you come over to the real life image the wires will be
[2:56] the real life image the wires will be
[2:56] the real life image the wires will be going into the bottom of here
[2:58] going into the bottom of here
[2:58] going into the bottom of here the black and white and red and green
[3:00] the black and white and red and green
[3:00] the black and white and red and green wires will be
[3:01] wires will be
[3:02] wires will be attached to
[3:03] attached to
[3:03] attached to these two terminals
[3:05] these two terminals
[3:05] these two terminals on the conveyor

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
