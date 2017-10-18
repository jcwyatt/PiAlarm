from gpiozero import LED
from time import sleep
import datetime
import codecs
import os
import random
import urllib2
from bs4 import BeautifulSoup

#scrape the data from weather website
rawhtml=urllib2.urlopen("https://m.gov.je/Weather/TwentyFour").read(4000)
soup=BeautifulSoup(rawhtml,"html.parser")

#print(soup.prettify())


#the weather is grouped in 'p' tags

rawWeatherData=soup.findAll('p')

#print(rawWeatherData)


#get the text from each p tag and write to text file.

with codecs.open("metToday.txt","w",encoding='utf-8') as myfile:
	i=0
	parsedWeatherData=[]
	for n in rawWeatherData:
		parsedWeatherData.append(rawWeatherData[i].get_text()+" ")
		print(parsedWeatherData[i])
		myfile.write(parsedWeatherData[i])
		i += 1


print("All done. Check metToday.txt for output")
