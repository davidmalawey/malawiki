---
title: "More about USB than you ever wanted to know"
url: "https://www.youtube.com/watch?v=9c9-YUSbgYs"
video_id: "9c9-YUSbgYs"
published: 2024-07-25
duration: "57:46"
channel: "David Malawey"
views: 281880
likes: 6239
source: "Claude Chrome extension"
acquired: 2026-04-23
---

# Chapters

- 0:00 intro
- 0:30 anatomy
- 5:30 communication, shielding
- 8:49 power adapter
- 13:25 comparing adapters
- 19:10 voltage vs current
- 23:42 identify terminals
- 25:50 USB bus
- 29:30 sharing power
- 31:50 computer PSU
- 33:16 arduino projects
- 36:52 custom battery power
- 41:00 big battery
- 44:36 3v battery
- 47:43 measure AC power
- 51:10 quick charge
- 53:48 wireless charger

# Transcript

[0:00] this is an educational video about usb and I chopped up the video and
[0:06] edited it too many times and I hope there's not too many mistakes I hope you
[0:12] learned something and enjoy the content here we have a cable that we
[0:17] know is good quality micro USB and we know it because
[0:23] it came with this kit for a Texas Instruments um evaluation board it's
[0:29] it's it's called Uh Launchpad and this series is very similar to those uino
[0:35] boards but they're putting their name behind it and they want you to be
[0:40] successful so let's see what's inside of the
[0:46] cable by the way these dog nail clippers work
[0:51] fantastic for getting Clean Cuts to try to
[0:58] preserve the interior of this cable I'll try to just score it a little bit by
[1:03] twist and crimp and then I'll bend it to peel away the sheathing which is the
[1:10] plastic vinyl outer layer no looks like I still took the shielding along with it wow
[1:18] this one has every ingredient here is the foil shielding to
[1:25] reduce interference and it should wrap the exterior of all the
[1:31] wires then we have the cotton for strength and preventing the
[1:38] stretching and then we have this copper probably tin clad
[1:45] copper to carry the ground which connects this housing and the other ends
[1:53] housing then you have the gold plated terminals inside of here compared with
[1:59] the cheaper cable where you have uh silver color I believe that's nickel or
[2:05] tin coated terminals much nicer and then they even invested the
[2:13] care to give the power wires a larger diameter than the signal wires green and
[2:21] white are for communication black and red are for power to carry the 5
[2:28] volts you can actually read on here that they've labeled it 28 gauge and 22 gauge
[2:38] so the red and black are for powering this device and intended to carry more
[2:45] current whereas these are treated as kind of next to zero current just for
[2:52] signals now I've said that the purpose of
[2:57] this bare wire is to connect connect the two housings and give you grounding not
[3:04] to tie into the ground of the power supply and you can just as easily find
[3:11] some cable where those two housings don't have
[3:18] continuity in this case you're totally missing
[3:24] that let's chop it open and take a look
[3:34] oh boy charging
[3:45] only so here we have no shielding no communication
[3:52] wires and no ground wire for the housings
[3:58] themselves and and a very small wires for the power the current
[4:08] carrying so this is maybe 28 gauge it
[4:13] will work but easily can deceive you to think that
[4:19] you would be able to communicate before you go chopping all of your cables open
[4:25] you can sometimes read how many conductors are in inside of the wire on the printed label or you
[4:33] could perhaps find the part number and look that up online this one I I cannot
[4:40] detect what it should have on the inside from the label one of these super flimsy cheap
[4:48] looking wires that may come with um just a simple flashlight or something where
[4:55] this still does its job but it's only for charging you have ground and power
[5:01] only and that has uh loads of impacts we'll get into that shortly hopefully
[5:07] you're beginning to see why Apple would demand push strongly to have its own
[5:14] branded connector because then you don't have a million wires out on the market
[5:20] where the customers are attempting to use it they can't tell the difference and Apple has no control of the quality
[5:28] of everyone else's cable and they that that gives me the feeling of what we had
[5:33] at Toyota which is if the customer has a problem then we have a problem as we
[5:40] have to engineer our product so that it serves the customer even if the customer
[5:45] tries to do something ordinary and stupid you will notice if you buy an
[5:51] appliance like a printer they Supply a USB cable and there's a reason for that
[5:58] um one of them is you can often see they've done a heavy job of shielding and they've even added
[6:05] this uh magnetic oh I'm forgetting what you call it but it suppress it helps
[6:11] suppress the noise and so when you're traveling specifically data sending data
[6:18] that is universal serial bus it was initially designed to communicate
[6:23] serially so if your printer is 10 ft away then that's 10 ft of antenna that
[6:29] the wire behaves as an antenna to pick up interference and they're doing their
[6:34] best to suppress that so um often this will be uh the type of cable you get
[6:42] when you're dealing with type B with this house
[6:47] shaped this cable also features a ferite core which kills high high frequency
[6:55] noise so block the noise with the shield Kill The Noise with the ferite core and
[7:02] some ferite cores are made of
[7:07] rubber no I'm just kidding but I did just slice this open to make this video
[7:13] and there's literally nothing but rubber inside of this Cable's ferite core which
[7:19] is absolute crazy that means it's not a ferite core the way that you can tell is
[7:27] fite or any conductive steel is going to
[7:32] be magnetic so you can check if somebody's trying to rip you off and
[7:37] giving a cheap cable now with the world of uh many many
[7:43] electronic appliances getting hooked up via USB micro USB or
[7:50] USBC um we have a bifurcation of some devices that are using it for powering
[7:57] and charging charging up a rechargeable battery inside the appliance there's
[8:02] your USB symbol um here's a charging Point
[8:08] charging port on this flashlight and devices that are communicating that definitely require
[8:15] the four wires to do anything so we this is an Arduino we plug it in and then
[8:21] we're going to do powering of this entire device from the computer let's say if we're plugging it in um with our
[8:30] micro USB it's getting it's receiving that 5 volts to power the entire
[8:36] microcontroller and then it's communicating from the computer to the
[8:41] MCU and back with um those two green and white signal wires USB devices are not
[8:49] all made equally so these basic ones with the standard USB uh output are
[8:56] intended to have 5 volts but you will get a varying output 5.15
[9:05] is healthy but sometimes they'll be below five at the very beginning and
[9:12] that's usually the cheap ones um that does not tell you the whole story of how
[9:18] much power they're prepared to provide or how um well conditioned your power is
[9:24] so as we said USB has the S standing for seral and in in your electronic devices
[9:31] such as sensors you might connect to a computer or to a microcontroller that is
[9:37] connected to a computer you have again these two um two wires connecting for
[9:46] data transmission SC is for clock da is for data voltage in and ground anytime
[9:54] that you find a wire um bringing you to a position of only two terminals such as
[10:00] this magnetic swiveling wire for charging then you know that this cable
[10:07] is only intended for charging if you had a phone with micro USB and you wanted to
[10:13] send the pictures to your computer you will not be able to as long as you see only two contacts that means you have
[10:21] power and ground and that means there is not going to be sending of data or
[10:27] photos Over The Wire if you wind up with a device like this
[10:34] microphone we would call that a so calleded sensor and it has a USB cable
[10:41] that does not mean that you need the USB um for wires to communicate uh there's
[10:47] two protocols going on this this port USBC is only for charging the device and
[10:54] the microcontroller on board says power's coming in so I'll receive that power at 5 volts and I'll charge up the
[11:02] small battery that's embedded in here and then the communication of the audio
[11:09] happens on a totally different Channel synchronous communication using Bluetooth between the device wirelessly
[11:17] and the phone so those those are two different activities the charging and the communication on a device like this
[11:24] however in this particular microphone setup we do have Comm communication
[11:29] going to the phone over uh the the pins that you'd expect you can ignore how
[11:36] many there are now for for now uh consider the two wires that are involved
[11:41] in the same USB micro USB cable and um
[11:47] the the chip inside of here is doing the job of coordinating two Bluetooth
[11:53] connections simultaneously can be communicating wirelessly to this device
[12:00] uh it merges or performs a mux of that data and then transmits in real time
[12:06] back and forth to the phone over this cable only there's no cable involved
[12:11] since we can plug directly in this is the the apple lightning connector in the
[12:18] case of your Android the USBC will be doing the exact same thing and there
[12:24] will be very little difference on the internals of the device so with all that
[12:29] that said now you can be certain that when you have um simple charging blocks
[12:37] they're converting AC power at 120 volts to a 5V DC power and only two of those
[12:48] four terminals inside are being utilized there's not a communication happening in
[12:54] the traditional USB port Over The Wire
[12:59] like this wire to charge up a device you're only using the two and you don't need to have
[13:06] the the fancy shielded cable the shielding is for communication and what the difference in
[13:13] in quality on your wires going to be what's the gauge what is the the size of
[13:19] the copper carrying my power difference in quality on these
[13:24] will be ordinarily designated with how many amps they can delete deliver so uh
[13:31] the nice good quality when back when we were worrying about whether we had the
[13:37] Apple brand or the name brand um charging block it was all about this uh
[13:43] how many watts does it oh boy so here you can see output 5 volts 1500 milliamps or 1.5
[13:54] amps this one if it's true to its designation provides
[13:59] 1.5 times the the output before you drop below it will fade away from 5 Vols down
[14:07] down lower if you draw more H compared with this one came with the Dremel tool
[14:12] for charging it says I deliver boy there's a lot of text on this
[14:18] one I can deliver one amp um it is
[14:24] common that your devices let's say this flashlight I want to charge up this flashl flashlight okay and it has a USB
[14:32] uh connector to charge its battery even if it came with a cheap 1 aamp
[14:38] charger um you can go up from there you will not harm any device just because
[14:45] the rating says it can deliver more uh higher amperage but and in some cases the
[14:52] engineering is such that this could accept much more than 1 amp but it only came with the 1 amp charger so yeah use
[14:59] your best quality block to charge at the fastest rate um this is all before we
[15:06] dive into PD that's power delivery and QC those two protocols for charging that
[15:13] come along with the new um USBC situation the first thing that you can
[15:19] do to help yourself when you're getting into to charging is to make sure let's
[15:26] say you have a car adapter like this one we're coming from 12 volts input uh definitely the the power will not be
[15:33] limited by the car at 12 volts we can provide plenty of amps from the source
[15:39] side and then what can we pull from these it says 4.8 amps total output and
[15:46] 2.4 amps Max for each so no you cannot
[15:52] draw uh we'll just call that 5x5 25 watts you cannot draw 25 watts from one
[15:57] port you can draw 12 12 Watts from each and that's if your device is ready to
[16:05] accept that much without PD and without QC so even if your phone has um QC
[16:14] that's uh I'm forgetting right now it's a protocol to ask for a higher power
[16:20] level it usually comes with a higher voltage this one is flat out 5 volts
[16:25] doesn't matter you're only going to get at most the 2.4 4 amps this might help explain what's
[16:32] going on so this thing and this thing and this thing are the same we have uh
[16:42] receiving two terminals with no ground that takes 120 volts or 240 um in AC
[16:50] power and converts it to a constant single voltage DC power in this case
[16:56] it's 5 volts this claims I think two amps and this is the same deal just uh
[17:05] made in a different shape and with a much uh bulkier circuit but okay so we
[17:13] have ground that's tied into this aluminum case we have neutral and line
[17:19] which are the two terminals corresponding here on screw terminals so the the
[17:26] grounding just means then uh if I want to integrate this into an
[17:33] assembly then I can have it safer and not a have a static charge buildup but
[17:39] um anyway on the outside we have just an LED indicating that it's on and we have
[17:46] V minus v+ that means we're getting 5 volts um coming out and
[17:53] it's ready for rated for 2 amps so 10 watts
[17:59] and then um in this case we have an adjustment here so that uh whatever I
[18:04] think usually the deviations in the resistors and capacitors in here will
[18:11] give you uh cheap components have plus or minus 5% frequently or 2% so they
[18:18] said well however we built the circuit we we're not going to test it on the assembly line each one it will deviate
[18:24] by um like you might get 5 point 05
[18:30] volts and then you can adjust it here with this uh I guess it's a potentiometer uh if you need a specific
[18:37] five this is cheap these might be as little as $5 um and then here same thing every
[18:44] wallart that you have comes with an appliance for a certain uh DC voltage is
[18:50] just taking the AC doing the conversion and giving you two terminals out every
[18:57] time and you can cut these wires they'll even indicate uh usually which one is
[19:02] the positive so if you want to put your own terminal on the end you can do that
[19:07] and then the behavior so I did run tests with these 5volt dude ads and in another
[19:15] case shown here is with the 12vt dad um and then we're testing as as we draw
[19:23] current and different loads of current then how does the voltage uh behave
[19:29] so this is for a 12vt power supply but you really get a very um very similar
[19:37] shape on your load test for the USB devices this is before we get into
[19:44] gallium nitride and the and the USBC these those ones are a new story so
[19:51] consider the basic simple um 5vt adapters for USB they're going to have
[19:58] all right we're drawing 0 amps and we have slightly above the voltage that it's claims uh it might be
[20:06] 5.1 volts 5.2 we draw half an amp and we
[20:11] get it the volt is just dropping slightly so 10 is here 12 is here we're
[20:16] all uh nominally within let's say 10% of the claim all right and and the
[20:24] rating will be here usually when you when you have a healthy device that
[20:30] matches its rating then the voltage will be slightly lower than the the
[20:36] nominal before it drops off totally but okay so we go half an amp 1 amp and
[20:43] we're driving down towards 11 Vols 1.5 2 amps 2.5 3 amps and and this
[20:52] one behaved according to the the rating
[20:57] so after 3 amps if we try to go to 3.5 amps we get
[21:04] this erratic Behavior you you don't know what it's going to do after that you
[21:09] should not if you place any load here in some cases you might get uh okay we're
[21:15] still powering at a healthy amount it's still 10.5 volts and you Cruise forever
[21:22] but uh it's just not reliable if you're here at 11.5 volts that's it's okay to
[21:29] run most uh devices indic um rated for 12 volts but then you have a fluctuation
[21:36] or a surge DC devices will do that then you can uh you can crash as I'll say
[21:44] you'll crash the voltage once you go down here if you back it off so we're at
[21:50] 3.5 uh amps here and we go next to nothing the wattage has gone down you've
[21:56] you've uh terminated the use of whatever device was operating on there and it's
[22:01] going to reboot or it's going to just not start back up again and
[22:07] um and then if you back off and from the testing side so this is connected to a
[22:15] control tester that can pull a specified amperage and just measure the voltage
[22:20] back off back to 2 amps you probably won't get it you need to uh if you
[22:26] haven't destroyed the device which I I never have so far so that's the good thing if you you draw too much current
[22:33] it just Fades out the voltage uh sometimes they'll they'll have a a reset
[22:38] function and or a protection and they'll just turn off unplug and plug back in
[22:44] and then you could draw two amps again um another thing is if you were to
[22:51] draw um 2 amps suddenly from a 2 amp rated device you might have other uh
[22:58] phenomena cause it to actually draw 2.5 since this is a tester we don't have
[23:04] fluctuations in the in the draw but in real life you're going to have fluctuations just like that little uh
[23:11] fan that I showed you so the fan turns on it draws more current than an amp
[23:17] even though it's it's rated for an amp and you
[23:22] can you can cause a catastrophe so um so
[23:28] this this is uh just to show you the behavior of what you get as you draw more current your voltage will draw down
[23:34] it will stay steady and until you reach whatever the max is that your um that
[23:40] your device is rated for now if you want to verify which wire you're working with
[23:46] from the terminals um you can do that just by probing so I've stripped a bit of my
[23:53] black ground wire off now I can just look up the standard
[23:59] configuration of this diagram online and that's fairly
[24:05] trustworthy um but you can also so by trustworthy I mean the position of that
[24:12] uh of that terminal inside of this inside of this connector is
[24:18] consistent they don't move that um they don't move any of those four even
[24:24] different brands of devices oh shoot sorry about the poor viewing angle but anyway so we make our
[24:32] contacts we hear the that we have continuity if I touch those together and
[24:37] then we're not tied into the housing and we are tied into one of these four so
[24:43] one 2 3 4 and then you know which terminal is
[24:50] connected to which wire you could do that or we can use these very affordable
[24:56] breakout boards usually come in a pack of five or so for five or six bucks and
[25:03] then you can plug in in this case I've got USBC I can plug that in to my board
[25:10] pin that down so nothing's flailing around I don't short circuit anything that I'm connected to and I can simply
[25:17] Probe on the labeled connections the labels will be again fairly consistent
[25:23] we have voltage out which is the same as the the positive
[25:33] ground um communication data data CC1 and cc2 are
[25:38] protocol are definitions for USBC protocol we'll jump into that later it's
[25:45] important to note if you are just starting out this is one key takeaway that will bring you very far um USB on a
[25:55] device even with multiple ports is it's one bus so you will have continuity
[26:01] between pin three of this port and pin three of this port if your device is
[26:06] more sophisticated like this Raspberry Pi 3 compared with a uh simple Arduino
[26:14] then you may have two USB buses um Universal serial bus means that all the
[26:21] traces that bring you from those communication pins on this rail to the
[26:27] communication pin in here all the way to your computer now it will be tied in
[26:32] with the same bus one bus on your computer will be talking to the bus on
[26:37] this board and um just consider it as every RX clock um ground and power are
[26:47] tied together this is one of the reasons you don't want to Power It Up um Power
[26:53] It Up from here and then communicate with your computer then you might have DV viting voltages and and noise
[27:00] injected from one side to the other um it's best to do your your powering and your communication all um at the same
[27:08] time if you're if you're doing communication with your board on your
[27:14] computer you may have a device that's doing a splitting of USB splitter which
[27:20] does allow you to communicate with multiple devices because the computer's
[27:26] uh software SL drivers are um communicating with the device and
[27:33] they're detecting what is the device and its ident and its ID and then it will do
[27:40] serial communication to that but the same data the same binary information
[27:47] and the same 0 and five volts are being transmitted to all the devices at the
[27:52] same time that is because I have one wire connected to one port that means I
[27:58] just have uh speed limitation of how much am I communicating to all the devices as
[28:06] shared and so usually you're not troubled with any uh speed limitations
[28:12] in communicating with one device but we wanted to overtime the standards allowed
[28:18] for ramping up of speed this gets you into USB 3 with the blue
[28:25] color we have a higher speed n because there's a limit limitation with talking with one device but because now I may
[28:32] want to record from a camera right here and I may want to listen to audio and
[28:38] receive all that digital information at the exact same time even though they're
[28:44] sharing data lines then you have a limitation of powering devices I would
[28:49] not want to charge my iPhone on this bus because I'm already sourcing at 5 volts
[28:56] from from the power Supply to through the the com um the motherboard to one of
[29:04] these ports and the wire the communicate uh the plugs every terminal maybe a
[29:11] resistive limitation and I'm already drawing a little bit of current to power
[29:16] up and activate this microphone and power up this camera even if I'm not using the camera actively and so I will
[29:24] be current limited if I want to charge something something on this I'll do that somewhere else times people are getting
[29:31] errors on their devices and they're not even knowing that it's because of a power limitation so if you look here we
[29:39] have 4.94 volts which is already I would consider that uh at risk of problematic
[29:47] because in the back of the board of the computer we had over 5 volts now we've
[29:52] run an extension and there's a resistive loss just on this C cable and then this
[30:00] extension that's like uh not the best practice if you can if you can get
[30:05] closer shorter cables that's good then we see all right there's a doo printer
[30:11] and I'm going to turn it on so just for communication and we get a drop in that
[30:18] voltage so we're trying to draw more current across that one little red wire that's um at Best you've got good uh 22
[30:27] or 20 gauge cables inside here but most of the time 28 so my Dao printer already has its own
[30:36] power supply so uh that that's best case scenario if you're wanting to operate
[30:42] multiple devices on the same bus and they don't have their own power supply
[30:48] you very much need to watch out for that okay so let's see what it's going to look like if we power up uh if we're
[30:55] charging something on this same circuit this one will draw .92 amps at 5 volts
[31:01] it's a small DC motor and then uh okay so I'm going to turn it
[31:09] on and we're dropping way down just because the voltage has dropped we're
[31:15] drawing only 700 milliamps even less than this one will do at five and
[31:22] charging devices like a phone will be over an amp or it will want to pull over
[31:27] an amp consider this a very unhealthy thing to do if you have problems with uh
[31:34] devices connecting and disconnecting from your PC uh and the windows or
[31:40] something is alerting you then check the power that you're pulling out of it or
[31:45] distribute your um your devices to multiple different buses you can find on
[31:51] your motherboard open up the manual to motherboard you'll see how many there are and then if it's if you're drawing
[31:58] just a lot of USB power overall your actual limitation is not the the current
[32:05] on each bus it's the the power supply for the computer overall so we said um
[32:14] the 5 volts DC output for this fairly Hefty um Cooler Master PSU is 15 amps
[32:24] and you can trust that at at or above amps this is minus whatever is being
[32:31] consumed by your computer itself is um is going to drop it below
[32:38] 5.0 and then I'd have to look in more detail to say okay is this offering an
[32:43] extra 2.5 amps on a different cable you can dive into that by looking up your
[32:50] ATX um specifications to see where those are routing this is the reason why many
[32:57] splitters like this one are going to have their own designated power port yes
[33:02] you can transmit power over the USB but limited wiring limited contacts and it's
[33:09] better to get your current from a designated Source if you can boy sorry about the focus
[33:15] there the most common error that I see in student projects is that they're
[33:20] drawing power from an Arduino board or a microcontroller board uh at the 5vt PIN
[33:28] which you know we say oh here's we have 3.3 volts and we have 5 volts um
[33:34] VN all right and then they went to power up something like a light strip but LEDs
[33:41] except for very dim indicator LEDs they draw loads of current and this
[33:47] one may be 2 amps at 5 volts so um one
[33:53] amp that's only 5 Watts you can easily draw 5 Watts from a nice LED strip and
[33:59] what they'll do is uh the power will fluctuate on the entire board while
[34:05] they're drawing power and then they'll have a communication error or a Wi-Fi
[34:10] mishap and and it's very hard to trace because no one's monitoring the voltage
[34:16] on that pin while they're operating the system so then they just don't know and
[34:24] easily you can look up on the data sheet all right this actually has its own own um its own regulator this is probably a
[34:31] 3.3 volt regulator but your board may have a power input plug and a 5vt regulator even still you um that
[34:39] regulator is specified only for a certain number of amps and then on top of that you have just the connection to
[34:46] the pin is a very very small contact with a low pressure Dupont connectors
[34:53] like these ones are only intended for making you can expect that you are
[34:59] making a very very tiny point of contact where a bent piece of metal is making contact with a flat piece of metal gold
[35:07] helps with that uh having the the gold coated pins and good quality wires but
[35:12] really these are designed for communication and not for powering
[35:17] actuators quick tip um you're not always going to know how much power things like
[35:23] to draw so the device these led strips
[35:28] come in 12vt Styles and 5vt styles but right off
[35:33] the bat if you have two uh two voltages for a product that may be pulling power
[35:41] you can assume uh the 12vt is offered in much more volume more options it's
[35:48] because that's really a more reliable way to do it even if this is your only
[35:54] device on the bus um you're any given 5vt Supply you drop it down by half a
[35:59] volt and now nothing else on the data sheet is meeting its um meeting its
[36:06] claims common mistake I see is people borrowing appliances to draw power now
[36:13] okay my television has a USB plug it's intended for um communicating data and
[36:20] receiving let's say pulling photos from here it's not designed probably for
[36:26] delivering power and that's one of the things that's improving with USBC the appliance
[36:32] manufacturers know that loads of devices on USBC are going to be draw drawing
[36:37] power so maybe they're uh increasing the the amperage available on the circuit
[36:44] board but usually that's that's not intended for powering anything now that
[36:51] we know what's inside of the cable itself then we can do anything we want
[36:57] to access that 5 volts and send it somewhere else so I have a little power bank here from Texas Instruments and
[37:05] then yes on any old splitter you can use that as a power distribution device and
[37:12] so if I don't have access to the the plug here and I want to power up some
[37:18] some lights or some device yes you can just make your own cable where I've tied
[37:23] in ground and power to the mail end for both and then I can power up this thing
[37:33] build your own splitter or bring power somewhere where you didn't have it before um including you can source that
[37:40] uh those two wires from any plain 5vt device uh anyway all right so we have
[37:46] 5.12 volts that means this thing is giving a healthy it's ready to crank out amps I can turn this guy
[37:55] on oh no it was not so
[38:00] happy okay so the next thing to do would be to discover is a limitation in here
[38:05] or is it uh the the circuits in this gu just very
[38:11] weak taking control of the wires inside this cable also give you the power to
[38:18] verify you only sending power to a device and is not attempting to communicate so now I've plugged this
[38:25] into the splitter and I'm getting two uh 20 milliamps that is um an expectable
[38:34] amount of power that has this microcontroller running and thinking not
[38:40] powering up the lights Etc uh based on that I mean you can already understand that just having the
[38:47] light on uh one some of these microcontrollers arduinos have a have a
[38:52] light that will pull just as many milliamps as the entire board itself depending depending on the the program
[39:00] you're running and then the other magic thing about this is we can count up how
[39:06] much energy is being used by my device if you're charging up a battery you can
[39:12] say from the you know low voltage to full charge how much how many milliamp
[39:19] hours have I actually used is the battery inside the device as specified
[39:24] or is it still any good and it's going to automatically this device five or 10
[39:30] bucks for the USB meter it will automatically continue counting up the milliamp hours and then you have a
[39:38] capacity or an energy rating for whatever you're drawing this gets more into the um the
[39:45] student projects and specific technical items but the reason you would want to
[39:51] um perform a not a one-time measurement of amperage but and uh integrated take
[40:00] the integral of this over time is that when you're going down a sequence of
[40:06] commands that's in your script and you've flashed this with a specific program it can vary widely vary how much
[40:13] power is being drawn you don't know the the frequency or at what moment are you
[40:19] pulling the max power so so to get a more accurate measurement you measure over time and then uh consider that to
[40:26] be your average magical thing you can do is to use one of these um cigarette
[40:32] lighter Chargers which now these are getting fairly competitive where most
[40:38] average place you can stop in and and pick one up it'll have um at at minimum
[40:44] 2 amps which used to be a respectable uh
[40:49] available all right so anything 12 volts to sometimes 24 volts these uh cigarette
[40:57] light ERS are intended to handle it so we don't have to worry if we want if we have an 18vt power tool battery and we
[41:05] can make that available to our cigarette lighter now we can power lots of stuff
[41:11] and we could make our own uh distributor okay so we're getting our 12 volts plus
[41:16] we're not worrying about frying this adapter and this adapter if it does fry
[41:22] it's protecting um it's protecting what you've plugged in over the USB so now
[41:29] this is a more healthy solution um this is for special cases we of course we
[41:35] make we build circuits with our appropriate adapters and so forth but um
[41:40] really depends on the audience this is one uh one way you can gain access to
[41:46] get your 5 volts and charge something um and disconnected remote places one
[41:52] reason is worth exploring these larger batteries cells and 12 volts and above
[42:00] is because in many student projects they're they're uh designing in
[42:05] integrating their own charging circuits which can take up like more than half of an entire Capstone design effort and so
[42:13] they're purchasing boards like this one where we say oh add your own capacitor purchase this other battery specific
[42:20] size they're always undersized um they're always thrown in the trash afterwards these Lithium
[42:26] Polymer packs and then okay plug in your load and then they're going to design
[42:31] something to integrate this into a box and an enclosure and um the the more off
[42:38] the shelf you go if it fits if it's appropriate the less you have to do the
[42:44] engineering of the integrals of your parts and that that was not the intention of multidisiplinary
[42:51] projects is to design your own charging circuit it's uh just kind of silly
[42:57] another thing you can do if you establish the circuit with a very nice uh High amperage limit uh it's output is
[43:05] capable and its output is more capable than your device if it has this plug on
[43:11] it you can basically expect it's not going to draw it'll be less than 3 amps
[43:16] um but now I want to know is my actuator healthy to be drawing from this thing
[43:22] has a known limit of 1,000 milliamps so plugging this into this and
[43:29] running it you might have lower current going just because your current limited
[43:35] now in this circuit I've got more than healthy voltage
[43:41] 5.22 um and now I'm going to run
[43:47] it I can see all right so I'll consider this 0.93
[43:54] amps is what I want to run this at full power then you can come back and plug
[44:00] this into another device let's say you don't know how much it's capable of say
[44:06] I don't have the data sheet or I don't have any claims on the back or it's from China and we just don't know if we can
[44:11] trust the claim on the back then we uh plug this into our final circuit and we
[44:19] run the same actuator and this time we just check is it pulling as many amps as
[44:26] I pulled in my experiment without a known current limitation uh known to not
[44:33] have a current limitation now let's say you don't have access to a full 5 volts
[44:40] but or your um your battery source is going to give you three or four volts
[44:46] like this lipo this gorgeous sexy Panasonic um but it's nominally 3.7
[44:53] volts so now we have these super simple cheap boost Regulators they're compact
[45:00] you can get these into a small enclosure and this will last I mean 3,300 milliamp
[45:07] hours and super long life so uh then we
[45:13] have three uh 3 volts in or whatever and a fixed 5 volts out I tie in my battery
[45:20] cell any old small uh small voltage and and then I can solder
[45:28] in my outputs to get my 5 volts and power any USB power device this has a
[45:35] two amp output limit so now all I have to do is make sure that my um I have
[45:44] available okay so here's my circuit my device asks for 1,000 milliamps or 1 amp
[45:53] at 5 volts that's 5 watts and power in equals power out this is how we're going
[45:59] to check on things this is our adapter going from 3 volts out to 5 volts and an
[46:07] unknown current the question is can this battery support enough current to do
[46:13] what I need to do and then so V1 i1 = V2
[46:18] I2 that means 3 * my current is 5 so x =
[46:25] 5 over 3 and so the sanity check says if we
[46:31] needed one amp in and this is 1.67 amps sorry we need 1 amp out so we
[46:39] need 1.67 amps in that's where the battery comes into play we can provide 6
[46:46] amps so 1.67 is no problem and then if you wanted to add some uh consideration
[46:53] for losses I suggest 20% is fairly concern conservative so now we need
[46:59] 1.67 * 1.2 and if your battery can do it you're
[47:06] all good if I need one amp at 5 volts and
[47:12] your input is 12 volts then you only need to draw 22 amps from your 12vt
[47:19] supply and you if your power source is 3 volts you're going to be drawing more
[47:25] than an amp from that battery uh
[47:30] so then you would add 20% on top of this 1.2 times this is how much I want to
[47:38] make sure that I can get from this single battery to do the job okay here's
[47:44] our next situation we want to measure the power of a USB device well these are
[47:50] commonly lying around in labs and people want to uh find out how much uh how fast
[47:57] are they charging or how much capacity if we integrate the power on here
[48:02] terrible idea um you cannot trust your information first of all because this
[48:09] sensor itself is drawing power then this the coil in here that's giving you the
[48:17] conversion um is losing power and the
[48:23] resolution of your sensor is just not appropri so we have Z amps supposedly
[48:29] coming through we have 0.1 Watts which is rounding error away from 100% off
[48:39] um and these were data points from
[48:44] previously so this kilowatt hour says how how much uh energy have I consumed
[48:50] from the AC circuit so in summary uh a
[48:56] simple $5 sensor like this one can do marveles for you if you're dealing with
[49:01] five Watts actually and these will sense sorry not 5 volts or in many cases these
[49:09] will go between one and 20 volts so you can measure energy using this guy not
[49:17] that anything up to 20 volts I would strongly advise you don't know the the
[49:23] loss here and your resolution um this is intended to measure up to
[49:30] kilowatts hours it's not a scientific instrument so you you can't expect to
[49:35] get uh three or more significant figures of accuracy um this is the situation to use
[49:44] a 5vt uh or USB power meter just for a quick
[49:51] experiment okay so we're charging this little power bank it by the way consists
[49:57] of two 18650 cells and we say we're getting 5.6 Watts going here and right
[50:04] here we've got we'd have to do the math 5.07 volts 84 amps that's less than so
[50:11] it's less than an amp that's less than 5 wats that's actually exiting through this USB cable so um we're at least at
[50:21] minimum 10% wrong and probably more than 20% so a aside from the brands the data
[50:28] sheets and um the cost of your instruments you always want to choose an
[50:34] instrument with the appropriate range for what you want to measure we want to dictate we want to uh detect if we have
[50:43] a a change in even 0.1 watts and this instrument is intended to uh measure
[50:51] more than a th000 Watts this one is intended to measure around 10 so
[50:57] consider the resolution and consider that you always want to when it comes to
[51:03] instruments you want to come down to a device in the same range as what you're
[51:09] measuring the last thing to dive into for this video I think is going to be uh
[51:15] Quick Charge that's the QC designation that was common on the market uh for
[51:21] quite some time before PD really got established um USBC and power delivery
[51:28] I'll push that off to another video because this one's getting so long um and that one is going to be so much more
[51:34] fun than this video because these are uh it's wicked cool what you can do with PD
[51:42] so much versatility I just did some quick research on quick charge and it looks like it's a whole Rabbit Hole I
[51:48] didn't describe it exactly accurately so don't treat it as ground truth but it's useful to look at these experiments
[51:55] anyway so here's an example of maybe a decade old charger for an LG cell phone and it
[52:03] says fast charge I believe the protocol actually is Quick Charge and um QC
[52:09] actually is a specific standard what it gives you is an option to boost up to 9
[52:16] volts instead of five so it is the one exception to the rule where if you're
[52:24] seeing if you're seeing this ordinary USB port then you're getting 5 volts all
[52:31] the time for every device now with QC it's possible that 9 volts might happen
[52:39] and that can confuse loads of stuff so on your PC on the back of your router
[52:44] all these ports that you're expecting 5 volts they're still going to be 5 volts you'll only get uh the chance of 9 volts
[52:50] if you basically have a designated charging device that's a general rule of
[52:56] thumb and then the other rule is they're uh still looking out for the safety of
[53:02] your uh appliances so they're always going to start with 5 volts um when they
[53:09] boot up and um and you may just always operate with 5 volts if you plug other
[53:15] stuff into this it's that is not uh fast charge qualified Quick Charge qualified
[53:21] then you're just going to remain in the 5vt zone cool and it's actually a
[53:27] healthy uh a nice variant among uh power
[53:35] adapters because it's going to be rated for more more amps than most of them this one says o 1.8 amps at five that's
[53:44] not that awesome so since I've experimented there's really only one place where I find QC to be exciting to
[53:53] work with and that's when it comes to wireless charging uh wireless charging is riddled with issues such as um high
[54:01] and low quality devices misguiding uh ratings on your shopping experience so
[54:08] this one was rated at something like uh 20 watts since I'm thinking yay it's it
[54:14] charge my phone at 20 watts um it depends uh there are more ways to cause
[54:21] it to fail than there are to cause it to succeed so first we have a five volts
[54:26] being delivered to my cable and a cable which has only two terminals that means
[54:33] there's no data lines that blue light is lit up and I'll snap that on and then
[54:39] I'm going to charge the phone or at least
[54:47] try all right so we're charging it7 amps and 5 volts you can see in the mirror
[54:55] I've got this wireless charger hooked up we're going to run this test again but this time we
[55:02] have a cable with all four wires including the data lines and then come
[55:09] here try to charge the
[55:17] phone all right there's our 9 volts and the amperage is
[55:24] climbing this means that I'm using the two pins on the the two data lines to
[55:33] request the 9vt the voltage to boost from 5 volts up to
[55:39] 9 then a lot more questions a lot more uncertainty and if you're developing
[55:45] circuits it can be pretty troubling uh overall it is cool because it at 2 amps
[55:51] you can get almost 20 watts just like that with the QC and can be useful it is
[55:58] not useful for anything around the shop where we have all these appliances that we want to recharge they have USB micro
[56:06] or USBC and uh recharging my tape measure
[56:12] it doesn't make any difference all this does is take up more space compared with the compact block lastly regarding QC
[56:20] and charging with 9 volts is the trouble where um if you have this on a splitter
[56:27] and then your Appliance requests 9 volts from the charger now I don't know what's
[56:33] going to happen I don't know if the request will get rejected or if all of the the ports on this bus for 5 volts
[56:41] will jump up to 9 volts and there is no chance since the number of pins are the
[56:47] same the the v in the positive terminal will stay the same and whoever else is
[56:54] connected on the the 5volt bus of this splitter is going to receive that 9
[57:02] volts in the worst case and who knows you might fry something so this is where
[57:07] I another reason to steer away from dealing with QC and dealing with higher
[57:13] voltages when you're only uh using the old school um regular USB port so uh
[57:21] let's wrap it up there it was a very long video and I I'm really excited to talk about the USBC and power delivery
[57:28] this is where loads of magic can happen and hopefully this video was informative
[57:34] for you I'd love to hear your comments and again I make errors and uh can't be
[57:40] an expert in everything so so do share uh information the audience might find valuable
