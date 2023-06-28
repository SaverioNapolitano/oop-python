from unittest import TestCase

from exercises.python.iterativestatements.divisible_by_7 import divisible_by_7


class Test(TestCase):
    def test_divisible_by_7(self):
        self.assertIsNone(divisible_by_7())
