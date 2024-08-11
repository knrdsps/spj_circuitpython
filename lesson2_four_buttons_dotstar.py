import board
import time
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.1

switchyellow = DigitalInOut(board.D1)
switchyellow.direction = Direction.INPUT
switchyellow.pull = Pull.DOWN

switchorange = DigitalInOut(board.D2)
switchorange.direction = Direction.INPUT
switchorange.pull = Pull.DOWN

switchblue = DigitalInOut(board.D3)
switchblue.direction = Direction.INPUT
switchblue.pull = Pull.DOWN

switchgreen = DigitalInOut(board.D4)
switchgreen.direction = Direction.INPUT
switchgreen.pull = Pull.DOWN

while True:
    if switchyellow.value:
        led.value = True
        led[0] = (255, 0, 0)
    elif switchorange.value:
        led.value = True
        led[0] = (0, 255, 0)
    elif switchblue.value:
        led.value = True
        led[0] = (0, 0, 255)
    elif switchgreen.value:
        led.value = True
        led[0] = (255, 255, 255)
    else:
        led.value = False
        led[0] = (0, 0, 0)
        time.sleep(0.01)  # debounce delay
