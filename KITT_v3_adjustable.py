# This script will cycle back and forth across 10 LEDs like KITT from Knight Rider
# It uses software PWM and hardware inputs to pause and stop the program.

import RPi.GPIO as GPIO
from gpiozero import MCP3008
import os
from time import sleep

def clear_screen():
    os.system('clear')

# This function clears the current state of the LEDs and then cycles through the
# next LEDs to be turned on.  The center led will always be the brightest while
# the offset LED brightness is adjusted based on the dutycycle_index list.
# The LEDs are updated each ineration through this function using the ChangeDutyCycle
# method

def turn_led_on(center_led, shift_index, dutycycle_index):
    clear_LED()
    dutycycle_pot = pot3.value
    for z in range(0,len(shift_index)):
        try:
            if center_led + shift_index[z] < 0:  # if the LED index is less than 0,
                continue                         # skip to next LED to avoid wrapping around
            else:
                dutycycle = dutycycle_index[z]*dutycycle_pot
                if dutycycle > 100:
                    dutycycle = 100
                else:
                    pass
                led_list[center_led + shift_index[z]].ChangeDutyCycle(dutycycle)
                #led_list[center_led + shift_index[z]].ChangeDutyCycle(dutycycle_index[z])
        except IndexError:  # if LED index is greater than the number of LEDs on the list
            continue        # ignore it to avoid an IndexError

def start_all_leds():       # initialize all LEDs with DutyCycle of 0
    for z in range(0,len(led_list)):
        led_list[z].start(0)

def stop_all_leds():        # stop all LEDs
    for z in range(0,len(led_list)):
        led_list[z].stop(0)

# this will change the duty cycle of all LEDs to 0.  This should be used instead of 'stop' to avoid
# segmentation errors in the PWM module
def clear_LED():            
    for z in range(0,len(led_list)):
        led_list[z].ChangeDutyCycle(0)


def update_speed():
    return round(pot1.value,2)/2

def change_freq():
    freq_pot = int(50*round(pot2.value,2))
    for z in range(0,len(led_list)):
        try:
            led_list[z].ChangeFrequency(freq_pot)
        except ValueError:
            led_list[z].ChangeFrequency(5)
        

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

# setup other lists and variables
dutycycle_pot = pot3.value
shift_index = [-2, -1, 0, 1, 2]             # index to update the center LED and the 2 on each side
dutycycle_index = [5, 40, 200, 40, 5]       # index to change duty cycle on LEDs to be lit up
#dutycycle_index = [2, 25, 100, 25, 2] 
led_list = [a, b, c, d, e, g, h, i, j, k]   # index of PWM objects

# start program here
#GPIO.add_event_detect(18, GPIO.FALLING, bouncetime = 200)  #blue button - exit
#GPIO.add_event_detect(23, GPIO.FALLING, bouncetime = 200)  #red button - pause
start_all_leds()                                           # initialize the LEDs
clear_screen()                                             # clear the terminal screen
raw_input("Push RED to Pause/Unpause, Blue to exit. ENTER to start.")


center_led = 0                                             # first center LED on the farthest on the left
direction = "right"                                        # initially shifting to the right

try:
    while True:
        sleep(update_speed())             # sleep based on pot 1
        change_freq()
        turn_led_on(center_led, shift_index, dutycycle_index)
        if direction == "left":      # shifting left
            print("Shifting left")
            if center_led >= 1:      # check led that was lit
                center_led -= 1      # if led has not yet reached the left side, then keep going left
            else:
                center_led = 1       # if led it has reached the left side, then send it right
                direction = "right"
        elif direction == "right":   # shifting right
            print("Shifting right")
            if center_led <= 8:      # check to see if led is all the way to the right
                center_led += 1      # if led has not yet reached the right side, then keep going right
            else:
                center_led = 8       # if it has reached the right side, then send it left
                direction = "left"  
        else:
            continue
finally:
    stop_program()
    
    
