#comment
import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

## constant LED vars that won't change based on buttons
## (pin and count aren't constant because of reading light future feature)
#LED_COUNT = 149
#LED_COUNT = 107
#LED_PIN = 18
LED_PIN_A = 18
LED_PIN_B = 19
LED_FREQ_HZ = 800000
LED_DMA = 10
#LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_CHANNEL_A = 0
LED_CHANNEL_B = 1

## instantiate state save vars (used for turning off on double press)
STATE_BR = 0
STATE_R = 0
STATE_G = 0
STATE_B = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#-------------------------------------------------
# start watching for buttons
#-------------------------------------------------
while True:
    bright_red_state = GPIO.input(22)
    dim_red_state = GPIO.input(17)
    bright_white_state = GPIO.input(27)
    dim_white_state = GPIO.input(23)

    #-------------------------------------------------
    # dim red button pressed
    #-------------------------------------------------
    if dim_red_state == False:
        ## set request vars to equal dim red
        print('Dim Red Button Pressed')
        BRIGHT = 10
        RED = 255
        GREEN = 0
        BLUE = 0

        #-------------------------------------------------
        # if lights aren't already set to dim red, set them
        #-------------------------------------------------
        if BRIGHT != STATE_BR or RED != STATE_R or GREEN != STATE_G or BLUE != STATE_B:
            ## save state vars that equal dim red
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## full length vars
            LED_COUNT = 106

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are dim red")
            time.sleep(.5) ## play nice with human fingers

        #-------------------------------------------------
        # if lights are already set to dim red, turn off
        #-------------------------------------------------
        else:
            ## set request vars to equal off
            BRIGHT = 0
            RED = 0
            GREEN = 0
            BLUE = 0

            ## full length vars
            LED_COUNT = 106

            ## save state vars that equal off
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are off")
            time.sleep(.5) ## play nice with human fingers

    elif bright_red_state == False:
        ## set request vars to equal bright red
        print('bright red button pressed')
        BRIGHT = 255
        RED = 255
        GREEN = 0
        BLUE = 0

        #-------------------------------------------------
        # if lights aren't already set to bright red, set them
        #-------------------------------------------------
        if BRIGHT != STATE_BR or RED != STATE_R or GREEN != STATE_G or BLUE != STATE_B:
            ## save state vars that equal bright red
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## full length vars
            LED_COUNT = 106

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are bright red")
            time.sleep(.5) ## play nice with human fingers

        #-------------------------------------------------
        # if lights are already set to bright red, turn off
        #-------------------------------------------------
        else:
            ## set request vars to equal off
            BRIGHT = 0
            RED = 0
            GREEN = 0
            BLUE = 0

            ## full length vars
            LED_COUNT = 106

            ## save state vars that equal off
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are off")
            time.sleep(.5) ## play nice with human fingers

    elif dim_white_state == False:
        ## set request vars to equal dim white
        print('dim white button pressed')
        BRIGHT = 10
        RED = 255
        GREEN = 255
        BLUE = 255

        #-------------------------------------------------
        # if lights aren't already set to dim white, set them
        #-------------------------------------------------
        if BRIGHT != STATE_BR or RED != STATE_R or GREEN != STATE_G or BLUE != STATE_B:
            ## save state vars that equal dim white
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## full length vars
            LED_COUNT = 106

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are dim white")
            time.sleep(.5) ## play nice with human fingers

        #-------------------------------------------------
        # if lights are already set to dim white, turn off
        #-------------------------------------------------
        else:
            ## set request vars to equal off
            BRIGHT = 0
            RED = 0
            GREEN = 0
            BLUE = 0

            ## full length vars
            LED_COUNT = 106

            ## save state vars that equal off
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are off")
            time.sleep(.5) ## play nice with human fingers

    elif bright_white_state == False:
        print('bright white button pressed')
        BRIGHT = 255
        RED = 255
        GREEN = 255
        BLUE = 255

        #-------------------------------------------------
        # if lights aren't already set to bright white, set them
        #-------------------------------------------------
        if BRIGHT != STATE_BR or RED != STATE_R or GREEN != STATE_G or BLUE != STATE_B:
            ## save state vars that equal bright white
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## full length vars
            LED_COUNT = 106

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are bright white")
            time.sleep(.5) ## play nice with human fingers

        #-------------------------------------------------
        # if lights are already set to bright white, turn off
        #-------------------------------------------------
        else:
            ## set request vars to equal off
            BRIGHT = 0
            RED = 0
            GREEN = 0
            BLUE = 0

            ## full length vars
            LED_COUNT = 106

            ## save state vars that equal off
            STATE_BR = BRIGHT
            STATE_R = RED
            STATE_G = GREEN
            STATE_B = BLUE

            ## activate lights
            strip_a = Adafruit_NeoPixel(LED_COUNT, LED_PIN_A, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_A)
            strip_a.begin()

            for i in range (0, LED_COUNT):
                strip_a.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_a.show()

            strip_b = Adafruit_NeoPixel(LED_COUNT, LED_PIN_B, LED_FREQ_HZ, LED_DMA, LED_INVERT, BRIGHT, LED_CHANNEL_B)
            strip_b.begin()

            for i in range (0, LED_COUNT):
                strip_b.setPixelColor(i, Color(RED,GREEN,BLUE))
                strip_b.show()

            print("lights are off")
            time.sleep(.5) ## play nice with human fingers

        time.sleep(0.2) ## don't crash pi with infinite loop
