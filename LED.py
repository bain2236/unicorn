import unicornhat as unicorn
import time
import math
import colorsys

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

        # set unicorn vars
        unicorn.set_layout(unicorn.PHAT)
        self.max_x, self.max_y = unicorn.get_shape()

        # set led vars via funcs
        self.set_colours(colours)
        self.set_brightness(brightness)
        self.set_position(position)
        self.set_rotation(rotation)

        self.stats = ("position:{0},{1}, colour:{2},{3},{4}, brightness {5}".format(
            self.x_position, self.y_position, self.red, self.green, self.blue, self.brightness
        ))
        print("Created LED with {0}".format(self.stats))

    def on(self):
        unicorn.set_pixel(self.x_position, self.y_position, self.red, self.green, self.blue)
        print("Showing LED {0}".format(self.stats))

    def off(self):
        unicorn.set_pixel(self.x_position, self.y_position, 0, 0, 0)
        print("Hiding LED {0}".format(self.stats))

    def set_colours(self, colours):
        if all(0 <= col <= 255 for col in colours):
            self.red = colours[0]
            self.green = colours[1]
            self.blue = colours[2]
        else:
            self.red = 255
            self.green = 255
            self.blue = 255

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

    def set_brightness(self, brightness):

        if 0 <= brightness <= 0.5:

            self.brightness = brightness
            unicorn.brightness = brightness
            print("LED IS SETTING BRIGHGNRESS TO {0}".format(self.brightness))
        else:
            self.brightness = 0.01
            unicorn.brightness = 0.01
            print("LED IS SETTING BRIGHGNRESS TO {0}".format(self.brightness))

    def set_position(self, position):
        if 0 <= position[0] <= self.max_x:
            self.x_position = position[0]
        else:
            self.x_position = 0
        if 0 <= position[1] <= self.max_y:
            self.y_position = position[1]
        else:
            self.y_position = 0

    def set_rotation(self, rotation):
        # do some more things by here to allow you to flip things around
        unicorn.rotation = rotation


    def get_colour(self):
        return self.red, self.green, self.blue

    def get_position(self):
        return self.x_position, self.y_position

    def get_brightness(self):
        return self.brightness

