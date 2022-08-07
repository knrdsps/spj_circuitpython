import board
import time
import adafruit_dotstar
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

rgb = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
rgb.brightness = 0.3

red_button = DigitalInOut(board.D4)
red_button.direction = Direction.INPUT
red_button.pull = Pull.DOWN

yellow_button = DigitalInOut(board.D3)
yellow_button.direction = Direction.INPUT
yellow_button.pull = Pull.DOWN

def check(token):
    if token == "RED":
        return red_button.value
    if token == "YELLOW":
        return yellow_button.value
     
while True:
    if check("RED"):
        print("Red Button has been pressed")
    else:
        print("Red Button has not been pressed")

    if check("YELLOW"):
        print("Yellow Button has been pressed")
    else:
        print("Yellow Button has not been pressed")
    led.value = check("RED")

    if check("YELLOW"):
        rgb[0] = (255, 255, 0)
    else:
        rgb[0] = (0, 0, 0)

    time.sleep(0.2)
