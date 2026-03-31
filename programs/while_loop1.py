# While-Loop 1
#
# s.case 10/26/20
#
#

# Bring in the libraries that you need
from microbit import *


i = 1
while i < 5:                    # execute loop 5 times?
    display.show(Image.SKULL)
    sleep(500)
    display.clear()
    sleep(500)
    i = i + 1