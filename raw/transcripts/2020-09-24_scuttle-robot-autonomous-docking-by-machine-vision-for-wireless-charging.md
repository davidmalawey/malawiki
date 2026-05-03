---
title: "SCUTTLE Robot - Autonomous Docking by machine vision for Wireless Charging"
url: "https://www.youtube.com/watch?v=ffzLKSx1p6A"
video_id: "ffzLKSx1p6A"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-09-24
duration: "11:44"
duration_sec: 704
views: 1008
likes: 19
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/ffzLKSx1p6A/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 716
chapters_count: 10
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: https://scuttlerobot.org

This video covers most of the design and demonstration of the wireless charging station built by capstone team "nextec" at the Texas A&M ETID department.  This team graduated in fall of 2019.  The proof of concept design charges the robot's 3-cell lipo battery wirelessly and recognizes the scuttle arrival.  The scuttle uses machine vision to discover the charging station's colored beacon. IoT is implemented using Cayenne.

0:00 autonomous docking demo
0:24 Conceptual Block Diagram
2:37 Software Flow Diagram
4:59 Station Panel Design
5:30 Chassis-fixed Panel Explained
6:10 RFID card module
6:40 RFID Software Flow Chart
8:35 Station PCB Schematic
9:30 Chassis-fixed PCB
10:30 RFID Scan Demo

More On This Project:
Charging and Undocking From Station: youtu.be/IprAJX3xK3A

RFID Updating With Different Tags: youtu.be/EMONM6zKg00

Occupancy Status of Station: youtu.be/GEWiNxjF4qw

Autonomous Docking With Station (10 Tests, 11 min) youtu.be/NDbsoNvCBXI

Final Presentation Live (Partial) youtu.be/QkN5Fhh5uTA

Final Presentation Recording (Full) youtu.be/Av9WNS2dgkg

## Chapters

- 0:00 autonomous docking demo
- 0:24 Conceptual Block Diagram
- 2:37 Software Flow Diagram
- 4:59 Station Panel Design
- 5:30 Chassis-fixed Panel Explained
- 6:10 RFID card module
- 6:40 RFID Software Flow Chart
- 8:35 Station PCB Schematic
- 9:30 Chassis-fixed PCB
- 10:30 RFID Scan Demo

## Transcript

[0:03] okay no no
[0:03] okay no no we want to just park i want to dock
[0:07] we want to just park i want to dock
[0:07] we want to just park i want to dock manually oh did you do it automatically
[0:09] manually oh did you do it automatically
[0:09] manually oh did you do it automatically yeah yeah i did
[0:11] yeah yeah i did
[0:11] yeah yeah i did still be fine it should go actually yeah
[0:14] still be fine it should go actually yeah
[0:14] still be fine it should go actually yeah you'll
[0:31] okay super and then can you undock it
[0:31] okay super and then can you undock it and then we'll watch this
[0:32] and then we'll watch this
[0:32] and then we'll watch this watch this indicator yeah
[0:44] no it says it's vacant again
[0:44] no it says it's vacant again through electronics design software
[0:45] through electronics design software
[0:45] through electronics design software design enclosure design and then
[0:47] design enclosure design and then
[0:47] design enclosure design and then talk about the timeline how it takes
[0:48] talk about the timeline how it takes
[0:48] talk about the timeline how it takes with the project how many hours on the
[0:50] with the project how many hours on the
[0:50] with the project how many hours on the project and then
[0:51] project and then
[0:51] project and then how much it costs
[0:55] our project's primary goal is to create
[0:55] our project's primary goal is to create a system for enabling a scuttle detox
[0:57] a system for enabling a scuttle detox
[0:57] a system for enabling a scuttle detox you're on the go maybe you want to do a
[0:58] you're on the go maybe you want to do a
[0:58] you're on the go maybe you want to do a mobile hotspot or whatever
[0:59] mobile hotspot or whatever
[0:59] mobile hotspot or whatever but for our project we want to make sure
[1:01] but for our project we want to make sure
[1:01] but for our project we want to make sure that it works with tamu's network
[1:02] that it works with tamu's network
[1:02] that it works with tamu's network because it will be used for students
[1:03] because it will be used for students
[1:03] because it will be used for students here
[1:04] here
[1:04] here all of that information is being
[1:05] all of that information is being
[1:05] all of that information is being communicated to the cayenne iot database
[1:07] communicated to the cayenne iot database
[1:07] communicated to the cayenne iot database where it's represented by that laptop
[1:08] where it's represented by that laptop
[1:08] where it's represented by that laptop there
[1:09] there
[1:09] there and we're displaying information such as
[1:10] and we're displaying information such as
[1:10] and we're displaying information such as the battery levels and the
[1:12] the battery levels and the
[1:12] the battery levels and the rfid status of the charging station
[1:16] rfid status of the charging station
[1:16] rfid status of the charging station so this is our system functional block
[1:17] so this is our system functional block
[1:17] so this is our system functional block diagram the top half represents the
[1:18] diagram the top half represents the
[1:18] diagram the top half represents the charging station
[1:19] charging station
[1:19] charging station and the bottom half represents what you
[1:21] and the bottom half represents what you
[1:21] and the bottom half represents what you see onboard the scuttle
[1:22] see onboard the scuttle
[1:22] see onboard the scuttle the charging station is a little bit
[1:24] the charging station is a little bit
[1:24] the charging station is a little bit simple in design basically we just need
[1:25] simple in design basically we just need
[1:25] simple in design basically we just need to take in power from the wall and
[1:27] to take in power from the wall and
[1:27] to take in power from the wall and supply enough power to our three
[1:28] supply enough power to our three
[1:28] supply enough power to our three charging pads that are on the front
[1:29] charging pads that are on the front
[1:29] charging pads that are on the front there as well as the rfid reader and the
[1:31] there as well as the rfid reader and the
[1:31] there as well as the rfid reader and the beaglebone blue all housed inside we'll
[1:33] beaglebone blue all housed inside we'll
[1:33] beaglebone blue all housed inside we'll take a look at the pcb and how that
[1:34] take a look at the pcb and how that
[1:34] take a look at the pcb and how that works here in a second
[1:35] works here in a second
[1:35] works here in a second and then the scuttle onboard module
[1:36] and then the scuttle onboard module
[1:36] and then the scuttle onboard module below same rough idea we know we need to
[1:38] below same rough idea we know we need to
[1:38] below same rough idea we know we need to take in power from the receiver pads we
[1:40] take in power from the receiver pads we
[1:40] take in power from the receiver pads we need to control that power using those
[1:41] need to control that power using those
[1:41] need to control that power using those relays that's how we can check for
[1:42] relays that's how we can check for
[1:42] relays that's how we can check for charging and then obviously
[1:43] charging and then obviously
[1:44] charging and then obviously um ensure that we don't overcharge the
[1:46] um ensure that we don't overcharge the
[1:46] um ensure that we don't overcharge the batteries
[1:47] batteries
[1:47] batteries and then we need to supply that power
[1:48] and then we need to supply that power
[1:48] and then we need to supply that power through a light bulb connection um to
[1:50] through a light bulb connection um to
[1:50] through a light bulb connection um to the scuttle's battery pack which is
[1:51] the scuttle's battery pack which is
[1:51] the scuttle's battery pack which is modified to have that lipo connection on
[1:53] modified to have that lipo connection on
[1:53] modified to have that lipo connection on the bottom of it
[1:54] the bottom of it
[1:54] the bottom of it and this is all controlled with one gpio
[1:56] and this is all controlled with one gpio
[1:56] and this is all controlled with one gpio pin from the beaglebone blue
[1:57] pin from the beaglebone blue
[1:57] pin from the beaglebone blue through a low side switching fifth
[2:02] so our deliverables are the prototype
[2:02] so our deliverables are the prototype charging station you see here the
[2:04] charging station you see here the
[2:04] charging station you see here the prototype scuttle on board module you
[2:06] prototype scuttle on board module you
[2:06] prototype scuttle on board module you see here and just watched run around
[2:08] see here and just watched run around
[2:08] see here and just watched run around as well as all of our prototype scuttle
[2:09] as well as all of our prototype scuttle
[2:09] as well as all of our prototype scuttle docking scripts and the
[2:11] docking scripts and the
[2:11] docking scripts and the scuttle battery life and id management
[2:13] scuttle battery life and id management
[2:13] scuttle battery life and id management gui scripts that are in the charging
[2:14] gui scripts that are in the charging
[2:14] gui scripts that are in the charging station and on the scuttle itself
[2:19] these are our initial functional
[2:19] these are our initial functional requirements that we had we've met all
[2:21] requirements that we had we've met all
[2:21] requirements that we had we've met all of them
[2:22] of them
[2:22] of them we just displayed them in the demo and
[2:24] we just displayed them in the demo and
[2:24] we just displayed them in the demo and now we'll go into
[2:25] now we'll go into
[2:25] now we'll go into the design of the station as well as the
[2:27] the design of the station as well as the
[2:27] the design of the station as well as the scuttle
[2:28] scuttle
[2:28] scuttle on board module and talk about how we
[2:30] on board module and talk about how we
[2:30] on board module and talk about how we solved the
[2:31] solved the
[2:31] solved the problems we ran into as well as clear
[2:34] problems we ran into as well as clear
[2:34] problems we ran into as well as clear projects
[2:36] projects
[2:36] projects so we did i didn't expect it to be
[2:39] so we did i didn't expect it to be
[2:39] so we did i didn't expect it to be as difficult as it was but we do have
[2:41] as difficult as it was but we do have
[2:41] as difficult as it was but we do have this setup and we'll document it as well
[2:43] this setup and we'll document it as well
[2:43] this setup and we'll document it as well how you can set up your script so that
[2:44] how you can set up your script so that
[2:44] how you can set up your script so that runs whenever you plug in the station so
[2:46] runs whenever you plug in the station so
[2:46] runs whenever you plug in the station so you just plug in the station you don't
[2:47] you just plug in the station you don't
[2:47] you just plug in the station you don't even have to connect to it it's already
[2:49] even have to connect to it it's already
[2:49] even have to connect to it it's already doing its thing you don't have to run
[2:50] doing its thing you don't have to run
[2:50] doing its thing you don't have to run any code it's already running you're
[2:51] any code it's already running you're
[2:51] any code it's already running you're good to go and it remembers its client
[2:53] good to go and it remembers its client
[2:53] good to go and it remembers its client id through power
[2:54] id through power
[2:54] id through power recycle it does three power cycles
[2:56] recycle it does three power cycles
[2:56] recycle it does three power cycles where's that store it's stored inside
[2:57] where's that store it's stored inside
[2:58] where's that store it's stored inside the file itself
[2:59] the file itself
[2:59] the file itself on the on the sd card okay
[3:05] okay so this is our docking sequence
[3:05] okay so this is our docking sequence flowchart um
[3:06] flowchart um
[3:06] flowchart um whenever the script is started it's
[3:08] whenever the script is started it's
[3:08] whenever the script is started it's going to ascertain the distance that it
[3:10] going to ascertain the distance that it
[3:10] going to ascertain the distance that it needs to get to the station so it'll
[3:12] needs to get to the station so it'll
[3:12] needs to get to the station so it'll turn and find the station
[3:13] turn and find the station
[3:14] turn and find the station if it's too close or too far it'll
[3:15] if it's too close or too far it'll
[3:15] if it's too close or too far it'll adjust um
[3:18] adjust um
[3:18] adjust um to in order to get in front of the
[3:21] to in order to get in front of the
[3:21] to in order to get in front of the station
[3:22] station
[3:22] station so whenever it is within a certain
[3:24] so whenever it is within a certain
[3:24] so whenever it is within a certain target heading it's going to
[3:26] target heading it's going to
[3:26] target heading it's going to face the station again ascertain the
[3:29] face the station again ascertain the
[3:29] face the station again ascertain the distance
[3:30] distance
[3:30] distance make sure it's not too close or too far
[3:33] make sure it's not too close or too far
[3:33] make sure it's not too close or too far and then
[3:33] and then
[3:33] and then it's going to get in front of the
[3:34] it's going to get in front of the
[3:34] it's going to get in front of the station maintaining
[3:36] station maintaining
[3:36] station maintaining the target heading as it gets closer to
[3:40] the target heading as it gets closer to
[3:40] the target heading as it gets closer to the station
[3:40] the station
[3:40] the station when it's in front of the station it's
[3:42] when it's in front of the station it's
[3:42] when it's in front of the station it's going to
[3:45] going to
[3:45] going to assess how far it is from the station
[3:48] assess how far it is from the station
[3:48] assess how far it is from the station and continue driving slowly forward on
[3:51] and continue driving slowly forward on
[3:51] and continue driving slowly forward on uh and closing theta offset
[3:53] uh and closing theta offset
[3:54] uh and closing theta offset um until it reaches the station when it
[3:55] um until it reaches the station when it
[3:55] um until it reaches the station when it detects that
[3:57] detects that
[3:57] detects that it's there and the radius of the
[4:00] it's there and the radius of the
[4:00] it's there and the radius of the target is large enough it'll stop and
[4:03] target is large enough it'll stop and
[4:03] target is large enough it'll stop and then it's going to keep checking
[4:05] then it's going to keep checking
[4:05] then it's going to keep checking area's going to check if it's batteries
[4:06] area's going to check if it's batteries
[4:06] area's going to check if it's batteries are charging if it's not it's going to
[4:08] are charging if it's not it's going to
[4:08] are charging if it's not it's going to back up
[4:10] back up
[4:10] back up and then re-dock and then once it's
[4:14] and then re-dock and then once it's
[4:14] and then re-dock and then once it's docked correctly
[4:16] docked correctly
[4:16] docked correctly it's going to continually ascertain the
[4:19] it's going to continually ascertain the
[4:19] it's going to continually ascertain the battery
[4:19] battery
[4:20] battery levels once the batteries are full
[4:23] levels once the batteries are full
[4:23] levels once the batteries are full it's going to exit the script so on a
[4:25] it's going to exit the script so on a
[4:25] it's going to exit the script so on a high level
[4:26] high level
[4:26] high level until it docks successfully it will
[4:28] until it docks successfully it will
[4:28] until it docks successfully it will continue to dock
[4:31] continue to dock
[4:31] continue to dock sorry one thing mentioned here in theta
[4:33] sorry one thing mentioned here in theta
[4:33] sorry one thing mentioned here in theta offset is defined
[4:34] offset is defined
[4:34] offset is defined as the difference david's familiar with
[4:35] as the difference david's familiar with
[4:35] as the difference david's familiar with this that offset is defined as the
[4:38] this that offset is defined as the
[4:38] this that offset is defined as the difference
[4:38] difference
[4:38] difference as the angle between the center of the
[4:40] as the angle between the center of the
[4:40] as the angle between the center of the scuttle's vision and the target in its
[4:42] scuttle's vision and the target in its
[4:42] scuttle's vision and the target in its vision so if it can see the target and
[4:44] vision so if it can see the target and
[4:44] vision so if it can see the target and it's peripheral over here
[4:45] it's peripheral over here
[4:45] it's peripheral over here it wants to be sure to close that angle
[4:48] it wants to be sure to close that angle
[4:48] it wants to be sure to close that angle so that it's constantly facing it and
[4:49] so that it's constantly facing it and
[4:49] so that it's constantly facing it and that's what you see when it drives
[4:50] that's what you see when it drives
[4:50] that's what you see when it drives forward where it kind of
[4:51] forward where it kind of
[4:51] forward where it kind of wiggles its way that's uh that's what
[4:53] wiggles its way that's uh that's what
[4:53] wiggles its way that's uh that's what it's doing so that's that part so i
[4:55] it's doing so that's that part so i
[4:55] it's doing so that's that part so i tried to define that later
[4:57] tried to define that later
[4:57] tried to define that later this is the charging station enclosure
[4:59] this is the charging station enclosure
[4:59] this is the charging station enclosure design um as you can tell and as you've
[5:01] design um as you can tell and as you've
[5:01] design um as you can tell and as you've seen before the demo
[5:02] seen before the demo
[5:02] seen before the demo um these pads are spaced out to match
[5:04] um these pads are spaced out to match
[5:04] um these pads are spaced out to match the receiver pads on onboard module
[5:06] the receiver pads on onboard module
[5:06] the receiver pads on onboard module this is the back panel right here you
[5:08] this is the back panel right here you
[5:08] this is the back panel right here you can see where we've mounted both
[5:09] can see where we've mounted both
[5:09] can see where we've mounted both the beaglebone blue and the charging
[5:11] the beaglebone blue and the charging
[5:11] the beaglebone blue and the charging station pcb
[5:13] station pcb
[5:13] station pcb and the distances um from the side panel
[5:15] and the distances um from the side panel
[5:15] and the distances um from the side panel where those are those are conveniently
[5:17] where those are those are conveniently
[5:17] where those are those are conveniently placed so they can easily be plugged
[5:18] placed so they can easily be plugged
[5:18] placed so they can easily be plugged into both receiver pads
[5:19] into both receiver pads
[5:19] into both receiver pads as far as pcb goes and the rfid reader
[5:21] as far as pcb goes and the rfid reader
[5:21] as far as pcb goes and the rfid reader for the big bone blue
[5:25] for the big bone blue
[5:25] for the big bone blue back as well
[5:31] so this is the mounting design for the
[5:31] so this is the mounting design for the onboard module
[5:32] onboard module
[5:32] onboard module after a lot of conversations and
[5:33] after a lot of conversations and
[5:34] after a lot of conversations and different iterations the main thing is
[5:35] different iterations the main thing is
[5:36] different iterations the main thing is that we want to make sure
[5:37] that we want to make sure
[5:37] that we want to make sure that this pcb fit conveniently on within
[5:39] that this pcb fit conveniently on within
[5:39] that this pcb fit conveniently on within the scuttle's existing architecture so
[5:41] the scuttle's existing architecture so
[5:41] the scuttle's existing architecture so we have it snapped to this
[5:42] we have it snapped to this
[5:42] we have it snapped to this rear the rear side of this front rail
[5:44] rear the rear side of this front rail
[5:44] rear the rear side of this front rail here which provides very easy
[5:45] here which provides very easy
[5:45] here which provides very easy connections to the bigger one blue
[5:47] connections to the bigger one blue
[5:47] connections to the bigger one blue and to the battery pack as well but
[5:49] and to the battery pack as well but
[5:49] and to the battery pack as well but additionally it allows us to plug in
[5:50] additionally it allows us to plug in
[5:50] additionally it allows us to plug in these the wireless receiver pads that
[5:52] these the wireless receiver pads that
[5:52] these the wireless receiver pads that are on the front their cord comes
[5:54] are on the front their cord comes
[5:54] are on the front their cord comes underneath and can easily plug into the
[5:55] underneath and can easily plug into the
[5:56] underneath and can easily plug into the back
[5:56] back
[5:56] back of the pcb there the panel on the front
[5:59] of the pcb there the panel on the front
[5:59] of the pcb there the panel on the front and turn it around so you can see
[6:01] and turn it around so you can see
[6:01] and turn it around so you can see the panel on the front you can see in
[6:02] the panel on the front you can see in
[6:02] the panel on the front you can see in the image is designed to hold the
[6:05] the image is designed to hold the
[6:05] the image is designed to hold the and it you can't see it because it's
[6:06] and it you can't see it because it's
[6:06] and it you can't see it because it's covered up but there are lines here on
[6:07] covered up but there are lines here on
[6:07] covered up but there are lines here on the etched on this acrylic
[6:09] the etched on this acrylic
[6:09] the etched on this acrylic which define where you need to place
[6:10] which define where you need to place
[6:10] which define where you need to place your receiver pads that they line up
[6:11] your receiver pads that they line up
[6:11] your receiver pads that they line up with the station
[6:12] with the station
[6:12] with the station and then it also has a spot for your
[6:14] and then it also has a spot for your
[6:14] and then it also has a spot for your rfid tag as well whatever rfid tag you
[6:16] rfid tag as well whatever rfid tag you
[6:16] rfid tag as well whatever rfid tag you may be using to identify that scuttle
[6:19] may be using to identify that scuttle
[6:19] may be using to identify that scuttle and so that's how our our mounting
[6:21] and so that's how our our mounting
[6:21] and so that's how our our mounting process takes place oh sorry also
[6:23] process takes place oh sorry also
[6:23] process takes place oh sorry also this front panel i don't really want to
[6:25] this front panel i don't really want to
[6:25] this front panel i don't really want to take it off right now but
[6:26] take it off right now but
[6:26] take it off right now but the front panel can slide off easily
[6:28] the front panel can slide off easily
[6:28] the front panel can slide off easily with these clips on the side right here
[6:30] with these clips on the side right here
[6:30] with these clips on the side right here that you see so you can just slide it on
[6:31] that you see so you can just slide it on
[6:31] that you see so you can just slide it on and off and so you're either ready to
[6:33] and off and so you're either ready to
[6:33] and off and so you're either ready to wirelessly
[6:34] wirelessly
[6:34] wirelessly charge or not however you want to go so
[6:35] charge or not however you want to go so
[6:35] charge or not however you want to go so i don't see any screws or snaps how does
[6:37] i don't see any screws or snaps how does
[6:37] i don't see any screws or snaps how does the printed circuit board matter to that
[6:39] the printed circuit board matter to that
[6:39] the printed circuit board matter to that rail
[6:39] rail
[6:39] rail oh sorry you don't see it um if you look
[6:42] oh sorry you don't see it um if you look
[6:42] oh sorry you don't see it um if you look behind our libraries and begin
[6:44] behind our libraries and begin
[6:44] behind our libraries and begin connecting to cayenne using
[6:46] connecting to cayenne using
[6:46] connecting to cayenne using its unique client id then first starting
[6:50] its unique client id then first starting
[6:50] its unique client id then first starting start scanning for an rfid tag there is
[6:52] start scanning for an rfid tag there is
[6:52] start scanning for an rfid tag there is the rfid tag
[6:53] the rfid tag
[6:53] the rfid tag we then compare that scan our rfid tag
[6:56] we then compare that scan our rfid tag
[6:56] we then compare that scan our rfid tag to our list of skull ids
[6:57] to our list of skull ids
[6:57] to our list of skull ids if it's recognized we want to match our
[7:00] if it's recognized we want to match our
[7:00] if it's recognized we want to match our status to that rfid tag
[7:02] status to that rfid tag
[7:02] status to that rfid tag um if uh if the tag is not recognized we
[7:05] um if uh if the tag is not recognized we
[7:05] um if uh if the tag is not recognized we want to add a new widget
[7:07] want to add a new widget
[7:07] want to add a new widget and add it to our list of recognized ids
[7:09] and add it to our list of recognized ids
[7:09] and add it to our list of recognized ids and then update the status accordingly
[7:11] and then update the status accordingly
[7:11] and then update the status accordingly if there is an rfrd tag we set our
[7:13] if there is an rfrd tag we set our
[7:13] if there is an rfrd tag we set our status to vacant and we only update our
[7:15] status to vacant and we only update our
[7:15] status to vacant and we only update our status upon
[7:16] status upon
[7:16] status upon a status change how do you set up the
[7:19] a status change how do you set up the
[7:19] a status change how do you set up the unique id
[7:21] unique id
[7:21] unique id the unique ideas for charging station
[7:25] the unique ideas for charging station
[7:25] the unique ideas for charging station um connect to cayenne using
[7:28] um connect to cayenne using
[7:28] um connect to cayenne using client id yes how do you set that up so
[7:31] client id yes how do you set that up so
[7:31] client id yes how do you set that up so you would set that up um whenever you
[7:33] you would set that up um whenever you
[7:33] you would set that up um whenever you create your account in cayenne
[7:36] create your account in cayenne
[7:36] create your account in cayenne you add a new device and when you add a
[7:38] you add a new device and when you add a
[7:38] you add a new device and when you add a new device
[7:39] new device
[7:39] new device kind will give you that client id you
[7:42] kind will give you that client id you
[7:42] kind will give you that client id you then go into
[7:43] then go into
[7:43] then go into your code and you have to copy paste
[7:44] your code and you have to copy paste
[7:44] your code and you have to copy paste that client id into the code and um in
[7:47] that client id into the code and um in
[7:47] that client id into the code and um in our l1 cayenne
[7:48] our l1 cayenne
[7:48] our l1 cayenne um script that we've created and is that
[7:51] um script that we've created and is that
[7:51] um script that we've created and is that process documented in
[7:53] process documented in
[7:53] process documented in it is it'll be in the user manual and
[7:55] it is it'll be in the user manual and
[7:55] it is it'll be in the user manual and i've run it i've already started on it
[7:56] i've run it i've already started on it
[7:56] i've run it i've already started on it perfect
[7:58] perfect
[7:58] perfect our customer and what he expects to see
[8:00] our customer and what he expects to see
[8:00] our customer and what he expects to see from the project and what he wants to
[8:01] from the project and what he wants to
[8:02] from the project and what he wants to see from the autonomous docking part as
[8:03] see from the autonomous docking part as
[8:03] see from the autonomous docking part as well as for the charging station itself
[8:05] well as for the charging station itself
[8:05] well as for the charging station itself additionally we wanted to make sure that
[8:06] additionally we wanted to make sure that
[8:06] additionally we wanted to make sure that this platform was easy to use and move
[8:07] this platform was easy to use and move
[8:08] this platform was easy to use and move around so the charging station is pretty
[8:09] around so the charging station is pretty
[8:09] around so the charging station is pretty simple
[8:09] simple
[8:09] simple you can lift this thing up with one hand
[8:11] you can lift this thing up with one hand
[8:11] you can lift this thing up with one hand no problem and
[8:13] no problem and
[8:13] no problem and don't lose your monkey it's very
[8:14] don't lose your monkey it's very
[8:14] don't lose your monkey it's very important
[8:18] and also we want to make sure that the
[8:18] and also we want to make sure that the scuttle can be modularly equipped with
[8:20] scuttle can be modularly equipped with
[8:20] scuttle can be modularly equipped with the onboard components so that the
[8:22] the onboard components so that the
[8:22] the onboard components so that the student can just
[8:23] student can just
[8:23] student can just attach the parts assuming they're
[8:25] attach the parts assuming they're
[8:25] attach the parts assuming they're already made for them they can just
[8:26] already made for them they can just
[8:26] already made for them they can just attach the equipment
[8:27] attach the equipment
[8:27] attach the equipment power the charging station run the code
[8:29] power the charging station run the code
[8:29] power the charging station run the code good to go
[8:30] good to go
[8:30] good to go so that's where those performance specs
[8:31] so that's where those performance specs
[8:31] so that's where those performance specs came is the monkey included in the
[8:32] came is the monkey included in the
[8:32] came is the monkey included in the delivery
[8:33] delivery
[8:33] delivery unfortunately not um he uh he's very
[8:36] unfortunately not um he uh he's very
[8:36] unfortunately not um he uh he's very crucial i don't think we can leave him
[8:37] crucial i don't think we can leave him
[8:37] crucial i don't think we can leave him behind
[8:39] behind
[8:39] behind um so that was the schematic for the
[8:41] um so that was the schematic for the
[8:41] um so that was the schematic for the charging station pcb it's very simple
[8:42] charging station pcb it's very simple
[8:42] charging station pcb it's very simple once again we're just taking in power
[8:43] once again we're just taking in power
[8:44] once again we're just taking in power from a barrel jack
[8:44] from a barrel jack
[8:44] from a barrel jack through the wall here as you see here um
[8:47] through the wall here as you see here um
[8:47] through the wall here as you see here um and then supplying that through usb
[8:48] and then supplying that through usb
[8:48] and then supplying that through usb connections to the beaglebone blue and
[8:50] connections to the beaglebone blue and
[8:50] connections to the beaglebone blue and our three
[8:51] our three
[8:51] our three wireless space charging pads the
[8:52] wireless space charging pads the
[8:52] wireless space charging pads the important thing is that this
[8:54] important thing is that this
[8:54] important thing is that this circuit board is designed to have enough
[8:56] circuit board is designed to have enough
[8:56] circuit board is designed to have enough traces that are big enough it's actually
[8:58] traces that are big enough it's actually
[8:58] traces that are big enough it's actually just two large planes
[8:59] just two large planes
[8:59] just two large planes so that current can flow very easily we
[9:01] so that current can flow very easily we
[9:01] so that current can flow very easily we know that these charging pads
[9:02] know that these charging pads
[9:02] know that these charging pads individually can take about
[9:04] individually can take about
[9:04] individually can take about two amps each at most um so we need to
[9:06] two amps each at most um so we need to
[9:06] two amps each at most um so we need to be able to supply at least six amps to
[9:08] be able to supply at least six amps to
[9:08] be able to supply at least six amps to those guys as well and obviously still
[9:09] those guys as well and obviously still
[9:09] those guys as well and obviously still power the beaglebone below
[9:15] and then looking to the schematic for
[9:15] and then looking to the schematic for the onboard module here and i'll
[9:16] the onboard module here and i'll
[9:16] the onboard module here and i'll bring this into view so you can see it
[9:19] bring this into view so you can see it
[9:19] bring this into view so you can see it um it's mounted on the back right here
[9:21] um it's mounted on the back right here
[9:21] um it's mounted on the back right here this uh this schematic was designed so
[9:24] this uh this schematic was designed so
[9:24] this uh this schematic was designed so that we can
[9:25] that we can
[9:25] that we can very easily and simply and simply
[9:27] very easily and simply and simply
[9:27] very easily and simply and simply provide power from the receiver pads to
[9:29] provide power from the receiver pads to
[9:29] provide power from the receiver pads to the battery pack
[9:30] the battery pack
[9:30] the battery pack as well as control it using the scuttle
[9:32] as well as control it using the scuttle
[9:32] as well as control it using the scuttle so this schematic flows from the top
[9:33] so this schematic flows from the top
[9:33] so this schematic flows from the top down you have power coming into the top
[9:35] down you have power coming into the top
[9:35] down you have power coming into the top managed by the relays here in the center
[9:37] managed by the relays here in the center
[9:37] managed by the relays here in the center controlled by a gpio
[9:39] controlled by a gpio
[9:39] controlled by a gpio low side switching fat the gpio pin
[9:40] low side switching fat the gpio pin
[9:40] low side switching fat the gpio pin comes in from the beaglebone blue
[9:42] comes in from the beaglebone blue
[9:42] comes in from the beaglebone blue and then your lipo connection to supply
[9:43] and then your lipo connection to supply
[9:43] and then your lipo connection to supply power to the batteries
[9:46] power to the batteries
[9:46] power to the batteries the design of the pcb was mostly
[9:47] the design of the pcb was mostly
[9:48] the design of the pcb was mostly governed by we knew we needed it to fit
[9:49] governed by we knew we needed it to fit
[9:49] governed by we knew we needed it to fit on the front rail
[9:50] on the front rail
[9:50] on the front rail of the charging of the skull robot
[9:52] of the charging of the skull robot
[9:52] of the charging of the skull robot itself so its dimensions our designs
[9:54] itself so its dimensions our designs
[9:54] itself so its dimensions our designs that it fits snugly underneath here so
[9:56] that it fits snugly underneath here so
[9:56] that it fits snugly underneath here so it's about even with the surface of this
[9:58] it's about even with the surface of this
[9:58] it's about even with the surface of this and can be and the back side of it which
[10:00] and can be and the back side of it which
[10:00] and can be and the back side of it which is not showing the backs of it has clear
[10:01] is not showing the backs of it has clear
[10:01] is not showing the backs of it has clear spots for mounting the little clips
[10:03] spots for mounting the little clips
[10:03] spots for mounting the little clips which are what
[10:03] which are what
[10:04] which are what actually hold it onto the front rail and
[10:06] actually hold it onto the front rail and
[10:06] actually hold it onto the front rail and then again the
[10:08] then again the
[10:08] then again the micro usbs were intentionally placed
[10:09] micro usbs were intentionally placed
[10:09] micro usbs were intentionally placed spaced out far apart along the bottom of
[10:11] spaced out far apart along the bottom of
[10:11] spaced out far apart along the bottom of the pad so that the receiver pads on the
[10:13] the pad so that the receiver pads on the
[10:13] the pad so that the receiver pads on the front can snap in on the underside
[10:15] front can snap in on the underside
[10:15] front can snap in on the underside and your gpio pin is very prominently
[10:17] and your gpio pin is very prominently
[10:17] and your gpio pin is very prominently located so you can very easily plug in
[10:19] located so you can very easily plug in
[10:19] located so you can very easily plug in from the bagel bone blue
[10:20] from the bagel bone blue
[10:20] from the bagel bone blue and your lipo connection again very
[10:22] and your lipo connection again very
[10:22] and your lipo connection again very easily accessible and
[10:23] easily accessible and
[10:23] easily accessible and closest to the battery pack so you can
[10:24] closest to the battery pack so you can
[10:24] closest to the battery pack so you can have minimal wires crossing over
[10:26] have minimal wires crossing over
[10:26] have minimal wires crossing over everything
[10:28] everything
[10:28] everything so going into the flow chart for our
[10:30] so going into the flow chart for our
[10:30] so going into the flow chart for our charging station um
[10:33] charging station um
[10:33] charging station um yeah so this is our number two
[10:37] yeah so this is our number two
[10:37] yeah so this is our number two cc scale two lights up uh-huh it's no
[10:39] cc scale two lights up uh-huh it's no
[10:39] cc scale two lights up uh-huh it's no longer vacant
[10:41] longer vacant
[10:41] longer vacant go ahead and throw on number one which
[10:44] go ahead and throw on number one which
[10:44] go ahead and throw on number one which is the blue one yeah so this this is
[10:45] is the blue one yeah so this this is
[10:45] is the blue one yeah so this this is scuttle
[10:45] scuttle
[10:46] scuttle one let's just scuttle whenever one
[10:49] one let's just scuttle whenever one
[10:49] one let's just scuttle whenever one lights up it's no longer vacant
[10:55] all right and show them with the new tag
[10:55] all right and show them with the new tag we got a new student
[10:56] we got a new student
[10:56] we got a new student something unrecognized tag it hasn't
[10:59] something unrecognized tag it hasn't
[10:59] something unrecognized tag it hasn't been registered yet
[11:04] and it'll sell you a new widget so then
[11:04] and it'll sell you a new widget so then from there you can
[11:06] from there you can
[11:06] from there you can access your new widget if it'll let me
[11:08] access your new widget if it'll let me
[11:08] access your new widget if it'll let me sorry
[11:09] sorry
[11:09] sorry and go into the settings you can name it
[11:11] and go into the settings you can name it
[11:11] and go into the settings you can name it whatever you want
[11:13] whatever you want
[11:13] whatever you want i will name it schedule number three
[11:20] number three and you can change it to
[11:20] number three and you can change it to whichever
[11:22] whichever
[11:22] whichever um i'm sorry whichever icon you would
[11:24] um i'm sorry whichever icon you would
[11:24] um i'm sorry whichever icon you would like and i always prefer
[11:28] like and i always prefer
[11:28] like and i always prefer find it
[11:33] so there you go so now if he ever scans
[11:33] so there you go so now if he ever scans it again
[11:34] it again
[11:34] it again can you scan number three again yeah
[11:36] can you scan number three again yeah
[11:36] can you scan number three again yeah yeah
[11:38] yeah
[11:38] yeah it is always congruent and will always
[11:39] it is always congruent and will always
[11:40] it is always congruent and will always update to that widget
[11:42] update to that widget
[11:42] update to that widget super

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
