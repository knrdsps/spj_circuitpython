import board
import digitalio
import time

led = digitalio.DigitalInOut(board.A0)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
