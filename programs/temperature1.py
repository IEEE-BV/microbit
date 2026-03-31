#
# Temperature Measurement Program
#
# The microbit has an internal thermistor on the actual microprocesor chip.
#
#


from microbit import *
while True:
    if button_a.was_pressed():
        display.scroll(temperature())
    elif button_b.was_pressed():
        display.scroll("Hi   My name is   Steve   ")