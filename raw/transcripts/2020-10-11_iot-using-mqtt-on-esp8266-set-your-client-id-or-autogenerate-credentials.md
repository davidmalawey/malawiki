---
title: "IoT using MQTT on ESP8266 - set your client ID or autogenerate credentials"
url: "https://www.youtube.com/watch?v=CTDlxl7dhgs"
video_id: "CTDlxl7dhgs"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-10-11
duration: "7:25"
duration_sec: 445
views: 1583
likes: 10
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/CTDlxl7dhgs/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 352
chapters_count: 4
has_description: true
has_comments: false
---

## Description

I made this video to document today's learning on Client ID, MQTT connection error codes, ESP8266 library for MQTT, and making my own credentials in the arduino code.

Video Contents:
This video relates to ESP8266
1) MQTT connection error
2) how is the client ID generated
3) Is ID, Username, Password required?
4) Set your own credentials
5) A good example & library to start from

CAD models for the ESP & 3D printed SCUTTLE bracket are found on my GrabCAD page.
https://grabcad.com/david.m-50/models

Since this is an effort to enhance the SCUTTLE Robotic IoT ecosystem, find more about that project here:
https://mxet.github.io/SCUTTLE

## Chapters

- 0:00 Intro
- 0:19 The problem
- 5:26 Conclusion
- 6:37 Example

## Transcript

[0:04] today i was working with my esp device
[0:04] today i was working with my esp device over here and i had a new era that i
[0:07] over here and i had a new era that i
[0:07] over here and i had a new era that i haven't had before so i want to
[0:09] haven't had before so i want to
[0:09] haven't had before so i want to document it for myself i did a quick
[0:11] document it for myself i did a quick
[0:11] document it for myself i did a quick dive into
[0:13] dive into
[0:13] dive into the root cause and and i got
[0:16] the root cause and and i got
[0:16] the root cause and and i got some progress so let me share it
[0:19] some progress so let me share it
[0:19] some progress so let me share it this is my serial window for the arduino
[0:22] this is my serial window for the arduino
[0:22] this is my serial window for the arduino um while it's running
[0:24] um while it's running
[0:24] um while it's running and right here where it says attempting
[0:26] and right here where it says attempting
[0:26] and right here where it says attempting to connect to the mqtt broker
[0:29] to connect to the mqtt broker
[0:29] to connect to the mqtt broker on my last connection i got an
[0:32] on my last connection i got an
[0:32] on my last connection i got an error it said error code 2 from the
[0:34] error it said error code 2 from the
[0:34] error it said error code 2 from the broker so i dove in
[0:36] broker so i dove in
[0:36] broker so i dove in to find out what is what are the common
[0:46] error codes i found a reference i found
[0:46] error codes i found a reference i found that
[0:47] that
[0:47] that error two is the connection is refused
[0:49] error two is the connection is refused
[0:50] error two is the connection is refused because the identifier is rejected
[0:52] because the identifier is rejected
[0:52] because the identifier is rejected um there's probably a lot of reading to
[0:54] um there's probably a lot of reading to
[0:54] um there's probably a lot of reading to do about what that truly means but
[0:57] do about what that truly means but
[0:57] do about what that truly means but before i start to study i i looked for
[1:00] before i start to study i i looked for
[1:00] before i start to study i i looked for someone else with this
[1:01] someone else with this
[1:01] someone else with this issue so someone else said
[1:08] they got the same error and they're not
[1:08] they got the same error and they're not sure why
[1:09] sure why
[1:10] sure why someone else is responding there's no
[1:12] someone else is responding there's no
[1:12] someone else is responding there's no client id
[1:13] client id
[1:13] client id set now the way this library is supposed
[1:15] set now the way this library is supposed
[1:15] set now the way this library is supposed to work
[1:16] to work
[1:16] to work is the the library called
[1:26] arduino mqtt client is supposed to
[1:26] arduino mqtt client is supposed to generate an
[1:27] generate an
[1:27] generate an automatic client id for you
[1:30] automatic client id for you
[1:30] automatic client id for you when you're connecting to their broker
[1:32] when you're connecting to their broker
[1:32] when you're connecting to their broker to it to any broker sorry
[1:35] to it to any broker sorry
[1:35] to it to any broker sorry and this seems to be fairly standard
[1:37] and this seems to be fairly standard
[1:37] and this seems to be fairly standard because if you go to the websocket
[1:39] because if you go to the websocket
[1:39] because if you go to the websocket client you'll find
[1:46] that in this connection configuration it
[1:46] that in this connection configuration it says
[1:48] says
[1:48] says it says at some point that this client
[1:49] it says at some point that this client
[1:49] it says at some point that this client id is automatically generated
[1:51] id is automatically generated
[1:51] id is automatically generated and if you leave the page and come back
[1:53] and if you leave the page and come back
[1:53] and if you leave the page and come back then there's a new one and it's fairly
[1:55] then there's a new one and it's fairly
[1:55] then there's a new one and it's fairly random
[1:56] random
[1:56] random so the client the broker just needs
[2:00] so the client the broker just needs
[2:00] so the client the broker just needs something there and it also does not
[2:02] something there and it also does not
[2:02] something there and it also does not need a
[2:03] need a
[2:03] need a username and password you can leave
[2:05] username and password you can leave
[2:05] username and password you can leave these blank
[2:06] these blank
[2:06] these blank but today i'm adding some just to see if
[2:09] but today i'm adding some just to see if
[2:09] but today i'm adding some just to see if it solves my problem
[2:12] it solves my problem
[2:12] it solves my problem so um this arduino
[2:16] so um this arduino
[2:16] so um this arduino program which i need to bring down here
[2:19] program which i need to bring down here
[2:19] program which i need to bring down here this arduino program
[2:20] this arduino program
[2:20] this arduino program is a derivative from a few examples that
[2:24] is a derivative from a few examples that
[2:24] is a derivative from a few examples that i've
[2:24] i've
[2:24] i've modified and added features to but at
[2:27] modified and added features to but at
[2:27] modified and added features to but at the root
[2:28] the root
[2:28] the root it's an example that comes from the
[2:30] it's an example that comes from the
[2:30] it's an example that comes from the arduino mqtt client library
[2:33] arduino mqtt client library
[2:33] arduino mqtt client library so i wanted to find out what's happening
[2:36] so i wanted to find out what's happening
[2:36] so i wanted to find out what's happening with the auto generation of client id
[2:38] with the auto generation of client id
[2:38] with the auto generation of client id and i haven't looked closely at this
[2:41] and i haven't looked closely at this
[2:41] and i haven't looked closely at this part of the library before
[2:43] part of the library before
[2:43] part of the library before so today i did the mq client this is a
[2:47] so today i did the mq client this is a
[2:47] so today i did the mq client this is a function i made
[2:48] function i made
[2:48] function i made but i copied and pasted these lines what
[2:51] but i copied and pasted these lines what
[2:51] but i copied and pasted these lines what happens is
[2:52] happens is
[2:52] happens is it says you can provide a unique client
[2:54] it says you can provide a unique client
[2:54] it says you can provide a unique client id if not
[2:55] id if not
[2:55] id if not set the library uses arduino
[2:58] set the library uses arduino
[2:58] set the library uses arduino millis which will
[3:01] millis which will
[3:01] millis which will bring you a fairly random number because
[3:04] bring you a fairly random number because
[3:04] bring you a fairly random number because it's going to be in the
[3:05] it's going to be in the
[3:05] it's going to be in the tens of thousands or hundreds of
[3:07] tens of thousands or hundreds of
[3:07] tens of thousands or hundreds of thousands it's a milliseconds since the
[3:09] thousands it's a milliseconds since the
[3:09] thousands it's a milliseconds since the boot
[3:10] boot
[3:10] boot and it's unlikely to repeat the same id
[3:15] and it's unlikely to repeat the same id
[3:15] and it's unlikely to repeat the same id very often um because
[3:18] very often um because
[3:18] very often um because it's just hard to capture the same
[3:20] it's just hard to capture the same
[3:20] it's just hard to capture the same millisecond that you captured in another
[3:22] millisecond that you captured in another
[3:22] millisecond that you captured in another occasion
[3:23] occasion
[3:23] occasion anyway so now i'm making my own client
[3:25] anyway so now i'm making my own client
[3:26] anyway so now i'm making my own client id to this is going to be
[3:27] id to this is going to be
[3:27] id to this is going to be scuttle esp6011 i'm going to try to stay
[3:31] scuttle esp6011 i'm going to try to stay
[3:31] scuttle esp6011 i'm going to try to stay away from
[3:31] away from
[3:31] away from characters such as dots spaces
[3:35] characters such as dots spaces
[3:35] characters such as dots spaces spaces probably wouldn't work anyway but
[3:37] spaces probably wouldn't work anyway but
[3:37] spaces probably wouldn't work anyway but i'm going to try out this as my
[3:40] i'm going to try out this as my
[3:40] i'm going to try out this as my my standard for now if i hook up another
[3:42] my standard for now if i hook up another
[3:42] my standard for now if i hook up another esp device
[3:43] esp device
[3:43] esp device in my scuttle environment then i'll call
[3:46] in my scuttle environment then i'll call
[3:46] in my scuttle environment then i'll call it 6012.
[3:48] it 6012.
[3:48] it 6012. um and it says you can provide a
[3:50] um and it says you can provide a
[3:50] um and it says you can provide a username and password for authentic
[3:52] username and password for authentic
[3:52] username and password for authentic authentication um also this
[3:55] authentication um also this
[3:55] authentication um also this this is the part that's not required so
[3:59] this is the part that's not required so
[3:59] this is the part that's not required so i'm going to fill it out i'm going to
[4:00] i'm going to fill it out i'm going to
[4:00] i'm going to fill it out i'm going to call myself skittle user 601
[4:04] call myself skittle user 601
[4:04] call myself skittle user 601 and i'm going to name my password the
[4:06] and i'm going to name my password the
[4:06] and i'm going to name my password the super generic
[4:08] super generic
[4:08] super generic t-e-m-p pwd
[4:11] t-e-m-p pwd
[4:11] t-e-m-p pwd which i don't mind sharing at this point
[4:13] which i don't mind sharing at this point
[4:13] which i don't mind sharing at this point because i'm not doing anything
[4:15] because i'm not doing anything
[4:15] because i'm not doing anything i need to maintain control of or or
[4:19] i need to maintain control of or or
[4:19] i need to maintain control of or or secrecy if i start to pass
[4:23] secrecy if i start to pass
[4:23] secrecy if i start to pass data that i'll use to control robots
[4:26] data that i'll use to control robots
[4:26] data that i'll use to control robots here then if there's anything related to
[4:29] here then if there's anything related to
[4:29] here then if there's anything related to safety
[4:30] safety
[4:30] safety or privacy then then that's going to be
[4:33] or privacy then then that's going to be
[4:33] or privacy then then that's going to be made into something non-generic but
[4:36] made into something non-generic but
[4:36] made into something non-generic but we're going
[4:37] we're going
[4:37] we're going right now from from nothing to something
[4:39] right now from from nothing to something
[4:39] right now from from nothing to something so
[4:40] so
[4:40] so um now i
[4:44] um now i
[4:44] um now i went ahead and connected again and
[4:49] went ahead and connected again and
[4:49] went ahead and connected again and this time it it connected just fine as
[4:51] this time it it connected just fine as
[4:51] this time it it connected just fine as you can see here
[4:52] you can see here
[4:52] you can see here and i began to publish the rssi
[4:57] and i began to publish the rssi
[4:57] and i began to publish the rssi this is the signal strength of my
[5:00] this is the signal strength of my
[5:00] this is the signal strength of my of my wi-fi and there's another curious
[5:03] of my wi-fi and there's another curious
[5:03] of my wi-fi and there's another curious note that i had to investigate later but
[5:05] note that i had to investigate later but
[5:05] note that i had to investigate later but these numbers are always supposed to be
[5:07] these numbers are always supposed to be
[5:07] these numbers are always supposed to be negative now it's positive i've i think
[5:09] negative now it's positive i've i think
[5:10] negative now it's positive i've i think i've never seen that before so
[5:12] i've never seen that before so
[5:12] i've never seen that before so um that's very strange it's not it's not
[5:15] um that's very strange it's not it's not
[5:15] um that's very strange it's not it's not correct that someone can transmit a
[5:17] correct that someone can transmit a
[5:17] correct that someone can transmit a signal and it
[5:18] signal and it
[5:18] signal and it the the gain has increased by the time
[5:21] the the gain has increased by the time
[5:21] the the gain has increased by the time it reaches you
[5:22] it reaches you
[5:22] it reaches you normally so um
[5:26] normally so um
[5:26] normally so um this is going to become the the standard
[5:29] this is going to become the the standard
[5:29] this is going to become the the standard recommendation
[5:30] recommendation
[5:30] recommendation until i get something that works more
[5:32] until i get something that works more
[5:32] until i get something that works more reliably we
[5:34] reliably we
[5:34] reliably we we took a problem that may be fixable
[5:36] we took a problem that may be fixable
[5:36] we took a problem that may be fixable just by handling the library better
[5:39] just by handling the library better
[5:39] just by handling the library better for example if we understood why
[5:42] for example if we understood why
[5:42] for example if we understood why the arduino millis usually works and it
[5:45] the arduino millis usually works and it
[5:45] the arduino millis usually works and it worked for a couple of years and and now
[5:47] worked for a couple of years and and now
[5:47] worked for a couple of years and and now it doesn't
[5:48] it doesn't
[5:48] it doesn't then we could maybe make a better
[5:51] then we could maybe make a better
[5:51] then we could maybe make a better direction but
[5:52] direction but
[5:52] direction but for now this is this is the direction
[5:55] for now this is this is the direction
[5:55] for now this is this is the direction we'll go
[5:56] we'll go
[5:56] we'll go and i'll put information like this after
[5:59] and i'll put information like this after
[5:59] and i'll put information like this after it's been tested a fair number of times
[6:01] it's been tested a fair number of times
[6:01] it's been tested a fair number of times i'll put that information into the
[6:03] i'll put that information into the
[6:03] i'll put that information into the scuttle
[6:05] scuttle
[6:05] scuttle iot guide where we're sharing our best
[6:08] iot guide where we're sharing our best
[6:08] iot guide where we're sharing our best practices that we found so far for iot
[6:11] practices that we found so far for iot
[6:11] practices that we found so far for iot so um the takeaways from this video
[6:14] so um the takeaways from this video
[6:14] so um the takeaways from this video could be
[6:15] could be
[6:15] could be for you if you're starting out that
[6:18] for you if you're starting out that
[6:18] for you if you're starting out that the uh good library to work with esp8266
[6:24] the uh good library to work with esp8266
[6:24] the uh good library to work with esp8266 and a few others is the arduino mqtt
[6:27] and a few others is the arduino mqtt
[6:27] and a few others is the arduino mqtt client
[6:29] client
[6:29] client the capital letters makes a difference
[6:31] the capital letters makes a difference
[6:31] the capital letters makes a difference because there
[6:32] because there
[6:32] because there there are a couple similar ones with
[6:34] there are a couple similar ones with
[6:34] there are a couple similar ones with different casing
[6:36] different casing
[6:36] different casing here the example that i always use
[6:39] here the example that i always use
[6:39] here the example that i always use is under it's inside the library
[6:43] is under it's inside the library
[6:43] is under it's inside the library arduino mqtt client wi-fi echo callback
[6:48] arduino mqtt client wi-fi echo callback
[6:48] arduino mqtt client wi-fi echo callback and i choose this one because it
[6:52] and i choose this one because it
[6:52] and i choose this one because it uh tests both outgoing and incoming
[6:55] uh tests both outgoing and incoming
[6:56] uh tests both outgoing and incoming or response to um messages that are
[6:59] or response to um messages that are
[6:59] or response to um messages that are subscribed
[7:00] subscribed
[7:00] subscribed so i can test both of those and this
[7:02] so i can test both of those and this
[7:02] so i can test both of those and this doesn't work
[7:03] doesn't work
[7:03] doesn't work out of the box for me so i do some
[7:06] out of the box for me so i do some
[7:06] out of the box for me so i do some manipulation of this and i definitely
[7:08] manipulation of this and i definitely
[7:08] manipulation of this and i definitely change the broker
[7:10] change the broker
[7:10] change the broker you can follow along if you want to do
[7:12] you can follow along if you want to do
[7:12] you can follow along if you want to do the same
[7:14] the same
[7:14] the same style as me if you want to be in the
[7:16] style as me if you want to be in the
[7:16] style as me if you want to be in the scuttle ecosystem
[7:18] scuttle ecosystem
[7:18] scuttle ecosystem you can go into the iot guide and it has
[7:20] you can go into the iot guide and it has
[7:20] you can go into the iot guide and it has the information on that

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
