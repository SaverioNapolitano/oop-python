import math
from unittest import TestCase

from exercises.python.classes.circle import Circle


class TestCircle(TestCase):
    def test_radius(self):
        self.assertRaises(ValueError, Circle, -1)

    def test_perimeter(self):
        self.assertEqual(6 * math.pi, Circle(3).perimeter())

    def test_area(self):
        self.assertEqual(4*math.pi, Circle(2).area())
