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

### Lesson: List of Lessons

- FOR2 - Nested for-loops
- SOUND2 - Learn how buttons work
- DICE - roll the dice!

### Lesson: List of Games to Try

- MUSIC - plays musical scales
- DICE - roll the dice!
- DUCK - Group Game
- WEATHER - weather station, temperature of cpu
- FUNNY - Text to SPEECH
- HOT POTATO - Use battery and toss microbit to friends (need to write)
-  
-  
- 







