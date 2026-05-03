---
title: "SCUTTLE Robot - Beaglebone Blue setup WPA enterprise WiFi"
url: "https://www.youtube.com/watch?v=5l-xO3AWcM8"
video_id: "5l-xO3AWcM8"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2019-08-26
duration: "4:13"
duration_sec: 253
views: 262
likes: 2
category: "Entertainment"
keywords: ["yt:cc=on", "scuttle robot"]
thumbnail_url: "https://i.ytimg.com/vi/5l-xO3AWcM8/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 142
chapters_count: 0
has_description: true
has_comments: false
---

## Description

SCUTTLE Project: MXET.github.com/SCUTTLE

In this video: connecting to Beaglebone wifi access point (AP), retrieving a python program from the project github, configure the beagle's Debian OS to connect by wifi to the Enterprise Wifi access point, and specifically, connect to the wifi at your university (this one is at Texas A&M but most are similar). Enterprise APs are special because they require both a username and password.

This video supports MXET 300 Lab1 from fall 2019.

## Transcript

[0:04] okay at this time you have installed the
[0:04] okay at this time you have installed the latest Debian image on your beagle and
[0:06] latest Debian image on your beagle and
[0:06] latest Debian image on your beagle and it's time to get your beagle connected
[0:08] it's time to get your beagle connected
[0:08] it's time to get your beagle connected to the Internet so first we need to get
[0:11] to the Internet so first we need to get
[0:11] to the Internet so first we need to get access to a file that we will use when
[0:13] access to a file that we will use when
[0:13] access to a file that we will use when we're offline but connected by Wi-Fi to
[0:16] we're offline but connected by Wi-Fi to
[0:16] we're offline but connected by Wi-Fi to the Beagle you navigate to scuttle the
[0:20] the Beagle you navigate to scuttle the
[0:20] the Beagle you navigate to scuttle the scuttle github web page then you're
[0:22] scuttle github web page then you're
[0:22] scuttle github web page then you're going to go to software Python basics
[0:25] going to go to software Python basics
[0:25] going to go to software Python basics and come down here to find setup WPA
[0:28] and come down here to find setup WPA
[0:28] and come down here to find setup WPA enterprise PI it's called that PI
[0:31] enterprise PI it's called that PI
[0:31] enterprise PI it's called that PI because it's a Python program if you
[0:34] because it's a Python program if you
[0:34] because it's a Python program if you click raw then you're going to get only
[0:36] click raw then you're going to get only
[0:36] click raw then you're going to get only the text of the program control a
[0:38] the text of the program control a
[0:38] the text of the program control a control copy control that is control C
[0:42] control copy control that is control C
[0:42] control copy control that is control C and go to your desktop create a new text
[0:48] and go to your desktop create a new text
[0:48] and go to your desktop create a new text document I'll just name it accurately
[1:05] for good measure I'm going to edit with
[1:05] for good measure I'm going to edit with notepad plus plus I will paste my text
[1:08] notepad plus plus I will paste my text
[1:08] notepad plus plus I will paste my text here and I don't even need to save it
[1:10] here and I don't even need to save it
[1:10] here and I don't even need to save it because I don't need to close it now
[1:13] because I don't need to close it now
[1:13] because I don't need to close it now we're going to come over to cloud 9 at
[1:19] we're going to come over to cloud 9 at
[1:19] we're going to come over to cloud 9 at this point you will have connected your
[1:23] this point you will have connected your
[1:23] this point you will have connected your Wi-Fi to your BeagleBone by finding the
[1:26] Wi-Fi to your BeagleBone by finding the
[1:26] Wi-Fi to your BeagleBone by finding the SSID that's your signature here you're
[1:30] SSID that's your signature here you're
[1:30] SSID that's your signature here you're going to connect using password
[1:32] going to connect using password
[1:32] going to connect using password BeagleBone with no spaces and capital
[1:35] BeagleBone with no spaces and capital
[1:35] BeagleBone with no spaces and capital b's and then you'll arrive here in the
[1:39] b's and then you'll arrive here in the
[1:39] b's and then you'll arrive here in the cloud9 IDE after you've chosen 192.168.1
[1:46] cloud9 IDE after you've chosen 192.168.1
[1:46] cloud9 IDE after you've chosen 192.168.1 colon 3000 that's support 3000 then we
[1:51] colon 3000 that's support 3000 then we
[1:51] colon 3000 that's support 3000 then we are going to look at the workspace where
[1:54] are going to look at the workspace where
[1:54] are going to look at the workspace where we have our tree of folders we are going
[1:57] we have our tree of folders we are going
[1:57] we have our tree of folders we are going to show home in favorites so the home
[2:01] to show home in favorites so the home
[2:01] to show home in favorites so the home will be shown by default we can make a
[2:03] will be shown by default we can make a
[2:03] will be shown by default we can make a new terminal if you do LS then you can
[2:09] new terminal if you do LS then you can
[2:09] new terminal if you do LS then you can see the files that are located in the
[2:10] see the files that are located in the
[2:10] see the files that are located in the cloud 9 directory if you type CD space
[2:14] cloud 9 directory if you type CD space
[2:14] cloud 9 directory if you type CD space tilde and to enter then we can reach the
[2:19] tilde and to enter then we can reach the
[2:19] tilde and to enter then we can reach the the home directory but where we should
[2:22] the home directory but where we should
[2:22] the home directory but where we should have just one file LS enter we have a
[2:26] have just one file LS enter we have a
[2:26] have just one file LS enter we have a folder called bin and we have setup WPA
[2:28] folder called bin and we have setup WPA
[2:28] folder called bin and we have setup WPA enterprise type hi because I already
[2:31] enterprise type hi because I already
[2:31] enterprise type hi because I already created it to create it again in order
[2:33] created it to create it again in order
[2:33] created it to create it again in order to create it for the first time you're
[2:35] to create it for the first time you're
[2:35] to create it for the first time you're going to right click on that folder
[2:36] going to right click on that folder
[2:36] going to right click on that folder you're gonna do new file my file dot I
[2:45] you're gonna do new file my file dot I
[2:45] you're gonna do new file my file dot I single click outside of it it'll
[2:48] single click outside of it it'll
[2:48] single click outside of it it'll complete making the file and you can
[2:50] complete making the file and you can
[2:50] complete making the file and you can double click it to open it in my case
[2:53] double click it to open it in my case
[2:53] double click it to open it in my case I've double clicked the setup WPA I've
[2:56] I've double clicked the setup WPA I've
[2:56] I've double clicked the setup WPA I've pasted in the information from this file
[2:59] pasted in the information from this file
[2:59] pasted in the information from this file and I will ctrl s to save and you'll see
[3:03] and I will ctrl s to save and you'll see
[3:03] and I will ctrl s to save and you'll see all changes saved shown here you can
[3:06] all changes saved shown here you can
[3:06] all changes saved shown here you can close your python file and return to the
[3:08] close your python file and return to the
[3:08] close your python file and return to the terminal now you need to navigate to the
[3:13] terminal now you need to navigate to the
[3:13] terminal now you need to navigate to the home directory CD space tilde enter LS
[3:17] home directory CD space tilde enter LS
[3:17] home directory CD space tilde enter LS here we go we're gonna run it python
[3:20] here we go we're gonna run it python
[3:20] here we go we're gonna run it python sudo python 3 setup underscore wpa
[3:25] sudo python 3 setup underscore wpa
[3:25] sudo python 3 setup underscore wpa da-da-da-da-dah
[3:27] da-da-da-da-dah
[3:27] da-da-da-da-dah enter to EMP PWD and now you're going to
[3:33] enter to EMP PWD and now you're going to
[3:33] enter to EMP PWD and now you're going to enter your credentials for the WPA tammy
[3:38] enter your credentials for the WPA tammy
[3:38] enter your credentials for the WPA tammy link wpa access point and i won't show
[3:42] link wpa access point and i won't show
[3:42] link wpa access point and i won't show this part but it will hide the
[3:43] this part but it will hide the
[3:43] this part but it will hide the characters for your password it will not
[3:46] characters for your password it will not
[3:46] characters for your password it will not hide the characters for your username
[3:49] hide the characters for your username
[3:49] hide the characters for your username but then after it goes through the menu
[3:54] but then after it goes through the menu
[3:54] but then after it goes through the menu it should connect to the internet you
[3:56] it should connect to the internet you
[3:56] it should connect to the internet you may need to reboot your beagle and then
[4:00] may need to reboot your beagle and then
[4:00] may need to reboot your beagle and then you will be you will have a
[4:01] you will be you will have a
[4:01] you will be you will have a configuration file saved on your beagle
[4:04] configuration file saved on your beagle
[4:04] configuration file saved on your beagle that contains the information to log on
[4:06] that contains the information to log on
[4:06] that contains the information to log on and it should automatically connect to
[4:08] and it should automatically connect to
[4:08] and it should automatically connect to the internet from there on

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
