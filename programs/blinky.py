#
#  blinky.py  - Let's mak an LED blink on the edge connector, Pin1
#

from microbit import *



while True:
	pin1.write_digital(1)
	sleep(1000)
	pin1.write_digital(0)
	sleep(1000)
