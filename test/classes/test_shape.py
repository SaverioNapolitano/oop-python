from unittest import TestCase

from exercises.python.classes.shape import Shape


class TestShape(TestCase):
    def test_area(self):
        self.assertEqual(0, Shape().area())

