from gpiozero import MCP3008
import os
from time import sleep


pot1 = MCP3008(channel=0, port = 0, device = 0)
pot2 = MCP3008(channel=1, port = 0, device = 0)
pot3 = MCP3008(channel=2, port = 0, device = 0)

try:
    while True:
        x1 = round(pot1.value,2)
        x1sq = round(x1**2,2)
        x1sq2 = round(2 * x1**2,2)
        x1sq05 = round(0.5 * x1**2,2)
        x2 = int(100*round(pot2.value,2))
        x3 = round(pot3.value,2)
        print("|  x  |  x^2  |  2x^2  |  3x^2  |")
        print("| ",x1," | ",x1sq05," | ",x1sq," | ",x1sq2," |")
        print("Value of Potentiometer 2 is, ",x2)
        print("Value of Potentiometer 3 is, ",x3)
        sleep(0.5)
        os.system('clear')
finally:
    raw_input("Done.  ENTER to quit.")

