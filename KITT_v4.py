# This script will cycle back and forth across 10 LEDs like KITT from Knight Rider
# It uses software PWM and hardware inputs to pause and stop the program.

import RPi.GPIO as GPIO
from gpiozero import MCP3008
import os
from time import sleep


def clear_screen():
    os.system('clear')


def start_all_leds():       # initialize all LEDs with DutyCycle of 0
    for z in range(0,len(led_list)):
        led_list[z].start(0)


# This function clears the current state of the LEDs and then cycles through the
# next LEDs to be turned on.  The center led will always be the brightest while
# the offset LED brightness is adjusted based on the dutycycle_index list.
# The LEDs are updated each ineration through this function using the ChangeDutyCycle
# method
def turn_led_on(center_led):
    dc_min = [2, 25, 80, 25, 2]
    dc_max = [40, 60, 100, 60, 40]
    shift_index = [-2, -1, 0, 1, 2]              # index to update the center LED and the 2 on each side
    dc_pot = round(pot3.value,2)
    
    for z in range(0,len(shift_index)):
        try:
            if center_led + shift_index[z] < 0:  # if the LED index is less than 0,
                continue                         # skip to next LED to avoid wrapping around
            else:
                dutycycle = dc_min[z] + (dc_max[z]-dc_min[z])*dc_pot
                led_list[center_led + shift_index[z]].ChangeDutyCycle(dutycycle)
        except IndexError:                       # if LED index is greater than the number of LEDs on the list
            continue                             # ignore it to avoid an IndexError


# this will change the duty cycle of all LEDs to 0.  This should be used instead of 'stop' to avoid
# segmentation errors in the PWM module
def clear_LED():            
    for z in range(0,len(led_list)):
        led_list[z].ChangeDutyCycle(0)


def update_sleep():
    sleep_min = 0.005
    sleep_max = 0.5
    sleep_pot = round(pot1.value,2)
    new_sleep = sleep_min + (sleep_max-sleep_min)*sleep_pot
    return (new_sleep)


def update_frequency():
    freq_min = 5
    freq_max = 100
    freq_pot = round(pot2.value,2)
    new_freq = freq_min + (freq_max - freq_min)*freq_pot
    for z in range(0,len(led_list)):
        led_list[z].ChangeFrequency(new_freq)


def update_center_led(center_led, direction):
    if direction == "l":      # shifting left
        if center_led >= 1:      # check led that was lit
            center_led -= 1      # if led has not yet reached the left side, then keep going left
        else:
            center_led = 1       # if led it has reached the left side, then send it right
            direction = "r"
    else:                        # shifting right
        if center_led <= 8:      # check to see if led is all the way to the right
            center_led += 1      # if led has not yet reached the right side, then keep going right
        else:
            center_led = 8       # if it has reached the right side, then send it left
            direction = "l"
    return(center_led, direction)


def stop_all_leds():        # stop all LEDs
    for z in range(0,len(led_list)):
        led_list[z].stop(0)


def stop_program():
    print("Cleaning up")
    stop_all_leds()
    raw_input('Done.  ENTER to stop program.')
    GPIO.cleanup()


# setup GPIO board here
led_channel_list = [2, 3, 4, 17, 27, 22, 5, 6, 13, 19]  # led GPIO channels
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_channel_list, GPIO.OUT, initial=GPIO.LOW)   # initial LED setup
a = GPIO.PWM(2, 100)     # setting up PWM objects by channel with 100Hz freq
b = GPIO.PWM(3, 100)
c = GPIO.PWM(4, 100)
d = GPIO.PWM(17, 100)
e = GPIO.PWM(27, 100)
g = GPIO.PWM(22, 100)
h = GPIO.PWM(5, 100)
i = GPIO.PWM(6, 100)
j = GPIO.PWM(13, 100)
k = GPIO.PWM(19, 100)
pot1 = MCP3008(channel=0, port = 0, device = 0)
pot2 = MCP3008(channel=1, port = 0, device = 0)
pot3 = MCP3008(channel=2, port = 0, device = 0)
led_list = [a, b, c, d, e, g, h, i, j, k]   # index of PWM objects
center_led = 0                                             # first center LED on the farthest on the left
direction = "r"                                        # initially shifting to the right

# start program here
start_all_leds()                                           # initialize the LEDs
raw_input("Push RED to Pause/Unpause, Blue to exit. ENTER to start.")
clear_screen()                                             # clear the terminal screen

try:
    while True:
        sleep(update_sleep())             # sleep based on pot 1
        update_frequency()
        clear_LED()
        turn_led_on(center_led)
        center_led, direction = update_center_led(center_led, direction)
finally:
    stop_program()
    
    
