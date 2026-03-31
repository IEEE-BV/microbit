#
#  frequency.py
#
#  produce square wave on pin
#
#

from microbit import *

while True:
    
    pin0.write_digital(1)
    sleep(10)
    pin0.write_digital(0)
    sleep(10)
    
    
