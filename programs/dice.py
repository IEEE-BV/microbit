
#
# dice.py
#
# Shake the microbit to roll the dice.
#
#

from microbit import *
import random, music

def beeper() :
  for i in range(8):
    freq = random.randint(100,2000)
    sleep(50)
    music.pitch(freq, 50)


while True:
    if accelerometer.was_gesture('shake'):
        beeper()
        number = random.randint(1, 6)
        if number == 1:
            display.show(Image(
                "00000:"
                "00000:"
                "00900:"
                "00000:"
                "00000"))
        elif number == 2:
            display.show(Image(
                "00000:"
                "00000:"
                "90009:"
                "00000:"
                "00000"))
        elif number == 3:
            display.show(Image(
                "00009:"
                "00000:"
                "00900:"
                "00000:"
                "90000"))
        elif number == 4:
            display.show(Image(
                "90009:"
                "00000:"
                "00000:"
                "00000:"
                "90009"))
        elif number == 5:
            display.show(Image(
                "90009:"
                "00000:"
                "00900:"
                "00000:"
                "90009"))
        else:
            display.show(Image(
                "90009:"
                "00000:"
                "90009:"
                "00000:"
                "90009"))
