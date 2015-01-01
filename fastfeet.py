#!/usr/bin/env python


class Trip(object):

    def __init__(self):
        self.bicycles = []
        self.customers = []
        self.vehicle = None

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)


class Mechanic(object):

    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        pass


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
