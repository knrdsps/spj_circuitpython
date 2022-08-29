import board
import adafruit_dotstar
from digitalio import DigitalInOut, Direction, Pull
from adafruit_debouncer import Debouncer

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.1

pin = DigitalInOut(board.D4)
pin.direction = Direction.INPUT
pin.pull = Pull.DOWN
switch = Debouncer(pin)

RED = (255, 0, 0)
GREEN = (0, 255, 0)

while True:
    switch.update()
    if switch.fell:
        led.value = True
        led[0] = (GREEN)
    if switch.rose:
        led.value = True
        led[0] = (RED)
