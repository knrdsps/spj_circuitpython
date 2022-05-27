import time
import board
import digitalio

from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.A0)
led.direction = Direction.OUTPUT

led.value = True
time.sleep(0.9)



