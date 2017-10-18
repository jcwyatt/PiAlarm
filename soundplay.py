import os
import random
from time import sleep

while True:
	soundChoice = str(random.randint(1,5))
	playSound = ('aplay '+soundChoice+'.wav')
	print (playSound)
	os.system(playSound)
	sleep (5)

