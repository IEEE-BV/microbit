# Write your code here :-)
from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        # When pressing both buttons only play via the edge connector
        audio.play(Sound.HELLO)
    elif button_a.is_pressed():
        # On button A play a sound and when it's done show an image
        audio.play(Sound.HAPPY)
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        # On button B play a sound and show an image at the same time
        audio.play(Sound.TWINKLE, wait=False)
        display.show(Image.BUTTERFLY)

    sleep(500)
    display.clear()
