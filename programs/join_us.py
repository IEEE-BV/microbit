#
# join_us.py - show prospective students the micro:bit
#

from microbit import *
import speech
import music


while True :

    display.show(Image.HAPPY)
    sleep(1000)
    speech.say("Hello,FRIEND")
    sleep(1000)
    speech.say("Would you like to join our class?")
    sleep(1000)
    
    while not button_a.is_pressed() and not button_b.is_pressed() :
        sleep(10)
    
    if button_a.is_pressed():
        display.show(Image.YES)
        speech.say("Thank you, We will have fun")
        sleep(500)
        music.play(music.POWER_UP)
    elif button_b.is_pressed():
        display.show(Image.SAD)
        sleep(1000)
        speech.say("Come back if you change your mind")
        sleep(500)
        music.play(music.PUNCHLINE)
        
    sleep(1000)
    display.show(Image.HEART_SMALL)
    
    while not (button_a.is_pressed() ):
        sleep(10)
