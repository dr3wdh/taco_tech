# Example Scripts
Here are a few example scripts that should work pretty consitently.  My hello worlds for the WS2812B strip
## Description/FYI
- strips are only supported on certain GPIO pins
- pins relate to channels (something to do with PWM channels, need to do more research)
- pins 12 and 18 can be used with channel 0
- pins 13 and 19 can be used with channel 1

## Requirements
|**Description**|**Command Reference**|
|---------------|---------------------|
|Python, 2 or 3 should work||
|rpi_ws281x python module|`sudo pip install rpi_ws281x`|

## Vars
All are hardcoded at this point (no arguements passed)

|**Variable**|**Description**|
|------------|---------------|
|LED_PIN|The GPIO pin the LED strip is connected to|
|LED_CHANNEL|The PWM channel for the strip (relates to pin, see note in description|
LED_COUNT|Total number of LEDs in strip (106 currently)|

## Example Execution
```bash
sudo python ./baseline.py

```

## Links for reference
  - (outdated) https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/
  - https://github.com/rpi-ws281x/rpi-ws281x-python
## Author Info
@dr3wdh
