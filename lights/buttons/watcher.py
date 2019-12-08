#comment
import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

#LED_COUNT = 149
#LED_COUNT = 38
#LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
#LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

STATE_BR = 0
STATE_R = 0
STATE_G = 0
STATE_B = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    red_state = GPIO.input(17)
    white_state = GPIO.input(27)

    if red_state == False:
        print('Red Button Pressed')
        BRIGHT = 10
        RED = 255
        GREEN = 0
        BLUE = 0

        if BRIGHT != STATE_BR or RED != STATE_R or GREEN != STATE_G or BLUE != STATE_B:
            STATE_BR = 10
            STATE_R = 255
            STATE_G = 0
            STATE_B = 0

            LED_COUNT = 38
            LED_PIN = 18

            BRIGHT = STATE_BR
            RED = STATE_R
            GREEN = STATE_G
            BLUE = STATE_B

            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL)
            strip.begin()

            for i in range (0, LED_COUNT):
                strip.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip.show()

            print("lights are red")
            time.sleep(1)

        else:
            STATE_BR = 0
            STATE_R = 0
            STATE_G = 0
            STATE_B = 0

            LED_COUNT = 38
            LED_PIN = 18

            BRIGHT = STATE_BR
            RED = STATE_R
            GREEN = STATE_G
            BLUE = STATE_B

            strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL)
            strip.begin()

            for i in range (0, LED_COUNT):
                strip.setPixelColor(i, Color(RED, GREEN, BLUE))
                strip.show()

            print("lights are off")
            time.sleep(1)

    
    elif white_state == False:
        print('white button pressed')

        LED_COUNT = 38
        LED_PIN = 18
        LED_BRIGHTNESS = 255

        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        for i in range (0, LED_COUNT):
            strip.setPixelColor(i, Color(255,255,255))
            strip.show()

        print("lights are white")
        time.sleep(1)


        time.sleep(0.2)






