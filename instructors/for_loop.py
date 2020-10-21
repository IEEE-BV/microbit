# Bring in the libraries that you need
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Built in red LED is on pin D13 and is internal to the Gemma
led = DigitalInOut(board.D13)       # setup external led
led.direction = Direction.OUTPUT    # set IO pin as output

# Execute loop 5 times
for i in range (5):
  led.value = 1
  time.sleep(.5)
  led.value = 0
  time.sleep(.5)

print ("Done with 5")
