import unittest

from src.hello_world.hello_world import hello


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!")
