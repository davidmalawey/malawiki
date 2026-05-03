---
title: "Design for Manufacturing: Polymer FDM [Part 1]"
url: "https://www.youtube.com/watch?v=HYnm2MD0Nks"
video_id: "HYnm2MD0Nks"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2022-06-20
duration: "11:54"
duration_sec: 714
views: 841
likes: 32
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/HYnm2MD0Nks/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 569
chapters_count: 10
has_description: true
has_comments: false
---

## Description

Tips & rules of thumb for designing for additive manufacturing (3D Printing)

0:00 What is DFM?
0:45 Overhangs
2:39 Mininum wall thickness
3:12 Path Width
4:28 Max hole size
5:42 debossed labels
6:35 label fonts
6:56 fine tolerances
9:49 minimize points of contact
10:43 tolerance rule of thumb

## Chapters

- 0:00 What is DFM?
- 0:45 Overhangs
- 2:39 Mininum wall thickness
- 3:12 Path Width
- 4:28 Max hole size
- 5:42 debossed labels
- 6:35 label fonts
- 6:56 fine tolerances
- 9:49 minimize points of contact
- 10:43 tolerance rule of thumb

## Transcript

[0:05] the very first and most important tip is
[0:05] the very first and most important tip is when you design a part for printing you
[0:07] when you design a part for printing you
[0:07] when you design a part for printing you consider that there's directionality to
[0:10] consider that there's directionality to
[0:10] consider that there's directionality to the print and the gravity is working
[0:12] the print and the gravity is working
[0:12] the print and the gravity is working against you so you want to create a part
[0:15] against you so you want to create a part
[0:15] against you so you want to create a part that does not have overhangs where an
[0:17] that does not have overhangs where an
[0:17] that does not have overhangs where an unsupported region of the part will
[0:20] unsupported region of the part will
[0:20] unsupported region of the part will require supports or it will be printing
[0:22] require supports or it will be printing
[0:22] require supports or it will be printing over thin air as the nozzle moves around
[0:26] over thin air as the nozzle moves around
[0:26] over thin air as the nozzle moves around the nozzle will look like this
[0:28] the nozzle will look like this
[0:28] the nozzle will look like this and it's traveling around layer by layer
[0:31] and it's traveling around layer by layer
[0:31] and it's traveling around layer by layer starting from the first one
[0:33] starting from the first one
[0:33] starting from the first one depositing
[0:34] depositing
[0:34] depositing melted plastic
[0:36] melted plastic
[0:36] melted plastic once on top of another
[0:38] once on top of another
[0:38] once on top of another as it builds the part
[0:40] as it builds the part
[0:40] as it builds the part so the best way to make the part
[0:43] so the best way to make the part
[0:43] so the best way to make the part difficult or come out poorly is
[0:46] difficult or come out poorly is
[0:46] difficult or come out poorly is to
[0:47] to
[0:47] to have a design that requires this
[0:49] have a design that requires this
[0:49] have a design that requires this overhang something like this ceiling
[0:51] overhang something like this ceiling
[0:51] overhang something like this ceiling here
[0:51] here
[0:51] here that is going to need
[0:54] that is going to need
[0:54] that is going to need extra support and extra effort on the
[0:57] extra support and extra effort on the
[0:57] extra support and extra effort on the person that's manufacturing it so if we
[1:00] person that's manufacturing it so if we
[1:00] person that's manufacturing it so if we generate supports here and click like
[1:02] generate supports here and click like
[1:02] generate supports here and click like that
[1:03] that
[1:03] that it's going to automatically generate
[1:04] it's going to automatically generate
[1:04] it's going to automatically generate them
[1:05] them
[1:05] them if we go ahead and prepare the print
[1:07] if we go ahead and prepare the print
[1:07] if we go ahead and prepare the print it's going to create all this extra
[1:09] it's going to create all this extra
[1:09] it's going to create all this extra infill
[1:10] infill
[1:10] infill these are support materials that are
[1:13] these are support materials that are
[1:13] these are support materials that are added as extra plastic to support the
[1:15] added as extra plastic to support the
[1:15] added as extra plastic to support the overhanging regions
[1:17] overhanging regions
[1:17] overhanging regions and
[1:18] and
[1:18] and our job as designers in any given
[1:21] our job as designers in any given
[1:21] our job as designers in any given manufacturing process should be that we
[1:23] manufacturing process should be that we
[1:23] manufacturing process should be that we consider the design
[1:26] consider the design
[1:26] consider the design how the design is going to be
[1:27] how the design is going to be
[1:27] how the design is going to be manufactured and the constraints
[1:28] manufactured and the constraints
[1:28] manufactured and the constraints associated with that
[1:31] associated with that
[1:31] associated with that manufacturing process that means
[1:33] manufacturing process that means
[1:34] manufacturing process that means our very first job as designing for 3d
[1:37] our very first job as designing for 3d
[1:37] our very first job as designing for 3d printing is that we're going to consider
[1:39] printing is that we're going to consider
[1:39] printing is that we're going to consider the constraints involved
[1:41] the constraints involved
[1:41] the constraints involved and try to eliminate the supports
[1:43] and try to eliminate the supports
[1:43] and try to eliminate the supports and that might can that might sound like
[1:46] and that might can that might sound like
[1:46] and that might can that might sound like an extra burden to always be considering
[1:48] an extra burden to always be considering
[1:48] an extra burden to always be considering the the build direction but actually
[1:51] the the build direction but actually
[1:51] the the build direction but actually it's pretty well aligned with other
[1:53] it's pretty well aligned with other
[1:53] it's pretty well aligned with other manufacturing methods where we also have
[1:56] manufacturing methods where we also have
[1:56] manufacturing methods where we also have major constraints to consider that
[1:59] major constraints to consider that
[1:59] major constraints to consider that happens with
[2:00] happens with
[2:00] happens with cnc machining with blind features that
[2:02] cnc machining with blind features that
[2:02] cnc machining with blind features that happens with
[2:04] happens with
[2:04] happens with injection molding
[2:05] injection molding
[2:05] injection molding and it happens with
[2:07] and it happens with
[2:07] and it happens with stamping for sure pretty much any
[2:09] stamping for sure pretty much any
[2:09] stamping for sure pretty much any manufacturing process can be made vastly
[2:12] manufacturing process can be made vastly
[2:12] manufacturing process can be made vastly more difficult or impossible
[2:15] more difficult or impossible
[2:15] more difficult or impossible and if certainly costly if the designer
[2:18] and if certainly costly if the designer
[2:18] and if certainly costly if the designer doesn't take into consideration what is
[2:20] doesn't take into consideration what is
[2:20] doesn't take into consideration what is the manufacturing process that will be
[2:22] the manufacturing process that will be
[2:22] the manufacturing process that will be used so we can do the same thing with 3d
[2:25] used so we can do the same thing with 3d
[2:25] used so we can do the same thing with 3d printing and we can make our parts much
[2:27] printing and we can make our parts much
[2:27] printing and we can make our parts much more rapidly made easily made and made
[2:30] more rapidly made easily made and made
[2:30] more rapidly made easily made and made with a with a low-cost machine inside of
[2:33] with a with a low-cost machine inside of
[2:33] with a with a low-cost machine inside of the building instead of having to use
[2:35] the building instead of having to use
[2:35] the building instead of having to use the very very expensive 3d printers
[2:39] the very very expensive 3d printers
[2:39] the very very expensive 3d printers try to use a minimum wall thickness of
[2:42] try to use a minimum wall thickness of
[2:42] try to use a minimum wall thickness of 1.5 millimeters maybe even 2 millimeters
[2:47] 1.5 millimeters maybe even 2 millimeters
[2:47] 1.5 millimeters maybe even 2 millimeters you can see in here the sketch has these
[2:50] you can see in here the sketch has these
[2:50] you can see in here the sketch has these walls defined at 1.5
[3:01] this is how the part flexes
[3:01] this is how the part flexes at 1.5 millimeters thickness
[3:04] at 1.5 millimeters thickness
[3:04] at 1.5 millimeters thickness most nozzles for common 3d printers are
[3:07] most nozzles for common 3d printers are
[3:07] most nozzles for common 3d printers are 0.4 millimeters
[3:09] 0.4 millimeters
[3:09] 0.4 millimeters hole diameter
[3:16] when you input import your part into a
[3:16] when you input import your part into a slicer then
[3:19] slicer then
[3:19] slicer then the
[3:19] the
[3:19] the setting for
[3:21] setting for
[3:21] setting for the
[3:22] the
[3:22] the diameter will be here and then you'll
[3:24] diameter will be here and then you'll
[3:24] diameter will be here and then you'll also have an extrusion width which
[3:26] also have an extrusion width which
[3:26] also have an extrusion width which usually gives it a little bit of squish
[3:28] usually gives it a little bit of squish
[3:28] usually gives it a little bit of squish so the width of the laid down plastic is
[3:31] so the width of the laid down plastic is
[3:31] so the width of the laid down plastic is a little bit wider than the width of the
[3:34] a little bit wider than the width of the
[3:34] a little bit wider than the width of the nozzle or sometimes it's the same
[3:36] nozzle or sometimes it's the same
[3:36] nozzle or sometimes it's the same the default might be 0.4 for yours
[3:40] the default might be 0.4 for yours
[3:40] the default might be 0.4 for yours and when you generate your print you're
[3:42] and when you generate your print you're
[3:42] and when you generate your print you're going to see
[3:43] going to see
[3:43] going to see that
[3:44] that
[3:44] that there's
[3:45] there's
[3:45] there's one two
[3:47] one two
[3:47] one two two walls that's going to make up um
[3:52] two walls that's going to make up um
[3:52] two walls that's going to make up um the two walls will make up 0.8
[3:54] the two walls will make up 0.8
[3:54] the two walls will make up 0.8 sorry in my case it's 0.88 and then
[3:57] sorry in my case it's 0.88 and then
[3:57] sorry in my case it's 0.88 and then whatever is in the middle is being
[3:59] whatever is in the middle is being
[3:59] whatever is in the middle is being filled in with some given pattern and in
[4:02] filled in with some given pattern and in
[4:02] filled in with some given pattern and in some cases
[4:03] some cases
[4:03] some cases your wall thickness could force the
[4:05] your wall thickness could force the
[4:05] your wall thickness could force the slicer to avoid this space altogether if
[4:09] slicer to avoid this space altogether if
[4:09] slicer to avoid this space altogether if you don't allow enough space for a third
[4:11] you don't allow enough space for a third
[4:11] you don't allow enough space for a third path and it's only a fraction of a path
[4:14] path and it's only a fraction of a path
[4:14] path and it's only a fraction of a path then you would end up with a hollow wall
[4:16] then you would end up with a hollow wall
[4:16] then you would end up with a hollow wall which would be much
[4:18] which would be much
[4:18] which would be much much weaker because you would not have
[4:20] much weaker because you would not have
[4:20] much weaker because you would not have you really need the adhesion between the
[4:22] you really need the adhesion between the
[4:22] you really need the adhesion between the inside and the outside wall to have any
[4:24] inside and the outside wall to have any
[4:24] inside and the outside wall to have any strength
[4:31] to avoid supports when you're making
[4:31] to avoid supports when you're making holes in the vertical plane then uh
[4:33] holes in the vertical plane then uh
[4:34] holes in the vertical plane then uh small diameters are acceptable like
[4:35] small diameters are acceptable like
[4:36] small diameters are acceptable like three millimeters is okay
[4:38] three millimeters is okay
[4:38] three millimeters is okay but after
[4:39] but after
[4:39] but after about six millimeters the ceiling of the
[4:41] about six millimeters the ceiling of the
[4:41] about six millimeters the ceiling of the hole will fail to perform and you'll
[4:44] hole will fail to perform and you'll
[4:44] hole will fail to perform and you'll need supports
[4:45] need supports
[4:45] need supports so
[4:46] so
[4:46] so the way this looks here
[4:48] the way this looks here
[4:48] the way this looks here is like that
[4:50] is like that
[4:50] is like that you can see that the bottom of the hole
[4:53] you can see that the bottom of the hole
[4:53] you can see that the bottom of the hole comes out
[4:54] comes out
[4:54] comes out pretty accurately but the top
[4:56] pretty accurately but the top
[4:56] pretty accurately but the top has uh begins to deteriorate
[4:59] has uh begins to deteriorate
[4:59] has uh begins to deteriorate with the hangover
[5:01] with the hangover
[5:01] with the hangover sorry overhang
[5:03] sorry overhang
[5:03] sorry overhang this is benchy which is a very common
[5:05] this is benchy which is a very common
[5:05] this is benchy which is a very common benchmark type of print it's not a
[5:08] benchmark type of print it's not a
[5:08] benchmark type of print it's not a perfect one but this overhang feature if
[5:11] perfect one but this overhang feature if
[5:11] perfect one but this overhang feature if you choose not to build any supports
[5:14] you choose not to build any supports
[5:14] you choose not to build any supports it's very common to get it looking like
[5:16] it's very common to get it looking like
[5:16] it's very common to get it looking like that
[5:17] that
[5:17] that and the width
[5:19] and the width
[5:19] and the width i would say it's not quite acceptable
[5:21] i would say it's not quite acceptable
[5:21] i would say it's not quite acceptable the width there
[5:26] is
[5:26] is about nine millimeters
[5:28] about nine millimeters
[5:28] about nine millimeters so
[5:28] so
[5:28] so one other solution when you have a large
[5:31] one other solution when you have a large
[5:31] one other solution when you have a large hole is to put a if it was a circle put
[5:34] hole is to put a if it was a circle put
[5:34] hole is to put a if it was a circle put a teardrop shape so it comes to a point
[5:37] a teardrop shape so it comes to a point
[5:37] a teardrop shape so it comes to a point and then you get a really nice build
[5:39] and then you get a really nice build
[5:39] and then you get a really nice build quality without any
[5:41] quality without any
[5:41] quality without any supports
[5:43] supports
[5:43] supports if you want to make labels
[5:45] if you want to make labels
[5:45] if you want to make labels we recommend using a
[5:48] we recommend using a
[5:48] we recommend using a a dbos instead of emboss so that means
[5:51] a dbos instead of emboss so that means
[5:51] a dbos instead of emboss so that means the part the label is cut into the
[5:53] the part the label is cut into the
[5:53] the part the label is cut into the plastic
[5:54] plastic
[5:54] plastic instead of protruding outward
[5:57] instead of protruding outward
[5:57] instead of protruding outward for the cleanest look
[5:59] for the cleanest look
[5:59] for the cleanest look and
[6:00] and
[6:00] and the depth
[6:02] the depth
[6:02] the depth a good
[6:03] a good
[6:03] a good depth to make it show up is 0.5
[6:06] depth to make it show up is 0.5
[6:06] depth to make it show up is 0.5 millimeters
[6:08] millimeters
[6:08] millimeters that's um a little bit more than one
[6:11] that's um a little bit more than one
[6:11] that's um a little bit more than one thickness of a of an extrusion width so
[6:13] thickness of a of an extrusion width so
[6:13] thickness of a of an extrusion width so it's sure to show up
[6:20] here's how the label looks at 0.5
[6:20] here's how the label looks at 0.5 millimeter depth
[6:22] millimeter depth
[6:22] millimeter depth and this is actually a little bit rushed
[6:24] and this is actually a little bit rushed
[6:24] and this is actually a little bit rushed you can see the ringing
[6:26] you can see the ringing
[6:26] you can see the ringing in the font if you slow down the speed
[6:28] in the font if you slow down the speed
[6:28] in the font if you slow down the speed of your printing you can make it look uh
[6:31] of your printing you can make it look uh
[6:31] of your printing you can make it look uh much nicer
[6:34] much nicer
[6:34] much nicer when you deboss this font like this you
[6:37] when you deboss this font like this you
[6:37] when you deboss this font like this you can you can impact the strength of your
[6:40] can you can impact the strength of your
[6:40] can you can impact the strength of your component but as you see here if you
[6:42] component but as you see here if you
[6:42] component but as you see here if you choose a a thin depth like 0.5
[6:46] choose a a thin depth like 0.5
[6:46] choose a a thin depth like 0.5 millimeters then we don't have too much
[6:48] millimeters then we don't have too much
[6:48] millimeters then we don't have too much loss of material along this wall
[6:56] once in a while you might need to have a
[6:56] once in a while you might need to have a fine tolerance like this cap
[6:59] fine tolerance like this cap
[6:59] fine tolerance like this cap that has a snug fit
[7:01] that has a snug fit
[7:01] that has a snug fit on the tube
[7:02] on the tube
[7:02] on the tube okay but you should only assume that you
[7:05] okay but you should only assume that you
[7:05] okay but you should only assume that you can achieve
[7:06] can achieve
[7:06] can achieve 0.3 millimeters tolerance
[7:09] 0.3 millimeters tolerance
[7:10] 0.3 millimeters tolerance on any dimension for your printer here's
[7:12] on any dimension for your printer here's
[7:12] on any dimension for your printer here's why
[7:13] why
[7:13] why when your printer lays down the
[7:16] when your printer lays down the
[7:16] when your printer lays down the extrusion
[7:18] extrusion
[7:18] extrusion the extruded plastic is going to have
[7:20] the extruded plastic is going to have
[7:20] the extruded plastic is going to have some squish it's absolutely necessary
[7:23] some squish it's absolutely necessary
[7:23] some squish it's absolutely necessary for layers to adhese from one to the
[7:25] for layers to adhese from one to the
[7:25] for layers to adhese from one to the next one below it
[7:27] next one below it
[7:27] next one below it and so
[7:28] and so
[7:28] and so the the width of this squish is going to
[7:32] the the width of this squish is going to
[7:32] the the width of this squish is going to create this uh well in this case it's a
[7:35] create this uh well in this case it's a
[7:35] create this uh well in this case it's a pattern
[7:36] pattern
[7:36] pattern of ins and outs
[7:38] of ins and outs
[7:38] of ins and outs that shows up on the surface of your
[7:40] that shows up on the surface of your
[7:40] that shows up on the surface of your part and the thickness of this
[7:44] part and the thickness of this
[7:44] part and the thickness of this will be related to
[7:46] will be related to
[7:46] will be related to the height of your layer
[7:54] where in this case our layer is
[7:54] where in this case our layer is 0.3 millimeters
[7:57] 0.3 millimeters
[7:57] 0.3 millimeters i i like to print at point three many
[7:59] i i like to print at point three many
[7:59] i i like to print at point three many people print around point two as a
[8:01] people print around point two as a
[8:01] people print around point two as a default
[8:02] default
[8:02] default um on most slicers
[8:05] um on most slicers
[8:05] um on most slicers let's pretend each one of these
[8:08] let's pretend each one of these
[8:08] let's pretend each one of these bubbles
[8:10] bubbles
[8:10] bubbles is an extrusion path going into the
[8:12] is an extrusion path going into the
[8:12] is an extrusion path going into the board this is the base
[8:15] board this is the base
[8:15] board this is the base this is the plate
[8:16] this is the plate
[8:16] this is the plate of the printer
[8:18] of the printer
[8:18] of the printer so what we just measured was
[8:33] and let's look closer
[8:33] and let's look closer let's look at this zone here
[8:45] so we have
[8:46] one
[8:46] one two
[8:47] two
[8:47] two three
[8:48] three
[8:48] three four
[8:50] four
[8:50] four and our
[8:51] and our
[8:51] and our design was 1.5
[8:54] design was 1.5
[8:54] design was 1.5 millimeters so we have
[8:56] millimeters so we have
[8:56] millimeters so we have 0.25
[9:02] excess
[9:02] excess which means
[9:03] which means
[9:03] which means 0.125
[9:08] over overbuilt
[9:08] over overbuilt on each side
[9:09] on each side
[9:10] on each side so this is the
[9:11] so this is the
[9:11] so this is the plus
[9:12] plus
[9:12] plus in regards to tolerance
[9:14] in regards to tolerance
[9:14] in regards to tolerance so that means somewhere in here
[9:18] so that means somewhere in here
[9:18] so that means somewhere in here we have the design
[9:25] the designed wall was here on this
[9:25] the designed wall was here on this dotted line and somewhere outside the
[9:27] dotted line and somewhere outside the
[9:27] dotted line and somewhere outside the designed wall
[9:29] designed wall
[9:29] designed wall is where we built to
[9:31] is where we built to
[9:31] is where we built to and this distance here
[9:34] and this distance here
[9:34] and this distance here is 0.125
[9:37] is 0.125
[9:37] is 0.125 i'd say that's pretty accurate and
[9:40] i'd say that's pretty accurate and
[9:40] i'd say that's pretty accurate and you could ask your printer to achieve
[9:42] you could ask your printer to achieve
[9:42] you could ask your printer to achieve better
[9:43] better
[9:43] better but we're not designing for what we can
[9:46] but we're not designing for what we can
[9:46] but we're not designing for what we can achieve we're designing for what we can
[9:48] achieve we're designing for what we can
[9:48] achieve we're designing for what we can readily achieve
[9:51] readily achieve
[9:51] readily achieve what's better than relying on a tight
[9:53] what's better than relying on a tight
[9:53] what's better than relying on a tight tolerance for a design like this one is
[9:56] tolerance for a design like this one is
[9:56] tolerance for a design like this one is okay we need that snug fit
[9:59] okay we need that snug fit
[9:59] okay we need that snug fit but
[10:00] but
[10:00] but if you printed
[10:02] if you printed
[10:02] if you printed it slightly too large you're going to
[10:04] it slightly too large you're going to
[10:04] it slightly too large you're going to have to reprint and if you printed it
[10:06] have to reprint and if you printed it
[10:06] have to reprint and if you printed it too small you'll have to sand out this
[10:08] too small you'll have to sand out this
[10:08] too small you'll have to sand out this entire surface or maybe just reprint
[10:11] entire surface or maybe just reprint
[10:12] entire surface or maybe just reprint so what do we do
[10:13] so what do we do
[10:14] so what do we do just make three contact points and and
[10:16] just make three contact points and and
[10:16] just make three contact points and and uh we use this feature adding in this
[10:19] uh we use this feature adding in this
[10:19] uh we use this feature adding in this bump
[10:20] bump
[10:20] bump and there's three of them
[10:22] and there's three of them
[10:22] and there's three of them so the part maintains its center
[10:25] so the part maintains its center
[10:25] so the part maintains its center and it also
[10:27] and it also
[10:27] and it also we have the opportunity to just uh
[10:30] we have the opportunity to just uh
[10:30] we have the opportunity to just uh overbuild these bumps and sand them down
[10:33] overbuild these bumps and sand them down
[10:33] overbuild these bumps and sand them down if they if they come out too large we
[10:35] if they if they come out too large we
[10:35] if they if they come out too large we can just file down on that on those
[10:37] can just file down on that on those
[10:37] can just file down on that on those zones instead of trying to sand the
[10:39] zones instead of trying to sand the
[10:39] zones instead of trying to sand the whole inner surface
[10:42] whole inner surface
[10:42] whole inner surface so the rule of thumb is you measure your
[10:45] so the rule of thumb is you measure your
[10:45] so the rule of thumb is you measure your part let's say like this blue tube and
[10:47] part let's say like this blue tube and
[10:48] part let's say like this blue tube and then you want to make a mating part
[10:49] then you want to make a mating part
[10:49] then you want to make a mating part we're not talking about a press fit and
[10:52] we're not talking about a press fit and
[10:52] we're not talking about a press fit and we're not talking about a loose
[10:54] we're not talking about a loose
[10:54] we're not talking about a loose clearance fit actually we're just saying
[10:56] clearance fit actually we're just saying
[10:56] clearance fit actually we're just saying what is the minimum
[10:58] what is the minimum
[10:58] what is the minimum to achieve clearance so that your parts
[11:01] to achieve clearance so that your parts
[11:01] to achieve clearance so that your parts go together and that rule of thumb is
[11:04] go together and that rule of thumb is
[11:04] go together and that rule of thumb is 0.3 millimeters so
[11:06] 0.3 millimeters so
[11:06] 0.3 millimeters so if the inside diameter of this blue tube
[11:09] if the inside diameter of this blue tube
[11:09] if the inside diameter of this blue tube was 100 millimeters
[11:11] was 100 millimeters
[11:11] was 100 millimeters then you would design the exterior of
[11:14] then you would design the exterior of
[11:14] then you would design the exterior of your gray
[11:15] your gray
[11:15] your gray cap
[11:16] cap
[11:16] cap here at this interface you would make
[11:19] here at this interface you would make
[11:19] here at this interface you would make that
[11:19] that
[11:20] that 100 minus
[11:21] 100 minus
[11:21] 100 minus 0.3 millimeters on each side and pretty
[11:24] 0.3 millimeters on each side and pretty
[11:24] 0.3 millimeters on each side and pretty much anybody that you send this print
[11:26] much anybody that you send this print
[11:26] much anybody that you send this print out to it's gonna it's gonna fit
[11:29] out to it's gonna it's gonna fit
[11:29] out to it's gonna it's gonna fit and
[11:29] and
[11:30] and then the the looseness will be another
[11:32] then the the looseness will be another
[11:32] then the the looseness will be another factor you can look up press fits and
[11:35] factor you can look up press fits and
[11:35] factor you can look up press fits and clearance fits
[11:37] clearance fits
[11:37] clearance fits in design guides online those ones have
[11:40] in design guides online those ones have
[11:40] in design guides online those ones have been around for
[11:41] been around for
[11:41] been around for many decades
[11:43] many decades
[11:43] many decades but 0.3 here is going to give you the
[11:47] but 0.3 here is going to give you the
[11:47] but 0.3 here is going to give you the the fitment so it enters without
[11:50] the fitment so it enters without
[11:50] the fitment so it enters without interference of the blue part

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
