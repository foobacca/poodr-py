#!/usr/bin/env python
from datetime import date

from bike import SchedulableMixin


class Trip(object):

    def __init__(self):
        self.bicycles = []
        self.customers = []
        self.vehicle = None

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)


class Vehicle(SchedulableMixin, object):
    def lead_days(self):
        return 3


class Mechanic(SchedulableMixin, object):

    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        pass

    def lead_days(self):
        return 4


class TripCoordinator(object):

    def prepare_trip(self, trip):
        self.buy_food(trip.customers)

    def buy_food(self, customers):
        pass


class Driver(object):

    def prepare_trip(self, trip):
        self.fuel_up(trip.vehicle)
        self.fill_water_tank(trip.vehicle)

    def fuel_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass


if __name__ == '__main__':
    starting = date(2015, 9, 4)
    ending = date(2015, 9, 10)

    v = Vehicle()
    v.is_schedulable(starting, ending)

    m = Mechanic()
    m.is_schedulable(starting, ending)
