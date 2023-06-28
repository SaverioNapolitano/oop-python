from unittest import TestCase

from exercises.python.conditionalstatements.count_odd_even import count_odd_even


class Test(TestCase):
    def test_count_odd_even(self):
        self.assertEqual((1, 2), count_odd_even(1, 2, 3))
        self.assertEqual((2, 1), count_odd_even(1, 2, 4))
