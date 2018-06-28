#  This will be my LED flashing python script

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24,GPIO.OUT,initial=GPIO.LOW)


while True:
    GPIO.output(24,GPIO.HIGH)
    sleep(1)
    GPIO.output(24,GPIO.LOW)
    sleep(1)
