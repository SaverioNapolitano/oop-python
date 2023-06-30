from unittest import TestCase

from exercises.python.tuple.sorting_tuples_product import sorting_tuples_product


class Test(TestCase):
    def test_sorting_tuples_product(self):
        self.assertEqual([(2, 3), (4, 2), (1, 10)], sorting_tuples_product([(1, 10), (2, 3), (4, 2)]))
