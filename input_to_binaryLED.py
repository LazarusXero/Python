# This program will convert a user-input value from 01 to 15 to binary
# LED value.  Then when the user pushes the push-button, the LED's
# will reset and the user input on the screen will display again.
# User can quit using the ESC key.

from gpiozero import Button, LED
import os

# Detect a push button and display a printed message to the screen when
# pushed.

# This function will turn all LEDs off
def clear_LED():
    led1.off()
    led2.off()
    led3.off()
    led4.off()

# This function will simply wait for the breadboard button to be pressed
# and will then clear the screen and re-enter the main loop
def wait_for_reset():
    print("Push button to reset...")
    button.wait_for_press()
    os.system('clear')

# This function will display the value typed, and then display the binary
# equivalent on the LEDs on the breadboard
def display_led(key):
    print("You entered {0}". format(key))
    print("Displaying binary equivalent on LEDs, which is {0:04b}".format(key))
    if key in led1set:
        led1.on()
    if key in led2set:
        led2.on()
    if key in led3set:
        led3.on()
    if key in led4set:
        led4.on()

# This is the initiation of the GPIO pins using the GPIOZero library
# The pin number arguments are BCM coded and not the actual pin number
led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
button = Button(18)

# The following sets is a faster way of pushing the binary equivalent
# Each set is tied to an LED and if the entered value is in the set
# the LED is illuminated
# This saves me from coding each value in separately
led1set = [8,9,10,11,12,13,14,15]
led2set = [4,5,6,7,12,13,14,15]
led3set = [2,3,6,7,10,11,14,15]
led4set = [1,3,5,7,9,11,13,15]

os.system('clear')
while True:
    clear_LED()
    key = raw_input("Input a number between 1 and 15 or 'Q' to quit.")
    
    if key == "q" or key == "Q":
        break
    try:
        key = int(key)
        if key > 0 and key < 16:
            display_led(key)
        else:
            print("Please enter a number 1 to 15!")
            raw_input("Press ENTER to continue.")
            continue
    except:
        print("A number needs to be pressed.")
        raw_input("Press ENTER to continue.")
        continue
    wait_for_reset()

print("Quitting")


