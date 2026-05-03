---
title: "Human-inspired / Bio-inspired Ideas MISSING in Modern Robots"
url: "https://www.youtube.com/watch?v=5sXRnYCKep4"
video_id: "5sXRnYCKep4"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2023-06-16
duration: "12:15"
duration_sec: 735
views: 588
likes: 26
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/5sXRnYCKep4/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 534
chapters_count: 8
has_description: true
has_comments: false
---

## Description

How can we improve robot dynamics by observing nature? Sharing some concepts in VERY ROUGH format - this discussion has mistakes but the key takeaways will move us towards more affordable, sensible robotics options.

Find the notes & engineering sketches here.  Again - plenty of errors, i'm sure.
https://qr.page/g/57oBvPAqQv2

I'm going to design an open-source, hackable robot arm, and I'd love to collaborate with the open source community!  AI can help so much more in robotics state of the art if we allow it to be part of the DYNAMICS, and we design for that plan.
Web Page here: https://qr.page/g/2wY5JrxcciD

0:00 Robots fail to implement human dynamics
1:25 ►1 Never move a large before small mass
1:46 ►2 Don't induce reaction forces at base
2:12 ►3 Generate high acceleration by maintaining a CG
2:55 ►4 Enhance accel with Force by preloading
4:55 ►5 Conserve angular momentum when possible
5:33 ►6 We DONT require rigidity or FINE Measurement
8:13 Quick discussion of my sketches

## Chapters

- 0:00 Robots fail to implement human dynamics
- 1:25 1 Never move a large before small mass
- 1:46 2 Don't induce reaction forces at base
- 2:12 3 Generate high acceleration by maintaining a CG
- 2:55 4 Enhance accel with Force by preloading
- 4:55 5 Conserve angular momentum when possible
- 5:33 6 We DONT require rigidity or FINE Measurement
- 8:13 Quick discussion of my sketches

## Transcript

[0:04] hi everybody I'm David
[0:04] hi everybody I'm David um sorry this video isn't well prepared
[0:06] um sorry this video isn't well prepared
[0:06] um sorry this video isn't well prepared I just did a ton of thinking I'm
[0:09] I just did a ton of thinking I'm
[0:09] I just did a ton of thinking I'm exhausted and then I took some notes
[0:10] exhausted and then I took some notes
[0:10] exhausted and then I took some notes that I'd love to share with the world
[0:13] that I'd love to share with the world
[0:13] that I'd love to share with the world and I know that if I take the time to
[0:15] and I know that if I take the time to
[0:15] and I know that if I take the time to refine them to the Quality they deserve
[0:17] refine them to the Quality they deserve
[0:17] refine them to the Quality they deserve then uh it could be many months before I
[0:21] then uh it could be many months before I
[0:21] then uh it could be many months before I share anything so I just want to kind of
[0:24] share anything so I just want to kind of
[0:24] share anything so I just want to kind of um describe the outline this is for
[0:26] um describe the outline this is for
[0:26] um describe the outline this is for robotics development and what we can do
[0:28] robotics development and what we can do
[0:28] robotics development and what we can do to improve
[0:29] to improve
[0:29] to improve and
[0:31] and
[0:31] and um then I'll scan these uh these notes
[0:34] um then I'll scan these uh these notes
[0:34] um then I'll scan these uh these notes into a PDF I'll post it at the bottom of
[0:37] into a PDF I'll post it at the bottom of
[0:37] into a PDF I'll post it at the bottom of the video with a link and anyone who's
[0:39] the video with a link and anyone who's
[0:39] the video with a link and anyone who's very mechanically inclined understands
[0:42] very mechanically inclined understands
[0:42] very mechanically inclined understands kinematics Dynamics
[0:44] kinematics Dynamics
[0:44] kinematics Dynamics or state of robots and what we can do
[0:47] or state of robots and what we can do
[0:47] or state of robots and what we can do with artificial intelligence then I
[0:50] with artificial intelligence then I
[0:50] with artificial intelligence then I think your feedback would be valuable or
[0:53] think your feedback would be valuable or
[0:53] think your feedback would be valuable or you can take some of these ideas and
[0:54] you can take some of these ideas and
[0:54] you can take some of these ideas and roll with it
[0:56] roll with it
[0:56] roll with it um
[0:57] um
[0:57] um so there's like six points here I woke
[1:00] so there's like six points here I woke
[1:00] so there's like six points here I woke up thinking what do humans do that
[1:03] up thinking what do humans do that
[1:03] up thinking what do humans do that robots don't do
[1:05] robots don't do
[1:05] robots don't do the precursor is
[1:07] the precursor is
[1:07] the precursor is in 2011 I got my bachelor's in
[1:10] in 2011 I got my bachelor's in
[1:10] in 2011 I got my bachelor's in mechanical engineering learned all about
[1:12] mechanical engineering learned all about
[1:12] mechanical engineering learned all about motion and I thought that humans were
[1:15] motion and I thought that humans were
[1:15] motion and I thought that humans were incredibly inefficient in their motion
[1:19] incredibly inefficient in their motion
[1:19] incredibly inefficient in their motion uh basically until now
[1:21] uh basically until now
[1:21] uh basically until now I I just spent the time thinking about
[1:24] I I just spent the time thinking about
[1:24] I I just spent the time thinking about these things so one uh we never move a
[1:27] these things so one uh we never move a
[1:27] these things so one uh we never move a large mass if we can move a small Mass
[1:30] large mass if we can move a small Mass
[1:30] large mass if we can move a small Mass so the finger is used before the wrist
[1:33] so the finger is used before the wrist
[1:33] so the finger is used before the wrist is used before the elbow is used before
[1:36] is used before the elbow is used before
[1:36] is used before the elbow is used before the shoulder is used for the Torso so
[1:39] the shoulder is used for the Torso so
[1:39] the shoulder is used for the Torso so I'm not using my torso to pick up this
[1:42] I'm not using my torso to pick up this
[1:42] I'm not using my torso to pick up this eraser
[1:44] eraser
[1:44] eraser um next thing we don't induce reaction
[1:46] um next thing we don't induce reaction
[1:46] um next thing we don't induce reaction forces at the base if we can
[1:48] forces at the base if we can
[1:48] forces at the base if we can counterbalance instead that is for
[1:51] counterbalance instead that is for
[1:51] counterbalance instead that is for example if I reach to grab something
[1:53] example if I reach to grab something
[1:54] example if I reach to grab something with my right arm
[1:55] with my right arm
[1:55] with my right arm I'm retracting my left shoulder instead
[1:59] I'm retracting my left shoulder instead
[1:59] I'm retracting my left shoulder instead of
[2:00] of
[2:00] of instead of
[2:02] instead of
[2:02] instead of pushing with the Torso
[2:05] pushing with the Torso
[2:05] pushing with the Torso next and that's a larger muscle mass and
[2:09] next and that's a larger muscle mass and
[2:09] next and that's a larger muscle mass and a larger mass that needs to be rotated
[2:12] a larger mass that needs to be rotated
[2:12] a larger mass that needs to be rotated next we don't generate sorry we generate
[2:15] next we don't generate sorry we generate
[2:15] next we don't generate sorry we generate High accelerations by maintaining a
[2:18] High accelerations by maintaining a
[2:18] High accelerations by maintaining a center of gravity and that's the only
[2:21] center of gravity and that's the only
[2:21] center of gravity and that's the only way we do it for the highest
[2:23] way we do it for the highest
[2:23] way we do it for the highest accelerations my example here first was
[2:26] accelerations my example here first was
[2:26] accelerations my example here first was you flick the finger and I flick
[2:30] you flick the finger and I flick
[2:30] you flick the finger and I flick this larger Mass moves down a little bit
[2:34] this larger Mass moves down a little bit
[2:34] this larger Mass moves down a little bit while the finger moves a larger amount
[2:37] while the finger moves a larger amount
[2:37] while the finger moves a larger amount that conserves the
[2:39] that conserves the
[2:39] that conserves the the center of gravity of everything
[2:41] the center of gravity of everything
[2:41] the center of gravity of everything after the wrist and this is why I don't
[2:45] after the wrist and this is why I don't
[2:45] after the wrist and this is why I don't need to induce a reaction force with my
[2:48] need to induce a reaction force with my
[2:48] need to induce a reaction force with my my elbow shoulder
[2:50] my elbow shoulder
[2:50] my elbow shoulder absolutely not my feet
[2:53] absolutely not my feet
[2:53] absolutely not my feet um
[2:54] um
[2:54] um then generating High acceleration then
[2:57] then generating High acceleration then
[2:57] then generating High acceleration then we enhance High acceleration motions by
[3:01] we enhance High acceleration motions by
[3:01] we enhance High acceleration motions by pre-loading reaction forces if the
[3:05] pre-loading reaction forces if the
[3:05] pre-loading reaction forces if the acceleration predicts a high Force if
[3:07] acceleration predicts a high Force if
[3:07] acceleration predicts a high Force if I'm anticipating I'm going to reach out
[3:10] I'm anticipating I'm going to reach out
[3:10] I'm anticipating I'm going to reach out and grab an item okay I'm not
[3:14] and grab an item okay I'm not
[3:14] and grab an item okay I'm not anticipating a high Force then I can
[3:24] enhance that motion and keep my high
[3:24] enhance that motion and keep my high acceleration if I pre-load so if you
[3:27] acceleration if I pre-load so if you
[3:27] acceleration if I pre-load so if you took some martial arts courses they tell
[3:30] took some martial arts courses they tell
[3:30] took some martial arts courses they tell you you're using your feet and your
[3:32] you you're using your feet and your
[3:32] you you're using your feet and your torso
[3:34] torso
[3:34] torso to drive force into a punch for example
[3:37] to drive force into a punch for example
[3:37] to drive force into a punch for example and so we throw a right jab by
[3:40] and so we throw a right jab by
[3:40] and so we throw a right jab by retracting that shoulder and only this
[3:44] retracting that shoulder and only this
[3:44] retracting that shoulder and only this mass is moving everything above the
[3:46] mass is moving everything above the
[3:46] mass is moving everything above the chest
[3:46] chest
[3:46] chest is moving and that's energy we need to
[3:50] is moving and that's energy we need to
[3:50] is moving and that's energy we need to spend for that amount of mass to go and
[3:52] spend for that amount of mass to go and
[3:52] spend for that amount of mass to go and accelerate however if we want to have
[3:55] accelerate however if we want to have
[3:55] accelerate however if we want to have the most powerful force then we're going
[3:57] the most powerful force then we're going
[3:57] the most powerful force then we're going to start with the feet
[4:00] to start with the feet
[4:00] to start with the feet maybe move the hips and the knees the
[4:02] maybe move the hips and the knees the
[4:02] maybe move the hips and the knees the entire body uh is put into motion and we
[4:07] entire body uh is put into motion and we
[4:07] entire body uh is put into motion and we put that into motion before we extend
[4:10] put that into motion before we extend
[4:10] put that into motion before we extend the arm so then the acceleration happens
[4:13] the arm so then the acceleration happens
[4:13] the arm so then the acceleration happens at the arm
[4:16] at the arm
[4:16] at the arm um
[4:16] um
[4:16] um still at a high speed
[4:19] still at a high speed
[4:19] still at a high speed not all in one it's a chain rather than
[4:24] not all in one it's a chain rather than
[4:24] not all in one it's a chain rather than what you see in a robot is it's moving
[4:28] what you see in a robot is it's moving
[4:28] what you see in a robot is it's moving all of the members at once we require
[4:30] all of the members at once we require
[4:30] all of the members at once we require very high torque Motors in series
[4:34] very high torque Motors in series
[4:34] very high torque Motors in series actuators like
[4:36] actuators like
[4:36] actuators like um
[4:37] um
[4:37] um a five dof robot is
[4:40] a five dof robot is
[4:40] a five dof robot is it it specifies the torque of the motor
[4:43] it it specifies the torque of the motor
[4:43] it it specifies the torque of the motor at the base to be able to overcome the
[4:46] at the base to be able to overcome the
[4:46] at the base to be able to overcome the momentum of all the joints and that's
[4:49] momentum of all the joints and that's
[4:49] momentum of all the joints and that's demanding far more energy from each of
[4:53] demanding far more energy from each of
[4:53] demanding far more energy from each of the motors on a robot
[4:56] the motors on a robot
[4:56] the motors on a robot next conserve angular momentum whenever
[4:59] next conserve angular momentum whenever
[4:59] next conserve angular momentum whenever possible uh first I mentioned conserving
[5:02] possible uh first I mentioned conserving
[5:02] possible uh first I mentioned conserving the keeping the the center of gravity
[5:06] the keeping the the center of gravity
[5:06] the keeping the the center of gravity of a set of
[5:12] Point masses now it's conserving angular
[5:12] Point masses now it's conserving angular momentum so when I extend my arm
[5:15] momentum so when I extend my arm
[5:15] momentum so when I extend my arm this I don't extend like this
[5:19] this I don't extend like this
[5:19] this I don't extend like this because it's easier if I do go ahead and
[5:22] because it's easier if I do go ahead and
[5:22] because it's easier if I do go ahead and let the shoulder rotate and I'm
[5:25] let the shoulder rotate and I'm
[5:25] let the shoulder rotate and I'm rotating
[5:27] rotating
[5:27] rotating this part of my arm in the opposite
[5:29] this part of my arm in the opposite
[5:29] this part of my arm in the opposite direction then this part of the arm that
[5:32] direction then this part of the arm that
[5:32] direction then this part of the arm that conserves the angular momentum so it's
[5:34] conserves the angular momentum so it's
[5:34] conserves the angular momentum so it's actually pretty efficient to reach then
[5:37] actually pretty efficient to reach then
[5:37] actually pretty efficient to reach then we don't require rigidity or find
[5:40] we don't require rigidity or find
[5:40] we don't require rigidity or find measurements at the base this is huge
[5:42] measurements at the base this is huge
[5:42] measurements at the base this is huge we're we're building robots that are
[5:45] we're we're building robots that are
[5:45] we're we're building robots that are very expensive and that are measuring
[5:47] very expensive and that are measuring
[5:47] very expensive and that are measuring the the extremely fine resolution at
[5:51] the the extremely fine resolution at
[5:51] the the extremely fine resolution at every joint and we don't need to do that
[5:54] every joint and we don't need to do that
[5:54] every joint and we don't need to do that so my example here is if you pick a
[5:57] so my example here is if you pick a
[5:57] so my example here is if you pick a petal from a flower you do not need to
[6:00] petal from a flower you do not need to
[6:00] petal from a flower you do not need to compute the perfect place to plant your
[6:02] compute the perfect place to plant your
[6:02] compute the perfect place to plant your feet you don't need to know where is the
[6:05] feet you don't need to know where is the
[6:05] feet you don't need to know where is the position of all these other joints the
[6:08] position of all these other joints the
[6:08] position of all these other joints the negotiation is happening between the
[6:10] negotiation is happening between the
[6:10] negotiation is happening between the finger the wrist
[6:12] finger the wrist
[6:12] finger the wrist the flower and the eyes
[6:14] the flower and the eyes
[6:14] the flower and the eyes so if I can measure the finger and the
[6:17] so if I can measure the finger and the
[6:17] so if I can measure the finger and the flower nothing else needs to be measured
[6:19] flower nothing else needs to be measured
[6:19] flower nothing else needs to be measured and I think now that we have ai
[6:23] and I think now that we have ai
[6:24] and I think now that we have ai starting to penetrate the industry now
[6:28] starting to penetrate the industry now
[6:28] starting to penetrate the industry now we can come back and say do we what do
[6:30] we can come back and say do we what do
[6:30] we can come back and say do we what do we need to measure at all times what do
[6:32] we need to measure at all times what do
[6:32] we need to measure at all times what do we need to compute at all times do we
[6:34] we need to compute at all times do we
[6:34] we need to compute at all times do we need to do kinematics all the way from
[6:36] need to do kinematics all the way from
[6:36] need to do kinematics all the way from the toenail to the finger in order to
[6:38] the toenail to the finger in order to
[6:38] the toenail to the finger in order to have a robot pick a flower no probably
[6:40] have a robot pick a flower no probably
[6:40] have a robot pick a flower no probably not first thing computer vision can
[6:43] not first thing computer vision can
[6:43] not first thing computer vision can allow us to pick a flower between the
[6:46] allow us to pick a flower between the
[6:46] allow us to pick a flower between the the computation of its depth and these
[6:50] the computation of its depth and these
[6:51] the computation of its depth and these small motions
[6:52] small motions
[6:52] small motions and it's it you could treat using that
[6:55] and it's it you could treat using that
[6:55] and it's it you could treat using that sensor if it's visual you can contrite
[6:57] sensor if it's visual you can contrite
[6:57] sensor if it's visual you can contrite those two items that need to interact
[7:00] those two items that need to interact
[7:00] those two items that need to interact the flower and the finger
[7:02] the flower and the finger
[7:02] the flower and the finger as two separate entities from the rest
[7:06] as two separate entities from the rest
[7:06] as two separate entities from the rest of the robot now all I have to do is
[7:08] of the robot now all I have to do is
[7:08] of the robot now all I have to do is control
[7:09] control
[7:09] control once I'm in the same visual frame all I
[7:11] once I'm in the same visual frame all I
[7:11] once I'm in the same visual frame all I have to do is control
[7:12] have to do is control
[7:12] have to do is control these small actuators and measure these
[7:15] these small actuators and measure these
[7:15] these small actuators and measure these small actuators
[7:17] small actuators
[7:17] small actuators you can do model predictive control to
[7:20] you can do model predictive control to
[7:20] you can do model predictive control to where you know uh this joint you might
[7:25] where you know uh this joint you might
[7:25] where you know uh this joint you might not have this angle measured
[7:28] not have this angle measured
[7:28] not have this angle measured but
[7:30] but
[7:30] but you might not have everything before
[7:32] you might not have everything before
[7:32] you might not have everything before that joint measured but once you know
[7:34] that joint measured but once you know
[7:34] that joint measured but once you know the this wrist rotation
[7:38] the this wrist rotation
[7:38] the this wrist rotation then you can compute kinematics from the
[7:40] then you can compute kinematics from the
[7:40] then you can compute kinematics from the wrist forward and do the job like that
[7:43] wrist forward and do the job like that
[7:43] wrist forward and do the job like that it's so much less intensive than
[7:44] it's so much less intensive than
[7:44] it's so much less intensive than Computing and we're going to calculate
[7:48] Computing and we're going to calculate
[7:48] Computing and we're going to calculate the finger to the wrist of the elbow to
[7:50] the finger to the wrist of the elbow to
[7:50] the finger to the wrist of the elbow to the shoulder to the to the feet to the
[7:52] the shoulder to the to the feet to the
[7:52] the shoulder to the to the feet to the ground to the pot
[7:55] ground to the pot
[7:55] ground to the pot to the flower that doesn't make sense is
[7:57] to the flower that doesn't make sense is
[7:57] to the flower that doesn't make sense is we're already not Computing the move the
[8:00] we're already not Computing the move the
[8:00] we're already not Computing the move the the positions from the floor to the item
[8:03] the positions from the floor to the item
[8:03] the positions from the floor to the item that we're contacting or manipulating
[8:07] that we're contacting or manipulating
[8:07] that we're contacting or manipulating the rest of the notes are just diving
[8:10] the rest of the notes are just diving
[8:10] the rest of the notes are just diving into sketches and saying well how can we
[8:11] into sketches and saying well how can we
[8:11] into sketches and saying well how can we do a a counterbalanced
[8:16] do a a counterbalanced
[8:16] do a a counterbalanced mascara robot was the first concept that
[8:18] mascara robot was the first concept that
[8:18] mascara robot was the first concept that I've Loved Scara robots because you can
[8:21] I've Loved Scara robots because you can
[8:21] I've Loved Scara robots because you can hold a position without wearing the
[8:24] hold a position without wearing the
[8:24] hold a position without wearing the motors and without exerting energy I
[8:26] motors and without exerting energy I
[8:26] motors and without exerting energy I feel like that's entirely underutilized
[8:29] feel like that's entirely underutilized
[8:29] feel like that's entirely underutilized but then aside from just using mascara
[8:34] but then aside from just using mascara
[8:34] but then aside from just using mascara and then counterbalanced mascara so you
[8:36] and then counterbalanced mascara so you
[8:36] and then counterbalanced mascara so you have a mass that's on each side of the
[8:40] have a mass that's on each side of the
[8:40] have a mass that's on each side of the the center
[8:42] the center
[8:42] the center um other configurations that we can add
[8:44] um other configurations that we can add
[8:44] um other configurations that we can add to make this robot more like a human so
[8:49] to make this robot more like a human so
[8:49] to make this robot more like a human so um
[8:50] um
[8:50] um starts to get into how do we conserve
[8:53] starts to get into how do we conserve
[8:53] starts to get into how do we conserve angular momentum between two joints not
[8:56] angular momentum between two joints not
[8:56] angular momentum between two joints not just maintain the center of mass by
[8:59] just maintain the center of mass by
[8:59] just maintain the center of mass by having an opposite Mass
[9:01] having an opposite Mass
[9:02] having an opposite Mass what can we do between two smaller
[9:05] what can we do between two smaller
[9:05] what can we do between two smaller joints like the human's arms to help
[9:08] joints like the human's arms to help
[9:08] joints like the human's arms to help with that and reduce reaction forces at
[9:11] with that and reduce reaction forces at
[9:11] with that and reduce reaction forces at the floor and how can we measure
[9:14] the floor and how can we measure
[9:14] the floor and how can we measure reaction forces at our lower
[9:17] reaction forces at our lower
[9:17] reaction forces at our lower um
[9:17] um
[9:17] um our lower actuators
[9:20] our lower actuators
[9:20] our lower actuators to then tell us something about this
[9:22] to then tell us something about this
[9:22] to then tell us something about this motion if we eliminate encoders from all
[9:25] motion if we eliminate encoders from all
[9:25] motion if we eliminate encoders from all the joints then what do we have left to
[9:28] the joints then what do we have left to
[9:28] the joints then what do we have left to measure well if we're controlling the
[9:31] measure well if we're controlling the
[9:31] measure well if we're controlling the Torso with the feet and the Torso
[9:34] Torso with the feet and the Torso
[9:34] Torso with the feet and the Torso has Motion in induced by this motion of
[9:39] has Motion in induced by this motion of
[9:39] has Motion in induced by this motion of the elbow
[9:40] the elbow
[9:40] the elbow then we could measure
[9:43] then we could measure
[9:43] then we could measure the actuators
[9:45] the actuators
[9:45] the actuators mechanical electromechanical actuator
[9:49] mechanical electromechanical actuator
[9:49] mechanical electromechanical actuator at the feet
[9:50] at the feet
[9:50] at the feet and it will tell us something about this
[9:53] and it will tell us something about this
[9:53] and it will tell us something about this motion so and and that takes learning
[9:55] motion so and and that takes learning
[9:55] motion so and and that takes learning that's as we're infants and becoming
[9:58] that's as we're infants and becoming
[9:58] that's as we're infants and becoming functional humans that's what the that's
[10:01] functional humans that's what the that's
[10:01] functional humans that's what the that's what the intelligence is doing we're
[10:03] what the intelligence is doing we're
[10:03] what the intelligence is doing we're we're just performing experiments
[10:06] we're just performing experiments
[10:06] we're just performing experiments between all of our joints and
[10:09] between all of our joints and
[10:09] between all of our joints and um nobody taught you how to throw a
[10:11] um nobody taught you how to throw a
[10:11] um nobody taught you how to throw a baseball by using math
[10:13] baseball by using math
[10:13] baseball by using math first you got you you learned through
[10:16] first you got you you learned through
[10:16] first you got you you learned through feel
[10:17] feel
[10:17] feel and Performing experiments many
[10:20] and Performing experiments many
[10:20] and Performing experiments many iterations until the feeling had a
[10:23] iterations until the feeling had a
[10:23] iterations until the feeling had a meaning and we didn't ever compute that
[10:25] meaning and we didn't ever compute that
[10:25] meaning and we didn't ever compute that meaning using math or
[10:28] meaning using math or
[10:28] meaning using math or Dynamics Newton wasn't involved in that
[10:33] Dynamics Newton wasn't involved in that
[10:33] Dynamics Newton wasn't involved in that um what if the mass rotates in another
[10:36] um what if the mass rotates in another
[10:36] um what if the mass rotates in another plane what if we add slip Rings now slip
[10:40] plane what if we add slip Rings now slip
[10:40] plane what if we add slip Rings now slip Rings I've been thinking about for 10
[10:42] Rings I've been thinking about for 10
[10:42] Rings I've been thinking about for 10 years and 3D printing helped us get
[10:46] years and 3D printing helped us get
[10:46] years and 3D printing helped us get closer ball bearings and some parametric
[10:49] closer ball bearings and some parametric
[10:49] closer ball bearings and some parametric designs online are offered and there are
[10:51] designs online are offered and there are
[10:51] designs online are offered and there are I think there are some brilliant ways to
[10:53] I think there are some brilliant ways to
[10:53] I think there are some brilliant ways to put together the cheapest components in
[10:55] put together the cheapest components in
[10:55] put together the cheapest components in the world and have a slip ring that's
[10:57] the world and have a slip ring that's
[10:57] the world and have a slip ring that's still custom size using parametric CAD
[11:00] still custom size using parametric CAD
[11:00] still custom size using parametric CAD models
[11:01] models
[11:02] models is it important to control the center of
[11:05] is it important to control the center of
[11:05] is it important to control the center of gravity of the robot along the y
[11:08] gravity of the robot along the y
[11:08] gravity of the robot along the y direction if the Y is that the height
[11:11] direction if the Y is that the height
[11:11] direction if the Y is that the height that's an unanswered question but it
[11:13] that's an unanswered question but it
[11:13] that's an unanswered question but it deserves
[11:15] deserves
[11:15] deserves it deserves consideration when we're
[11:18] it deserves consideration when we're
[11:18] it deserves consideration when we're configuring the robot before we build
[11:20] configuring the robot before we build
[11:20] configuring the robot before we build the next design
[11:22] the next design
[11:22] the next design and all of these sketches are are trying
[11:26] and all of these sketches are are trying
[11:26] and all of these sketches are are trying to orient us towards something that is a
[11:28] to orient us towards something that is a
[11:28] to orient us towards something that is a parametric design that can be
[11:29] parametric design that can be
[11:29] parametric design that can be manipulated to other variations
[11:32] manipulated to other variations
[11:32] manipulated to other variations then
[11:34] then
[11:34] then what if we manipulate the angular
[11:37] what if we manipulate the angular
[11:37] what if we manipulate the angular momentum
[11:39] momentum
[11:39] momentum of
[11:40] of
[11:40] of an end joint
[11:42] an end joint
[11:42] an end joint along with a counter Mass
[11:46] along with a counter Mass
[11:46] along with a counter Mass and
[11:52] what if we Implement breaking
[11:52] what if we Implement breaking with the superior actuators while we're
[11:58] with the superior actuators while we're
[11:58] with the superior actuators while we're implementing motion with the inferior
[12:01] implementing motion with the inferior
[12:01] implementing motion with the inferior actuators
[12:02] actuators
[12:02] actuators that that starts to get really
[12:04] that that starts to get really
[12:04] that that starts to get really interesting
[12:05] interesting
[12:05] interesting okay well if hopefully that was
[12:08] okay well if hopefully that was
[12:08] okay well if hopefully that was interesting to some of you I know not to
[12:10] interesting to some of you I know not to
[12:10] interesting to some of you I know not to most but I just wanted to share

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
