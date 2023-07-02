from unittest import TestCase

from exercises.python.classes.shape import Square


class TestSquare(TestCase):
    def test_length(self):
        self.assertRaises(ValueError, Square, -1)

    def test_area(self):
        self.assertEqual(4, Square(2).area())
