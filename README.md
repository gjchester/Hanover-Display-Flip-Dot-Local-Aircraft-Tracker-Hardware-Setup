# Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup

This is not my code.   This is a companion piece to Simon Prickett's wonderful local aircraft tracker    https://github.com/simonprickett/local-aircraft-tracker/.  Simon has written the code and helped with a few errors I saw along the way.

Simon's code was written in 2023 and based on the Pi Buster OS release.  His also has some processing on the Pi attached to the sign and some on a PC on the network.  I wanted to do this entirely in the Pi and keep all the electronics out of sight and in the sign.  This is my documentation on my build progress to hopefully help someone else following our footsteps.

First up the sign is a Hanover Displays - 84x8 Flip Dot Display, these were originally used on public transport (usually busses) to display route number and destination.   They are still used on some trains, but they have been replaced by LED versions as the LED’s are brighter and don't need additional lighting after dark.  There are also some that are hybrids, using flip dot and a LED in each segment to light the dot up, but I’m digressing.  

I also own a LED version and where things differ for the LED sign these will be noted too.

FlipDots are electromagnetic in nature, I'm not going to cover how they work, John Whittington has already done it much better than I can - https://engineer.john-whittington.co.uk/2017/11/adventures-flippy-flip-dot-display/ .  They are in effect like E-ink, once a message is sent to them, they retain the message even after power loss.

The usual source for these displays is eBay, or Bus Collector/memorabilia sites, Many Bus Operators have moved to LEDs already, so these tend to be in the hands of either collectors, hobbyists, or bus restorers.    These displays are heavy and have a large piece of safety glass at the front so are not easily shipped.

A typcial Bus Set consisted of three units, 
* A Front Destination board, commonly 96x16 dots, the front is a bigger sign  and will either use a bigger font to help make it more visable at a greater distances, or multiple lines of text for example **X1 Trumpton** on the top and then **VIA Camberwick Green** below.
* A Side Destination Board,  usually 84x8 dots, usually used to show the route number and destination, ie **X1 Trumpton**
* A Side or Rear Board usually 20x14 dots, these typically just have the route number, ex **X1**

Other sizes do exit,  There are bigger resolution signs (128* x 32 Front Display, and 28*14 Side/Rear Display) for the Chinese market due to the complexity of Chinese characters, and some 7 row variants also exist.   Mine is a 84 x 8 unit and I beleive Simon has a 86 x 7 unit.   This differnce isn't really of great relevence to this document, other than telling the code what sign size it should be sending to.


I’m dividing this write up into a few sections mainly so it not a huge wall of text…

 * [General Considerations](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/General%20Considerations)
 * [Sign Electrics](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Sign%20Electrics)  
 * [Sign Comms](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Sign%20Comms)
 * [Pi Electrics](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/PiElectrics)
 * [Pi OS Setup](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Pi%20Setup)
 * [Pi Program Setup and Config](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Pi%20Program)
 * [Testing](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Testing )
 * [Other considerations](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Other%20considerations)



