import RPi.GPIO as GPIO
import os
import getch as g

def turn_led_on(x, led_list):
    clear_LED()
    GPIO.output(led_list[x],GPIO.HIGH)
    
def clear_LED():
    GPIO.output(led_list, GPIO.LOW)

#setup GPIO board here
button_list = [18,23]
led_list = [2,3,4,17]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_list, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# start program here
clear_LED()
os.system('clear')
x = raw_input("Which number to start with (1-4)?")
x = int(x) - 1
GPIO.add_event_detect(18, GPIO.FALLING)
GPIO.add_event_detect(23, GPIO.FALLING)
choice = 1
print("Press red button to go right, and blue button to go left.  Q to quit")

try:
    while True:
        turn_led_on(x, led_list)   # turns on the xth led
        if GPIO.event_detected(23):  # red_button pushed
            if x <= 2:                 # check led that was lit
                x = x + 1              # if led was less than or equal to 3, then go to next
            else:
                x = 0                  # if led was at 4, then reset to 1
        elif GPIO.event_detected(18):  # blue button pushed
            if x >= 1:
                x = x - 1
            else:
                x = 3
        else:
            continue
finally:
    print('cleaning up')
    GPIO.cleanup()
    print('done')

        
    