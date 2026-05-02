---
title: "How to Design a 3D Print - (with example, funtional Hinge)"
url: "https://www.youtube.com/watch?v=ZOMu9AFOdCk"
video_id: "ZOMu9AFOdCk"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-06-08
duration: "41:00"
duration_sec: 2460
views: 2049
likes: 119
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/ZOMu9AFOdCk/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1712
chapters_count: 10
has_description: true
has_comments: false
---

## Description

This hinge design is one of the most carefully designed parts you will find online.  So, it is a good example to show the standards we use for SCUTTLE Robotics parts designs, and for open-source collaboration.   I'm explaining the details and the thought processes that drive each dimension, how our parameters are named, how the 3D printer's tolerances impact the function of the part.  

You can learn:
► how to plan a design for printability
► how to name your feature tree and organize it
► how to integrate friction & motion in your design
► how to plan one part for hundreds of future parts
► how to use color for designating solid bodies
► how to make your dimensions easy to adjust
► how to use keywords to find your files later
► how to re-use your design for different projects

[Links]
PDF Slides ► https://lobfile.com/file/UqvgQknr.pdf
CAD Model ► https://grabcad.com/library/fan_joint-1
More Lab Info ► https://qr.net/openlabproject
My Discord ► (see bio)

[CHAPTERS]
0:00 why this video?
03:54 naming files & features
06:20 tolerancing gaps
8:00 parametric using constraints
17:12 printing nozzle phenomena
19:50 increase hinge friction
23:00 evenness in strength
24:45 function of chamfers
25:50 debossing of version
28:40 file properties - more professional

## Chapters

- 0:00 why this video?
- 3:54 naming files & features
- 6:20 tolerancing gaps
- 8:00 parametric using constraints
- 17:12 printing nozzle phenomena
- 19:50 increase hinge friction
- 23:00 evenness in strength
- 24:45 function of chamfers
- 25:50 debossing of version
- 28:40 file properties - more professional

## Transcript

[0:02] Hi everybody. This is David Malloway.
[0:02] Hi everybody. This is David Malloway. I'm a mechanical engineer and a robotics
[0:05] I'm a mechanical engineer and a robotics
[0:05] I'm a mechanical engineer and a robotics engineer and an educator. And um today
[0:08] engineer and an educator. And um today
[0:08] engineer and an educator. And um today I'm looking at um strategies for
[0:12] I'm looking at um strategies for
[0:12] I'm looking at um strategies for designing. And I have a particular part.
[0:15] designing. And I have a particular part.
[0:15] designing. And I have a particular part. It's a 3D printable hinge that is also
[0:18] It's a 3D printable hinge that is also
[0:18] It's a 3D printable hinge that is also parametric that is also designed for 3D
[0:21] parametric that is also designed for 3D
[0:21] parametric that is also designed for 3D printing specifically. So we have design
[0:23] printing specifically. So we have design
[0:23] printing specifically. So we have design for manufacturing. We have design intent
[0:26] for manufacturing. We have design intent
[0:26] for manufacturing. We have design intent that I think is fairly well overlooked
[0:28] that I think is fairly well overlooked
[0:28] that I think is fairly well overlooked on average. Um and we have uh all of the
[0:32] on average. Um and we have uh all of the
[0:32] on average. Um and we have uh all of the strategies for well for instance
[0:35] strategies for well for instance
[0:35] strategies for well for instance combining a feature tree into something
[0:37] combining a feature tree into something
[0:37] combining a feature tree into something sensible. Um I think there are 100
[0:41] sensible. Um I think there are 100
[0:41] sensible. Um I think there are 100 individual decisions inside of this
[0:42] individual decisions inside of this
[0:42] individual decisions inside of this design that that are not usually talked
[0:45] design that that are not usually talked
[0:45] design that that are not usually talked about. And so by that I mean this is
[0:48] about. And so by that I mean this is
[0:48] about. And so by that I mean this is what I mean when I say I've never ever
[0:50] what I mean when I say I've never ever
[0:50] what I mean when I say I've never ever seen a YouTube video that that shows um
[0:54] seen a YouTube video that that shows um
[0:54] seen a YouTube video that that shows um how to design a part. And of course one
[0:57] how to design a part. And of course one
[0:57] how to design a part. And of course one of the reasons is there are many kinds
[0:59] of the reasons is there are many kinds
[0:59] of the reasons is there are many kinds of parts but uh but all right so I'll
[1:03] of parts but uh but all right so I'll
[1:03] of parts but uh but all right so I'll give an example
[1:05] give an example
[1:05] give an example um of what we are we are and are not
[1:08] um of what we are we are and are not
[1:08] um of what we are we are and are not talking about. So for instance how to
[1:10] talking about. So for instance how to
[1:10] talking about. So for instance how to use solid works. I'm going to go through
[1:13] use solid works. I'm going to go through
[1:13] use solid works. I'm going to go through uh several Solid Works um steps in this
[1:17] uh several Solid Works um steps in this
[1:17] uh several Solid Works um steps in this video, but it is not about using Solid
[1:20] video, but it is not about using Solid
[1:20] video, but it is not about using Solid Works. It's kind of like if I I showed
[1:22] Works. It's kind of like if I I showed
[1:22] Works. It's kind of like if I I showed you how to paint a picture of a a turtle
[1:25] you how to paint a picture of a a turtle
[1:25] you how to paint a picture of a a turtle using Microsoft Paint, but it's not a
[1:27] using Microsoft Paint, but it's not a
[1:27] using Microsoft Paint, but it's not a video about using Microsoft Paint. That
[1:29] video about using Microsoft Paint. That
[1:29] video about using Microsoft Paint. That is assumed that you can discover that
[1:31] is assumed that you can discover that
[1:31] is assumed that you can discover that information elsewhere. um we are talking
[1:35] information elsewhere. um we are talking
[1:35] information elsewhere. um we are talking about uh decisions that are a in the
[1:38] about uh decisions that are a in the
[1:38] about uh decisions that are a in the design for a hinge that is part of the
[1:41] design for a hinge that is part of the
[1:41] design for a hinge that is part of the design intent. So you could generalize
[1:43] design intent. So you could generalize
[1:44] design intent. So you could generalize it and say okay if we wanted this fixed
[1:46] it and say okay if we wanted this fixed
[1:46] it and say okay if we wanted this fixed we would do the opposite of what we want
[1:48] we would do the opposite of what we want
[1:48] we would do the opposite of what we want if we're going to have a part that's
[1:50] if we're going to have a part that's
[1:50] if we're going to have a part that's moving. Um, well, maybe uh since I don't
[1:53] moving. Um, well, maybe uh since I don't
[1:53] moving. Um, well, maybe uh since I don't know how to structure the video
[1:55] know how to structure the video
[1:55] know how to structure the video specifically, I will just jump in and I
[1:58] specifically, I will just jump in and I
[1:58] specifically, I will just jump in and I think the the audience will get some
[2:00] think the the audience will get some
[2:00] think the the audience will get some things out of it and I'm not sure
[2:03] things out of it and I'm not sure
[2:03] things out of it and I'm not sure depending on where you're coming from
[2:04] depending on where you're coming from
[2:04] depending on where you're coming from which things you'll get out of it. So,
[2:06] which things you'll get out of it. So,
[2:06] which things you'll get out of it. So, I'll just go through it. This is like a
[2:07] I'll just go through it. This is like a
[2:08] I'll just go through it. This is like a first try and then uh and then we're
[2:09] first try and then uh and then we're
[2:09] first try and then uh and then we're going to discover a little better what
[2:11] going to discover a little better what
[2:11] going to discover a little better what part is is missing information for the
[2:14] part is is missing information for the
[2:14] part is is missing information for the audience. What do they need to
[2:15] audience. What do they need to
[2:15] audience. What do they need to understand better? And um maybe the next
[2:18] understand better? And um maybe the next
[2:18] understand better? And um maybe the next most related video to this one would be
[2:22] most related video to this one would be
[2:22] most related video to this one would be um a video where I talked about uh it
[2:25] um a video where I talked about uh it
[2:26] um a video where I talked about uh it was designed for 3D printing with
[2:27] was designed for 3D printing with
[2:27] was designed for 3D printing with tolerances borrow a tolerance. So it was
[2:30] tolerances borrow a tolerance. So it was
[2:30] tolerances borrow a tolerance. So it was a set of strategies relating to how do
[2:33] a set of strategies relating to how do
[2:33] a set of strategies relating to how do we design a mechanism not just a part so
[2:36] we design a mechanism not just a part so
[2:36] we design a mechanism not just a part so that mechanism can borrow hardness or
[2:39] that mechanism can borrow hardness or
[2:39] that mechanism can borrow hardness or strength etc. I'll I'll link the video
[2:41] strength etc. I'll I'll link the video
[2:41] strength etc. I'll I'll link the video um in this one. So let's dive in. um
[2:45] um in this one. So let's dive in. um
[2:45] um in this one. So let's dive in. um contents. I just figured out you can
[2:47] contents. I just figured out you can
[2:47] contents. I just figured out you can copy and paste from the from the
[2:49] copy and paste from the from the
[2:49] copy and paste from the from the Microsoft uh the left
[2:57] hand whatever talk about that later. Uh
[2:57] hand whatever talk about that later. Uh I'm going to just pop into these slides
[2:59] I'm going to just pop into these slides
[2:59] I'm going to just pop into these slides because I made them two days ago.
[3:02] because I made them two days ago.
[3:02] because I made them two days ago. Um so this is a twobody component a two
[3:07] Um so this is a twobody component a two
[3:07] Um so this is a twobody component a two body mechanism that is two separate
[3:11] body mechanism that is two separate
[3:11] body mechanism that is two separate parts at the end but in the beginning it
[3:14] parts at the end but in the beginning it
[3:14] parts at the end but in the beginning it is one solid body that has been sliced
[3:18] is one solid body that has been sliced
[3:18] is one solid body that has been sliced with a gap so that in any solid in uh
[3:22] with a gap so that in any solid in uh
[3:22] with a gap so that in any solid in uh modeling software it will will
[3:24] modeling software it will will
[3:24] modeling software it will will understand there to be two bodies. Um
[3:28] understand there to be two bodies. Um
[3:28] understand there to be two bodies. Um okay the first decisions are like
[3:31] okay the first decisions are like
[3:31] okay the first decisions are like standardizing because now there are
[3:32] standardizing because now there are
[3:32] standardizing because now there are several variants of this hinge. We say
[3:35] several variants of this hinge. We say
[3:35] several variants of this hinge. We say we're going to make the fixed side the
[3:37] we're going to make the fixed side the
[3:37] we're going to make the fixed side the side which has two arms around the hinge
[3:40] side which has two arms around the hinge
[3:40] side which has two arms around the hinge pin and the the um moving side or the
[3:44] pin and the the um moving side or the
[3:44] pin and the the um moving side or the pivot body will be the one that has one
[3:46] pivot body will be the one that has one
[3:46] pivot body will be the one that has one arm. And you can make any decision that
[3:49] arm. And you can make any decision that
[3:49] arm. And you can make any decision that you want. There's no there's no industry
[3:52] you want. There's no there's no industry
[3:52] you want. There's no there's no industry requirement. But deciding that instead
[3:55] requirement. But deciding that instead
[3:55] requirement. But deciding that instead of not deciding that is uh well that
[3:59] of not deciding that is uh well that
[3:59] of not deciding that is uh well that cascades into the naming of your
[4:01] cascades into the naming of your
[4:02] cascades into the naming of your features and that cascades into the the
[4:05] features and that cascades into the the
[4:05] features and that cascades into the the lack of ambiguity later on when you're
[4:07] lack of ambiguity later on when you're
[4:07] lack of ambiguity later on when you're sharing or collaborating or you go back
[4:09] sharing or collaborating or you go back
[4:09] sharing or collaborating or you go back two years and make an update. Things are
[4:11] two years and make an update. Things are
[4:11] two years and make an update. Things are named with respect to the a decision
[4:14] named with respect to the a decision
[4:14] named with respect to the a decision that you made instead of a decision you
[4:16] that you made instead of a decision you
[4:16] that you made instead of a decision you avoided. um for two degree of freedom
[4:19] avoided. um for two degree of freedom
[4:19] avoided. um for two degree of freedom hinges since you'll see later there's a
[4:21] hinges since you'll see later there's a
[4:21] hinges since you'll see later there's a there's like this one that has three
[4:23] there's like this one that has three
[4:23] there's like this one that has three components now then we decided this rule
[4:27] components now then we decided this rule
[4:28] components now then we decided this rule um I decided that uh the purple is fixed
[4:31] um I decided that uh the purple is fixed
[4:31] um I decided that uh the purple is fixed to the main assembly where um like let's
[4:34] to the main assembly where um like let's
[4:34] to the main assembly where um like let's say this is a large uh standing toolbox
[4:37] say this is a large uh standing toolbox
[4:37] say this is a large uh standing toolbox and this is a a shelf that's going to
[4:40] and this is a a shelf that's going to
[4:40] and this is a a shelf that's going to pivot well then the purple one will be
[4:42] pivot well then the purple one will be
[4:42] pivot well then the purple one will be the fixed one and that is the one that
[4:44] the fixed one and that is the one that
[4:44] the fixed one and that is the one that is fixed to the larger heavier Um main
[4:48] is fixed to the larger heavier Um main
[4:48] is fixed to the larger heavier Um main assembly in a in the final
[4:51] assembly in a in the final
[4:51] assembly in a in the final application two degrees of freedom
[4:54] application two degrees of freedom
[4:54] application two degrees of freedom uh opposing purple is fixed to a module
[4:58] uh opposing purple is fixed to a module
[4:58] uh opposing purple is fixed to a module the green part is not fixed to any
[5:00] the green part is not fixed to any
[5:00] the green part is not fixed to any module. Oh yeah. So in this case it's
[5:03] module. Oh yeah. So in this case it's
[5:03] module. Oh yeah. So in this case it's fixed to the smaller assembly and in
[5:07] fixed to the smaller assembly and in
[5:07] fixed to the smaller assembly and in this case green will be fixed to
[5:09] this case green will be fixed to
[5:09] this case green will be fixed to nothing. Um okay body's identification.
[5:14] nothing. Um okay body's identification.
[5:14] nothing. Um okay body's identification. Uh this drove me towards solving a long
[5:17] Uh this drove me towards solving a long
[5:17] Uh this drove me towards solving a long long long problem about how the
[5:19] long long problem about how the
[5:19] long long problem about how the appearances seem to all get messed up in
[5:21] appearances seem to all get messed up in
[5:21] appearances seem to all get messed up in Solid Works if they're not uh applied
[5:24] Solid Works if they're not uh applied
[5:24] Solid Works if they're not uh applied carefully and uh recovering a material
[5:27] carefully and uh recovering a material
[5:27] carefully and uh recovering a material that I once saved sometimes it gets lost
[5:30] that I once saved sometimes it gets lost
[5:30] that I once saved sometimes it gets lost so that if I open Solid Works later um
[5:33] so that if I open Solid Works later um
[5:33] so that if I open Solid Works later um where is the so you have to understand
[5:37] where is the so you have to understand
[5:37] where is the so you have to understand the material is one type of file that
[5:39] the material is one type of file that
[5:39] the material is one type of file that saves information about the material and
[5:41] saves information about the material and
[5:41] saves information about the material and its appearance. the appearance is
[5:43] its appearance. the appearance is
[5:43] its appearance. the appearance is another kind of file and for your given
[5:46] another kind of file and for your given
[5:46] another kind of file and for your given CAD software you should really
[5:47] CAD software you should really
[5:47] CAD software you should really understand that because we're making
[5:49] understand that because we're making
[5:49] understand that because we're making assemblies more often than single parts
[5:51] assemblies more often than single parts
[5:52] assemblies more often than single parts and then coloring is a a crucial
[5:55] and then coloring is a a crucial
[5:55] and then coloring is a a crucial indicator for what's happening in your
[5:57] indicator for what's happening in your
[5:57] indicator for what's happening in your assembly. Um so I'll just save the all
[6:00] assembly. Um so I'll just save the all
[6:00] assembly. Um so I'll just save the all these slides you'll have access to in
[6:02] these slides you'll have access to in
[6:02] these slides you'll have access to in openlab uh
[6:04] openlab uh
[6:04] openlab uh qr.net/openlab project. Um so if you're
[6:07] qr.net/openlab project. Um so if you're
[6:07] qr.net/openlab project. Um so if you're a solid works user you can see that more
[6:09] a solid works user you can see that more
[6:09] a solid works user you can see that more closely. solid bodies. It features two
[6:13] closely. solid bodies. It features two
[6:13] closely. solid bodies. It features two bodies. In this case, an air gap exists
[6:15] bodies. In this case, an air gap exists
[6:15] bodies. In this case, an air gap exists in between and the selection of that air
[6:17] in between and the selection of that air
[6:17] in between and the selection of that air gap in our case is 0.3 millime. So,
[6:20] gap in our case is 0.3 millime. So,
[6:20] gap in our case is 0.3 millime. So, ordinarily 0.3 mm is my standard
[6:24] ordinarily 0.3 mm is my standard
[6:24] ordinarily 0.3 mm is my standard tolerance to give a clearance between
[6:26] tolerance to give a clearance between
[6:26] tolerance to give a clearance between two parts.
[6:27] two parts.
[6:27] two parts. Um so that if we have to have clearance
[6:30] Um so that if we have to have clearance
[6:30] Um so that if we have to have clearance and then we also have to be certain that
[6:33] and then we also have to be certain that
[6:33] and then we also have to be certain that the parts can move we would usually I
[6:35] the parts can move we would usually I
[6:35] the parts can move we would usually I would usually uh increase from 0.3 to a
[6:39] would usually uh increase from 0.3 to a
[6:39] would usually uh increase from 0.3 to a larger uh gap because then if your
[6:42] larger uh gap because then if your
[6:42] larger uh gap because then if your printer has one small defect we still
[6:44] printer has one small defect we still
[6:44] printer has one small defect we still want our part robust enough that it
[6:46] want our part robust enough that it
[6:46] want our part robust enough that it spins freely. But in our case the way
[6:49] spins freely. But in our case the way
[6:49] spins freely. But in our case the way this is printed and produced is that uh
[6:51] this is printed and produced is that uh
[6:51] this is printed and produced is that uh there are very minor regions that may
[6:53] there are very minor regions that may
[6:53] there are very minor regions that may might make contact. We actually want the
[6:55] might make contact. We actually want the
[6:55] might make contact. We actually want the minimal clearances and we want friction.
[6:58] minimal clearances and we want friction.
[6:58] minimal clearances and we want friction. So then we crack the part with an impact
[7:00] So then we crack the part with an impact
[7:00] So then we crack the part with an impact to to separate it later. Um, okay. So
[7:05] to to separate it later. Um, okay. So
[7:05] to to separate it later. Um, okay. So naming these bodies once the bodies
[7:08] naming these bodies once the bodies
[7:08] naming these bodies once the bodies exist in your feature tree is one point
[7:12] exist in your feature tree is one point
[7:12] exist in your feature tree is one point of uh attention. So do that. Um, it's
[7:15] of uh attention. So do that. Um, it's
[7:15] of uh attention. So do that. Um, it's simply F2. Just like you rename a file,
[7:17] simply F2. Just like you rename a file,
[7:17] simply F2. Just like you rename a file, you can rename uh bodies and then there
[7:20] you can rename uh bodies and then there
[7:20] you can rename uh bodies and then there will appear to be three bodies
[7:22] will appear to be three bodies
[7:22] will appear to be three bodies afterwards. If you named the body before
[7:24] afterwards. If you named the body before
[7:24] afterwards. If you named the body before you have split it in any given feature
[7:26] you have split it in any given feature
[7:26] you have split it in any given feature tree, then once it splits, the the
[7:30] tree, then once it splits, the the
[7:30] tree, then once it splits, the the software doesn't know which part is your
[7:33] software doesn't know which part is your
[7:33] software doesn't know which part is your your main part. So you have to name them
[7:37] your main part. So you have to name them
[7:37] your main part. So you have to name them uh as you
[7:39] uh as you
[7:39] uh as you go. Um
[7:42] go. Um
[7:42] go. Um okay, for bodies matching to hinge
[7:45] okay, for bodies matching to hinge
[7:45] okay, for bodies matching to hinge thickness. So we're beginning to make um
[7:48] thickness. So we're beginning to make um
[7:48] thickness. So we're beginning to make um I'm just speaking from the picture.
[7:50] I'm just speaking from the picture.
[7:50] I'm just speaking from the picture. We're making a choice of our key
[7:53] We're making a choice of our key
[7:53] We're making a choice of our key dimensions that will later become
[7:55] dimensions that will later become
[7:55] dimensions that will later become parameters. So this um this 40 mm that's
[8:00] parameters. So this um this 40 mm that's
[8:00] parameters. So this um this 40 mm that's hard to see is the height of the hinge.
[8:03] hard to see is the height of the hinge.
[8:03] hard to see is the height of the hinge. Um and we want to be able to adjust this
[8:07] Um and we want to be able to adjust this
[8:07] Um and we want to be able to adjust this design later so that let's say we make
[8:09] design later so that let's say we make
[8:09] design later so that let's say we make the height double then we also want the
[8:11] the height double then we also want the
[8:11] the height double then we also want the features to follow along with it without
[8:14] features to follow along with it without
[8:14] features to follow along with it without having to put to rework the CAD. That's
[8:16] having to put to rework the CAD. That's
[8:16] having to put to rework the CAD. That's the essence of parametric modeling. So
[8:19] the essence of parametric modeling. So
[8:19] the essence of parametric modeling. So we start with naming these variables
[8:22] we start with naming these variables
[8:22] we start with naming these variables very
[8:23] very
[8:23] very early. Um this slide was simply
[8:28] early. Um this slide was simply
[8:28] early. Um this slide was simply uh describing what the version 3 model
[8:32] uh describing what the version 3 model
[8:32] uh describing what the version 3 model is for. Since I am saving these I'm not
[8:34] is for. Since I am saving these I'm not
[8:34] is for. Since I am saving these I'm not I'm not just making one model. I'm
[8:37] I'm not just making one model. I'm
[8:37] I'm not just making one model. I'm making a uh there are now three or four
[8:40] making a uh there are now three or four
[8:40] making a uh there are now three or four models that each of them is a template
[8:42] models that each of them is a template
[8:42] models that each of them is a template for expanding and changing with minimal
[8:45] for expanding and changing with minimal
[8:45] for expanding and changing with minimal effort. Uh this is the one where we want
[8:48] effort. Uh this is the one where we want
[8:48] effort. Uh this is the one where we want the the beefiest
[8:50] the the beefiest
[8:50] the the beefiest um assembly with respect to that single
[8:53] um assembly with respect to that single
[8:53] um assembly with respect to that single hinge pin. So everything has each body.
[8:56] hinge pin. So everything has each body.
[8:56] hinge pin. So everything has each body. The diameter zone has a particular
[8:59] The diameter zone has a particular
[8:59] The diameter zone has a particular thickness that matches the purple parts
[9:02] thickness that matches the purple parts
[9:02] thickness that matches the purple parts panels thickness and the green panels
[9:05] panels thickness and the green panels
[9:05] panels thickness and the green panels thickness. Then we have hinge version
[9:09] thickness. Then we have hinge version
[9:09] thickness. Then we have hinge version two. Uh need to update the slide but
[9:12] two. Uh need to update the slide but
[9:12] two. Uh need to update the slide but it's for mounting a panel flush to one
[9:14] it's for mounting a panel flush to one
[9:14] it's for mounting a panel flush to one another. carry 10 kg using one pair of
[9:18] another. carry 10 kg using one pair of
[9:18] another. carry 10 kg using one pair of hinges and okay so a pair of hinges this
[9:21] hinges and okay so a pair of hinges this
[9:21] hinges and okay so a pair of hinges this does not provide a strong alignment if
[9:24] does not provide a strong alignment if
[9:24] does not provide a strong alignment if you bracket a large item that is
[9:26] you bracket a large item that is
[9:26] you bracket a large item that is swinging it takes a pair of these hinges
[9:29] swinging it takes a pair of these hinges
[9:29] swinging it takes a pair of these hinges and that that's part of the design
[9:31] and that that's part of the design
[9:31] and that that's part of the design intent. So we can minimize this part its
[9:34] intent. So we can minimize this part its
[9:34] intent. So we can minimize this part its height and the the span of its hinge pin
[9:38] height and the the span of its hinge pin
[9:38] height and the the span of its hinge pin can be reduced if we know we are going
[9:40] can be reduced if we know we are going
[9:40] can be reduced if we know we are going to use two of them and that's all part
[9:43] to use two of them and that's all part
[9:43] to use two of them and that's all part of uh how you choose your your sizes. So
[9:46] of uh how you choose your your sizes. So
[9:46] of uh how you choose your your sizes. So this one was able to be made more
[9:48] this one was able to be made more
[9:48] this one was able to be made more compact. Um hinge double this part is
[9:53] compact. Um hinge double this part is
[9:53] compact. Um hinge double this part is going to be for adding articulation to a
[9:55] going to be for adding articulation to a
[9:55] going to be for adding articulation to a light load. Uh only using one set of
[9:58] light load. Uh only using one set of
[9:58] light load. Uh only using one set of this printed part. um about 1 kilogram
[10:02] this printed part. um about 1 kilogram
[10:02] this printed part. um about 1 kilogram will swing and it will hold itself
[10:04] will swing and it will hold itself
[10:04] will swing and it will hold itself steady if you it's oriented vertically
[10:07] steady if you it's oriented vertically
[10:07] steady if you it's oriented vertically as as shown. Then if you hang 1 kilogram
[10:10] as as shown. Then if you hang 1 kilogram
[10:10] as as shown. Then if you hang 1 kilogram on the extremity then it and then you
[10:13] on the extremity then it and then you
[10:13] on the extremity then it and then you push it to turn a little bit it will
[10:15] push it to turn a little bit it will
[10:15] push it to turn a little bit it will hold that position. If you if you take
[10:18] hold that position. If you if you take
[10:18] hold that position. If you if you take this assembly as you see it and turn it
[10:20] this assembly as you see it and turn it
[10:20] this assembly as you see it and turn it 90° then it's going to swing down just
[10:22] 90° then it's going to swing down just
[10:22] 90° then it's going to swing down just due to the weight. It will not have that
[10:25] due to the weight. It will not have that
[10:25] due to the weight. It will not have that much friction but I have a note about um
[10:28] much friction but I have a note about um
[10:28] much friction but I have a note about um how you can control the friction later.
[10:31] how you can control the friction later.
[10:31] how you can control the friction later. Okay, the first use case for this double
[10:34] Okay, the first use case for this double
[10:34] Okay, the first use case for this double hinge is as shown here. Um, we have a
[10:39] hinge is as shown here. Um, we have a
[10:39] hinge is as shown here. Um, we have a small fan that's mounted on the double
[10:42] small fan that's mounted on the double
[10:42] small fan that's mounted on the double hinge and it has uh you can orient it
[10:47] hinge and it has uh you can orient it
[10:47] hinge and it has uh you can orient it however you need. And this whole thing
[10:49] however you need. And this whole thing
[10:49] however you need. And this whole thing could be reversed to reverse the
[10:51] could be reversed to reverse the
[10:51] could be reversed to reverse the direction of the fan. It mounts onto
[10:54] direction of the fan. It mounts onto
[10:54] direction of the fan. It mounts onto 3030 drail
[10:56] 3030 drail
[10:56] 3030 drail uh sorry 35 millimeter drail and then we
[10:59] uh sorry 35 millimeter drail and then we
[11:00] uh sorry 35 millimeter drail and then we are able to position a small fan at uh
[11:03] are able to position a small fan at uh
[11:03] are able to position a small fan at uh at a heat source such as the
[11:05] at a heat source such as the
[11:05] at a heat source such as the microprocessor your Raspberry Pi or in
[11:07] microprocessor your Raspberry Pi or in
[11:07] microprocessor your Raspberry Pi or in our case the Beagle Bone AI. Uh Beagle
[11:10] our case the Beagle Bone AI. Uh Beagle
[11:10] our case the Beagle Bone AI. Uh Beagle Bone Y AI is the one we're working with
[11:13] Bone Y AI is the one we're working with
[11:13] Bone Y AI is the one we're working with this month. Um and we don't know yet.
[11:18] this month. Um and we don't know yet.
[11:18] this month. Um and we don't know yet. This is like relating to the design of
[11:20] This is like relating to the design of
[11:20] This is like relating to the design of the robot. We don't know how much uh
[11:22] the robot. We don't know how much uh
[11:22] the robot. We don't know how much uh which software will ultimately be run.
[11:24] which software will ultimately be run.
[11:24] which software will ultimately be run. How much load does that place on the
[11:26] How much load does that place on the
[11:26] How much load does that place on the CPU? And then how much cooling finally
[11:28] CPU? And then how much cooling finally
[11:28] CPU? And then how much cooling finally do we need on that system? And since
[11:31] do we need on that system? And since
[11:31] do we need on that system? And since we've only been working with this for a
[11:33] we've only been working with this for a
[11:33] we've only been working with this for a short time, we don't know all the the
[11:35] short time, we don't know all the the
[11:35] short time, we don't know all the the heat characteristics of that system.
[11:37] heat characteristics of that system.
[11:37] heat characteristics of that system. Will we need to design our own um uh
[11:41] Will we need to design our own um uh
[11:42] Will we need to design our own um uh custom cooling uh cowling and solution
[11:45] custom cooling uh cowling and solution
[11:45] custom cooling uh cowling and solution for the Beagle? Then this is our uh this
[11:49] for the Beagle? Then this is our uh this
[11:49] for the Beagle? Then this is our uh this supports a set of trials so that we have
[11:52] supports a set of trials so that we have
[11:52] supports a set of trials so that we have the adjustability in the short term to
[11:54] the adjustability in the short term to
[11:54] the adjustability in the short term to gain better information and then design
[11:57] gain better information and then design
[11:57] gain better information and then design the best solution for the long term. Um
[12:01] the best solution for the long term. Um
[12:01] the best solution for the long term. Um one of the the precursors to the the
[12:04] one of the the precursors to the the
[12:04] one of the the precursors to the the single hinge was like this. And so um we
[12:08] single hinge was like this. And so um we
[12:08] single hinge was like this. And so um we have a tool rack with many different hex
[12:10] have a tool rack with many different hex
[12:10] have a tool rack with many different hex bits that are being held. And we can lay
[12:14] bits that are being held. And we can lay
[12:14] bits that are being held. And we can lay it all flat and turn them to the side so
[12:17] it all flat and turn them to the side so
[12:17] it all flat and turn them to the side so that we can shut the toolbox lid or you
[12:20] that we can shut the toolbox lid or you
[12:20] that we can shut the toolbox lid or you know just gain space or you can pull it
[12:22] know just gain space or you can pull it
[12:22] know just gain space or you can pull it out so you can more easily select and
[12:24] out so you can more easily select and
[12:24] out so you can more easily select and grab your parts. Uh but this this
[12:28] grab your parts. Uh but this this
[12:28] grab your parts. Uh but this this central geometry is the same for many
[12:31] central geometry is the same for many
[12:31] central geometry is the same for many many hinges in the lab. And so this uh
[12:34] many hinges in the lab. And so this uh
[12:34] many hinges in the lab. And so this uh the reason I brought this one out is to
[12:36] the reason I brought this one out is to
[12:36] the reason I brought this one out is to show you the screws. So, we'll have a
[12:38] show you the screws. So, we'll have a
[12:38] show you the screws. So, we'll have a some nominal amount of friction on this
[12:41] some nominal amount of friction on this
[12:41] some nominal amount of friction on this hinge coming from the uh the pink and
[12:45] hinge coming from the uh the pink and
[12:46] hinge coming from the uh the pink and purple and
[12:47] purple and
[12:47] purple and blue, purple and green. My brain is in
[12:50] blue, purple and green. My brain is in
[12:50] blue, purple and green. My brain is in too many places at once. um some nominal
[12:54] too many places at once. um some nominal
[12:54] too many places at once. um some nominal nominal amount of friction once it's all
[12:55] nominal amount of friction once it's all
[12:55] nominal amount of friction once it's all gets fit together and depending on the
[12:57] gets fit together and depending on the
[12:58] gets fit together and depending on the the grip the grip zone, the diameters of
[13:01] the grip the grip zone, the diameters of
[13:01] the grip the grip zone, the diameters of those holes, how they come out when
[13:03] those holes, how they come out when
[13:03] those holes, how they come out when they're printed, uh fit fitting onto
[13:05] they're printed, uh fit fitting onto
[13:05] they're printed, uh fit fitting onto this tube. And so we have a a quarter
[13:09] this tube. And so we have a a quarter
[13:09] this tube. And so we have a a quarter inch tube and we have a 10 mm tube about
[13:13] inch tube and we have a 10 mm tube about
[13:13] inch tube and we have a 10 mm tube about double this one. And so those two uh
[13:17] double this one. And so those two uh
[13:17] double this one. And so those two uh different plastic parts are very very
[13:20] different plastic parts are very very
[13:20] different plastic parts are very very tough and those are the core of many
[13:22] tough and those are the core of many
[13:22] tough and those are the core of many hinge designs because these tubes you
[13:25] hinge designs because these tubes you
[13:25] hinge designs because these tubes you can purchase in lengths of 10 m or 35 ft
[13:29] can purchase in lengths of 10 m or 35 ft
[13:30] can purchase in lengths of 10 m or 35 ft and then uh and so it's it's affordable
[13:33] and then uh and so it's it's affordable
[13:33] and then uh and so it's it's affordable and nearly free to make adjustments.
[13:36] and nearly free to make adjustments.
[13:36] and nearly free to make adjustments. Slice the tube and and stick it into the
[13:39] Slice the tube and and stick it into the
[13:39] Slice the tube and and stick it into the the assembly and then make adjustments
[13:41] the assembly and then make adjustments
[13:41] the assembly and then make adjustments later. It gives us that flexibility to
[13:44] later. It gives us that flexibility to
[13:44] later. It gives us that flexibility to continue enhancing
[13:46] continue enhancing
[13:46] continue enhancing designs. Okay. Parameter summary. Um so
[13:50] designs. Okay. Parameter summary. Um so
[13:50] designs. Okay. Parameter summary. Um so this is how I approach pretty much all
[13:54] this is how I approach pretty much all
[13:54] this is how I approach pretty much all uh parametric designs. Um it is naming.
[13:59] uh parametric designs. Um it is naming.
[13:59] uh parametric designs. Um it is naming. As soon as you get into the sketches
[14:00] As soon as you get into the sketches
[14:00] As soon as you get into the sketches that you know are defining the main
[14:02] that you know are defining the main
[14:02] that you know are defining the main features of the the design, we start to
[14:06] features of the the design, we start to
[14:06] features of the the design, we start to name them and we try to name them
[14:08] name them and we try to name them
[14:08] name them and we try to name them uniquely. Uh but sometimes they'll
[14:10] uniquely. Uh but sometimes they'll
[14:10] uniquely. Uh but sometimes they'll they'll
[14:11] they'll
[14:12] they'll a change. So like width may actually be
[14:15] a change. So like width may actually be
[14:15] a change. So like width may actually be describing more of a height once we're
[14:18] describing more of a height once we're
[14:18] describing more of a height once we're finalized uh in that design. And then
[14:21] finalized uh in that design. And then
[14:22] finalized uh in that design. And then you may need to just go ahead and um
[14:25] you may need to just go ahead and um
[14:25] you may need to just go ahead and um adjust the name. So they're desri disc
[14:28] adjust the name. So they're desri disc
[14:28] adjust the name. So they're desri disc when we release these open- source
[14:31] when we release these open- source
[14:31] when we release these open- source designs. When I publish mine, it's uh
[14:34] designs. When I publish mine, it's uh
[14:34] designs. When I publish mine, it's uh it's as good as the latest u parametric
[14:38] it's as good as the latest u parametric
[14:38] it's as good as the latest u parametric designs that you can find out there. And
[14:40] designs that you can find out there. And
[14:40] designs that you can find out there. And we are trying to describe these most
[14:44] we are trying to describe these most
[14:44] we are trying to describe these most specifically and accurately for another
[14:46] specifically and accurately for another
[14:46] specifically and accurately for another user to download those and understand
[14:48] user to download those and understand
[14:48] user to download those and understand the design quickly. So even if you're
[14:51] the design quickly. So even if you're
[14:51] the design quickly. So even if you're going to design this in another
[14:53] going to design this in another
[14:53] going to design this in another software, being able to see these names
[14:57] software, being able to see these names
[14:57] software, being able to see these names and their comments and then uh going
[15:00] and their comments and then uh going
[15:00] and their comments and then uh going back to the model to see where they're
[15:03] back to the model to see where they're
[15:03] back to the model to see where they're applied is essential for someone else to
[15:06] applied is essential for someone else to
[15:06] applied is essential for someone else to understand the parametric design. If
[15:08] understand the parametric design. If
[15:08] understand the parametric design. If they're going to change one feature,
[15:10] they're going to change one feature,
[15:10] they're going to change one feature, they do not need to break the whole
[15:12] they do not need to break the whole
[15:12] they do not need to break the whole model. They can see which features are
[15:15] model. They can see which features are
[15:15] model. They can see which features are actually parametric and can be adjusted
[15:17] actually parametric and can be adjusted
[15:18] actually parametric and can be adjusted in what range without breaking the
[15:20] in what range without breaking the
[15:20] in what range without breaking the model. And so we just start naming
[15:23] model. And so we just start naming
[15:23] model. And so we just start naming global
[15:24] global
[15:24] global variables and those ones will appear
[15:27] variables and those ones will appear
[15:27] variables and those ones will appear again in another variant of the design
[15:30] again in another variant of the design
[15:30] again in another variant of the design and they will appear in other
[15:33] and they will appear in other
[15:33] and they will appear in other configurations of the design. So
[15:36] configurations of the design. So
[15:36] configurations of the design. So depending on how much stuff you want to
[15:37] depending on how much stuff you want to
[15:37] depending on how much stuff you want to do with your design, the more carefully
[15:40] do with your design, the more carefully
[15:40] do with your design, the more carefully you want to do this stuff. Um, so in our
[15:43] you want to do this stuff. Um, so in our
[15:44] you want to do this stuff. Um, so in our case, pin diameter is describing a part
[15:46] case, pin diameter is describing a part
[15:46] case, pin diameter is describing a part that doesn't exist in our model. It is
[15:48] that doesn't exist in our model. It is
[15:48] that doesn't exist in our model. It is the the tube itself. And so we may put
[15:52] the the tube itself. And so we may put
[15:52] the the tube itself. And so we may put 6.35. You know, 6.6 millimeters was the
[15:55] 6.35. You know, 6.6 millimeters was the
[15:55] 6.35. You know, 6.6 millimeters was the decided standard for once this is
[15:59] decided standard for once this is
[15:59] decided standard for once this is printed with all of its minor defects
[16:01] printed with all of its minor defects
[16:02] printed with all of its minor defects and then we want to assemble it. um with
[16:05] and then we want to assemble it. um with
[16:05] and then we want to assemble it. um with a with
[16:07] a with
[16:07] a with a proper friction and this is the 6.6
[16:12] a proper friction and this is the 6.6
[16:12] a proper friction and this is the 6.6 was a good value for us and then it
[16:14] was a good value for us and then it
[16:14] was a good value for us and then it would be adjusted if someone wants to
[16:17] would be adjusted if someone wants to
[16:17] would be adjusted if someone wants to print an exact copy and then they find
[16:19] print an exact copy and then they find
[16:19] print an exact copy and then they find that they're they're using a different
[16:21] that they're they're using a different
[16:21] that they're they're using a different hinge pin. Uh pin diameter is the yellow
[16:25] hinge pin. Uh pin diameter is the yellow
[16:25] hinge pin. Uh pin diameter is the yellow one. Width of the hinge is the green
[16:27] one. Width of the hinge is the green
[16:27] one. Width of the hinge is the green one.
[16:28] one.
[16:28] one. Um, so that's just information for
[16:31] Um, so that's just information for
[16:31] Um, so that's just information for people that are specifically going to
[16:33] people that are specifically going to
[16:33] people that are specifically going to download and use these parts. Um, the
[16:35] download and use these parts. Um, the
[16:35] download and use these parts. Um, the gap describes this gap in the bodies. So
[16:38] gap describes this gap in the bodies. So
[16:38] gap describes this gap in the bodies. So I went ahead and sliced the vertical
[16:40] I went ahead and sliced the vertical
[16:40] I went ahead and sliced the vertical view. Um, and you can see this small gap
[16:45] view. Um, and you can see this small gap
[16:45] view. Um, and you can see this small gap in between. Note that the gap in the
[16:48] in between. Note that the gap in the
[16:48] in between. Note that the gap in the vertical zone is is actually a different
[16:52] vertical zone is is actually a different
[16:52] vertical zone is is actually a different decision than the gap in the horizontal
[16:53] decision than the gap in the horizontal
[16:54] decision than the gap in the horizontal zone that we grouped them because we
[16:55] zone that we grouped them because we
[16:55] zone that we grouped them because we were lucky to see that um the vertical
[16:59] were lucky to see that um the vertical
[16:59] were lucky to see that um the vertical zone is is its tolerance is based on the
[17:03] zone is is its tolerance is based on the
[17:04] zone is is its tolerance is based on the the squish
[17:06] the squish
[17:06] the squish uh the squish out from the printer um
[17:10] uh the squish out from the printer um
[17:10] uh the squish out from the printer um depositing plastic with the nozzle. How
[17:13] depositing plastic with the nozzle. How
[17:13] depositing plastic with the nozzle. How much does that plastic droop or squish
[17:16] much does that plastic droop or squish
[17:16] much does that plastic droop or squish outward in the lateral zones, a lateral
[17:19] outward in the lateral zones, a lateral
[17:19] outward in the lateral zones, a lateral direction? And uh and and then how much
[17:22] direction? And uh and and then how much
[17:22] direction? And uh and and then how much does it deviate from one line to
[17:24] does it deviate from one line to
[17:24] does it deviate from one line to another? So if you zoom in on this part
[17:26] another? So if you zoom in on this part
[17:26] another? So if you zoom in on this part in real life, you'll see that it's not a
[17:28] in real life, you'll see that it's not a
[17:28] in real life, you'll see that it's not a perfectly straight line. It's going to
[17:29] perfectly straight line. It's going to
[17:29] perfectly straight line. It's going to be bumpy. And so that's one uh design
[17:35] be bumpy. And so that's one uh design
[17:35] be bumpy. And so that's one uh design for manufacturing consideration versus a
[17:38] for manufacturing consideration versus a
[17:38] for manufacturing consideration versus a different one for this height. this this
[17:40] different one for this height. this this
[17:40] different one for this height. this this height the the nozzle is extremely
[17:42] height the the nozzle is extremely
[17:42] height the the nozzle is extremely repeatable in any horizontal direction.
[17:46] repeatable in any horizontal direction.
[17:46] repeatable in any horizontal direction. That's why we can print layers as thin
[17:49] That's why we can print layers as thin
[17:49] That's why we can print layers as thin as 0.1 mm. But the the function to be
[17:56] as 0.1 mm. But the the function to be
[17:56] as 0.1 mm. But the the function to be concerned with is as the nozzle is
[17:58] concerned with is as the nozzle is
[17:58] concerned with is as the nozzle is printing a a free part above another
[18:02] printing a a free part above another
[18:02] printing a a free part above another part and we don't want them to be
[18:05] part and we don't want them to be
[18:05] part and we don't want them to be bonded. Then how much gap do you need to
[18:08] bonded. Then how much gap do you need to
[18:08] bonded. Then how much gap do you need to leave of uh an air an air gap for that
[18:13] leave of uh an air an air gap for that
[18:13] leave of uh an air an air gap for that wet uh liquid plastic to droop down? And
[18:17] wet uh liquid plastic to droop down? And
[18:17] wet uh liquid plastic to droop down? And it may make a little bit of contact with
[18:19] it may make a little bit of contact with
[18:19] it may make a little bit of contact with the layer below, but we don't want it to
[18:21] the layer below, but we don't want it to
[18:21] the layer below, but we don't want it to be fully bonded. And so this is uh
[18:25] be fully bonded. And so this is uh
[18:25] be fully bonded. And so this is uh also um 0.3 in our case is healthy
[18:28] also um 0.3 in our case is healthy
[18:28] also um 0.3 in our case is healthy enough. Then you can take that out of
[18:30] enough. Then you can take that out of
[18:30] enough. Then you can take that out of the printer. It um these two parts will
[18:33] the printer. It um these two parts will
[18:33] the printer. It um these two parts will be uh the three parts will be stuck
[18:36] be uh the three parts will be stuck
[18:36] be uh the three parts will be stuck together. We insert the pin and then we
[18:39] together. We insert the pin and then we
[18:39] together. We insert the pin and then we can just strike it with a very small
[18:42] can just strike it with a very small
[18:42] can just strike it with a very small hammer or you can press it against the
[18:44] hammer or you can press it against the
[18:44] hammer or you can press it against the table and it will crack free. But then
[18:46] table and it will crack free. But then
[18:46] table and it will crack free. But then you don't have gaps. You don't have a a
[18:49] you don't have gaps. You don't have a a
[18:49] you don't have gaps. You don't have a a shaking that is possible between the
[18:51] shaking that is possible between the
[18:51] shaking that is possible between the parts. So that's wonderful. Then if we
[18:53] parts. So that's wonderful. Then if we
[18:53] parts. So that's wonderful. Then if we want to compress those arms in the
[18:55] want to compress those arms in the
[18:55] want to compress those arms in the assembly more, that's when the screw
[18:58] assembly more, that's when the screw
[18:58] assembly more, that's when the screw comes in. So you can um you can let's
[19:02] comes in. So you can um you can let's
[19:02] comes in. So you can um you can let's say you have just a little bit of
[19:04] say you have just a little bit of
[19:04] say you have just a little bit of friction. When I turn this and I tilt it
[19:07] friction. When I turn this and I tilt it
[19:07] friction. When I turn this and I tilt it like that, uh, initially the green lever
[19:12] like that, uh, initially the green lever
[19:12] like that, uh, initially the green lever will drop down just due to the weight of
[19:15] will drop down just due to the weight of
[19:15] will drop down just due to the weight of these things. But now I've taken the
[19:19] these things. But now I've taken the
[19:19] these things. But now I've taken the screw and fastened that
[19:22] screw and fastened that
[19:23] screw and fastened that into it's not it has a clearance with
[19:27] into it's not it has a clearance with
[19:27] into it's not it has a clearance with the it doesn't contact the blue part and
[19:29] the it doesn't contact the blue part and
[19:29] the it doesn't contact the blue part and it doesn't actually contact the green
[19:31] it doesn't actually contact the green
[19:31] it doesn't actually contact the green part. It is it has a segment of this
[19:34] part. It is it has a segment of this
[19:34] part. It is it has a segment of this tube and then it pulls. So the screw is
[19:37] tube and then it pulls. So the screw is
[19:37] tube and then it pulls. So the screw is driven down and it pulls the top up
[19:41] driven down and it pulls the top up
[19:41] driven down and it pulls the top up while pulling the bottom down. And that
[19:44] while pulling the bottom down. And that
[19:44] while pulling the bottom down. And that stretching of the the black
[19:47] stretching of the the black
[19:47] stretching of the the black screw is fighting against the
[19:50] screw is fighting against the
[19:50] screw is fighting against the compressing of however much I stretch
[19:54] compressing of however much I stretch
[19:54] compressing of however much I stretch the black tube is how much this the blue
[19:57] the black tube is how much this the blue
[19:57] the black tube is how much this the blue part will want to react and and squeeze
[20:00] part will want to react and and squeeze
[20:00] part will want to react and and squeeze down. And since there was no gap since
[20:02] down. And since there was no gap since
[20:02] down. And since there was no gap since they were already making contact, then
[20:04] they were already making contact, then
[20:04] they were already making contact, then as soon as the blue part starts to
[20:06] as soon as the blue part starts to
[20:06] as soon as the blue part starts to squeeze down, then it is squeezing that
[20:09] squeeze down, then it is squeezing that
[20:09] squeeze down, then it is squeezing that green part and then it's adding more and
[20:11] green part and then it's adding more and
[20:11] green part and then it's adding more and more friction. So down to we can control
[20:14] more friction. So down to we can control
[20:14] more friction. So down to we can control exactly how much force it takes to push
[20:16] exactly how much force it takes to push
[20:16] exactly how much force it takes to push this and push it down. And so that's
[20:19] this and push it down. And so that's
[20:19] this and push it down. And so that's excellent. There's one size of screw
[20:20] excellent. There's one size of screw
[20:20] excellent. There's one size of screw that will work with the the small parts
[20:23] that will work with the the small parts
[20:23] that will work with the the small parts and another size of screw that will work
[20:25] and another size of screw that will work
[20:25] and another size of screw that will work with the the the larger one. We don't
[20:28] with the the the larger one. We don't
[20:28] with the the the larger one. We don't use this blue urethane. We're using
[20:30] use this blue urethane. We're using
[20:30] use this blue urethane. We're using HDPE, but it's around this
[20:33] HDPE, but it's around this
[20:33] HDPE, but it's around this size. Okay.
[20:35] size. Okay.
[20:35] size. Okay. Grips.
[20:37] Grips.
[20:37] Grips. Um what is a grip? Oh, the grip is what
[20:39] Um what is a grip? Oh, the grip is what
[20:40] Um what is a grip? Oh, the grip is what I'm calling this uh the the
[20:43] I'm calling this uh the the
[20:43] I'm calling this uh the the arms which contact the um the pin. Okay,
[20:49] arms which contact the um the pin. Okay,
[20:49] arms which contact the um the pin. Okay, so we have three grips. Uh right side
[20:52] so we have three grips. Uh right side
[20:52] so we have three grips. Uh right side has two grips and the and the left side
[20:53] has two grips and the and the left side
[20:53] has two grips and the and the left side has one grip. And um for a general uh
[20:58] has one grip. And um for a general uh
[20:58] has one grip. And um for a general uh balance of strength, first you say,
[21:01] balance of strength, first you say,
[21:01] balance of strength, first you say, well, we would want them to be uh
[21:03] well, we would want them to be uh
[21:03] well, we would want them to be uh symmetric in strength. So they would
[21:05] symmetric in strength. So they would
[21:05] symmetric in strength. So they would both have the total amount of height
[21:07] both have the total amount of height
[21:08] both have the total amount of height that uh that is equal. So if you split
[21:11] that uh that is equal. So if you split
[21:11] that uh that is equal. So if you split this into four pieces, you drew a line
[21:13] this into four pieces, you drew a line
[21:13] this into four pieces, you drew a line here, then you would have four equal
[21:15] here, then you would have four equal
[21:15] here, then you would have four equal pieces. You drew a line right in the
[21:16] pieces. You drew a line right in the
[21:16] pieces. You drew a line right in the middle where oh my you can't see my
[21:19] middle where oh my you can't see my
[21:19] middle where oh my you can't see my mouse.
[21:21] mouse.
[21:21] mouse. Uh so if you drew a line cut just like
[21:25] Uh so if you drew a line cut just like
[21:25] Uh so if you drew a line cut just like this, you could see four equal pieces
[21:27] this, you could see four equal pieces
[21:27] this, you could see four equal pieces and they would the goal is make them
[21:29] and they would the goal is make them
[21:29] and they would the goal is make them approximately equal. And then if we
[21:31] approximately equal. And then if we
[21:31] approximately equal. And then if we change that parameter of the height of
[21:33] change that parameter of the height of
[21:33] change that parameter of the height of the part then that the height of each
[21:38] the part then that the height of each
[21:38] the part then that the height of each segment uh each grip would also increase
[21:43] segment uh each grip would also increase
[21:43] segment uh each grip would also increase and have a matching ratio to the
[21:47] and have a matching ratio to the
[21:47] and have a matching ratio to the original part. Okay. So this one's 17
[21:49] original part. Okay. So this one's 17
[21:49] original part. Okay. So this one's 17 this is 23. At the end after this design
[21:53] this is 23. At the end after this design
[21:53] this is 23. At the end after this design was tested and adjusted then this uh the
[21:57] was tested and adjusted then this uh the
[21:58] was tested and adjusted then this uh the total of this blue line is 23 mm. The
[22:01] total of this blue line is 23 mm. The
[22:01] total of this blue line is 23 mm. The total of the green is 17. So that means
[22:03] total of the green is 17. So that means
[22:03] total of the green is 17. So that means we've made these larger. And the reason
[22:05] we've made these larger. And the reason
[22:05] we've made these larger. And the reason is essentially the the simplest way to
[22:08] is essentially the the simplest way to
[22:08] is essentially the the simplest way to describe the mechanical
[22:11] describe the mechanical
[22:11] describe the mechanical um strength is every time that you you
[22:16] um strength is every time that you you
[22:16] um strength is every time that you you split an arm into multiple pieces. Uh
[22:20] split an arm into multiple pieces. Uh
[22:20] split an arm into multiple pieces. Uh well the having these arms spread gives
[22:23] well the having these arms spread gives
[22:23] well the having these arms spread gives you a a better moment
[22:27] you a a better moment
[22:27] you a a better moment uh moment
[22:29] uh moment
[22:29] uh moment reaction capability or reaction strength
[22:32] reaction capability or reaction strength
[22:32] reaction capability or reaction strength to the the moment that happens. Let's
[22:34] to the the moment that happens. Let's
[22:34] to the the moment that happens. Let's say my my hand is a mass and I'm going
[22:36] say my my hand is a mass and I'm going
[22:36] say my my hand is a mass and I'm going to uh drop it down or pull down. Having
[22:41] to uh drop it down or pull down. Having
[22:41] to uh drop it down or pull down. Having these arms spread out of course is a
[22:45] these arms spread out of course is a
[22:45] these arms spread out of course is a stronger condition than having them
[22:47] stronger condition than having them
[22:47] stronger condition than having them together. Just like you see those those
[22:49] together. Just like you see those those
[22:49] together. Just like you see those those dancers on the pole when they when they
[22:51] dancers on the pole when they when they
[22:51] dancers on the pole when they when they hold themselves out laterally that they
[22:53] hold themselves out laterally that they
[22:53] hold themselves out laterally that they do it by spreading their hands out
[22:55] do it by spreading their hands out
[22:55] do it by spreading their hands out further. So having that spread we can I
[22:59] further. So having that spread we can I
[22:59] further. So having that spread we can I think this is inverted actually this one
[23:01] think this is inverted actually this one
[23:01] think this is inverted actually this one would be uh we need less in total length
[23:05] would be uh we need less in total length
[23:05] would be uh we need less in total length for the blue section than the green
[23:07] for the blue section than the green
[23:07] for the blue section than the green section. But at least for the sake of
[23:10] section. But at least for the sake of
[23:10] section. But at least for the sake of this discussion you can pay attention to
[23:12] this discussion you can pay attention to
[23:12] this discussion you can pay attention to it and play with it and and work with
[23:14] it and play with it and and work with
[23:14] it and play with it and and work with it. this for our parts it was not
[23:15] it. this for our parts it was not
[23:16] it. this for our parts it was not extremely
[23:16] extremely
[23:17] extremely crucial.
[23:24] Um okay it's just another visualization
[23:24] Um okay it's just another visualization with the colors in
[23:26] with the colors in
[23:26] with the colors in there.
[23:34] Um essentially divided by two uh pin
[23:34] Um essentially divided by two uh pin diameter we're calling this yellow zone.
[23:37] diameter we're calling this yellow zone.
[23:37] diameter we're calling this yellow zone. I talk about the stackup of tolerances
[23:39] I talk about the stackup of tolerances
[23:39] I talk about the stackup of tolerances which so you have one simple number for
[23:42] which so you have one simple number for
[23:42] which so you have one simple number for the size that we allocated to this uh to
[23:46] the size that we allocated to this uh to
[23:46] the size that we allocated to this uh to this inner diameter which will contact
[23:49] this inner diameter which will contact
[23:50] this inner diameter which will contact the pin.
[23:51] the pin.
[23:51] the pin. Um but I don't think I can say it
[23:55] Um but I don't think I can say it
[23:55] Um but I don't think I can say it extremely concisely and so I'm going to
[23:57] extremely concisely and so I'm going to
[23:57] extremely concisely and so I'm going to skip that and we could discuss it in the
[23:59] skip that and we could discuss it in the
[23:59] skip that and we could discuss it in the comments or something like that.
[24:02] comments or something like that.
[24:02] comments or something like that. Um we have these chamfers that are also
[24:05] Um we have these chamfers that are also
[24:05] Um we have these chamfers that are also parametric in that you can adjust it and
[24:08] parametric in that you can adjust it and
[24:08] parametric in that you can adjust it and it'll adjust all over the part but also
[24:10] it'll adjust all over the part but also
[24:10] it'll adjust all over the part but also they have an impact in the design uh the
[24:13] they have an impact in the design uh the
[24:13] they have an impact in the design uh the the manufacturing of the part. So if you
[24:18] the manufacturing of the part. So if you
[24:18] the manufacturing of the part. So if you consider that this part is symmetric top
[24:20] consider that this part is symmetric top
[24:20] consider that this part is symmetric top to bottom. So the bottom side will have
[24:22] to bottom. So the bottom side will have
[24:22] to bottom. So the bottom side will have these chamfers the same as the top and
[24:24] these chamfers the same as the top and
[24:24] these chamfers the same as the top and the
[24:26] the
[24:26] the uh the space where
[24:30] uh the space where
[24:30] uh the space where you you have this 40 they're always 45
[24:34] you you have this 40 they're always 45
[24:34] you you have this 40 they're always 45 degrees the chamfers it's uh reduces the
[24:38] degrees the chamfers it's uh reduces the
[24:38] degrees the chamfers it's uh reduces the chance of having this elephant's foot
[24:40] chance of having this elephant's foot
[24:40] chance of having this elephant's foot that's the term for uh the excessive
[24:43] that's the term for uh the excessive
[24:44] that's the term for uh the excessive squish of the of the model against the
[24:47] squish of the of the model against the
[24:47] squish of the of the model against the base of the print and so that's just a
[24:49] base of the print and so that's just a
[24:50] base of the print and so that's just a standard we do for all different parts.
[24:52] standard we do for all different parts.
[24:52] standard we do for all different parts. And then in the intermediate sections
[24:54] And then in the intermediate sections
[24:54] And then in the intermediate sections where these hoops contact each other, we
[24:57] where these hoops contact each other, we
[24:57] where these hoops contact each other, we already said that the the small gap is
[25:00] already said that the the small gap is
[25:00] already said that the the small gap is not enough to make them completely free
[25:03] not enough to make them completely free
[25:04] not enough to make them completely free from one another. So the grips will
[25:05] from one another. So the grips will
[25:05] from one another. So the grips will contact one another and we reducing this
[25:08] contact one another and we reducing this
[25:08] contact one another and we reducing this contact area that needs to be cracked
[25:11] contact area that needs to be cracked
[25:11] contact area that needs to be cracked free later by reducing this um this
[25:16] free later by reducing this um this
[25:16] free later by reducing this um this contact area. The larger chamfer reduces
[25:19] contact area. The larger chamfer reduces
[25:19] contact area. The larger chamfer reduces the total area, reduces the bonding
[25:21] the total area, reduces the bonding
[25:21] the total area, reduces the bonding between the two
[25:28] [Music]
[25:28] [Music] parts. This is some discussion that I've
[25:31] parts. This is some discussion that I've
[25:31] parts. This is some discussion that I've already covered a little bit.
[25:34] already covered a little bit.
[25:34] already covered a little bit. Labeling. Okay, so this is the labeling
[25:36] Labeling. Okay, so this is the labeling
[25:36] Labeling. Okay, so this is the labeling standard that I use for all 3D parts.
[25:39] standard that I use for all 3D parts.
[25:39] standard that I use for all 3D parts. I've mentioned this in other videos, but
[25:41] I've mentioned this in other videos, but
[25:41] I've mentioned this in other videos, but um there are years and years of
[25:43] um there are years and years of
[25:43] um there are years and years of experience behind it. So, uh, the
[25:46] experience behind it. So, uh, the
[25:46] experience behind it. So, uh, the decision of deboss or emboss. Debboss is
[25:49] decision of deboss or emboss. Debboss is
[25:49] decision of deboss or emboss. Debboss is always the default choice for adding
[25:52] always the default choice for adding
[25:52] always the default choice for adding text into the parts. Um, it comes out
[25:55] text into the parts. Um, it comes out
[25:55] text into the parts. Um, it comes out better when you're printing it. That's
[25:57] better when you're printing it. That's
[25:57] better when you're printing it. That's the essential thing. And your slicer
[26:00] the essential thing. And your slicer
[26:00] the essential thing. And your slicer does not attempt to add any small little
[26:02] does not attempt to add any small little
[26:02] does not attempt to add any small little supports that are just hanging off there
[26:05] supports that are just hanging off there
[26:05] supports that are just hanging off there to support some tiny um, emboss. Okay.
[26:09] to support some tiny um, emboss. Okay.
[26:09] to support some tiny um, emboss. Okay. So 0.5 mm in our case is between is at
[26:13] So 0.5 mm in our case is between is at
[26:13] So 0.5 mm in our case is between is at least greater than one path width where
[26:16] least greater than one path width where
[26:16] least greater than one path width where the path width is the the when the
[26:20] the path width is the the when the
[26:20] the path width is the the when the nozzle exerts a a path for a single
[26:25] nozzle exerts a a path for a single
[26:25] nozzle exerts a a path for a single extrusion then that's 0.4 millimeters.
[26:28] extrusion then that's 0.4 millimeters.
[26:28] extrusion then that's 0.4 millimeters. And if we make it larger than one path
[26:30] And if we make it larger than one path
[26:30] And if we make it larger than one path then then even given different
[26:32] then then even given different
[26:32] then then even given different tolerances or cranking up the print
[26:34] tolerances or cranking up the print
[26:34] tolerances or cranking up the print speed you can still read this uh this
[26:37] speed you can still read this uh this
[26:37] speed you can still read this uh this text. It's not necessary for it to be
[26:40] text. It's not necessary for it to be
[26:40] text. It's not necessary for it to be more than two path widths. Um, more than
[26:44] more than two path widths. Um, more than
[26:44] more than two path widths. Um, more than two also can impact the strength of your
[26:46] two also can impact the strength of your
[26:46] two also can impact the strength of your part if you're making assumptions about
[26:48] part if you're making assumptions about
[26:48] part if you're making assumptions about the the overall thickness impact on the
[26:51] the the overall thickness impact on the
[26:51] the the overall thickness impact on the the part strength. Okay. The height of
[26:53] the part strength. Okay. The height of
[26:54] the part strength. Okay. The height of the text 6 mm because that is the
[26:56] the text 6 mm because that is the
[26:56] the text 6 mm because that is the smallest that you can make and fit in
[26:59] smallest that you can make and fit in
[26:59] smallest that you can make and fit in almost any part that we build, but it is
[27:02] almost any part that we build, but it is
[27:02] almost any part that we build, but it is also still legible. it's the large
[27:05] also still legible. it's the large
[27:05] also still legible. it's the large enough that that it doesn't get lost in
[27:08] enough that that it doesn't get lost in
[27:08] enough that that it doesn't get lost in the part. Then finally, the orientation
[27:10] the part. Then finally, the orientation
[27:10] the part. Then finally, the orientation is very meaningful. It's telling us
[27:12] is very meaningful. It's telling us
[27:12] is very meaningful. It's telling us which way the part is designed to be
[27:14] which way the part is designed to be
[27:14] which way the part is designed to be printed. You should be re able to read
[27:16] printed. You should be re able to read
[27:16] printed. You should be re able to read this when you're running your print.
[27:19] this when you're running your print.
[27:19] this when you're running your print. That helps later on in troubleshooting.
[27:21] That helps later on in troubleshooting.
[27:21] That helps later on in troubleshooting. Oops, I've I've uh set the wrong uh the
[27:24] Oops, I've I've uh set the wrong uh the
[27:24] Oops, I've I've uh set the wrong uh the old version of the part in the printer.
[27:26] old version of the part in the printer.
[27:26] old version of the part in the printer. And now you can see it very early in the
[27:28] And now you can see it very early in the
[27:28] And now you can see it very early in the print before you waste your plastic. You
[27:31] print before you waste your plastic. You
[27:31] print before you waste your plastic. You can see that version one pop in and and
[27:33] can see that version one pop in and and
[27:34] can see that version one pop in and and let you know um you can see in real life
[27:37] let you know um you can see in real life
[27:37] let you know um you can see in real life if you have oriented the part properly
[27:39] if you have oriented the part properly
[27:39] if you have oriented the part properly for the printing and the
[27:41] for the printing and the
[27:41] for the printing and the slicing. Um and then the other way that
[27:44] slicing. Um and then the other way that
[27:44] slicing. Um and then the other way that we indicate the orientation actually
[27:46] we indicate the orientation actually
[27:46] we indicate the orientation actually comes out through the STL file. we we
[27:49] comes out through the STL file. we we
[27:49] comes out through the STL file. we we create our own um a set of axes that is
[27:54] create our own um a set of axes that is
[27:54] create our own um a set of axes that is just like the origin uh coordinate frame
[27:57] just like the origin uh coordinate frame
[27:57] just like the origin uh coordinate frame that's called print and usually it
[28:01] that's called print and usually it
[28:01] that's called print and usually it matches the original coordinate frame of
[28:03] matches the original coordinate frame of
[28:03] matches the original coordinate frame of the software like solid works but on
[28:06] the software like solid works but on
[28:06] the software like solid works but on occasion based on what we what we are
[28:09] occasion based on what we what we are
[28:09] occasion based on what we what we are designing we may rotate that later and
[28:12] designing we may rotate that later and
[28:12] designing we may rotate that later and then it defines the vertical direction
[28:14] then it defines the vertical direction
[28:14] then it defines the vertical direction in the STL you cannot um STL file as the
[28:18] in the STL you cannot um STL file as the
[28:18] in the STL you cannot um STL file as the the
[28:20] the
[28:20] the tessillated
[28:22] tessillated
[28:23] tessillated triangulated output, but it does have it
[28:26] triangulated output, but it does have it
[28:26] triangulated output, but it does have it does have an orientation embedded
[28:27] does have an orientation embedded
[28:27] does have an orientation embedded somewhere inside of
[28:29] somewhere inside of
[28:29] somewhere inside of it. Um, properties, I actually go ahead
[28:33] it. Um, properties, I actually go ahead
[28:33] it. Um, properties, I actually go ahead and add properties when a part is
[28:35] and add properties when a part is
[28:35] and add properties when a part is intended to be when we anticipate it's
[28:38] intended to be when we anticipate it's
[28:38] intended to be when we anticipate it's going to have revisions. It's going to
[28:39] going to have revisions. It's going to
[28:39] going to have revisions. It's going to have different varieties and its name is
[28:41] have different varieties and its name is
[28:42] have different varieties and its name is related to several other parts that are
[28:43] related to several other parts that are
[28:43] related to several other parts that are out there on the hard drive. Um, so
[28:46] out there on the hard drive. Um, so
[28:46] out there on the hard drive. Um, so keywords are actually crucial. If we
[28:49] keywords are actually crucial. If we
[28:49] keywords are actually crucial. If we fully describe, what I'm seeing all the
[28:51] fully describe, what I'm seeing all the
[28:51] fully describe, what I'm seeing all the time is people are are entering the file
[28:54] time is people are are entering the file
[28:54] time is people are are entering the file name of the part, the full part number
[28:57] name of the part, the full part number
[28:57] name of the part, the full part number and model number and stuff. Um, and that
[29:01] and model number and stuff. Um, and that
[29:01] and model number and stuff. Um, and that that gets things very confusing very
[29:03] that gets things very confusing very
[29:03] that gets things very confusing very quickly. If you look inside the folder
[29:05] quickly. If you look inside the folder
[29:05] quickly. If you look inside the folder full of parts that make up one assembly.
[29:08] full of parts that make up one assembly.
[29:08] full of parts that make up one assembly. So this motor would say
[29:12] So this motor would say
[29:12] So this motor would say DF410B 24H 40mm fan and 12 volts or
[29:18] DF410B 24H 40mm fan and 12 volts or
[29:18] DF410B 24H 40mm fan and 12 volts or something. We're putting that
[29:19] something. We're putting that
[29:19] something. We're putting that information into the title of the file
[29:22] information into the title of the file
[29:22] information into the title of the file because later if we want to search for
[29:24] because later if we want to search for
[29:24] because later if we want to search for it on the hard drive or if someone wants
[29:26] it on the hard drive or if someone wants
[29:26] it on the hard drive or if someone wants to search it online then they can find
[29:28] to search it online then they can find
[29:28] to search it online then they can find it. And so then these file names become
[29:31] it. And so then these file names become
[29:31] it. And so then these file names become very long and also you can it's hard to
[29:33] very long and also you can it's hard to
[29:33] very long and also you can it's hard to see the stuff in the feature tree unless
[29:35] see the stuff in the feature tree unless
[29:35] see the stuff in the feature tree unless you expand the feature tree while you're
[29:37] you expand the feature tree while you're
[29:37] you expand the feature tree while you're modeling. And so that's undesirable
[29:40] modeling. And so that's undesirable
[29:40] modeling. And so that's undesirable these long names. Alternatively, you can
[29:43] these long names. Alternatively, you can
[29:43] these long names. Alternatively, you can take all that information and enter it
[29:45] take all that information and enter it
[29:45] take all that information and enter it in the keywords. And so if we want thing
[29:48] in the keywords. And so if we want thing
[29:48] in the keywords. And so if we want thing models and designs to last for 10 years
[29:50] models and designs to last for 10 years
[29:50] models and designs to last for 10 years and to be useful for other people to
[29:52] and to be useful for other people to
[29:52] and to be useful for other people to build on and if we want to have
[29:54] build on and if we want to have
[29:54] build on and if we want to have communities full of parts that are easy
[29:56] communities full of parts that are easy
[29:56] communities full of parts that are easy to navigate, that's when you enter
[29:59] to navigate, that's when you enter
[29:59] to navigate, that's when you enter everything that you can enter in the
[30:01] everything that you can enter in the
[30:01] everything that you can enter in the keyword. Basically, my rule of thumb is
[30:04] keyword. Basically, my rule of thumb is
[30:04] keyword. Basically, my rule of thumb is if I've searched for the part, uh, one
[30:06] if I've searched for the part, uh, one
[30:06] if I've searched for the part, uh, one year later, I looked for this and I
[30:08] year later, I looked for this and I
[30:08] year later, I looked for this and I called it a pivot and I and I but I
[30:10] called it a pivot and I and I but I
[30:10] called it a pivot and I and I but I searched for a hinge. And so, uh, then I
[30:14] searched for a hinge. And so, uh, then I
[30:14] searched for a hinge. And so, uh, then I went searching hinge and it wasn't in
[30:16] went searching hinge and it wasn't in
[30:16] went searching hinge and it wasn't in here. And so, I added hinge as a keyword
[30:19] here. And so, I added hinge as a keyword
[30:19] here. And so, I added hinge as a keyword as soon as I opened up the part. After I
[30:21] as soon as I opened up the part. After I
[30:21] as soon as I opened up the part. After I found it, I add that. So, next time I
[30:23] found it, I add that. So, next time I
[30:23] found it, I add that. So, next time I search, if I'm searching pivot or hinge,
[30:25] search, if I'm searching pivot or hinge,
[30:25] search, if I'm searching pivot or hinge, I can pull it up. Um, and then I talked
[30:28] I can pull it up. Um, and then I talked
[30:28] I can pull it up. Um, and then I talked about the past version because there is
[30:31] about the past version because there is
[30:31] about the past version because there is a past version I don't want to throw
[30:32] a past version I don't want to throw
[30:32] a past version I don't want to throw away. It's not um it's not a full
[30:35] away. It's not um it's not a full
[30:36] away. It's not um it's not a full improvement. This is a change in
[30:37] improvement. This is a change in
[30:37] improvement. This is a change in improvement, this version three. And so
[30:41] improvement, this version three. And so
[30:41] improvement, this version three. And so uh I still need to retain the old
[30:43] uh I still need to retain the old
[30:43] uh I still need to retain the old version. I'm not going to delete it.
[30:45] version. I'm not going to delete it.
[30:45] version. I'm not going to delete it. Then at least if I choose a part to use
[30:48] Then at least if I choose a part to use
[30:48] Then at least if I choose a part to use as a template later, I'm going to be
[30:51] as a template later, I'm going to be
[30:51] as a template later, I'm going to be able to open up the description and say,
[30:52] able to open up the description and say,
[30:52] able to open up the description and say, "Oh, this is the latest. This is the one
[30:55] "Oh, this is the latest. This is the one
[30:55] "Oh, this is the latest. This is the one I want to use as my template. It has the
[30:57] I want to use as my template. It has the
[30:58] I want to use as my template. It has the cleanest feature tree,
[31:01] cleanest feature tree,
[31:01] cleanest feature tree, etc. Okay, here's the hinge design
[31:04] etc. Okay, here's the hinge design
[31:04] etc. Okay, here's the hinge design inside of Solid Works. So, we can spin
[31:06] inside of Solid Works. So, we can spin
[31:06] inside of Solid Works. So, we can spin it around and look at it a little bit.
[31:09] it around and look at it a little bit.
[31:09] it around and look at it a little bit. Um, the first thing I wanted to share is
[31:12] Um, the first thing I wanted to share is
[31:12] Um, the first thing I wanted to share is the how the feature tree is done. This
[31:15] the how the feature tree is done. This
[31:15] the how the feature tree is done. This is a set of standards you'll find in all
[31:17] is a set of standards you'll find in all
[31:17] is a set of standards you'll find in all of our parts that we've done except the
[31:19] of our parts that we've done except the
[31:19] of our parts that we've done except the ones that were done in a hurry where the
[31:22] ones that were done in a hurry where the
[31:22] ones that were done in a hurry where the part itself is a a full tutorial for
[31:27] part itself is a a full tutorial for
[31:27] part itself is a a full tutorial for anyone who wishes to learn this. Um if
[31:29] anyone who wishes to learn this. Um if
[31:29] anyone who wishes to learn this. Um if you download any of my parts, you should
[31:31] you download any of my parts, you should
[31:31] you download any of my parts, you should see a clean feature tree that is able to
[31:33] see a clean feature tree that is able to
[31:33] see a clean feature tree that is able to teach you. You can ask questions to the
[31:36] teach you. You can ask questions to the
[31:36] teach you. You can ask questions to the model and get your answers. So like the
[31:39] model and get your answers. So like the
[31:39] model and get your answers. So like the first question is how did the designer
[31:41] first question is how did the designer
[31:41] first question is how did the designer start this design? where uh did they
[31:45] start this design? where uh did they
[31:45] start this design? where uh did they make uh swept um swept or extrusions or
[31:50] make uh swept um swept or extrusions or
[31:50] make uh swept um swept or extrusions or rotated uh revolved boss etc. And so you
[31:54] rotated uh revolved boss etc. And so you
[31:54] rotated uh revolved boss etc. And so you go to the very first feature and you see
[31:56] go to the very first feature and you see
[31:56] go to the very first feature and you see we're starting with the hinge bodies the
[31:58] we're starting with the hinge bodies the
[31:58] we're starting with the hinge bodies the the round parts. Okay, there's a
[32:01] the round parts. Okay, there's a
[32:01] the round parts. Okay, there's a cylinder. How is that cylinder defined?
[32:03] cylinder. How is that cylinder defined?
[32:03] cylinder. How is that cylinder defined? And we edit sketch. And now we can see
[32:06] And we edit sketch. And now we can see
[32:06] And we edit sketch. And now we can see that there are only three dimensions.
[32:09] that there are only three dimensions.
[32:09] that there are only three dimensions. Everything else is just a constraint. So
[32:11] Everything else is just a constraint. So
[32:12] Everything else is just a constraint. So this is communicating the design intent.
[32:14] this is communicating the design intent.
[32:14] this is communicating the design intent. We said uh well how far up from the from
[32:18] We said uh well how far up from the from
[32:18] We said uh well how far up from the from the central center um the origin is the
[32:22] the central center um the origin is the
[32:22] the central center um the origin is the start of the hinge and that is the
[32:26] start of the hinge and that is the
[32:26] start of the hinge and that is the answer is far up uh sorry as we're
[32:31] answer is far up uh sorry as we're
[32:31] answer is far up uh sorry as we're should be looking like this up and down
[32:34] should be looking like this up and down
[32:34] should be looking like this up and down in the placement of the of the part in
[32:37] in the placement of the of the part in
[32:37] in the placement of the of the part in real life. How far up is this line?
[32:40] real life. How far up is this line?
[32:40] real life. How far up is this line? Well, it's up. It is below the origin to
[32:44] Well, it's up. It is below the origin to
[32:44] Well, it's up. It is below the origin to the degree which sets the middle of the
[32:48] the degree which sets the middle of the
[32:48] the degree which sets the middle of the hinge at the center of the design.
[32:50] hinge at the center of the design.
[32:50] hinge at the center of the design. That's a constraint instead of using a
[32:54] That's a constraint instead of using a
[32:54] That's a constraint instead of using a instead of using a dimension. So with
[32:57] instead of using a dimension. So with
[32:57] instead of using a dimension. So with the constraint having this midpoint
[32:59] the constraint having this midpoint
[32:59] the constraint having this midpoint centered along this origin that is one
[33:03] centered along this origin that is one
[33:03] centered along this origin that is one of the things that lets us change the
[33:06] of the things that lets us change the
[33:06] of the things that lets us change the parameter and maintain everything nicely
[33:09] parameter and maintain everything nicely
[33:09] parameter and maintain everything nicely in the design. The the only thing that's
[33:12] in the design. The the only thing that's
[33:12] in the design. The the only thing that's intended in this design
[33:15] intended in this design
[33:15] intended in this design um to really define this specific model
[33:18] um to really define this specific model
[33:18] um to really define this specific model is are these three numbers. And then if
[33:20] is are these three numbers. And then if
[33:20] is are these three numbers. And then if we click one, what is 30? And then it's
[33:23] we click one, what is 30? And then it's
[33:23] we click one, what is 30? And then it's a global variable. Oh my my graphics. I
[33:27] a global variable. Oh my my graphics. I
[33:27] a global variable. Oh my my graphics. I got to get this over
[33:41] here. We'll double click this one. This
[33:41] here. We'll double click this one. This one is a global variable. That's what
[33:42] one is a global variable. That's what
[33:42] one is a global variable. That's what that little world means. And then that
[33:45] that little world means. And then that
[33:45] that little world means. And then that is the outer diameter of the hinge. OD
[33:47] is the outer diameter of the hinge. OD
[33:47] is the outer diameter of the hinge. OD hinge. And it should have an E. So if I
[33:51] hinge. And it should have an E. So if I
[33:51] hinge. And it should have an E. So if I want to change
[33:57] that inner diameter will work with that.
[33:57] that inner diameter will work with that. This is OD tube. That is the diameter of
[34:02] This is OD tube. That is the diameter of
[34:02] This is OD tube. That is the diameter of the tube that's going to be placed in
[34:03] the tube that's going to be placed in
[34:03] the tube that's going to be placed in there. Let's change that and let's see
[34:05] there. Let's change that and let's see
[34:05] there. Let's change that and let's see what happens. So we're going to build
[34:07] what happens. So we're going to build
[34:07] what happens. So we're going to build this. We're going to go to equations,
[34:10] this. We're going to go to equations,
[34:10] this. We're going to go to equations, manage
[34:12] manage
[34:12] manage equations, and then we say uh OD tube.
[34:16] equations, and then we say uh OD tube.
[34:16] equations, and then we say uh OD tube. We're going to make that four instead of
[34:18] We're going to make that four instead of
[34:18] We're going to make that four instead of 6.6.
[34:19] 6.6.
[34:19] 6.6. six and then okay the model will
[34:23] six and then okay the model will
[34:23] six and then okay the model will rebuild. That's small. Let's see if the
[34:25] rebuild. That's small. Let's see if the
[34:25] rebuild. That's small. Let's see if the model can maintain itself. Wow. Okay.
[34:29] model can maintain itself. Wow. Okay.
[34:29] model can maintain itself. Wow. Okay. So, if you need to design this hinge,
[34:31] So, if you need to design this hinge,
[34:31] So, if you need to design this hinge, same type of hinge for a different type
[34:34] same type of hinge for a different type
[34:34] same type of hinge for a different type of pin, you can simply change that one
[34:36] of pin, you can simply change that one
[34:36] of pin, you can simply change that one single variable and everything rebuilds.
[34:40] single variable and everything rebuilds.
[34:40] single variable and everything rebuilds. So that communicates also the design
[34:42] So that communicates also the design
[34:42] So that communicates also the design intent is not not about uh that specific
[34:47] intent is not not about uh that specific
[34:47] intent is not not about uh that specific interior diameter uh the the essence of
[34:50] interior diameter uh the the essence of
[34:50] interior diameter uh the the essence of the design must be something else and so
[34:53] the design must be something else and so
[34:53] the design must be something else and so if you change everything that you can
[34:55] if you change everything that you can
[34:55] if you change everything that you can change and then the things that are not
[34:59] change and then the things that are not
[34:59] change and then the things that are not changeable is kind of the essence of the
[35:01] changeable is kind of the essence of the
[35:01] changeable is kind of the essence of the design. I don't know if that if that
[35:03] design. I don't know if that if that
[35:03] design. I don't know if that if that description has meaning but um okay so
[35:06] description has meaning but um okay so
[35:06] description has meaning but um okay so manage equations we move that back to
[35:08] manage equations we move that back to
[35:08] manage equations we move that back to 6.6
[35:10] 6.6
[35:10] 6.6 six. But the more you know what you are
[35:15] six. But the more you know what you are
[35:15] six. But the more you know what you are trying to aim for in your design, the
[35:17] trying to aim for in your design, the
[35:17] trying to aim for in your design, the more you're able to uh make things
[35:20] more you're able to uh make things
[35:20] more you're able to uh make things parametric. And some of that's just
[35:22] parametric. And some of that's just
[35:22] parametric. And some of that's just experience and some of it
[35:24] experience and some of it
[35:24] experience and some of it is intention. Um, okay.
[35:29] is intention. Um, okay.
[35:29] is intention. Um, okay. So, what did they do? What did the
[35:32] So, what did they do? What did the
[35:32] So, what did they do? What did the designer do? By the way, these colors,
[35:34] designer do? By the way, these colors,
[35:34] designer do? By the way, these colors, that's a problem I don't know how to fix
[35:36] that's a problem I don't know how to fix
[35:36] that's a problem I don't know how to fix when I when I rebuild the part
[35:39] when I when I rebuild the part
[35:39] when I when I rebuild the part sometimes. So, we'll do this. Adding the
[35:42] sometimes. So, we'll do this. Adding the
[35:42] sometimes. So, we'll do this. Adding the color to a face. Oh, it's just m it's
[35:46] color to a face. Oh, it's just m it's
[35:46] color to a face. Oh, it's just m it's maintaining the color in the model even
[35:49] maintaining the color in the model even
[35:49] maintaining the color in the model even though the color was applied to a body.
[35:52] though the color was applied to a body.
[35:52] though the color was applied to a body. Oh, I'll show you that here. So, later
[35:55] Oh, I'll show you that here. So, later
[35:55] Oh, I'll show you that here. So, later on,
[35:56] on,
[35:56] on, uh, after we clear the hinge, this is
[35:59] uh, after we clear the hinge, this is
[35:59] uh, after we clear the hinge, this is the moment where All right, we've made
[36:01] the moment where All right, we've made
[36:01] the moment where All right, we've made our first slice.
[36:03] our first slice.
[36:03] our first slice. But we haven't made the vertical slice
[36:05] But we haven't made the vertical slice
[36:05] But we haven't made the vertical slice that separates this into two parts. No,
[36:07] that separates this into two parts. No,
[36:07] that separates this into two parts. No, we did. We did. Okay. So, now we have
[36:09] we did. We did. Okay. So, now we have
[36:09] we did. We did. Okay. So, now we have two bodies where previously we had one
[36:13] two bodies where previously we had one
[36:13] two bodies where previously we had one before we clear the hinge. Body A. And
[36:17] before we clear the hinge. Body A. And
[36:17] before we clear the hinge. Body A. And then we clear the hinge. There must be
[36:19] then we clear the hinge. There must be
[36:20] then we clear the hinge. There must be two bodies now. And the only one of them
[36:22] two bodies now. And the only one of them
[36:22] two bodies now. And the only one of them has a name because I named it later on
[36:24] has a name because I named it later on
[36:24] has a name because I named it later on in the feature tree. I I won't I won't
[36:26] in the feature tree. I I won't I won't
[36:26] in the feature tree. I I won't I won't play with that.
[36:28] play with that.
[36:28] play with that. Um so this is how the designer did not
[36:32] Um so this is how the designer did not
[36:32] Um so this is how the designer did not make two separate drawings for these
[36:34] make two separate drawings for these
[36:34] make two separate drawings for these parts. It is uh begins as one drawing
[36:36] parts. It is uh begins as one drawing
[36:36] parts. It is uh begins as one drawing and that's kind of what helps it remain
[36:44] unified. I think the only other thing
[36:44] unified. I think the only other thing that I would like to to share in the
[36:47] that I would like to to share in the
[36:47] that I would like to to share in the model instead of going through all of it
[36:48] model instead of going through all of it
[36:48] model instead of going through all of it right here is uh just the the printing
[36:52] right here is uh just the the printing
[36:52] right here is uh just the the printing features. So uh if you view coordinate
[36:56] features. So uh if you view coordinate
[36:56] features. So uh if you view coordinate systems we have this print here um in
[37:00] systems we have this print here um in
[37:00] systems we have this print here um in this version of the hinge hinge double
[37:02] this version of the hinge hinge double
[37:02] this version of the hinge hinge double now the the coordinate system is not at
[37:05] now the the coordinate system is not at
[37:05] now the the coordinate system is not at the very center of the mass of the part
[37:07] the very center of the mass of the part
[37:07] the very center of the mass of the part anymore because and that communicates I
[37:09] anymore because and that communicates I
[37:09] anymore because and that communicates I mean that's evidence that this design
[37:13] mean that's evidence that this design
[37:13] mean that's evidence that this design focuses on the the
[37:15] focuses on the the
[37:15] focuses on the the first right hand the second one is only
[37:19] first right hand the second one is only
[37:19] first right hand the second one is only a copy of
[37:20] a copy of
[37:20] a copy of that Um, and then the the Why are we
[37:27] that Um, and then the the Why are we
[37:27] that Um, and then the the Why are we Well, okay. Along with the Z-axis of the
[37:30] Well, okay. Along with the Z-axis of the
[37:30] Well, okay. Along with the Z-axis of the print. I wish this would display more
[37:32] print. I wish this would display more
[37:32] print. I wish this would display more nicely. I don't know why it shows up
[37:33] nicely. I don't know why it shows up
[37:33] nicely. I don't know why it shows up like that. If anyone knows, please tell
[37:35] like that. If anyone knows, please tell
[37:35] like that. If anyone knows, please tell me. Um, now we have
[37:43] the cleanup. Oh, that's an empty folder.
[37:43] the cleanup. Oh, that's an empty folder. Still not a perfect model. Um, you
[37:45] Still not a perfect model. Um, you
[37:45] Still not a perfect model. Um, you should be able to see what is the
[37:47] should be able to see what is the
[37:47] should be able to see what is the designer doing. And I've made it into
[37:50] designer doing. And I've made it into
[37:50] designer doing. And I've made it into folders so that it's not just one uh not
[37:53] folders so that it's not just one uh not
[37:53] folders so that it's not just one uh not just features that have names but also
[37:54] just features that have names but also
[37:54] just features that have names but also their groups have names and it's easier
[37:57] their groups have names and it's easier
[37:57] their groups have names and it's easier when there are dependencies. They
[37:58] when there are dependencies. They
[37:58] when there are dependencies. They usually take place inside of the folder
[38:01] usually take place inside of the folder
[38:01] usually take place inside of the folder itself. This is nothing more. These
[38:03] itself. This is nothing more. These
[38:03] itself. This is nothing more. These folders don't change the model at all.
[38:05] folders don't change the model at all.
[38:05] folders don't change the model at all. They are just for the organization of
[38:08] They are just for the organization of
[38:08] They are just for the organization of for the designers. Um and so you'll see
[38:11] for the designers. Um and so you'll see
[38:11] for the designers. Um and so you'll see a chamfer or something that only takes
[38:13] a chamfer or something that only takes
[38:13] a chamfer or something that only takes place and only can take place after a
[38:15] place and only can take place after a
[38:16] place and only can take place after a certain feature is made.
[38:18] certain feature is made.
[38:18] certain feature is made. And then when I put this in a folder
[38:22] And then when I put this in a folder
[38:22] And then when I put this in a folder then someone is not trying to move uh
[38:25] then someone is not trying to move uh
[38:25] then someone is not trying to move uh features of a model in the model tree to
[38:29] features of a model in the model tree to
[38:29] features of a model in the model tree to suppress something that's required to
[38:31] suppress something that's required to
[38:31] suppress something that's required to make another feature. We have we have
[38:33] make another feature. We have we have
[38:33] make another feature. We have we have continuity from top to bottom. Um okay
[38:39] continuity from top to bottom. Um okay
[38:39] continuity from top to bottom. Um okay joint we're champing the
[38:41] joint we're champing the
[38:41] joint we're champing the joints. We add this I'm calling this
[38:44] joints. We add this I'm calling this
[38:44] joints. We add this I'm calling this pivot body and this fixed body. These
[38:46] pivot body and this fixed body. These
[38:46] pivot body and this fixed body. These are the assets that
[38:49] are the assets that
[38:49] are the assets that wh okay. So before we add that body,
[38:53] wh okay. So before we add that body,
[38:53] wh okay. So before we add that body, it's just a hinge. Then we say what kind
[38:56] it's just a hinge. Then we say what kind
[38:56] it's just a hinge. Then we say what kind of geometry is going to sit on this
[38:58] of geometry is going to sit on this
[38:58] of geometry is going to sit on this right hand that decides how we're going
[39:01] right hand that decides how we're going
[39:01] right hand that decides how we're going to um how we're going to m it to the
[39:04] to um how we're going to m it to the
[39:04] to um how we're going to m it to the next thing in the assembly. And then
[39:06] next thing in the assembly. And then
[39:06] next thing in the assembly. And then that gets built. Um it includes also
[39:11] that gets built. Um it includes also
[39:11] that gets built. Um it includes also this fastener here because we want
[39:15] this fastener here because we want
[39:15] this fastener here because we want We want to be able to disassemble the
[39:19] We want to be able to disassemble the
[39:19] We want to be able to disassemble the hinge and then place a screw in here and
[39:21] hinge and then place a screw in here and
[39:21] hinge and then place a screw in here and then mount it out to in this direction.
[39:24] then mount it out to in this direction.
[39:24] then mount it out to in this direction. This direction to another solid uh
[39:29] This direction to another solid uh
[39:29] This direction to another solid uh component. Okay. And
[39:32] component. Okay. And
[39:32] component. Okay. And then but that's optional. The whole
[39:34] then but that's optional. The whole
[39:34] then but that's optional. The whole thing could be glued with cyanoacrylate
[39:37] thing could be glued with cyanoacrylate
[39:37] thing could be glued with cyanoacrylate and CA glue and then permanently fixed
[39:39] and CA glue and then permanently fixed
[39:39] and CA glue and then permanently fixed if the other material is in this case
[39:43] if the other material is in this case
[39:43] if the other material is in this case the black plastic is not compatible with
[39:48] the black plastic is not compatible with
[39:48] the black plastic is not compatible with CA glue. It's kind of glue proof and
[39:50] CA glue. It's kind of glue proof and
[39:50] CA glue. It's kind of glue proof and that's when we include the the screw to
[39:53] that's when we include the the screw to
[39:53] that's when we include the the screw to fasten it. All decisions that give you
[39:57] fasten it. All decisions that give you
[39:57] fasten it. All decisions that give you the customization that you want.
[40:10] So in finishing we have the version
[40:10] So in finishing we have the version number and this is manually updated. You
[40:14] number and this is manually updated. You
[40:14] number and this is manually updated. You can see
[40:16] can see
[40:16] can see uh sorry I'll edit the
[40:19] uh sorry I'll edit the
[40:19] uh sorry I'll edit the sketch SK version means it's the sketch
[40:23] sketch SK version means it's the sketch
[40:23] sketch SK version means it's the sketch for the version. SK is my my prefix for
[40:26] for the version. SK is my my prefix for
[40:26] for the version. SK is my my prefix for sketches. So I define those so they're
[40:28] sketches. So I define those so they're
[40:28] sketches. So I define those so they're easy to find. um edit sketch and then
[40:31] easy to find. um edit sketch and then
[40:31] easy to find. um edit sketch and then you'll see the the text here. If you
[40:34] you'll see the the text here. If you
[40:34] you'll see the the text here. If you double click the text, then you can go
[40:36] double click the text, then you can go
[40:36] double click the text, then you can go in and you can adjust it. Um but you'll
[40:39] in and you can adjust it. Um but you'll
[40:39] in and you can adjust it. Um but you'll find this in the same way for all of my
[40:42] find this in the same way for all of my
[40:42] find this in the same way for all of my uh all my models will have the same
[40:44] uh all my models will have the same
[40:44] uh all my models will have the same font, the same height, same orientation
[40:47] font, the same height, same orientation
[40:47] font, the same height, same orientation with respect to the print. And so yeah,
[40:51] with respect to the print. And so yeah,
[40:51] with respect to the print. And so yeah, the my models as it stands right now are
[40:54] the my models as it stands right now are
[40:54] the my models as it stands right now are kind of a library for uh newer CAD
[40:57] kind of a library for uh newer CAD
[40:57] kind of a library for uh newer CAD designers to gain

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
