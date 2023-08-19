import board
import digitalio
import time

led = digitalio.DigitalInOut(board.A0)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D2)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

while True:
    if switch.value:
        led.value = True
    else:
        led.value = False
        time.sleep(0.1)
