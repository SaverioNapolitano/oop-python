from unittest import TestCase

from exercises.python.conditionalstatements.sum_squared import sum_squared


class Test(TestCase):
    def test_sum_squared(self):
        self.assertEqual(338350, sum_squared())
