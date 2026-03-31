#
#  frequency.py
#
#  produce square wave on pin
#
#

from microbit import *
import utime

while True:
    
    pin0.write_digital(1)
    utime.sleep(200)
    pin0.write_digital(0)
    utime.sleep(200)
    