**General Consideration for your setup.
**

This is for Hanover displays, there are other Flip Dot sign makers and other Bus destination Display makers (AlfaZeta / Luminator and Mobitec) but this only code works with Hanover (Or a Badger W if you use that headend) and you may want to write your own code for other diaplsys.

You need to have some basic understanding of Linux, I’ll try and link to helpful sites, but I can’t cover everything.
You need basic electronics knowledge, but nothing to complicated but you’ll be opening covers, and changing wiring, If you can follow the instructions and take your time you should be fine.  However, if it doesn’t work, you’ll need to back track and find out why.
With the back off electroncis are exposed, please take care, whiel the sign is at 24V therte aerw a nbuemr of capacater than can hold a charge even after being powered off.  

I planned to have everything inside the sign, and it works well that way when the back cover ios off, unfortunately the Hanover cases are reasonably strong metal cases, with some shielding plates behind the display to prevent RF interference.   This means if you are putting the Pi inside the Wi-Fi signals are attenuated and may effectively be blocked.  Its not a perfect faraday cage, but the Pi’s only have small inbuilt antenna.
Possible workarounds are to use a USB based Wi-Fi Adapter that can have an extension cable antenna and disable the onboard Pi one, or modify the Pi to add a U.FL connector.  Modifying the Pi is potential cleaner, and easier but will invalidate any warranty and RF compliance.  It is your choice how to proceed.

See https://www.briandorey.com/post/raspberry-pi-zero-2-w-external-antenna-mod
https://www.hackster.io/simon-vavpotic/adding-an-external-antenna-to-raspberry-pi-5-4-3-36db41
I intend to use a USB adapter with an extension to a side mounted through connecter 

I also intend to add a side mounted HDMI and USB port these will link to the Pi internally, so I do not need to open and close the case if I need to connect a keyboard and display.  Again, this is down to personal choice.  I know Simon has some of the processing offboard and tend to run his sign without the back plate , which means the Wi-Fi signal isn’t an issue.
