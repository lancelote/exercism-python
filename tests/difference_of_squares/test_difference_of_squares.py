import unittest

from src.difference_of_squares.difference_of_squares import (
    difference_of_squares,
)
from src.difference_of_squares.difference_of_squares import square_of_sum
from src.difference_of_squares.difference_of_squares import sum_of_squares


class DifferenceOfSquaresTest(unittest.TestCase):
    def test_square_of_sum_1(self):
        self.assertEqual(square_of_sum(1), 1)

    def test_square_of_sum_5(self):
        self.assertEqual(square_of_sum(5), 225)

    def test_square_of_sum_100(self):
        self.assertEqual(square_of_sum(100), 25502500)

    def test_sum_of_squares_1(self):
        self.assertEqual(sum_of_squares(1), 1)

    def test_sum_of_squares_5(self):
        self.assertEqual(sum_of_squares(5), 55)

    def test_sum_of_squares_100(self):
        self.assertEqual(sum_of_squares(100), 338350)

    def test_difference_of_squares_1(self):
        self.assertEqual(difference_of_squares(1), 0)

    def test_difference_of_squares_5(self):
        self.assertEqual(difference_of_squares(5), 170)

    def test_difference_of_squares_100(self):
        self.assertEqual(difference_of_squares(100), 25164150)
