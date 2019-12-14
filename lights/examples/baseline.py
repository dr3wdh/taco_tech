#from rpi_ws281x import *
from rpi_ws281x import *
import time

#LED_COUNT = 106
LED_COUNT = 10
#LED_PIN = 18
LED_PIN = 19
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
#LED_CHANNEL = 0
LED_CHANNEL = 1

COLOR_R = 255
COLOR_G = 0
COLOR_B = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

try:
    while True:
        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(COLOR_R,COLOR_G,COLOR_B))
            strip.show()
        time.sleep( 1 )
except KeyboardInterrupt:
    for i in range (0, LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()



