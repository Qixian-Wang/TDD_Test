import unittest
from carpet import CarpetQuote, Room, Carpet

class RoundRoom(object):
    def __init__(self, radius):
        self.radius = radius

    def Room_area(self):
        return self.radius * self.radius

class CarpetQuoteTest(unittest.TestCase):
    def test_quote_no_rounding(self):
        carpet_quote = CarpetQuote(Room(12.55, 10.0), Carpet(10.0, False))
        self.assertEqual(1255, carpet_quote.quote())

    def test_quote_rounding(self):
        carpet_quote = CarpetQuote(Room(12.55, 10.0), Carpet(10.0, True))
        self.assertEqual(1260, carpet_quote.quote())

    def test_quote_round_room(self):
        carpet_quote = CarpetQuote(RoundRoom(10.0), Carpet(10.0, False))
        self.assertEqual(1000, carpet_quote.quote())
