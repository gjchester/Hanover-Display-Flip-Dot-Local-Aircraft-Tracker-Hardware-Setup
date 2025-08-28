Usually, when supplied the sign will come with three or four connectors, in two pairs, Power and Data.

**POWER PAIR**

1. Power into the sign.
   - This is the standard 24V in to power the sign, in a bus it would be live when the ignition was on.

2.	Lighting Circuit Feed.
     - This is a 24V feed that would have been powered when the bus lights were on, this turns on the power to the lights in the case.  When on a bus it would have been used so the signs were easily read after dark.
     - The lighting and display power connectors from the signs are clearly marked with a light bulb and battery symbol respectively.   Some signs only have one power input, these are wired so the lighting is always on.

**WARNING:** My sign has internal LED's for lighting, Older signs maybe fitted with 12V or 24V  Halogen lights  these will be clearly labelled on the Lighting wiring.

**DATA PAIR**

3.	Data In.
     - On a bus this would have been connected to a “Destination Controller” but we will use a Pi.
4.	Data Out.
     - This used to send data to the next sign, via daisy chain wiring.  Each sign can be addresses individually (see COMM section).
    - A rear sign typically only a communications input cable, as it was the end of the wiring loom in most cases.    The comms output is available on the PCB but has no wiring supplied  as standard.

This document only deals with the power side, Comms is coered in another section.    Hanover signs were designed for Bus's that generally use 24V power.  This presents a challenge as the Pi will need 5V however we can easily work around this, this is covered in the Pi Setup section.

This document also lists the way to power a LED variant sign, The setup is more or less the same but Hanover moved the connectors around but also added cleared labelling on the PCB to help.  LED signs do not have a lighting circuit.

Hanover generally do not respond to requests for data, however, some of the manuals have been published on the web by enthusiasts.  The Flip Dot Manual V8 says that the signs need 18 to 32V as input, and 1.3A @ 24V DC (Approx. 32 W).
Simon has used a 20V laptop PSU, I used a “wall wart” type 24V Power Supply rated for 72W/3A, these are usually sold as PSU’s for LED Strips.  Underpowering these signs can give unpredictable results and in my use case I also wanted to power a Pi, hence the 3A supply.
I will refer to 24V here, as that is my set up.   The colours of the connectors are the colours in my sign.   I assume they are the same in all signs, but please verify this yourself. 

**NOTE:** Pi 3 and Pi Zero W spec calls for a 5V 2.5A power supply, but they can run on the 2A that my chosen convert is rated for (see Pi Electrics section).  The Pi 4 and Pi 5 need more power than a Pi 3 or Pi zero 2. The Pi 4 specs say its needs 5V / 3A, and the Pi 5 needs 5V/5A. Your choice of Pi should guide your choice of convertor. Raspberry Pi's are capable of running on underpowered chargers, but unexpected issues or SD card corruption may be seen.
If you are aiming for the "in sign" approach then if you do use a higher rater 12/24V to 5V convertor and you may also need to use a higher rated 24V PSU to ensure all components are correclty powered. If you are planning on having the Pi outside the sign case this is less relevent as you will problaby be powering the Pi vua its own mains PSU.


**SIGN POWER**

This is probably the simplest part of the process.  On removing the back panel it should be very easy to follow the wires to work out the power input points.  

**FLIPDOT Signs**

Incoming power wires are connected to the 3 PIN orange power block as shown in the image.  
To assist further as you look at the 3 pin connecter, the terminal closest to the sign / PCB edge is the lighting power in, the centre is used by both lighting and power in as a neutral, and the furthest from the sign / PCB edge is sign power in.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/FlipDot%20Wiring.jpg)


**LED signs**

Hanwell added labels to the PCB, and moved the location, however it is now much more obvious where the 24V needs to be connected via a green power connector.  In my LED sign there is a 4 pole connector, marked 0V/24V/0V/24V,  it is unknown why this has been chosen, potentially the PCB design was first used on Flip Dots with a separate lighting circuit, and the re-used o the LED signs. It is strongly recommetned that power should only be wired to the LEFT hand Side ternals until someone documments where the right pair are wired to.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/LEDDot%20Wiring.jpg)

**LIGHTING POWER - Flip Dot Only**

I wanted the lighting circuit to be externally switchable and intended to remove the supplied external wiring loom.  This leaves a hole where the loom entered the sign.  Hanover have precut 4 holes one on each corner, but three are plugged.   The hole is 16MM and a 16mm black latching 12V-24V switch with an internal LED fitted perfectly and blended in.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/Button.jpg)

The incoming power feed is split, ion my case via multiway Wago connectors and power is feed to the sign to power it on, but also to the switch.  An additional power feed goes to the power the Pi, this is covered in the  Pi section).   
![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/Wago-5Way.jpg)


The switch was wired so the Lighting circuit power came in through the switch, then through the LED and then out to the lighting circuit.  This mean the the lights are controlled by the push button on the external case, allowing mw to only turn themn on when needed,  and the switch fitted so well gave a neat finish to the setup.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/SwitchWiring.jpg)


**Power Wiring Testing**

There is not much to go wrong, however be careful of stray tendrils of wire (espiially if you have multicore flex wire) shoering points.  This can be fixed by dipping the wire into molten solder, or using cable end crimps.  Solder is possibly easier due to the size of the connnctors.

When powered a Flip Dot sign will do a self test, to determine the size of the s=sing in use.   It will draw a vertical column  on the display, followed by a horizontal line before the sign clears and waits to receive data. 

A LED Sign will display one lit Pixel at the top left.

There are also two or three LED's on the board.   LED 1 turns on and off once per second. This Heartbeat shows that the processor is running, which means the sign has power, the use and status of the other LEDs will be mentioned later. 

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/StatusLED.jpg)

You can also short Link E on the 5 way PIN connector to intiate a self test but the  flashign LED is all that is really needed to confirm power is being supplied.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Electrics/JumperLK3.jpg)


That’s all for the Power side of the sign.


