import unittest

from src.resistor_color.resistor_color import color_code
from src.resistor_color.resistor_color import colors


class ResistorColorTest(unittest.TestCase):
    def test_black(self):
        self.assertEqual(color_code("black"), 0)

    def test_white(self):
        self.assertEqual(color_code("white"), 9)

    def test_orange(self):
        self.assertEqual(color_code("orange"), 3)

    def test_colors(self):
        expected = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
        self.assertEqual(colors(), expected)
