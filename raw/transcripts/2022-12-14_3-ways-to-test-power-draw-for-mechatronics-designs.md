---
title: "3 Ways to test Power Draw for mechatronics designs"
url: "https://www.youtube.com/watch?v=s4Syzco1ziM"
video_id: "s4Syzco1ziM"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2022-12-14
duration: "9:54"
duration_sec: 594
views: 724
likes: 18
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/s4Syzco1ziM/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 430
chapters_count: 10
has_description: true
has_comments: false
---

## Description

Made for TAMU-MXET students, designing and building mechatronics projects.  Three types of power meters are available for use which can validate your devices, reduce complexity, and help you produce good prototypes.

ALSO: Power Budget Tutorial ►  www.youtube.com/watch?v=DKPFsVOTJpw

0:00 Three tester types
0:41 USB testing small sensors
2:23 USB example measurements
3:01 DC supply testing
4:04 DC 10W load example
5:17 CBA introduction
5:40 CBA Battery Discharge
7:00 CBA Battery Monitoring
8:23 How to choose
8:53 Customize your test

## Chapters

- 0:00 Three tester types
- 0:41 USB testing small sensors
- 2:23 USB example measurements
- 3:01 DC supply testing
- 4:04 DC 10W load example
- 5:17 CBA introduction
- 5:40 CBA Battery Discharge
- 7:00 CBA Battery Monitoring
- 8:23 How to choose
- 8:53 Customize your test

## Transcript

[0:02] these three kinds of Power meters can
[0:02] these three kinds of Power meters can pretty much cover any of the
[0:04] pretty much cover any of the
[0:04] pretty much cover any of the mechatronics projects you want to build
[0:06] mechatronics projects you want to build
[0:06] mechatronics projects you want to build we have USB or USBC type meters they're
[0:10] we have USB or USBC type meters they're
[0:10] we have USB or USBC type meters they're very affordable
[0:12] very affordable
[0:12] very affordable then you have the power works or
[0:15] then you have the power works or
[0:15] then you have the power works or off-brand power works for higher powered
[0:17] off-brand power works for higher powered
[0:17] off-brand power works for higher powered this one says up to 150 amps this is
[0:20] this one says up to 150 amps this is
[0:20] this one says up to 150 amps this is what the name brand unit looks like and
[0:23] what the name brand unit looks like and
[0:23] what the name brand unit looks like and the knockoffs are nearly accurate
[0:26] the knockoffs are nearly accurate
[0:26] the knockoffs are nearly accurate compared with the the name brand then
[0:29] compared with the the name brand then
[0:29] compared with the the name brand then you have the CBA
[0:32] you have the CBA
[0:32] you have the CBA um computerized battery analyzer this is
[0:34] um computerized battery analyzer this is
[0:34] um computerized battery analyzer this is version five and we have this in the
[0:36] version five and we have this in the
[0:36] version five and we have this in the department as well that you can check
[0:38] department as well that you can check
[0:38] department as well that you can check out from your lab coordinator
[0:40] out from your lab coordinator
[0:40] out from your lab coordinator when you're starting your mechatronics
[0:42] when you're starting your mechatronics
[0:42] when you're starting your mechatronics project or Electronics project and you
[0:45] project or Electronics project and you
[0:45] project or Electronics project and you are designing usually you'll have a
[0:48] are designing usually you'll have a
[0:48] are designing usually you'll have a micro controller and you'll have some
[0:51] micro controller and you'll have some
[0:51] micro controller and you'll have some sensors or actuators that are plugged
[0:53] sensors or actuators that are plugged
[0:53] sensors or actuators that are plugged into it and each of these has a power
[0:56] into it and each of these has a power
[0:56] into it and each of these has a power consumption information on their data
[0:58] consumption information on their data
[0:58] consumption information on their data sheet but there are several good reasons
[1:00] sheet but there are several good reasons
[1:00] sheet but there are several good reasons to do a testing anyway directly
[1:04] to do a testing anyway directly
[1:04] to do a testing anyway directly um
[1:05] um
[1:05] um it's a good idea to take your sensors
[1:09] it's a good idea to take your sensors
[1:09] it's a good idea to take your sensors and plug them into the interface that
[1:12] and plug them into the interface that
[1:12] and plug them into the interface that they'll actually support them
[1:14] they'll actually support them
[1:14] they'll actually support them when you're measuring the power and
[1:16] when you're measuring the power and
[1:16] when you're measuring the power and instead of measuring them individually
[1:19] instead of measuring them individually
[1:19] instead of measuring them individually measure them in real time when you're
[1:21] measure them in real time when you're
[1:21] measure them in real time when you're calling on functions that utilize the
[1:23] calling on functions that utilize the
[1:23] calling on functions that utilize the sensors like this infrared temperature
[1:25] sensors like this infrared temperature
[1:25] sensors like this infrared temperature sensor
[1:26] sensor
[1:26] sensor then even if it's a 3.3 volt device
[1:30] then even if it's a 3.3 volt device
[1:30] then even if it's a 3.3 volt device you'll get actual power coming in at 5
[1:33] you'll get actual power coming in at 5
[1:33] you'll get actual power coming in at 5 volts that's converted on the board of
[1:35] volts that's converted on the board of
[1:35] volts that's converted on the board of the device that you're that's hosting
[1:37] the device that you're that's hosting
[1:37] the device that you're that's hosting the sensor this is more reliable because
[1:40] the sensor this is more reliable because
[1:40] the sensor this is more reliable because there's a conversion loss in converting
[1:43] there's a conversion loss in converting
[1:43] there's a conversion loss in converting from 5.5 volts down to three volts and
[1:47] from 5.5 volts down to three volts and
[1:47] from 5.5 volts down to three volts and the same thing if you're running a
[1:49] the same thing if you're running a
[1:49] the same thing if you're running a Raspberry Pi or any micro computer it's
[1:52] Raspberry Pi or any micro computer it's
[1:52] Raspberry Pi or any micro computer it's a great way to verify how much energy
[1:54] a great way to verify how much energy
[1:54] a great way to verify how much energy your sensors will use by actually just
[1:58] your sensors will use by actually just
[1:58] your sensors will use by actually just measuring a Delta
[2:00] measuring a Delta
[2:00] measuring a Delta in the power consumption of this device
[2:03] in the power consumption of this device
[2:03] in the power consumption of this device so instead of
[2:05] so instead of
[2:05] so instead of calculating the power at 3.3 volts you
[2:09] calculating the power at 3.3 volts you
[2:09] calculating the power at 3.3 volts you just say what is the the energy used
[2:13] just say what is the the energy used
[2:13] just say what is the the energy used when I'm just running my macro
[2:15] when I'm just running my macro
[2:15] when I'm just running my macro controller
[2:16] controller
[2:16] controller and then what is the energy used when I
[2:19] and then what is the energy used when I
[2:19] and then what is the energy used when I start reading from a sensor
[2:21] start reading from a sensor
[2:21] start reading from a sensor and then then you can take the
[2:22] and then then you can take the
[2:22] and then then you can take the difference
[2:26] you can check that
[2:27] you can check that on your power meter
[2:28] on your power meter
[2:28] on your power meter and you can log that as your real power
[2:31] and you can log that as your real power
[2:31] and you can log that as your real power level this model here is a little bit
[2:34] level this model here is a little bit
[2:34] level this model here is a little bit fancier and it will give you three down
[2:37] fancier and it will give you three down
[2:37] fancier and it will give you three down to the one milliamp resolution
[2:40] to the one milliamp resolution
[2:40] to the one milliamp resolution and it shows you how many watts are
[2:42] and it shows you how many watts are
[2:42] and it shows you how many watts are being pulled if you're actually using a
[2:45] being pulled if you're actually using a
[2:45] being pulled if you're actually using a power electronic over USB rather than
[2:48] power electronic over USB rather than
[2:48] power electronic over USB rather than just sensors you're going to find it
[2:50] just sensors you're going to find it
[2:50] just sensors you're going to find it pulls a lot more current
[2:54] pulls a lot more current
[2:54] pulls a lot more current in this case
[2:56] in this case
[2:56] in this case it's almost one amp so 4.5 Watts
[3:01] it's almost one amp so 4.5 Watts
[3:01] it's almost one amp so 4.5 Watts if you're using a wall adapter it's
[3:03] if you're using a wall adapter it's
[3:03] if you're using a wall adapter it's gonna probably claim 12 volts or
[3:06] gonna probably claim 12 volts or
[3:06] gonna probably claim 12 volts or something like that but you're going to
[3:08] something like that but you're going to
[3:08] something like that but you're going to get a varying voltage coming out of it
[3:10] get a varying voltage coming out of it
[3:10] get a varying voltage coming out of it and that's good to measure uh with this
[3:13] and that's good to measure uh with this
[3:13] and that's good to measure uh with this type of meter so you get your Ender
[3:16] type of meter so you get your Ender
[3:16] type of meter so you get your Ender Anderson connectors crimped on and then
[3:19] Anderson connectors crimped on and then
[3:19] Anderson connectors crimped on and then you can see with no load we're at 12.3
[3:23] you can see with no load we're at 12.3
[3:23] you can see with no load we're at 12.3 volts and when we apply a load it's
[3:26] volts and when we apply a load it's
[3:26] volts and when we apply a load it's going to drop down let's try out this 12
[3:28] going to drop down let's try out this 12
[3:28] going to drop down let's try out this 12 volt peristaltic pump
[3:30] volt peristaltic pump
[3:30] volt peristaltic pump so we're going to always
[3:33] so we're going to always
[3:33] so we're going to always um attach these alligator clips before
[3:35] um attach these alligator clips before
[3:35] um attach these alligator clips before we plug in our connector our power so
[3:39] we plug in our connector our power so
[3:39] we plug in our connector our power so that we don't have a chance of
[3:42] that we don't have a chance of
[3:42] that we don't have a chance of of the clips contacting something in
[3:44] of the clips contacting something in
[3:44] of the clips contacting something in short circuiting
[3:45] short circuiting
[3:45] short circuiting then when we plug in the load we can see
[3:48] then when we plug in the load we can see
[3:48] then when we plug in the load we can see how the voltage drops down and how much
[3:50] how the voltage drops down and how much
[3:50] how the voltage drops down and how much power is being pulled
[3:57] you can hear it now the motor is turning
[3:57] you can hear it now the motor is turning oh it only dropped down a very small
[3:59] oh it only dropped down a very small
[3:59] oh it only dropped down a very small amount 12.25
[4:02] amount 12.25
[4:02] amount 12.25 and we're pulling 4.3 Watts
[4:09] let's try again with this higher power
[4:09] let's try again with this higher power device that's going to pull I think it's
[4:11] device that's going to pull I think it's
[4:11] device that's going to pull I think it's 10 or 20 watts when we turn it on
[4:19] so this time
[4:19] so this time it's gonna be
[4:24] 12 Watts getting pulled
[4:24] 12 Watts getting pulled 12.2 watts and still the voltage held up
[4:28] 12.2 watts and still the voltage held up
[4:28] 12.2 watts and still the voltage held up above 12 volts that's pretty nice
[4:31] above 12 volts that's pretty nice
[4:31] above 12 volts that's pretty nice at one amp so a power supply rated at
[4:34] at one amp so a power supply rated at
[4:34] at one amp so a power supply rated at three amps like this one is going to do
[4:36] three amps like this one is going to do
[4:36] three amps like this one is going to do pretty good if it's a decent quality
[4:39] pretty good if it's a decent quality
[4:39] pretty good if it's a decent quality well as you can see it's important to
[4:42] well as you can see it's important to
[4:42] well as you can see it's important to test uh in your real uh connected
[4:45] test uh in your real uh connected
[4:45] test uh in your real uh connected situation because the wattage of the
[4:48] situation because the wattage of the
[4:48] situation because the wattage of the device depends on the voltage and the
[4:50] device depends on the voltage and the
[4:50] device depends on the voltage and the wattage will vary from the data sheet
[4:52] wattage will vary from the data sheet
[4:52] wattage will vary from the data sheet the power meter is going to give you
[4:56] the power meter is going to give you
[4:56] the power meter is going to give you um the host inefficiency values and
[5:02] um the host inefficiency values and
[5:02] um the host inefficiency values and the adapter that you're using or battery
[5:05] the adapter that you're using or battery
[5:05] the adapter that you're using or battery is going to deviate as you go
[5:08] is going to deviate as you go
[5:08] is going to deviate as you go depending on how much power You Pull and
[5:11] depending on how much power You Pull and
[5:11] depending on how much power You Pull and how nice of an adapter it is so the data
[5:13] how nice of an adapter it is so the data
[5:13] how nice of an adapter it is so the data sheet is not going to tell you
[5:14] sheet is not going to tell you
[5:14] sheet is not going to tell you everything and it's really nice to have
[5:16] everything and it's really nice to have
[5:16] everything and it's really nice to have real data lastly we have the
[5:19] real data lastly we have the
[5:19] real data lastly we have the computerized battery analyzer for very
[5:22] computerized battery analyzer for very
[5:22] computerized battery analyzer for very sophisticated measurements but it has a
[5:25] sophisticated measurements but it has a
[5:25] sophisticated measurements but it has a really simple software on the PC and it
[5:28] really simple software on the PC and it
[5:28] really simple software on the PC and it communicates over USB using just like a
[5:32] communicates over USB using just like a
[5:32] communicates over USB using just like a USB printer cable to your computer so
[5:36] USB printer cable to your computer so
[5:36] USB printer cable to your computer so when you plug this one in
[5:39] when you plug this one in
[5:39] when you plug this one in foreign
[5:39] foreign
[5:39] foreign it's useful for something like
[5:43] it's useful for something like
[5:43] it's useful for something like grabbing a battery that you selected for
[5:46] grabbing a battery that you selected for
[5:46] grabbing a battery that you selected for your project and then measuring how long
[5:48] your project and then measuring how long
[5:48] your project and then measuring how long will your battery last what voltage does
[5:51] will your battery last what voltage does
[5:51] will your battery last what voltage does it carry
[5:52] it carry
[5:52] it carry throughout its uh its life and
[5:56] throughout its uh its life and
[5:56] throughout its uh its life and consumption what we're starting the CBA
[5:59] consumption what we're starting the CBA
[5:59] consumption what we're starting the CBA battery software can discharge a battery
[6:03] battery software can discharge a battery
[6:03] battery software can discharge a battery and measure the current and the amperage
[6:05] and measure the current and the amperage
[6:06] and measure the current and the amperage in the wattage as we go so we can click
[6:08] in the wattage as we go so we can click
[6:08] in the wattage as we go so we can click new test this is a free software
[6:11] new test this is a free software
[6:11] new test this is a free software everything in the blue box is only for
[6:14] everything in the blue box is only for
[6:14] everything in the blue box is only for your recorded information it's not
[6:16] your recorded information it's not
[6:16] your recorded information it's not critical to set up the test this is the
[6:18] critical to set up the test this is the
[6:18] critical to set up the test this is the whole test setup right here we're going
[6:21] whole test setup right here we're going
[6:21] whole test setup right here we're going to set the cutoff voltage to be 17 volts
[6:23] to set the cutoff voltage to be 17 volts
[6:23] to set the cutoff voltage to be 17 volts if you click detect battery it's going
[6:25] if you click detect battery it's going
[6:25] if you click detect battery it's going to give you the voltage detected at the
[6:28] to give you the voltage detected at the
[6:28] to give you the voltage detected at the terminals without any load and then we
[6:31] terminals without any load and then we
[6:31] terminals without any load and then we can set how many amps we want to pull
[6:34] can set how many amps we want to pull
[6:34] can set how many amps we want to pull from the battery for our test and so
[6:36] from the battery for our test and so
[6:36] from the battery for our test and so we'll put that at four for this large
[6:38] we'll put that at four for this large
[6:38] we'll put that at four for this large battery then when we click Start then
[6:42] battery then when we click Start then
[6:42] battery then when we click Start then that's okay then it's going to
[6:45] that's okay then it's going to
[6:45] that's okay then it's going to immediately drop down from a no load
[6:47] immediately drop down from a no load
[6:48] immediately drop down from a no load voltage to a 4 amp load voltage and then
[6:52] voltage to a 4 amp load voltage and then
[6:52] voltage to a 4 amp load voltage and then this Red Line will slowly sweep down
[6:54] this Red Line will slowly sweep down
[6:54] this Red Line will slowly sweep down until it reaches the cutoff voltage
[6:56] until it reaches the cutoff voltage
[6:56] until it reaches the cutoff voltage where the test is automated and it will
[6:58] where the test is automated and it will
[6:58] where the test is automated and it will stop automatically and give you a total
[7:01] stop automatically and give you a total
[7:01] stop automatically and give you a total amp hours and Watt hours
[7:04] amp hours and Watt hours
[7:04] amp hours and Watt hours another great function of this machine
[7:06] another great function of this machine
[7:06] another great function of this machine is you can perform a charge monitor
[7:10] is you can perform a charge monitor
[7:10] is you can perform a charge monitor where you simply measure the the charge
[7:14] where you simply measure the the charge
[7:14] where you simply measure the the charge the voltage at the terminals while you
[7:18] the voltage at the terminals while you
[7:18] the voltage at the terminals while you either charge or discharge or manipulate
[7:21] either charge or discharge or manipulate
[7:21] either charge or discharge or manipulate your battery or your system overall and
[7:24] your battery or your system overall and
[7:24] your battery or your system overall and see how the the value adjusts over time
[7:30] see how the the value adjusts over time
[7:30] see how the the value adjusts over time the charge monitor test measures voltage
[7:33] the charge monitor test measures voltage
[7:33] the charge monitor test measures voltage but it does not measure the current that
[7:35] but it does not measure the current that
[7:36] but it does not measure the current that you're consuming so you just hook up
[7:38] you're consuming so you just hook up
[7:38] you're consuming so you just hook up your battery and then you can put
[7:40] your battery and then you can put
[7:40] your battery and then you can put something else in series sorry in
[7:42] something else in series sorry in
[7:42] something else in series sorry in parallel then in this case I want to I
[7:45] parallel then in this case I want to I
[7:45] parallel then in this case I want to I want to look after the voltages the
[7:47] want to look after the voltages the
[7:47] want to look after the voltages the current as well so then I'm going to
[7:48] current as well so then I'm going to
[7:48] current as well so then I'm going to hook up my Appliance to
[7:53] hook up my Appliance to
[7:53] hook up my Appliance to the power Works meter
[7:55] the power Works meter
[7:55] the power Works meter okay now I can see that I'm pulling 11.3
[7:59] okay now I can see that I'm pulling 11.3
[7:59] okay now I can see that I'm pulling 11.3 watts and then I can collect data on
[8:01] watts and then I can collect data on
[8:01] watts and then I can collect data on here and watch as this battery voltage
[8:05] here and watch as this battery voltage
[8:05] here and watch as this battery voltage Powers down to see how long will my
[8:07] Powers down to see how long will my
[8:07] Powers down to see how long will my system last
[8:09] system last
[8:09] system last this is a charge monitor test in real
[8:11] this is a charge monitor test in real
[8:11] this is a charge monitor test in real time
[8:12] time
[8:12] time these are the data points collected with
[8:14] these are the data points collected with
[8:14] these are the data points collected with no load on the battery and you can click
[8:16] no load on the battery and you can click
[8:16] no load on the battery and you can click to see the actual values
[8:18] to see the actual values
[8:18] to see the actual values and the data indicates a lower voltage
[8:21] and the data indicates a lower voltage
[8:21] and the data indicates a lower voltage when we have connected the load
[8:23] when we have connected the load
[8:23] when we have connected the load so to wrap it up there are three kinds
[8:26] so to wrap it up there are three kinds
[8:26] so to wrap it up there are three kinds of Power meters that can pretty much
[8:27] of Power meters that can pretty much
[8:27] of Power meters that can pretty much solve all your issues is if you want to
[8:30] solve all your issues is if you want to
[8:30] solve all your issues is if you want to measure power and energy over time and
[8:33] measure power and energy over time and
[8:33] measure power and energy over time and actually have a log that's accurate you
[8:35] actually have a log that's accurate you
[8:35] actually have a log that's accurate you can use the CBA if you need to check the
[8:38] can use the CBA if you need to check the
[8:38] can use the CBA if you need to check the power consumption or power delivery of a
[8:41] power consumption or power delivery of a
[8:41] power consumption or power delivery of a fairly High wattage device between one
[8:44] fairly High wattage device between one
[8:44] fairly High wattage device between one Watt and 150 watts or more you can use
[8:48] Watt and 150 watts or more you can use
[8:48] Watt and 150 watts or more you can use the Anderson device and the USB power
[8:51] the Anderson device and the USB power
[8:51] the Anderson device and the USB power meters are great for all kinds of things
[8:53] meters are great for all kinds of things
[8:53] meters are great for all kinds of things even if you need to make your own setup
[8:56] even if you need to make your own setup
[8:56] even if you need to make your own setup where you simply provide 5 volts to your
[8:59] where you simply provide 5 volts to your
[8:59] where you simply provide 5 volts to your device you can create your own setup
[9:02] device you can create your own setup
[9:02] device you can create your own setup however you need to suit your
[9:04] however you need to suit your
[9:04] however you need to suit your application
[9:05] application
[9:05] application and don't forget that by crimping the
[9:09] and don't forget that by crimping the
[9:09] and don't forget that by crimping the compatible terminals on your electronics
[9:12] compatible terminals on your electronics
[9:12] compatible terminals on your electronics you might save a lot of hairballs of
[9:15] you might save a lot of hairballs of
[9:15] you might save a lot of hairballs of wires on your desk as you connect many
[9:18] wires on your desk as you connect many
[9:18] wires on your desk as you connect many other things in your project
[9:19] other things in your project
[9:19] other things in your project you can easily find off-the-shelf
[9:21] you can easily find off-the-shelf
[9:21] you can easily find off-the-shelf components like this breakout board so
[9:24] components like this breakout board so
[9:24] components like this breakout board so you can provide your power over USB
[9:26] you can provide your power over USB
[9:26] you can provide your power over USB directly and you can take your
[9:29] directly and you can take your
[9:29] directly and you can take your measurements on something that might not
[9:31] measurements on something that might not
[9:31] measurements on something that might not have the USB connector and you can find
[9:34] have the USB connector and you can find
[9:34] have the USB connector and you can find loads of other off-the-shelf parts to
[9:36] loads of other off-the-shelf parts to
[9:36] loads of other off-the-shelf parts to make your adaptations easy simple and
[9:40] make your adaptations easy simple and
[9:40] make your adaptations easy simple and reliable so that that reduces how many
[9:42] reliable so that that reduces how many
[9:42] reliable so that that reduces how many custom
[9:43] custom
[9:44] custom wirings you need to do throughout your
[9:46] wirings you need to do throughout your
[9:46] wirings you need to do throughout your project and reduce the the amount of
[9:48] project and reduce the the amount of
[9:48] project and reduce the the amount of mess on your desk as you work with many
[9:51] mess on your desk as you work with many
[9:51] mess on your desk as you work with many components at the same time

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
