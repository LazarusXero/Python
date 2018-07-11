import RPi.GPIO as GPIO
import os


def clear_screen():
    os.system('clear')


def turn_led_on(center_led, led_channel_list, led_offset):
    clear_LED(led_channel_list)
    for z in range(0,len(led_offset)):
        try:
            GPIO.output(led_channel_list[center_led + z], GPIO.HIGH)
        except IndexError:
            continue


def clear_LED(led_channel_list):
    GPIO.output(led_channel_list, GPIO.LOW)


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


# setup other lists
led_offset = [-2, -1, 0, 1, 2]                 # index to update the primary LED and 2 on each side

# start program here
clear_LED(led_channel_list)    # clear LEDs
clear_screen()
print("Starting in the center")
center_led = 5
GPIO.add_event_detect(18, GPIO.FALLING, bouncetime = 200)  #blue button - go right
GPIO.add_event_detect(23, GPIO.FALLING, bouncetime = 200)  #red button - go left
print("Press red button to go left, and blue button to go right.")
turn_led_on(center_led, led_channel_list, led_offset)

try:
    while True:
        turn_led_on(center_led, led_channel_list, led_offset)        
        if GPIO.event_detected(23):  # red_button pushed, go left
            center_led = shift_left(center_led)
        elif GPIO.event_detected(18):  # blue button pushed, go right
            center_led = shift_right(center_led)
        else:
            continue
finally:
    print("Cleaning up")
    clear_LED(led_channel_list)
    GPIO.cleanup()
    raw_input('Done.  ENTER to stop program.')
