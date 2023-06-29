from unittest import TestCase

from exercises.python.conditionalstatements.square import square


class Test(TestCase):
    def test_square(self):
        self.assertEqual(4, square(2))
        self.assertEqual(200, square(300))
