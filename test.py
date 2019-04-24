import unicornhat as unicorn
import time
import math
import colorsys
from LED import LED




def run():
    unicorn.set_layout(unicorn.PHAT)
    max_width, max_height = unicorn.get_shape()
    leds = []
    for x in range(max_width):
        for y in range(max_height):
            led = LED(position=(x, y), colours=(255, 255, 255))
            leds.append(led)

    while True:
        for count, led in enumerate(leds):
            led.set_colour("red", count * 5)
            led.on()
            unicorn.show()
            time.sleep(0.05)
            led.off()
        # for led in leds:
        #
        #     unicorn.show()
        #     time.sleep(0.05)

if __name__ == "__main__":
    try:
        run()
    finally:
        unicorn.clear()
