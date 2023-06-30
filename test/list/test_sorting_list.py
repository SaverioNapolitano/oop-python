from unittest import TestCase

from exercises.python.list.sorting_list import sorting_list


class Test(TestCase):
    def test_sorting_list(self):
        self.assertEqual(([1, 2, 3], [3, 2, 1]), sorting_list([2, 3, 1]))
        self.assertEqual(([-10, 4, 5], [5, 4, -10]), sorting_list([4, -10, 5]))
