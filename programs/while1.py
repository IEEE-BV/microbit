from microbit import *

i = 0

while i<10 :
    display.scroll(i)
    sleep(500)
    i=i+1
    
print("Done")
