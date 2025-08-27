
This should be a relative short section.   The Pi needs 5V, but the sign is receiving 24V.
Thankfully there are a multitude of adapter aimed as the auto market that convert anything between e12V and 24V to 5V and many come with a USB connector that makes it easier to power a Pi.  These adapters can be bought with 1 or 2 USB connectors and it's personal choice which you would use.   In some use cases a 2nd USB supply in the sing may be helpful, for example RGB LED ligting, or if you need a powered USB hub

![A small converter unit that takes 12 or 24V and oputputs 5V via a USB socket](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/PiElectrics/Car12_24toUSB.jpg)


The power to the converter was connected in my case by multiway Wago connectors.  Alternatively soldering, or using terminal blocks is also fine, I happened to have suitable Wago connectors available.   Crimping is also acceptable as long as the crimps are tight.   If you solder or use crimps they must then be insulated in some way to prevent a short to any part of the case or other part of the PCB.

![a 5 way WAGO connector to connect wires without the need to a  screwdrivert](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/PiElectrics/Wago-5Way.jpg)

The Pi is powered by a suitable USB cable.

![Wiring Diagram ](https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/blob/main/PiElectrics/SwitchWiring_withPi.jpg)
