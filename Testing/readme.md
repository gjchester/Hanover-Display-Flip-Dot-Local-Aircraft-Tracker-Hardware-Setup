**Testing**

If you have got this far, we are now on the final steps, however this can be the most frustrating part as there is little feedback, it usually either works or does not.

Thankfully there a few programs we can use to help us.  You do not need to follow these in order, but if you jump to the end and it fails you need to come back here and do these steps in order to work out where the issue is.  If yo uwant o jump ahead go to the Running The Program page

**Wiring check**

Hanover Signs have a test mode, the controller sends a signal out that causes all sign to go into test mode.  This is useful to check the USB to RS485 is wired correctly.  

Sam Briggs wrote a python driver, and a way to emulate the Hanover Controller test mode.  The code does much more but we just need the sign test.  Start by GIT cloning his code to your Pi, I have it under the user home directory on mine

`git clone https://github.com/briggySmalls/pyflipdot`

then move into that directory run the setup 

`python setup.py install`

He has also posted the code to start a test  https://briggysmalls.github.io/pyflipdot/usage.html  this is replicated here in case Sam ever removes his document, but I do not wish to claim that hsi is my code is mine, its not.

Copy the code on the useage page or copy the TestSign.py and Stoptest.py   I’m lazy and I named them that way so tab complete works quicker

After you have the code installed and the start and stop file you can trigger a sign test.  This is done by sending the command `pyflipdot TestSign.py`  (or the Stoptest.py), once run  a FlipDot will run through a few test patterns, and the LED dot will have a rolling message telling you the size, and firmware version.  

This is sent to all sign addresses so only really serves to show the USB to RS485 is working as expected.

If this does not work go back and check the wiring, being especially careful you do not have strands of wire causing shorts on the RS485 connection at either end.


**Comms check**

This is where it can be harder, not only do we need the USB to serial working but we need to also make sure we have the right settings.  Using the wrong values for address, row, or columns generally means nothing happen.  If you are lucky you are close and you get some reaction but more often than not you have no feedback.

To run these tests we will use   John Whittington's code to send simple messages to the display.  https://engineer.john-whittington.co.uk/2017/11/adventures-flippy-flip-dot-display/
There are a few thing to note before we start.  John has a 56×7 display that has an address of 5, and so this is the default for his code.   Unless you have the same size module, with the same address you will need to specify the address, rows and columns on the command line or tweak the code.

Start by GIT cloning his code to your Pi, I have it under the user home directly 

`https://github.com/tuna-f1sh/node-flipdot`

then change into that directory and run the setup 

`npm install -g flipdot-display`

We can then send the command to the display.   This is where the address issue may be the most obvious, while my display is address is 1 I have to use address 2 in this code (remember my FlipDot is is 8 rows x 86 colums) 

`flipdot -a 2 -r 8 -c 86`

the screen should echo this following and if all goes well the sign works.

```
FlipDot port open on /dev/ttyUSB0 @: 4800
Sending: Hello World!!
Written!
```

If this step fails then it down to trial and error and persistance, first you can try and change the address unitl you get some response  eg `flipdot -a 3 -r 8 -c 86` then `flipdot -a 4 -r 8 -c 86` and work through the settings.

The other thing to try is to remove the rows and column so it used the default, this will result in a squashed output but should at least let you work out the address part by trial and error.


It is useful to check that the LED’s status on the processor board.  When in normal use LED 1 (Heartbeat) will flash once about couple of seconds to show the sign electronics are working (ie not crashed) and LED 2 (Comms) will flash briefly whan  the sign electrioncis receives data for the sign. 

On signs with a 7070 & 7080 Board LED 3 will flash every time the processor sends a signal to  Flip/LED display. 

LED2 can display the following status indications via its status.   

• brief flash when the sign receives a valid comms message addressed to it. 

• long flash if the sign receives a message with bad contents. 

• permanently on if the sign has not received a valid message within the previous 60 seconds. 

