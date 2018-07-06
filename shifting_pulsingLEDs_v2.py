from gpiozero import LED
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

# start program here
clear_LED()
os.system('clear')
x = raw_input("Which number to start with (1-4)?")
x = int(x) - 1

while True:
    turn_led_on(x, led_list)
    choice = raw_input("Press ENTER to move to next LED, or Q to quit.")
    if choice == 'q' or choice == 'Q':
        break
    else:
        if x <= 2:
            x = x + 1
        else:
            x = 0
            
print('done')

        
    