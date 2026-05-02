---
title: "How to design a functional, printable, open source mechanical part"
url: "https://www.youtube.com/watch?v=CvhiSP_6ESQ"
video_id: "CvhiSP_6ESQ"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-12-09
duration: "37:09"
duration_sec: 2229
views: 4189
likes: 221
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/CvhiSP_6ESQ/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1500
chapters_count: 15
has_description: true
has_comments: false
---

## Description

This video explains how a mechanical engineer approaches a design for a functional part.  I think its a big improvement on my last design tutorial.  Your feedback helps everything improve.

[Links]
Sleeve CAD model ► https://grabcad.com/library/sleeve-35
Open Lab Info ► qr.net/openlabproject
Discord ► (see my bio)

[Chapters]
0:00 design purpose
3:00 video purpose
4:24 design questions
10:25 research questions
16:13 testing loads
18:18 defining a design
18:58 questions embedded in parts
19:36 parametric designs
21:18 answers in files
22:00 focus on parts
25:10 application1
27:48 application 2
29:53 branches of parts
33:33 cad model
35:20 parts library

## Chapters

- 0:00 design purpose
- 3:00 video purpose
- 4:24 design questions
- 10:25 research questions
- 16:13 testing loads
- 18:18 defining a design
- 18:58 questions embedded in parts
- 19:36 parametric designs
- 21:18 answers in files
- 22:00 focus on parts
- 25:10 application1
- 27:48 application 2
- 29:53 branches of parts
- 33:33 cad model
- 35:20 parts library

## Transcript

[0:02] Let's start here. Why did I want to make
[0:02] Let's start here. Why did I want to make this design? Because I wanted to control
[0:07] this design? Because I wanted to control
[0:07] this design? Because I wanted to control a shaft through a thin steel wall.
[0:11] a shaft through a thin steel wall.
[0:11] a shaft through a thin steel wall. And why would I want that? Well, I can
[0:13] And why would I want that? Well, I can
[0:13] And why would I want that? Well, I can show you. If you look at these lamps,
[0:15] show you. If you look at these lamps,
[0:15] show you. If you look at these lamps, you'll see a thin steel wall and a pin.
[0:19] you'll see a thin steel wall and a pin.
[0:19] you'll see a thin steel wall and a pin. And the designers took control of the
[0:21] And the designers took control of the
[0:21] And the designers took control of the pin in the steel wall. Now you have an
[0:24] pin in the steel wall. Now you have an
[0:24] pin in the steel wall. Now you have an adjustable lamp. If you look at this
[0:27] adjustable lamp. If you look at this
[0:27] adjustable lamp. If you look at this lamp, you'll see the same. A thin steel
[0:30] lamp, you'll see the same. A thin steel
[0:30] lamp, you'll see the same. A thin steel wall and a pin
[0:33] wall and a pin
[0:33] wall and a pin taking control of a joint. If you look
[0:36] taking control of a joint. If you look
[0:36] taking control of a joint. If you look at this fan, it's a thin steel wall and
[0:39] at this fan, it's a thin steel wall and
[0:39] at this fan, it's a thin steel wall and a pin and the designers took control to
[0:43] a pin and the designers took control to
[0:43] a pin and the designers took control to form a dually supported joint. And the
[0:46] form a dually supported joint. And the
[0:46] form a dually supported joint. And the same is true here. We have a hole in a
[0:49] same is true here. We have a hole in a
[0:49] same is true here. We have a hole in a thin steel wall that gives us another
[0:52] thin steel wall that gives us another
[0:52] thin steel wall that gives us another degree of freedom. And then if you look
[0:54] degree of freedom. And then if you look
[0:54] degree of freedom. And then if you look back further, we have still a pin in a
[0:58] back further, we have still a pin in a
[0:58] back further, we have still a pin in a thin steel wall that carries a load and
[1:02] thin steel wall that carries a load and
[1:02] thin steel wall that carries a load and takes control. If we come over to this
[1:05] takes control. If we come over to this
[1:05] takes control. If we come over to this television and look at the mount, we
[1:07] television and look at the mount, we
[1:07] television and look at the mount, we have a four bar linkage. And we have a
[1:11] have a four bar linkage. And we have a
[1:11] have a four bar linkage. And we have a pin and a thin steel wall that supports
[1:14] pin and a thin steel wall that supports
[1:14] pin and a thin steel wall that supports it. And then this beam is just made up
[1:16] it. And then this beam is just made up
[1:16] it. And then this beam is just made up of two more thin steel walls that are uh
[1:20] of two more thin steel walls that are uh
[1:20] of two more thin steel walls that are uh constrained also by the pin. And all
[1:23] constrained also by the pin. And all
[1:23] constrained also by the pin. And all throughout this design, it's the same.
[1:25] throughout this design, it's the same.
[1:25] throughout this design, it's the same. If we look at this dishwasher, we have a
[1:28] If we look at this dishwasher, we have a
[1:28] If we look at this dishwasher, we have a smooth operation and a supported hinge
[1:31] smooth operation and a supported hinge
[1:31] smooth operation and a supported hinge on this door that's based on a pin going
[1:35] on this door that's based on a pin going
[1:35] on this door that's based on a pin going through a thin steel wall here. If
[1:38] through a thin steel wall here. If
[1:38] through a thin steel wall here. If you're relaxing on the couch, you're
[1:39] you're relaxing on the couch, you're
[1:39] you're relaxing on the couch, you're supported by several pins and thin steel
[1:44] supported by several pins and thin steel
[1:44] supported by several pins and thin steel walls.
[1:52] And the friction and the movement
[1:52] And the friction and the movement and the freedom to move is all
[1:54] and the freedom to move is all
[1:54] and the freedom to move is all controlled by the materials and the
[1:57] controlled by the materials and the
[1:57] controlled by the materials and the decisions around that pin in those thin
[1:59] decisions around that pin in those thin
[1:59] decisions around that pin in those thin steel walls. If you take apart a monitor
[2:02] steel walls. If you take apart a monitor
[2:02] steel walls. If you take apart a monitor mount, an adjustable mount, then you
[2:05] mount, an adjustable mount, then you
[2:05] mount, an adjustable mount, then you will find these beams that are made up
[2:09] will find these beams that are made up
[2:09] will find these beams that are made up from a pin in a thin steel wall for all
[2:14] from a pin in a thin steel wall for all
[2:14] from a pin in a thin steel wall for all of the joints. These are just covered in
[2:17] of the joints. These are just covered in
[2:17] of the joints. These are just covered in plastic.
[2:19] plastic.
[2:19] plastic. In fact, you'll notice the whole world
[2:22] In fact, you'll notice the whole world
[2:22] In fact, you'll notice the whole world revolves around a pin that goes through
[2:25] revolves around a pin that goes through
[2:25] revolves around a pin that goes through a thin steel wall.
[2:33] So, I produced this sleeve and its
[2:33] So, I produced this sleeve and its variations to begin to have for
[2:35] variations to begin to have for
[2:35] variations to begin to have for ourselves a set of answers that take
[2:39] ourselves a set of answers that take
[2:39] ourselves a set of answers that take control of pins going through steel
[2:41] control of pins going through steel
[2:41] control of pins going through steel walls. Um, this apparatus here gives us
[2:43] walls. Um, this apparatus here gives us
[2:44] walls. Um, this apparatus here gives us a gearbox, but the more important thing
[2:47] a gearbox, but the more important thing
[2:47] a gearbox, but the more important thing is to have a really nice um, set of
[2:50] is to have a really nice um, set of
[2:50] is to have a really nice um, set of offerings that give us that control and
[2:54] offerings that give us that control and
[2:54] offerings that give us that control and give us the ability to adjust the design
[2:56] give us the ability to adjust the design
[2:56] give us the ability to adjust the design to manipulate that joint right there.
[2:59] to manipulate that joint right there.
[2:59] to manipulate that joint right there. You may be getting new ideas on how to
[3:02] You may be getting new ideas on how to
[3:02] You may be getting new ideas on how to plan a design for multiple assemblies
[3:05] plan a design for multiple assemblies
[3:05] plan a design for multiple assemblies and what assemblies are possible to be
[3:09] and what assemblies are possible to be
[3:09] and what assemblies are possible to be built with um 3D printed parts. So this
[3:13] built with um 3D printed parts. So this
[3:13] built with um 3D printed parts. So this is another integrated part with
[3:15] is another integrated part with
[3:15] is another integrated part with off-the-shelf parts. And so I'm using
[3:17] off-the-shelf parts. And so I'm using
[3:17] off-the-shelf parts. And so I'm using keyword print for the online posts that
[3:20] keyword print for the online posts that
[3:20] keyword print for the online posts that have parts like this.
[3:23] have parts like this.
[3:23] have parts like this. And as a designer, even if you're not a
[3:25] And as a designer, even if you're not a
[3:25] And as a designer, even if you're not a mechanical engineer, you should gain
[3:28] mechanical engineer, you should gain
[3:28] mechanical engineer, you should gain some insights as to how do you approach
[3:30] some insights as to how do you approach
[3:30] some insights as to how do you approach the specific problems? What problems do
[3:32] the specific problems? What problems do
[3:32] the specific problems? What problems do we encounter when we're trying to create
[3:35] we encounter when we're trying to create
[3:35] we encounter when we're trying to create something from scratch to do to do a
[3:37] something from scratch to do to do a
[3:37] something from scratch to do to do a job? Um, and how does a mechanical
[3:40] job? Um, and how does a mechanical
[3:40] job? Um, and how does a mechanical engineer think through uh a design
[3:42] engineer think through uh a design
[3:42] engineer think through uh a design process and make steps out of it. I
[3:47] process and make steps out of it. I
[3:47] process and make steps out of it. I should also mention that we're still on
[3:49] should also mention that we're still on
[3:49] should also mention that we're still on track. From 6 months or a year back, I
[3:53] track. From 6 months or a year back, I
[3:53] track. From 6 months or a year back, I showed people how to throw together this
[3:55] showed people how to throw together this
[3:55] showed people how to throw together this simple joint uh bracket that holds a big
[3:58] simple joint uh bracket that holds a big
[3:58] simple joint uh bracket that holds a big fan that uh allows you to position it
[4:02] fan that uh allows you to position it
[4:02] fan that uh allows you to position it that is simply made from the same
[4:04] that is simply made from the same
[4:04] that is simply made from the same components we're going to look at today.
[4:06] components we're going to look at today.
[4:06] components we're going to look at today. And the next steps are to be able to
[4:09] And the next steps are to be able to
[4:09] And the next steps are to be able to take more control over th those joints
[4:12] take more control over th those joints
[4:12] take more control over th those joints um to control the friction or the
[4:15] um to control the friction or the
[4:16] um to control the friction or the clicking. And that means we're going to
[4:17] clicking. And that means we're going to
[4:17] clicking. And that means we're going to need some sort of components that give
[4:20] need some sort of components that give
[4:20] need some sort of components that give us access to manipulate the joint. And
[4:22] us access to manipulate the joint. And
[4:22] us access to manipulate the joint. And that's where we're going. So I want this
[4:25] that's where we're going. So I want this
[4:25] that's where we're going. So I want this bolt to go securely into these holes. Um
[4:30] bolt to go securely into these holes. Um
[4:30] bolt to go securely into these holes. Um let's just consider one hole. How do I
[4:32] let's just consider one hole. How do I
[4:32] let's just consider one hole. How do I get the bolt to fit? Well, I'm going to
[4:35] get the bolt to fit? Well, I'm going to
[4:35] get the bolt to fit? Well, I'm going to use a reducer. So, I'll reduce that size
[4:38] use a reducer. So, I'll reduce that size
[4:38] use a reducer. So, I'll reduce that size from large to small 8 millimeters. How
[4:42] from large to small 8 millimeters. How
[4:42] from large to small 8 millimeters. How will such a reducer um install into this
[4:46] will such a reducer um install into this
[4:46] will such a reducer um install into this wall? It's going to have a slip fit.
[4:49] wall? It's going to have a slip fit.
[4:49] wall? It's going to have a slip fit. It's going to just pass in uh without
[4:51] It's going to just pass in uh without
[4:51] It's going to just pass in uh without pressing. And so that answer of the slip
[4:55] pressing. And so that answer of the slip
[4:55] pressing. And so that answer of the slip fit is defined in this diameter here
[5:00] fit is defined in this diameter here
[5:00] fit is defined in this diameter here exactly where you'll see the flush wall
[5:04] exactly where you'll see the flush wall
[5:04] exactly where you'll see the flush wall of my steel on the flush uh surface
[5:09] of my steel on the flush uh surface
[5:09] of my steel on the flush uh surface located right here. How will I prevent
[5:12] located right here. How will I prevent
[5:12] located right here. How will I prevent the sleeve from passing all the way
[5:14] the sleeve from passing all the way
[5:14] the sleeve from passing all the way through and have it just contact and
[5:17] through and have it just contact and
[5:17] through and have it just contact and stop here where I want it? Well, that's
[5:19] stop here where I want it? Well, that's
[5:19] stop here where I want it? Well, that's going to be defined by having a a
[5:22] going to be defined by having a a
[5:22] going to be defined by having a a diameter larger. Instead of an a slit
[5:25] diameter larger. Instead of an a slit
[5:25] diameter larger. Instead of an a slit fit, we're just saying depending on this
[5:28] fit, we're just saying depending on this
[5:28] fit, we're just saying depending on this diameter, we need a millimeter or two
[5:31] diameter, we need a millimeter or two
[5:32] diameter, we need a millimeter or two larger than this 22 mm. And so that
[5:35] larger than this 22 mm. And so that
[5:35] larger than this 22 mm. And so that answer is embedded in this diameter
[5:38] answer is embedded in this diameter
[5:38] answer is embedded in this diameter right here. Okay. So, we have something
[5:41] right here. Okay. So, we have something
[5:41] right here. Okay. So, we have something thin that slips in. Conceptually,
[5:44] thin that slips in. Conceptually,
[5:44] thin that slips in. Conceptually, we said, um, how will the bolt fit into
[5:49] we said, um, how will the bolt fit into
[5:49] we said, um, how will the bolt fit into this reducing device? Well, it's going
[5:52] this reducing device? Well, it's going
[5:52] this reducing device? Well, it's going to also have a slip fit. And so, that
[5:55] to also have a slip fit. And so, that
[5:55] to also have a slip fit. And so, that hole is defined by the diameter of the
[5:58] hole is defined by the diameter of the
[5:58] hole is defined by the diameter of the screw plus some amount that gives me the
[6:02] screw plus some amount that gives me the
[6:02] screw plus some amount that gives me the clearance fit. And that answer actually
[6:05] clearance fit. And that answer actually
[6:05] clearance fit. And that answer actually is a routine answer. And that lives in a
[6:07] is a routine answer. And that lives in a
[6:08] is a routine answer. And that lives in a set of design rules. I actually
[6:09] set of design rules. I actually
[6:09] set of design rules. I actually published um a PDF 18 pages so far and
[6:13] published um a PDF 18 pages so far and
[6:13] published um a PDF 18 pages so far and that's available although it's just a
[6:15] that's available although it's just a
[6:15] that's available although it's just a draft. Okay. So then we ask how will we
[6:19] draft. Okay. So then we ask how will we
[6:19] draft. Okay. So then we ask how will we install it or rather how will we secure
[6:21] install it or rather how will we secure
[6:21] install it or rather how will we secure it after we put it in and it's going to
[6:24] it after we put it in and it's going to
[6:24] it after we put it in and it's going to need some kind of hardware or fastener
[6:26] need some kind of hardware or fastener
[6:26] need some kind of hardware or fastener or clamping. How do I maintain this uh
[6:29] or clamping. How do I maintain this uh
[6:29] or clamping. How do I maintain this uh flush against that wall so that makes
[6:31] flush against that wall so that makes
[6:31] flush against that wall so that makes contact and we don't have movement in
[6:34] contact and we don't have movement in
[6:34] contact and we don't have movement in this direction? So, that's answered
[6:37] this direction? So, that's answered
[6:37] this direction? So, that's answered first by an e-clipip. This is fairly
[6:40] first by an e-clipip. This is fairly
[6:40] first by an e-clipip. This is fairly standard in some automotive
[6:42] standard in some automotive
[6:42] standard in some automotive applications.
[6:44] applications.
[6:44] applications. Um, and they're ubiquitous,
[6:46] Um, and they're ubiquitous,
[6:46] Um, and they're ubiquitous, long-standing parts that's uh found in
[6:50] long-standing parts that's uh found in
[6:50] long-standing parts that's uh found in several trades, found all around low
[6:53] several trades, found all around low
[6:53] several trades, found all around low cost. And so, I grabbed one of these to
[6:55] cost. And so, I grabbed one of these to
[6:55] cost. And so, I grabbed one of these to try it out. Now, how will we um mate
[6:59] try it out. Now, how will we um mate
[6:59] try it out. Now, how will we um mate with the e-clipip? How will we make sure
[7:01] with the e-clipip? How will we make sure
[7:01] with the e-clipip? How will we make sure that this thing accepts this e-clipip?
[7:04] that this thing accepts this e-clipip?
[7:04] that this thing accepts this e-clipip? Uh that is going to be a matter of these
[7:07] Uh that is going to be a matter of these
[7:07] Uh that is going to be a matter of these are designated for a certain diameter
[7:09] are designated for a certain diameter
[7:10] are designated for a certain diameter like it's essentially the diameter you'd
[7:12] like it's essentially the diameter you'd
[7:12] like it's essentially the diameter you'd measure around here plus or minus some
[7:15] measure around here plus or minus some
[7:15] measure around here plus or minus some range. And so we take that information
[7:18] range. And so we take that information
[7:18] range. And so we take that information about this diameter and that gets
[7:21] about this diameter and that gets
[7:21] about this diameter and that gets plugged into this groove. So we have
[7:25] plugged into this groove. So we have
[7:25] plugged into this groove. So we have mating.
[7:27] mating.
[7:27] mating. Let's zoom in.
[7:29] Let's zoom in.
[7:29] Let's zoom in. We have mating with the wall. Then we
[7:31] We have mating with the wall. Then we
[7:31] We have mating with the wall. Then we have flush with the interior wall. And
[7:33] have flush with the interior wall. And
[7:34] have flush with the interior wall. And then we have a diameter here. And that
[7:37] then we have a diameter here. And that
[7:37] then we have a diameter here. And that is an answer to the question of what
[7:39] is an answer to the question of what
[7:39] is an answer to the question of what diameter will fit with the E-clipip um
[7:43] diameter will fit with the E-clipip um
[7:44] diameter will fit with the E-clipip um retaining ring or Cclipip sometimes
[7:46] retaining ring or Cclipip sometimes
[7:46] retaining ring or Cclipip sometimes they're called. And then um how wide of
[7:50] they're called. And then um how wide of
[7:50] they're called. And then um how wide of a groove do we need to accept this
[7:52] a groove do we need to accept this
[7:52] a groove do we need to accept this E-clipip? Well, then that's also defined
[7:55] E-clipip? Well, then that's also defined
[7:55] E-clipip? Well, then that's also defined by the eclipse geometry and it's
[7:57] by the eclipse geometry and it's
[7:57] by the eclipse geometry and it's relating to the thickness of that
[7:59] relating to the thickness of that
[7:59] relating to the thickness of that eclipse. So, we make a groove equal to
[8:03] eclipse. So, we make a groove equal to
[8:03] eclipse. So, we make a groove equal to that thickness. And then you can see
[8:05] that thickness. And then you can see
[8:05] that thickness. And then you can see it's sort of uh it seems a little bit
[8:07] it's sort of uh it seems a little bit
[8:07] it's sort of uh it seems a little bit larger, but it's tapered. And that is a
[8:10] larger, but it's tapered. And that is a
[8:10] larger, but it's tapered. And that is a question of how will my 3D printed model
[8:14] question of how will my 3D printed model
[8:14] question of how will my 3D printed model allow 3D printing without supports?
[8:17] allow 3D printing without supports?
[8:17] allow 3D printing without supports? Well, that um then we're not going to
[8:19] Well, that um then we're not going to
[8:20] Well, that um then we're not going to have overhangs. That's the answer to
[8:21] have overhangs. That's the answer to
[8:21] have overhangs. That's the answer to that question. And so that transforms.
[8:24] that question. And so that transforms.
[8:24] that question. And so that transforms. We add this chamfer here that's going to
[8:28] We add this chamfer here that's going to
[8:28] We add this chamfer here that's going to um eliminate that horizontal overhang.
[8:31] um eliminate that horizontal overhang.
[8:31] um eliminate that horizontal overhang. So that makes it easier to 3D print. Um
[8:35] So that makes it easier to 3D print. Um
[8:35] So that makes it easier to 3D print. Um so you could start to see that um each
[8:39] so you could start to see that um each
[8:39] so you could start to see that um each one of the design questions can be
[8:42] one of the design questions can be
[8:42] one of the design questions can be enumerated and they can be matched to a
[8:45] enumerated and they can be matched to a
[8:45] enumerated and they can be matched to a feature.
[8:47] feature.
[8:47] feature. Um, if you're designing systematically,
[8:49] Um, if you're designing systematically,
[8:49] Um, if you're designing systematically, then they can be matched to a feature or
[8:51] then they can be matched to a feature or
[8:52] then they can be matched to a feature or a dimension inside your CAD model. Once
[8:55] a dimension inside your CAD model. Once
[8:55] a dimension inside your CAD model. Once we got that far, then you would have um
[8:58] we got that far, then you would have um
[8:58] we got that far, then you would have um this bolt or shaft pass in and it would
[9:01] this bolt or shaft pass in and it would
[9:02] this bolt or shaft pass in and it would probably start to wobble because we have
[9:04] probably start to wobble because we have
[9:04] probably start to wobble because we have a slip fit here. And so you have some
[9:07] a slip fit here. And so you have some
[9:07] a slip fit here. And so you have some play that's going to be allowed. Um,
[9:10] play that's going to be allowed. Um,
[9:10] play that's going to be allowed. Um, unless these are drilled
[9:12] unless these are drilled
[9:12] unless these are drilled post-processing, we want to eliminate
[9:13] post-processing, we want to eliminate
[9:14] post-processing, we want to eliminate post-processing. So, keeping that, how
[9:16] post-processing. So, keeping that, how
[9:16] post-processing. So, keeping that, how can we keep it from uh tilting this far
[9:18] can we keep it from uh tilting this far
[9:18] can we keep it from uh tilting this far and this far? Well, then we're going to
[9:21] and this far? Well, then we're going to
[9:21] and this far? Well, then we're going to add a thickness on this side. So, prior
[9:24] add a thickness on this side. So, prior
[9:24] add a thickness on this side. So, prior to this design question, we didn't have
[9:26] to this design question, we didn't have
[9:26] to this design question, we didn't have all this thickness. We just had a
[9:29] all this thickness. We just had a
[9:29] all this thickness. We just had a millimeter or so here. That would allow
[9:31] millimeter or so here. That would allow
[9:31] millimeter or so here. That would allow um it's less support on the shaft.
[9:35] um it's less support on the shaft.
[9:35] um it's less support on the shaft. So, you can imagine now we're contacting
[9:38] So, you can imagine now we're contacting
[9:38] So, you can imagine now we're contacting the shaft in a range, let's say as wide
[9:40] the shaft in a range, let's say as wide
[9:40] the shaft in a range, let's say as wide as my finger. And this is a a ballpark
[9:45] as my finger. And this is a a ballpark
[9:45] as my finger. And this is a a ballpark choice of uh 10 or 12 mm. And it is
[9:48] choice of uh 10 or 12 mm. And it is
[9:48] choice of uh 10 or 12 mm. And it is simply large enough to [clears throat]
[9:51] simply large enough to [clears throat]
[9:51] simply large enough to [clears throat] control the alignment of the shaft in
[9:54] control the alignment of the shaft in
[9:54] control the alignment of the shaft in general. And then controlling more
[9:56] general. And then controlling more
[9:56] general. And then controlling more carefully will be the job of having two
[10:00] carefully will be the job of having two
[10:00] carefully will be the job of having two of these that will increase the um the
[10:05] of these that will increase the um the
[10:05] of these that will increase the um the constraint from this narrow range to all
[10:08] constraint from this narrow range to all
[10:08] constraint from this narrow range to all the way out here. that uh elongating
[10:11] the way out here. that uh elongating
[10:11] the way out here. that uh elongating that constrained circular region gives
[10:14] that constrained circular region gives
[10:14] that constrained circular region gives us a more careful alignment of this
[10:19] us a more careful alignment of this
[10:19] us a more careful alignment of this shaft being perpendicular to say
[10:22] shaft being perpendicular to say
[10:22] shaft being perpendicular to say parallel to the floor where this is set
[10:24] parallel to the floor where this is set
[10:24] parallel to the floor where this is set down. All the questions so far that are
[10:27] down. All the questions so far that are
[10:27] down. All the questions so far that are answered in that design that we
[10:29] answered in that design that we
[10:29] answered in that design that we discussed are general design questions
[10:32] discussed are general design questions
[10:32] discussed are general design questions and and that I mean that these answers
[10:34] and and that I mean that these answers
[10:34] and and that I mean that these answers can be borrowed from other parts. they
[10:37] can be borrowed from other parts. they
[10:37] can be borrowed from other parts. they can be taken from my my design rules
[10:41] can be taken from my my design rules
[10:41] can be taken from my my design rules because I'm using those answers all of
[10:43] because I'm using those answers all of
[10:43] because I'm using those answers all of the time. Um, for instance, what is the
[10:46] the time. Um, for instance, what is the
[10:46] the time. Um, for instance, what is the size that the clearance fit? Well, we
[10:48] size that the clearance fit? Well, we
[10:48] size that the clearance fit? Well, we took an 8 mm shaft,
[10:51] took an 8 mm shaft,
[10:51] took an 8 mm shaft, then we always add uh 0.6 I always add
[10:55] then we always add uh 0.6 I always add
[10:55] then we always add uh 0.6 I always add 0.6 mm to that design um for 3D
[10:59] 0.6 mm to that design um for 3D
[10:59] 0.6 mm to that design um for 3D printing. And in the case of um we're
[11:04] printing. And in the case of um we're
[11:04] printing. And in the case of um we're printing in this direction. So 6 is the
[11:07] printing in this direction. So 6 is the
[11:08] printing in this direction. So 6 is the closing the overbuild. It's related to
[11:10] closing the overbuild. It's related to
[11:10] closing the overbuild. It's related to overbuild and I'll talk about that
[11:12] overbuild and I'll talk about that
[11:12] overbuild and I'll talk about that another time. [snorts] Then you have the
[11:14] another time. [snorts] Then you have the
[11:14] another time. [snorts] Then you have the questions that are uh a little bit more
[11:16] questions that are uh a little bit more
[11:16] questions that are uh a little bit more detailed such as if you place this in
[11:18] detailed such as if you place this in
[11:18] detailed such as if you place this in here
[11:21] here
[11:21] here and then we're using this retaining ring
[11:23] and then we're using this retaining ring
[11:23] and then we're using this retaining ring which is designed usually for uh
[11:27] which is designed usually for uh
[11:27] which is designed usually for uh contacting metals. It has a really
[11:29] contacting metals. It has a really
[11:29] contacting metals. It has a really strong pinching force. This force in
[11:32] strong pinching force. This force in
[11:32] strong pinching force. This force in this direction and it has that force
[11:34] this direction and it has that force
[11:34] this direction and it has that force concentrated on these narrow regions
[11:39] concentrated on these narrow regions
[11:39] concentrated on these narrow regions when it's being inserted. So then the
[11:42] when it's being inserted. So then the
[11:42] when it's being inserted. So then the question is is this uh is this metal is
[11:45] question is is this uh is this metal is
[11:45] question is is this uh is this metal is it going to be too much force or if I
[11:48] it going to be too much force or if I
[11:48] it going to be too much force or if I install this uh two times and remove it
[11:52] install this uh two times and remove it
[11:52] install this uh two times and remove it is it going to damage that printed
[11:55] is it going to damage that printed
[11:55] is it going to damage that printed plastic? And if I'm just printing with
[11:57] plastic? And if I'm just printing with
[11:57] plastic? And if I'm just printing with ordinary settings, then I have a hollow
[11:59] ordinary settings, then I have a hollow
[12:00] ordinary settings, then I have a hollow region. Actually, this is 30% infill on
[12:02] region. Actually, this is 30% infill on
[12:02] region. Actually, this is 30% infill on this part. Um, is am I going to have a
[12:05] this part. Um, is am I going to have a
[12:05] this part. Um, is am I going to have a fight between my printer settings and
[12:08] fight between my printer settings and
[12:08] fight between my printer settings and the survival of this plastic? That is
[12:12] the survival of this plastic? That is
[12:12] the survival of this plastic? That is something that we can't really compute.
[12:15] something that we can't really compute.
[12:16] something that we can't really compute. it would be unreasonable to try to put
[12:18] it would be unreasonable to try to put
[12:18] it would be unreasonable to try to put that into an FEA simulation or something
[12:21] that into an FEA simulation or something
[12:21] that into an FEA simulation or something when you could instead just print the
[12:24] when you could instead just print the
[12:24] when you could instead just print the part and do some verification. So, we're
[12:27] part and do some verification. So, we're
[12:27] part and do some verification. So, we're going to specifically observe, this is
[12:29] going to specifically observe, this is
[12:29] going to specifically observe, this is my activity, specifically observe
[12:31] my activity, specifically observe
[12:31] my activity, specifically observe pushing this on.
[12:34] pushing this on.
[12:34] pushing this on. The answer to that question was
[12:36] The answer to that question was
[12:36] The answer to that question was interesting. Um, I was able to install
[12:39] interesting. Um, I was able to install
[12:39] interesting. Um, I was able to install this multiple times. The installation
[12:41] this multiple times. The installation
[12:41] this multiple times. The installation goes with uh with some pliers. You'll
[12:44] goes with uh with some pliers. You'll
[12:44] goes with uh with some pliers. You'll need a tool because it's really hard to
[12:46] need a tool because it's really hard to
[12:46] need a tool because it's really hard to push that with your fingers. And I don't
[12:49] push that with your fingers. And I don't
[12:49] push that with your fingers. And I don't know if I can demonstrate right on
[12:52] know if I can demonstrate right on
[12:52] know if I can demonstrate right on camera, but okay. So, it goes on pretty
[12:55] camera, but okay. So, it goes on pretty
[12:55] camera, but okay. So, it goes on pretty neat. And when I remove that, you will
[12:57] neat. And when I remove that, you will
[12:57] neat. And when I remove that, you will find a little bit of superficial damage
[12:59] find a little bit of superficial damage
[12:59] find a little bit of superficial damage on the plastic. There's um it looks like
[13:03] on the plastic. There's um it looks like
[13:03] on the plastic. There's um it looks like it's not changing the net shape, but it
[13:06] it's not changing the net shape, but it
[13:06] it's not changing the net shape, but it the plastic is surviving good enough we
[13:08] the plastic is surviving good enough we
[13:08] the plastic is surviving good enough we could get by. However, um installing and
[13:11] could get by. However, um installing and
[13:11] could get by. However, um installing and uninstalling multiple times leads me to
[13:14] uninstalling multiple times leads me to
[13:14] uninstalling multiple times leads me to discover that that's just difficult. And
[13:16] discover that that's just difficult. And
[13:16] discover that that's just difficult. And if you use a tool, um you're going to
[13:19] if you use a tool, um you're going to
[13:19] if you use a tool, um you're going to have to be very careful not to jab your
[13:22] have to be very careful not to jab your
[13:22] have to be very careful not to jab your fingers or something like that. And so
[13:24] fingers or something like that. And so
[13:24] fingers or something like that. And so I've modified the C clip in this case.
[13:30] I've modified the C clip in this case.
[13:30] I've modified the C clip in this case. So this C clip is the exact same uh part
[13:36] So this C clip is the exact same uh part
[13:36] So this C clip is the exact same uh part as this but it has been reduced in the
[13:40] as this but it has been reduced in the
[13:40] as this but it has been reduced in the spring force it takes to close it. the
[13:43] spring force it takes to close it. the
[13:43] spring force it takes to close it. the net uh interior diameter has no change,
[13:48] net uh interior diameter has no change,
[13:48] net uh interior diameter has no change, but we've reduced the spring force by
[13:50] but we've reduced the spring force by
[13:50] but we've reduced the spring force by reducing the thickness of that spring
[13:52] reducing the thickness of that spring
[13:52] reducing the thickness of that spring region just by grinding it out with uh
[13:56] region just by grinding it out with uh
[13:56] region just by grinding it out with uh basically a a [snorts] Dremel and some
[13:58] basically a a [snorts] Dremel and some
[13:58] basically a a [snorts] Dremel and some carbide. Um you could equally do that
[14:01] carbide. Um you could equally do that
[14:01] carbide. Um you could equally do that with a file. And so the res that was the
[14:04] with a file. And so the res that was the
[14:04] with a file. And so the res that was the answer to the research question of how
[14:06] answer to the research question of how
[14:06] answer to the research question of how does how does it work out trying to
[14:09] does how does it work out trying to
[14:09] does how does it work out trying to install these on plastic?
[14:12] install these on plastic?
[14:12] install these on plastic? Um, and it's a little bit easier to to
[14:15] Um, and it's a little bit easier to to
[14:15] Um, and it's a little bit easier to to handle it with your fingers and just get
[14:17] handle it with your fingers and just get
[14:17] handle it with your fingers and just get a sense of the force that's going to
[14:18] a sense of the force that's going to
[14:18] a sense of the force that's going to take to install it, etc. Um, so now we
[14:23] take to install it, etc. Um, so now we
[14:23] take to install it, etc. Um, so now we have a brand new option. Uh, we have the
[14:25] have a brand new option. Uh, we have the
[14:25] have a brand new option. Uh, we have the option of if your off-the-shelf part
[14:28] option of if your off-the-shelf part
[14:28] option of if your off-the-shelf part fits nicely, you can do that. Um, but if
[14:31] fits nicely, you can do that. Um, but if
[14:31] fits nicely, you can do that. Um, but if you want to be able to turn it and
[14:33] you want to be able to turn it and
[14:33] you want to be able to turn it and adjust it, let's say this edge is going
[14:36] adjust it, let's say this edge is going
[14:36] adjust it, let's say this edge is going to interfere with the interior corner of
[14:38] to interfere with the interior corner of
[14:38] to interfere with the interior corner of the wall. So, you've got to install it
[14:40] the wall. So, you've got to install it
[14:40] the wall. So, you've got to install it this way. etc. You get more control by
[14:44] this way. etc. You get more control by
[14:44] this way. etc. You get more control by uh taking a moment to grind these or you
[14:47] uh taking a moment to grind these or you
[14:47] uh taking a moment to grind these or you could grind down the corners etc. It it
[14:49] could grind down the corners etc. It it
[14:49] could grind down the corners etc. It it can go further and further uh the
[14:51] can go further and further uh the
[14:51] can go further and further uh the discovery of options that you have. Um
[14:54] discovery of options that you have. Um
[14:54] discovery of options that you have. Um but the simplest option is described
[14:56] but the simplest option is described
[14:56] but the simplest option is described simply I can measure this and say uh
[14:59] simply I can measure this and say uh
[14:59] simply I can measure this and say uh prescribe this for the design and say
[15:01] prescribe this for the design and say
[15:01] prescribe this for the design and say it's going to have a C clip and you're
[15:03] it's going to have a C clip and you're
[15:03] it's going to have a C clip and you're going to have only a 2 mm um arm spring
[15:08] going to have only a 2 mm um arm spring
[15:08] going to have only a 2 mm um arm spring arms on it.
[15:11] arms on it.
[15:11] arms on it. And so I would consider that type of
[15:13] And so I would consider that type of
[15:13] And so I would consider that type of question that requires some exploration
[15:15] question that requires some exploration
[15:15] question that requires some exploration and data gathering um the research
[15:19] and data gathering um the research
[15:19] and data gathering um the research design questions. But once these are
[15:21] design questions. But once these are
[15:21] design questions. But once these are done, once we've accumulated these, and
[15:23] done, once we've accumulated these, and
[15:23] done, once we've accumulated these, and I've accumulated a lot so far, we then
[15:25] I've accumulated a lot so far, we then
[15:25] I've accumulated a lot so far, we then have new options that we can just copy
[15:27] have new options that we can just copy
[15:27] have new options that we can just copy and paste in other designs. And since
[15:30] and paste in other designs. And since
[15:30] and paste in other designs. And since these are extremely popular and 3D
[15:32] these are extremely popular and 3D
[15:32] these are extremely popular and 3D printing with ABS is very popular. um if
[15:36] printing with ABS is very popular. um if
[15:36] printing with ABS is very popular. um if I include this data, other people can
[15:39] I include this data, other people can
[15:39] I include this data, other people can reuse that solution in many other
[15:41] reuse that solution in many other
[15:41] reuse that solution in many other situations. It's just a matter of um how
[15:45] situations. It's just a matter of um how
[15:45] situations. It's just a matter of um how many research questions, which questions
[15:48] many research questions, which questions
[15:48] many research questions, which questions am I answering in my documentation and
[15:51] am I answering in my documentation and
[15:51] am I answering in my documentation and how do I describe that sufficiently to
[15:53] how do I describe that sufficiently to
[15:53] how do I describe that sufficiently to get uh transfer the understanding to the
[15:56] get uh transfer the understanding to the
[15:56] get uh transfer the understanding to the audience? That moves it down from a
[15:58] audience? That moves it down from a
[15:58] audience? That moves it down from a research question into a design
[16:00] research question into a design
[16:00] research question into a design question. the next person can just say,
[16:03] question. the next person can just say,
[16:03] question. the next person can just say, "How do I retain the thing?" Well, I can
[16:06] "How do I retain the thing?" Well, I can
[16:06] "How do I retain the thing?" Well, I can use an e-clipip that's been uh reduced
[16:09] use an e-clipip that's been uh reduced
[16:09] use an e-clipip that's been uh reduced in its spring force. Okay? So, all this
[16:12] in its spring force. Okay? So, all this
[16:12] in its spring force. Okay? So, all this design discussion only matters if the
[16:15] design discussion only matters if the
[16:15] design discussion only matters if the assembly can actually bear a load, which
[16:17] assembly can actually bear a load, which
[16:17] assembly can actually bear a load, which it can. So, I'll show you jumping ahead
[16:20] it can. So, I'll show you jumping ahead
[16:20] it can. So, I'll show you jumping ahead and running a test on one of these
[16:22] and running a test on one of these
[16:22] and running a test on one of these parts. Just understand there's a few
[16:24] parts. Just understand there's a few
[16:24] parts. Just understand there's a few variations. you so you'll see the one
[16:26] variations. you so you'll see the one
[16:26] variations. you so you'll see the one that has the bearing and all these
[16:28] that has the bearing and all these
[16:28] that has the bearing and all these variations have the same geometry um in
[16:32] variations have the same geometry um in
[16:32] variations have the same geometry um in common which bears the load. So we make
[16:35] common which bears the load. So we make
[16:35] common which bears the load. So we make a press fit in uh of the bearing into
[16:39] a press fit in uh of the bearing into
[16:39] a press fit in uh of the bearing into the part and then we install it.
[16:44] the part and then we install it.
[16:44] the part and then we install it. And what we're going to have is when the
[16:48] And what we're going to have is when the
[16:48] And what we're going to have is when the shaft pushes down on the bearing, it's
[16:50] shaft pushes down on the bearing, it's
[16:50] shaft pushes down on the bearing, it's going to want to tilt like this. it's
[16:53] going to want to tilt like this. it's
[16:53] going to want to tilt like this. it's going to be pulling on some of the
[16:54] going to be pulling on some of the
[16:54] going to be pulling on some of the features because there's a there's a
[16:56] features because there's a there's a
[16:56] features because there's a there's a moment
[16:58] moment
[16:58] moment on the part. Um only if the bearing was
[17:01] on the part. Um only if the bearing was
[17:02] on the part. Um only if the bearing was centered directly over that wall could
[17:04] centered directly over that wall could
[17:04] centered directly over that wall could we have no tilting or twisting and no
[17:07] we have no tilting or twisting and no
[17:07] we have no tilting or twisting and no moment. Um so given that constraint that
[17:11] moment. Um so given that constraint that
[17:11] moment. Um so given that constraint that limitation can how much weight can we
[17:14] limitation can how much weight can we
[17:14] limitation can how much weight can we hold? So far I've tested only using this
[17:17] hold? So far I've tested only using this
[17:17] hold? So far I've tested only using this method. So I set a block on top of those
[17:20] method. So I set a block on top of those
[17:20] method. So I set a block on top of those shafts. Um, I keep it from slipping out
[17:23] shafts. Um, I keep it from slipping out
[17:23] shafts. Um, I keep it from slipping out of place with those pieces of cork. And
[17:27] of place with those pieces of cork. And
[17:27] of place with those pieces of cork. And then we can start pressing on it. And to
[17:30] then we can start pressing on it. And to
[17:30] then we can start pressing on it. And to press more, I can come over here,
[17:34] press more, I can come over here,
[17:34] press more, I can come over here, set the wood on it. I'm going to steady
[17:36] set the wood on it. I'm going to steady
[17:36] set the wood on it. I'm going to steady my hands on this bench, but I'm going to
[17:38] my hands on this bench, but I'm going to
[17:38] my hands on this bench, but I'm going to put my weight on the assembly. Okay. So,
[17:43] put my weight on the assembly. Okay. So,
[17:43] put my weight on the assembly. Okay. So, I can stand on there. Oh, I just tilted
[17:46] I can stand on there. Oh, I just tilted
[17:46] I can stand on there. Oh, I just tilted back to my heel. I'm sure that I just
[17:49] back to my heel. I'm sure that I just
[17:49] back to my heel. I'm sure that I just put all of my weight on there. And so we
[17:54] put all of my weight on there. And so we
[17:54] put all of my weight on there. And so we have
[17:56] have
[17:56] have no problems, no defect from performing
[18:00] no problems, no defect from performing
[18:00] no problems, no defect from performing these tests. And so that even if we
[18:05] these tests. And so that even if we
[18:05] these tests. And so that even if we don't use it in that heavy of a range,
[18:07] don't use it in that heavy of a range,
[18:07] don't use it in that heavy of a range, we have a really good starting point to
[18:09] we have a really good starting point to
[18:09] we have a really good starting point to know um what applications, what span of
[18:13] know um what applications, what span of
[18:13] know um what applications, what span of of loads can we tolerate on an assembly
[18:16] of loads can we tolerate on an assembly
[18:16] of loads can we tolerate on an assembly like this.
[18:18] like this.
[18:18] like this. Okay, now I'm going to voice over a
[18:19] Okay, now I'm going to voice over a
[18:20] Okay, now I'm going to voice over a little bit and improve this explanation.
[18:22] little bit and improve this explanation.
[18:22] little bit and improve this explanation. I took a moment to carefully define
[18:25] I took a moment to carefully define
[18:25] I took a moment to carefully define design because we have a more
[18:27] design because we have a more
[18:27] design because we have a more complicated situation than a typical
[18:29] complicated situation than a typical
[18:29] complicated situation than a typical design. We are creating a parametric
[18:32] design. We are creating a parametric
[18:32] design. We are creating a parametric part and then that part is developing
[18:35] part and then that part is developing
[18:35] part and then that part is developing sister parts or children parts that have
[18:38] sister parts or children parts that have
[18:38] sister parts or children parts that have some similarities and some differences.
[18:41] some similarities and some differences.
[18:41] some similarities and some differences. The first five questions that I wrote in
[18:43] The first five questions that I wrote in
[18:43] The first five questions that I wrote in black are considered to be the questions
[18:46] black are considered to be the questions
[18:46] black are considered to be the questions answered for this initial design. The
[18:49] answered for this initial design. The
[18:49] answered for this initial design. The bushing style part which has no bearings
[18:53] bushing style part which has no bearings
[18:53] bushing style part which has no bearings and it has the the simplest geometry.
[18:58] and it has the the simplest geometry.
[18:58] and it has the the simplest geometry. Each of the numbered items uh such as
[19:00] Each of the numbered items uh such as
[19:00] Each of the numbered items uh such as number one, it says hold steady. That is
[19:03] number one, it says hold steady. That is
[19:03] number one, it says hold steady. That is corresponding to a question. How will we
[19:06] corresponding to a question. How will we
[19:06] corresponding to a question. How will we hold the shaft steady? And we mentioned
[19:09] hold the shaft steady? And we mentioned
[19:09] hold the shaft steady? And we mentioned the answer. It's going to have a slip
[19:11] the answer. It's going to have a slip
[19:11] the answer. It's going to have a slip fit, but it'll sit resting on the
[19:15] fit, but it'll sit resting on the
[19:15] fit, but it'll sit resting on the interior hole of the part. And so each
[19:18] interior hole of the part. And so each
[19:18] interior hole of the part. And so each of these questions,
[19:20] of these questions,
[19:20] of these questions, well, these answers aren't written down
[19:22] well, these answers aren't written down
[19:22] well, these answers aren't written down in words anywhere. They are built into
[19:26] in words anywhere. They are built into
[19:26] in words anywhere. They are built into the geometry of that physical part. And
[19:29] the geometry of that physical part. And
[19:29] the geometry of that physical part. And they are stored, for instance, in the
[19:31] they are stored, for instance, in the
[19:31] they are stored, for instance, in the CAD model. Um, they get carried over to
[19:34] CAD model. Um, they get carried over to
[19:34] CAD model. Um, they get carried over to the physical part that gets printed.
[19:37] the physical part that gets printed.
[19:37] the physical part that gets printed. So when I publish this design and call
[19:39] So when I publish this design and call
[19:39] So when I publish this design and call it sleeve, that's sleeve.solid part. Um
[19:43] it sleeve, that's sleeve.solid part. Um
[19:43] it sleeve, that's sleeve.solid part. Um that's a design that takes all questions
[19:47] that's a design that takes all questions
[19:47] that's a design that takes all questions one through five and delivers an answer
[19:50] one through five and delivers an answer
[19:50] one through five and delivers an answer and then uh to demonstrate adding on
[19:53] and then uh to demonstrate adding on
[19:53] and then uh to demonstrate adding on another criteria to the same set of
[19:56] another criteria to the same set of
[19:56] another criteria to the same set of answers um as intended from the very
[20:00] answers um as intended from the very
[20:00] answers um as intended from the very start. We have the same design where
[20:03] start. We have the same design where
[20:04] start. We have the same design where most of the features are in common
[20:05] most of the features are in common
[20:05] most of the features are in common because those features answers the
[20:07] because those features answers the
[20:07] because those features answers the answer these questions. So sleeve BR is
[20:11] answer these questions. So sleeve BR is
[20:11] answer these questions. So sleeve BR is for a sleeve with a bearing and it
[20:14] for a sleeve with a bearing and it
[20:14] for a sleeve with a bearing and it simply has a widened shell and it now it
[20:18] simply has a widened shell and it now it
[20:18] simply has a widened shell and it now it carries this bearing for an 8 mm shaft.
[20:20] carries this bearing for an 8 mm shaft.
[20:20] carries this bearing for an 8 mm shaft. It's a 608 bearing. And so if you want
[20:23] It's a 608 bearing. And so if you want
[20:23] It's a 608 bearing. And so if you want one through six, those are in the file
[20:27] one through six, those are in the file
[20:27] one through six, those are in the file called sleeve BR. But the file starts to
[20:29] called sleeve BR. But the file starts to
[20:29] called sleeve BR. But the file starts to get more complicated.
[20:31] get more complicated.
[20:31] get more complicated. So this is where my methods break off
[20:34] So this is where my methods break off
[20:34] So this is where my methods break off from traditional engineering design
[20:36] from traditional engineering design
[20:36] from traditional engineering design methods. We have a second part which you
[20:40] methods. We have a second part which you
[20:40] methods. We have a second part which you could consider a version two that
[20:43] could consider a version two that
[20:43] could consider a version two that enhances the design for one specific
[20:46] enhances the design for one specific
[20:46] enhances the design for one specific application but not for every
[20:48] application but not for every
[20:48] application but not for every application. So I want to take this
[20:51] application. So I want to take this
[20:51] application. So I want to take this group of features all in the CAD model
[20:54] group of features all in the CAD model
[20:54] group of features all in the CAD model where we have answered a cohesive set of
[20:56] where we have answered a cohesive set of
[20:56] where we have answered a cohesive set of questions before proceeding and save
[20:59] questions before proceeding and save
[20:59] questions before proceeding and save this and give it a name and then
[21:01] this and give it a name and then
[21:01] this and give it a name and then describe in documentation what is the
[21:03] describe in documentation what is the
[21:03] describe in documentation what is the function of that specific part so other
[21:06] function of that specific part so other
[21:06] function of that specific part so other users can download and access and reuse
[21:10] users can download and access and reuse
[21:10] users can download and access and reuse the solutions that are already embedded
[21:12] the solutions that are already embedded
[21:12] the solutions that are already embedded in the part and then proceed to make a
[21:15] in the part and then proceed to make a
[21:15] in the part and then proceed to make a second version and give it a name.
[21:18] second version and give it a name.
[21:18] second version and give it a name. So here are these three parts side by
[21:21] So here are these three parts side by
[21:21] So here are these three parts side by side. Sleeve which was made first,
[21:23] side. Sleeve which was made first,
[21:24] side. Sleeve which was made first, sleeve BR that was derived from this one
[21:26] sleeve BR that was derived from this one
[21:26] sleeve BR that was derived from this one and BR inch which was derived from this
[21:29] and BR inch which was derived from this
[21:29] and BR inch which was derived from this one. And each time I made changes to add
[21:32] one. And each time I made changes to add
[21:32] one. And each time I made changes to add value, right? But some of those changes
[21:36] value, right? But some of those changes
[21:36] value, right? But some of those changes remove value that lives inside of this
[21:39] remove value that lives inside of this
[21:39] remove value that lives inside of this one. So for example, if you want an
[21:41] one. So for example, if you want an
[21:41] one. So for example, if you want an assembly that's low cost and minimal,
[21:43] assembly that's low cost and minimal,
[21:43] assembly that's low cost and minimal, you don't need this ultra low friction.
[21:45] you don't need this ultra low friction.
[21:45] you don't need this ultra low friction. then you wouldn't want to spend the
[21:48] then you wouldn't want to spend the
[21:48] then you wouldn't want to spend the money on these bearings. And so each one
[21:51] money on these bearings. And so each one
[21:51] money on these bearings. And so each one of them deserves to exist. That's why
[21:53] of them deserves to exist. That's why
[21:53] of them deserves to exist. That's why I'm publishing uh multiple solid files
[21:56] I'm publishing uh multiple solid files
[21:56] I'm publishing uh multiple solid files instead of just one. I'll add a personal
[21:59] instead of just one. I'll add a personal
[21:59] instead of just one. I'll add a personal note here that can only come from
[22:01] note here that can only come from
[22:01] note here that can only come from experience. Okay. So you have this open-
[22:03] experience. Okay. So you have this open-
[22:03] experience. Okay. So you have this open- source robot. It has a hundred very
[22:07] source robot. It has a hundred very
[22:07] source robot. It has a hundred very useful, very versatile components. It
[22:09] useful, very versatile components. It
[22:10] useful, very versatile components. It was specifically designed so that the
[22:12] was specifically designed so that the
[22:12] was specifically designed so that the modules inside would have their own
[22:14] modules inside would have their own
[22:14] modules inside would have their own value. in student projects. That's all
[22:17] value. in student projects. That's all
[22:17] value. in student projects. That's all related to my role as an educator at the
[22:21] related to my role as an educator at the
[22:21] related to my role as an educator at the university. Um, but inside that design,
[22:26] university. Um, but inside that design,
[22:26] university. Um, but inside that design, nobody is actually discovering the parts
[22:30] nobody is actually discovering the parts
[22:30] nobody is actually discovering the parts and the components and the value of
[22:31] and the components and the value of
[22:32] and the components and the value of those parts. So, I've published this uh
[22:35] those parts. So, I've published this uh
[22:35] those parts. So, I've published this uh robot that we're talking years ago.
[22:37] robot that we're talking years ago.
[22:37] robot that we're talking years ago. Let's say you get um a 100red downloads
[22:40] Let's say you get um a 100red downloads
[22:40] Let's say you get um a 100red downloads on GrabCAD and and truly any other
[22:43] on GrabCAD and and truly any other
[22:43] on GrabCAD and and truly any other platform. No one's expecting that we're
[22:46] platform. No one's expecting that we're
[22:46] platform. No one's expecting that we're designing in this way to actually help
[22:48] designing in this way to actually help
[22:48] designing in this way to actually help them. So, I'll publish this, get a 100
[22:51] them. So, I'll publish this, get a 100
[22:51] them. So, I'll publish this, get a 100 downloads, and then separately later,
[22:54] downloads, and then separately later,
[22:54] downloads, and then separately later, I'm like, there's so much more in here.
[22:57] I'm like, there's so much more in here.
[22:57] I'm like, there's so much more in here. I'll publish the design of this little
[22:59] I'll publish the design of this little
[22:59] I'll publish the design of this little fan or this little terminal, and that
[23:02] fan or this little terminal, and that
[23:02] fan or this little terminal, and that design will get 5,000 downloads in a
[23:07] design will get 5,000 downloads in a
[23:07] design will get 5,000 downloads in a month. And it's just comm. just showing
[23:10] month. And it's just comm. just showing
[23:10] month. And it's just comm. just showing it's because um no one is expecting that
[23:13] it's because um no one is expecting that
[23:14] it's because um no one is expecting that the assembly and the parts inside of a
[23:16] the assembly and the parts inside of a
[23:16] the assembly and the parts inside of a large design are made up to the quality
[23:19] large design are made up to the quality
[23:19] large design are made up to the quality that those components are actually
[23:21] that those components are actually
[23:21] that those components are actually helpful to them. And that makes sense.
[23:24] helpful to them. And that makes sense.
[23:24] helpful to them. And that makes sense. It's not an ordinary thing. We don't put
[23:26] It's not an ordinary thing. We don't put
[23:26] It's not an ordinary thing. We don't put the design uh the details usually into
[23:31] the design uh the details usually into
[23:31] the design uh the details usually into all of our parts in such a manner that
[23:34] all of our parts in such a manner that
[23:34] all of our parts in such a manner that this bracket here, this design that I
[23:38] this bracket here, this design that I
[23:38] this bracket here, this design that I publish on the robot is more useful to
[23:41] publish on the robot is more useful to
[23:41] publish on the robot is more useful to you than getting this design from the
[23:44] you than getting this design from the
[23:44] you than getting this design from the manufacturer because I cleaned up the
[23:46] manufacturer because I cleaned up the
[23:46] manufacturer because I cleaned up the model and made it easier to work with
[23:48] model and made it easier to work with
[23:48] model and made it easier to work with and added names and datmss and uh
[23:51] and added names and datmss and uh
[23:51] and added names and datmss and uh everything that the engineers need to
[23:53] everything that the engineers need to
[23:53] everything that the engineers need to proceed from there. And so
[23:57] proceed from there. And so
[23:57] proceed from there. And so many many interactions like that have
[24:00] many many interactions like that have
[24:00] many many interactions like that have led me to uh let's say if I publish a
[24:03] led me to uh let's say if I publish a
[24:04] led me to uh let's say if I publish a part I've got to focus on the part and
[24:07] part I've got to focus on the part and
[24:07] part I've got to focus on the part and so I'll still create assemblies and
[24:09] so I'll still create assemblies and
[24:09] so I'll still create assemblies and demonstrations but I'm going to focus
[24:12] demonstrations but I'm going to focus
[24:12] demonstrations but I'm going to focus the communication and explain that the
[24:15] the communication and explain that the
[24:15] the communication and explain that the value in this part is so much more. Um,
[24:19] value in this part is so much more. Um,
[24:19] value in this part is so much more. Um, and you're looking at a part that's far
[24:21] and you're looking at a part that's far
[24:21] and you're looking at a part that's far more refined where the effort went into
[24:24] more refined where the effort went into
[24:24] more refined where the effort went into this and not into this. Um, the refined
[24:28] this and not into this. Um, the refined
[24:28] this and not into this. Um, the refined effort is in here. And so, let's publish
[24:30] effort is in here. And so, let's publish
[24:30] effort is in here. And so, let's publish the parts individually and describe
[24:33] the parts individually and describe
[24:33] the parts individually and describe them. And that has formulated my that
[24:35] them. And that has formulated my that
[24:35] them. And that has formulated my that has formed my mindset about how I'm uh I
[24:39] has formed my mindset about how I'm uh I
[24:39] has formed my mindset about how I'm uh I publishing open-source models. And it is
[24:43] publishing open-source models. And it is
[24:43] publishing open-source models. And it is unlocking this awareness that okay these
[24:46] unlocking this awareness that okay these
[24:46] unlocking this awareness that okay these these models aren't all equivalent. You
[24:49] these models aren't all equivalent. You
[24:49] these models aren't all equivalent. You can design specifically for open source
[24:51] can design specifically for open source
[24:51] can design specifically for open source and it's a lot more helpful for the
[24:54] and it's a lot more helpful for the
[24:54] and it's a lot more helpful for the recipient for the downloader and then uh
[24:57] recipient for the downloader and then uh
[24:57] recipient for the downloader and then uh people have had their good will and
[25:01] people have had their good will and
[25:01] people have had their good will and actually they're raising their quality
[25:03] actually they're raising their quality
[25:03] actually they're raising their quality together and we're learning from each
[25:05] together and we're learning from each
[25:05] together and we're learning from each other.
[25:07] other.
[25:07] other. Okay, we have a design, we have a
[25:09] Okay, we have a design, we have a
[25:09] Okay, we have a design, we have a sleeve. Now, if we install two of these,
[25:12] sleeve. Now, if we install two of these,
[25:12] sleeve. Now, if we install two of these, we support a shaft. If we install two
[25:14] we support a shaft. If we install two
[25:14] we support a shaft. If we install two more, we could have two shafts. Maybe
[25:16] more, we could have two shafts. Maybe
[25:16] more, we could have two shafts. Maybe that's the simplest application we can
[25:19] that's the simplest application we can
[25:19] that's the simplest application we can go to. But we covered design questions
[25:22] go to. But we covered design questions
[25:22] go to. But we covered design questions and the need. Now, one of those needs
[25:25] and the need. Now, one of those needs
[25:25] and the need. Now, one of those needs can fit in an application. And that
[25:28] can fit in an application. And that
[25:28] can fit in an application. And that looks like this. We have a gear box um
[25:32] looks like this. We have a gear box um
[25:32] looks like this. We have a gear box um or a belt box. Not sure. Anyway, we can
[25:35] or a belt box. Not sure. Anyway, we can
[25:35] or a belt box. Not sure. Anyway, we can use a chain or we could use any other
[25:38] use a chain or we could use any other
[25:38] use a chain or we could use any other driving mechanism such as a belt or even
[25:41] driving mechanism such as a belt or even
[25:41] driving mechanism such as a belt or even a simple O-ring made to be used as a
[25:45] a simple O-ring made to be used as a
[25:45] a simple O-ring made to be used as a belt. In this case, we have a 25 to uh
[25:49] belt. In this case, we have a 25 to uh
[25:49] belt. In this case, we have a 25 to uh pulley on the input shaft and an output
[25:52] pulley on the input shaft and an output
[25:52] pulley on the input shaft and an output shaft with 10 [snorts] teeth. So, it's a
[25:55] shaft with 10 [snorts] teeth. So, it's a
[25:55] shaft with 10 [snorts] teeth. So, it's a 2.5 times increase if we're driving the
[25:59] 2.5 times increase if we're driving the
[25:59] 2.5 times increase if we're driving the system from this side. So, if I drive it
[26:03] system from this side. So, if I drive it
[26:03] system from this side. So, if I drive it with my driver, it spins. [snorts]
[26:06] with my driver, it spins. [snorts]
[26:06] with my driver, it spins. [snorts] We have everything moving
[26:10] We have everything moving
[26:10] We have everything moving and this could handle a fair amount of
[26:11] and this could handle a fair amount of
[26:11] and this could handle a fair amount of torque. There hasn't been much testing
[26:14] torque. There hasn't been much testing
[26:14] torque. There hasn't been much testing yet.
[26:25] But in any case, that works. And so, we
[26:25] But in any case, that works. And so, we could continue with that example. What
[26:27] could continue with that example. What
[26:27] could continue with that example. What might I get? What would I want that for?
[26:30] might I get? What would I want that for?
[26:30] might I get? What would I want that for? Um, one example is a high-speed tool.
[26:34] Um, one example is a high-speed tool.
[26:34] Um, one example is a high-speed tool. Um, just like a Dremel only having more
[26:37] Um, just like a Dremel only having more
[26:37] Um, just like a Dremel only having more torque, which is something that I very
[26:39] torque, which is something that I very
[26:39] torque, which is something that I very much need. We could make this to be
[26:41] much need. We could make this to be
[26:41] much need. We could make this to be mounted on a benchtop. And that's
[26:43] mounted on a benchtop. And that's
[26:43] mounted on a benchtop. And that's something I actually want um a benchtop
[26:46] something I actually want um a benchtop
[26:46] something I actually want um a benchtop mounted um driving tool to drive these
[26:51] mounted um driving tool to drive these
[26:51] mounted um driving tool to drive these um tools that have a 1/8 in shaft or 3.2
[26:56] um tools that have a 1/8 in shaft or 3.2
[26:56] um tools that have a 1/8 in shaft or 3.2 2 millimeter shaft uh like this carbide
[26:59] 2 millimeter shaft uh like this carbide
[26:59] 2 millimeter shaft uh like this carbide burr because when you have this high
[27:01] burr because when you have this high
[27:01] burr because when you have this high speed, it's a whole different range of
[27:04] speed, it's a whole different range of
[27:04] speed, it's a whole different range of utility compared with the lower speed
[27:07] utility compared with the lower speed
[27:07] utility compared with the lower speed tools. Almost everything in our shops
[27:10] tools. Almost everything in our shops
[27:10] tools. Almost everything in our shops are somewhere around 3,000 and less
[27:13] are somewhere around 3,000 and less
[27:13] are somewhere around 3,000 and less RPMs, whereas this one goes up to 25,000
[27:17] RPMs, whereas this one goes up to 25,000
[27:17] RPMs, whereas this one goes up to 25,000 RPMs. And it really changes the
[27:20] RPMs. And it really changes the
[27:20] RPMs. And it really changes the functionality. It changes which devices
[27:23] functionality. It changes which devices
[27:23] functionality. It changes which devices you'd want to connect with it. And so um
[27:26] you'd want to connect with it. And so um
[27:26] you'd want to connect with it. And so um I'd like to work towards that and maybe
[27:29] I'd like to work towards that and maybe
[27:29] I'd like to work towards that and maybe many other people will work towards
[27:30] many other people will work towards
[27:30] many other people will work towards their own applications or the same and
[27:33] their own applications or the same and
[27:33] their own applications or the same and that can uh be a collaborative thing.
[27:35] that can uh be a collaborative thing.
[27:35] that can uh be a collaborative thing. But at least now we have one
[27:37] But at least now we have one
[27:37] But at least now we have one demonstration that we can make our our
[27:39] demonstration that we can make our our
[27:39] demonstration that we can make our our initial observations and start to test
[27:42] initial observations and start to test
[27:42] initial observations and start to test and examine what's possible and what
[27:45] and examine what's possible and what
[27:45] and examine what's possible and what would need to be adjusted.
[27:47] would need to be adjusted.
[27:47] would need to be adjusted. The next application demonstrates
[27:50] The next application demonstrates
[27:50] The next application demonstrates meeting a completely different um
[27:53] meeting a completely different um
[27:53] meeting a completely different um outcome with mostly the same needs. And
[27:56] outcome with mostly the same needs. And
[27:56] outcome with mostly the same needs. And so this same bushing sorry sleeve is
[27:59] so this same bushing sorry sleeve is
[27:59] so this same bushing sorry sleeve is being used. And this is a variation of
[28:03] being used. And this is a variation of
[28:03] being used. And this is a variation of the model mostly with shared features.
[28:06] the model mostly with shared features.
[28:06] the model mostly with shared features. And then the added bearing and this is
[28:08] And then the added bearing and this is
[28:08] And then the added bearing and this is the bearing that has a 1/2 in inner
[28:11] the bearing that has a 1/2 in inner
[28:11] the bearing that has a 1/2 in inner diameter. And so this part is um 90% of
[28:16] diameter. And so this part is um 90% of
[28:16] diameter. And so this part is um 90% of the work was already done in the initial
[28:20] the work was already done in the initial
[28:20] the work was already done in the initial design. We add a very small effort to
[28:23] design. We add a very small effort to
[28:23] design. We add a very small effort to accommodate that bearing and then we can
[28:26] accommodate that bearing and then we can
[28:26] accommodate that bearing and then we can do a completely different thing. Um I'm
[28:29] do a completely different thing. Um I'm
[28:29] do a completely different thing. Um I'm not really intending to use this
[28:31] not really intending to use this
[28:31] not really intending to use this assembly. I wanted to tinker and I
[28:34] assembly. I wanted to tinker and I
[28:34] assembly. I wanted to tinker and I wanted to explore well how much load can
[28:36] wanted to explore well how much load can
[28:36] wanted to explore well how much load can we put in this uh steel box and how much
[28:41] we put in this uh steel box and how much
[28:41] we put in this uh steel box and how much will things fall apart if we start to
[28:43] will things fall apart if we start to
[28:43] will things fall apart if we start to spin it and uh so that is a significant
[28:47] spin it and uh so that is a significant
[28:47] spin it and uh so that is a significant amount of mass and that's just giving me
[28:50] amount of mass and that's just giving me
[28:50] amount of mass and that's just giving me more data that I can use to um to decide
[28:55] more data that I can use to um to decide
[28:55] more data that I can use to um to decide on what configurations what are the
[28:57] on what configurations what are the
[28:57] on what configurations what are the limitations of the parts directly 3D
[29:00] limitations of the parts directly 3D
[29:00] limitations of the parts directly 3D printed as they are. And
[29:09] well, it this this whole situation
[29:09] well, it this this whole situation starts with observations. I don't have
[29:11] starts with observations. I don't have
[29:11] starts with observations. I don't have too much to say about it because this
[29:13] too much to say about it because this
[29:13] too much to say about it because this was a quick project just for me to play.
[29:16] was a quick project just for me to play.
[29:16] was a quick project just for me to play. You can see I I screwed these into the
[29:19] You can see I I screwed these into the
[29:19] You can see I I screwed these into the 2x4 just to get something mounted and to
[29:22] 2x4 just to get something mounted and to
[29:22] 2x4 just to get something mounted and to be able to get uh get this laith chuck
[29:26] be able to get uh get this laith chuck
[29:26] be able to get uh get this laith chuck spinning. This [snorts] is around 60
[29:28] spinning. This [snorts] is around 60
[29:28] spinning. This [snorts] is around 60 bucks on Amazon. And so now we are
[29:31] bucks on Amazon. And so now we are
[29:31] bucks on Amazon. And so now we are seeing this per integration. Integrating
[29:34] seeing this per integration. Integrating
[29:34] seeing this per integration. Integrating these off-the-shelf parts gives us easy
[29:37] these off-the-shelf parts gives us easy
[29:37] these off-the-shelf parts gives us easy access to start configuring a machine
[29:40] access to start configuring a machine
[29:40] access to start configuring a machine however you want to. If you want to
[29:42] however you want to. If you want to
[29:42] however you want to. If you want to configure the drive um the driving input
[29:46] configure the drive um the driving input
[29:46] configure the drive um the driving input spinning shaft the way that you want to
[29:48] spinning shaft the way that you want to
[29:48] spinning shaft the way that you want to and the speed that you want to. Now
[29:50] and the speed that you want to. Now
[29:50] and the speed that you want to. Now we're get starting to get that freedom.
[29:54] we're get starting to get that freedom.
[29:54] we're get starting to get that freedom. So we basically have um these three
[29:56] So we basically have um these three
[29:56] So we basically have um these three parts forming a tree where the most of
[30:01] parts forming a tree where the most of
[30:01] parts forming a tree where the most of the work and most of the trouble to find
[30:04] the work and most of the trouble to find
[30:04] the work and most of the trouble to find answers and test things out was
[30:07] answers and test things out was
[30:07] answers and test things out was performed on this main branch that
[30:09] performed on this main branch that
[30:09] performed on this main branch that sleeve solid part. Um these ones are
[30:13] sleeve solid part. Um these ones are
[30:13] sleeve solid part. Um these ones are derived. Okay. Now why do I not just
[30:16] derived. Okay. Now why do I not just
[30:16] derived. Okay. Now why do I not just make three configurations of one file?
[30:19] make three configurations of one file?
[30:19] make three configurations of one file? Why am I publishing three files? That's
[30:22] Why am I publishing three files? That's
[30:22] Why am I publishing three files? That's where we come and we find that there's
[30:25] where we come and we find that there's
[30:25] where we come and we find that there's been branched off already. This uh
[30:29] been branched off already. This uh
[30:29] been branched off already. This uh sleeve variation where we have the
[30:30] sleeve variation where we have the
[30:30] sleeve variation where we have the offset and the centered version, those
[30:34] offset and the centered version, those
[30:34] offset and the centered version, those already come from inside of sleeve. And
[30:37] already come from inside of sleeve. And
[30:37] already come from inside of sleeve. And so you have sleeves
[30:46] for offset. That's the one that has the
[30:46] for offset. That's the one that has the 3 mm um moved over center line. Okay.
[30:51] 3 mm um moved over center line. Okay.
[30:51] 3 mm um moved over center line. Okay. But the sleeve OFS um this is a
[30:55] But the sleeve OFS um this is a
[30:55] But the sleeve OFS um this is a configuration inside of sleeve and it's
[30:58] configuration inside of sleeve and it's
[30:58] configuration inside of sleeve and it's defined by having this uh this dimension
[31:01] defined by having this uh this dimension
[31:01] defined by having this uh this dimension here
[31:02] here
[31:02] here where we have our offset distance.
[31:07] where we have our offset distance.
[31:07] where we have our offset distance. And so that's offset.
[31:10] And so that's offset.
[31:10] And so that's offset. That's a variable that lives inside the
[31:12] That's a variable that lives inside the
[31:12] That's a variable that lives inside the CAD model. And any designer can open up
[31:16] CAD model. And any designer can open up
[31:16] CAD model. And any designer can open up the file and adjust that. And so
[31:20] the file and adjust that. And so
[31:20] the file and adjust that. And so we have uh not just different
[31:22] we have uh not just different
[31:22] we have uh not just different configurations with this parameter but
[31:24] configurations with this parameter but
[31:24] configurations with this parameter but actual a whole range that you can make
[31:28] actual a whole range that you can make
[31:28] actual a whole range that you can make this zero or you can make it uh maybe
[31:32] this zero or you can make it uh maybe
[31:32] this zero or you can make it uh maybe you can go all the way up to 5 mm and
[31:34] you can go all the way up to 5 mm and
[31:34] you can go all the way up to 5 mm and you can place that anywhere that you
[31:36] you can place that anywhere that you
[31:36] you can place that anywhere that you need to. And if I were designing the
[31:40] need to. And if I were designing the
[31:40] need to. And if I were designing the next um the next assembly, let's say I'm
[31:43] next um the next assembly, let's say I'm
[31:43] next um the next assembly, let's say I'm going to use this rubber belt and I want
[31:45] going to use this rubber belt and I want
[31:45] going to use this rubber belt and I want an exact offset, then I'm going to
[31:48] an exact offset, then I'm going to
[31:48] an exact offset, then I'm going to choose a new value for this.
[31:52] choose a new value for this.
[31:52] choose a new value for this. And I'm going to then produce the let's
[31:56] And I'm going to then produce the let's
[31:56] And I'm going to then produce the let's say the STL model and [snorts] then
[31:58] say the STL model and [snorts] then
[31:58] say the STL model and [snorts] then print.
[32:05] And this may be saved inside of a folder
[32:05] And this may be saved inside of a folder that has all the other parts for my belt
[32:08] that has all the other parts for my belt
[32:08] that has all the other parts for my belt driven assembly. So if this is one
[32:12] driven assembly. So if this is one
[32:12] driven assembly. So if this is one parameter um and that's the offset the
[32:16] parameter um and that's the offset the
[32:16] parameter um and that's the offset the there are a couple of other parameters
[32:18] there are a couple of other parameters
[32:18] there are a couple of other parameters as well. So for example this whole uh
[32:22] as well. So for example this whole uh
[32:22] as well. So for example this whole uh this series of humps that's intended to
[32:26] this series of humps that's intended to
[32:26] this series of humps that's intended to mate with the this is called a halfinch
[32:29] mate with the this is called a halfinch
[32:29] mate with the this is called a halfinch trade size. Um the hole in this box,
[32:32] trade size. Um the hole in this box,
[32:32] trade size. Um the hole in this box, it's because it goes with the half inch
[32:35] it's because it goes with the half inch
[32:35] it's because it goes with the half inch trade. It's much larger than a half
[32:36] trade. It's much larger than a half
[32:36] trade. It's much larger than a half inch, 22ish millimeters. Um that goes
[32:40] inch, 22ish millimeters. Um that goes
[32:40] inch, 22ish millimeters. Um that goes with the EMT conduit that's half inch.
[32:43] with the EMT conduit that's half inch.
[32:43] with the EMT conduit that's half inch. And uh we have 3/4 in. And we also have
[32:47] And uh we have 3/4 in. And we also have
[32:47] And uh we have 3/4 in. And we also have unlimited numbers of holes in every
[32:49] unlimited numbers of holes in every
[32:49] unlimited numbers of holes in every other uh thinwalled steel or or metal um
[32:53] other uh thinwalled steel or or metal um
[32:53] other uh thinwalled steel or or metal um apparatus. You may want to change the
[32:56] apparatus. You may want to change the
[32:56] apparatus. You may want to change the thickness of this region here for a
[32:59] thickness of this region here for a
[32:59] thickness of this region here for a different thickness of a wall. This part
[33:02] different thickness of a wall. This part
[33:02] different thickness of a wall. This part still has enough engineering in it that
[33:04] still has enough engineering in it that
[33:04] still has enough engineering in it that it's worth it to copy the part or copy
[33:07] it's worth it to copy the part or copy
[33:07] it's worth it to copy the part or copy those features rather than reproducing
[33:10] those features rather than reproducing
[33:10] those features rather than reproducing all of the um the exploration that it
[33:13] all of the um the exploration that it
[33:13] all of the um the exploration that it takes. We know that it works. We know
[33:15] takes. We know that it works. We know
[33:15] takes. We know that it works. We know how much gap you need between the
[33:17] how much gap you need between the
[33:17] how much gap you need between the dimension of this and the dimension of a
[33:20] dimension of this and the dimension of a
[33:20] dimension of this and the dimension of a hole. And so you can retain that
[33:23] hole. And so you can retain that
[33:23] hole. And so you can retain that reproduce. You can make several
[33:25] reproduce. You can make several
[33:25] reproduce. You can make several adjustments of variables and then
[33:27] adjustments of variables and then
[33:27] adjustments of variables and then reproduce that design very very quickly.
[33:30] reproduce that design very very quickly.
[33:30] reproduce that design very very quickly. So how does all that look in the CAD
[33:33] So how does all that look in the CAD
[33:33] So how does all that look in the CAD model? Well, um we come from the feature
[33:36] model? Well, um we come from the feature
[33:36] model? Well, um we come from the feature tree. That's the default tab over to
[33:38] tree. That's the default tab over to
[33:38] tree. That's the default tab over to configuration manager. And if you were
[33:40] configuration manager. And if you were
[33:40] configuration manager. And if you were to just open this and start working with
[33:42] to just open this and start working with
[33:42] to just open this and start working with it, you'll see these two configurations.
[33:45] it, you'll see these two configurations.
[33:45] it, you'll see these two configurations. It's a double click to go to the offset
[33:47] It's a double click to go to the offset
[33:48] It's a double click to go to the offset configuration or to go back to this one.
[33:51] configuration or to go back to this one.
[33:51] configuration or to go back to this one. Um, and when you go into those, oops,
[33:55] Um, and when you go into those, oops,
[33:55] Um, and when you go into those, oops, hey, stop that. You can see this cut
[34:00] hey, stop that. You can see this cut
[34:00] hey, stop that. You can see this cut rectangle for example, it is simply
[34:02] rectangle for example, it is simply
[34:02] rectangle for example, it is simply suppressed.
[34:04] suppressed.
[34:04] suppressed. So, the feature is added. The
[34:06] So, the feature is added. The
[34:06] So, the feature is added. The information is still in this file, but
[34:09] information is still in this file, but
[34:09] information is still in this file, but it is um not manifesting itself. And
[34:12] it is um not manifesting itself. And
[34:12] it is um not manifesting itself. And that's exactly the same as commenting
[34:14] that's exactly the same as commenting
[34:14] that's exactly the same as commenting out our code. Okay, from this point I
[34:17] out our code. Okay, from this point I
[34:17] out our code. Okay, from this point I think I'll do a voice over to abbreviate
[34:19] think I'll do a voice over to abbreviate
[34:19] think I'll do a voice over to abbreviate this section I had recorded um because
[34:22] this section I had recorded um because
[34:22] this section I had recorded um because we're kind of going into the details of
[34:24] we're kind of going into the details of
[34:24] we're kind of going into the details of how this functions inside the CAD model,
[34:26] how this functions inside the CAD model,
[34:26] how this functions inside the CAD model, but that's all depending on somebody
[34:29] but that's all depending on somebody
[34:29] but that's all depending on somebody who's using Solid Works. Um however, the
[34:34] who's using Solid Works. Um however, the
[34:34] who's using Solid Works. Um however, the workflows are similar in all of the
[34:36] workflows are similar in all of the
[34:36] workflows are similar in all of the other CAD programs. It's just a a
[34:39] other CAD programs. It's just a a
[34:39] other CAD programs. It's just a a question of whether the designer
[34:42] question of whether the designer
[34:42] question of whether the designer actually implemented
[34:44] actually implemented
[34:44] actually implemented um more layers of detail in a CAD model
[34:47] um more layers of detail in a CAD model
[34:47] um more layers of detail in a CAD model or not. And so that discussion of how to
[34:50] or not. And so that discussion of how to
[34:50] or not. And so that discussion of how to handle um these details on the possible
[34:53] handle um these details on the possible
[34:53] handle um these details on the possible variations of parts and still maintain
[34:56] variations of parts and still maintain
[34:56] variations of parts and still maintain the functionality and somehow
[34:59] the functionality and somehow
[34:59] the functionality and somehow potentially make these designs and their
[35:02] potentially make these designs and their
[35:02] potentially make these designs and their options more available to users uh way
[35:06] options more available to users uh way
[35:06] options more available to users uh way outside of mechanical engineering or
[35:08] outside of mechanical engineering or
[35:08] outside of mechanical engineering or outside of the expertise with Solid
[35:10] outside of the expertise with Solid
[35:10] outside of the expertise with Solid Works. That's what we want to go for
[35:12] Works. That's what we want to go for
[35:12] Works. That's what we want to go for ultimately. And so um for details on
[35:15] ultimately. And so um for details on
[35:15] ultimately. And so um for details on files I will maybe put this together in
[35:18] files I will maybe put this together in
[35:18] files I will maybe put this together in a different video.
[35:20] a different video.
[35:20] a different video. Hopefully you get a sense from this
[35:22] Hopefully you get a sense from this
[35:22] Hopefully you get a sense from this video al together that we are extremely
[35:25] video al together that we are extremely
[35:25] video al together that we are extremely close to a world where um tons of
[35:28] close to a world where um tons of
[35:28] close to a world where um tons of mechanical things can be simply
[35:30] mechanical things can be simply
[35:30] mechanical things can be simply downloaded for free and printed by
[35:32] downloaded for free and printed by
[35:32] downloaded for free and printed by people that are not engineers but simply
[35:34] people that are not engineers but simply
[35:34] people that are not engineers but simply have some hands-on um interest in
[35:37] have some hands-on um interest in
[35:37] have some hands-on um interest in building things. Um, so for me, this is
[35:41] building things. Um, so for me, this is
[35:41] building things. Um, so for me, this is one part out of a series that will go um
[35:44] one part out of a series that will go um
[35:44] one part out of a series that will go um first of all to my students that are
[35:47] first of all to my students that are
[35:47] first of all to my students that are engineering undergrads and then they
[35:50] engineering undergrads and then they
[35:50] engineering undergrads and then they have access to if they're doing an
[35:52] have access to if they're doing an
[35:52] have access to if they're doing an electronics project, they have some
[35:54] electronics project, they have some
[35:54] electronics project, they have some template parts on mechanical uh projects
[35:58] template parts on mechanical uh projects
[35:58] template parts on mechanical uh projects that they can equip themselves on the
[36:01] that they can equip themselves on the
[36:01] that they can equip themselves on the discipline that they're not experts in.
[36:04] discipline that they're not experts in.
[36:04] discipline that they're not experts in. Um, it's something that we should have
[36:06] Um, it's something that we should have
[36:06] Um, it's something that we should have had from the beginning. Um, if you were
[36:09] had from the beginning. Um, if you were
[36:09] had from the beginning. Um, if you were to open up a mechanical engineering
[36:11] to open up a mechanical engineering
[36:11] to open up a mechanical engineering textbook like this, Shiggley's
[36:13] textbook like this, Shiggley's
[36:13] textbook like this, Shiggley's mechanical engineering design, I've got
[36:16] mechanical engineering design, I've got
[36:16] mechanical engineering design, I've got these uh little bookmark tabs wherever a
[36:19] these uh little bookmark tabs wherever a
[36:19] these uh little bookmark tabs wherever a major section um is listed. And it
[36:24] major section um is listed. And it
[36:24] major section um is listed. And it doesn't actually take all that many
[36:26] doesn't actually take all that many
[36:26] doesn't actually take all that many parametric parts to cover the 90% range
[36:30] parametric parts to cover the 90% range
[36:30] parametric parts to cover the 90% range of mechanical things that we would want.
[36:34] of mechanical things that we would want.
[36:34] of mechanical things that we would want. It can all be really easy if we follow a
[36:38] It can all be really easy if we follow a
[36:38] It can all be really easy if we follow a few rules which is design for 3D
[36:41] few rules which is design for 3D
[36:41] few rules which is design for 3D printing design to integrate the most
[36:46] printing design to integrate the most
[36:46] printing design to integrate the most important off-the-shelf parts
[36:49] important off-the-shelf parts
[36:50] important off-the-shelf parts and design opensource in a way that
[36:53] and design opensource in a way that
[36:53] and design opensource in a way that leaves it accessible. When we get to
[36:55] leaves it accessible. When we get to
[36:55] leaves it accessible. When we get to that stage where online we figure out
[36:59] that stage where online we figure out
[36:59] that stage where online we figure out how to really distribute and make these
[37:03] how to really distribute and make these
[37:03] how to really distribute and make these available um and understandable in the
[37:06] available um and understandable in the
[37:06] available um and understandable in the way that we want to for everybody.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
