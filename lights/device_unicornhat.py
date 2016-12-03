#!/usr/bin/env python3

import lights
import unicornhat as unicorn

# UnicornHat Object
class UnicornHat(lights.DeviceObj):
    def __init__(self, name, rot=0, bri=1):
        width, height = unicorn.get_shape()
        lights.DeviceObj.__init__(self, name, "unicornhat", width, height)

        # Save Parameters
        self.rotation = rot
        self.brightness = bri

        # Initialize Unicorn Hat
        unicorn.set_layout(unicorn.HAT)
        unicorn.rotation(rot)
        unicorn.brightness(bri)

    def set(self, r, g, b, x=0, y=0):
        lights.DeviceObj.set(self, r, g, b, x, y)

        # Set Pixel
        unicorn.set_pixel(x, y, r, g, b)

    def show(self):
        lights.DeviceObj.show(self)

        # Update Display
        unicorn.show()