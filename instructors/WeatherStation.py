# Thermometer
# https://microbit.org/projects/make-it-code-it/thermometer/?editor=python

from microbit import *

def detect_light():
    if display.read_light_level() > 100:
            display.show(Image(
                "90909:"
                "09990:"
                "99999:"
                "09990:"
                "90909"))
    else:
            display.clear()

while True:

    if button_a.was_pressed():
        display.scroll(temperature())  # temperature in celcius

    elif button_b.was_pressed():
        display.scroll(temperature()*9/5 + 32)  # temperature in Fahrenheit

    else:
        detect_light()
