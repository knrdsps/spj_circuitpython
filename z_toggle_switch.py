import board
import time
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.1

switchyellow = DigitalInOut(board.D3)
switchyellow.direction = Direction.INPUT
switchyellow.pull = Pull.DOWN

button_state = False

while True:
    if switchyellow.value:
        if button_state:
            button_state = False
            led.value = False
            led[0] = (0, 0, 0)
        else:
            button_state = True
            led.value = True
            led[0] = (255, 255, 0)
        
    time.sleep(0.3)
