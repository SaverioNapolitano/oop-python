from unittest import TestCase

from exercises.python.list.print_half import print_half


class Test(TestCase):
    def test_print_half(self):
        self.assertIsNone(print_half([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
