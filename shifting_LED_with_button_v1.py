from gpiozero import LED, Button
import os

def turn_led_on(x, led_list):
    clear_LED()
    led_list[x].on()
    
def clear_LED():
    led1.off()
    led2.off()
    led3.off()
    led4.off()


#set variables here
led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led_list = [led1, led2, led3, led4]
red_button = Button(18)
blue_button = Button(23)

# start program here
clear_LED()
os.system('clear')
x = raw_input("Which number to start with (1-4)?")
x = int(x) - 1

while True:
    turn_led_on(x, led_list)   # turns on the xth led
    print("Press red button and then blue button to move to next LED.")
    red_button.wait_for_press()    # wait for button to be pressed
    red_button.wait_for_release()
    blue_button.wait_for_press()
    blue_button.wait_for_release()
    if x <= 2:                 # check led that was lit
        x = x + 1              # if led was less than or equal to 3, then go to next
    else:
        x = 0                  # if led was at 4, then reset to 1
            
print('done')

        
    