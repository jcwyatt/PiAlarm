from gpiozero import LED
from time import sleep

led3 = LED(3)
led4 = LED(4)

while True:

    led3.on()
    led4.on()
    sleep(1)
    led3.off()
    led4.off()
    sleep(1)
