from unittest import TestCase

from exercises.python.comprehension.random_from_list import random_from_list


class Test(TestCase):
    def test_random_from_list(self):
        self.assertIsNone(random_from_list())
