**Pi Program Setup**

For the most part I  would refer you back to Simon’s documentation  https://github.com/simonprickett/local-aircraft-tracker.

Each section has a readme within it and should be simple to set up.  I offer this additional information as assistance.

Addition notes on some sections:

**Receiver.**

Simon mentions you need a working copy of Dump1090.   This page offers a comprehensive guide to compiling and installing the software if you are not familiar with the process.
https://www.satsignal.eu/raspberry-pi/dump1090.html

Note that you need to copy the env.example to .env  even if you make no changes.
cp env.example  .env

A file starting with . means it is hidden in Linux,  if you need to check the content of the folder **ls -al**  will show all the contents.

Nano is the easier editer to use if you are not familiar with Linux, however you probalby do not need to make changes to thsi if you are running all the code on the same computuer

If you make change to the .env file you need to redo the **npm install** step to ensure changes are written to the system.


**Enricher**

Again that you need to copy the env.example to .env  and make changes to add your Fligtware API key.     

cp env.example  .env

then nse nano to edit the file 

nano .env

Make the change and **Ctrl X ** then **Y** to exit

Afterthe intial setup, and after any changes to the .env file you need to redo the **npm install** step to ensure changes are written to the system.


**Notifier**

Again that you need to copy the env.example to .env  and make changes to add your location and how far yo uwant to havbe a a radius around your location.     

cp env.example  .env

then use nano to edit the file 

nano .env

Make the change and **Ctrl X ** then **Y** to exit

After the intial setup, and after any changes to the .env file you need to redo the **npm install** step to ensure changes are written to the system.


**Frontends**

You may remember in the Sign Comms there was a refernce to note down the sign address, this is where that is needed.   https://github.com/gjchester/Hanover-Display-Flip-Dot-Local-Aircraft-Tracker-Hardware-Setup/tree/main/Sign%20Comms

For the last time, you need to copy the env.example to .env  and make changes to add your sign details.  In my example image mu sign is set to 1,   You need to set the line **SIGN_ADDRESS=1** to match tha number, however in some cases you need to add 1 so you woulsd use **SIGN_ADDRESS=2** 
The rest of the settings in the .env should be obvious.  

cp env.example  .env

then use nano to edit the file 

nano .env

Make the change and **Ctrl X ** then **Y** to exit

Again After the intial setup, and after any changes to the .env file you need to redo the **npm install** step to ensure changes are written to the system.

This concludes the Software setup part. 
