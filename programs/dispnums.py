#
#  For loop demo with display
#

from microbit import *
import random
display.clear()

dig(0) = Image("99999\n"
               "90009\n"
               "90009\n"
               "90009\n"
               "99999")
display.show(dig(0))
sleep(500)
dig(10) = Image("90999\n"
                "90909\n"
                "90909\n"
                "90909\n"
                "90999")
display.show(dig(10))
sleep(500)
