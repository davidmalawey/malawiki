---
title: "Program a PLC with Conveyor, Arduino and Industrial Robot"
url: "https://www.youtube.com/watch?v=30GM4m-Lyec"
video_id: "30GM4m-Lyec"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2021-09-29
duration: "22:00"
duration_sec: 1320
views: 1699
likes: 33
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/30GM4m-Lyec/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1062
chapters_count: 10
has_description: true
has_comments: false
---

## Description

MXET 400 conveyor demo. Learn more on the github:
https://www.github.com/dmalawey/MXET-Conveyor-2021

This demo includes the industrial PLC, Arduino, sensors, actuators, UR-3e robots, and conveyor.

CHAPTERS:
00:00 System Documentation 
02:00 System Power Distribution
06:22 CAD models PLC
07:17 CAD conveyor & brackets
07:33 Programming the PLC
12:18 Compiling C++ Code
14:40 Sensors & VL53 function
16:55 Arduino tabs & headers
18:44 Arduino sensor program
21:38 Arduino (find the files)

## Chapters

- 0:00 System Documentation
- 2:00 System Power Distribution
- 6:22 CAD models PLC
- 7:17 CAD conveyor & brackets
- 7:33 Programming the PLC
- 12:18 Compiling C++ Code
- 14:40 Sensors & VL53 function
- 16:55 Arduino tabs & headers
- 18:44 Arduino sensor program
- 21:38 Arduino (find the files)

## Transcript

[0:02] hi everybody i'm david and i'm here
[0:02] hi everybody i'm david and i'm here today to share with you an overview of
[0:03] today to share with you an overview of
[0:03] today to share with you an overview of our system that's the new conveyor demo
[0:06] our system that's the new conveyor demo
[0:06] our system that's the new conveyor demo in mechatronics and the system is
[0:08] in mechatronics and the system is
[0:08] in mechatronics and the system is fascinating because it it converges plc
[0:12] fascinating because it it converges plc
[0:12] fascinating because it it converges plc functionality as well as embedded
[0:14] functionality as well as embedded
[0:14] functionality as well as embedded microcontrollers and the conveyor system
[0:16] microcontrollers and the conveyor system
[0:16] microcontrollers and the conveyor system and industrial robotics so the
[0:19] and industrial robotics so the
[0:19] and industrial robotics so the components of the video will go as
[0:21] components of the video will go as
[0:21] components of the video will go as follows
[0:23] follows
[0:23] follows we have the uh the documentation for the
[0:25] we have the uh the documentation for the
[0:25] we have the uh the documentation for the whole system overall
[0:27] whole system overall
[0:27] whole system overall the safety
[0:29] the safety
[0:29] the safety comments and how the power is routed
[0:31] comments and how the power is routed
[0:31] comments and how the power is routed throughout the system
[0:33] throughout the system
[0:33] throughout the system where to find the cad files for the plc
[0:35] where to find the cad files for the plc
[0:35] where to find the cad files for the plc controller as well as the other brackets
[0:39] controller as well as the other brackets
[0:39] controller as well as the other brackets programming the plc which we do with
[0:41] programming the plc which we do with
[0:41] programming the plc which we do with productivity blocks the program
[0:43] productivity blocks the program
[0:43] productivity blocks the program breakdown
[0:44] breakdown
[0:44] breakdown in the sequence of the program
[0:46] in the sequence of the program
[0:46] in the sequence of the program then going into how the pins are mapped
[0:50] then going into how the pins are mapped
[0:50] then going into how the pins are mapped that is
[0:51] that is
[0:51] that is the pins are mapped from the software to
[0:54] the pins are mapped from the software to
[0:54] the pins are mapped from the software to the hardware
[0:56] the hardware
[0:56] the hardware then compiling the c plus plus code
[0:58] then compiling the c plus plus code
[0:58] then compiling the c plus plus code which we we produce c from productivity
[1:02] which we we produce c from productivity
[1:02] which we we produce c from productivity blocks and we'll upload the code to the
[1:04] blocks and we'll upload the code to the
[1:04] blocks and we'll upload the code to the plc with arduino
[1:06] plc with arduino
[1:06] plc with arduino we're going to go into sensors where we
[1:08] we're going to go into sensors where we
[1:08] we're going to go into sensors where we look at the
[1:09] look at the
[1:09] look at the distance sensor functionality and the
[1:12] distance sensor functionality and the
[1:12] distance sensor functionality and the connections between the sensor and the
[1:14] connections between the sensor and the
[1:14] connections between the sensor and the arduino board
[1:15] arduino board
[1:15] arduino board then we'll go into the arduino software
[1:17] then we'll go into the arduino software
[1:17] then we'll go into the arduino software where we look at the tabs the
[1:20] where we look at the tabs the
[1:20] where we look at the tabs the the distance sensor program routine
[1:22] the distance sensor program routine
[1:22] the distance sensor program routine and where to find all of those files as
[1:25] and where to find all of those files as
[1:25] and where to find all of those files as well so that you can basically reproduce
[1:27] well so that you can basically reproduce
[1:27] well so that you can basically reproduce the project after you've seen this video
[1:29] the project after you've seen this video
[1:29] the project after you've seen this video and you have access to the resources
[1:32] and you have access to the resources
[1:32] and you have access to the resources all the documentation is found here at
[1:35] all the documentation is found here at
[1:35] all the documentation is found here at this github repository and the best
[1:37] this github repository and the best
[1:38] this github repository and the best place to start is by opening the
[1:39] place to start is by opening the
[1:39] place to start is by opening the documentation folder and going to these
[1:41] documentation folder and going to these
[1:41] documentation folder and going to these slides that contain
[1:44] slides that contain
[1:44] slides that contain not only the slides that i refer to here
[1:46] not only the slides that i refer to here
[1:46] not only the slides that i refer to here in this video but also other wiring
[1:48] in this video but also other wiring
[1:48] in this video but also other wiring diagrams and
[1:51] diagrams and
[1:51] diagrams and code descriptions and logic tables that
[1:54] code descriptions and logic tables that
[1:54] code descriptions and logic tables that describe how the demo works so that you
[1:57] describe how the demo works so that you
[1:57] describe how the demo works so that you can reverse engineer everything that
[1:58] can reverse engineer everything that
[1:58] can reverse engineer everything that you'd like to work on
[2:02] you'd like to work on
[2:02] you'd like to work on the power comes into the system for this
[2:04] the power comes into the system for this
[2:04] the power comes into the system for this demo all starting with this e-stop which
[2:06] demo all starting with this e-stop which
[2:06] demo all starting with this e-stop which is a push-pull type there's no switching
[2:09] is a push-pull type there's no switching
[2:09] is a push-pull type there's no switching there's no rotating
[2:11] there's no rotating
[2:11] there's no rotating the power is coming from the wall at 120
[2:14] the power is coming from the wall at 120
[2:14] the power is coming from the wall at 120 volts and it passes through this east up
[2:16] volts and it passes through this east up
[2:16] volts and it passes through this east up first and then it comes over to the
[2:18] first and then it comes over to the
[2:18] first and then it comes over to the power switch here
[2:20] power switch here
[2:20] power switch here and you should see no led there and no
[2:23] and you should see no led there and no
[2:23] and you should see no led there and no led
[2:24] led
[2:24] led on these other two modules the conveyor
[2:26] on these other two modules the conveyor
[2:26] on these other two modules the conveyor module and the power supply for 24 volts
[2:30] module and the power supply for 24 volts
[2:30] module and the power supply for 24 volts then when we activate uh we pull this
[2:33] then when we activate uh we pull this
[2:33] then when we activate uh we pull this then we have 120 volts going back to
[2:36] then we have 120 volts going back to
[2:36] then we have 120 volts going back to this
[2:37] this
[2:37] this and
[2:38] and
[2:38] and the
[2:38] the
[2:38] the two cables come over to our
[2:41] two cables come over to our
[2:41] two cables come over to our system on the left and then the third
[2:42] system on the left and then the third
[2:42] system on the left and then the third cable or more goes to the uar robot or
[2:46] cable or more goes to the uar robot or
[2:46] cable or more goes to the uar robot or second ur robot
[2:48] second ur robot
[2:48] second ur robot so let me trace the power into uh first
[2:51] so let me trace the power into uh first
[2:51] so let me trace the power into uh first of all 120 volts is coming into this
[2:54] of all 120 volts is coming into this
[2:54] of all 120 volts is coming into this uh dorner conveyor controller and that's
[2:56] uh dorner conveyor controller and that's
[2:56] uh dorner conveyor controller and that's powering this stepper motor and driving
[2:59] powering this stepper motor and driving
[2:59] powering this stepper motor and driving the conveyor
[3:00] the conveyor
[3:00] the conveyor then secondly we have 120 volts um
[3:04] then secondly we have 120 volts um
[3:04] then secondly we have 120 volts um neutral at white and hot on the black
[3:07] neutral at white and hot on the black
[3:07] neutral at white and hot on the black line coming into this 24 volt power
[3:09] line coming into this 24 volt power
[3:09] line coming into this 24 volt power supply and if this light comes on that
[3:12] supply and if this light comes on that
[3:12] supply and if this light comes on that means the power is active coming in and
[3:15] means the power is active coming in and
[3:15] means the power is active coming in and then you have 24 volts coming out of
[3:17] then you have 24 volts coming out of
[3:17] then you have 24 volts coming out of there and going into these junctions
[3:20] there and going into these junctions
[3:20] there and going into these junctions the way this is laid out you can notice
[3:23] the way this is laid out you can notice
[3:23] the way this is laid out you can notice this horizontal tab that's bridging all
[3:26] this horizontal tab that's bridging all
[3:26] this horizontal tab that's bridging all the connectors on
[3:27] the connectors on
[3:27] the connectors on this block
[3:29] this block
[3:29] this block and this horizontal tab
[3:31] and this horizontal tab
[3:31] and this horizontal tab bridging all these connectors so you
[3:32] bridging all these connectors so you
[3:32] bridging all these connectors so you have ground on the left
[3:34] have ground on the left
[3:34] have ground on the left and hot 24 volts on the right
[3:38] and hot 24 volts on the right
[3:38] and hot 24 volts on the right and let me back up a second when you
[3:40] and let me back up a second when you
[3:40] and let me back up a second when you come from here we are immediately
[3:42] come from here we are immediately
[3:42] come from here we are immediately grounding
[3:43] grounding
[3:44] grounding everything
[3:45] everything
[3:45] everything coming in to this
[3:47] coming in to this
[3:47] coming in to this actual steel frame
[3:49] actual steel frame
[3:49] actual steel frame so the
[3:51] so the
[3:51] so the the green wire is the ground wire
[3:53] the green wire is the ground wire
[3:53] the green wire is the ground wire and it goes into this terminal block
[3:55] and it goes into this terminal block
[3:55] and it goes into this terminal block that's blended green and yellow and that
[3:58] that's blended green and yellow and that
[3:58] that's blended green and yellow and that block is actually grounded to the din
[4:01] block is actually grounded to the din
[4:01] block is actually grounded to the din rail itself
[4:03] rail itself
[4:03] rail itself so
[4:04] so
[4:04] so after you get 24 volts coming into your
[4:06] after you get 24 volts coming into your
[4:06] after you get 24 volts coming into your power blocks then you have 24 volts that
[4:10] power blocks then you have 24 volts that
[4:10] power blocks then you have 24 volts that one
[4:11] one
[4:11] one powers up the p1 am system and two
[4:15] powers up the p1 am system and two
[4:15] powers up the p1 am system and two it powers this
[4:17] it powers this
[4:17] it powers this 24 volt output module and those are
[4:20] 24 volt output module and those are
[4:20] 24 volt output module and those are separately
[4:21] separately
[4:21] separately separately passed
[4:23] separately passed
[4:23] separately passed so this is the the pair of cables going
[4:25] so this is the the pair of cables going
[4:25] so this is the the pair of cables going to the am
[4:26] to the am
[4:26] to the am p1 am and this is the input voltage
[4:30] p1 am and this is the input voltage
[4:30] p1 am and this is the input voltage going into the module that it's driving
[4:33] going into the module that it's driving
[4:33] going into the module that it's driving out coming from the p1am system these uh
[4:37] out coming from the p1am system these uh
[4:37] out coming from the p1am system these uh these blocks are all tied together and
[4:40] these blocks are all tied together and
[4:40] these blocks are all tied together and you have a five volt
[4:42] you have a five volt
[4:42] you have a five volt access to source 5 volts
[4:45] access to source 5 volts
[4:45] access to source 5 volts from the left side on these two pins
[4:47] from the left side on these two pins
[4:47] from the left side on these two pins where green is ground blue is 5 volts
[4:50] where green is ground blue is 5 volts
[4:50] where green is ground blue is 5 volts and we're bridging that over to power
[4:52] and we're bridging that over to power
[4:52] and we're bridging that over to power and esp
[4:53] and esp
[4:53] and esp in the end the esp
[4:55] in the end the esp
[4:55] in the end the esp is only operating as a
[4:58] is only operating as a
[4:58] is only operating as a as a sensor that gives input to the
[5:00] as a sensor that gives input to the
[5:00] as a sensor that gives input to the system and it's getting its power from
[5:02] system and it's getting its power from
[5:02] system and it's getting its power from here
[5:03] here
[5:03] here if you unplug the esp then it should get
[5:06] if you unplug the esp then it should get
[5:06] if you unplug the esp then it should get unplugged
[5:07] unplugged
[5:07] unplugged from
[5:08] from
[5:08] from this
[5:09] this
[5:09] this from this side of the connector
[5:11] from this side of the connector
[5:11] from this side of the connector so that you're isolating the power from
[5:13] so that you're isolating the power from
[5:13] so that you're isolating the power from the wires right away
[5:16] the wires right away
[5:16] the wires right away now we can come back over here
[5:18] now we can come back over here
[5:18] now we can come back over here the other place where this 24 volts goes
[5:21] the other place where this 24 volts goes
[5:21] the other place where this 24 volts goes is indirectly to the relay system
[5:24] is indirectly to the relay system
[5:24] is indirectly to the relay system so the relay is tied with a common
[5:27] so the relay is tied with a common
[5:28] so the relay is tied with a common ground to the same ground as the other
[5:30] ground to the same ground as the other
[5:30] ground to the same ground as the other components
[5:31] components
[5:31] components through this black wire and then the
[5:34] through this black wire and then the
[5:34] through this black wire and then the signals outgoing from this digital 24
[5:37] signals outgoing from this digital 24
[5:37] signals outgoing from this digital 24 volt module
[5:39] volt module
[5:39] volt module send on these black wires to the input 0
[5:42] send on these black wires to the input 0
[5:42] send on these black wires to the input 0 and 1
[5:43] and 1
[5:43] and 1 in order to drive the relays 0 and 1.
[5:47] in order to drive the relays 0 and 1.
[5:47] in order to drive the relays 0 and 1. then those make the contact on these
[5:49] then those make the contact on these
[5:49] then those make the contact on these wires these wires are not part of the
[5:51] wires these wires are not part of the
[5:51] wires these wires are not part of the the power system and when you do
[5:53] the power system and when you do
[5:53] the power system and when you do something like
[5:54] something like
[5:54] something like activate this switch like changing the
[5:57] activate this switch like changing the
[5:57] activate this switch like changing the condition then this is when the
[6:00] condition then this is when the
[6:00] condition then this is when the the p1 am responds
[6:03] the p1 am responds
[6:03] the p1 am responds because it's listening to the switch it
[6:05] because it's listening to the switch it
[6:05] because it's listening to the switch it outputs to this module this module
[6:07] outputs to this module this module
[6:07] outputs to this module this module outputs to the relay and then you see
[6:09] outputs to the relay and then you see
[6:09] outputs to the relay and then you see the led come on
[6:11] the led come on
[6:11] the led come on then you see
[6:12] then you see
[6:12] then you see this light come on and you see the
[6:14] this light come on and you see the
[6:14] this light come on and you see the conveyor moving
[6:15] conveyor moving
[6:15] conveyor moving if we replace the
[6:17] if we replace the
[6:17] if we replace the the can here then it all stops
[6:25] if you want to find the cad models for a
[6:25] if you want to find the cad models for a component then you need to go to the
[6:27] component then you need to go to the
[6:27] component then you need to go to the individual components product page on
[6:29] individual components product page on
[6:29] individual components product page on automationdirect and then you'll find
[6:31] automationdirect and then you'll find
[6:31] automationdirect and then you'll find this button here called 3d cad and that
[6:34] this button here called 3d cad and that
[6:34] this button here called 3d cad and that button takes you down to the bottom of
[6:35] button takes you down to the bottom of
[6:35] button takes you down to the bottom of the page
[6:36] the page
[6:36] the page you can select any file type you want
[6:38] you can select any file type you want
[6:38] you can select any file type you want and download it but
[6:40] and download it but
[6:40] and download it but then you're going to need to fill out
[6:41] then you're going to need to fill out
[6:41] then you're going to need to fill out this form so you can skip that and just
[6:44] this form so you can skip that and just
[6:44] this form so you can skip that and just do with the stp model which is very
[6:47] do with the stp model which is very
[6:47] do with the stp model which is very compatible when you click here it'll
[6:49] compatible when you click here it'll
[6:49] compatible when you click here it'll download right away
[6:50] download right away
[6:50] download right away and then that's definitely compatible
[6:53] and then that's definitely compatible
[6:53] and then that's definitely compatible with solidworks and you can just save
[6:55] with solidworks and you can just save
[6:55] with solidworks and you can just save the file up here as a solid part
[7:02] the cad models for our assembly
[7:02] the cad models for our assembly including the soda can rack and
[7:04] including the soda can rack and
[7:04] including the soda can rack and including the distance sensor rack here
[7:07] including the distance sensor rack here
[7:07] including the distance sensor rack here are found linked from the github you can
[7:10] are found linked from the github you can
[7:10] are found linked from the github you can come down here under cad models and you
[7:12] come down here under cad models and you
[7:12] come down here under cad models and you can find
[7:13] can find
[7:13] can find these links to grab cad
[7:15] these links to grab cad
[7:15] these links to grab cad that'll take you here on grabcad and you
[7:18] that'll take you here on grabcad and you
[7:18] that'll take you here on grabcad and you can click load in 3d viewer for the
[7:20] can click load in 3d viewer for the
[7:20] can click load in 3d viewer for the assemblies make sure it has the parts
[7:22] assemblies make sure it has the parts
[7:22] assemblies make sure it has the parts that you're looking for and then you can
[7:24] that you're looking for and then you can
[7:24] that you're looking for and then you can download the files
[7:26] download the files
[7:26] download the files inside of here the step files or
[7:30] inside of here the step files or
[7:30] inside of here the step files or solidworks files will be available
[7:34] solidworks files will be available
[7:34] solidworks files will be available after installing productivity blocks
[7:36] after installing productivity blocks
[7:36] after installing productivity blocks then start by opening arduino
[7:38] then start by opening arduino
[7:38] then start by opening arduino then make yourself a new file
[7:41] then make yourself a new file
[7:41] then make yourself a new file so that you do not end up overwriting
[7:44] so that you do not end up overwriting
[7:44] so that you do not end up overwriting your old file
[7:47] your old file
[7:47] your old file i'll show you the point where this could
[7:48] i'll show you the point where this could
[7:48] i'll show you the point where this could happen so we go to tools we go to
[7:51] happen so we go to tools we go to
[7:51] happen so we go to tools we go to productivity blocks
[7:54] productivity blocks
[7:54] productivity blocks then open up the file that you're
[7:55] then open up the file that you're
[7:55] then open up the file that you're interested in in our case we have the
[7:57] interested in in our case we have the
[7:57] interested in in our case we have the conveyor demo
[7:59] conveyor demo
[7:59] conveyor demo this is where you'll see the the
[8:01] this is where you'll see the the
[8:01] this is where you'll see the the graphical uh version of your file
[8:05] graphical uh version of your file
[8:05] graphical uh version of your file and you can do verify but before you
[8:07] and you can do verify but before you
[8:07] and you can do verify but before you verify go into arduino because this will
[8:10] verify go into arduino because this will
[8:10] verify go into arduino because this will be used to verify
[8:12] be used to verify
[8:12] be used to verify change your board to p1 am 100
[8:15] change your board to p1 am 100
[8:15] change your board to p1 am 100 and when you click verify this code is
[8:17] and when you click verify this code is
[8:17] and when you click verify this code is going to generate a c plus version of
[8:20] going to generate a c plus version of
[8:20] going to generate a c plus version of the code
[8:21] the code
[8:21] the code and it will ask you to save it as
[8:23] and it will ask you to save it as
[8:23] and it will ask you to save it as something so we're going to call it
[8:26] something so we're going to call it
[8:26] something so we're going to call it conveyor
[8:28] conveyor
[8:28] conveyor test
[8:33] and
[8:33] and all of the functions in this code
[8:37] all of the functions in this code
[8:37] all of the functions in this code are the corresponding
[8:39] are the corresponding
[8:39] are the corresponding actions the corresponding c plus plus
[8:42] actions the corresponding c plus plus
[8:42] actions the corresponding c plus plus code to these functions over here
[8:44] code to these functions over here
[8:44] code to these functions over here and then when you upload that's when it
[8:46] and then when you upload that's when it
[8:46] and then when you upload that's when it will get transferred over to the p1 am
[8:49] will get transferred over to the p1 am
[8:49] will get transferred over to the p1 am system but first it has to be plugged in
[8:54] system but first it has to be plugged in
[8:54] system but first it has to be plugged in our program written in productivity
[8:56] our program written in productivity
[8:56] our program written in productivity blocks essentially fulfills the
[8:58] blocks essentially fulfills the
[8:58] blocks essentially fulfills the conditions here in the truth table
[9:00] conditions here in the truth table
[9:00] conditions here in the truth table regarding the rack being full the object
[9:03] regarding the rack being full the object
[9:03] regarding the rack being full the object being near
[9:04] being near
[9:04] being near and then it moves on to the conveyor
[9:06] and then it moves on to the conveyor
[9:06] and then it moves on to the conveyor actions about which direction will it go
[9:08] actions about which direction will it go
[9:08] actions about which direction will it go and will it go or stop
[9:10] and will it go or stop
[9:10] and will it go or stop so let's look at the yellow blocks here
[9:12] so let's look at the yellow blocks here
[9:12] so let's look at the yellow blocks here in our program
[9:17] so
[9:17] so below the first pink line which is a
[9:19] below the first pink line which is a
[9:19] below the first pink line which is a comment we have the conditions being
[9:22] comment we have the conditions being
[9:22] comment we have the conditions being verified we check the inputs to the p1
[9:25] verified we check the inputs to the p1
[9:25] verified we check the inputs to the p1 am system and then we're going to set a
[9:28] am system and then we're going to set a
[9:28] am system and then we're going to set a a flag low or high the rack full flag
[9:32] a flag low or high the rack full flag
[9:32] a flag low or high the rack full flag will be set low
[9:34] will be set low
[9:34] will be set low under one under one condition of the
[9:35] under one under one condition of the
[9:35] under one under one condition of the switch and the rack full will be flag
[9:38] switch and the rack full will be flag
[9:38] switch and the rack full will be flag will be set high under the other
[9:39] will be set high under the other
[9:39] will be set high under the other condition and the same is taking place
[9:42] condition and the same is taking place
[9:42] condition and the same is taking place for the object near or the object not
[9:45] for the object near or the object not
[9:45] for the object near or the object not near
[9:47] near
[9:47] near then we move on to the actions the
[9:50] then we move on to the actions the
[9:50] then we move on to the actions the conveyor actions are essentially just
[9:52] conveyor actions are essentially just
[9:52] conveyor actions are essentially just dependent on the outputs of the 24 volt
[9:55] dependent on the outputs of the 24 volt
[9:55] dependent on the outputs of the 24 volt module that we attached to our p1 am
[9:58] module that we attached to our p1 am
[9:58] module that we attached to our p1 am system
[9:59] system
[9:59] system so we are sending ones or zeros and
[10:01] so we are sending ones or zeros and
[10:02] so we are sending ones or zeros and though those will
[10:04] though those will
[10:04] though those will subsequently drive
[10:06] subsequently drive
[10:06] subsequently drive the conveyor to
[10:11] go or stop
[10:11] go or stop so
[10:13] so
[10:13] so the way that looks in our productivity
[10:15] the way that looks in our productivity
[10:15] the way that looks in our productivity block system is we're going to set point
[10:19] block system is we're going to set point
[10:19] block system is we're going to set point if the rack full flag is high we'll set
[10:23] if the rack full flag is high we'll set
[10:23] if the rack full flag is high we'll set this point to be low
[10:25] this point to be low
[10:25] this point to be low and the comments here indicate the
[10:26] and the comments here indicate the
[10:26] and the comments here indicate the conveyor will stop
[10:28] conveyor will stop
[10:28] conveyor will stop and the other conditions are regarding
[10:32] and the other conditions are regarding
[10:32] and the other conditions are regarding slot 1.2 we're going to set that low
[10:35] slot 1.2 we're going to set that low
[10:35] slot 1.2 we're going to set that low these green blocks and their
[10:38] these green blocks and their
[10:38] these green blocks and their their other details are essentially just
[10:40] their other details are essentially just
[10:40] their other details are essentially just setting the outputs
[10:41] setting the outputs
[10:42] setting the outputs of that
[10:43] of that
[10:43] of that 24 volt module
[10:45] 24 volt module
[10:45] 24 volt module and then we we accommodate all the
[10:48] and then we we accommodate all the
[10:48] and then we we accommodate all the conditions that we want to accommodate
[10:55] one nuance about productivity blocks
[10:55] one nuance about productivity blocks that you'll notice is sometimes we're
[10:57] that you'll notice is sometimes we're
[10:57] that you'll notice is sometimes we're talking about get point with just a pin
[10:59] talking about get point with just a pin
[11:00] talking about get point with just a pin number and there's other occasions where
[11:02] number and there's other occasions where
[11:02] number and there's other occasions where we set point or get point
[11:04] we set point or get point
[11:04] we set point or get point having a slot and a point uh indicated
[11:07] having a slot and a point uh indicated
[11:08] having a slot and a point uh indicated by the user here's the difference in
[11:10] by the user here's the difference in
[11:10] by the user here's the difference in those two when we just talk about pin
[11:12] those two when we just talk about pin
[11:12] those two when we just talk about pin numbers we're talking about the pins
[11:14] numbers we're talking about the pins
[11:14] numbers we're talking about the pins that are directly tied to the p1am
[11:16] that are directly tied to the p1am
[11:16] that are directly tied to the p1am controller inside of this plastic box so
[11:19] controller inside of this plastic box so
[11:20] controller inside of this plastic box so those are referring to the pins in this
[11:22] those are referring to the pins in this
[11:22] those are referring to the pins in this terminal block here
[11:23] terminal block here
[11:23] terminal block here on the left side of the p1am unit
[11:27] on the left side of the p1am unit
[11:27] on the left side of the p1am unit that means pin d2 that's referenced in
[11:31] that means pin d2 that's referenced in
[11:31] that means pin d2 that's referenced in our productivity blocks program here
[11:33] our productivity blocks program here
[11:33] our productivity blocks program here will correspond to pin d2 or pin 2 on
[11:38] will correspond to pin d2 or pin 2 on
[11:38] will correspond to pin d2 or pin 2 on this terminal block
[11:39] this terminal block
[11:39] this terminal block then when we move to the right side of
[11:41] then when we move to the right side of
[11:41] then when we move to the right side of the p1am we refer to the modules as
[11:45] the p1am we refer to the modules as
[11:45] the p1am we refer to the modules as slots so the first slot will be the
[11:48] slots so the first slot will be the
[11:48] slots so the first slot will be the first module on the right side of the
[11:50] first module on the right side of the
[11:50] first module on the right side of the p1am and we have only one slot here but
[11:53] p1am and we have only one slot here but
[11:53] p1am and we have only one slot here but you can expand them with as many modules
[11:55] you can expand them with as many modules
[11:55] you can expand them with as many modules as you like
[11:57] as you like
[11:57] as you like so you'll see in the productivity blocks
[11:59] so you'll see in the productivity blocks
[11:59] so you'll see in the productivity blocks program that we have
[12:01] program that we have
[12:01] program that we have a command to set the point of slot 1.1
[12:05] a command to set the point of slot 1.1
[12:05] a command to set the point of slot 1.1 that's going to refer to
[12:07] that's going to refer to
[12:07] that's going to refer to this 24 volt output module the 0.1
[12:11] this 24 volt output module the 0.1
[12:11] this 24 volt output module the 0.1 contact in the slot
[12:18] a few notes about the directionality of
[12:18] a few notes about the directionality of this process
[12:19] this process
[12:19] this process when you adapt the
[12:21] when you adapt the
[12:21] when you adapt the productivity blocks program
[12:23] productivity blocks program
[12:23] productivity blocks program you export to the dot ino file which is
[12:27] you export to the dot ino file which is
[12:27] you export to the dot ino file which is a c plus file
[12:29] a c plus file
[12:29] a c plus file automatically upon verifying or
[12:31] automatically upon verifying or
[12:32] automatically upon verifying or uploading
[12:33] uploading
[12:33] uploading and when you verify the program you have
[12:35] and when you verify the program you have
[12:35] and when you verify the program you have this here that's able to be customized
[12:37] this here that's able to be customized
[12:38] this here that's able to be customized by you if you would like to say
[12:40] by you if you would like to say
[12:40] by you if you would like to say my comment
[12:41] my comment
[12:41] my comment if you would like to add comments change
[12:44] if you would like to add comments change
[12:44] if you would like to add comments change variable names or completely change the
[12:46] variable names or completely change the
[12:46] variable names or completely change the program you can do that but you cannot
[12:48] program you can do that but you cannot
[12:48] program you can do that but you cannot re-export the ino file from the arduino
[12:54] re-export the ino file from the arduino
[12:54] re-export the ino file from the arduino workspace over to productivity blocks
[12:56] workspace over to productivity blocks
[12:56] workspace over to productivity blocks it's a one-way process
[12:58] it's a one-way process
[12:58] it's a one-way process so if i want to save
[13:00] so if i want to save
[13:00] so if i want to save my customize file i can do file save as
[13:03] my customize file i can do file save as
[13:03] my customize file i can do file save as and then it's going to say conveyor test
[13:06] and then it's going to say conveyor test
[13:06] and then it's going to say conveyor test custom
[13:07] custom
[13:07] custom [Music]
[13:08] [Music]
[13:08] [Music] and if i save that on the desktop just
[13:10] and if i save that on the desktop just
[13:10] and if i save that on the desktop just like any other arduino
[13:12] like any other arduino
[13:12] like any other arduino folders you need to have the folder
[13:15] folders you need to have the folder
[13:15] folders you need to have the folder that's going to be automatically
[13:17] that's going to be automatically
[13:17] that's going to be automatically generated with the same name as your
[13:20] generated with the same name as your
[13:20] generated with the same name as your main dot ino file
[13:26] the other thing that you cannot do with
[13:26] the other thing that you cannot do with productivity blocks is
[13:28] productivity blocks is
[13:28] productivity blocks is upload
[13:29] upload
[13:29] upload directly from productivity blocks to
[13:32] directly from productivity blocks to
[13:32] directly from productivity blocks to your unit so if i make a change here
[13:36] your unit so if i make a change here
[13:36] your unit so if i make a change here and i want to verify it or i want to
[13:39] and i want to verify it or i want to
[13:39] and i want to verify it or i want to upload it
[13:40] upload it
[13:40] upload it then just know that when you click
[13:42] then just know that when you click
[13:42] then just know that when you click verify or you click upload it's going to
[13:45] verify or you click upload it's going to
[13:45] verify or you click upload it's going to overwrite
[13:47] overwrite
[13:47] overwrite whatever file you have open currently
[13:49] whatever file you have open currently
[13:50] whatever file you have open currently and so if conveyor test custom had your
[13:52] and so if conveyor test custom had your
[13:52] and so if conveyor test custom had your comments written in it those comments
[13:55] comments written in it those comments
[13:55] comments written in it those comments are going to be deleted as soon as you
[13:57] are going to be deleted as soon as you
[13:57] are going to be deleted as soon as you click verify or if you click upload
[14:00] click verify or if you click upload
[14:00] click verify or if you click upload upload here is the same meaning as
[14:03] upload here is the same meaning as
[14:03] upload here is the same meaning as upload
[14:04] upload
[14:04] upload on the arduino ide where the clicking
[14:07] on the arduino ide where the clicking
[14:07] on the arduino ide where the clicking this button will first verify the code
[14:10] this button will first verify the code
[14:10] this button will first verify the code by compiling it and then try to send it
[14:13] by compiling it and then try to send it
[14:13] by compiling it and then try to send it out to um to the p1 am system over the
[14:17] out to um to the p1 am system over the
[14:17] out to um to the p1 am system over the com port
[14:20] com port
[14:20] com port lastly when you save your arduino file
[14:22] lastly when you save your arduino file
[14:22] lastly when you save your arduino file it does not save the productivity blocks
[14:25] it does not save the productivity blocks
[14:25] it does not save the productivity blocks file so if you make a change here
[14:29] file so if you make a change here
[14:29] file so if you make a change here you will see the little star here
[14:30] you will see the little star here
[14:30] you will see the little star here meaning the file has not been saved
[14:33] meaning the file has not been saved
[14:33] meaning the file has not been saved and if you close the arduino
[14:36] and if you close the arduino
[14:36] and if you close the arduino ide
[14:37] ide
[14:37] ide then it's going to close both and you
[14:39] then it's going to close both and you
[14:39] then it's going to close both and you will lose your saved changes
[14:42] will lose your saved changes
[14:42] will lose your saved changes let's look at the anatomy of the arduino
[14:44] let's look at the anatomy of the arduino
[14:44] let's look at the anatomy of the arduino code that's running this
[14:47] code that's running this
[14:47] code that's running this esp8266 or node mcu which is reading
[14:51] esp8266 or node mcu which is reading
[14:51] esp8266 or node mcu which is reading from the distance sensor the circuit
[14:53] from the distance sensor the circuit
[14:53] from the distance sensor the circuit looks like this where we've attached the
[14:55] looks like this where we've attached the
[14:55] looks like this where we've attached the distance sensor over the i2c bus to the
[14:58] distance sensor over the i2c bus to the
[14:58] distance sensor over the i2c bus to the node mcu
[14:59] node mcu
[14:59] node mcu and the node mcu is the one that's
[15:02] and the node mcu is the one that's
[15:02] and the node mcu is the one that's running the c plus program to loop by
[15:05] running the c plus program to loop by
[15:05] running the c plus program to loop by measuring
[15:06] measuring
[15:06] measuring the distance and
[15:08] the distance and
[15:08] the distance and blurring the buzzer in the case that the
[15:11] blurring the buzzer in the case that the
[15:11] blurring the buzzer in the case that the distance is near and also outputting a
[15:14] distance is near and also outputting a
[15:14] distance is near and also outputting a signal on the gpio pins that can be read
[15:19] signal on the gpio pins that can be read
[15:19] signal on the gpio pins that can be read by the input pins of the p1 am system
[15:23] by the input pins of the p1 am system
[15:23] by the input pins of the p1 am system so overall when this can comes down onto
[15:26] so overall when this can comes down onto
[15:26] so overall when this can comes down onto the conveyor and it comes in proximity
[15:28] the conveyor and it comes in proximity
[15:28] the conveyor and it comes in proximity to the distance sensor we have a
[15:30] to the distance sensor we have a
[15:30] to the distance sensor we have a threshold where if the can is near then
[15:33] threshold where if the can is near then
[15:33] threshold where if the can is near then we're going to take actions from the
[15:42] esp8266 this image shows how the vl 53
[15:42] esp8266 this image shows how the vl 53 sensor is connected to the i2c bus on
[15:45] sensor is connected to the i2c bus on
[15:45] sensor is connected to the i2c bus on our node mcu and also how the buzzer is
[15:48] our node mcu and also how the buzzer is
[15:48] our node mcu and also how the buzzer is connected and when we come
[15:50] connected and when we come
[15:50] connected and when we come back to the image of the overall setup
[15:53] back to the image of the overall setup
[15:53] back to the image of the overall setup you can see that we've remote mounted
[15:55] you can see that we've remote mounted
[15:55] you can see that we've remote mounted the vl sensor but it's still connected
[15:59] the vl sensor but it's still connected
[15:59] the vl sensor but it's still connected in the exact same way as when it's
[16:01] in the exact same way as when it's
[16:01] in the exact same way as when it's directly mounted on the board here where
[16:03] directly mounted on the board here where
[16:03] directly mounted on the board here where you can plug it into the female header
[16:05] you can plug it into the female header
[16:05] you can plug it into the female header pins that i've soldered on
[16:13] a disclaimer here that i'm not a c plus
[16:13] a disclaimer here that i'm not a c plus bus expert and i have some habits that
[16:16] bus expert and i have some habits that
[16:16] bus expert and i have some habits that may not be customary
[16:18] may not be customary
[16:18] may not be customary for example we when we start up this
[16:20] for example we when we start up this
[16:20] for example we when we start up this code it has three tabs
[16:22] code it has three tabs
[16:22] code it has three tabs i like to separate the buzzer functions
[16:24] i like to separate the buzzer functions
[16:24] i like to separate the buzzer functions and the vl53 sensor functions with
[16:28] and the vl53 sensor functions with
[16:28] and the vl53 sensor functions with away from the main tab
[16:31] away from the main tab
[16:31] away from the main tab and i name them both with the dot h
[16:33] and i name them both with the dot h
[16:33] and i name them both with the dot h because if they're if they have the dot
[16:36] because if they're if they have the dot
[16:36] because if they're if they have the dot h file extension then i can control the
[16:39] h file extension then i can control the
[16:39] h file extension then i can control the the sequence in which i include them
[16:42] the sequence in which i include them
[16:42] the sequence in which i include them and that will control in turn the other
[16:45] and that will control in turn the other
[16:45] and that will control in turn the other includes of libraries that we need
[16:48] includes of libraries that we need
[16:48] includes of libraries that we need and i like to have that control because
[16:50] and i like to have that control because
[16:50] and i like to have that control because sometimes the tabs have overlapping uh
[16:53] sometimes the tabs have overlapping uh
[16:53] sometimes the tabs have overlapping uh requirements
[16:54] requirements
[16:54] requirements so this is the the main um
[16:58] so this is the the main um
[16:58] so this is the the main um file that determines the behavior of
[17:00] file that determines the behavior of
[17:00] file that determines the behavior of this code so we essentially set up the
[17:03] this code so we essentially set up the
[17:04] this code so we essentially set up the buzzer after starting the serial
[17:06] buzzer after starting the serial
[17:06] buzzer after starting the serial communications
[17:08] communications
[17:08] communications we set up the vl sensor and by the way
[17:11] we set up the vl sensor and by the way
[17:11] we set up the vl sensor and by the way the serial communication is only used
[17:12] the serial communication is only used
[17:12] the serial communication is only used for debugging because once it's placed
[17:15] for debugging because once it's placed
[17:15] for debugging because once it's placed on the rack here
[17:17] on the rack here
[17:17] on the rack here it doesn't have any ability to
[17:19] it doesn't have any ability to
[17:19] it doesn't have any ability to communicate over serial to the user
[17:21] communicate over serial to the user
[17:21] communicate over serial to the user that's only
[17:23] that's only
[17:23] that's only talking to your your laptop or your pc
[17:25] talking to your your laptop or your pc
[17:25] talking to your your laptop or your pc while you're running
[17:27] while you're running
[17:27] while you're running then
[17:28] then
[17:28] then we set a
[17:29] we set a
[17:29] we set a output pin for pin d4 which is going to
[17:34] output pin for pin d4 which is going to
[17:34] output pin for pin d4 which is going to communicate to the buzzer sorry to the
[17:37] communicate to the buzzer sorry to the
[17:37] communicate to the buzzer sorry to the p1 am
[17:38] p1 am
[17:38] p1 am then in our loop
[17:40] then in our loop
[17:40] then in our loop we establish a my distance which is in
[17:44] we establish a my distance which is in
[17:44] we establish a my distance which is in me in millimeters it takes the distance
[17:47] me in millimeters it takes the distance
[17:47] me in millimeters it takes the distance read by the vl sensor
[17:49] read by the vl sensor
[17:50] read by the vl sensor and then
[17:51] and then
[17:51] and then for every loop it always resets the
[17:53] for every loop it always resets the
[17:53] for every loop it always resets the output pin to be low
[17:55] output pin to be low
[17:55] output pin to be low and this is the the d4 output pin which
[17:58] and this is the the d4 output pin which
[17:58] and this is the the d4 output pin which is being read by
[18:01] is being read by
[18:01] is being read by the p1 am system as an input here on
[18:04] the p1 am system as an input here on
[18:04] the p1 am system as an input here on this green terminal block
[18:05] this green terminal block
[18:05] this green terminal block so we come back here and we have a
[18:07] so we come back here and we have a
[18:07] so we come back here and we have a couple of if statements
[18:09] couple of if statements
[18:09] couple of if statements if the distance is not zero
[18:12] if the distance is not zero
[18:12] if the distance is not zero the distance if the distance is zero
[18:15] the distance if the distance is zero
[18:15] the distance if the distance is zero that the range the item
[18:18] that the range the item
[18:18] that the range the item measured could be very far away and it
[18:20] measured could be very far away and it
[18:20] measured could be very far away and it will return a zero because it's out of
[18:22] will return a zero because it's out of
[18:22] will return a zero because it's out of range so we want to toss that out
[18:24] range so we want to toss that out
[18:24] range so we want to toss that out and then when you say if the distance is
[18:27] and then when you say if the distance is
[18:27] and then when you say if the distance is uh if the obstacle is detected
[18:31] uh if the obstacle is detected
[18:31] uh if the obstacle is detected because
[18:37] so everything here is the main
[18:37] so everything here is the main functionality of the esp device in this
[18:41] functionality of the esp device in this
[18:41] functionality of the esp device in this conveyor demo so let's run through it
[18:43] conveyor demo so let's run through it
[18:43] conveyor demo so let's run through it really quickly we have two integers to
[18:45] really quickly we have two integers to
[18:45] really quickly we have two integers to declare the distance that we discover
[18:48] declare the distance that we discover
[18:48] declare the distance that we discover and the trigger distance which is 10
[18:50] and the trigger distance which is 10
[18:50] and the trigger distance which is 10 centimeters and then we have a flag
[18:52] centimeters and then we have a flag
[18:52] centimeters and then we have a flag for use later in the loop
[18:55] for use later in the loop
[18:55] for use later in the loop first in our setup loop we
[18:57] first in our setup loop we
[18:57] first in our setup loop we start the serial communication we set up
[18:59] start the serial communication we set up
[19:00] start the serial communication we set up the buzzer
[19:01] the buzzer
[19:01] the buzzer using functions from this tab we set up
[19:03] using functions from this tab we set up
[19:03] using functions from this tab we set up the vl distance sensor using functions
[19:05] the vl distance sensor using functions
[19:05] the vl distance sensor using functions from this tab
[19:07] from this tab
[19:07] from this tab and then we establish this d4 output pin
[19:09] and then we establish this d4 output pin
[19:09] and then we establish this d4 output pin which is the pin that's going to
[19:10] which is the pin that's going to
[19:10] which is the pin that's going to communicate
[19:11] communicate
[19:12] communicate from the
[19:13] from the
[19:13] from the esp device to the p1am inputs on this
[19:17] esp device to the p1am inputs on this
[19:17] esp device to the p1am inputs on this terminal lot
[19:19] terminal lot
[19:19] terminal lot then after the setup we start the loop
[19:22] then after the setup we start the loop
[19:22] then after the setup we start the loop we take a measurement for every loop
[19:24] we take a measurement for every loop
[19:24] we take a measurement for every loop using the vl sensor and store that in my
[19:27] using the vl sensor and store that in my
[19:27] using the vl sensor and store that in my distance then
[19:29] distance then
[19:29] distance then we write
[19:30] we write
[19:30] we write a reset function to to make sure that
[19:33] a reset function to to make sure that
[19:33] a reset function to to make sure that the pin on the output of d4 is set low
[19:37] the pin on the output of d4 is set low
[19:37] the pin on the output of d4 is set low that's the the default communication
[19:40] that's the the default communication
[19:40] that's the the default communication to the p1am if the can
[19:43] to the p1am if the can
[19:44] to the p1am if the can if the object is not detected near
[19:47] if the object is not detected near
[19:47] if the object is not detected near and less than the threshold
[19:49] and less than the threshold
[19:49] and less than the threshold then we have two if groups the first if
[19:52] then we have two if groups the first if
[19:52] then we have two if groups the first if statement is saying if the distance is
[19:54] statement is saying if the distance is
[19:54] statement is saying if the distance is not zero well when uh the vl sensor is
[19:58] not zero well when uh the vl sensor is
[19:58] not zero well when uh the vl sensor is out of range then it's going to return a
[20:00] out of range then it's going to return a
[20:00] out of range then it's going to return a zero and we don't want to handle that so
[20:02] zero and we don't want to handle that so
[20:02] zero and we don't want to handle that so we say if we don't need to handle that
[20:04] we say if we don't need to handle that
[20:04] we say if we don't need to handle that then we're going to check is my distance
[20:06] then we're going to check is my distance
[20:06] then we're going to check is my distance less than the trigger or the threshold
[20:09] less than the trigger or the threshold
[20:09] less than the trigger or the threshold of 10 centimeters
[20:11] of 10 centimeters
[20:11] of 10 centimeters if so we raise the flag
[20:14] if so we raise the flag
[20:14] if so we raise the flag then the next if loop is going to
[20:17] then the next if loop is going to
[20:17] then the next if loop is going to act on that flag if the flag is high
[20:20] act on that flag if the flag is high
[20:20] act on that flag if the flag is high then we're going to write the output of
[20:22] then we're going to write the output of
[20:22] then we're going to write the output of d4 to be high
[20:24] d4 to be high
[20:24] d4 to be high and then we're going to ask the buzzer
[20:26] and then we're going to ask the buzzer
[20:26] and then we're going to ask the buzzer to make its chirping sound to indicate
[20:29] to make its chirping sound to indicate
[20:29] to make its chirping sound to indicate to the user
[20:31] to the user
[20:31] to the user that the
[20:32] that the
[20:32] that the the the object was detected
[20:34] the the object was detected
[20:34] the the object was detected so this line 32 indicates to the p1am
[20:37] so this line 32 indicates to the p1am
[20:38] so this line 32 indicates to the p1am plc that the object was detected and
[20:41] plc that the object was detected and
[20:41] plc that the object was detected and line 33 indicates it to the user
[20:44] line 33 indicates it to the user
[20:44] line 33 indicates it to the user two separate communications
[20:46] two separate communications
[20:46] two separate communications then we delay for 50 milliseconds but uh
[20:49] then we delay for 50 milliseconds but uh
[20:50] then we delay for 50 milliseconds but uh but take note that this uh chirp takes
[20:52] but take note that this uh chirp takes
[20:52] but take note that this uh chirp takes maybe 500 milliseconds so we're we're
[20:55] maybe 500 milliseconds so we're we're
[20:55] maybe 500 milliseconds so we're we're taking
[20:56] taking
[20:56] taking uh the d4 to be a high position a little
[20:59] uh the d4 to be a high position a little
[20:59] uh the d4 to be a high position a little over half of a second which is plenty of
[21:01] over half of a second which is plenty of
[21:01] over half of a second which is plenty of time
[21:02] time
[21:02] time for
[21:03] for
[21:03] for for the p1am
[21:06] for the p1am
[21:06] for the p1am plc to notice that the input has gone
[21:09] plc to notice that the input has gone
[21:09] plc to notice that the input has gone high
[21:10] high
[21:10] high and this loop overall because i've
[21:13] and this loop overall because i've
[21:13] and this loop overall because i've tested it runs around 50 hertz so 50
[21:16] tested it runs around 50 hertz so 50
[21:16] tested it runs around 50 hertz so 50 times a second we have the the
[21:18] times a second we have the the
[21:18] times a second we have the the opportunity to notice
[21:20] opportunity to notice
[21:20] opportunity to notice if the object has approached that means
[21:22] if the object has approached that means
[21:22] if the object has approached that means if you turn the speed up all the way
[21:24] if you turn the speed up all the way
[21:24] if you turn the speed up all the way and you have a small object you probably
[21:26] and you have a small object you probably
[21:26] and you have a small object you probably can still detect if it comes within
[21:28] can still detect if it comes within
[21:28] can still detect if it comes within range of the sensor
[21:31] range of the sensor
[21:31] range of the sensor the last line of the code is just to
[21:33] the last line of the code is just to
[21:33] the last line of the code is just to reset the flag to be low and then we
[21:35] reset the flag to be low and then we
[21:35] reset the flag to be low and then we jump back to the beginning of the loop
[21:41] you can find the arduino files to run
[21:41] you can find the arduino files to run this software in the arduino folder of
[21:44] this software in the arduino folder of
[21:44] this software in the arduino folder of the mxct conveyor github repository and
[21:48] the mxct conveyor github repository and
[21:48] the mxct conveyor github repository and you'll need to download each of these
[21:49] you'll need to download each of these
[21:49] you'll need to download each of these files and put them in a folder called
[21:52] files and put them in a folder called
[21:52] files and put them in a folder called 007.12 buzz vl
[21:54] 007.12 buzz vl
[21:54] 007.12 buzz vl and that's the only way to get the
[21:56] and that's the only way to get the
[21:56] and that's the only way to get the arduino program to recognize it

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
