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

    def __init__(self, size=None, chain=None, tyre_size=None):
        self.size = size
        self.chain = chain or self.default_chain()
        self.tyre_size = tyre_size or self.default_tyre_size()

    def default_chain(self):
        return "10-speed"

    def default_tyre_size(self):
        raise NotImplementedError(
            'This %s cannot respond to: default_tyre_size' % self.__class__)


class RoadBike(Bicycle):

    def __init__(self, tape_colour=None, **kwargs):
        self.tape_colour = tape_colour
        super(RoadBike, self).__init__(**kwargs)

    def default_tyre_size(self):
        return '23'

    def spares(self):
        return {
            'chain': '10-speed',
            'tyre_size': '23',
            'tape_colour': self.tape_colour
        }


class MountainBike(Bicycle):
    def __init__(self, front_shock=None, rear_shock=None, **kwargs):
        self.front_shock = front_shock
        self.rear_shock = rear_shock
        super(MountainBike, self).__init__(**kwargs)

    def default_tyre_size(self):
        return '2.1'

    def spares(self):
        spares = super(MountainBike, self).spares()
        spares.update({
            'rear_shock': self.rear_shock
        })
        return spares


class RecumbentBike(Bicycle):

    def default_chain(self):
        return '9-speed'


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

    bike = RoadBike(size='M', tape_colour='red')
    print bike.spares()

    mountain_bike = MountainBike(
        size='S',
        front_shock='Manitou',
        rear_shock='fox')
    print mountain_bike.size
    # print mountain_bike.spares()

    bent = RecumbentBike()
