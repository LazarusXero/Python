from gpiozero import LED
import os

def turn_led_on(bin_x, led_list):
    clear_LED()
    for i in range(0,len(bin_x)):
        if bin_x[i] == '1':
            led_list[i].on()
        else:
            continue
    
def clear_LED():
    led1.off()
    led2.off()
    led3.off()
    led4.off()

def convert_x_to_binary(x):
    bin_x = '{0:04b}'.format(x)
    return(bin_x)

#set variables here
led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
led_list = [led1, led2, led3, led4]

# start program here
clear_LED()
os.system('clear')
x = raw_input("Which number to start with (1-15)?")
x = int(x)

while True:
    bin_x = convert_x_to_binary(x)
    turn_led_on(bin_x, led_list)
    choice = raw_input("Press ENTER to move to next LED, or Q to quit.")
    if choice == 'q' or choice == 'Q':
        break
    else:
        if x <= 14:
            x = x + 1
        else:
            x = 1
            

print('done')

        
    