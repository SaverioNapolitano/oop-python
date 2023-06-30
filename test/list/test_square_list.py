from unittest import TestCase

from exercises.python.list.square_list import square_list


class Test(TestCase):
    def test_square_list(self):
        self.assertEqual([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],
                         square_list())
