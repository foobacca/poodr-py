#!/usr/bin/env python


class Trip(object):

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycles(self.bicycles)
            elif isinstance(preparer, TripCoordinator):
                preparer.buy_food(self.customers)
            elif isinstance(preparer, Driver):
                preparer.fuel_up(self.vehicle)
                preparer.fill_water_tank(self.vehicle)


class Mechanic(object):

    def prepare_bicycles(self, bicycles):
        for bicycle in bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        pass


class TripCoordinator(object):

    def buy_food(self, customers):
        pass


class Driver(object):

    def fuel_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass
