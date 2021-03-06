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


class Parts(object):

    def __init__(self, parts=None):
        self.parts = parts

    def spares(self):
        return [part for part in self.parts if part.needs_spare]


class PartsFactory(object):
    class Part(object):
        def __init__(self, **kwargs):
            self.name = kwargs['name']
            self.description = kwargs['description']
            self.needs_spare = kwargs['needs_spare']

        def __unicode__(self):
            uni = "%s: %s" % (self.name, self.description)
            if self.needs_spare:
                uni += " (needs spare)"
            return uni

    @staticmethod
    def build(config, parts_class=Parts):
        return parts_class([
            PartsFactory._create_part(part_config) for part_config in config
        ])

    @staticmethod
    def _create_part(part_config):
        return PartsFactory.Part(
            name=part_config[0],
            description=part_config[1],
            needs_spare=part_config[2] if len(part_config) > 2 else True
        )


class Bicycle(SchedulableMixin, object):

    def __init__(self, size=None, parts=None):
        self.size = size
        self.parts = parts

    def spares(self):
        return self.parts.spares()

    def lead_days(self):
        return 1


def spares_to_string(spares):
    return '[' + \
        ', '.join([unicode(s) for s in spares]) + \
        ']'


road_config = [
    ['chain', '10-speed'],
    ['tyre_size', '23'],
    ['tape_colour', 'red'],
]
mountain_config = [
    ['chain', '10-speed'],
    ['tyre_size', '2.1'],
    ['front_shock', 'Manitou', False],
    ['rear_shock', 'Fox'],
]
recumbent_config = [
    ['chain', '9-speed'],
    ['tyre_size', '28'],
    ['flag', 'tall and orange'],
]


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

    road_bike = Bicycle(
        size='M',
        parts=PartsFactory.build(road_config))
    print road_bike.size
    print spares_to_string(road_bike.spares())

    mountain_bike = Bicycle(
        size='L',
        parts=PartsFactory.build(mountain_config))
    print mountain_bike.size
    print spares_to_string(mountain_bike.spares())

    recumbent_bike = Bicycle(
        size='L',
        parts=PartsFactory.build(recumbent_config))
    print recumbent_bike.size
    print spares_to_string(recumbent_bike.spares())

    starting = date(2015, 9, 4)
    ending = date(2015, 9, 10)
    b = Bicycle()
    b.is_schedulable(starting, ending)
