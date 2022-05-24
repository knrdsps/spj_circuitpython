# Write your code here :-)
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
import time
import board

# For Trinket M0, Gemma M0, ItsyBitsy M0 Express, and ItsyBitsy M4 Express
import adafruit_dotstar
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

# import neopixel
# led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

while True:
    led[0] = (255, 0, 0)
    time.sleep(0.9)
    led[0] = (0, 255, 0)
    time.sleep(0.9)
    led[0] = (0, 0, 255)
    time.sleep(0.9)
