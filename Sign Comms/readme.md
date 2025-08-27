The comms setup is relatively simple.  Hanover signs use RS485 but their own protocol.  

As previously mentioned, when supplied the sign will come with three or four connectors, in two pairs, Power and Data.

**POWER PAIR**

1.	Power into the sign.
2.	Lighting Circuit Feed.
These maybe combined for signs with always on lighting.

**DATA PAIR**

3.	Data In.
   o	On a bus this would have been connected to a “Destination Controller” but we will use a Pi.
This is marked with an Arrow going INTO a Box
4.	Data Out.
   o	This is marked with an Arrow going OUT of a Box
   o	This used to send data to the next sign, via daisy chain wiring. Each sign can be addresses individually.
   o	A rear sign typically only a communications input cable, as it was the end of the wiring loom in most cases. The comms output is available on the PCB but has no wiring supplied as standard.

**SIGN ADDRESS** 
In their original configuration in a bus the Destination controller would be able to address multiple signs, usually three, with signs situated at the Front, Side and Rear of a bus.  While they could display completely different messages, usually they would replace each other to some extent.   The Front being the most details, the side less detail and the rear often just the route number.  The way Hanover have implemented is to daisy chain the RS485 but have a rotary selector to choose the address.   On most bus’s the front sign is 0, the side sign 1, and the rear sign 2.   The address numbers do not matter, although if multiple sings are all set to the same address they will display the same data.   
The Aircraft Tracker software is only set to drive one sign of a set size.  Trying to use multiple signs of different sizes may give unexpected results. 

Please locate the rotary selected and note the switch position.   Simons code default is set to address 5, I chose to leave mine at 1 and change the code slightly.

![alt text](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Comms/Rotary.jpg?raw=true)

**USB to RS485 Controller**

Any RS485 controller will suffice, I have tried a Waveshare Industrial USB TO RS485 with a CH343G chipset, and cheap AliExpress sources USB To RS485 converter using the CH340 and PL2303 chipset.  All were seen by the Pi and all worked as expected although the Waveshare device does have a better build quality.


![RS485 adapter](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Comms/RS485_1.jpg)   ![RS485 adapter](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Comms/RS485_2.jpg)  ![RS485 adapter](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/Sign%20Comms/RS485_3.jpg)


For the purposes of this we are only wiring up the Data In line.   Daisy chain the data out to another signs data in is possible again with the proviso that the sign should be set to the same address and be the same size.

**CONNECTING THE WIRING**

_ You are advised to take a photograph of the setup BEFORE you undo the wires to the plug. _


On a Flip Dot I have the wiring is in the order BLACK / RED / BLACK / RED.  The wire nearest to the POWER connector is Black.
On a LED sign I have the wiring is in the order BLACK / RED / BLACK / RED.  The wire furthest to the POWER connector is Black.

The wiring is relatively simple.   If your adapter has two terminals they should be marked A and B or + and -.   If your adapter has more than two terminals, they will usually be marked A, B and GRD.  5 terminal adapters also usually add in a 2nd Ground and a 5V out.
Remove the RED wire and connect it to A
Remove the RED wire and connect it to A

GROUND, or 5V are not needed.  Once again be careful of stray strands of wire that may short and solder dipping may help remove this issue.

The concludes the wiring, as noted before you may wish to remove the original cable and reuse the holes as cable entry points or a lighting power switch. 
