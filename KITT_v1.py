import RPi.GPIO as GPIO
import os
from time import sleep

def clear_screen():
    os.system('clear')


def turn_led_on(center_led, led_offset, dutycycle_index):
    clear_LED()
    for z in range(0,len(led_offset)):
        try:
            led_list[center_led + led_offset[z]].ChangeDutyCycle(dutycycle_index[z])
        except IndexError:
            print("Index Error")
            continue

def start_all_leds():
    for z in range(0,len(led_list)):
        led_list[z].start(0)

def stop_all_leds():
    for z in range(0,len(led_list)):
        led_list[z].stop(0)

def clear_LED():
    for z in range(0,len(led_list)):
        led_list[z].ChangeDutyCycle(0)


def shift_left(center_led):
    print("Shifting left")
    if center_led >= 1:  # check led that was lit
        center_led -= 1  # if led was greater than or equal to 1, then go left
    else:
        center_led = 9  # if led was at 0, then reset to 9
    return(center_led)


def shift_right(center_led):
    print("Shifting right")
    if center_led <= 8:
        center_led += 1
    else:
        center_led = 0
    return(center_led)

    
# setup GPIO board here
button_list = [18, 23]
led_channel_list = [2, 3, 4, 17, 27, 10, 9, 11, 5, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_channel_list, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(button_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
a = GPIO.PWM(2, 100)     # setting up PWM objects by channel with 100Hz freq
b = GPIO.PWM(3, 100)
c = GPIO.PWM(4, 100)
d = GPIO.PWM(17, 100)
e = GPIO.PWM(27, 100)
g = GPIO.PWM(10, 100)
h = GPIO.PWM(9, 100)
i = GPIO.PWM(11, 100)
j = GPIO.PWM(5, 100)
k = GPIO.PWM(6, 100)

# setup other lists
led_offset = [-2, -1, 0, 1, 2]                 # index to update the primary LED and 2 on each side
dutycycle_index = [2, 25, 100, 25, 2]         # index to change duty cycle on leds
led_list = [a, b, c, d, e, g, h, i, j, k]   # index of PWM objects

# start program here
clear_LED()    # clear LEDs
clear_screen()
print("Starting in the center")
center_led = 5
GPIO.add_event_detect(18, GPIO.FALLING, bouncetime = 200)  #blue button - go right
GPIO.add_event_detect(23, GPIO.FALLING, bouncetime = 200)  #red button - go left
print("Press red button to go left, and blue button to go right.")
start_all_leds()

try:
    while True:
        turn_led_on(center_led, led_offset, dutycycle_index)
        while True:
            if GPIO.event_detected(23):  # red_button pushed, go left
                center_led = shift_left(center_led)
                break
            elif GPIO.event_detected(18):  # blue button pushed, go right
                center_led = shift_right(center_led)
                break
            else:
                continue
finally:
    print("Cleaning up")
    stop_all_leds()
    GPIO.cleanup()
    raw_input('Done.  ENTER to stop program.')
