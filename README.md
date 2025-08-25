# Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup

This is not my code.   This is a companion piece to Simon Prickett's wonderful local aircraft tracker    https://github.com/simonprickett/local-aircraft-tracker/.  Simon has written the code and helped with a few errors I saw along the way.

Simon's code was written in 2023 and based on the Pi Buster OS release.  His also has some processing on the Pi attached to the sign and some on a PC on the network.  I wanted to do this entirely in the pi and keep all the electronics out of sight and in the sign.  This is my documentation on my build progress to hopefully help someone else following out footsteps.

First up the sign is a Hanover Displays - 84x8 Flip Dot Display, these were originally used on public transport (usually busses) to display route number and destination.   They are still used on some trains, but they have been replaced by LED versions as the LED’s are brighter and done need additional lighting after dark.  There are also some that are hybrids, using flip dot and a LED in each segment to light the dot up, but I’m digressing.  

FlipDots are electromagnetic in nature, I'm not going to cover how they work, John Whittington has already done it much better than I can - https://engineer.john-whittington.co.uk/2017/11/adventures-flippy-flip-dot-display/ .  They are in effect like E-ink, once a message is sent to them, they retain the message even after power loss.

The usual source for these displays is eBay, or Bus Collector/memorabilia sites, Many Bus Operators have moved to LEDs already, so these tend to be in the hands of either collectors, hobbyists, or bus restorers.    These displays are heavy and have a large piece of safety glass at the front so are not easily shipped.

A typcial Bus Set consisted of three units, 
* A Front Destination board, commonly 96x16 dots, the fron is a bigger sign  and will either use a bigger font to help make it more visable at a greater distances, or multiple lines of text for example a VIA type message.
* A Side Destination Board,  usually 84x8 flip dots, used to showe the route number and destiation
* A Side or Rear Board usually 20x14 dots, these typeically just have the route number.

Other sizes do exit,  There are bigger resolution signs (128* x 32 Front Display, and 28*14 Side/Rear Display) for the Chinese market due to the complexity of Chinese characters, and some 7 row variants also exist.   Mine is a 84 x 8 unit and I beeive Simon has a 86 x 7 unit.   This differnet isn't really of great relevence to this document.


I’m dividing this write up into a few sections mainly so it not a huge wall of text…

 * Sign Electrics
 * Sign Comms
 * Pi Setup
 * Other considerations



