#!/usr/bin/env python


class Gear(object):

    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    def ratio(self):
        return self.chainring / (self.cog * 1.0)


print Gear(52, 11).ratio()
print Gear(30, 27).ratio()
