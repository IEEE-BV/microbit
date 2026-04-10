#
# funny.py - use speech for some fun
#

from microbit import *
import speech


display.show(Image.HAPPY)
sleep(1000)
speech.say("Hello,FRIEND")
sleep(1000)
display.show(Image.HEART)
sleep(1000)
speech.say("Hello,BUDDY")
sleep(1000)
display.show(Image.DIAMOND)
speech.say("Hello,STUDENT", speed=80, pitch=282, throat=120)
sleep(1000)
speech.say("SHALL WE PLAY A GAME?")
sleep(1000)
display.show(Image.HEART_SMALL)
speech.say("BE MY FRIEND")
