---
title: "SCUTTLE Robot - Check boot drive space in Debian on Beaglebone Blue"
url: "https://www.youtube.com/watch?v=SzzNJBzTZss"
video_id: "SzzNJBzTZss"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-09-04
duration: "3:01"
duration_sec: 181
views: 44
likes: 1
category: "Entertainment"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/SzzNJBzTZss/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 106
chapters_count: 0
has_description: true
has_comments: false
---

## Description

useful commands to see what disc you have booted from and how much space is remaining.

## Transcript

[0:02] this is just a quick video to check some
[0:02] this is just a quick video to check some items on your boot drive and partitions
[0:06] items on your boot drive and partitions
[0:06] items on your boot drive and partitions you have available if you've run the
[0:08] you have available if you've run the
[0:08] you have available if you've run the command called F disk space - L you're
[0:15] command called F disk space - L you're
[0:15] command called F disk space - L you're gonna get this output that talks about
[0:17] gonna get this output that talks about
[0:17] gonna get this output that talks about the the memory hardware and partitions
[0:22] the the memory hardware and partitions
[0:22] the the memory hardware and partitions that you have available so the
[0:25] that you have available so the
[0:25] that you have available so the information starts with these headers
[0:27] information starts with these headers
[0:27] information starts with these headers and when you see this header it's a it's
[0:30] and when you see this header it's a it's
[0:30] and when you see this header it's a it's indicating a list of the partitions you
[0:32] indicating a list of the partitions you
[0:32] indicating a list of the partitions you have already created on your device so
[0:36] have already created on your device so
[0:36] have already created on your device so right now it's only considering the
[0:38] right now it's only considering the
[0:38] right now it's only considering the partition on the SD card that is not the
[0:43] partition on the SD card that is not the
[0:43] partition on the SD card that is not the internal memory of the Beagle and that
[0:46] internal memory of the Beagle and that
[0:46] internal memory of the Beagle and that SD card has had its partition grown to
[0:49] SD card has had its partition grown to
[0:49] SD card has had its partition grown to 14.5 gigabytes
[0:51] 14.5 gigabytes
[0:51] 14.5 gigabytes by doing the commands in our self
[0:53] by doing the commands in our self
[0:53] by doing the commands in our self installer part 1 so when you see this is
[0:57] installer part 1 so when you see this is
[0:57] installer part 1 so when you see this is kind of the signature for the memory
[0:59] kind of the signature for the memory
[0:59] kind of the signature for the memory block it has a star because that's the
[1:01] block it has a star because that's the
[1:01] block it has a star because that's the one it's booting from and if we had more
[1:04] one it's booting from and if we had more
[1:04] one it's booting from and if we had more block blocks partitioned and ready to
[1:06] block blocks partitioned and ready to
[1:06] block blocks partitioned and ready to use then those would be listed with no
[1:09] use then those would be listed with no
[1:09] use then those would be listed with no star and because this this name matches
[1:14] star and because this this name matches
[1:14] star and because this this name matches the name of above back before we ran the
[1:17] the name of above back before we ran the
[1:17] the name of above back before we ran the self installer this size here was only
[1:20] self installer this size here was only
[1:20] self installer this size here was only three points something gigabytes and we
[1:23] three points something gigabytes and we
[1:23] three points something gigabytes and we needed to expand that partition and we
[1:26] needed to expand that partition and we
[1:26] needed to expand that partition and we could see basically that it matched this
[1:28] could see basically that it matched this
[1:28] could see basically that it matched this name to this name and all of the 14
[1:31] name to this name and all of the 14
[1:32] name to this name and all of the 14 point 5 gigabytes were there on the disk
[1:34] point 5 gigabytes were there on the disk
[1:34] point 5 gigabytes were there on the disk but they weren't partitioned any other
[1:37] but they weren't partitioned any other
[1:37] but they weren't partitioned any other useful information on here would be to
[1:40] useful information on here would be to
[1:40] useful information on here would be to show that the the device named block 1
[1:44] show that the the device named block 1
[1:44] show that the the device named block 1 it has three point six gigabytes which
[1:47] it has three point six gigabytes which
[1:47] it has three point six gigabytes which seems to coincide with the four
[1:49] seems to coincide with the four
[1:49] seems to coincide with the four gigabytes we we should have on our on
[1:54] gigabytes we we should have on our on
[1:54] gigabytes we we should have on our on our Beagle it seems that whenever
[1:56] our Beagle it seems that whenever
[1:56] our Beagle it seems that whenever whatever is labeled or advertised you
[1:58] whatever is labeled or advertised you
[1:58] whatever is labeled or advertised you have a little bit less space than that
[2:00] have a little bit less space than that
[2:00] have a little bit less space than that on available on once you're in your
[2:03] on available on once you're in your
[2:03] on available on once you're in your operating system
[2:05] operating system
[2:05] operating system so the other information that you can
[2:09] so the other information that you can
[2:09] so the other information that you can quickly get is with a pseudo what DF you
[2:16] quickly get is with a pseudo what DF you
[2:16] quickly get is with a pseudo what DF you don't need pseudo for this one DF space
[2:18] don't need pseudo for this one DF space
[2:18] don't need pseudo for this one DF space what is it slash slash that's gonna
[2:23] what is it slash slash that's gonna
[2:23] what is it slash slash that's gonna refer to your root directory you can see
[2:27] refer to your root directory you can see
[2:27] refer to your root directory you can see how much space you have used which in
[2:30] how much space you have used which in
[2:30] how much space you have used which in our case is 1.9 gigabytes and it's only
[2:38] our case is 1.9 gigabytes and it's only
[2:38] our case is 1.9 gigabytes and it's only 14% of what we have available if you
[2:42] 14% of what we have available if you
[2:42] 14% of what we have available if you added a flash drive I believe that would
[2:46] added a flash drive I believe that would
[2:46] added a flash drive I believe that would also show up here in this list or if you
[2:49] also show up here in this list or if you
[2:49] also show up here in this list or if you partitioned the the onboard memory on
[2:52] partitioned the the onboard memory on
[2:52] partitioned the the onboard memory on the Beagle to be storage space

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
