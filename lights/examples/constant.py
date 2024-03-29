#from rpi_ws281x import *
from neopixel import *
from led_config import *

#LED_COUNT = 149
LED_COUNT = 38
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
#LED_BRIGHTNESS = 64
LED_INVERT = False
LED_CHANNEL = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for i in range (0, LED_COUNT):
    strip.setPixelColor(i, Color(COLOR_G,COLOR_R,COLOR_B))
    strip.show()
