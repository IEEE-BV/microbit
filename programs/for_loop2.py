#
#  For loop demo with display
#

from microbit import *
import random
display.clear()


while True:
    for i in range(0, 5):
        for j in range(0, 5):
          display.set_pixel(j, i, random.randint(0, 9))
    sleep(80)

    display.clear()