from pyflipdot.pyflipdot import HanoverController
from serial import Serial

# Create a serial port (update with port name on your system)
ser = Serial('/dev/ttyUSB0')

# Create a controller
controller = HanoverController(ser)

# Stop the test sequence on any connected signs
controller.stop_test_signs()
