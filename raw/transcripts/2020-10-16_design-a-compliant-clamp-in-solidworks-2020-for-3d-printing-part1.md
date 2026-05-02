---
title: "Design a compliant clamp in Solidworks 2020 for 3D Printing (part1)"
url: "https://www.youtube.com/watch?v=VyrneksJNfw"
video_id: "VyrneksJNfw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-10-16
duration: "19:57"
duration_sec: 1197
views: 752
likes: 8
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/VyrneksJNfw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 988
chapters_count: 4
has_description: true
has_comments: false
---

## Description

20 minute walkthrough of design of a clamp in solidworks.  In this video I think out loud through the design process, and describe all the features that must be engineered to have a successful prototype. 

This design will be used for the SCUTTLE Robot: https://scuttlerobot.org

My comments address these design elements:
~ ideation and purpose of the part
~ addressing 3d printability
~ modifying features in the feature tree
~ planning the test of first prototype
~ consideration of tolerance of a printer
~ consideration of mechanical stresses
~ conservation of material & money

## Chapters

- 0:00 Intro
- 1:14 Design
- 4:00 Sketch
- 10:25 Assembly

## Transcript

[0:03] hi everybody um today i'm working
[0:03] hi everybody um today i'm working on a new design it's going to be version
[0:06] on a new design it's going to be version
[0:06] on a new design it's going to be version one of a conveyor that goes on the
[0:08] one of a conveyor that goes on the
[0:08] one of a conveyor that goes on the scuttle robot
[0:09] scuttle robot
[0:09] scuttle robot uh powered by a very common nema 23
[0:12] uh powered by a very common nema 23
[0:12] uh powered by a very common nema 23 stepper motor
[0:13] stepper motor
[0:13] stepper motor we haven't used a stepper motor on
[0:15] we haven't used a stepper motor on
[0:15] we haven't used a stepper motor on scuttle
[0:17] scuttle
[0:17] scuttle maybe once or twice with a small group
[0:19] maybe once or twice with a small group
[0:19] maybe once or twice with a small group with a small project but
[0:21] with a small project but
[0:21] with a small project but we'll try to make this a robust enough
[0:24] we'll try to make this a robust enough
[0:24] we'll try to make this a robust enough design that it can be copied
[0:25] design that it can be copied
[0:26] design that it can be copied and several students in the past have
[0:28] and several students in the past have
[0:28] and several students in the past have asked me about
[0:29] asked me about
[0:29] asked me about giving some instructions and tutorials a
[0:32] giving some instructions and tutorials a
[0:32] giving some instructions and tutorials a little bit
[0:33] little bit
[0:33] little bit about modeling and solidworks i got most
[0:36] about modeling and solidworks i got most
[0:36] about modeling and solidworks i got most of the way through this
[0:37] of the way through this
[0:37] of the way through this version one of a clamp that i
[0:40] version one of a clamp that i
[0:40] version one of a clamp that i i was just realizing now i should have
[0:42] i was just realizing now i should have
[0:42] i was just realizing now i should have shared the whole process because this
[0:44] shared the whole process because this
[0:44] shared the whole process because this was really only
[0:45] was really only
[0:45] was really only uh 30 minutes designing checking
[0:48] uh 30 minutes designing checking
[0:48] uh 30 minutes designing checking tolerances and building
[0:52] tolerances and building
[0:52] tolerances and building and there's a lot you can learn because
[0:53] and there's a lot you can learn because
[0:53] and there's a lot you can learn because this would take me a lot more than 30
[0:54] this would take me a lot more than 30
[0:54] this would take me a lot more than 30 minutes
[0:56] minutes
[0:56] minutes back in my first year working with
[0:57] back in my first year working with
[0:57] back in my first year working with solidworks but let me just go over the
[0:59] solidworks but let me just go over the
[0:59] solidworks but let me just go over the features
[1:00] features
[1:00] features um and before i go over the features
[1:02] um and before i go over the features
[1:02] um and before i go over the features i'll just show you how i came up with
[1:04] i'll just show you how i came up with
[1:04] i'll just show you how i came up with the concept
[1:06] the concept
[1:06] the concept so i said when the
[1:09] so i said when the
[1:09] so i said when the when the belt is sliding along the
[1:11] when the belt is sliding along the
[1:11] when the belt is sliding along the inside of this conveyor
[1:13] inside of this conveyor
[1:13] inside of this conveyor which is shown here this belt is going
[1:16] which is shown here this belt is going
[1:16] which is shown here this belt is going to be resized
[1:18] to be resized
[1:18] to be resized to i think come almost all the way over
[1:20] to i think come almost all the way over
[1:20] to i think come almost all the way over to this edge
[1:22] to this edge
[1:22] to this edge and something has to keep it on track or
[1:24] and something has to keep it on track or
[1:24] and something has to keep it on track or else it'll want to walk down or walk
[1:26] else it'll want to walk down or walk
[1:26] else it'll want to walk down or walk up and i would like it not to be walking
[1:29] up and i would like it not to be walking
[1:29] up and i would like it not to be walking right into my aluminum parts or
[1:31] right into my aluminum parts or
[1:31] right into my aluminum parts or shredding itself
[1:33] shredding itself
[1:33] shredding itself on the borders of other parts i won't
[1:35] on the borders of other parts i won't
[1:35] on the borders of other parts i won't have a designated
[1:36] have a designated
[1:36] have a designated guide for it so um
[1:40] guide for it so um
[1:40] guide for it so um that means i need something to lie on
[1:43] that means i need something to lie on
[1:43] that means i need something to lie on this
[1:44] this
[1:44] this um on this 30 30
[1:47] um on this 30 30
[1:47] um on this 30 30 rail and also i
[1:51] rail and also i
[1:51] rail and also i understand that there's there's a piece
[1:52] understand that there's there's a piece
[1:52] understand that there's there's a piece of nylon already designed to sit on top
[1:54] of nylon already designed to sit on top
[1:54] of nylon already designed to sit on top of here but
[1:55] of here but
[1:55] of here but we can adjust the height of this clamp
[1:57] we can adjust the height of this clamp
[1:57] we can adjust the height of this clamp as needed
[1:59] as needed
[1:59] as needed depending on either i'll trim back this
[2:01] depending on either i'll trim back this
[2:01] depending on either i'll trim back this nylon sheet
[2:02] nylon sheet
[2:02] nylon sheet or i'll make the clamp larger but the
[2:05] or i'll make the clamp larger but the
[2:05] or i'll make the clamp larger but the the first step is to design something
[2:07] the first step is to design something
[2:07] the first step is to design something from the concept
[2:08] from the concept
[2:08] from the concept get it 3d printed and then fit it and
[2:10] get it 3d printed and then fit it and
[2:10] get it 3d printed and then fit it and get it in my hand so that i can try it
[2:12] get it in my hand so that i can try it
[2:12] get it in my hand so that i can try it out
[2:13] out
[2:13] out and so it's going to sit right here
[2:17] and so it's going to sit right here
[2:17] and so it's going to sit right here and so here we are
[2:20] and so here we are
[2:20] and so here we are on the top i want to have a screw
[2:23] on the top i want to have a screw
[2:23] on the top i want to have a screw two screws i want to have the minimal
[2:25] two screws i want to have the minimal
[2:25] two screws i want to have the minimal number of parts truly
[2:27] number of parts truly
[2:27] number of parts truly and so that's why my initial idea in my
[2:30] and so that's why my initial idea in my
[2:30] and so that's why my initial idea in my mind was
[2:31] mind was
[2:31] mind was actually two or more parts so they would
[2:33] actually two or more parts so they would
[2:33] actually two or more parts so they would clamp with each other
[2:34] clamp with each other
[2:34] clamp with each other similar to what i found in the on the
[2:37] similar to what i found in the on the
[2:37] similar to what i found in the on the tables
[2:38] tables
[2:38] tables in the cnc machine there's
[2:41] in the cnc machine there's
[2:41] in the cnc machine there's t-slot clamping kits and and those are
[2:44] t-slot clamping kits and and those are
[2:44] t-slot clamping kits and and those are usually
[2:45] usually
[2:45] usually two or three pieces but since we're
[2:47] two or three pieces but since we're
[2:47] two or three pieces but since we're working with plastic and 3d printers we
[2:49] working with plastic and 3d printers we
[2:49] working with plastic and 3d printers we can
[2:50] can
[2:50] can just make it conforming so this
[2:53] just make it conforming so this
[2:54] just make it conforming so this this web is designed to bend
[2:57] this web is designed to bend
[2:57] this web is designed to bend and these brass inserts are way
[3:00] and these brass inserts are way
[3:00] and these brass inserts are way oversized for how much tension we need
[3:01] oversized for how much tension we need
[3:02] oversized for how much tension we need to
[3:02] to
[3:02] to put on the screw but i'm commonizing the
[3:05] put on the screw but i'm commonizing the
[3:05] put on the screw but i'm commonizing the size of these
[3:06] size of these
[3:06] size of these with other parts in the assembly so that
[3:08] with other parts in the assembly so that
[3:08] with other parts in the assembly so that we only need to buy one kind of
[3:10] we only need to buy one kind of
[3:10] we only need to buy one kind of m6 screw and also
[3:15] m6 screw and also
[3:15] m6 screw and also it will it's easier to handle the large
[3:18] it will it's easier to handle the large
[3:18] it will it's easier to handle the large um the large fasteners i think
[3:21] um the large fasteners i think
[3:21] um the large fasteners i think um heat set insert wise
[3:25] um heat set insert wise
[3:25] um heat set insert wise two of them it's it's a little bit
[3:27] two of them it's it's a little bit
[3:27] two of them it's it's a little bit costly but
[3:28] costly but
[3:28] costly but um people appreciate appreciate
[3:32] um people appreciate appreciate
[3:32] um people appreciate appreciate the part that they're working with and
[3:33] the part that they're working with and
[3:33] the part that they're working with and and try not to mess it up
[3:36] and try not to mess it up
[3:36] and try not to mess it up um okay so we need clearance in here
[3:39] um okay so we need clearance in here
[3:39] um okay so we need clearance in here these
[3:40] these
[3:40] these these extrusions have varying web widths
[3:43] these extrusions have varying web widths
[3:43] these extrusions have varying web widths so what i did was i took the the width
[3:45] so what i did was i took the the width
[3:45] so what i did was i took the the width that i know mine is
[3:47] that i know mine is
[3:47] that i know mine is and i made it slightly smaller and i
[3:49] and i made it slightly smaller and i
[3:49] and i made it slightly smaller and i centered
[3:50] centered
[3:50] centered the bottom on the center of
[3:53] the bottom on the center of
[3:53] the bottom on the center of the aluminum so let's go into the sketch
[3:56] the aluminum so let's go into the sketch
[3:56] the aluminum so let's go into the sketch and i'll show that
[4:00] and i'll show that
[4:00] and i'll show that by the way the way this is made is in a
[4:02] by the way the way this is made is in a
[4:02] by the way the way this is made is in a sequence exactly like this design tree
[4:06] sequence exactly like this design tree
[4:06] sequence exactly like this design tree so it was made starting out ugly
[4:09] so it was made starting out ugly
[4:09] so it was made starting out ugly and if i open up the main body it
[4:11] and if i open up the main body it
[4:11] and if i open up the main body it started with a sketch if i edit that
[4:13] started with a sketch if i edit that
[4:13] started with a sketch if i edit that sketch
[4:14] sketch
[4:14] sketch this is all the main dimensions for
[4:17] this is all the main dimensions for
[4:17] this is all the main dimensions for the part that really drive what it does
[4:20] the part that really drive what it does
[4:20] the part that really drive what it does so my width is like 8.2 millimeters for
[4:23] so my width is like 8.2 millimeters for
[4:23] so my width is like 8.2 millimeters for my extrusions
[4:24] my extrusions
[4:24] my extrusions and i've that's also the ones back in
[4:27] and i've that's also the ones back in
[4:27] and i've that's also the ones back in texas
[4:27] texas
[4:28] texas where we first ordered them and
[4:31] where we first ordered them and
[4:31] where we first ordered them and i found the same in asia so that's great
[4:34] i found the same in asia so that's great
[4:34] i found the same in asia so that's great 7.5
[4:35] 7.5
[4:35] 7.5 is more than enough clearance so that
[4:37] is more than enough clearance so that
[4:37] is more than enough clearance so that the 3d printer can be
[4:38] the 3d printer can be
[4:38] the 3d printer can be deviating and we have no problem then
[4:41] deviating and we have no problem then
[4:41] deviating and we have no problem then i need a shoulder here i've made this
[4:44] i need a shoulder here i've made this
[4:44] i need a shoulder here i've made this small
[4:45] small
[4:45] small shoulder 1.5 millimeters so that when
[4:47] shoulder 1.5 millimeters so that when
[4:47] shoulder 1.5 millimeters so that when you're sliding it on manually
[4:49] you're sliding it on manually
[4:49] you're sliding it on manually it has an end stop it it knows
[4:53] it has an end stop it it knows
[4:53] it has an end stop it it knows it's a repeatable placement so wherever
[4:55] it's a repeatable placement so wherever
[4:55] it's a repeatable placement so wherever we design this
[4:56] we design this
[4:56] we design this edge that's supposed to run up against
[4:58] edge that's supposed to run up against
[4:58] edge that's supposed to run up against the the polyurethane
[5:00] the the polyurethane
[5:00] the the polyurethane or other material
[5:03] or other material
[5:03] or other material belt that edge is going to be repeatable
[5:06] belt that edge is going to be repeatable
[5:06] belt that edge is going to be repeatable and whatever design changes we make to
[5:08] and whatever design changes we make to
[5:08] and whatever design changes we make to the belt
[5:09] the belt
[5:09] the belt will we can be sure this border
[5:12] will we can be sure this border
[5:12] will we can be sure this border is going to stay where it is so
[5:16] is going to stay where it is so
[5:16] is going to stay where it is so the center line was the first thing that
[5:19] the center line was the first thing that
[5:19] the center line was the first thing that i did
[5:19] i did
[5:19] i did and i took it from the top edge this is
[5:22] and i took it from the top edge this is
[5:22] and i took it from the top edge this is supposed to represent the top edge of
[5:24] supposed to represent the top edge of
[5:24] supposed to represent the top edge of the aluminum
[5:24] the aluminum
[5:24] the aluminum and i said aluminum is 30 millimeters
[5:27] and i said aluminum is 30 millimeters
[5:27] and i said aluminum is 30 millimeters that's
[5:27] that's
[5:27] that's very precise plus or minus a few
[5:31] very precise plus or minus a few
[5:31] very precise plus or minus a few hundredths of a millimeter at most
[5:34] hundredths of a millimeter at most
[5:34] hundredths of a millimeter at most and so 15 is for sure the halfway point
[5:37] and so 15 is for sure the halfway point
[5:38] and so 15 is for sure the halfway point there and if i center my my 7.5
[5:41] there and if i center my my 7.5
[5:41] there and if i center my my 7.5 millimeters in here then i know i can
[5:42] millimeters in here then i know i can
[5:42] millimeters in here then i know i can slide in with no problem
[5:45] slide in with no problem
[5:45] slide in with no problem 1.5 is pretty much the minimum size that
[5:48] 1.5 is pretty much the minimum size that
[5:48] 1.5 is pretty much the minimum size that i would make
[5:49] i would make
[5:49] i would make a shoulder because if it gets smaller
[5:51] a shoulder because if it gets smaller
[5:51] a shoulder because if it gets smaller that's when
[5:53] that's when
[5:53] that's when 3d printers features if your printer is
[5:56] 3d printers features if your printer is
[5:56] 3d printers features if your printer is having a bad day
[5:58] having a bad day
[5:58] having a bad day half a millimeter can kind of turn into
[6:00] half a millimeter can kind of turn into
[6:00] half a millimeter can kind of turn into a
[6:01] a
[6:01] a lump instead of a nice square so two
[6:04] lump instead of a nice square so two
[6:04] lump instead of a nice square so two millimeters in thickness
[6:06] millimeters in thickness
[6:06] millimeters in thickness and then um i need this whole thing to
[6:09] and then um i need this whole thing to
[6:09] and then um i need this whole thing to be compliant
[6:10] be compliant
[6:10] be compliant so the outside web this i might even
[6:13] so the outside web this i might even
[6:13] so the outside web this i might even make this smaller but right now it's 2.5
[6:15] make this smaller but right now it's 2.5
[6:15] make this smaller but right now it's 2.5 and i need this length here 11
[6:18] and i need this length here 11
[6:18] and i need this length here 11 millimeters
[6:20] millimeters
[6:20] millimeters that honestly um is the minimum
[6:24] that honestly um is the minimum
[6:24] that honestly um is the minimum that i want it i would love to make it
[6:26] that i want it i would love to make it
[6:26] that i want it i would love to make it longer
[6:27] longer
[6:27] longer because then this has a small amount of
[6:30] because then this has a small amount of
[6:30] because then this has a small amount of flex
[6:31] flex
[6:31] flex when you're clamping the top when you're
[6:34] when you're clamping the top when you're
[6:34] when you're clamping the top when you're clamping this
[6:35] clamping this
[6:35] clamping this to this and compressing those with the
[6:38] to this and compressing those with the
[6:38] to this and compressing those with the screw
[6:40] screw
[6:40] screw i i don't want my screws here
[6:48] so screw's going to be fed from the top
[6:48] so screw's going to be fed from the top and go to the bottom and clamp this i
[6:50] and go to the bottom and clamp this i
[6:50] and go to the bottom and clamp this i don't want to compress
[6:52] don't want to compress
[6:52] don't want to compress this part of the web i actually want it
[6:54] this part of the web i actually want it
[6:54] this part of the web i actually want it to bend
[6:56] to bend
[6:56] to bend and curl so the further to the left
[6:59] and curl so the further to the left
[6:59] and curl so the further to the left that i can make my screws the better it
[7:02] that i can make my screws the better it
[7:02] that i can make my screws the better it is going to achieve that
[7:04] is going to achieve that
[7:04] is going to achieve that that result and and this is kind of
[7:06] that result and and this is kind of
[7:06] that result and and this is kind of pushing it i'm going to print this out
[7:08] pushing it i'm going to print this out
[7:08] pushing it i'm going to print this out and find out well how
[7:09] and find out well how
[7:09] and find out well how small how compact can i make this whole
[7:11] small how compact can i make this whole
[7:11] small how compact can i make this whole clamp
[7:12] clamp
[7:12] clamp um using less printing material etc
[7:16] um using less printing material etc
[7:16] um using less printing material etc and still achieve what i'm looking for
[7:26] okay so then what other features are
[7:26] okay so then what other features are important
[7:27] important
[7:27] important um i just decided by eyeballing that 12
[7:30] um i just decided by eyeballing that 12
[7:30] um i just decided by eyeballing that 12 millimeters is
[7:31] millimeters is
[7:31] millimeters is more than enough for the belt guide that
[7:34] more than enough for the belt guide that
[7:34] more than enough for the belt guide that should make people very quickly aware
[7:38] should make people very quickly aware
[7:38] should make people very quickly aware that this is the top side
[7:40] that this is the top side
[7:40] that this is the top side in case they were about to um
[7:43] in case they were about to um
[7:43] in case they were about to um set it upside down because you could
[7:45] set it upside down because you could
[7:45] set it upside down because you could almost make this symmetric
[7:46] almost make this symmetric
[7:46] almost make this symmetric you could make this very thin and it
[7:49] you could make this very thin and it
[7:49] you could make this very thin and it would still do its job since the belt is
[7:51] would still do its job since the belt is
[7:51] would still do its job since the belt is only 1.6 millimeters in thickness
[7:53] only 1.6 millimeters in thickness
[7:53] only 1.6 millimeters in thickness and it should be snug enough that it's
[7:55] and it should be snug enough that it's
[7:55] and it should be snug enough that it's not jumping up and down
[7:58] not jumping up and down
[7:58] not jumping up and down 3.5 is kind of the minimum wall
[8:01] 3.5 is kind of the minimum wall
[8:01] 3.5 is kind of the minimum wall thickness that i do for
[8:02] thickness that i do for
[8:02] thickness that i do for something that's supposed to have some
[8:03] something that's supposed to have some
[8:03] something that's supposed to have some strength and rigidity
[8:05] strength and rigidity
[8:05] strength and rigidity when i'm dealing with abs plastic all
[8:08] when i'm dealing with abs plastic all
[8:08] when i'm dealing with abs plastic all the other plastics that we print with
[8:09] the other plastics that we print with
[8:09] the other plastics that we print with are really just
[8:11] are really just
[8:11] are really just consequential to my choices about abs
[8:15] consequential to my choices about abs
[8:15] consequential to my choices about abs sometimes they match the performance and
[8:17] sometimes they match the performance and
[8:17] sometimes they match the performance and sometimes they don't but
[8:19] sometimes they don't but
[8:19] sometimes they don't but i i designed for abs um
[8:22] i i designed for abs um
[8:22] i i designed for abs um a lot of the choices are from experiment
[8:24] a lot of the choices are from experiment
[8:24] a lot of the choices are from experiment experience i'm not simulating this stuff
[8:28] experience i'm not simulating this stuff
[8:28] experience i'm not simulating this stuff so i make this 3.5 and then okay i know
[8:32] so i make this 3.5 and then okay i know
[8:32] so i make this 3.5 and then okay i know on the top side i need
[8:33] on the top side i need
[8:33] on the top side i need room to nest my screws as much as
[8:37] room to nest my screws as much as
[8:37] room to nest my screws as much as possible i like to keep the screws
[8:39] possible i like to keep the screws
[8:39] possible i like to keep the screws flush or internal to my assembly so that
[8:42] flush or internal to my assembly so that
[8:42] flush or internal to my assembly so that i can always add more features with
[8:44] i can always add more features with
[8:44] i can always add more features with without
[8:46] without
[8:46] without so many hang-ups also if i nest it then
[8:48] so many hang-ups also if i nest it then
[8:48] so many hang-ups also if i nest it then the overall
[8:49] the overall
[8:49] the overall dimension top to bottom
[8:53] dimension top to bottom
[8:53] dimension top to bottom so this is a driven
[9:04] here that window went way off to the
[9:04] here that window went way off to the left side of the screen
[9:06] left side of the screen
[9:06] left side of the screen um make this driven okay so it's gray
[9:09] um make this driven okay so it's gray
[9:09] um make this driven okay so it's gray it's just giving me information
[9:11] it's just giving me information
[9:11] it's just giving me information 22.25 that means um
[9:15] 22.25 that means um
[9:15] 22.25 that means um that uh i i don't want to buy screws
[9:19] that uh i i don't want to buy screws
[9:19] that uh i i don't want to buy screws that are
[9:20] that are
[9:20] that are like 25 millimeters or longer
[9:23] like 25 millimeters or longer
[9:23] like 25 millimeters or longer i think if i keep this from here to here
[9:27] i think if i keep this from here to here
[9:27] i think if i keep this from here to here 20 millimeters then i can companize the
[9:29] 20 millimeters then i can companize the
[9:29] 20 millimeters then i can companize the screw so that's one thing that i'm
[9:31] screw so that's one thing that i'm
[9:31] screw so that's one thing that i'm aiming for but i'm not gonna
[9:33] aiming for but i'm not gonna
[9:33] aiming for but i'm not gonna base my whole design on that so first
[9:35] base my whole design on that so first
[9:35] base my whole design on that so first most primarily i want to nest it
[9:38] most primarily i want to nest it
[9:38] most primarily i want to nest it and then and it might be countersunk it
[9:41] and then and it might be countersunk it
[9:41] and then and it might be countersunk it might be counter-bored we'll we'll find
[9:43] might be counter-bored we'll we'll find
[9:43] might be counter-bored we'll we'll find out that later
[9:44] out that later
[9:44] out that later when i order some screws or when i try
[9:46] when i order some screws or when i try
[9:46] when i order some screws or when i try out the ones that i have on the shelf
[9:48] out the ones that i have on the shelf
[9:48] out the ones that i have on the shelf and then the bottom i know that my
[9:50] and then the bottom i know that my
[9:50] and then the bottom i know that my threaded inserts
[9:52] threaded inserts
[9:52] threaded inserts they need to be um
[9:55] they need to be um
[9:55] they need to be um i think the m6 ones i don't deal with a
[9:57] i think the m6 ones i don't deal with a
[9:57] i think the m6 ones i don't deal with a lot but i think they're
[9:58] lot but i think they're
[9:58] lot but i think they're probably six millimeters um this is not
[10:01] probably six millimeters um this is not
[10:01] probably six millimeters um this is not the ideal situation for this
[10:03] the ideal situation for this
[10:03] the ideal situation for this brass insert but it's definitely going
[10:05] brass insert but it's definitely going
[10:05] brass insert but it's definitely going to serve its purpose so 5.5 is more than
[10:07] to serve its purpose so 5.5 is more than
[10:08] to serve its purpose so 5.5 is more than enough
[10:09] enough
[10:09] enough um but it has to be a little bit beefy
[10:11] um but it has to be a little bit beefy
[10:11] um but it has to be a little bit beefy to to take that heat and not just
[10:13] to to take that heat and not just
[10:13] to to take that heat and not just totally melt apart while i'm inserting
[10:16] totally melt apart while i'm inserting
[10:16] totally melt apart while i'm inserting um okay so then a lot of these
[10:20] um okay so then a lot of these
[10:20] um okay so then a lot of these uh were adjusted after i made the
[10:23] uh were adjusted after i made the
[10:23] uh were adjusted after i made the following features
[10:24] following features
[10:24] following features so after that i said okay now i need to
[10:28] so after that i said okay now i need to
[10:28] so after that i said okay now i need to cut the holes where are the screws gonna
[10:29] cut the holes where are the screws gonna
[10:29] cut the holes where are the screws gonna go i want
[10:31] go i want
[10:31] go i want um i'd love to have more but for
[10:34] um i'd love to have more but for
[10:34] um i'd love to have more but for assembly purposes and purchasing
[10:36] assembly purposes and purchasing
[10:36] assembly purposes and purchasing let's keep it to two for now
[10:43] and let's place them
[10:43] and let's place them using as minimal dimensions as we can
[10:47] using as minimal dimensions as we can
[10:47] using as minimal dimensions as we can first i draw a line say where are they
[10:48] first i draw a line say where are they
[10:48] first i draw a line say where are they going to be centered from the outside
[10:51] going to be centered from the outside
[10:51] going to be centered from the outside or from the inside i dimension it from
[10:53] or from the inside i dimension it from
[10:53] or from the inside i dimension it from the outside because
[11:00] i want to clear this wall and i want to
[11:00] i want to clear this wall and i want to know
[11:01] know
[11:01] know how how far can i get from the wall
[11:04] how how far can i get from the wall
[11:04] how how far can i get from the wall if i need to iterate this part then i'll
[11:06] if i need to iterate this part then i'll
[11:06] if i need to iterate this part then i'll increase that but
[11:09] increase that but
[11:09] increase that but on the other hand the there's a
[11:12] on the other hand the there's a
[11:12] on the other hand the there's a limitation how far i can make it but
[11:14] limitation how far i can make it but
[11:14] limitation how far i can make it but i'll just
[11:14] i'll just
[11:14] i'll just check that visually because i don't care
[11:17] check that visually because i don't care
[11:17] check that visually because i don't care how close as long as there's no
[11:18] how close as long as there's no
[11:18] how close as long as there's no interference i don't care how close
[11:20] interference i don't care how close
[11:20] interference i don't care how close these threads are
[11:21] these threads are
[11:21] these threads are to my aluminum i'll show you what i mean
[11:23] to my aluminum i'll show you what i mean
[11:24] to my aluminum i'll show you what i mean and then
[11:24] and then
[11:24] and then six millimeters is going to be a
[11:26] six millimeters is going to be a
[11:26] six millimeters is going to be a clearance hole for m6
[11:29] clearance hole for m6
[11:29] clearance hole for m6 and i drove those holes all the way
[11:31] and i drove those holes all the way
[11:31] and i drove those holes all the way through
[11:32] through
[11:32] through so that goes through the assembly and
[11:35] so that goes through the assembly and
[11:35] so that goes through the assembly and then i can
[11:36] then i can
[11:36] then i can use the feature on the bottom if i
[11:37] use the feature on the bottom if i
[11:37] use the feature on the bottom if i change the size of the hole
[11:39] change the size of the hole
[11:39] change the size of the hole as my guide i chamfered those but later
[11:42] as my guide i chamfered those but later
[11:42] as my guide i chamfered those but later they'll probably be counter-bored
[11:44] they'll probably be counter-bored
[11:44] they'll probably be counter-bored this is the part where i'm starting to
[11:45] this is the part where i'm starting to
[11:46] this is the part where i'm starting to think about the 3d printing
[11:48] think about the 3d printing
[11:48] think about the 3d printing so my print orientation is like this a
[11:51] so my print orientation is like this a
[11:51] so my print orientation is like this a simple extrude
[11:52] simple extrude
[11:52] simple extrude is always 3d printable but these holes
[11:54] is always 3d printable but these holes
[11:54] is always 3d printable but these holes are nearing
[11:55] are nearing
[11:56] are nearing the the upper limit of how large can i
[11:59] the the upper limit of how large can i
[11:59] the the upper limit of how large can i make the diameter before it
[12:00] make the diameter before it
[12:00] make the diameter before it um before the i i need supports here and
[12:04] um before the i i need supports here and
[12:04] um before the i i need supports here and this
[12:04] this
[12:04] this roof is going to be ugly i know that if
[12:06] roof is going to be ugly i know that if
[12:06] roof is going to be ugly i know that if i just tried to
[12:08] i just tried to
[12:08] i just tried to take this off the printer and drop the
[12:09] take this off the printer and drop the
[12:09] take this off the printer and drop the screw in this top
[12:11] screw in this top
[12:11] screw in this top area is going to interfere for sure i'm
[12:13] area is going to interfere for sure i'm
[12:13] area is going to interfere for sure i'm going to have to kind of
[12:14] going to have to kind of
[12:14] going to have to kind of saw it with my hands but but these are
[12:17] saw it with my hands but but these are
[12:17] saw it with my hands but but these are small impacts i think
[12:18] small impacts i think
[12:18] small impacts i think six millimeters we might get away with
[12:20] six millimeters we might get away with
[12:20] six millimeters we might get away with it so we'll try it
[12:25] the three millimeters always work okay
[12:26] the three millimeters always work okay then i fill it this is mainly for
[12:27] then i fill it this is mainly for
[12:27] then i fill it this is mainly for aesthetics but also i think it will help
[12:30] aesthetics but also i think it will help
[12:30] aesthetics but also i think it will help make the stress flow
[12:33] make the stress flow
[12:33] make the stress flow i talk about things like um stress
[12:35] i talk about things like um stress
[12:35] i talk about things like um stress concentrations and so forth
[12:37] concentrations and so forth
[12:37] concentrations and so forth this stuff is most of these
[12:41] this stuff is most of these
[12:41] this stuff is most of these parts in the assembly are nowhere near
[12:43] parts in the assembly are nowhere near
[12:43] parts in the assembly are nowhere near their their limits
[12:45] their their limits
[12:45] their their limits in tension or compression or for the
[12:47] in tension or compression or for the
[12:47] in tension or compression or for the material but
[12:49] material but
[12:49] material but we just keep the good design principles
[12:51] we just keep the good design principles
[12:51] we just keep the good design principles in mind
[12:52] in mind
[12:52] in mind so we try to relieve that tension in
[12:54] so we try to relieve that tension in
[12:54] so we try to relieve that tension in here for outside it's for aesthetics
[12:56] here for outside it's for aesthetics
[12:56] here for outside it's for aesthetics mainly and for
[12:58] mainly and for
[12:58] mainly and for i mean why print this material that's a
[13:01] i mean why print this material that's a
[13:01] i mean why print this material that's a few
[13:01] few
[13:01] few cubic millimeters of material that we
[13:04] cubic millimeters of material that we
[13:04] cubic millimeters of material that we don't need to have
[13:05] don't need to have
[13:05] don't need to have because out there it doesn't experience
[13:08] because out there it doesn't experience
[13:08] because out there it doesn't experience any it doesn't hold any load out there
[13:11] any it doesn't hold any load out there
[13:11] any it doesn't hold any load out there um if we were to have a sharp corner so
[13:13] um if we were to have a sharp corner so
[13:13] um if we were to have a sharp corner so that material that was basically removed
[13:15] that material that was basically removed
[13:15] that material that was basically removed by the fillet
[13:16] by the fillet
[13:16] by the fillet it's just saving me money and time on
[13:19] it's just saving me money and time on
[13:19] it's just saving me money and time on the printer
[13:20] the printer
[13:20] the printer also printer performance seems to be
[13:22] also printer performance seems to be
[13:22] also printer performance seems to be best we
[13:23] best we
[13:23] best we when we do the curved corners i think it
[13:26] when we do the curved corners i think it
[13:26] when we do the curved corners i think it helps with adhesion but that's a
[13:28] helps with adhesion but that's a
[13:28] helps with adhesion but that's a a loose claim that's up for argument
[13:32] a loose claim that's up for argument
[13:32] a loose claim that's up for argument um on the inside i don't want to risk
[13:35] um on the inside i don't want to risk
[13:35] um on the inside i don't want to risk filleting these
[13:36] filleting these
[13:36] filleting these because i need the height of this to do
[13:38] because i need the height of this to do
[13:38] because i need the height of this to do a job
[13:39] a job
[13:39] a job and it's already short 1.5 millimeters
[13:42] and it's already short 1.5 millimeters
[13:42] and it's already short 1.5 millimeters um this one i didn't fill it because
[13:45] um this one i didn't fill it because
[13:45] um this one i didn't fill it because well i could fill it
[13:49] well i could fill it
[13:49] well i could fill it yeah if this was short then i wouldn't
[13:52] yeah if this was short then i wouldn't
[13:52] yeah if this was short then i wouldn't do it but let me go ahead and add that
[13:59] so you can see the list of edges that
[13:59] so you can see the list of edges that are selected in solidworks
[14:01] are selected in solidworks
[14:01] are selected in solidworks you just hit the green check okay now
[14:03] you just hit the green check okay now
[14:03] you just hit the green check okay now that's there
[14:04] that's there
[14:04] that's there see something i don't like is if if this
[14:06] see something i don't like is if if this
[14:06] see something i don't like is if if this turns out to be
[14:08] turns out to be
[14:08] turns out to be um let's look at the assembly
[14:16] see my my bottom screws i'll come back
[14:16] see my my bottom screws i'll come back to this
[14:17] to this
[14:17] to this the bottom screws um the
[14:20] the bottom screws um the
[14:20] the bottom screws um the diameter of the brass insert is nine
[14:23] diameter of the brass insert is nine
[14:23] diameter of the brass insert is nine millimeters
[14:24] millimeters
[14:24] millimeters it actually has multiple diameters
[14:25] it actually has multiple diameters
[14:25] it actually has multiple diameters because it's um it kind of
[14:28] because it's um it kind of
[14:28] because it's um it kind of kind of has a an angle to it
[14:31] kind of has a an angle to it
[14:31] kind of has a an angle to it and multiple features but nine is what
[14:33] and multiple features but nine is what
[14:33] and multiple features but nine is what i'm going to try
[14:35] i'm going to try
[14:35] i'm going to try and and then i chamfered the bottom
[14:37] and and then i chamfered the bottom
[14:38] and and then i chamfered the bottom holes that's
[14:39] holes that's
[14:39] holes that's for cleanliness of 3d printing more than
[14:42] for cleanliness of 3d printing more than
[14:42] for cleanliness of 3d printing more than anything else and also
[14:43] anything else and also
[14:44] anything else and also if there's a burr here when we insert
[14:45] if there's a burr here when we insert
[14:45] if there's a burr here when we insert the the
[14:47] the the
[14:47] the the threaded insert then it's going to be
[14:49] threaded insert then it's going to be
[14:49] threaded insert then it's going to be more likely to
[14:59] caused me to make a mistake in my
[14:59] caused me to make a mistake in my placement
[15:00] placement
[15:00] placement so that it might not be absolutely
[15:02] so that it might not be absolutely
[15:02] so that it might not be absolutely concentric and and this should help
[15:05] concentric and and this should help
[15:05] concentric and and this should help remove burrs when you can and also make
[15:07] remove burrs when you can and also make
[15:07] remove burrs when you can and also make the part prettier
[15:08] the part prettier
[15:08] the part prettier um most the time when i do a threaded
[15:11] um most the time when i do a threaded
[15:11] um most the time when i do a threaded insert
[15:18] um yeah this background they're always
[15:18] um yeah this background they're always so
[15:18] so
[15:18] so dark yellow looks like mustard
[15:22] dark yellow looks like mustard
[15:22] dark yellow looks like mustard anyway usually these are used by
[15:25] anyway usually these are used by
[15:26] anyway usually these are used by me in the opposite way i'm pulling them
[15:28] me in the opposite way i'm pulling them
[15:28] me in the opposite way i'm pulling them out of the material
[15:31] out of the material
[15:31] out of the material i mean it's not on purpose but i'll put
[15:33] i mean it's not on purpose but i'll put
[15:33] i mean it's not on purpose but i'll put a pcb here
[15:35] a pcb here
[15:35] a pcb here and then the screw through both or
[15:37] and then the screw through both or
[15:37] and then the screw through both or through that and then into the threaded
[15:38] through that and then into the threaded
[15:38] through that and then into the threaded insert and
[15:39] insert and
[15:39] insert and if somebody were to lift on the pcb
[15:41] if somebody were to lift on the pcb
[15:41] if somebody were to lift on the pcb you'd want to pull out the threaded
[15:42] you'd want to pull out the threaded
[15:42] you'd want to pull out the threaded insert
[15:43] insert
[15:43] insert on this part we have a privilege of the
[15:46] on this part we have a privilege of the
[15:46] on this part we have a privilege of the the tension of the screw is actually
[15:48] the tension of the screw is actually
[15:48] the tension of the screw is actually wanting to seat the insert more which is
[15:51] wanting to seat the insert more which is
[15:51] wanting to seat the insert more which is another reason why i'm not concerned
[15:53] another reason why i'm not concerned
[15:53] another reason why i'm not concerned about having
[15:54] about having
[15:54] about having the thickness of this plastic the full
[15:56] the thickness of this plastic the full
[15:56] the thickness of this plastic the full height
[15:58] height
[15:58] height of the insert so
[16:01] of the insert so
[16:01] of the insert so um and then as we can see we're getting
[16:05] um and then as we can see we're getting
[16:05] um and then as we can see we're getting very close to the
[16:06] very close to the
[16:06] very close to the to the aluminum but i think that's at
[16:08] to the aluminum but i think that's at
[16:08] to the aluminum but i think that's at least a millimeter because this is a
[16:09] least a millimeter because this is a
[16:09] least a millimeter because this is a millimeter and a half
[16:11] millimeter and a half
[16:11] millimeter and a half i'm just gonna not worry about it until
[16:13] i'm just gonna not worry about it until
[16:13] i'm just gonna not worry about it until i test the first part
[16:14] i test the first part
[16:14] i test the first part this is very close but i mean we're
[16:16] this is very close but i mean we're
[16:16] this is very close but i mean we're we're inserting these
[16:18] we're inserting these
[16:18] we're inserting these with a yellow piece standing alone and
[16:19] with a yellow piece standing alone and
[16:19] with a yellow piece standing alone and then we'll insert the yellow piece so we
[16:21] then we'll insert the yellow piece so we
[16:21] then we'll insert the yellow piece so we have
[16:22] have
[16:22] have we um we can make adjustments as needed
[16:27] we um we can make adjustments as needed
[16:27] we um we can make adjustments as needed um as for this fillet so
[16:31] um as for this fillet so
[16:31] um as for this fillet so i want to guarantee that every
[16:34] i want to guarantee that every
[16:34] i want to guarantee that every millimeter along this path is
[16:37] millimeter along this path is
[16:37] millimeter along this path is resting against something on my aluminum
[16:41] resting against something on my aluminum
[16:41] resting against something on my aluminum that's the whole
[16:41] that's the whole
[16:41] that's the whole clamping force is going to come from the
[16:43] clamping force is going to come from the
[16:43] clamping force is going to come from the friction at those two faces
[16:46] friction at those two faces
[16:46] friction at those two faces if this was short which i might even
[16:48] if this was short which i might even
[16:48] if this was short which i might even make it shorter
[16:49] make it shorter
[16:49] make it shorter yeah that's just a waste of material
[16:51] yeah that's just a waste of material
[16:51] yeah that's just a waste of material nothing happens on the inside of here
[16:53] nothing happens on the inside of here
[16:53] nothing happens on the inside of here um then if this was too short then
[16:57] um then if this was too short then
[16:57] um then if this was too short then i'm taking i'm stealing some of the
[16:59] i'm taking i'm stealing some of the
[17:00] i'm taking i'm stealing some of the material some that's contacting
[17:01] material some that's contacting
[17:02] material some that's contacting once this gets clamped control eight
[17:08] once it gets clamped that gap's gonna
[17:08] once it gets clamped that gap's gonna close and and even this
[17:10] close and and even this
[17:10] close and and even this radius i wish it were not there because
[17:12] radius i wish it were not there because
[17:12] radius i wish it were not there because then i get more
[17:14] then i get more
[17:14] then i get more um surface that's mating so that's the
[17:17] um surface that's mating so that's the
[17:17] um surface that's mating so that's the consideration
[17:18] consideration
[17:18] consideration um open part
[17:21] um open part
[17:21] um open part and i can edit this sketch so right now
[17:26] and i can edit this sketch so right now
[17:26] and i can edit this sketch so right now what's driving this is they're just
[17:28] what's driving this is they're just
[17:28] what's driving this is they're just simply um
[17:29] simply um
[17:29] simply um co-linear lines so i delete this
[17:32] co-linear lines so i delete this
[17:32] co-linear lines so i delete this single click and drag that somewhere and
[17:36] single click and drag that somewhere and
[17:36] single click and drag that somewhere and it's actually moving everything so i'll
[17:37] it's actually moving everything so i'll
[17:37] it's actually moving everything so i'll have to make adjustments
[17:39] have to make adjustments
[17:39] have to make adjustments and i'm going to create a dimension
[17:47] uh no i can simply make this shorter
[17:47] uh no i can simply make this shorter no dimension there um
[17:50] no dimension there um
[17:50] no dimension there um so let's make this 3.5 and
[17:54] so let's make this 3.5 and
[17:54] so let's make this 3.5 and um and then what did i mess up
[18:00] um and then what did i mess up
[18:00] um and then what did i mess up so what we're messing with right now is
[18:02] so what we're messing with right now is
[18:02] so what we're messing with right now is the
[18:09] the length of this area
[18:09] the length of this area so what purpose does that area serve
[18:11] so what purpose does that area serve
[18:11] so what purpose does that area serve almost nothing
[18:12] almost nothing
[18:12] almost nothing so
[18:18] well this makes contact with the top
[18:18] well this makes contact with the top which gives us some friction
[18:21] which gives us some friction
[18:21] which gives us some friction so if i made this as short as this
[18:24] so if i made this as short as this
[18:24] so if i made this as short as this then we have i don't know it feels like
[18:27] then we have i don't know it feels like
[18:27] then we have i don't know it feels like a little less
[18:27] a little less
[18:28] a little less clamping action so
[18:37] i should make these co-linear instead of
[18:37] i should make these co-linear instead of just
[18:37] just
[18:37] just putting the constraint i'll actually
[18:39] putting the constraint i'll actually
[18:39] putting the constraint i'll actually draw the line because
[18:42] draw the line because
[18:42] draw the line because both of these are going to rest against
[18:44] both of these are going to rest against
[18:44] both of these are going to rest against the shoulder of
[18:45] the shoulder of
[18:45] the shoulder of the aluminum and
[18:59] okay so the design decision here
[18:59] okay so the design decision here is how far in do i want this face
[19:02] is how far in do i want this face
[19:02] is how far in do i want this face guiding my um
[19:05] guiding my um
[19:05] guiding my um guiding my belt from the outside of the
[19:08] guiding my belt from the outside of the
[19:08] guiding my belt from the outside of the aluminum extrusion
[19:10] aluminum extrusion
[19:10] aluminum extrusion so 15 millimeters is the midpoint
[19:13] so 15 millimeters is the midpoint
[19:13] so 15 millimeters is the midpoint um six
[19:17] um six
[19:17] um six let's do seven that kind of feels like
[19:21] let's do seven that kind of feels like
[19:21] let's do seven that kind of feels like where i was before and we'll adjust that
[19:24] where i was before and we'll adjust that
[19:24] where i was before and we'll adjust that we're going to have to print once test
[19:26] we're going to have to print once test
[19:26] we're going to have to print once test it out and then decide where we want our
[19:28] it out and then decide where we want our
[19:28] it out and then decide where we want our belt to sit
[19:30] belt to sit
[19:30] belt to sit or maybe we'll find the belt only comes
[19:32] or maybe we'll find the belt only comes
[19:32] or maybe we'll find the belt only comes in certain increments we'll buy it we'll
[19:34] in certain increments we'll buy it we'll
[19:34] in certain increments we'll buy it we'll place it and then we'll adjust this
[19:36] place it and then we'll adjust this
[19:36] place it and then we'll adjust this thing so ctrl save
[19:39] thing so ctrl save
[19:39] thing so ctrl save close that so you can look at this and
[19:43] close that so you can look at this and
[19:43] close that so you can look at this and just ask yourself is this far enough
[19:45] just ask yourself is this far enough
[19:45] just ask yourself is this far enough over from the edge that it doesn't feel
[19:48] over from the edge that it doesn't feel
[19:48] over from the edge that it doesn't feel like it's going to fall off
[19:50] like it's going to fall off
[19:50] like it's going to fall off well i think at this point we just have
[19:52] well i think at this point we just have
[19:52] well i think at this point we just have to try it out

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
