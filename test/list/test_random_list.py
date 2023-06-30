from unittest import TestCase

from exercises.python.list.random_list import random_list


class Test(TestCase):
    def test_random_list(self):
        self.assertIsNone(random_list())
