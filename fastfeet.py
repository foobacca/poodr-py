#!/usr/bin/env python


class Trip(object):

    def prepare(self, mechanic):
        mechanic.prepare_bicycles(self.bicycles)


class Mechanic(object):

    def prepare_bicycles(self, bicycles):
        for bicycle in bicycles:
            self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        pass
