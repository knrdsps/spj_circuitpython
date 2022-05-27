# Write your code here :-)
import time
import board
import digitalio

from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.A0)
led.direction = Direction.OUTPUT

for i in range(5):

    led.value = True
    time.sleep(0.5)
    led.value= False
    time.sleep(0.5)
