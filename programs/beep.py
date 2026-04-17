#
#  beep.py
#

from microbit import *
import music

def my_beep(pitch, duration):
    music.pitch(pitch, duration)

stepsize = 25

while True:
    for i in range(440, 1100, stepsize):
        my_beep(i, 200)
        
