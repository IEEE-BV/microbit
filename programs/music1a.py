#
# Music demo 1A
#

from microbit import *
import music


if button_a.is_pressed():
   display.show(Image.HAPPY)
   music.play(music.PYTHON)
elif button_b.is_pressed():
   display.show(Image.SAD)
   music.play(music.FUNERAL)

display.clear()

