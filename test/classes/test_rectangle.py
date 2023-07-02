from unittest import TestCase

from exercises.python.classes.rectangle import Rectangle


class TestRectangle(TestCase):
    def test_length(self):
        self.assertRaises(ValueError, Rectangle, -1, 4)

    def test_width(self):
        self.assertRaises(ValueError, Rectangle, 1, -2)

    def test_perimeter(self):
        self.assertEqual(10, Rectangle(2, 3).perimeter())

    def test_area(self):
        self.assertEqual(6, Rectangle(2, 3).area())
