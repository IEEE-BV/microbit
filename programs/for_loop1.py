#
# For-Loop 1
#

from microbit import *
import music

# Execute loop 5 times
for i in range(5):
    display.show(Image.MUSIC_QUAVERS)
    music.play(music.FUNK)

    sleep(500)
    display.clear()
    sleep(500)
