from math import ceil

class Room(object):
    def __init__(self, length, width):
        self._width = width
        self._length = length

    def Room_area(self):
        return self._length * self._width

class Carpet(object):
    def __init__(self, price_per_sqr_mtr, round_up):
        self.price_per_sqr_mtr = price_per_sqr_mtr
        self.round_up = round_up

    def price(self, area):
        if self.round_up:
            area = ceil(area)
        return area * self.price_per_sqr_mtr


class CarpetQuote(object):
    def __init__(self, room, carpet):
        self.carpet = carpet
        self.room = room

    def quote(self):
        area = self.room.Room_area()
        return self.carpet.price(area)



