import board
from digitalio import DigitalInOut, Direction,
import adafruit_dotstar
from adafruit_debouncer import Debouncer

pin = digitalio.DigitalInOut(board.D4)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.DOWN
switch = Debouncer(pin)

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.1

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
