#
# Hot Potato
#



from microbit import *
import random
import music

def my_beep(duration):
      music.pitch(800, duration)
    
def disp_num(number) :
        if number == 1:
            display.show(Image(
                "00005:"
                "00005:"
                "00005:"
                "00005:"
                "00005"))
        elif number == 2:
            display.show(Image(
                "55555:"
                "00005:"
                "55555:"
                "50000:"
                "55555"))
        elif number == 3:
            display.show(Image(
                "55555:"
                "00005:"
                "00555:"
                "00005:"
                "55555"))
        elif number == 4:
            display.show(Image(
                "50005:"
                "50005:"
                "55555:"
                "00005:"
                "00005"))
        elif number == 5:
            display.show(Image(
                "55555:"
                "50000:"
                "55555:"
                "00005:"
                "55555"))
            
# program starts here

while True:

# do a countdown to start the game
  if button_a.is_pressed():
            
    display.clear()            
    for i in range (5, 0,-1):
        disp_num(i)
        my_beep(500)
        sleep(1000)

    display.show(Image.YES)
    sleep(500)

    display.clear()


# generate a random number for the number of beeps
# before the potato goes off
    display.show(Image.HAPPY)
    beep_count = random.randint(6,11)
    print(beep_count)

    while (beep_count > 0) :
        my_beep(500)
        sleep(2000)
        beep_count = beep_count - 1
    
# times up - time to Buzzzzzzz
    display.show(Image.SAD)
    my_beep(5000)
    display.clear()

# its over - since we are in a while-true loop
# pressing the 'A' button starts a new game
  
      

