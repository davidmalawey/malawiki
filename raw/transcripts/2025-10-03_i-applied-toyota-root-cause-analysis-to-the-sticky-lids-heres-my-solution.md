---
title: "I applied Toyota Root Cause Analysis to the sticky lids - Here's my solution"
url: "https://www.youtube.com/watch?v=IvZXdxWh7dg"
video_id: "IvZXdxWh7dg"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-10-03
duration: "20:18"
duration_sec: 1218
views: 6335
likes: 355
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/IvZXdxWh7dg/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 886
chapters_count: 9
has_description: true
has_comments: false
---

## Description

Why do these metal lids always get stuck? In this video I demonstrate root-cause-analysis for the overly tight lids and leaky canisters.  See my observations, testing, design of a solution, and behaviors updated before open-sourcing a design. The story is a problem with the caps on pvc glue and other chemicals, and the solution is an extra grip, printable, for all the cans in the lab.  See the initial solution, my checking back, and my improvements.  Now, all my fluids last 2x longer.  I tighten the caps better with an easy design called "grip", and now it's open source.  Ultimately I encourage all the engineers to solve our old problems and distribute solutions so we can climb out of the 1800s with our society. 

[LESSONS]
► an example of root-cause-analysis from Toyota Business Practice.
► how to publish an open-source hardware design
► what is the root cause of a stuck cap?
► what makes a parametric model advantageous over regular CAD?
► who can benefit from an open hardware design?
► why common businesses must compete with FREE now
► why would an engineer waste time on a cap grip design?

[LINKS]
OpenLab Project ► qr.net/openlabproject
CAD model "Grip" ► https://grabcad.com/library/grip-22

[CHAPTERS]
0:00 root cause analysis
3:22 countermeasure
04:20 plan-do-check-act
5:52 adjusted method
7:22 published value
11:28 extended value
14:38 duplicating solution
16:45 business value
19:03 engineers must ACT

## Chapters

- 0:00 root cause analysis
- 3:22 countermeasure
- 4:20 plan-do-check-act
- 5:52 adjusted method
- 7:22 published value
- 11:28 extended value
- 14:38 duplicating solution
- 16:45 business value
- 19:03 engineers must ACT

## Transcript

[0:03] So last year I lost about $100 worth of
[0:03] So last year I lost about $100 worth of materials. They were all fluid materials
[0:05] materials. They were all fluid materials
[0:05] materials. They were all fluid materials that had gone bad. And so I did a little
[0:08] that had gone bad. And so I did a little
[0:08] that had gone bad. And so I did a little investigating about why they're gone
[0:10] investigating about why they're gone
[0:10] investigating about why they're gone bad. And it's related to the ceiling of
[0:14] bad. And it's related to the ceiling of
[0:14] bad. And it's related to the ceiling of the fluid and the vapors at the top at
[0:16] the fluid and the vapors at the top at
[0:16] the fluid and the vapors at the top at the at the cap.
[0:19] the at the cap.
[0:19] the at the cap. I performed a little bit of root
[0:20] I performed a little bit of root
[0:20] I performed a little bit of root [clears throat] cause analysis and I'll
[0:23] [clears throat] cause analysis and I'll
[0:23] [clears throat] cause analysis and I'll just give you a sample of that. So, I
[0:25] just give you a sample of that. So, I
[0:25] just give you a sample of that. So, I noticed that one of these other
[0:27] noticed that one of these other
[0:27] noticed that one of these other substances, the the cap was not so tight
[0:31] substances, the the cap was not so tight
[0:31] substances, the the cap was not so tight that it performs sealing and sometimes
[0:35] that it performs sealing and sometimes
[0:35] that it performs sealing and sometimes it requires me to put it on very
[0:37] it requires me to put it on very
[0:37] it requires me to put it on very tightly. Uh so maybe on occasions the
[0:42] tightly. Uh so maybe on occasions the
[0:42] tightly. Uh so maybe on occasions the tightness is higher than I can even do
[0:45] tightness is higher than I can even do
[0:45] tightness is higher than I can even do with my hand. Okay. And so then I'm
[0:48] with my hand. Okay. And so then I'm
[0:48] with my hand. Okay. And so then I'm asking in what occasions is it requiring
[0:52] asking in what occasions is it requiring
[0:52] asking in what occasions is it requiring this very strong tightening force and
[0:55] this very strong tightening force and
[0:56] this very strong tightening force and one of those occasions is when there's
[0:58] one of those occasions is when there's
[0:58] one of those occasions is when there's debris that is accumulated on those
[1:01] debris that is accumulated on those
[1:01] debris that is accumulated on those threads. Okay. Um, and then I explored
[1:05] threads. Okay. Um, and then I explored
[1:05] threads. Okay. Um, and then I explored across many bottles in which cases does
[1:09] across many bottles in which cases does
[1:09] across many bottles in which cases does the debris I'm always uh attempting to
[1:12] the debris I'm always uh attempting to
[1:12] the debris I'm always uh attempting to be clean and neat and systematic, but in
[1:15] be clean and neat and systematic, but in
[1:15] be clean and neat and systematic, but in some cases it accumulates more than
[1:17] some cases it accumulates more than
[1:17] some cases it accumulates more than others. And here's um something that I
[1:20] others. And here's um something that I
[1:20] others. And here's um something that I noticed. If there is even a tiny bit of
[1:24] noticed. If there is even a tiny bit of
[1:24] noticed. If there is even a tiny bit of um dried fluid on the threads, then it
[1:28] um dried fluid on the threads, then it
[1:28] um dried fluid on the threads, then it rapidly raises the amount of torque you
[1:30] rapidly raises the amount of torque you
[1:30] rapidly raises the amount of torque you need to actually seal it to a close it
[1:33] need to actually seal it to a close it
[1:33] need to actually seal it to a close it to a sealed state. But since we don't
[1:37] to a sealed state. But since we don't
[1:37] to a sealed state. But since we don't know just by looking and feeling if
[1:39] know just by looking and feeling if
[1:39] know just by looking and feeling if we've reached a actual sealed state,
[1:43] we've reached a actual sealed state,
[1:43] we've reached a actual sealed state, then um we would just standard tighten
[1:46] then um we would just standard tighten
[1:46] then um we would just standard tighten it as good as you can while still being
[1:48] it as good as you can while still being
[1:48] it as good as you can while still being able to get it loose. Um okay. So then
[1:52] able to get it loose. Um okay. So then
[1:52] able to get it loose. Um okay. So then there's a if we always tighten it
[1:55] there's a if we always tighten it
[1:55] there's a if we always tighten it nicely, then the sealing happens. If we
[1:58] nicely, then the sealing happens. If we
[1:58] nicely, then the sealing happens. If we fail to seal it, then the little bit of
[2:00] fail to seal it, then the little bit of
[2:00] fail to seal it, then the little bit of liquid that is near and on the edge, the
[2:03] liquid that is near and on the edge, the
[2:03] liquid that is near and on the edge, the thread, the cap, that will harden and
[2:07] thread, the cap, that will harden and
[2:07] thread, the cap, that will harden and interfere even more and make the the
[2:10] interfere even more and make the the
[2:10] interfere even more and make the the gaps worse and make the venting worse,
[2:13] gaps worse and make the venting worse,
[2:13] gaps worse and make the venting worse, causing a whole lot more of that
[2:16] causing a whole lot more of that
[2:16] causing a whole lot more of that nearthread fluid to harden and ex make
[2:21] nearthread fluid to harden and ex make
[2:21] nearthread fluid to harden and ex make the problem exponential. In the world of
[2:24] the problem exponential. In the world of
[2:24] the problem exponential. In the world of PVC glues, this problem is so severe
[2:26] PVC glues, this problem is so severe
[2:26] PVC glues, this problem is so severe that they sell a tool. It's commonly
[2:29] that they sell a tool. It's commonly
[2:29] that they sell a tool. It's commonly recognized and distributed off the
[2:31] recognized and distributed off the
[2:31] recognized and distributed off the shelf. You clamp it onto the lid. You
[2:34] shelf. You clamp it onto the lid. You
[2:34] shelf. You clamp it onto the lid. You squeeze it with these two handles to
[2:35] squeeze it with these two handles to
[2:35] squeeze it with these two handles to enhance the grip and then you turn.
[2:37] enhance the grip and then you turn.
[2:37] enhance the grip and then you turn. Between the activities of just using my
[2:40] Between the activities of just using my
[2:40] Between the activities of just using my hands to tighten and loosen these jars
[2:43] hands to tighten and loosen these jars
[2:43] hands to tighten and loosen these jars between many different jars, when is the
[2:45] between many different jars, when is the
[2:45] between many different jars, when is the occasion that I bust out the tool? That
[2:47] occasion that I bust out the tool? That
[2:47] occasion that I bust out the tool? That is specifically for loosening and not
[2:50] is specifically for loosening and not
[2:50] is specifically for loosening and not for tightening. And so that is a moment
[2:53] for tightening. And so that is a moment
[2:53] for tightening. And so that is a moment to pay attention to. Here's what I
[2:56] to pay attention to. Here's what I
[2:56] to pay attention to. Here's what I learned. As this cap gets messier, then
[2:59] learned. As this cap gets messier, then
[2:59] learned. As this cap gets messier, then it gets harder to put on. Okay, we put
[3:01] it gets harder to put on. Okay, we put
[3:01] it gets harder to put on. Okay, we put it on still and then it cures while it's
[3:04] it on still and then it cures while it's
[3:04] it on still and then it cures while it's sitting and it's harder to come off. So,
[3:07] sitting and it's harder to come off. So,
[3:07] sitting and it's harder to come off. So, there's a certain moment where you need
[3:08] there's a certain moment where you need
[3:08] there's a certain moment where you need to have this tool or some kind of tool.
[3:11] to have this tool or some kind of tool.
[3:11] to have this tool or some kind of tool. And at the moment that you need that
[3:13] And at the moment that you need that
[3:13] And at the moment that you need that tool is the same moment when the debris
[3:17] tool is the same moment when the debris
[3:17] tool is the same moment when the debris has accumulated up to that critical
[3:20] has accumulated up to that critical
[3:20] has accumulated up to that critical point where it's just going to get far
[3:21] point where it's just going to get far
[3:21] point where it's just going to get far worse. If we use this tool only in the
[3:25] worse. If we use this tool only in the
[3:25] worse. If we use this tool only in the situation of removal but not in
[3:28] situation of removal but not in
[3:28] situation of removal but not in replacement
[3:30] replacement
[3:30] replacement then the problem will expand rapidly.
[3:33] then the problem will expand rapidly.
[3:33] then the problem will expand rapidly. Once you reach the point where you need
[3:35] Once you reach the point where you need
[3:35] Once you reach the point where you need this, then you have already got a
[3:38] this, then you have already got a
[3:38] this, then you have already got a substance that is going to expire
[3:40] substance that is going to expire
[3:40] substance that is going to expire rapidly, say 10 times faster than it
[3:43] rapidly, say 10 times faster than it
[3:43] rapidly, say 10 times faster than it would permanently seal. That brought me
[3:45] would permanently seal. That brought me
[3:45] would permanently seal. That brought me to a stage where I implemented a policy.
[3:48] to a stage where I implemented a policy.
[3:48] to a stage where I implemented a policy. I said, I will always use the tool to
[3:50] I said, I will always use the tool to
[3:50] I said, I will always use the tool to tighten the lids, not only to remove
[3:53] tighten the lids, not only to remove
[3:53] tighten the lids, not only to remove them. And then for certain lids, like
[3:55] them. And then for certain lids, like
[3:55] them. And then for certain lids, like this one, this tool doesn't fit. And so
[3:58] this one, this tool doesn't fit. And so
[3:58] this one, this tool doesn't fit. And so I 3D printed an adapter.
[4:01] I 3D printed an adapter.
[4:01] I 3D printed an adapter. because I have the design skills, I can
[4:03] because I have the design skills, I can
[4:03] because I have the design skills, I can do this quickly and easily. So, it's
[4:05] do this quickly and easily. So, it's
[4:05] do this quickly and easily. So, it's worth it for me to build this adapter.
[4:07] worth it for me to build this adapter.
[4:07] worth it for me to build this adapter. It reduces the size of the tool. Okay.
[4:11] It reduces the size of the tool. Okay.
[4:11] It reduces the size of the tool. Okay. Okay. So, the project isn't done. Uh
[4:13] Okay. So, the project isn't done. Uh
[4:13] Okay. So, the project isn't done. Uh we're following the process of plan do
[4:15] we're following the process of plan do
[4:15] we're following the process of plan do check act always on anything we do. I
[4:17] check act always on anything we do. I
[4:17] check act always on anything we do. I implemented this policy change and I
[4:19] implemented this policy change and I
[4:19] implemented this policy change and I implemented a device a design and now I
[4:23] implemented a device a design and now I
[4:23] implemented a device a design and now I have to take the following months and
[4:25] have to take the following months and
[4:25] have to take the following months and see how things unfold. Make
[4:27] see how things unfold. Make
[4:27] see how things unfold. Make observations. This would be the checking
[4:29] observations. This would be the checking
[4:29] observations. This would be the checking part of plan do check act or PDCA. Um
[4:33] part of plan do check act or PDCA. Um
[4:33] part of plan do check act or PDCA. Um and that goes that checking happens
[4:36] and that goes that checking happens
[4:36] and that goes that checking happens across many different substances and
[4:38] across many different substances and
[4:38] across many different substances and many different activities.
[4:40] many different activities.
[4:40] many different activities. And by the way there's a time factor in
[4:42] And by the way there's a time factor in
[4:42] And by the way there's a time factor in that because several of these substances
[4:44] that because several of these substances
[4:44] that because several of these substances the problem occurs after giving a month
[4:47] the problem occurs after giving a month
[4:47] the problem occurs after giving a month of waiting time where something has uh
[4:50] of waiting time where something has uh
[4:50] of waiting time where something has uh gone from liquid to curing and being
[4:52] gone from liquid to curing and being
[4:52] gone from liquid to curing and being part of the problem. But then I noticed
[4:54] part of the problem. But then I noticed
[4:54] part of the problem. But then I noticed on these bottles, um, it's in sort of a
[4:59] on these bottles, um, it's in sort of a
[4:59] on these bottles, um, it's in sort of a a more extreme situation of the same.
[5:01] a more extreme situation of the same.
[5:01] a more extreme situation of the same. Once you fail to, uh, tighten it all the
[5:05] Once you fail to, uh, tighten it all the
[5:05] Once you fail to, uh, tighten it all the way, you're kind of dunzo. On the other
[5:07] way, you're kind of dunzo. On the other
[5:07] way, you're kind of dunzo. On the other hand, I saw that I had testers a few
[5:10] hand, I saw that I had testers a few
[5:10] hand, I saw that I had testers a few bottles of these that was still good
[5:12] bottles of these that was still good
[5:12] bottles of these that was still good from 15 years ago. and the paint
[5:16] from 15 years ago. and the paint
[5:16] from 15 years ago. and the paint performance compared to these other
[5:18] performance compared to these other
[5:18] performance compared to these other paints. This is one of the best uh
[5:21] paints. This is one of the best uh
[5:21] paints. This is one of the best uh performing enamels that like if you
[5:25] performing enamels that like if you
[5:25] performing enamels that like if you think this is just for models and so
[5:27] think this is just for models and so
[5:27] think this is just for models and so it's uh an aesthetic product rather than
[5:29] it's uh an aesthetic product rather than
[5:29] it's uh an aesthetic product rather than a performance of hardness and
[5:31] a performance of hardness and
[5:31] a performance of hardness and durability. No, it's great for
[5:33] durability. No, it's great for
[5:33] durability. No, it's great for performance. So then back to behavior,
[5:36] performance. So then back to behavior,
[5:36] performance. So then back to behavior, the behavior of always bringing this
[5:39] the behavior of always bringing this
[5:39] the behavior of always bringing this tool out wherever I'm doing a paint
[5:42] tool out wherever I'm doing a paint
[5:42] tool out wherever I'm doing a paint project or a mineral spirits project or
[5:44] project or a mineral spirits project or
[5:44] project or a mineral spirits project or a PVC project. Uh that's too
[5:47] a PVC project. Uh that's too
[5:47] a PVC project. Uh that's too inconvenient and I simply won't follow
[5:49] inconvenient and I simply won't follow
[5:49] inconvenient and I simply won't follow the rule. So the question is, can we
[5:53] the rule. So the question is, can we
[5:53] the rule. So the question is, can we raise how much we're tightening the
[5:56] raise how much we're tightening the
[5:56] raise how much we're tightening the substances just enough so that we don't
[5:59] substances just enough so that we don't
[6:00] substances just enough so that we don't get that cycle of curing and becoming
[6:03] get that cycle of curing and becoming
[6:03] get that cycle of curing and becoming less sealed and also hard to remove? And
[6:06] less sealed and also hard to remove? And
[6:06] less sealed and also hard to remove? And that answer became a resounding yes. If
[6:09] that answer became a resounding yes. If
[6:09] that answer became a resounding yes. If we change this circle,
[6:11] we change this circle,
[6:11] we change this circle, um, instead of needing the tool, we
[6:14] um, instead of needing the tool, we
[6:14] um, instead of needing the tool, we change it to a shape that we can grip,
[6:16] change it to a shape that we can grip,
[6:16] change it to a shape that we can grip, such as a hexagon, then we can squeeze
[6:20] such as a hexagon, then we can squeeze
[6:20] such as a hexagon, then we can squeeze this on. Even though there's deviating
[6:23] this on. Even though there's deviating
[6:23] this on. Even though there's deviating kinds of uh shapes on the cap a little
[6:26] kinds of uh shapes on the cap a little
[6:26] kinds of uh shapes on the cap a little bit, we can squeeze it. And with the
[6:27] bit, we can squeeze it. And with the
[6:27] bit, we can squeeze it. And with the hand squeezing force, um, I used this on
[6:31] hand squeezing force, um, I used this on
[6:31] hand squeezing force, um, I used this on my small jars for some time. And I found
[6:34] my small jars for some time. And I found
[6:34] my small jars for some time. And I found out that if I use the extra grip to
[6:37] out that if I use the extra grip to
[6:37] out that if I use the extra grip to tighten it, then they always turn out
[6:40] tighten it, then they always turn out
[6:40] tighten it, then they always turn out easy enough months later come to loosen
[6:43] easy enough months later come to loosen
[6:43] easy enough months later come to loosen it and it will always be loose enough
[6:46] it and it will always be loose enough
[6:46] it and it will always be loose enough that I can do this whole thing without a
[6:48] that I can do this whole thing without a
[6:48] that I can do this whole thing without a tool. And trust me, there's times where
[6:50] tool. And trust me, there's times where
[6:50] tool. And trust me, there's times where you where these things get so tight that
[6:52] you where these things get so tight that
[6:52] you where these things get so tight that you need pliers to actually remove them.
[6:54] you need pliers to actually remove them.
[6:54] you need pliers to actually remove them. &gt;&gt; Wait a minute. Think about that. It
[6:56] &gt;&gt; Wait a minute. Think about that. It
[6:56] &gt;&gt; Wait a minute. Think about that. It means that if I close it tighter when
[6:59] means that if I close it tighter when
[6:59] means that if I close it tighter when I'm sealing, it is looser when I'm
[7:02] I'm sealing, it is looser when I'm
[7:02] I'm sealing, it is looser when I'm loosening.
[7:04] loosening.
[7:04] loosening. Not intuitive. So now it's separate from
[7:07] Not intuitive. So now it's separate from
[7:07] Not intuitive. So now it's separate from YouTube. I'll publish this geometry for
[7:09] YouTube. I'll publish this geometry for
[7:09] YouTube. I'll publish this geometry for free, this model on GrabCAD and some
[7:12] free, this model on GrabCAD and some
[7:12] free, this model on GrabCAD and some people will discover it and be able to
[7:14] people will discover it and be able to
[7:14] people will discover it and be able to benefit.
[7:17] benefit.
[7:17] benefit. All right. So, I've posted this open
[7:18] All right. So, I've posted this open
[7:18] All right. So, I've posted this open model and then if the audience has their
[7:21] model and then if the audience has their
[7:21] model and then if the audience has their own 3D printer, then they just need the
[7:24] own 3D printer, then they just need the
[7:24] own 3D printer, then they just need the concept to benefit. They can have that
[7:26] concept to benefit. They can have that
[7:26] concept to benefit. They can have that value. Um, understanding what's being
[7:29] value. Um, understanding what's being
[7:29] value. Um, understanding what's being done here just by including images of
[7:33] done here just by including images of
[7:33] done here just by including images of the part that's integrated in its
[7:35] the part that's integrated in its
[7:35] the part that's integrated in its solution space, not just the image of
[7:38] solution space, not just the image of
[7:38] solution space, not just the image of the the model itself. Um, okay. If they
[7:43] the the model itself. Um, okay. If they
[7:43] the the model itself. Um, okay. If they have testers paints like this, then they
[7:47] have testers paints like this, then they
[7:47] have testers paints like this, then they benefit from seeing that root cause,
[7:50] benefit from seeing that root cause,
[7:50] benefit from seeing that root cause, that endeavor that I took to learn about
[7:53] that endeavor that I took to learn about
[7:54] that endeavor that I took to learn about this cycle of not tightening enough and
[7:57] this cycle of not tightening enough and
[7:57] this cycle of not tightening enough and then becoming harder to untighten. Um,
[8:00] then becoming harder to untighten. Um,
[8:00] then becoming harder to untighten. Um, so then if I describe the problem that
[8:03] so then if I describe the problem that
[8:03] so then if I describe the problem that I'm solving in my open post, then just
[8:07] I'm solving in my open post, then just
[8:07] I'm solving in my open post, then just that description is the value for that
[8:09] that description is the value for that
[8:09] that description is the value for that person and they might say, "Oh, I don't
[8:11] person and they might say, "Oh, I don't
[8:11] person and they might say, "Oh, I don't need this plastic thing. I'm just going
[8:16] need this plastic thing. I'm just going
[8:16] need this plastic thing. I'm just going to imitate the behavior and I'll pay
[8:18] to imitate the behavior and I'll pay
[8:18] to imitate the behavior and I'll pay closer attention to tightening up all my
[8:21] closer attention to tightening up all my
[8:21] closer attention to tightening up all my paints. That's going to save me money."
[8:23] paints. That's going to save me money."
[8:23] paints. That's going to save me money." Okay. If the person has no printer, but
[8:26] Okay. If the person has no printer, but
[8:26] Okay. If the person has no printer, but they've got money to spend, then the STL
[8:29] they've got money to spend, then the STL
[8:29] they've got money to spend, then the STL model, it's uh the fully rendered
[8:32] model, it's uh the fully rendered
[8:32] model, it's uh the fully rendered geometry, that's just exactly this part.
[8:35] geometry, that's just exactly this part.
[8:35] geometry, that's just exactly this part. They can download that, they can send it
[8:37] They can download that, they can send it
[8:37] They can download that, they can send it to a print shop, and for a dollar or so,
[8:40] to a print shop, and for a dollar or so,
[8:40] to a print shop, and for a dollar or so, they can grab my STL file that I've
[8:44] they can grab my STL file that I've
[8:44] they can grab my STL file that I've included and they can get a solution for
[8:47] included and they can get a solution for
[8:47] included and they can get a solution for specifically this size of bottle. Now,
[8:50] specifically this size of bottle. Now,
[8:50] specifically this size of bottle. Now, hold up. Do they really need money?
[8:53] hold up. Do they really need money?
[8:53] hold up. Do they really need money? Because if this is $25 and this doubles
[8:57] Because if this is $25 and this doubles
[8:57] Because if this is $25 and this doubles the lifespan of this thing and this
[9:00] the lifespan of this thing and this
[9:00] the lifespan of this thing and this doubles the lifespan of this and this is
[9:04] doubles the lifespan of this and this is
[9:04] doubles the lifespan of this and this is $2,000,
[9:06] $2,000,
[9:06] $2,000, then you're getting paid. Um if the
[9:10] then you're getting paid. Um if the
[9:10] then you're getting paid. Um if the person has modeling skills then they uh
[9:15] person has modeling skills then they uh
[9:15] person has modeling skills then they uh I'm giving them a shortcut if I include
[9:17] I'm giving them a shortcut if I include
[9:17] I'm giving them a shortcut if I include the geometry the actual not just the
[9:20] the geometry the actual not just the
[9:20] the geometry the actual not just the rendered asset but the geometry behind
[9:24] rendered asset but the geometry behind
[9:24] rendered asset but the geometry behind the asset which lives in a CAD model and
[9:27] the asset which lives in a CAD model and
[9:27] the asset which lives in a CAD model and the step file will suffice to give
[9:30] the step file will suffice to give
[9:30] the step file will suffice to give deliver that value. Um, and then if they
[9:33] deliver that value. Um, and then if they
[9:33] deliver that value. Um, and then if they have engineering skills, so they're
[9:36] have engineering skills, so they're
[9:36] have engineering skills, so they're maybe wanting to pivot this design,
[9:39] maybe wanting to pivot this design,
[9:39] maybe wanting to pivot this design, improve it, change it for another type
[9:41] improve it, change it for another type
[9:41] improve it, change it for another type of model, or uh run trials of their own
[9:45] of model, or uh run trials of their own
[9:45] of model, or uh run trials of their own to uh explore creating other models from
[9:49] to uh explore creating other models from
[9:49] to uh explore creating other models from this model. And so for them, the the
[9:53] this model. And so for them, the the
[9:54] this model. And so for them, the the value that's included is the parametric
[9:56] value that's included is the parametric
[9:56] value that's included is the parametric model. the fact that this um design is
[10:01] model. the fact that this um design is
[10:01] model. the fact that this um design is equationbased. And so it's uh it's a
[10:06] equationbased. And so it's uh it's a
[10:06] equationbased. And so it's uh it's a special type of model that's that has
[10:09] special type of model that's that has
[10:09] special type of model that's that has the dimensions linked to one another so
[10:11] the dimensions linked to one another so
[10:11] the dimensions linked to one another so that you can just change a couple of
[10:12] that you can just change a couple of
[10:12] that you can just change a couple of variables and see it all change. that
[10:15] variables and see it all change. that
[10:15] variables and see it all change. that person with let's say a young engineer
[10:17] person with let's say a young engineer
[10:17] person with let's say a young engineer that wants to enhance their skills. They
[10:20] that wants to enhance their skills. They
[10:20] that wants to enhance their skills. They now have a functional working example
[10:23] now have a functional working example
[10:23] now have a functional working example model that simply is a lesson on how to
[10:26] model that simply is a lesson on how to
[10:26] model that simply is a lesson on how to make a regular model parametric. And the
[10:29] make a regular model parametric. And the
[10:29] make a regular model parametric. And the way they would do that is they would uh
[10:31] way they would do that is they would uh
[10:31] way they would do that is they would uh model up their own version of this and
[10:33] model up their own version of this and
[10:33] model up their own version of this and then they would download my model and
[10:35] then they would download my model and
[10:35] then they would download my model and then they would see the differences and
[10:37] then they would see the differences and
[10:37] then they would see the differences and what makes uh my upload it's uh harder
[10:42] what makes uh my upload it's uh harder
[10:42] what makes uh my upload it's uh harder to break. you change one variable, one
[10:45] to break. you change one variable, one
[10:45] to break. you change one variable, one dimension and the part adjusts and
[10:47] dimension and the part adjusts and
[10:47] dimension and the part adjusts and updates and they can discover how that's
[10:49] updates and they can discover how that's
[10:49] updates and they can discover how that's done. So then they they can boost their
[10:51] done. So then they they can boost their
[10:51] done. So then they they can boost their skills or in any case at a much simpler
[10:55] skills or in any case at a much simpler
[10:55] skills or in any case at a much simpler level um someone that has Solid Works,
[10:58] level um someone that has Solid Works,
[10:58] level um someone that has Solid Works, they can download my solid part file and
[11:01] they can download my solid part file and
[11:01] they can download my solid part file and there's three variations built into this
[11:03] there's three variations built into this
[11:03] there's three variations built into this one single file. You can drop down,
[11:05] one single file. You can drop down,
[11:05] one single file. You can drop down, click the testers version. You can click
[11:08] click the testers version. You can click
[11:08] click the testers version. You can click the 35mm version and it will create
[11:14] the 35mm version and it will create
[11:14] the 35mm version and it will create three separate versions final like ready
[11:16] three separate versions final like ready
[11:16] three separate versions final like ready to go in a second and then they could
[11:19] to go in a second and then they could
[11:19] to go in a second and then they could crank out STL versions of that the
[11:22] crank out STL versions of that the
[11:22] crank out STL versions of that the rendered thing that goes to the print to
[11:24] rendered thing that goes to the print to
[11:24] rendered thing that goes to the print to 3D printer to produce a physical part.
[11:28] 3D printer to produce a physical part.
[11:28] 3D printer to produce a physical part. Now, if the audience has a small
[11:31] Now, if the audience has a small
[11:31] Now, if the audience has a small business like a printing business or
[11:33] business like a printing business or
[11:33] business like a printing business or they distribute tools or something, then
[11:36] they distribute tools or something, then
[11:36] they distribute tools or something, then by the way, there's thousands of those
[11:38] by the way, there's thousands of those
[11:38] by the way, there's thousands of those single person businesses already. Um,
[11:40] single person businesses already. Um,
[11:40] single person businesses already. Um, then they can have the full design, not
[11:43] then they can have the full design, not
[11:43] then they can have the full design, not just the design STL, but the source of
[11:45] just the design STL, but the source of
[11:46] just the design STL, but the source of that design and that includes where did
[11:49] that design and that includes where did
[11:49] that design and that includes where did it come from, who produced that. So that
[11:51] it come from, who produced that. So that
[11:51] it come from, who produced that. So that what they can do is they can download
[11:53] what they can do is they can download
[11:54] what they can do is they can download the models and then they can see the
[11:55] the models and then they can see the
[11:55] the models and then they can see the author
[11:56] author
[11:56] author &gt;&gt; or they can map this back to the openlab
[11:58] &gt;&gt; or they can map this back to the openlab
[11:58] &gt;&gt; or they can map this back to the openlab project at qr.net/openlab
[12:01] project at qr.net/openlab
[12:01] project at qr.net/openlab project. They can find if it was me that
[12:05] project. They can find if it was me that
[12:05] project. They can find if it was me that created it or peer community and they
[12:07] created it or peer community and they
[12:07] created it or peer community and they can communicate with that person and
[12:10] can communicate with that person and
[12:10] can communicate with that person and they could say hey is it true I can just
[12:12] they could say hey is it true I can just
[12:12] they could say hey is it true I can just download this and I can profit from that
[12:14] download this and I can profit from that
[12:14] download this and I can profit from that and no it's no problem. Um, and I'll
[12:17] and no it's no problem. Um, and I'll
[12:17] and no it's no problem. Um, and I'll say, "Yep." Or they can say, "Well,
[12:19] say, "Yep." Or they can say, "Well,
[12:19] say, "Yep." Or they can say, "Well, there's a couple hang-ups for me to be
[12:21] there's a couple hang-ups for me to be
[12:21] there's a couple hang-ups for me to be able to adjust this to actually make it
[12:23] able to adjust this to actually make it
[12:23] able to adjust this to actually make it sellable, like, uh, could you make a
[12:25] sellable, like, uh, could you make a
[12:25] sellable, like, uh, could you make a could you take a snapshot of it in this
[12:27] could you take a snapshot of it in this
[12:27] could you take a snapshot of it in this way?" And, uh, and then they can make an
[12:31] way?" And, uh, and then they can make an
[12:31] way?" And, uh, and then they can make an exchange of business. Oh, I'll give you
[12:33] exchange of business. Oh, I'll give you
[12:33] exchange of business. Oh, I'll give you some royalties or something like that.
[12:35] some royalties or something like that.
[12:35] some royalties or something like that. [snorts] So, the value is new
[12:37] [snorts] So, the value is new
[12:37] [snorts] So, the value is new collaborations. The value is making
[12:39] collaborations. The value is making
[12:39] collaborations. The value is making profits. The value is, and I'm what I'm
[12:41] profits. The value is, and I'm what I'm
[12:41] profits. The value is, and I'm what I'm holding in my hands is an example part.
[12:43] holding in my hands is an example part.
[12:43] holding in my hands is an example part. This is a a 3D printed battery adapter
[12:46] This is a a 3D printed battery adapter
[12:46] This is a a 3D printed battery adapter that I ordered like three or four years
[12:49] that I ordered like three or four years
[12:49] that I ordered like three or four years ago on Amazon. So this single maker with
[12:52] ago on Amazon. So this single maker with
[12:52] ago on Amazon. So this single maker with a couple of 3D printers in his basement,
[12:56] a couple of 3D printers in his basement,
[12:56] a couple of 3D printers in his basement, he is producing these things a useful
[12:58] he is producing these things a useful
[12:58] he is producing these things a useful tool and he has a shop. These things
[13:00] tool and he has a shop. These things
[13:00] tool and he has a shop. These things don't uh they they come and go the
[13:03] don't uh they they come and go the
[13:03] don't uh they they come and go the demand for a specific type of model. So
[13:06] demand for a specific type of model. So
[13:06] demand for a specific type of model. So that kind of person is carrying multiple
[13:08] that kind of person is carrying multiple
[13:08] that kind of person is carrying multiple they want to carry good quality stuff.
[13:11] they want to carry good quality stuff.
[13:11] they want to carry good quality stuff. uh they may not have the capability to
[13:13] uh they may not have the capability to
[13:13] uh they may not have the capability to design every single thing and that
[13:15] design every single thing and that
[13:15] design every single thing and that everyone doesn't need to be a designer.
[13:17] everyone doesn't need to be a designer.
[13:17] everyone doesn't need to be a designer. So this is u this is crucial I add that
[13:20] So this is u this is crucial I add that
[13:20] So this is u this is crucial I add that into my post it's coming it's connected
[13:23] into my post it's coming it's connected
[13:23] into my post it's coming it's connected to the individual person that is the
[13:25] to the individual person that is the
[13:25] to the individual person that is the source as well as the the story of the
[13:27] source as well as the the story of the
[13:27] source as well as the the story of the source. Okay. Then if a person has a
[13:31] source. Okay. Then if a person has a
[13:31] source. Okay. Then if a person has a similar design let's say it's an
[13:32] similar design let's say it's an
[13:32] similar design let's say it's an engineer like me. I've got all this work
[13:34] engineer like me. I've got all this work
[13:34] engineer like me. I've got all this work to do on my own but sitting on my hard
[13:36] to do on my own but sitting on my hard
[13:36] to do on my own but sitting on my hard drive is a is a good project that I've
[13:39] drive is a is a good project that I've
[13:39] drive is a is a good project that I've created. Now, how do I unlock that
[13:41] created. Now, how do I unlock that
[13:41] created. Now, how do I unlock that project so that other people can
[13:42] project so that other people can
[13:42] project so that other people can benefit? Then the post itself becomes a
[13:46] benefit? Then the post itself becomes a
[13:46] benefit? Then the post itself becomes a method of documentation. How can I turn
[13:49] method of documentation. How can I turn
[13:49] method of documentation. How can I turn this thing that is not producing value
[13:50] this thing that is not producing value
[13:50] this thing that is not producing value into a thing that is producing value?
[13:53] into a thing that is producing value?
[13:53] into a thing that is producing value? Um, how do I get a pat on the back from
[13:55] Um, how do I get a pat on the back from
[13:55] Um, how do I get a pat on the back from a community for doing an extra high work
[13:58] a community for doing an extra high work
[13:58] a community for doing an extra high work level of effort on my thing, etc. And so
[14:03] level of effort on my thing, etc. And so
[14:03] level of effort on my thing, etc. And so that would be my uh the full GrabCad
[14:07] that would be my uh the full GrabCad
[14:08] that would be my uh the full GrabCad post and it would be my maybe
[14:09] post and it would be my maybe
[14:10] post and it would be my maybe descriptions in openlab.org
[14:13] descriptions in openlab.org
[14:13] descriptions in openlab.org whatever.
[14:14] whatever.
[14:14] whatever. And and so um because we don't have we
[14:20] And and so um because we don't have we
[14:20] And and so um because we don't have we have things like printables, libraries
[14:22] have things like printables, libraries
[14:22] have things like printables, libraries where you can download gadgets, but we
[14:25] where you can download gadgets, but we
[14:25] where you can download gadgets, but we don't have the full stack open-source
[14:28] don't have the full stack open-source
[14:28] don't have the full stack open-source hardware methodologies really
[14:30] hardware methodologies really
[14:30] hardware methodologies really established in our planet. And so now
[14:32] established in our planet. And so now
[14:32] established in our planet. And so now now we have an example and that's that's
[14:36] now we have an example and that's that's
[14:36] now we have an example and that's that's value just by itself. Okay. Now since I
[14:39] value just by itself. Okay. Now since I
[14:39] value just by itself. Okay. Now since I took this journey I discovered that
[14:41] took this journey I discovered that
[14:41] took this journey I discovered that these three sizes are extremely common
[14:44] these three sizes are extremely common
[14:44] these three sizes are extremely common and that un unexpectedly I discovered
[14:48] and that un unexpectedly I discovered
[14:48] and that un unexpectedly I discovered certain cap sizes between the the large
[14:51] certain cap sizes between the the large
[14:51] certain cap sizes between the the large fluids are all shared very much
[14:54] fluids are all shared very much
[14:54] fluids are all shared very much simplifying the effort if someone wants
[14:56] simplifying the effort if someone wants
[14:56] simplifying the effort if someone wants to improve their whole cap situation.
[14:59] to improve their whole cap situation.
[14:59] to improve their whole cap situation. All right. So there's 22, 45, and 35 mm
[15:03] All right. So there's 22, 45, and 35 mm
[15:03] All right. So there's 22, 45, and 35 mm diameters. Now, in this model that
[15:06] diameters. Now, in this model that
[15:06] diameters. Now, in this model that you're looking at here, two of the
[15:09] you're looking at here, two of the
[15:09] you're looking at here, two of the variations have been fully
[15:11] variations have been fully
[15:11] variations have been fully characterized. And so those are in the
[15:13] characterized. And so those are in the
[15:13] characterized. And so those are in the table of configurations, and I can uh
[15:16] table of configurations, and I can uh
[15:16] table of configurations, and I can uh swap between those two. Exact same
[15:18] swap between those two. Exact same
[15:18] swap between those two. Exact same model, just a couple of different values
[15:20] model, just a couple of different values
[15:20] model, just a couple of different values have changed.
[15:23] have changed.
[15:23] have changed. So today I'm recalling this is version
[15:25] So today I'm recalling this is version
[15:25] So today I'm recalling this is version two. I forgot even about doing version
[15:27] two. I forgot even about doing version
[15:27] two. I forgot even about doing version one. And so the fact that I always put
[15:30] one. And so the fact that I always put
[15:30] one. And so the fact that I always put my version numbers at least of some sort
[15:34] my version numbers at least of some sort
[15:34] my version numbers at least of some sort on the actual STL models means if this
[15:37] on the actual STL models means if this
[15:37] on the actual STL models means if this winds up in the hands of someone, it's a
[15:40] winds up in the hands of someone, it's a
[15:40] winds up in the hands of someone, it's a clue that they could wherever they got
[15:42] clue that they could wherever they got
[15:42] clue that they could wherever they got this, they could potentially go find the
[15:45] this, they could potentially go find the
[15:45] this, they could potentially go find the newer version. Or if they only find this
[15:48] newer version. Or if they only find this
[15:48] newer version. Or if they only find this one, then they it's a clue um that
[15:51] one, then they it's a clue um that
[15:51] one, then they it's a clue um that there's a whole story behind this design
[15:53] there's a whole story behind this design
[15:53] there's a whole story behind this design and that they could probably go retrieve
[15:55] and that they could probably go retrieve
[15:55] and that they could probably go retrieve more.
[15:56] more.
[15:56] more. Additionally, if my friend uh grabs this
[16:00] Additionally, if my friend uh grabs this
[16:00] Additionally, if my friend uh grabs this STL and one day he shares it with
[16:03] STL and one day he shares it with
[16:03] STL and one day he shares it with another friend, but then it's been
[16:06] another friend, but then it's been
[16:06] another friend, but then it's been separated from all the post and all the
[16:08] separated from all the post and all the
[16:08] separated from all the post and all the authored data, then this um this version
[16:14] authored data, then this um this version
[16:14] authored data, then this um this version number is indicating the upright
[16:16] number is indicating the upright
[16:16] number is indicating the upright direction for printers uh when you put
[16:20] direction for printers uh when you put
[16:20] direction for printers uh when you put this on the FDM printer machine. And so
[16:22] this on the FDM printer machine. And so
[16:22] this on the FDM printer machine. And so that's one more clue that will more
[16:24] that's one more clue that will more
[16:24] that's one more clue that will more likely make them successful at printing
[16:27] likely make them successful at printing
[16:27] likely make them successful at printing this out. When it comes to this whole
[16:29] this out. When it comes to this whole
[16:29] this out. When it comes to this whole business situation, I personally don't
[16:32] business situation, I personally don't
[16:32] business situation, I personally don't have capacity or interest in pursuing
[16:35] have capacity or interest in pursuing
[16:35] have capacity or interest in pursuing that endeavor. It's a whole lot more
[16:37] that endeavor. It's a whole lot more
[16:37] that endeavor. It's a whole lot more work to produce that more value that
[16:39] work to produce that more value that
[16:39] work to produce that more value that comes in the form of of money revenue
[16:43] comes in the form of of money revenue
[16:43] comes in the form of of money revenue for uh such a business as this. And but
[16:46] for uh such a business as this. And but
[16:46] for uh such a business as this. And but remember all of our intellectual
[16:48] remember all of our intellectual
[16:48] remember all of our intellectual property laws and systems and even the
[16:51] property laws and systems and even the
[16:51] property laws and systems and even the knowledge carried by lawyers and so
[16:53] knowledge carried by lawyers and so
[16:53] knowledge carried by lawyers and so forth, it was all based on a world where
[16:56] forth, it was all based on a world where
[16:56] forth, it was all based on a world where it was impossible to get connected or
[16:59] it was impossible to get connected or
[16:59] it was impossible to get connected or very very unlikely that you would get
[17:01] very very unlikely that you would get
[17:01] very very unlikely that you would get connected with the person that authored
[17:04] connected with the person that authored
[17:04] connected with the person that authored a design and that's in the past. Now
[17:07] a design and that's in the past. Now
[17:07] a design and that's in the past. Now it's very very possible to get connected
[17:10] it's very very possible to get connected
[17:10] it's very very possible to get connected and this is what this is how software
[17:12] and this is what this is how software
[17:12] and this is what this is how software exchange free exchange of software
[17:14] exchange free exchange of software
[17:14] exchange free exchange of software evolved because you can forget about the
[17:17] evolved because you can forget about the
[17:18] evolved because you can forget about the business people and the lawyers and the
[17:19] business people and the lawyers and the
[17:19] business people and the lawyers and the and the
[17:21] and the
[17:21] and the all the structures that that stand in
[17:23] all the structures that that stand in
[17:24] all the structures that that stand in the way of one design communicate one
[17:26] the way of one design communicate one
[17:26] the way of one design communicate one designer one uh creator maker
[17:29] designer one uh creator maker
[17:29] designer one uh creator maker communicating with another those don't
[17:31] communicating with another those don't
[17:31] communicating with another those don't matter because we have the internet now
[17:34] matter because we have the internet now
[17:34] matter because we have the internet now and so that sort of free distribution,
[17:38] and so that sort of free distribution,
[17:38] and so that sort of free distribution, it doesn't have any significant impact
[17:40] it doesn't have any significant impact
[17:40] it doesn't have any significant impact on me and for someone else it might and
[17:43] on me and for someone else it might and
[17:43] on me and for someone else it might and then they can choose not to do it and
[17:45] then they can choose not to do it and
[17:45] then they can choose not to do it and there's no problem whatsoever. But um if
[17:49] there's no problem whatsoever. But um if
[17:49] there's no problem whatsoever. But um if now somebody wants to fully own fully
[17:52] now somebody wants to fully own fully
[17:52] now somebody wants to fully own fully close off a design for a similar uh
[17:56] close off a design for a similar uh
[17:56] close off a design for a similar uh situation, a similar um solution,
[18:01] situation, a similar um solution,
[18:01] situation, a similar um solution, then they still have to compete. they
[18:03] then they still have to compete. they
[18:03] then they still have to compete. they still have to outperform whatever I've
[18:06] still have to outperform whatever I've
[18:06] still have to outperform whatever I've distributed for free. They're going to
[18:08] distributed for free. They're going to
[18:08] distributed for free. They're going to have to make it much better than that.
[18:10] have to make it much better than that.
[18:10] have to make it much better than that. And it's a good thing. So, you have u
[18:14] And it's a good thing. So, you have u
[18:14] And it's a good thing. So, you have u next year somebody does a better design
[18:16] next year somebody does a better design
[18:16] next year somebody does a better design privately and holds on to it and
[18:19] privately and holds on to it and
[18:19] privately and holds on to it and distributes it. That's a $5 product that
[18:21] distributes it. That's a $5 product that
[18:21] distributes it. That's a $5 product that you can buy at the store while this one
[18:23] you can buy at the store while this one
[18:23] you can buy at the store while this one is the free product that you can print
[18:26] is the free product that you can print
[18:26] is the free product that you can print for 30 cents. And both of them should
[18:29] for 30 cents. And both of them should
[18:29] for 30 cents. And both of them should exist. Both of them should exist because
[18:32] exist. Both of them should exist because
[18:32] exist. Both of them should exist because then we create more benchmarking
[18:33] then we create more benchmarking
[18:33] then we create more benchmarking opportunities, more opportunities to see
[18:35] opportunities, more opportunities to see
[18:35] opportunities, more opportunities to see someone else looked into this problem,
[18:38] someone else looked into this problem,
[18:38] someone else looked into this problem, formed a solution and the knowledge that
[18:41] formed a solution and the knowledge that
[18:41] formed a solution and the knowledge that they they discovered on that journey is
[18:44] they they discovered on that journey is
[18:44] they they discovered on that journey is now becoming manifest. And then we can
[18:47] now becoming manifest. And then we can
[18:47] now becoming manifest. And then we can compare and while we build things for
[18:49] compare and while we build things for
[18:49] compare and while we build things for free, while we share things openly, we
[18:51] free, while we share things openly, we
[18:51] free, while we share things openly, we can easily retrieve those ideas from the
[18:55] can easily retrieve those ideas from the
[18:55] can easily retrieve those ideas from the the
[18:57] the
[18:57] the capitalist world. and uh and just level
[19:01] capitalist world. and uh and just level
[19:01] capitalist world. and uh and just level up, level up, level up continually. So,
[19:03] up, level up, level up continually. So,
[19:03] up, level up, level up continually. So, I know for a fact some people are asking
[19:05] I know for a fact some people are asking
[19:05] I know for a fact some people are asking in their heads, uh, David, you're so
[19:08] in their heads, uh, David, you're so
[19:08] in their heads, uh, David, you're so talented, you're so well educated, why
[19:10] talented, you're so well educated, why
[19:10] talented, you're so well educated, why would you spend your time on such a a
[19:12] would you spend your time on such a a
[19:12] would you spend your time on such a a trivial problem? Someone else could do
[19:14] trivial problem? Someone else could do
[19:14] trivial problem? Someone else could do that or you're not getting paid, why why
[19:16] that or you're not getting paid, why why
[19:16] that or you're not getting paid, why why would you just do it on your own? And I
[19:19] would you just do it on your own? And I
[19:19] would you just do it on your own? And I would ask them like one of my peers in
[19:21] would ask them like one of my peers in
[19:21] would ask them like one of my peers in mechanical engineering. Um, okay. If you
[19:25] mechanical engineering. Um, okay. If you
[19:25] mechanical engineering. Um, okay. If you saw a problem that you encountered at
[19:27] saw a problem that you encountered at
[19:27] saw a problem that you encountered at age 35
[19:29] age 35
[19:29] age 35 and you could recall back that you also
[19:31] and you could recall back that you also
[19:31] and you could recall back that you also had that problem at age 10 and then you
[19:35] had that problem at age 10 and then you
[19:35] had that problem at age 10 and then you could recall back that your father had
[19:36] could recall back that your father had
[19:36] could recall back that your father had that problem and then you traveled to
[19:40] that problem and then you traveled to
[19:40] that problem and then you traveled to Asia and you lived in Asia and you saw
[19:41] Asia and you lived in Asia and you saw
[19:41] Asia and you lived in Asia and you saw that those people have the same problem.
[19:46] that those people have the same problem.
[19:46] that those people have the same problem. It doesn't matter what qualifications it
[19:48] It doesn't matter what qualifications it
[19:48] It doesn't matter what qualifications it requires. It certainly doesn't require a
[19:50] requires. It certainly doesn't require a
[19:50] requires. It certainly doesn't require a master of science to solve this problem.
[19:52] master of science to solve this problem.
[19:52] master of science to solve this problem. Well, I don't want to live in a country
[19:55] Well, I don't want to live in a country
[19:55] Well, I don't want to live in a country where we go to the moon twice and we
[19:59] where we go to the moon twice and we
[19:59] where we go to the moon twice and we still have to deal with these small
[20:00] still have to deal with these small
[20:00] still have to deal with these small problems that could have been solved a
[20:02] problems that could have been solved a
[20:02] problems that could have been solved a long time ago. It's an embarrassment to
[20:06] long time ago. It's an embarrassment to
[20:06] long time ago. It's an embarrassment to our economy. It's an embarrassment to
[20:08] our economy. It's an embarrassment to
[20:08] our economy. It's an embarrassment to the name of mechanical engineers in the
[20:10] the name of mechanical engineers in the
[20:10] the name of mechanical engineers in the world. And there are a thousand more
[20:13] world. And there are a thousand more
[20:13] world. And there are a thousand more problems just like it that uh it's time
[20:16] problems just like it that uh it's time
[20:16] problems just like it that uh it's time to get them solved.

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
