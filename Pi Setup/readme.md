**Pi Setup.**

For the most part I  would refer you back to Simon’s documentation  https://github.com/simonprickett/local-aircraft-tracker.

Each section has a readme within it and should be simple to set up.  I offer this additional information as assistance.

Simon wrote the code on the Buster version of Raspbian (Debian 10) .   I wanted to use the latest Pi OS. Partly as it difficult to get old versions of software and partly as I wondered it if would work.

I also wished to do everything “in sign”.  While I already have an ADS-B setup at home I wanted to make this portable if I needed to take it anywhere, or at least as portable as a large sign with a glass front can be).   Simon used a Pi 3 to interface to the sign, but other parts were running on a offboard computer.  Again I wanted to make this all “in sign” if possible.

I decided to try and use a Pi Zero W 2, The Pi 3 offers a little better performance than the Pi Zero W2, they have ethe same CPU, but the W is clocked to 1Ghz, whereas the Pi 3 is clocked  to 1.2Ghz.  The base Pi 3 also has 1GB of memory Vs the W has 512MB, however the Pi Zero W 2 is much smaller and is rated (at least on paper) to a higher temperature.  
The Pi 3 also has 4 USB ports whereas the Zero W needs a small USB hub.  

After getting this set up on a Pi Zero I hit the issue that the case became a faraday cage effectively stopping me SSH-ing on to the Pi, and the Pi being able to sit on my Wi-Fi and I decided to use an external WiF adaopter over the Pi Zero’s onboard.  

There are advantages to using either Pi, and ultimately it may be decided by what you have to hand.   If you need to buy a Pi then a Pi 4 or 5 would be the preferable option although it is probably more performance than needed.

The Pi Zero has some issues but these are easily worked around.

I have a FlightAware Pro Stick Plus  https://www.flightaware.com/adsb/prostick/  mounted inside the sign, This and the RS485 to USB adapter are connected to the Pi via a small USB hub that has a Micro USB cable rather than full size USB.  In my case it has a Charge/OTG switch, it needs to be se tot OTG to allow data flow.

Once the USB parts are connected we can install Raspberry Pi Rasbian OS.   I used a Sandisk Ultra SD card, the card does not need to be big, and it’s not going to do a lot of write backs to the database, however personal choice is to use SanDisk Ultra as I find they seem to last longest in Pi’s compared to other brands.  A large card is not needed, however (at the time of writing) Micro SD card smaller than 32 GB are generally more expensive than a 32G or 64GB card.

PI OS was writing to the SD card using the Raspberry Pi imager, with customisation set to enable SSH, configure Wi-Fi and create an account for me rather than the default Pi.  You may wish to sdo this or stick with the defaults.

The card was inserted into the PI and it was left to boot. 

We do not need the GUI interface so this should be disabled on boot to reduce memory load, and I prefer to enable autologin.   This can be done in one of two ways, the first is to use the GUI and set the Pi to boot to the CLI.  The other is to SSH into the Pi and use the Raspi-Config tool to set the Pi to autologon to the desktop.

Once the Pi was running and we have a stable conenction all cables are stuck with tape /  cable ties to prevent movement as much as possible, and you should put the Pi in a case and then stick the case down to prevent movement that could lead to cable disconnection.

**Note** Depending on your Pi case it may be easier to wait until the SD card is inserted into the Pi and the Pi in the case before sticking it down.  Not all cases hase SD card access slots.
