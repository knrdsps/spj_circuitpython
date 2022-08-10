import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixel_pin = board.A2
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

switchyellow = DigitalInOut(board.D3)
switchyellow.direction = Direction.INPUT
switchyellow.pull = Pull.DOWN

switchred = DigitalInOut(board.D4)
switchred.direction = Direction.INPUT
switchred.pull = Pull.DOWN


yellow_state = False
red_state = False

while True:
    if switchred.value:
        if red_state:
            red_state = False
            pixels.value = False
            pixels.fill(BLACK)
            pixels.show()
        else:
            red_state = True
            pixels.value = True
            pixels.fill(RED)
            pixels.show()

    if switchyellow.value:
        if yellow_state:
            yellow_state = False
            pixels.value = False
            pixels.fill(BLACK)
            pixels.show()
        else:
            yellow_state = True
            pixels.value = True
            pixels.fill(YELLOW)
            pixels.show()

    time.sleep(0.3)

