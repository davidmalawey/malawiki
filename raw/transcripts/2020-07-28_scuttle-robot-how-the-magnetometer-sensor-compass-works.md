---
title: "SCUTTLE Robot - How the Magnetometer Sensor (compass) works"
url: "https://www.youtube.com/watch?v=o6_OJ3TO8rM"
video_id: "o6_OJ3TO8rM"
channel: "David Malawey"
channel_id: "UCwirLDXiN1ybgPyIDNt85PA"
channel_url: "https://www.youtube.com/channel/UCwirLDXiN1ybgPyIDNt85PA"
published: 2020-07-28
duration: "7:56"
duration_sec: 476
views: 2815
likes: 65
category: "Education"
keywords: []
thumbnail_url: "https://i.ytimg.com/vi/o6_OJ3TO8rM/maxresdefault.jpg"
is_live: false
was_live: false
is_upcoming: false
source: "yt-dlp via fetch-transcripts.py"
acquired: 2026-05-02
transcript_segments: 388
chapters_count: 5
has_description: true
has_comments: false
---

## Description

Explanation of the theory behind the magnetometer sensor, and how it must be calibrated.

SCUTTLE Project Info: https://www.SCUTTLErobot.org

Most magnetometer sensors work the same (including "IMU"s which are just magnetometers coupled to accelerometers and gyros).  This example is MPU9250 on the Beaglebone Blue.

## Chapters

- 0:00 <Untitled Chapter 1>
- 1:27 Calibration
- 2:15 How Does the Magnetometer Behave
- 4:55 Determining the Absolute Orientation
- 7:26 Choosing the Quadrant

## Transcript

[0:03] let's quickly look at
[0:03] let's quickly look at what the compass does and how we
[0:05] what the compass does and how we
[0:05] what the compass does and how we calibrate it
[0:06] calibrate it
[0:06] calibrate it so scuttle has a compass for the
[0:08] so scuttle has a compass for the
[0:08] so scuttle has a compass for the orientation
[0:09] orientation
[0:10] orientation of the robot the compass is nothing but
[0:12] of the robot the compass is nothing but
[0:12] of the robot the compass is nothing but a three
[0:13] a three
[0:13] a three axis magnetometer that means it's really
[0:15] axis magnetometer that means it's really
[0:16] axis magnetometer that means it's really three
[0:16] three
[0:16] three sensors encoders can provide the
[0:19] sensors encoders can provide the
[0:19] sensors encoders can provide the relative orientation
[0:21] relative orientation
[0:21] relative orientation such as how far do i move when i move
[0:24] such as how far do i move when i move
[0:24] such as how far do i move when i move one wheel
[0:25] one wheel
[0:25] one wheel but the compass is required to get the
[0:27] but the compass is required to get the
[0:27] but the compass is required to get the global orientation
[0:28] global orientation
[0:28] global orientation so if i drive in many circles
[0:31] so if i drive in many circles
[0:31] so if i drive in many circles then i want to know where am i relative
[0:35] then i want to know where am i relative
[0:35] then i want to know where am i relative to the building or to
[0:36] to the building or to
[0:36] to the building or to north um on the map
[0:40] north um on the map
[0:40] north um on the map the compass is embedded in the imu
[0:42] the compass is embedded in the imu
[0:42] the compass is embedded in the imu that's a nine-axis
[0:45] that's a nine-axis
[0:45] that's a nine-axis sensor and many sensors for embedded
[0:48] sensor and many sensors for embedded
[0:48] sensor and many sensors for embedded devices
[0:49] devices
[0:49] devices are like this where inside their sensor
[0:52] are like this where inside their sensor
[0:52] are like this where inside their sensor they have
[0:53] they have
[0:53] they have a magnetometer sensor and inside the
[0:55] a magnetometer sensor and inside the
[0:56] a magnetometer sensor and inside the magnetometer of course there's
[0:57] magnetometer of course there's
[0:57] magnetometer of course there's three parts they're oriented in the
[1:00] three parts they're oriented in the
[1:00] three parts they're oriented in the indicated directions
[1:02] indicated directions
[1:02] indicated directions on the beaglebone the direction is
[1:04] on the beaglebone the direction is
[1:04] on the beaglebone the direction is indicated with this
[1:05] indicated with this
[1:05] indicated with this silk screen x and y and z
[1:08] silk screen x and y and z
[1:08] silk screen x and y and z has this little circle pointed up that's
[1:11] has this little circle pointed up that's
[1:11] has this little circle pointed up that's an arrow pointed
[1:12] an arrow pointed
[1:12] an arrow pointed at you we don't really look at the z
[1:15] at you we don't really look at the z
[1:15] at you we don't really look at the z for this lesson this is the file
[1:19] for this lesson this is the file
[1:19] for this lesson this is the file that we run in order to access and test
[1:22] that we run in order to access and test
[1:22] that we run in order to access and test the magnetometer mpu.pi and
[1:26] the magnetometer mpu.pi and
[1:26] the magnetometer mpu.pi and each magnetometer requires calibration
[1:29] each magnetometer requires calibration
[1:29] each magnetometer requires calibration all three axes and all
[1:32] all three axes and all
[1:32] all three axes and all robots need to have their own individual
[1:34] robots need to have their own individual
[1:34] robots need to have their own individual calibration
[1:40] theta is defined this is just a reminder
[1:40] theta is defined this is just a reminder as
[1:41] as
[1:41] as scuttle's x vector minus the global
[1:44] scuttle's x vector minus the global
[1:44] scuttle's x vector minus the global x vector so global is our purple
[1:47] x vector so global is our purple
[1:47] x vector so global is our purple set here scuttle's x vector is where
[1:51] set here scuttle's x vector is where
[1:51] set here scuttle's x vector is where he's pointed
[1:51] he's pointed
[1:51] he's pointed forward and theta sub c we're going to
[1:55] forward and theta sub c we're going to
[1:55] forward and theta sub c we're going to call
[1:55] call
[1:55] call the compass theta or the theta indicated
[1:59] the compass theta or the theta indicated
[1:59] the compass theta or the theta indicated by the compass
[2:00] by the compass
[2:00] by the compass is my forward heading
[2:04] is my forward heading
[2:04] is my forward heading minus the the x since this is
[2:07] minus the the x since this is
[2:08] minus the the x since this is positive because this is greater than
[2:10] positive because this is greater than
[2:10] positive because this is greater than this one
[2:11] this one
[2:12] this one using the right hand rule next
[2:16] using the right hand rule next
[2:16] using the right hand rule next how does the magnetometer behave an axis
[2:19] how does the magnetometer behave an axis
[2:19] how does the magnetometer behave an axis of the magnetometer is
[2:21] of the magnetometer is
[2:21] of the magnetometer is at a maximum when it's aligned with the
[2:23] at a maximum when it's aligned with the
[2:23] at a maximum when it's aligned with the north
[2:24] north
[2:24] north vector of uh the actual
[2:27] vector of uh the actual
[2:28] vector of uh the actual earth's polar north vector
[2:31] earth's polar north vector
[2:31] earth's polar north vector so magnetic north so we're going to use
[2:36] so magnetic north so we're going to use
[2:36] so magnetic north so we're going to use this blue table as our reference our
[2:39] this blue table as our reference our
[2:39] this blue table as our reference our visual reference this is the values
[2:41] visual reference this is the values
[2:41] visual reference this is the values desired by
[2:42] desired by
[2:42] desired by a direction using the x-axis only we're
[2:46] a direction using the x-axis only we're
[2:46] a direction using the x-axis only we're not looking at y
[2:47] not looking at y
[2:47] not looking at y or z the purple pink arrow here
[2:51] or z the purple pink arrow here
[2:51] or z the purple pink arrow here is showing our x and we're saying that
[2:54] is showing our x and we're saying that
[2:54] is showing our x and we're saying that the compass x
[2:55] the compass x
[2:55] the compass x should return zero in this condition
[2:58] should return zero in this condition
[2:58] should return zero in this condition this is the condition where
[2:59] this is the condition where
[2:59] this is the condition where north is this direction on the page
[3:02] north is this direction on the page
[3:02] north is this direction on the page and x is pointed east then that
[3:05] and x is pointed east then that
[3:05] and x is pointed east then that magnetometer
[3:06] magnetometer
[3:06] magnetometer value should be zero
[3:09] value should be zero
[3:09] value should be zero and then it's um its maximum when
[3:12] and then it's um its maximum when
[3:12] and then it's um its maximum when aligned with north
[3:13] aligned with north
[3:13] aligned with north minimum when opposing it so that means
[3:15] minimum when opposing it so that means
[3:16] minimum when opposing it so that means i'm aligned with north here i should get
[3:17] i'm aligned with north here i should get
[3:17] i'm aligned with north here i should get a one
[3:18] a one
[3:18] a one i'm opposing north here i should get a
[3:21] i'm opposing north here i should get a
[3:21] i'm opposing north here i should get a minus one because i'm pointed
[3:23] minus one because i'm pointed
[3:23] minus one because i'm pointed south um but we would never actually
[3:26] south um but we would never actually
[3:26] south um but we would never actually know if we're east or west
[3:27] know if we're east or west
[3:28] know if we're east or west because we're gonna get a zero for
[3:29] because we're gonna get a zero for
[3:29] because we're gonna get a zero for either one of those conditions that's
[3:31] either one of those conditions that's
[3:31] either one of those conditions that's why we need multiple axes
[3:34] why we need multiple axes
[3:34] why we need multiple axes after calibration we can achieve the
[3:35] after calibration we can achieve the
[3:35] after calibration we can achieve the behavior below that means
[3:37] behavior below that means
[3:37] behavior below that means we don't actually get these numbers
[3:39] we don't actually get these numbers
[3:39] we don't actually get these numbers right out of the
[3:40] right out of the
[3:40] right out of the package we have to calibrate it
[3:43] package we have to calibrate it
[3:43] package we have to calibrate it discover the maximum and minimum values
[3:45] discover the maximum and minimum values
[3:46] discover the maximum and minimum values by rotating the sensor in a full
[3:47] by rotating the sensor in a full
[3:47] by rotating the sensor in a full circle this is this the first step to
[3:51] circle this is this the first step to
[3:51] circle this is this the first step to your calibration
[3:52] your calibration
[3:52] your calibration it's best if your beaglebone is
[3:55] it's best if your beaglebone is
[3:55] it's best if your beaglebone is on the robot because you have some steel
[3:58] on the robot because you have some steel
[3:58] on the robot because you have some steel anything
[3:58] anything
[3:58] anything ferrous as well as permanent magnets may
[4:01] ferrous as well as permanent magnets may
[4:01] ferrous as well as permanent magnets may influence
[4:03] influence
[4:03] influence the value so we want to just
[4:06] the value so we want to just
[4:06] the value so we want to just uh do the calibration in the condition
[4:09] uh do the calibration in the condition
[4:09] uh do the calibration in the condition you'll finally have
[4:10] you'll finally have
[4:10] you'll finally have when you're driving step two
[4:14] when you're driving step two
[4:14] when you're driving step two is going to be the rescaling and the
[4:17] is going to be the rescaling and the
[4:17] is going to be the rescaling and the centering
[4:18] centering
[4:18] centering we're gonna we're gonna re uh adjust
[4:20] we're gonna we're gonna re uh adjust
[4:20] we're gonna we're gonna re uh adjust this range to go instead of a range of
[4:23] this range to go instead of a range of
[4:23] this range to go instead of a range of 42 we're going to squish it down to just
[4:26] 42 we're going to squish it down to just
[4:26] 42 we're going to squish it down to just be
[4:27] be
[4:27] be a range of two and then we're going to
[4:29] a range of two and then we're going to
[4:29] a range of two and then we're going to subtract one
[4:30] subtract one
[4:30] subtract one so that the the neutral value or this
[4:33] so that the the neutral value or this
[4:33] so that the the neutral value or this the average value
[4:34] the average value
[4:34] the average value is zero and then after calibration you
[4:37] is zero and then after calibration you
[4:37] is zero and then after calibration you should see values like
[4:39] should see values like
[4:39] should see values like this you might deviate by
[4:42] this you might deviate by
[4:42] this you might deviate by less than 10 percent maybe 1.03 or
[4:45] less than 10 percent maybe 1.03 or
[4:45] less than 10 percent maybe 1.03 or something
[4:46] something
[4:46] something and minus 1.03 but you
[4:49] and minus 1.03 but you
[4:49] and minus 1.03 but you your calibration should get you close to
[4:51] your calibration should get you close to
[4:51] your calibration should get you close to these values
[4:52] these values
[4:52] these values as the maximum and the minimum
[4:56] as the maximum and the minimum
[4:56] as the maximum and the minimum determining the absolute orientation
[4:59] determining the absolute orientation
[4:59] determining the absolute orientation the x and y axes are sufficient
[5:01] the x and y axes are sufficient
[5:01] the x and y axes are sufficient information to give the heading
[5:03] information to give the heading
[5:03] information to give the heading the z-axis is not so important as long
[5:06] the z-axis is not so important as long
[5:06] the z-axis is not so important as long as
[5:07] as
[5:07] as scuttle is laying flat on a fairly flat
[5:10] scuttle is laying flat on a fairly flat
[5:10] scuttle is laying flat on a fairly flat surface
[5:11] surface
[5:11] surface theta is defined as the rotation of
[5:13] theta is defined as the rotation of
[5:13] theta is defined as the rotation of scuttle from the global coordinate
[5:15] scuttle from the global coordinate
[5:15] scuttle from the global coordinate frame that means if my y
[5:18] frame that means if my y
[5:18] frame that means if my y is further to the left than the global y
[5:23] is further to the left than the global y
[5:23] is further to the left than the global y then i have a positive turn which means
[5:25] then i have a positive turn which means
[5:25] then i have a positive turn which means it's a left turn and if you drew the x
[5:28] it's a left turn and if you drew the x
[5:28] it's a left turn and if you drew the x axis it would be right here x minus x
[5:31] axis it would be right here x minus x
[5:31] axis it would be right here x minus x prime would be the same angle
[5:34] prime would be the same angle
[5:34] prime would be the same angle positive theta means scuttle is turned
[5:36] positive theta means scuttle is turned
[5:36] positive theta means scuttle is turned left from north
[5:38] left from north
[5:38] left from north we can define north as the y-axis of the
[5:41] we can define north as the y-axis of the
[5:41] we can define north as the y-axis of the global coordinate frame
[5:43] global coordinate frame
[5:43] global coordinate frame you can actually define that coordinate
[5:46] you can actually define that coordinate
[5:46] you can actually define that coordinate frame
[5:47] frame
[5:47] frame wherever you want for example you it
[5:49] wherever you want for example you it
[5:49] wherever you want for example you it could be
[5:50] could be
[5:50] could be however you started the robot when you
[5:53] however you started the robot when you
[5:53] however you started the robot when you turned on
[5:54] turned on
[5:54] turned on the microprocessor or you can define
[5:57] the microprocessor or you can define
[5:57] the microprocessor or you can define this as
[6:03] north earth's north vector
[6:03] north earth's north vector so this is an example to show um
[6:06] so this is an example to show um
[6:06] so this is an example to show um x and y magnetometer versus robot
[6:08] x and y magnetometer versus robot
[6:08] x and y magnetometer versus robot heading after
[6:09] heading after
[6:09] heading after scaling the maximum is one then the
[6:12] scaling the maximum is one then the
[6:12] scaling the maximum is one then the minimum
[6:13] minimum
[6:13] minimum is negative one and um
[6:17] is negative one and um
[6:17] is negative one and um each pair of coordinates or values
[6:20] each pair of coordinates or values
[6:20] each pair of coordinates or values returned by the
[6:21] returned by the
[6:21] returned by the axes of the magnetometer is unique
[6:25] axes of the magnetometer is unique
[6:25] axes of the magnetometer is unique now each value isn't unique see this
[6:27] now each value isn't unique see this
[6:27] now each value isn't unique see this value reoccurs
[6:28] value reoccurs
[6:28] value reoccurs it's uh slightly less than zero and
[6:31] it's uh slightly less than zero and
[6:31] it's uh slightly less than zero and slightly less than zero here
[6:33] slightly less than zero here
[6:33] slightly less than zero here each value independently is not unique
[6:35] each value independently is not unique
[6:35] each value independently is not unique but each pair is
[6:36] but each pair is
[6:36] but each pair is and so this pink oval is selecting an
[6:40] and so this pink oval is selecting an
[6:40] and so this pink oval is selecting an example pair and it's saying that
[6:44] example pair and it's saying that
[6:44] example pair and it's saying that 0.91 and 0.42 what do we have
[6:47] 0.91 and 0.42 what do we have
[6:47] 0.91 and 0.42 what do we have the y prime value is the
[6:50] the y prime value is the
[6:50] the y prime value is the the vector of the magnetic north and
[6:53] the vector of the magnetic north and
[6:54] the vector of the magnetic north and x vector is weakly pointed towards it
[6:57] x vector is weakly pointed towards it
[6:57] x vector is weakly pointed towards it so it's 0.42 as a reading
[7:01] so it's 0.42 as a reading
[7:01] so it's 0.42 as a reading and the y vector is strongly pointed
[7:04] and the y vector is strongly pointed
[7:04] and the y vector is strongly pointed towards it but not
[7:05] towards it but not
[7:05] towards it but not quite aligned so it's 0.91
[7:10] quite aligned so it's 0.91
[7:10] quite aligned so it's 0.91 neither of them are opposing it so
[7:11] neither of them are opposing it so
[7:11] neither of them are opposing it so they're both positive values
[7:14] they're both positive values
[7:14] they're both positive values and the returned value from arctan 2
[7:18] and the returned value from arctan 2
[7:18] and the returned value from arctan 2 is 25 degrees the definition of arctan 2
[7:22] is 25 degrees the definition of arctan 2
[7:22] is 25 degrees the definition of arctan 2 is just like arctan but it's
[7:25] is just like arctan but it's
[7:25] is just like arctan but it's element-wise arc tangent
[7:27] element-wise arc tangent
[7:27] element-wise arc tangent choosing the quadrant correctly this is
[7:29] choosing the quadrant correctly this is
[7:29] choosing the quadrant correctly this is copied and pasted from
[7:31] copied and pasted from
[7:31] copied and pasted from the library and it's a wonderful
[7:35] the library and it's a wonderful
[7:35] the library and it's a wonderful function
[7:35] function
[7:35] function because otherwise you would have
[7:39] because otherwise you would have
[7:39] because otherwise you would have only half of the span
[7:42] only half of the span
[7:42] only half of the span available you wouldn't know if you were
[7:44] available you wouldn't know if you were
[7:44] available you wouldn't know if you were pointed east or west
[7:47] pointed east or west
[7:47] pointed east or west theta is positive when scuttle points
[7:49] theta is positive when scuttle points
[7:49] theta is positive when scuttle points west theta is negative when
[7:51] west theta is negative when
[7:51] west theta is negative when scuttle points east

## Comments

<!-- reserved for yt-comments-fetch skill; intentionally empty. -->
