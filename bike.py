#!/usr/bin/env python
from datetime import date, timedelta
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


class Schedule(object):

    def is_scheduled(self, schedulable, start_date, end_date):
        print "This %s is not scheduled\nbetween %s and %s" % \
            (schedulable.__class__, start_date, end_date)


class SchedulableMixin(object):
    @property
    def schedule(self):
        if not hasattr(self, '_schedule'):
            self._schedule = Schedule()
        return self._schedule

    def is_schedulable(self, start_date, end_date):
        return not self.is_scheduled(
            start_date - timedelta(days=self.lead_days()), end_date)

    def is_scheduled(self, start_date, end_date):
        return self.schedule.is_scheduled(self, start_date, end_date)

    def lead_days(self):
        return 0


class Bicycle(SchedulableMixin, object):

    def __init__(self, size=None, chain=None, tyre_size=None, **kwargs):
        self.size = size
        self.chain = chain or self.default_chain()
        self.tyre_size = tyre_size or self.default_tyre_size()
        self.post_init(**kwargs)

    def post_init(self, **kwargs):
        pass

    def default_chain(self):
        return "10-speed"

    def default_tyre_size(self):
        raise NotImplementedError(
            'This %s cannot respond to: default_tyre_size' % self.__class__)

    def spares(self):
        spares = {
            'chain': self.chain,
            'tyre_size': self.tyre_size,
        }
        spares.update(self.local_spares())
        return spares

    def local_spares(self):
        return {}

    def lead_days(self):
        return 1


class RoadBike(Bicycle):

    def post_init(self, **kwargs):
        self.tape_colour = kwargs.get('tape_colour')

    def default_tyre_size(self):
        return '23'

    def local_spares(self):
        return {'tape_colour': self.tape_colour}


class MountainBike(Bicycle):
    def post_init(self, **kwargs):
        self.front_shock = kwargs.get('front_shock')
        self.rear_shock = kwargs.get('rear_shock')

    def default_tyre_size(self):
        return '2.1'

    def local_spares(self):
        return {'rear_shock': self.rear_shock}


class RecumbentBike(Bicycle):
    def post_init(self, **kwargs):
        self.flag = kwargs.get('flag')

    def default_chain(self):
        return '9-speed'

    def default_tyre_size(self):
        return '28'

    def local_spares(self):
        return {'flag': self.flag}


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
    print mountain_bike.spares()

    bent = RecumbentBike(flag="tall and orange")
    print bent.spares()

    starting = date(2015, 9, 4)
    ending = date(2015, 9, 10)
    b = RoadBike()
    b.is_schedulable(starting, ending)
