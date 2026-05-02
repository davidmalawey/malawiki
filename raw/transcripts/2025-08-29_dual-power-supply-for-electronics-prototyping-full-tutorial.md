---
title: "Dual Power supply for Electronics Prototyping [FULL TUTORIAL]"
url: "https://www.youtube.com/watch?v=Zrt5EQ3SnGU"
video_id: "Zrt5EQ3SnGU"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-08-29
duration: "16:49"
duration_sec: 1009
views: 3118
likes: 104
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/Zrt5EQ3SnGU/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 718
chapters_count: 11
has_description: true
has_comments: false
---

## Description

One solid example of gaining the benefits of our new, ubiquitous USB-PD technology and making more space at your benchtop, to build more electronics stuff!  Designed by a mechanical engineer who works at a university, where students need more space, simpler wiring, and more portable power for hundreds of projects every year. 

Hackers welcome: Learn to make your own benchtop power for most mechatronics prototype tests.  Get your two main voltages directly from a USB-C cable and any PD grade wall adapter.  We can simultenously draw 30 watts at 12v and 5 watts at 5v and then you have exactly what you need for the MICROCONTROLLER and the ACTUATOR.    Is it professional grade?  No.  It's better, because it's more accessible & less investment.

[CHAPTERS]
0:00 Intro for Administrators
0:36 PD Trigger Board
1:24 Find Vias for Solder
3:00 Merge 2 Boards
5:40 test power terminals
6:50 build output wires
8:21 cork board
9:40 hot glue with MODS
11:50 USE CASES
13:00 integrate 12v power
15:40 power analyzer

[LINKS]
I'm integrating components links, shopping links, etc in my open source laboratory documentation - Please check qr.net/openlabproject for details and please take time to comment if you need a link that I've not yet posted there!  Ultimately we want experts to help us design the best possible laboratory with the most favorable tools for all projects!

## Chapters

- 0:00 Intro for Administrators
- 0:36 PD Trigger Board
- 1:24 Find Vias for Solder
- 3:00 Merge 2 Boards
- 5:40 test power terminals
- 6:50 build output wires
- 8:21 cork board
- 9:40 hot glue with MODS
- 11:50 USE CASES
- 13:00 integrate 12v power
- 15:40 power analyzer

## Transcript

[0:04] Hi, I'm David Malloway and this is for
[0:04] Hi, I'm David Malloway and this is for folks that are at prototyping with
[0:05] folks that are at prototyping with
[0:05] folks that are at prototyping with electronics. Behind me there's a video
[0:08] electronics. Behind me there's a video
[0:08] electronics. Behind me there's a video that's showing a mechanical engineering
[0:09] that's showing a mechanical engineering
[0:10] that's showing a mechanical engineering team using sensors and to power the
[0:12] team using sensors and to power the
[0:12] team using sensors and to power the stuff up. They've had to migrate from
[0:14] stuff up. They've had to migrate from
[0:14] stuff up. They've had to migrate from the benchtop to the floor because they
[0:16] the benchtop to the floor because they
[0:16] the benchtop to the floor because they completely ran out of space to set down
[0:19] completely ran out of space to set down
[0:19] completely ran out of space to set down these benchtop power supplies and do the
[0:21] these benchtop power supplies and do the
[0:21] these benchtop power supplies and do the circuitry just to get things powered on.
[0:23] circuitry just to get things powered on.
[0:23] circuitry just to get things powered on. And we can make this a whole lot better.
[0:25] And we can make this a whole lot better.
[0:25] And we can make this a whole lot better. I'm about to show you a whole hands-on
[0:27] I'm about to show you a whole hands-on
[0:27] I'm about to show you a whole hands-on tutorial start to finish for a very
[0:29] tutorial start to finish for a very
[0:29] tutorial start to finish for a very simple circuit to make that easier.
[0:36] Okay, this might be a little bit messy,
[0:36] Okay, this might be a little bit messy, but we're going to use this to measure
[0:38] but we're going to use this to measure
[0:38] but we're going to use this to measure something about our PD trigger board.
[0:42] something about our PD trigger board.
[0:42] something about our PD trigger board. We're going to build a gadget that makes
[0:44] We're going to build a gadget that makes
[0:44] We're going to build a gadget that makes 12 volts and 5 volts together. Uh both
[0:46] 12 volts and 5 volts together. Uh both
[0:46] 12 volts and 5 volts together. Uh both of them available at the same time. So,
[0:49] of them available at the same time. So,
[0:49] of them available at the same time. So, the PD trigger will give us um 12 volts
[0:52] the PD trigger will give us um 12 volts
[0:52] the PD trigger will give us um 12 volts or even 15, 20, etc. It's going to
[0:55] or even 15, 20, etc. It's going to
[0:55] or even 15, 20, etc. It's going to output these on the screw terminal.
[0:57] output these on the screw terminal.
[0:57] output these on the screw terminal. We're going to figure out where we can
[0:59] We're going to figure out where we can
[0:59] We're going to figure out where we can tap into that full voltage without
[1:02] tap into that full voltage without
[1:02] tap into that full voltage without messing with our screw terminals. And
[1:04] messing with our screw terminals. And
[1:04] messing with our screw terminals. And then we're going to uh get access to
[1:07] then we're going to uh get access to
[1:07] then we're going to uh get access to that. And I'll show you how. So, all I
[1:09] that. And I'll show you how. So, all I
[1:09] that. And I'll show you how. So, all I want to do is um figure out where the
[1:11] want to do is um figure out where the
[1:11] want to do is um figure out where the 12vt trace is involved.
[1:19] We're going here. Well, I already I
[1:19] We're going here. Well, I already I already [clears throat] checked it
[1:20] already [clears throat] checked it
[1:20] already [clears throat] checked it previously. So
[1:30] all right. So this screw is always going
[1:30] all right. So this screw is always going to be common with the terminal itself.
[1:33] to be common with the terminal itself.
[1:33] to be common with the terminal itself. See that's ground. This is positive.
[1:35] See that's ground. This is positive.
[1:35] See that's ground. This is positive. Ground we have here and positive we have
[1:38] Ground we have here and positive we have
[1:38] Ground we have here and positive we have here. So we can use these VAS. They're
[1:41] here. So we can use these VAS. They're
[1:41] here. So we can use these VAS. They're silver lined holes where you can tap in.
[1:44] silver lined holes where you can tap in.
[1:44] silver lined holes where you can tap in. Uh you could put anything you want in
[1:46] Uh you could put anything you want in
[1:46] Uh you could put anything you want in there. And that metal is going to be
[1:48] there. And that metal is going to be
[1:48] there. And that metal is going to be continuous with the circuit voltage
[1:49] continuous with the circuit voltage
[1:49] continuous with the circuit voltage itself. See? Plus, minus.
[1:52] itself. See? Plus, minus.
[1:52] itself. See? Plus, minus. Um. All right. Okay. So, my solid core
[1:56] Um. All right. Okay. So, my solid core
[1:56] Um. All right. Okay. So, my solid core wire. I'm using solid core so I get the
[1:58] wire. I'm using solid core so I get the
[1:58] wire. I'm using solid core so I get the rigidity. And I'm going to uh solder it
[2:02] rigidity. And I'm going to uh solder it
[2:02] rigidity. And I'm going to uh solder it in to that via. And then we're going to
[2:05] in to that via. And then we're going to
[2:05] in to that via. And then we're going to come down here and do the ground. Okay.
[2:07] come down here and do the ground. Okay.
[2:07] come down here and do the ground. Okay. I'm just adjusting the position of this
[2:10] I'm just adjusting the position of this
[2:10] I'm just adjusting the position of this wire so that it's clean.
[2:13] wire so that it's clean.
[2:13] wire so that it's clean. Uh I had it already soldered and then I
[2:15] Uh I had it already soldered and then I
[2:15] Uh I had it already soldered and then I rememeeded it and hand just moved this.
[2:18] rememeeded it and hand just moved this.
[2:18] rememeeded it and hand just moved this. You want to do this quickly so that you
[2:21] You want to do this quickly so that you
[2:21] You want to do this quickly so that you don't um melt the insulation like I did.
[2:24] don't um melt the insulation like I did.
[2:24] don't um melt the insulation like I did. Just a little bit. Okay. Now, ground
[2:27] Just a little bit. Okay. Now, ground
[2:27] Just a little bit. Okay. Now, ground goes.
[2:30] goes.
[2:30] goes. Don't put too much solder. And we got to
[2:32] Don't put too much solder. And we got to
[2:32] Don't put too much solder. And we got to wait until the board itself heats up.
[2:36] wait until the board itself heats up.
[2:36] wait until the board itself heats up. That one resisted just a little bit more
[2:38] That one resisted just a little bit more
[2:38] That one resisted just a little bit more because the ground has a large plane and
[2:40] because the ground has a large plane and
[2:40] because the ground has a large plane and that uh dissipates heat across the
[2:43] that uh dissipates heat across the
[2:43] that uh dissipates heat across the copper around this board. And hopefully
[2:45] copper around this board. And hopefully
[2:45] copper around this board. And hopefully these didn't make contact with one
[2:47] these didn't make contact with one
[2:47] these didn't make contact with one another here.
[2:54] I'll fiddle with this off camera and
[2:54] I'll fiddle with this off camera and make sure that they're not going to make
[2:55] make sure that they're not going to make
[2:55] make sure that they're not going to make contact. Maybe add some hot glue.
[2:59] contact. Maybe add some hot glue.
[2:59] contact. Maybe add some hot glue. Okay, these two leads are getting
[3:00] Okay, these two leads are getting
[3:00] Okay, these two leads are getting snipped so we're not at risk of
[3:05] snipped so we're not at risk of
[3:05] snipped so we're not at risk of making contact with something short
[3:07] making contact with something short
[3:07] making contact with something short circuit. And I've got my two wires clean
[3:11] circuit. And I've got my two wires clean
[3:11] circuit. And I've got my two wires clean enough sticking out. Um,
[3:15] enough sticking out. Um,
[3:15] enough sticking out. Um, there's a lot of information on this
[3:16] there's a lot of information on this
[3:16] there's a lot of information on this board.
[3:19] board.
[3:19] board. Oh, you can lock it into one of the
[3:21] Oh, you can lock it into one of the
[3:21] Oh, you can lock it into one of the voltages just by adding a resistor on
[3:24] voltages just by adding a resistor on
[3:24] voltages just by adding a resistor on one of these. So much functionality.
[3:27] one of these. So much functionality.
[3:27] one of these. So much functionality. This is only I think it's about $8.
[3:30] This is only I think it's about $8.
[3:30] This is only I think it's about $8. 16 bucks for two. Okay, so I added a
[3:33] 16 bucks for two. Okay, so I added a
[3:33] 16 bucks for two. Okay, so I added a ruler for scale. You've got these two
[3:35] ruler for scale. You've got these two
[3:35] ruler for scale. You've got these two that are mechanically held kind of
[3:37] that are mechanically held kind of
[3:37] that are mechanically held kind of together by the solid core of these two
[3:40] together by the solid core of these two
[3:40] together by the solid core of these two copper wires. The insulation is there
[3:43] copper wires. The insulation is there
[3:43] copper wires. The insulation is there keeps them from contacting each other. I
[3:45] keeps them from contacting each other. I
[3:45] keeps them from contacting each other. I stripped it down to the length that I
[3:47] stripped it down to the length that I
[3:47] stripped it down to the length that I need. Starting with um this kit pack of
[3:51] need. Starting with um this kit pack of
[3:51] need. Starting with um this kit pack of wires. These are fairly useful. And when
[3:53] wires. These are fairly useful. And when
[3:53] wires. These are fairly useful. And when you're doing only a matter of small
[3:55] you're doing only a matter of small
[3:56] you're doing only a matter of small things, it's great to just snip some of
[3:58] things, it's great to just snip some of
[3:58] things, it's great to just snip some of these to the length that you need and
[3:59] these to the length that you need and
[4:00] these to the length that you need and you get that rigidity. You can bend them
[4:02] you get that rigidity. You can bend them
[4:02] you get that rigidity. You can bend them fairly easily with needlense or even
[4:05] fairly easily with needlense or even
[4:05] fairly easily with needlense or even those uh the tweezers that I always use
[4:08] those uh the tweezers that I always use
[4:08] those uh the tweezers that I always use for soldering. All right. Now, um, this
[4:13] for soldering. All right. Now, um, this
[4:13] for soldering. All right. Now, um, this what we have, uh, you're going to hear
[4:14] what we have, uh, you're going to hear
[4:14] what we have, uh, you're going to hear the beep if I've got continuity. So,
[4:17] the beep if I've got continuity. So,
[4:17] the beep if I've got continuity. So, this is the negative terminal, and this
[4:19] this is the negative terminal, and this
[4:19] this is the negative terminal, and this is my center pin. I I have two pins
[4:21] is my center pin. I I have two pins
[4:21] is my center pin. I I have two pins coming up, and the ground wraps around
[4:23] coming up, and the ground wraps around
[4:23] coming up, and the ground wraps around the bottom and just makes contact there.
[4:25] the bottom and just makes contact there.
[4:25] the bottom and just makes contact there. This is all quite fragile, so all we
[4:27] This is all quite fragile, so all we
[4:27] This is all quite fragile, so all we have to do is reinforce it. This is how
[4:29] have to do is reinforce it. This is how
[4:29] have to do is reinforce it. This is how we get around. All right, it's still
[4:31] we get around. All right, it's still
[4:31] we get around. All right, it's still prototyping level. You're still working
[4:33] prototyping level. You're still working
[4:33] prototyping level. You're still working with what would otherwise be just a
[4:35] with what would otherwise be just a
[4:35] with what would otherwise be just a bunch of jumper wires and breadboards,
[4:38] bunch of jumper wires and breadboards,
[4:38] bunch of jumper wires and breadboards, etc., But this is this is simpler as
[4:41] etc., But this is this is simpler as
[4:41] etc., But this is this is simpler as long as we can mechanically secure it.
[4:43] long as we can mechanically secure it.
[4:43] long as we can mechanically secure it. You can see we don't have the positive
[4:45] You can see we don't have the positive
[4:45] You can see we don't have the positive anywhere coming up. But we do have the
[4:47] anywhere coming up. But we do have the
[4:47] anywhere coming up. But we do have the positive down there where it enters the
[4:49] positive down there where it enters the
[4:49] positive down there where it enters the board. So if we set this to 12 volts, we
[4:52] board. So if we set this to 12 volts, we
[4:52] board. So if we set this to 12 volts, we should get 12 volts and ground coming
[4:54] should get 12 volts and ground coming
[4:54] should get 12 volts and ground coming into this 5V regulator board. The green
[4:57] into this 5V regulator board. The green
[4:58] into this 5V regulator board. The green board is about a $1 5volt regulator. It
[5:01] board is about a $1 5volt regulator. It
[5:01] board is about a $1 5volt regulator. It used to have a label HK something
[5:04] used to have a label HK something
[5:04] used to have a label HK something something. But the selection of this,
[5:06] something. But the selection of this,
[5:06] something. But the selection of this, these are reliable, cheap, plentiful
[5:09] these are reliable, cheap, plentiful
[5:09] these are reliable, cheap, plentiful types of gadgets that are um all over 10
[5:12] types of gadgets that are um all over 10
[5:12] types of gadgets that are um all over 10 of them for 10 bucks type of deal. Very
[5:15] of them for 10 bucks type of deal. Very
[5:15] of them for 10 bucks type of deal. Very uh very abundant now. You can choose any
[5:18] uh very abundant now. You can choose any
[5:18] uh very abundant now. You can choose any type. Um and then I added the two header
[5:21] type. Um and then I added the two header
[5:21] type. Um and then I added the two header pins. So we should be able to measure
[5:23] pins. So we should be able to measure
[5:23] pins. So we should be able to measure our 5 volts here from the five at the
[5:26] our 5 volts here from the five at the
[5:26] our 5 volts here from the five at the extremity and zero uh ground in the
[5:29] extremity and zero uh ground in the
[5:29] extremity and zero uh ground in the middle. So let's test that out. Okay,
[5:33] middle. So let's test that out. Okay,
[5:33] middle. So let's test that out. Okay, I've just plugged it in. Um,
[5:35] I've just plugged it in. Um,
[5:35] I've just plugged it in. Um, I don't know why it's blinking, but my
[5:37] I don't know why it's blinking, but my
[5:37] I don't know why it's blinking, but my PD is always available with uh one or
[5:41] PD is always available with uh one or
[5:41] PD is always available with uh one or two cables at the soldering station. If
[5:43] two cables at the soldering station. If
[5:43] two cables at the soldering station. If I press it here, 9 volts blinking.
[5:46] I press it here, 9 volts blinking.
[5:46] I press it here, 9 volts blinking. Blinking 12 volts. I don't really like
[5:49] Blinking 12 volts. I don't really like
[5:49] Blinking 12 volts. I don't really like that blinking because I think that's a
[5:50] that blinking because I think that's a
[5:50] that blinking because I think that's a warning. Let's reset it. 12 volts. Nice.
[5:56] warning. Let's reset it. 12 volts. Nice.
[5:56] warning. Let's reset it. 12 volts. Nice. Oh, it's only appearing to be blinking
[5:58] Oh, it's only appearing to be blinking
[5:58] Oh, it's only appearing to be blinking on the camera. In real life, it's solid
[6:01] on the camera. In real life, it's solid
[6:01] on the camera. In real life, it's solid blue. Um, so we can go up to 20 volts.
[6:06] blue. Um, so we can go up to 20 volts.
[6:06] blue. Um, so we can go up to 20 volts. Wonderful. Now, let's measure that. We
[6:09] Wonderful. Now, let's measure that. We
[6:09] Wonderful. Now, let's measure that. We have I use my multimeter
[6:13] have I use my multimeter
[6:13] have I use my multimeter first. I'm going to measure
[6:19] the 12
[6:19] the 12 positive minus and oops, we got to do
[6:24] positive minus and oops, we got to do
[6:24] positive minus and oops, we got to do the voltage function.
[6:31] DC volts
[6:31] DC volts 12.18 beautiful now
[6:34] 12.18 beautiful now
[6:34] 12.18 beautiful now uh
[6:37] uh
[6:37] uh 5 volts after the regulator 4.99
[6:41] 5 volts after the regulator 4.99
[6:41] 5 volts after the regulator 4.99 beautiful as well and it's negative
[6:43] beautiful as well and it's negative
[6:43] beautiful as well and it's negative because I oops I reversed my probes here
[6:46] because I oops I reversed my probes here
[6:46] because I oops I reversed my probes here so
[6:54] when I make the cable for my
[6:54] when I make the cable for my receiving end device for the 5V
[6:56] receiving end device for the 5V
[6:56] receiving end device for the 5V situation
[7:06] Okay, now I pulled out from my Deont
[7:06] Okay, now I pulled out from my Deont supplies. Ground goes into the
[7:11] supplies. Ground goes into the
[7:11] supplies. Ground goes into the ground goes into the terminal with the
[7:18] arrow.
[7:18] arrow. Okay. And then try your best not to peel
[7:22] Okay. And then try your best not to peel
[7:22] Okay. And then try your best not to peel those apart.
[7:24] those apart.
[7:24] those apart. And the other side gets to have the
[7:27] And the other side gets to have the
[7:27] And the other side gets to have the three pin. That's because I need an
[7:29] three pin. That's because I need an
[7:29] three pin. That's because I need an extra position available in my
[7:33] extra position available in my
[7:33] extra position available in my um yeah, I'm going to reverse these.
[7:37] um yeah, I'm going to reverse these.
[7:37] um yeah, I'm going to reverse these. They're going to be twisted. What I mean
[7:39] They're going to be twisted. What I mean
[7:39] They're going to be twisted. What I mean by that is if you drew a diagram now,
[7:43] by that is if you drew a diagram now,
[7:43] by that is if you drew a diagram now, you can see there's a twist in this
[7:45] you can see there's a twist in this
[7:45] you can see there's a twist in this wire. It's going to switch over.
[7:47] wire. It's going to switch over.
[7:47] wire. It's going to switch over. Just
[7:49] Just
[7:49] Just that's useful to think about if you're
[7:51] that's useful to think about if you're
[7:51] that's useful to think about if you're going to document your stuff.
[7:53] going to document your stuff.
[7:53] going to document your stuff. Okay, I removed one end and I added heat
[7:55] Okay, I removed one end and I added heat
[7:55] Okay, I removed one end and I added heat shrink. Be careful not to uh melt your
[7:58] shrink. Be careful not to uh melt your
[7:58] shrink. Be careful not to uh melt your housing like I nearly did there. Um, but
[8:01] housing like I nearly did there. Um, but
[8:01] housing like I nearly did there. Um, but that's going to help give this some more
[8:03] that's going to help give this some more
[8:03] that's going to help give this some more rigidity. You can't pull one without
[8:06] rigidity. You can't pull one without
[8:06] rigidity. You can't pull one without pulling the other. This is just a
[8:08] pulling the other. This is just a
[8:08] pulling the other. This is just a mechanically a good practice if you're
[8:09] mechanically a good practice if you're
[8:09] mechanically a good practice if you're going to fiddle with this wire a lot.
[8:11] going to fiddle with this wire a lot.
[8:11] going to fiddle with this wire a lot. Okay. Now, you're looking at a piece of
[8:13] Okay. Now, you're looking at a piece of
[8:13] Okay. Now, you're looking at a piece of uni strut
[8:15] uni strut
[8:15] uni strut and a piece of cork material. Uh, we're
[8:18] and a piece of cork material. Uh, we're
[8:18] and a piece of cork material. Uh, we're going to measure that. We're
[8:23] going to measure that. We're
[8:23] going to measure that. We're okay. We need 40 mm [snorts] for the
[8:26] okay. We need 40 mm [snorts] for the
[8:26] okay. We need 40 mm [snorts] for the square. That's going to have this here.
[8:30] square. That's going to have this here.
[8:30] square. That's going to have this here. And
[8:32] And
[8:32] And a simple utility knife will do the job.
[8:35] a simple utility knife will do the job.
[8:35] a simple utility knife will do the job. You want to have this very, very sharp.
[8:37] You want to have this very, very sharp.
[8:37] You want to have this very, very sharp. And then you're going to get that nice
[8:39] And then you're going to get that nice
[8:39] And then you're going to get that nice clean edge. Okay. This is an adhesive on
[8:42] clean edge. Okay. This is an adhesive on
[8:42] clean edge. Okay. This is an adhesive on one side that I'll peel off and I'll
[8:44] one side that I'll peel off and I'll
[8:44] one side that I'll peel off and I'll stick that down. And we're going to
[8:45] stick that down. And we're going to
[8:46] stick that down. And we're going to protect since this is steel and we're
[8:48] protect since this is steel and we're
[8:48] protect since this is steel and we're going to stick our circuit to this. It's
[8:50] going to stick our circuit to this. It's
[8:50] going to stick our circuit to this. It's going to protect it from uh short
[8:52] going to protect it from uh short
[8:52] going to protect it from uh short circuiting
[8:54] circuiting
[8:54] circuiting under any vibrations etc.
[8:58] under any vibrations etc.
[8:58] under any vibrations etc. See how if if you're not careful you get
[9:00] See how if if you're not careful you get
[9:00] See how if if you're not careful you get that crummy stuff. And that is um
[9:05] that crummy stuff. And that is um
[9:05] that crummy stuff. And that is um okay natural insulator 8 inch thick
[9:08] okay natural insulator 8 inch thick
[9:08] okay natural insulator 8 inch thick adhesive backed cork material. I use
[9:10] adhesive backed cork material. I use
[9:10] adhesive backed cork material. I use this for loads of stuff. If you do
[9:12] this for loads of stuff. If you do
[9:12] this for loads of stuff. If you do mechanical things and creating stuff,
[9:14] mechanical things and creating stuff,
[9:14] mechanical things and creating stuff, it's just super handy. You'll see more
[9:17] it's just super handy. You'll see more
[9:17] it's just super handy. You'll see more in the coming videos. Just peeled off
[9:19] in the coming videos. Just peeled off
[9:19] in the coming videos. Just peeled off the backing. Now you can see the
[9:21] the backing. Now you can see the
[9:21] the backing. Now you can see the adhesive tape stuff and I'll line it up
[9:25] adhesive tape stuff and I'll line it up
[9:25] adhesive tape stuff and I'll line it up and stick it, apply some pressure, and
[9:28] and stick it, apply some pressure, and
[9:28] and stick it, apply some pressure, and then we're ready to put our circuit on
[9:30] then we're ready to put our circuit on
[9:30] then we're ready to put our circuit on there. And now we have this thing
[9:31] there. And now we have this thing
[9:31] there. And now we have this thing portable and uh with weight, so it's has
[9:35] portable and uh with weight, so it's has
[9:36] portable and uh with weight, so it's has the mass not to flip around and create a
[9:38] the mass not to flip around and create a
[9:38] the mass not to flip around and create a dangerous situation. Okay, hot glue
[9:41] dangerous situation. Okay, hot glue
[9:41] dangerous situation. Okay, hot glue gun's warming up. And since I'm
[9:43] gun's warming up. And since I'm
[9:43] gun's warming up. And since I'm multitasking, sometimes I like to bust
[9:45] multitasking, sometimes I like to bust
[9:45] multitasking, sometimes I like to bust out the hourglass. If this 2 minutes, if
[9:48] out the hourglass. If this 2 minutes, if
[9:48] out the hourglass. If this 2 minutes, if I have anything, uh, if this is all gone
[9:51] I have anything, uh, if this is all gone
[9:51] I have anything, uh, if this is all gone and I walk past this, it's kind of a
[9:53] and I walk past this, it's kind of a
[9:53] and I walk past this, it's kind of a reminder like, hey, you probably left
[9:55] reminder like, hey, you probably left
[9:55] reminder like, hey, you probably left this on cuz when I store when I unplug
[9:57] this on cuz when I store when I unplug
[9:57] this on cuz when I store when I unplug this, this goes away or at least gets
[9:59] this, this goes away or at least gets
[10:00] this, this goes away or at least gets tipped back over. Only two minutes to
[10:02] tipped back over. Only two minutes to
[10:02] tipped back over. Only two minutes to warm this up because my uh, hot glue gun
[10:05] warm this up because my uh, hot glue gun
[10:05] warm this up because my uh, hot glue gun has some mods inside. Um, it's got it's
[10:10] has some mods inside. Um, it's got it's
[10:10] has some mods inside. Um, it's got it's got extra fiberglass insulation wrapped
[10:12] got extra fiberglass insulation wrapped
[10:12] got extra fiberglass insulation wrapped around the heating thing in there. So,
[10:14] around the heating thing in there. So,
[10:14] around the heating thing in there. So, when you touch this, where I'm touching
[10:16] when you touch this, where I'm touching
[10:16] when you touch this, where I'm touching right now, it's uh Don't mind my nails.
[10:19] right now, it's uh Don't mind my nails.
[10:19] right now, it's uh Don't mind my nails. I was just changing the brakes on my
[10:21] I was just changing the brakes on my
[10:21] I was just changing the brakes on my car. Um, this is not nearly as warm as
[10:24] car. Um, this is not nearly as warm as
[10:24] car. Um, this is not nearly as warm as it used to be, that means more heat
[10:26] it used to be, that means more heat
[10:26] it used to be, that means more heat enters into the the heating channel
[10:29] enters into the the heating channel
[10:30] enters into the the heating channel where we want it and less heat exits out
[10:32] where we want it and less heat exits out
[10:32] where we want it and less heat exits out of the enclosure. So, [snorts] we've
[10:34] of the enclosure. So, [snorts] we've
[10:34] of the enclosure. So, [snorts] we've raised the efficiency of this at least
[10:36] raised the efficiency of this at least
[10:36] raised the efficiency of this at least 25%. It's pretty awesome. And it heats
[10:38] 25%. It's pretty awesome. And it heats
[10:38] 25%. It's pretty awesome. And it heats up twice as fast, 5 minutes or so, down
[10:41] up twice as fast, 5 minutes or so, down
[10:41] up twice as fast, 5 minutes or so, down to 2 minutes. [snorts]
[10:44] to 2 minutes. [snorts]
[10:44] to 2 minutes. [snorts] And if you're really multitasking, then
[10:47] And if you're really multitasking, then
[10:47] And if you're really multitasking, then it's good to just grab a piece of
[10:48] it's good to just grab a piece of
[10:48] it's good to just grab a piece of silicone and leave that in the same
[10:51] silicone and leave that in the same
[10:51] silicone and leave that in the same place as your glue gun. When it drips,
[10:52] place as your glue gun. When it drips,
[10:52] place as your glue gun. When it drips, no matter what surface, this will just
[10:54] no matter what surface, this will just
[10:54] no matter what surface, this will just peel easily easily right off of the
[10:57] peel easily easily right off of the
[10:57] peel easily easily right off of the silicone. Um, and then also you can
[11:00] silicone. Um, and then also you can
[11:00] silicone. Um, and then also you can carry this off to the drawer where
[11:01] carry this off to the drawer where
[11:01] carry this off to the drawer where you're storing your hot glue because uh
[11:04] you're storing your hot glue because uh
[11:04] you're storing your hot glue because uh then you can put it away hot and if it
[11:06] then you can put it away hot and if it
[11:06] then you can put it away hot and if it drips, no problem at all. Okay, the glue
[11:09] drips, no problem at all. Okay, the glue
[11:09] drips, no problem at all. Okay, the glue is flowing. So, we're going to apply
[11:11] is flowing. So, we're going to apply
[11:11] is flowing. So, we're going to apply some on the bottom of each of these.
[11:14] some on the bottom of each of these.
[11:14] some on the bottom of each of these. Making note to add a little bit of
[11:16] Making note to add a little bit of
[11:16] Making note to add a little bit of height to our assembly. That way, the
[11:19] height to our assembly. That way, the
[11:19] height to our assembly. That way, the pins don't teeter totter the boards out
[11:22] pins don't teeter totter the boards out
[11:22] pins don't teeter totter the boards out of the um flat plain sort of
[11:28] of the um flat plain sort of
[11:28] of the um flat plain sort of This is just an OCDC thing type of thing
[11:31] This is just an OCDC thing type of thing
[11:31] This is just an OCDC thing type of thing for me, but I don't want to see the
[11:34] for me, but I don't want to see the
[11:34] for me, but I don't want to see the region of the board that has the pins on
[11:36] region of the board that has the pins on
[11:36] region of the board that has the pins on it.
[11:37] it.
[11:38] it. Um, just tipping up. It looks like there
[11:41] Um, just tipping up. It looks like there
[11:41] Um, just tipping up. It looks like there was no fourth Um, okay. So, now we
[11:44] was no fourth Um, okay. So, now we
[11:44] was no fourth Um, okay. So, now we have a weighted modular
[11:47] have a weighted modular
[11:47] have a weighted modular uh dual voltage
[11:50] uh dual voltage
[11:50] uh dual voltage supply.
[11:52] supply.
[11:52] supply. Okay. This circuit is useful for
[11:53] Okay. This circuit is useful for
[11:53] Okay. This circuit is useful for millions of possible projects. And uh
[11:57] millions of possible projects. And uh
[11:57] millions of possible projects. And uh like one example that I'm going to
[11:59] like one example that I'm going to
[11:59] like one example that I'm going to implement this in is uh some of you may
[12:02] implement this in is uh some of you may
[12:02] implement this in is uh some of you may recognize
[12:04] recognize
[12:04] recognize stepper motor stepper motor driver
[12:06] stepper motor stepper motor driver
[12:06] stepper motor stepper motor driver breakout board. That's a fairly new
[12:08] breakout board. That's a fairly new
[12:08] breakout board. That's a fairly new thing on the market. And we have this.
[12:10] thing on the market. And we have this.
[12:10] thing on the market. And we have this. It's magnetic so we can quickly clamp it
[12:13] It's magnetic so we can quickly clamp it
[12:13] It's magnetic so we can quickly clamp it on and get to work. Our 5 volts is
[12:16] on and get to work. Our 5 volts is
[12:16] on and get to work. Our 5 volts is available on these two pins which is the
[12:19] available on these two pins which is the
[12:19] available on these two pins which is the two side by side Dupant style pins is
[12:22] two side by side Dupant style pins is
[12:22] two side by side Dupant style pins is what powers up loads and loads of
[12:24] what powers up loads and loads of
[12:24] what powers up loads and loads of microcontrollers as well as just
[12:27] microcontrollers as well as just
[12:27] microcontrollers as well as just accessory boards. So this is a
[12:29] accessory boards. So this is a
[12:29] accessory boards. So this is a communicating type of board. It's using
[12:31] communicating type of board. It's using
[12:31] communicating type of board. It's using 5 volts for its logic stuff and for its
[12:34] 5 volts for its logic stuff and for its
[12:34] 5 volts for its logic stuff and for its pulse uh pulse inputs.
[12:37] pulse uh pulse inputs.
[12:37] pulse uh pulse inputs. We can go ground
[12:41] We can go ground
[12:41] We can go ground down here at the base and red. The red
[12:44] down here at the base and red. The red
[12:44] down here at the base and red. The red row is 5 volts. All right. This um light
[12:50] row is 5 volts. All right. This um light
[12:50] row is 5 volts. All right. This um light comes on indicating that it's ready to
[12:52] comes on indicating that it's ready to
[12:52] comes on indicating that it's ready to communicate, but we don't have voltage
[12:54] communicate, but we don't have voltage
[12:54] communicate, but we don't have voltage going to the motor itself. That's a
[12:57] going to the motor itself. That's a
[12:58] going to the motor itself. That's a separate thingy. Now, since we're doing
[13:00] separate thingy. Now, since we're doing
[13:00] separate thingy. Now, since we're doing prototyping, I keep a bag with the last
[13:05] prototyping, I keep a bag with the last
[13:05] prototyping, I keep a bag with the last projects sets of wires, and it's always
[13:08] projects sets of wires, and it's always
[13:08] projects sets of wires, and it's always 18 gauge being used for powered
[13:11] 18 gauge being used for powered
[13:11] 18 gauge being used for powered mechatronic stuff. And it's always
[13:14] mechatronic stuff. And it's always
[13:14] mechatronic stuff. And it's always simple ferals on the ends because the
[13:16] simple ferals on the ends because the
[13:16] simple ferals on the ends because the most common connector out of all powered
[13:20] most common connector out of all powered
[13:20] most common connector out of all powered electronics for prototyping are going to
[13:23] electronics for prototyping are going to
[13:23] electronics for prototyping are going to be these screw terminals we use. Oh,
[13:26] be these screw terminals we use. Oh,
[13:26] be these screw terminals we use. Oh, check it out. I just invented something
[13:28] check it out. I just invented something
[13:28] check it out. I just invented something new. I added, you can see there's a
[13:30] new. I added, you can see there's a
[13:30] new. I added, you can see there's a third wire in there. That's the solid
[13:32] third wire in there. That's the solid
[13:32] third wire in there. That's the solid copper that was remaining on the
[13:34] copper that was remaining on the
[13:34] copper that was remaining on the benchtop. And I believe now that I've
[13:36] benchtop. And I believe now that I've
[13:36] benchtop. And I believe now that I've heat shrunk it, uh, it's still a little
[13:38] heat shrunk it, uh, it's still a little
[13:38] heat shrunk it, uh, it's still a little bit hot. We can take this arrangement
[13:41] bit hot. We can take this arrangement
[13:41] bit hot. We can take this arrangement and we can bend it 90 degrees uh like
[13:46] and we can bend it 90 degrees uh like
[13:46] and we can bend it 90 degrees uh like so.
[13:48] so.
[13:48] so. And now you have something that conforms
[13:51] And now you have something that conforms
[13:51] And now you have something that conforms a little better just in case you wanted
[13:53] a little better just in case you wanted
[13:53] a little better just in case you wanted something like that. Okay. So, this demo
[13:56] something like that. Okay. So, this demo
[13:56] something like that. Okay. So, this demo isn't going to be ready yet because we
[13:57] isn't going to be ready yet because we
[13:57] isn't going to be ready yet because we still need a pulse up and down input to
[14:00] still need a pulse up and down input to
[14:00] still need a pulse up and down input to the motor driver to make this thing
[14:02] the motor driver to make this thing
[14:02] the motor driver to make this thing work. It's just an example for purpose
[14:05] work. It's just an example for purpose
[14:05] work. It's just an example for purpose use case for your dual voltage power
[14:08] use case for your dual voltage power
[14:08] use case for your dual voltage power supply. Um, let's plug that in. Now we
[14:11] supply. Um, let's plug that in. Now we
[14:11] supply. Um, let's plug that in. Now we have 12. We got a light here.
[14:16] have 12. We got a light here.
[14:16] have 12. We got a light here. Okay. I'm supposed to check that I
[14:17] Okay. I'm supposed to check that I
[14:18] Okay. I'm supposed to check that I cannot turn this because if we have
[14:20] cannot turn this because if we have
[14:20] cannot turn this because if we have power going to the coils, soon as that's
[14:22] power going to the coils, soon as that's
[14:22] power going to the coils, soon as that's lit up, I want to be able to get a uh
[14:25] lit up, I want to be able to get a uh
[14:25] lit up, I want to be able to get a uh it'll be a static one position signal of
[14:29] it'll be a static one position signal of
[14:29] it'll be a static one position signal of the current that runs to the coils in
[14:31] the current that runs to the coils in
[14:31] the current that runs to the coils in here and it's going to be held stat
[14:33] here and it's going to be held stat
[14:33] here and it's going to be held stat steady. But there's um the enable pin.
[14:38] steady. But there's um the enable pin.
[14:38] steady. But there's um the enable pin. Oh boy. As I was saying, there is a pin
[14:41] Oh boy. As I was saying, there is a pin
[14:41] Oh boy. As I was saying, there is a pin here on the yellow contact. That's the
[14:46] here on the yellow contact. That's the
[14:46] here on the yellow contact. That's the enable pin for the motor. It must be
[14:48] enable pin for the motor. It must be
[14:48] enable pin for the motor. It must be pulled down to ground to activate the
[14:51] pulled down to ground to activate the
[14:51] pulled down to ground to activate the current to come in here and run to the
[14:53] current to come in here and run to the
[14:53] current to come in here and run to the motor. In any case, now we've got it
[14:55] motor. In any case, now we've got it
[14:55] motor. In any case, now we've got it fixed in place. And it does not want to
[14:58] fixed in place. And it does not want to
[14:58] fixed in place. And it does not want to move.
[15:00] move.
[15:00] move. This circuit here is useful for a
[15:02] This circuit here is useful for a
[15:02] This circuit here is useful for a million things. As I said for the
[15:05] million things. As I said for the
[15:06] million things. As I said for the Arduino or for an ESP32, ESP 8266
[15:10] Arduino or for an ESP32, ESP 8266
[15:10] Arduino or for an ESP32, ESP 8266 or Raspberry Pi, all of them have two
[15:13] or Raspberry Pi, all of them have two
[15:13] or Raspberry Pi, all of them have two pins available side by side to receive
[15:15] pins available side by side to receive
[15:15] pins available side by side to receive that 5 volts and ground. It's sufficient
[15:17] that 5 volts and ground. It's sufficient
[15:17] that 5 volts and ground. It's sufficient to deliver the current and evacuate the
[15:21] to deliver the current and evacuate the
[15:21] to deliver the current and evacuate the USB ports from here so that you can have
[15:23] USB ports from here so that you can have
[15:23] USB ports from here so that you can have a portable situation. Um, and also we
[15:26] a portable situation. Um, and also we
[15:26] a portable situation. Um, and also we can cycle through the different voltages
[15:30] can cycle through the different voltages
[15:30] can cycle through the different voltages by pressing this button. We can go up to
[15:33] by pressing this button. We can go up to
[15:33] by pressing this button. We can go up to say 15 volts. It's blinking now because
[15:35] say 15 volts. It's blinking now because
[15:35] say 15 volts. It's blinking now because it's saying I am being asked for more
[15:39] it's saying I am being asked for more
[15:39] it's saying I am being asked for more current than I can produce because these
[15:41] current than I can produce because these
[15:41] current than I can produce because these stepper motors are pretty current
[15:43] stepper motors are pretty current
[15:43] stepper motors are pretty current hungry. I've come back to the 9volt
[15:46] hungry. I've come back to the 9volt
[15:46] hungry. I've come back to the 9volt position and then we can also suddenly
[15:50] position and then we can also suddenly
[15:50] position and then we can also suddenly grab just a $10 device like this tester
[15:54] grab just a $10 device like this tester
[15:54] grab just a $10 device like this tester and we can gain information about the
[15:57] and we can gain information about the
[15:57] and we can gain information about the circuit that we're working with. So any
[15:59] circuit that we're working with. So any
[15:59] circuit that we're working with. So any actuator plus any microcontroller. Now
[16:02] actuator plus any microcontroller. Now
[16:02] actuator plus any microcontroller. Now you can power the system and you can
[16:04] you can power the system and you can
[16:04] you can power the system and you can measure up
[16:06] measure up
[16:06] measure up um how much power are we drawing just
[16:09] um how much power are we drawing just
[16:09] um how much power are we drawing just because now we're powering from USBC. We
[16:13] because now we're powering from USBC. We
[16:13] because now we're powering from USBC. We can see we're working with 8.96 volts
[16:15] can see we're working with 8.96 volts
[16:15] can see we're working with 8.96 volts and we're pulling uh uh call it.1 amps
[16:20] and we're pulling uh uh call it.1 amps
[16:20] and we're pulling uh uh call it.1 amps and that's really cool. Now I wonder if
[16:23] and that's really cool. Now I wonder if
[16:23] and that's really cool. Now I wonder if I play with this shaft.
[16:26] I play with this shaft.
[16:26] I play with this shaft. Oh yeah, it climbs up when I start
[16:29] Oh yeah, it climbs up when I start
[16:29] Oh yeah, it climbs up when I start putting uh force against that shaft. But
[16:33] putting uh force against that shaft. But
[16:33] putting uh force against that shaft. But in any case, I think that's a sufficient
[16:35] in any case, I think that's a sufficient
[16:35] in any case, I think that's a sufficient demo to say here's a useful circuit. And
[16:38] demo to say here's a useful circuit. And
[16:38] demo to say here's a useful circuit. And um anyone in the audience that can show
[16:40] um anyone in the audience that can show
[16:40] um anyone in the audience that can show us how to build something cleaner and
[16:42] us how to build something cleaner and
[16:42] us how to build something cleaner and simpler with this much versatility, I
[16:44] simpler with this much versatility, I
[16:44] simpler with this much versatility, I would love to see it because we want to
[16:46] would love to see it because we want to
[16:46] would love to see it because we want to always improve. Thanks everyone.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
