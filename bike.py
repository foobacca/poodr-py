#!/usr/bin/env python


class Wheel(object):

    def __init__(self, rim, tyre):
        self.rim = rim
        self.tyre = tyre

    def diameter(self):
        return self.rim + (self.tyre * 2)


def wheelify(data):
    return [Wheel(cell[0], cell[1]) for cell in data]


class Gear(object):

    def __init__(self, chainring, cog, rim, tyre):
        self.chainring = chainring
        self.cog = cog
        self.wheel = Wheel(rim, tyre)

    def ratio(self):
        return self.chainring / (self.cog * 1.0)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()


class RevealingReferences(object):

    def __init__(self, data):
        self.wheels = wheelify(data)

    def diameters(self):
        return [self.diameter(wheel) for wheel in self.wheels]

    def diameter(self, wheel):
        return wheel.rim + (wheel.tyre * 2)


print Gear(52, 11, 26, 1.5).gear_inches()
print Gear(52, 11, 24, 1.25).gear_inches()

data = [[622, 20], [622, 23], [559, 30], [559, 40]]
print RevealingReferences(data).diameters()
