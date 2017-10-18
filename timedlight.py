from gpiozero import LED
from time import sleep
import datetime
import os
import random

led = LED(4)

overRide='auto'
amOn=datetime.time(05,45,00)
amOff=datetime.time(07,30,00)
pmOn=datetime.time(21,45,00)
pmOff=datetime.time(22,15,00)

print (pmOff)
soundTrigger=0
while True:
	while overRide=='auto':

		timeNow=datetime.datetime.now().time()
		soundchoice = str(random.randint(1,8))
		playsound=('aplay /home/pi/Documents/pythonsaves/'+soundchoice+'.wav')
		if timeNow>pmOn and timeNow<pmOff or timeNow>amOn and timeNow<amOff:
			led.on()
			print('led on')
			soundTrigger+=1
			if soundTrigger==1:
				os.system(playsound)	
				os.system(python /home/pi/Documents/pythonsaves/metscrape.py)	
				sleep(4)
				sayWeather=('espeak -f metToday.txt -v +m1 -a 200 -w weather2.wav $$ aplay weather2.wav')
				os.system(sayWeather)
		else:
			led.off()
			print('led off')
			soundTrigger=0		
		sleep(60)
