---
title: "Exoskeleton Design & Control of Fastener Torque"
url: "https://www.youtube.com/watch?v=khiMEj0_Yjo"
video_id: "khiMEj0_Yjo"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2026-02-13
duration: "23:21"
duration_sec: 1401
views: 1391
likes: 36
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/khiMEj0_Yjo/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 1090
chapters_count: 9
has_description: true
has_comments: false
---

## Description

Meet two colleagues, Ibraheem and Precious, who are studying for their Mechanical Engineering PhD degrees and performing resesarch with this advanced robotic exoskeleton.

First I'll show you the purpose of the exoskeleton, then show a few details about how the research lab is equipped, then a lesson about how to measure the torque spec on a screw.  How do you use a torque wrench to evaluate the pre-existing load on a fastener in an already-assembled assembly?  Find my method in the second half.

[CHAPTERS]
0:00 introduce Ibraheem & Precious
1:00 exoskeleton purpose
3:15 bio-signal meters
4:25 research goals
8:50 improving lab workflow
12:45 harmonic drive close-up
14:05 torque measuring devices
19:10 demonstrate torque eval
22:56 help from audience?

## Chapters

- 0:00 introduce Ibraheem & Precious
- 1:00 exoskeleton purpose
- 3:15 bio-signal meters
- 4:25 research goals
- 8:50 improving lab workflow
- 12:45 harmonic drive close-up
- 14:05 torque measuring devices
- 19:10 demonstrate torque eval
- 22:56 help from audience?

## Transcript

[0:01] Okay. So, right now I'm in the
[0:01] Okay. So, right now I'm in the laboratory of um
[0:05] laboratory of um
[0:05] laboratory of um uh Dr. Lang Gary. He's a former adviser
[0:08] uh Dr. Lang Gary. He's a former adviser
[0:08] uh Dr. Lang Gary. He's a former adviser of mine. I'm pointing the camera this
[0:10] of mine. I'm pointing the camera this
[0:10] of mine. I'm pointing the camera this way so you don't you don't have to I'm
[0:12] way so you don't you don't have to I'm
[0:12] way so you don't you don't have to I'm just kind of u capturing the moment
[0:14] just kind of u capturing the moment
[0:14] just kind of u capturing the moment because I just met Ibraim and um
[0:20] because I just met Ibraim and um
[0:20] because I just met Ibraim and um not perfect.
[0:21] not perfect.
[0:21] not perfect. &gt;&gt; Precious. I keep saying perfect because
[0:23] &gt;&gt; Precious. I keep saying perfect because
[0:23] &gt;&gt; Precious. I keep saying perfect because I'm because I'm communicating with
[0:25] I'm because I'm communicating with
[0:25] I'm because I'm communicating with perfect a lot. So, this is Precious.
[0:27] perfect a lot. So, this is Precious.
[0:27] perfect a lot. So, this is Precious. She's um she's a mechanical engineering
[0:29] She's um she's a mechanical engineering
[0:29] She's um she's a mechanical engineering PhD student from uh Nigeria and
[0:33] PhD student from uh Nigeria and
[0:33] PhD student from uh Nigeria and specifically specifically from Aeri and
[0:36] specifically specifically from Aeri and
[0:36] specifically specifically from Aeri and that's where so uh Precious has been for
[0:39] that's where so uh Precious has been for
[0:40] that's where so uh Precious has been for one semester she spent at the university
[0:43] one semester she spent at the university
[0:43] one semester she spent at the university in Aeri where we're building the the
[0:45] in Aeri where we're building the the
[0:45] in Aeri where we're building the the Scuttle Lab Nigeria. Um, and so both of
[0:48] Scuttle Lab Nigeria. Um, and so both of
[0:48] Scuttle Lab Nigeria. Um, and so both of these guys, they're doing controls. Uh,
[0:51] these guys, they're doing controls. Uh,
[0:51] these guys, they're doing controls. Uh, they're doing their PhD um, in the
[0:54] they're doing their PhD um, in the
[0:54] they're doing their PhD um, in the second year out of five years in
[0:56] second year out of five years in
[0:56] second year out of five years in controls. And we're working again on the
[0:59] controls. And we're working again on the
[0:59] controls. And we're working again on the old project that came from uh, some
[1:01] old project that came from uh, some
[1:01] old project that came from uh, some former graduates. And this is a um,
[1:06] former graduates. And this is a um,
[1:06] former graduates. And this is a um, semiautonomous what assisted what would
[1:09] semiautonomous what assisted what would
[1:09] semiautonomous what assisted what would you call it if in one phrase? uh assist
[1:13] you call it if in one phrase? uh assist
[1:13] you call it if in one phrase? uh assist as needed exoskeleton for
[1:16] as needed exoskeleton for
[1:16] as needed exoskeleton for rehabilitation. That's what I said.
[1:18] rehabilitation. That's what I said.
[1:18] rehabilitation. That's what I said. &gt;&gt; So, it's an exoskeleton and
[1:21] &gt;&gt; So, it's an exoskeleton and
[1:21] &gt;&gt; So, it's an exoskeleton and the the audience would benefit probably
[1:24] the the audience would benefit probably
[1:24] the the audience would benefit probably by knowing there will be different words
[1:27] by knowing there will be different words
[1:27] by knowing there will be different words for a robotics thing. If you program
[1:29] for a robotics thing. If you program
[1:29] for a robotics thing. If you program this to just move on its own, it could
[1:32] this to just move on its own, it could
[1:32] this to just move on its own, it could almost be like scooping up equipment and
[1:34] almost be like scooping up equipment and
[1:34] almost be like scooping up equipment and moving it repeatedly. That's based on a
[1:37] moving it repeatedly. That's based on a
[1:37] moving it repeatedly. That's based on a software. Then you would call it an
[1:38] software. Then you would call it an
[1:38] software. Then you would call it an autonomous robot. The exoskeleton is is
[1:42] autonomous robot. The exoskeleton is is
[1:42] autonomous robot. The exoskeleton is is based on its function. And so um if a
[1:46] based on its function. And so um if a
[1:46] based on its function. And so um if a person in rehab needs their joint uh
[1:48] person in rehab needs their joint uh
[1:48] person in rehab needs their joint uh they need to exercise muscles in a per a
[1:51] they need to exercise muscles in a per a
[1:51] they need to exercise muscles in a per a certain direction of their shoulder or
[1:53] certain direction of their shoulder or
[1:53] certain direction of their shoulder or their arm, then they strap into this
[1:57] their arm, then they strap into this
[1:57] their arm, then they strap into this thing here. And then it can be
[1:59] thing here. And then it can be
[1:59] thing here. And then it can be programmed to simply perform resistance
[2:02] programmed to simply perform resistance
[2:02] programmed to simply perform resistance or it could make you weightless. Program
[2:04] or it could make you weightless. Program
[2:04] or it could make you weightless. Program it to say your arm has zero mass and
[2:07] it to say your arm has zero mass and
[2:07] it to say your arm has zero mass and then you'll feel like you're on the
[2:09] then you'll feel like you're on the
[2:09] then you'll feel like you're on the moon. and just very gentle uh muscle
[2:13] moon. and just very gentle uh muscle
[2:13] moon. and just very gentle uh muscle contractions could give you that
[2:14] contractions could give you that
[2:14] contractions could give you that mobility. And so this is uh I think
[2:17] mobility. And so this is uh I think
[2:17] mobility. And so this is uh I think beneficial in rehab in the sense that
[2:19] beneficial in rehab in the sense that
[2:19] beneficial in rehab in the sense that you could go from all right we have no
[2:23] you could go from all right we have no
[2:23] you could go from all right we have no no strength because we just had surgery
[2:26] no strength because we just had surgery
[2:26] no strength because we just had surgery to uh executing a full strength movement
[2:29] to uh executing a full strength movement
[2:29] to uh executing a full strength movement against gravity and everything else.
[2:31] against gravity and everything else.
[2:31] against gravity and everything else. This gives you like a stepping path uh
[2:35] This gives you like a stepping path uh
[2:35] This gives you like a stepping path uh from zero to full muscle actuation
[2:39] from zero to full muscle actuation
[2:39] from zero to full muscle actuation or even I think a patient could strap in
[2:43] or even I think a patient could strap in
[2:43] or even I think a patient could strap in here and say where does it hurt and if
[2:45] here and say where does it hurt and if
[2:45] here and say where does it hurt and if there's a certain range where they're
[2:47] there's a certain range where they're
[2:47] there's a certain range where they're their joints are giving them trouble.
[2:49] their joints are giving them trouble.
[2:49] their joints are giving them trouble. Now we have a a literal measurement that
[2:51] Now we have a a literal measurement that
[2:51] Now we have a a literal measurement that says uh for the doctor exactly here in
[2:54] says uh for the doctor exactly here in
[2:54] says uh for the doctor exactly here in this reference frame at this angle
[2:57] this reference frame at this angle
[2:57] this reference frame at this angle that's where my my elbow gives me
[2:59] that's where my my elbow gives me
[2:59] that's where my my elbow gives me trouble. And I think that could probably
[3:01] trouble. And I think that could probably
[3:01] trouble. And I think that could probably help a lot with diagnosing what's going
[3:05] help a lot with diagnosing what's going
[3:05] help a lot with diagnosing what's going on inside the body.
[3:07] on inside the body.
[3:07] on inside the body. &gt;&gt; Oh yeah, we have like torque sensors in
[3:09] &gt;&gt; Oh yeah, we have like torque sensors in
[3:09] &gt;&gt; Oh yeah, we have like torque sensors in every single joint. And we have
[3:13] every single joint. And we have
[3:13] every single joint. And we have electromyiography
[3:14] electromyiography
[3:14] electromyiography sensors over here.
[3:16] sensors over here.
[3:16] sensors over here. &gt;&gt; What is it?
[3:16] &gt;&gt; What is it?
[3:16] &gt;&gt; What is it? &gt;&gt; These measure electrical signals that
[3:19] &gt;&gt; These measure electrical signals that
[3:19] &gt;&gt; These measure electrical signals that come from your muscles. So I would
[3:21] come from your muscles. So I would
[3:21] come from your muscles. So I would attach it to your skin. So it's like
[3:24] attach it to your skin. So it's like
[3:24] attach it to your skin. So it's like bunch of probes. You have some sticky
[3:27] bunch of probes. You have some sticky
[3:27] bunch of probes. You have some sticky uh stuff that you put here. Then you
[3:29] uh stuff that you put here. Then you
[3:29] uh stuff that you put here. Then you attach it to the patient. So when they
[3:31] attach it to the patient. So when they
[3:31] attach it to the patient. So when they contract their muscle, you'll actually
[3:32] contract their muscle, you'll actually
[3:32] contract their muscle, you'll actually see the muscle signal on the program.
[3:36] see the muscle signal on the program.
[3:36] see the muscle signal on the program. &gt;&gt; So this is kind of like another way of
[3:38] &gt;&gt; So this is kind of like another way of
[3:38] &gt;&gt; So this is kind of like another way of measuring patient performance other than
[3:41] measuring patient performance other than
[3:41] measuring patient performance other than just um like force feedback, velocity,
[3:44] just um like force feedback, velocity,
[3:44] just um like force feedback, velocity, and that kind of stuff.
[3:46] and that kind of stuff.
[3:46] and that kind of stuff. &gt;&gt; That's brand new.
[3:47] &gt;&gt; That's brand new.
[3:47] &gt;&gt; That's brand new. &gt;&gt; So this is really expensive.
[3:49] &gt;&gt; So this is really expensive.
[3:49] &gt;&gt; So this is really expensive. &gt;&gt; Um this came from Is this brand new to
[3:52] &gt;&gt; Um this came from Is this brand new to
[3:52] &gt;&gt; Um this came from Is this brand new to you or um
[3:54] you or um
[3:54] you or um &gt;&gt; It's where
[3:55] &gt;&gt; It's where
[3:55] &gt;&gt; It's where &gt;&gt; it's been here in the lab for a while,
[3:56] &gt;&gt; it's been here in the lab for a while,
[3:56] &gt;&gt; it's been here in the lab for a while, but yeah, I've never worked with them.
[3:58] but yeah, I've never worked with them.
[3:58] but yeah, I've never worked with them. And then what this is the brand
[4:00] And then what this is the brand
[4:00] And then what this is the brand &gt;&gt; and they have a software that's already
[4:02] &gt;&gt; and they have a software that's already
[4:02] &gt;&gt; and they have a software that's already built and it's just counting up like for
[4:05] built and it's just counting up like for
[4:05] built and it's just counting up like for each module this is how much uh
[4:08] each module this is how much uh
[4:08] each module this is how much uh actuation of the muscle is is taking
[4:10] actuation of the muscle is is taking
[4:10] actuation of the muscle is is taking place.
[4:10] place.
[4:10] place. &gt;&gt; You actually see the signals. So it's
[4:12] &gt;&gt; You actually see the signals. So it's
[4:12] &gt;&gt; You actually see the signals. So it's just giving you the output the signal
[4:14] just giving you the output the signal
[4:14] just giving you the output the signal that it's detecting from your nervous
[4:17] that it's detecting from your nervous
[4:17] that it's detecting from your nervous system when you're trying to activate a
[4:18] system when you're trying to activate a
[4:18] system when you're trying to activate a muscle.
[4:19] muscle.
[4:19] muscle. &gt;&gt; Nice.
[4:20] &gt;&gt; Nice.
[4:20] &gt;&gt; Nice. &gt;&gt; We have our own software on love view
[4:22] &gt;&gt; We have our own software on love view
[4:22] &gt;&gt; We have our own software on love view that does the same thing that the
[4:23] that does the same thing that the
[4:23] that does the same thing that the company did.
[4:25] company did.
[4:25] company did. &gt;&gt; What would you want to keep in the long
[4:26] &gt;&gt; What would you want to keep in the long
[4:26] &gt;&gt; What would you want to keep in the long term? Sorry.
[4:28] term? Sorry.
[4:28] term? Sorry. &gt;&gt; What would you want to? So, between the
[4:30] &gt;&gt; What would you want to? So, between the
[4:30] &gt;&gt; What would you want to? So, between the Lab View software and this one, what's
[4:31] Lab View software and this one, what's
[4:31] Lab View software and this one, what's the um Why are there two?
[4:34] the um Why are there two?
[4:34] the um Why are there two? &gt;&gt; Well, because our system uh runs on Lab
[4:37] &gt;&gt; Well, because our system uh runs on Lab
[4:37] &gt;&gt; Well, because our system uh runs on Lab View. So, we made like a L view
[4:40] View. So, we made like a L view
[4:40] View. So, we made like a L view interface that works with this.
[4:42] interface that works with this.
[4:42] interface that works with this. &gt;&gt; So, everything works with Liew.
[4:44] &gt;&gt; So, everything works with Liew.
[4:44] &gt;&gt; So, everything works with Liew. &gt;&gt; So, you're pulling a real-time data
[4:46] &gt;&gt; So, you're pulling a real-time data
[4:46] &gt;&gt; So, you're pulling a real-time data stream from this um basically
[4:48] stream from this um basically
[4:48] stream from this um basically &gt;&gt; sensor and then that can be coordinated
[4:50] &gt;&gt; sensor and then that can be coordinated
[4:50] &gt;&gt; sensor and then that can be coordinated together with this. So, you could say
[4:52] together with this. So, you could say
[4:52] together with this. So, you could say whenever Oh my gosh, the options are
[4:55] whenever Oh my gosh, the options are
[4:55] whenever Oh my gosh, the options are like
[4:56] like
[4:56] like &gt;&gt; unreal. Yeah to do with it.
[4:59] &gt;&gt; unreal. Yeah to do with it.
[4:59] &gt;&gt; unreal. Yeah to do with it. &gt;&gt; The patient could say
[5:01] &gt;&gt; The patient could say
[5:01] &gt;&gt; The patient could say well have you have you received inputs
[5:03] well have you have you received inputs
[5:03] well have you have you received inputs from the medical field to say why what
[5:06] from the medical field to say why what
[5:06] from the medical field to say why what would you want to coordinate between the
[5:07] would you want to coordinate between the
[5:07] would you want to coordinate between the machine and the and the sensors.
[5:11] machine and the and the sensors.
[5:11] machine and the and the sensors. &gt;&gt; So um a healthy per so the idea this
[5:15] &gt;&gt; So um a healthy per so the idea this
[5:15] &gt;&gt; So um a healthy per so the idea this project is mainly for poststroke
[5:18] project is mainly for poststroke
[5:18] project is mainly for poststroke patients. So a lot of them if they
[5:21] patients. So a lot of them if they
[5:21] patients. So a lot of them if they survive the stroke itself they will lose
[5:23] survive the stroke itself they will lose
[5:23] survive the stroke itself they will lose motor skills and that's partially due to
[5:26] motor skills and that's partially due to
[5:26] motor skills and that's partially due to let's say either they won't their
[5:29] let's say either they won't their
[5:29] let's say either they won't their muscles won't receive proper signals
[5:30] muscles won't receive proper signals
[5:30] muscles won't receive proper signals from their brain right or nothing at
[5:32] from their brain right or nothing at
[5:32] from their brain right or nothing at all. So this will be a way to measure
[5:35] all. So this will be a way to measure
[5:35] all. So this will be a way to measure the level of impairment
[5:37] the level of impairment
[5:37] the level of impairment that they have due to the stroke.
[5:39] that they have due to the stroke.
[5:39] that they have due to the stroke. &gt;&gt; And if they slowly rehabilitate
[5:41] &gt;&gt; And if they slowly rehabilitate
[5:41] &gt;&gt; And if they slowly rehabilitate &gt;&gt; if they say I I feel like I can't even
[5:45] &gt;&gt; if they say I I feel like I can't even
[5:45] &gt;&gt; if they say I I feel like I can't even command this muscle that could be
[5:47] command this muscle that could be
[5:47] command this muscle that could be confirmed or
[5:49] confirmed or
[5:49] confirmed or &gt;&gt; you can confirm that let's say by the
[5:51] &gt;&gt; you can confirm that let's say by the
[5:51] &gt;&gt; you can confirm that let's say by the lack of torque produced from the patient
[5:53] lack of torque produced from the patient
[5:53] lack of torque produced from the patient or through the muscle signal.
[5:55] or through the muscle signal.
[5:55] or through the muscle signal. &gt;&gt; So if you could find a way to benchmark
[5:56] &gt;&gt; So if you could find a way to benchmark
[5:56] &gt;&gt; So if you could find a way to benchmark what the signal should look like if the
[5:58] what the signal should look like if the
[5:58] what the signal should look like if the person would be healthy versus what
[6:00] person would be healthy versus what
[6:00] person would be healthy versus what we're actually seeing. Let's say there's
[6:01] we're actually seeing. Let's say there's
[6:01] we're actually seeing. Let's say there's no signal at all or there's a weak
[6:04] no signal at all or there's a weak
[6:04] no signal at all or there's a weak signal. Then hopefully we can make a
[6:07] signal. Then hopefully we can make a
[6:07] signal. Then hopefully we can make a system that evaluates how much help does
[6:09] system that evaluates how much help does
[6:09] system that evaluates how much help does that person need through the robot
[6:11] that person need through the robot
[6:11] that person need through the robot without the need for a a therapist to
[6:14] without the need for a a therapist to
[6:14] without the need for a a therapist to like look at the patient and evaluate
[6:16] like look at the patient and evaluate
[6:16] like look at the patient and evaluate &gt;&gt; how much aid they need. So that's the
[6:18] &gt;&gt; how much aid they need. So that's the
[6:18] &gt;&gt; how much aid they need. So that's the idea.
[6:20] idea.
[6:20] idea. &gt;&gt; That's cool. Did for either of you guys
[6:23] &gt;&gt; That's cool. Did for either of you guys
[6:23] &gt;&gt; That's cool. Did for either of you guys did you have uh do you imagine a lot of
[6:27] did you have uh do you imagine a lot of
[6:27] did you have uh do you imagine a lot of future for this? like do you have a
[6:28] future for this? like do you have a
[6:28] future for this? like do you have a passion about this or for you right now
[6:30] passion about this or for you right now
[6:30] passion about this or for you right now it's just a subject for for you to get
[6:33] it's just a subject for for you to get
[6:33] it's just a subject for for you to get uh accomplish the PhD in control
[6:35] uh accomplish the PhD in control
[6:35] uh accomplish the PhD in control &gt;&gt; it's nice I mean the potential as you
[6:37] &gt;&gt; it's nice I mean the potential as you
[6:38] &gt;&gt; it's nice I mean the potential as you said there's a lot to do there's a lot
[6:39] said there's a lot to do there's a lot
[6:39] said there's a lot to do there's a lot of
[6:40] of
[6:40] of &gt;&gt; there's a big gap in research so
[6:42] &gt;&gt; there's a big gap in research so
[6:42] &gt;&gt; there's a big gap in research so everything I'm reading
[6:43] everything I'm reading
[6:43] everything I'm reading &gt;&gt; until now does not have proper basically
[6:47] &gt;&gt; until now does not have proper basically
[6:47] &gt;&gt; until now does not have proper basically a proper system that can evaluate the
[6:49] a proper system that can evaluate the
[6:49] a proper system that can evaluate the impairment of a patient we're really
[6:51] impairment of a patient we're really
[6:51] impairment of a patient we're really highly dependent on therapists so
[6:54] highly dependent on therapists so
[6:54] highly dependent on therapists so hopefully this can make therapy more
[6:56] hopefully this can make therapy more
[6:56] hopefully this can make therapy more accessible
[6:57] accessible
[6:58] accessible Um so yeah there's a lot of there's a
[7:00] Um so yeah there's a lot of there's a
[7:00] Um so yeah there's a lot of there's a big venue for this project and there's a
[7:02] big venue for this project and there's a
[7:02] big venue for this project and there's a lot of hope very difficult but hopefully
[7:05] lot of hope very difficult but hopefully
[7:05] lot of hope very difficult but hopefully it'll be worthwhile. Yeah. And once it
[7:07] it'll be worthwhile. Yeah. And once it
[7:07] it'll be worthwhile. Yeah. And once it gets to the mechanical um once it was
[7:11] gets to the mechanical um once it was
[7:11] gets to the mechanical um once it was established like the design was
[7:14] established like the design was
[7:14] established like the design was distributed to multiple research teams
[7:16] distributed to multiple research teams
[7:16] distributed to multiple research teams then a lot of trials and a lot of
[7:19] then a lot of trials and a lot of
[7:19] then a lot of trials and a lot of development could happen without the
[7:21] development could happen without the
[7:21] development could happen without the expensive equipment simply uh by
[7:25] expensive equipment simply uh by
[7:25] expensive equipment simply uh by um comparing data sets and and trying
[7:29] um comparing data sets and and trying
[7:29] um comparing data sets and and trying out new things that so a lot of brains
[7:32] out new things that so a lot of brains
[7:32] out new things that so a lot of brains could be uh collaborating on making it
[7:35] could be uh collaborating on making it
[7:35] could be uh collaborating on making it better and cheaper.
[7:36] better and cheaper.
[7:36] better and cheaper. quickly I think. Cool. And and is this
[7:40] quickly I think. Cool. And and is this
[7:40] quickly I think. Cool. And and is this designed to owned by um a supporting
[7:46] designed to owned by um a supporting
[7:46] designed to owned by um a supporting who who owns the the research material?
[7:51] who who owns the the research material?
[7:51] who who owns the the research material? So
[7:53] So
[7:53] So this was built inhouse in Texas&amp;
[8:03] Foundation.
[8:03] Foundation. So it's possible that we we could
[8:05] So it's possible that we we could
[8:05] So it's possible that we we could convince Dr. Langiri to let us open
[8:07] convince Dr. Langiri to let us open
[8:07] convince Dr. Langiri to let us open source it. We'll see
[8:09] source it. We'll see
[8:09] source it. We'll see &gt;&gt; maybe. So it's only it's only dependent
[8:12] &gt;&gt; maybe. So it's only it's only dependent
[8:12] &gt;&gt; maybe. So it's only it's only dependent on if there's private interests already
[8:14] on if there's private interests already
[8:14] on if there's private interests already having invested in this and whether they
[8:16] having invested in this and whether they
[8:16] having invested in this and whether they um they are expecting
[8:20] um they are expecting
[8:20] um they are expecting uh intellectual property back that's
[8:22] uh intellectual property back that's
[8:22] uh intellectual property back that's secured and only only belonging to them.
[8:24] secured and only only belonging to them.
[8:24] secured and only only belonging to them. &gt;&gt; Not sure those details honestly though.
[8:26] &gt;&gt; Not sure those details honestly though.
[8:26] &gt;&gt; Not sure those details honestly though. &gt;&gt; Neat. Okay. Uh I better stop
[8:28] &gt;&gt; Neat. Okay. Uh I better stop
[8:28] &gt;&gt; Neat. Okay. Uh I better stop interrupting the project today. We're
[8:30] interrupting the project today. We're
[8:30] interrupting the project today. We're supposed to get something dismantled and
[8:31] supposed to get something dismantled and
[8:31] supposed to get something dismantled and I've been delaying it a little bit. So,
[8:33] I've been delaying it a little bit. So,
[8:34] I've been delaying it a little bit. So, thanks you guys.
[8:36] thanks you guys.
[8:36] thanks you guys. So, right now, Abraham is dismantling.
[8:39] So, right now, Abraham is dismantling.
[8:39] So, right now, Abraham is dismantling. We're trying to get the the 3D [snorts]
[8:41] We're trying to get the the 3D [snorts]
[8:41] We're trying to get the the 3D [snorts] printed element disassembled from the
[8:45] printed element disassembled from the
[8:45] printed element disassembled from the aluminum machined parts. So, we can put
[8:48] aluminum machined parts. So, we can put
[8:48] aluminum machined parts. So, we can put on a new 3D print here that has been
[8:51] on a new 3D print here that has been
[8:51] on a new 3D print here that has been cracked. Maybe we'll find a better
[8:52] cracked. Maybe we'll find a better
[8:52] cracked. Maybe we'll find a better quality of a of a printed material
[8:55] quality of a of a printed material
[8:55] quality of a of a printed material that's tougher. But in the meantime, I'm
[8:58] that's tougher. But in the meantime, I'm
[8:58] that's tougher. But in the meantime, I'm over here looking back like 5 years into
[9:02] over here looking back like 5 years into
[9:02] over here looking back like 5 years into the past where I had I ordered this uh
[9:06] the past where I had I ordered this uh
[9:06] the past where I had I ordered this uh this drawer set for Dr. Ling Gary and
[9:09] this drawer set for Dr. Ling Gary and
[9:09] this drawer set for Dr. Ling Gary and some of the organizing bins and I'm
[9:12] some of the organizing bins and I'm
[9:12] some of the organizing bins and I'm seeing what uh some confirmation of my
[9:15] seeing what uh some confirmation of my
[9:16] seeing what uh some confirmation of my theory.
[9:17] theory.
[9:17] theory. several years back, these parts did not
[9:19] several years back, these parts did not
[9:19] several years back, these parts did not exist. And these are these miscellaneous
[9:23] exist. And these are these miscellaneous
[9:23] exist. And these are these miscellaneous uh seemingly unimportant detailed parts,
[9:27] uh seemingly unimportant detailed parts,
[9:27] uh seemingly unimportant detailed parts, but that what's expensive about these
[9:31] but that what's expensive about these
[9:31] but that what's expensive about these zip ties is not that they cost a lot or
[9:35] zip ties is not that they cost a lot or
[9:35] zip ties is not that they cost a lot or that they're these are particularly
[9:37] that they're these are particularly
[9:37] that they're these are particularly important, but to take the researchers
[9:39] important, but to take the researchers
[9:39] important, but to take the researchers time to shop and identify and find a
[9:42] time to shop and identify and find a
[9:42] time to shop and identify and find a supplier and a choice for every single
[9:44] supplier and a choice for every single
[9:44] supplier and a choice for every single one of these. And if 4 in wasn't exactly
[9:47] one of these. And if 4 in wasn't exactly
[9:47] one of these. And if 4 in wasn't exactly right and then they had to get 4 and 1/2
[9:49] right and then they had to get 4 and 1/2
[9:49] right and then they had to get 4 and 1/2 in, all of that time is just huge
[9:53] in, all of that time is just huge
[9:53] in, all of that time is just huge investment of uh a 12-year-old kid could
[9:56] investment of uh a 12-year-old kid could
[9:56] investment of uh a 12-year-old kid could be doing it, but we have our our
[9:59] be doing it, but we have our our
[9:59] be doing it, but we have our our worldass researchers doing it. Well, if
[10:02] worldass researchers doing it. Well, if
[10:02] worldass researchers doing it. Well, if we use open lab to take the identify
[10:07] we use open lab to take the identify
[10:07] we use open lab to take the identify these things that are recurring in every
[10:08] these things that are recurring in every
[10:08] these things that are recurring in every single remember how I I made a tape
[10:11] single remember how I I made a tape
[10:11] single remember how I I made a tape video with 30 different tapes and you're
[10:14] video with 30 different tapes and you're
[10:14] video with 30 different tapes and you're going to find five of them here
[10:16] going to find five of them here
[10:16] going to find five of them here incidentally just just by coincidence
[10:19] incidentally just just by coincidence
[10:19] incidentally just just by coincidence you ended up needing the same things
[10:21] you ended up needing the same things
[10:21] you ended up needing the same things that I have there. And so if I make this
[10:24] that I have there. And so if I make this
[10:24] that I have there. And so if I make this list, I published the the examples.
[10:26] list, I published the the examples.
[10:26] list, I published the the examples. Here's a template list of supplies that
[10:28] Here's a template list of supplies that
[10:28] Here's a template list of supplies that we need. And then the the operators of
[10:31] we need. And then the the operators of
[10:32] we need. And then the the operators of labs,
[10:33] labs,
[10:33] labs, um Dr. and Gary can get the the
[10:37] um Dr. and Gary can get the the
[10:37] um Dr. and Gary can get the the necessary components equipped so that
[10:39] necessary components equipped so that
[10:39] necessary components equipped so that when students come in from around the
[10:41] when students come in from around the
[10:41] when students come in from around the world to do their their research on a
[10:43] world to do their their research on a
[10:43] world to do their their research on a robot thing, then they can have um what
[10:47] robot thing, then they can have um what
[10:47] robot thing, then they can have um what like 50% of their effort already handled
[10:52] like 50% of their effort already handled
[10:52] like 50% of their effort already handled because we want to solve this problem
[10:54] because we want to solve this problem
[10:54] because we want to solve this problem one time and then keep it permanently.
[10:57] one time and then keep it permanently.
[10:57] one time and then keep it permanently. not solve it every single time that
[10:59] not solve it every single time that
[10:59] not solve it every single time that somebody comes into the room and and do
[11:01] somebody comes into the room and and do
[11:02] somebody comes into the room and and do a whole discovery process because they
[11:04] a whole discovery process because they
[11:04] a whole discovery process because they may not know that uh they might not know
[11:07] may not know that uh they might not know
[11:07] may not know that uh they might not know the materials of every single one of
[11:09] the materials of every single one of
[11:09] the materials of every single one of these things. And so the the mechanical
[11:12] these things. And so the the mechanical
[11:12] these things. And so the the mechanical engineer sits and studies every
[11:14] engineer sits and studies every
[11:14] engineer sits and studies every different material of every tape that
[11:15] different material of every tape that
[11:15] different material of every tape that comes out to find out what would be
[11:18] comes out to find out what would be
[11:18] comes out to find out what would be appropriate
[11:20] appropriate
[11:20] appropriate and then samples it and tries it out and
[11:22] and then samples it and tries it out and
[11:22] and then samples it and tries it out and wears the technician hat and just redo
[11:25] wears the technician hat and just redo
[11:25] wears the technician hat and just redo the same work as the the last generation
[11:28] the same work as the the last generation
[11:28] the same work as the the last generation of the PhD here over and over and over.
[11:32] of the PhD here over and over and over.
[11:32] of the PhD here over and over and over. And uh I think we can I think we can
[11:36] And uh I think we can I think we can
[11:36] And uh I think we can I think we can improve that a huge amount and that will
[11:37] improve that a huge amount and that will
[11:37] improve that a huge amount and that will be through publishing at least a
[11:40] be through publishing at least a
[11:40] be through publishing at least a starting point will be open lab. Um
[11:43] starting point will be open lab. Um
[11:44] starting point will be open lab. Um every single every single item in here I
[11:48] every single every single item in here I
[11:48] every single every single item in here I can see there are new stuff that was
[11:49] can see there are new stuff that was
[11:49] can see there are new stuff that was just ordered because oh now we need a
[11:52] just ordered because oh now we need a
[11:52] just ordered because oh now we need a general oil now we need a lubricant for
[11:54] general oil now we need a lubricant for
[11:54] general oil now we need a lubricant for plastic gears and they they're all the
[11:57] plastic gears and they they're all the
[11:57] plastic gears and they they're all the same uh items that I already identified.
[12:01] same uh items that I already identified.
[12:01] same uh items that I already identified. So that makes me happy. I don't have
[12:02] So that makes me happy. I don't have
[12:02] So that makes me happy. I don't have anyone uh anyone really cheering me on
[12:06] anyone uh anyone really cheering me on
[12:06] anyone uh anyone really cheering me on and saying, "Wow, it's really important
[12:07] and saying, "Wow, it's really important
[12:07] and saying, "Wow, it's really important for you to name a kind of zip tie, but
[12:11] for you to name a kind of zip tie, but
[12:11] for you to name a kind of zip tie, but it is important because this this
[12:13] it is important because this this
[12:13] it is important because this this research is how we're going to
[12:16] research is how we're going to
[12:16] research is how we're going to make the world better. And if it costs a
[12:19] make the world better. And if it costs a
[12:19] make the world better. And if it costs a million dollars to make the world this
[12:22] million dollars to make the world this
[12:22] million dollars to make the world this much better, then it won't won't get
[12:24] much better, then it won't won't get
[12:24] much better, then it won't won't get better very quickly."
[12:33] This is one that I need to get inside of
[12:34] This is one that I need to get inside of simply a driver tool, but it has a nice
[12:37] simply a driver tool, but it has a nice
[12:37] simply a driver tool, but it has a nice bearing on the back. So, we could
[12:40] bearing on the back. So, we could
[12:40] bearing on the back. So, we could identify a good brand of this. It has
[12:42] identify a good brand of this. It has
[12:42] identify a good brand of this. It has its own little collet just like that one
[12:45] its own little collet just like that one
[12:45] its own little collet just like that one found on the Dremel. Okay. Oh, this is
[12:49] found on the Dremel. Okay. Oh, this is
[12:49] found on the Dremel. Okay. Oh, this is what the gearbox.
[12:51] what the gearbox.
[12:51] what the gearbox. &gt;&gt; Yeah,
[12:51] &gt;&gt; Yeah,
[12:51] &gt;&gt; Yeah, &gt;&gt; the um synchronous
[12:57] what do they call it? harmonic gearbox.
[12:57] what do they call it? harmonic gearbox. &gt;&gt; Yes.
[12:58] &gt;&gt; Yes.
[12:58] &gt;&gt; Yes. &gt;&gt; Oh, you can see the
[12:59] &gt;&gt; Oh, you can see the
[12:59] &gt;&gt; Oh, you can see the &gt;&gt; the gap up on this side and not on that
[13:02] &gt;&gt; the gap up on this side and not on that
[13:02] &gt;&gt; the gap up on this side and not on that side. So, that's showing its position.
[13:05] side. So, that's showing its position.
[13:05] side. So, that's showing its position. Oh, yeah.
[13:06] Oh, yeah.
[13:06] Oh, yeah. &gt;&gt; Oh, yeah. Well, you should know. I'm
[13:08] &gt;&gt; Oh, yeah. Well, you should know. I'm
[13:08] &gt;&gt; Oh, yeah. Well, you should know. I'm glad I did that because you you need to
[13:10] glad I did that because you you need to
[13:10] glad I did that because you you need to know what's loose and what's
[13:12] know what's loose and what's
[13:12] know what's loose and what's &gt;&gt; like
[13:14] &gt;&gt; like
[13:14] &gt;&gt; like Okay. And there's that the D-shaped
[13:16] Okay. And there's that the D-shaped
[13:16] Okay. And there's that the D-shaped shaft. Um,
[13:18] shaft. Um,
[13:18] shaft. Um, so when you go to position your shaft,
[13:20] so when you go to position your shaft,
[13:20] so when you go to position your shaft, that'll
[13:21] that'll
[13:21] that'll &gt;&gt; that'll be your flat spot.
[13:24] &gt;&gt; that'll be your flat spot.
[13:24] &gt;&gt; that'll be your flat spot. This is the ma the male part to that
[13:26] This is the ma the male part to that
[13:26] This is the ma the male part to that female. And
[13:28] female. And
[13:28] female. And &gt;&gt; then this is I guess the aluminum is
[13:31] &gt;&gt; then this is I guess the aluminum is
[13:31] &gt;&gt; then this is I guess the aluminum is fixed to the plastic.
[13:32] fixed to the plastic.
[13:32] fixed to the plastic. &gt;&gt; Yeah.
[13:32] &gt;&gt; Yeah.
[13:32] &gt;&gt; Yeah. &gt;&gt; So that's how you're transmitting the
[13:34] &gt;&gt; So that's how you're transmitting the
[13:34] &gt;&gt; So that's how you're transmitting the torque to the plastic.
[13:37] torque to the plastic.
[13:37] torque to the plastic. And these three screws are setting it in
[13:39] And these three screws are setting it in
[13:39] And these three screws are setting it in there.
[13:41] there.
[13:41] there. &gt;&gt; What is this? Your motor?
[13:43] &gt;&gt; What is this? Your motor?
[13:43] &gt;&gt; What is this? Your motor? &gt;&gt; Yeah, the motor is back here.
[13:45] &gt;&gt; Yeah, the motor is back here.
[13:45] &gt;&gt; Yeah, the motor is back here. &gt;&gt; Oh, so when this
[13:48] &gt;&gt; Oh, so when this
[13:48] &gt;&gt; Oh, so when this Okay, directly driving that shaft. Cool.
[13:53] Okay, directly driving that shaft. Cool.
[13:53] Okay, directly driving that shaft. Cool. Okay. What's the next question? I think
[13:54] Okay. What's the next question? I think
[13:54] Okay. What's the next question? I think you can just take out these three
[13:55] you can just take out these three
[13:55] you can just take out these three screws.
[13:56] screws.
[13:56] screws. &gt;&gt; The problem is like I was removing it,
[13:57] &gt;&gt; The problem is like I was removing it,
[13:57] &gt;&gt; The problem is like I was removing it, but it's kind of chipping.
[14:00] but it's kind of chipping.
[14:00] but it's kind of chipping. &gt;&gt; What was chipping?
[14:01] &gt;&gt; What was chipping?
[14:01] &gt;&gt; What was chipping? &gt;&gt; Oh, see.
[14:02] &gt;&gt; Oh, see.
[14:02] &gt;&gt; Oh, see. &gt;&gt; Okay, let's I'll help you verify the
[14:04] &gt;&gt; Okay, let's I'll help you verify the
[14:04] &gt;&gt; Okay, let's I'll help you verify the right uh size of that X.
[14:08] right uh size of that X.
[14:08] right uh size of that X. Okay, I'm going to share one solution um
[14:11] Okay, I'm going to share one solution um
[14:11] Okay, I'm going to share one solution um that I discussed with my two new
[14:14] that I discussed with my two new
[14:14] that I discussed with my two new researcher friends um and the
[14:17] researcher friends um and the
[14:17] researcher friends um and the methodology that goes together with it.
[14:18] methodology that goes together with it.
[14:18] methodology that goes together with it. This is regarding the screw torque on an
[14:22] This is regarding the screw torque on an
[14:22] This is regarding the screw torque on an existing assembly that you're just now
[14:24] existing assembly that you're just now
[14:24] existing assembly that you're just now working with. Um, so they have a tool in
[14:27] working with. Um, so they have a tool in
[14:27] working with. Um, so they have a tool in their lab that I don't have yet. Um,
[14:29] their lab that I don't have yet. Um,
[14:29] their lab that I don't have yet. Um, it's a handheld torque screwdriver just
[14:32] it's a handheld torque screwdriver just
[14:32] it's a handheld torque screwdriver just like a torque wrench. It can tighten a a
[14:36] like a torque wrench. It can tighten a a
[14:36] like a torque wrench. It can tighten a a screw to a certain um a fastener to a
[14:39] screw to a certain um a fastener to a
[14:40] screw to a certain um a fastener to a certain amount of torque. Okay. And then
[14:43] certain amount of torque. Okay. And then
[14:43] certain amount of torque. Okay. And then this collar here can't do any pointing
[14:46] this collar here can't do any pointing
[14:46] this collar here can't do any pointing right now. The collar is rotated until
[14:49] right now. The collar is rotated until
[14:49] right now. The collar is rotated until you reach the numeric value that you're
[14:51] you reach the numeric value that you're
[14:51] you reach the numeric value that you're looking for. And then just like another
[14:53] looking for. And then just like another
[14:53] looking for. And then just like another screwdriver with the hex drive outlet,
[14:56] screwdriver with the hex drive outlet,
[14:56] screwdriver with the hex drive outlet, um you will hand tighten this until you
[14:59] um you will hand tighten this until you
[14:59] um you will hand tighten this until you reach that. And this is good for much
[15:02] reach that. And this is good for much
[15:02] reach that. And this is good for much lower torques like handheld uh levels of
[15:05] lower torques like handheld uh levels of
[15:05] lower torques like handheld uh levels of torque compared with the big torque
[15:07] torque compared with the big torque
[15:07] torque compared with the big torque wrench that I have. That is my the
[15:10] wrench that I have. That is my the
[15:10] wrench that I have. That is my the father the style my father had in
[15:12] father the style my father had in
[15:12] father the style my father had in working as a mechanic. And so this is
[15:16] working as a mechanic. And so this is
[15:16] working as a mechanic. And so this is good for the tightening phase. But then
[15:18] good for the tightening phase. But then
[15:18] good for the tightening phase. But then you have the removal phase where um
[15:21] you have the removal phase where um
[15:21] you have the removal phase where um instead of performing the tightness to
[15:24] instead of performing the tightness to
[15:24] instead of performing the tightness to the spec, we want to discover the spec
[15:26] the spec, we want to discover the spec
[15:26] the spec, we want to discover the spec by uh by measuring. So this one is less
[15:29] by uh by measuring. So this one is less
[15:29] by uh by measuring. So this one is less good for measuring although you can get
[15:31] good for measuring although you can get
[15:31] good for measuring although you can get a ballpark. Basically when this gets
[15:34] a ballpark. Basically when this gets
[15:34] a ballpark. Basically when this gets tight to when it reaches the value
[15:38] tight to when it reaches the value
[15:38] tight to when it reaches the value indicated on its uh on its scale, then
[15:41] indicated on its uh on its scale, then
[15:41] indicated on its uh on its scale, then it will do a click while you're
[15:43] it will do a click while you're
[15:43] it will do a click while you're tightening. then it'll be interrupted by
[15:45] tightening. then it'll be interrupted by
[15:45] tightening. then it'll be interrupted by a a click and then you'll know that you
[15:47] a a click and then you'll know that you
[15:47] a a click and then you'll know that you reached that. So if your screw is 1
[15:50] reached that. So if your screw is 1
[15:50] reached that. So if your screw is 1 Newton meter of tightness and you set
[15:54] Newton meter of tightness and you set
[15:54] Newton meter of tightness and you set this to 0.8 before the screw starts
[15:57] this to 0.8 before the screw starts
[15:57] this to 0.8 before the screw starts moving, you will feel the click and
[15:59] moving, you will feel the click and
[15:59] moving, you will feel the click and you'll know that the screw is more than
[16:01] you'll know that the screw is more than
[16:01] you'll know that the screw is more than 0.8 Newton meters of torque in how tight
[16:06] 0.8 Newton meters of torque in how tight
[16:06] 0.8 Newton meters of torque in how tight it is. Okay. So uh the other tool that
[16:09] it is. Okay. So uh the other tool that
[16:09] it is. Okay. So uh the other tool that I'm recommending that I do not yet have
[16:12] I'm recommending that I do not yet have
[16:12] I'm recommending that I do not yet have in open lab. So this is an example of a
[16:14] in open lab. So this is an example of a
[16:14] in open lab. So this is an example of a beam style to work wrench and this is
[16:17] beam style to work wrench and this is
[16:17] beam style to work wrench and this is recommended to have in a mechanical lab
[16:21] recommended to have in a mechanical lab
[16:21] recommended to have in a mechanical lab of for any kind of mechanical projects
[16:24] of for any kind of mechanical projects
[16:24] of for any kind of mechanical projects and this is uh with the square drive on
[16:26] and this is uh with the square drive on
[16:26] and this is uh with the square drive on it. It's a I think it's a quarter inch.
[16:28] it. It's a I think it's a quarter inch.
[16:28] it. It's a I think it's a quarter inch. So this is smaller
[16:30] So this is smaller
[16:30] So this is smaller um it says 0 to 80 inchbs and my unit is
[16:33] um it says 0 to 80 inchbs and my unit is
[16:33] um it says 0 to 80 inchbs and my unit is a larger one. Uh so it's less capable to
[16:36] a larger one. Uh so it's less capable to
[16:36] a larger one. Uh so it's less capable to measure these small uh fine units but
[16:39] measure these small uh fine units but
[16:40] measure these small uh fine units but basically you have a a bending moment of
[16:43] basically you have a a bending moment of
[16:43] basically you have a a bending moment of inertia of this beam and since you will
[16:46] inertia of this beam and since you will
[16:46] inertia of this beam and since you will bend it as you push on the end and
[16:49] bend it as you push on the end and
[16:49] bend it as you push on the end and tighten the screw then this upper beam
[16:51] tighten the screw then this upper beam
[16:51] tighten the screw then this upper beam will stay still and indicate the torque.
[16:54] will stay still and indicate the torque.
[16:54] will stay still and indicate the torque. Okay, we might as well uh mention
[16:56] Okay, we might as well uh mention
[16:56] Okay, we might as well uh mention economy as well. So this unit is a very
[16:59] economy as well. So this unit is a very
[16:59] economy as well. So this unit is a very reputable brand that comes from Germany.
[17:01] reputable brand that comes from Germany.
[17:01] reputable brand that comes from Germany. Vera is a famous brand and this device
[17:04] Vera is a famous brand and this device
[17:04] Vera is a famous brand and this device isund almost $120.
[17:07] isund almost $120.
[17:08] isund almost $120. Um so that is not a a cheap tool. I
[17:11] Um so that is not a a cheap tool. I
[17:11] Um so that is not a a cheap tool. I would say that's above the affordable
[17:13] would say that's above the affordable
[17:13] would say that's above the affordable range. Now I'd say after 2020, after
[17:18] range. Now I'd say after 2020, after
[17:18] range. Now I'd say after 2020, after 2015,
[17:19] 2015,
[17:19] 2015, several new brands came onto the market
[17:21] several new brands came onto the market
[17:22] several new brands came onto the market and so there are alternative options
[17:24] and so there are alternative options
[17:24] and so there are alternative options that will do just as well, but we don't
[17:26] that will do just as well, but we don't
[17:26] that will do just as well, but we don't necessarily know what those options are
[17:29] necessarily know what those options are
[17:29] necessarily know what those options are as uh as consumers. And so one of the
[17:32] as uh as consumers. And so one of the
[17:32] as uh as consumers. And so one of the intentions of open lab is um someone
[17:35] intentions of open lab is um someone
[17:35] intentions of open lab is um someone like me can purchase a lowerc cost one
[17:38] like me can purchase a lowerc cost one
[17:38] like me can purchase a lowerc cost one but this is a risk of maybe it won't be
[17:41] but this is a risk of maybe it won't be
[17:41] but this is a risk of maybe it won't be up to mechanical
[17:44] up to mechanical
[17:44] up to mechanical desirable quality and then it shouldn't
[17:47] desirable quality and then it shouldn't
[17:47] desirable quality and then it shouldn't get listed on open lab the so finding
[17:51] get listed on open lab the so finding
[17:51] get listed on open lab the so finding the best community favorite that that
[17:54] the best community favorite that that
[17:54] the best community favorite that that does meet the needs at the minimum
[17:56] does meet the needs at the minimum
[17:56] does meet the needs at the minimum starting price that's pretty relevant uh
[17:59] starting price that's pretty relevant uh
[17:59] starting price that's pretty relevant uh something that I'd like to do and with
[18:00] something that I'd like to do and with
[18:00] something that I'd like to do and with the help of the community you can feel
[18:02] the help of the community you can feel
[18:02] the help of the community you can feel free to add names uh brands and or model
[18:06] free to add names uh brands and or model
[18:06] free to add names uh brands and or model numbers in the comments and no I opened
[18:09] numbers in the comments and no I opened
[18:09] numbers in the comments and no I opened this one even though I don't have this
[18:11] this one even though I don't have this
[18:11] this one even though I don't have this model this is the the quarter inch drive
[18:13] model this is the the quarter inch drive
[18:14] model this is the the quarter inch drive size compared with my let's say half
[18:17] size compared with my let's say half
[18:17] size compared with my let's say half inch drive or 38 um this one will give
[18:19] inch drive or 38 um this one will give
[18:20] inch drive or 38 um this one will give you finer measurements but still not
[18:22] you finer measurements but still not
[18:22] you finer measurements but still not quite at the low range of this wear tool
[18:25] quite at the low range of this wear tool
[18:25] quite at the low range of this wear tool so both of these are useful and they're
[18:27] so both of these are useful and they're
[18:28] so both of these are useful and they're they're mutually excl exclusive jobs to
[18:31] they're mutually excl exclusive jobs to
[18:31] they're mutually excl exclusive jobs to be done. Um, they have overlapping
[18:33] be done. Um, they have overlapping
[18:33] be done. Um, they have overlapping functions, but both have a have a
[18:35] functions, but both have a have a
[18:35] functions, but both have a have a purpose.
[18:41] And I've pulled this one up on screen
[18:41] And I've pulled this one up on screen because uh, No is a brand that does have
[18:45] because uh, No is a brand that does have
[18:45] because uh, No is a brand that does have a solid reputation, although it's
[18:47] a solid reputation, although it's
[18:47] a solid reputation, although it's affordable. So, $25 for this unit.
[18:49] affordable. So, $25 for this unit.
[18:49] affordable. So, $25 for this unit. That's um, uh, the brand originates in
[18:53] That's um, uh, the brand originates in
[18:53] That's um, uh, the brand originates in Taiwan. So, they're made in THI Taiwan
[18:55] Taiwan. So, they're made in THI Taiwan
[18:55] Taiwan. So, they're made in THI Taiwan andor China, but um but this brand does
[18:59] andor China, but um but this brand does
[18:59] andor China, but um but this brand does have a a name to uphold. Okay. And so,
[19:02] have a a name to uphold. Okay. And so,
[19:02] have a a name to uphold. Okay. And so, without any experience information, a
[19:04] without any experience information, a
[19:04] without any experience information, a friend to advise a brand, I would
[19:06] friend to advise a brand, I would
[19:06] friend to advise a brand, I would probably choose that. This is the method
[19:10] probably choose that. This is the method
[19:10] probably choose that. This is the method to discover the torque spec on an
[19:13] to discover the torque spec on an
[19:13] to discover the torque spec on an assembly that's already been assembled
[19:14] assembly that's already been assembled
[19:14] assembly that's already been assembled and you don't have the torque spec
[19:16] and you don't have the torque spec
[19:16] and you don't have the torque spec written down anymore. So by
[19:18] written down anymore. So by
[19:18] written down anymore. So by disassembling uh we'll measure and then
[19:21] disassembling uh we'll measure and then
[19:21] disassembling uh we'll measure and then we're going to make a note of the torque
[19:23] we're going to make a note of the torque
[19:23] we're going to make a note of the torque spec and record that so we have it in
[19:25] spec and record that so we have it in
[19:25] spec and record that so we have it in our documentation. So before this dotted
[19:28] our documentation. So before this dotted
[19:28] our documentation. So before this dotted line someone else has uh tightened the
[19:30] line someone else has uh tightened the
[19:30] line someone else has uh tightened the fasteners to the spec assuming that the
[19:33] fasteners to the spec assuming that the
[19:33] fasteners to the spec assuming that the expert has the has already built the
[19:35] expert has the has already built the
[19:35] expert has the has already built the assembly then we begin down here under
[19:37] assembly then we begin down here under
[19:37] assembly then we begin down here under the dash line and we're going to make a
[19:39] the dash line and we're going to make a
[19:39] the dash line and we're going to make a mark on the fastener. And so we'll say
[19:42] mark on the fastener. And so we'll say
[19:42] mark on the fastener. And so we'll say for example um you could say that this
[19:45] for example um you could say that this
[19:45] for example um you could say that this is our fastener that has a uh a
[19:48] is our fastener that has a uh a
[19:48] is our fastener that has a uh a sensitive specification for the torque
[19:51] sensitive specification for the torque
[19:51] sensitive specification for the torque or you don't know if it's sensitive and
[19:53] or you don't know if it's sensitive and
[19:53] or you don't know if it's sensitive and you want to just be sure. And so we grab
[19:56] you want to just be sure. And so we grab
[19:56] you want to just be sure. And so we grab our torque wrench and this is the the
[19:59] our torque wrench and this is the the
[19:59] our torque wrench and this is the the beam style one. This one's better for
[20:01] beam style one. This one's better for
[20:01] beam style one. This one's better for reading while the click style is better
[20:04] reading while the click style is better
[20:04] reading while the click style is better for uh performing the the tightening.
[20:08] for uh performing the the tightening.
[20:08] for uh performing the the tightening. All right. And so we're going to move
[20:09] All right. And so we're going to move
[20:09] All right. And so we're going to move this. And I can feel as I press down on
[20:13] this. And I can feel as I press down on
[20:13] this. And I can feel as I press down on here. I'll fix the camera.
[20:16] here. I'll fix the camera.
[20:16] here. I'll fix the camera. I can actually feel from experience. I
[20:18] I can actually feel from experience. I
[20:18] I can actually feel from experience. I can feel when the bolt starts to move.
[20:20] can feel when the bolt starts to move.
[20:20] can feel when the bolt starts to move. It's already moving right away. This one
[20:22] It's already moving right away. This one
[20:22] It's already moving right away. This one doesn't take much torque. Um, but
[20:25] doesn't take much torque. Um, but
[20:25] doesn't take much torque. Um, but otherwise, if you can't feel it, you can
[20:27] otherwise, if you can't feel it, you can
[20:27] otherwise, if you can't feel it, you can have this mark here just to make sure
[20:29] have this mark here just to make sure
[20:29] have this mark here just to make sure because you don't want to overtighten it
[20:30] because you don't want to overtighten it
[20:30] because you don't want to overtighten it during this process just to and break
[20:32] during this process just to and break
[20:32] during this process just to and break something. Okay. So, however much it
[20:34] something. Okay. So, however much it
[20:34] something. Okay. So, however much it takes to turn that. I'm going to tighten
[20:36] takes to turn that. I'm going to tighten
[20:36] takes to turn that. I'm going to tighten it a little bit more just so we can get
[20:37] it a little bit more just so we can get
[20:38] it a little bit more just so we can get some deflection. All right. So, while
[20:40] some deflection. All right. So, while
[20:40] some deflection. All right. So, while I'm pushing, before anything turns at
[20:42] I'm pushing, before anything turns at
[20:42] I'm pushing, before anything turns at all, I'm getting this increase on my
[20:45] all, I'm getting this increase on my
[20:45] all, I'm getting this increase on my measure. And, uh, many of these have a
[20:48] measure. And, uh, many of these have a
[20:48] measure. And, uh, many of these have a little plastic tab that will record the
[20:51] little plastic tab that will record the
[20:51] little plastic tab that will record the peak and it'll slide out of place. In
[20:54] peak and it'll slide out of place. In
[20:54] peak and it'll slide out of place. In this case, I don't have it.
[20:57] this case, I don't have it.
[20:57] this case, I don't have it. So, if it's very important, I might uh,
[21:00] So, if it's very important, I might uh,
[21:00] So, if it's very important, I might uh, I don't know, put this piece of magnet
[21:02] I don't know, put this piece of magnet
[21:02] I don't know, put this piece of magnet here, and I can see how far the magnet
[21:04] here, and I can see how far the magnet
[21:04] here, and I can see how far the magnet moves. So, that's going to be my
[21:06] moves. So, that's going to be my
[21:06] moves. So, that's going to be my indicator. All right. So then I turn
[21:09] indicator. All right. So then I turn
[21:09] indicator. All right. So then I turn until the bolt just starts to tighten.
[21:12] until the bolt just starts to tighten.
[21:12] until the bolt just starts to tighten. And I'm going even tighter. I know I'm
[21:15] And I'm going even tighter. I know I'm
[21:15] And I'm going even tighter. I know I'm disassembling, but before I disassemble,
[21:17] disassembling, but before I disassemble,
[21:17] disassembling, but before I disassemble, I'm going to tighten it just to detect
[21:19] I'm going to tighten it just to detect
[21:19] I'm going to tighten it just to detect something. Taking that uh nut and
[21:22] something. Taking that uh nut and
[21:22] something. Taking that uh nut and tightening it further will be in the
[21:24] tightening it further will be in the
[21:24] tightening it further will be in the same direction that previously was was
[21:27] same direction that previously was was
[21:27] same direction that previously was was and therefore the friction will be in
[21:30] and therefore the friction will be in
[21:30] and therefore the friction will be in the same mechanical interlockings can
[21:33] the same mechanical interlockings can
[21:33] the same mechanical interlockings can happen. So you are more consistent.
[21:35] happen. So you are more consistent.
[21:35] happen. So you are more consistent. you'll get a better reading going the
[21:37] you'll get a better reading going the
[21:37] you'll get a better reading going the same direction as the assembly, not
[21:39] same direction as the assembly, not
[21:39] same direction as the assembly, not counterclockwise for this measurement.
[21:42] counterclockwise for this measurement.
[21:42] counterclockwise for this measurement. So, I can see on my readout that I
[21:45] So, I can see on my readout that I
[21:45] So, I can see on my readout that I reached 200 inb. And so, that's the
[21:49] reached 200 inb. And so, that's the
[21:49] reached 200 inb. And so, that's the value that I can write down and record
[21:51] value that I can write down and record
[21:51] value that I can write down and record together with with this machine wherever
[21:54] together with with this machine wherever
[21:54] together with with this machine wherever I'm keeping the documentation. Now, that
[21:56] I'm keeping the documentation. Now, that
[21:56] I'm keeping the documentation. Now, that gets recorded. Um, and we're all done.
[22:00] gets recorded. Um, and we're all done.
[22:00] gets recorded. Um, and we're all done. When we go, we can disassemble the whole
[22:02] When we go, we can disassemble the whole
[22:02] When we go, we can disassemble the whole thing. And when we put it back together,
[22:04] thing. And when we put it back together,
[22:04] thing. And when we put it back together, we use the same value. Now, this is what
[22:08] we use the same value. Now, this is what
[22:08] we use the same value. Now, this is what we call the click style torque wrench.
[22:10] we call the click style torque wrench.
[22:10] we call the click style torque wrench. And this is a huge one. It's for much
[22:12] And this is a huge one. It's for much
[22:12] And this is a huge one. It's for much bigger numbers. Um, and this one is the
[22:15] bigger numbers. Um, and this one is the
[22:16] bigger numbers. Um, and this one is the one you would use during the assembly
[22:17] one you would use during the assembly
[22:17] one you would use during the assembly process. You would twist this and dial
[22:20] process. You would twist this and dial
[22:20] process. You would twist this and dial it up to the the proper torque and then
[22:23] it up to the the proper torque and then
[22:23] it up to the the proper torque and then start to use it. And when you reach the
[22:25] start to use it. And when you reach the
[22:25] start to use it. And when you reach the tightness uh desired, then it will it
[22:27] tightness uh desired, then it will it
[22:27] tightness uh desired, then it will it will click. There will be a little gap.
[22:29] will click. There will be a little gap.
[22:29] will click. There will be a little gap. Um, and each one of those comes with its
[22:32] Um, and each one of those comes with its
[22:32] Um, and each one of those comes with its own manual and so forth. But, uh, even
[22:35] own manual and so forth. But, uh, even
[22:35] own manual and so forth. But, uh, even this can, even though it can go to, I
[22:37] this can, even though it can go to, I
[22:37] this can, even though it can go to, I don't know, 200 foot-pounds, uh, we want
[22:41] don't know, 200 foot-pounds, uh, we want
[22:41] don't know, 200 foot-pounds, uh, we want to have a smaller version of the same
[22:43] to have a smaller version of the same
[22:43] to have a smaller version of the same exact tool because of the the resolution
[22:46] exact tool because of the the resolution
[22:46] exact tool because of the the resolution on a smaller one will be much more
[22:47] on a smaller one will be much more
[22:47] on a smaller one will be much more appropriate for uh, for some small
[22:50] appropriate for uh, for some small
[22:50] appropriate for uh, for some small assemblies. And that's why I want to
[22:52] assemblies. And that's why I want to
[22:52] assemblies. And that's why I want to order the one that they have at the at
[22:54] order the one that they have at the at
[22:54] order the one that they have at the at their lab. So to summarize, the
[22:56] their lab. So to summarize, the
[22:56] their lab. So to summarize, the tightening task, it's best to use the
[22:58] tightening task, it's best to use the
[22:58] tightening task, it's best to use the click type and the measuring task, it's
[23:01] click type and the measuring task, it's
[23:01] click type and the measuring task, it's best to use the beam type. And yeah, for
[23:04] best to use the beam type. And yeah, for
[23:04] best to use the beam type. And yeah, for anyone in my audience who has the
[23:05] anyone in my audience who has the
[23:06] anyone in my audience who has the experience and has purchased a an
[23:08] experience and has purchased a an
[23:08] experience and has purchased a an economical version of that small
[23:10] economical version of that small
[23:10] economical version of that small handheld uh torque tool, I would love to
[23:12] handheld uh torque tool, I would love to
[23:12] handheld uh torque tool, I would love to know a brand uh that's costs less than
[23:15] know a brand uh that's costs less than
[23:15] know a brand uh that's costs less than the wearer version. And I think the
[23:16] the wearer version. And I think the
[23:16] the wearer version. And I think the audience also would like to know. So,
[23:18] audience also would like to know. So,
[23:18] audience also would like to know. So, please drop one in the comments if you
[23:19] please drop one in the comments if you
[23:19] please drop one in the comments if you have the information on

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
