import unicornhat as unicorn
import time
import math
import colorsys
import numpy

class LED:
    def __init__(self, position,  brightness=0.5, colours=(255, 255, 255), rotation=0):
        # set led vars
        self.red = None
        self.green = None
        self.blue = None
        self.brightness = None
        self.x_position = None
        self.y_position = None
        self.rotation = None
        self.stats = None

        # set unicorn vars
        unicorn.set_layout(unicorn.PHAT)
        self.max_x, self.max_y = unicorn.get_shape()

        # set led vars via funcs
        self.set_colours(colours)
        self.set_brightness(brightness)
        self.set_position(position)
        self.set_rotation(rotation)
        self.set_stats()
        print("Created LED with {0}".format(self.stats))

    def on(self):
        print("Showing LED {0}".format(self.stats))
        unicorn.set_pixel(self.x_position, self.y_position, self.red, self.green, self.blue)
        unicorn.show()

    def off(self):
        print("Hiding LED {0}".format(self.stats))
        unicorn.set_pixel(self.x_position, self.y_position, 0, 0, 0)
        unicorn.show()

    def set_colours(self, colours):
        if all(type(c) == float or type(c) == numpy.float64 for c in colours):
            # floating point values come from hsv to rgb's

            colours[0] = int(colours[0] * 255.0)
            colours[1] = int(colours[1] * 255.0)
            colours[2] = int(colours[2] * 255.0)
        if any(0 <= col <= 255 for col in colours):
            self.red = colours[0]
            self.green = colours[1]
            self.blue = colours[2]
        else:
            print("setting colour to white due to input colours being {0}".format(colours))
            self.red = 255
            self.green = 255
            self.blue = 255
        self.set_stats()

    def set_colour(self, colour, intensity):
        if colour == "red":
            if 0 <= intensity <= 255:
                self.red = intensity
                print("setting red to {0}".format(intensity))
            else:
                print("setting red to {0}".format(intensity))
                self.red = 0
        if colour == "green":
            if 0 <= intensity <= 255:
                self.green = intensity
            else:
                self.green = 0
        if colour == "blue":
            if 0 <= intensity <= 255:
                self.blue = intensity
            else:
                self.blue = 0
        self.set_stats()

    def set_brightness(self, brightness):
        if 0 <= brightness <= 0.5:
            self.brightness = brightness
            unicorn.brightness = brightness
        else:
            self.brightness = 0.01
            unicorn.brightness = 0.01
        self.set_stats()

    def set_position(self, position):
        if 0 <= position[0] <= self.max_x:
            self.x_position = position[0]
        else:
            self.x_position = 0
        if 0 <= position[1] <= self.max_y:
            self.y_position = position[1]
        else:
            self.y_position = 0
        self.set_stats()

    def set_rotation(self, rotation):
        # do some more things by here to allow you to flip things around
        unicorn.rotation = rotation


    def get_colour(self):
        return self.red, self.green, self.blue

    def get_position(self):
        return self.x_position, self.y_position

    def get_brightness(self):
        return self.brightness

    def get_stats(self):
        return self.stats

    def set_stats(self):
        self.stats = ("position:{0},{1}, colour:{2},{3},{4}, brightness {5}".format(
            self.x_position, self.y_position, self.red, self.green, self.blue, self.brightness
        ))

    def blink(self):
        self.on()
        time.sleep(0.05)
        self.off()
