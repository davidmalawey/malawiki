---
title: "Power Budget Explained [Mechatronics Capstone Projects]"
url: "https://www.youtube.com/watch?v=DKPFsVOTJpw"
video_id: "DKPFsVOTJpw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2022-11-20
duration: "12:18"
duration_sec: 738
views: 415
likes: 7
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/DKPFsVOTJpw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 578
chapters_count: 0
has_description: true
has_comments: false
---

## Description

Tips & Template for budgeting power in your multidisciplinary/mechatronics engineering design project. 

Get the template in my resource page: https://qr.page/g/4ZptmdWxn5y

## Transcript

[0:03] hello Capstone teams this is your lab
[0:03] hello Capstone teams this is your lab coordinator David and I'm going to give
[0:05] coordinator David and I'm going to give
[0:05] coordinator David and I'm going to give a quick walkthrough of the the power
[0:07] a quick walkthrough of the the power
[0:07] a quick walkthrough of the the power budget example document that I shared
[0:10] budget example document that I shared
[0:10] budget example document that I shared with your Capstone professors so this is
[0:13] with your Capstone professors so this is
[0:13] with your Capstone professors so this is not a requirement I don't think it's an
[0:16] not a requirement I don't think it's an
[0:16] not a requirement I don't think it's an explicit requirement but the document
[0:18] explicit requirement but the document
[0:18] explicit requirement but the document itself in Excel should offer a nice
[0:22] itself in Excel should offer a nice
[0:22] itself in Excel should offer a nice template for you to start evaluating the
[0:25] template for you to start evaluating the
[0:25] template for you to start evaluating the power that you need for your battery how
[0:27] power that you need for your battery how
[0:27] power that you need for your battery how much is consumed by each device how to
[0:29] much is consumed by each device how to
[0:29] much is consumed by each device how to estimate the overall
[0:31] estimate the overall
[0:31] estimate the overall decisions you need for selecting wires
[0:34] decisions you need for selecting wires
[0:34] decisions you need for selecting wires and and configuring your software how to
[0:37] and and configuring your software how to
[0:37] and and configuring your software how to run your project for any larger power
[0:41] run your project for any larger power
[0:41] run your project for any larger power than larger than embedded system
[0:44] than larger than embedded system
[0:44] than larger than embedded system mechatronics assemblies so let's just do
[0:49] mechatronics assemblies so let's just do
[0:49] mechatronics assemblies so let's just do a quick walk through I want to explain
[0:50] a quick walk through I want to explain
[0:50] a quick walk through I want to explain everything but I'll give an introduction
[0:53] everything but I'll give an introduction
[0:53] everything but I'll give an introduction basically the first tab on this
[0:55] basically the first tab on this
[0:55] basically the first tab on this spreadsheet is talking about what are
[0:57] spreadsheet is talking about what are
[0:57] spreadsheet is talking about what are the goals that you should be considering
[0:59] the goals that you should be considering
[0:59] the goals that you should be considering when you're making your power budget it
[1:01] when you're making your power budget it
[1:01] when you're making your power budget it kind of explains why you would want to
[1:03] kind of explains why you would want to
[1:03] kind of explains why you would want to make a power budget and when you start
[1:05] make a power budget and when you start
[1:05] make a power budget and when you start answering all these questions for
[1:07] answering all these questions for
[1:07] answering all these questions for yourself then you can discover a little
[1:09] yourself then you can discover a little
[1:09] yourself then you can discover a little bit more clearly what uh what estimates
[1:13] bit more clearly what uh what estimates
[1:13] bit more clearly what uh what estimates and what level of detail you need to go
[1:15] and what level of detail you need to go
[1:15] and what level of detail you need to go into to actually serve your own purpose
[1:17] into to actually serve your own purpose
[1:17] into to actually serve your own purpose whether that's for supporting your
[1:20] whether that's for supporting your
[1:20] whether that's for supporting your electrical designer or supporting the
[1:23] electrical designer or supporting the
[1:23] electrical designer or supporting the person that's making the report on the
[1:25] person that's making the report on the
[1:25] person that's making the report on the specifications looking out for your your
[1:29] specifications looking out for your your
[1:29] specifications looking out for your your final demo Etc
[1:31] final demo Etc
[1:31] final demo Etc um the example that's been used for this
[1:36] um the example that's been used for this
[1:36] um the example that's been used for this the example used for this uh document
[1:39] the example used for this uh document
[1:39] the example used for this uh document itself is from the the cast team that
[1:42] itself is from the the cast team that
[1:42] itself is from the the cast team that was taking the Scuttle robot and
[1:45] was taking the Scuttle robot and
[1:45] was taking the Scuttle robot and creating a covid related
[1:48] creating a covid related
[1:48] creating a covid related sanitizing machine
[1:50] sanitizing machine
[1:50] sanitizing machine and all the mechanical and electronics
[1:53] and all the mechanical and electronics
[1:53] and all the mechanical and electronics associated with that and so their system
[1:56] associated with that and so their system
[1:56] associated with that and so their system included an extra battery a couple of
[1:59] included an extra battery a couple of
[1:59] included an extra battery a couple of extra sensors and an actuator a motor to
[2:02] extra sensors and an actuator a motor to
[2:02] extra sensors and an actuator a motor to move an arm up and down in some powerful
[2:05] move an arm up and down in some powerful
[2:05] move an arm up and down in some powerful ultraviolet lights we won't get into the
[2:08] ultraviolet lights we won't get into the
[2:08] ultraviolet lights we won't get into the the sensor here on the right that's for
[2:10] the sensor here on the right that's for
[2:10] the sensor here on the right that's for sensing the ultraviolet
[2:13] sensing the ultraviolet
[2:13] sensing the ultraviolet um output
[2:14] um output
[2:14] um output so go through the the goals and ask
[2:17] so go through the the goals and ask
[2:17] so go through the the goals and ask yourself what you need to know before
[2:19] yourself what you need to know before
[2:19] yourself what you need to know before you begin basically we it's starting a
[2:22] you begin basically we it's starting a
[2:22] you begin basically we it's starting a little bit more broad like what is the
[2:23] little bit more broad like what is the
[2:23] little bit more broad like what is the peak power demand of your machine
[2:26] peak power demand of your machine
[2:26] peak power demand of your machine and then it gets a little bit more
[2:28] and then it gets a little bit more
[2:28] and then it gets a little bit more detailed such as what cables sizes are
[2:31] detailed such as what cables sizes are
[2:31] detailed such as what cables sizes are necessary some of these decisions are
[2:33] necessary some of these decisions are
[2:33] necessary some of these decisions are already made for you you have to
[2:35] already made for you you have to
[2:35] already made for you you have to consider what your your project includes
[2:38] consider what your your project includes
[2:38] consider what your your project includes and what are your constraints to decide
[2:40] and what are your constraints to decide
[2:40] and what are your constraints to decide which questions are really relevant and
[2:42] which questions are really relevant and
[2:42] which questions are really relevant and this should be when you input data you
[2:45] this should be when you input data you
[2:45] this should be when you input data you should really have clear answers for
[2:47] should really have clear answers for
[2:47] should really have clear answers for those versus skipping them
[2:50] those versus skipping them
[2:50] those versus skipping them um then we come down to what you're
[2:52] um then we come down to what you're
[2:52] um then we come down to what you're going to compute your Computing
[2:54] going to compute your Computing
[2:54] going to compute your Computing estimates of the device's consumption
[2:57] estimates of the device's consumption
[2:57] estimates of the device's consumption individually your Computing
[3:01] individually your Computing
[3:01] individually your Computing um
[3:02] um
[3:02] um data that comes in from the outside from
[3:04] data that comes in from the outside from
[3:04] data that comes in from the outside from like data sheets and then estimates that
[3:06] like data sheets and then estimates that
[3:06] like data sheets and then estimates that you come up with on your own if you
[3:08] you come up with on your own if you
[3:08] you come up with on your own if you don't have the data sheets for every
[3:10] don't have the data sheets for every
[3:10] don't have the data sheets for every single thing or for your operating
[3:12] single thing or for your operating
[3:12] single thing or for your operating condition you're going to consider
[3:14] condition you're going to consider
[3:14] condition you're going to consider logically how your estimates may be
[3:16] logically how your estimates may be
[3:16] logically how your estimates may be valid so that you don't run into trouble
[3:19] valid so that you don't run into trouble
[3:19] valid so that you don't run into trouble having a completely wrong power supply
[3:21] having a completely wrong power supply
[3:21] having a completely wrong power supply when you're ready to do your demo
[3:24] when you're ready to do your demo
[3:24] when you're ready to do your demo and then
[3:25] and then
[3:25] and then um the bottom section says well how will
[3:28] um the bottom section says well how will
[3:28] um the bottom section says well how will the above information impact Your Design
[3:31] the above information impact Your Design
[3:31] the above information impact Your Design decisions such as selecting a battery
[3:34] decisions such as selecting a battery
[3:34] decisions such as selecting a battery um so the following Tabs are actually
[3:37] um so the following Tabs are actually
[3:37] um so the following Tabs are actually tabulated data and we're going to do in
[3:40] tabulated data and we're going to do in
[3:40] tabulated data and we're going to do in the normal View
[3:41] the normal View
[3:41] the normal View so data from Electronics we're basically
[3:45] so data from Electronics we're basically
[3:45] so data from Electronics we're basically just capturing the key metrics that come
[3:48] just capturing the key metrics that come
[3:48] just capturing the key metrics that come from each of the components the
[3:49] from each of the components the
[3:49] from each of the components the electronic sensors Etc that are included
[3:52] electronic sensors Etc that are included
[3:52] electronic sensors Etc that are included in the project or are planned to be
[3:54] in the project or are planned to be
[3:54] in the project or are planned to be included we have modifications to the
[3:57] included we have modifications to the
[3:57] included we have modifications to the Scuttle platform that include a lidar we
[4:01] Scuttle platform that include a lidar we
[4:01] Scuttle platform that include a lidar we have the elements on a moving arm that
[4:04] have the elements on a moving arm that
[4:04] have the elements on a moving arm that include ultraviolet LEDs and the motor
[4:06] include ultraviolet LEDs and the motor
[4:06] include ultraviolet LEDs and the motor that moves it we have the the Scuttle
[4:09] that moves it we have the the Scuttle
[4:09] that moves it we have the the Scuttle base machine and the general power
[4:11] base machine and the general power
[4:11] base machine and the general power consumption of that
[4:13] consumption of that
[4:13] consumption of that we look at how many of them are included
[4:16] we look at how many of them are included
[4:16] we look at how many of them are included what are the what is the voltage that
[4:18] what are the what is the voltage that
[4:18] what are the what is the voltage that they're operating at
[4:19] they're operating at
[4:19] they're operating at um and then essentially get the total
[4:22] um and then essentially get the total
[4:22] um and then essentially get the total power to know when they're all running
[4:24] power to know when they're all running
[4:24] power to know when they're all running full speed then what's the what's the
[4:28] full speed then what's the what's the
[4:28] full speed then what's the what's the power consumed and if you ran everything
[4:30] power consumed and if you ran everything
[4:30] power consumed and if you ran everything at 100 duty cycle what would be the
[4:33] at 100 duty cycle what would be the
[4:33] at 100 duty cycle what would be the power demanded
[4:35] power demanded
[4:35] power demanded then we looked a little bit closer and
[4:37] then we looked a little bit closer and
[4:37] then we looked a little bit closer and break it into assemblies to say okay
[4:39] break it into assemblies to say okay
[4:39] break it into assemblies to say okay here's the power of each of our modules
[4:41] here's the power of each of our modules
[4:41] here's the power of each of our modules that might help your designer who
[4:44] that might help your designer who
[4:44] that might help your designer who um who's addressing one module and the
[4:48] um who's addressing one module and the
[4:48] um who's addressing one module and the other designer who's addressing another
[4:51] other designer who's addressing another
[4:51] other designer who's addressing another um then we have the peak current this is
[4:54] um then we have the peak current this is
[4:54] um then we have the peak current this is going to help you with other decisions
[4:56] going to help you with other decisions
[4:56] going to help you with other decisions in your in your design such as wiring
[4:59] in your in your design such as wiring
[4:59] in your in your design such as wiring and connectors sizing
[5:01] and connectors sizing
[5:01] and connectors sizing um and selection of a power supply if
[5:03] um and selection of a power supply if
[5:03] um and selection of a power supply if you have an adapter
[5:05] you have an adapter
[5:05] you have an adapter next section is run runtime
[5:09] next section is run runtime
[5:09] next section is run runtime um
[5:10] um
[5:10] um okay so we want to start with our design
[5:13] okay so we want to start with our design
[5:13] okay so we want to start with our design criteria compare the project Target with
[5:16] criteria compare the project Target with
[5:16] criteria compare the project Target with the available energy
[5:18] the available energy
[5:18] the available energy this was driven essentially by battery
[5:20] this was driven essentially by battery
[5:20] this was driven essentially by battery size selection how many milliamps hours
[5:23] size selection how many milliamps hours
[5:23] size selection how many milliamps hours do we need in our battery for a mobile
[5:26] do we need in our battery for a mobile
[5:26] do we need in our battery for a mobile machine to do such uh such a task
[5:29] machine to do such uh such a task
[5:29] machine to do such uh such a task so
[5:31] so
[5:31] so we can look at
[5:33] we can look at
[5:33] we can look at um
[5:34] um
[5:34] um the desired runtime as a key input so
[5:37] the desired runtime as a key input so
[5:37] the desired runtime as a key input so well we want it to run for two hours
[5:39] well we want it to run for two hours
[5:39] well we want it to run for two hours that's the invention we've been asked to
[5:40] that's the invention we've been asked to
[5:40] that's the invention we've been asked to make
[5:41] make
[5:41] make what is the average power coming from
[5:44] what is the average power coming from
[5:44] what is the average power coming from the previous tab that we expect to be
[5:46] the previous tab that we expect to be
[5:46] the previous tab that we expect to be using during this runtime and then how
[5:50] using during this runtime and then how
[5:50] using during this runtime and then how many amp hours will we need to support
[5:51] many amp hours will we need to support
[5:51] many amp hours will we need to support that based on the battery's nominal
[5:54] that based on the battery's nominal
[5:54] that based on the battery's nominal voltage
[5:55] voltage
[5:55] voltage then we come back to come to capacity
[5:58] then we come back to come to capacity
[5:58] then we come back to come to capacity criteria
[5:59] criteria
[5:59] criteria how much energy is is needed given this
[6:04] how much energy is is needed given this
[6:04] how much energy is is needed given this many amp hours and this many watts now
[6:07] many amp hours and this many watts now
[6:07] many amp hours and this many watts now we're talking about if you want to
[6:08] we're talking about if you want to
[6:08] we're talking about if you want to select your own battery there's no
[6:10] select your own battery there's no
[6:10] select your own battery there's no battery included in the devices that you
[6:12] battery included in the devices that you
[6:12] battery included in the devices that you you have brought into your project and
[6:14] you have brought into your project and
[6:14] you have brought into your project and you have to choose that yourself okay
[6:16] you have to choose that yourself okay
[6:16] you have to choose that yourself okay well if this is the voltage then this is
[6:18] well if this is the voltage then this is
[6:18] well if this is the voltage then this is how many amp hours we need then you can
[6:20] how many amp hours we need then you can
[6:20] how many amp hours we need then you can design a battery or or put batteries in
[6:23] design a battery or or put batteries in
[6:23] design a battery or or put batteries in series Etc
[6:25] series Etc
[6:25] series Etc then we have robot modules grouped by
[6:27] then we have robot modules grouped by
[6:27] then we have robot modules grouped by actions this uh table steers us towards
[6:30] actions this uh table steers us towards
[6:30] actions this uh table steers us towards having a decisions on how we're going to
[6:33] having a decisions on how we're going to
[6:33] having a decisions on how we're going to run the robot well sometimes we will
[6:35] run the robot well sometimes we will
[6:35] run the robot well sometimes we will have our actuator assembly operating and
[6:39] have our actuator assembly operating and
[6:39] have our actuator assembly operating and it's doing that when it's moving the arm
[6:41] it's doing that when it's moving the arm
[6:41] it's doing that when it's moving the arm uh it'll move the arm 25 of the time
[6:44] uh it'll move the arm 25 of the time
[6:44] uh it'll move the arm 25 of the time this is a ballpark idea before you go
[6:47] this is a ballpark idea before you go
[6:47] this is a ballpark idea before you go too far into your project then we say
[6:49] too far into your project then we say
[6:49] too far into your project then we say the power the power of that movement is
[6:52] the power the power of that movement is
[6:52] the power the power of that movement is this much because I'll have the motor is
[6:55] this much because I'll have the motor is
[6:55] this much because I'll have the motor is the only item running during that time
[6:58] the only item running during that time
[6:58] the only item running during that time so now we've broken down power in a
[7:01] so now we've broken down power in a
[7:01] so now we've broken down power in a different way that says
[7:02] different way that says
[7:02] different way that says um
[7:03] um
[7:03] um different conditions based on the the
[7:06] different conditions based on the the
[7:06] different conditions based on the the sequence that your robot or your machine
[7:08] sequence that your robot or your machine
[7:08] sequence that your robot or your machine is operating
[7:10] is operating
[7:10] is operating that's very driven by the the task of
[7:13] that's very driven by the the task of
[7:13] that's very driven by the the task of your machine
[7:14] your machine
[7:14] your machine okay
[7:21] system power map we have different power
[7:21] system power map we have different power sources there's only one power source
[7:24] sources there's only one power source
[7:24] sources there's only one power source that's driving the whole system but if
[7:27] that's driving the whole system but if
[7:27] that's driving the whole system but if you look deeper the the converter which
[7:30] you look deeper the the converter which
[7:30] you look deeper the the converter which pulls power from the battery and only
[7:32] pulls power from the battery and only
[7:32] pulls power from the battery and only feeds certain electronics and has its
[7:34] feeds certain electronics and has its
[7:34] feeds certain electronics and has its own
[7:35] own
[7:35] own um it is a power source as well and so
[7:37] um it is a power source as well and so
[7:37] um it is a power source as well and so it can deliver a certain number of amps
[7:40] it can deliver a certain number of amps
[7:40] it can deliver a certain number of amps and there will be certain devices that
[7:42] and there will be certain devices that
[7:42] and there will be certain devices that are connected to the 24 volt output not
[7:45] are connected to the 24 volt output not
[7:45] are connected to the 24 volt output not all of them and so this this table
[7:48] all of them and so this this table
[7:48] all of them and so this this table actually this whole page is to help us
[7:51] actually this whole page is to help us
[7:51] actually this whole page is to help us understand and decide
[7:53] understand and decide
[7:53] understand and decide um do we have sufficient power at each
[7:56] um do we have sufficient power at each
[7:56] um do we have sufficient power at each power source not just at the battery at
[7:59] power source not just at the battery at
[7:59] power source not just at the battery at the at the overall
[8:01] the at the overall
[8:01] the at the overall so here we have an example where we we
[8:03] so here we have an example where we we
[8:03] so here we have an example where we we did a conditional formatting we said
[8:05] did a conditional formatting we said
[8:05] did a conditional formatting we said well the converter is going to crank out
[8:08] well the converter is going to crank out
[8:08] well the converter is going to crank out the converter needs eight amps but our
[8:11] the converter needs eight amps but our
[8:11] the converter needs eight amps but our first battery selected only can provide
[8:13] first battery selected only can provide
[8:13] first battery selected only can provide 6 amps and so this value comes out to a
[8:16] 6 amps and so this value comes out to a
[8:16] 6 amps and so this value comes out to a negative number it's the only one that's
[8:17] negative number it's the only one that's
[8:17] negative number it's the only one that's negative it'll be yellow if it has a
[8:19] negative it'll be yellow if it has a
[8:19] negative it'll be yellow if it has a small margin relative relative to the
[8:22] small margin relative relative to the
[8:22] small margin relative relative to the others and then we should make a note
[8:25] others and then we should make a note
[8:25] others and then we should make a note and decide what to do about it and you
[8:27] and decide what to do about it and you
[8:27] and decide what to do about it and you can put your notes here if you want to
[8:29] can put your notes here if you want to
[8:29] can put your notes here if you want to organize your your design
[8:32] organize your your design
[8:32] organize your your design process in the same way
[8:34] process in the same way
[8:34] process in the same way then we have power losses this is going
[8:37] then we have power losses this is going
[8:37] then we have power losses this is going to be more filled out but basically an
[8:39] to be more filled out but basically an
[8:39] to be more filled out but basically an example is the converter that gives us
[8:42] example is the converter that gives us
[8:42] example is the converter that gives us 24 volts it loses a lot because boost
[8:44] 24 volts it loses a lot because boost
[8:45] 24 volts it loses a lot because boost can converters lose a lot if you get an
[8:47] can converters lose a lot if you get an
[8:47] can converters lose a lot if you get an expensive one you could maybe get it 90
[8:49] expensive one you could maybe get it 90
[8:49] expensive one you could maybe get it 90 efficient but the Amazon
[8:53] efficient but the Amazon
[8:54] efficient but the Amazon types they're more closer to 80 percent
[8:57] types they're more closer to 80 percent
[8:57] types they're more closer to 80 percent efficient
[8:59] efficient
[9:00] efficient um next tab
[9:07] um all right power exclusions this tabs
[9:07] um all right power exclusions this tabs only relevant for teams that that found
[9:09] only relevant for teams that that found
[9:09] only relevant for teams that that found that well they have a cluster of
[9:11] that well they have a cluster of
[9:11] that well they have a cluster of elements that actually
[9:13] elements that actually
[9:13] elements that actually ought to be excluded from the power
[9:14] ought to be excluded from the power
[9:14] ought to be excluded from the power budget make it simpler make it easier to
[9:17] budget make it simpler make it easier to
[9:17] budget make it simpler make it easier to evaluate because
[9:19] evaluate because
[9:19] evaluate because for example on their uh their sensing
[9:23] for example on their uh their sensing
[9:23] for example on their uh their sensing and indicating array all of the Power
[9:27] and indicating array all of the Power
[9:27] and indicating array all of the Power consuming devices are in milliamps so
[9:30] consuming devices are in milliamps so
[9:30] consuming devices are in milliamps so there's two possibilities one of them is
[9:32] there's two possibilities one of them is
[9:32] there's two possibilities one of them is you're looking at these LEDs and you're
[9:34] you're looking at these LEDs and you're
[9:34] you're looking at these LEDs and you're going to say well we'll just negate this
[9:35] going to say well we'll just negate this
[9:35] going to say well we'll just negate this from all our computations because it
[9:37] from all our computations because it
[9:37] from all our computations because it won't have an impact on the on the
[9:39] won't have an impact on the on the
[9:39] won't have an impact on the on the project or you can say that
[9:42] project or you can say that
[9:42] project or you can say that these um
[9:44] these um
[9:44] these um these devices are all driving uh pulling
[9:47] these devices are all driving uh pulling
[9:48] these devices are all driving uh pulling power from a specific Source such as the
[9:51] power from a specific Source such as the
[9:51] power from a specific Source such as the Raspberry Pi and when uh when the
[9:55] Raspberry Pi and when uh when the
[9:55] Raspberry Pi and when uh when the Raspberry Pi outputs to its 5 volt uh 5
[9:59] Raspberry Pi outputs to its 5 volt uh 5
[9:59] Raspberry Pi outputs to its 5 volt uh 5 volt Source at the USB ports that has
[10:03] volt Source at the USB ports that has
[10:03] volt Source at the USB ports that has its own limitation this table can remind
[10:06] its own limitation this table can remind
[10:06] its own limitation this table can remind you to go back into the data sheet of
[10:08] you to go back into the data sheet of
[10:08] you to go back into the data sheet of the the Raspberry Pi and then check well
[10:11] the the Raspberry Pi and then check well
[10:11] the the Raspberry Pi and then check well how much current can actually drive from
[10:13] how much current can actually drive from
[10:13] how much current can actually drive from that device itself since it's doing the
[10:15] that device itself since it's doing the
[10:15] that device itself since it's doing the job of regulating at 5 volts
[10:18] job of regulating at 5 volts
[10:18] job of regulating at 5 volts um actions this is a place for you to
[10:20] um actions this is a place for you to
[10:20] um actions this is a place for you to just make your notes about uh how how
[10:23] just make your notes about uh how how
[10:24] just make your notes about uh how how this will have an impact and maybe a
[10:26] this will have an impact and maybe a
[10:26] this will have an impact and maybe a discussion about why you estimated
[10:28] discussion about why you estimated
[10:28] discussion about why you estimated something is not due relevant and you've
[10:30] something is not due relevant and you've
[10:30] something is not due relevant and you've omitted it from your overall uh final
[10:33] omitted it from your overall uh final
[10:33] omitted it from your overall uh final presentation
[10:34] presentation
[10:34] presentation then justifications this tab is
[10:37] then justifications this tab is
[10:37] then justifications this tab is um it's a pretty rough draft but I
[10:42] um it's a pretty rough draft but I
[10:42] um it's a pretty rough draft but I included the examples of this is a
[10:44] included the examples of this is a
[10:44] included the examples of this is a discussion that came from the Capstone
[10:45] discussion that came from the Capstone
[10:45] discussion that came from the Capstone team in Fall of 2022 sorry spring 2022
[10:51] team in Fall of 2022 sorry spring 2022
[10:51] team in Fall of 2022 sorry spring 2022 how they made their decisions about duty
[10:54] how they made their decisions about duty
[10:54] how they made their decisions about duty cycle and there will be other
[10:56] cycle and there will be other
[10:56] cycle and there will be other estimations that you want to make not
[10:58] estimations that you want to make not
[10:58] estimations that you want to make not just not just Duty as indicated in this
[11:01] just not just Duty as indicated in this
[11:01] just not just Duty as indicated in this column then references also they these
[11:05] column then references also they these
[11:05] column then references also they these really are are ultimately going to find
[11:07] really are are ultimately going to find
[11:07] really are are ultimately going to find their way into your
[11:09] their way into your
[11:09] their way into your um into your final document if they're
[11:12] um into your final document if they're
[11:12] um into your final document if they're relevant but in the during the design
[11:14] relevant but in the during the design
[11:14] relevant but in the during the design process you might have a nice list of
[11:17] process you might have a nice list of
[11:17] process you might have a nice list of bookmarks that you should should be
[11:20] bookmarks that you should should be
[11:20] bookmarks that you should should be sharing with your other team members you
[11:22] sharing with your other team members you
[11:22] sharing with your other team members you might toss them out at the end or you
[11:24] might toss them out at the end or you
[11:24] might toss them out at the end or you might realize that that you continue
[11:26] might realize that that you continue
[11:26] might realize that that you continue coming back to them and they're really
[11:28] coming back to them and they're really
[11:28] coming back to them and they're really driving the explanation for your overall
[11:31] driving the explanation for your overall
[11:31] driving the explanation for your overall power power evaluation so feel free to
[11:34] power power evaluation so feel free to
[11:34] power power evaluation so feel free to use this whole Excel spreadsheet
[11:37] use this whole Excel spreadsheet
[11:37] use this whole Excel spreadsheet um I strongly recommend thinking
[11:39] um I strongly recommend thinking
[11:39] um I strongly recommend thinking thoughtfully about this and I think that
[11:41] thoughtfully about this and I think that
[11:41] thoughtfully about this and I think that the
[11:42] the
[11:42] the thoughtfully about the questions so that
[11:46] thoughtfully about the questions so that
[11:46] thoughtfully about the questions so that you can trim back your work overall and
[11:49] you can trim back your work overall and
[11:49] you can trim back your work overall and only deliver in your in your
[11:52] only deliver in your in your
[11:52] only deliver in your in your deliverables the information and the
[11:55] deliverables the information and the
[11:55] deliverables the information and the calculations that really matter
[11:57] calculations that really matter
[11:57] calculations that really matter and then set you can set aside
[12:00] and then set you can set aside
[12:00] and then set you can set aside everything else simply by by justifying
[12:02] everything else simply by by justifying
[12:02] everything else simply by by justifying it if you've thought of it or if you
[12:05] it if you've thought of it or if you
[12:05] it if you've thought of it or if you haven't thought of it and it's not on
[12:06] haven't thought of it and it's not on
[12:06] haven't thought of it and it's not on this list maybe you're going to be okay
[12:08] this list maybe you're going to be okay
[12:08] this list maybe you're going to be okay without it so
[12:10] without it so
[12:10] without it so um hope that helps and you can just talk
[12:12] um hope that helps and you can just talk
[12:12] um hope that helps and you can just talk to your professor if you need to get a
[12:14] to your professor if you need to get a
[12:14] to your professor if you need to get a copy of this of this Excel spreadsheet

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
