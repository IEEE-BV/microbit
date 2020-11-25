# Music demo 1
#
# s.case 11/13/20
#


from microbit import *
import music

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        music.play(music.PYTHON)
    elif button_b.is_pressed():
        display.show(Image.SAD)
        music.play(music.FUNERAL)
    display.clear()
