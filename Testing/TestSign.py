from pyflipdot.pyflipdot import HanoverController
from serial import Serial

# Create a serial port (update with port name on your system)
ser = Serial('/dev/ttyUSB0')

# Create a controller
controller = HanoverController(ser)

# Start the test sequence on any connected signs
controller.start_test_signs()
