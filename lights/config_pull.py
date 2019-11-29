#from rpi_ws281x import *
from neopixel import *
import time
import configparser

#LED_COUNT = 149
LED_COUNT = 38
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 70
LED_INVERT = False
LED_CHANNEL = 0

STATIC_A = 0
STATIC_B = 0
STATIC_C = 0
STATIC_D = 0
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#strip.begin()

try:
    while True:
        config = configparser.ConfigParser()
        config.read('led_config.ini')

        LED_BRIGHTNESS = int(config['defaults']['LED_BRIGHTNESS'])
        COLOR_R = int(config['defaults']['COLOR_R'])
        COLOR_G = int(config['defaults']['COLOR_G'])
        COLOR_B = int(config['defaults']['COLOR_B'])

        if LED_BRIGHTNESS != STATIC_A or COLOR_R != STATIC_B or COLOR_G != STATIC_C or COLOR_B != STATIC_D:
            STATIC_A = LED_BRIGHTNESS
            STATIC_B = COLOR_R
            STATIC_C = COLOR_G
            STATIC_D = COLOR_B
        
            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
            strip.begin()

            for i in range (0, LED_COUNT):
                strip.setPixelColor(i, Color(COLOR_G,COLOR_R,COLOR_B))
                #strip.setPixelColor(i, Color(255,255,255))
                strip.show()
            time.sleep( 1 )
except KeyboardInterrupt:
    for i in range (0, LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
        strip.show()



