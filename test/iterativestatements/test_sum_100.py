from unittest import TestCase

from exercises.python.iterativestatements.sum_100 import sum_100


class Test(TestCase):
    def test_sum_100(self):
        self.assertEqual(5050, sum_100())
