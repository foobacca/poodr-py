#!/usr/bin/env python
import math


class Wheel(object):

    def __init__(self, rim, tyre):
        self.rim = rim
        self.tyre = tyre

    def diameter(self):
        return self.rim + (self.tyre * 2)

    def circumference(self):
        return self.diameter() * math.pi


def wheelify(data):
    return [Wheel(cell[0], cell[1]) for cell in data]


class Gear(object):

    def __init__(self, chainring, cog, wheel=None):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()


class RevealingReferences(object):

    def __init__(self, data):
        self.wheels = wheelify(data)

    def diameters(self):
        return [wheel.diameter() for wheel in self.wheels]


print Gear(52, 11, Wheel(26, 1.5)).gear_inches()
print Gear(52, 11, Wheel(24, 1.25)).gear_inches()

data = [[622, 20], [622, 23], [559, 30], [559, 40]]
print RevealingReferences(data).diameters()

wheel = Wheel(26, 1.5)
print wheel.circumference()

print Gear(52, 11, wheel).gear_inches()
print Gear(52, 11).ratio()
