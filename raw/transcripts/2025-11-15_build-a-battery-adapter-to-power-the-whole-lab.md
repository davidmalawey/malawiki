---
title: "Build a battery adapter to power the whole Lab"
url: "https://www.youtube.com/watch?v=lcV9Wvxn6qk"
video_id: "lcV9Wvxn6qk"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-11-15
duration: "30:51"
duration_sec: 1851
views: 10848
likes: 670
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/lcV9Wvxn6qk/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1296
chapters_count: 10
has_description: true
has_comments: false
---

## Description

This video has:
1) instruction to build the battery adapter with USB-C PD, outperforming the market leader
2) breakdown of modules - to access battery directly, send DC power to anything you wish (even jump start your car)
3) identify 3D printed and OTS parts, free CAD downloads
4) purpose of the DC adapter for present and future
5) message to Elon on how to do engineering better.

[links]
CAD model, on grabCAD ► https://grabcad.com/library/terminal_v2-1
Many handybox models ► https://qr.net/openboxproject
My laboratory data ► https://qr.net/openlabproject

If this content helps you, you're welcome to support me on patreon! Link in bio. I love this work but youtube has not generated much revenue this year.  Every help is impactful.

[Chapters]
0:00 the need for USBC
3:22 Printable 3D Model
7:20 wiring the device
10:50 mounting, fasteners
12:50 testing
18:30 gaining functionality
22:09 swap connectors
24:16 open-source versatility
26:25 compete with industry
27:00 message to Elon

## Chapters

- 0:00 the need for USBC
- 3:22 Printable 3D Model
- 7:20 wiring the device
- 10:50 mounting, fasteners
- 12:50 testing
- 18:30 gaining functionality
- 22:09 swap connectors
- 24:16 open-source versatility
- 26:25 compete with industry
- 27:00 message to Elon

## Transcript

[0:01] Okay, here we go. It's going to be a
[0:01] Okay, here we go. It's going to be a knowledge dump. I'm going to show you
[0:03] knowledge dump. I'm going to show you
[0:03] knowledge dump. I'm going to show you how to build a device just like this,
[0:06] how to build a device just like this,
[0:06] how to build a device just like this, but that performs better, costs less.
[0:08] but that performs better, costs less.
[0:08] but that performs better, costs less. This is an $89ish product from Rigid,
[0:12] This is an $89ish product from Rigid,
[0:12] This is an $89ish product from Rigid, sold at Home Depot. It's pretty much a
[0:14] sold at Home Depot. It's pretty much a
[0:14] sold at Home Depot. It's pretty much a class leading offering for getting a PD
[0:18] class leading offering for getting a PD
[0:18] class leading offering for getting a PD USBC PD power delivery output from uh a
[0:22] USBC PD power delivery output from uh a
[0:22] USBC PD power delivery output from uh a power tool battery. And Rigid also has,
[0:25] power tool battery. And Rigid also has,
[0:25] power tool battery. And Rigid also has, I think, the best power tool batteries.
[0:27] I think, the best power tool batteries.
[0:27] I think, the best power tool batteries. You can you can pretty well abuse these
[0:30] You can you can pretty well abuse these
[0:30] You can you can pretty well abuse these things uh because they have thermal
[0:32] things uh because they have thermal
[0:32] things uh because they have thermal control. If you bring it outside in the
[0:34] control. If you bring it outside in the
[0:34] control. If you bring it outside in the hot or the cold, then it shuts off uh if
[0:37] hot or the cold, then it shuts off uh if
[0:37] hot or the cold, then it shuts off uh if it's out of spec for temperature. It has
[0:40] it's out of spec for temperature. It has
[0:40] it's out of spec for temperature. It has a power indicator built in. They have
[0:43] a power indicator built in. They have
[0:43] a power indicator built in. They have lifetime warranty with free replacement.
[0:46] lifetime warranty with free replacement.
[0:46] lifetime warranty with free replacement. And I'm not even uh I'm not even worried
[0:48] And I'm not even uh I'm not even worried
[0:48] And I'm not even uh I'm not even worried about whether we're preferring the rigid
[0:51] about whether we're preferring the rigid
[0:51] about whether we're preferring the rigid cells. I'm uh indicating that when you
[0:55] cells. I'm uh indicating that when you
[0:55] cells. I'm uh indicating that when you have something that is this competitive,
[0:57] have something that is this competitive,
[0:57] have something that is this competitive, there's millions of engineering hours
[0:59] there's millions of engineering hours
[0:59] there's millions of engineering hours behind it. They have a nice big market
[1:01] behind it. They have a nice big market
[1:01] behind it. They have a nice big market share. So, whatever we designed that
[1:03] share. So, whatever we designed that
[1:03] share. So, whatever we designed that goes along with a cell like this, a
[1:06] goes along with a cell like this, a
[1:06] goes along with a cell like this, a battery pack like this becomes
[1:08] battery pack like this becomes
[1:08] battery pack like this becomes incredibly useful immediately because
[1:10] incredibly useful immediately because
[1:10] incredibly useful immediately because other people have the ingredients, the
[1:12] other people have the ingredients, the
[1:12] other people have the ingredients, the components to work uh to produce the
[1:16] components to work uh to produce the
[1:16] components to work uh to produce the same outcome or similar because we've
[1:19] same outcome or similar because we've
[1:19] same outcome or similar because we've already got a standard.
[1:21] already got a standard.
[1:21] already got a standard. Okay. Why uh is it important? Why is
[1:23] Okay. Why uh is it important? Why is
[1:23] Okay. Why uh is it important? Why is this the most important thing for the
[1:25] this the most important thing for the
[1:25] this the most important thing for the device? It's because um getting 45 watts
[1:29] device? It's because um getting 45 watts
[1:29] device? It's because um getting 45 watts out from the USBC
[1:31] out from the USBC
[1:32] out from the USBC is like a high power delivery for new
[1:35] is like a high power delivery for new
[1:35] is like a high power delivery for new appliances. And um in the past, we're
[1:38] appliances. And um in the past, we're
[1:38] appliances. And um in the past, we're looking at something like 10 watts for a
[1:40] looking at something like 10 watts for a
[1:40] looking at something like 10 watts for a USB port, 2 amps, 5 volts, and now we
[1:43] USB port, 2 amps, 5 volts, and now we
[1:43] USB port, 2 amps, 5 volts, and now we can get up to 20 volts or maybe even
[1:46] can get up to 20 volts or maybe even
[1:46] can get up to 20 volts or maybe even more. New appliances are coming out
[1:48] more. New appliances are coming out
[1:48] more. New appliances are coming out continually that can take advantage of
[1:50] continually that can take advantage of
[1:50] continually that can take advantage of that high wattage. And I want to uh
[1:54] that high wattage. And I want to uh
[1:54] that high wattage. And I want to uh reuse all these wonderful batteries to
[1:57] reuse all these wonderful batteries to
[1:57] reuse all these wonderful batteries to do things like soldering. So
[1:59] do things like soldering. So
[1:59] do things like soldering. So [clears throat]
[2:00] [clears throat]
[2:00] [clears throat] when you grab o one of these modern
[2:04] when you grab o one of these modern
[2:04] when you grab o one of these modern soldering irons, um we can go up to 80.
[2:08] soldering irons, um we can go up to 80.
[2:08] soldering irons, um we can go up to 80. Wow, that's so flexible for the input.
[2:10] Wow, that's so flexible for the input.
[2:10] Wow, that's so flexible for the input. But 24 volts, we're going to get around
[2:12] But 24 volts, we're going to get around
[2:12] But 24 volts, we're going to get around 21 volts out of this. and
[2:14] 21 volts out of this. and
[2:14] 21 volts out of this. and [clears throat] crank it up fast. Now,
[2:17] [clears throat] crank it up fast. Now,
[2:17] [clears throat] crank it up fast. Now, Rigid thought the most important thing
[2:18] Rigid thought the most important thing
[2:18] Rigid thought the most important thing here was the inverter, right? So, you
[2:20] here was the inverter, right? So, you
[2:20] here was the inverter, right? So, you can get AC output from here. But with
[2:23] can get AC output from here. But with
[2:23] can get AC output from here. But with all the new things coming onto the
[2:24] all the new things coming onto the
[2:24] all the new things coming onto the market, we're going to use DC directly
[2:26] market, we're going to use DC directly
[2:26] market, we're going to use DC directly for most appliances um when possible
[2:29] for most appliances um when possible
[2:29] for most appliances um when possible because the inverter is just a good way
[2:31] because the inverter is just a good way
[2:31] because the inverter is just a good way to lose 20% of your energy uh all the
[2:35] to lose 20% of your energy uh all the
[2:35] to lose 20% of your energy uh all the time, no matter what. All right. So,
[2:36] time, no matter what. All right. So,
[2:36] time, no matter what. All right. So, another constraint is we got two watts
[2:39] another constraint is we got two watts
[2:39] another constraint is we got two watts of constant draw when this is powered
[2:41] of constant draw when this is powered
[2:41] of constant draw when this is powered on. um you use the machine, you turn
[2:46] on. um you use the machine, you turn
[2:46] on. um you use the machine, you turn press this button to access the power
[2:49] press this button to access the power
[2:49] press this button to access the power and then if you forget to press that
[2:50] and then if you forget to press that
[2:50] and then if you forget to press that again, then you're going to lose the
[2:53] again, then you're going to lose the
[2:53] again, then you're going to lose the next morning, the whole battery will be
[2:55] next morning, the whole battery will be
[2:55] next morning, the whole battery will be drained. Um even if you only used 10% of
[2:58] drained. Um even if you only used 10% of
[2:58] drained. Um even if you only used 10% of it for your work. So we have uh very big
[3:03] it for your work. So we have uh very big
[3:03] it for your work. So we have uh very big shortcoming in my opinion. There's a
[3:05] shortcoming in my opinion. There's a
[3:05] shortcoming in my opinion. There's a reason they designed it that way. It's
[3:07] reason they designed it that way. It's
[3:07] reason they designed it that way. It's because um cuz it's probably worse if
[3:10] because um cuz it's probably worse if
[3:10] because um cuz it's probably worse if you were expecting the machine to work
[3:12] you were expecting the machine to work
[3:12] you were expecting the machine to work and it just timed out while you were
[3:14] and it just timed out while you were
[3:14] and it just timed out while you were pulling power from it. Um but that's not
[3:17] pulling power from it. Um but that's not
[3:17] pulling power from it. Um but that's not my problem. My problem is uh this thing
[3:20] my problem. My problem is uh this thing
[3:20] my problem. My problem is uh this thing quietly draining the energy away. So now
[3:23] quietly draining the energy away. So now
[3:23] quietly draining the energy away. So now you're looking at something called
[3:24] you're looking at something called
[3:24] you're looking at something called terminal V2. This is a new uh build for
[3:29] terminal V2. This is a new uh build for
[3:29] terminal V2. This is a new uh build for the terminal component that I've posted
[3:31] the terminal component that I've posted
[3:31] the terminal component that I've posted on GrabCAD. The first version was um
[3:36] on GrabCAD. The first version was um
[3:36] on GrabCAD. The first version was um only uh it was one piece. It was similar
[3:39] only uh it was one piece. It was similar
[3:39] only uh it was one piece. It was similar to this product that some gentleman um
[3:43] to this product that some gentleman um
[3:43] to this product that some gentleman um designed, built and sold on eBay and
[3:45] designed, built and sold on eBay and
[3:45] designed, built and sold on eBay and Amazon in the past a few years back. So
[3:47] Amazon in the past a few years back. So
[3:47] Amazon in the past a few years back. So I I purchased this without the without
[3:49] I I purchased this without the without
[3:49] I I purchased this without the without the region in my left hand. Um this is a
[3:52] the region in my left hand. Um this is a
[3:52] the region in my left hand. Um this is a scuttle apparatus to give me some ports
[3:54] scuttle apparatus to give me some ports
[3:54] scuttle apparatus to give me some ports and a switch. But uh so it's a popular
[3:58] and a switch. But uh so it's a popular
[3:58] and a switch. But uh so it's a popular device already. People are accessing the
[4:00] device already. People are accessing the
[4:00] device already. People are accessing the power from their batteries. Um, and you
[4:03] power from their batteries. Um, and you
[4:03] power from their batteries. Um, and you have two offtheshelf.
[4:06] have two offtheshelf.
[4:06] have two offtheshelf. These are from something like Mouser.
[4:08] These are from something like Mouser.
[4:08] These are from something like Mouser. You'll find connectors. Those are a
[4:10] You'll find connectors. Those are a
[4:10] You'll find connectors. Those are a little bit challenging to find, but I
[4:11] little bit challenging to find, but I
[4:12] little bit challenging to find, but I found at least a good selection and I've
[4:15] found at least a good selection and I've
[4:15] found at least a good selection and I've open sourced it. So, we're looking at
[4:17] open sourced it. So, we're looking at
[4:17] open sourced it. So, we're looking at Molex 44262
[4:19] Molex 44262
[4:19] Molex 44262 series of connectors.
[4:23] series of connectors.
[4:23] series of connectors. And then, um, a geometry here in this 3D
[4:26] And then, um, a geometry here in this 3D
[4:26] And then, um, a geometry here in this 3D printed device that lets you slide them
[4:29] printed device that lets you slide them
[4:29] printed device that lets you slide them in. And then I've done uh when you cover
[4:32] in. And then I've done uh when you cover
[4:32] in. And then I've done uh when you cover it up, it's going to cover them, prevent
[4:34] it up, it's going to cover them, prevent
[4:34] it up, it's going to cover them, prevent them from falling out. The base of these
[4:37] them from falling out. The base of these
[4:37] them from falling out. The base of these connectors is seated into the 3D
[4:39] connectors is seated into the 3D
[4:39] connectors is seated into the 3D plastic. So, this is printable with no
[4:41] plastic. So, this is printable with no
[4:41] plastic. So, this is printable with no supports as always, per my 3D printing
[4:44] supports as always, per my 3D printing
[4:44] supports as always, per my 3D printing design rules. Um, and it'll operate just
[4:47] design rules. Um, and it'll operate just
[4:47] design rules. Um, and it'll operate just by itself. So, you can hook this up.
[4:51] by itself. So, you can hook this up.
[4:51] by itself. So, you can hook this up. It's going to slide in here and those
[4:54] It's going to slide in here and those
[4:54] It's going to slide in here and those terminals will go. If you download this
[4:56] terminals will go. If you download this
[4:56] terminals will go. If you download this model, then there's part A and B
[5:00] model, then there's part A and B
[5:00] model, then there's part A and B essentially. A is here. You can print
[5:02] essentially. A is here. You can print
[5:02] essentially. A is here. You can print this out and now you can get access. You
[5:04] this out and now you can get access. You
[5:04] this out and now you can get access. You can crimp your own terminals
[5:06] can crimp your own terminals
[5:06] can crimp your own terminals [clears throat] to your own wires. These
[5:08] [clears throat] to your own wires. These
[5:08] [clears throat] to your own wires. These are I think uh common for all my
[5:11] are I think uh common for all my
[5:11] are I think uh common for all my projects is 18 gauge and this is a
[5:13] projects is 18 gauge and this is a
[5:13] projects is 18 gauge and this is a little bit larger. So, call it 14 gauge.
[5:16] little bit larger. So, call it 14 gauge.
[5:16] little bit larger. So, call it 14 gauge. That's enough to carry at least 20 amps.
[5:19] That's enough to carry at least 20 amps.
[5:19] That's enough to carry at least 20 amps. And our [snorts] Anderson connector.
[5:20] And our [snorts] Anderson connector.
[5:20] And our [snorts] Anderson connector. This is just one way to connect. Um, in
[5:24] This is just one way to connect. Um, in
[5:24] This is just one way to connect. Um, in any case, once you have
[5:27] any case, once you have
[5:27] any case, once you have this module, this is the simplest
[5:30] this module, this is the simplest
[5:30] this module, this is the simplest possible geometry to both connect into
[5:35] possible geometry to both connect into
[5:35] possible geometry to both connect into your battery. The minimal amount of
[5:38] your battery. The minimal amount of
[5:38] your battery. The minimal amount of material and complexity to access those
[5:41] material and complexity to access those
[5:41] material and complexity to access those terminals, get power, and then you have
[5:44] terminals, get power, and then you have
[5:44] terminals, get power, and then you have something when you combine them, you
[5:46] something when you combine them, you
[5:46] something when you combine them, you have something that's a little bit
[5:47] have something that's a little bit
[5:47] have something that's a little bit closer to these go together like that.
[5:51] closer to these go together like that.
[5:51] closer to these go together like that. It is one CAD model to have both of
[5:54] It is one CAD model to have both of
[5:54] It is one CAD model to have both of these uh with two bodies. Um two solid
[5:59] these uh with two bodies. Um two solid
[5:59] these uh with two bodies. Um two solid bodies as in Solid Works. Um so these go
[6:02] bodies as in Solid Works. Um so these go
[6:02] bodies as in Solid Works. Um so these go together and then a screw. If you want
[6:05] together and then a screw. If you want
[6:05] together and then a screw. If you want them permanent then you can fasten the
[6:07] them permanent then you can fasten the
[6:07] them permanent then you can fasten the screw in the left hand and the right
[6:08] screw in the left hand and the right
[6:08] screw in the left hand and the right hand that's M2.5 and it'll go in here.
[6:12] hand that's M2.5 and it'll go in here.
[6:12] hand that's M2.5 and it'll go in here. Okay. So, we can work with these
[6:14] Okay. So, we can work with these
[6:14] Okay. So, we can work with these separately, which gives us a lot of
[6:16] separately, which gives us a lot of
[6:16] separately, which gives us a lot of freedom for new designs, more um
[6:20] freedom for new designs, more um
[6:20] freedom for new designs, more um flexible assembly, but also grab this
[6:23] flexible assembly, but also grab this
[6:24] flexible assembly, but also grab this open model and adapt it to make the
[6:26] open model and adapt it to make the
[6:26] open model and adapt it to make the thing that you want with the type of
[6:27] thing that you want with the type of
[6:27] thing that you want with the type of terminals you want or grab this one and
[6:30] terminals you want or grab this one and
[6:30] terminals you want or grab this one and uh attach whatever you want. Here's a
[6:33] uh attach whatever you want. Here's a
[6:33] uh attach whatever you want. Here's a quick demonstration. We choose uh
[6:35] quick demonstration. We choose uh
[6:35] quick demonstration. We choose uh vehicle lamps. nice, beautiful, u rigid
[6:39] vehicle lamps. nice, beautiful, u rigid
[6:39] vehicle lamps. nice, beautiful, u rigid uh lamp with a good brightness and
[6:41] uh lamp with a good brightness and
[6:41] uh lamp with a good brightness and aluminum housing. This is going to be a
[6:44] aluminum housing. This is going to be a
[6:44] aluminum housing. This is going to be a lifetime device and it'll work just like
[6:47] lifetime device and it'll work just like
[6:48] lifetime device and it'll work just like the the ones they sell for power tools,
[6:50] the the ones they sell for power tools,
[6:50] the the ones they sell for power tools, but now it's flexible. You could do two
[6:53] but now it's flexible. You could do two
[6:53] but now it's flexible. You could do two of these in parallel and this is easily
[6:56] of these in parallel and this is easily
[6:56] of these in parallel and this is easily going to provide the power that you
[6:58] going to provide the power that you
[6:58] going to provide the power that you need. Now, where do we want to attach
[6:59] need. Now, where do we want to attach
[6:59] need. Now, where do we want to attach this? Somebody might want it on a big
[7:01] this? Somebody might want it on a big
[7:01] this? Somebody might want it on a big lever. Somebody might want it mounted
[7:03] lever. Somebody might want it mounted
[7:04] lever. Somebody might want it mounted very closely to the battery so the mass
[7:07] very closely to the battery so the mass
[7:07] very closely to the battery so the mass of the battery can be the stabilizing
[7:09] of the battery can be the stabilizing
[7:09] of the battery can be the stabilizing thing. All right.
[7:12] thing. All right.
[7:12] thing. All right. So the next step will be to take these
[7:15] So the next step will be to take these
[7:15] So the next step will be to take these combine them
[7:18] combine them
[7:18] combine them and [snorts] that will get you this. So
[7:21] and [snorts] that will get you this. So
[7:21] and [snorts] that will get you this. So we've connected the terminals. We've
[7:23] we've connected the terminals. We've
[7:23] we've connected the terminals. We've passed them through the two holes in um
[7:27] passed them through the two holes in um
[7:27] passed them through the two holes in um body B version 3.3.
[7:30] body B version 3.3.
[7:30] body B version 3.3. And then we're gonna have um the wires
[7:33] And then we're gonna have um the wires
[7:33] And then we're gonna have um the wires routed wherever we want. And we're going
[7:36] routed wherever we want. And we're going
[7:36] routed wherever we want. And we're going to get these two holes on our handy box.
[7:39] to get these two holes on our handy box.
[7:39] to get these two holes on our handy box. This is an off-the-shelf $2.5
[7:43] This is an off-the-shelf $2.5
[7:43] This is an off-the-shelf $2.5 um device uh electrical outlet box. It's
[7:48] um device uh electrical outlet box. It's
[7:48] um device uh electrical outlet box. It's very very standard, very available.
[7:50] very very standard, very available.
[7:50] very very standard, very available. Sorry, it's more oriented towards North
[7:52] Sorry, it's more oriented towards North
[7:52] Sorry, it's more oriented towards North America. Canada has another slight
[7:55] America. Canada has another slight
[7:55] America. Canada has another slight variation. And uh I don't know what all
[7:58] variation. And uh I don't know what all
[7:58] variation. And uh I don't know what all is going on in Europe, but we're trying
[8:01] is going on in Europe, but we're trying
[8:01] is going on in Europe, but we're trying to handle we're trying to help you guys
[8:02] to handle we're trying to help you guys
[8:02] to handle we're trying to help you guys too. Uh Europeans, I'm sure there's an
[8:04] too. Uh Europeans, I'm sure there's an
[8:04] too. Uh Europeans, I'm sure there's an engineer that can come up with something
[8:07] engineer that can come up with something
[8:07] engineer that can come up with something along these lines. And the again, open-
[8:10] along these lines. And the again, open-
[8:10] along these lines. And the again, open- source geometry means maybe you can just
[8:13] source geometry means maybe you can just
[8:13] source geometry means maybe you can just adjust one little feature like these and
[8:15] adjust one little feature like these and
[8:15] adjust one little feature like these and the holes to get compatibility. All
[8:18] the holes to get compatibility. All
[8:18] the holes to get compatibility. All right. So now you've got wires in a box
[8:21] right. So now you've got wires in a box
[8:21] right. So now you've got wires in a box and probably 500 watts you could pass
[8:24] and probably 500 watts you could pass
[8:24] and probably 500 watts you could pass through here. So, what happens next? I
[8:27] through here. So, what happens next? I
[8:27] through here. So, what happens next? I just got done painting this. So, we're
[8:29] just got done painting this. So, we're
[8:29] just got done painting this. So, we're going to reintroduce those Anderson
[8:31] going to reintroduce those Anderson
[8:31] going to reintroduce those Anderson ports. Okay. So, now we can uh just plug
[8:36] ports. Okay. So, now we can uh just plug
[8:36] ports. Okay. So, now we can uh just plug in like we wanted to before. And then we
[8:39] in like we wanted to before. And then we
[8:39] in like we wanted to before. And then we have this device. It may be called a
[8:42] have this device. It may be called a
[8:42] have this device. It may be called a cigarette lighter or a car power outlet,
[8:46] cigarette lighter or a car power outlet,
[8:46] cigarette lighter or a car power outlet, something along those lines. But this
[8:48] something along those lines. But this
[8:48] something along those lines. But this will be added into that hole. Um,
[8:52] will be added into that hole. Um,
[8:52] will be added into that hole. Um, fastened down, but still removable.
[8:54] fastened down, but still removable.
[8:54] fastened down, but still removable. removable mechanically and electrically.
[8:57] removable mechanically and electrically.
[8:57] removable mechanically and electrically. And then we are going to add our USBC
[9:01] And then we are going to add our USBC
[9:01] And then we are going to add our USBC power delivery uh adapter that gives 65
[9:05] power delivery uh adapter that gives 65
[9:05] power delivery uh adapter that gives 65 watts. So our device will have higher
[9:08] watts. So our device will have higher
[9:08] watts. So our device will have higher performance than the market leading
[9:10] performance than the market leading
[9:10] performance than the market leading off-the-shelf device, costs less and is
[9:14] off-the-shelf device, costs less and is
[9:14] off-the-shelf device, costs less and is updatable because you can change this
[9:16] updatable because you can change this
[9:16] updatable because you can change this next year when you when a new gadget
[9:18] next year when you when a new gadget
[9:18] next year when you when a new gadget comes out. So let's build.
[9:21] comes out. So let's build.
[9:21] comes out. So let's build. Um, this little piece of PVC is just
[9:24] Um, this little piece of PVC is just
[9:24] Um, this little piece of PVC is just helping to uh adjust. We want our
[9:27] helping to uh adjust. We want our
[9:27] helping to uh adjust. We want our fastener to not tighten down all the way
[9:29] fastener to not tighten down all the way
[9:29] fastener to not tighten down all the way to this radius where it it kind of um
[9:33] to this radius where it it kind of um
[9:33] to this radius where it it kind of um bumps up against the corners interiorly
[9:36] bumps up against the corners interiorly
[9:36] bumps up against the corners interiorly in the interior corners. Um, so this is
[9:40] in the interior corners. Um, so this is
[9:40] in the interior corners. Um, so this is just a spacer. You can craft that out of
[9:42] just a spacer. You can craft that out of
[9:42] just a spacer. You can craft that out of anything that you want. And then we're
[9:44] anything that you want. And then we're
[9:44] anything that you want. And then we're going to get our uh
[9:47] going to get our uh
[9:47] going to get our uh big uh round nut thing. You can tighten
[9:50] big uh round nut thing. You can tighten
[9:50] big uh round nut thing. You can tighten that by hand and it'll probably be
[9:52] that by hand and it'll probably be
[9:52] that by hand and it'll probably be sufficient. Um, definitely going to be
[9:55] sufficient. Um, definitely going to be
[9:55] sufficient. Um, definitely going to be sufficient for today so I can get
[9:57] sufficient for today so I can get
[9:57] sufficient for today so I can get through this tutorial. All right. So now
[9:59] through this tutorial. All right. So now
[9:59] through this tutorial. All right. So now we have Anderson on one side. We have
[10:01] we have Anderson on one side. We have
[10:02] we have Anderson on one side. We have leads because we have made a Y junction.
[10:05] leads because we have made a Y junction.
[10:05] leads because we have made a Y junction. Your wires um use basic soldering
[10:08] Your wires um use basic soldering
[10:08] Your wires um use basic soldering skills. Heat shrink that carefully. And
[10:11] skills. Heat shrink that carefully. And
[10:11] skills. Heat shrink that carefully. And then you'll have red for 20 volts, black
[10:15] then you'll have red for 20 volts, black
[10:15] then you'll have red for 20 volts, black for um zero. All right. So, I'm going to
[10:21] for um zero. All right. So, I'm going to
[10:21] for um zero. All right. So, I'm going to stick that down.
[10:24] stick that down.
[10:24] stick that down. We're going to get that connected. And
[10:26] We're going to get that connected. And
[10:26] We're going to get that connected. And then it'll be a matter of just coiling
[10:29] then it'll be a matter of just coiling
[10:29] then it'll be a matter of just coiling these wires neatly enough.
[10:31] these wires neatly enough.
[10:31] these wires neatly enough. And you want to do this while the
[10:33] And you want to do this while the
[10:33] And you want to do this while the battery is not connected. Uh coiling
[10:36] battery is not connected. Uh coiling
[10:36] battery is not connected. Uh coiling these
[10:37] these
[10:37] these pack these wires into the apparatus,
[10:40] pack these wires into the apparatus,
[10:40] pack these wires into the apparatus, which is also why, you know, the handy
[10:43] which is also why, you know, the handy
[10:43] which is also why, you know, the handy box is larger than it must be to work
[10:45] box is larger than it must be to work
[10:46] box is larger than it must be to work for this design. But it sure is nice to
[10:48] for this design. But it sure is nice to
[10:48] for this design. But it sure is nice to have plenty of extra space to pack wires
[10:52] have plenty of extra space to pack wires
[10:52] have plenty of extra space to pack wires um instead of making it too tight,
[10:56] um instead of making it too tight,
[10:56] um instead of making it too tight, basically. All right, so I'm just
[10:59] basically. All right, so I'm just
[10:59] basically. All right, so I'm just looking for my holes. There we are.
[11:02] looking for my holes. There we are.
[11:02] looking for my holes. There we are. We're lined up. And okay, so the screws
[11:07] We're lined up. And okay, so the screws
[11:07] We're lined up. And okay, so the screws we're using M4 metric screws, which are
[11:11] we're using M4 metric screws, which are
[11:11] we're using M4 metric screws, which are just slightly larger than the size that
[11:13] just slightly larger than the size that
[11:13] just slightly larger than the size that comes with I think this is 832. 8-32. a
[11:17] comes with I think this is 832. 8-32. a
[11:17] comes with I think this is 832. 8-32. a number eight screw. That's an imperial
[11:19] number eight screw. That's an imperial
[11:19] number eight screw. That's an imperial thread. Thanks, Britain. Um, and I've uh
[11:23] thread. Thanks, Britain. Um, and I've uh
[11:23] thread. Thanks, Britain. Um, and I've uh boarded out or I I've retapped it so
[11:25] boarded out or I I've retapped it so
[11:25] boarded out or I I've retapped it so that it's now metric 4 mm. And that
[11:29] that it's now metric 4 mm. And that
[11:29] that it's now metric 4 mm. And that gives us a little bit better clamping
[11:32] gives us a little bit better clamping
[11:32] gives us a little bit better clamping force
[11:34] force
[11:34] force between the screw and
[11:37] between the screw and
[11:37] between the screw and the electric gizmo.
[11:48] You can maybe see the the screw reaching
[11:48] You can maybe see the the screw reaching in there thanks to that small gap right
[11:50] in there thanks to that small gap right
[11:50] in there thanks to that small gap right there. And then we're going to put
[11:52] there. And then we're going to put
[11:52] there. And then we're going to put another one over here. And I used this
[11:54] another one over here. And I used this
[11:54] another one over here. And I used this one's counter sunk, but most you it's
[11:57] one's counter sunk, but most you it's
[11:57] one's counter sunk, but most you it's intended for a a flatheaded
[12:00] intended for a a flatheaded
[12:00] intended for a a flatheaded screw.
[12:03] screw.
[12:03] screw. Okay. So, now we're fastened. We have
[12:06] Okay. So, now we're fastened. We have
[12:06] Okay. So, now we're fastened. We have one unit. Um, and these screws are M2.5,
[12:12] one unit. Um, and these screws are M2.5,
[12:12] one unit. Um, and these screws are M2.5, they've already been threaded in, they
[12:14] they've already been threaded in, they
[12:14] they've already been threaded in, they don't even uh we just have a slightly
[12:16] don't even uh we just have a slightly
[12:16] don't even uh we just have a slightly unders sized hole. And because we're not
[12:19] unders sized hole. And because we're not
[12:19] unders sized hole. And because we're not uh going to encounter pull out forces,
[12:22] uh going to encounter pull out forces,
[12:22] uh going to encounter pull out forces, we just need those really to act like a
[12:24] we just need those really to act like a
[12:24] we just need those really to act like a pin. So, there's just little
[12:25] pin. So, there's just little
[12:25] pin. So, there's just little interference between the plastic and
[12:27] interference between the plastic and
[12:27] interference between the plastic and this hole and that screw. And that's
[12:29] this hole and that screw. And that's
[12:29] this hole and that screw. And that's sufficient for this design. We don't
[12:31] sufficient for this design. We don't
[12:31] sufficient for this design. We don't need to have uh carefully thought out
[12:33] need to have uh carefully thought out
[12:33] need to have uh carefully thought out threads or a heat set insert, etc. All
[12:37] threads or a heat set insert, etc. All
[12:37] threads or a heat set insert, etc. All right. All right. So, now we should be
[12:38] right. All right. So, now we should be
[12:38] right. All right. So, now we should be looking for the light to light up when I
[12:41] looking for the light to light up when I
[12:41] looking for the light to light up when I slide this on. We have this little
[12:43] slide this on. We have this little
[12:43] slide this on. We have this little pocket here just carefully placed not to
[12:47] pocket here just carefully placed not to
[12:47] pocket here just carefully placed not to interfere with the with the screw, but
[12:49] interfere with the with the screw, but
[12:49] interfere with the with the screw, but also still to match up to these um
[12:53] also still to match up to these um
[12:54] also still to match up to these um springy things.
[13:03] Now, we're lit up. Okay, we have
[13:03] Now, we're lit up. Okay, we have Anderson.
[13:05] Anderson.
[13:05] Anderson. And then we should get an that the green
[13:07] And then we should get an that the green
[13:07] And then we should get an that the green light plus our I think blue light on
[13:10] light plus our I think blue light on
[13:10] light plus our I think blue light on this one. Boom. Okay. So, the beauty of
[13:13] this one. Boom. Okay. So, the beauty of
[13:13] this one. Boom. Okay. So, the beauty of this is I've already tested the power by
[13:15] this is I've already tested the power by
[13:15] this is I've already tested the power by separating the device from the battery.
[13:19] separating the device from the battery.
[13:19] separating the device from the battery. We get we're pulling less than one watt.
[13:22] We get we're pulling less than one watt.
[13:22] We get we're pulling less than one watt. Um, and I've already tested that. So,
[13:25] Um, and I've already tested that. So,
[13:25] Um, and I've already tested that. So, we'll have twice as much life leaving
[13:28] we'll have twice as much life leaving
[13:28] we'll have twice as much life leaving this on. And you can also make a
[13:31] this on. And you can also make a
[13:31] this on. And you can also make a variation on this if you want to switch
[13:34] variation on this if you want to switch
[13:34] variation on this if you want to switch off the the power entirely.
[13:38] off the the power entirely.
[13:38] off the the power entirely. I've built this also on with a switch.
[13:41] I've built this also on with a switch.
[13:41] I've built this also on with a switch. So, this will isolate completely the
[13:43] So, this will isolate completely the
[13:43] So, this will isolate completely the battery from anything on the outputs.
[13:45] battery from anything on the outputs.
[13:45] battery from anything on the outputs. This one doesn't have the cigarette
[13:46] This one doesn't have the cigarette
[13:46] This one doesn't have the cigarette lighter. Um, it just has Anderson and
[13:50] lighter. Um, it just has Anderson and
[13:50] lighter. Um, it just has Anderson and does the same thing. Then this, uh,
[13:53] does the same thing. Then this, uh,
[13:53] does the same thing. Then this, uh, metal shell, which I've painted gloss
[13:55] metal shell, which I've painted gloss
[13:55] metal shell, which I've painted gloss black, matte black. um that becomes a
[13:59] black, matte black. um that becomes a
[13:59] black, matte black. um that becomes a mounting feature where you can go and
[14:02] mounting feature where you can go and
[14:02] mounting feature where you can go and build your next design uh feature. So,
[14:05] build your next design uh feature. So,
[14:05] build your next design uh feature. So, if I want to mount this on, I could bore
[14:07] if I want to mount this on, I could bore
[14:07] if I want to mount this on, I could bore out one of those holes just slightly and
[14:09] out one of those holes just slightly and
[14:09] out one of those holes just slightly and thread this in. And it's still I can
[14:11] thread this in. And it's still I can
[14:11] thread this in. And it's still I can still change my mind if I want to. Um
[14:14] still change my mind if I want to. Um
[14:14] still change my mind if I want to. Um and just having that rigid wall is
[14:17] and just having that rigid wall is
[14:17] and just having that rigid wall is fantastic for adding new things. It's
[14:19] fantastic for adding new things. It's
[14:19] fantastic for adding new things. It's much much nicer than having just a a
[14:22] much much nicer than having just a a
[14:22] much much nicer than having just a a plastic 3D printed housing. Um, so
[14:25] plastic 3D printed housing. Um, so
[14:25] plastic 3D printed housing. Um, so Handybox help us helps us out again. Now
[14:28] Handybox help us helps us out again. Now
[14:28] Handybox help us helps us out again. Now let's just quickly demonstrate with the
[14:32] let's just quickly demonstrate with the
[14:32] let's just quickly demonstrate with the uh USB device.
[14:45] This lovely cord here has just been way
[14:45] This lovely cord here has just been way more valuable than I expected when I
[14:47] more valuable than I expected when I
[14:47] more valuable than I expected when I bought it. So I bought another one. It's
[14:49] bought it. So I bought another one. It's
[14:49] bought it. So I bought another one. It's going to when we power something on,
[14:52] going to when we power something on,
[14:52] going to when we power something on, it'll tell us the power level uh within
[14:55] it'll tell us the power level uh within
[14:55] it'll tell us the power level uh within something like 0.1 watts. So, and it'll
[14:59] something like 0.1 watts. So, and it'll
[14:59] something like 0.1 watts. So, and it'll indicate PD if we're doing the P power
[15:01] indicate PD if we're doing the P power
[15:01] indicate PD if we're doing the P power delivery communication that asks for a
[15:03] delivery communication that asks for a
[15:03] delivery communication that asks for a voltage besides 5 volts. That's how PD
[15:06] voltage besides 5 volts. That's how PD
[15:06] voltage besides 5 volts. That's how PD works. Um, okay. So, if I press right
[15:10] works. Um, okay. So, if I press right
[15:10] works. Um, okay. So, if I press right here, I think it's going to go for 350°,
[15:13] here, I think it's going to go for 350°,
[15:13] here, I think it's going to go for 350°, 12 watts, 52 watts.
[15:17] 12 watts, 52 watts.
[15:17] 12 watts, 52 watts. Add a boy. Okay, so we have exceeded the
[15:20] Add a boy. Okay, so we have exceeded the
[15:20] Add a boy. Okay, so we have exceeded the rated power of the rigid device.
[15:24] rated power of the rigid device.
[15:24] rated power of the rigid device. We're getting really the most we could
[15:26] We're getting really the most we could
[15:26] We're getting really the most we could get. Look, we're already at 370
[15:29] get. Look, we're already at 370
[15:29] get. Look, we're already at 370 degrees on this iron. And that's not
[15:32] degrees on this iron. And that's not
[15:32] degrees on this iron. And that's not even a real small uh when you have this
[15:35] even a real small uh when you have this
[15:35] even a real small uh when you have this amount of power on your and it's an
[15:39] amount of power on your and it's an
[15:39] amount of power on your and it's an efficient uh soldering iron, you can do
[15:41] efficient uh soldering iron, you can do
[15:42] efficient uh soldering iron, you can do a lot more. And so this uh this is I I
[15:46] a lot more. And so this uh this is I I
[15:46] a lot more. And so this uh this is I I think for all the range of soldering to
[15:48] think for all the range of soldering to
[15:48] think for all the range of soldering to be done, this will accommodate twice as
[15:51] be done, this will accommodate twice as
[15:51] be done, this will accommodate twice as many things as one of our lowcost Weller
[15:54] many things as one of our lowcost Weller
[15:54] many things as one of our lowcost Weller devices.
[16:01] All right. So this is 42 watts, but
[16:02] All right. So this is 42 watts, but that's the power draw. That doesn't uh
[16:05] that's the power draw. That doesn't uh
[16:05] that's the power draw. That doesn't uh talk about how much heat reaches the
[16:07] talk about how much heat reaches the
[16:07] talk about how much heat reaches the tip. And so that's a specialized tip.
[16:10] tip. And so that's a specialized tip.
[16:10] tip. And so that's a specialized tip. But anyway, we have on a on a device
[16:12] But anyway, we have on a on a device
[16:12] But anyway, we have on a on a device like this, um, it is less efficient in
[16:16] like this, um, it is less efficient in
[16:16] like this, um, it is less efficient in that more heat is exiting along this
[16:18] that more heat is exiting along this
[16:18] that more heat is exiting along this steel zone and we get less heat at the
[16:21] steel zone and we get less heat at the
[16:21] steel zone and we get less heat at the tip, right where we need it. And this
[16:24] tip, right where we need it. And this
[16:24] tip, right where we need it. And this one, it's just wonderful. Um, so the
[16:28] one, it's just wonderful. Um, so the
[16:28] one, it's just wonderful. Um, so the prices of these are going down. There
[16:30] prices of these are going down. There
[16:30] prices of these are going down. There are similar brands besides this one.
[16:32] are similar brands besides this one.
[16:32] are similar brands besides this one. This one, uh, is Pine Sill. So I'm happy
[16:35] This one, uh, is Pine Sill. So I'm happy
[16:35] This one, uh, is Pine Sill. So I'm happy with this one. I was happy with the
[16:37] with this one. I was happy with the
[16:37] with this one. I was happy with the other. Um, all right. And now it's only
[16:40] other. Um, all right. And now it's only
[16:40] other. Um, all right. And now it's only taking 11 watts to maintain the
[16:42] taking 11 watts to maintain the
[16:42] taking 11 watts to maintain the temperature. Um, let's go on to the next
[16:46] temperature. Um, let's go on to the next
[16:46] temperature. Um, let's go on to the next feature. So, while we're still heating
[16:48] feature. So, while we're still heating
[16:48] feature. So, while we're still heating up the iron, we can we can No, we better
[16:52] up the iron, we can we can No, we better
[16:52] up the iron, we can we can No, we better make sure this is turned off. Yeah,
[16:53] make sure this is turned off. Yeah,
[16:53] make sure this is turned off. Yeah, that's off. We have an adapter that's
[16:55] that's off. We have an adapter that's
[16:55] that's off. We have an adapter that's going to pretend it's this is called
[16:57] going to pretend it's this is called
[16:57] going to pretend it's this is called dummy. It's a dummy for a battery. So,
[16:59] dummy. It's a dummy for a battery. So,
[16:59] dummy. It's a dummy for a battery. So, it'll still send the power, but there's
[17:00] it'll still send the power, but there's
[17:00] it'll still send the power, but there's obviously no battery there. We're going
[17:02] obviously no battery there. We're going
[17:02] obviously no battery there. We're going to get our power from somewhere else.
[17:04] to get our power from somewhere else.
[17:04] to get our power from somewhere else. And then we're going to power that on.
[17:07] And then we're going to power that on.
[17:07] And then we're going to power that on. Oh, yeah.
[17:19] And so there you have it. You do not
[17:19] And so there you have it. You do not have a DC power out feature on this. And
[17:23] have a DC power out feature on this. And
[17:23] have a DC power out feature on this. And it's to me the DC out is more valuable.
[17:27] it's to me the DC out is more valuable.
[17:27] it's to me the DC out is more valuable. Um so uh we've beat the the market
[17:31] Um so uh we've beat the the market
[17:31] Um so uh we've beat the the market leader for less cost and it's open
[17:33] leader for less cost and it's open
[17:33] leader for less cost and it's open source. Um,
[17:36] source. Um,
[17:36] source. Um, in the coming years, I think you will
[17:39] in the coming years, I think you will
[17:39] in the coming years, I think you will find more and more gadgets just wanting
[17:41] find more and more gadgets just wanting
[17:41] find more and more gadgets just wanting the direct power in the range of 18 to
[17:45] the direct power in the range of 18 to
[17:45] the direct power in the range of 18 to it's rated at 18 volts. It goes up to
[17:47] it's rated at 18 volts. It goes up to
[17:47] it's rated at 18 volts. It goes up to 21. This one, while I'm running it,
[17:50] 21. This one, while I'm running it,
[17:50] 21. This one, while I'm running it, well, I can demonstrate. I'm going to
[17:53] well, I can demonstrate. I'm going to
[17:53] well, I can demonstrate. I'm going to hook up this meter.
[17:55] hook up this meter.
[17:56] hook up this meter. Okay. And then we're going to look at
[17:58] Okay. And then we're going to look at
[17:58] Okay. And then we're going to look at how much power gets pulled, how many
[18:00] how much power gets pulled, how many
[18:00] how much power gets pulled, how many amps. We're starting at 20.5 volts.
[18:09] So when we draw 150 watts, this comes
[18:09] So when we draw 150 watts, this comes down by half a volt. Um this is a
[18:11] down by half a volt. Um this is a
[18:11] down by half a volt. Um this is a healthy battery though. This one, yeah,
[18:14] healthy battery though. This one, yeah,
[18:14] healthy battery though. This one, yeah, uh a more aged battery or more used up
[18:17] uh a more aged battery or more used up
[18:17] uh a more aged battery or more used up one would probably drop more than that.
[18:20] one would probably drop more than that.
[18:20] one would probably drop more than that. Um in any case, now we have sufficient
[18:22] Um in any case, now we have sufficient
[18:22] Um in any case, now we have sufficient power and sharper new uh tools on our
[18:27] power and sharper new uh tools on our
[18:27] power and sharper new uh tools on our jigsaws and routers and many things. We
[18:29] jigsaws and routers and many things. We
[18:29] jigsaws and routers and many things. We can cut metal with these types of
[18:31] can cut metal with these types of
[18:31] can cut metal with these types of things. Um there's so much uh so far
[18:36] things. Um there's so much uh so far
[18:36] things. Um there's so much uh so far that we can go um working with some of
[18:40] that we can go um working with some of
[18:40] that we can go um working with some of the traditional tools in brand new ways.
[18:43] the traditional tools in brand new ways.
[18:43] the traditional tools in brand new ways. And so this is why in this lab overall I
[18:46] And so this is why in this lab overall I
[18:46] And so this is why in this lab overall I want to get uh new modular jigs to hold
[18:49] want to get uh new modular jigs to hold
[18:49] want to get uh new modular jigs to hold this and make this into a benchtop tool.
[18:51] this and make this into a benchtop tool.
[18:51] this and make this into a benchtop tool. I've spoken about that a little bit in
[18:53] I've spoken about that a little bit in
[18:53] I've spoken about that a little bit in short videos, but um imagine now we have
[18:57] short videos, but um imagine now we have
[18:57] short videos, but um imagine now we have some sort of tabletop. Can we bracket
[19:00] some sort of tabletop. Can we bracket
[19:00] some sort of tabletop. Can we bracket this onto uh a flat steel rigid surface?
[19:05] this onto uh a flat steel rigid surface?
[19:05] this onto uh a flat steel rigid surface? Can we do the same with the jigsaw? Can
[19:07] Can we do the same with the jigsaw? Can
[19:07] Can we do the same with the jigsaw? Can we roll these out to areas where we have
[19:10] we roll these out to areas where we have
[19:10] we roll these out to areas where we have to do the work? Um the initial purpose
[19:14] to do the work? Um the initial purpose
[19:14] to do the work? Um the initial purpose of this was uh well, the most recent
[19:17] of this was uh well, the most recent
[19:17] of this was uh well, the most recent need I had was to do some soldering in
[19:19] need I had was to do some soldering in
[19:19] need I had was to do some soldering in the in my car in the vehicle. I've got
[19:22] the in my car in the vehicle. I've got
[19:22] the in my car in the vehicle. I've got to disconnect the battery and solder on
[19:23] to disconnect the battery and solder on
[19:23] to disconnect the battery and solder on a wire. Then where am I going to get
[19:26] a wire. Then where am I going to get
[19:26] a wire. Then where am I going to get that power? I don't want to run
[19:29] that power? I don't want to run
[19:29] that power? I don't want to run [clears throat]
[19:30] [clears throat]
[19:30] [clears throat] extension cords like I would need to
[19:32] extension cords like I would need to
[19:32] extension cords like I would need to back in the old days with something like
[19:34] back in the old days with something like
[19:34] back in the old days with something like this.
[19:41] So, um, we don't have to use Anderson if
[19:41] So, um, we don't have to use Anderson if that's not your favorite connector, but
[19:43] that's not your favorite connector, but
[19:43] that's not your favorite connector, but that's just what I'm going to commonize
[19:45] that's just what I'm going to commonize
[19:45] that's just what I'm going to commonize across the the scuttle robotics
[19:47] across the the scuttle robotics
[19:47] across the the scuttle robotics equipment, the lab equipment, and um,
[19:52] equipment, the lab equipment, and um,
[19:52] equipment, the lab equipment, and um, instrumentation. So, let's say you don't
[19:55] instrumentation. So, let's say you don't
[19:55] instrumentation. So, let's say you don't have this socket on this end.
[19:59] have this socket on this end.
[19:59] have this socket on this end. By the way, I'll show you about I'm I'm
[20:01] By the way, I'll show you about I'm I'm
[20:01] By the way, I'll show you about I'm I'm really pleased with this um with this
[20:03] really pleased with this um with this
[20:03] really pleased with this um with this adapter that's only $10 and it's made by
[20:07] adapter that's only $10 and it's made by
[20:07] adapter that's only $10 and it's made by a little knockoff brand that seems to do
[20:09] a little knockoff brand that seems to do
[20:09] a little knockoff brand that seems to do really high quality work. I I haven't
[20:11] really high quality work. I I haven't
[20:11] really high quality work. I I haven't heard of them until this week. This
[20:13] heard of them until this week. This
[20:13] heard of them until this week. This one's called Akeer. So, uh, there's
[20:17] one's called Akeer. So, uh, there's
[20:17] one's called Akeer. So, uh, there's gallium nitride involved and I just know
[20:19] gallium nitride involved and I just know
[20:19] gallium nitride involved and I just know that because they're so, um, it's so
[20:22] that because they're so, um, it's so
[20:22] that because they're so, um, it's so compact and it is ever more efficient.
[20:26] compact and it is ever more efficient.
[20:26] compact and it is ever more efficient. Uh, every year I'm finding these at
[20:28] Uh, every year I'm finding these at
[20:28] Uh, every year I'm finding these at something like 95% efficiency, the power
[20:31] something like 95% efficiency, the power
[20:31] something like 95% efficiency, the power in versus power going out. And the when
[20:35] in versus power going out. And the when
[20:35] in versus power going out. And the when you take 18 volts and drop it down to 12
[20:37] you take 18 volts and drop it down to 12
[20:38] you take 18 volts and drop it down to 12 volts, if I want 12 or 5 volts coming
[20:39] volts, if I want 12 or 5 volts coming
[20:39] volts, if I want 12 or 5 volts coming out of here, dropping down is much more
[20:42] out of here, dropping down is much more
[20:42] out of here, dropping down is much more efficient than going up. And so for uh
[20:45] efficient than going up. And so for uh
[20:45] efficient than going up. And so for uh years of projects where I needed just
[20:48] years of projects where I needed just
[20:48] years of projects where I needed just say a uh a meter to power source, this
[20:52] say a uh a meter to power source, this
[20:52] say a uh a meter to power source, this is not just oh the a solution for when I
[20:56] is not just oh the a solution for when I
[20:56] is not just oh the a solution for when I need portability. This one is better uh
[20:59] need portability. This one is better uh
[20:59] need portability. This one is better uh overall solution for me to do some
[21:02] overall solution for me to do some
[21:02] overall solution for me to do some high-owered device prototyping and
[21:05] high-owered device prototyping and
[21:05] high-owered device prototyping and testing even compared with these
[21:07] testing even compared with these
[21:07] testing even compared with these benchtop power supplies. So, if I could
[21:09] benchtop power supplies. So, if I could
[21:09] benchtop power supplies. So, if I could only have one between this uh elegant
[21:14] only have one between this uh elegant
[21:14] only have one between this uh elegant little benchtop power supply, this one
[21:16] little benchtop power supply, this one
[21:16] little benchtop power supply, this one still maxes out at 300 vol uh watts. And
[21:20] still maxes out at 300 vol uh watts. And
[21:20] still maxes out at 300 vol uh watts. And and if you're only at 10 volts, then
[21:23] and if you're only at 10 volts, then
[21:23] and if you're only at 10 volts, then you've only got 100 watts to work with.
[21:26] you've only got 100 watts to work with.
[21:26] you've only got 100 watts to work with. 10 amps is the limiting factor. And we
[21:28] 10 amps is the limiting factor. And we
[21:28] 10 amps is the limiting factor. And we can do more more with that one. Um so
[21:34] can do more more with that one. Um so
[21:34] can do more more with that one. Um so yes the the suggestion is even in
[21:37] yes the the suggestion is even in
[21:37] yes the the suggestion is even in engineering labs we're doing learning
[21:39] engineering labs we're doing learning
[21:39] engineering labs we're doing learning and measuring
[21:41] and measuring
[21:41] and measuring um this is good for a certain range of
[21:44] um this is good for a certain range of
[21:44] um this is good for a certain range of accuracy that you may need a certain
[21:46] accuracy that you may need a certain
[21:46] accuracy that you may need a certain duration if you got to have something
[21:47] duration if you got to have something
[21:48] duration if you got to have something plugged in for a whole week and a steady
[21:50] plugged in for a whole week and a steady
[21:50] plugged in for a whole week and a steady output. All right. But if we're testing
[21:53] output. All right. But if we're testing
[21:53] output. All right. But if we're testing something that's going to be portable,
[21:54] something that's going to be portable,
[21:54] something that's going to be portable, it's just going to
[21:57] it's just going to
[21:57] it's just going to uh draw a lot of power to simulate a
[22:01] uh draw a lot of power to simulate a
[22:01] uh draw a lot of power to simulate a real work scenario. There we go. Oh,
[22:04] real work scenario. There we go. Oh,
[22:04] real work scenario. There we go. Oh, right. I was going to mention the your
[22:06] right. I was going to mention the your
[22:06] right. I was going to mention the your favorite connector. If you don't want to
[22:08] favorite connector. If you don't want to
[22:08] favorite connector. If you don't want to use Anderson and you want to use another
[22:10] use Anderson and you want to use another
[22:10] use Anderson and you want to use another type, that whole feature is dictated
[22:14] type, that whole feature is dictated
[22:14] type, that whole feature is dictated just by um this parametric sleeve. And
[22:18] just by um this parametric sleeve. And
[22:18] just by um this parametric sleeve. And so I published this maybe a year ago
[22:21] so I published this maybe a year ago
[22:21] so I published this maybe a year ago which will fit into the the socket the
[22:25] which will fit into the the socket the
[22:25] which will fit into the the socket the the cutouts knockouts on the box and
[22:29] the cutouts knockouts on the box and
[22:29] the cutouts knockouts on the box and then adapts it for the shape that you
[22:30] then adapts it for the shape that you
[22:30] then adapts it for the shape that you want. There is one extrude cut in a
[22:33] want. There is one extrude cut in a
[22:33] want. There is one extrude cut in a rectangle shape that determines this uh
[22:37] rectangle shape that determines this uh
[22:37] rectangle shape that determines this uh function. And so the way this one works
[22:40] function. And so the way this one works
[22:40] function. And so the way this one works is you set the Anderson terminal in
[22:44] is you set the Anderson terminal in
[22:44] is you set the Anderson terminal in there and then you'll notice where we
[22:46] there and then you'll notice where we
[22:46] there and then you'll notice where we have this um spring pin. That'll be
[22:49] have this um spring pin. That'll be
[22:49] have this um spring pin. That'll be instead M2.5 screw. Uh so it'll align up
[22:54] instead M2.5 screw. Uh so it'll align up
[22:54] instead M2.5 screw. Uh so it'll align up to the right location and we'll drop
[22:56] to the right location and we'll drop
[22:56] to the right location and we'll drop that screw in there. And then it's just
[22:59] that screw in there. And then it's just
[22:59] that screw in there. And then it's just locking it in place. It doesn't need to
[23:02] locking it in place. It doesn't need to
[23:02] locking it in place. It doesn't need to to thread into these. It is simply
[23:04] to thread into these. It is simply
[23:04] to thread into these. It is simply acting as a as a pin. Um, and when we uh
[23:10] acting as a as a pin. Um, and when we uh
[23:10] acting as a as a pin. Um, and when we uh if if this had to be compressed just a
[23:12] if if this had to be compressed just a
[23:12] if if this had to be compressed just a little bit to go into the wall of that
[23:16] little bit to go into the wall of that
[23:16] little bit to go into the wall of that box, then when you insert these, it
[23:19] box, then when you insert these, it
[23:19] box, then when you insert these, it stretches it back out and it helps
[23:21] stretches it back out and it helps
[23:21] stretches it back out and it helps retain it in its position. If there's
[23:23] retain it in its position. If there's
[23:24] retain it in its position. If there's trouble with any trouble with retention,
[23:26] trouble with any trouble with retention,
[23:26] trouble with any trouble with retention, then you might add a little adhesive.
[23:28] then you might add a little adhesive.
[23:28] then you might add a little adhesive. And so I think this one is uh I've added
[23:30] And so I think this one is uh I've added
[23:30] And so I think this one is uh I've added some glue there. hot glue will do or um
[23:36] some glue there. hot glue will do or um
[23:36] some glue there. hot glue will do or um what do you call that?
[23:38] what do you call that?
[23:38] what do you call that? Ah yes, contact adhesive. So E6000
[23:42] Ah yes, contact adhesive. So E6000
[23:42] Ah yes, contact adhesive. So E6000 um even without the premium works fine.
[23:45] um even without the premium works fine.
[23:45] um even without the premium works fine. Now the reason I mentioned hot glue and
[23:47] Now the reason I mentioned hot glue and
[23:47] Now the reason I mentioned hot glue and contact adhesive is because it is still
[23:50] contact adhesive is because it is still
[23:50] contact adhesive is because it is still somewhat removable. um unlike the the
[23:53] somewhat removable. um unlike the the
[23:53] somewhat removable. um unlike the the PVC glue will will melt and form into
[23:57] PVC glue will will melt and form into
[23:57] PVC glue will will melt and form into the plastic of this device and uh
[24:00] the plastic of this device and uh
[24:00] the plastic of this device and uh probably it will take a destructive
[24:03] probably it will take a destructive
[24:03] probably it will take a destructive removal to take it out versus contact
[24:05] removal to take it out versus contact
[24:05] removal to take it out versus contact adhesive or hot glue. It's going to give
[24:07] adhesive or hot glue. It's going to give
[24:08] adhesive or hot glue. It's going to give you that the security that you want but
[24:10] you that the security that you want but
[24:10] you that the security that you want but still mind changeability that you might
[24:13] still mind changeability that you might
[24:13] still mind changeability that you might want uh until you get everything
[24:15] want uh until you get everything
[24:15] want uh until you get everything configured. So that is the the value of
[24:20] configured. So that is the the value of
[24:20] configured. So that is the the value of the open- source and its intention is
[24:22] the open- source and its intention is
[24:22] the open- source and its intention is that people can still pivot the designs
[24:25] that people can still pivot the designs
[24:25] that people can still pivot the designs to suit their needs. Um improvements a
[24:29] to suit their needs. Um improvements a
[24:29] to suit their needs. Um improvements a huge amount of effort goes into making
[24:31] huge amount of effort goes into making
[24:31] huge amount of effort goes into making this very very nice so that it is
[24:33] this very very nice so that it is
[24:33] this very very nice so that it is something that is worth improving on.
[24:36] something that is worth improving on.
[24:36] something that is worth improving on. What? Um, sharing the STL file gives
[24:39] What? Um, sharing the STL file gives
[24:39] What? Um, sharing the STL file gives you, okay, a thousand people can uh
[24:42] you, okay, a thousand people can uh
[24:42] you, okay, a thousand people can uh download and print this out, but then
[24:44] download and print this out, but then
[24:44] download and print this out, but then you're going to have a couple of
[24:45] you're going to have a couple of
[24:45] you're going to have a couple of designers who are really talented. We
[24:48] designers who are really talented. We
[24:48] designers who are really talented. We want to give them a head start and say,
[24:50] want to give them a head start and say,
[24:50] want to give them a head start and say, "Start here because we have a well-made
[24:54] "Start here because we have a well-made
[24:54] "Start here because we have a well-made model with all of the um the titles
[24:57] model with all of the um the titles
[24:57] model with all of the um the titles added to the features in the feature
[24:58] added to the features in the feature
[24:58] added to the features in the feature tree." And it's easy to read, easy to
[25:00] tree." And it's easy to read, easy to
[25:00] tree." And it's easy to read, easy to recognize, and it comes with the the
[25:02] recognize, and it comes with the the
[25:02] recognize, and it comes with the the package of data, a PDF that includes the
[25:06] package of data, a PDF that includes the
[25:06] package of data, a PDF that includes the information and research gathered for
[25:08] information and research gathered for
[25:08] information and research gathered for this because this uh they may want to
[25:11] this because this uh they may want to
[25:11] this because this uh they may want to change this as well. We're really trying
[25:13] change this as well. We're really trying
[25:13] change this as well. We're really trying to put the engineering out into the open
[25:16] to put the engineering out into the open
[25:16] to put the engineering out into the open source, not just a copy of the result.
[25:19] source, not just a copy of the result.
[25:19] source, not just a copy of the result. [snorts] Okay, now think about this. I
[25:21] [snorts] Okay, now think about this. I
[25:22] [snorts] Okay, now think about this. I never dreamed this would happen, but
[25:24] never dreamed this would happen, but
[25:24] never dreamed this would happen, but Rigid is owned by Emerson Electric.
[25:26] Rigid is owned by Emerson Electric.
[25:26] Rigid is owned by Emerson Electric. They're they've got loads of engineers.
[25:28] They're they've got loads of engineers.
[25:28] They're they've got loads of engineers. Their market cap um market capital value
[25:31] Their market cap um market capital value
[25:31] Their market cap um market capital value of this business is $75 billion
[25:35] of this business is $75 billion
[25:35] of this business is $75 billion and they work for me now because this is
[25:38] and they work for me now because this is
[25:38] and they work for me now because this is this is my creation and when they
[25:42] this is my creation and when they
[25:42] this is my creation and when they improve this battery makes the next
[25:45] improve this battery makes the next
[25:45] improve this battery makes the next generation of this then they will be
[25:47] generation of this then they will be
[25:47] generation of this then they will be enhancing my design. This is what
[25:50] enhancing my design. This is what
[25:50] enhancing my design. This is what happens when we can take the time to
[25:52] happens when we can take the time to
[25:52] happens when we can take the time to appreciate what did the engineers do to
[25:54] appreciate what did the engineers do to
[25:54] appreciate what did the engineers do to create value in these in these creations
[25:57] create value in these in these creations
[25:57] create value in these in these creations and then capture that value and respect
[26:00] and then capture that value and respect
[26:00] and then capture that value and respect what is on the regular market that is
[26:03] what is on the regular market that is
[26:03] what is on the regular market that is doing amazing jobs um and anticipate
[26:07] doing amazing jobs um and anticipate
[26:07] doing amazing jobs um and anticipate what how is this unfolding because we've
[26:10] what how is this unfolding because we've
[26:10] what how is this unfolding because we've seen uh these continue to sell for 10
[26:13] seen uh these continue to sell for 10
[26:13] seen uh these continue to sell for 10 years and uh Reiko they manufacture this
[26:16] years and uh Reiko they manufacture this
[26:16] years and uh Reiko they manufacture this box those engineers are working for me
[26:19] box those engineers are working for me
[26:19] box those engineers are working for me because I have studied their design
[26:21] because I have studied their design
[26:21] because I have studied their design enough to say this is worth taking into
[26:23] enough to say this is worth taking into
[26:23] enough to say this is worth taking into our design. Um, it's mass-produced. The
[26:26] our design. Um, it's mass-produced. The
[26:26] our design. Um, it's mass-produced. The logistics are performed by Reiko. The
[26:28] logistics are performed by Reiko. The
[26:28] logistics are performed by Reiko. The advertising, the updating of all the
[26:30] advertising, the updating of all the
[26:30] advertising, the updating of all the drawings performed by Reiko. And then we
[26:33] drawings performed by Reiko. And then we
[26:33] drawings performed by Reiko. And then we have something here that outperforms
[26:35] have something here that outperforms
[26:35] have something here that outperforms this with I mean basically 45 watts
[26:39] this with I mean basically 45 watts
[26:39] this with I mean basically 45 watts versus 60 idle power 2.2 versus one DC
[26:43] versus 60 idle power 2.2 versus one DC
[26:43] versus 60 idle power 2.2 versus one DC output no versus yes. Uh, it's probably
[26:46] output no versus yes. Uh, it's probably
[26:46] output no versus yes. Uh, it's probably more than 200 watts. And we have the
[26:49] more than 200 watts. And we have the
[26:49] more than 200 watts. And we have the total cost 85 versus 20. Um, so wow. Uh,
[26:55] total cost 85 versus 20. Um, so wow. Uh,
[26:56] total cost 85 versus 20. Um, so wow. Uh, we can really do this guys. You don't
[26:58] we can really do this guys. You don't
[26:58] we can really do this guys. You don't have to be a huge company. You can use
[27:01] have to be a huge company. You can use
[27:01] have to be a huge company. You can use leverage the huge companies. Um, and
[27:03] leverage the huge companies. Um, and
[27:03] leverage the huge companies. Um, and then this is my message to Elon Musk. We
[27:07] then this is my message to Elon Musk. We
[27:07] then this is my message to Elon Musk. We imagined um that technology the purpose
[27:11] imagined um that technology the purpose
[27:11] imagined um that technology the purpose of technology is to design things and
[27:13] of technology is to design things and
[27:13] of technology is to design things and release products with higher performance
[27:15] release products with higher performance
[27:16] release products with higher performance with lower cost and longer lifespan from
[27:19] with lower cost and longer lifespan from
[27:19] with lower cost and longer lifespan from the very first thing we release. Okay.
[27:22] the very first thing we release. Okay.
[27:22] the very first thing we release. Okay. Um and that is compared with the market
[27:24] Um and that is compared with the market
[27:24] Um and that is compared with the market leader through technology. Elon, do you
[27:28] leader through technology. Elon, do you
[27:28] leader through technology. Elon, do you remember this car back in 2012? We
[27:31] remember this car back in 2012? We
[27:31] remember this car back in 2012? We brought your cars over to Toyota. This
[27:33] brought your cars over to Toyota. This
[27:33] brought your cars over to Toyota. This is the Toyota Design Center in Saline,
[27:36] is the Toyota Design Center in Saline,
[27:36] is the Toyota Design Center in Saline, Michigan. Okay. And all of us engineers,
[27:41] Michigan. Okay. And all of us engineers,
[27:41] Michigan. Okay. And all of us engineers, Americans from all around the US, we're
[27:43] Americans from all around the US, we're
[27:43] Americans from all around the US, we're working here. We checked out your cars.
[27:45] working here. We checked out your cars.
[27:45] working here. We checked out your cars. Of course, naturally, we're doing
[27:47] Of course, naturally, we're doing
[27:47] Of course, naturally, we're doing benchmarking. Okay? And I took this for
[27:50] benchmarking. Okay? And I took this for
[27:50] benchmarking. Okay? And I took this for a weekend. I stuck my girlfriend in it
[27:54] a weekend. I stuck my girlfriend in it
[27:54] a weekend. I stuck my girlfriend in it and evaluated. What are you designing
[27:56] and evaluated. What are you designing
[27:56] and evaluated. What are you designing and what are you releasing?
[27:59] and what are you releasing?
[27:59] and what are you releasing? And Elon, we were listening. We heard
[28:02] And Elon, we were listening. We heard
[28:02] And Elon, we were listening. We heard the messages coming out of your company
[28:03] the messages coming out of your company
[28:04] the messages coming out of your company at Tesla. We thought you were going to
[28:06] at Tesla. We thought you were going to
[28:06] at Tesla. We thought you were going to give us higher performance and lower
[28:08] give us higher performance and lower
[28:08] give us higher performance and lower cost and longer lifespan. We thought
[28:10] cost and longer lifespan. We thought
[28:10] cost and longer lifespan. We thought that you were going to outperform the
[28:13] that you were going to outperform the
[28:13] that you were going to outperform the state-of-the-art technology with all the
[28:16] state-of-the-art technology with all the
[28:16] state-of-the-art technology with all the resources that you had access to. And if
[28:19] resources that you had access to. And if
[28:19] resources that you had access to. And if that were true, if this thing had the
[28:23] that were true, if this thing had the
[28:23] that were true, if this thing had the mileage and the cost and it had the
[28:26] mileage and the cost and it had the
[28:26] mileage and the cost and it had the performance that was going to last
[28:28] performance that was going to last
[28:28] performance that was going to last longer than a Toyota, then I would be
[28:30] longer than a Toyota, then I would be
[28:30] longer than a Toyota, then I would be working for you today.
[28:33] working for you today.
[28:33] working for you today. So,
[28:35] So,
[28:35] So, I don't know what to tell you, but it
[28:37] I don't know what to tell you, but it
[28:37] I don't know what to tell you, but it can be done. It can be done from the
[28:39] can be done. It can be done from the
[28:39] can be done. It can be done from the very first product. And you don't have
[28:40] very first product. And you don't have
[28:40] very first product. And you don't have to do this. You don't have to do this.
[28:43] to do this. You don't have to do this.
[28:43] to do this. You don't have to do this. Oh, we're going to make it first uh cost
[28:45] Oh, we're going to make it first uh cost
[28:45] Oh, we're going to make it first uh cost twice as much and then later think about
[28:48] twice as much and then later think about
[28:48] twice as much and then later think about how to reduce the cost. No,
[28:51] how to reduce the cost. No,
[28:51] how to reduce the cost. No, that was Michigan. Now I'm in Texas. Um
[28:55] that was Michigan. Now I'm in Texas. Um
[28:55] that was Michigan. Now I'm in Texas. Um and I have several friends that are now
[28:57] and I have several friends that are now
[28:57] and I have several friends that are now working for you. You you came over to
[28:59] working for you. You you came over to
[28:59] working for you. You you came over to Texas after me. Uh an hour and a half
[29:02] Texas after me. Uh an hour and a half
[29:02] Texas after me. Uh an hour and a half away from here in Austin. You're setting
[29:05] away from here in Austin. You're setting
[29:05] away from here in Austin. You're setting up your plants. You're still building.
[29:07] up your plants. You're still building.
[29:07] up your plants. You're still building. It's more than 10 years later. And you
[29:09] It's more than 10 years later. And you
[29:09] It's more than 10 years later. And you still haven't made cars cost less. Uh,
[29:13] still haven't made cars cost less. Uh,
[29:13] still haven't made cars cost less. Uh, we're disappointed. We're disappointed.
[29:16] we're disappointed. We're disappointed.
[29:16] we're disappointed. We're disappointed. And my my pals that work for Tesla are
[29:19] And my my pals that work for Tesla are
[29:19] And my my pals that work for Tesla are not um they're there for their paycheck.
[29:23] not um they're there for their paycheck.
[29:23] not um they're there for their paycheck. And I watch them go home and do their
[29:25] And I watch them go home and do their
[29:26] And I watch them go home and do their very best, most passionate work in their
[29:29] very best, most passionate work in their
[29:29] very best, most passionate work in their backyard, in their garage, in their
[29:31] backyard, in their garage, in their
[29:32] backyard, in their garage, in their living room on projects where they can
[29:34] living room on projects where they can
[29:34] living room on projects where they can finally put their creativity and do
[29:36] finally put their creativity and do
[29:36] finally put their creativity and do something that that really uh comes from
[29:40] something that that really uh comes from
[29:40] something that that really uh comes from their inspiration. So, you're missing
[29:42] their inspiration. So, you're missing
[29:42] their inspiration. So, you're missing out on the inspiration of a lot of
[29:44] out on the inspiration of a lot of
[29:44] out on the inspiration of a lot of engineers
[29:45] engineers
[29:45] engineers and you already know why. So,
[29:49] and you already know why. So,
[29:49] and you already know why. So, uh hope you guys enjoyed this video. I
[29:52] uh hope you guys enjoyed this video. I
[29:52] uh hope you guys enjoyed this video. I hope this is uh something helpful to
[29:54] hope this is uh something helpful to
[29:54] hope this is uh something helpful to you. Your feedback and your inputs are
[29:56] you. Your feedback and your inputs are
[29:56] you. Your feedback and your inputs are always welcome and if they're technical
[29:57] always welcome and if they're technical
[29:57] always welcome and if they're technical inputs, put them there on uh so we have
[30:00] inputs, put them there on uh so we have
[30:00] inputs, put them there on uh so we have qr.net/openlab net/openlab
[30:02] qr.net/openlab net/openlab
[30:02] qr.net/openlab net/openlab project and we have open box which is an
[30:05] project and we have open box which is an
[30:05] project and we have open box which is an array of the designs that relate to uh
[30:08] array of the designs that relate to uh
[30:08] array of the designs that relate to uh this handybox and some of the great
[30:11] this handybox and some of the great
[30:11] this handybox and some of the great things you can do with these handy
[30:12] things you can do with these handy
[30:12] things you can do with these handy boxes. So, um, if they're technical
[30:14] boxes. So, um, if they're technical
[30:14] boxes. So, um, if they're technical inputs, drop them there, um, in the
[30:17] inputs, drop them there, um, in the
[30:17] inputs, drop them there, um, in the GitHub repository where we've got the
[30:20] GitHub repository where we've got the
[30:20] GitHub repository where we've got the discussions about this stuff, um, or on
[30:22] discussions about this stuff, um, or on
[30:22] discussions about this stuff, um, or on the Grabcad where we've posted the, um,
[30:26] the Grabcad where we've posted the, um,
[30:26] the Grabcad where we've posted the, um, I posted my models and any other
[30:29] I posted my models and any other
[30:29] I posted my models and any other questions that if I need to add the
[30:31] questions that if I need to add the
[30:31] questions that if I need to add the vectors for the content, then just let
[30:33] vectors for the content, then just let
[30:33] vectors for the content, then just let me know in the comments of this YouTube
[30:35] me know in the comments of this YouTube
[30:35] me know in the comments of this YouTube video and then I'll uh, I'll keep
[30:37] video and then I'll uh, I'll keep
[30:37] video and then I'll uh, I'll keep posting. Thanks everyone. Hope to find
[30:39] posting. Thanks everyone. Hope to find
[30:39] posting. Thanks everyone. Hope to find more collaborators. I hope I find one
[30:42] more collaborators. I hope I find one
[30:42] more collaborators. I hope I find one solid collaborator who's interested in
[30:45] solid collaborator who's interested in
[30:45] solid collaborator who's interested in these battery and power related projects
[30:47] these battery and power related projects
[30:47] these battery and power related projects from this video.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
