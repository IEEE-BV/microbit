from microbit import *
import music, random



for i in range(8):
  freq = random.randint(100,2000)
  sleep(50)
  music.pitch(freq, 50)
