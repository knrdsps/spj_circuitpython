import time
import board
import adafruit_dotstar

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

led.brightness = 0.1

while True:
    led[0] = (255, 0, 0)
    time.sleep(0.9)
    led[0] = (0, 255, 0)
    time.sleep(0.9)
    led[0] = (0, 0, 255)
    time.sleep(0.9)
