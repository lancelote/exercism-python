import unittest

from src.resistor_color_duo.resistor_color_duo import value


class ResistorColorDuoTest(unittest.TestCase):
    def test_brown_and_black(self):
        self.assertEqual(value(["brown", "black"]), 10)

    def test_blue_and_grey(self):
        self.assertEqual(value(["blue", "grey"]), 68)

    def test_yellow_and_violet(self):
        self.assertEqual(value(["yellow", "violet"]), 47)

    def test_orange_and_orange(self):
        self.assertEqual(value(["orange", "orange"]), 33)

    def test_ignore_additional_colors(self):
        self.assertEqual(value(["green", "brown", "orange"]), 51)

    def test_ignore_multiple_colors(self):
        self.assertEqual(value(["green", "brown", "orange", "white"]), 51)
