---
title: "Embedded Computer users Should Know this Power Issue"
url: "https://www.youtube.com/watch?v=EF9fIMgCdZw"
video_id: "EF9fIMgCdZw"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2025-03-20
duration: "14:43"
duration_sec: 883
views: 2464
likes: 94
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/EF9fIMgCdZw/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 680
chapters_count: 9
has_description: true
has_comments: false
---

## Description

Today I’m working with a cool new board from Beaglebone.  It’s similar to a Raspberry Pi, and there is an issue with power that appears with all of these new SBCs.

Embedded computers, especially with AI, demand more power than previous generations and they are easy to power up at your desk but hard to mobilize.  It’s all rooted in the power adapters. Each developer of a robotics project tends to design their own solution. Instead of constant rework, I’m calling on the community to discover and converge on best practices.

[chapters]
0:00 purpose
1:10 beaglebone Y-AI, Pi 5
5:00 portable energy
6:15 invisible problem
7:00 DC converter issues
8:00 eperts' gaps
9:30 corded scenario
10:30 cordless scenario
14:00 feedback

## Chapters

- 0:00 purpose
- 1:10 beaglebone Y-AI, Pi 5
- 5:00 portable energy
- 6:15 invisible problem
- 7:00 DC converter issues
- 8:00 eperts' gaps
- 9:30 corded scenario
- 10:30 cordless scenario
- 14:00 feedback

## Transcript

[0:03] testing 1 2 3 1 2 3 hi everybody I'm
[0:03] testing 1 2 3 1 2 3 hi everybody I'm David okay this video has one specific
[0:06] David okay this video has one specific
[0:06] David okay this video has one specific purpose and that is to get down to the
[0:08] purpose and that is to get down to the
[0:08] purpose and that is to get down to the bottom of a problem I want to describe a
[0:11] bottom of a problem I want to describe a
[0:11] bottom of a problem I want to describe a problem because it's not easy to
[0:12] problem because it's not easy to
[0:12] problem because it's not easy to describe uh briefly in writing or in one
[0:16] describe uh briefly in writing or in one
[0:16] describe uh briefly in writing or in one sentence uh so I'll describe it I think
[0:19] sentence uh so I'll describe it I think
[0:19] sentence uh so I'll describe it I think several people out there in the world
[0:21] several people out there in the world
[0:21] several people out there in the world are aware of it not everyone and some
[0:23] are aware of it not everyone and some
[0:23] are aware of it not everyone and some people are only aware of parts of it and
[0:26] people are only aware of parts of it and
[0:26] people are only aware of parts of it and so we want to get down to the root cause
[0:28] so we want to get down to the root cause
[0:28] so we want to get down to the root cause which is very likely to be multiple root
[0:32] which is very likely to be multiple root
[0:32] which is very likely to be multiple root causes uh
[0:34] causes uh
[0:34] causes uh crisscrossing and so the solution will
[0:36] crisscrossing and so the solution will
[0:37] crisscrossing and so the solution will not be One Singular solution um I was
[0:41] not be One Singular solution um I was
[0:41] not be One Singular solution um I was about to email today um some of the
[0:44] about to email today um some of the
[0:44] about to email today um some of the designers in beagle bone. org or in the
[0:48] designers in beagle bone. org or in the
[0:48] designers in beagle bone. org or in the beaglebone uh company which is an open
[0:51] beaglebone uh company which is an open
[0:52] beaglebone uh company which is an open source they generate open source
[0:54] source they generate open source
[0:54] source they generate open source technology um similar to Raspberry Pi
[0:57] technology um similar to Raspberry Pi
[0:57] technology um similar to Raspberry Pi extremely Hightech embedded computer
[1:00] extremely Hightech embedded computer
[1:00] extremely Hightech embedded computer in um and we in I
[1:03] in um and we in I
[1:03] in um and we in I am in the process of integrating the
[1:07] am in the process of integrating the
[1:07] am in the process of integrating the Beagle bone y AI on Scuttle so we can
[1:12] Beagle bone y AI on Scuttle so we can
[1:12] Beagle bone y AI on Scuttle so we can have a version of scuttle that supports
[1:15] have a version of scuttle that supports
[1:15] have a version of scuttle that supports the users who love bigle bone um this is
[1:18] the users who love bigle bone um this is
[1:18] the users who love bigle bone um this is an AI board it's very similar to
[1:21] an AI board it's very similar to
[1:21] an AI board it's very similar to Raspberry Pi in a lot of ways um with
[1:25] Raspberry Pi in a lot of ways um with
[1:25] Raspberry Pi in a lot of ways um with some unique benefits of working with
[1:28] some unique benefits of working with
[1:28] some unique benefits of working with beagle especi especially if you're a
[1:31] beagle especi especially if you're a
[1:31] beagle especi especially if you're a very Advanced Linux user or embedded um
[1:35] very Advanced Linux user or embedded um
[1:35] very Advanced Linux user or embedded um developer then those are the people that
[1:38] developer then those are the people that
[1:38] developer then those are the people that find the most benefit I think um among
[1:41] find the most benefit I think um among
[1:41] find the most benefit I think um among users with uh single board computers
[1:44] users with uh single board computers
[1:44] users with uh single board computers using beagle anyway so all of the latest
[1:48] using beagle anyway so all of the latest
[1:48] using beagle anyway so all of the latest released boards are using USBC at least
[1:52] released boards are using USBC at least
[1:52] released boards are using USBC at least as an option or as a default for
[1:55] as an option or as a default for
[1:55] as an option or as a default for powering up the board and if you're
[1:58] powering up the board and if you're
[1:58] powering up the board and if you're unfamiliar this is the Raspberry Pi I
[2:01] unfamiliar this is the Raspberry Pi I
[2:01] unfamiliar this is the Raspberry Pi I think version this is version three this
[2:03] think version this is version three this
[2:03] think version this is version three this is version four and this is the the
[2:07] is version four and this is the the
[2:07] is version four and this is the the bigab bone y
[2:08] bigab bone y
[2:08] bigab bone y AI the problem to talk about today is on
[2:12] AI the problem to talk about today is on
[2:12] AI the problem to talk about today is on Power and I would recommend um as I said
[2:16] Power and I would recommend um as I said
[2:16] Power and I would recommend um as I said the the purpose of the video is to
[2:18] the the purpose of the video is to
[2:18] the the purpose of the video is to actually ask for answers from the
[2:20] actually ask for answers from the
[2:20] actually ask for answers from the community and I'm going to send this to
[2:21] community and I'm going to send this to
[2:21] community and I'm going to send this to beagle bone um but if you are not a
[2:24] beagle bone um but if you are not a
[2:24] beagle bone um but if you are not a person who provides answers you can
[2:27] person who provides answers you can
[2:27] person who provides answers you can probably still uh understand and learn a
[2:29] probably still uh understand and learn a
[2:29] probably still uh understand and learn a a lot about this I would bet that anyone
[2:32] a lot about this I would bet that anyone
[2:32] a lot about this I would bet that anyone who's working with uh embedded
[2:34] who's working with uh embedded
[2:34] who's working with uh embedded devices microcontrollers and
[2:37] devices microcontrollers and
[2:37] devices microcontrollers and microcomputers you will learn something
[2:39] microcomputers you will learn something
[2:39] microcomputers you will learn something so um it starts with the USBC Port where
[2:44] so um it starts with the USBC Port where
[2:44] so um it starts with the USBC Port where uh we now have the option to power many
[2:47] uh we now have the option to power many
[2:47] uh we now have the option to power many of our boards um
[2:50] of our boards um
[2:50] of our boards um previously there's a 5vt bus on these
[2:52] previously there's a 5vt bus on these
[2:52] previously there's a 5vt bus on these boards that's the main power bus uh
[2:56] boards that's the main power bus uh
[2:56] boards that's the main power bus uh providing power to several onboard
[2:59] providing power to several onboard
[2:59] providing power to several onboard components
[3:00] components
[3:00] components um let's
[3:02] um let's
[3:02] um let's see before even powering up um I did
[3:06] see before even powering up um I did
[3:06] see before even powering up um I did some reading and it looks that it's it's
[3:08] some reading and it looks that it's it's
[3:08] some reading and it looks that it's it's reported that beagle has made this port
[3:12] reported that beagle has made this port
[3:12] reported that beagle has made this port to take the typical 5V power level from
[3:18] to take the typical 5V power level from
[3:18] to take the typical 5V power level from the USBC rather than 12 volts or 15
[3:22] the USBC rather than 12 volts or 15
[3:22] the USBC rather than 12 volts or 15 volts one of the other PD Power delivery
[3:26] volts one of the other PD Power delivery
[3:26] volts one of the other PD Power delivery voltages so that means if you want Ed 15
[3:31] voltages so that means if you want Ed 15
[3:31] voltages so that means if you want Ed 15 watts let's say to power a higher AI
[3:35] watts let's say to power a higher AI
[3:35] watts let's say to power a higher AI ready microchip um that 15 watts would
[3:39] ready microchip um that 15 watts would
[3:39] ready microchip um that 15 watts would be pulling one amp over the USBC cable
[3:43] be pulling one amp over the USBC cable
[3:43] be pulling one amp over the USBC cable if it at 15 volts but if it's only at
[3:46] if it at 15 volts but if it's only at
[3:46] if it at 15 volts but if it's only at five now you need three amps so 3 amps
[3:50] five now you need three amps so 3 amps
[3:50] five now you need three amps so 3 amps is triple the current going through that
[3:53] is triple the current going through that
[3:53] is triple the current going through that uh that wire triple the current being
[3:55] uh that wire triple the current being
[3:55] uh that wire triple the current being passed at that really teeny tiny
[3:57] passed at that really teeny tiny
[3:58] passed at that really teeny tiny connector and so we have to be aware of
[4:03] connector and so we have to be aware of
[4:03] connector and so we have to be aware of the the power
[4:05] the the power
[4:05] the the power scheme so
[4:07] scheme so
[4:07] scheme so USP uh for many years had a standard of
[4:11] USP uh for many years had a standard of
[4:11] USP uh for many years had a standard of a maximum of 2 amps while there's a
[4:14] a maximum of 2 amps while there's a
[4:14] a maximum of 2 amps while there's a helicopter flying over right now don't
[4:16] helicopter flying over right now don't
[4:16] helicopter flying over right now don't know if you can hear that it's
[4:20] know if you can hear that it's
[4:20] know if you can hear that it's distracting um so typically 2 amps was
[4:24] distracting um so typically 2 amps was
[4:24] distracting um so typically 2 amps was the maximum for both the devices pulling
[4:27] the maximum for both the devices pulling
[4:27] the maximum for both the devices pulling power and for the
[4:40] adapters it's really hard to think when
[4:40] adapters it's really hard to think when there the house is rattling and these
[4:43] there the house is rattling and these
[4:43] there the house is rattling and these machines are flying over
[4:45] machines are flying over
[4:45] machines are flying over okay
[4:47] okay
[4:47] okay uh I'll show you the spread of devices
[4:51] uh I'll show you the spread of devices
[4:51] uh I'll show you the spread of devices and how this amperage and and
[4:53] and how this amperage and and
[4:53] and how this amperage and and voltage impacts us let's adjust this
[4:56] voltage impacts us let's adjust this
[4:56] voltage impacts us let's adjust this camera here
[5:05] um so 2 amps was the standard for a good
[5:05] um so 2 amps was the standard for a good quality 5vt ordinary USB um adapter and
[5:10] quality 5vt ordinary USB um adapter and
[5:10] quality 5vt ordinary USB um adapter and that means including the ones that take
[5:13] that means including the ones that take
[5:13] that means including the ones that take it down from 120 volts ac coming from
[5:18] it down from 120 volts ac coming from
[5:18] it down from 120 volts ac coming from wall power the ones that are um adapting
[5:23] wall power the ones that are um adapting
[5:23] wall power the ones that are um adapting from a higher voltage like 12 volts or
[5:25] from a higher voltage like 12 volts or
[5:25] from a higher voltage like 12 volts or 14 from a vehicle and then providing
[5:28] 14 from a vehicle and then providing
[5:28] 14 from a vehicle and then providing that 5 volt USB and also many many of
[5:33] that 5 volt USB and also many many of
[5:33] that 5 volt USB and also many many of these uh portable power devices power
[5:36] these uh portable power devices power
[5:36] these uh portable power devices power bank Etc um the good quality ones were
[5:39] bank Etc um the good quality ones were
[5:39] bank Etc um the good quality ones were offering two amps and so there are
[5:42] offering two amps and so there are
[5:42] offering two amps and so there are millions of devices out here that can
[5:44] millions of devices out here that can
[5:44] millions of devices out here that can give you 2 amps at 5 volts that's
[5:47] give you 2 amps at 5 volts that's
[5:47] give you 2 amps at 5 volts that's millions of devices that users will
[5:50] millions of devices that users will
[5:50] millions of devices that users will attempt to use to power up their new
[5:55] attempt to use to power up their new
[5:55] attempt to use to power up their new boards that have chips that com these
[5:59] boards that have chips that com these
[5:59] boards that have chips that com these demand
[6:00] demand
[6:00] demand higher power levels or they can make use
[6:03] higher power levels or they can make use
[6:03] higher power levels or they can make use of higher power levels so 15 watts will
[6:05] of higher power levels so 15 watts will
[6:05] of higher power levels so 15 watts will say is 3 amps um it looks that the
[6:10] say is 3 amps um it looks that the
[6:10] say is 3 amps um it looks that the Rasberry Pi as well as the Beagle bone
[6:14] Rasberry Pi as well as the Beagle bone
[6:14] Rasberry Pi as well as the Beagle bone are not using PD so that is they're
[6:17] are not using PD so that is they're
[6:17] are not using PD so that is they're still drawing power at the 5vt level but
[6:21] still drawing power at the 5vt level but
[6:21] still drawing power at the 5vt level but they want to draw more than that if
[6:24] they want to draw more than that if
[6:24] they want to draw more than that if you're limiting if you are using this
[6:27] you're limiting if you are using this
[6:27] you're limiting if you are using this type of adapter to power something that
[6:29] type of adapter to power something that
[6:29] type of adapter to power something that needs more than two amps um the in the
[6:32] needs more than two amps um the in the
[6:32] needs more than two amps um the in the worst case the user isn't checking any
[6:34] worst case the user isn't checking any
[6:34] worst case the user isn't checking any of the amperage ratings and they will
[6:37] of the amperage ratings and they will
[6:37] of the amperage ratings and they will just give one or two amps from a typical
[6:41] just give one or two amps from a typical
[6:41] just give one or two amps from a typical type of device see 5 Volt 2 amps will
[6:44] type of device see 5 Volt 2 amps will
[6:44] type of device see 5 Volt 2 amps will power up it will function and do things
[6:46] power up it will function and do things
[6:46] power up it will function and do things but you'll be limited from its peak
[6:48] but you'll be limited from its peak
[6:48] but you'll be limited from its peak computing power the performance will be
[6:50] computing power the performance will be
[6:50] computing power the performance will be much lower than It ultimately can do and
[6:53] much lower than It ultimately can do and
[6:53] much lower than It ultimately can do and so the trouble with this problem is that
[6:55] so the trouble with this problem is that
[6:55] so the trouble with this problem is that it's invisible it is not detectable
[6:57] it's invisible it is not detectable
[6:57] it's invisible it is not detectable unless you specifically go to find that
[6:59] unless you specifically go to find that
[6:59] unless you specifically go to find that problem it's uh in my opinion it's
[7:01] problem it's uh in my opinion it's
[7:01] problem it's uh in my opinion it's better if the device would uh fail to
[7:03] better if the device would uh fail to
[7:03] better if the device would uh fail to power up give an error or simply um not
[7:06] power up give an error or simply um not
[7:06] power up give an error or simply um not function so that we can so that all
[7:08] function so that we can so that all
[7:08] function so that we can so that all those users can detect what's going on
[7:10] those users can detect what's going on
[7:10] those users can detect what's going on uh and and solve that issue so the
[7:12] uh and and solve that issue so the
[7:12] uh and and solve that issue so the solution at level one for uh smart users
[7:15] solution at level one for uh smart users
[7:15] solution at level one for uh smart users will go to find they'll find read the
[7:17] will go to find they'll find read the
[7:17] will go to find they'll find read the rated power demand and then they'll go
[7:18] rated power demand and then they'll go
[7:18] rated power demand and then they'll go purchase an adapter like this one that
[7:20] purchase an adapter like this one that
[7:20] purchase an adapter like this one that says 5 volts 3 amps and then U they will
[7:23] says 5 volts 3 amps and then U they will
[7:23] says 5 volts 3 amps and then U they will be providing or attempting to provide
[7:25] be providing or attempting to provide
[7:25] be providing or attempting to provide that 15 watts available but uh one thing
[7:27] that 15 watts available but uh one thing
[7:27] that 15 watts available but uh one thing shopping for these it's harder to find
[7:29] shopping for these it's harder to find
[7:29] shopping for these it's harder to find um especially so now you can find loads
[7:32] um especially so now you can find loads
[7:32] um especially so now you can find loads and loads of devices from the AC power
[7:35] and loads of devices from the AC power
[7:35] and loads of devices from the AC power adapters that will give you more
[7:36] adapters that will give you more
[7:36] adapters that will give you more amperage now that's becoming very very
[7:38] amperage now that's becoming very very
[7:38] amperage now that's becoming very very popular and then but if you shop for DC
[7:40] popular and then but if you shop for DC
[7:40] popular and then but if you shop for DC converters that give you something say
[7:42] converters that give you something say
[7:42] converters that give you something say step down from 12 volts down um there
[7:45] step down from 12 volts down um there
[7:45] step down from 12 volts down um there are fewer options to find uh three amps
[7:48] are fewer options to find uh three amps
[7:48] are fewer options to find uh three amps available there are and then there are
[7:49] available there are and then there are
[7:49] available there are and then there are uh quality issues so these these strange
[7:52] uh quality issues so these these strange
[7:52] uh quality issues so these these strange brands that don't have a strong
[7:53] brands that don't have a strong
[7:53] brands that don't have a strong reputation and professional
[7:55] reputation and professional
[7:55] reputation and professional documentation they much much more often
[7:57] documentation they much much more often
[7:57] documentation they much much more often do not uh do not meet their their claims
[7:59] do not uh do not meet their their claims
[8:00] do not uh do not meet their their claims and their specs or the specs are not
[8:01] and their specs or the specs are not
[8:01] and their specs or the specs are not well written into product pages when
[8:02] well written into product pages when
[8:02] well written into product pages when you're shopping so it's much harder to
[8:04] you're shopping so it's much harder to
[8:04] you're shopping so it's much harder to be sure to find that 15 watts available
[8:07] be sure to find that 15 watts available
[8:07] be sure to find that 15 watts available at 5 volts um and have a reliable
[8:09] at 5 volts um and have a reliable
[8:09] at 5 volts um and have a reliable solution many many ways to think you
[8:12] solution many many ways to think you
[8:12] solution many many ways to think you have purchased it and and you do not
[8:14] have purchased it and and you do not
[8:14] have purchased it and and you do not have a reliable solution so that's an
[8:15] have a reliable solution so that's an
[8:15] have a reliable solution so that's an issue and then uh let's say that you you
[8:18] issue and then uh let's say that you you
[8:18] issue and then uh let's say that you you did your homework you chose the adapter
[8:20] did your homework you chose the adapter
[8:20] did your homework you chose the adapter that you ought to have by specification
[8:23] that you ought to have by specification
[8:23] that you ought to have by specification um then also how many of those users
[8:25] um then also how many of those users
[8:25] um then also how many of those users have a power meter to verify whether
[8:27] have a power meter to verify whether
[8:27] have a power meter to verify whether they're getting healthy power so the
[8:30] they're getting healthy power so the
[8:30] they're getting healthy power so the most um the most Avid users of
[8:32] most um the most Avid users of
[8:32] most um the most Avid users of microcontrollers are computer scientists
[8:34] microcontrollers are computer scientists
[8:34] microcontrollers are computer scientists and software developers and they they
[8:36] and software developers and they they
[8:36] and software developers and they they make up the largest population of people
[8:37] make up the largest population of people
[8:37] make up the largest population of people that use these um and that expertise
[8:40] that use these um and that expertise
[8:40] that use these um and that expertise area is usually not uh does not include
[8:42] area is usually not uh does not include
[8:43] area is usually not uh does not include expertise in evaluating power and the
[8:45] expertise in evaluating power and the
[8:45] expertise in evaluating power and the physical electrical Hardware demands so
[8:47] physical electrical Hardware demands so
[8:48] physical electrical Hardware demands so um devices like this are an obvious
[8:50] um devices like this are an obvious
[8:50] um devices like this are an obvious requirement for my lab but they are not
[8:52] requirement for my lab but they are not
[8:52] requirement for my lab but they are not an obvious requirement for many of the
[8:53] an obvious requirement for many of the
[8:53] an obvious requirement for many of the users of these devices so um at the
[8:55] users of these devices so um at the
[8:55] users of these devices so um at the moment basically you'll purchase this
[8:57] moment basically you'll purchase this
[8:57] moment basically you'll purchase this and then you'll find things all work but
[8:59] and then you'll find things all work but
[8:59] and then you'll find things all work but then much much much later down the line
[9:01] then much much much later down the line
[9:01] then much much much later down the line you will run into some problem like the
[9:02] you will run into some problem like the
[9:02] you will run into some problem like the the Wi-Fi is repeatedly disconnecting
[9:05] the Wi-Fi is repeatedly disconnecting
[9:05] the Wi-Fi is repeatedly disconnecting and that at that stage we are so deep
[9:06] and that at that stage we are so deep
[9:06] and that at that stage we are so deep into the software um weeds and we have
[9:08] into the software um weeds and we have
[9:09] into the software um weeds and we have scripted our own software that has its
[9:10] scripted our own software that has its
[9:10] scripted our own software that has its has its own bugs and so we we tend to
[9:12] has its own bugs and so we we tend to
[9:12] has its own bugs and so we we tend to just uh now we're trapped when we have
[9:14] just uh now we're trapped when we have
[9:14] just uh now we're trapped when we have an issue with connectivity or an issue
[9:15] an issue with connectivity or an issue
[9:16] an issue with connectivity or an issue with um a strange behavior when you have
[9:18] with um a strange behavior when you have
[9:18] with um a strange behavior when you have a motor demand or other device on that
[9:20] a motor demand or other device on that
[9:20] a motor demand or other device on that same 5volt Source it's much harder to
[9:23] same 5volt Source it's much harder to
[9:23] same 5volt Source it's much harder to trace the the issue now this is an issue
[9:26] trace the the issue now this is an issue
[9:26] trace the the issue now this is an issue for Robotics and megatronics makers when
[9:28] for Robotics and megatronics makers when
[9:28] for Robotics and megatronics makers when you have um a whole machine that's is
[9:31] you have um a whole machine that's is
[9:31] you have um a whole machine that's is drawing power from a system that's on
[9:32] drawing power from a system that's on
[9:32] drawing power from a system that's on board um I would say that that General
[9:35] board um I would say that that General
[9:35] board um I would say that that General developers with with Raspberry Pi also
[9:37] developers with with Raspberry Pi also
[9:37] developers with with Raspberry Pi also uh maybe eight out of 10 of them are not
[9:39] uh maybe eight out of 10 of them are not
[9:39] uh maybe eight out of 10 of them are not working with a wireless cordless system
[9:42] working with a wireless cordless system
[9:42] working with a wireless cordless system so the reliability is better I'll give
[9:44] so the reliability is better I'll give
[9:44] so the reliability is better I'll give you an example um let's say a typical
[9:47] you an example um let's say a typical
[9:47] you an example um let's say a typical use case for Raspberry Pi or AI device
[9:48] use case for Raspberry Pi or AI device
[9:48] use case for Raspberry Pi or AI device is um let's say a custom home security
[9:51] is um let's say a custom home security
[9:51] is um let's say a custom home security system where you have a camera hooked up
[9:53] system where you have a camera hooked up
[9:53] system where you have a camera hooked up it's plugged into the wall everything's
[9:54] it's plugged into the wall everything's
[9:54] it's plugged into the wall everything's running as long as you need it to no
[9:55] running as long as you need it to no
[9:56] running as long as you need it to no batteries and it's running AI for face
[9:57] batteries and it's running AI for face
[9:57] batteries and it's running AI for face detection or robotic something detection
[10:00] detection or robotic something detection
[10:00] detection or robotic something detection done with AI um and then those those
[10:03] done with AI um and then those those
[10:03] done with AI um and then those those systems have a solution uh now if you go
[10:05] systems have a solution uh now if you go
[10:05] systems have a solution uh now if you go to a good brand this is called canakit
[10:08] to a good brand this is called canakit
[10:08] to a good brand this is called canakit it's one of the Branded reputable
[10:10] it's one of the Branded reputable
[10:10] it's one of the Branded reputable offerings that that sell Raspberry Pi
[10:12] offerings that that sell Raspberry Pi
[10:12] offerings that that sell Raspberry Pi along with the um SD card and uh power
[10:16] along with the um SD card and uh power
[10:16] along with the um SD card and uh power supply and and maybe an enclosure with a
[10:17] supply and and maybe an enclosure with a
[10:17] supply and and maybe an enclosure with a little fan so they're getting people
[10:19] little fan so they're getting people
[10:19] little fan so they're getting people equipped quickly to get moving um with
[10:21] equipped quickly to get moving um with
[10:21] equipped quickly to get moving um with their Computing
[10:23] their Computing
[10:23] their Computing efforts so um this video was initiated
[10:26] efforts so um this video was initiated
[10:26] efforts so um this video was initiated uh when I was writing an email to ask
[10:28] uh when I was writing an email to ask
[10:28] uh when I was writing an email to ask one specific specific question and
[10:29] one specific specific question and
[10:29] one specific specific question and that's what is your recommended uh power
[10:31] that's what is your recommended uh power
[10:31] that's what is your recommended uh power adapter or even a brand that has a
[10:33] adapter or even a brand that has a
[10:33] adapter or even a brand that has a series of adapters that is reliable for
[10:35] series of adapters that is reliable for
[10:35] series of adapters that is reliable for remote power um when those AI projects
[10:38] remote power um when those AI projects
[10:38] remote power um when those AI projects that are using onboard Computing single
[10:40] that are using onboard Computing single
[10:40] that are using onboard Computing single board computers when those projects Go
[10:41] board computers when those projects Go
[10:42] board computers when those projects Go Mobile now suddenly they have problems
[10:43] Mobile now suddenly they have problems
[10:43] Mobile now suddenly they have problems that they were not expecting um as do
[10:46] that they were not expecting um as do
[10:46] that they were not expecting um as do any of the the designers who make
[10:48] any of the the designers who make
[10:48] any of the the designers who make robotic things straight away um so I
[10:51] robotic things straight away um so I
[10:51] robotic things straight away um so I suspect that they don't have a very
[10:53] suspect that they don't have a very
[10:53] suspect that they don't have a very particular answer when I worked with
[10:54] particular answer when I worked with
[10:54] particular answer when I worked with Texas Instruments uh a couple years ago
[10:56] Texas Instruments uh a couple years ago
[10:56] Texas Instruments uh a couple years ago we were setting up a similar um system
[10:59] we were setting up a similar um system
[10:59] we were setting up a similar um system with the Texas Instruments Edge AI
[11:01] with the Texas Instruments Edge AI
[11:01] with the Texas Instruments Edge AI machine it's an even It's a larger board
[11:03] machine it's an even It's a larger board
[11:03] machine it's an even It's a larger board also I think it's it's powered with the
[11:05] also I think it's it's powered with the
[11:05] also I think it's it's powered with the same with the same method it may have PD
[11:07] same with the same method it may have PD
[11:07] same with the same method it may have PD available once you use PD then then you
[11:10] available once you use PD then then you
[11:10] available once you use PD then then you allow a negotiation between the adapter
[11:12] allow a negotiation between the adapter
[11:12] allow a negotiation between the adapter and the and the Machine and there are in
[11:16] and the and the Machine and there are in
[11:16] and the and the Machine and there are in my opinion more chances that you can get
[11:17] my opinion more chances that you can get
[11:17] my opinion more chances that you can get the power sufficiently um available um
[11:20] the power sufficiently um available um
[11:20] the power sufficiently um available um higher voltage is is better in my
[11:22] higher voltage is is better in my
[11:22] higher voltage is is better in my opinion it makes sense why you would
[11:23] opinion it makes sense why you would
[11:23] opinion it makes sense why you would want to uh consume power at 5 volts
[11:26] want to uh consume power at 5 volts
[11:26] want to uh consume power at 5 volts because there are so many devices like
[11:28] because there are so many devices like
[11:28] because there are so many devices like as I mentioned that already are
[11:30] as I mentioned that already are
[11:30] as I mentioned that already are available with that 5vt power level but
[11:34] available with that 5vt power level but
[11:34] available with that 5vt power level but for robotic
[11:35] for robotic
[11:35] for robotic systems it's nice to have it's nice to
[11:37] systems it's nice to have it's nice to
[11:37] systems it's nice to have it's nice to have the higher voltage of PD so this
[11:39] have the higher voltage of PD so this
[11:39] have the higher voltage of PD so this adapter is unusual this one comes with
[11:40] adapter is unusual this one comes with
[11:40] adapter is unusual this one comes with the canakit and it's high quality
[11:43] the canakit and it's high quality
[11:43] the canakit and it's high quality Raspberry Pi also sells one that's uh
[11:45] Raspberry Pi also sells one that's uh
[11:45] Raspberry Pi also sells one that's uh this one's rated at 5.1 volts 3.5 amps
[11:48] this one's rated at 5.1 volts 3.5 amps
[11:48] this one's rated at 5.1 volts 3.5 amps and that is actually a very you see how
[11:51] and that is actually a very you see how
[11:51] and that is actually a very you see how the cable is very thick the label is is
[11:54] the cable is very thick the label is is
[11:54] the cable is very thick the label is is full of information model numbers there
[11:56] full of information model numbers there
[11:56] full of information model numbers there and so this is good quality um but it's
[11:59] and so this is good quality um but it's
[11:59] and so this is good quality um but it's not it's not the most common this level
[12:02] not it's not the most common this level
[12:02] not it's not the most common this level of quality is not very well matched by
[12:04] of quality is not very well matched by
[12:04] of quality is not very well matched by offerings that are portable so that's
[12:06] offerings that are portable so that's
[12:06] offerings that are portable so that's the question of how how do you the users
[12:09] the question of how how do you the users
[12:09] the question of how how do you the users how do you guys Source power when you're
[12:11] how do you guys Source power when you're
[12:12] how do you guys Source power when you're taking power from a 12volt source to
[12:14] taking power from a 12volt source to
[12:14] taking power from a 12volt source to this and how would you repeat that if
[12:15] this and how would you repeat that if
[12:15] this and how would you repeat that if other variables change so um besides
[12:18] other variables change so um besides
[12:18] other variables change so um besides that one very model number is there a
[12:20] that one very model number is there a
[12:20] that one very model number is there a brand that you know of that's available
[12:21] brand that you know of that's available
[12:21] brand that you know of that's available on Mouser they worldwide or Digi
[12:23] on Mouser they worldwide or Digi
[12:23] on Mouser they worldwide or Digi key they ship worldwide and element 14
[12:25] key they ship worldwide and element 14
[12:25] key they ship worldwide and element 14 AO Electronics so I don't want to just
[12:28] AO Electronics so I don't want to just
[12:28] AO Electronics so I don't want to just find one solution one type of power
[12:30] find one solution one type of power
[12:30] find one solution one type of power adapter I would like to know um is there
[12:33] adapter I would like to know um is there
[12:33] adapter I would like to know um is there a brand that has come out to meet a
[12:35] a brand that has come out to meet a
[12:35] a brand that has come out to meet a range of needs and all always offer data
[12:37] range of needs and all always offer data
[12:38] range of needs and all always offer data sheets because this is what we need in
[12:40] sheets because this is what we need in
[12:40] sheets because this is what we need in the Scuttle organization we need to
[12:41] the Scuttle organization we need to
[12:41] the Scuttle organization we need to recommend that to our users we need to
[12:43] recommend that to our users we need to
[12:43] recommend that to our users we need to provide so when we sell this kit and we
[12:45] provide so when we sell this kit and we
[12:45] provide so when we sell this kit and we especially if we sell it with a the
[12:47] especially if we sell it with a the
[12:47] especially if we sell it with a the high-powered Computing um then we ALS we
[12:50] high-powered Computing um then we ALS we
[12:50] high-powered Computing um then we ALS we are selling them a problem and we also
[12:51] are selling them a problem and we also
[12:51] are selling them a problem and we also need to offer the solution to that
[12:53] need to offer the solution to that
[12:53] need to offer the solution to that problem at the very same time um not
[12:55] problem at the very same time um not
[12:55] problem at the very same time um not that's not just relating to selling
[12:56] that's not just relating to selling
[12:56] that's not just relating to selling that's for the whole open source
[12:58] that's for the whole open source
[12:58] that's for the whole open source Community everyone that's designing
[12:59] Community everyone that's designing
[12:59] Community everyone that's designing robots and trying to advance robotics or
[13:01] robots and trying to advance robotics or
[13:01] robots and trying to advance robotics or learn uh they need the the solutions
[13:03] learn uh they need the the solutions
[13:03] learn uh they need the the solutions that we uh we are not so equipped the
[13:07] that we uh we are not so equipped the
[13:07] that we uh we are not so equipped the whole Computing space is still quite
[13:08] whole Computing space is still quite
[13:08] whole Computing space is still quite segmented away from the robotic space
[13:10] segmented away from the robotic space
[13:10] segmented away from the robotic space okay I'm doing AI I'm doing software
[13:12] okay I'm doing AI I'm doing software
[13:12] okay I'm doing AI I'm doing software development but we need to build that
[13:15] development but we need to build that
[13:15] development but we need to build that bridge better to the the hardware side
[13:18] bridge better to the the hardware side
[13:18] bridge better to the the hardware side um it all needs the solutions need to be
[13:20] um it all needs the solutions need to be
[13:20] um it all needs the solutions need to be available together so if any of the
[13:22] available together so if any of the
[13:22] available together so if any of the users have ideas I'd love to hear them
[13:24] users have ideas I'd love to hear them
[13:24] users have ideas I'd love to hear them um I'll backtrack just a little bit I
[13:26] um I'll backtrack just a little bit I
[13:26] um I'll backtrack just a little bit I was telling a story of integrating with
[13:27] was telling a story of integrating with
[13:27] was telling a story of integrating with the ti machine um at that time our
[13:29] the ti machine um at that time our
[13:29] the ti machine um at that time our experts at TI were shopping lots of
[13:32] experts at TI were shopping lots of
[13:32] experts at TI were shopping lots of various brands of portable power Banks
[13:34] various brands of portable power Banks
[13:34] various brands of portable power Banks so that they could find one that meets
[13:36] so that they could find one that meets
[13:36] so that they could find one that meets uh meets their needs and that one
[13:38] uh meets their needs and that one
[13:38] uh meets their needs and that one solution is not a carryover the the
[13:40] solution is not a carryover the the
[13:40] solution is not a carryover the the brand may not have a long life or it may
[13:42] brand may not have a long life or it may
[13:42] brand may not have a long life or it may not have availability around the world
[13:43] not have availability around the world
[13:43] not have availability around the world so we need we need the the full solution
[13:45] so we need we need the the full solution
[13:45] so we need we need the the full solution available I'll leave I'll wrap up this
[13:47] available I'll leave I'll wrap up this
[13:48] available I'll leave I'll wrap up this video with the question of um how do
[13:50] video with the question of um how do
[13:50] video with the question of um how do users and my audience how do you handle
[13:53] users and my audience how do you handle
[13:53] users and my audience how do you handle making power available for your digital
[13:55] making power available for your digital
[13:55] making power available for your digital devices when there's no power delivery
[13:57] devices when there's no power delivery
[13:57] devices when there's no power delivery no PD and when you're coming from a a
[14:01] no PD and when you're coming from a a
[14:01] no PD and when you're coming from a a wireless sorry a portable battery system
[14:04] wireless sorry a portable battery system
[14:04] wireless sorry a portable battery system and how do we solve this without
[14:07] and how do we solve this without
[14:07] and how do we solve this without building our own custom circuit just to
[14:10] building our own custom circuit just to
[14:10] building our own custom circuit just to do something that's very very possible
[14:13] do something that's very very possible
[14:13] do something that's very very possible and feasible um with off the-shelf
[14:16] and feasible um with off the-shelf
[14:16] and feasible um with off the-shelf products last bit here um your comments
[14:19] products last bit here um your comments
[14:19] products last bit here um your comments on these videos have been fantastic for
[14:22] on these videos have been fantastic for
[14:22] on these videos have been fantastic for delivering key information and beginning
[14:25] delivering key information and beginning
[14:25] delivering key information and beginning conversations and if you have more to
[14:28] conversations and if you have more to
[14:28] conversations and if you have more to talk about and share with us I always
[14:30] talk about and share with us I always
[14:31] talk about and share with us I always have my Discord linked here and there's
[14:33] have my Discord linked here and there's
[14:33] have my Discord linked here and there's loads of brilliant people in there um
[14:36] loads of brilliant people in there um
[14:36] loads of brilliant people in there um sharing knowledge so you're always
[14:38] sharing knowledge so you're always
[14:38] sharing knowledge so you're always welcome to share deeper insights here in
[14:41] welcome to share deeper insights here in
[14:41] welcome to share deeper insights here in the Discord

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
