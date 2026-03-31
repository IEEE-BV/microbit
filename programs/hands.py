#
# Quickly display the hands of a clock turning
#

from microbit import *

hands=[Image.CLOCK1,Image.CLOCK2,Image.CLOCK3,Image.CLOCK4,
       Image.CLOCK5,Image.CLOCK6,Image.CLOCK7,Image.CLOCK8,
       Image.CLOCK9,Image.CLOCK10,Image.CLOCK11,Image.CLOCK12]

display.clear()

for i in hands:
    display.show(i)
    sleep(200)
    