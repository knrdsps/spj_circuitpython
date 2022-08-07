import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.A2
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

switchblue = DigitalInOut(board.D1)
switchblue.direction = Direction.INPUT
switchblue.pull = Pull.DOWN

switchgreen = DigitalInOut(board.D2)
switchgreen.direction = Direction.INPUT
switchgreen.pull = Pull.DOWN

switchyellow = DigitalInOut(board.D3)
switchyellow.direction = Direction.INPUT
switchyellow.pull = Pull.DOWN

switchred = DigitalInOut(board.D4)
switchred.direction = Direction.INPUT
switchred.pull = Pull.DOWN

while True:
    if switchred.value:
        pixels.fill(RED)
        pixels.show()
        time.sleep(0.5)

    if switchyellow.value:
        pixels.fill(YELLOW)
        pixels.show()
        time.sleep(0.5)

    if switchgreen.value:
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(0.5)

    if switchblue.value:
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(0.5)

    else:
        pixels.value = False
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.01)
