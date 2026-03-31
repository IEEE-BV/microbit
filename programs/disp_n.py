
#
# disp_n.py
#
# Shake the microbit to roll the dice.
#
#

from microbit import *
import random

def disp_num(number) :
        if number == 1:
            display.show(Image(
                "00005:"
                "00005:"
                "00005:"
                "00005:"
                "00005"))
        elif number == 2:
            display.show(Image(
                "55555:"
                "00005:"
                "55555:"
                "50000:"
                "55555"))
        elif number == 3:
            display.show(Image(
                "55555:"
                "00005:"
                "00555:"
                "00005:"
                "55555"))
        elif number == 4:
            display.show(Image(
                "50005:"
                "50005:"
                "55555:"
                "00005:"
                "00005"))
        elif number == 5:
            display.show(Image(
                "55555:"
                "50000:"
                "55555:"
                "00005:"
                "55555"))
        elif number == 6:
            display.show(Image(
                "50000:"
                "50000:"
                "55555:"
                "50005:"
                "55555"))
        elif number == 7:
            display.show(Image(
                "55555:"
                "00005:"
                "00005:"
                "00005:"
                "00005"))
        elif number == 8:
            display.show(Image(
                "55555:"
                "50005:"
                "55555:"
                "50005:"
                "55555"))
        elif number == 9:
            display.show(Image(
                "55555:"
                "50005:"
                "55555:"
                "00005:"
                "55555"))
        elif number == 0:
            display.show(Image(
                "55555:"
                "50005:"
                "50005:"
                "0005:"
                "55555"))
        elif number == 10:
            display.show(Image(
                "50555:"
                "50505:"
                "50505:"
                "50505:"
                "50555"))

display.clear()
while True :
  for n in range(10,-1, -1):
    disp_num(n)
    sleep(2000)
  display.clear