#
#  frequency.py
#
#  produce square wave on pin
#
#

from microbit import *

while True:
    
    pins.digital_write_pin(DigitalPin.P1, 1)
    sleep(500)
    pins.digital_write_pin(DigitalPin.P1, 0)
    sleep
    
