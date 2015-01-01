#!/usr/bin/env python
import math


class Wheel(object):

    def __init__(self, rim=26, tyre=1.5):
        self.rim = rim
        self.tyre = tyre

    def diameter(self):
        return self.rim + (self.tyre * 2)

    def circumference(self):
        return self.diameter() * math.pi


def wheelify(data):
    return [Wheel(rim=cell[0], tyre=cell[1]) for cell in data]


class Gear(object):

    def __init__(self, chainring=40, cog=18, wheel=None):
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


class Bicycle(object):

    def __init__(self, style='road', size=None, tape_colour=None,
                 front_shock=None, rear_shock=None):
        self.style = style
        self.size = size
        self.tape_colour = tape_colour
        self.front_shock = front_shock
        self.rear_shock = rear_shock

    def spares(self):
        if self.style == 'road':
            return {
                'chain': '10-speed',
                'tyre_size': '23',
                'tape_colour': self.tape_colour
            }
        else:
            return {
                'chain': '10-speed',
                'tyre_size': '2.1',
                'rear_shock': self.rear_shock
            }


if __name__ == '__main__':
    print Gear(
        chainring=52,
        cog=11,
        wheel=Wheel(rim=26, tyre=1.5)).gear_inches()
    print Gear(
        chainring=52,
        cog=11,
        wheel=Wheel(rim=24, tyre=1.25)).gear_inches()

    data = [[622, 20], [622, 23], [559, 30], [559, 40]]
    print RevealingReferences(data).diameters()

    wheel = Wheel(rim=26, tyre=1.5)
    print wheel.circumference()

    print Gear(chainring=52, cog=11, wheel=wheel).gear_inches()
    print Gear(chainring=52, cog=11).ratio()

    bike = Bicycle(
        style='mountain',
        size='S',
        front_shock='Manitou',
        rear_shock='Fox')
    print bike.spares()
