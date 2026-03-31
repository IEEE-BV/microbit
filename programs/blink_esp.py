# blink_esp.py
#
# s.case 1/8/21
#
#


# Bring in the libraries that you need
import machine
pin2 = machine.Pin(2, machine.Pin.OUT)

# Execute loop 5 times
for i in range(5):
    pin2.value(True)
    sleep(500)
    pin2.value(False)
    sleep(500)
