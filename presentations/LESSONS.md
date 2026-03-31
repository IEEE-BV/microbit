# Micropython Lessons
## Basics
### Use the REPL
1+1
print("Hello World")

### Lesson: Libraries
import machine
dir(machine)

import microbit
dir(microbit)

dir(Image)

========================================================

### Lesson: FOR LOOPS

from microbit import *
import music

for i in range(5):
    display.show(Image.HAPPY)
    music.play(music.CHASE)

    sleep(500)
    display.clear()
    sleep(500)

========================================================

### Lesson: Running, booting
- ItemRun what is in the editor screen (F5)
- import program_to_run

Create main.py (works similar to boot.py)

^s == SAVE
^c==QUIT
^d==REBOOT

========================================================

In REPL show the contents of the library modules

- import music
dir(music)
import machine
dir(machine)

### Lesson Plan
- Presentation mico:bit v3
- HELLO - Easy program to type a name
- FOR2 - Nested for-loops
- SOUND2 - Learn how buttons work
- DICE - roll the dice! Random number generator

### List of Programs and Games

- MUSIC - plays musical scales
- DICE - roll the dice! Contains functions()
- DIGITS - How to design digits for the led display
- COUNTDOWN.PY - Uses display for a countdown from 10 to 0. BUT WAIT! There's a bug in the code. Find it and fix it!
-
- DUCK - Group Game
- WEATHER - weather station, temperature of cpu
- FUNNY - Text to SPEECH demo
- HOT POTATO - Use battery and toss micro:bit to friends (need to write)
- EIGHT_BALL.PY - Learn how to shake the micro:bit and display something
- HELLO - Easy program to put text on the display 
- BEEP.PY - Use external speaker for micro:bit v1
- AUDIO.PY - Generate sin, square and triangle wave and display on led screen
- BOOT.PY - Used by other MicroPython implementations to 'boot' the machine. Not used by micro:bit?
- DALEK.PY - Advanced. Uses lists to generate random poem for Dr Who
- HANDS.PY - Display the hands of a clock turning
- 







