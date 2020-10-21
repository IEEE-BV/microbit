# Bring in the libraries that you need
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Built in red LED is on pin D13 and is internal to the Gemma
led = DigitalInOut(board.D13)       # setup external led
led.direction = Direction.OUTPUT    # set IO pin as output

i = 1
while i < 5 :                    # execute loop 5 times
  led.value = 1
  time.sleep(.5)
  led.value = 0
  time.sleep(.5)
  i = i + 1

print ("Done with 5")
