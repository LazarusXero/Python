from gpiozero import Button, LED
from signal import pause

def switch_led():
    current_led.off()
    if index == 3:
        index = 0
    else:
        index += 1
    current_led = led_list[led_index]
    print("new led is {0}".format(led_index))
    current_led.on()
    return

def get_ready():
    print("get ready")

def clear_LED():
    led1.off()
    led2.off()
    led3.off()
    led4.off()

led1 = LED(2)
led2 = LED(3)
led3 = LED(4)
led4 = LED(17)
button = Button(18)

led_list = [led1, led2, led3, led4]
led_index = 0
current_led = led_list[led_index]

clear_LED()

current_led.on()
button.when_pressed = get_ready
button.when_released = switch_led

pause()