import unicornhat as unicorn
import time
import math
import colorsys
from LED import LED
import numpy
import collections

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.5)
unicorn.rotation(0)
max_width, max_height = unicorn.get_shape()
rand_mat = numpy.random.rand(max_width, max_height)


def run():
    leds = collections.OrderedDict()
    for x in range(max_width):
        for y in range(max_height):
            led = LED(position=[x, y], colours=[255, 255, 255])
            leds[led.get_position()] = led

    test_simple_flow(leds)
    test_hsv(leds)


def test_simple_flow(leds):
    for led in leds.values():
       led.blink()


def test_hsv(leds):
    saturation = 0.0
    while True:
        for hue in numpy.arange(0.0, 1.0, 0.1):
            print("hue")
            for position, led in leds.iteritems():
                led.set_colours(list(colorsys.hsv_to_rgb(hue, 1.0, 1.0)))
                led.blink()
        for saturation in numpy.arange(0.0, 1.0, 0.05):
            print("saturation")
            for position, led in leds.iteritems():
                led.set_colours(list(colorsys.hsv_to_rgb(1.0, saturation, 1.0)))
                led.blink()
        for value in numpy.arange(0.0, 1.0, 0.05):
            print("value")
            for position, led in leds.iteritems():
                led.set_colours(list(colorsys.hsv_to_rgb(1.0, 1.0, value)))
                led.blink()




if __name__ == "__main__":
    try:
        run()
    finally:
        unicorn.off()
