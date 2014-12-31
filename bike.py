#!/usr/bin/env python


class Gear(object):

    def __init__(self, chainring, cog, rim, tyre):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tyre = tyre

    def ratio(self):
        return self.chainring / (self.cog * 1.0)

    def gear_inches(self):
        return self.ratio() * (self.rim + (self.tyre * 2))


print Gear(52, 11, 26, 1.5).gear_inches()
print Gear(52, 11, 24, 1.25).gear_inches()
